for hour in range(24):
    if hour == 0:
        suffix = "Midnight"
    elif hour == 12:
        suffix = "Noon"
    elif hour < 12:
        suffix = f"{hour} AM"
    else:
        suffix = f"{hour - 12} PM"

    print(f"{hour:02d}:00 - {suffix}")