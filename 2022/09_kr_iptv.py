
import time
import requests


'''
https://iptv-org.github.io/iptv/countries/kr.m3u 

파일을 가져와서 필요한 채널들만 골라
순서를 정렬하고 채널 이름을 보기좋게 바꾼다

'''

url = 'https://iptv-org.github.io/iptv/countries/kr.m3u'
m3ufile = requests.get(url)
filename = url.split('/')[-1]
with open(filename, 'wb', ) as f:
    f.write(m3ufile.content)
time.sleep(2)
with open(filename, 'r', encoding='utf8') as f:
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

    if  'EXTINF' not in line: 
        tv_list[-1].append(line)

my_channels={

    #--- popular channels --
    'KBS1 (720p)':'KBS1',
    'KBS2 (720p) [Not 24/7]':'KBS2',
    'KBS Drama (480p)':'KBS 드라마',
    'MBC (1080p) [Not 24/7]':'MBC',
    'EBS 1 (400p)':'EBS1',
    'KBS Joy (480p)':'KBS 예능',
    'KBS Life (480p)':'KBS 라이프',
    'KBS News D (720p)':'KBS 뉴스D',
    'KBS Story (480p)':'KBS 스토리',
    'Korea TV':'KTV 국민방송',
    'Korean Election TV':'한국선거방송',


    'Mnet (540p)':'M-net',
    'Korean Song Channel':'한국가요',
    'GugakTV 국악방송 (1080p)':'국악방송',
    
    'KBS Kids (480p)': 'KBS 어린이',
    'Daekyo Kids TV (540p)':'대교 어린이',
    'EBS kids (400p)':'EBS 어린이',
    'Pinkfong (540p)':'핑크퐁 어린이',
    'Tooniverse (540p)':'투니버스 어린이', 

    'Carrie TV (540p)':'채널A', # 임시 오류 링크..
    'Channel China (1080p)':'FTV 낚시', # 임시 오류 링크..
    'OLIFE (540p)':'OLife 여행', 
    'Gusto TV (1080p)':'Gusto 미식가',
    'Chunghwa TV (540p)':'중화티비',
    'Cinema Heaven (540p)':'시네마천국',
    'iHQ drama (540p)':'iHQ 드라마',


    'MTN (720p)':'MTN 머니투데이',
    'NHTV (720p)':'NGTV 농협방송',
    'NBS Korea Agricultural Broadcasting (720p)':'NBS 농업방송',
    'National Assembly TV (720p)':'한국국회방송',
    'NEC ETV 한국선거방송 (720p)':'NEC한국선거방송◐',
    'Gugbang TV (1080p) [Not 24/7]':'국방TV',
    'TVWorkNet (480p)':'한국직업방송',
    'WBC TV (1080p)':'복지TV',

    'KBS LiveCam DokDo (540p)':'KBS 독도카메라',
    'TBS Seoul (720p)':'TBS 서울시민방송',
    'KCTV 광주 CH05 (720p) [Not 24/7]':'KCTV 광주 DV',
    'JCN TV':'JCN울산방송',
    'OBS Gyeongin TV (540p)':'OBS 경인', # 쇼핑몰 여부 재확인 요

    'Baduk TV (540p)':'바둑',
    'Billiards TV (540p)':'당구',
    'FTV (540p)':'PBA&GOlf 당구&골프*',
    'IB Sports (540p)':'IB 스포츠',
    'MavTV Select (720p)':'MavTV 모터스포츠',


    'EBS 1 (400p)':'EBS1',
    'EBS 2 (400p)':'EBS2',
    'EBS e (400p)':'EBS영어',
    'EBS+ 1 (400p)':'EBS+ 1',
    'EBS+ 2 (400p)':'EBS+ 2',

    'SBS F!L (540p)':'F!L 예능', #SBS FiL : 라이프 스타일 예능 채널
    'SBS CJB (CJB청주방송) (540p) [Not 24/7]':'CJB 청주 SBS',
    'SBS JIBS (JIBS SBS) (720p) [Not 24/7]':'JIBS 제주 SBS',
    'SBS JTV (JTV전주방송) (406p) [Not 24/7]':'JTV 전주 SBS',
    'SBS KBC (KBC 광주방송) (1080p) [Not 24/7]':'KBC 광주 SBS',
    'SBS KNN (KNN 부산경남대표방송) (450p) [Not 24/7]':'KNN 부산경남 SBS',
    'SBS TBC (TBC 대구방송) (540p) [Not 24/7]':'TBC 대구 SBS', # 신호 없음22/12/21
    'SBS TJB (1080p) [Not 24/7]':'TJB 대전 SBS',
    'SBS UBC (UBC 울산방송) (540p) [Not 24/7]':'UBC 울산 SBS',

    'MBC Andong (안동MBC) (360p) [Not 24/7]':'안동 MBC',
    'MBC Busan (부산MBC) (360p) [Not 24/7]':'부산 MBC',
    'MBC Chuncheon (춘천 MBC) (480p) [Not 24/7]':'춘천 MBC',
    'MBC Daegu (대구 MBC) (480p) [Not 24/7]':'대구 MBC◐',
    'MBC Daejeon (대전 MBC) (720p) [Not 24/7]':'대전 MBC',
    'MBC Gwangju (광주 MBC) (1080p) [Geo-blocked] [Not 24/7]':'광주 MBC',
    'MBC Gyeongnam (경상 MBC) (1080p) [Not 24/7]':'경상 MBC◐',
    'MBC Jeju (제주 MBC) (352p) [Not 24/7]':'제주 MBC',
    'MBC Mokpo (목포 MBC) (720p) [Not 24/7]':'목포 MBC',
    'MBC Ulsan (울산 MBC) (540p) [Not 24/7]':'울산 MBC',
    'MBC Yeosu (여수 MBC) (1080p) [Not 24/7]':'여수 MBC',
    'MBC Drama (480p) [Geo-blocked]':'MBC 드라마(X)', # 신호없음 22/12/21
    

    'JTBC (540p)':'JtBC',
    'JTBC2 (540p)':'JTBC 2',
    'JTBC4 (1080p)':'JTBC 4',
    'JTBC Golf (540p)':'JTBC 골프',
    'JTBC Golf & Sports (1080p)':'JTBC 골프&스포츠',

    'tvN (540p)':'tvN',
    'tvN Asia (Indonesian Subtitle) (576p)':'tvN 아시아',
    'tvN DRAMA (540p)':'tvN 드라마',
    'tvN Movies (Indonesian Subtitle) (576p)':'tvN 영화',
    'tvN SHOW (540p)':'tvN 예능',
    'tvN STORY (540p)':'tvN 스토리',

    'Yonhap News TV (540p)':'연합뉴스',
    

    #--- 영어채널---
    'STIRR MavTV (720p)':'Stirr Mav 모트스포츠', #신호 유, 내용 무
    'Sofy TV (720p)':'Sofy 단편영화(영)', #Sofy.tv - Watch Great Short Films Online
    'Bloomberg TV Asia (576p)':'Bloomberg아시아(영)',
    'CGTN Documentary (576p)':'CGTN 다큐(영)',
    'Classic Arts Showcase':'클래식아트(영)',
    'CNA International (1080p)':'CNA 국제방송(영)',
    'DW English (1080p)':'독일의 소리(영어)',
    'ETB Basque (480p)':'ETB 바스케(스/프)',
    'Euro Indie Music Chart TV (360p)':'유럽뮤직(영)',
    'Euronews German':'유럽뉴스(독)',
    'Euronews Italian':'유럽뉴스(이탈)',
    'Euronews Portuguese':'유럽뉴스(포)',
    'EWTN Asia-Pacific (720p) [Not 24/7]':'EWTN 가톨릭(영)',
    'FIGHT SPORTS (1080p)':'격투 스포츠(영)',
    'France 24 English (1080p)':'France 24프랑스국영방송(영)',
    'Metro Globe Network (1080p) [Not 24/7]':'Metro Globe 인도방송(영)',
    'Pluto TV Euronews (720p) [Not 24/7]':'Pluto 유럽뉴스(스)',
    'Red Bull TV (1080p)':'Red Bull 탐험(영)', # 내용 재확인 요
    'RT Documentary Russian (1080p) [Not 24/7]':'RT 다큐(러)',
    'Insight TV (1080p)':'인사이트(영)', # 네덜란드 방송
    'Dust (1080p)':'科幻电影(영)',# 신호 나쁨
    'TRT World (720p) [Not 24/7]':'TRT 국제방송(영)', #channel for all latest in-depth
    'TVM Internacional (480p) [Not 24/7]':'TBM 모잠비크국제방송(영)', # TVM Internacional is Mozambique TV channel
    'UN Web TV (540p)':'UNTV 유엔방송',
    'Wion (576p)':'Wion 세계는하나(영)',


    #--- 종교채널---
    'BBS Buddhist Broadcasting (1080p)':'BBS불교방송',
    'BTN TV (1080p)':'BTN불교대표방송',
    'BTV World (720p) [Not 24/7]':'인도불교방송',
    'CBS (1080p)':'CBS기독교방송',
    'CTS기독교TV (720p)':'CTS기독교TV',
    'GoodTV (1080p)':'GoodTV기독복음방송',

    
    #--- 쇼핑채널---
    'CJ OnStyle (540p)':'CJ쇼핑',
    'CJ OnStyle Plus (540p)':'CJ쇼핑+',
    'Gongyoung Shopping (720p)':'공영쇼핑',
    'GS Shop (1080p)':'GS 쇼핑',
    'GS My Shop (1080p)':'GS My쇼핑',
    'Home & Shopping (720p)':'홈쇼핑',
    'Hyundai Home Shopping (720p)':'현대홈쇼핑',
    'Hyundai Home Shopping Plus (720p)':'현대홈쇼핑+',
    'KShopping':'kt알파쇼핑',
    'Lotte Home Shopping (720p)':'롯데홈쇼',
    'NS Home Shopping (720p)':'NS 홈쇼핑',
    'NS Shop Plus (720p)':'NS 쇼핑+',
    'Shinsegae Shopping TV (720p)':'신세계 쇼핑',
    'Shopping NT (720p)':'쇼핑NT',
    'W Shopping (720p)':'더블유 쇼핑'
    
    }

