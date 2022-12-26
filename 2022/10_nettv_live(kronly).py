
from selenium import webdriver
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup

import lxml
import time

import csv
import random

import pyautogui
import tkinter
import tkinter.messagebox as msgbox

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
           # "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6",
            #"Accept-Encoding":"gzip, deflate"
}   #Chrome

def make_channel_page_dict(page):
    #输入页号， 下载保存页面中的频道主页网址
    temp_channel_dict = {}
    channel_number = 1
    for i in range(page,page + 1):
        
        pageurl = 'http://nettv.live/Asia/Korea/' + 'list_{}.html'.format(i)
        time.sleep(1)

        res = requests.get(pageurl,headers=headers,timeout=30)
        res.raise_for_status()
    
        soup = BeautifulSoup(res.content.decode('utf8','replace'), "lxml")
        channels = soup.find_all('div', attrs={'class':'col-xl-3 col-lg-4 col-sm-6'}) 
        
        for i, channel in enumerate(channels):
            channel_name = channel.find('img').get('alt')
            channel_page = 'http://nettv.live' + channel.find('a').get('href')
            print('{}channel_name: {} ,channel_page:  {}'.format(channel_number, channel_name,channel_page))
            temp_channel_dict[channel_name]= channel_page
            channel_number +=1

    page_links_filename = './01_nettv_live/Korea/channel_pg_list_{}.csv'.format(page)
    with open(page_links_filename,'w',encoding='utf-8-sig',newline='') as csvfile:
        writer =  csv.writer(csvfile)
        for channel in temp_channel_dict.items():
            writer.writerow(channel)




# print('채널 총수: {} \n{}'.format(len(channel_list),channel_list))
# # selenium 方法
# browser = webdriver.Chrome()
# browser.get(channel_pages.get(channel_list[0]))
# time.sleep(1)
# logo = browser.find_element(By.CLASS_NAME, 'img-thumbnail').get_attribute('src')
# addrs = browser.find_element(By.CLASS_NAME, 'video-meta').find_element(By.TAG_NAME,'a').get_attribute('onclick')



