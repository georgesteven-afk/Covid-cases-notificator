import requests
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
from urllib.request import urlopen, Request
#importing required libs 

header = {"User-agent":"George"}
res = Request('https://www.worldometers.info/coronavirus/country/india/', headers = header)
html = urlopen(res)

obj = bs(html)

new_cases_today = obj.find('li', {"class":"news_li"}).strong.text.split()[0]
#creating a variable for newcases

new_deaths_today = list(obj.find('li', {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
#creating a variable for newdeaths

new_deaths_today

notifier = ToastNotifier()
dis_msg = "New_Cases: "+new_cases_today+"\nDeaths: "+new_deaths_today

dis_msg

notifier.show_toast(title="Corona cases update", msg=dis_msg)
