from pymongo import MongoClient #pip install pymongo dnspython으로 패키지 설치
client = MongoClient('mongodb+srv://sparta:test@clustermin.c5qq9dk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 'users'라는 collection에 {'name':,'age':숫자}를 넣습니다
doc = {
    'name':'영수',
    'age':24
}

db.users.insert_one(doc)

db.users.insert_one({'name':'영희','age':30})
db.users.insert_one({'name':'민식','age':40})
db.users.insert_one({'name':'철수','age':24})

