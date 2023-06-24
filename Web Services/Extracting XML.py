import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
print('Retrieving:', url)

with urllib.request.urlopen(url) as response:
    data = response.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('count:', len(counts))

total = sum(int(count.text) for count in counts)
print('sum:', total)