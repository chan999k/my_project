from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


@app.route('/mypage')
def my_page():
    return 'This is My Page!'


if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)