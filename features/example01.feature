# Created by jframos at 1/7/16
  
Feature: Calculator: Sum numbers
  As  a student user
  I   want to sum numbers
  so that  I can operate with them


  @Scenario1.Example<row.index>
  @TL.1.GRAVItY-101 @TL.2.GRAVItY-102 @TL.3.GRAVItY-103
  Scenario Outline: The sum of numbers is the expected one. TestLink ID in tags.
    Given the number "<number1>"
    When  I add the given number number to "<number2>"
    Then  the result is "<result>"

    Examples:
      | number1 | number2 | result |
      | 5       | 5       | 10     |
      | 3       | 2       | 5      |
      | 100     | 0       | 115    |


  @Scenario2.Example<row.index>
  @TL.<testlink>
  Scenario Outline: The sum of numbers is the expected one (2). TestLink ID in Examples.
    Given the number "<number1>"
    When  I add the given number number to "<number2>"
    Then  the result is "<result>"

    Examples:
      | number1 | number2 | result | testlink     |
      | 5       | 5       | 10     | GRAVItY-201  |
      | 3       | 2       | 5      | GRAVItY-202  |
      | 100     | 0       | 115    | GRAVItY-203  |


  @Scenario3
  @TL.GRAVITY-300
  Scenario: The sum of numbers is the expected one (3). Normal Scenario.
    Given the number "1"
    When  I add the given number number to "1"
    Then  the result is "2"
