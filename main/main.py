# import urllib3
# import json
# import ssl
# import os

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# def get_data():
#     http = urllib3.PoolManager(cert_reqs=ssl.CERT_NONE)
#     # Read token from file
#     with open("token.txt", "r") as file:
#         token = file.read().strip()

#     url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
#     resp = http.request("GET", url)
#     values = json.loads(resp.data)
#     print(values)
#     return values

# get_data()

# import urllib3
# import json
# import ssl
# import os

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# def get_data():
#     http = urllib3.PoolManager(cert_reqs=ssl.CERT_NONE)
#     # Read token from file
#     with open("token.txt", "r") as file:
#         token = file.read().strip()

#     url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={token}"
#     resp = http.request("GET", url)
    
#     # Debug statements to inspect the response
#     print(f"Response Status: {resp.status}")
#     print(f"Response Data: {resp.data}")

#     if resp.status == 200:
#         try:
#             values = json.loads(resp.data)
#             print("JSON data parsed successfully.")
#             print(values)
#             return values
#         except json.JSONDecodeError as e:
#             print(f"JSON decoding error: {e}")
#             return None
#     else:
#         print(f"API request failed with status code: {resp.status}")
#         return None

# get_data()


import urllib3
import json

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







