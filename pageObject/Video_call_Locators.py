from appium.webdriver.common.appiumby import AppiumBy
from time import sleep



class video_call_Locator:
    number = "+919653184217"
    repeat = 3


    phn_dialer_xpath='//android.widget.TextView[@content-desc="Phone"]'
    recent_btn_xpath='//android.view.View[@resource-id="com.google.android.dialer:id/navigation_bar_item_active_indicator_view"]'
    keypad_xpath='//android.widget.ImageButton[@content-desc="key pad"]'
    textarea_num_xpath='//android.widget.EditText[@resource-id="com.google.android.dialer:id/digits"]'
    video_call_xpath='//android.widget.TextView[@resource-id="com.google.android.dialer:id/search_action_text" and @text="Video call"]'
    # for Iteration 50 times
    Video_End_button = '//android.widget.ImageButton[@content-desc="End call"]'
    Audio_End_button = '//android.widget.Button[@content-desc="End call"]'
    call_timer_xpath='//android.widget.Chronometer[@resource-id="com.google.android.dialer:id/contactgrid_bottom_timer"]'
    video_call_btn_number='//android.widget.ImageView[@resource-id="com.google.android.dialer:id/call_button"]'



    def __init__(self,driver,driver2):
        self.driver=driver
        self.driver2=driver2



    def Open_phn_dialer(self):
        self.driver.find_element(AppiumBy.XPATH, self.phn_dialer_xpath).click()
        sleep(1)

    def press_dial_pad(self):
        self.driver.find_element(AppiumBy.XPATH, self.recent_btn_xpath).click()
        sleep(1)
        self.driver.find_element(AppiumBy.XPATH, self.keypad_xpath).click()
        sleep(1)

    def enterNumber(self):
        self.driver.find_element(AppiumBy.XPATH,self.textarea_num_xpath).send_keys(self.number)
        sleep(1)



    def click_video_call(self,start_x,start_y,end_x,end_y ):
        self.driver.swipe(start_x, start_y, end_x, end_y)
        sleep(1)

    def Recieve_call(self):
        self.driver2.tap([(893, 494)])
        sleep(1)

















