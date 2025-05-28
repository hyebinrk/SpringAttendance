// DB에서 사용자 정보를 가져오는 인터페이스

package com.example.demo.repository;

import com.example.demo.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    // username으로 사용자 한 명 찾기
    User findByUsername(String username);
}
