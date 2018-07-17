Feature: login fail
  @LoginFail
  Scenario: login fail L003
    Given login fail Access Egdescale website
    when login fail with username zhengqiong.zhu, password zhuzhengqiong123
    Then stay in login page