# requests 方法
def chn_pg_to_chn_m3u_list_csvfile(page):

    # 读取频道列表csv 文件 --> pagelist 变量
    pg_csvfile = './01_nettv_live/Korea/channel_pg_list_{}.csv'.format(page)  
    with open(pg_csvfile,'r',encoding = 'utf-8-sig', newline='\n') as f:
        reader = csv.reader(f)
        pagelist = list(reader)

    temp_nettv_live = []
    channel_number = 1
    for channel in pagelist:
        interval = random.randint(1,3)
        time.sleep(interval)
        res = requests.get(channel[1],headers=headers,timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        # logo = 'http://nettv.live/' + soup.find('img', attrs={'class':'img-thumbnail'}).get('src')
        # print('logo addres: {}'.format(logo))

        addrs = soup.find('ul', attrs={'class':'video-meta'}).find_all('a')
        for i, addr in enumerate(addrs):
            if i == 7 : break
            # stopsignal =['wuxianlu','error.php']
            # if any(signal  in addr.get('onclick') for signal in stopsignal) : break
            # if 'm3u8' not in addr.get('onclick') : break
            # addrlink = addr.get('onclick').split('url=')[1].split('&')[0]
            addrlink = 'http' + addr.get('onclick')
            print('{},{} 直播地址： {}'.format(channel_number,channel[0], addrlink))
            channel_number +=1
            temp_nettv_live.append([channel[0], addrlink]) # dictionary 添加的方法
            # nettv_live.append([channel,addrlink])  # list 添加的方法

    m3u_addr_filename = './01_nettv_live/Korea/channel_pg_list_{}m3u.csv'.format(page)
    with open(m3u_addr_filename,'w',encoding='utf-8-sig',newline='') as csvfile:
        writer =  csv.writer(csvfile)
        for channel_m3u in temp_nettv_live:
            writer.writerow(channel_m3u)


def merge_m3u_files(outputfilename):
    # 把 11개의 m3u 文件合并成一个文件
    totallist = []
    for i in range(1,12):
        templist = []
        m3u_addr_filename = './01_nettv_live/Korea/channel_pg_list_{}m3u.csv'.format(i)
        print(m3u_addr_filename)
        with open(m3u_addr_filename,'r',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            templist =list(reader)
            # print(templist)
            # time.sleep(1)
        totallist.extend(templist)
        print(len(totallist))

    with open(outputfilename,'w',encoding = 'utf-8-sig', newline='\n') as f:
        writer = csv.writer(f)
        for channel in totallist:
            writer.writerow(channel)
 

def washing_data(input_filename):
    output_filename = input_filename.split('.csv')[0] + '최종.csv'
    # 다운받은 링크파일을 정리하여 csv 파일로 저장
    with open(input_filename,'r',encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        templist =list(reader)
        print(len(templist))

    count = 0
    for i in range(len(templist)-1,-1,-1):
        #  무효한 링크 삭제
        delflag = ['wuxianlu','error','wuxianhao','wap.html']
        if any(x in templist[i][1] for x in delflag):
            # print(i,templist[i])
            templist.remove(templist[i])
            count += 1
    print('{}개 무효한 링크 삭제'.format(count))

    count = 0
    for i in range(len(templist)-1,-1,-1):
        # 링크중 url= 와 m3u8 이 있는 경우 링크 잘라서 업데이트
        if 'url='in templist[i][1] and 'm3u8' in templist[i][1] :
            templist[i][1] = templist[i][1].split('url=')[1].split('m3u8')[0] +'m3u8'
            templist[i][0] = '★ ' + templist[i][0]
            count += 1
    print('{}개 링크중 url= 와 m3u8 이 있는 경우 링크 잘라서 업데이트 '.format(count))

    count = 0
    for i in range(len(templist)-1,-1,-1):
        # "httpframe('/embed"  로 시작되는 링크 앞부분 보완하고 뒷부분 잘라주기
        if  templist[i][1].startswith("httpframe('/embed") :
            templist[i][1] = 'http://nettv.live/' + templist[i][1].split("httpframe('/")[1].split("','")[0]
            templist[i][0] = '★ ' + templist[i][0]
            count += 1
    print('{}개 링크중 "httpframe(\'/embed"  로 시작되는 링크 앞부분 보완하고 뒷부분 잘라주기'.format(count))

    count = 0
    for i in range(len(templist)-1,-1,-1):
        # "httpframe('/player" 로 시작되는 링크 앞뒤 자르기
        if  templist[i][1].startswith("httpframe('/player") :
            templist[i][1] = templist[i][1].split("url=")[1].split("','")[0]
            templist[i][0] = '★ ' + templist[i][0]
            count += 1
    print('{}개 링크 "httpframe(\'/player" 로 시작되는 링크 앞뒤 자르기 함'.format(count))

    count = 0
    for i in range(len(templist)-1,-1,-1):
        # "httpframe('/rtmp" 로 시작되는 링크 앞뒤 자르기
        if  templist[i][1].startswith("httpframe('/rtmp") :
            templist[i][1] = templist[i][1].split("url=")[1].split("','")[0]
            templist[i][0] = '★ ' + templist[i][0]
            count += 1
    print('{}개 링크 "httpframe(\'/rtmp" 로 시작되는 링크 앞뒤 자르기 함'.format(count))

    count = 0
    for i in range(len(templist)-1,-1,-1):
        # "httpframe('http" 로 시작되는 링크 앞뒤 자르기
        if  templist[i][1].startswith("httpframe('http") :
            templist[i][1] = templist[i][1].split("httpframe('")[1].split("','")[0]
            templist[i][0] = '★ ' + templist[i][0]
            count += 1
    print('{}개 링크 httpframe(\'http" 로 시작되는 링크 앞뒤 자르기 함'.format(count))

    # 정상적인 파일 저장
    with open(output_filename,'w',encoding = 'utf-8-sig', newline='\n') as f:
        writer = csv.writer(f)
        for channel in templist:
            writer.writerow(channel)
        print(len(templist))

    # # 오류 데이타만 저장(테스트 용)
    # with open('./01_nettv_live/임시m3u파일.csv','w',encoding = 'utf-8-sig', newline='\n') as f:
    #     writer = csv.writer(f)
    #     i = 0
    #     for channel in templist:
    #         if '★' not in channel[0]:
    #             writer.writerow(channel)
    #             i += 1
    #             print(channel)
    #     print(i)
    time.sleep(1)







def btncmd1():
    page = int(listbox1.selection_get().split('page')[1])
    # print(type(page),page)
    make_channel_page_dict(page)
    msgbox.showinfo( 'confirm', 'Page' + str(page) + '的电台网址保存成功')

def btncmd2():
    page = int(listbox1.selection_get().split('page')[1])
    print(type(page),page)
    chn_pg_to_chn_m3u_list_csvfile(page)
    msgbox.showinfo( 'confirm', 'Page' + str(page) + '的电台直播地址抓取成功')

def btncmd3():
    outputfilename = './01_nettv_live/Korea/channel_pg_list_m3u.csv'
    merge_m3u_files(outputfilename)
    msgbox.showinfo('confirm', 'm3u8 파일들을 합병하여 {}에 저장하였습니다.'.format(outputfilename))

def btncmd4():
    input_filename = './01_nettv_live/Korea/channel_pg_list_m3u.csv'
    output_filename = output_filename = input_filename.split('.csv')[0] + '최종.csv'
    washing_data(input_filename)
    msgbox.showinfo('confirm', 'm3u8 파일들을 합병하여 {}에 저장하였습니다.'.format(output_filename))

root = tkinter.Tk()
root.title ('NetTV.Live 直播网址爬取')
root.geometry('400x500')

listbox1 = tkinter.Listbox(root, selectmode='single',height = 11)
listbox1.insert(0,'page1','page2','page3','page4','page5','page6','page7','page8','page9','page10','page11')


listbox1.pack()

btn1 = tkinter.Button(root,padx=5,pady=5,width = 20, height = 2, text='获取电台主页', command= btncmd1).pack()
btn2 = tkinter.Button(root,padx=5,pady=5,width = 20, height = 2,text='获取直播网址', command= btncmd2).pack()
btn3 = tkinter.Button(root,padx=5,pady=5,width = 20, height = 2,text='m3u8 파일 병합', command= btncmd3).pack()
btn4 = tkinter.Button(root,padx=5,pady=5,width = 20, height = 2,text='링크세탁', command= btncmd4).pack()




root.mainloop()



# 运行
# # 1. 保存频道页面网址,保存为csv文件
# page = pyautogui.prompt(title = 'Please input page numbernumber(1-11) : ',text = '输入页码以抓取频道主页网址') 
# make_channel_page_dict(page)


# # 2. 读取页面文件并下载 频道直播网址,保存为csv文件
# page = pyautogui.prompt(title = 'Please input page numbernumber(1-11) : ',text = '输入页码以生成 m3u 直播网址列表') 
# chn_pg_to_chn_m3u_list_csvfile(page)


# # 3. 파일을 합치기
# outputfilename = './01_nettv_live/Korea/channel_pg_list_m3u.csv'
# merge_m3u_files(outputfilename)


# # 4. m3u link 파일을 세탁하기
input_filename = './01_nettv_live/Korea/channel_pg_list_m3u.csv'

# washing_data(input_filename)
