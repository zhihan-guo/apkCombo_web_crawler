'''
Author: Guo Zhihan
Date: 2021-10-26 20:18:30
LastEditors: Guo Zhihan
LastEditTime: 2021-10-29 20:05:03
Description: file content
FilePath: falseundefinedd:falsePhDfalseappfalseAPKComboCategoryurls.py
'''

import requests
from lxml import etree
import pickle
import sys
import os
import pandas as pd
import multiprocessing
import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# get categoryUrls

ROW = []
fileRead = open('D://categoryurls.txt', 'r')
fileWrite = open('D://APKComboCategoryurls.txt', 'w')
headers = { 'cookie': 'OGPC=19022591-1:; SEARCH_SAMESITE=CgQIlZMB; _ga=GA1.3.1237261510.1635081802; _gid=GA1.3.2065717507.1635081802; OTZ=6212963_24_24__24_; SID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu_C-80ETG-sZzsOEgJeqvgw.; __Secure-1PSID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu9LUCyllIpXjoboHS5z39KQ.; __Secure-3PSID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu1QVbynNzQUZLh2ydxrqrkg.; HSID=AfleN2kPDhiRV8b3o; SSID=AfJUvuYYZoIwkl4oI; APISID=aqvXqLHQJtI9jGjU/AKrEMi6GQVxEjQlyu; SAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; __Secure-1PAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; __Secure-3PAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; 1P_JAR=2021-10-25-12; _gac_UA-19995903-1=1.1635165364.CjwKCAjwq9mLBhB2EiwAuYdMtfZJg07aQ8_WvDdegCNRI6INfCz_CmGTCjVoIVRXvI1XF0Q5SzV7ThoCV8QQAvD_BwE; NID=511=eWl6Q11myPWSUIORd9rhsDjw6TGZS-FzG0R5na1JGIrV_aT_yiENBo-kwzbh4rdqSoS2_-e61i8x2YhigfhFudVdmEOQ6kzZ6xXv-uE_XmeGm245o8vkn3IIMii0P3CP4f1ky1ZmRfZk7u0RpZ4_mHOJ9jhAGrBbnGtupivh42tvRn5kPLRVCKPfg2y4Avax08RIDRJ3bQ1UIZGFP7qxDSVmhAsgnEeIaMHx4Y-FKQZ0AvduPXjCz6ZHfZke6a0KZk8CZvmNCkyRH4YtcdlSathJJA0CkcCoKIR8tQNZt40m; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=authuser-0; SIDCC=AJi4QfFxKCxzkHXAqK-VozbOIjbyCKWV8eRddSoWZFJ9waBvf9OUFk3TOV9qyV4xhdwel514bYM; __Secure-3PSIDCC=AJi4QfHPygWnAXRtqVo_jyCzzKzXW2cFITf7H9rD1KmUzoyjVi52dN76s0WcK4jhLxBOoIx5hBTF', 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'referer': 'https://apkcombo.com/category/'}

for url in fileRead.readlines():
    url = url.strip('\n')
    newUrl = 'https://apkcombo.com' + url
    ROW.append(newUrl)

# filehandler = open("D://APKComboCategoryurls.pkl", "wb")
# pickle.dump(ROW, filehandler)
# filehandler.close()

categoryUrls = []

for url in ROW:
    # print(url)
    response = requests.get(url, headers = headers)
    tree = etree.HTML(response.text)
    moreUrls = tree.xpath('//*[@class="column is-12"]//*[@class="more"]/a/@href')
    for moreUrl in moreUrls:
        moreUrl = moreUrl.strip('\n')
        moreUrl = 'https://apkcombo.com' + moreUrl
        categoryUrls.append(moreUrl)

filehandler = open("D://url_category.pkl", "wb")
pickle.dump(categoryUrls,filehandler)
filehandler.close()

# get appUrls

# filehandler = open("D://url_category.pkl","rb")
# moreUrl = pickle.load(filehandler)
# filehandler.close()

# headers1 = {
#     'Referer': 'https://apkcombo.com/category/auto-and-vehicles/top-grossing/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#     'cookie': 'OGPC=19022591-1:; SEARCH_SAMESITE=CgQIlZMB; _ga=GA1.3.1237261510.1635081802; _gid=GA1.3.2065717507.1635081802; OTZ=6212963_24_24__24_; SID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu_C-80ETG-sZzsOEgJeqvgw.; __Secure-1PSID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu9LUCyllIpXjoboHS5z39KQ.; __Secure-3PSID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu1QVbynNzQUZLh2ydxrqrkg.; HSID=AfleN2kPDhiRV8b3o; SSID=AfJUvuYYZoIwkl4oI; APISID=aqvXqLHQJtI9jGjU/AKrEMi6GQVxEjQlyu; SAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; __Secure-1PAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; __Secure-3PAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; 1P_JAR=2021-10-25-12; _gac_UA-19995903-1=1.1635165364.CjwKCAjwq9mLBhB2EiwAuYdMtfZJg07aQ8_WvDdegCNRI6INfCz_CmGTCjVoIVRXvI1XF0Q5SzV7ThoCV8QQAvD_BwE; NID=511=eWl6Q11myPWSUIORd9rhsDjw6TGZS-FzG0R5na1JGIrV_aT_yiENBo-kwzbh4rdqSoS2_-e61i8x2YhigfhFudVdmEOQ6kzZ6xXv-uE_XmeGm245o8vkn3IIMii0P3CP4f1ky1ZmRfZk7u0RpZ4_mHOJ9jhAGrBbnGtupivh42tvRn5kPLRVCKPfg2y4Avax08RIDRJ3bQ1UIZGFP7qxDSVmhAsgnEeIaMHx4Y-FKQZ0AvduPXjCz6ZHfZke6a0KZk8CZvmNCkyRH4YtcdlSathJJA0CkcCoKIR8tQNZt40m; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=authuser-0; SIDCC=AJi4QfFxKCxzkHXAqK-VozbOIjbyCKWV8eRddSoWZFJ9waBvf9OUFk3TOV9qyV4xhdwel514bYM; __Secure-3PSIDCC=AJi4QfHPygWnAXRtqVo_jyCzzKzXW2cFITf7H9rD1KmUzoyjVi52dN76s0WcK4jhLxBOoIx5hBTF', 
# }

