import requests
from requests.exceptions import HTTPError


def fetch_example_with_bug():
    try:
        response = requests.get("mock://example.com/")

        response.raise_for_status()
    except HTTPError as error:
        if error.response and error.response.status_code == 404:
            print("Not Found")

        print("An error occurred")


def fetch_example():
    try:
        response = requests.get("mock://example.com/")

        response.raise_for_status()
    except HTTPError as error:
        if error.response is not None and error.response.status_code == 404:
            print("Not Found")

        print("An error occurred")
