# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/3 14:38

import os
import logging
from log import setup_logging
from crawler.main_spider import spider
from displayer.main_window import display, app

# Set up logger by log.yaml
setup_logging(default_path=os.path.join(os.getcwd(), r"log.yaml"))
logger = logging.getLogger("fileLogger")

# Init app
try:
    App = app
    logger.info("Initialise app successfully.")
except Exception as e:
    logger.error(e)
    logger.error("Initialise app failed")

# Crawl data
try:
    spider()
except Exception as e:
    logger.error(e)
    logger.error("Crawl data failed.")

# Display text
try:
    display()
except Exception as e:
    logger.error(e)
    logger.error("Display text failed.")
