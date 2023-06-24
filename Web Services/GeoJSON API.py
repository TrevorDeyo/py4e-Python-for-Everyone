import urllib.parse
import urllib.request
import json

# API endpoint
base_url = 'http://py4e-data.dr-chuck.net/json?'

# prompt for location
address = input('Enter location: ')

# construct URL with parameters
params = {'address': address, 'key': 42}
url = base_url + urllib.parse.urlencode(params)
print(url)

# retrieve data from URL and parse JSON
response = urllib.request.urlopen(url).read()
data = json.loads(response.decode())

# extract place_id from JSON
place_id = data['results'][0]['place_id']

# print result
print('Place id', place_id)