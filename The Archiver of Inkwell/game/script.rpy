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
    define config.layers = ['master','transient','screens','front','overlay']

    image snow = Snow("Helpers/effects/snow2.png")
    image snowback = Snow("Helpers/effects/snow1.png")

    image eileen_glitched:
        animation
        #At("eileen happy", glitch)
        glitch("eileen happy",randkey=None)
        pause 0.2
        #At("eileen happy", glitch)
        glitch("eileen happy",randkey=None)
        pause 0.1
        #At("eileen happy",square_glitch)
        square_glitch("eileen happy",randkey=None)
        pause 0.2
        #At("eileen happy",animated_glitch)
        animated_glitch("eileen happy")
        pause 0.3
        #At("eileen happy",square_glitch)
        square_glitch("eileen happy",randkey=None)
        pause 0.1
        At("eileen happy")
        pause 2.5
        repeat

label start:

    scene bg whitehouse:
        zoom 1.5
    
    show eileen_glitched at center zorder 10
    
    show snow zorder 15
    show snowback zorder 5
    show snow onlayer front
        
    "start of visual novel"

    $ Chapter(0).start()

    return