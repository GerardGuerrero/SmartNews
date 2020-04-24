Feature: Register Comment
  In order to give my opinion about a Notice
  As a user
  I want to comment a Notice

  Background: There is a registered user
      Given Exists a user "user" with password "password"

    Scenario: Register just comment text
      Given I login as user "user" with password "password"
      When I register Comment
        | text     |
        | myopinion |
      Then I'm viewing the details page for comment by "user"
        | text    |
        | myopinion |
      And There are 1 comments
