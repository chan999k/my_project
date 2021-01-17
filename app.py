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

# 실패작 참고용
# def death_tanker_count():
#     all_count = db.WOW.count_document({'이름': '죽음의 상흔 탱커'})
#     stars = list(db.WOW.find({'이름': '죽음의 상흔 탱커'}))
#     print(stars['평점'])
#     for all_star in stars:
#         basic_star = 0
#         all_star = all_star + basic_star
#         print(all_star)
#     return jsonify({'result': 'success'})

@app.route('/star', methods=['GET'])
def death_tanker_count():
    stars = list(db.WOW.find({'이름': '죽음의 상흔 탱커'}))
    all_count = len(stars)
    sum = 0
    for star in stars:
        num = int(star['평점'])
        sum = sum + num
    return jsonify({'result': 'success', '개수': all_count, '합': sum})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)
