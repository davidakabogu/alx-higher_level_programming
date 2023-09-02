#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {"email": email}

    # Send a POST request to the URL with the email parameter
    response = requests.post(url, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.text)
    else:
        print(
            f"Failed to send POST request. Status Code: {response.status_code}"
            )
