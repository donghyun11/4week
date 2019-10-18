from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbhome                    # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)

# @app.route('/')
# def home():
#    return 'This is Home!'

@app.route('/mypage')
def mypage():
   return 'This is My Page!'

@app.route('/')
def home():
		   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def posting():
    item_receive = request.form['item_give']
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    print(item_receive, name_receive, count_receive, address_receive, phone_receive)


    orders = {'name': name_receive, 'count': count_receive, 'address': address_receive, 'phone': phone_receive,
              'item': item_receive}

    db.orders.insert_one(orders)

    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/order', methods=['GET'])
def listing():
    item_receive = request.args.get('item_give')
    print(item_receive)
    result = list(db.orders.find({'item': item_receive}, {'_id': 0}))
    # articles라는 키 값으로 기사정보 내려주기
    return jsonify({'result': 'success', 'orders': result})




if __name__ == '__main__':
   app.run('localhost',port=5000,debug=True)