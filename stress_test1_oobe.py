"""Test 1"""
#不断地factory，重启
import subprocess
import sys
import time

class Test:
    """Setup Events"""
    events = ["adb shell input keyevent BUTTON_A",
              "adb shell input keyevent DPAD_DOWN",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent DPAD_DOWN",
              "adb shell input keyevent BUTTON_A",
              "adb shell input text aakriti.nvidia",
              "adb shell input keyevent ENTER",
              "adb shell input text nvidia@1234",
              "adb shell input keyevent ENTER",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent BUTTON_A",
              "adb shell input keyevent BUTTON_A",
             ]
    boot_completed = "boot_completed"
    leanback_focus = "Displayed com.google.android.leanbacklauncher/.MainActivity"
    factory_reset_cmd = ['adb reboot-bootloader',
                         'fastboot erase userdata',
                         'fastboot erase cache',
                         'fastboot reboot']
    logcat = "adb shell logcat > log.txt"
    dmesg = "adb shell dmesg > dmesg.txt"
    log = "adb shell logcat -d > log1.txt"
    wait_device = "adb wait-for-device"

    def run_cmd(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        if p.returncode != 0:
            print "Error while running - %s" % cmd
            print error
        return output 

    def run_cmd_background(self, cmd):
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    def start_test(self, number):
        count = 1
        while count <= number:
            print "Cycle %d" % count
            self.run_cmd(self.wait_device)
            time.sleep(300)
            self.run_cmd(self.log)
            if not self.boot_completed in open("log1.txt").read():
                time.sleep(30)
                self.run_cmd(self.log)
            self.run_cmd_background(self.logcat)
            for event in self.events:
                self.run_cmd(event)
                time.sleep(5)
            print "Setup Complete..."
            self.run_cmd(self.log)
            if not self.leanback_focus in open("log1.txt").read():
                print "leanback is not in focus"
                self.run_cmd(self.dmesg)
                sys.exit(1)
            print "Leanback in focus..."
            for reset in self.factory_reset_cmd:
                print reset
                self.run_cmd(reset)
            count = count + 1
        

if __name__ == '__main__':
    t = Test()
    t.start_test(sys.argv[1])
