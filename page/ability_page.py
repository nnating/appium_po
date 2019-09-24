# @Time     : 13:55
# @Author   :dengyuting
# @File     :.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.profile_account.profile_page import ProfilePage
from page.want_question.question_page import QuestionPage


class AbilityPage(BasePage):
    driver = None
    app = "com.mmm.ability"
    activity = ".ui.splash.SplashActivity"

    tvTabPwd = (By.ID,"com.mmm.ability:id/tvTabPwd")
    tvToLogin = (By.ID,"com.mmm.ability:id/tvToLogin")
    account = (By.ID,"com.mmm.ability:id/etAccount")
    password = (By.ID,"com.mmm.ability:id/etPwd")

    _ivSkip = (By.ID, "com.mmm.ability:id/ivSkip")
    _ivTitle = (By.ID,"com.mmm.ability:id/ivTitle")

    _iwantquestion = (By.ID,'lavWantToQuestion')
    _mine = (By.ID, 'com.mmm.ability:id/ivMine')

    def first_start(self,account_value,password_value):
    #def first_start(self, account_value="13559112967", password_value="123456"):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "New_Device_API_29"
        caps["appPackage"] = self.app
        caps["appActivity"] = self.activity
        caps["autoGrantPermissions"] = True
        caps["noreset"] = True
        #caps['automationName'] = 'Uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)



        self.click_element(self.tvTabPwd)
        self.input_text(self.account,account_value)
        self.input_text(self.password,password_value)
        self.click_element(self.tvToLogin)


        AbilityPage.driver = self.driver

    def __init__(self,account_value="13559112967",password_value="123456"):
        if AbilityPage.driver == None:
            self.first_start(account_value,password_value)
            self.click_element(self._ivSkip)
        else:
            print("======================launch app========================")
            self.driver.start_activity(self.app,self.activity)
        self.wait_element_visibility(self._ivTitle)
        #WebDriverWait(self.driver,60).until(expected_conditions.invisibility_of_element_located((MobileBy.ACCESSIBILITY_ID,'com.mmm.ability:id/ivTitle')))


    def goto_profile(self):
        self.click_element(self._mine)
        return ProfilePage(self.driver)

    def goto_question(self):
        self.click_element(self._iwantquestion)
        return QuestionPage(self.driver)



