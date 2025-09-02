def calc_ms_in_hours(time_ms):
    return time_ms / (1000 * 60 * 60)

def calc_hours_in_days(hours):
    return round(hours / 24)

def calc_ms_in_min(time_ms):
    return round(time_ms / (1000 * 60))

def calc_min_in_hours(min):
    return round(min / 60)