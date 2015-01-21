# Created by mpetyx at 1/7/15
Feature: RIF Parser
  Parsing rif documents according to the official W3C standard is a core for this library

  Scenario: Parse Empty XML RIF
    Given a valid rif empty xml document
    When I parse it
    Then I retrieve python rule class

   Scenario: Parse a valid XML RIF document
     Given that i have the document "http://www.w3.org/2005/rules/test/repository/tc/Frames/Frames-premise.rif"
     When I parse it
     Then I retrieve python rule class