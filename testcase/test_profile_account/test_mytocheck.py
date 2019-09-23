# @Time     :2019/9/23 14:59
# @Author   :dengyuting
# @File     :test_mytocheck.py
from page.ability_page import AbilityPage


class TestMyToCheck:

    def setup(self):
        self.ability = AbilityPage("13559112966","123456")
        self.mycheckdetail = self.ability.goto_profile().goto_mycheck().goto_check_detail()

    def test_mycheck_suc(self):
        self.mycheckdetail.click_receiveque_yes()
        self.mycheckdetail.click_scoreinc()
        self.mycheckdetail.click_submit()
        assert "审核成功" in self.mycheckdetail.get_toast().text

    # def
