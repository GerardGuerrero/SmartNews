Feature: Edit Restaurant
  In order to keep updated my previous registers about restaurants
  As a user
  I want to edit a restaurant register I created

Background: There are registered users and a restaurant by one of them
  Given Exists a user "user1" with password "password"
  And Exists comment registered by "user1"
    | description |
    | comentari   |

Scenario: Edit owned comment description
  Given I login as user "user1" with password "password"
  When I edit the comment with description "comentari"
    | description        |
    | comentari editat   |
  Then I'm viewing the details page for comment by "user1"
    | description        |
    | comentari editat   |
  And There are 1 comments
