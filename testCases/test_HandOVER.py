from selenium.common import InvalidSessionIdException

from pageObject.Vowifi_Handover import handOver
from pageObject.Audio_call import audio_Call
from pageObject.voWifi import vo_wifi
from utilities.common_function import Common_methods
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from utilities.log import LogGen
from time import sleep




class Test_vowifi_handover:
    logger = LogGen().setup_logger()


    def test_handover_vowifi(self,setup):
        self.driver=setup
        self.obj=handOver(self.driver)

        self.com = Common_methods(self.driver)


        self.obj.wifi_On()
        self.com.check_1_toggle()
        sleep(7)
        self.com.swipe_DOWN()
        self.obj.add_wifi()
        sleep(2)
        self.com.swipe_UP()
        self.driver.back()
        self.com.swipe_DOWN()

        self.obj.Verify()
        wait = WebDriverWait(self.driver, 120)

        self.vo=vo_wifi(self.driver)

        try:
            if self.driver.find_element(AppiumBy.XPATH,self.vo.status_SIM1_XP).is_displayed():
                try:
                    wait.until(Ec.presence_of_element_located((AppiumBy.XPATH,self.vo.check_vowifi_xp)))
                    if self.driver.find_element(AppiumBy.XPATH,self.vo.check_vowifi_xp).is_displayed():
                        self.logger.info('********************************* Sim 1 is successfully connected to VoWifi ****************************************')

                        print("Sim 1 is successfully connected to VoWifi")
                except Exception:
                    self.logger.critical('********************************* "Failed:-->Sim 1 is not connected to VoWifi" ****************************************')
                    print("Failed:-->Sim 1 is not connected to VoWifi even after waiting for 2 min")
        except Exception:
            self.logger.warning('********************************* SIM 1 is Not Available ****************************************')
            print("SIM 1 is Not Available")

        self.com.swipe_DOWN()

        try:
            if self.driver.find_element(AppiumBy.XPATH,self.vo.status_SIM2_xp).is_displayed():
                try:
                    wait.until(Ec.presence_of_element_located((AppiumBy.XPATH, self.vo.check_vowifi_xp)))
                    if self.driver.find_element(AppiumBy.XPATH, self.vo.check_vowifi_xp).is_displayed():
                        print("Sim 2 is successfully connected to VoWifi")
                except:
                    self.logger.critical('********************************* "Failed:-->Sim 2 is not connected to VoWifi" ****************************************')
                    print("Failed:-->Sim 2 is not connected to VoWifi even after waiting for 2 min")
        except Exception:
            self.logger.warning('********************************* SIM 2 is Not Available ****************************************')
            print("SIM 2 is Not Available")
        finally:
            for _ in range(3):
                sleep(1)
                self.driver.back()
                self.driver.back()

    def test_make_call(self,setup,setup2):
        self.driver = setup
        self.driver2 = setup2
        self.obj = audio_Call(self.driver, self.driver2)
        self.obj.open_phn_dialer()
        self.obj.click_dialpad()
        self.obj.Enter_number(self.obj.Number)

        try:
            self.driver.find_element(AppiumBy.XPATH, self.obj.Call_btn_xpath).click()
        except Exception:
            try:
                self.driver.find_element(AppiumBy.XPATH, self.obj.Num_call_btn_xp).click()
            except Exception:
                print("Both video call buttons are not present")
        sleep(7)
        try:
            print("waiting to tap")
            self.obj.Recieve_call()
            sleep(3)
            self.obj.Recieve_call()
        except Exception:
            self.driver.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()
        sleep(25)
        self.driver.back()
        self.driver.back()
        self.driver.open_notifications()
        sleep(2)
        self.Hand=handOver(self.driver)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.Hand.Notif_wifi_And_UI).click()
        sleep(2)

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.Hand.Now_call_AND_UI).click()
        sleep(2)

        try:
            wait = WebDriverWait(self.driver, 180)
            wait.until(Ec.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,self.obj.phn_dialer_AND_UI)))
            self.driver=setup2
            self.driver2.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()
            print("FAILED")
        except:
            self.driver = setup2
            self.driver2.find_element(AppiumBy.XPATH,self.obj.Audio_End_button).click()
            print("PASSED")

    def test_setting_wifi(self,setup,setup2):

        self.driver=setup
        self.driver2=setup2

        self.obj = audio_Call(self.driver, self.driver2)
        self.Hand = handOver(self.driver)
        self.com = Common_methods(self.driver)

        self.driver.open_notifications()
        sleep(2)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.Hand.Notif_wifi_And_UI).click()
        sleep(5)
        self.driver.back()
        sleep(2)

        self.obj.open_phn_dialer()
        self.obj.click_dialpad()
        self.obj.Enter_number(self.obj.Number)

        try:
            self.driver.find_element(AppiumBy.XPATH, self.obj.Call_btn_xpath).click()
        except Exception:
            try:
                self.driver.find_element(AppiumBy.XPATH, self.obj.Num_call_btn_xp).click()
            except Exception:
                print("Both video call buttons are not present")
        sleep(7)
        try:
            print("waiting to tap")
            self.obj.Recieve_call()
            sleep(3)
            self.obj.Recieve_call()
        except Exception:
            self.driver.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()

        sleep(25)
        self.driver.back()
        self.driver.back()

        self.Hand.wifi_On()
        self.com.close_toggle()


        try:
            wait = WebDriverWait(self.driver2, 180)
            wait.until(Ec.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,self.obj.phn_dialer_AND_UI)))
            self.driver = setup2
            print("FAILED")
        except :
            self.driver = setup2
            self.driver2.find_element(AppiumBy.XPATH,self.obj.Audio_End_button).click()

            print("PASSED")
        self.driver.back()
        self.driver.back()


    def  test_vowifi_calling(self,setup,setup2):
        self.driver=setup
        self.driver2=setup2

        self.obj = audio_Call(self.driver, self.driver2)
        self.Hand = handOver(self.driver)
        self.com = Common_methods(self.driver)

        self.driver.open_notifications()
        sleep(2)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.Hand.Notif_wifi_And_UI).click()
        sleep(5)
        self.driver.back()
        sleep(2)

        self.obj.open_phn_dialer()
        self.obj.click_dialpad()
        self.obj.Enter_number(self.obj.Number)

        try:
            self.driver.find_element(AppiumBy.XPATH, self.obj.Call_btn_xpath).click()
        except Exception:
            try:
                self.driver.find_element(AppiumBy.XPATH, self.obj.Num_call_btn_xp).click()
            except Exception:
                print("Both video call buttons are not present")
        sleep(7)
        try:
            print("waiting to tap")
            self.obj.Recieve_call()
            sleep(3)
            self.obj.Recieve_call()
        except Exception:
            self.driver.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()

        sleep(25)
        self.driver.back()
        self.driver.back()




        try:
            wait = WebDriverWait(self.driver2, 180)
            wait.until(Ec.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.obj.phn_dialer_AND_UI)))
            self.driver = setup2
            print("FAILED")
        except:
            self.driver = setup2
            self.driver2.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()

            print("PASSED")
        self.driver.back()
        self.driver.back()
























