@api
Feature: API Automation Testing with Behave BDD Framework

  @smoke @get
  Scenario: Retrieve post details successfully
    When I send a GET request to "/posts/1"
    Then the response status code should be 200
    And the response field "id" should equal 1

  @regression @post
  Scenario Outline: Create posts with parameterized data
    When I create a post with title "<Title>" and body "<Body>"
    Then the response status code should be 201
    And the response should contain an "id" field

    Examples: Post Data Table
      | Title                 | Body                           |
      | Test Post Title One   | Content body for test post 1   |
      | Test Post Title Two   | Content body for test post 2   |