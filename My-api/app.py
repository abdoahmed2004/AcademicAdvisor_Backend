from flask import Flask, jsonify
import pymysql

app = Flask(__name__)


conn = pymysql.connect(
    host='sql12.freesqldatabase.com',
    user='sql12778098',
    password='ck3faGpWQK',
    database='sql12778098',
    port=3306
)

@app.route('/students')
def get_students():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
