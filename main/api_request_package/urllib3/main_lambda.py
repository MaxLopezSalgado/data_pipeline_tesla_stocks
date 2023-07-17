import urllib3
import json
def get_data_lambda(event, context):
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token=<YOUR_TOKEN_HERE>"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    return values
