import requests

url = "https://scratch.mit.edu/projects/643496502/fullscreen/"

data = requests.get(url)
print (data)

print(data.text)