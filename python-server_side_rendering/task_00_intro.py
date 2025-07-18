#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template should be a string")
        return
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if not isinstance(attendees, list) or \
       not all(isinstance(i, dict) for i in attendees):
        print("Attendees should be a list of dictionaries")
        return
    if attendees == []:
        print("No data provided, no output files generated.")
        return

    output_no = 0
    for i in attendees:
        try:
            name = str(i.get("name") or "N/A")
            event_title = str(i.get("event_title") or "N/A")
            event_date = str(i.get("event_date") or "N/A")
            event_location = str(i.get("event_location") or "N/A")

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
