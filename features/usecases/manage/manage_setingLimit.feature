Feature: setting limit
  @SettingLimit
  Scenario: setting limit MA008
    Given None
    when setting limit with limitType device, limit 100
    then setting limit resultMessage Success