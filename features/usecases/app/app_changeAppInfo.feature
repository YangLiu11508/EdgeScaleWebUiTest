Feature: change app info
  @ChangeAppInfo
  Scenario: Change app info A007
    Given None
    when change app info with Appname newname, Description new description
    then change app info resultMessage Success