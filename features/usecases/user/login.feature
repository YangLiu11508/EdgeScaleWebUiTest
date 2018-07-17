Feature: login
  @login
  Scenario: login success L001
    Given Access Egdescale website
    when login with username zhengqiong.zhu, password zhuzhengqiong
    Then There is username zhengqiong.zhu
