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


def download_page(content_url,bookfolder):
    # 下载一个页面到指定文件夹
    response = requests.get(url = content_url,headers=headers)
    response.encoding ='gbk'
    sel = parsel.Selector(response.text)
    bookname = bookfolder.split('/')[-2]
    title = sel.css('.bookname h1::text').getall()
    content = sel.css('#content::text').getall()
    file_full_path = bookdir + bookname + '/' + title[0] + '.txt'

    with open(file_full_path, 'w', encoding='utf-8') as f:
        f.write(title[0]+ '\n\n')
        for c in content:
            f.write(c+ '\n')
            # print(c)
        print('下载成功 ----------： ' + title[0])




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

# pages = 15 # for testing
# pages = input('input pages number to download: ')



book_url =  input('input book\'s url addres : ')
# book_url = 'https://www.xbiquge.so/book/53406/'
get__book(book_url)
