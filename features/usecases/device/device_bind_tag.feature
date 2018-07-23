Feature: bind tag to device
  @BindTagToDevice
  Scenario: bind tag to device D005
    Given None
    when bind tag with tag abcdef123
    then bind tag resultMessage Success

  @DeleteBindTagFromDevice
  Scenario: delete bind tag from device D005
    Given None
    when delete bind tag
    then delete bind tag resultMessage Success