# This is my firstcucumber feature file
#@SmokeFeature
Feature: check google search function

  #	@smoketest
  Scenario: Validate that the google search is working
    Given user is in google landing page
    When user enters a search keyword in search text box
    And clicks on search button
    Then user should get the search results
    #Examples: 
     # | username | password |
      #| user1    | psw1     |
      #| user2    | psw2     |
