Feature: Delete Comment
  In order to delete my previous comments
  As a user
  I want to delete a comment register I created

Background: There are registered users and a restaurant by one of them
  Given Exists a user "user1" with password "password"
  And Exists comment registered by "user1"
    | description |
    | comentari   |

Scenario:
  Given I login as user "user1" with password "password"
  When I delete the comment with description "comentari"
  Then There are 0 comments
