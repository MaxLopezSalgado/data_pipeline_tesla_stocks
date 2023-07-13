import urllib3
import json


def get_data():
    http = urllib3.PoolManager()
    # Read token from file
    with open("token.txt", "r") as file:
        token = file.read().strip()
        
    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
get_data()