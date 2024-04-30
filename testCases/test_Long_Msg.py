from pageObject.Long_msg_loctors import Long_msg
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
class Test_Long_Msg:
    number="8210171981"
    msg=("A well-organized paragraph supports or develops a single controlling idea,"
         " which is expressed in a sentence called the topic sentence. "
         "A topic sentence has several important functions: it substantiates or supports an essay’s"
         " thesis statement; it unifies the content of a paragraph and directs the order of the sentences;"
         " and it advises the reader of the subject to be discussed and how the paragraph will discuss it."
         " Readers generally look to the first few sentences in a paragraph to determine the subject and "
         "perspective of the paragraph. That’s why it’s often best to put the topic sentence at the very"
         " beginning of the paragraph. In some cases, however, it’s more effective to place another sentence "
         "before the topic sentence—for example, a sentence linking the current paragraph to the previous one,"
         " or one providing background information")

    def test_msg(self,setup):
        self.driver=setup
        self.obj=Long_msg(self.driver)
        self.obj.open_Msg()
        self.obj.compose_msg()
        self.obj.enter_number(self.number)
        cnt=0
        failed=0
        for i in range(3):

            self.obj.type_Msg(self.msg)
            sleep(2)

            self.obj.send_Msg_Verify()
            try:
                if self.driver.find_element(AppiumBy.XPATH,self.obj.double_click_xpath).is_displayed():
                    cnt+=1
                print(f'Long msg has been send {cnt} times')
            except Exception:
                failed+=1
                print(f'Msg cannot be send {failed} times')
        self.driver.back()
        self.driver.back()
        self.driver.back()
        print(f'Total msg--> {failed}')
        print(f'total msg successfully send-->{cnt}')

