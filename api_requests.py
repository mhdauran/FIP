import requests

try:
    response = requests.get(
        "https://api.github.com", timeout=10
    )

    response.raise_for_status()
    data = response.json()

    print("API request successful!")
    print(data)

except request.exceptions.timeout:
    print("Error: Request timed out.")

except request.exception.connectionError:
    print("Error: check your internet connection.")

except requests.exceptions.HTTPError:
    print("Error: Server returned an HTTP error.")

except requests.exceptions.RequestException:
    print("Error: something went wrong.")

except ValueError:
    print("Error: Invalid response data.")