from behave import when, then
import requests

@when('I send a GET request to "{endpoint}"')
def step_get_request(context, endpoint):
    url = context.base_url + endpoint
    context.response = context.session.get(url)

@when('I create a post with title "{title}" and body "{body}"')
def step_post_request(context, title, body):
    url = context.base_url + "/posts"
    payload = {"title": title, "body": body, "userId": 1}
    context.response = context.session.post(url, json=payload)

@then('the response status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected status {status_code}, got {context.response.status_code}"

@then('the response field "{field_name}" should equal {expected_value:d}')
def step_verify_field_int(context, field_name, expected_value):
    actual_value = context.response.json().get(field_name)
    assert actual_value == expected_value, \
        f"Expected {field_name}={expected_value}, got {actual_value}"

@then('the response should contain an "{field_name}" field')
def step_verify_field_exists(context, field_name):
    json_data = context.response.json()
    assert field_name in json_data, f"Field '{field_name}' not found in response JSON!"
    