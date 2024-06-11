from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from utilities.common_function import Common_methods
class handOver:
    setting_ANDUI='new UiSelector().text("Settings")'
    wifi_And_UI='new UiSelector().text("Wi-Fi")'
    add_Network_AND_UI='new UiSelector().text("Add network")'

    Hotspot_AND_UI='new UiSelector().className("android.widget.EditText").instance(0)'
    Password_AND_UI='new UiSelector().className("android.widget.EditText").instance(1)'
    save_btn_AND_UI='new UiSelector().resourceId("com.oplus.wirelesssettings:id/menu_save")'

    about_AND_UI='new UiSelector().text("About device")'
    status_AND_UI='new UiSelector().text("Status")'
    sim_And_UI='new UiSelector().resourceId("com.android.settings:id/coui_preference_widget_jump").instance(0)'

    Notif_wifi_And_UI='new UiSelector().description("Open Wi-Fi settings.")'
    Now_call_AND_UI='new UiSelector().text("now")'


    def __init__(self,driver):
        self.driver=driver
        self.com=Common_methods(self.driver)


    def wifi_On(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.setting_ANDUI).click()
        self.com.swipe_UP()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.wifi_And_UI).click()

    def add_wifi(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.add_Network_AND_UI).click()
        sleep(1)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.Hotspot_AND_UI).send_keys('Airtel_Admin_Saffo_5G')
        sleep(1)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.Password_AND_UI).send_keys("Saffo@2023")
        sleep(1)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.save_btn_AND_UI).click()

    def Verify(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.about_AND_UI).click()
        sleep(1)
        self.com.swipe_DOWN()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.status_AND_UI).click()
        sleep(1)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.sim_And_UI).click()

