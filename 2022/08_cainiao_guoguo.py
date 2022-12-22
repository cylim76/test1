
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as waitfor 
from selenium. webdriver.support import expected_conditions as expc
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
import csv

import time
url ='https://www.guoguo-app.com/'

chrome_options = Options()
chrome_options.add_argument("log-level=3")
chrome_options.add_argument("log-level=3") # 终端不显示 错误提示 SSL error code 1


browser = webdriver.Chrome(options = chrome_options)
browser.get(url)
time.sleep(5)

'''
菜鸟裹裹主页快递公司

'''

page = browser.page_source


soup = BeautifulSoup(page,'lxml')

cps = soup.find('div',attrs={'id':'J_ExpressCompanyList'}).find_all('a')
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
 
cp_list =[['No', '快递公司名称({}家)'.format(len(cps))]]
print(cp_list[0][0],cp_list[0][1])
for index, cp in enumerate(cps):
    cp_list.append([index+1, cp['title']])
    print(index+1, cp['title'])

# # 写入文件的方法1, csv模块写入
# with open ('cplist.csv','w',encoding='utf-8-sig',newline= "") as f:
#     csv.writer(f).writerows(cp_list) # writerrows 函数一次写入整个list
    

# # 写入csv文件的方法2,  pandas模块写入
# pd = pandas.DataFrame(cp_list)
# pd.to_csv('cplist.csv')

# # 写入excel文件的方法,  pandas模块写入
# import pandas
# pd = pandas.DataFrame(cp_list)
# pd.to_excel('cplist.xlsx', sheet_name='快递公司', index=False, header=False) 

#element.location_once_scrolled_into_view 
time.sleep(2)
