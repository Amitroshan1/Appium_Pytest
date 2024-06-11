from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class CheckOperatorManually:
    off_btn_operator_AND_UI='new UiSelector().resourceId("android:id/button3")'
    Auto_select_Xpath='//android.widget.TextView[@text="Auto-select"]'
    avail_network_AND_UI='new UiSelector().text("Available networks")'
    radio_btn_AND_UI='new UiSelector().resourceId("com.android.phone:id/coui_tail_mark").instance(0)'
    error_text_AND_UI='new UiSelector().resourceId("com.android.phone:id/alertTitle")'
    error_cancle_AND_UI='new UiSelector().resourceId("android:id/button2")'





    def __init__(self,driver):
        self.driver=driver

    def tap_On_Opertaor(self):
        try:
            if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("VoLTE calls")').is_displayed():
                self.driver.tap([(594,2016)])
        except:
            self.driver.tap([(1004,1787)])
            sleep(2)

    def clickOnOFFbtn(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.off_btn_operator_AND_UI).click()
        sleep(1)

    def CheckingOpertaor(self):
        try:
            wait = WebDriverWait(self.driver, 70)
            wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.avail_network_AND_UI)))
            sleep(2)
            self.driver.save_screenshot('.//ScreenShot//Opertaor.png')

            for n in range(1, 10 ):
                self.element=f'(//android.widget.CheckBox[@resource-id="com.android.phone:id/coui_tail_mark"])[{n}]'


                try:
                    self.driver.find_element(AppiumBy.XPATH,self.element).click()
                    wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Access point names")')))
                    print("Registraion is Done")
                    self.tap_On_Opertaor()
                    wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.avail_network_AND_UI)))
                    sleep(2)
                    continue
                except:
                    try:

                        if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.error_text_AND_UI).is_displayed():
                            print(f'registration failed on {n} option')
                            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.error_cancle_AND_UI).click()
                            sleep(2)

                    except:
                        print("there is no more option")
                        break
        except:
            pass






