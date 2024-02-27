$ renpy.include("Helpers/characters.rpy")
$ renpy.include("Helpers/trackers.rpy")
$ renpy.include("Helpers/particles.rpy")

init:
    define config.layers = ['master','transient','screens','front','overlay']

    image rainbacklight:
        Snow("Helpers/effects/snow1.png",750,800,0)
    
    image rainmidlight:
        Snow("Helpers/effects/snow1.png",350,800,0)

    image rainbackheavy:
        Snow("Helpers/effects/snow1.png",3000,1500,0)
    
    image rainmidheavy:
        Snow("Helpers/effects/snow1.png",1750,1500,0)

    image rainfront:
        Snow("Helpers/effects/snow1.png",50,800,0)

label ch_0:

    scene bg college at center with dissolve_fast
    
    show rainbacklight zorder 5
    show rainmidlight zorder 15
    show rainfront onlayer front

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "As I leave my last lecture for the day, I follow the stream of other students out of the building." 
    
    "The drone of chatter can be heard all around as I leave the building, but it is soon replaced by the familiar pitter-patter of rainfall."

    show bg street with dissolve_slow
    
    "As the local kids play in the puddles and adults line up to buy from the different stands, a small childish part of my brain almost wants to join in and jump in the puddles to relive my youth, those distant memories still so vivid..."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "The walk home feels more alive hearing the laughter of the children ring out, contrasting with the scenery’s muted tone. I take my time walking, drinking in the quiet atmosphere that we call home." 
    
    "My walk is interrupted by several notifications buzzing in quick succession, so I pull my phone out with a sigh."

    #sound effect would be better than this
    "{i}bzzzzz. bzzzzz.{/i}"

    p "What’s going on in the group chat now…?"

    #if we have time/assets, would be good to just show a phone, with scrolling texts (no detail)
    "As I’m watching the texts come in, it looks like, instead of studying for midterms next week, everyone would prefer to meet up for our weekly hangout at one of the local bars."

    p "Do I want to go…? Nah. I’m already tired, I’d rather just go home and relax."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    #tapping sounds play
    "I reply that I’m going to pass this time, and immediately get hit with a few jokes about me ‘holing up in my cave.’ I chuckle to myself as I mute my phone and put it back in my pocket." 
    
    "Even if they are my friends, it gets a bit exhausting being surrounded by people all day, pretty much every day, so it’s nice to have some alone time."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "As I walk down the street, it's easy to appreciate the calm feeling the rain gives me. I turn down a footpath, continuing on my way home for the evening."

    p "{i}Do I want to stop in somewhere…?{/i}"

    show rainbackheavy
    show rainmidheavy

    #heavier rain effects fade in, and at peak, fade lighter effects down 50% maybe?
    "Suddenly, the pattering on my umbrella intensifies, and the wind picks up. Hearing my umbrella strain against the building wind, I realize the weather is making the decision for me as I duck into the nearest open storefront."

    scene bg cafe with slideleft
    hide rainfront onlayer front

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "Opening the door, I’m warmly welcomed by the twin aromas of brewed coffee and tea, with the soft chattering of the store’s guests providing a pleasant backdrop." 
    
    "Inside a warm, dark wood-filled cafe, you see a couple of faces that you might recognize from school mixed in with the crowd." 
    
    "All of them are soaked to various degrees; there are people alone with headphones, a couple talking about the sudden storm, and a group of students congregating around a couple of the big round tables in the center, working or playing on their phones and laptops."

    "At the counter, a barista asks for my order, and I look up at the options."

    menu:
        "I’ll have green tea with added honey. Hot, please.":
            $ greentea = True
            p "I’ll have green tea with added honey. Hot, please."
            "The storm is making it feel colder, so a nice, hot cup of tea seems perfect right now."
        "Hmm, one Americano, please.":
            $ americano = True
            p  "Hmm, one Americano, please."
            "With it dark relatively soon, I didn’t want to add too much caffeine to my system, but how can I resist a cup of coffee in a place like this?"
        "Hm… Can I get a cocoa? Large? With added caramel?":
            $ cocoa = True
            p "Hm… Can I get a cocoa? Large? With added caramel?"
            "The day has been feeling a bit long, to say the least. I deserve a little treat so let’s cut loose with something sweet."
    
    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe? maybe split it into two?
    "After picking up my drink from the counter, I walk deeper inside to look for a seat. I don’t know if it’s because of the storm or if the cafe is popular, but it seems like all of the tables have been taken already." 
    
    "Finally, I spot a free chair by the windows. It’s between a woman and a plant, but it’s a seat."

    "Her black hair shines in the warm light, and her jacket hangs down, revealing a little of her shoulders, the fur collar splayed out on the sides, the back of it brushing her hair."

    "As I wind my way over between the tables, I notice that she’s absorbed in a book. I don’t really want to disturb her, but I should still be polite and ask if it’s okay to sit next to her."

    #subtly fade up rain effects to signify approaching windows
    "As I walk up, I try to get her attention."

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
    "As she turns to look at me, I notice her hair is split between a pitch black and a stark white, right down the middle."
    
    "Her hair frames a pair of golden eyes that almost seem to glow, even in this light. The stark white contrasts the dark wood of the wall next to her, her black hair ornament matching the other half of her hair." 
    
    "Her purple dress seems out of place for the current fashion, but it’s not like I’m always the most up-to-date, anyway."

    p "Oh! Sorry, um. Is this seat taken…?"

    p "{i}She can probably tell how nervous I am. Never been good at talking to strangers, for better or worse...{/i}"

    shi "Nope, it's free."

    p "Um! Can I sit here, then?"

    shi "Hm? Oh! Yeah, that’s fine."

    p "Thanks."

    shi "Mhm."

    #chair sliding sfx or something, lower camera angle to be at level with Shiori (if i’m doing that), slightly fade up the rain effects since closer to the window
    "Without another word, she turns back to her book, pulling her oversized jacket together a little. The fur collar brushes her hair, and the purple down interior is hidden from view again."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "Catching myself staring again, I turn to look out the window, watching the rain beat against the glass, the wind battering the trees lining the path outside." 
    
    "I lift the cup to my lips, taking a moment to enjoy my drink. And to try to ignore the somewhat awkward silence between myself and the woman next to me."

    p "{i}Nope… Still awkward…{/i}"

    shi "Hey, um... What did you get to drink?"

    if greentea:
        p "I just got some tea. Thought it would be nice considering outside."

        shi "Oh, is that green tea? You got my other favorite!"

        p "Really? What’s the other one, then?"

        shi "This! It’s Earl Grey."

        "The girl picks up her mug and brings it next to mine. I don’t know if she is trying to make a toast or just showing me her tea, but her enthusiasm is kinda cute."
    
    if americano:
        p "Oh, I just went with an Americano."

        shi "Ah, I thought so with that scent."

        "The girl hesitates for a moment, as if she wants to say something but is holding back."

        shi "Uh, hey... This might be a weird request, but... Can I sniff your drink?"

        p "{i}Now I see why she was trying to restrain herself. Just wished she was better at it, though…{/i}"

        menu:
            "Let her do it.":
                $ sniff = True
            "Refuse.":
                $ sniff = False
        
        if sniff:
            p "Well, sure... I guess..."

            shi "Eh? Really? Wasn’t expecting that, but thanks!"

            "Popping the lid off, I bring my cup closer to her side of the counter and lift it up a bit. The girl lowers her head and draws a long, gentle breath."

            #animate to soft satisfied smile Shiori
            "After a second or two, she sits back upright with a soft smile creeping across her face."

            p "Hey, if you don’t mind me asking, why did you ask?"

            shi "Well... I like the smell of coffee, but I just can’t drink it. So the scent’s the only way I can enjoy it."
        else:
            p "Uhhh... Do you ask everyone that?"

            shi "You're not gonna let me smell it?"

            p "Of course not! That's weird!"

            "The girl sulks and pouts, but doesn’t say anything more about it."
    if cocoa:
        p "I got this; it’s cocoa with caramel. Not something I would drink everyday, but I think I deserve a sweet treat on a day like this."

        shi "You’re not worried about your weight?"

        p "I move around a lot so it’s fine, plus you’re one to talk with a plate full of cake."

        shi "It’s an off-day, so a little cake is fine, meanie!"

        "{i}And now she’s pouting at me. I thought that was something only anime girls do, but here we are...{/i}"
    
    p "So, uh... What’re you reading? Seems pretty good, just going off how immersed you are."

    shi "Oh, a book. I like it, yeah!"

    p "{i}That’s not what I meant... Is she a little ditzy? Or blowing me off?{/i}"

    p "So... What book are you reading?"

    #animate to sad Shiori
    shi "Ah, it’s a story that… A friend helped with. Sorry, it’s kind of personal..."

    #would be better as a camera pan/zoom
    "I glance at the book in her hands, but can only see two pages: one blank and another with strange symbols on it."

    #would be better as a camera pan/zoom
    "Looking back up at her, I see her watching me, studying me."

    shi "Do... Do you like books?"

    p "Huh...?"

    "I heard her but needed a moment to get over my surprise as she suddenly spoke up, and another to think of an answer."

    menu:
        "Honestly? I love them.":
            $ booklove = True
        "They're alright.":
            $ bookneutral = True
        "Not really.":
            $ bookhate = True
    
    if booklove:
        p "Honestly? I love them. The smell of the ink and the paper, the feel of the pages in your hands, the lives and worlds they all contain... It’s just... the best."

        #animate to show her face lighting up
        shi "ME TOO!"

        "She nearly shouts in excitement, but she takes a moment to compose herself..."

        shi "I... Ahem... Me too, I just love getting lost in them. It's like you jump into a whole new world, you know? All the different perspectives and everything..."

        "You nod along as she continues to ramble for a moment, almost more to herself than to you."
    
    if bookneutral:
        p "They’re alright. I wouldn’t say I love them, but I do read just for fun every now and then."

        #animate to show her smiling, giggle sound effect on the giggle
        shi "Really? I love them." 
        
        shi "They can take you to places you might never have even dreamed of and can teach you all kinds of things." 
        
        shi "I might be a bit biased though... *giggle*"

        p "{i}Her appreciation for books is inspiring...{/i}" 
        
        p "{i}I need to get some reference books from the library soon, so maybe I’ll pick something up just to try getting back into it.{/i}"

    if bookhate:
        p "Not really. I read them if I have to for class, but I don’t really enjoy it. I’d rather play games or watch TV."

        #animate to show a little pout
        shi "Aw... Really? They can take you to brand new places, help you relax, teach you all kinds of lessons... And they smell great!" 
        
        shi "I like how they feel as I flip through them, too."

        #animate to show happy Shiori
        "She continues talking about why books are great, and why everyone should read them more."

        p "{i}Her love for books is actually a little infectious...{/i}" 
        
        p "{i}I have to get some reference books from the library soon, so maybe I’ll pick something up to see how it feels to read for fun again.{/i}"
    
    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    #fade out the heavy rain effects, fade in the lighter rain effects (still muffled because inside)
    "The two of us continue talking about books for a while, but as we’re talking, I get the sense that there’s more than just love for books behind her passion." 
    
    "Eventually, we reach a lull in the conversation, but it’s not uncomfortable this time. Rather, it’s a pleasant silence, accented by the light tapping of the rain on the window."

    #extend the textbox upward to cover more, so all of the text can be seen, centered, maybe?
    "The time passes slowly but comfortably, so much so that you almost don’t notice the storm letting up." 
    
    "It takes me a couple minutes to notice that the store's nearly empty as well, with groups of people quickly heading back out into town to salvage what's left of their plans."
    
    "The woman obviously didn’t notice, just like when I first approached. I drink the last bit of my drink and stand."

    p "Well, I should get going. This has been a lot more fun than just sitting on my own. I have to get some books soon, so I’ll see if I find anything interesting to read for myself, too." 
    
    p "Oh, and thanks for the recommendations!"

    "She smiles and nods, not making any kind of move to leave herself. Then, as I turn to leave..."

    shi "Oh, hey! I have a question, if that’s ok?"

    p "Oh, uh, sure, what’s up?"

    shi "Any interest in being a Novelite?"

    p "Uh... what?"

    #this would be better as an animation
    "Seeing my confusion, she shakes her head, dismissing her own question."

    shi "Never mind, forget it. It’s not important right now."

    p "Right... Well, maybe I’ll see you around."

    shi "Sorry for the weird question. Anyway, have a safe trip home, and make sure not to get struck by lightning!"

    "Grabbing my umbrella on the way out, I sneak a glance back at her. The sight of her reading under the warm lights makes my lips curl into a soft smile."

    show bg street with dissolve_fast

    show rainbacklight zorder 5
    show rainmidlight zorder 15
    show rainfront onlayer front

    #door entry bell sfx, fade out cafe music, fade in light rain effects
    "I came in just to shelter from the storm. Now, I feel excited for some reason, but…"

    p "{i}Why am I getting the sense that, no matter what, she’s gonna be involved in my life…?{/i}"

    #fade to black here
    hide rainfront onlayer front
    scene black with fade
    
