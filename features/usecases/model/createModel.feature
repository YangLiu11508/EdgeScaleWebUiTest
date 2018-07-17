Feature: create model
  @CreateModel
  Scenario: create model M001
    Given None
    when create model with Model 666, Type iot, Platform ls1046a, Vendor nxp
    then create model resultMessage Success

  @EditModel
  Scenario: edit model M002
    Given None
    when edit model with Model new666, Type thing, Platform ls1046a, Vendor nxp
    then edit model resultMessage Success

  @DeleteModel
  Scenario: delete model M003
    Given None
    when delete model
    then delete model resultMessage Success