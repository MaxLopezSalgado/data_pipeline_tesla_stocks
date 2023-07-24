import ssl
import urllib3
import json
import os

def get_data_lambda(event, context):
    # Print the contents of /tmp/ to check if the file is present
    print(os.listdir("/tmp/"))
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    http = urllib3.PoolManager(cert_reqs='CERT_NONE', ssl_context=ssl_context)

    # Use the absolute path for the token file
    with open("token.txt", "r") as file:
        token = file.read().strip()

    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    return values
