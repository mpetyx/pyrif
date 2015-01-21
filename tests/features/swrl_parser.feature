# Created by mpetyx at 1/7/15
Feature: SWRL parser
  The library should be able to parse swrl documents according to the document


  Scenario: Parse empty document
    Given the empty xml swrl document
    When I parse it
    Then I retrieve 1

