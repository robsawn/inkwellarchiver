define shi = Character("[shiori_name]",color='#c213e5',window_background="gui/textbox1_purple.png",callback=speaker("shi"))
define p = Character("[player_name]",color='#0de3a6',window_background="gui/textbox1_grey.png")
define p_i = Character("[player_name]",color='#0de3a6',window_background="gui/textbox1_grey.png",what_prefix="{i}",what_suffix="{/i}")
define p_shi = Character("[player_name] & [shiori_name]",color='#687BC6',window_background="gui/textbox1_purple.png",what_prefix="{i}",what_suffix="{/i}")
define s = Character("Classmate",color='#FFFFFF',window_background="gui/textbox1_grey.png")
define fs = Character("Focused Student",color='#FFFFFF',window_background="gui/textbox1_grey.png")
define qs = Character("Questionable Student",color='#eefc87',window_background="gui/textbox1_grey.png")
define o = Character("911 Operator",color='#eefc87',window_background="gui/textbox1_grey.png")
define fc = Character("Frustrated Yellow Stranger",color='#FFFF00',window_background="gui/textbox1_grey.png")
define vc = Character("Vicious Yellow Stranger",color='#FFFF00',window_background="gui/textbox1_grey.png")
define sc = Character("Serious Yellow Stranger",color='#FFFF00',window_background="gui/textbox1_grey.png")
define hc = Character("Helpful Cultist",color='#FFFF00',window_background="gui/textbox1_grey.png")
define cc = Character("Confused Cultist",color='#FFFF00',window_background="gui/textbox1_grey.png")
define cl = Character("Cult Leader",color='#FFFF00',window_background="gui/textbox1_grey.png")
define cat = Character("Cat",color='#FFFFFF',what_prefix="{i}",what_suffix="{/i}",window_background="gui/textbox1_grey.png")
define k = Character("Knight",window_background="gui/textbox1_grey.png",color='#F3A5A5')
define r = Character("Rook",window_background="gui/textbox1_grey.png",color='#B4B1D3')
define m = Character("Monster",window_background="gui/textbox1_grey.png",color='#00ffff')

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
image shiori neutral = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth neutral", "images/shiori/Mouths/mouth_neutral.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows1.png")

image shiori smile = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_closed.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows1.png")

image shiori elated = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_open1.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows4.png")

image shiori happy = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_open1.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows1.png")

image shiori surprised = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth neutral", "images/shiori/Mouths/mouth_open4.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows4.png")

image shiori frown = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_frown.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows2.png")

image shiori frown = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyesshock",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_frown.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows3.png")

image shiori sad = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_frown.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows4.png")

image shiori satisfied = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "images/shiori/Eyes/eyes_closed.png",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_closed.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows2.png")

image shiori stunned = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyesshock",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_open4.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows4.png")

image shiori shocked = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyesextreme",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_open5.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows4.png")

image shiori wink = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyestease",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_open1.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows1.png")

image shiori cry = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "images/shiori/Eyes/eyes_closed.png",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_open4.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows5.png",
    (0,0), "images/shiori/Eyes/tears.png")

image shiori happytearsclose = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "images/shiori/Eyes/eyes_closed.png",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_closed.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows5.png",
    (0,0), "images/shiori/Eyes/tears.png")

image shiori mortified = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyesextreme",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_open5.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows4.png")

image shiori mad = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_frown.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows_angry.png")

image shiori serious = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth neutral", "images/shiori/Mouths/mouth_neutral.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows_angry.png")

image shiori smug = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyes",
    (0,0), WhileSpeaking("shi", "shio mouth normal", "images/shiori/Mouths/mouth_closed.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows_angry.png")

image shiori stare = Composite(
    (562,840),
    (0,0), "images/shiori/base.png",
    (0,0), "shio eyesshock",
    (0,0), WhileSpeaking("shi", "shio mouth frown", "images/shiori/Mouths/mouth_frown.png"),
    (0,0), "images/shiori/Eyebrows/eyebrows_angry.png")

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

image shio eyesshock:
    "images/shiori/Eyes/eyes_opensmall.png"
    choice:
        1.5
    choice:
        2.0
    choice:
        1.0
    # This randomizes the time between blinking.
    "images/shiori/Eyes/eyes_closed.png"
    .25
    repeat

image shio eyestease:
    "images/shiori/Eyes/eyes_wink.png"
    choice:
        1.5
    choice:
        2.0
    choice:
        1.0
    # This randomizes the time between blinking.
    "images/shiori/Eyes/eyes_closed.png"
    .25
    repeat

image shio eyesextreme:
    "images/shiori/Eyes/eyes_open_small_pupils2.png"
    choice:
        1.5
    choice:
        2.0
    choice:
        1.0
    # This randomizes the time between blinking.
    "images/shiori/Eyes/eyes_closed.png"
    .25
    repeat

image shio mouth normal:
    "images/shiori/Mouths/mouth_closed.png"
    .1
    "images/shiori/Mouths/mouth_open1.png"
    .2
    "images/shiori/Mouths/mouth_closed.png"
    .15
    "images/shiori/Mouths/mouth_open2.png"
    .2
    "images/shiori/Mouths/mouth_closed.png"
    .17
    "images/shiori/Mouths/mouth_open3.png"
    .1
    repeat

image shio mouth frown:
    "images/shiori/Mouths/mouth_frown.png"
    .1
    "images/shiori/Mouths/mouth_open5.png"
    .2
    "images/shiori/Mouths/mouth_frown.png"
    .15
    "images/shiori/Mouths/mouth_open5.png"
    .2
    "images/shiori/Mouths/mouth_frown.png"
    .17
    "images/shiori/Mouths/mouth_open5.png"
    .1
    repeat

image shio mouth neutral:
    "images/shiori/Mouths/mouth_neutral.png"
    .1
    "images/shiori/Mouths/mouth_open4.png"
    .2
    "images/shiori/Mouths/mouth_neutral.png"
    .15
    "images/shiori/Mouths/mouth_open4.png"
    .2
    "images/shiori/Mouths/mouth_neutral.png"
    .17
    "images/shiori/Mouths/mouth_open4.png"
    .1
    repeat