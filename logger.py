# -*-coding=utf-8-*-
import logging
import datetime
from setting import llogger
def lloger():
    logging.basicConfig(
                        level=logging.DEBUG,
                        # format='%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] %(message)s',
                        # datefmt='%Y%m%d %H:%M:%S',
                        # filename=datetime.datetime.now().strftime("%Y-%m-%d") + '.log',
                        filemode='a')

    # 创建一个logger
    logger = logging.getLogger('mylogger')
    # logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(datetime.datetime.now().strftime("%Y-%m-%d") + '.log')
    # fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)

    # 定义handler的输出格式
    formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
    fh.setFormatter(formatter)
    # ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    # logger.addHandler(ch)

    return logger

f=llogger(__file__)
f.info('On the file')
