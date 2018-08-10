Feature: solution
  @CreateSolution
  Scenario: Create Solution success S001
    Given None
    when create solution with name test123, modelName nxp--ls1046a--gateway--cloud, version 1806, tagName test, imageUrl https://s3-us-west-2.amazonaws.com/edgescale.org/release/ls1046ardb/dcca_lsdk1706-ls1046_image_sdboot.tgz
    then create solution with resultMessage Success

  @DeleteSolution
  Scenario: Delete Solution success S002
    Given None
    when delete solution with solutionName test123
    then delete solution with resultMessage Success