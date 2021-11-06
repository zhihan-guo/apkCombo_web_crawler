'''
Author: Guo Zhihan
Date: 2021-10-26 11:22:34
LastEditors: Guo Zhihan
LastEditTime: 2021-10-26 12:18:07
Description: file content
FilePath: falseundefinedd:falsePhDfalseappfalsegetAppUrls.py
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

ROW = []
headers = { 'cookie': 'OGPC=19022591-1:; SEARCH_SAMESITE=CgQIlZMB; _ga=GA1.3.1237261510.1635081802; _gid=GA1.3.2065717507.1635081802; OTZ=6212963_24_24__24_; SID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu_C-80ETG-sZzsOEgJeqvgw.; __Secure-1PSID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu9LUCyllIpXjoboHS5z39KQ.; __Secure-3PSID=DQh0o1900G1Ke8wsN_YAEqVwWJbCrs-5sfjIhTsF4oOW9RCu1QVbynNzQUZLh2ydxrqrkg.; HSID=AfleN2kPDhiRV8b3o; SSID=AfJUvuYYZoIwkl4oI; APISID=aqvXqLHQJtI9jGjU/AKrEMi6GQVxEjQlyu; SAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; __Secure-1PAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; __Secure-3PAPISID=NAA47PQZjff151of/A-yy5ZTKok8nulS3n; 1P_JAR=2021-10-25-12; _gac_UA-19995903-1=1.1635165364.CjwKCAjwq9mLBhB2EiwAuYdMtfZJg07aQ8_WvDdegCNRI6INfCz_CmGTCjVoIVRXvI1XF0Q5SzV7ThoCV8QQAvD_BwE; NID=511=eWl6Q11myPWSUIORd9rhsDjw6TGZS-FzG0R5na1JGIrV_aT_yiENBo-kwzbh4rdqSoS2_-e61i8x2YhigfhFudVdmEOQ6kzZ6xXv-uE_XmeGm245o8vkn3IIMii0P3CP4f1ky1ZmRfZk7u0RpZ4_mHOJ9jhAGrBbnGtupivh42tvRn5kPLRVCKPfg2y4Avax08RIDRJ3bQ1UIZGFP7qxDSVmhAsgnEeIaMHx4Y-FKQZ0AvduPXjCz6ZHfZke6a0KZk8CZvmNCkyRH4YtcdlSathJJA0CkcCoKIR8tQNZt40m; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=authuser-0; SIDCC=AJi4QfFxKCxzkHXAqK-VozbOIjbyCKWV8eRddSoWZFJ9waBvf9OUFk3TOV9qyV4xhdwel514bYM; __Secure-3PSIDCC=AJi4QfHPygWnAXRtqVo_jyCzzKzXW2cFITf7H9rD1KmUzoyjVi52dN76s0WcK4jhLxBOoIx5hBTF', 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'referer': 'https://play.google.com/'}
file = open('D://appListurls.txt','r')
for url in file.readlines():
    url = url.strip('\n')
    response = requests.get(url, headers = headers)
    print(url, response.status_code)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("C:\\Program Files\Google\Chrome\Application\chromedriver.exe", options = options)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    tree = etree.HTML(response.text)
    try:
        appNames = tree.xpath('//*[@class = "WsMG1c nnK0zc"]/text()')
        appCompanys = tree.xpath('//*[@class = "KoLSrc"]/text()')
        print(appNames)
        print(appCompanys)
        # for i in urls:
        #     urlList.append(i)
    except:
        appNames = ''
        appCompanys = ''
    for i in range(len(appNames)):
        app_dict = { 
                        "appNames": appNames[i],
                        "appCompanys": appCompanys[i]
                    }
        ROW.append(app_dict)

df = pd.DataFrame(ROW)
df.to_excel("D:\\AppInformation.xlsx")
