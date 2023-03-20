from pymongo import MongoClient #pip install pymongo dnspython으로 패키지 설치
client = MongoClient('mongodb+srv://sparta:test@clustermin.c5qq9dk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#'users'라는 collection에 {'name':,'age':숫자}를 넣습니다.
#  doc = {
#     'name':'영수',
#     'age':24
#  }

#  db.users.insert_one(doc)

#  db.users.insert_one({'name':'영희','age':30})
#  db.users.insert_one({'name':'민식','age':40})
#  db.users.insert_one({'name':'철수','age':24})

#모든 데이터 뽑아보기(find)
all_users = list(db.users.find({},{'_id':False}))

print(all_users[0]) # 0번째 결과값을 보기
print(all_users[1]['name']) # 1번째 'name'값을 보기

for a in all_users: # 반복문을 활용하여 모든 데이터 보기
    print(a)

#특정 값만 뽑아보기(find_one)
user = db.users.find_one({'name':'민식'},{'_id':False})
print(user)

#값 수정하기(upate_one)
db.users.update_one({'name':'철수'},{'$set':{'age':18}})
user_one = db.users.find_one({'name':'철수'})
print(user_one)