from urllib.request import urlretrieve, Request

url = "https://static.zerochan.net/Skadi.%28Arknights%29.full.2858106.jpg"
# urlretrieve(url, "skadi.png")
request = Request(url)
print(request.data)
