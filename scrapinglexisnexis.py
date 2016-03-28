# __author__ = 'keerthikorvi'
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
noOfAttemptsDictionary ={}

def exists_by_id(id,browser):
    try:
        browser.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def exists_by_css_selector(browser,css_selector):
    try:
        #WebDriverWait(browser,60).until(EC.presence_of_element_located(By.CSS_SELECTOR,css_selector))
        browser.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True

def exists_by_xpath(browser,xpath):
    try:
        browser.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#checks if after the search if the page contains any results
def checkIfNoResultsPageFound(browser):
    NoDocsFoundText='No Documents Found'
    pagesource=BeautifulSoup(browser.page_source).prettify()
    return (NoDocsFoundText in pagesource.title())




def downloadDocuments(browser, ticker, date, company_name):
    print('download docs...')
    #go to the k-state nexis lexis url
    browser.get('https://er.lib.k-state.edu/login?qurl=http%3a%2f%2fwww.lexis-nexis.com%2funiverse')
    #browser.implicitly_wait(40)
     # Go to the mainFramw in the webpage where you find the search and advanced options.
     # Try for 80 seconds till you find the frame. otherwise return to the calling function.
    try:
        frameData = WebDriverWait(browser, 80).until(EC.frame_to_be_available_and_switch_to_it(('mainFrame')))
    except TimeoutException:
        return 0


    #can delete later
    #frameData=browser.switch_to.frame('mainFrame')
    # Find the advanced button in the frame
    advanceButton=browser.find_element_by_id('lblAdvancDwn').click()
    date_string=datetime.strptime(date, '%m/%d/%Y').date()
    fromDate=(date_string-timedelta(days=1)).strftime('%m/%d/%Y')
    toDate=(date_string+timedelta(days=1)).strftime('%m/%d/%Y')
    # Find the from date element
    browser.implicitly_wait(60)
    txtFrmDate=browser.find_element_by_id('txtFrmDate')
    browser.implicitly_wait(60)
    txtFrmDate.clear()
    browser.implicitly_wait(60)
    #send the fromDate to the advanced search
    txtFrmDate.send_keys(fromDate)
    browser.implicitly_wait(60)
    #find the to date in the browser
    txtToDate=browser.find_element_by_id('txtToDate')
    browser.implicitly_wait(60)
    txtToDate.clear()
    browser.implicitly_wait(60)
    #send input to date to the field
    txtToDate.send_keys(toDate)

    browser.implicitly_wait(60)
    #check if the dates are properlyset
    if txtFrmDate.get_attribute('value')!=fromDate:
        txtFrmDate.send_keys(fromDate)
    if txtToDate.get_attribute('value')!=toDate:
        txtToDate.send_keys(toDate)




    #Find the source field in the advanced section
    sourceTitleAdv=browser.find_element_by_name('sourceTitleAdv')
    browser.implicitly_wait(60)
    sourceTitleAdv.clear()
    browser.implicitly_wait(60)
    sourceTitleAdv.send_keys('The New York Times')

    browser.implicitly_wait(60)

    browser.find_element_by_link_text('The New York Times').click()
    browser.implicitly_wait(60)

    sourceTitleAdv.clear()
    sourceTitleAdv.send_keys('Wall Street Journal Abstracts')

    browser.implicitly_wait(60)

    browser.find_element_by_link_text('Wall Street Journal Abstracts').click()
    browser.implicitly_wait(60)
    #click the apply button in the advanced search options
    applyButton=browser.find_element_by_id('OkButt').click()
    browser.implicitly_wait(20)

    #send the search terms to lexis nexis
    searchTerms=browser.find_element_by_id('terms')
    searchTerms.clear()
    browser.implicitly_wait(20)
    searchTerms.send_keys(company_name)
    #click the search button on the lexis nexis page
    submit_button=browser.find_element_by_id('srchButt').click()
    browser.implicitly_wait(3000)


    #check if no results found
    if checkIfNoResultsPageFound(browser)==True:
        return 0

    if exists_by_css_selector(browser,"frame[title='Results Navigation Frame']"):
        logging.debug('found results for the search')
        #Find the download link in the results page
        browser.switch_to.frame(browser.find_element_by_css_selector("frame[title='Results Navigation Frame']"))
        downloadDocs=browser.find_element_by_css_selector("img[title='Download Documents']")
        mainWindow=browser.current_window_handle
        browser.implicitly_wait(100)
        downloadDocs.click()
        #get the window which holds the link to download the page after pressing the save button in the search results
        popupWindowHandle=browser.window_handles[1]
        browser.switch_to.window(popupWindowHandle)
        #print(browser.page_source)
        # Find the title download
        browser.implicitly_wait(3000)
        #after the popup opens check if that hangs and does not respond
        popupPageSource=BeautifulSoup(browser.page_source).prettify()
        popupContainDownloadDocs= 'Download Documents' in popupPageSource
        if popupContainDownloadDocs==False:
            if ticker+date in noOfAttemptsDictionary:
                if noOfAttemptsDictionary[ticker+date]>2:
                    logging.info('ERROR:SEARCH FAILED:For the inputs ')
                    del noOfAttemptsDictionary[ticker+date]
                    browser.close()
                    browser.switch_to.window(mainWindow)
                    return 0
                noOfAttemptsDictionary[ticker+date]=noOfAttemptsDictionary[ticker+date]+1
                print('Tried searching...'+str(noOfAttemptsDictionary[ticker+date])+' times')
            else:
                  noOfAttemptsDictionary[ticker+date]=1
                  print('Tried searching...'+str(noOfAttemptsDictionary[ticker+date])+' times')
            print('retrying again.....')
            browser.close()
            browser.switch_to.window(mainWindow)
             #make sure that the after each search there is a random delay
            seconds = 5 + (random.random() * 5)
            time.sleep(seconds)
            try:
                downloadDocuments(browser,ticker,date,company_name)
            except (NoSuchElementException,ElementNotVisibleException,BaseException) as e:
                logging.info('ERROR:SEARCH FAILED:For the inputs ')
                return 0
            return 0



        downloadButton=browser.find_element_by_css_selector("img[title='Download']")
        downloadButton.click()
        downloadhref=browser.find_element_by_partial_link_text('.DOC').get_attribute('href')
        print(downloadhref)
        browser.find_element_by_partial_link_text('.DOC').click()
        browser.close()
        print('downloaded document')
        browser.switch_to.window(mainWindow)
    else:
        logging.warning('could not find documents for the search')
        return 0
    return 0


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
    logging.info('created firefox profile with the below parameters:')
    logging.info(profile.default_preferences)
    return profile

