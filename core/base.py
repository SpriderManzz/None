# coding=utf8

import os
import time
import configparser


cf = configparser.ConfigParser()


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()

    def forward(self):
        """
        浏览器前进
        :return:
        """
        self.driver.forward()

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()

    def wait(self, seconds):
        """
        浏览器等待
        :param seconds:
        :return:
        """
        self.driver.implicitly_wait(seconds)

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.close()

    def get_page_img(self):
        """
        下载图片
        :return:
        """
        current_path = os.path.abspath('..')
        img_path = os.path.join(current_path, 'screenshots')
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        screen_name = os.path.join(img_path, str(time.time()) + '.png')
        self.driver.get_screenshot_as_file(screen_name)

    def open_browser(self):
        current_path = os.path.abspath('.')
        conf_path = os.path.join(current_path, 'config.conf')
        cf.read(conf_path)
        url = cf.get("url", "url")
        self.driver.get(url)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        return self.driver


