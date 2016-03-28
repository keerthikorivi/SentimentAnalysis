#__author__ = 'keerthikorvi'
import requests
from requests import  session
from bs4 import BeautifulSoup



#r=requests.get("http://www.lexisnexis.com.er.lib.k-state.edu/lnacui2api/results/docview/docview.do?docLinkInd=true&risb=21_T22141316825&format=GNBFI&sort=RELEVANCE&startDocNo=1&resultsUrlKey=29_T22141316829&cisb=22_T22141316828&treeMax=true&treeWidth=0&csi=279934&docNo=4")
params={
    'user':'keerthik',
    'pass':'Keer300391'
}
s=requests.session()

r=s.post("https://login.er.lib.k-state.edu/login",params)
p=s.get("http://www.lexisnexis.com.er.lib.k-state.edu/lnacui2api/results/docview/docview.do?docLinkInd=true&risb=21_T22141715907&format=GNBFI&sort=RELEVANCE&startDocNo=1&resultsUrlKey=29_T22141715911&cisb=22_T22141715910&treeMax=true&treeWidth=0&csi=6742&docNo=1")


#https://er.lib.k-state.edu/login?url=http://www.lexisnexis.com/hottopics/lnacademic/?
soup=BeautifulSoup(p.content)
print(soup.prettify());
#listvalues=soup.find_all("div")
#print(listvalues)


