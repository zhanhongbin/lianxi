from appium import webdriver


class  Driver:
    __app_driver = None
    @classmethod
    def get_app_driver(cls):
        if  not  cls.__app_driver:
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'resetKeyboard': True,  # 重置⼿机键盘
                'unicodeKeyboard': True  # 使⽤unicode编码键盘 发送数据都会使⽤unicode
            }
            # 声明我们的driver对象
            cls.__app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.__app_driver
        else:
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver !=None :
            cls.__app_driver.quit()
            cls.__app_driver = None



















































