import requests
import json
# r = requests.get('https://api.github.com/user', auth=('user','pass'))
# print(r.headers["content-type"])
# print(r.encoding)
# print(r.text)
#
# payload= {"key1":"value1", "key2":"value2"}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.text)


# payload = {'some': "data"}
# print(json.dumps(payload)) # dumps: python dict to json
# a = json.dumps(payload)
# print(json.load(a))  # json to python dict
#
# url= 'http://httpbin.org/post'
# files = {'file': open('test.xlsx', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)
# print(r.status_code)
# print(r.headers)
#
#
# bad_r = requests.get("http://httpbin.org/status/404")
# print(bad_r.status_code)
# bad_r.raise_for_status() #主动抛出异常

# url='http://example.com/some/cooke/setting/url'
# r = requests.get(url)
# print(r.cookies)
#
# url='http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)
#
# r = requests.get("http://github.com")
# print(r.url)
# print(r.status_code)
# print(r.history)

# r = requests.get("http://github.com", allow_redirects=False)
# print(r.status_code)
# print(r.history)


#requests.get('http://github.com', timeout=1)


# r = requests.get('http://api.apiopen.top/musicBroadcastingDetails?channelname=public_tuijian_spring')
# print(r.text)
# if "漫步春天" in r.text:
#     print("aaa")

import requests
# r = requests.get("https://api.github.com/events")

# r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)

r = requests.get('https://api.github.com/events')
print(r.text)
print(r.content)
print(r.json())





