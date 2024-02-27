$ renpy.include("characters.rpy")

init python:
    class Chapter:
        def __init__(self,ch_number):
            self.ch_number = ch_number
            self.ch_title = f"Chapter {ch_number}"
        
        def start(self):
            renpy.call(f"ch_{self.ch_number}")

label start:

    $ player_name = renpy.input("What's my name, again?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Yorick"
    
    $ p.name = player_name

    $ Chapter(0).start()

    return