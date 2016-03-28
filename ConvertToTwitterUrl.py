import csv
import logging
import coloredlogs
from datetime import datetime, timedelta
import  os

__author__ = 'keerthikorvi'


def readcsv(urlwriter):
    f = open('Ticker Company Name Dates.csv')
    csv_f = csv.reader(f)
    i=0
    for row in csv_f:
        if i==0:
            i=1
        else:
            # send the browser,ticker,date and company name details to download the documents
            logging.debug('current request'+row[0]+":"+row[1]+":"+row[2])
            try:
                convertUrl(row[0],row[1],row[2],urlwriter)
            except BaseException as e:
                logging.debug('UrlConversionFailed')

    f.close()

def convertUrl(tickerSymbol,date,companyName,urlwriter):
    parsed_date = datetime.strptime(date, "%m/%d/%Y")
    since = (parsed_date - timedelta(days=1)).strftime("%Y-%m-%d")
    until = (parsed_date + timedelta(days=1)).strftime("%Y-%m-%d")
    companyNameTokens=companyName.split()
    companyNameParsed=""
    for i in range (0,len(companyNameTokens)):
        companyNameParsed=companyNameParsed+companyNameTokens[i]
        if(i<len(companyNameTokens)-1):
            companyNameParsed=companyNameParsed+'%20'
    actualUrl='https://twitter.com/search?q='+companyNameParsed+'%20lang%3Aen%20since%3A'+since+'%20until%3A'+until+'&src=typd&vertical=default&f=tweets&lang=en'
    urlwriter.writerow([tickerSymbol]+[date]+[companyName]+[actualUrl])
    logging.debug(actualUrl)
    #print(actualUrl)



logging.basicConfig(filename='twitterurllogfile.log',level=logging.DEBUG)
coloredlogs.install()
with open('TwitterUrlsFile.csv', 'w',newline='\n') as TwitterUrlsCsvFile:
    urlwriter = csv.writer(TwitterUrlsCsvFile, delimiter=',')
    readcsv(urlwriter)
