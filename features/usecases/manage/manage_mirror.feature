Feature: create mirror
  @CreateMirror
  Scenario: create mirror MA001
    Given None
    when create mirror with Mirror mirror123, Description abc
    then create mirror resultMessage Success

  @DeleteMirror
  Scenario: delete mirror MA003
    Given None
    when delete mirror
    then delete mirror resultMessage Success