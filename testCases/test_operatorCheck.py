from pageObject.voWifi import vo_wifi
from appium.webdriver.common.appiumby import AppiumBy
from pageObject.check_operator import CheckOperatorManually
from utilities.common_function import Common_methods
from time import sleep




class Test_operatorManuallyCheck:


    def test_operator(self,setup):
        self.driver=setup
        self.voWifi=vo_wifi(self.driver)

        self.optr=CheckOperatorManually(self.driver)
        self.com=Common_methods(self.driver)

        self.voWifi.Open_setting_app()
        self.voWifi.swipe_UP()
        self.voWifi.click_mobile_network()

        try:
            if self.driver.find_element(AppiumBy.XPATH,self.voWifi.Sim1).is_displayed():
                self.voWifi.click_on_Sim1()
                print('Sim1 is clicked')
                sleep(3)
                self.optr.tap_On_Opertaor()
                print("tap done")

        except:
            print("came here why")
            pass

        try:
            print("checking Auto select")
            if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.optr.avail_network_AND_UI).is_displayed():
                self.com.close_toggle()
                self.optr.clickOnOFFbtn()
                self.optr.clickOnOFFbtn()
        except:
            print("Auto select is off")
            self.optr.CheckingOpertaor()
        self.driver.back()
        self.driver.back()


        try:
            if self.driver.find_element(AppiumBy.XPATH,self.voWifi.Sim2).is_displayed():
                self.voWifi.Click_on_Sim2()
                print('Sim2 is clicked')
                sleep(2)
                self.optr.tap_On_Opertaor()
                print("tap done")

        except:

            pass

        try:
            print("checking Auto select")
            if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.optr.avail_network_AND_UI).is_displayed():
                self.com.close_toggle()
                self.optr.clickOnOFFbtn()
                self.optr.clickOnOFFbtn()
        except:
            print("Auto select is off")
            self.optr.CheckingOpertaor()
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()






