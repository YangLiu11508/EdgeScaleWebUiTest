Feature: create user
  @CreateUser
  Scenario: create user MA007
    Given None
    when create user with username user123, email abc@qq.com
    then create user resultMessage Success