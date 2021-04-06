from selenium.webdriver.remote.webdriver import WebDriver
from common.basepage import BasePage
from PageLocators.login_page_locator import LoginPageLocator as loc

class LoginPageObject(BasePage):

    #登录
    def login(self,username,passwd):
        self.input_value(loc=loc.user_loc,value=username,img_discription='登录页面_输入用户名')
        self.input_value(loc=loc.passwd_loc,value=passwd,img_discription='登录页面_输入密码')
        self.click_element(loc=loc.login_button_loc,img_discription='登录页面_点击登录按钮')

    #获取表单错误提示信息
    def get_form_error_info(self):
        return self.get_text(loc=loc.login_error_loc,img_discription='登录页面_获取登录表单错误提示信息')

    #获取页面中间的错误提示信息
    def get_page_center_error_info(self):
        return self.get_text(loc=loc.login_center_error_loc,img_discription='登录页面_获取页面中间错误提示信息')