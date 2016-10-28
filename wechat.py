#coding=utf-8
from appium import webdriver
import time
from selenium.webdriver.common.keys import Keys
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
print "---open wechat----"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
print "---login---"
cl= driver.find_element_by_id("com.tencent.mm:id/c7m")
cl.click()
print "---change login---"
time.sleep(5)
driver.find_element_by_id("com.tencent.mm:id/b9c").click()
time.sleep(10)
log=driver.find_element_by_name("QQ号/微信号/Email")
print "---user---"
log.send_keys("*****") #*引号内输入用户名
time.sleep(1)
print "---passwd---"
pas=driver.find_element_by_xpath("//*[@NAF='true']")
pas.send_keys("***")#引号内输入密码
logi=driver.find_element_by_name('登录')
logi.click()
time.sleep(10)
driver.find_element_by_name("是").click()
time.sleep(10)
driver.find_element_by_accessibility_id("搜索").click()
time.sleep(2)
driver.find_element_by_name("搜索").send_keys("dandan")
time.sleep(5)
#选中联系人
driver.tap([(26,257),(122,353)],100)#此处是根据坐标位置来的，可以用UI Atutomator viewer  bounds 来找到对应的坐标
time.sleep(2)
#展开更多功能
driver.find_element_by_accessibility_id("更多功能按钮，已折叠").click()
time.sleep(2)
#打开选择图片
driver.find_element_by_id("com.tencent.mm:id/ka").click() #这个地方待优化，其实展开后的其他几个功能图标也是这个id，可以考虑使用xpath或者坐标定位
time.sleep(2)
#选择图片
driver.tap([(458,160),(498,200)],100) #此处是根据坐标位置来的，可以用UI Atutomator viewer  bounds 来找到对应的坐标
time.sleep(2)
#发送
driver.find_element_by_id("com.tencent.mm:id/fb").click()
print "done"
driver.quit()