Feature: Surf Google

  Scenario: Search Bahamas
    Given  I open google in browser
    When   I search for Bahamas
    And    I ensure I have arrived on the Bahamas result page
    And    I take a screenshot of result page
    And    I search for Amsterdam
    Then   I ensure I have arrived on Amsterdam the result page
