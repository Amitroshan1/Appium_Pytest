from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.Video_call_Locators import video_call_Locator





class Test_call_msg:
    number="+919315227062"
    start_x = 604
    start_y = 963
    end_x = 604
    end_y = 494
    repeat=50
    def test_make_video_call(self,setup,setup2):
        self.driver=setup
        self.driver2=setup2
        self.obj=video_call_Locator(self.driver,self.driver2)
        self.obj.Open_phn_dialer()
        self.obj.press_dial_pad()
        self.obj.enterNumber(self.number)
        self.obj.click_video_call(self.start_x,self.start_y,self.end_x,self.end_y)
        wait_for_call = WebDriverWait(self.driver, 28)
        total=0
        cnt = 0
        Drop = 0
        switch=0
        for i in range(self.repeat):
            total+=1
            timestamp = datetime.now().strftime("%Y-%m-%d___%H:%M:%S")
            try:
                self.driver.find_element(AppiumBy.XPATH, self.obj.video_call_xpath).click()
            except Exception:
                try:
                    self.driver.find_element(AppiumBy.XPATH, self.obj.video_call_btn_number).click()
                except Exception:
                    print("Both video call buttons are not present")
                    continue
            sleep(7)
            total+=1
            print("waiting to tap")
            self.obj.Recieve_call()
            self.obj.Recieve_call()

            try:
                wait_for_call.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.obj.call_timer_xpath)))
                print("timer is visible")
                self.driver.tap([(1122, 925)])
                try:
                    wait_for_call.until(EC.any_of(EC.presence_of_element_located((AppiumBy.XPATH,self.obj.recent_btn_xpath)),
                                                  EC.presence_of_element_located((AppiumBy.XPATH,self.obj.Audio_End_button))))
                    try:
                        if self.driver.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).is_displayed():
                            self.driver.find_element(AppiumBy.XPATH, self.obj.Audio_End_button).click()
                            switch += 1
                            print(f"Your call got switched from Video to Audio Call-->{timestamp}--->{switch}times ")
                            continue
                    except :
                        if self.driver.find_element(AppiumBy.XPATH,self.obj.recent_btn_xpath).is_displayed():
                            Drop += 1
                            print(f"Video call is dropped {Drop} times {timestamp}")
                            continue
                except:
                    pass

                cnt+=1
                self.driver.find_element(AppiumBy.XPATH, self.obj.Video_End_button).click()
                print(f'you made the Video call {cnt}st time')
                sleep(2)

            except Exception:
                print("Reciever end is not picking or switch Off or out of range")
                if total==self.repeat:
                    try:
                        self.driver.find_element(AppiumBy.XPATH, self.obj.Video_End_button).click()
                    except:
                        pass
                else:
                    continue
        print("Total Call Drop--->", Drop)
        print("Total Video to Audio switch--->",switch)
        self.driver.back()





