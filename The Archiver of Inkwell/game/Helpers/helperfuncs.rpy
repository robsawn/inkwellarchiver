init python:
    from datetime import datetime, timedelta, timezone
    import time
    import json

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
    
    # def save_game_data(slot=0):
    #     now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #     save_data = {
    #         "player_name": player_name,
    #         "shiori_name": shiori_name,
    #         "greentea": greentea,
    #         "americano": americano,
    #         "cocoa": cocoa,
    #         "sniff": sniff,
    #         "booklove": booklove,
    #         "bookneutral": bookneutral,
    #         "bookhate": bookhate,
    #         "route_slice": route_slice,
    #         "route_lc": route_lc,
    #         "route_fantasy": route_fantasy,
    #         "correctstudy": correctstudy,
    #         "studycheck": studycheck,
    #         "getrest": getrest,
    #         "exhaustion": exhaustion,
    #         "followcultists": followcultists,
    #         "followcats": followcats,
    #         "grabcoat": grabcoat,
    #         "callpolice": callpolice,
    #         "ending": ending,
    #         "wep_1_dc": wep_1_dc,
    #         "blunder": blunder,
    #         "wep_2": wep_2,
    #     }
    #     json_data = json.dumps(save_data)
    #     filename = f"save_{player_name}_{slot}_{now}"
    #     renpy.save(filename,json_data)



init -5:
    define config.layers = ['master','transient','screens','front','overlay']