Feature: create app
  @CreateApp
  Scenario: Create App A001
    Given None
    when create app with dockerName test, vendor nxp, appIcon images\appIcon.jpg, registry devops.nxp.com, imageName test, version 1709
    then Jump to the app list page

  @DeleteApp
   Scenario: Delete App A002
     Given None
     when delete app with appName test
     then delete app resultMessage Success