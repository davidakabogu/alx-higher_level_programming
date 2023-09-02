#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    # response = requests.get("https://intranet.hbtn.io/status")
    r = requests.get("http://0.0.0.0:5050/status")
    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
