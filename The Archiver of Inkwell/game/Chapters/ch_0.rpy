init:
    image rainbacklight:
        Snow("Helpers/effects/rain2.png",1500,800,0)
    
    image rainmidlight:
        Snow("Helpers/effects/rain2.png",700,800,0)

    image rainbackheavy:
        Snow("Helpers/effects/rain3.png",6000,1500,0)
    
    image rainmidheavy:
        Snow("Helpers/effects/rain3.png",3500,1500,0)

    image rainfront:
        Snow("Helpers/effects/rain3.png",50,800,0)
    
    image emberback:
        Snow("Helpers/effects/ember1.png",300,speed=-150,wind=100)
    image embermid:
        Snow("Helpers/effects/ember2.png",300,speed=-150,wind=100)
    
label ch_0:

    scene bg college with dissolve_fast
    
    show rainbacklight zorder 5
    show rainmidlight zorder 15
    show rainfront onlayer front

    play music "audio/0 Prologue/Outside Music.ogg" loop fadein 0.5 volume 0.65
    play nature "audio/Ambient/rain4.ogg" loop fadein 0.5 volume 0.65

    "As I leave my last lecture for the day, I follow the stream of other students out of the building."
    
    "The drone of chatter can be heard all around as I leave the building, but it is soon replaced by the familiar pitter-patter of rainfall."

    show bg street with dissolve_slow
    
    "As the local kids play in the puddles and adults line up to buy from the different stands, a small childish part of my brain almost wants to join in and jump in the puddles to relive my youth, those distant memories still so vivid..."

    "The walk home feels more alive hearing the laughter of the children ring out, contrasting with the scenery's muted tone. I take my time walking, drinking in the quiet atmosphere that we call home."
    
    "My walk is interrupted by several notifications buzzing in quick succession, so I pull my phone out with a sigh."

    #sound effect would be better than this
    "{i}bzzzzz. bzzzzz.{/i}"

    p "What's going on in the group chat now…?"

    "As I'm watching the texts come in, it looks like, instead of studying for midterms next week, everyone would prefer to meet up for our weekly hangout at one of the local bars."

    p "Do I want to go…? Nah. I'm already tired, I'd rather just go home and relax."

    "I reply that I'm going to pass this time, and immediately get hit with a few jokes about me 'holing up in my cave.' I chuckle to myself as I mute my phone and put it back in my pocket."
    
    "Even if they are my friends, it gets a bit exhausting being surrounded by people all day, pretty much every day, so it's nice to have some alone time."

    "As I walk down the street, it's easy to appreciate the calm feeling the rain gives me. I turn down a footpath, continuing on my way home for the evening."

    p_i "Do I want to stop in somewhere…?"

    show rainbackheavy zorder 5
    show rainmidheavy zorder 15
    stop nature fadeout 0.5
    play nature "audio/Ambient/rain4.ogg" loop fadein 0.5

    "Suddenly, the pattering on my umbrella intensifies, and the wind picks up. Hearing my umbrella strain against the building wind, I realize the weather is making the decision for me as I duck into the nearest open storefront."

    hide rainfront onlayer front
    stop nature fadeout 0.75
    stop music fadeout 0.5
    scene bg cafe with slideleft
    define cafetracks = ['audio/0 Prologue/cafe1.ogg','audio/0 Prologue/cafe2.ogg','audio/0 Prologue/cafe3.ogg']
    $ renpy.random.shuffle(cafetracks)
    $ renpy.music.queue(cafetracks,channel='music',loop=True,clear_queue=False,fadein=0.5,tight=True)

    "Opening the door, I'm warmly welcomed by the twin aromas of brewed coffee and tea, with the soft chattering of the store's guests providing a pleasant backdrop."
    
    "Inside a warm, dark wood-filled cafe, you see a couple of faces that you might recognize from school mixed in with the crowd."
    
    "All of them are soaked to various degrees; there are people alone with headphones, a couple chatting, and a group of students gathered around one of the big round tables in the center, working or playing on their phones and laptops."

    "At the counter, a barista asks for my order, and I look up at the options."

    menu:
        "I'll have green tea with added honey. Hot, please.":
            $ greentea = True
            p "I'll have green tea with added honey. Hot, please."
            "The storm is making it feel colder, so a nice, hot cup of tea seems perfect right now."
        "Hmm, one Americano, please.":
            $ americano = True
            p "Hmm, one Americano, please."
            "With it dark relatively soon, I didn't want to add too much caffeine to my system, but how can I resist a cup of coffee in a place like this?"
        "Hm… Can I get a cocoa? Large? With added caramel?":
            $ cocoa = True
            p "Hm… Can I get a cocoa? Large? With added caramel?"
            "The day has been feeling a bit long, to say the least. I deserve a little treat so let's cut loose with something sweet."
    
    "After picking up my drink from the counter, I walk deeper inside to look for a seat. I don't know if it's because of the storm or if the cafe is popular, but it seems like all of the tables have been taken already."
    
    "Finally, I spot a free chair by the windows. It's between a woman and a plant, but it's a seat."

    "Her black hair shines in the warm light, and her jacket hangs down, revealing a little of her shoulders, the fur collar splayed out on the sides, the back of it brushing her hair."

    "As I wind my way over between the tables, I notice that she's absorbed in a book. I don't really want to disturb her, but I should still be polite and ask if it's okay to sit next to her."

    play nature "audio/Ambient/rain4.ogg" loop fadein 0.5 volume 0.2

    "As I walk up, I try to get her attention."

    p "Excuse me?"

    shi "..."

    p "Um... Sorry, excuse me?"

    shi "..."

    p_i "She's really focused. Or, I'm being ignored, which seems just as likely, to be honest."

    "I brace myself, and wave my hand next to her, hoping she notices this time."

    p "Excuse me?"

    show shiori surprised with Dissolve(0.25)

    shi "Hwah?! Oh! Can I... help you?"

    show shiori neutral

    "As she turns to look at me, I notice her hair is split between a pitch black and a stark white, right down the middle."
    
    "Her hair frames a pair of golden eyes that almost seem to glow, even in this light. The stark white contrasts the dark wood of the wall next to her, her black hair ornament matching the other half of her hair."
    
    "Her grey dress seems out of place for the current fashion, but it's not like I'm always the most up-to-date, anyway."

    p "Oh! Sorry, um. Is this seat taken…?"

    p_i "She can probably tell how nervous I am. Never been good at talking to strangers, for better or worse."

    show shiori smile
    
    shi "Nope, it's free."

    show shiori neutral

    p "Um! Can I sit here, then?"

    shi "Hm? Oh! Yeah, that's fine."

    p "Thanks."

    shi "Mhm."

    show shiori neutral at right_third with MoveTransition(1.0)
    
    "Without another word, she turns back to her book, pulling her oversized jacket together a little. The fur collar brushes her hair, and the purple down interior is hidden from view again."

    hide shiori neutral with dissolve_fast
    
    "Catching myself staring again, I turn to look out the window, watching the rain beat against the glass, the wind battering the trees lining the path outside."
    
    "I lift the cup to my lips, taking a moment to enjoy my drink. And to try to ignore the somewhat awkward silence between myself and the woman next to me."

    p_i "Nope. Still awkward."

    show shiori neutral at right_third with dissolve_fast

    shi "Hey, um... What did you get to drink?"

    if greentea:
        p "I just got some tea. Thought it would be nice considering outside."

        show shiori happy

        shi "Oh, is that green tea? You got my other favorite!"

        p "Really? What's the other one, then?"

        shi "This! It's Earl Grey."
        
        show shiori smile

        "The girl picks up her mug and brings it next to mine. I don't know if she is trying to make a toast or just showing me her tea, but her enthusiasm is kinda cute."

        show shiori neutral
    
    if americano:
        p "Oh, I just went with an Americano."

        shi "Ah, I thought so with that scent."

        "The girl hesitates for a moment, as if she wants to say something but is holding back."

        shi "Uh, hey. This might be a weird request, but can I sniff your drink?"

        p_i "Now I see why she was trying to restrain herself. Just wished she was better at it, though…"

        menu:
            "Let her do it.":
                $ sniff = True
            "Refuse.":
                $ sniff = False
            
        if sniff:
            p "Well, sure. I guess?"

            show shiori happy

            shi "Eh? Really? Wasn't expecting that, but thanks!"

            "Popping the lid off, I bring my cup closer to her side of the counter and lift it up a bit. The girl lowers her head and draws a long, gentle breath."

            show shiori neutral
            show shiori satisfied with dissolve_slow

            "After a second or two, she sits back upright with a soft smile creeping across her face."

            p "Hey, if you don't mind me asking, why did you ask?"

            show shiori smile

            shi "Well, I like the smell of coffee, but I just can't drink it. So the scent's the only way I can enjoy it."

            show shiori neutral

        else:
            p "Uhhh... Do you ask everyone that?"

            show shiori frown

            shi "You're not gonna let me smell it?"

            p "Of course not! That's weird!"
            
            show shiori mad

            "The girl sulks and pouts, but doesn't say anything more about it."

    if cocoa:
        p "I got this; it's cocoa with caramel. Not something I would drink everyday, but I think I deserve a sweet treat on a day like this."

        show shiori surprised

        shi "You're not worried about your weight?"

        p "I move around a lot so it's fine, plus you're one to talk with a plate full of cake."
        
        show shiori mad

        shi "It's an off-day, so a little cake is fine, meanie!"

        p_i "And now she's pouting at me. I thought that was something only anime girls do, but here we are."
    
    show shiori neutral

    p "So what're you reading? Seems pretty good, just going off how immersed you are."

    show shiori happy
    shi "Oh, a book. I like it, yeah!"

    p_i "That's not what I meant. Is she a little ditzy? Or blowing me off?"

    p "So what book are you reading?"

    show shiori sad with dissolve_slow

    shi "Ah, it's a story that... A friend helped with. Sorry, it's kind of personal..."

    hide shiori sad with dissolve_fast

    "I glance at the book in her hands, but can only see two pages: one blank and another with strange symbols on it."

    show shiori neutral at right with dissolve_fast

    "Looking back up at her, I see her watching me, studying me."

    show shiori neutral

    shi "Do... Do you like books?"

    p "Huh?"

    "I heard her but needed a moment to get over my surprise as she suddenly spoke up, and another to think of an answer."

    menu:
        "Honestly? I love them.":
            $ booklove = True
        "They're alright.":
            $ bookneutral = True
        "Not really.":
            $ bookhate = True
    
    if booklove:
        p "Honestly? I love them. The smell of the ink and the paper, the feel of the pages in your hands, the lives and worlds they all contain... It's just the best."

        show shiori elated

        shi "ME TOO!"

        "She nearly shouts in excitement, but she takes a moment to compose herself."

        show shiori happy

        shi "I- Ahem. Me too, I just love getting lost in them. It's like you jump into a whole new world, you know? All the different perspectives and everything..."

        "You nod along as she continues to ramble for a moment, almost more to herself than to you."
    
    if bookneutral:
        p "They're alright. I wouldn't say I love them, but I do read just for fun every now and then."

        show shiori smile
        play sound "audio/shiogiggles/Shio giggles 4.ogg" 

        shi "Really? I love them."

        shi "They can take you to places you might never have even dreamed of and can teach you all kinds of things."
        
        show shiori happy
        play sound "audio/shiogiggles/Shio giggles 10.ogg"

        shi "I might be a bit biased though. *giggle*"

        p_i "Her appreciation for books is inspiring."
            
        p_i "I need to get some reference books from the library soon, so maybe I'll pick something up just to try getting back into it."

    if bookhate:
        p "Not really. I read them if I have to for class, but I don't really enjoy it. I'd rather play games or watch TV."

        show shiori frown

        shi "Aw really? They can take you to brand new places, help you relax, teach you all kinds of lessons. Oh, and they smell great!"

        show shiori neutral

        shi "I like how they feel as I flip through them, too."
        
        show shiori happy

        "She continues talking about why books are great, and why everyone should read them more."

        p_i "Her love for books is actually a little infectious..."
            
        p_i "I have to get some reference books from the library soon, so maybe I'll pick something up to see how it feels to read for fun again."

    stop nature fadeout 0.5
    play nature "audio/Ambient/rain1.ogg" loop fadein 0.5 volume 0.25

    show shiori neutral

    "The two of us continue talking about books for a while, but as we're talking, I get the sense that there's more than just love for books behind her passion."
    
    "Eventually, we reach a lull in the conversation, but it's not uncomfortable this time. Rather, it's a pleasant silence, accented by the light tapping of the rain on the window."

    "The time passes slowly but comfortably, so much so that I almost don't notice the storm letting up."
    
    "It takes me a couple minutes to notice that the store's nearly empty as well, with groups of people quickly heading back out into town to salvage what's left of their plans."
    
    "The woman obviously didn't notice, just like when I first approached. I drink the last bit of my drink and stand."

    p "Well, I should get going. This has been a lot more fun than just sitting on my own. I have to get some books soon, so I'll see if I find anything interesting to read for myself, too."
    
    p "Oh, and thanks for the recommendations!"

    show shiori smile at center with MoveTransition(0.75)

    "She smiles and nods, not making any kind of move to leave herself. Then, as I turn to leave I hear a squeak of a chair leg on the floor."

    show shiori neutral

    shi "Oh, hey! I have a question, if that's ok?"

    p "Oh, uh, sure, what's up?"

    shi "Any interest in being a Novelite?"

    p "Uh. What?"

    "Seeing my confusion, she shakes her head, dismissing her own question."

    show shiori smile

    shi "Never mind, forget it. It's not important right now."

    p "Right. Well, maybe I'll see you around."

    show shiori happy

    shi "Sorry for the weird question. Anyway, have a safe trip home, and make sure not to get struck by lightning!"

    show shiori neutral 

    "Grabbing my umbrella on the way out, I sneak a glance back at her. The sight of her reading under the warm lights makes my lips curl into a soft smile."

    hide shiori neutral with dissolve_fast
    
    stop music fadeout 0.5
    stop nature fadeout 0.5
    scene bg street with dissolve_fast
    play music "audio/0 Prologue/Outside Music.ogg" loop fadein 0.5 volume 0.65
    play nature "audio/Ambient/rain1.ogg" loop fadein 0.5

    show rainbacklight zorder 5
    show rainmidlight zorder 15
    show rainfront onlayer front

    #door entry bell sfx, fade out cafe music, fade in light rain effects

    "I came in just to shelter from the storm. Now, I feel excited for some reason, but..."

    p_i "Why am I getting the sense that, no matter what, she's gonna be involved in my life...?"

    hide rainfront onlayer front
    stop music fadeout 1.0
    stop sound fadeout 1.0
    stop nature fadeout 1.0
    scene black with Dissolve(1.0)

