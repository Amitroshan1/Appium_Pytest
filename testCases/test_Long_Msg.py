from pageObject.Long_msg_loctors import Long_msg
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from utilities.log import LogGen
from utilities.common_function import Common_methods



class Test_Long_Msg:
    number="+919653184217"
    repeat=3

    msg=("A well-organized paragraph supports or develops a single controlling idea,"
         " which is expressed in a sentence called the topic sentence. "
         "A topic sentence has several important functions: it substantiates or supports an essay’s"
         " thesis statement; it unifies the content of a paragraph and directs the order of the sentences;"
         " and it advises the reader of the subject to be discussed and how the paragraph will discuss it."
         " Readers generally look to the first few sentences in a paragraph to determine the subject and "
         )
    shrt_msg="hi i am amit kumar"

    logger = LogGen.setup_logger()





    def test_msg(self,setup):

        self.driver=setup
        self.obj=Long_msg(self.driver)
        self.logger.info('********************************* test_msg ****************************************')

        self.obj.open_Msg()
        self.logger.info('********************************* opened Msg app****************************************')
        self.obj.test_RCS_ststus_delivery_report()
        self.logger.info('********************************* RCS chat and Delirvery report ****************************************')
        sleep(1)
        self.obj.compose_msg()
        self.logger.info('********************************* clicked on compose msg ****************************************')
        self.obj.enter_number(self.number)
        self.logger.info('********************************* Number is entered ****************************************')
        wait=WebDriverWait(self.driver,60)
        cnt=0
        failed=0
        for i in range(self.repeat):
            try:
                if self.driver.find_element(AppiumBy.XPATH, self.obj.txtSim1_xp).is_displayed:
                    self.obj.sim_type_Msg(self.msg)
            except:
                try:
                    if self.driver.find_element(AppiumBy.XPATH, self.obj.RcsSim1_xp).is_displayed():
                        self.obj.sim_type_Msg(self.msg)
                except:
                    self.obj.type_Msg(self.msg)
            sleep(2)
            try:
                wait.until(Ec.any_of(Ec.visibility_of_element_located((AppiumBy.XPATH,self.obj.double_click_xpath)),
                                     Ec.visibility_of_any_elements_located((AppiumBy.XPATH,self.obj.double_click2_xpath))))
                cnt+=1
                print(f'Long msg has been send {cnt} times')
            except Exception:
                failed+=1
                print(f'Msg cannot be send {failed} times')
                self.logger.info('********************************* test_msg  testcase completed  ** **************************************')
        self.driver.back()
        self.driver.back()
        self.driver.back()

        print(f'Total msg Failed--> {failed}')
        print(f'total msg successfully send-->{cnt}')

    def test_short_msg(self,setup):
        self.driver=setup
        self.obj=Long_msg(self.driver)
        self.obj.open_Msg()
        self.obj.compose_msg()
        self.obj.enter_number(self.number)
        wait = WebDriverWait(self.driver, 60)
        cnt=0
        failed=0
        for i in range(self.repeat):
            try:
                if self.driver.find_element(AppiumBy.XPATH, self.obj.txtSim1_xp).is_displayed:
                    self.obj.sim_type_Msg(self.shrt_msg)
            except:
                try:
                    if self.driver.find_element(AppiumBy.XPATH, self.obj.RcsSim1_xp).is_displayed():
                        self.obj.sim_type_Msg(self.shrt_msg)
                except:
                    self.obj.type_Msg(self.shrt_msg)
            sleep(2)

            try:
                wait.until(Ec.any_of(Ec.visibility_of_element_located((AppiumBy.XPATH, self.obj.double_click_xpath)),
                                     Ec.visibility_of_any_elements_located((AppiumBy.XPATH, self.obj.double_click2_xpath))))
                cnt += 1
                print(f'Short msg has been send {cnt} times')
            except Exception:
                failed+=1
                print(f'Msg cannot be send {failed} times')
        self.driver.back()
        self.driver.back()
        self.driver.back()
        print(f'Total msg Failed--> {failed}')
        print(f'total msg successfully send-->{cnt}')

