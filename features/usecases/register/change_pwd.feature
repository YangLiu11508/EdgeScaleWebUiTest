Feature: change password
  @ChangePwd
  Scenario: change password R003
    Given None
    when change password with OldPassword zhuzhengqiong, Password zhuzhengqiong111
    Then change password with resultMessage Success to change password