# function to read the source,date and company names from an input csv file
def readcsv(browser):
    f = open('ticker_company_small_sets.csv')
    csv_f = csv.reader(f)
    i=0
    for row in csv_f:
        if i==0:
            i=1
        else:
            # send the browser,ticker,date and company name details to download the documents
            logging.debug('current request'+row[0]+":"+row[1]+":"+row[2])
            print('current request'+row[0]+":"+row[1]+":"+row[2])
            print('startng download')
            try:
                x=downloadDocuments(browser,row[0],row[1],row[2])
            except (NoSuchElementException,ElementNotVisibleException,BaseException) as e:
                logging.info('ERROR:SEARCH FAILED')
                #make sure that the after each search there is a random delay
            seconds = 5 + (random.random() * 5)
            time.sleep(seconds)

    f.close()


def main():
    try:
        #Log the events in this log file
        logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
        coloredlogs.install()
        #create firefox profile
        profile = webdriver.FirefoxProfile()
        # update browser properties
        profile=createFireFoxProfile(profile)
        #create browser using the firefox profile created
        browser = webdriver.Firefox(firefox_profile=profile)
        #maximize the window
        browser.maximize_window()
        # read the csv file
        readcsv(browser)
        browser.close()
    except (ElementNotVisibleException,NoSuchElementException,BaseException) as exp:
        pass


try:
    main()
except (ElementNotVisibleException,NoSuchElementException,BaseException) as exp:
        pass


