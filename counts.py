#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhangjinsi'

import time

from page_parsing import url_list


while True:
    print url_list.find().count()
    time.sleep(5)