from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class Long_msg:
    msg_xpath='//android.widget.TextView[@text="Messages"]'
    start_chat_Xpath='//android.widget.Button[@content-desc="Start chat"]'
    Search_contact_xpath='//android.widget.EditText[@resource-id="ContactSearchField"]'
    confirm_contact_xpath='//android.view.View[@resource-id="GlideMonogram"]'
    text_area_xpath="//android.widget.EditText[@text='RCS message']"
    send_button_xpath='//android.widget.ImageView[@content-desc="Send end-to-end encrypted message"]'
    double_click_xpath='//android.widget.ImageView[@resource-id="com.google.android.apps.messaging:id/status_icon"]'



    def __init__(self,driver):
        self.driver=driver


    def open_Msg(self):
        self.driver.find_element(AppiumBy.XPATH,self.msg_xpath).click()

    def compose_msg(self):
        self.driver.find_element(AppiumBy.XPATH,self.start_chat_Xpath).click()

    def enter_number(self,number):
        self.driver.find_element(AppiumBy.XPATH,self.Search_contact_xpath).send_keys(number)
        sleep(2)
        self.driver.find_element(AppiumBy.XPATH,self.confirm_contact_xpath).click()

    def type_Msg(self,msg):
        self.driver.find_element(AppiumBy.XPATH, self.text_area_xpath).clear()
        self.driver.find_element(AppiumBy.XPATH,self.text_area_xpath).send_keys(msg)
        sleep(1)

    def send_Msg_Verify(self):
        self.driver.find_element(AppiumBy.XPATH,self.send_button_xpath).click()
        sleep(1)

