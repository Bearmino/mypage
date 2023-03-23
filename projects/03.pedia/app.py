from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient 
client = MongoClient('mongodb+srv://testmino:test@clustermino.440aylp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
	return render_template('index.html')

#POST 서버 만들기
@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    #크롤링
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']

    #mongodb에 저장하기
    doc = {
        'title':ogtitle,
        'desc':ogdesc,
        'image':ogimage,
        'comment':comment_receive,
    }

    db.movie_list.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

#GET 서버만들기
@app.route("/movie", methods=["GET"])
def movie_get():
	all_movies = list(db.movie_list.find({},{'_id':False}))
	return jsonify({'result':all_movies})

if __name__ == '__main__':
	app.run('0.0.0.0', port=5000, debug=True)