days, hours, minutes, seconds = input("Enter the duration in the format D:HH:MM:SS. ").split(":")

if int(hours) > 24:
    print("The duration you entered to the hours slot was invalid.")

if int(minutes) > 60:
    print("The duration you entered to the minutes slot was invalid.")

if int(seconds) > 60:
    print("The duration you entered to the seconds slot was invalid.")

duration = int(seconds) + (int(minutes) * 60) + (int(hours) * 3600) + (int(days) * 86400)

print("The duration in seconds is {} seconds.".format(duration))
