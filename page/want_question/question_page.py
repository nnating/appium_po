# @Time     :${date} 14:59
# @Author   :dengyuting
# @File     :${name}.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage


class QuestionPage(BasePage):

    _adddept = (By.ID,"tvAddDept")
    _choicedeptname = (By.XPATH,"//*[@text='研发部']")
    _deptname = (By.ID,"tvDeptName")
    _title = (By.ID,"etQueTitle")
    _content = (By.ID,"etQueContent")
    _release = (By.ID,"tvRelease")
    _voice = (By.XPATH,"//*[@text='按住说话']")
    _switchvoice = (By.ID,"com.mmm.ability:id/llSwitchVoice")
    _duration_voice =(By.ID,"com.mmm.ability:id/tvDuration")

    def __init__(self, driver:WebDriver):
        self.driver = driver

    #点击问题相关部门
    def click_dept(self):
        self.click_element(self._adddept)
        return self

    #选择部门
    def choice_deptname(self):
        self.click_element(self._choicedeptname)
        return self

    #做断言，判断所选择的部门名字
    def get_deptname(self):
        deptname = self.get_element_text(self._deptname)
        return deptname


    #输入标题
    def input_title(self,title_value):
        self.input_text(self._title,title_value)
        return self

    #输入内容
    def input_content(self,content_value):
        self.input_text(self._content,content_value)
        return self

    #点击发布
    def click_Release(self):
        self.click_element(self._release)
        return self

    #切换语音模式
    def click_switchvoice(self):
        self.click_element(self._switchvoice)
        return self

    #长按“按住说话”
    def long_click_voice(self):
        self.long_click(self._voice)

    # def click_back(self):
    #     sleep(3)
    #     self.driver.find_element_by_id("com.mmm.ability:id/ivBack").click()