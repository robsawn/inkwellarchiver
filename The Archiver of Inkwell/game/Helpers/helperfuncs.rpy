init python:
    from datetime import datetime, timedelta, timezone
    import time

    def show_time(timestamp):
        local_offset_seconds = -time.timezone if (time.localtime().tm_isdst == 0) else -time.altzone
        local_offset_hours = local_offset_seconds / 3600

        dt_utc = datetime.utcfromtimestamp(timestamp)
        local_time = dt_utc + timedelta(hours=local_offset_hours)

        format_time = local_time.strftime('%I:%M %p').lstrip("0")
        return format_time

