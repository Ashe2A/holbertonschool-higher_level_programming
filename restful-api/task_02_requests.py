#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSON PlaceHolder and print titles"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if 200 <= r.status_code <= 299:
        parse_fetched_request = r.json()
    for i in parse_fetched_request:
        print(i["title"])


def fetch_and_save_posts():
    """Fetch posts from JSON PlaceHolder and write it out a CSV file"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if 200 <= r.status_code <= 299:
        parse_fetched_request = r.json()
        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            csv_data = csv.DictWriter(f,
                                      ["id", "title", "body"],
                                      extrasaction="ignore")
            csv_data.writeheader()
            for i in parse_fetched_request:
                csv_data.writerow(i)
