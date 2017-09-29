#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhangjinsi'
import requests
from bs4 import BeautifulSoup


start_url = 'http://km.58.com/sale.shtml'
url_host = 'http://km.58.com'

def get_channel_urls(url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = url_host + link.get('href')
        print page_url

#get_channel_urls(start_url)

channel_list = '''
    http://km.58.com/shouji/
    http://km.58.com/tongxunyw/
    http://km.58.com/danche/
    http://km.58.com/diandongche/
    http://km.58.com/fzixingche/
    http://km.58.com/sanlunche/
    http://km.58.com/peijianzhuangbei/
    http://km.58.com/diannao/
    http://km.58.com/bijiben/
    http://km.58.com/pbdn/
    http://km.58.com/diannaopeijian/
    http://km.58.com/zhoubianshebei/
    http://km.58.com/shuma/
    http://km.58.com/shumaxiangji/
    http://km.58.com/mpsanmpsi/
    http://km.58.com/youxiji/
    http://km.58.com/ershoukongtiao/
    http://km.58.com/dianshiji/
    http://km.58.com/xiyiji/
    http://km.58.com/bingxiang/
    http://km.58.com/jiadian/
    http://km.58.com/binggui/
    http://km.58.com/chuang/
    http://km.58.com/ershoujiaju/
    http://km.58.com/yingyou/
    http://km.58.com/yingeryongpin/
    http://km.58.com/muyingweiyang/
    http://km.58.com/muyingtongchuang/
    http://km.58.com/yunfuyongpin/
    http://km.58.com/fushi/
    http://km.58.com/nanzhuang/
    http://km.58.com/fsxiemao/
    http://km.58.com/xiangbao/
    http://km.58.com/meirong/
    http://km.58.com/yishu/
    http://km.58.com/shufahuihua/
    http://km.58.com/zhubaoshipin/
    http://km.58.com/yuqi/
    http://km.58.com/tushu/
    http://km.58.com/tushubook/
    http://km.58.com/wenti/
    http://km.58.com/yundongfushi/
    http://km.58.com/jianshenqixie/
    http://km.58.com/huju/
    http://km.58.com/qiulei/
    http://km.58.com/yueqi/
    http://km.58.com/bangongshebei/
    http://km.58.com/diannaohaocai/
    http://km.58.com/bangongjiaju/
    http://km.58.com/ershoushebei/
    http://km.58.com/chengren/
    http://km.58.com/nvyongpin/
    http://km.58.com/qinglvqingqu/
    http://km.58.com/qingquneiyi/
    http://km.58.com/chengren/
    http://km.58.com/xiaoyuan/
    http://km.58.com/ershouqiugou/
    http://km.58.com/tiaozao/
    http://km.58.com/tiaozao/
    http://km.58.com/tiaozao/
'''
