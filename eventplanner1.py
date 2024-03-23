attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(f"The recommended venue for {attendees} attendees is: {venue}")