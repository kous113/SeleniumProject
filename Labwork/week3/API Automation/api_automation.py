"""
API Automation Demo Script
Demonstrates Session management, Basic/Bearer auth, and PUT vs PATCH behavior.
"""
import requests

def demo_session_and_auth():
    print("=== 1. Demonstrating Session Management & Basic Auth ===")
    session = requests.Session()
    session.auth = ("user", "passwd")
    
    res = session.get("https://httpbin.org/basic-auth/user/passwd")
    print(f"Basic Auth Status: {res.status_code}")
    print(f"Authenticated Payload: {res.json()}")
    session.close()
    print("========================================================\n")

def demo_put_vs_patch():
    print("=== 2. Demonstrating PUT vs PATCH ===")
    base_url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # PUT Call (Full replacement)
    put_data = {"id": 1, "title": "Full Replacement Title", "body": "Full Replacement Body", "userId": 1}
    put_res = requests.put(base_url, json=put_data)
    print(f"PUT Status: {put_res.status_code}")
    print(f"PUT Response: {put_res.json()}")
    
    # PATCH Call (Partial replacement)
    patch_data = {"title": "Partial Patch Title Only"}
    patch_res = requests.patch(base_url, json=patch_data)
    print(f"PATCH Status: {patch_res.status_code}")
    print(f"PATCH Response: {patch_res.json()}")
    print("======================================\n")

if __name__ == "__main__":
    demo_session_and_auth()
    demo_put_vs_patch()