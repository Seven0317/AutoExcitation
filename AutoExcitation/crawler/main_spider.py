# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/2 13:56

from crawler import downloader
from crawler import outputer
from log import setup_logging
import threading
import logging
import os


setup_logging(default_path=os.path.join(os.getcwd(), r".\log.yaml"))
logger = logging.getLogger("fileLogger")


class MainSpider(object):
    """
    定义一个数据爬取器
    """

    def __init__(self, url=None, count=0):
        # 初始化下载地址
        self.url = url
        # 初始化爬取数据总数
        self.count = count
        # 初始化下载器
        self.downloader = downloader.Downloader()
        # 初始化输出器
        self.outputer = outputer.Outputer()

    def crawl(self):
        # 爬取数据并存入datas字典中
        datas = self.downloader.download(self.url, self.count)
        # 提取datas数据并保存在json文件中
        self.outputer.output(datas)


# Design a timer for crawling data
def spider():
    def fun_spide():
        try:
            obj_spider = MainSpider(url="http://www.iciba.com", count=1)
            logging.info("Initialize web driver(chrome) successfully.")
        except Exception as e:
            logging.error(e)
            logging.error(r"Initialize web driver(chrome) failed.\nCannot update data and only refresh text with data in resource file.")
        # 调用爬取方法
        obj_spider.crawl()
        # Crawl data every 8 hours
        timer = threading.Timer(60 * 60 * 8, fun_spide)
        timer.start()
    # Crawl data after 10s from initialising the app
    timer = threading.Timer(10, fun_spide)
    timer.start()


# Remember to modify related path of resource.json, log.yaml if run module directly
if __name__ == '__main__':
    # spider()
    obj_spider = MainSpider(url="http://www.iciba.com", count=100)
    # 调用爬取方法
    obj_spider.crawl()
