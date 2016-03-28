#__author__ = 'keerthikorvi'
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://pyladies.com/')
print(str.__contains__('Python',r.data) )
print(r.status)
print(r.data)
