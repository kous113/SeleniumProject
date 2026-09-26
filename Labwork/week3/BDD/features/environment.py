import requests

def before_all(context):
    print("\n[BDD HOOK] Initializing API Test Suite Execution...")
    context.base_url = "https://jsonplaceholder.typicode.com"

def before_scenario(context, scenario):
    print(f"\n[BDD HOOK] Starting Scenario: {scenario.name}")
    context.session = requests.Session()
    context.session.headers.update({"Content-Type": "application/json"})

def after_scenario(context, scenario):
    print(f"[BDD HOOK] Completed Scenario: {scenario.name} - Status: {scenario.status}")
    if hasattr(context, "session"):
        context.session.close()

def after_all(context):
    print("\n[BDD HOOK] API Test Suite Execution Completed.")