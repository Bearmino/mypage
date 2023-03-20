import requests # requests 라이브러리 설치 필요
r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

gu_seoul = rjson['RealtimeCityAir']['row']

for gu_mise in gu_seoul:
    print(gu_mise['MSRSTE_NM'], gu_mise['IDEX_MVL'])

print('미세먼지가 60미만인 구만 찾아라')

for gu_mise in gu_seoul:
    if gu_mise['IDEX_MVL'] < 60:
        print(gu_mise['MSRSTE_NM'], gu_mise['IDEX_MVL'])