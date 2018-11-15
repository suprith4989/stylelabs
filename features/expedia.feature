Feature: Surf Expedia
  
  Scenario: Search flight + accommodation
    Given  I navigate to expedia website
    When   I look for a flight+accommodation from Brussels to New York
    Then   Result page contains travel option for the chosen destination
