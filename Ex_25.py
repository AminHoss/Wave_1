duration = int(input("How many seconds is the duration? "))

time_in_seconds = duration % 60 

time_in_minutes = (duration - time_in_seconds) / 60
time_displayed_in_minutes = int(time_in_minutes % 60)

time_in_hours = (time_in_minutes - time_displayed_in_minutes) / 60
time_displayed_in_hours = int(time_in_hours % 24)

time_in_days = int((time_in_hours - time_displayed_in_hours) / 60)

if time_in_seconds < 10:
        time_in_seconds = "0" + str(time_in_seconds)

if time_displayed_in_minutes < 10:
        time_displayed_in_minutes = "0" + str(time_displayed_in_minutes)
        
if time_displayed_in_hours < 10:
        time_displayed_in_hours = "0" + str(time_displayed_in_hours)

print("{}:{}:{}:{}".format(time_in_days, time_displayed_in_hours, time_displayed_in_minutes, time_in_seconds))
