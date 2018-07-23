Feature: change password
  @ChangePwd
  Scenario: change password R003
    Given None
    when change password with OldPassword yangliu123, Password yangliu1234
    Then change password with resultMessage Success to change password
