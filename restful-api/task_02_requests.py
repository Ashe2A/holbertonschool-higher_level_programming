#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if 200 <= r.status_code <= 299:
        parse_fetched_request = r.json()
    for i in parse_fetched_request:
        print(i["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if 200 <= r.status_code <= 299:
        parse_fetched_request = r.json()
        with open("posts.csv", "w") as f:
            csv_data = csv.DictWriter(f, ["id", "title", "body", "userId"])
            csv_data.writeheader()
            for i in parse_fetched_request:
                csv_data.writerow(i)
