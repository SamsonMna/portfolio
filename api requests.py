# Get that api request back or make a call to an API database
import urllib
import json

url = 'abc.com/dce/xyz'
https = urllib.PoolManager()
response = https.request('GET', url)
print(response.data) # the xyz of the dce folder in your url. Has to be in a key-value format else we use the response.content in bs4
# Make a post to api to receive data in form of a Json or csv or yaml
https = urllib.PoolManager()
response = https.request('POST', url, fields={'whichever fields you want return in a a dictionary format: "abc" : "xyz"'})
if response.status_code == 200:
    data = response.json()
    with open('response.json', 'w') as f:
        json.dump(data, f)
# Read the API documentation to know the kind of response to expect since not all APIs return values in a key-value pair response
