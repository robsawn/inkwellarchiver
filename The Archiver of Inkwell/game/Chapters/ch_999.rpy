label ch_999:
    "this is chapter 1."
    ## show shiori stoic
    shi "Here is my first line"

    $ time = show_time(1708311600)
    "it says [time]"

    menu:
        "Tell her she's pretty.":
            jump choice_testpretty

        "Tell her she's adorable":
            jump choice_testadorable
        
        "Stay silent.":
            jump choice_testsilence
        
    label choice_testpretty:
        $ flag_testpretty = True
        
        shi "Nah... Thanks though!"

        jump choice_testdone
        
    label choice_testadorable:
        $ flag_testadorable = True
        
        shi "Oh, you're so sweet..."

        jump choice_testdone

    label choice_testsilence:
        $ counter_testsilence += 1
        
        shi "What's up?"

        jump choice_testdone
    
    label choice_testdone:
        if counter_testsilence > 0:
            shi "What's wrong? Why so quiet?"
        
        else:
            shi "You're gonna make me blush..."

        if flag_testpretty:
            shi "What made you call me pretty?"
        
        if flag_testadorable:
            shi "What made you call me adorable?"