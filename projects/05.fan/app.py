from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient #pip install pymongo dnspython으로 패키지 설치
client = MongoClient('mongodb+srv://testmino:test@clustermino.440aylp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.fan.insert_one(doc)
    return jsonify({'msg': '응원완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_fan = list(db.fan.find({},{'_id':False}))
    return jsonify({'result':all_fan})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)