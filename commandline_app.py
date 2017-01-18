import json
import urllib.request


def uni_search():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    jsonstr = response.read().decode()
    final_dict = json.loads(jsonstr)
    print(final_dict)


if __name__ == '__main__':
    uni_search()