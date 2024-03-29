# @Time     :2019/9/23 14:54
# @Author   :dengyuting
# @File     :checkdetail_page.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class CheckDetailPage(BasePage):
    _receiveque_yes = (By.ID,"com.mmm.ability:id/tvYes")
    _submit = (By.ID,"com.mmm.ability:id/tvSubmit")
    _scoreincrease = (By.ID,"com.mmm.ability:id/ivScoreIncrease")
    _mycheck_toast = (By.XPATH, "//*[contains(@text,'审核成功')]")

    def click_receiveque_yes(self):
        self.click_element(self._receiveque_yes)

    def click_submit(self):
        self.click_element(self._submit)

    def click_scoreinc(self):
        self.swipe_locator()
        self.click_element(self._scoreincrease)

    def get_toast(self):
        mycheck_toast = self.get_toast_msg(self._mycheck_toast)
        return mycheck_toast