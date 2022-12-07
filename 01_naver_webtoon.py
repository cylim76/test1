import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}   #Chrome
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"} # edge

url = "https://comic.naver.com/webtoon/weekday"

res = requests.get(url, headers=headers,timeout=5)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


# #1.  화요일만 가져오기： 개체마다  화요일 정보가 있는 경우
# soup3 = soup.find_all("a",attrs= { "class":"title","href":re.compile("tue$"),})
# for s3 in soup3:
#     link = "https://comic.naver.com" + s3.get("href")
#     print(s3.get_text(),  link)




'''
웹페이지 구조
<div class="col">요일별 칼럼 테이블 div_col  
    <div class ="col_inner"> 요일별 상세정보 테이블 div 2급
        <h4 class ="tue 요일 태그">
            <span>요일 이름 </span>
        </h4>

        <ul (요일별 웹툰 list tag)>
            <li (웹툰 tag)>  
                # 웹툰 정보 태그 1: 제목,이미지 ,요일 그룹 정보  
                <div class ="thum">
                    <a href ="요일 링크"> 
                        <img 이미지 파일>
                        <span></span>
                    </a>
                </div>

                #웹툰 정보 태그 2: 제목, 링크 정보,위에 div 태그와 형제관계
                <a  href="만화 폐이지 링크", class ="title",title ="웹툰제목">웹툰제목</a>
            </li>

            <li>
                두번째 웹툰 정보
            </li>
    </div>
</div>

<div>
다음 요일 웹툰 칼럼
</div>
  
'''


# #2.  화요일만 가져오기： 개체마다  화요일 정보가 <없>다고 가정
# # contents[] 속성을 이용하요 자식 태그 지정
# uls = soup.find_all("ul" )
# # 6번째 ul tag가 월요웹툰 칼럼이고, ul 밑에 웹툰정보 1번부터 li 태그가 있고 ,li 밑에 웹툰정보가 있다
# li =uls[7].contents   # 6번 월요일 - 12 일요일
 
# for index,i in enumerate(range (1,len(li),2)):
#     title = li[i].contents[3].get_text()
#     link = "https://comic.naver.com" + li[i].contents[3].get("href")
#     print(index + 1, title, link)



#3. 화요일만 가져오기:  find_all() 함수 검색 기능 연습
# 요일을 입력하여 변수에 저장
week = False
while week not in ["mon", "tue", "wed", "thu", "fri","sat", "sun"]:
     week = input("요일[mon,tue,wed,thu,fri,sat,sun]을 입력하세요 :")

# 요일 태그<h4>를 찾는다 
h4_list = soup.find_all("h4",attrs= {"class":week})

'''
# h4_list 와 h4_list[0]의 차이:
print(h4_list)
# 리스트이다. 개체가 하나뿐인
[<h4 class="mon"><span>월요 웹툰</span></h4>]

print(h4_list[0])
# 리스트 안에 개체
<h4 class="mon"><span>월요 웹툰</span></h4>
'''
#요일 태그<h4>의 형제 태그<ul>를 찾고,또 그형제 태그<ul>의 자식태그<a>를 검색한다
ul_a_list = h4_list[0].next_sibling.next_sibling.find_all("a",attrs ={"class":"title"})


for index,ul_a in enumerate(ul_a_list):
    title = ul_a.get_text()
    link = "https://comic.naver.com" + ul_a.get("href")
    print(index + 1, title.ljust(15), link.ljust())
