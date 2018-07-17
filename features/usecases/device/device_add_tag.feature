Feature: add tag to device
  @AddTagToDevice
  Scenario: add tag to device D003
    Given None
    when add tag with tag tag123
    then add tag resultMessage Success

  @DeleteTagFromDevice
  Scenario: delete tag from device D004
    Given None
    when delete tag
    then delete tag resultMessage Success
