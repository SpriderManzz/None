# coding=utf-8

import os
import time
import unittest
import configparser
from selenium import webdriver
from core.base import Base
from demo.baidu_page import BaiduPage
cf = configparser.ConfigParser()

current_path = os.path.abspath('.')
conf_path = os.path.join(current_path, 'config.conf')
cf.read(conf_path)


class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

        # 相当于 webdriver.Chrome()
        web_driver = getattr(webdriver, cf.get("browser_type", "browser_name"))()
        browse = Base(web_driver)
        cls.driver = browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = BaiduPage(self.driver)
        homepage.search_thing("//input[@id='kw']", 'selenium')
        homepage.click_button("//input[@id='su']")
        time.sleep(2)
        homepage.get_page_img()
