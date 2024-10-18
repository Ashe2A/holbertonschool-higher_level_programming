#!/usr/bin/python3

def fetch_and_print_posts():
    fetch_post = requests.get()
    print("Status Code: {}".format(fetch_post["id"]))