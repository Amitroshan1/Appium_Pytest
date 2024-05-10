from pageObject.voWifi import vo_wifi
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from appium.webdriver.common.appiumby import AppiumBy
from utilities.log import LogGen




class Test_setting:
    logger = LogGen.setup_logger()



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
