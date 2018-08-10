Feature: create device
  @CreateDevice
  Scenario: Create Device success D001
    Given None
    when create device with SN test123, nxp--ls1046a--gateway--cloud

  @DeleteDevice
  Scenario: delete Device D002
    Given None
    when delete device with deviceName 823b878856605082adbfda80d9ddfa44.cloud.gateway.ls1046a.nxp
    then delete device resultMessage Success