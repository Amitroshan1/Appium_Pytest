from datetime import datetime
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.Audio_call import audio_Call
from selenium.webdriver.support import expected_conditions as EC


class Test_audio_call:
    repeat=3


    def test_audio(self,setup,setup2):
        self.driver=setup
        self.driver2=setup2
        self.obj=audio_Call(self.driver,self.driver2)
        self.obj.open_phn_dialer()
        self.obj.click_dialpad()
        self.obj.Enter_number(self.obj.Number)
        wait_for_call = WebDriverWait(self.driver, 38)
        total = 0
        cnt = 0
        Drop = 0
        switch = 0
        for i in range(self.repeat):
            total += 1
            timestamp = datetime.now().strftime("%Y-%m-%d___%H:%M:%S")
            try:
                self.driver.find_element(AppiumBy.XPATH, self.obj.Call_btn_xpath).click()
            except Exception:
                try:
                    self.driver.find_element(AppiumBy.XPATH, self.obj.Num_call_btn_xp).click()
                except Exception:
                    print("Both video call buttons are not present")
            sleep(5)
            try:
                print("waiting to tap")
                self.obj.Recieve_call()
                sleep(3)
                self.obj.Recieve_call()
            except Exception:
                self.driver.find_element(AppiumBy.XPATH,self.obj.Audio_End_button).click()
                continue



            try:
                wait_for_call.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.obj.call_timer_xpath)))
                print("timer is visible")

                try:
                    wait_for_call.until(EC.presence_of_element_located((AppiumBy.XPATH,self.obj.recent_btn_xpath)))
                    if self.driver.find_element(AppiumBy.XPATH, self.obj.recent_btn_xpath).is_displayed():
                        Drop+=1
                        print('Call Drop--->',timestamp)
                        continue
                except:
                    cnt+=1
                    self.driver.find_element(AppiumBy.XPATH,self.obj.Audio_End_button).click()
                    print("Call was Successfull--->",cnt)
                    sleep(1)
            except Exception:

                if total == self.repeat:
                    try:
                        self.driver.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()
                    except:
                        pass
                else:
                    print("Reciever end is not picking or switch Off or out of range")
                    continue
        print("Total Call Made--->",total)
        print("Total Call Drop--->",Drop)
        print("Total Test Call Pass-->",cnt)
        self.driver.back()
        self.driver.back()


