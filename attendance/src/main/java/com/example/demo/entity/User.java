// 데이터베이스의 users 테이블과 연결되는 클래스

package com.example.demo.entity;

import jakarta.persistence.*;

@Entity // 이 클래스는 데이터베이스 테이블과 연결됨을 의미
@Table(name = "user") // 연결할 테이블 이름: user
public class User {
    @ID // 이 필드는 테이블의 키본 키
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 자동 증가
    PRIVATE lONG ID;

    @Column(nullable = false, unique = true) // null 불가, 중복 불가
    private String username;

    Column(nullable = false) // null 불가

    private String password;

    // 아래는 자바에서 값을 꺼내거나 넣을 때 쓰는 Getter/Setter
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPssword(String password) {
        this.password = password;
    }
}
