Feature: deploy app
  @DeployApp
  Scenario: Deploy app A004
    Given None
    when deploy app
    then deploy app resultMessage Success

  @DeleteTask
  Scenario: Delete task T002
    Given None
    when delete task
    then delete task resultMessage Success