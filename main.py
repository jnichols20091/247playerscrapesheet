import datetime
import re
import gspread

import requests, datetime, json,lxml
from bs4 import BeautifulSoup

gc = gspread.service_account(filename='service_account.json')
url = 'https://247sports.com/college/transfer-portal/Season/2023-Football/TransferPortal/'
wks = gc.open('gspreadtest').sheet1

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
# def get247():
#     for link in soup.find_all('li', class_='transfer-player'):
#         print(link.text)
#     else:
#         return None
# get247()
    # prin6t(link.text)
now = datetime.datetime.now()
now_str = now.strftime("%m/%d/%Y %H:%M:%S")
date = {
    "date": now_str
}
json_date = json.dumps(date)

wks.append_row([json_date])
for link in soup.find_all('li', class_='transfer-player'):
    x = re.sub('Rating', '', link.text)
    i = x.split(' ')[0:2]
    wks.append_row([i[0], i[1]])















