$ renpy.include("Helpers/characters.rpy")
$ renpy.include("Helpers/trackers.rpy")

label ch_0:
    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "The echoing bells once again resonate throughout the building, signaling the end of today’s classes. Typical chatter can be heard all around as I leave the premises, but it is soon replaced by the familiar pitter-patter of rainfall. As children play in the puddles and adults line up to buy from roadside stalls, A small childish part of your brain almost wants to join in, jump in the puddles to relive your childhood, those moments that seemed all too far yet close to you…"

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "The walk home feels more alive, contrasting with the scenery’s muted tone. I take my time walking, drinking in the quiet atmosphere that we call home, but it is periodically interrupted by my phone."

    #sound effect would be better than this
    "{i}bzzzzz. bzzzzz.{/i}"

    p "What’s going on in the group chat now…?"

    #if we have time/assets, would be good to just show a phone, with scrolling texts (no detail)
    "As I’m watching the texts come in, it looks like, instead of studying for midterms next week, everyone’s going out to a local bar for our weekly hangout."

    p "Do I want to go…? Nah. I’m already tired, I’d rather just go home and relax."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    #tapping sounds play
    "As I type out a quick response, telling my friends that I’m passing this time, a couple of jokes come in about me holing up in my cave, and, chuckling a little, I mute the phone and put it back in my pocket. Even if they’re my friends, it gets a bit exhausting being surrounded by people all day, pretty much every day, so it’s nice to have some alone time."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "As I walk, it’s easy to appreciate how the quiet rain around me creates a calm vibe. I turn down a walking path, continuing on my way home for the evening. The warm glow of the storefronts on either side tempts me to stop and take a load off."

    p "{i}Do I want to stop in somewhere…?{/i}"

    #heavier rain effects fade in, and at peak, fade lighter effects down 50% maybe?
    "Suddenly, the pattering on my umbrella intensifies, and the wind picks up. Hearing the creak of the umbrella straining, I realize the weather made the decision for me and duck into the nearest open storefront."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "Opening the door, I’m warmly welcomed by the twin aromas of brewed coffee and tea, the soft chattering of the store’s guests providing a pleasant backdrop. Inside a warm, dark wood-filled cafe, you see a couple of faces that you might have recognized from school mixed in with the crowd. All of them are a varied level of soaked; some alone with headphones, a couple talking about the sudden storm, and a group of students congregating around a couple of the big round tables in the center, some on their phones, others on laptops."

    "Up at the counter, a barista asks for my order, and I look up at the options."

    menu:
        "I’ll have green tea with added honey. Hot, please.":
            $ greentea = True
            p "I’ll have green tea with added honey. Hot, please."
            "The storm is making it feel colder, so a nice, hot cup of tea seems perfect right now."
        "Hmm, one Americano, please.":
            $ americano = True
            p  "Hmm, one Americano, please."
            "With it turning night relatively soon, I didn’t want to add too much caffeine to my system, but how can I resist a cup of coffee in a place like this?"
        "Hm… Can I get a cocoa? Large? With added caramel?":
            $ cocoa = True
            p "Hm… Can I get a cocoa? Large? With added caramel?"
            "The day has been feeling a bit daunting, to say the least. I deserve a little treat so let’s cut loose a bit on the sweets."
    
    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe? maybe split it into two?
    "After picking up my drink from the counter, I walk deeper inside to look for a seat. I don’t know if it is because of the storm or if this store is popular, but most of the tables have been taken already. Finally, I spot a free chair by the windows. It’s between a woman and a plant, but it’s a seat."

    "Her black hair shines in the warm light, but her jacket hangs down revealing a little of her shoulders, the fur collar flayed out on the sides, the back of it brushing her hair."

    "As I wind my way over between the tables, I notice she’s totally focused on a book. I don’t really want to disturb her, but I should still ask if it’s okay to sit there out of courtesy."

    #subtly fade up rain effects to signify approaching windows
    "As I walk up, I notice she’s totally focused on a book, and try to get her attention."

    p "Excuse me?"

    shi "..."

    p "Um... Sorry, excuse me?"

    shi "..."

    p "{i}She’s… really focused. Or, I’m being ignored, which seems just as likely, to be honest.{/i}"

    #could do an animation and sound effect here instead of saying it
    "I brace myself, and wave my hand next to her, hoping she notices this time."

    p "Excuse me?"

    shi "Hwah?! Oh! Can I... help you?"

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "As she turns to look at me, I notice her hair is split between a pitch black and a stark white, right down the middle. Her hair frames a pair of golden eyes that almost seem to glow, even in this light. The stark white contrasts the dark wood of the wall next to her, her black hair ornament matching the other half of her hair. Her purple dress seems out of place for the current fashion, but it’s not like I’m always the most up-to-date, anyway."

    p "Oh! Sorry, um. Is this seat taken…?"

    p "{i}She can probably tell how nervous I am… Never been good at talking to strangers, for better or worse…{/i}"

    shi "Nope, it's free."

    p "Um! Can I sit here, then?"

    shi "Hm? Oh! Yeah, that’s fine."

    p "Thanks."

    shi "Mhm."

    #chair sliding sfx or something, lower camera angle to be at level with Shiori (if i’m doing that), slightly fade up the rain effects since closer to the window
    "Without another word, she turns back to her book, pulling the oversized jacket she’s wearing together a little more. The fur collar brushes the bottom of her hair, and the purple down interior is hidden from view again."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "Catching myself staring again, I turn to look out the window, watching the rain beat against the window, the wind battering the trees lining the path outside. I lift the cup to my lips, taking a moment to enjoy my drink. And to try to ignore the somewhat awkward silence between myself and this woman next to me."

    p "{i}Nope… Still awkward…{/i}"

    shi "Hey, anyway, what did you get to drink?"

    if greentea:
        p "I just got some tea. Thought it would be nice considering outside."

        shi "Hey, is that green tea? You got my other favorite!"

        p "Really? What’s the other one, then?"

        shi "This! It’s Earl Grey."

        "The girl picks up her mug and brings it next to mine. I don’t know if she is trying to make a toast or is just showing me her tea, but her enthusiasm is kinda cute."
    
    if americano:
        p "Oh, I just went with an Americano."

        shi "Ah, I thought so with that scent."

        "The girl seems a bit hesitant afterward, as if she wants to say something but is holding back."

        shi "Uh, hey… This might be a weird request, but can I sniff your drink?"

        p "{i}Now I see why she was trying to restrain herself. Just wished she was better at it, though…{/i}"

        menu:
            "Let her do it.":
                $ sniff = True
            "Refuse.":
                $ sniff = False
        
        if sniff:
            p "Well, sure… I guess…"

            shi "Eh? Really? Wasn’t expecting that, but thanks!"

            "Popping the lid off, I bring my cup closer to her side of the counter and lift it up a bit. The girl then lowered her head close, taking a long, but gentle breath."

            #animate to soft satisfied smile Shiori
            "After a while, she moved back upright with a soft smile plastered on her face."

            p "Hey, if you don’t mind me asking, why did you ask?"

            shi "Well… I like the smell of coffee, but I just can’t drink it. So the scent’s the only way I can enjoy it."
        else:
            p "Uhhh… Do you ask everyone that?"

            shi "You're not gonna let me smell it?"

            p "Of course not! That's weird!"

            "The girl sulks and pouts, but she doesn’t say anything more about it."
    if cocoa:
        p "I got this. It’s cocoa with caramel. Not something I would drink everyday, but I think I deserve a sweet treat on a day like this."

        shi "You’re not worried about your weight?"

        p "I move around a lot so it’s fine, plus you’re one to talk with a plate full of cake."

        shi "Hey, look away! It’s an off-day, so a little cake is fine, meanie!"

        "{i}And now she’s pouting at me. I thought  that was something only anime girls do, but here we are…{/i}"
    
    p "So, uh… What’re you reading? Seems pretty good, just going off of how immersed you are."

    shi "Oh, a book. I like it, yeah!"

    p "{i}That’s not what I meant… Is.. Is she a little ditzy? Or blowing me off?{/i}"

    p "So… What book are you reading?"

    #animate to sad Shiori
    shi "Ah, it’s a story that… A friend helped with. Sorry, it’s kind of personal..."

    #would be better as a camera pan/zoom
    "I glance at the pages but only see a blank page and a page with weird scribbles on it."

    #would be better as a camera pan/zoom
    "Looking back up at her, I see her watching me, studying me."

    shi "Do… do you like books?"

    p "Huh...?"

    "I heard her but needed a moment to digest the surprise as she suddenly spoke up and a moment to think of an answer."

    menu:
        "Honestly? I love them.":
            $ booklove = True
        "They're alright.":
            $ bookneutral = True
        "Not really.":
            $ bookhate = True
    
    if booklove:
        p "Honestly? I love them. The sound and feel of the pages, the smell of the ink, the worlds and lives recorded on the page, it’s just… the best."

        #animate to show her face lighting up
        shi "ME TOO!"

        "Her voice almost gets too loud in excitement, she takes a moment to compose herself..."

        shi "I... ahem... Me too, I just love getting lost in them. It's like you jump into a whole new world, you know? All the different perspectives and everything..."

        "She keeps talking on and on for a moment, almost more to herself then you, you nod as she mumbles for a moment."
    
    if bookneutral:
        p "They’re alright. I wouldn’t say I love them, but I do read just for fun every now and then."

        #animate to show her smiling, giggle sound effect on the giggle
        shi "Really? I love them. They can take you to places you might never have even dreamed of and can teach you all kinds of things. I might be a bit biased though… *giggle*"

        p "{i}Her appreciation for books is inspiring. I need to get some reference books from the library soon, so maybe I’ll pick something up just to try reading more often.{/i}"

    if bookhate:
        p "Not really. I read them if I have to for class, but I don’t really enjoy it. I’d rather play games or watch TV."

        #animate to show a little pout
        shi "Aw… Really? They can take you to brand new places, help you relax, teach you all kinds of lessons… And they smell great! I like how they feel as I flip through them, too."

        #animate to show happy Shiori
        "She continues talking about why books are great, and why everyone should read them more, almost stuck in her own little world."

        p "{i}Her love for books is actually a little infectious. I have to get some reference books from the library tomorrow, so maybe I’ll pick something up to see how it feels to read again.{/i}"
    
    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    #fade out the heavy rain effects, fade in the lighter rain effects (still muffled because inside)
    "The two of us continue talking about books for a while, but while we’re talking, I get the sense that there’s more than just love for books behind her passion. Eventually, we reach a lull in the conversation, but it’s not uncomfortable this time. Rather, it’s a comfortable silence, accented by the tranquility of the rain lightly tapping on the glass."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "The time passes slowly, but comfortably as you almost don’t notice the storm letting up. With groups of people quickly rushing out back into town to salvage what was left of their plans, the store was nearly empty. Shiori obviously hadn’t taken notice, not much more than when you first approached. I drink the last bit of my drink and stand."

    p "Well, I should get going, too. This has been a lot more fun than just sitting on my own. I have to get some books tomorrow, so I’ll see if I find anything interesting to read for myself, too. Thanks for the recommendations!"

    "She smiles and nods, not making any kind of move to leave herself. I turn to leave."

    shi "Oh, hey! I have a question, if that’s ok?"

    p "Oh, uh, sure, what’s up?"

    shi "Any interest in being a Novelite?"

    p "Uh... what?"

    #this would be better as an animation
    "Seeing my confusion, she shakes her head, dismissing her own question."

    shi "Never mind, forget it, it’s not important right now, anyway."

    p "Right… Well, maybe I’ll see you around."

    shi "Well, sorry for the question. Anyway, have a safe trip home, and make sure not to get struck by lightning!"

    "Grabbing my umbrella on the way out, I sneak a glance at her again. The warm glow of the lights around her makes her more memorable than she already was."

    #door entry bell sfx, fade out cafe music, fade in light rain effects
    "I came in just to shelter from the storm. Now, I feel excited for some reason, but…"

    p "{i}Why am I getting the sense that, no matter what, she’s gonna be involved in my life…?{/i}"

    #fade to black here

