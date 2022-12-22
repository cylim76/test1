

import requests
from bs4 import BeautifulSoup
import re


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}   #Chrome
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"} # edge



#지정한 갯수만큼 서버 정보 가져오기
# 구독,  백업서버: 0번
from  ___mdms import get_host,get_server
qty_of_server = 2
hosts   = [get_host(i) for i in range(0,qty_of_server)] 
servers = [get_server(i) for i in range(0,qty_of_server)] 
urls    = [get_host(i)[0] for i in range(0,qty_of_server)]
files   = [get_server(i)[0] for i in range(0,qty_of_server)]


browser  = webdriver.Chrome()

for index,url in enumerate(urls):

    browser.get(url)

    time.sleep(4)
    namepw = browser.find_elements(By.CLASS_NAME,"ant-input")
    namepw[0].send_keys(get_host(index)[1])
    namepw[1].send_keys(get_host(index)[2])
    login = browser.find_element(By.TAG_NAME,"button")
    login.click()


    # driver.save_screenshot('91_login.png')
    time.sleep(2)
    # 进入入站列表
    url = url + 'xui/inbounds'
    browser.get(url)


    time.sleep(3)
    #爬取页面信息的练习
    head ="操作 启用 id 备注 协议 端口 流量↑|↓ 详细信息 传输配置 到期时间".split(" ")

    list =[]
    list.append(head)
    inbounds = browser.find_elements(By.TAG_NAME,'tr')
    for i, inbound in enumerate(inbounds):
        if i ==0 :   continue # 跳过第一个空值
        entry = inbound.find_elements(By.TAG_NAME,'td')
        e = []
        
        for j,col in enumerate(entry):
            # print(i,j,len(entry),col.text)
            # 在requests的 beautifulsoup 에서 속성은 element['attr'] 或者 element.get('attr') 调用
            # 在selenium的 brouser.page_source  通过 .get_attribute('attr') 函数调用
            if j == 1 : 
                onoff = col.find_element(By.TAG_NAME,"button").get_attribute('aria-checked')
                if onoff == 'true':
                    e.append("on")
                else:
                    e.append("off")
                continue

            # print()
            e.append(col.text)      # e는 리스트로 생성된다

        # e[1]= col.get_attibute("aria-checked")
        list.append(e)



        
    for i,inbound in enumerate(list):
        print(i,inbound)

    # 保存到 csv 文件    
    sublinkfilename = './' + files[index].split('.')[0] + '爬取练习.csv'
    with open(sublinkfilename, "w", encoding="utf-8-sig",newline="") as f:
        csv.writer(f).writerows(list)
        print('{}文件保存成功!'.format(sublinkfilename))
        
        
    # 保存到 excel 文件
    import pandas
    sublinkfilename = './' + files[index].split('.')[0] + '爬取练习.xlsx'
    pd = pandas.DataFrame(list)
    pd.to_excel(sublinkfilename, sheet_name='节点信息', index=False, header=False) 



# 登出X-ui面板
menu = browser.find_elements(By.TAG_NAME,'li')
menu[4].click()

#关闭浏览器
browser.close()





 

