Feature: create device
  @CreateDevice
  Scenario: Create Device success D001
    Given None
    when create device with SN testtesttesttest123, modelName nxp--ls1046a--gateway--iot

  @DeleteDevice
  Scenario: delete Device D002
    Given None
    when delete device with deviceName 12ad0f2a888150e199378590dccfc4d6.iot.gateway.ls1046a.nxp
    then delete device resultMessage Success