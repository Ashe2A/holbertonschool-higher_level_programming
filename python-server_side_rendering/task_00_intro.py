#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template should be a string")
    if template == "":
        raise ValueError("Template is empty, no output files generated.")

    if not isinstance(attendees, list) or \
       not all(isinstance(i, dict) for i in attendees):
        raise TypeError("Attendees should be a list of dictionaries")
    if attendees == []:
        raise ValueError("No data provided, no output files generated.")

    output_no = 0
    for i in attendees:
        try:
            name = str(i.get("name", "N/A") or "N/A")
            event_title = str(i.get("event_title", "N/A") or "N/A")
            event_date = str(i.get("event_date", "N/A") or "N/A")
            event_location = str(i.get("event_location", "N/A") or "N/A")

            formatted = template.replace("{name}", name)
            formatted = formatted.replace("{event_title}", event_title)
            formatted = formatted.replace("{event_date}", event_date)
            formatted = formatted.replace("{event_location}", event_location)

            output_no += 1
            filename = "output_{}.txt".format(output_no)
            if os.path.exists(filename):
                print("File {} already exists.".format(filename))
                continue

            with open(filename, "w", encoding="utf-8") as f:
                f.write(formatted)
        except Exception as e:
            print(str(e))
