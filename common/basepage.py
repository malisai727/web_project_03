import logging
import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.dir_contents import IMAGE_DIR

class BasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    #截图
    def save_image(self,img_discription):
        '''
        :param img_discription:图片的描述：页面名称_功能名称
        :return:
        '''
        time_stamp = time.strftime("%Y-%m-%d %H %M %S")
        image_name = f'{img_discription}{time_stamp}.png'
        image_path = os.path.join(IMAGE_DIR,image_name)
        try:
            self.driver.save_screenshot(image_path)
        except:
            logging.exception('当前网页截图保存失败')
        else:
            logging.info(f'截图成功，截图存放在{image_path}')

    #等待元素可见
    def wait_loc_visible(self,loc,img_discription,timeout=20,frequence=0.5):
        start_time = datetime.datetime.now()
        try:
            WebDriverWait(self.driver,timeout,frequence).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception(f'等待元素{loc}可见失败！')
            #截图
            self.save_image(img_discription)
            raise
        else:
            end_time = datetime.datetime.now()
            logging.info(f'等待{img_discription}元素{loc}可见成功，耗时{end_time - start_time}')

    #等待元素存在
    def wait_loc_presence(self,loc,img_discription,timeout=20,frequence=0.5):
        start_time = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequence).until(EC.presence_of_element_located(loc))
        except:
            logging.exception(f'等待元素{loc}存在失败！')
            # 截图
            self.save_image(img_discription)
            raise
        else:
            end_time = datetime.datetime.now()
            logging.info(f'等待{img_discription}元素{loc}存在成功，耗时{end_time - start_time}')

    #查找元素
    def get_element(self,loc,img_discription):
        try:
            ele = self.driver.find_element(*loc)
        except:
            logging.exception(f'查找{img_discription}元素{loc}失败!')
            self.save_image(img_discription)
            raise
        else:
            logging.info(f'查找{img_discription}元素{loc}成功！')
            return ele

    #点击对象
    def click_element(self,loc,img_discription,timeout=20,frequence=0.5):
        #等待元素可见
        self.wait_loc_visible(loc,img_discription,timeout,frequence)
        #查找元素
        ele = self.get_element(loc,img_discription)
        #操作
        try:
            ele.click()
        except:
            logging.exception(f'点击{img_discription}元素{loc}失败!')
            self.save_image(img_discription)
            raise
        else:
            logging.info(f'点击{img_discription}元素{loc}成功!')

    #输入值
    def input_value(self,loc,value,img_discription,timeout=20,frequence=0.5):
        #等待元素可见
        self.wait_loc_visible(loc,img_discription,timeout,frequence)
        #查找元素
        ele = self.get_element(loc,img_discription)
        #操作
        try:
            ele.send_keys(value)
        except:
            logging.exception(f'在{img_discription}元素{loc}上输入文本{value}失败！')
            self.save_image(img_discription)
            raise
        else:
            logging.exception(f'在{img_discription}元素{loc}上输入文本{value}成功！')

    #获取元素文本值
    def get_text(self,loc,img_discription,timeout=20,frequence=0.5):
        #等待元素可见
        self.wait_loc_visible(loc,img_discription,timeout,frequence)
        #查找元素
        ele = self.get_element(loc,img_discription)
        #获取文本值
        try:
            text = ele.text
        except:
            logging.exception(f'获取{img_discription}元素{loc}文本失败！')
            self.save_image(img_discription)
            raise
        else:
            logging.exception(f'获取{img_discription}元素{loc}文本成功！')
            return text


    #alert切换

    #上传

    #下拉列表

    #window切换

    




