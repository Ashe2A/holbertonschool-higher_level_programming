#!/usr/bin/python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template should be a string")
    if template == "":
        raise ValueError("Template should not be an empty string")

    if not isinstance(attendees, list) or \
       all(isinstance(i, dict) for i in attendees):
        raise TypeError("Attendees should be a list of dictionaries")
    if attendees == []:
        raise ValueError("The list of attendees should not be empty")

    output_no = 0
    for i in attendees:            
        name = i["name"]
        if name is None:
            name = "N/A"
            
        event_title = i["event_title"]
        if event_title is None:
            event_title = "N/A"

        event_date = i["event_date"]
        if event_date is None:
            event_date = "N/A"

        event_location = i["event_location"]
        if event_location is None:
            event_location = "N/A"

        format = template.replace("{name}", name)
        format = format.replace("{event_title}", event_title)
        format = format.replace("{event_date}", event_date)
        format = format.replace("{event_location}", event_location)
        
        output_no += 1

        with open("output_" + str(output_no) + ".txt", "w", encoding="utf-8") as f:
            f.write(format)
