DAYS_IN_A_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start_time, duration_time, starting_day=None):
    # Split the start time
    time_part, period = start_time.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert start hour to 24-hour time
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    if period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Split the duration time
    duration_hour, duration_minute = map(int, duration_time.split(':'))

    # Add time
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour time
    period = 'AM' if final_hour_24 < 12 else 'PM'
    display_hour = final_hour_24 % 12
    display_hour = 12 if display_hour == 0 else display_hour

    display_minutes = f"{final_minutes:02}"

    # Handle the new day
    if starting_day:
        index = DAYS_IN_A_WEEK.index(starting_day.capitalize())
        new_day_index = (index + days_later) % 7
        new_day = DAYS_IN_A_WEEK[new_day_index]
    else:
        new_day = None

    # Build final output string
    result = f"{display_hour}:{display_minutes} {period}"
    if new_day:
        result += f", {new_day}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result
