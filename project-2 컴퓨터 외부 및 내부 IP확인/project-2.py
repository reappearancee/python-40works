import socket
import requests
import re

### 2-1번
# in_addr = socket.gethostbyname(socket.gethostbyname())
# print(in_addr)

### 2-2번
# in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# in_addr.connect(("www.google.co.kr", 443))
# print(in_addr.getsockname()[0])

### 2-3번
# req = requests.get("https://ipconfig.kr")
# out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
# print(out_addr)


### 2-4번
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부Ip : ", in_addr.getsockname()[0])

req = requests.get("https://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부IP : ",out_addr)