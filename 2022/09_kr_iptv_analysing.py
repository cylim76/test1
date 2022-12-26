

import time

import requests

 '''
 把 IPTV-org m3u文件格式转换成便于查看的格式
 '''

url = 'https://iptv-org.github.io/iptv/countries/kr.m3u'
tvlistfile = requests.get(url)
filename = url.split('/')[-1]


with open(filename, 'wb', ) as f:
    f.write(tvlistfile.content)

# time.sleep(55)

with open('kr.m3u', 'r', encoding='utf8') as f:
    m3ulines  = f.readlines()



tv_list =[]

for i, line in enumerate(m3ulines):

    a = []
    b = []
    if i == 0:   
        head = line +'\n'
        continue 
    if 'EXTINF' in line: #i % 2 ==1:
        a=line.split(' ', maxsplit=3)
        b = a[-1].split(',')
        a[3] = b[0]
        a.append(b[1])
        tv_list.append(a)

    if 'EXTINF' not in line: #i% 2 == 0:
        tv_list[-1].append(line)


# print(head) 


# head = '#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/af.xml,https://iptv-org.github.io/epg/guides/ao.xml,https://iptv-org.github.io/epg/guides/ar.xml,https://iptv-org.github.io/epg/guides/ba.xml,https://iptv-org.github.io/epg/guides/cy.xml,https://iptv-org.github.io/epg/guides/cz.xml,https://iptv-org.github.io/epg/guides/kr.xml"\n\n'


with open (filename.split('.')[0] + '分析用.txt','w',encoding='utf-8-sig') as f:
    f.writelines(head)

    for i,channel in enumerate(tv_list):

        # if  channel[4].split('\n')[0] != keys: continue

        channel_info = str(i+1) + '\n' +channel[1] + '\n' + channel[4]  +channel[5] + '\n'  # id, logo, group, name, addr
        f.writelines(channel_info)



 

