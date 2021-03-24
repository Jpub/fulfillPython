import json
from urllib import request, parse

def get_json(param):
    with request.urlopen(build_url(param)) as f:
        return json.load(f)

def get_data(url):
    with request.urlopen(url) as f:
        return f.read()

def build_url(param):
    query = parse.urlencode(param)
    return ('https://www.googleapis.com'
            f'/books/v1/volumes?{query}')