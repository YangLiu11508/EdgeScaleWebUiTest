Feature: add tag to solution
  @AddTagToSolution
  Scenario: add tag to solution S006
    Given None
    when add tag to solution with tag newTag
    then add tag to solution resultMessage Success

  @DeleteTagFromSolution
  Scenario: delete tag from solution S006
    Given None
    when delete tag from solution
    then delete tag from solution resultMessage Success
