// 로그인 요청을 처리하는 컨트롤러

package com.example.demo.controller;

import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;
import org.springframework.web.bind.annotation.*;

@RestController // 컨트롤러 : HTTP 요청을 처리하는 클래스
@RequestMapping("/login") // "/login" 경로로 요청이 오면 여기서 처리함
public class LoginController {
    private final UserRepository userRepository;

    // 생성자 주입: 스프링이 자동으로 Repository를 넣어줌
    public LoginController(UserRepository userRepository){
        this.userRepository = userRepository;
    }

    // 로그인 요청 처리
    @PostMapping // POST 요청으로 "/Login" 경로 들어오면 실행
    public String login(@RequestParam String user name, @RequestParam String password){
      User user = userRepository.findByUsername(username);  
    }
}
