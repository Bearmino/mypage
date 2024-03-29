import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨

soup = BeautifulSoup(data.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a

#select를 이용해서, tr들을 불어오기
movie_trs = soup.select('#old_content > table > tbody > tr')
# movie_trs (tr들) 의 반복문을 돌리기
for tr in movie_trs:
    # movie 안에 a 가 있으면,
    a = tr.select_one('td.title > div > a')
    if a is not None:
        title = a.text   # a 태그 사이의 텍스트를 가져오기
        rank = tr.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
        star = tr.select_one('td.point').text # td 태그 사이의 텍스트를 가져오기
        print(rank, title, star) 
          
# 선택자를 사용하는 방법 (copy selector)
#   soup.select('태그명')
#   soup.select('.클래스명')
#   soup.select('#아이디명')
#   soup.select('상위태그명 > 하위태그명 > 하위태그명')
#   soup.select('상위태그명.클래스명 > 하위태그명.클래스명')
#   태그와 속성값으로 찾는 방법
#   soup.select('태그명[속성="값"]')
# 한 개만 가져오고 싶은 경우
#   soup.select_one('위와 동일')