Feature: Automation on android app MyObservatory

  @w1
  Scenario: Navigate to 9-day forecast screen
    Given install and launch MyObservatory app
    And allow permissions
    When close AD screens
    And click left side menu
    And click 9-day forecast item
    Then navigate 9-day forecast screen successfully