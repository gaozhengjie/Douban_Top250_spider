#!/usr/bin/env python3.x
# -*- coding: utf-8 -*-
# @Time     : 2017/7/17 18:59
# @Author   : GaoZhengjie
# @Contact  : gaozhengj@foxmail.com
# @Software : PyCharm

import os

# os.system("scrapy crawl douban")

from scrapy.cmdline import execute
execute("scrapy crawl douban".split())