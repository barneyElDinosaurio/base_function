# Copyright (c) 2013-2015, NVIDIA CORPORATION.  All Rights Reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

# -------------------------------------------------------------------------------
# Name    : OTAtest
# Purpose : OTA stress test accross all platforms
# Author  : shyamk@nvidia.com
# Version : 1.0
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
import sys
import time
import datetime
import traceback
import subprocess
import threading
import platform
import re
import glob
from threading import *
from uiautomator import Device

__doc__ = """ This module is used to perform OTA stress  """

if (os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utility")))):
    BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.path.join(BASE_PATH, "common"))
else:
    BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sys.path.insert(0, os.path.join(BASE_PATH, "tests", "common"))

from base_common import *
from utility.file import *
from utility.result import *
from utility.device_utils import DeviceUtils
from utility.net_utils import FTPUtils, HTTPUtils
from utility.pm342_utils import PM342, RELAY
from utility.build_utils.device_build_utils import AndroidBuildUtils

GARBAGE_CHARACTER_LIST = ("\x00")
#output a [] garbage

class UartLogging(threading.Thread):
    def __init__(self, container, device="/dev/ttyUSB2", baudrate=115200, logfile=None, cond_var=None, flash_log=False):
        """
        Initialize the parameters such as
        device  = Which port to select for communication baudrate
        logfile = log file where logs needs to be saved is specified none logs will be dumped to STDOUT
        bailout time, logcat file name etc
        """
        import serial

        threading.Thread.__init__(self, name="UART Logging")
        self.setDaemon(True)
        self._devd = serial.Serial(device, baudrate, timeout=2, writeTimeout=20)
        self._uart_log_file = logfile
        self.set_log_file()
        self._command = None
        self._cond_var = cond_var
        self._flash_log = flash_log
        self._send_command = Condition()
        self.send_command_string = "S_o_M_e_T_h_I_n_G_Unique"
        self.common = container
        self._cond = Condition()
        self.re_partition_updation = None
        self.re_kernel_timestamp = None
        self.re_tegraboot_version = None
        self.re_bootloader_version = None
        self.uart_issue = False
        if (self._devd == None):
            raise IOError()
        self._end_event = threading.Event()

    def set_log_file(self):
        """
        set the file descriptor where u want to dump the logs
        it may be either STDOUT or logfile.
        """
        if self._uart_log_file == None:
            self._logd = sys.stdout
        else:
            self._logd = open(self._uart_log_file, "a+")
        if (self._logd == None):
            raise IOError()

    def run(self):
        """
        deamon which runs continuesly which checks for test status.
        if expected string set by method set_expected_string() occurs
        then marks the test as pass .
        """
        self.compile_parser_regexes()
        line = ""
        characters = []
        while (False == self._end_event.isSet()):
            try:
                line = self._devd.readline()
                if (line != ""):
                    self.analysis_logs(line)
                    self._logd.write(line)
                    self._logd.flush()
            except Exception as e:
                self.handle_exception(e)

    def handle_exception(self, e):
        if ((e.__class__.__name__ == "OSError" and re.search('resource\s*temporarily\s*unavailable', e.strerror,
                                                             re.I)) or e.__class__.__name__ == "SerialException"):
            if (not self.uart_issue):
                self.uart_issue = True
                self.log_exception_traceback(
                    "*** Serial Port seems to be compromised . UART logs might miss out prints... ***")
            return
        else:
            self.log_exception_traceback()
        raise e

    def log_exception_traceback(self, msg=None):
        if (getattr(self, "common", False) and getattr(self.common, "log", False)):
            if (msg):
                self.common.log.warning(msg)
            self.common.log.warning(traceback.format_exc())
        else:
            traceback.print_exc()

    def clear_garbage(self, line):
        global GARBAGE_CHARACTER_LIST
        line_original = line
        try:
            for character in GARBAGE_CHARACTER_LIST:
                if ( character in line):
                    line = line.replace(character, '')
            return line
        except Exception:
            self.common.log.info("Exception occured is:\n%s" % (traceback.format_exc()))
            return line_original

    def compile_parser_regexes(self):
        self.re_partition_updation = re.compile("\s*end\s*updating\s*(\w*)|\s*update partition\s*(.*)\s*success",
                                                re.IGNORECASE)
        self.re_kernel_timestamp = re.compile("\\[[\s*\d+\.+]+\].*Linux version .* SMP PREEMPT\s*(.*)", re.IGNORECASE)
        self.re_tegraboot_version = re.compile(".*\[TegraBoot\]\s*\(version(.*)\)", re.IGNORECASE)
        self.re_bootloader_version = re.compile(".*\[bootloader\]\s*\(version(.*)\)|.*cboot\s*version\:*\s*(.*)",
                                                re.IGNORECASE)

    def analysis_logs(self, line):
        if (self.re_partition_updation.search(line)):
            search_obj = self.re_partition_updation.search(line)
            if (search_obj):
                self.common.log.info("[REGEX MATCH] Partition update")
                partition = ""
                if (search_obj.group(1) == None):
                    partition = search_obj.group(2).strip()
                else:
                    partition = search_obj.group(1).strip()
                self.common.log.debug("[REGEX MATCH] Partition : [%s]" % (partition))
                if (self.common.ota_initiated):
                    self.common.ota_started = True
                    if (partition in self.common.ota_complete_prints_copy):
                        self.common.ota_complete_prints_copy.remove(partition)
                        self.common.log.info(line)
                        if (len(self.common.ota_complete_prints_copy) == 0):
                            self.common.log.info("***OTA flashing done***")
                            self.common.ota_done = True
                    else:
                        self.common.log.info(
                            "Partition [%s] not mentioned in the input xml file but seems like %s got updated" % (
                            partition, partition))
            else:
                self.common.log.info("Regex failed to find a Valid partition in  String [%s]" % (line))

        elif (self.re_kernel_timestamp.search(line)):
            search_obj = self.re_kernel_timestamp.search(line)
            if (search_obj):
                self.common.log.info("[REGEX MATCH] Kernel Timestamp")
                if (self.common.ota_done):
                    if (not self.common.post_ota_kernal_timestamp):
                        self.common.post_ota_kernal_timestamp = search_obj.group(1).strip()
                        self.common.log.info(
                            "Post OTA Kernel Timestamp : [%s]" % (self.common.post_ota_kernal_timestamp))
                        self.common.result_dict['Post OTA Kernel timestamp'] = self.common.post_ota_kernal_timestamp
                else:
                    if (self.common.base_build_flashed and not self.common.pre_ota_kernal_timestamp):
                        self.common.pre_ota_kernal_timestamp = search_obj.group(1).strip()
                        self.common.log.info("Pre OTA Kernel Timestamp : [%s]" % (self.common.pre_ota_kernal_timestamp))
                        self.common.result_dict['Pre OTA Kernel timestamp'] = self.common.pre_ota_kernal_timestamp

        elif (self.re_tegraboot_version.search(line)):
            search_obj = self.re_tegraboot_version.search(line)
            if (search_obj):
                self.common.log.info("[REGEX MATCH] Tegraboot Version")
                if (self.common.ota_done):
                    if (not self.common.post_ota_tegra_boot_version):
                        self.common.post_ota_tegra_boot_version = search_obj.group(1).strip()
                        self.common.log.info(
                            "Post OTA TegraBoot Version : [%s]" % (self.common.post_ota_tegra_boot_version))
                        self.common.result_dict['Post OTA Tegraboot Version'] = self.common.post_ota_tegra_boot_version
                else:
                    if (self.common.base_build_flashed and not self.common.pre_ota_tegra_boot_version):
                        self.common.pre_ota_tegra_boot_version = search_obj.group(1).strip()
                        self.common.log.info(
                            "Pre OTA TegraBoot Version : [%s]" % (self.common.pre_ota_tegra_boot_version))
                        self.common.result_dict['Pre OTA Tegraboot Version'] = self.common.pre_ota_tegra_boot_version

        elif (self.re_bootloader_version.search(line)):
            search_obj = self.re_bootloader_version.search(line)
            if (search_obj):
                self.common.log.info("[REGEX MATCH] Bootloader version")
                bl = ""
                if (search_obj.group(1) == None):
                    bl = search_obj.group(2).strip()
                else:
                    bl = search_obj.group(1).strip()
                if (self.common.ota_done):
                    if (not self.common.post_ota_bootloader_version):
                        self.common.post_ota_bootloader_version = bl
                        self.common.log.info(
                            "Post OTA Bootloader Version : [%s]" % (self.common.post_ota_bootloader_version))
                        self.common.result_dict['Post OTA Bootloader Version'] = self.common.post_ota_bootloader_version
                else:
                    if (self.common.base_build_flashed and not self.common.pre_ota_bootloader_version):
                        self.common.pre_ota_bootloader_version = bl
                        self.common.log.info(
                            "Pre OTA Bootloader Version : [%s]" % (self.common.pre_ota_bootloader_version))
                        self.common.result_dict['Pre OTA Bootloader Version'] = self.common.pre_ota_bootloader_version

        elif re.search(".*power-up\s*reason\:\s*(pmu rtc alarm|usb hotplug)", line, re.I):
            self.common.log.warn("Found : %s" % (line))
            self.common.log.info(
                "This is expected. Will reboot the device and continue test from the current iteration")
            self.common.reboot_required = True

        elif re.search(self.send_command_string, line, re.I):
            self.common.log.info("send command complete %s" % (line))
            self.test_status = True
            self._send_command.acquire()  #acquire the lock
            self._send_command.notifyAll()
            self._send_command.release()

        if (self.common.args.uart_stdout):
            print(line)

    def release_cond_var(self):
        """
        release blocking thread
        """
        self._cond_var.acquire()  #acquire the lock
        self._cond_var.notifyAll()
        self._cond_var.release()

    def send_command(self, command, expected=None, time_out=10):
        """
        Run the user commands in shell.
        it does su to get super user access before running the command.
        """
        if (expected != None):
            self.send_command_string = expected
        else:
            self.send_command_string = "S_o_M_e_T_h_I_n_G_Unique"
        self._command = command
        self.test_status = False
        self._send_command.acquire()
        self.common.log.info("running command " + self._command)
        for character in self._command:
            self._devd.write(character)
            self._devd.flush()
            time.sleep(0.001)
        self._devd.write('\n')
        self._send_command.wait(time_out)
        self._send_command.release()
        self.send_command_string = "S_o_M_e_T_h_I_n_G_Unique"
        return self.test_status

    def get_test_status(self):
        """
        Returns the test status True is test passes , False for failure.
        """
        return self.test_status

    def stop(self):
        """
        stops the tests
        """
        self._end_event.set()
        self.join()
        self._devd.close()
        if self._logd.fileno() != sys.stdout.fileno():
            self._logd.close()


