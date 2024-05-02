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

init -5:
    define config.layers = ['master','transient','immersionvfx','screens','front','overlay']

init: 
    define vpunch = Move((0,20),(0,-20),.10,bounce=True,repeat=True,delay=.275)
    define hpunch = Move((25,0),(-25,0),.10,bounce=True,repeat=True,delay=.275)

    define vpunch2 = Move((0,40),(0,-40),.20,bounce=True,repeat=True,delay=.275)
    define hpunch2 = Move((45,0),(-45,0),.20,bounce=True,repeat=True,delay=.275)

    define vpunch3 = Move((0,20),(0,-20),.10,bounce=True,repeat=True,delay=.275)
    define hpunch3 = Move((25,0),(-25,0),.10,bounce=True,repeat=True,delay=.275)