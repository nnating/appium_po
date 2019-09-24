# @Time     :2019/9/20 16:31
# @Author   :dengyuting
# @File     :base_page.py
import os
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.log import MyLog


class BasePage:

    black_list = [(By.ID,"com.mmm.ability:id/ivSkip"),]
    max = 0

    def __init__(self,driver:WebDriver):
        self.driver = driver

    # def find_blacklist(self,locator) -> WebElement:
    #     try:
    #         return self.driver.find_element(*locator)
    #     except Exception:
    #         if BasePage.max >10:
    #             raise Exception
    #         BasePage.max = BasePage.max+1
    #         for black in self.black_list:
    #             elements = self.driver.find_element(*black)
    #             print(elements)
    #             if len(elements) >=1:
    #                 print(elements[0])
    #                 elements[0].click()
    #         return self.find(locator)

    #等待元素出现
    def wait_element_visibility(self, locator) -> WebElement:
        MyLog.info("等待元素：{}".format(locator))
        try:
            element = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(locator))
            return element
        except Exception as e:
            MyLog.error("等待元素：{}超时".format(locator))
            self.save_image()
            raise e

    #点击元素
    def click_element(self,locator):
        element = self.wait_element_visibility(locator)
        try:
            MyLog.info("点击元素：{}".format(locator))
            element.click()
        except Exception as e:
            MyLog.error("点击元素：{}失败".format(locator))
            self.save_image()
            raise e

    #输入数据
    def input_text(self,locator,value):
        element = self.wait_element_visibility(locator)
        try:
            MyLog.info("点击：{}，输入：{}".format(locator, value))
            element.send_keys(value)
        except Exception as e:
            MyLog.error("输入数据：{}失败".format(value))
            self.save_image()
            raise e

    #获取元素文本内容，主要用来做断言
    def get_element_text(self,locator):
        element = self.wait_element_visibility(locator)
        try:
            MyLog.info("获取：{}元素文本：{}".format(locator,element.text))
            return element.text
        except Exception as e:
            MyLog.error("获取元素文本：{}失败".format(element.text))
            self.save_image()
            raise e

    def size(self,locator) -> int:
        return len(self.driver.find_elements(*locator))

    @classmethod
    def id_locator(cls, locator):
        return (By.ID,locator)

    @classmethod
    def text_locator(cls, locator):
        return (By.XPATH, "//*[@text='%s']" %locator)

    #@classmethod
    def get_toast_msg(self,locator):
        #return (By.XPATH, "//*[@class='android.widget.Toast']")
        #return (By.XPATH, "//*[@text='审核成功']")
        toast_msg = self.wait_element_visibility(locator)
        try:
            MyLog.info("获取toast元素：{}，文本：{}".format(locator, toast_msg.text))
            return toast_msg.text
        except Exception as e:
            MyLog.error("获取toast元素文本：{}失败".format(toast_msg.text))
            self.save_image()
            raise e

    def save_image(self):
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            screenshot_dir = os.path.join(base_dir, "image")
            screenshot_img = os.path.join(screenshot_dir, str(int(time.time())) + ".png")
            self.driver.get_screenshot_as_file(screenshot_img)
            MyLog.info('保存截图至:{}'.format(screenshot_img))
        except NameError as e:
            MyLog.info('保存截图失败：%s' % e)
            self.save_image()
        return screenshot_img



    #滚动查找点击
    def scroll_text_click(self,text_value):
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("'+text_value+'").instance(0));').click()
        MyLog.info("找到text:{}".format(text_value))

    #长按
    def long_click(self,locator):
        action = TouchAction(self.driver)
        element = self.wait_element_visibility(locator)
        try:
            MyLog.info("长按：{}元素".format(locator))
            action.long_press(element).wait(10000).perform()
        except Exception as e:
            MyLog.error("长按元素：{}失败".format(locator))
            self.save_image()
            raise e

    def swipe_locator(self):
        self.height = self.driver.get_window_size()['height']
        self.width = self.driver.get_window_size()['width']
        for i in range(5):
            self.driver.swipe(self.width*0.8, self.height*0.9, self.width*0.2, self.height*0.1, 1000)




