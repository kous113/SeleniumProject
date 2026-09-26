"""
Handling HTTP Responses Demo Script
Demonstrates response properties, binary downloads, streaming, latency check, and exception handling.
"""
import requests
from requests.exceptions import HTTPError, RequestException

def demo_response_properties_and_exceptions():
    print("=== 1. Response Properties & Latency SLA Check ===")
    url = "https://httpbin.org/get"
    response = requests.get(url)
    
    print(f"URL: {response.url}")
    print(f"Status Code: {response.status_code} (OK: {response.ok})")
    print(f"Elapsed Time: {response.elapsed.total_seconds()} seconds")
    print(f"Content-Type Header: {response.headers.get('Content-Type')}\n")

    print("=== 2. Exception Handling Demo (raise_for_status) ===")
    try:
        error_url = "https://httpbin.org/status/404"
        err_res = requests.get(error_url)
        print(f"Fetched URL: {error_url}, Status: {err_res.status_code}")
        err_res.raise_for_status()
    except HTTPError as e:
        print(f"Caught Expected HTTPError: {e}\n")

def demo_streaming():
    print("=== 3. Streaming Response Chunking ===")
    stream_url = "https://httpbin.org/bytes/5000"
    with requests.get(stream_url, stream=True) as res:
        res.raise_for_status()
        total_bytes = 0
        for chunk in res.iter_content(chunk_size=1024):
            total_bytes += len(chunk)
            print(f"  Received chunk size: {len(chunk)} bytes")
        print(f"Total Bytes Downloaded: {total_bytes} bytes\n")

if __name__ == "__main__":
    demo_response_properties_and_exceptions()
    demo_streaming()