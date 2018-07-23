Feature: create vendor
  @CreateVendor
  Scenario: create vendor MA004
    Given None
    when create vendor with vendor vendortest
    then create vendor resultMessage Success

  @DeleteVendor
  Scenario: delete vendor MA006
    Given None
    when delete vendor
    then delete vendor resultMessage Success