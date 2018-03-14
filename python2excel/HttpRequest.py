import urllib.request
import urllib.parse

url = 'http://api.gpsspg.com/convert/coord/?oid=7594&from=0&to=4&latlng=84.21,38.70;22.9621107600,113.9826665700;39.9173698900,116.3489858800'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))

