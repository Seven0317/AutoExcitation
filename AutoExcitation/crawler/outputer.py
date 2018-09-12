# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/2 13:59

from log import setup_logging
import logging
import os


setup_logging(default_path=os.path.join(os.getcwd(), r".\log.yaml"))
logger = logging.getLogger("fileLogger")


class Outputer(object):
    """
    定义一个输出器
    """
    def output(self, datas):
        # 如果爬取的内容为空则返回空
        if datas == []:
            logger.info("Crawled data is none.")
            return
        # 否则按照下面定义格式输出到目标文件中
        try:
            # 创建文件锁
            LOCK_PATH = os.path.abspath(os.path.join(os.getcwd(), r".\lock.txt"))
            logging.info("Create a lock file.")
            with open(LOCK_PATH, 'a', encoding='utf-8') as fa:
                fa.write("I am a lock")
            # 循环将爬取数据追加写入目标文件中
            JSON_PATH = os.path.abspath(os.path.join(os.getcwd(), r".\resource.json"))
            l = []

            with open(JSON_PATH, 'r+', encoding='utf-8') as frw:
                for item in frw.readlines():
                    l.append(item.strip('\n'))
                for data in datas:
                    if str(data) in l:
                        logger.info("Crawled data was already in resource.json.")
                        pass
                    else:
                        frw.write(str(data))
                        frw.write('\n')
                        logger.info("Crawled data is stored in resource.json.")
            # 释放文件锁
            os.remove(LOCK_PATH)
            logging.info("Delete file for locking.")
        except Exception as e:
            logger.error(e)
            logger.error("Output text failed.")

