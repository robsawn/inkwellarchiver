init python:
    class Chapter:
        def __init__(self,ch_number):
            self.ch_number = ch_number
            self.ch_title = f"Chapter {ch_number}"
        
        def start(self):
            renpy.call(f"ch_{self.ch_number}")

label start:

    scene black

    "start of visual novel"
    $ Chapter(1).start()

    $ Chapter(2).start()

    return
