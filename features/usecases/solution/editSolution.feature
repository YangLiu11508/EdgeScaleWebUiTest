Feature: edit solution
  @EditSolution
  Scenario: edit solution S004
    Given None
    when edit solution with link https://s3-us-west-2.amazonaws.com/edgescale.org/release/ls1046ardb/dcca_lsdk1706-ls1046_image_sdboot.tgz, permission public
    then edit solution resultMessage Success
