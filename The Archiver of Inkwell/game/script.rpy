$ renpy.include("Helpers/transforms.rpy")
$ renpy.include("Helpers/helperfuncs.rpy")
$ renpy.include("Helpers/deltatime.rpy")
$ renpy.include("Helpers.particles.rpy")

init python:
    class Chapter:
        def __init__(self,ch_number):
            self.ch_number = ch_number
            self.ch_title = f"Chapter {ch_number}"
        
        def start(self):
            renpy.call(f"ch_{self.ch_number}")

init:
    image snow = Snow("Helpers/effects/snow2.png")
    image snowback = Snow("Helpers/effects/snow1.png")

    define config.layers = ['master','transient','screens','front','overlay']

label start:

    scene bg whitehouse:
        zoom 1.5
    
    show eileen happy at center zorder 10

    show snow zorder 15
    show snowback zorder 5
    show snow onlayer front
    
        
    "start of visual novel"

    $ Chapter(1).start()

    $ Chapter(2).start()

    return