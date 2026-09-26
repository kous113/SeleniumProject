"""
Python HTTP Libraries Demo Script
Demonstrates GET, POST, validation of status codes and headers, and E2E flow.
"""
import requests

def demo_http_methods_and_validations():
    print("=== 1. Validating GET Request ===")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Assertions
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "application/json" in response.headers.get("Content-Type", ""), "Not JSON!"
    
    print(f"Status Code Check Passed: {response.status_code}")
    print(f"Header Check Passed (Content-Type): {response.headers['Content-Type']}")
    print(f"JSON Payload Title: {response.json()['title']}\n")

    print("=== 2. Validating POST Request ===")
    post_url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Automated API Test Post",
        "body": "Running automated POST test using Python Requests",
        "userId": 101
    }
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    
    post_res = requests.post(post_url, json=payload, headers=headers)
    assert post_res.status_code == 201, f"Expected 201, got {post_res.status_code}"
    
    created_item = post_res.json()
    print(f"POST Status Code: {post_res.status_code}")
    print(f"Created Resource ID: {created_item.get('id')}\n")

if __name__ == "__main__":
    demo_http_methods_and_validations()