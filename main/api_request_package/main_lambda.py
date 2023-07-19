import ssl
import urllib3
import json
def get_data_lambda(event, context):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    http = urllib3.PoolManager(cert_reqs='CERT_NONE', ssl_context=ssl_context)
    
     # Read token from file
    with open("token.txt", "r") as file:
        token = file.read().strip()

    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    return values
