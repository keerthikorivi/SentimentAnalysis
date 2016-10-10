#__author__ = 'keerthikorvi'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import urllib3
import urllib
import urllib.request
import os

MY_EMAIL = 'keerthik'
MY_PASSWORD = ''
MY_PROFILE_NAME = ''
path_to_chromedriver = 'D:\Keerthi\chromedriver_win32\chromedriver.exe' # change path as needed
profile=webdriver.FirefoxProfile()

profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", os.getcwd())
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "None")
profile.set_preference("browser.helperApps.neverAsk.openFile", "None")

#new configuration

profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", 'C:\\Users\\keerthikorvi\\PycharmProjects\\nexislexisdocs')
profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
profile.set_preference("browser.download.manager.showWhenStarting", False);
profile.set_preference("browser.download.manager.focusWhenStarting", False);
#profile.set_preference("browser.download.useDownloadDir", true);
profile.set_preference("browser.helperApps.alwaysAsk.force", False);
profile.set_preference("browser.download.manager.closeWhenDone", True);
profile.set_preference("browser.download.manager.showAlertOnComplete", False);
profile.set_preference("browser.download.manager.useWindow", False);
profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False);
profile.set_preference("pdfjs.disabled", True);
profile.set_preference("browser.download.animateNotifications",False)


print('set configuration...')
browser = webdriver.Firefox(firefox_profile=profile)
#browser = webdriver.Firefox()

browser.maximize_window()
browser.get('https://er.lib.k-state.edu/login?qurl=http%3a%2f%2fwww.lexis-nexis.com%2funiverse')
browser.implicitly_wait(40)
print('waited for 40 second till the browser loaded')
#email=browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/p[1]/input[@name="user"]')
#email = browser.find_element_by_css_selector('input#user')
#email.send_keys(MY_EMAIL)
#pw = browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/p[2]/input[@name="pass"]')
#pw.send_keys(MY_PASSWORD)
#submit_button=browser.find_element_by_id('submit_button').click()
#browser.implicitly_wait(45)  # seconds
#x=browser.get_screenshot_as_png()
#page_source=browser.page_source
print('waited for 45 seconds...')
#y=browser.find_element_by_xpath('//*[@id="logo_img"]/a').text
#search_terms=browser.find_element_by_xpath('//*[@id="terms"]')
#search_terms.send_keys('AAPL')
#browser.current_url
#browser.find_element_by_link_text(MY_PROFILE_NAME).click()
#print(y)
#iframe = browser.find_elements_by_tag_name('iframe')[0]
#browser.switch_to.frame(iframe)
#soup=BeautifulSoup(browser.page_source)
#print(soup.prettify());

#browser.switch_to.active_element(browser.find_element_by_tag_name('body'))
frameData=browser.switch_to.frame('mainFrame')
advanceButton=browser.find_element_by_id('lblAdvancDwn').click()

txtFrmDate=browser.find_element_by_id('txtFrmDate')
txtFrmDate.send_keys('03/10/2015')

txtToDate=browser.find_element_by_id('txtToDate')
txtToDate.send_keys('05/10/2015')

browser.implicitly_wait(60)
sourceTitleAdv=browser.find_element_by_name('sourceTitleAdv')
sourceTitleAdv.clear()
browser.implicitly_wait(60)
sourceTitleAdv.send_keys('The New York Times')

browser.implicitly_wait(60)

browser.find_element_by_link_text('The New York Times').click()
browser.implicitly_wait(60)


sourceTitleAdv.send_keys('Daily News (New York)')

browser.implicitly_wait(60)

browser.find_element_by_link_text('Daily News (New York)').click()
browser.implicitly_wait(60)

browser.implicitly_wait(60)
applyButton=browser.find_element_by_id('OkButt').click()
#sourceTitleAdv.click()
#print('down')
#print("first "+sourceTitleAdv.get_attribute('value'))
#sourceTitleAdv.send_keys('The New York Times',Keys.ARROW_DOWN)


#print("second "+sourceTitleAdv.get_attribute('value'))
#divValue=browser.find_element_by_id('divAdvSrcs')
#browser.execute_script("arguments[0].value='hello';",divValue)
#print("divvalue "+divValue.text)



searchTerms=browser.find_element_by_id('terms')
searchTerms.clear()
searchTerms.send_keys('AAPL')
submit_button=browser.find_element_by_id('srchButt').click()
print('done clicking the button....')
browser.implicitly_wait(200)
print('waited for 200 seconds.....................')
#print(browser.page_source)
#browser.find_element_by_name('fr_resultsNav~ResultsMaxGroupTemplate0')
browser.switch_to.frame(browser.find_element_by_css_selector("frame[title='Results Navigation Frame']"))
x=browser.find_element_by_css_selector("img[title='Download Documents']")
mainWindow=browser.current_window_handle
x.click()
#browser.switch_to.frame('fs_content')
#print(browser.page_source)
#browser.switch_to.frame('fs_main.0')
#print(browser.page_source)

#print(browser.find_element_by_tag_name('iframe').get_attribute('src'))

#browser.find_element_by_id('srchButt').click()
allWindowHandles=browser.window_handles[1]
browser.switch_to.window(allWindowHandles)

downloadButton=browser.find_element_by_css_selector("img[title='Download']")
downloadButton.click()
browser.implicitly_wait(60)

downloadhref=browser.find_element_by_partial_link_text('.DOC').get_attribute('href')
browser.find_element_by_partial_link_text('.DOC').click()
#browser.get(downloadhref)
print(downloadhref)

#os.system("wget "+downloadhref)



#os.chdir('C:\\Users\\keerthikorvi\\PycharmProjects\\nexislexisdocs')
#os.system('wget -O document.doc --http-user keerthik --http-password Keer300391 "'+downloadhref+'"')






#print(browser.page_source)
print('done')
