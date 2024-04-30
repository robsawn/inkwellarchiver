init python:
    class Chapter:
        def __init__(self,ch_number):
            self.ch_number = ch_number
            self.ch_title = f"Chapter {ch_number}"
        
        def start(self):
            renpy.call(f"ch_{self.ch_number}")

label start:

    show shiori frown

    $ player_name = renpy.input("What's my name, again?",length=24, default="")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Yorick"
    
    $ p.name = player_name

    $ Chapter(0).start()
    $ Chapter(1).start()

    if route_lc:
        $ Chapter(12).start()
        $ Chapter(13).start()
        $ Chapter(14).start()
        if ending >= 2:
            $ Chapter(151).start()
        else:
            $ Chapter(152).start()
    if route_fantasy:
        $ Chapter(22).start()
        $ Chapter(23).start()
        $ Chapter(24).start()
        if mistakes >= 2:
            $ Chapter(251).start()
        else:
            $ Chapter(252).start()
    # if route_slice:
    #     $ Chapter(32).start()
    #     $ Chapter(33).start()
    #     $ Chapter(34).start()
    #     if ending > 2:
    #         $ Chapter(351).start()
    #     else:
    #         $ Chapter(352).start()

    return