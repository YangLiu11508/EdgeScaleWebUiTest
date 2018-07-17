Feature: solution
  @CreateSolution
  Scenario: Create Solution success S001
    Given None
    Then create solution with name test, modelName nxp--ls1043ardb--gateway--cloud, version 1806, tagName test, imageUrl https://s3-us-west-2.amazonaws.com/edgescale.org/release/ls1046ardb/dcca_lsdk1706-ls1046_image_sdboot.tgz
    Then delete solution with solutionName test, resultMessage Success