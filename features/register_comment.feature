Feature: Register Comment
  In order to give my opinion about the news that I have read
  As a user
  I want to register a news comment together with it's news identifier

  Background: There is a registered user
      Given Exists a user "user" with password "password"

    Scenario: Register just a comment title
      Given I login as user "user" with password "password"
      When I register a comment title
        | title                           | newsCode  |
        | Trump's attitude is outrageous  | 019282AAB |
      Then I'm viewing the content of comment by "user"
        | title                           | content  |
        | Trump's attitude is outrageous  |          |
      And There are 1 comment

    Scenario: Register a comment with content
      Given I login as user "user" with password "password"
      When I register a comment
        | title                           | newsCode  | content                             |
        | Trump's attitude is outrageous  | 019282AAB | The USA president is a blablabla... |
      Then I'm viewing the content of comment by "user"
        | title                           | content                             |
        | Trump's attitude is outrageous  | The USA president is a blablabla... |
      And There are 1 comment

    Scenario: Try to register a comment but not logged in
      Given I'm not logged in
      When I register a comment
        | title                           | newsCode  | content                             |
        | Trump's attitude is outrageous  | 019282AAB | The USA president is a blablabla... |
      Then I'm redirected to the login form
      And There are 0 comment
