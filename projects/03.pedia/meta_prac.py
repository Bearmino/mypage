#조각 파일
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191597'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#크롤링하기
og_image = soup.select_one('meta[property="og:image"]')['content']
og_title = soup.select_one('meta[property="og:title"]')['content']
og_description = soup.select_one('meta[property="og:description"]')['content']

print(og_image,og_title,og_description)
