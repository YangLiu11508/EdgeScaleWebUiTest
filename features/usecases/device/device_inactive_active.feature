Feature: active device
  @InactiveDevice
  Scenario: inactive device D007
    Given None
    when inactive device
    then inactive resultMessage Inactive the device successfully

  @ActiveDevice
  Scenario: active device D006
    Given None
    when active device
    then active resultMessage Active the device successfully! The process can last several minutes, please wait patiently.