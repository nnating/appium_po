# @Time     :2019/9/23 14:44
# @Author   :dengyuting
# @File     :mycheck_page.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.profile_account.checkdetail_page import CheckDetailPage


class MyCheckPage(BasePage):

    _needcheck = (By.XPATH,"(//*[@resource-id='com.mmm.ability:id/tvQueTitle'])[1]")
    _back = (By.ID,"com.mmm.ability:id/ivBack")

    def goto_check_detail(self):
        self.click_element(self._needcheck)
        return CheckDetailPage(self.driver)

