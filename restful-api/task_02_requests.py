#!/usr/bin/python3

import requests

def fetch_and_print_posts():
    fetch_post = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(fetch_post.status_code))

    if fetch_post.status_code == 200:
        json_ed = fetch_post.json()

    for i in json_ed:
        print(i["title"])
