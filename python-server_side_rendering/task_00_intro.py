#!/usr/bin/python3
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

        new_template = template.replace("{name}", name)
        new_template = new_template.replace("{event_title}", event_title)
        new_template = new_template.replace("{event_date}", event_date)
        new_template = new_template.replace("{event_location}", event_location)
        
        output_no += 1

        with open("output_" + str(output_no) + ".txt", "w", encoding="utf-8") as f:
            f.write(new_template)
