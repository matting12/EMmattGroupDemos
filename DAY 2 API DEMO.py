import requests
import json

BASE_URL = "http://localhost:3000"


response = requests.get(f"{BASE_URL}/person/3")

if response.status_code == 200:
    data = response.json()
    print("[OK] Data fetched successfully!")
    print("\nRaw JSON:")
    print(json.dumps(current_data, indent=2))
else:
    print(f"[ERROR] API Error: {response.status_code}")