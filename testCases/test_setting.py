from pageObject.voWifi import vo_wifi
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from appium.webdriver.common.appiumby import AppiumBy
from utilities.log import LogGen
from time import sleep




class Test_setting:
    logger = LogGen.setup_logger()
    wifi_xp='new UiSelector().className("android.widget.LinearLayout").instance(5)'



    def test_wifi(self,setup):
        self.driver=setup
        self.obj=vo_wifi(self.driver)
        self.logger.info('********************************* test_wifi ****************************************')
        self.logger.info('********************************* connecting to wifi ****************************************')
        self.obj.Open_setting_app()
        self.obj.swipe_UP()
        self.obj.search_in_setting('wifi')
        wait = WebDriverWait(self.driver, 50)
        self.obj.Click_on_1st_search()
        self.obj.check_1_toggle()

        try:
            wait.until(Ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,self.obj.wifi_connection)))
            self.logger.info('********************************* wifi is Connected ****************************************')
            print('Wifi is connected')
        except Exception:
            self.logger.info('********************************* wifi_is_not connected ****************************************')
            print("wifi is not connected")
        self.driver.back()
        self.driver.back()


    def test_mobile_network(self,setup):
        self.driver=setup
        self.obj=vo_wifi(self.driver)
        self.logger.info('********************************* test_mobile_network ****************************************')
        self.logger.info('********************************* mobile data ON ****************************************')

        self.obj.click_mobile_network()
        try:
            if self.driver.find_element(AppiumBy.XPATH,self.obj.Auto_Switch_xp).is_displayed():
                self.obj.check_3_toggle()
                self.logger.info('********************************* Only one Sim crd ****************************************')



        except Exception:
            self.obj.check_1_toggle()

    def test_simcard(self,setup):
        self.driver = setup
        self.obj = vo_wifi(self.driver)
        self.logger.info('********************************* test_simcard ****************************************')
        self.logger.info('********************************* Checking Sim card ****************************************')

        try:
            self.obj.Click_on_Sim2()
            self.logger.info('********************************* checking SIM 2****************************************')
            print("getting into SIM2")
            self.obj.check_wifi_call()
            self.obj.check_1_toggle()
            self.obj.click_wifi_prefrence()
            self.driver.back()
            self.driver.back()

            self.obj.click_on_Sim1()
            self.logger.info('********************************* checking SIM 1 ****************************************')
            print("getting into SIM1")
            self.obj.check_wifi_call()
            self.obj.check_1_toggle()
            self.obj.click_wifi_prefrence()
            self.driver.back()
            self.driver.back()

        except Exception:
            try:
                if self.driver.find_element(AppiumBy.XPATH,self.obj.No_sim_card1_xp).is_displayed():
                    self.obj.Click_on_Sim2()
                    self.obj.check_wifi_call()
                    self.obj.check_1_toggle()
                    self.obj.click_wifi_prefrence()

            except Exception:
                if self.driver.find_element(AppiumBy.XPATH, self.obj.NO_sim_card2_xp).is_displayed():
                    self.obj.click_on_Sim1()
                    self.obj.check_wifi_call()
                    self.obj.check_1_toggle()
                    self.obj.click_wifi_prefrence()


            finally:
                self.driver.back()
                self.driver.back()
        finally:
            self.driver.back()


    def test_verify_vowifi(self,setup):
        self.driver = setup
        self.obj = vo_wifi(self.driver)
        wait=WebDriverWait(self.driver,120)
        self.logger.info('********************************* test_verify_vowifi ****************************************')
        self.logger.info('********************************* checking the status of voWifi ****************************************')

        self.obj.swipe_DOWN()
        self.obj.Click_about_device()
        try:
            if self.driver.find_element(AppiumBy.XPATH,self.obj.status_SIM1_XP).is_displayed():
                try:
                    wait.until(Ec.presence_of_element_located((AppiumBy.XPATH,self.obj.check_vowifi_xp)))
                    if self.driver.find_element(AppiumBy.XPATH,self.obj.check_vowifi_xp).is_displayed():
                        self.logger.info('********************************* Sim 1 is successfully connected to VoWifi ****************************************')

                        print("Sim 1 is successfully connected to VoWifi")
                except Exception:
                    self.logger.critical('********************************* "Failed:-->Sim 1 is not connected to VoWifi" ****************************************')
                    print("Failed:-->Sim 1 is not connected to VoWifi")
        except Exception:
            self.logger.warn('********************************* SIM 1 is Not Available ****************************************')
            print("SIM 1 is Not Available")

        self.obj.swipe_DOWN()

        try:
            if self.driver.find_element(AppiumBy.XPATH,self.obj.status_SIM2_xp).is_displayed():
                try:
                    wait.until(Ec.presence_of_element_located((AppiumBy.XPATH, self.obj.check_vowifi_xp)))
                    if self.driver.find_element(AppiumBy.XPATH, self.obj.check_vowifi_xp).is_displayed():
                        print("Sim 2 is successfully connected to VoWifi")
                except:
                    self.logger.critical('********************************* "Failed:-->Sim 2 is not connected to VoWifi" ****************************************')
                    print("Failed:-->Sim 2 is not connected to VoWifi")
        except Exception:
            self.logger.warn('********************************* SIM 2 is Not Available ****************************************')
            print("SIM 2 is Not Available")
        finally:
            for _ in range(3):
                self.driver.back()

    def test_repeatation(self,setup):
        self.driver = setup
        self.obj = vo_wifi(self.driver)
        for _ in range(4):
            sleep(1)
            self.obj.swipe_UP()
            sleep(1)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.wifi_xp).click()
            sleep(2)
            self.obj.close_toggle_wait()
            wait = WebDriverWait(self.driver, 50)
            try:
                wait.until(Ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,self.obj.wifi_connection)))
                self.logger.info('********************************* wifi is Connected ****************************************')
                print('Wifi is connected')
            except Exception:
                self.logger.info('********************************* wifi_is_not connected ****************************************')
                print("wifi is not connected")
            self.driver.back()
            self.test_verify_vowifi(setup)



























