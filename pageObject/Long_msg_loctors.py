from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from utilities.common_function import Common_methods
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Long_msg:


    profie_AND_UI='new UiSelector().resourceId("com.google.android.apps.messaging:id/og_apd_internal_image_view")'
    msg_setting_AND_UI='new UiSelector().text("Messages settings")'
    Advance_AND_UI='new UiSelector().text("Advanced")'
    fourth_toggle = '(//android.widget.Switch[@resource-id="com.google.android.apps.messaging:id/switchWidget"])[4]'
    second_toggle='(//android.widget.Switch[@resource-id="com.google.android.apps.messaging:id/switchWidget"])[2]'

    #two simcard
    general_AND_UI='new UiSelector().text("General")'
    sim1_AND_UI='new UiSelector().text("SIM1")'
    sim2_And_UI='new UiSelector().text("SIM2")'
    txtSim1_xp="//android.widget.EditText[@text='Text (SIM1)']"
    RcsSim1_xp="//android.widget.EditText[@text='RCS (SIM1)']"

    msg_xpath='//android.widget.TextView[@text="Messages"]'
    start_chat_Xpath='//android.widget.Button[@content-desc="Start chat"]'
    Search_contact_xpath='//android.widget.EditText[@resource-id="ContactSearchField"]'
    confirm_contact_xpath='//android.view.View[@resource-id="GlideMonogram"]'


    RCS_CHAT_xp='//android.widget.TextView[@text="RCS chats"]'
    RCS_area_xpath="//android.widget.EditText[@text='RCS message']"
    RCS_send_btn_xpath='//android.widget.ImageView[@content-desc="Send end-to-end encrypted message"]'
    RCS_send2_xpath='//android.view.View[@resource-id="Compose:Draft:Send"]/android.widget.Button'
    RCS_toggle_AND_UI='new UiSelector().resourceId("com.google.android.apps.messaging:id/switchWidget").instance(0)'
    RCS_Status_xp='//android.widget.TextView[@text="Status: Connected"]'

    double_click_xpath='//android.widget.ImageView[@resource-id="com.google.android.apps.messaging:id/status_icon"]'
    double_click2_xpath='//android.view.View[@resource-id="message_list"]/android.view.View[1]/android.view.View[2]'

    txt_area_xp="//android.widget.EditText[@text='Text message']"
    txt_send_btn_AND_UI='new UiSelector().description("Send SMS")'



    def __init__(self,driver):
        self.driver=driver

    def check_4_toggle(self):
        toggle = self.driver.find_element(AppiumBy.XPATH, self.fourth_toggle)
        toggle_state = toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")

    def check_2_toggle(self):
        toggle = self.driver.find_element(AppiumBy.XPATH, self.second_toggle)
        toggle_state = toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")

    def RCS_toggle(self):
        toggle = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.RCS_toggle_AND_UI)
        toggle_state = toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")

    def open_Msg(self):
        self.driver.find_element(AppiumBy.XPATH,self.msg_xpath).click()
        sleep(1)




    def test_RCS_ststus_delivery_report(self):

        self.com_obj=Common_methods(self.driver)
        self.open_Msg()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.profie_AND_UI).click()
        sleep(2)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.msg_setting_AND_UI).click()
        sleep(1)
        try:
            if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.general_AND_UI).is_displayed():
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.general_AND_UI).click()

                self.driver.find_element(AppiumBy.XPATH,self.RCS_CHAT_xp).click()
                sleep(2)
                self.RCS_toggle()
        except:
            self.driver.find_element(AppiumBy.XPATH, self.RCS_CHAT_xp).click()
            sleep(2)
            self.RCS_toggle()
        wait=WebDriverWait(self.driver,120)

        try:
            wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.RCS_Status_xp)))
            if self.driver.find_element(AppiumBy.XPATH,self.RCS_Status_xp).is_displayed():
                print("RCS is ON")
                self.driver.back()
                sleep(2)
        except:
            print("RCS is NOT on")
            self.driver.back()
            sleep(2)


        self.com_obj.swipe_DOWN()
        sleep(2)
        try:
            if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.Advance_AND_UI).is_displayed():
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.Advance_AND_UI).click()
                sleep(1)
                try:
                    self.check_4_toggle()
                    self.driver.back()
                except:
                    self.check_2_toggle()
                    self.driver.back()
        except:

            self.driver.back()
            try:
                if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.sim1_AND_UI).is_displayed():
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.sim1_AND_UI).click()
                    sleep(1)
                    self.check_4_toggle()
                    self.driver.back()
                    sleep(1)
                if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.sim2_And_UI).is_displayed():
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.sim2_And_UI).click()
                    sleep(1)
                    self.check_4_toggle()
                    self.driver.back()

            except:
                print("sim not present")
                pass



        sleep(1)
        self.driver.back()





    def compose_msg(self):
        self.driver.find_element(AppiumBy.XPATH,self.start_chat_Xpath).click()
        sleep(1)

    def enter_number(self,number):
        self.driver.find_element(AppiumBy.XPATH,self.Search_contact_xpath).send_keys(number)
        sleep(2)
        self.driver.find_element(AppiumBy.XPATH,self.confirm_contact_xpath).click()
        sleep(1)

    def type_Msg(self,msg):
        try:
            #print("looking for RCS")
            if self.driver.find_element(AppiumBy.XPATH, self.RCS_area_xpath).is_displayed():
                self.driver.find_element(AppiumBy.XPATH, self.RCS_area_xpath).send_keys(msg)
                sleep(1)
                self.driver.find_element(AppiumBy.XPATH, self.RCS_send_btn_xpath).click()
                print("msg send")
        except:
            #print("looking for txt")
            try:
                if self.driver.find_element(AppiumBy.XPATH, self.txt_area_xp).is_displayed():
                    self.driver.find_element(AppiumBy.XPATH, self.txt_area_xp).send_keys(msg)
                    sleep(1)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.txt_send_btn_AND_UI).click()
            except:

                try:
                    #print("looking for txt send button")
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.txt_send_btn_AND_UI).click()
                    sleep(1)
                except:
                    #print("looking for RCS send button")
                    try:
                        self.driver.find_element(AppiumBy.XPATH, self.RCS_send_btn_xpath).click()
                        sleep(1)
                    except:
                        self.driver.find_element(AppiumBy.XPATH,self.RCS_send2_xpath).click()

    def sim_type_Msg(self,msg):
        try:
            if self.driver.find_element(AppiumBy.XPATH,self.txtSim1_xp).is_displayed:
                self.driver.find_element(AppiumBy.XPATH,self.txtSim1_xp).send_keys(msg)
                sleep(1)
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.txt_send_btn_AND_UI).click()

        except:
            try:
                if self.driver.find_element(AppiumBy.XPATH,self.RcsSim1_xp).is_displayed():
                    self.driver.find_element(AppiumBy.XPATH, self.RcsSim1_xp).send_keys(msg)
                    sleep(1)
                    self.driver.find_element(AppiumBy.XPATH, self.RCS_send_btn_xpath).click()
            except:
                pass



