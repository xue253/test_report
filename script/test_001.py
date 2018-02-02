import pytest,allure
class Test_A():
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("第一条测试用例")
    def test_001(self):
        assert 1
    def test_002(self):
        assert 0