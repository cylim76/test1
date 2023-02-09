#!/usr/bin/python3
# 笔趣阁爬虫练习 20230208
# 笔趣阁 https://www.xbiquge.so/

import requests
import parsel
import os

bookdir = './books/'
headers = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def get__book(book_url):
    #获取整本书目录
    response = requests.get(url = book_url,headers=headers)
    response.encoding ='gbk'
    sel = parsel.Selector(response.text)
    bookname = sel.css('#info h1::text').getall()[0]
    bookfolder = bookdir + bookname + '/'
    os.makedirs(bookfolder, exist_ok=True) 

    chapter_list = sel.css('#list dd a')    #.getall()

    for i,chapter in enumerate(chapter_list):
        # if i == pages : break   # for testing
        chapter_name = chapter.css('::text').get().replace('?','？').replace(':','：')
        chapter_url = book_url + chapter.css('::attr(href)').get()
        download_page(chapter_url, bookfolder)

def download_page(content_url,bookfolder):
    # 下载一个页面到指定文件夹
    response = requests.get(url = content_url,headers=headers)
    response.encoding ='gbk'
    sel = parsel.Selector(response.text)
    bookname = bookfolder.split('/')[-2]
    title = sel.css('.bookname h1::text').getall()[0]
    title_num =hanzi_num2arabic_num(title)
    content = sel.css('#content::text').getall()
    file_full_path = bookdir+ bookname + '/' + str(title_num)  + title + '.txt'

    with open(file_full_path, 'w', encoding='utf-8') as f:
        f.write(title + '\n\n')
        for c in content:
            f.write(c+ '\n')
            # print(c)
        print('下载成功 ----------： ' + title)

def hanzi_num2arabic_num(hanzi_num):
    hanzi_num_dict ={'一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '零':0 }
    hanzi_mul_dict = { '个':1, '十':10, '百':100, '千':1000, '万':10000 }
    hanzi_num_char = ['零','一','二','两','三','四','五','六','七','八','九','十','百','千','万']

    if not hanzi_num: return 0,0
    if ' ' in hanzi_num : hanzi_num = hanzi_num.split(' ')[0]   # 章节号有空格 先切片
    hanzi_num = hanzi_num.replace('张','章').replace('掌','章') # 错别字替换
    hanzi_num = list(hanzi_num)
    # print(hanzi_num)
    # if '第' not in hanzi_num or '章' not in hanzi_num : return 0,0

    for char in reversed(hanzi_num):
        if char not in hanzi_num_char:
            hanzi_num.remove(char)
            # print(hanzi_num)
    arabic_num = 0
    before_num = 0
    for i,h in enumerate(hanzi_num):
        if h == '零' :
            curr_num  =  hanzi_num_dict.get(h)
            before_num = curr_num
            curr_mul_num = 0
        elif hanzi_num_dict.get(h) and i+1  < len(hanzi_num) :
            curr_num  =  hanzi_num_dict.get(h)
            before_num = curr_num
            curr_mul_num = 0
        elif hanzi_num_dict.get(h) and i+1  == len(hanzi_num) :
            curr_num  =  hanzi_num_dict.get(h)
            arabic_num += curr_num
            break
        else:
            if hanzi_mul_dict.get(h):
                if before_num == 0: before_num =1
                curr_mul_num = before_num * hanzi_mul_dict.get(h)
        arabic_num += curr_mul_num
        
    # print(hanzi_num, arabic_num)
    return arabic_num

# pages = 15 # for testing
# pages = input('input pages number to download: ')



book_url =  input('input book\'s url addres : ')
# book_url = 'https://www.xbiquge.so/book/53406/'
get__book(book_url)
