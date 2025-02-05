def add_time(start, duration, start_day=None):
    # Parse the start time into hours, minutes, and period
    start_time, period = start.split()
    start_h, start_m = map(int, start_time.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM' and start_h != 12:
        start_h += 12
    elif period == 'AM' and start_h == 12:
        start_h = 0
    
    total_start_min = start_h * 60 + start_m
    
    # Parse the duration into hours and minutes
    dur_h, dur_m = map(int, duration.split(':'))
    total_dur_min = dur_h * 60 + dur_m
    
    # Calculate total minutes and days passed
    total_min = total_start_min + total_dur_min
    days_passed = total_min // (24 * 60)
    remaining_min = total_min % (24 * 60)
    
    # Convert remaining minutes to 24-hour time
    new_h = remaining_min // 60
    new_m = remaining_min % 60
    
    # Convert to 12-hour format and determine period
    if new_h == 0:
        period_new = 'AM'
        new_h_12 = 12
    elif 1 <= new_h < 12:
        period_new = 'AM'
        new_h_12 = new_h
    elif new_h == 12:
        period_new = 'PM'
        new_h_12 = 12
    else:
        period_new = 'PM'
        new_h_12 = new_h - 12
    
    # Format the new time string
    time_str = f"{new_h_12}:{new_m:02d} {period_new}"
    
    # Determine the new day of the week if applicable
    new_day = None
    if start_day:
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = days_of_week.index(start_day.strip().lower())
        new_day_index = (day_index + days_passed) % 7
        new_day = days_of_week[new_day_index].capitalize()
    
    # Build the output string
    output = time_str
    if new_day:
        output += f", {new_day}"
    
    if days_passed == 1:
        output += " (next day)"
    elif days_passed > 1:
        output += f" ({days_passed} days later)"
    
    return output
