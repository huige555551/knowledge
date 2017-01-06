#coding=utf-8
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get('https://passport.csdn.net/account/login')
# elemUsername = driver.find_element_by_name('username')
# elemPassword = driver.find_element_by_name('password')
# elemUsername.send_keys('1026367919@qq.com')
# elemPassword.send_keys('86575501')
# driver.find_elements_by_class_name("logging")[0].click()
driver.get('http://my.csdn.net/my/mycsdn')
print driver.page_source.encode('utf-8')

# iplist = []  ##初始化一个list用来存放我们获取到的IP
# html = requests.get("http://my.csdn.net/my/mycsdn")  ##不解释咯
# print html.text.encode('utf-8')
# iplistn = re.findall(r"matchArr.*?'(.*?)'", html.text, re.S)  ##表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
# for ip in iplistn:
#     i = re.sub('\n', '', ip)  ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
#     iplist.append(i.strip())  ##添加到我们上面初始化的list里面
#     print ip.encode('utf-8')
