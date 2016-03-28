__author__ = 'keerthikorvi'
__author__ = 'keerthikorvi'
import csv
from selenium import webdriver
import logging
import coloredlogs
from datetime import datetime,date,timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
import time
import random
import timestring
import os
from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import html
from lxml import etree
from itertools import chain

# function to set preferences to the firefox browser profile
def createFireFoxProfile(profile):
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.download.dir", os.getcwd())
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "None")
    profile.set_preference("browser.helperApps.neverAsk.openFile", "None")
    profile.set_preference("browser.download.dir", 'D:\\nexislexis')
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
    profile.set_preference("browser.download.manager.showWhenStarting", False);
    profile.set_preference("browser.download.manager.focusWhenStarting", False);
    #profile.set_preference("browser.download.useDownloadDir",False );
    profile.set_preference("browser.helperApps.alwaysAsk.force", False);
    profile.set_preference("browser.download.manager.closeWhenDone", True);
    profile.set_preference("browser.download.manager.showAlertOnComplete", False);
    profile.set_preference("browser.download.manager.useWindow", False);
    profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False);
    profile.set_preference("pdfjs.disabled", True);
    profile.set_preference("browser.download.animateNotifications",False)
    return profile


#create firefox profile
profile = webdriver.FirefoxProfile()
#update browser properties
profile=createFireFoxProfile(profile)
#create browser using the firefox profile created
browser = webdriver.Firefox(firefox_profile=profile)
#maximize the window
#Twitter Advanced Search
#path_to_phantomjs = 'C:\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe'
#dcap = dict(DesiredCapabilities.PHANTOMJS)
#dcap["phantomjs.page.settings.userAgent"] = (
 #    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
 #    "(KHTML, like Gecko) Chrome/15.0.87")



#browser = webdriver.PhantomJS(executable_path = path_to_phantomjs,desired_capabilities = dcap)
browser.maximize_window()

browser.get('https://twitter.com/search?q=%22AGILENT%20TECHNOLOGIES%22%20lang%3Aen%20since%3A2012-11-18%20until%3A2012-11-20&src=typd&vertical=default&f=tweets&lang=en')
browser.implicitly_wait(1000)
scrollTopInitial=browser.execute_script("return document.body.scrollTop;")
print('scrollTopInitial..'+str(scrollTopInitial))
print('scrolling to the body height.....')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
scrollToplater1=browser.execute_script("return document.body.scrollTop;")
print('scrollToplater1..'+str(scrollToplater1))
browser.implicitly_wait(1000)
pageoffset=browser.execute_script("return window.pageYOffset;")
scrollToplater2=browser.execute_script("return document.body.scrollTop;")
print('scrollToplater2..'+str(scrollToplater2))
print('pageoffset'+str(pageoffset))
print('scrolling to the body height.....')
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#browser.implicitly_wait(1000)

pageoffset=browser.execute_script("return window.pageYOffset;")
print('pageoffset'+str(pageoffset))
#tree=html.fromstring(browser.page_source)
divs_html=[]
bs=BeautifulSoup(browser.page_source)
#print(bs.encode('utf-8'))
divs_html+=bs.findAll("div",attrs={"class":"content"})
for divtag in divs_html:
    ptag=divtag.find("p",{"class":"TweetTextSize  js-tweet-text tweet-text"})
    print(ptag)




    # filter removes possible Nones in texts and tails

print("page 1")
#print(browser.page_source)
#endOfContent='Back to top ?' in NoResults
endOfContent=False
#print(beautifulsoup)
scrollable=True
i=1
print('done')






while i<1:
    x=browser.execute_script("return (document.body.scrollHeight);")
    print(x)
    z=browser.execute_script("return ( document.documentElement.Height);")
    print(z)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.implicitly_wait(1000)
    time.sleep(10)
    test_sample=browser.execute_script("return document.documentElement.scrollHeight>document.documentElement.clientHeight;")
    #print(test_sample)
    html_source = browser.page_source
    i=i+1
    print("page"+str(i))
    #tweets2=tree.find_class('content')
    #print(tweets2)
    beautifulsoup_html_source=BeautifulSoup(html_source)
    divs_html=[]
    divs_html+=bs.findAll("div",attrs={"class":"content"})
    for divtag in divs_html:
        ptag=divtag.find("p",{"class":"TweetTextSize  js-tweet-text tweet-text"})
        print(ptag)
    browser.implicitly_wait(60)
   # AllPagesScolled='Back to top' in beautifulsoup_html_source
    scrollable=test_sample
    i=i+1
