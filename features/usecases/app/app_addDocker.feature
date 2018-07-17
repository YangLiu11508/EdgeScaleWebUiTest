Feature: add docker
  @AddDocker
  Scenario: Add docker A008
    Given None
    when add docker with Registry hub.docker.com, imageName newimage, Version new123
    then add docker resultMessage Success