import pytest
from selenium import webdriver
from TestDatas import common_datas,login_datas
from PageObject.login_page_object import LoginPageObject
from PageObject.home_page_object import HomePageObject


@pytest.mark.login
@pytest.mark.usefixtures('init_driver')
class TestLogin():

    #登录成功
    def test_login_success(self,init_driver):
        LoginPageObject(init_driver).login(login_datas.success['user'],login_datas.success['passwd'])
        assert HomePageObject(init_driver).check_username_exist()
        assert init_driver.current_url == login_datas.success['check']

    #密码为空/手机号为空/手机号格式错误
    @pytest.mark.smoke
    @pytest.mark.parametrize('data',login_datas.invalid_datas)
    def test_login_none_password(self,init_driver,data):
        lp_obj = LoginPageObject(init_driver)
        lp_obj.login(data['user'], data['passwd'])
        assert data['check'] == lp_obj.get_form_error_info()

    #手机号未注册/账号密码错误
    @pytest.mark.slow
    @pytest.mark.parametrize('data',login_datas.invalid_2_datas)
    def test_login_wrong_password(self,init_driver,data):
        lp_obj = LoginPageObject(init_driver)
        lp_obj.login(data['user'],data['passwd'])
        assert data['check'] == lp_obj.get_page_center_error_info()