Feature: update app document
  @UpdateAppDocument
  Scenario: Update app document A003
    Given None
    when update app document with content abvcde12345
    then update app document resultMessage Success to update APP documents