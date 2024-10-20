#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    fetch_post = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(fetch_post.status_code))

    if fetch_post.status_code == 200:
        json_ed = fetch_post.json()

        for i in json_ed:
            print(i["title"])

    else:
        print("Error {}".format(fetch_post.status_code))


fetch_and_print_posts()


def fetch_and_save_posts():
    fetch_post = requests.get('https://jsonplaceholder.typicode.com/posts')

    if fetch_post.status_code == 200:
        json_ed = fetch_post.json()

        dict_list = []
        for i in json_ed:
            new_dict = {}
            new_dict["id"] = i["id"]
            new_dict["title"] = i["title"]
            new_dict["body"] = i["body"]
            dict_list.append(new_dict)

        with open("posts.csv", 'w', encoding="utf-8") as file:
            write_to_csv = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            write_to_csv.writeheader()
            write_to_csv.writerows(dict_list)

    else:
        print("Error {}".format(fetch_post.status_code))


fetch_and_save_posts()
