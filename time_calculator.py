def add_time(start, duration, today=None):
    time = ""
    week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    s_time, meridiem = start.split(" ")
    s_hour, s_minute = s_time.split(":")
    s_hour, s_minute = int(s_hour), int(s_minute)
    d_hour, d_minute = duration.split(":")
    d_hour, d_minute = int(d_hour), int(d_minute)
    minute = ((s_minute + d_minute) % 60)
    total_hours = (s_hour + d_hour) + ((s_minute + d_minute) // 59)
    days = total_hours // 23
    print("Days:", days)
    print("Total hours",total_hours)
    hours = total_hours % 23
    print("Hours",hours)
    
    if hours == 12:
        if hours > 12:
            hours %= 12  # Error in Hours
        meridiem = "PM"
    else:
        meridiem = "AM" 
    
    time += str(hours) + ":"

    if len(str(minute)) == 1:
        time += "0" + str(minute)
    else:
        time += str(minute)
    
    time += " " + meridiem

    if days:
        next_day = days % 7
        if today:
            today = today.title()
            # print(((next_day + week.index(today)) % 7)) 
            time += ", " + week[((next_day + week.index(today) + 1) % 7)] # Code worked but logic is still need to be cleared.
        else:
            if next_day > 1:
                time += str(f"{next_day} days later")
            if next_day == 1:
                time += " (next day)"
    else:
        if today:
            time += ", "+ today.title()

    # if meridiem == "AM":
    #     if ((s_hour + d_hour) // 11) % 2 != 0:
    #         meridiem = "PM"
        
    # if meridiem == "PM":
    #     if ((s_hour + d_hour) // 11) % 2 == 0:
    #         meridiem = "AM"
    
        
    return time

print(add_time("11:30 AM", "2:32", "Monday")) #expected O/P "00:03 AM Thursday" 

""" add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tuesday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later) """