#!/usr/bin/python3
"""
First API requests management in Python
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Printing the status code of the response
    If the request was sucessful,
    parsing the fetched data into a JSON object
    Iterate through the parsed JSON data
    and printing out the titles of all the posts.
    """
    print("Status Code: {}".format(res.status_code))

    if res.status_code / 100 == 2:
        for i in res.json():
            print(i["title"])


def fetch_and_save_posts():
    """
    If the request was sucessfull, instead of printing titles,
    structuring the data into a list of dictionaries,
    where each dictionary represents a post with keys
    and values for id, title, and body.
    Writing this data into a CSV file called posts.csv
    with columns corresponding to the dictionary keys
    """
    if res.status_code / 100 == 2:
        dic_list = []
        for i in res.json():
            dic_list.append({"id": i["id"],
                             "title": i["title"],
                             "body": i["body"]})

    with open("posts.csv", 'w') as csv_file:
        writing_buffer = csv.DictWriter(csv_file, ["id", "title", "body"])
        writing_buffer.writeheader()
        writing_buffer.writerows(dic_list)


if __name__ != "__main__":
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
