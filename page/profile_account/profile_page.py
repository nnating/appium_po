# @Time     :${date} 14:58
# @Author   :dengyuting
# @File     :${name}.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.profile_account.new_moderated_number_page import NewModeratedNumberPage


class ProfilePage(BasePage):

    _NewModeratedNumber = (By.ID,"com.mmm.ability:id/tvNewModeratedNumber")
    _mytocheck = (By.ID, "com.mmm.ability:id/clMyToCheck")
    _mytochecknum = (By.ID,"com.mmm.ability:id/tvMyToCheckNumber")

    def goto_new_moderated_number_page(self):
        self.click_element(self._NewModeratedNumber)
        return NewModeratedNumberPage(self.driver)




