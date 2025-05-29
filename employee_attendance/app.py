from flask import Flask, render_template # Flask 기능 중에 Flask라는 클래스와 HTML을 보여주는 기능을 가져옴
from flask import request, redirect, url_for, session
import cx_Oracle

# Flask 앱 객체 생성
app = Flask(__name__) # 이 파일을 기준으로 Flask앱을 만들겠다는 의미
app.secret_key - '비밀키는_꼭_안전하게_관리하세요'

# Oracle DB 연결 정보
dsn = cx_Oracle.makedsn("loalhost", 1521, service_name="xe")
conn = cx_Oracle.connect(user="your_user", password="1234", dsn=dsn) # 오라클 DB연결(아이디, 비번, 주소입력필요!!)


# 기본 경로("/")에 접속하면 login.html 페이지 보여줌
@app.route('/')         # 웹사이트에서 http://주소/ 로 들어왔을 때 실행할 함수 지정
def home():             # 방문했을 때 실행할 함수(-> 로그인 페이지 보여주기)
    return render_template('login.html') # templateas/login.html 파일을 화면에 보여줌

# 로그인 처리
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'] # 로그인 폼에서 입력한 아이디 가져옴
    password = request.form['password']

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = :username AND password = :password",
                   {'username':username, 'password':password})   # 유저 테이블에서 해당 유저가 있는지 확인
    user = cursor.fetchone()    # 결과 한 줄 가져옴(없으면 None)

    if user:
        session['username'] = username            #  로그인 성공 시 세션에 사용자 이름 저장
        return redirect(url_for('dashboar'))      # 로그인 성공 후 대시보드 홈페이지로 이동
    else:
        return render_template('login.html', error='아이디 또는 비밀번호가 틀렸습니다.')
    
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"<h1>{session['username']}님 출근체크 페이지입니다!</h1>"
    else:
        return redirect(url_for('home'))

# Flask 앱 실행(디버그 모드 켜기)
if __name__ == '__main__':
    app.run(debug = True) # 서버 실행 + 에러 있으면 화면에 자세히 보여줌