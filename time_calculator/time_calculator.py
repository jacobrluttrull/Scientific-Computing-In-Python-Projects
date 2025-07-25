DAYS_IN_A_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start_time, duration_time, starting_day=None):
    time_part, period = start_time.split()
    start_hour, start_minutes = map(int, time_part.split(':'))

    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    if period.upper() == 'AM' and start_hour == 12:
        start_hour = 0
    duration_hour, duration_minutes = map(int, duration_time.split(':'))

    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    period = 'AM' if final_hour_24 < 12 else 'PM'
    display_hour = 12 if final_hour_24 % 12 == 0 else final_hour_24 % 12

    display_mins = f"{final_minutes:02}"

    if starting_day:
        index = DAYS_IN_A_WEEK.index(starting_day.strip().capitalize())
        new_day = DAYS_IN_A_WEEK[(index + days_later) % 7]
    else:
        new_day = None

    result = f"{display_hour}:{display_mins} {period}"
    if new_day:
        result += f", {new_day}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    return result
