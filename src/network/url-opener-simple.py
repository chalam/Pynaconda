import requests

URL = 'http://echo.jsontest.com/key/value/one/two/three/four'
def get_page(URL):
    print(requests.get(URL).text)

get_page(URL)