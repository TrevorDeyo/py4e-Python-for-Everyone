import urllib.request
import json

# url selection
url = input('Enter URL: ')
if len(url) == 0:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
elif len(url) == 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1764476.json'
else:
    pass
print('Retrieving:', url)

# url retrieval
with urllib.request.urlopen(url) as response:
    data = response.read()
print('Retrieved', len(data), 'characters')

json_data = json.loads(data)

def count_keys(json_data):
    count = 0
    for comment in json_data['comments']:
        if 'count' in comment:
            count += 1
    return count
print('Counts:', count_keys(json_data))

# sum of the 'count' values
def sum_counts(json_data):
    sum = 0
    for comment in json_data['comments']:
        sum += comment['count']
    return sum
print('Sum:', sum_counts(json_data))
print(json_data)