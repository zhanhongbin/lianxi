from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base_Tool:
    def __init__(self):
        self.driver = Driver.get_app_driver()

    def base_ele(self,loc,timeout=10,poll_frequency=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x : x.find_element(*loc))

    def base_eles(self,loc,timeout=10,poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))


    def base_click(self,loc,timeout=10,poll_frequency=0.5):
        # 点击操作
        self.base_ele(loc,timeout,poll_frequency).click()

    def base_input(self,loc,text,timeout=10,poll_frequency=0.5):
        # 输入 操作
        tp = self.base_ele(loc,timeout,poll_frequency)
        tp.clear()
        tp.send_keys(text)

    def base_text(self,loc,timeout=10,poll_frequency=0.5):
        # 获取文本操作
        ta = self.base_eles(loc,timeout,poll_frequency)
        return  [i.text for i in ta]
