my_channel_sorted =[key for key in my_channels.keys() ]


# 파일 쓰기 함수로 만들기 연습
# mykriptv.m3u 파일에 저장되지 않은 채널 정보 따로 출력기능 추가 할 예정
# 링크주소외 불명의 정보 한줄이 링크대신 들어가는 버그 수정 해야함
# 정리된 순서대로 mykriptv.M3U 파일로 저장 
myfilename = 'mykriptv.m3u'
# myfilename = './station/iprklinks/mykriptv.m3u'

with open (myfilename,'w',encoding='utf-8-sig') as f:
    f.writelines(head)
    for keys in my_channel_sorted:
        for i,channel in enumerate(tv_list):

            if  channel[4].split('\n')[0] != keys: continue

            channel_info ='#' + str(i+1) + '\n' + '#EXTINF:-1 ' + channel[1] + ' ' + channel[2] + ' ' + channel[3] + ',' + my_channels.get(channel[4].split('\n')[0]) + '\n' +channel[5] + '\n'  # id, logo, group, name, addr
            f.writelines(channel_info)


with open ('삭제된mykriptv.m3u' ,'w',encoding='utf-8-sig') as f:
    f.writelines(head)
    deleted_channels = 0
    for i,channel in enumerate(tv_list):
        for j,keys in enumerate(my_channel_sorted):
            if channel[4].split('\n')[0] == keys: break
            if j == len(my_channel_sorted)-1 and channel[4].split('\n')[0] != keys: 
                # channel_info ='#' + str(i+1) + '\n' + '#EXTINF:-1 ' + channel[1] + ' ' + channel[2] + ' ' + channel[3] + ',' + channel[4] +channel[5] + '\n'  # id, logo, group, name, addr
                channel_info ='#' + str(i+1) + '\n'   + channel[4] + channel[5] + '\n'  # id,  name, addr

                f.writelines(channel_info)
                deleted_channels += 1
    f.writelines('\n\n一共{}个频道被删除!\n'.format(deleted_channels))
