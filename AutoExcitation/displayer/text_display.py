# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/2 14:10

import os
import time
import win32api
import win32con
import logging
from log import setup_logging

setup_logging(default_path=os.path.join(os.getcwd(), r".\log.yaml"))
logger = logging.getLogger("fileLogger")


class Texter(object):

    def en_display(self):
        pass

    def zh_display(self):
        pass

    def full_display(self):
        data = []
        # 检查文件锁是否存在
        LOCK_PATH = os.path.abspath(os.path.join(os.getcwd(), r".\lock.txt"))
        # 如果存在就循环等待5秒判断一次，不存在就跳出等待
        while True:
            if not os.path.exists(LOCK_PATH):
                break
            else:
                logging.info("Waiting before reading.")
                time.sleep(5)
        JSON_PATH = os.path.abspath(os.path.join(os.getcwd(), r".\resource.json"))
        with open(JSON_PATH, 'r+', encoding='utf-8') as fr:
            logging.info("Read form resource.json.")
            cont_old = fr.readlines()
            if len(cont_old) == 0:
                data.append("{'en': 'No More sentence.', 'zh': '没有更多的句子了，好好学习天天向上吧！'}\n")
            else:
                data.append(cont_old.pop())
                logging.info("Pop data from resource.json.")
                fr.seek(0)
                fr.truncate()
                logging.info("Delete all data left in resource.json.")
                cont_new = data + cont_old
                for item in cont_new:
                    fr.write(item)
                logging.info("Update data of resource.json.")
        text = eval((data[0].strip()))
        en_text = text['en']
        zh_text = text['zh']
        full_text = (en_text + '\n' + zh_text)
        return full_text

    def location_display(self):
        # 获取屏幕长
        screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        # 获取屏幕宽
        screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        # 设置文本标签位置坐标
        text_x = screen_x * 0.5
        text_y = screen_y * 0.005
        return text_x, text_y
