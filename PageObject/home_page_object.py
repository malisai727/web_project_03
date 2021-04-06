from common.basepage import BasePage
from PageLocators.home_page_locator import HomePageLocator


class HomePageObject(BasePage):

    def check_username_exist(self):
        try:
            self.wait_loc_visible(HomePageLocator.my_account,'主页_检查用户名存在')
            return True
        except:
            return False
