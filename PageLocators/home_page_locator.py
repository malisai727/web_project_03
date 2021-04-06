from selenium.webdriver.common.by import By

class HomePageLocator():
    #我的账户
    my_account = (By.XPATH,'//a[contains(text(),"我的帐户")]')