# @Time     :2019/9/23 11:52
# @Author   :dengyuting
# @File     :index_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from appium_po.page.base_page import BasePage


class IndexPage(BasePage):

    _ivTitle = (By.ID, "com.mmm.ability:id/ivTitle")

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def get_title(self):
        title = self.get_element_text(self._ivTitle)
        return title