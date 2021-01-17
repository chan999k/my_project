from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.my_project


@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


@app.route('/mypage')
def my_page():
    return 'This is My Page!'


@app.route('/star', methods=['POST'])
def star_point():
    star_receive = request.form['give_star']
    name_receive = request.form['give_name']
    db.WOW.insert_one({'이름': name_receive, '평점': star_receive})
    return jsonify({'result': 'success'})


@app.route('/star', methods=['GET'])
def death_tanker_count():
    all_Count = db.WOW.count({'이름': '죽음의 상흔 탱커'})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)
