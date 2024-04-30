from appium.webdriver.common.appiumby import AppiumBy

class audio_Call:
    phn_dialer_xpath = '//android.widget.TextView[@content-desc="Phone"]'
    recent_btn_xpath = '//android.view.View[@resource-id="com.google.android.dialer:id/navigation_bar_item_active_indicator_view"]'
    keypad_xpath = '//android.widget.ImageButton[@content-desc="key pad"]'
    textarea_num_xpath = '//android.widget.EditText[@resource-id="com.google.android.dialer:id/digits"]'
    Call_btn_xpath='//android.widget.Button[@content-desc="dial"]'
    Num_call_btn_xp='//android.widget.ImageView[@resource-id="com.google.android.dialer:id/call_button"]'
    Audio_End_button = '//android.widget.Button[@content-desc="End call"]'
    call_timer_xpath = '//android.widget.Chronometer[@resource-id="com.google.android.dialer:id/contactgrid_bottom_timer"]'



    def __init__(self,driver,driver2):
        self.driver=driver
        self.driver2=driver2


    def open_phn_dialer(self):
        self.driver.find_element(AppiumBy.XPATH,self.phn_dialer_xpath).click()
        self.driver.find_element(AppiumBy.XPATH, self.recent_btn_xpath).click()

    def click_dialpad(self):
        self.driver.find_element(AppiumBy.XPATH, self.keypad_xpath).click()


    def Enter_number(self,number):
        self.driver.find_element(AppiumBy.XPATH, self.textarea_num_xpath).send_keys(number)

    def make_call(self):
        self.driver.find_element(AppiumBy.XPATH, self.Call_btn_xpath).click()


    def Recieve_call(self):
        self.driver2.tap([(893, 494)])


