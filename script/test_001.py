import pytest,allure
class Test_A():
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("第一条测试用例")
    @allure.attach("描述","判断正确")
    def test_001(self):
        assert 1