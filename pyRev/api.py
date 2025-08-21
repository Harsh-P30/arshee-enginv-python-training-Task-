import requests

# Fetch data from a public API
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print("Failed to fetch data, status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error while making request:", e)
