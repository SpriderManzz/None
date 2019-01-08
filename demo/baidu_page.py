# coding=utf8

from core.base import Base


class BaiduPage(Base):
    def search_thing(self, xpath, text):
        ele = self.driver.find_element_by_xpath(xpath)
        ele.clear()
        ele.send_keys(text)

    def click_button(self, xpath):
        ele = self.driver.find_element_by_xpath(xpath)
        ele.click()
