# Created by Anna at 30.05.2018
Feature: BMI calculation


  Scenario: Metric data, Female, 165 cm, 55kg, non-athletic
    Given the user is on BMI page
    When user selects metric units
    When the user enters 168 as height
    When the user enters 55 kg as weight
    When the user selects female as gender
    When the user selects no as body type option
    When the user submits data
    Then the result displayed is 19.49


#
  Scenario: Invalid data entry - text instead of numeric
    Given the user is on BMI page
    When user selects metric units
    When the user enters 182 as height
    When the user enters ss kg as weight
    When the user selects male as gender
    When the user selects no as body type option
    When the user submits data
    Then error message is displayed

#

