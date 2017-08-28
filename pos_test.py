#encoding=utf-8

from selenium import webdriver
import unittest,time,re,os,sys,datetime,HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from init_testnumber import DeleteMb
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')

class pos_base(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.base_url='http://pos-p.4008827123.cn'
        self.verificationErrors=[]
        self.accept_next_alert=True
        self.mem=DeleteMb()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def denglu(self, phone, pw):
        u'''登录'''
        driver=self.driver
        driver.get(self.base_url)
        #driver.maximize_window()

        time.sleep(1)
        driver.find_element_by_id('username').send_keys(phone)
        driver.find_element_by_id('password').send_keys(pw)
        driver.find_element_by_id('login-sub').click()

    def is_login_sucess(self):
        u'''是否登录成功'''
        try:
            text=self.driver.find_element_by_id("merchant").text
            return True
        except:
            return False

    def is_element_exist(self, id):
        u'''判断元素是否存在'''
        try:
            self.driver.find_element_by_id(id).click()
            return True
        except:
            return False

    def push_card(self,card):
        self.driver.find_element_by_id("member-index-value-no").send_keys(card)
        self.driver.find_element_by_id("member-index-view-sub").click()

    def add_membership(self,phone):
        driver=self.driver
        try:
            self.denglu("18310101046","abc123")
            self.push_card(phone)
            time.sleep(2)
            driver.find_element_by_xpath(".//*[@id='card-type-selector-view']/div/div[2]/ul/li").click()
            time.sleep(2)
            driver.find_element_by_id("reg-member-view-sub").click()
            time.sleep(2)
            test1 = driver.find_element_by_xpath(".//*[@id='coupon-recharge-l']/span").text
            #test2 = u"注券"

            #print test1, test2, type(test1), type(test2)

            self.assertEqual(test1, u"注券", msg="shibai")
        except:
            self.driver.get_screenshot_as_file('E:\\android\\addmem1.png')
            print u'加会员失败'
            raise traceback.print_exc()

    def card_activety(self,cardno):
        try:
            self.denglu("18310101046","abc123")
            self.push_card(cardno)
            time.sleep(1)
            self.driver.find_element_by_id("confirm-view-sub").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='active-yazuo-card-view']/div/div[1]/div/table/tbody/tr[3]/td[2]/div/span[1]/input").send_keys('18365652222')
            Select(self.driver.find_element_by_xpath(".//*[@id='active-yazuo-card-view']/div/div[1]/div/table/tbody/tr[10]/td[2]/select")).select_by_visible_text("czq")
            self.driver.find_element_by_id("active-yazuo-card-view-sub").click()
            time.sleep(2)
            self.driver.find_element_by_id("print-preview-cancel").click()
        except:
            self.driver.get_screenshot_as_file('E:\\android\\addmem1.png')
            print u'卡激活失败'
            raise traceback.print_exc()
        finally:
            self.mem.deletemb()
            self.mem.del_card()

    def consumption(self,memid):
        try:
            self.denglu("18310101046", "abc123")
            self.push_card(memid)
            time.sleep(3)
            #print self.is_element_exist("mobile-card-view-sub")

            if self.is_element_exist("mobile-card-view-sub"):
                self.driver.find_element_by_id("mobile-card-view-sub").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='member-checklist']/table[5]/tbody/tr[1]/td[3]/input").send_keys("1")
            self.driver.find_element_by_xpath(".//*[@id='member-checklist']/table[5]/tbody/tr[2]/td[3]/input").send_keys("1")
            self.driver.find_element_by_xpath(".//*[@id='member-checklist']/table[5]/tbody/tr[3]/td[2]/input").send_keys("50")
            self.driver.find_element_by_xpath(".//*[@id='member-checklist']/table[5]/tbody/tr[4]/td[2]/input").send_keys("10")
            self.driver.find_element_by_id("member-checklist-sub").click()
            time.sleep(2)
            self.driver.find_element_by_id("mem-confirm-view-sub").click()
            time.sleep(2)
            self.driver.find_element_by_id("print-preview-cancel").click()
        except:
            self.driver.get_screenshot_as_file('E:\\android\\'+memid+'.png')
            print u'消费失败'
            raise traceback.print_exc()

    def card_rechange(self, cardno):
        try:
            self.denglu("18310101046","abc123")
            self.push_card(cardno)
            time.sleep(2)
            self.driver.find_element_by_id("card-recharge-l").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='card-recharge-checklist']/table/tbody[1]/tr[2]/td[3]/input").send_keys("100")
            Select(self.driver.find_element_by_xpath(".//*[@id='card-recharge-checklist']/table/tbody[3]/tr/td[3]/select")).select_by_visible_text("czq")
            self.driver.find_element_by_id("member-checklist-sub").click()
            time.sleep(2)
            self.driver.find_element_by_id("print-preview-cancel").click()
            except:
                self.driver.get_screenshot_as_file('E:\\android\\cardrechange.png')
                print u'储值失败'
                raise traceback.print_exc()



    def test0001(self):
        u'''正确账号登录'''
        self.denglu("18310101046","abc123")
        #判断结果

        result=self.is_login_sucess()
        self.assertTrue(result)

    def test0002(self):
        u'''错误账号登录'''
        self.denglu("18310101046","123123")
        #判断结果

        result = self.is_login_sucess()
        self.assertEqual(result, False, msg=u"密码错误")

    def test0003(self):
        u'''手机号加会员'''
        self.add_membership('18365652222')
        self.mem.deletemb()

    def test0004(self):
        u'''卡激活'''
        self.mem.init_card()
        self.card_activety("6201200561666938")
        #card.deletemb()

        #card.del_card()


    def test0005(self):
        u'''卡号消费'''
        self.consumption("6201200561635068")

    def test0006(self):
        u'''手机号消费'''
        self.consumption("18310104695")

    def test0007(self):
        u'''一号多卡消费'''
        self.consumption("18310104696")

    def test0008(self):
        u'''储值'''





if __name__=="__main__":
    suite=unittest.TestSuite()
    #suite.addTest(pos_base("test0001"))

    suite.addTest(pos_base("test0007"))
    timestr=time.strftime('%y%m%d%H%M%S',time.localtime())
    filename="E:\\android\\result_"+timestr+"report.html"
    print (filename)
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试结果',
        description=u'测试报告'
    )
    runner.run(suite)
    fp.close()
    #mail = Sendmail()

    #mail.send(filename)
