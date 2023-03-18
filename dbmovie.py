from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@clustermin.c5qq9dk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#1.영화제목 '가버나움'의 평점을 가져오기
movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])

#2.'가버나움'의 평점과 같은 평점의 영화 제목을 가져오기
movie = db.movies.find_one({'title':'가버나움'})
targe_star = movie['star']

movies= list(db.movies.find({'star':targe_star},{'_id':False}))
print(movies)

for a in movies:
    print(a['title'])

#3.'밥정'영화의 평점을 0으로 만들기
db.movies.update_one({'title':'밥정'},{'$set':{'star':0}})