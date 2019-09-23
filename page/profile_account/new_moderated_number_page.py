# @Time     :2019/9/23 10:27
# @Author   :dengyuting
# @File     :new_moderated_number_page.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class NewModeratedNumberPage(BasePage):

    _new_moderated_title = (By.XPATH,"(//*[@resource-id='com.mmm.ability:id/tvQueTitle'])[1]")

    def get_new_moderated_title(self):
        new_moderated_title = self.get_element_text(self._new_moderated_title)
        return new_moderated_title