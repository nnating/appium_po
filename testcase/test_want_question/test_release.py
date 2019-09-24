# @Time     :2019/9/19 15:07
# @Author   :dengyuting
# @File     :test_release.py
import random

import pytest

from page.ability_page import AbilityPage
from page.want_question.question_page import QuestionPage


class TestRelease:

    def setup(self):
        self.ability = AbilityPage()

    @pytest.mark.parametrize('title,content',[("自动化测试标题"+str(random.randint(1,9999))+"","自动化测试内容"+str(random.randint(1,9999))+"")])
    def test_release_suc(self,title,content):
        self.ability.goto_question().click_dept().choice_deptname().input_title(title).input_content(content).click_Release()
        assert self.ability.goto_profile().goto_newmoderated().get_new_moderated_title() == title

    def test_voice(self):
        self.ability.goto_question().click_switchvoice().long_click_voice()
        assert "com.mmm.ability:id/tvDuration" in self.ability.driver.page_source

    #失败用例示范1
    def test_voice_1(self):
        self.ability.goto_question().click_switchvoice().long_click_voice()
        assert "com.mmm.ability:id/tvDuration" not in self.ability.driver.page_source

    @pytest.mark.skip("reason='跳过这条测试用例'")
    def test_voice_2(self):
        self.ability.goto_question().click_switchvoice().long_click_voice()
        assert "com.mmm.ability:id/tvDuration" not in self.ability.driver.page_source


