-- 사용자 생성 (출석용 계정)
CREATE USER attend_user IDENTIFIED BY 1234;

-- 권한 부여
GRANT CONNECT, RESOURCE TO attend_user;

/* attend_user 사용자에게 테이블스페이스 권한 부여 */
-- 해당 사용자가 데이터를 저장할 기본공간을 USERS 테이블스페이스로 지정
ALTER USER attend_user DEFAULT TABLESPACE users;
-- 그 공간에 얼마든지 데이터를 저장할 수 있도록 허용
ALTER USER attend_user quota unlimited ON users;