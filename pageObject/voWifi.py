from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class vo_wifi:

    setting_app_xp='//android.widget.TextView[@content-desc="Settings"]'
    search_Setting_xp='//android.widget.AutoCompleteTextView[@text="Search"]'
    first_search_ui_AUTO='new UiSelector().className("android.widget.LinearLayout").instance(5)'
    toggle_xp='//android.widget.Switch[@resource-id="android:id/switch_widget"]'
    cancle_inSearch_xp='//android.widget.ImageView[@content-desc="Clear query"]'
    No_search_result_xp='//android.widget.TextView[@text="No search results"]'
    Auto_Switch_xp='//android.widget.TextView[@text="Auto-switch data SIM"]'
    wifi_name_AND_UI='new UiSelector().text("Airtel_Admin_Saffo_5G")'

    mobile_network_AND_UI='new UiSelector().text("Mobile network")'
    No_sim_card1_xp='//android.widget.TextView[@resource-id="com.android.phone:id/simsetting_title1" and  @text="No SIM card"]'
    NO_sim_card2_xp='//android.widget.TextView[@resource-id="com.android.phone:id/simsetting_title2" and  @text="No SIM card"]'
    Sim2='//android.widget.TextView[@text="SIM2"]'
    Sim1='//android.widget.TextView[@text="SIM1"]'

    wifi_calling_xp='//android.widget.TextView[@text="Wi-Fi Calling"]'
    wifi_call_preference='//android.widget.TextView[@text="Wi-Fi Calling preferences"]'
    wifi_call_option_xp='//android.widget.CheckedTextView[@text="Wi-Fi Calling Preferred"]'
    wifi_call_Done_xp='//android.widget.TextView[@text="Done"]'
    wifi_connection = 'new UiSelector().resourceId("android:id/summary")'

    AboutDevice_ANd_UI='new UiSelector().text("About device")'
    status_xp='//android.widget.TextView[@text="Status"]'
    SIM_card_status_AND_UI='new UiSelector().text("SIM card status")'
    check_vowifi_xp='//android.widget.TextView[@text="IWLAN"]'
    status_SIM1_XP='//android.widget.TextView[@text="SIM 1"]'
    status_SIM2_xp='//android.widget.TextView[@text="SIM 2"]'





    def __init__(self,driver):
        self.driver=driver

    def Open_setting_app(self):
        self.driver.find_element(AppiumBy.XPATH,self.setting_app_xp).click()
        sleep(1)

    def search_in_setting(self,text):
        self.driver.find_element(AppiumBy.XPATH,self.search_Setting_xp).click()
        self.driver.find_element(AppiumBy.XPATH, self.search_Setting_xp).send_keys(text)
        sleep(1)

    def Click_on_1st_search(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.first_search_ui_AUTO).click()
        sleep(1)


    def close_toggle_wait(self):
        toggle = self.driver.find_element(AppiumBy.XPATH, self.toggle_xp)
        toggle_state = toggle.get_attribute("checked")
        if toggle_state == 'true':
            toggle.click()
            print("toggle is already Off Now")
            sleep(50)
            toggle.click()
            sleep(1)

        else:
            sleep(50)
            print("Toggle is already On")

    def check_1_toggle(self):
        toggle=self.driver.find_element(AppiumBy.XPATH,self.toggle_xp)
        toggle_state=toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")

    def check_3_toggle(self):
        toggle=self.driver.find_element(AppiumBy.XPATH,'(//android.widget.Switch[@resource-id="android:id/switch_widget"])[3]')
        toggle_state=toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")

    def clear_search_box(self):
        self.driver.find_element(AppiumBy.XPATH,self.cancle_inSearch_xp).click()
        sleep(1)

    def click_mobile_network(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.mobile_network_AND_UI).click()
        sleep(1)

    def click_on_Sim1(self):
        self.driver.find_element(AppiumBy.XPATH,self.Sim1).click()
        sleep(1)

    def Click_on_Sim2(self):
        self.driver.find_element(AppiumBy.XPATH,self.Sim2).click()

    def check_wifi_call(self):
        self.driver.find_element(AppiumBy.XPATH,self.wifi_calling_xp).click()

    def click_wifi_prefrence(self):
        self.driver.find_element(AppiumBy.XPATH,self.wifi_call_preference).click()
        sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.wifi_call_option_xp).click()
        sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.wifi_call_Done_xp).click()
        sleep(1)

    def swipe_DOWN(self):
        self.driver.swipe(998,2640,594,409)
        sleep(1)

    def swipe_UP(self):
        self.driver.swipe(594,409,998,2640)
        sleep(1)

    def Click_about_device(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.AboutDevice_ANd_UI).click()
        self.swipe_DOWN()
        sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.status_xp).click()
        sleep(1)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.SIM_card_status_AND_UI).click()
        sleep(1)






