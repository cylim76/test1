# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:49:48 2018

@author: qinglong.lin
"""


import urllib.request as uuu
import os
import time
import re

try:
    print('''
          此应用用来测试下载网络文件,
          以h公司人事系统照片为测试对象
          输入社号区间及保存的文件夹名称后下载.
          (直接按回车按默认值开始)
          ''')
    startid = input('请输入开始的社号(如: 10000):')
    if startid == '': startid = 10000
    else : startid = int(startid)
    endid = input('请输入截止社号(如: 12000)')
    if endid == '': endid = 12000
    else: endid = (int(endid))

    rrr = re.findall(r'\w*\.(\w{6})',str(time.time()))


    hdir = input('请输入要保存的文件夹名(如: hphoto): ')
    if hdir == '': hdir = 'hphoto'+"("+ rrr[0] + ")"
    else: hdir = hdir +"("+ rrr[0] + ")"
    os.mkdir(hdir +"(%s -%s)" % (startid,endid))
    pdir = hdir +"(%s -%s)" % (startid,endid)
    
    stopid = 0
    print("开始下载并保存照片到当前目录 %s文件夹下" % pdir)
    for x in range(startid,endid+1):
            try: 
                if stopid == 10:
                    print('后面大概没有照片了')
                    break
                url ="http://156.147.36.82:7781/filedown/photo/" +str(x) +".gif"
            
#            if  uuu.urlopen(url).code  == 'Not Found':
#                continue
                uuu.urlretrieve(url,pdir + '\\'+str(x)+ '.gif') 
                print('照片 %s 下载成功' % (str(x)+ '.gif'))
                f1 = open(pdir + '\\list%s-%s.txt' % (startid,endid),'a+')
                f1.write('照片 %s 下载成功\n' % (str(x)+ '.gif'))
                f1.close()
                stopid =0
            except:
                print('社号 %s 不存在' % str(x))   
                stopid +=1
                continue
     
    input("测试结束,按'Enter'键退出")
except:   
    print('输入信息有误')
    input("测试结束,按'Enter'键退出")
#   import requestscode=requests.get("http://www.baidu.com").status_code
#   print code

