int(input("Enter number of attendees: "))
venue = "large hall" if "attendees" > 100 else "conference room"

facilities = "basic"


if attendees > 50:
    facilities = "audio system"
if attendees > 100:
    facilities = facilities + ", projector" 

print(f"The recommended venue for {"attendees"} attendees is: {venue}")
print(f"Recommended facilities: {facilities}")