#!/usr/bin/python3
from data_00_intro import attendees

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError(str("Template should be a string"))
    if template == "":
        raise ValueError(str("Template should not be an empty string"))

    if not isinstance(attendees, list) and \
       all(isinstance(i, dict) for i in attendees):
        raise TypeError(str("Attendees should be a list of dictionaries"))
    if attendees == []:
        raise ValueError(str("The list of attendees should not be empty"))

    output_no = -1
    for i in attendees:
        if "name" in i:
            name = i["name"]
        else:
            name = "N/A"

        if "event_title" in i:
            event_title = i["event_title"]
        else:
            event_title = "N/A"

        if "event_date" in i:
            event_date = i["event_date"]
        else:
            event_date = "N/A"

        if "event_location" in i:
            event_location = i["event_location"]
        else:
            event_location = "N/A"
        
        template = template.replace("{name}", name)
        template = template.replace("{event_title}", event_title)
        template = template.replace("{event_date}", event_date)
        template = template.replace("{event_location}", event_location)
        
        output_no += 1

        with open("output_" + str(output_no) + ".txt", "w", encoding="utf-8") as f:
            return f.write(template)
