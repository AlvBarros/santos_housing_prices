def getRequest(url: str) -> str:
    import requests
    from requests.exceptions import RequestException

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def postRequest(url: str, data: dict) -> str:
    import requests
    from requests.exceptions import RequestException

    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()