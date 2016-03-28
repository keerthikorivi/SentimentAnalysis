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

def readcsv(browser):
    f = open('twitterUrls.csv')
    csv_f = csv.reader(f)
    i=0
    for row in csv_f:
            # send the browser,ticker,date and company name details to download the documents
            logging.debug('current request'+row[0]+":"+row[1]+":"+row[2]+":"+row[3])
            print('current request'+row[0]+":"+row[1]+":"+row[2]+":"+row[3])
            print('startng download')
            try:
                x=scrapeTwitter(browser,row[0],row[1],row[2],row[3])
            except (BaseException) as e:
                logging.info('ERROR:SCRAPINGFAILED')
                #make sure that the after each search there is a random delay
            seconds = 5 + (random.random() * 5)
            time.sleep(seconds)

    f.close()


def scrapeTwitter(browser,ticker,date,company_name,url):
    #browser.get('https://twitter.com/search?q=%22AGILENT%20TECHNOLOGIES%22%20lang%3Aen%20since%3A2012-11-18%20until%3A2012-11-20&src=typd&vertical=default&f=tweets&lang=en')
    #browser.get('https://twitter.com/search?q=%22ALCOA%20INC%22%20lang%3Aen%20since%3A2013-01-08%20until%3A2013-01-10&src=typd&vertical=default&f=tweets&lang=en%27')
    browser.get(url)
    #browser.get('https://twitter.com/search?q=%22ADVANCE%20AUTO%20PARTS%20INC%22%20lang%3Aen%20since%3A2012-11-28%20until%3A2012-11-30&src=typd&vertical=default&f=tweets&lang=en%27')
    directory_path='C:\\Masters\\project-690\\TwitterDocs'
    datenewFormat=date.replace('/','-')
    directory_name=company_name+datenewFormat
    directory=directory_path+os.sep+directory_name
    if not os.path.exists(directory):
        os.makedirs(directory)
    browser.implicitly_wait(2000)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.implicitly_wait(2000)
    divs_html=[]
    bs=BeautifulSoup(browser.page_source)
    print('created dirs....')
    outputfile= open(directory+os.sep+company_name+'1.txt','w')
    outputfile.write(str(bs.encode('utf-8')))
    outputfile.close()
    divs_html+=bs.findAll("div",attrs={"class":"content"})
    all_p_tags=divs_html
    isSubset=False
    i=2
    while isSubset==False:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        browser.implicitly_wait(2000)
        divs_html=[]
        bs=BeautifulSoup(browser.page_source)
        divs_html+=bs.findAll("div",attrs={"class":"content"})
        isSubset=set(divs_html).issubset(all_p_tags)
        if(isSubset==True):
            print('isSubset....SEARCH SUCCESS')
        else:
            outputfile= open(directory+os.sep+company_name+str(i)+'.txt','w')
            outputfile.write(str(bs.encode('utf-8')))
            outputfile.close()

        all_p_tags+=divs_html
        all_p_tags=list(set(all_p_tags))
        print('page '+str(i))
        i+=1

    print('done....')

def createBrowser():
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
    return browser

browser=createBrowser()
readcsv(browser)






