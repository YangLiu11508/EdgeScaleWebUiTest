Feature: register fail
  @RegisterFail
  Scenario: register fail R002
    Given register fail Access Egdescale website
    when register fail with FirstName liu, LastName yang, Email liu.yang_1@nxp.com, AccountType USER, CompanyName nxp
    Then stay in register page