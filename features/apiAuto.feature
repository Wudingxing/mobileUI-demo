Feature: Verify 9-Day forecast api

  @a1
  Scenario Outline: User get info from 9-Day Forecast page
    Given 9-day forecast related endpoint
    When send a request with <param>
    Then response status code is <code>
    Then verify results are consistent with related content on 9-day forecast page
    Examples:
      | code | param  |
      | 200  | normal |

    Scenario Outline: Get humidity for the day after tomorrow from 9-Day Forecast page
    Given 9-day forecast related endpoint
    When send a request with <param>
    Then response status code is <code>
    Then get humidity for the day after tomorrow
    Examples:
      | code | param  |
      | 200  | normal |

  Scenario Outline: Verify Local Forecast response status with specific parameter
    Given local forecast related endpoint
    When send a request with <param>
    Then response status code is <code>
    Then no any content from response
    Examples:
      | code | param             |
      | 304  | if-modified-since |

  Scenario Outline: Bad ending for 9-day forecast with bad parameters
    Given 9-day forecast related endpoint
    When send a request with <param>
    Then response status code is <code>
    Examples:
      | code | param         |
      | 404  | fake_endpoint |
      | 403  | fake_body     |


