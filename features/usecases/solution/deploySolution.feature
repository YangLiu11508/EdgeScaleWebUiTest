Feature: deploy solution
  @DeploySolution
  Scenario: Deploy solution S003
    Given None
    when deploy solution
    then deploy solution resultMessage Success
