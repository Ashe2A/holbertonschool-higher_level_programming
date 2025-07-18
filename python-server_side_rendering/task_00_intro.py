#!/usr/bin/python3
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
        name = i.get("name") or "N/A"
        event_title = i.get("event_title") or "N/A"
        event_date = i.get("event_date") or "N/A"
        event_location = i.get("event_location") or "N/A"

        formatted = template.replace("{name}", name)
        formatted = formatted.replace("{event_title}", event_title)
        formatted = formatted.replace("{event_date}", event_date)
        formatted = formatted.replace("{event_location}", event_location)

        output_no += 1

        with open(f"output_{output_no}.txt", "w", encoding="utf-8") as f:
            f.write(formatted)