# length = len(moreUrl)
# for count in range(length):
#     appUrls = []
#     url = moreUrl[count].strip('\n')
#     # print(url)
#     i = 1
#     while True:
#         newUrl = url + '?page=' + str(i)
#         response = requests.get(newUrl, headers = headers1)
#         if response.status_code != 200:
#             break
#         tree = etree.HTML(response.text)
#         appContents = tree.xpath('//*[@class = "content content-apps"]/a/@href')
#         for appContent in appContents:
#             # print(appContent)
#             appUrl = appContent.strip('\n')
#             appUrl = 'https://apkcombo.com' + appUrl
#             # print(appUrl)
#             appUrls.append(appUrl)
#         i += 1
#     # print(count)
#     filehandler = open("D://url_{}.pkl".format(count),"wb")
#     pickle.dump(appUrls,filehandler)
#     filehandler.close()

# get app description



# headers2 = {
#     'cookie': '__gads=ID=7f41b88e96173414-2272d9ebe6cc0013:T=1635249776:RT=1635249776:S=ALNI_MaytH3HaWUecGP1x8K3frZwK8ZOzA; _ga=GA1.2.1191057358.1635249776; _gid=GA1.2.66160981.1635249778; __apkcombo_lang=en',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# }

# for num in range(1, 322):
#     appDiscription = []

#     filehandler = open("D://appUrl/url_{}.pkl".format(num),"rb")
#     appUrls = pickle.load(filehandler)
#     filehandler.close()

#     length = len(appUrls)
#     for i in range(length):
#         response = requests.get(appUrls[i], headers = headers2)
#         appContent = etree.HTML(response.text)
#         try:
#             appName = appContent.xpath('//div[@class="info"]/div[@class="app_name"]/h1/text()')[0]
#         except:
#             appName = ''
        
#         try:
#             appAuthor = appContent.xpath('//div[@class="info"]/div[@class="author"]/a[@class="is-link"]/text()')[0]
#         except:
#             appAuthor = ''

#         try:
#             appAuthorUrl = appContent.xpath('//div[@class="info"]/div[@class="author"]/a[@class="is-link"]/@href')[0]
#             appAuthorUrl = 'https://apkcombo.com' + appAuthorUrl
#         except:
#             appAuthorUrl = ''

#         try:
#             appDownloadUrl = appContent.xpath('//div[@class="button-group mt-14 mb-20 is-mobile-only"]/a[@class="button is-success is-fullwidth"]/@href')[0]
#             appDownloadUrl = 'https://apkcombo.com' + appDownloadUrl
#         except:
#             appDownloadUrl = ''
#         # print('appName:', appName, '\nappUrl:', appUrls[i], '\nappAuthor:', appAuthor, '\nappAuthorUrl:', appAuthorUrl, '\nappDownloadUrl:', appDownloadUrl)
#         # break

#         appDict = {
#             'appName': appName,
#             'appUrl': appUrls[i],
#             'appAuthor': appAuthor,
#             'appAuthorUrl': appAuthorUrl,
#             'appDownloadUrl': appDownloadUrl
#         }
#         # print(appDict)
#         appDiscription.append(appDict)
#         if i % 50 == 0:
#             print('file: ', num, ', length: ', length, ', now: ', i)

#     df = pd.DataFrame(appDiscription)
#     df.to_excel("D://appDescription/app_{}.xlsx".format(num))


# Merge Excel
# import pandas as pd
# excel_dir = Path("D://appDescription/")
# excel_dir = Path("D://test/")
# excel_files = excel_dir.glob('*.xlsx')

# df = pd.DataFrame()
# count = 0
# for xls in excel_files:
#     print(count)
#     data = pd.read_excel(xls)
#     df = df.append(data)
#     count += 1

# df.to_excel("D://test1/output7.xlsx")

# import csv
# f = open('D://output.csv','w')
# csv_writer = csv.writer(f)
# csv_writer.writerow(['appName',	'appUrl', 'appAuthor', 'appAuthorUrl', 'appDownloadUrl'])

# De-duplication
# df = pd.read_csv('D://App_df.csv')
# df = df.drop_duplicates(subset='appName', keep='last')
