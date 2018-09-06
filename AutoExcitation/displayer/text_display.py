# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/2 14:10

import os
import win32api
import win32con


class Texter(object):

    def en_display(self):
        pass

    def zh_display(self):
        pass

    def full_display(self):
        data = []
        JSON_PATH = os.path.abspath(os.path.join(os.getcwd(), r".\resource.json"))
        with open(JSON_PATH, 'r+', encoding='utf-8') as fr:
            cont_old = fr.readlines()
            if len(cont_old) == 0:
                data.append("{'en': 'No More sentence.', 'zh': '没有更多的句子了，好好学习天天向上吧！'}\n")
            else:
                data.append(cont_old.pop())
                fr.seek(0)
                fr.truncate()
                cont_new = data + cont_old
                for item in cont_new:
                    fr.write(item)
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
