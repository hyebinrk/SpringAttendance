/* 시퀀스 생성 */
CREATE SEQUENCE users_seq
	START WITH 1		/* 1부터시작 */
	INCREMENT BY 1		/* 1씩 증가 */
	NOCACHE				/* 캐시하지않음(안정성 우선) */
	NOCYCLE;			/* 반복하지않음 */

/* 테이블 생성 */
CREATE TABLE users (
	id NUMBER PRIMARY KEY,
	username varchar2(50) NOT NULL UNIQUE,
	password varchar2(100) NOT null
);

