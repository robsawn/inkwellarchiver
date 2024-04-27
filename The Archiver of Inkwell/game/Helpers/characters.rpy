define shi = Character("Strange Woman",color='#c213e5',window_background="gui/textbox1_purple.png",callback=speaker("Shiori"))
define p = Character("",color='#ffffff',window_background="gui/textbox1_grey.png")
define p_i = Character("",color='#ffffff',window_background="gui/textbox1_grey.png",what_prefix="{i}",what_suffix="{/i}")
define s = Character("Classmate",window_background="gui/textbox1_grey.png")

init -10 python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
    
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

# Composite things together to make a character with blinking eyes and
# lip-flap.
image shiori normal = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), "images/shiori/Eyebrows/eyebrows1.png",
    (0,0), WhileSpeaking("shi", "shio mouth", "images/shiori/Mouths/mouth_closed.png"))

image shiori concern = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), "images/shiori/Eyebrows/eyebrows2.png",
    (0,0), WhileSpeaking("shi", "shio mouth", "images/shiori/Mouths/mouth_closed.png"))

image shiori sad = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), "images/shiori/Eyebrows/eyebrows3.png",
    (0,0), WhileSpeaking("shi", "shio mouth", "images/shiori/Mouths/mouth_closed.png"))

image shio eyes:
    "images/shiori/Eyes/eyes_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "images/shiori/Eyes/eyes_closed.png"
    .25
    repeat

image shio mouth:
    "images/shiori/Mouths/mouth_open1.png"
    .2
    "images/shiori/Mouths/mouth_open2.png"
    .2
    "images/shiori/Mouths/mouth_open3.png"
    .2
    repeat