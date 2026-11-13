from datetime import datetime

event_title = input("Enter event title: ")
event_year = input("Enter year: ")
event_month = input("Enter month: ")
event_day = input("Enter day: ")

date_obj = datetime.strptime(f"{event_year} {event_month} {event_day}", "%Y %B %d")
weekday = date_obj.strftime("%A")

print("\nFormatted Output")
print("Event:", event_title.upper())
print("Date: ", event_month , event_day,",", event_year)
print("Year: ", event_year)
print("Month: ", event_month.title())
print("Day: ", event_day)
print("Weekday: ", weekday)
