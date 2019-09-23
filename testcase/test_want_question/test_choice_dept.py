# @Time     :2019/9/19 15:27
# @Author   :dengyuting
# @File     :test_choice_dept.py
import pytest

from page.ability_page import AbilityPage


class TestChoiceDept:

    def setup(self):
        self.ability = AbilityPage()

    def test_choice_dept_1(self):
        assert "研发部" in self.ability.goto_question().click_dept().choice_deptname().get_deptname()

    def test_choice_dept_2(self):
        assert "测试部1" not in self.ability.goto_question().click_dept().choice_deptname().get_deptname()
    #
    # def test_choice_dept_3(self):
    #     assert "测试部111" not in self.ability.goto_question().click_dept().choice_deptname().get_deptname()

    # def teardown(self):
    #     self.ability.goto_question().click_back()

