"""
Python Basics & REST API Demo Script
Demonstrates basic requests call, status check, JSON parsing, and HTTP methods.
"""
import requests

def demo_rest_vs_soap_concept():
    print("=== REST API Demo Call ===")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Content Type: {response.headers.get('Content-Type')}")
    
    if response.status_code == 200:
        json_data = response.json()
        print("Response Body (JSON):")
        print(f"  ID: {json_data.get('id')}")
        print(f"  Title: {json_data.get('title')}")
        print(f"  Body: {json_data.get('body')}")
    print("==========================\n")

if __name__ == "__main__":
    demo_rest_vs_soap_concept()