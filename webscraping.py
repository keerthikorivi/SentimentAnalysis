#__author__ = 'keerthikorvi'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
path_to_chromedriver = 'D:\Keerthi\chromedriver_win32\chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://google.com'
browser.get(url)
#browser.switch_to_frame('mainFrame')
#browser.switch_to.frame('mainFrame')
#browser.switch_to('mainFrame')
browser.implicitly_wait(100)
print("waited for 30 seconds")
#x=browser.find_element_by_tag_name('input').send_keys('selenium')
x=browser.find_element_by_id('lst-ib').send_keys('selenium')
scroll=ActionChains(browser).move_to_element_with_offset(x,10,100)
scroll.perform()
y=browser.find_element_by_tag_name('a')

print(y.get_attribute('href'))
#some_object = WebDriverWait(browser, 120).until(S(EC.element_to_be_selected('iframe')))
#browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
#x=browser.find_element_by_id('divTrmsCotrs').get_attribute('style')
#y=browser.find_element_by_id('sourceTitleAdv').get_attribute('value')
#z=browser.find_element_by_xpath('//*[@id="terms"]')
print('done executing')
#print ('element.text: {0}'.format(x.text))
#print(x.get_attribute('value'))
#print('element.get_attribute(\'value\'): {0}'.format(x.get_attribute('value')))
#print(x)
#print(some_object)
