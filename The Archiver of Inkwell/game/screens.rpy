################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        textbutton _("Extras") action ShowMenu("extras")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    #add gui.main_menu_background
    add gui.main_menu_background
    add gui.game_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    imagebutton auto "gui/mainmenu/start-%s.png":
        xpos 0
        ypos 335
        action Start()

    imagebutton auto "gui/mainmenu/load-%s.png":
        xpos 0
        ypos 425
        action ShowMenu("load")

    imagebutton auto "gui/mainmenu/prefs-%s.png":
        xpos 0
        ypos 520
        action ShowMenu("preferences")

    imagebutton auto "gui/mainmenu/about-%s.png":
        xpos 0
        ypos 610
        action ShowMenu("about")

    imagebutton auto "gui/mainmenu/extras-%s.png":
        xpos 0
        ypos 700
        action ShowMenu("extras")

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")



## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation
    
    textbutton _("Return") style "return_button" action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("\nThis game contains third-party sounds and uses third-party programs to assist with filtering of scenes.")
            text _("\nThis game is a product of 'The Novelites' Workspace'.")
            text _("\n~~~~~")
            text _("\nServer Admin:\n    Shiori's Jacket")
            text _("\nDirector:\n    robsawn")
            text _("\nWriters:\n    Alice\n    ChemistWeeb\n    MakeShiftWriter\n    Penguiboss\n    robsawn\n    Kronosok Kusok\n    SynergyREEE\n    Wax\n    Zero Zeta")
            text _("\nEditors:\n    Ingram\n    robsawn\n    Thadd\n    Wax")
            text _("\nSprite Artists:\n    Ichira (Fantasy Characters)\n    Jermy (Shiori, Yellow Stranger)\n    Nobu (outlines, Fantasy Characters)")
            text _("\nScene Artists:\n    hzlform (library)\n    Yomosaka (main menu)\n    P!ckleMan (cafe)\n    Phosphophyllite Boss")
            text _("\nAnimators: \n    Jusagi-chan (main menu)")
            text _("\nComposers & Musicians:\n    Nokutaan\n    Sinnoh")
            text _("\nProgrammers:\n    robsawn")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen extras():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Extras"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Audio Drama\n\n"
            text _("A group of Novelites (credited below) came together to create an audio drama, just for Shiori Novella! You can find it {a=https://youtu.be/h18nHdNIfgE}here{/a}!\n\n")
            text _("Writer/Director/Producer:\n    Kracken")
            text _("\nArtist:\n    Okato")
            text _("\nAudio Engineering and Music:\n    Sinnoh")
            text _("\nCast in order of appearance:\n    Party Planner Novelite - Real_\n    Helpful Novelite - Alice\n    Neko Nya-velite/Considerate Novelite - Neon\n    Chef Novelite - NostalgiaDrive\n    Wizard Novelite - Smilely\n    'You Dirty Novelite' - TD\n    'Stealthy' Novelite - Redbricked\n    Earnest Novelite - Siren\n    'Came back with the Milk' Novelite aka Dad - Mizu\n    Awestruck Novelite - TripleD\n    Timid Novelite - Wax\n    Tattoo Novelite - Kracken")
            text _("Special Thanks:\n    Shiori's Jacket")
            text _("\n~~~~~\n\n\n\n\n")


            label "Fan Letters\n\n"

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            #AlphaCas
            text _("AlphaCas\n~~~~~\n")
            text _("Dear Shiorin >////<\n\n")
            text _("Happy Birthday, Shiorin! Thank you for being our wholesome archiver! I would like to thank you for all your hard work for all novelites. I love how you fostered a large community full of passionate people, who came together and created this wonderful project for you. You have shown me how limitless content creation is via your vlog content, unity streams, and piano recording streams. Thank you for inspiring me with your creativity, and I aspire to have the courage to push the limit of content creation like you.\n")
            text _("Also, thank you for always supporting your community. I like how you support all the fanworks through twitter and even display fanart in your stream. That means a lot to me as an artist.\n")
            text _("Keep shining bright as our best archiver. You have my support, Shiorin!\n\n")
            text _("AlphaCas\n~~~~~\n\n\n")
            
            #Anastas
            text _("Anastas\n~~~~~\n")
            text _("Happy birthday, Shiori Novella!\n")
            text _("I've been watching almost every stream of yours ever since your first Sonic Frontiers stream! I love everything about you: your stunning Live2D model, your beautiful outfit and accessories, your beautiful yellow glowing eyes, your beautiful lips and smile, your cute voice, your beautiful hair with the color of half gray and half black, your unhinged but quite playful personality, and last but not least: your unique content, including your introduction for us to quite a lot of underrated horror games instead of something that is currently popular, your stream clips, your vlogging videos, and your piano playing skills!\n")
            text _("Thank you so much for hearting my comments under most of your streams and most of my writing prompts, as well as some of my posts on Twitter/X! I really appreciate you being so kind to me! I hope you continue doing that!\n")
            text _("And I hope you continue making me and other novelites happy with your future content as well! Oh, and I hope you'll be able to learn more Unity and make the Unity game of your dream as well!\n")
            text _("Anyways, I hope you have the best birthday ever! And just so you know, whenever you're feeling down, you can always contact me and other novelites!\n")
            text _("With love from Anastas\n~~~~~\n\n\n")

            #Blackwolf24
            text _("Blackwolf24\n~~~~~\n")
            text _("Dear Shiori,\n\n")
            text _("I hope this letter finds you well on your most joyful of Birthdays. I can't express how thankful or grateful I am to you for letting me be a part of this absolutely Wonderful community of Novelites. I still remember your debut like it was yesterday when you said, “I want you to scream for me~ Is that you can do for me~?” Party Balloons and all! The thing that's kept me coming back time and time again will always be your absolutely soothing voice. I still have my moments where even during a regular Zatsudan I'll be put to sleep by just you singing very softly. And even some normal more laid back streams.\n\n")
            text _("I've made Lots of friends in Inkwell. Met lots of composers and musicians and learned quite a bit of things to help me in my dream of being my own musician. Seeing you cry on stream, laughing, talking with not just your coworkers/friends in your own Gen, but other gens as well has been so much fun. I know you'll have Lots of more fun and cozy and absolutely whacky tangent filled streams and activities for us Novelites in the future and I can't wait. Now, if you'll excuse me your Highness, I must get lost in your Insanely beautiful eyes again~\n\n")
            text _("All the Headpats and cuddles from us to you. Your Midnight Wolf Novelite.\n\n")
            text _("Love, Blackwolf24\n~~~~~\n\n\n")

            #Boonster
            text _("Boonster\n~~~~~\n")
            text _("Dearest Princess-Nurse-News-Nyan-Cow-Toe-Judge-Rapper-Gamer-Protag-Wolf-Teacher-Chef-Witch-Nun—and so much more—vella,\n\n")
            text _("Happy birthday! I hope your day is brimming with joyous activities, surrounded by equally fantastic company and sumptuous food that elevates your soul to a blissful realm of euphoria. You deserve all of this and so much more. Please forgive my usual brevity; I tend to embrace a laconic style, but today, I'll make a concerted effort because you truly deserve to know how cherished you are.\n\n")
            text _("On this special day, I wanted to take a moment to tell you how much you mean to me. As I typed the opening greeting, I was reminded of all the wonderful moments we've shared throughout the year. I'm always amazed by the level of creativity and diversity that bursts from your imagination. Whether you're streaming, crafting stories, developing in Unity, playing piano, or singing, your talent and hard work know no bounds.\n\n")
            text _("It's a story I've heard retold ad infinitum—your ability to rekindle and ignite the flames of passion never ceases to amaze me. For many years, I've renounced pixel art and video editing, but your infectious enthusiasm and tenacity have breathed new life into passions I had long forgotten. And when you share your passion with us and the world, I'm drawn to your efforts like a moth to a flame. When you cry, I cry; when you laugh, I laugh; when you smile, I smile.\n\n")
            text _("Thank you for being our precious, charming, and adorkable Archiver. Let's continue to laugh, cry, smile, and embrace the future together. Let's continue to make more treasured memories. Let's continue to find our happily ever after.\n\n")
            text _("In my usual and true fashion, I leave you with this: I'm proud of you, Shiorin. Now and forever.\n\n")
            text _("Sincerely, your Novelknight,\nBoon.\n~~~~~\n\n\n")

            #Firemind
            text _("Firemind\n~~~~~\n")
            text _("Happy day of birth, Shiori~n!\n\n")
            text _("I hope you'll eat good and do the things you want and love to do the most in your special day! I'm honestly quite bad at wishing others a happy birthday, I rarely celebrate mine as is, I think this had to do with barely having friends.. if any www. But this honestly changed recently when you joined Hololive! I've met amazing Novelites whom I treasure and call friends now, we celebrated my bday in discord! It was short but sweet and I couldn't ask for more.\n\n")
            text _("You changed my perspective on many things and there's no words I can use to express how thankful I am to your mother for birthing you www. (and maybe also to mama Yagoo? www)\n\n")
            text _("Thank you so much for making all of our days better, and I hope we Novelites have also helped on making your days better.\n\n")
            text _("We love you and we are so proud of all the things you've achieved thus far, and I cannot wait to see you accomplish more amazing things in the future, be it small or big we will be there to celebrate it with you.\n\n")
            text _("So uhmm I think my anxiety on wishing others a happy bday is kicking in so I'll leave it here www, I can't wait to see what you have prep for your bday! I'm planning on making some cheese tonkatsu and for dessert I'm debating between passion fruit cheesecake or some fruit jello with condensed milk (yeee not that healthy www).\n\n")
            text _("Sooo yep! Happy Birthday !!! Love ya!\n\n")
            text _("-Firemind\n\n")
            text _("(Sorry for any spelling errors and whatnot, english is too hard www)\n~~~~~\n\n\n")

            #Forgotten Skinner
            text _("Forgotten Skinner\n~~~~~\n")
            text _("Dear Archiver,")
            text _("Good golly, what a ride it was. To see how much you've grown since debut, and all those wonderful things you've achieved… It's not going to be easy to express how much this day means to us, but I can say, it all started with a tangent...\n\n")
            text _("It's been a long time since you joined Hololive and made this wonderful community, full of artists, writers and probably the most creative minds I've ever seen.. And now, that we are all here celebrating your birthday, I must say with all my heart… Thank you, Shiori. For igniting the dreams and inspirations of so many aspiring artists, writers and storytellers around the world. For all the good memories and smiles you brought to this community; and especially for always encouraging us novelites to be glad to be ourselves. When days become too dark to handle, your advice feels like a hopeful breeze, bringing back a smile I thought was a goner long ago. For being related to the abyss, you really made this place a brighter one for sure.\n\n")
            text _("Anyway, I hope you have a wonderful birthday and that you spend time with all the people you love and care for. Never forget how much us novelites appreciate and are grateful to you. Inkwell will be always there for you, as you did for all of us. And as for me, I can't help but wonder what story is waiting to be unfolded by you next. Whenever that time comes, I'll be there to follow your journey. Happy Birthday, Archiver… You deserve the happiest of them all!\n\n")
            text _("Last eternal, Shiori Novella\n")
            text _("Sincerely,\nForgotten Skinner\n~~~~~\n\n\n")

            #General Scraggy
            text _("General Scraggy\n~~~~~\n")
            text _("Shiori~n!!!\n\n")
            text _("Hello Shiori!! By the time you're reading this, it will be your birthday! HAPPIEST OF BIRTHDAYS, MISS NOVELLA!! I hope the day is nothing but wonderful! I'm writing this letter to you to express my gratitude towards you! I am so grateful that you joined Hololive. You've brought a lot of joy with your content, whether that's streams, Twitter spaces, or, of course, your wonderful tangents! I also must thank you personally because you are partially the reason that I got back into drawing, so I guess you could say you were my muse. Haha, well, I will leave it at that before I get too into it and start tearing up.\n\n")
            text _("Once again, happy birthday, Shiori!\n\n")
            text _("Your loyal novelite\n")
            text _("General Scraggy\n~~~~~\n\n\n")

            #Guzumi
            text _("Guzumi\n~~~~~\n")
            text _("Dear Shiorin,\n\n")
            text _("Happy Birthday to our beloved archiver! I hope this letter puts a smile on your face and you can have a memorable time with your genmates. Ever since your debut, it's been 8 months and I've learned so much with you in quite the short span of time. I always love gaining more knowledge thanks to you. No matter the topic nor stream, I always learn something new and interesting. It's alway a fun time seeing you ramble on about your hobbies, interests and passion.\n\n")
            text _("Thank you for forging such a wonderful community where I met my friends and aspiring novelites with different talents and quirks. Seeing you chase your goals makes me want to be as skilled as you someday! With your tech savvy brain to your endless overflowing imagination you use for tangents and passion projects. I wish to see you grow and reach limitless heights!\n\n")
            text _("Thank you for joining Hololive and being an inspiration to the Novelites and I.\n\n")
            text _("With lots of love and wishes,\n\nThe one and only, Guzumi~\n~~~~~\n\n\n")

            #Jermy
            text _("Jermy\n~~~~~\n")
            text _("Happy birthday Shiori!\n\n")
            text _("You've probably got a lot of fun stuff planned for today, so I hope you aren't too stressed out and you've been able to get as much rest as you need to!\n\n")
            text _("I want to thank you so much for being such a wonderful, supportive, and funny archiver!\n\n")
            text _("I love the way you tangent and tell us about your random thoughts and stories from your life! It really makes it feel like we're all just chilling and listening to you chatting somewhere in Inkwell.\n\n")
            text _("You also know so much about things like Unity and obscure otome games! I learn something new in every stream!\n\n")
            text _("I'm so happy my art reaches you by the way! It means a lot to me when you like and feature it! I never thought my art would get any attention, but you've given me so many opportunities for my art to be seen, and I can't thank you enough for it! I see a lot of artists making fanart with the emo bangs, and it makes me happy knowing I was part of that! You've inspired me to make a lot more art than I used to and to keep pushing forward with it!\n\n")
            text _("You've mentioned how you hope that you're able to brighten people's days. I can say for sure you've brightened many of mine. Last year, I really wanted to find an online community where I felt I belonged. Since you debuted, you've been able to build that community and we've had so many great memories together!\n\n")
            text _("I hope this visual novel makes you smile. We worked really hard on it, and if it repays even a little bit of your kindness, that's all I could ask for. I'm tearing up a little, heh.\n\n")
            text _("Thank you for everything! Let's make even more wonderful memories! :)\n\n")
            text _("Sincerely,\n\n")
            text _("Jermy (jermy_9)\n~~~~~\n\n\n")

            #Jusagi Chan
            text _("Jusagi Chan\n~~~~~\n")
            text _("Happy birthday Shiorin!\n\n")
            text _("Thank you for everything you've done for all of us. You're someone in Hololive I really admire because you're not afraid to go against the norm and just do whatever the hell you want. It takes a lot of bravery to do that and I have so much respect for you.\n\n")
            text _("You've been a huge inspiration in my animation journey. You probably don't remember but you were one of the first hololive members to say something nice about my animations (even though they were pretty crappy back then www) and I've held your positive words in my heart for all these months. I'm never (ever) going to stop doing hololive animations so I hope you enjoy all the Shiorin and Advent animations from now on!\n\n")
            text _("But anyways, if you ever feel down or dejected or the slow crawling shadow of impostor syndrome, take it from your Novelites. We see how hard you work. We see how passionate you are. We see how much of yourself you pour into Hololive even if it's outside your comfort zone. And we appreciate it!! All of us are going to cheer you on forever!\n\n")
            text _("Happy birthday and see you at the next stream, Shiorin!\n\n")
            text _("Jusagi Chan\n~~~~~\n\n\n")

            #Kianrame
            text _("Kianrame\n~~~~~\n")
            text _("Shiori~n!!!\n\n")
            text _("Hello Shiori!!!!!! I wanted to reach out and wish you a happy birthday!\n\n")
            text _("I wish you a joyful birthday and a memorable day. I'm happy to one of the Novelites. I really like your streams and speed running stream. You can't believe how happy I was when you saw my cosplay, such a stupid thing made my cry.\n\n")
            text _("You helped me go through depressed day and working on my projects for college, watching you made me motivated to finish them.\n\n")
            text _("You give me courage to try new things and not to give up. And I love how you can drill one topic for infinite time.\n\n")
            text _("Thank you for everything and sorry if I made mistakes, I'm not good at writing and spilling out my emotions ;;;\n\n")
            text _("Extra kisses for Pepper (and you Ofc)\nKianrame\n~~~~~\n\n\n")

            #MiscDan
            text _("MiscDan\n~~~~~\n")
            text _("Happy birthday wishes to our happy Shiori~n!!\n\n")
            text _("I just want to thank you from the bottom of my heart for all the fun, smiles, and happiness you've given us all. I'm forever grateful I got to know you and the Novelites, as being part of this community has proven to be super comfy and welcoming!\n\n")
            text _("I never consider myself as active a fan as all the others, but I've always been happy sharing my artwork, highlights, clips and projects in the hashtags. I greatly respect that you always reach out to your fans wherever you can, and just hearing you wish the very best for everyone, fans and genmates, is the most heartwarming experience.\n\n")
            text _("Thank you for always lifting our spirits. Thank you for including us all in your community projects. Thank you for the highly clippable moments no matter what you do. And most of all, thank you for simply being here, Shiori. You're a true gift to us all.\n\n")
            text _("You're the sweetest, you're the funniest, and just hearing your tangents is always a treat. May you have a wonderful birthday and here's to many more Shiori shenanigans to come!\n\n")
            text _("Much love and warm regards,\nMiscDan\n~~~~~\n\n\n")

            #MTRY
            text _("MTRY\n~~~~~\n")
            text _("Happy birthday, dear Shiori~n!!\n\n")
            text _("I hope you have the most wonderful and amazing day today, filled with amazing gifts, food, and most importantly, memories with everyone. Thank you so much for all the amazing time you have given us. I can't describe just how impactful you have been to my life over the past 9 months. Having the experience to start drawing a fanart has been one of the biggest turning points in life within the past year. It was quite a nerve wracking moment when I first posted my artwork online, but thanks to you and your wholesome community, I gained lots of courage!\n\n")
            text _("I still recall back to the first ever drawing I drew under the ShiorinSketch tag, which was a very crude sketch of Novelknight design! That was my first ever fanart of a Vtuber I've ever made, but it sparked a sense of motivation within me. Thanks to your positive feedback and care you've shown to the artistic side of the community, it greatly pushed me to proceed forward and keep drawing more, trying out different art styles, topics and even trying to make an asset. It felt like breaking out an eggshell at first, not having any experience in being in a fandom in the beginning. But now that a sufficient time has passed, I can proudly claim that making that decision was one of the best thing I've done! It got me back to drawing out of passion, I've made many amazing friends amongst the Novelites, and it even allowed me to start commissions and showed a possible career path as an artist. Seeing you still using my assets, I am so honored and thankful, and it just excites me to keep on drawing more!\n\n")
            text _("I can't thank you enough for what you've done for me, and I can assure you that so many Novelites feel exactly the same! As one, I must say thank you from the bottom of my heart. Today is a very very special day, and you deserve all the Novelites' love! Once again, happy birthday and best wishes,  and I look forward to many more memories to make!\n\n")
            text _("Yours truly,\nMTRY, a Slimy Novelite\n~~~~~\n\n\n")

            #Nokutaan
            text _("Nokutaan\n~~~~~\n")
            text _("Today is a really special day!\n")
            text _("(I'm sorry about my English, it's very bad but I'm trying.)")
            text _("Your works are always incredible for me and I'm really grateful for all the content you put out: from the writing prompts to the piano stories, from livestreams and videos to audio spaces and Unity scenes.\n")
            text _("I genuinely think that Shiori is amazing and unique, I'm sure your works inspired a lot of people all over the world! I really enjoy everything you put out, supporting you or even just looking at your merch makes my day better!\n")
            text _("I'm very happy to be here and I couldn't have it any other way: I'm going to be a NovelKnight forever!!\n\n")
            text _("I wish you a very happy birthday and lots of happiness on your way, I'm going to eat something with lots of chocolate for this!\n")
            text _("            -Nokutaan\n~~~~~\n\n\n")

            #P!ckleMan
            text _("P!ckleMan\n~~~~~\n\n")
            text _("Happy birthday to the best archiver in the world and our royal highness of Inkwell,\nShiori Novella!\n")
            text _("You are the smartest, funniest, and adorkable person I have ever met. Every time I tune into your stream, your jokes, shenanigans, and tangents always give me a good laugh whether I am having a good or a bad day. Not only do your streams make me laugh, but I also get to learn new things from you like learning Unity, Japanese, how to cook a hot pot, or learn some new words like INNONCENT. What I also love about your streams is how you love to share your favorite songs, your childhood stories, otome games, and interests in clothing like lolitia dresses. All of these reasons are why I love your streams and why they are so special.\n\n")
            text _("Not only are you the most entertaining archiver in the world, but you are the most inspiring, too. Ever since I started watching you, I always loved your design, and it made me want to draw you. Now, I want to improve my drawing skills and draw you more often. I've been an artist for some time in my life and I've been decent at it, but my passion for art has grown even more thanks to you.\n\n")
            text _("Your community prompts and membership stories have also been very inspiring. I enjoy reading through them and writing follow up stories that come from my silly and dorky brain, hahaha. I may not be the best writer in the world, but I enjoy writing for fun. Thank you for making writing more entertaining, Shiori!\n\n")
            text _("I want to end this fan letter by saying thank you for being part of my life and for being the best kamioshi. I'm proud to be your Novelite and Novelknight, and I'll always love and support you till the very end. I wish for you to have all of the happiness and love in the world. I can't wait to make more fun memories with you, and finally, I wish for you to have most amazing birthday ever.\n")
            text _("From your silly Novelite and Novelknight, P!ckleMan\n~~~~~\n\n\n")
            
            #PhilLegacy
            text _("PhilLegacy\n~~~~~\n")
            text _("Happy Birthday, Shiori! I hope you get everything that you want today. Thank you for everything you have done for us. Just you being you brightens our day. My life has gotten much more fun since I became a novelite. You were my introduction to Hololive, and I have been loyal Novelite ever since. I look forward to all of your streams. Watching you spend run a game is fun. I love listening to you singing while playing your piano. The zatsu streams are comfy and I enjoyed chating with you and the other novelites. You might not know it, but you have helped us more than you can imagine. You give people the courage to try things they were too afraid to do. You have changed people's lives for the better. You bring people together. We've all made new friends because of you. Because of you I gained the courage to try writing. Thank you for everything Shiori. Have a great birthday.\n")
            text _("By Novelite\nElizabeth/PhilLegacy\n~~~~~\n\n\n")

            #RavenTheBird_
            text _("RavenTheBird_\n~~~~~\n")
            text _("I hope you have a fantastic day, filled with all things good and most importantly of all: CAKE!! It's been such an absolute joy to witness your journey. I still remember the day of your debut, we couldn't have expected such an adorable cinnamon bun to be behind that mysterious persona. I remember I was so shy to interact with people and, frankly, it took me about a month or so to actually do it but when I did I discovered a community I feel right at home with. All thanks to you, so from the bottom of my heart, I thank you, truly. You have pushed me to write more, something I always loved doing but never actually attempted out of fear. The other things such as drawing or music are still a work in progress, but I'll get there! I hope to be here for many more birthdays and you can always count on my support! I'm gonna wrap this up as it's getting quite long. I could say so much more but I'll leave it off on a thank you and a hope that your days are filled with happiness. You deserve it.\n\n")
            text _("With love,\nFrom the messenger birb of Inkwell,\nRaven\n~~~~~\n\n\n")

            #Real_
            text _("Real_\n~~~~~\n")
            text _("Happy birthday, Shiori!\n\n")
            text _("I hope that you have an especially great day today, and that you can have some good food and some nice birthday loot! Thank you for all the gifts you've given us Novelites over your time here already, from the only slightly unhinged chats and ramblings to the wonderful community Unity (commUnity?) projects, writing, and artwork projects that you've put together for us to take part in. Your willingness to go above and beyond like that is always touching, and it's what's made me as loyal a Novelite as I am. I've never been as active in a fan community as I have been with yours, so thank you for providing an environment where I can come out of my shell for a bit! Here's to this birthday, and many more yet to come with the Novelites at your side!\n\n")
            text _("Happy birthday and many well wishes,\nReal_, Novelknight\n~~~~~\n\n\n")

            #Recidivous
            text _("Dear Shiori,\n\n")
            text _("Happy birthday! It's the one day of the year you're entitled to spoil yourself. Don't hesitate to relinquish some of your responsibilities and act more selfishly, like eating your favorite foods or buying new dresses!\n\n")
            text _("You're my muse, Shiori. I have never been more inspired to write since you debuted as your writing prompts have allowed me to take up writing again. I look back at the days before I started writing for the prompts, realizing that I barely indulged in a habit I once loved to do. Now I'm swamped with so many ideas and projects that I have actually to organize and sort them by priority!\n\n")
            text _("Your encouragement to the Novelites to keep pursuing their passions and to improve themselves is what helps me keep going even in the moments I want to give it all up again.\n\n")
            text _("I want you to know that the Novelites and myself will always support you as you have always done for us. We know how hard you work, and we see how much love, care, and passion you give to everything you do. If there comes a time you're questioning yourself or are feeling dejected and alone, remember that you will always have us who will cheer you on.\n\n")
            text _("Once more, happy birthday! I can't wait to watch your next stream, Shiori.\n\n")
            text _("Recidivous\n~~~~~\n\n\n")

            #Redbrick
            text _("Redbrick\n~~~~~\n")
            text _("To Miss Shiori Novella\n\n")
            text _("No words can describe how greatful I am to know you. The kind heart that you showed, the hard work you do every day to make every streamings better...\n")
            text _("Your words with generousity made me cry from the inside. Interaction with us was no contest to any other fake smiles and praises that I had for my entire life.\n")
            text _("Thank you for giving me hope that I can do something to talents that I like. (Of course, it's admire-like, not love-like)\n")
            text _("Wanna say a lot in this letter, but that'll be boring and I think I enough said those on Twitter.\n")
            text _("I hope one day you and Advent visit Korea too.\n")
            text _("Until that miraculous day, Advent Advance!\n")
            text _("Sorry for my non organized thoughts and sayings\n\n")
            text _("From Korea, Redbrick.\n~~~~~\n\n\n")

            #robsawn
            text _("robsawn\n~~~~~\n")
            text _("Hiya, Princess~!\nHappy birthday! I hope you have a really great day, and continue to have fun with life, and are happy and healthy! (So no eating moldy food, ok?)\n\n")
            text _("I'm sorry that I've had to lurk so much recently to get this done, but I'm always happy to help out with game dev stuff! This was an…. Interesting project to work on, but I look forward to working with novelites again in the future! This was a nice project to semi-relax with! I haven't worked on a VN in a while, I tend to work with other kinds of 2D games and 3D games!\n\n")
            text _("I wanted this to be a better VN for you, but we worked hard and I feel ok about where it ended up given everything that happened during development, and the really short timeline we had for writing, editing, art, and all that. So, I hope you enjoy it and get a chance to play it, on stream or off!\n\n")
            text _("Anyway, I don't want to bore you too much, or drag on too much, so I'll just say: Happy birthday Shiorin! I hope you someday have time to go through and read the shiorin stories, since you mentioned enjoying reading them before, and I hope you continue having fun with Advent and everything else you do! I'm glad you're in a better place than you used to be!\n\n")
            text _("Your very eepy, loyal, sometimes useful, sometimes funny Novelknight since Day 1 (despite YouTube messing with me -.-),\nrobsawn\n~~~~~\n\n\n")

            #Shiori's Jacket
            text _("Shiori's Jacket\n~~~~~\n")
            text _("Happy Birthday, Shiori! I can't believe it's been 8 months since you've first debuted. Have you eaten anything nice? Have you rested well in regards? If so, I'm glad and happy for you. Today is May 2nd, which means it's your day. It's the day you've been born. Which means it's the day where you should be happy and celebrate with your peers, The Novelites.\n\n")
            text _("I want to thank you for coming into our lives and having the courage to bring back the spirits that all of us have lost. I can't speak for everyone but just know that you have brought back the passion that none of us could ever achieve. And because of you, we are happy with the progress we've made together. Before your existence, I used to be someone who I couldn't find a purpose for. And despite drawing, I just lost the passion within. I was a nobody and I struggled a lot in life ever since. However when you appeared, I tried my best to look into the positives by watching your streams daily, without a miss. And honestly it worked. Why? Because you brought back the fire that I've lost. My passion for art has returned because I felt encouraged by you. Without you, I wouldn't have made such progress like I have right now. I've made so many new friends, and also… made my own community. Because of you, I've met so many lovely and friendly communities who accepted me as their own. You and the Novelites have saved me from the void that I've felt throughout the years and because of that I want to thank you for everything.\n\n")
            text _("I've started to draw so much throughout the past few months because of you. Ever since you started to like my drawings and all, I've felt appreciated in my efforts regardless of the progress. And even though I still have a lot to work on, you never doubted my abilities as an artist. And it's not just me, The Novelites too.\n\n")
            text _("You are hardworking, passionate, kind, cute, positively unhinged, and such a sweetheart with a lovely soul within you. And that is what we admire about you. You may say things that are sometimes questionable, funny, or anything that sets your mind too, but you never stop being kind to others regardless of what you do. I'm pretty sure Advent feels the same. I can't speak for them. Believe in the fact that you've grown so much and improved. I really loved your first music cover and honestly I always listen to it on repeat.\n\n")
            text _("With the intention of everything. I thought of making something for you in return for all of the precious gifts and spoils you gave to us, Novelites. So I decided to organize a fan project for you to have as a gift. With the help of the Novelties' and community, we've decided to work together and give this precious gift to you. Not everything could be done but this was the best that we can do regardless of quality and such. This was our way to show you how much we all appreciate you for all the fun things you've done for us. You might say that we didn't have to do this. But we wanted to. We want to make your first year and birthday, the best of the best so you can never forget and have this archived (bookmarked) into your memories forever.\n\n")
            text _("We Novelites organized this exciting project for you to enjoy and end your day with a beautiful happy ending. I hope you like or love this. We will always be by your side until the end of time and we will always be rooting and supporting you no matter the outcome. You're never alone, and you deserve happiness. Never forget that. I hope you enjoy this gift. Let's celebrate together in Inkwell and have fun!\n\n")
            text _("As for me, Again, I want to thank you for bringing back my passion for art and encouraging me to do more, to continue drawing more, experience and learn new things, even to those who lost their passion within their talents. We wouldn't be here without you. So please, let's be happy and cheers for more memories to come! Cheers for more future achievements and every good thing to happen! Let's go on and make more memories together from here on out! We will rule and follow your lead!\n")
            text _("I hope you have a lovely and fantastic birthday!\n\n")
            text _("From, Project Organizer: Shiori's Jacket.\n~~~~~\n\n\n")

            #Sine_Fine_Belli
            text _("Sine_Fine_Belli\n~~~~~\n")
            text _("Happy Birthday Shiori!\n\n")
            text _("I remember well when you debuted. I was there watching all of Advent's debuts, including yours.\n")
            text _("You're one of my favorite Vtubers and oshies. I keep watching you because of how funny, Chill, comfy, and wholesome you are, and your funny, comfy, and chill streams are great!\n")
            text _("I watch your streams, gaming streams, karaoke streams, ASMR streams, and collab streams.\n")
            text _("I might not have been able to watch every stream, I wasn't able to attend and watch as many streams as I would have liked, but I enjoyed every stream I was able to watch. I'm glad that I was able to spend some time with you. Although I haven't watched most of your streams, I do enjoy the time I got to spend with you and the streams I managed to watch.\n")
            text _("I can't wait to see what you do, what you are also planning to do in the future. Here's to more fun and entertaining streams as well as your future plans!\n")
            text _("I'll continue to watch your streams and spend time with you\nWe are proud of what you achieved and accomplished.\nYou're such a great Oshi to have and I hope to attend more of your streams!\n")
            text _("Sine_Fine_Belli\n~~~~~\n\n\n")

            #Smilely
            text _("Smilely\n~~~~~\n")
            text _("Happy birthday Shiori!\n\n")
            text _("I can't believe it has been 8 months since your debut. I remember watching your debut stream and thinking “yeah, she's cool”. From then on, I continued to watch your streams, and realized you have become my oshi.\n\n")
            text _("You have this natural charisma that just draws people to you. You are so creative with the projects that you do like the Unity streams. Your tangents are quite entertaining and make me laugh all the time. Most importantly, you are just super genuine and kind.\n\n")
            text _("I also wanted to thank you for liking my little choreographies for both Advent's cover of Halloween Night, Tonight and your cover of Whisper Whisper Whisper. Truth be told, I have only danced seriously for a year now, but seeing your comments of encouragement gives me motivation to keep on improving. So if you ever decide to release another song in the future, I will be ready to work on a choreo for said song.\n\n")
            text _("The last thing I want to say before wrapping everything up is thank you for fostering such an amazing community. The Novelites have been so kind to me ever since I decided to get out of my comfort zone and actually interact with the community. There are so many talented artists, writers, musicians, voice actors, editors in Inkwell, and it's all thanks to you. So many people have continued their passion because of you. So no matter what, us Novelites will always support you with whatever talent we have to make you happy. Thank you for being our Archiver, and once again happy birthday Shiori!\n\n")
            text _("From Inkwell's Resident Dancer,\nSmilely\n~~~~~\n\n\n")

            #SourClout
            text _("SourClout\n~~~~~\n")
            text _("Shiori~n!!\nHappy birthday Shiori! I hope you have a great day full of friends, good food & fun! I've been a Novelite since September, your streams & sense of humour never fails to make me laugh. I can't remember laughing harder than seeing you clown on us during the Super Smash Bros streams. It is quite rare that a Hololive talent is as much of a gamer or more skilled than me, so I hope you know you're appreciated!\n\n")
            text _("Thanks for creating such a welcoming community & a fun unique interaction like the story prompts. Guys like me aren't as artistically inclined so it's great to have an Oshi that excels at the same skills as I do. I had given up entirely on writing 4 years ago but started again because of you, so thanks for the inspiration. I also get to enjoy a lot of games I would otherwise never have heard of without you.\n\n")
            text _("This is a bit dumb & selfish, but I really appreciated the time you hearted one of my story prompts. It's nice to know that my work is appreciated outside the context of D&D. I don't usually feel comfortable enough sharing the world I envisioned with others so I'm glad you & some Novelites enjoy it.\n\n")
            text _("You're truly an inspiration, both as a fellow writer & someone with a difficult past who embraces positivity, healing & growth despite it.\n\n")
            text _("Take good care of yourself, today & always. You deserve to be proud of your accomplishments!\n\n")
            text _("Happy birthday!!\n\n-SourClout\n~~~~~\n\n")

            #SynergyREEE
            text _("SynergyREEE\n~~~~~\n")
            text _("Happy birthday! Hope you enjoy your first mortality countdown as part of Hololive Production!\n\n")
            text _("Hi. It's me, the guy who made you some weapons and funny(?) memes on the internet. It's pretty funny, isn't it, that despite me being in this rabbit hole for 4 years now, it was you who pushed me to start creating something. I don't even remember how it started, probably from me reading how you encouraged us to make fanfictions of you right from debut. So I did, like everyone else, and the process of writing them pulled me into a new community that I enjoy staying in. I made new friends, I learned MMD animation, I helped make a visual novel about you, and I started to enjoy how it feels to interact with people again. So thanks, Shiori, for creating such a unique place to be in.\n\n")
            text _("Also, everytime you see and like the stuff I made, it gives me encouragement that what I made is actually enjoyable, and it gives me motivation to make more. For someone who struggles with finding motivation in doing anything, especially my responsibilities, this means a lot to me.\n\n")
            text _("Entertainment and being able to brighten someone's day is your goal, and you certainly hit those two marks spectacularly. At the very least, you've been shining like a star in these eyes of mine, brightening up my day without fail. And this time, I hope we can do the same for you with this visual novel. I hope you enjoy the stories we weaved, and I hope you enjoy this birthday project as much as we did creating it.\n\n")
            text _("Once again, happy birthday Shiori! Onwards to archiving these happy moments forever.\n\n")
            text _("(Also pay your child support)\n-SynergyREEE\n~~~~~\n\n\n")

            #Viratasya
            text _("Viratasya\n~~~~~\n")
            text _("Dear Shiori,\n\n")
            text _("I hope this letter reaches you well (would be weird if not), and that Pepper was a good boy today.\n\n")
            text _("I just wanted to express my deepest gratitude for you and everything you do for us Novelites. Be it your streams, your Spaces, your Twixxer posts or your unhinged tangents, everything you do, say or sometimes even scream brings joy to my heart. Damn, I even inhabited some of your lingo, like Shiover and Twixxer, in my daily life www.\n\n")
            text _("No but seriously, you are one of the reasons I am doing as good as I am now. You helped me through some really rough and lonely patches, like the Big (or like you now established 'Small') C, the big sadness and the fact that my fiancé was on the other side of the world for half a year now. You brought me back to this beautiful family called 'Hololive fandom', after I had some fallouts, and hey now I am here to stay forever, happy for this found family.\n\n")
            text _("Even tho its sometimes still so surreal for you, like you say so often, we Novelites will always be by your side and definitely like you till the end of all eternity, me absolutely included (Damn I am palnning a tattoo in your honors, I am committed www)\n\n")
            text _("Okay, gotta stop this now or I'll never end writing (or suddenly start crying). Have a beautiful day and keep being you, gorgeous, dorky Queen of Inkwell.\n\n")
            text _("Your,\nViratasya\n~~~~~\n\n\n")

            #Void Wyrm
            text _("Void Wyrm\n~~~~~\n")
            text _("Dear Shiori Novella, our precious Queen.\n\n")
            text _("This letter from me is made to commemorate your birthday, a special day for all of Inkwell. It is of great joy for me to be here to celebrate your first birthday with us in this wonderful community of ours.\n\n")
            text _("Ever since joining Inkwell last December, my life has changed greatly for the better. I became social over the internet again, I've met and learned about a lot of great people and I have gotten to understand and truly appreciate you over time.  Understanding how and why you are the way are, as well as all you do has helped me learn more about the special kinds of people out there and about myself and my special habits. All the while, I've experienced great joy seeing you grow and learn over your time with us.\n\n")
            text _("You've truly gotten accustomed to being here with us and all the friends you've made here. Along the way, we've laughed, we cried, we cringed, we smiled, we embrace your quirkiness and quiet self. You've achieved a great balance between your quiet self and your excitable self. Your streams are very entertaining, you get along with everyone and have lots of fun with them. You regularly engage with chat, asking us questions when needed and commenting on our posts.\n\n")
            text _("Its very fun watching your streams or seeing your twitter/youtube posts for what fun thing you'll say or post next. Your keen interest in anime and visual novels, along with the games you like has allowed me to hear and watch a lot of new content I would have never known existed otherwise. Its very interesting hearing your hobbies and interests such as your cute dolls or your cute fashion sense. Your very kind and sweet to us and animals. Salt and Pepper are very lucky to have you as their owner.\n\n")
            text _("You're not shy and timid anymore. You're very open with your emotions. You trust us and aren't afraid to tell us sensitive things now and show us your vulnerable side if you're feeling down. We and all your friends are always here to support you, whenever you need us. You make incredibly fun projects and show us the behind the scenes work put into those projects. I really love the unity scenes, the membership adventure stories and that snowed-in visual novel you made. Those are some great projects you made. Accomopolishing and growing so much, reaching 500K novelites in Inkwell. This place is truly shaping into a true kingdom over time. I'm proud of you for what you've achieved so far in hololive. You will be able to achieve more great things over time in hololive.\n\n")
            text _("I hope all your dreams come true over time. May this dream continue to be a splendid one for you. It's done wonders for your life, and will continue to do so for many years I believe. Your videos and shorts pick out and edit very funny moments from your streams. The other videos and shorts you make that aren't stream moments are very special too. The audio dramas are wonderful to listen to and I really loved the vlogging gear video. The educational stuff you make is very interesting to listen to. You have a lot of experience in youtube content and it shows. Lots of interesting facts and educational information can be learnt from your content. You make it very entertaining too.\n\n")
            text _("Some streams I really loved where the lord of the rings watchalongs, the membership zatsudans and the unity streams. Some games I loved watching you play were Sonic Frontiers, Ender Lilies and Slay the Princess. The handcam streams have been fun too. Those handcam streams have had their challenges and mishaps over time, but you've made some fun stuff out of them. As long as you had fun in those streams, we are happy. You've been very kind and nice to me when you respond to my comments in the streams. Gotten some fun responses from time to time. Finally, I love, love, love your piano playing and singing. It's so pleasant and fun to listen to. I think you will become great at those things someday. You put great effort into those things and it shows. We all love hearing you play and sing in the streams. I can see a great future where you and your friends jam it out greatly on the big stage with your 3d models in front of the loving fans. Your going to go far and do very well in hololive. I know it.\n\n")
            text _("This has been a long letter, so I will finish it here. Keep doing well Shiori, our dear Queen. We all love you. Thank you for being here with all of us and this great community you've made with us. From us to you Shiori, have a great day and an amazing birthday.\n\n")
            text _("With everlasting love from one of your many faithful caretakers,\nThe Void Wyrm.\n~~~~~\n\n\n")

            #Wrong
            text _("Wrong\n~~~~~\n")
            text _("Dear Shiori,\n\n")
            text _("I don't know how to write a proper letter, so I'll just wing it.\n\n")
            text _("It's your birthday today yay! (or at least that's what the official Hololive website says, but It's official, so I believe it). It's been like what, 8, maybe 9 months since your debut. I still remember when you used to talk about cannibalism on stream and now, you still talk about cannibalism but not as much as before I think (I'm not willing to check every vod to do the math, way too much work).\n\n")
            text _("I'd like to thank you for creating a pretty cool community consisting of flowers with eyes, pages with limbs, wyrms that are books, and knights that probably write novels. Seeing and reading everyone enjoy and reply to your prompts puts a smile on my face (We live in a society). The piano streams/spaces are also enjoyable to put as background music while doing other stuff (random dude comes out of nowhere and says “I'm stuff”).\n\n")
            text _("And with that I'm out of ideas to write, so to end this letter I'd like to thank you for all you do for the community, and I'd like to thank the community itself for organizing this. I hope you enjoy today because It's Shiori Novella's birthday!\nGet food, water, maybe some shelter while you're at it, and again on behalf of the Novelites and even the Novelights (Gotta throw em a bone every now and then “Bau bau”) thank you for being a cool archiver Shiori Novella.\n\n")
            text _("-Bobby Wrong\nP.S. I think letters with P.S. are cool! So I added one.\n~~~~~\n\n\n")

            #Yomosaka
            text _("yomosaka\n~~~~~\n")
            text _("Happy Birthday!\n")
            text _("I have been fulfilled every day since I met you and Advent. Thank you for always giving me so many interesting stories, piano playing, and lots of fun.\n")
            text _("I hope this year will be filled with many happy days for you, Shiori-san!\n")
            text _("- yomosaka\n~~~~~\n\n\n")

style extras_label is gui_label
style extras_label_text is gui_label_text
style extras_text is gui_text

style extras_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
