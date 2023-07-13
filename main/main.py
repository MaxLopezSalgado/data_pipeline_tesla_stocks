import urllib3
import json
def get_data():
    http = urllib3.PoolManager()
    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
get_data()