# @Time     :${date} 14:58
# @Author   :dengyuting
# @File     :${name}.py
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.profile_account.mycheck_page import MyCheckPage

from page.profile_account.newmoderated_page import NewModeratedNumberPage


class ProfilePage(BasePage):

    _NewModeratedNumber = (By.ID,"com.mmm.ability:id/tvNewModeratedNumber")
    _mycheck = (By.ID, "com.mmm.ability:id/clMyToCheck")
    #_mytochecknum = (By.ID,"com.mmm.ability:id/tvMyToCheckNumber")

    def goto_newmoderated(self):
        self.click_element(self._NewModeratedNumber)
        return NewModeratedNumberPage(self.driver)

    def goto_mycheck(self):
        self.click_element(self._mycheck)
        return MyCheckPage(self.driver)




