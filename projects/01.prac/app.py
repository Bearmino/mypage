from flask import Flask ,render_template, jsonify, request
app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됨

# @app.route('/')
# def home():
#    return 'This is Home!'

# @app.route('/mypage')
# def mypage():
#    return render_template('index.html')


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test2', methods=['POST'])
def test_post():
   title_receive = request.form['title_give'] #[request.form['title_give']가 index_html의 블랙팬서이다.
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

# GET 요청
#  - 통상적으로 데이터 조회(Read)를 요청할 때, 사용합니다!
#     예) 영화 목록 조회 
#  → 데이터 전달 : URL 뒤에 물음표를 붙여 key=value로 전달
    
# POST 요청
#  - 통상적으로 데이터 생성(Create), 변경(Update), 삭제(Delete) 요청 할 때 사용함  
#     예) 회원가입, 회원탈퇴, 비밀번호 수정    
#  → 데이터 전달 : 바로 보이지 않는 HTML

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)