class OTAtest(Common, BaseTestInterface):
    def __init__(self, bailout=120, uart_logfile=None, logcat_file="logcat_otastress.log", standalone=False):
        """
        Initialize the stresscount, bailout time, logcat file name etc
        """
        super(OTAtest, self).__init__()
        self.bailout = int(bailout)
        self.kernel_uart_log = uart_logfile
        self.logcat_file = logcat_file
        self.standalone = standalone
        self.pre_ota_apps_versions = {}
        self.post_ota_apps_versions = {}
        self.ota_done = False
        self._cond = Condition()
        self.uart_started = False
        self.result_csv_filename = "results.csv"
        self.market_apps_result_csv_filename = "market_apps_results.csv"
        self.result_list = []
        self.install_3rdparty_app_list = []
        self.ota_partition_list = {}
        self.orig_partition_list = {}
        self.pre_ota_kernal_timestamp = None
        self.post_ota_kernal_timestamp = None
        self.pre_ota_tegra_boot_version = None
        self.post_ota_tegra_boot_version = None
        self.pre_ota_bootloader_version = None
        self.post_ota_bootloader_version = None
        self.base_build_flashed = False
        self.ota_app_version = 2
        self.reboot_required = False
        self.ota_app_package_name = "com.nvidia.ota"
        self.tegraflash_command = None
        self.otadiff_script_location = ""
        self.passedIterations = 0
        self.failedIterations = 0

        self.ota_app_ui_elements = {
            "1":
                {
                    "activity_name": "com.nvidia.ota/com.nvidia.ota.TegraOTAActivity",
                    "launcher_activity_action": " com.nvidia.ota.SYSTEM_UPDATE_SETTINGS",
                    "text_branch": "Choose branch",
                    "resourceid_download": "com.nvidia.ota:id/download_dlg_pct_txt",
                    "text_download_finished": "Download finished",
                    "text_flash": "Flash",
                    "tot_index": 2
                },
            "2":
                {
                    "activity_name": "com.nvidia.ota/.ui.InternalOtaActivity",
                    "launcher_activity_action": " com.nvidia.ota.SYSTEM_UPDATE_SETTINGS",
                    "text_branch": "Branch",
                    "resourceid_download": "com.nvidia.ota:id/download_dlg_progress",
                    "text_download_finished": "Downloaded and verified",
                    "text_flash": "Flash",
                    "tot_index": 4
                },
        }

    def init_ota_test(self):
        """
        Initializes OTA test
        """
        self.set_utlities_path(os.path.join(BASE_PATH, "utility"))
        self.setup_dir()
        self.init_common()
        self.setup_working_dir()
        self.log_test_details()
        if (not self.args.build_utils_path):
            self.set_build_utils_path(os.path.abspath(os.path.join(BASE_PATH, "utility", "build_utils")))
        if (self.args.check_ota_partitions or self.args.ota_diff):
            self.init_ota_partition_check()
        self.test_setup()

    def init_ota_partition_check(self):
        """
        Initializes OTA partition check
        """
        self.log.info("Initializing OTA partition check configurations...\n\n")
        self.change_working_dir(self.ota_build_dir)
        ota_build_local_path = self.download_file(self.args.ota_build_path, self.ota_build_dir)
        if (not ota_build_local_path):
            raise Exception("Failed to download the OTA build. Skipping test")
        if (not self.extract_build(ota_build_local_path)):
            raise Exception("Failed to extract the OTA build...")
        if self.args.ota_diff:
            if not self.copy_ota_diff_files():
                raise Exception("Could not copy OTA diff script files")
        else:
            partitions = self.args.check_ota_partitions.split("|")
            for partition in partitions:
                self.orig_partition_list[partition] = None
                self.ota_partition_list[partition] = None

        self.flash_and_pull_partitions()

    def copy_ota_diff_files(self):
        self.log.info("Copying OTA_diff files")
        otadiff_script_name = "otadiff_core.py"
        if self.otadiff_script_location == "":
            self.log_message("INFO", "Checking if %s exists in the build" % otadiff_script_name)
            otadiff_script_path = FileHelper.find(otadiff_script_name, [self.working_dir], True)
            if (otadiff_script_path):
                self.log.info("%s found in build" % otadiff_script_name)
                self.otadiff_script_location = os.path.join(os.path.dirname(otadiff_script_path))
            else:
                self.log.info("%s not found in build. Taking from perforce" % otadiff_script_name)
                self.otadiff_script_location = os.path.join(self.utils_path, "otadiff_utilities")
        if not self.execute_cmd("sudo cp -rf %s/* ./" % self.otadiff_script_location, timeout=20):
            return True
        else:
            return False

    def log_test_details(self):
        """
        prints out the test details for user visiblity
        """
        self.log.info("\t\t===== TEST %s STARTED =====\t\t\n\n" % (self.args.test_name))
        self.log.info("Log Location                               : %s" % (self.test_log_dir))
        self.log.info("Stress count                               : %s" % (self.args.stresscount))
        self.log.info("Base Build                                 : %s" % (self.args.oldbuild))
        self.log.info("OTA Build                                  : %s" % (self.args.ota_build_path))
        self.log.info("User Production Build [no adb]             : %s" % (self.args.user_build))
        self.log.info("OTA on encrypted device                    : %s" % (self.args.encrypt_device))
        self.log.info("Branch                                     : %s" % (self.args.branch))
        self.log.info("Board                                      : %s" % (self.args.board))
        self.log.info("OTA Build String                           : %s" % (self.args.ota_build_string))
        self.log.info("Incremental OTA                            : %s" % (self.args.incremental))
        self.log.info("Use Fastboot                               : %s" % (self.args.use_fastboot))
        if (not self.args.use_fastboot):
            self.log.info("TNSPEC                                     : %s" % (self.args.tnspec))
        else:
            self.log.info("Fast boot partition list :                 : %s" % (self.args.fb_partitions.split("|")))
        self.log.info("Board Variant                              : %s" % (self.args.board_type))
        self.log.info("SKU                                        : %s" % (self.args.sku))
        self.log.info("OTA update partition list                  : %s" % (self.args.ota_update_partitions))
        self.log.info("OTA update partition image check list      : %s" % (self.args.check_ota_partitions))
        self.log.info("Use otadiff_core.py                        : %s" % str(self.args.ota_diff))
        self.log.info("UART port                                  : %s" % (self.args.uart_port))
        self.log.info("Minimum Battery level for OTA              : %s" % (self.args.min_battery_level))
        self.log.info("App Version check List                     : %s" % (self.args.version_check_app_list))
        self.log.info("Build mod utility path                     : %s\n\n" % (self.args.build_utils_path))
        if (self.args.encrypt_device):
            self.log.info("Encryption command                         : %s" % (self.args.encrypt_commandline))
        if (self.args.download_install_apps):
            self.log.info("Download & Install Apps                    : %s" % (self.args.download_install_apps))
        if (self.args.install_market_apps):
            self.log.info("Install Apps from Market                   : %s" % (self.args.install_market_apps))
            self.log.info("Google Account [username]                  : %s" % (self.args.google_username))
            self.log.info("Google Account [password]                  : %s" % (self.args.google_password))
        if (self.args.move_apps_to_sdcard):
            self.log.info("Move apps to sdcard                        : %s" % (self.args.move_apps_to_sdcard))
        if (self.args.app_launch_test):
            self.log.info("App Launch Test                            : %s" % (self.args.app_launch_test))

    def cleanup_working_dir(self):
        """
        Cleans up the working dir
        """
        import shutil

        if (self.working_dir != os.path.dirname(__file__)):
            #shutil.rmtree(self.working_dir)
            if (self.execute_cmd("sudo rm -rf %s" % (self.working_dir))):
                if (getattr(self, "log", False)):
                    self.log.info("Successfully cleaned up all contents from working directory")
                else:
                    print("Successfully cleaned up all contents from working directory")

    def setup_dir(self):
        """
        setup test dir creation of all dir should be here
        """
        self.init_test_dir()
        self.result_csv_filename = os.path.join(self.test_log_dir, 'results.csv')

    def is_environ_path_present(self, path):
        if path in os.environ['PATH'].split(os.pathsep):
            return True
        return False

    def setup_host_environment_variables(self, paths):
        """
        Setups the host environment variables
        """
        self.log.info("---- Setting up host environment variables----")
        for path in paths:
            if (not self.is_environ_path_present(path)):
                self.log.info("Adding [%s] to $PATH" % (path))
                os.environ['PATH'] += os.pathsep + path
        self.log.info("\n\n")

    def setup_working_dir(self):
        """
        Cleans and setups the working directory
        """
        self.working_dir = os.path.join(self.working_dir, "OTA_test_binaries")
        if (os.path.exists(self.working_dir)):
            self.cleanup_working_dir()
        FileHelper.mkdir(self.working_dir)

        self.change_working_dir(self.working_dir)
        self.ftp_location = "OTA_%s" % (str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '_'))
        self.ftp_result_file = "%s/ota_result" % (self.ftp_location)

        if (FTPUtils.make_ftp_dir("corpftp.nvidia.com", "sanik", "mW03VhG2", self.ftp_location)):
            self.log.info("Successfully created directory %s in the FTP server" % (self.ftp_location))
        else:
            self.log.error("Failed to create directory %s in the FTP server" % (self.ftp_location))

        self.setup_host_environment_variables([self.working_dir])
        self.setup_ota_partition_check_dir()

    def setup_ota_partition_check_dir(self):
        """
        Setups the OTA partition check directory
        """
        if (self.args.check_ota_partitions):
            self.log.info("Making required directories for OTA partition check test...")
            self.ota_build_dir = os.path.join(self.working_dir, "OTA_build_dir")
            self.pulled_partition_base_dir = os.path.join(self.working_dir, "OTA_pulled_partitions")

            self.orig_pulled_partition_dir = os.path.join(self.pulled_partition_base_dir, "orig_pulled_partitions")
            self.ota_pulled_partition_dir = os.path.join(self.pulled_partition_base_dir, "ota_pulled_partitions")

            FileHelper.mkdir(self.ota_build_dir)
            FileHelper.mkdir(self.orig_pulled_partition_dir)
            FileHelper.mkdir(self.ota_pulled_partition_dir)
        elif self.args.ota_diff:
            self.log.info("Making required directories for OTA Diff check test...")
            self.ota_build_dir = os.path.join(self.working_dir, "OTA_build_dir")
            self.ota_diff_output_folder = os.path.join(self.test_log_dir, "OTA_diff_output")
            self.ota_diff_output_file = os.path.join(self.test_log_dir, "OTA_diff_output_log")

            FileHelper.mkdir(self.ota_build_dir)
            FileHelper.mkdir(self.ota_diff_output_folder)

    def copy_required_files(self):
        """
        Copies required files to working directory
        """
        self.log.info("Copying Test required files...")
        import shutil

        files_to_copy = {self.args.build_utils_path: ["mkbootfs", "mkbootimg"]}
        for file_location in files_to_copy:
            for file_name in files_to_copy[file_location]:
                source_path = os.path.join(file_location, file_name)
                destination_path = os.path.join(self.working_dir, file_name)
                try:
                    self.log.debug("Copying %s to %s" % (source_path, destination_path))
                    shutil.copyfile(source_path, destination_path)
                    self.execute_cmd("sudo chmod 777 %s" % (destination_path))
                except:
                    traceback.print_exc()
                    self.log.warning("Failed to copy file [%s]" % (source_path))
                    self.log.warning("Exception Traceback : %s" % traceback.format_exc())
                    raise Exception("Failed to copy %s to %s" % (source_path, self.working_dir))
        if (self.args.download_install_apps):
            http_apks = self.args.download_install_apps.split("|")
            for http_apk in http_apks:
                local_apk_path = self.download_file(http_apk, self.working_dir)
                if (local_apk_path):
                    self.install_3rdparty_app_list.append(local_apk_path)
                else:
                    self.log.warning("Failed download apk @ [%s]. Cannot install the app." % (http_apk))

    def install_app(self):
        """
        Installs required apps to test device
        """
        self.log.info("Installing required apps")
        perforce_apk_location = os.path.join(self.p4root, "sw/apps/embedded/autosan/apks")
        perforce_apps = ["WifiConnect.apk", "OtaTest.apk", "Media_Player.apk", "app_launcher.apk"]
        for app in perforce_apps:
            app_path = os.path.join(perforce_apk_location, app)
            if (self.execute_adb_cmd("install -r %s " % (app_path), timeout=20, raise_exception=False)):
                self.log.warning("Failed to install %s" % (app_path))
            else:
                self.log.info("Successfully installed %s" % (app_path))

        for app in self.install_3rdparty_app_list:
            if (self.execute_adb_cmd("install -r %s " % (app), timeout=20, raise_exception=False)):
                self.log.warning("Failed to install %s" % (app))
            else:
                self.log.info("Successfully installed %s" % (app))

    def logDeviceUtilsOutput(self, output):
        self.log.info("-" * 50 + "\n%s\n" % (output) + "-" * 50)

    def logOutputToFile(self, logFilePath, output):
        try:
            with open(logFilePath, "a") as f:
                f.write(output)
        except:
            self.log.warning("Exception occurred while writint to log file [%s]" % (logFilePath))
            self.log.warning(traceback.format_exc())
            self.log.info("Printing the output to parent log file")
            self.logDeviceUtilsOutput(output)

    def installAppsFromPlaystore(self):
        returnVal = False
        target = 0
        installed = 0
        if (self.args.install_market_apps):
            self.logHeader("Install Apps from Google Playstore", decorSymbol="-")
            self.marketAppsResultDict = {}
            perforce_jar_location = os.path.join(self.p4root, "sw/apps/embedded/autosan/UIAutomator/DeviceSide")
            perforce_jars = ['gmail_login.jar', 'QVSPlaystoreAutomator.jar']
            self.log.info("\t\tPushing files to device \n\n")
            for file_to_push in perforce_jars:
                self.execute_adb_cmd("push %s /data/local/tmp/" % (os.path.join(perforce_jar_location, file_to_push)),
                                     timeout=20, raise_exception=False)

            self.log.info("Logging in to Google account [%s] with password [%s]" % (
            self.args.google_username, self.args.google_password))
            (returnVal, output) = DeviceUtils.addGoogleAccount(self.args.google_username, self.args.google_password)
            self.logOutputToFile(os.path.join(self.gmailLoginLogsDir, "gmail_login_stdout.txt"), output)
            self.pullLogsFromDevice("/data/qvs_logs", os.path.join(
                self.gmailLoginLogsDir))  #Pulling gmail login logs from device /data/qvs_logs
            if (returnVal):
                self.log.info("Successfully added Google account [%s]" % (self.args.google_username))

                self.log.info("Installing apps from Google Playstore...")

                appPackages = self.args.install_market_apps.split("|")
                target = len(appPackages)
                for appPackage in appPackages:
                    self.log.info("Attempting to install App [%s] from Google Playstore" % (appPackage))
                    self.marketAppsResultDict[appPackage] = {'Result': "Untested", \
                                                             'Failure Reason': "Unknown", \
                                                             'Pre OTA Package Status': "Unknown", \
                                                             'Pre OTA Package Version': "Unknown", \
                                                             'Pre OTA Package Launch Status': "Unknown", \
                                                             'Post OTA Package Status': "Unknown", \
                                                             'Post OTA Package Version': "Unknown", \
                                                             'Post OTA Package Launch Status': "Unknown" \
                        }

                    (returnVal, output) = DeviceUtils.installAppFromPlaystore(self.args.google_username,
                                                                              self.args.google_password, appPackage)
                    self.logOutputToFile(os.path.join(self.googlePlaystoreLogsDir, "playstore_app_install_stdout.txt"),
                                         output)
                    self.pullLogsFromDevice("/data/local/tmp/qvs_playstore_dir", os.path.join(
                        self.googlePlaystoreLogsDir))  #Pulling playstore logs from device
                    if (returnVal):
                        self.log.info("Successfully installed App [%s] from Google Playstore" % (appPackage))
                        installed += 1
                        appVersion = DeviceUtils.get_app_version(appPackage)
                        self.add_to_marketAppsTestResult(appPackage, "Pre OTA Package Status", "Installed")
                        self.add_to_marketAppsTestResult(appPackage, "Pre OTA Package Version", appVersion)
                    else:
                        self.log.warning("Failed to install App [%s] from Google Playstore" % (appPackage))
                        self.add_to_marketAppsTestResult(appPackage, "Pre OTA Package Status", "Not Installed")
                if (installed != 0 and installed == target):
                    self.log.info("Successfully installed all apps from Google Playstore")
            else:
                self.log.warning("Failed to add Google account [%s]" % (self.args.google_username))
                self.log.warning("Cannot install apps from Google playstore")
            self.logFooter(decorSymbol="-")

    def push_files_to_device(self):
        """
        Pushes required files to test device
        """
        if (hasattr(self, 'args') and hasattr(self.args,
                                              'incremental') and self.args.incremental and not self.ota_done):
            return
        else:
            files_to_push_list = ['utils.sh', 'busybox']
            self.log.info("\t\tPushing files to device \n\n")
            for file_to_push in files_to_push_list:
                self.execute_adb_cmd("push %s /system/bin/" % (os.path.join(self.utils_path, file_to_push)), timeout=20,
                                     raise_exception=False)
                self.execute_adb_cmd("shell chmod 777 /system/bin/%s" % (file_to_push), timeout=20,
                                     raise_exception=False)

    def adb_root_remount(self, exception=False):
        if (hasattr(self, 'args') and hasattr(self.args,
                                              'incremental') and self.args.incremental and not self.ota_done):
            return
        else:
            try:
                self.execute_adb_cmd("root", raise_exception=exception, verbose=True)
            except Exception:
                self.log.info("WAR for adb error: protocol fault")
                self.execute_adb_cmd("kill-server", raise_exception=exception, verbose=True)
                time.sleep(2)
                self.execute_adb_cmd("root", raise_exception=exception, verbose=True)
            finally:
                time.sleep(5)
                self.execute_adb_cmd("wait-for-device", raise_exception=exception)
                return_val = self.execute_adb_cmd_getbundle(command="remount", timeout=60, raise_exception=False,
                                                            large_out=False)
                attempt = 1
                while (attempt < 3):
                    disableVerityRegex = ".*adb disable-verity.*disable verity"
                    if ((return_val.stdout and re.search(disableVerityRegex, return_val.stdout, re.I)) or (
                        return_val.stderr and re.search(disableVerityRegex, return_val.stderr, re.I))):
                        self.log.info("Disabling dm_verity")
                        if (self.execute_adb_cmd("disable-verity", raise_exception=exception) == 0):
                            self.log.info("Successfully disabled dm_verity. Rebooting...")
                            if (self.reset_and_wait_for_boot_completion()):
                                self.execute_adb_cmd("root", raise_exception=exception, verbose=True)
                                time.sleep(5)
                                return_val = self.execute_adb_cmd_getbundle(command="remount", timeout=60,
                                                                            raise_exception=False, large_out=False)
                        else:
                            self.log.info("Failed to disable verity")
                    else:
                        break
                    attempt += 1
                time.sleep(5)

    def parse_cmd_line(self):
        """
        Parses commandline when executed standalone
        """
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, parents=[self.baseparser])

        mutually_exclusive_group = parser.add_mutually_exclusive_group()
        mutually_exclusive_group.add_argument("--nv_flash_cmd", default="", help="Flash command to flash base build")
        mutually_exclusive_group.add_argument("-t", "--tnspec", action="store", default="auto",
                                              help="board tnspec if flash using flash.sh")
        mutually_exclusive_group.add_argument("-f", "--use_fastboot", action="store_true",
                                              help="Use fastboot to flash the device")

        parser.add_argument("-b", "--board_type", action="store", default="unfused", required=True,
                            help="Board variant [fused | unfused]")
        parser.add_argument("-g", "--ota_build_string", action="store", default="TOT", required=True,
                            help="OTA build string that appears in TegraOTA apk [Unique string]. TOT to perform OTA on Top of the tree")
        parser.add_argument("--ota_build_flavor", action="store",
                            help="Provide the OTA build's flavor [user,userdebug]")
        parser.add_argument("-I", "--incremental", help="If set, considers the upgrade as an incremental OTA",
                            action="store_true", default=False)
        parser.add_argument("-k", "--sku", action="store", default="", help="na_wf/na_do/un_do")
        parser.add_argument("-m", "--min_battery_level", action="store", type=int, default=50,
                            help="Minimum battery percentage required for OTA")
        parser.add_argument("-o", "--oldbuild", action="store", default="", required=True, help="Old Build Url")
        parser.add_argument("-T", "--device_boot_time", action="store", type=int, default=300,
                            help="Maximum Boot time in seconds")
        parser.add_argument("--ota_update_partitions", default="NVC|EBT|BCT|RBL",
                            help="Provide partitions that are updated. With refernce to kmsg. Use | as separator.")
        parser.add_argument("--check_ota_partitions", default=None,
                            help="Provide partitions to be pulled and compared to confirm successful OTA.")
        parser.add_argument("--ota_build_path",
                            help="Provide corresponding OTA build path[Required in case of comparing partitions].")
        parser.add_argument("--ota_diff", action="store_true", default=False,
                            help="Use this argument if partition diff needs to be done using ota_diff.py")
        parser.add_argument("-U", "--user_build", action="store_true", default=False,
                            help="Use this argument if the build is user build (usb debugging isn't enabled)")
        parser.add_argument("-v", "--version_check_app_list", default="com.nvidia.tegrazone3|com.frozenbyte.Trine2",
                            help="Provide the package names to check app versions. Use | as separator.")
        parser.add_argument("-w", "--wait_for_min_battery", action="store_true", default=True,
                            help="Waits for minimum battery level before doing an OTA")
        parser.add_argument("--build_utils_path", action="store", default=None,
                            help="Provide the location for mkbootfs/mkbootimg")
        parser.add_argument("--test_name", help="Test name of the current test", default="OTATest")
        parser.add_argument("--encrypt_device", help="If set performs OTA on an encrypted device", default=False,
                            action="store_true")
        parser.add_argument("--encrypt_commandline", help="Commandline for encrypting the device",
                            default="vdc cryptfs enablecrypto inplace default")
        parser.add_argument("--download_install_apps", help="Provide http locations for app paths. Use | as separator.")
        parser.add_argument("--install_market_apps",
                            help="Provide package names of apps to be installed from Google playstore before OTA. Use | as separator.")
        parser.add_argument("--google_username",
                            help="Provide Google user account id. This is required for Google Playstore.")
        parser.add_argument("--google_password",
                            help="Provide Google user account password. This is required for Google Playstore.")

        parser.add_argument("--move_apps_to_sdcard",
                            help="Provide the package names to move to sdcard before OTA. Use | as separator.")
        parser.add_argument("--app_launch_test",
                            help="Provide the package names to perform launch test. Use | as separator.")

        parser.add_argument("--fb_partitions",
                            help="Provide Fastboot partition names and images. Use associate partition names with images. Use | to separate partitions.",
                            default="recovery:recovery.img|boot:boot.img|system:system.img|vendor:vendor.img|userdata:userdata32.img|staging:blob|bmp:bmp.blob")

        self.args = parser.parse_args()

        if ((self.args.check_ota_partitions or self.args.ota_diff) and not self.args.ota_build_path):
            raise Exception(
                "Cannot check ota partitions  [--check_ota_partitions] without the corresponding OTA build [--ota_build_path] ")
        if ((self.args.install_market_apps) and (not self.args.google_username or not self.args.google_password)):
            raise Exception(
                "[--google_username] or [--google_password] arguments missing. Cannot install Apps from Google Playstore")

    def capture_logs(self):
        pass

    def dump_logcat(self, log_file):
        if (self.execute_adb_cmd("logcat -v threadtime -d >> %s" % (log_file), raise_exception=False) == 0):
            self.log.info("Successfully dumped the logcat to [%s]" % (log_file))
        else:
            self.log.info("Failed to dumped the logcat to [%s]" % (log_file))

    def pullExtraDebugLogs(self, logDir):
        """
        Pulling Android debug logs
        """
        self.adb_root_remount(exception=False)
        self.logHeader("Pulling Extra Debug Logs", "-")
        self.execute_adb_cmd("pull /data/anr/traces.txt %s" % (logDir), raise_exception=False)
        self.execute_adb_cmd('bugreport %s/bugreport.zip' % (logDir), timeout=300, raise_exception=False)
        self.logFooter("-")

    def rename_csv_file(self):
        self.log.info("Renaming OTA diff Csv file")
        self.execute_cmd("sudo mv -f %s %s" % (os.path.join(self.ota_diff_output_folder, "results.csv"),
                                               os.path.join(self.ota_diff_output_folder, "ota_diff_results.csv")))

    def pull_logs_for_device(self):
        pass

    def pullLogsFromDevice(self, source, destination):
        if (self.execute_adb_cmd("pull %s %s" % (source, destination), raise_exception=False) == 0):
            self.log.info("Successfully pulled device side logs [%s] to [%s]" % (source, destination))
            return True
        self.log.info("Failed to pull device side logs [%s] to [%s]" % (source, destination))
        return False


    def start_testing(self):
        self.init_ota_test()
        self.start_stress_test()

    def start_uart_logging(self, uart_file_name):
        """
        start uart logginig
        """
        self.stop_uart_logging()
        self.log.info("Starting UART logging...\n")
        self.get_exclusive_com_port(self.get_log_port())
        self.uart = UartLogging(container=self, device=self.get_log_port(), logfile=uart_file_name, cond_var=self._cond)

        self.print_com_port_info(self.get_log_port())
        self.uart.start()
        self.uart_started = True
        if (not self.args.incremental):
            self.uart.send_command("su", expected=None, time_out=5)
            self.uart.send_command("source utils.sh", expected=None, time_out=5)
        self.capture_logs()

    def stop_uart_logging(self):
        """
        start uart logginig
        """
        if (self.uart_started):
            self.log.info("Stopping UART logging...\n")
            self.uart.stop()
            self.uart_started = False

    def download_file(self, file_path, location):
        """
        Download File
        """
        self.log.info("Downloading File : %s" % (file_path))
        file_name = HTTPUtils.get_file_name(file_path)
        local_file_path = os.path.join(location, file_name)
        rc = HTTPUtils.http_download_file(file_path, local_file_path)
        if (rc == 0):
            self.log.info("Successfully downloaded the File...\n")
            return local_file_path
        else:
            self.log.info("File download failed with code : %s" % (HTTPUtils.return_codes[rc]))
        return None

    def extract_build(self, build_local_path, extract_path=None):
        """
        Extract OTA base build
        """
        self.log.info("Extracting build : %s" % (build_local_path))
        if (FileHelper.extract_file(build_local_path, extract_path, self.log.info)):
            for tgz_file in glob.glob("android_*_os_image-*.tgz"):
                if os.path.isfile(tgz_file):
                    if (FileHelper.extract_file(tgz_file, extract_path, self.log.info)):
                        self.log.info("Successfully extracted [%s]" % (tgz_file))
                        #self.execute_cmd("rm -rf " + tgz_file)
                    else:
                        self.log.info("Failed to extract [%s]" % (tgz_file))
            self.log.info("Successfully extracted the build...")
            return True
        else:
            self.log.warning("Failed to extract the build...")
        return False

    def test_setup(self):
        """
        Initial test setup for OTA stress
        """
        self.logHeader("OTA Stress test setup")

        result_csv_header = ['Stress Count', 'Result', 'Failure Reason', 'Pre OTA Bootloader Version',
                             'Pre OTA Tegraboot Version', 'Pre OTA Kernel timestamp', 'OTA Build String',
                             'Post OTA Bootloader Version', 'Post OTA Tegraboot Version', 'Post OTA Kernel timestamp',
                             'Data Persistance Check', 'Modem firmware check', 'wifi check', 'Modem Data Check']

        if (self.args.check_ota_partitions):
            result_csv_header.append("OTA Partition check")

        if (self.args.ota_diff):
            result_csv_header.append("OTA Diff check")

        for app in self.args.version_check_app_list.split("|"):
            result_csv_header.append(app)

        if ("foster" in self.args.board):
            result_csv_header.append("Pre OTA FW Check")
            result_csv_header.append("Post OTA FW Check")
            result_csv_header.append("Pre OTA HDMI status")
            result_csv_header.append("Post OTA HDMI status")
            result_csv_header.append("Pre OTA Paired Blakes")
            result_csv_header.append("Post OTA Paired Blakes")

        if (self.args.app_launch_test):
            result_csv_header.append("App Launch Test")

        if (self.args.install_market_apps):
            result_csv_header.append("Market Apps Test")

        self.result_csv = CSVResult(self.result_csv_filename, result_csv_header)

        self.change_working_dir(self.working_dir)
        self.updateOTATestProgress(0, "Downloading Base build")
        self.logHeader("Download Build & Extract", "-")
        build_local_path = self.download_file(self.args.oldbuild, self.working_dir)
        if (not build_local_path):
            raise Exception("Failed to download the old build. Skipping test")

        self.updateOTATestProgress(0, "Extracting Base build")
        if (not self.extract_build(build_local_path)):
            raise Exception("Failed to extract the build...")
        self.logFooter("-")
        self.copy_required_files()
        if (self.args.user_build):
            self.log.warning(
                "*** ALERT ***   User Production images not supported in OTA stress. No way to enable adb. Test might fail")
            #self.enable_usb_debugging()
        self.logFooter()

    def setup_host_adb(self):
        adb_path = FileHelper.find("adb", [self.working_dir], True)
        if (not adb_path):
            self.log.warning("Failed to find adb. Test might fail if adb path not in environment variable.")
        else:
            adb_parent_dir = os.path.dirname(adb_path)
            if (not self.is_environ_path_present(adb_parent_dir)):
                self.setup_host_environment_variables([adb_parent_dir])

    def change_working_dir(self, directory):
        self.log.info("Changing working directory [%s] -> [%s]\n" % (os.getcwd(), directory))
        os.chdir(directory)

    def move_apks_to_sdcard(self):
        if (self.args.move_apps_to_sdcard):
            self.log.info("Moving apps to sdcard...")
            for package_name in self.args.move_apps_to_sdcard.split("|"):
                self.log.info("Moving app [%s] to sdcard..." % (package_name))
                if (DeviceUtils.move_package_to_sdcard(package_name)):
                    self.log.info("Successfully moved package [%s] to sdcard" % (package_name))
                else:
                    self.log.warning("Failed to move package [%s] to sdcard" % (package_name))
                    return False
        return True

    def screenCapture(self, screenshotFileName, hostSideDirectory, verbose=True):
        screenshotFileName = "%s_%s" % (time.time(), screenshotFileName)
        hostSideFilePath = os.path.join(hostSideDirectory, screenshotFileName)
        self.log.info("Capturing device screenshot @ [%s]" % (hostSideFilePath))
        if (DeviceUtils.screenCapture(hostSideFilePath)):
            if (verbose):
                self.log.info("Successfully captured screenshot @ [%s]" % (hostSideFilePath))
            return True
        if (verbose):
            self.log.warning("Failed to capture screenshot @ [%s]" % (hostSideFilePath))
        return False

    def perform_app_launch_test(self, appList):
        app_launch_test_results = {}
        if (not self.ota_done):
            self.logHeader("Pre OTA App Launch Tests")
        else:
            self.logHeader("Post OTA App Launch Tests")
        for package_name in appList:
            self.logHeader("Package : [%s]" % (package_name), decorSymbol="-")
            DeviceUtils.clear_ANR_traces()
            self.execute_adb_cmd("logcat -c", timeout=20)
            if (DeviceUtils.launch_app(package_name)):
                self.log.info("Successfully launched the app with package name [%s]" % (package_name))
                self.screenCapture("launch_%s.png" % (package_name.replace(".", "_")), self.appLaunchTestLogs)
                self.log.info("Sleeping 20 seconds before checking ANR/Crash")
                time.sleep(20)
                self.log.info("Checking for ANR...")
                if (DeviceUtils.has_ANR(package_name)):
                    self.log.warning("ANR observed while running package [%s]" % (package_name))
                    app_launch_test_results[package_name] = "Failed(ANR)"
                    self.screenCapture("ANR_%s.png" % (package_name.replace(".", "_")), self.appLaunchTestLogs)
                    self.logFooter(decorSymbol="-")
                    continue
                else:
                    self.log.info("No ANR observed while running package [%s]" % (package_name))
                if (DeviceUtils.has_crash(package_name)):
                    self.log.warning("Crash observed while running package [%s]" % (package_name))
                    app_launch_test_results[package_name] = "Failed(Crashed)"
                    self.screenCapture("crash_%s.png" % (package_name.replace(".", "_")), self.appLaunchTestLogs)
                    self.logFooter(decorSymbol="-")
                    continue
                else:
                    self.log.info("No Crash observed while running package [%s]" % (package_name))
                app_launch_test_results[package_name] = "Passed"
            else:
                self.log.info("Failed to launch the app with package name [%s]" % (package_name))
                app_launch_test_results[package_name] = "Failed(App not launched)"
                self.screenCapture("launch_failed_%s.png" % (package_name.replace(".", "_")), self.appLaunchTestLogs)

            self.logFooter(decorSymbol="-")
        return app_launch_test_results

    def performNonMarketAppLaunchTest(self):
        if (self.args.app_launch_test):
            appList = self.args.app_launch_test.split("|")
            app_launch_test_results = self.perform_app_launch_test(appList)
            app_launch_test_result_string = ""
            for packageName in app_launch_test_results.keys():
                app_launch_test_result_string = "%s%s %s|" % (
                app_launch_test_result_string, packageName, app_launch_test_results[packageName])
            self.add_to_result('App Launch Test', app_launch_test_result_string)

    def performMarketAppTest(self):
        if (self.args.install_market_apps):
            appList = self.args.install_market_apps.split("|")
            app_launch_test_results = self.perform_app_launch_test(appList)
            if (not self.ota_done):
                preOTAAppLaunchTestLogDir = os.path.join(self.appLaunchTestLogs, "pre_ota")
                FileHelper.mkdir(preOTAAppLaunchTestLogDir)
                self.log.info("Pulling logs of Pre OTA Market App Launch Test...\n")
                self.pullExtraDebugLogs(preOTAAppLaunchTestLogDir)

                for packageName in app_launch_test_results.keys():
                    if ("fail" in app_launch_test_results[packageName].lower()):
                        self.add_to_marketAppsTestResult(packageName, "Failure Reason",
                                                         app_launch_test_results[packageName])
                        self.add_to_marketAppsTestResult(packageName, "Pre OTA Package Launch Status", "Failed")
                    else:
                        self.add_to_marketAppsTestResult(packageName, "Pre OTA Package Launch Status", "Passed")
            else:
                postOTAAppLaunchTestLogDir = os.path.join(self.appLaunchTestLogs, "post_ota")
                FileHelper.mkdir(postOTAAppLaunchTestLogDir)
                self.log.info("Pulling logs of Post OTA Market App Launch Test...\n")
                self.pullExtraDebugLogs(postOTAAppLaunchTestLogDir)

                for packageName in self.args.install_market_apps.split("|"):
                    isAppInstalled = DeviceUtils.is_package_installed(packageName)
                    if (isAppInstalled):
                        self.log.info("App Package [%s] is installed on device post OTA" % (packageName))
                        appVersion = DeviceUtils.get_app_version(packageName)
                        self.add_to_marketAppsTestResult(packageName, "Post OTA Package Status", "Installed")
                        self.add_to_marketAppsTestResult(packageName, "Post OTA Package Version", appVersion)

                        if ("fail" in app_launch_test_results[packageName].lower()):
                            self.add_to_marketAppsTestResult(packageName, "Failure Reason",
                                                             app_launch_test_results[packageName])
                            self.add_to_marketAppsTestResult(packageName, "Post OTA Package Launch Status", "Failed")
                        else:
                            self.add_to_marketAppsTestResult(packageName, "Post OTA Package Launch Status", "Passed")
                    else:
                        self.log.warning("App Package [%s] is not installed on device post OTA" % (packageName))
                        self.add_to_marketAppsTestResult(packageName, "Post OTA Package Status", "Not Installed")

                for packageName in app_launch_test_results.keys():
                    self.add_to_marketAppsTestResult(packageName, "Post OTA Package Launch Status",
                                                     app_launch_test_results[packageName])

    def get_app_versions(self):
        """
        Get versions of apps
        """
        package_dict = {}
        package_list = self.args.version_check_app_list.split("|")
        for package in package_list:
            version = DeviceUtils.get_app_version(package)
            package_dict[package] = version
        return package_dict

    def cleanup_ftp_location(self):
        """
        Clean remote FTP location
        """
        if (FTPUtils.remove_ftp_dir("corpftp.nvidia.com", "sanik", "mW03VhG2", self.ftp_result_file)):
            self.log.info("Successfully cleaned up the old files from FTP")
        else:
            self.log.warning("Exception occured while cleaning old files from FTP")

    def data_persistence_setup(self):
        """
        Setup to check data persistence after OTA
        """
        self.log.info("Creating dummy file to check data persistence")
        FileHelper.generate_data_file(self.working_dir, 1024, "data_persistance", self.log.info)
        if (self.execute_adb_cmd("push %s /sdcard/" % (os.path.join(self.working_dir, "data_persistance")),
                                 timeout=20) == 0):
            self.log.info("Successfully pushed file to check data persistence")
        else:
            self.log.warning("Failed to push file to check data persistence")

    def connect_wifi(self):
        return_val = False
        if (DeviceUtils.is_internet_available()):
            self.log.info("Internet connection already available. No need to connect to wifi...")
            return True
        self.log.info("Connecting to wifi...")
        if (DeviceUtils.connect_wifi() and DeviceUtils.is_wifi_connected()):
            self.log.info("Successfully connected wifi")
            return_val = True
        else:
            self.log.warning("Failed to connect wifi")
            self.log.warning("Checking if internet connection is available")
            if (DeviceUtils.is_internet_available()):
                self.log.info("Internet connection available...")
            else:
                self.log.info("No Internet connection...")
                return_val = False
        self.log.info("::: NETCFG :::")
        return_val = self.execute_adb_cmd_getbundle(command="shell netcfg", timeout=60, raise_exception=False,
                                                    large_out=False)
        self.log.info("stdout    : %s" % (return_val.stdout))
        self.log.info("stderror  : %s" % (return_val.stderr))
        return return_val

    def pre_ota_setup(self):
        """
        All Pre OTA setups
        """
        self.log.info("Sleeping 20 seconds before pre ota setup\n")
        time.sleep(20)
        self.log.info("OTA test presetup\n")
        self.adb_root_remount(exception=False)
        if (self.execute_cmd("echo %s > ftp_dir" % (self.ftp_location), timeout=20) == 0):
            if (self.execute_adb_cmd("push ftp_dir /sdcard/", timeout=20) == 0):
                self.log.info("Pushed ftp location address to device [/sdcard/ftp_dir]")
            else:
                self.log.warning("Failed to push ftp_dir to device [/sdcard/ftp_dir]")
                return False
        else:
            self.log.warning("Failed write ftp location [%s] to ftp_dir" % (self.ftp_location))
            return False

        #USING THIS FILE TO CHECK IF OTA IS DONE FROM THE APK WHICH LAUNCHES AUTOMATICALLY POST EACH BOOT CYCLE
        if (self.execute_cmd("echo %s > base_kernel_timestamp.txt" % (self.pre_ota_kernal_timestamp), timeout=20) == 0):
            if (self.execute_adb_cmd("push base_kernel_timestamp.txt /sdcard/", timeout=20) == 0):
                self.log.info("Pushed Base build kernel timestamp to device [/sdcard/base_kernel_timestamp.txt]")
            else:
                self.log.warning(
                    "Failed to push Base build kernel timestamp to device [/sdcard/base_kernel_timestamp.txt]")
                return False
        else:
            self.log.warning("Failed write Base build kernel timestamp to /sdcard/base_kernel_timestamp.txt")
            return False

        self.install_app()

        if (not self.connect_wifi()):
            self.add_to_result('Result', "Failed")
            self.add_to_result('Failure Reason', "Failed to connect to wifi")
            return False

        self.log.info("Launching QVS OTATest App")
        self.execute_adb_cmd(" shell am start -n com.nvidia.otatest/.TestActivity")

        self.cleanup_ftp_location()
        self.data_persistence_setup()

        self.log.info("Getting versions for apps before OTA")
        self.pre_ota_apps_versions = self.get_app_versions()

        self.installAppsFromPlaystore()

        self.battery_check()

        return True

    def init_ota_test_params(self, stress_count):
        """
        Initializes/resets ota test values
        """
        self.ota_done = False
        self.ota_started = False
        self.ota_initiated = False
        self.base_build_flashed = False
        self.pre_ota_kernal_timestamp = None
        self.post_ota_kernal_timestamp = None
        self.pre_ota_tegra_boot_version = None
        self.post_ota_tegra_boot_version = None
        self.pre_ota_bootloader_version = None
        self.post_ota_bootloader_version = None
        self.ota_build_name = "Unknown"
        self.ota_complete_prints_copy = filter(None, self.args.ota_update_partitions.split("|"))
        print(self.ota_complete_prints_copy)

        self.result_dict = {'Stress Count': -1, 'Result': "Untested", 'Failure Reason': "Unknown",
                            'Pre OTA Bootloader Version': "Unknown", 'Pre OTA Tegraboot Version': "Unknown",
                            'Pre OTA Kernel timestamp': "Unknown", 'OTA Build String': "Unknown",
                            'Post OTA Bootloader Version': "Unknown", 'Post OTA Tegraboot Version': "Unknown",
                            'Post OTA Kernel timestamp': "Unknown", 'Data Persistance Check': "Untested",
                            'Modem firmware check': "Untested", 'wifi check': "Untested",
                            'Modem Data Check': "Untested"}

        if ("foster" in self.args.board):
            self.result_dict["Pre OTA FW Check"] = "Untested"
            self.result_dict["Post OTA FW Check"] = "Untested"
            self.result_dict["Pre OTA HDMI status"] = "Untested"
            self.result_dict["Post OTA HDMI status"] = "Untested"
            self.result_dict["Pre OTA Paired Blakes"] = "unknown"
            self.result_dict["Post OTA Paired Blakes"] = "unknown"

        if (self.args.install_market_apps):
            self.result_dict["Market Apps Test"] = "Untested"

        if (self.args.app_launch_test):
            self.result_dict["App Launch Test"] = "Untested"

        self.add_to_result('Stress Count', stress_count)

        if (self.args.check_ota_partitions):
            self.result_dict["OTA Partition check"] = "Untested"

        if (self.args.ota_diff):
            self.result_dict["OTA Diff check"] = "Untested"

        for app in self.args.version_check_app_list.split("|"):
            self.result_dict[app] = "Unknown"

        self.test_iteration_log_dir = os.path.join(self.test_log_dir, "OTA_iteration_%d" % (stress_count))
        FileHelper.mkdir(self.test_iteration_log_dir)

        if (self.args.install_market_apps or self.args.app_launch_test):

            self.appLaunchTestLogs = os.path.join(self.test_iteration_log_dir, "app_launch_test_logs")
            FileHelper.mkdir(self.appLaunchTestLogs)

            if (self.args.install_market_apps):
                self.gmailLoginLogsDir = os.path.join(self.test_iteration_log_dir, "gmail_login_logs")
                FileHelper.mkdir(self.gmailLoginLogsDir)

                self.googlePlaystoreLogsDir = os.path.join(self.test_iteration_log_dir, "google_playstore_logs")
                FileHelper.mkdir(self.googlePlaystoreLogsDir)

                market_apps_result_csv_filePath = os.path.join(self.test_iteration_log_dir,
                                                               self.market_apps_result_csv_filename)
                market_apps_result_csv_header = ['Package Name', 'Result', 'Failure Reason', 'Pre OTA Package Status',
                                                 'Pre OTA Package Version', 'Pre OTA Package Launch Status',
                                                 'Post OTA Package Status', 'Post OTA Package Version',
                                                 'Post OTA Package Launch Status']

                self.market_apps_result_csv = CSVResult(market_apps_result_csv_filePath, market_apps_result_csv_header)


    def sanitize_list(unsanitized_list):
        sanitized_list = []
        for element in unsanitized_list:
            if (not element and len(element.trim()) > 0):
                sanitized_list.append(element)
        return sanitized_list

    def add_to_result(self, key, value):
        """
        Add results to result dict
        """
        import types

        if (type(value) == types.IntType):
            if (self.result_dict[key] == -1):
                self.result_dict[key] = value
        else:
            if (self.result_dict[key].lower() in ("untested", "unknown", "", "None")):
                self.result_dict[key] = value
                if (key == "Result"):
                    if (value.lower() == "passed"):
                        self.passedIterations += 1
                    elif (value.lower() == "failed"):
                        self.failedIterations += 1

    def add_to_marketAppsTestResult(self, packageName, key, value):
        """
        Add results to Market Apps Test Result dict
        """
        if (self.marketAppsResultDict[packageName][key].lower() in ("untested", "unknown", "", "None")):
            self.marketAppsResultDict[packageName][key] = value

    def reset_and_wait_for_boot_completion(self, boot_wait_time=1200):
        """
        Resets the device and waits for boot completion
        """
        self.log.info("Resetting the device...")
        PM342.reset()
        self.boot_hawkeye()
        return self.wait_for_boot_completion()

    def boot_hawkeye(self):
        if (self.args.board in ("p2290_hawkeye_dvt2",)):
            self.log.info("Pressing onkey for 3 seconds to turn on the device\n")
            PM342.execute_command("onkey_down")
            time.sleep(3)
            PM342.execute_command("onkey_up")

    def wait_for_boot_completion(self, boot_wait_time=1200):
        """
        Waits for boot completion
        """
        self.log.info("Waiting for boot completion...")
        if (DeviceUtils.wait_for_boot_complete(boot_wait_time)):
            self.log.info("Device booted up...")
            return True
        else:
            self.log.info("Checking if device is in offline mode")
            if DeviceUtils.is_device_offline():
                self.log.warning("Looks like device is in offline mode. Restarting adb daemon via UART")
                if not self.uart.send_command(command="su", expected="#", time_out=5):
                    self.log.warning("Command [su] failed")
                command_list = ["stop adbd", "setprop service.adb.root 0", "start adbd"]
                for command in command_list:
                    if not self.uart.send_command(command="%s && echo __RETURN_CODE_$?_" % (command),
                                                  expected="RETURN_CODE_0", time_out=5):
                        self.log.warning("Command [%s] failed" % command)
            else:
                self.log.info("Device is not in offline mode")
            if DeviceUtils.wait_for_boot_complete(boot_wait_time):
                return True
        if self.reboot_required:
            self.reboot_required = False
            self.log.info("Resetting using pm342 reset\n")
            PM342.reset()
            self.boot_hawkeye()
            if (DeviceUtils.wait_for_boot_complete(boot_wait_time)):
                self.log.info("Device booted up...")
                return True
        self.log.info("Device failed to booted up...")
        return False

    def handle_post_flash_encryption(self):
        self.log.info("Checking for Post Flash Encryption...\n")
        if (DeviceUtils.wait_for_device_encryption_to_start()):
            self.log.info("Device is being encrypted. Waiting for device encryption.[600 secs]")
            if (DeviceUtils.wait_for_device_encryption_to_end(600)):
                self.log.info("Device encryption done...")
                return DeviceUtils.wait_for_boot_complete(1200)
        else:
            self.log.info("Device is not being encrypted. Continuing with the test...")
            return True
        self.log.info("Failed to wait for Device Encryption...")
        return False

    def get_tegraflash_command(self, flash_logs):
        self.log.info("Getting the Tegraflash command from the flash logs...\n")
        tegraflash_commandline = "(sudo.*tegraflash.py.*$)"
        with open(flash_logs) as fh_flash_logs:
            for line in fh_flash_logs:
                match_obj = re.match(tegraflash_commandline, line, re.I)
                if (match_obj):
                    self.tegraflash_command = match_obj.group(1)
                    self.log.info("Tegraflash Command : [%s]\n" % (self.tegraflash_command))
                    break

    def flash_and_wait_for_boot(self, stress_count):
        """
        Flashes build and waits for boot completion
        """
        return_val = False
        uartlog = os.path.join(self.test_iteration_log_dir, "base_build_flash_uart.txt")
        flash_log = os.path.join(self.test_iteration_log_dir, "base_build_flash_stdout.txt")
        self.start_uart_logging(uartlog)
        if (not self.flash_base_build(flash_log)):
            self.log.warning("Failed to flash old build...")
            self.add_to_result('Result', "Failed")
            self.add_to_result('Failure Reason', "Nvflash failure")
        else:
            self.base_build_flashed = True
            self.setup_host_adb()
            self.log.info("Successfully flashed the device with Base build\n")
            device_bootup_status = False
            for attempt in range(1, 4):
                device_bootup_status = self.wait_for_boot_completion(1200) if (
                attempt == 1) else self.reset_and_wait_for_boot_completion(1200)
                if (device_bootup_status):
                    if (not self.handle_post_flash_encryption()):
                        self.log.info("Failed to handle Post flash device encryption. Test might fail")
                    self.reset_and_wait_for_boot_completion()
                    self.post_flash_settings()
                    return_val = self.reset_and_wait_for_boot_completion() and self.pre_ota_setup()
                    if (not return_val):
                        self.log.warning("Failed to boot after performing post flash settings")
                        self.add_to_result('Result', "Failed")
                        self.add_to_result('Failure Reason', "Boot failure after flash presetup")
                    else:
                        break
            if (not device_bootup_status):
                self.log.warning("Device failed to booted up after flashing...")
                self.add_to_result('Result', "Failed")
                self.add_to_result('Failure Reason', "Post flash boot failure")
        self.stop_uart_logging()
        return return_val

    @execute_only_on_board("foster_cpc", "foster_pro", "foster_e")
    def check_device_firmwares(self, is_pre_ota_check=True):
        firmware_check_logfile = "firmware_check.txt"
        if (is_pre_ota_check):
            firmware_check_logfile = "pre_ota_%s" % (firmware_check_logfile)
        else:
            firmware_check_logfile = "post_ota_%s" % (firmware_check_logfile)
        firmware_check_logfile = os.path.join(self.test_iteration_log_dir, firmware_check_logfile)
        firmware_check_script_name = "fw_check.py"
        firmware_errors = ""
        result_csv_key = "Post OTA FW Check"
        fw_check_script_path = FileHelper.find(firmware_check_script_name, [self.working_dir], True)
        if (fw_check_script_path):
            self.log.info("Checking Device Firmwares [Using %s]" % (firmware_check_script_name))
            command = "python %s " % (fw_check_script_path)
            return_val = self.execute_cmd_getbundle(command, timeout=120)
            if (return_val.stdout):
                with open(firmware_check_logfile, "w") as firmware_check_log_fh:
                    firmware_check_log_fh.write(return_val.stdout)
                fail_check_regex = "\d+\s+\:\s*(.*)\s+(\[error\])"
                for line in return_val.stdout.splitlines():
                    search_obj = re.search(fail_check_regex, line, re.I)
                    if (search_obj):
                        self.log.info("Found Firmware error : [%s]" % (line))
                        firmware_errors = "%s, %s:%s" % (firmware_errors, search_obj.group(1), search_obj.group(2))
            else:
                self.log.info("Script [%s] Output seems to be NULL" % (fw_check_script_path))
                self.log.info("Output : %s" % (return_val.stdout))
                self.log.info("Error  : %s" % (return_val.stderr))
                return
        else:
            self.log.info("Failed to find the Firmware check script [%s]" % (firmware_check_script_name))
            return
        if (is_pre_ota_check):
            result_csv_key = "Pre OTA FW Check"
        if (len(firmware_errors) > 0):
            self.add_to_result(result_csv_key, firmware_errors)
        else:
            self.add_to_result(result_csv_key, "Passed")

    @execute_only_on_board("foster_cpc", "foster_pro", "foster_e")
    def check_hdmi_connection(self, is_pre_ota_check=True):
        self.log.info("Checking HDMI connection...")
        result_csv_key = "Post OTA HDMI status"
        hdmi_status = "Not Connected"
        if (DeviceUtils.is_hdmi_connected()):
            hdmi_status = "Connected"
        if (is_pre_ota_check):
            result_csv_key = "Pre OTA HDMI status"
        self.add_to_result(result_csv_key, hdmi_status)
        self.log.info("HDMI connection : [%s]" % (hdmi_status))

    @execute_only_on_board("foster_cpc", "foster_pro", "foster_e")
    def get_paired_blakes(self, is_pre_ota_check=True):
        self.log.info("Getting paired blakes/Thunderstrikes...")
        result_csv_key = "Post OTA Paired Blakes"
        blakes = ""
        for blake in DeviceUtils.get_paired_blakes():
            if (blake):
                blakes += "%s | " % (blake)
        if (is_pre_ota_check):
            result_csv_key = "Pre OTA Paired Blakes"
        self.add_to_result(result_csv_key, blakes)
        self.log.info("Paired blakes/Thunderstrikes [%s]" % (blakes))

    def write_csv_result(self, result):
        if (result):
            self.log.info("Result : [OTA Passed]")
            self.add_to_result('Result', "Passed")
            self.result_dict['Failure Reason'] = ""
        else:
            self.log.info("Result : [OTA Failed]")
            self.add_to_result('Result', "Failed")

        self.log.info("Writing to csv file...")
        self.result_csv.write_to_file(self.result_dict)

    def writeMarketAppsResult(self):
        marketAppsResultStatus = "Passed"
        if (self.args.install_market_apps):
            for packageName in self.args.install_market_apps.split("|"):
                if (self.marketAppsResultDict[packageName]['Failure Reason'] != None and
                            self.marketAppsResultDict[packageName]['Failure Reason'].lower() not in (
                        "unknown", "untested")):
                    marketAppsResultStatus = "Failed"
                if (self.marketAppsResultDict[packageName]['Failure Reason'] == None or
                            self.marketAppsResultDict[packageName]['Failure Reason'].lower() in (
                        "unknown", "untested")):
                    self.add_to_marketAppsTestResult(packageName, "Result", "Passed")
                    self.add_to_marketAppsTestResult(packageName, "Failure Reason", "")
                self.marketAppsResultDict[packageName]["Package Name"] = packageName
                self.log.info("[%s ]Writing to Market Apps Result csv file..." % (packageName))
                self.market_apps_result_csv.write_to_file(self.marketAppsResultDict[packageName])

                self.result_dict["Market Apps Test"] = marketAppsResultStatus

    def restart_adb_server(self):
        if (self.execute_cmd("sudo adb kill-server") == 0):
            time.sleep(3)
            if (self.execute_cmd("sudo adb start-server") == 0):
                time.sleep(3)
                self.log.info("Successfully restarted adb server")
                return True
        self.log.info("Failed to restart adb server")
        return False

    def check_recovery_logs(self, recovery_log, stress_count):
        probable_kernel_timestamp = None
        if (recovery_log):
            ota_success_regex = "script\s*succeeded\:\s*.*\[successful\S\]"
            kernel_time_stamp = "\[[\s*\d+\.+]+\].*Linux version .* SMP PREEMPT\s*(.*)"
            with open(recovery_log, "r") as recovery_lf:
                for line in recovery_lf:
                    search_obj = re.search(kernel_time_stamp, line, re.I)
                    if (search_obj):
                        probable_kernel_timestamp = search_obj.group(1).strip()
                    elif (re.search(ota_success_regex, line, re.I)):
                        self.log.info(
                            "Found OTA success print(in recovery log. Maybe OTA was done but UART logs for partition updation wasn't found..."))
                        self.post_ota_kernal_timestamp = probable_kernel_timestamp
                        self.ota_done = True
                        return self.post_ota_tests(stress_count)
        else:
            self.log.info("Looks like there is no recovery logs :-( .I'm giving up...")
        return False

    def encrypt_device(self):
        self.log.info("Encrypting the device")
        self.log.info("Using commandline : [%s]" % (self.args.encrypt_commandline))
        if (self.execute_adb_cmd('shell "%s"' % (self.args.encrypt_commandline), timeout=600,
                                 raise_exception=False) == 0):
            self.log.info("Looks like the device is encrypted.")
            if (DeviceUtils.wait_for_boot_complete(self.args.device_boot_time)):
                self.log.info("Device booted up...")
                self.log.info("Double checking if device is encrypted...")
                if (DeviceUtils.is_encrypted()):
                    self.log.info("Successfully encrypted the device...")
                    return True
            else:
                self.log.info("Device failed to booted up...")
        self.log.info("Failed to encrypt the device...")
        return False

    def get_kernel_timestamp(self):
        if (not self.pre_ota_kernal_timestamp):
            cat_command = "/proc/version"
            self.log.info(
                "Looks like I'm not getting kernel timestamp from UART logs. Will try with [%s]" % (cat_command))
            re_kernel_timestamp = re.compile("Linux version .* SMP PREEMPT\s*(.*)", re.IGNORECASE)
            output = DeviceUtils.cat(cat_command)
            if (output):
                self.log.info("[%s] output : [%s]" % (cat_command, output))
                search_obj = re_kernel_timestamp.search(output)
                if (search_obj):
                    self.pre_ota_kernal_timestamp = search_obj.group(1).strip()
                    self.log.info("Pre OTA Kernel Timestamp : [%s]" % (self.pre_ota_kernal_timestamp))
                    self.result_dict['Pre OTA Kernel timestamp'] = self.pre_ota_kernal_timestamp
                else:
                    self.log.info("Failed to match kernel timstamp regex")
            else:
                self.log.info("[%s] returned nothing" % (cat_command))
        else:
            self.log.info("Looks like I got kernel timestamp through UART logs already...")

    def enable_uart_logging(self):
        command = 'shell "echo 1 > /sys/class/tty/ttyS0/console_write_enable"'
        if (self.execute_adb_cmd(command, raise_exception=False) == 0):
            self.log.info("Successfully enabled uart logging...")
            return True
        self.log.info("Failed to enable uart logging...")
        return False

    def updateOTATestProgress(self, iteration=0, message=None):
        if (hasattr(self.args, "job_id") and self.args.job_id):
            try:
                if (os.path.exists(
                        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Scripts")))):
                    SCRIPTS_PATH = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Scripts"))
                    if (SCRIPTS_PATH not in sys.path):
                        sys.path.insert(1, SCRIPTS_PATH)

                from status_update import send_status

                progress = 0.0

                totalExecuted = iteration - 1
                if (totalExecuted <= 0):
                    currentQScore = 0.0
                else:
                    currentQScore = float(self.passedIterations) / totalExecuted * 100
                    currentQScore = float("{0:.2f}".format(currentQScore))

                progress = float(totalExecuted) / self.args.stresscount * 100
                progress = float("{0:.2f}".format(progress))
                if (progress <= 0):
                    progress = 10.0
                additionalInfo = "[OTA Stress]"
                if (message):
                    additionalInfo = "%s [%s]" % (additionalInfo, message)
                additionalInfo = "%s [%d/%d] [Q: %.2f] [P: %d] [F: %d]" % (
                additionalInfo, iteration, self.args.stresscount, currentQScore, self.passedIterations,
                self.failedIterations)
                self.log.info("Updating OTA Test progress [%.2f]" % (progress))
                self.log.info("Updating OTA Test Additional Info [%s]" % (additionalInfo))
                send_status(self.args.job_id, addnl_info=additionalInfo, percentage=progress)
            except:
                self.log.warning("Exception occurred while updating status")
                self.log.warning(traceback.format_exc())

    def start_stress_test(self, ota_retries=3):
        """
        Starts OTA stress
        """
        self.logHeader("Starting OTA Stress")
        for stress_count in range(1, self.args.stresscount + 1):
            self.log.info("Turning On USB via PM342 usb_on to enable usb bypass\n\n")
            PM342.usb_on()

            self.updateOTATestProgress(stress_count)
            self.restart_adb_server()
            ota_result = False
            self.init_ota_test_params(stress_count)
            self.logHeader("OTA Stress Iteration %d/%d" % (stress_count, self.args.stresscount), decorSymbol="=")
            self.log.info("Test iteration log directory [%s]" % (self.test_iteration_log_dir))
            self.updateOTATestProgress(stress_count, "Flashing device with Base build")
            if (self.flash_and_wait_for_boot(stress_count)):
                self.updateOTATestProgress(stress_count, "Successfully flashed device")

                self.get_kernel_timestamp()
                self.adb_root_remount(exception=False)
                self.enable_uart_logging()
                self.pre_ota_tests()

                retry = 0
                while (retry <= ota_retries):
                    attempt = retry + 1
                    self.logHeader("Attempt %d/%d" % (attempt, ota_retries), decorSymbol="-")
                    self.test_iteration_attempt_log_dir = os.path.join(self.test_iteration_log_dir,
                                                                       "ota_attempt_%d" % (attempt))
                    FileHelper.mkdir(self.test_iteration_attempt_log_dir)
                    self.log.info("OTA Attempt %d log directory [%s]" % (attempt, self.test_iteration_attempt_log_dir))

                    uartlog = os.path.join(self.test_iteration_attempt_log_dir, "pre_ota_uart.txt")
                    self.start_uart_logging(uartlog)

                    self.result_dict["Failure Reason"] = ""
                    if (not DeviceUtils.is_device_on()):
                        self.log.info("Either device isnt ON or usb debugging not enabled. Skipping test")
                        self.add_to_result('Failure Reason',
                                           "Either device isnt ON or usb debugging not enabled. Skipping test")
                        #break;
                    else:
                        self.connect_wifi()
                        logcat = os.path.join(self.test_iteration_attempt_log_dir, "pre_ota_logcat.txt")
                        self.dump_logcat(logcat)
                        self.updateOTATestProgress(stress_count, "Performing OTA")
                        self.perform_ota_update(attempt)

                    self.stop_uart_logging()

                    uartlog = os.path.join(self.test_iteration_attempt_log_dir, "post_ota_uart.txt")
                    self.start_uart_logging(uartlog)

                    recovery_log = self.get_recovery_dump_logs(stress_count, attempt)
                    self.pullExtraDebugLogs(self.test_iteration_attempt_log_dir)

                    if (self.ota_done):
                        self.updateOTATestProgress(stress_count,
                                                   "Successfully OTAed. Waiting for post OTA test results")
                        self.reset_and_wait_for_boot_completion()
                        self.log.info("Sleeping 200 seconds to get the results updated in FTP server")
                        time.sleep(200)  #SLEEPING FOR OTA TEST APP TO LAUNCH AND UPLOAD RESULTS TO FTP SERVER
                        #self.log.info("Sleeping 500 seconds to complete the audio playback")
                        #time.sleep(500) #SLEEPING FOR OTA TEST APP TO LAUNCH AND PLAYBACK AUDIO
                        ota_result = self.post_ota_tests(stress_count)
                        logcat = os.path.join(self.test_iteration_attempt_log_dir, "post_ota_logcat.txt")
                        self.dump_logcat(logcat)
                        self.logFooter(decorSymbol="-")
                        break;
                    else:
                        ota_result = self.check_recovery_logs(recovery_log, stress_count)
                        if (ota_result):
                            self.add_to_result('Failure Reason', "Didn't get partition update prints in UART logs")
                            break
                        if (self.ota_started):
                            self.log.info("OTA flashing was started but failed. Won't be retrying...")
                            break
                        retry = retry + 1
                        attempt = retry + 1
                        self.log.info("==== Retrying OTA [%d/%d] ====\n" % (attempt, ota_retries))
                        self.reset_and_wait_for_boot_completion()
                    self.stop_uart_logging()
                    self.logFooter(decorSymbol="-")
            self.writeMarketAppsResult()
            self.write_csv_result(ota_result)
            if self.args.ota_diff:
                self.rename_csv_file()
            self.log.info("OTA Stress Done %d/%d\n\n" % (stress_count, self.args.stresscount))
        self.log.info("OTA Stress Test Complete\n")
        self.logFooter()


    def split_boot_image(self):
        self.log.info("Splitting boot.img to get ramdisk.img and kernel")
        split_boot_script = os.path.join(self.utils_path, "build_utils", "split_boot.py")
        split_boot_command = "python %s -v -i %s -o %s" % (split_boot_script, "boot.img", self.working_dir)
        return_val = self.execute_cmd_getbundle(split_boot_command, 120)
        if (return_val.error_code == 0):
            self.log.info(return_val.stdout)
            self.log.info("Ramdisk and Kernel split successfull...")
            return True
        self.log.warning("***Failed to split Ramdisk and Kernel...")
        return False


    def unpack_ramdisk(self):
        self.log.info("Extracting ramdisk.img")
        if (self.execute_cmd("gzip -dc < 'ramdisk.img' | cpio --extract")):
            self.log.warning("Failed to extract ramdisk.img")
            if (throw_exception):
                raise Exception("Failed to extract ramdisk.img")

    def pack_ramdisk(self, ramdisk_path, throw_exception):
        self.log.info("Packing ramdisk.img")
        if (self.execute_cmd("sudo rm %s" % (ramdisk_path))):
            self.log.warning('Failed to remove ramdisk.img')

        mkboootfs_path = FileHelper.find("mkbootfs", [self.working_dir], True)
        if (not mkboootfs_path):
            raise Exception("Failed to find mkbootfs in working directory. Exiting...")
        if (self.execute_cmd("sudo %s tmp | gzip -9 > ramdisk.img" % (mkboootfs_path))):
            self.log.warning('Failed to pack ramdisk.img')
            if (throw_exception):
                raise Exception("Failed to pack ramdisk.img. Failed to enable USB Debugging")

    def build_boot_img(self, throw_exception):
        self.log.info("Rebuilding boot.img")

        if (self.execute_cmd("sudo rm -rf boot.img")):
            self.log.warning('Failed to remove boot.img')
            if (throw_exception):
                raise Exception("Failed to enable USB Debugging")
        mkbootimg = FileHelper.find("mkbootimg", [self.working_dir], True)
        kernel = FileHelper.find("kernel", [self.working_dir], True)
        if (not kernel):
            raise Exception("Failed to find kernel file to build boot.img . Cannot proceed")
        if (not mkbootimg):
            raise Exception("Failed to find mkbootimg in working directory. Exiting...")
        if (self.execute_cmd("sudo %s --kernel %s --ramdisk ramdisk.img -o boot.img" % (mkbootimg, kernel))):
            self.log.warning('Failed to make boot.img')
            if (throw_exception):
                raise Exception("Failed to build boot.img Failed to enable USB Debugging")

    def update_default_prop(self):
        try:
            if os.path.isfile("default.prop"):
                import fileinput

                self.log.info("Modifying default.prop")
                for line in fileinput.input("default.prop", inplace=True):
                    if line.find("ro.adb.secure=1") != -1:
                        self.log.info("[default.prop] <- ro.adb.secure=0")
                        sys.stdout.write("ro.adb.secure=0\n")
                    elif line.find("persist.sys.usb.config") != -1:
                        self.log.info("[default.prop] <- persist.sys.usb.config=mtp,adb")
                        sys.stdout.write("persist.sys.usb.config=mtp,adb\n")
                    else:
                        sys.stdout.write(line)
                with open("default.prop", "a") as fd:
                    self.log.info("[default.prop] <- persist.service.adb.enable=1")
                    fd.write("persist.service.adb.enable=1\n")
                    self.log.info("[default.prop] <- persist.service.debuggable=1")
                    fd.write("persist.service.debuggable=1\n")
                    self.log.info("[default.prop] <- persist.adb.notify=0")
                    fd.write("persist.adb.notify=0\n")
                    self.log.info("Successfully modified default.prop")
        except Exception:
            self.log.warning('USB Debugging not enabled...')
            self.log.warning('Cannot use device with adb')
            if (throw_exception):
                raise Exception("Failed to enable USB Debugging")

    def enable_usb_debugging(self, throw_exception=True):
        """
        Enable usb debugging on user builds
        """
        import shutil

        self.log.info("Reconfiguring to enable USB Debugging")
        FileHelper.rmdir("tmp")
        FileHelper.mkdir("tmp")
        ramdisk = "ramdisk.img"
        ramdisk_path = FileHelper.find(ramdisk, [self.working_dir], True)
        if (not ramdisk_path):
            self.log.warning("File not found : [%s] . Will try splitting boot.img to get the same" % (ramdisk))
            if (self.split_boot_image()):
                ramdisk_path = FileHelper.find(ramdisk, [self.working_dir], True)
                if (not ramdisk_path):
                    raise Exception("ramdisk.img not found. Failed to enable USB Debugging")
            else:
                self.log.warning("Failed to split boot.img to get ramdisk.img. Cannot proceed")
                raise Exception("ramdisk.img not found. Failed to enable USB Debugging")

        tmp_dir = os.path.join(self.working_dir, "tmp")
        if (self.execute_cmd("sudo mv %s %s" % (ramdisk_path, tmp_dir))):
            self.log.warning("Failed to move %s to %s" % (ramdisk_path, tmp_dir))
        FileHelper.chdir(tmp_dir)
        self.unpack_ramdisk()

        self.update_default_prop()

        FileHelper.chdir(self.working_dir)
        self.log.info('Current working directory : %s' % (os.getcwd()))
        return_val = self.execute_cmd_getbundle("sudo rm %s" % (os.path.join(self.working_dir, "ramdisk.img")))
        if (return_val.error_code):
            self.log.warning(return_val.stderr)
        else:
            self.log.info(return_val.stdout)

        self.pack_ramdisk(ramdisk_path, throw_exception)
        self.build_boot_img(throw_exception)
        self.log.info("Successfully done the reconfiguring")

    def get_flash_command(self, use_flash_script=True, tnspec=None):
        """
        Generates flash command
        """
        flash_command = None
        if (use_flash_script):
            if (not tnspec):
                self.log.warning('TNSPEC missing...')
                raise Exception("TNSPEC missing. Cannot flash the device")
            flash_command = ' '.join(["BOARD=%s" % tnspec, "./flash.sh"])
            if (self.args.board_type == "fused" and self.args.board not in ("p2290_hawkeye_dvt2",)):
                flash_command = "%s %s" % (flash_command, "-f")

            if re.search("foster|darcy", self.args.board, re.I):
                partsbackLocation = os.path.join(os.environ.get("HOME"), ".partsback")
                if os.path.exists(partsbackLocation):
                    self.log.info("Modifying flash command. Will flash using partsback @ %s" % (partsbackLocation))
                    flash_command = flash_command.replace("flash.sh", "flash.sh -p")

            self.execute_cmd("echo 'YES' > input_file")

            flash_command = "%s < %s" % (flash_command, "input_file")
        return flash_command

    def flash_base_build(self, flash_log=None):
        """
        Flash the device with the base build
        """
        self.change_working_dir(self.working_dir)
        self.log.info("Flashing device with Base build\n\n")
        return self.flash_build(flash_log)

    def get_fastboot_path(self):
        path = FileHelper.find("fastboot", [self.working_dir, ], True)
        if (not path):
            path = os.path.join(self.utils_path, "build_utils", "fastboot")
        return path

    def fb_erase_partition(self, partition_name):
        self.log.info("Erasing the partition [%s]" % (partition_name))
        if (self.fastboot.erase_partition(partition_name)):
            self.log.info("Successfully Erased partition [%s]" % (partition_name))
            return True
        self.log.warning("Failed to Erase partition [%s]" % (partition_name))
        return False

    def fb_flash_partition(self, partition_name, image_path):
        self.log.info("Flashing the partition [%s] with image @ [%s]" % (partition_name, image_path))
        if (self.fastboot.flash_partition(partition_name, image_path)):
            self.log.info("Successfully Flashed partition [%s] with Image [%s]\n" % (partition_name, image_path))
            return True
        self.log.warning("Failed to Flash partition [%s] with Image [%s]\n" % (partition_name, image_path))
        return False

    def check_for_fastboot_oem_unlock(self):
        self.log.info("Checking if device is in fastboot mode...")
        if (self.fastboot.wait_for_fastboot_mode()):
            self.log.info("Device in fastboot mode...")
            self.log.info("Unlocking OEM if device isn't unlocked...")
            if (self.args.board in ("TN8_CR_DO")):
                if (self.fastboot.unlock_OEM(self.args.board, False)):
                    self.log.info("OEM Unlocked... Proceeding with fastboot flashing...")
                    return True
            elif (self.fastboot.unlock_OEM(self.args.board)):
                self.log.info("OEM Unlocked... Proceeding with fastboot flashing...")
                return True
            else:
                self.log.warning("Failed OEM unlock the device...")
        else:
            self.log.warning("Failed to put the device in fastboot mode...")
        return False

    def prepare_for_fastboot(self):
        if (not DeviceUtils.is_device_on()):
            self.reset_and_wait_for_boot_completion()
        self.log.info("Putting the device to bootloader mode using Adb...")
        DeviceUtils.reboot_bootloader()
        if (not self.check_for_fastboot_oem_unlock()):
            self.log.warning("Failed to put the device in fastboot mode...")
            self.log.info("Trying relay sequence...")
            RELAY.fastboot_mode(self.args.board)
        return self.check_for_fastboot_oem_unlock()

    def fastboot_flash(self):
        from fastboot import Fastboot

        fastboot_binary_path = self.get_fastboot_path()
        if (fastboot_binary_path):
            self.fastboot = Fastboot(fastboot_binary_path, use_sudo=True)
            if (self.prepare_for_fastboot()):
                self.log.info("Performing fastboot flashing...")
                self.fb_erase_partition("cache")
                partitions = self.args.fb_partitions.split("|")
                for partition in partitions:
                    temp = partition.split(":")
                    p_name = temp[0]
                    p_image = temp[1]
                    p_image_abs_path = FileHelper.find(p_image, [self.working_dir, ], True)
                    if (p_image_abs_path):
                        self.log.info("Found Image [%s] @ [%s]" % (p_image, p_image_abs_path))
                        self.fb_erase_partition(p_name)
                        time.sleep(2)
                        if (not self.fb_flash_partition(p_name, p_image_abs_path)):
                            self.log.warning("****Fastboot Flashing Failed****")
                            return False
                        time.sleep(2)
                self.log.info("Fastboot flashing done... Rebooting")
                return self.fastboot.reboot()
        else:
            raise Exception("fastboot not found...Cannot proceed")

    def lsusb(self):
        self.log.debug("Listing all USB devices. lsusb ...")
        return_val = self.execute_cmd_getbundle("lsusb", timeout=120)
        if (return_val.stdout):
            self.log.info("\n%s\n" % (return_val.stdout))
        else:
            self.log.debug("Failed to get lsusb output\n")

    def flash_build(self, flash_log=None):
        """
        Flash the device
        """
        if (self.args.use_fastboot):
            return self.fastboot_flash()
        else:
            self.log.info("Putting the device to recovery mode...")
            PM342.force_recovery(self.args.board)

            self.lsusb()

            self.log.info("Flashing the device...")
            self.log.info("Current Working Dir : %s" % (os.getcwd()))
            flash_command = self.get_flash_command(True, self.args.tnspec)
            if (not flash_command):
                raise Exception("Couldn't figure out the flash command. God help us all !")
            if (flash_log):
                flash_command = "%s > '%s'" % (flash_command, flash_log)
            return_val = self.execute_cmd_getbundle(flash_command, 1800, large_out=True)
            (return_val.stdout, return_val.stderr, return_val.error_code)

            self.get_tegraflash_command(
                flash_log)  #TO KNOW THE TEGRAFLASH FLASHING COMMAND WHICH CAN BE USED WHILE READING PARTITIONS

            if (return_val.error_code):
                self.log.warning("****Nvflash Failed****")
                self.log.warning(return_val.stderr)
            else:
                return True
        return False

    def flash_OTA_build(self, flash_log=None):
        """
        Flash the device with the OTA build
        """
        self.change_working_dir(self.ota_build_dir)
        self.log.info("Flashing device with OTAed build to read partitions\n\n")
        return self.flash_build(flash_log)

    def flash_and_pull_partitions(self):
        self.log.info("Starting OTA build flash and partition read")
        ota_flash_logs = os.path.join(self.test_log_dir, "ota_build_flash_log")
        if (not self.flash_OTA_build(ota_flash_logs)):
            self.log.warning("Failed to flash OTA build. Cannot read the partitions now...")
            raise Exception("Failed to flash OTA build. Cannot read the partitions now...")
        if self.args.ota_diff:
            if not self.wait_for_boot_completion():
                return False
            self.adb_root_remount()
            if not self.run_ota_diff():
                self.log.warning("Could not run otadiff_core.py successfully on flashed OTA build")
                raise Exception("Could not run otadiff_core.py successfully on flashed OTA build")
            else:
                return True
        else:
            self.android_build_utils = AndroidBuildUtils(self.ota_build_dir, is_signed=False)
            self.pull_partitions(self.orig_partition_list, self.orig_pulled_partition_dir)

    @skip_if_not("android")
    def run_ota_diff(self):
        """
        Function to run otadiffcore.py
        """
        self.log.info("Running ota_diff")
        self.execute_cmd(
            'echo "=============================NEW_RUN_STARTING=============================" >> %s' % self.ota_diff_output_file)
        return_val = self.execute_cmd_getbundle(
            "sudo python otadiff_core.py -d %s >> %s" % (self.ota_diff_output_folder, self.ota_diff_output_file),
            timeout=3600, large_out=True)
        if return_val.error_code:
            self.log.error("OTA diff failed")
            return False
        else:
            self.log.info("OTA diff passed")
            return True

    @skip_if_not("android")
    def disable_packages(self, package_list):
        """
        Disables the list of packages provided
        """
        self.log.info("Disabling android Packages")
        for package in package_list:
            self.log.info("Disabling android Package %s " % (package))
            if (DeviceUtils.disable_package(package)):
                self.log.info("Successfully disabled android Package %s " % (package))
            else:
                self.log.info("Failed to disable android Package %s " % (package))

    def post_flash_settings(self):
        """
        Performs Post boot operations
        """
        self.log.info("Performing post boot configurations\n")
        for i in range(1, 4):
            try:
                self.adb_root_remount()
                break;
            except:
                self.log.info("***No Root Permissions***")
                if (i == 3):
                    raise
                self.log.info("Retrying...[%d/3] after 2 seconds" % (i + 1))
                time.sleep(2)

        DeviceUtils.never_suspend()

        self.disable_packages(
            ["com.google.android.setupwizard", "com.google.android.tungsten.setupwraith", "com.nvidia.shield.welcome",
             "com.nvidia.calibnotifier"])

        if (DeviceUtils.set_settings_property("secure", "user_setup_complete", "1")):
            self.log.info("User setup completed...")
        else:
            self.log.info("User setup incomplete...God help us now !")

        self.log.info("Changing display timeout")
        if (DeviceUtils.set_settings_property("system", "screen_off_timeout", "1800000")):
            self.log.info("Successfully changed display timeout")
        else:
            self.log.warning("Failed to change display timeout")

        if (DeviceUtils.allow_adb_app_installation()):
            self.log.info("Successfully enabled app installation over adb")
        else:
            self.log.warning("Failed to enable app installation over adb")

        if (DeviceUtils.disable_lock()):
            self.log.info("Successfully disabled Android lock screen")
        else:
            self.log.warning("Failed to disable Android lock screen")

        self.log.info("Force changing Language to English [en-US]. Setting property [persist.sys.locale]")
        if (DeviceUtils.set_prop("persist.sys.locale", "en-US")):
            self.log.info("Successfully changed language to English [en-US]")
        else:
            self.log.warning("Failed to change language to English [en-US]")

        self.push_files_to_device()

        if (self.args.encrypt_device):
            if not self.encrypt_device():
                self.log.warning("Failed to encrypt the device. Raising exception to fail the test")
                raise Exception("Failed to encrypt the device...")


    def wait_for_ota_completion(self, bailout=1200):
        self.log.info("Waiting for %d seconds for OTA completion" % (bailout))
        if (DeviceUtils.wait_4_device_2_enter_recovery(600)):
            self.log.info("Device entered OTA recovery")
            self.log.info("Waiting for OTA flash and bootcompletion [%d] seconds" % (600))
            if (DeviceUtils.wait_for_boot_complete(timeout=600)):
                if (self.ota_done):
                    return True
        else:
            self.log.info("Device failed to enter OTA recovery")
        return False

    def start_json_RPC_server(self, port=9008):
        self.log.info("Starting JSON RPC Server...")
        command = "forward tcp:%d tcp:%d" % (port, port)
        return_val = self.execute_adb_cmd_getbundle(command, timeout=60, raise_exception=False, large_out=False)
        if (return_val.error_code == 0):
            self.log.info("Checking if JSON RPC Server was started...")
            return_val = self.execute_adb_cmd_getbundle("forward --list | grep %d" % (port), timeout=60,
                                                        raise_exception=False, large_out=False)
            if (return_val.error_code == 0):
                self.log.info("Successfully started JSON RPC Server...")
                return self.check_json_RPC_server()
        self.log.info("Failed to start JSON RPC Server...")
        return False

    def check_json_RPC_server(self):
        self.log.info("Sending HTTP request to check JSON RPC Server...")
        command = "curl -d '{\"jsonrpc\":\"2.0\",\"method\":\"deviceInfo\",\"id\":1}' localhost:9008/jsonrpc/0"
        return_val = self.execute_cmd_getbundle(command, timeout=60, large_out=False)
        if (return_val.stdout):
            self.log.debug("JSON RPC STATUS : %s" % (return_val.stdout))
            import json

            uidevice_props = json.loads(return_val.stdout)
            print(uidevice_props)
            if (type(uidevice_props) == type(dict())):
                for key in uidevice_props.keys():
                    self.log.info("%s : %s" % (key, uidevice_props[key]))
                if ("error" in uidevice_props):
                    return False
                else:
                    self.log.info("JSON RPC Server ACTIVE...")
                    return True
            else:
                self.log.warning("Invalid Ui Device properties...")
        return False;

    def forcePushUIAutomationLibs(self):
        try:
            import uiautomator

            uiautomatorPath = os.path.dirname(uiautomator.__file__)
            uiautomatorLibsPath = os.path.join(uiautomatorPath, "libs")
            self.log.info("Force-pushing UI Automator libraries")
            if (os.path.exists(uiautomatorLibsPath)):
                self.log.info("Found Python uiautomator libs @ [%s]" % (uiautomatorLibsPath))
                files = os.listdir(uiautomatorLibsPath)
                for library in files:
                    if (library.endswith(".jar")):
                        libraryAbsolutePath = os.path.join(uiautomatorLibsPath, library)
                        self.log.info("Pushing JAR library [%s] to /data/local/tmp/" % (libraryAbsolutePath))
                        if (self.execute_adb_cmd("push %s /data/local/tmp/" % (libraryAbsolutePath), timeout=60,
                                                 raise_exception=False, verbose=True) == 0):
                            self.log.info("Successfully pushed [%s] to /data/local/tmp/" % (libraryAbsolutePath))
                        else:
                            self.log.warning("Failed to push [%s] to /data/local/tmp/" % (libraryAbsolutePath))
                    elif (library.endswith(".apk")):
                        libraryAbsolutePath = os.path.join(uiautomatorLibsPath, library)
                        self.log.info("installing apk library [%s]" % (libraryAbsolutePath))
                        if (self.execute_adb_cmd("install -r %s " % (libraryAbsolutePath), timeout=60,
                                                 raise_exception=False, verbose=True) == 0):
                            self.log.info("Successfully installed [%s]" % (libraryAbsolutePath))
                        else:
                            self.log.warning("Failed to install [%s]" % (libraryAbsolutePath))
                    else:
                        self.log.info("[%s] not required..." % (library))
            else:
                self.log.warning("Python UI Automator library [%s] not found" % (uiautomatorLibsPath))
        except Exception:
            self.log.warning("Exception occurred while force pushing UIAutomator libraries")
            self.log.warning(traceback.format_exc())

    def getUiDevice(self, retry_count=3):
        retry_attempt = 1
        while (retry_attempt <= retry_count):
            try:
                from uiautomator import device as ui_device

                ui_device.server.adb.cmd("shell ls /sdcard/").wait()
                ui_device.info
                return ui_device
            except Exception:
                self.log.warning("UIAutomator Exception")
                self.log.warning(traceback.format_exc())
                self.forcePushUIAutomationLibs()
                self.restart_adb_server()
                self.start_json_RPC_server()
            retry_attempt += 1
        self.add_to_result('Failure Reason', "UIAutomator Exception")
        return None

    def ui_auto_war(self, ui_device, retry_count=3):
        retry_attempt = 1
        while (retry_attempt <= retry_count):
            try:
                ui_device.server.adb.cmd("shell ls /sdcard/").wait()
                ui_device.info
                return True
            except Exception:
                self.log.warning("UIAutomator Exception")
                self.log.warning(traceback.format_exc())
                self.start_json_RPC_server()
            retry_attempt += 1
        self.add_to_result('Failure Reason', "UIAutomator Exception")


    def ui_auto_launch_nvidia_OTA_app(self, ui_device):
        if (DeviceUtils.is_package_installed(self.ota_app_package_name)):
            ota_app_version_name = DeviceUtils.get_app_version(self.ota_app_package_name)
            if (len(ota_app_version_name.strip()) > 0):
                self.ota_app_version = ota_app_version_name[0:ota_app_version_name.index(".")]

            if (self.args.incremental):
                launcherActivityAction = self.ota_app_ui_elements[self.ota_app_version]["launcher_activity_action"]
                self.log.info("Launching Nvidia OTA app [Version : %s]... ACTION [%s]" % (
                ota_app_version_name, launcherActivityAction))
                DeviceUtils.launch_app(self.ota_app_package_name, launcherActivityAction=launcherActivityAction)
                self.execute_adb_cmd("shell input keyevent KEYCODE_DPAD_DOWN", raise_exception=False)
            else:
                activity_name = self.ota_app_ui_elements[self.ota_app_version]["activity_name"]
                self.log.info("Launching Nvidia OTA app [Version : %s]... [%s]" % (ota_app_version_name, activity_name))
                DeviceUtils.launch_app(self.ota_app_package_name, activity_name)

            if (DeviceUtils.wait_for_app_launch(package_name=self.ota_app_package_name, timeout=20)):
                self.log.info("Successfully launched Tegra OTA app...")
                if (self.args.incremental):
                    self.log.info("Hitting Controller DPAD DOWN key to enter internal OTA")
                    ui_device.press("down")
                ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'ota_app_launched.png'))
                time.sleep(10)
                return True
            else:
                ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'ota_app_not_launched.png'))
                self.log.warning("Failed to launch Tegra OTA app...")
                self.add_to_result('Failure Reason', "Failed to launch Tegra OTA app...")
        else:
            self.log.warning("OTA app [%s] not installed on this device" % (self.ota_app_package_name))
            self.log.warning("Installed Packages : %s" % (DeviceUtils.get_installed_packages()))
            self.add_to_result('Failure Reason', "OTA app [%s] not installed..." % (self.ota_app_package_name))
        return False


    def ui_auto_handle_wifi_mac_dialog(self, ui_device):
        """
        Handle the wifi mac issue UI
        """
        try:
            ui_device(className='android.widget.Button', text="OK").click()
            if (ui_device(textContains='Wi-Fi unstable, due to default MAC').wait.gone(timeout=1000)):
                return True
        except Exception:
            self.log.warning("Oops ! exception occurred while handling the dialog")
            self.log.warning(traceback.format_exc())
        return False


    def ui_auto_choose_ota_branch(self, ui_device):
        self.log.info("Choosing the branch %s" % (self.args.branch))
        if (ui_device(text=self.ota_app_ui_elements[self.ota_app_version]["text_branch"]).wait.exists(timeout=60000)):
            ui_device(text=self.ota_app_ui_elements[self.ota_app_version]["text_branch"]).click.wait()
            if (ui_device(text=self.args.branch).wait.exists(timeout=10000)):
                ui_device(text=self.args.branch).click()
                return True
            else:
                self.log.warning("Provided Branch [%s] not found..." % (self.args.branch))
                ui_device.screenshot(
                    os.path.join(self.test_iteration_attempt_log_dir, 'no_branch_%s.png' % (self.args.branch)))
                self.add_to_result('Failure Reason', "Provided Branch [%s] not found..." % (self.args.branch))
        else:
            self.log.warning("No option to choose branch [Choose branch] button is missing...")
            ui_device.screenshot(
                os.path.join(self.test_iteration_attempt_log_dir, 'no_choose_branch_%s.png' % (self.args.branch)))
            self.add_to_result('Failure Reason', "No option to choose branch [Choose branch] button is missing...")
        return False


    def ui_auto_select_ota_build(self, ui_device):
        self.log.info("Selecting OTA build...")
        if self.args.ota_build_string.lower() == "tot":
            ui_device(className='android.widget.RelativeLayout',
                      index=self.ota_app_ui_elements[self.ota_app_version]["tot_index"]).click()
            return True
        else:
            if ui_device(scrollable=True).scroll.to(textContains=self.args.ota_build_string):
                self.ota_build_name = ui_device(textContains=self.args.ota_build_string).info['text']
                self.log.info("Clicking OTA build [%s]\n" % (self.ota_build_name))
                self.add_to_result('OTA Build String', self.ota_build_name)
                ui_device(textContains=self.args.ota_build_string).click()
                return True
            else:
                self.log.warning("OTA build string [%s] not found" % (self.args.ota_build_string))
                ui_device.screenshot(
                    os.path.join(self.test_iteration_attempt_log_dir, 'no_build_%s.png' % (self.args.ota_build_string)))
                self.add_to_result('Failure Reason', "OTA build string [%s] not found" % (self.args.ota_build_string))
        return False

    def new_ui_auto_select_ota_build(self, ui_device):
        self.log.info("Selecting OTA build...")
        if self.args.ota_build_string.lower() == "tot":
            build_selector = ui_device(className='android.widget.RelativeLayout',
                                       index=self.ota_app_ui_elements[self.ota_app_version]["tot_index"])
            self.ota_build_name = build_selector.sibling(resourceId="com.nvidia.ota:id/text1").info['text']
            build_selector.click()
            return True
        else:
            if (self.args.ota_build_flavor):
                self.log.info(
                    "Selecting Build [%s] | Flavor [(%s)]" % (self.args.ota_build_string, self.args.ota_build_flavor))
                flavorText = "(%s)" % (self.args.ota_build_flavor)
                i = 0
                while (True):
                    ui_device.wait.update()
                    ui_device.wait.idle()
                    retry = 0
                    while (retry <= 3):
                        build_selector = ui_device(textContains=self.args.ota_build_string).sibling(
                            textContains=flavorText)
                        if build_selector.exists:
                            self.ota_build_name = build_selector.sibling(textContains=self.args.ota_build_string).info[
                                'text']
                            self.log.info("Clicking OTA build [%s]\n" % (self.ota_build_name))
                            self.add_to_result('OTA Build String', self.ota_build_name)
                            build_selector.click()
                            return True
                        scrollResult = ui_device(scrollable=True).scroll(steps=100)
                        retry += 1
                    if (not scrollResult):
                        i += 1
                        if (i > 1):
                            break
                    self.log.warning("OTA build string [%s] Flavor [%s] not found" % (
                    self.args.ota_build_string, self.args.ota_build_flavor))
            else:
                if ui_device(scrollable=True).scroll.to(textContains=self.args.ota_build_string):
                    self.ota_build_name = ui_device(textContains=self.args.ota_build_string).info['text']
                    self.log.info("Clicking OTA build [%s]\n" % (self.ota_build_name))
                    self.add_to_result('OTA Build String', self.ota_build_name)
                    ui_device(textContains=self.args.ota_build_string).click()
                    return True
        self.log.warning("OTA build string [%s] not found" % (self.args.ota_build_string))
        ui_device.screenshot(
            os.path.join(self.test_iteration_attempt_log_dir, 'no_build_%s.png' % (self.args.ota_build_string)))
        self.add_to_result('Failure Reason', "OTA build string [%s] not found" % (self.args.ota_build_string))
        return False

    def uiGetUIElementByText(self, uiObjectWithGenericSelector, text, caseInsensitive=True, timeToWait=30000):
        if (uiObjectWithGenericSelector.wait.exists(timeout=timeToWait)):
            for uiObject in uiObjectWithGenericSelector:
                uiObjectText = uiObject.text
                if (caseInsensitive and uiObjectText):
                    uiObjectText = uiObjectText.lower()
                    if (text):
                        text = text.lower()
                if (text and uiObjectText == text):
                    return uiObject
        return None

    def ui_auto_download_ota_build(self, ui_device):

        self.log.info("Downloading OTA package...")
        uiDownloadButton = self.uiGetUIElementByText(ui_device(className='android.widget.Button'), "Download",
                                                     timeToWait=60000)
        if (uiDownloadButton):
            uiDownloadButton.click()
        else:
            self.log.info("Cannot find the Download button...")
            ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'no_download_btn.png'))
            self.add_to_result('Failure Reason', "Cannot find the Download button...")
            return False
        if (ui_device(resourceId=self.ota_app_ui_elements[self.ota_app_version]["resourceid_download"]).wait.exists(
                timeout=60000)):
            self.log.info("Download started...")
            self.log.info("Waiting for download to complete. Will wait for max 1 hour for the download to complete.")
            if (ui_device(
                    textContains=self.ota_app_ui_elements[self.ota_app_version]["text_download_finished"]).wait.exists(
                    timeout=3600000)):
                self.log.info("Download Complete...")
                return True
            else:
                self.log.info("Download still not complete. Can't wait anymore...")
                ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'download_incomplete.png'))
                self.add_to_result('Failure Reason', "OTA Download still not complete. Can't wait anymore...")
        else:
            self.log.info("Download didn't start")
            ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'download_notstarted.png'))
            self.add_to_result('Failure Reason', "OTA Download didnt start")
        return False


    def ui_auto_flash_ota_build(self, ui_device, retry):
        return_val = False
        self.log.info("OTA build flashing...")
        uiFlashButton = self.uiGetUIElementByText(ui_device(className='android.widget.Button'), "Flash",
                                                  timeToWait=30000)
        if (uiFlashButton):
            uiFlashButton.click()
            if (self.ota_app_version == "1"):
                uiInstallButton = self.uiGetUIElementByText(ui_device(className='android.widget.Button'), "Install",
                                                            timeToWait=30000)
                if (uiInstallButton):
                    self.log.info("Hitting the Install Button")
                    uiInstallButton.click()
                else:
                    self.log.info("Cannot find the Install button...")
                    ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'no_install_btn.png'))
                    self.add_to_result("failure_reason", "Cannot find the Install button...")
            ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'flashing_installing_ota.png'))
            self.log.info("Installing...")
            self.ota_initiated = True
            uartlog = os.path.join(self.test_iteration_attempt_log_dir, "ota_uart.txt")
            self.start_uart_logging(uartlog)
            if (self.wait_for_ota_completion()):
                return_val = True
            else:
                self.reset_and_wait_for_boot_completion()
                return_val = self.ota_done
            self.stop_uart_logging()
        else:
            self.log.info("Cannot find the Flash button...")
            ui_device.screenshot(os.path.join(self.test_iteration_attempt_log_dir, 'no_flash_btn.png'))
            self.add_to_result('Failure Reason', "Cannot find the Flash button...")
        return return_val


    def ota_ui_automation(self, retry):
        """
        UI automation to do an OTA with Tegra OTA app
        """
        self.logHeader("Starting OTA Update via Tegra OTA App", decorSymbol="-")
        #d = Device(self.args.adbserial)
        d = self.getUiDevice()
        try:
            if (d):
                if (d(textContains='Wi-Fi unstable, due to default MAC').wait.exists(timeout=5000)):
                    self.log.warning(
                        "Looks like device wifi is unstable. Device has MAC issues. Test might fail due to this...")
                    self.ui_auto_handle_wifi_mac_dialog(d)

                if (self.ui_auto_launch_nvidia_OTA_app(d)):
                    time.sleep(5)
                    if (self.ui_auto_choose_ota_branch(d)):
                        time.sleep(5)
                        if (self.new_ui_auto_select_ota_build(d)):
                            time.sleep(5)
                            if (self.ui_auto_download_ota_build(d)):
                                time.sleep(5)
                                return self.ui_auto_flash_ota_build(d, retry)
            else:
                return False

        except:
            logging.error('Exception Occured while ota update: %s' % (traceback.format_exc()))
            self.add_to_result('Failure Reason', "UI Automation Exception Occured while ota update")
            return False


    def battery_check(self):
        """
        Performs device battery checks
        """
        battery_level = DeviceUtils.get_battery_level()
        self.log.info("Battery Level : %s" % (battery_level))
        if (battery_level != -1):
            if (battery_level < self.args.min_battery_level):
                self.log.warning("Battery level less than minimum battery level [%d] required for OTA..." % (
                self.args.min_battery_level))
                self.log.info("Waiting for Battery to charge...")
                try:
                    if (not DeviceUtils.wait_for_battery_level(self.args.min_battery_level)):
                        self.log.warning("Failed to charge battery. Check if charger is connected...")
                        self.add_to_result('Failure Reason',
                                           "Battery level %d < Minimum battery level required for OTA %d" % (
                                           battery_level, self.args.min_battery_level))
                except Exception:
                    self.log.warning("Exception occured while waiting for battery charging...")
                    self.log.warning(traceback.format_exc())
        else:
            self.log.warning(
                "Failed to get the Battery level. OTA can fail due to battery level < %d" % self.args.min_battery_level)

    def clear_ota_app_cache(self):
        if (DeviceUtils.clear_app_cache(self.ota_app_package_name)):
            self.log.info("Successfully cleared the OTA app cache...")
            return True
        else:
            self.log.warning("Failed to clear the OTA app cache...")
        return False

    def perform_ota_update(self, retry):
        """
        Checks if OTA can be done and calls ota ui automation
        """
        self.adb_root_remount(exception=False)
        self.clear_ota_app_cache()
        if (not DeviceUtils.unlock_device()):
            self.log.warning(
                "Failed to unlock the device. Oh God ! I suspect OTA would fail as device isn't unlocked...")
            self.add_to_result('Failure Reason', "Failed to unlock device.")

        if (self.ota_ui_automation(retry)):
            return True
        else:
            self.log.info("OTA seems to be failed. Will check recovery logs further..")
            if (len(self.ota_complete_prints_copy) > 0):
                f_partitions = ""
                for partition in self.ota_complete_prints_copy:
                    self.log.warning("Failed to update %s" % partition)
                    f_partitions = "%s, %s" % (f_partitions, partition)
                self.add_to_result('Failure Reason', "Failed to update %s" % f_partitions)
        if (DeviceUtils.is_device_on()):
            self.execute_adb_cmd("shell am force-stop %s" % (self.ota_app_package_name), raise_exception=False)
            if (not DeviceUtils.wait_for_app_launch(package_name=self.ota_app_package_name, timeout=1)):
                self.log.info("Successfully killed Tegra OTA app...")
            else:
                self.log.warning("Failed to kill Tegra OTA app...")
        else:
            self.log.warning("Looks like device is not on...I suspect the error happened while flashing the OTA build")
            self.add_to_result('Failure Reason',
                               "Looks like device is not on...I suspect the error happened while flashing the OTA build")
            if (not self.reset_and_wait_for_boot_completion()):
                self.log.warning("Either Device failed to boot up or usb debugging is disabled...")
        return False

    def post_ota_kernel_timestamp_check(self):
        if (not self.pre_ota_kernal_timestamp):
            self.log.warning("Oops ! I don't have the pre OTA kernal timestamp :-(")
            self.add_to_result('Failure Reason', "Missing...Pre OTA kernel timestamp")
            return False

        if (not self.post_ota_kernal_timestamp):
            self.log.warning("Oops ! I don't have the post OTA kernal timestamp :-(")
            self.add_to_result('Failure Reason', "Missing...Post OTA kernel timestamp")
            return False

        if (self.pre_ota_kernal_timestamp and self.post_ota_kernal_timestamp):
            if (self.pre_ota_kernal_timestamp.strip() == self.post_ota_kernal_timestamp.strip()):
                self.log.warning("Looks like the pre OTA kernal timestamp and the post OTA kernal timestamp are same.")
                self.add_to_result('Failure Reason', "Pre and Post kernel timestamp matches...")
                return False
        return True

    def ota_partition_check(self):
        if (self.args.check_ota_partitions):
            self.log.info("Performing OTA partition compare check...\n\n")
            self.adb_root_remount()
            self.pull_partitions(self.ota_partition_list, self.ota_pulled_partition_dir)
            partition_result = self.check_ota_partitions()
            self.log.info("OTA partition check -> %s" % (partition_result))
            self.add_to_result('OTA Partition check', partition_result)
        elif (self.args.ota_diff):
            if not self.copy_ota_diff_files():
                self.add_to_result('OTA Diff check', "untested")
                self.log.error("Could not copy OTA diff Scripts")
                return
            self.log.info("Performing OTA diff on build with OTA update done on base build.\n\n")
            if self.run_ota_diff():
                self.add_to_result('OTA Diff check', "pass")
            else:
                self.add_to_result('OTA Diff check', "failed")

    def pre_ota_tests(self):
        """
        Perform All the pre-OTA tests
        """
        self.logHeader("Pre OTA Tests", decorSymbol="-")
        self.check_device_firmwares(is_pre_ota_check=True)
        self.move_apks_to_sdcard()
        self.get_paired_blakes(is_pre_ota_check=True)
        self.check_hdmi_connection(is_pre_ota_check=True)
        self.performMarketAppTest()
        self.logFooter(decorSymbol="-")


    def post_ota_tests(self, stress_count):
        """
        All OTA functional checks
        """
        self.logHeader("Post OTA Tests", decorSymbol="-")
        ota_functional_result = True
        self.ota_partition_check()
        self.check_device_firmwares(False)

        ota_result_ftp_address = "ftp://sanik:mW03VhG2@corpftp.nvidia.com/%s/ota_result" % (self.ftp_location)

        '''result_dir="ota_result_%d"%(stress_count)
        ota_result_dir = os.path.join(self.test_log_dir,result_dir)
        FileHelper.mkdir(ota_result_dir)'''
        ota_result = os.path.join(self.test_iteration_log_dir, "ota_result")

        if (FTPUtils.ftp_download_file(ota_result_ftp_address, ota_result) == os.EX_OK):
            self.log.info("Successfully downloaded results from FTP server...")
            if os.path.exists(ota_result):
                with open(ota_result, 'r') as f:
                    testdata = f.read()
                    self.parse_ftp_result_file(testdata)
            else:
                self.log.info("ota_result file not present @ [%s], skipping Functional Check" % (ota_result))
        else:
            self.log.warning("Failed to download results from FTP server...")

        if (not self.post_ota_kernel_timestamp_check()):
            ota_functional_result = False

        self.performNonMarketAppLaunchTest()
        self.performMarketAppTest()
        self.logFooter(decorSymbol="-")

        return ota_functional_result

    def parse_ftp_result_file(self, data):
        self.log.info("Parsing the result file pulled from FTP server")

        # ========= Data Persistence =========
        if re.search("Data Persistence,(.*)", data):
            output = re.search('.*Data Persistence,(.*)', data).group(1).rstrip()
            self.log.info("Data Persistence -> %s" % output)
            self.add_to_result('Data Persistance Check', output)
        else:
            self.log.warning("[REGEX][Data Persistence] Regex pattern didnt match...")

        # ========= Modem firmware check =========
        output = ""
        if self.args.sku != "na_wf":
            if re.search('.*modem_firmware,(.*)', data):
                output = re.search('.*modem_firmware,(.*)', data).group(1).rstrip()
                self.log.info("Modem_firmware -> %s" % (output))
                self.add_to_result('Modem firmware check', output)
            else:
                self.log.warning("[REGEX][Modem firmware] Regex pattern didnt match...")
        else:
            self.log.info("Modem_firmware -> Not applicable")
            self.add_to_result('Modem firmware check', "Not applicable")

        # ========= wifi check =========
        if re.search("WIFI,(.*)", data, re.I):
            output = re.search('.*WIFI,(.*)', data).group(1).rstrip()
            self.log.info("WIFI -> %s" % output)
            self.add_to_result('wifi check', output)
        else:
            self.log.warning("[REGEX][WIFI] Regex pattern didnt match...")

        # ========= Modem Data Check =========
        if self.args.sku != "na_wf":
            if re.search('.*Modem Data,(.*)', data):
                output = re.search('.*Modem Data,(.*)', data).group(1).rstrip()
                self.log.info("Modem Data check -> %s" % (output))
                self.add_to_result('Modem Data Check', output)
            else:
                self.log.warning("[REGEX][Modem Data] Regex pattern didnt match...")
        else:
            self.log.info("Modem Data check -> Not Applicable")
            self.add_to_result('Failure Reason', "Not Applicable")

        if (hasattr(self.args, 'board') and self.args.board in ("foster_cpc", "foster_pro", "foster_e")):
            # ========= HDMI check =========
            if re.search("HDMI,(.*)", data, re.I):
                output = re.search('.*HDMI,(.*)', data).group(1).rstrip()
                self.log.info("HDMI -> %s" % output)
                self.add_to_result('Post OTA HDMI status', output)
            else:
                self.log.warning("[REGEX][HDMI] Regex pattern didnt match...")

            # ========= Blake check =========
            if re.search("Blake Connections,(.*)", data, re.I):
                output = re.search('.*Blake Connections,(.*)', data).group(1).rstrip()
                self.log.info("Blake Connections -> %s" % output)
                self.add_to_result('Post OTA Paired Blakes', output)
            else:
                self.log.warning("[REGEX][Blake Connections] Regex pattern didnt match...")

        # ========= tegrazone version =========
        if re.search("Tegrazone Version\s*\:(.*)", data, re.I):
            output = re.search('.*Tegrazone Version\s*\:(.*)', data).group(1).rstrip()
            self.log.info("Tegrazone Version -> %s" % output)
            self.add_to_result('com.nvidia.tegrazone3', output)
        else:
            self.log.warning("[REGEX][Tegrazone Version] Regex pattern didnt match...")

        # ========= Kernel timestamp version =========
        if (not self.post_ota_kernal_timestamp):
            self.log.warning(
                "Oops ! I don't have the post OTA kernal timestamp. Looks like uart logs aren't coming up completely after post OTA")
            self.log.info("Checking FTP server result file for Kernel timestamp")
            if re.search("linux version", data, re.I):
                output = re.search('.*Linux version .* SMP PREEMPT\s*(.*)', data).group(1).rstrip()
                self.post_ota_kernal_timestamp = output.strip()
                self.log.info("Post OTA Kernel Timestamp : [%s]" % self.post_ota_kernal_timestamp)
                self.add_to_result('Post OTA Kernel timestamp', self.post_ota_kernal_timestamp)
            else:
                self.log.warning("[REGEX][Kernel Timestamp] Regex pattern didnt match...")

    def pull_partitions(self, partition_dict, location):
        if (not self.tegraflash_command):
            self.log.info(
                "Couldn't figure out the tegraflash command used for flashing. Will try using the default command")
        self.log.info("Putting the device to recovery mode...")
        PM342.force_recovery(self.args.board)

        time.sleep(5)
        self.lsusb()

        cmp_partitions = self.args.check_ota_partitions.split("|")
        for partition in cmp_partitions:
            partition = partition.strip()
            if (len(partition) > 0):
                target_file = os.path.join(location, partition + ".bin")
                self.log.info("Reading partition [%s]" % partition)
                partition_file = self.android_build_utils.read_partition(partition, target_file,
                                                                         tegra_flash_commandline=self.tegraflash_command)
                if (partition_file):
                    partition_dict[partition] = partition_file
                    self.log.warning("Successfully read the partition %s\n\n" % (partition_file))
                else:
                    self.log.warning("Couldn't read the partition %s\n\n" % (target_file))

    def check_ota_partitions(self):
        self.log.info("Performing OTA partition check...")
        cmp_partitions = self.args.check_ota_partitions.split("|")
        result_msg = ""
        diff_partition_list = []
        for partition in cmp_partitions:
            if (partition and self.orig_partition_list[partition] and self.ota_partition_list[partition]):
                if (FileHelper.diff(self.orig_partition_list[partition], self.ota_partition_list[partition])):
                    self.log.info("Partition %s Matches [%s] [%s]" % (
                    partition, self.orig_partition_list[partition], self.ota_partition_list[partition]))
                else:
                    self.log.warning("Partition %s differs [%s] [%s]" % (
                    partition, self.orig_partition_list[partition], self.ota_partition_list[partition]))
                    diff_partition_list.append(partition)
                    return_val = False
        if (len(diff_partition_list) > 0):
            result_msg = "Failed :- Partition [%s] differs" % (diff_partition_list)
        else:
            result_msg = "Passed"

        return result_msg

    def get_recovery_dump_logs(self, stress_count, retry_count):
        self.log.info("Pulling the OTA recovery logs...")
        log_file = os.path.join(self.test_iteration_attempt_log_dir, "ota_recovery.log")
        command = "shell dumpsys dropbox --print(SYSTEM_RECOVERY_LOG > %s" % (log_file))
        if (self.execute_adb_cmd(command, raise_exception=False)):
            self.log.info("Failed to pull the recovery logs...")
            return None
        self.log.info("Successfully pulled the recovery logs...")
        return log_file

    def set_utlities_path(self, utils_path):
        """
        set path for test utilities
        """
        if os.path.exists(utils_path):
            self.utils_path = utils_path
            return True
        raise Exception("utils path doesn't exists %s" % (utils_path))

    def set_working_dir(self, working_dir):
        """
        set_working_dir method sets the working dir
        """
        self.working_dir = working_dir

    def set_stress_count(self, stresscount=1000):
        """
        set_stress_count method sets the boot test stresscount
        """
        self.args.stresscount = stresscount

    def setbailout_time(self, bailout=100):
        """
        setbailout_time method sets the bailout time before which tests should be termed as failure
        """
        self.bailout = bailout

    def set_uart_log_file(self, uart_logfile=None):
        """
        set_uart_log_file sets the uart logs filename
        """
        self.kernel_uart_log = uart_logfile

    def set_logcat_file(self, logcat_file=None):
        """
        setlogcat_file sets the logcat logs filename
        """
        self.logcat_file = logcat_file

    def set_args(self, argument_bundle=None):
        """
        set the args value
        """
        self.args = argument_bundle
        self.set_default_arg_attributes()

    def set_relay_type(self, relay_type):
        """
        set relay type
        """
        self.args.relay_type = relay_type

    def set_log_location(self, log_location):
        """
        set log location
        """
        self.args.loglocation = log_location
        self.test_log_dir = log_location

    def set_debug_mode(self):
        """
        set debug mode value
        """
        self.args.debug = False

    def set_log_verbose(self):
        """
        set verbose level value
        """
        self.args.verbose = False

    def set_stress_count(self, stresscount=1000):
        """
        Function to set suspend resume stress count
        """
        self.args.stresscount = stresscount

    def set_adbserial(self, devserial=""):
        """
        set adb serial value
        """
        self.args.adbserial = devserial

    def set_build_utils_path(self, path):
        """
        set build utils path
        """
        self.args.build_utils_path = path

    def set_logs_port(self, port="/dev/ttyS0"):
        """
        set the port from which debug logs are collected for host where uart is used
        set it to /dev/ttyS0 for usb-uart convertor /dev/ttyUSBXX
        """
        self.args.uart_port = port

    def set_uart_log_file(self, uart_logfile=None):
        """
        set the log file where uart logs needs to be stored
        """
        self.kernel_uart_log = uart_logfile

    def set_boot_complete_string(self, boot_complete="BOOT_COMPLETE"):
        """
        Set custom boot complete string
        """
        self.args.boot_string = boot_complete

    def get_log_port(self):
        """
        return the port selected for collecting debug logs
        """
        return self.args.uart_port


'''
['Stress Count','Pre OTA Bootloader Version','Pre OTA Tegraboot Version','Pre OTA Kernel timestamp','Post OTA Bootloader Version','Post OTA Tegraboot Version','Post OTA Kernel timestamp','Data Persistance Check','Modem firmware check','wifi check','Modem Data Check','Tegrazone3 Version Check','Trine2 Version Check']
'''


def main():
    """
    main method here we create an instance of OTATest and set the basic parameters
    when reusing it in some other script we have to follow below lines of code .
    """
    ota_test = OTAtest()
    ota_test.parse_cmd_line()
    ota_test.start_testing()

#**********************************************************************************************************

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        print("Exception while running the OTA stress test")
