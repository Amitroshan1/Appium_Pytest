from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


class Common_methods:
    toggle_xp = '//android.widget.Switch[@resource-id="android:id/switch_widget"]'
    second_toggle = '(//android.widget.Switch[@resource-id="android:id/switch_widget"])[2]'
    third_toggle='(//android.widget.Switch[@resource-id="android:id/switch_widget"])[3]'

    def __init__(self,driver):
        self.driver=driver

    def close_toggle(self):
        toggle = self.driver.find_element(AppiumBy.XPATH, self.toggle_xp)
        toggle_state = toggle.get_attribute("checked")
        if toggle_state == 'true':
            toggle.click()
            print("toggle is  Off Now")
        else:
            pass

    def check_1_toggle(self):
        toggle=self.driver.find_element(AppiumBy.XPATH,self.toggle_xp)
        toggle_state=toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")



    def check_2_toggle(self):
        toggle=self.driver.find_element(AppiumBy.XPATH,self.second_toggle)
        toggle_state=toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")


    def check_3_toggle(self):
        toggle=self.driver.find_element(AppiumBy.XPATH,self.third_toggle)
        toggle_state=toggle.get_attribute("checked")
        if toggle_state == 'true':
            print("toggle is already On")
            pass
        else:
            toggle.click()
            print("Now Toggle is On")


    def swipe_DOWN(self):
        self.driver.swipe(998,2640,594,409)
        sleep(1)

    def swipe_UP(self):
        self.driver.swipe(594,409,998,2640)
        sleep(1)
