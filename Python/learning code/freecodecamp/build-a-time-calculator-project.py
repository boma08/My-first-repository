def add_time(start, duration, start_day = "None"):

    start_day = start_day.lower()

    def convert_to_minutes(time, mode = "AM"):
        time_and_mode = time.split()
        if len(time_and_mode) == 2:
            mode = time_and_mode[1]
            time = time_and_mode[0]
            am_pm = mode
        hours = int(time.split(":")[0])
        minutes = int(time.split(":")[1])
        if mode == "PM":
            hours += 12
        time_in_minutes = (hours * 60) + minutes
        return time_in_minutes

    def format_hour(hr):
        hour = 0
        am_pm = ""
        if hr > 12:
            hour = hr - 12
            am_pm = "PM"
        elif hr == 12:
            hour = hr
            am_pm = "PM"
        elif hr < 12:
            hour = hr
            am_pm = "AM"
        
        if hour == 0:
            hour = 12
        return hour, am_pm

    reference_time_in_minutes = convert_to_minutes(start) + convert_to_minutes(duration)

    total_hours = reference_time_in_minutes // 60
    days = total_hours // 24
    hours = str(format_hour(total_hours % 24)[0])
    minutes = str(reference_time_in_minutes % 60).rjust(2, "0")
    mode = format_hour(total_hours % 24)[1]
    end_day = ""
    
    days_of_the_week = [
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
        ]
    if start_day in days_of_the_week:
        start_ref = days_of_the_week.index(start_day)
        day_increment = days % 7
        end_day = days_of_the_week[(start_ref + day_increment) % 7]
        result = ""

    if days < 1 and start_day in days_of_the_week:
        result = f'{hours}:{minutes} {mode}, {end_day.title()}'
    elif days < 1:
        result = f'{hours}:{minutes} {mode}'
    elif days == 1 and start_day in days_of_the_week:
        result = f'{hours}:{minutes} {mode}, {end_day.title()} (next day)'
    elif days == 1:
        result = f'{hours}:{minutes} {mode} (next day)'
    elif days > 1 and start_day in days_of_the_week:
        result = f'{hours}:{minutes} {mode}, {end_day.title()} ({days} days later)'
    elif days > 1:
        result = f'{hours}:{minutes} {mode} ({days} days later)'
    print(result)
    return result

add_time('11:59 PM', '24:05', 'Wednesday')
