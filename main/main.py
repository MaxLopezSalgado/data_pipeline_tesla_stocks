import urllib3
import json
import os
import streamlit as lt

def get_data():
    # Disable SSL certificate verification (Not recommended for production)
    http = urllib3.PoolManager(cert_reqs='CERT_NONE')

    # Read token from file
    with open("token.txt", "r") as file:
        token = file.read().strip()

    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
    resp = http.request("GET", url)

    # Decode the response data and print it
    data = resp.data.decode("utf-8")
    print("Response Data:", data)

    try:
        values = json.loads(data)
        print(values)
        return values
    except json.JSONDecodeError as e:
        print("JSON Parsing Error:", e)
        return None

get_data()







