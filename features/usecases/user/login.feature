Feature: login
  @login
  Scenario: login success L001
    Given Access Egdescale website
    when login with username wei.yang, password 1qazxsw2
    Then There is username wei.yang
