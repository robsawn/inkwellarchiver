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

    def audio_crossfade(fadeTime,music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel-"music1"
            newChannel="music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel=None
            newChannel="music"
        
        if oldChannel is not None:
            renpy.music.stop(channel=oldChannel,fadeout=fadeTime)
        if newChannel is not None:
            renpy.music.play(music,channel=newChannel,loop=None,fadein=fadeTime)