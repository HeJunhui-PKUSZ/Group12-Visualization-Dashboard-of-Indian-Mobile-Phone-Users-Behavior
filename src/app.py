from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'messages.csv'

# 首页
@app.route('/')
def index():
    return render_template('index.html')


# 留言提交接口
from datetime import datetime

@app.route('/submit_message', methods=['POST'])
def submit_message():
    data = request.json

    message = data.get('message', '')
    nickname = data.get('nickname', '')
    gender = data.get('gender', '')
    phone = data.get('phone', '')
    email = data.get('email', '')

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['时间', '留言', '昵称', '性别', '电话号码', '邮箱'])
        writer.writerow([timestamp, message, nickname, gender, phone, email])

    return jsonify({
        'status': 'success',
        'time': timestamp
    })



if __name__ == '__main__':
    app.run(debug=True)
