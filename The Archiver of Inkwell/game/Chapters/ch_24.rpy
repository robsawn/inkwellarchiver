label ch_24:
    show bg cursedforest with dissolve_fast

    "As we step inside the magic circle, it begins to glow, and the ground itself starts to break apart."

    p "Uh, Knight? What's happening?"

    k "It's normal. The circle is rigged to destroy itself after we leave so the monster can't track us back to reality."

    hide knight weapon
    scene black with flash_white
    stop music
    stop sound
    stop voice

    "As Knight finishes explaining, I suddenly feel lightheaded. I'm blinded as everything around us starts to glow with an intense white, and then..."

    "Everything goes black."

    show bg ritual with dissolve_slow
    show shiori neutral

    play music "audio/3 Fantasy/1 Relaxed Exposition Track L 2.ogg" loop fadein 1.0

    "When I come to, I find myself back in the castle. Shiori and Rook are sitting against the wall, with Rook sound asleep. Meanwhile, Knight is nowhere to be seen."

    show shiori smile

    shi "Oh hey sleepyhead, you're finally awake."

    p "Oh... hi Shiori. Good morning, I guess?"

    shi "Here, come on. Up from the floor."

    "Shiori extends a hand to me. I take it and she pulls me up from the ground."

    p "Anyways, how long have we been out for?"

    show shiori neutral

    shi "Let's see... It's been around 6 hours since you guys went into the dream, 2 hours since Knight left, and you just woke up. So that's a solid 8 hours right there."

    p_i "Wait, 8 hours?! Did I just sleep through the night?"

    "I take my phone out to look at the time. The clock shows 6:40 AM."

    p "Wow, it really is morning."

    p_i "Guess that explains why Rook is sleeping over there. Hey, wait a minute..."

    p "Shiori, why aren't you sleeping? Did you get enough rest?"

    show shiori smile

    shi "Insomnia."

    p_i "Uh huh..."

    shi "But actually though, I no longer need to sleep. Not since I got this book, anyway."

    "Shiori shows me the book that she had tucked beneath her arm. There are no words written on the cover, but it seems to be similar to the book she was reading back in the cafe."

    shi "This book allows me to stay up at full energy all the time as long as I have it with me. Can't tell you how it does that though."

    p "Well, as long as you're okay, I guess."

    p_i "She's still brimming with energy, so it should be fine. Just hope that book really is what she says it is. Don't want her to suddenly collapse out of nowhere."

    p "Also, where did Knight g-"

    "Rook yawns loudly."

    show shiori at left_third
    with MoveTransition(1.0)
    show rook weapon at right_third with dissolve_fast

    r "Hahhh, good morning gentlefolk! You sure took your sweet time, kid. How did the exploration go?"

    shi "Good morning Rook! Knight has been awake for a while now. She's recuperating in her room, and Bishop just woke up too. Since both of us are here right now, why don't you tell us what happened?"

    p "I thought Knight would have told you about it already. Didn't she wake up before me?"

    shi "Just go along with it. I need to confirm something."

    "At Shiori's request, I recount everything that happened in the Dreamscape. From landing in the dream to fighting off the monster, I lay it all out, making sure not to leave out any detail."

    if blunder:
        p "...and then the ground under the circle shattered and we returned safely... mostly."

        show shiori neutral

        shi "Well, I expected something like this might happen on your first trip. Don't dwell too much on it. We're bound to make mistakes sometimes, but try to not let it happen again, alright? Thankfully it was Knight who went in with you this time. If it was Rook, you would've been dead by now."

        #bg slowly fades to 50% saturation - no. robsawn

        p "Wha- what do you mean?"

        r "Knight's the best runner we have, kid. If it were me, you would've been gobbled up before I could have gotten back to you."

        #bg brightness drops to 75% - no. robsawn

        hide rook weapon
        hide shiori neutral

        "My blood runs cold and I shudder at the thought of how close I was to death."

        p_i "If Knight wasn't there, I would be dead. And I put her in that situation in the first place! What have I done?!"

        "Suddenly, I feel something warm on my head."

        #bg turns back to normal - no. robsawn

        show shiori smile

        shi "There there."

        "Shiori pats my head in an attempt to calm me down."

        show shiori satisfied

        shi "It's still fine. You're still alive, after all. Knight anticipated this possibility beforehand, which must be why she chose to go with you first: to protect you. She's kinder than she looks, so make sure to thank her properly later, ok?"

        "She pats my head again gently before stepping back."

        p "Thank you, Shiori."

        "Shiori gives me a soft and warm smile. Her support helps me regain the confidence to keep pushing forward."
    
    else:
        p "...and then the ground under the circle shattered and we returned safely."

        show shiori neutral

        shi "Hm... Yup, nothing wrong with that. The first entry into the dream usually leaves someone's memory of their time there scrambled, but yours seem to be completely fine. Your compatibility with the dream really is high, just like I thought!"

        show shiori satisfied at left_third

        "Shiori puffs up her chest with a satisfied, almost smug look on her face."

        shi "And you managed to fight back against the monster on your own too!"

        p_i "I guess she's proud of me."

        show rook armslaugh at right_third

        r "Aye! You did well for your first time, kid. The title of Bishop is not wasted on ya."

        hide rook armslaugh
        show shiori satisfied at center
        with MoveTransition(1.0)


    show shiori smile at left_third

    shi "Now then, stand still for me, would you? I need to run some checks on you."

    "At her request, I stand still as she starts chanting spells. Several glowing lights swirl around me from head to toe before fading away."

    show shiori surprised at left_third

    shi "Hm... Oh wow! I was half-expecting this, but you don't show any signs of Dream Fatigue at all! Guess that's high compatibility for you!"

    p "Dream Fatigue? Is that something you get normally from going in the Dreamscape?"

    shi "Yup, that's right. Everyone gets hit with it strongly the first time, and then they slowly build tolerance for it the more they go in. Even so, they still experience general fatigue, just like Knight did. That's why she left to rest in her room right after coming back."

    p_i "So that's where she went, huh? I thought she was just tired of babysitting me."

    show rook armslaugh at right_third
    r "Speaking of which, you should go rest up too, kid. Even if you're not tired, you should spend some time for yourself in the real world. We're going back in tonight after all, hahahaha!"


    "Rook lets out a hearty laugh. He seems to be eager for his turn to go in."

    show rook arms at right_third

    show shiori smile

    shi "Yeah, you should do that [player_name]. Since you can't really leave the castle right now, might as well walk around! Who knows, you might find something interesting. Also, here you go!"

    "Shiori takes out her phone and sends me a file. It is a map of the castle, with all of the important places marked down in different colors."

    p_i "Wow, this is really useful! Now I won't get lost... hey wait a minute."

    p "Shiori, how did you get my contacts?!"

    show shiori wink

    shi "Secret~ Don't worry about it, tehe~"

    "Shiori gives a sly smile as she laughs off my concern. "

    shi "Anyways, go have fun bye!"

    hide shiori wink with dissolve_fast

    "As she says this, she immediately runs off from the ritual room."

    r "Haha, never a dull day with her around. I should go and prepare for tonight, too. See you around, kid."

    "Rook walks out of the room but not before turning around to me one more time."

    r "Also kid, if you're wanting to go after her, you'll know where she is soon enough. The same for us too!"

    hide rook arms

    p_i "'I will know where she is soon enough?' What did he mean by that? Oh well..."

    "Left alone in the ritual room, I take out my phone to look at the map again. From what it tells me, most of the rooms in the castle are either empty or used as storage. There are also several places of interest here, too."

    p_i "This is pretty nice and all, but I really wanna know where the others went."

    "Suddenly, the map starts to glow, and several moving dots of different colors appear on it. One is purple, one is red, and another is black. There is also a stationary one that is orange."

    p_i "What are these things? Did Shiori add these into the map?"

    "I contemplate the curious dots as I move around. As I do, the orange dot moves as well."

    p_i "Hm, this dot just moved when I did..."

    "I try moving back and forth, and the dot matches my movement on the map."

    p_i "I knew it! These things are like GPS markers. Now if I can just figure out who's who, I can tell where they are!"

    p_i "Thinking logically, the red dot should be Knight's. Her hair is red, after all. The real question is which dot is Shiori and which is Rook?"

    p "Oh well, I'll just guess."

    p_i "So then, where should I go?"

    menu:
        "Follow the black dot":
            $ downtime = 0

        "Follow the purple dot":
            $ downtime = 1

        "Follow the red dot":
            $ downtime = 2

    if downtime == 0:
        "Looking at the map, I decided to chase after the black dot. It's moving towards the small garden at the other end of the castle, and judging by how quickly it's going, I would bet a large sum of money that this dot is Shiori."

        p_i "Well, I won't know until I go there myself."

        "I head off towards the garden. It's a bit of a walk from the ritual room, but it's not too bad. When I reach it, a lone door stands between me and the small castle garden."

        "Little did I know, this castle would break my understanding of reality yet again."

        stop music fadeout 0.5
        play music "audio/1 Act 1/Library.ogg" loop fadein 0.5 volume 0.75

        show bg garden with fade

        "Opening the door, the sight that greets me is not a small balcony of potted plants and miniature shrubbery, but a large-scale park teeming with plant life and rivers." 
        
        "The paths paved in front of me are lined with colorful flower beds, and a familiar-looking goth girl sits at the end of one of them, playfully inspecting a flower."

        show shiori happy

        shi "Oh hey, you found me!"

        p "Well, the map was really helpful, to say the least. Even though someone added a little GPS tracker to my phone without my consent."

        show shiori wink

        shi "I don't know what you're talking about~"

        "Shiori tries to play innocent by whistling, but it's not very convincing."

        p "Oh well, it wasn't a virus so it's fine. Anyway, where are we? How does something like this fit in the castle?"

        show shiori smile

        shi "What are you talking about? This place isn't in the castle. Well it isn't, technically speaking. I made it using some silly willy space-time magic, but you don't need to worry about that."

        p_i "Space-time magic?! Is that something to be used lightly?"

        show shiori neutral

        shi "I know what you're thinking. 'Oh Shiori, you shouldn't be using such a powerful and important-sounding spell on something so trivial'. Well I do what I want, and what I want is a big garden where I can take naps whenever!"

        p "Naps? Didn't you mention you don't need to sleep anymore?"

        show shiori smile
        
        shi "Yeah, as long as I have this."

        "Shiori takes out the magic book from before."

        shi "This thing helps me out a lot, but naps are still nice. I can be lazy and forget about the world for a while that way."

        "Shiori leans backwards and falls onto a flowerbed. Curiously, the flowers seem to be moving themselves up, cushioning her."

        show shiori satisfied
        
        shi "Ah~ It feels so nice to relax... Come on [player_name], lay down too! It feels great, you know?"

        "Seeing Shiori enjoying herself, I lay down to rest close to her; not touching, but close enough to not feel like strangers."

        p "Huh, it really does feel nice."

        shi "Hehe, of course it does! The flowers we're sleeping on are called pushpetals, you know? They are extremely resilient, and a bunch of them together can even hold up a car."

        show shiori elated

        "Shiori then goes on about the various species of otherworldly flowers in the area. It seems that she spent a lot of time planting them here."

        p "You really know a lot about plants, huh?"

        shi "Well, being cooped up inside the same castle really pushes you to find new hobbies. Plus, most of that knowledge came from this."

        show shiori smile

        "Shiori takes out a different book from before. It looks to be the same one she was reading back in the cafe."

        shi "Although I can't show you the contents, a lot of info on plants is stored here too. It used to be a hobby of that friend I mentioned before, and sharing her hobby somehow makes me feel at peace."

        show shiori satisfied

        "She takes a deep breath, appreciating the scent of the flowers she worked hard to cultivate. I do the same, savoring this smell that can't be found anywhere else."

        "Afterwards, we both stay silent for a long while and fully appreciate the quiet moment. After the surreal experience the past couple of days, these kinds of moments become so much more enjoyable."

        p "..."

        shi "..."

        show shiori smile

        shi "Well, should we get going? There are still things to prepare before the next expedition."

        p "Maybe we should, but before that..."

        shi "Hm? What is it?"

        menu:
            "Why do those books look so similar?":
                p "If you don't mind me asking, why are the two books so similar? I thought one of them was written with your friend, and the other popped out of nowhere."

                show shiori neutral

                shi "..."

                "Shiori remains silent for a while, clearly debating if she should say anything. But then, she breaks her silence."

                shi "...All I can ever tell you is that the author of both of them is the same person."

                show shiori sad

                shi "Please don't ask anymore about it, okay?"

                "Whatever the truth about the books is, it's clear that Shiori doesn't want to divulge anything further. As her friend and knight, it's best to respect that decision."

                p "Alright, I won't ask again. Sorry."

            "Do you think we can beat the monster?":
                p "Pretty late to ask, but do you think we can actually beat the monster with just the four of us?"

                shi "Well, of course I do. Otherwise why would I drag you into all of this?"

                show shiori smug

                shi "Oh wait, is someone feeling a bit... unmotivated?"

                p "Not unmotivated, just... unsure. Yeah I went in once already and accomplished something, but who's to say things will go smoothly next time?"

                shi "Oh come on, get over here-"

                "Suddenly, Shiori rolls over towards me and pulls on my cheeks."

                p "Ow! What was that for?!"

                show shiori smile

                shi "A little wake-up pinch for our latest recruit. Have some more faith in yourself. Things will go badly if you think they will, and things will go great if you believe hard enough."

                shi "Placebos are still a thing, y'know? Don't go ruining the mission just because you're worried we're not strong enough."

            "Can I ask about your friend?":
                p "Who was your friend, anyway? You've mentioned them a couple times already. Why are they no longer here with you?"

                show shiori sad

                shi "...She- uh..."

                "From the looks of it, Shiori is having a hard time talking about her friend. It takes a while for her to stop being silent."

                show shiori cry

                shi "She was... a great person. One of the few people I could call a true friend. It was her who wrote the story within this book with me, and she was also responsible for warning me about the Dreamscape."

                show shiori sad

                shi "It would've been great if she could see the end of her work herself..."

                "Shiori sniffles a little bit, her face full of melancholy."

                shi "I don't really want to talk about it any more, if that's ok. There are a lot of things I don't want to relive about her disappearance."

                "Shiori breathes deeply before picking herself up from the ground."

                show shiori neutral

                shi "Well, that's enough sunbathing for today. Let's head back. You still have some prep work to do, right?"

                "I stand up from the flowerbed as well."

                p "Guess so. I should prepare as much as I can."

                show shiori smile

                shi "Well then, I'll head back to the throne room. See ya!"

                hide shiori smile

    if downtime == 1:
        "From the map, the purple dot is making its way towards what looks to be the lounge."

        p_i "Seems like whoever this is, they want to 'lounge' around for a while. Ehhhhhhh?"

        p_i "Hehehe..."

        "..."

        p_i "Great, now I'm laughing at my own jokes."

        "I decide to follow the dot to the lounge. It seems to be a nice place to sit around and relax, considering it is a part of the castle, and this will also let me see who the purple dot represents: Rook or Shiori?"

        "Winding through the seemingly endless corridors of Inkwell Castle, I finally arrive at the lounge. The gaudy twin doors standing between me and the room suggests that this place is of great importance."

        p_i "Guess Shiori really values her comfort, huh?"

        "Already, I'm intrigued about what Shiori might have installed into this facility upon laying eyes on the arguably over-decorated doors."

        "As I push gently on the handles, the twin doors swing open without too much resistance. It would seem that even the entrance is made in consideration of the owner's weaker constitution."

        "I chuckle a bit, imagining Shiori with noodles for arms, and make my way into the lounge. The gaudy doors and my imagination did not disappoint me at all... Or at least, it did so in a different way." 

        show bg lounge with fade
        stop music fadeout 0.5
        play music "audio/From SoL route/1 Hallway + Lecture Hall L.ogg" loop fadein 0.5

        "The image of a cushy room frequented by nobles that I have in my head is blown away by the sight of the real lounge: an unbelievably modern room with an open layout and floor-to-ceiling windows that are welcoming in a healthy amount of sunlight." 
        
        "Square couches are arranged around the room, with several side tables accompanying them. A large television sits on one side of the room, and there seems to be a gaming console attached to it."

        p_i "Perhaps it's something Shiori brought with her?"

        "I walk towards the console to take a look. Despite all that's going on right now, I am still a gamer at heart, so I can't resist at least a peek at what's here."

        "Suddenly, a noise comes from behind me."

        show rook mug

        r "Hey there, kid, we meet again. I see you figured out the map system and followed me here."

        "Rook greets me, a cup of hot drink in hand. I was so focused on the console that I didn't even notice he was in the room."

        p "Oh! Uh- yeah, hi."

        show rook muglaugh

        r "Did I startle you, kid? Focus on your surroundings a bit more, or else the monster will catch you off guard in the dream, hahaha!"

        "Rook lets out a hearty laugh. He seems amused to see me startled."

        show rook mug

        r "Anyhow, are you gonna use that thing? If so, we could play together, have a little bonding time before the chaos tonight."

        p "Do you know how to use a gaming console, Rook? I didn't think your world had anything like it."

        r "Well, we don't, but little Queen did teach me how to play. Suggested I use it to pass the time during recovery, she did."

        p "Is that so? Wait, did she actually suggest someone from another world play video games?"

        r "That she did, kid. It has been a wondrous experience, learning all the different things this world has to offer. Like this little slate!"

        show rook phone

        "Rook pulls out a phone from inside his armor. Do not ask me where he kept it or how. I don't want to know either."

        r "What was it called again? A fane? No, a foon! Amazing, this foon is. Such wonders of technological ingenuity! Even the highest grade spells cannot compare to the sheer convenience this affords!"

        show rook phoneeyeglow

        p_i "He really seems to love his phone, huh? I guess it's pretty amazing in the eyes of someone from a fantasy world."

        p "Ahem."

        show rook arms

        r "Oh, whoops. Sorry kid, got carried away there. Anyhow, would you care for a game with this old man?"

        p "Sure, let's go."

        "I sit down on one of the nearby couches while Rook fumbles around with the console's power button. Despite the trouble, he manages to turn on the system. The words 'Ink Knight's Adventure' are displayed on-screen. It would seem someone didn't turn off the console properly."

        r "Oh, would you look at that. The little Queen didn't close her game."

        p "Was she playing during her downtime as well?"

        r "Well of course she did. She is who taught me to play, after all."

        "Rook takes some time navigating through the menu, trying to change from Shiori's save file to his own. From the looks of his finger movements, it seems that he has been playing for a while."

        r "There we go. Get ready, kid."

        "Rook walks away from the TV and hands me a controller. He then sits down on a closeby couch."

        "After getting comfortable, Rook starts the game from his latest save. The game seems to be about a knightly creature made up of ink going on a quest to save the princess. Rook is playing as the knight, while I, the second player, am controlling a sidekick."

        "The game goes smoothly, with the conversations between us being mostly Rook saying how much this game reminds him of his life and us synchronizing for combo attacks. Despite being from another world, he is surprisingly good at the game."

        "After a while, we manage to get to the final boss: a devilish witch of the ravens who kidnapped the princess out of one-sided love. We didn't manage to beat her this time, but we had a lot of fun."

        show rook armslaugh

        r "Gotta admit, kid, you really know how to play!"

        p "You too. For someone from a different world, you sure played like an expert."

        "Rook stands up from the couch to turn off the console. Afterwards, he turns to me."

        show rook arms

        r "Right, kid. Been meaning to ask, but do you have anything you want to ask me?"

        p "That came out of nowhere."

        r "We'll be venturing into the Dreamscape later, might as well get your questions out now so we can focus."

        p "Alright then..."

        menu:
            "How did you end up here?":
                p "How did you end up here, anyway?"

                r "Well kid, it isn't something I like to think about much, but I'll tell you. It started off no different than a normal day. I sought to vanquish our monstrous friend in the forest near my liege's castle, but on that day, something strange happened." 
                
                r "The monster was far stronger than anyone had reported, and it wounded me deep. I ran from the fight, valuing my guts over glory, hah! That was when I met the little Queen and Knight."

                r "I only knew later when they took me to this castle that they weren't from my world, but yours. It was quite shocking, you know, learning that there was another world alongside my own."

            "Which world is better in your opinion?":
                p "So what do you think, which world is better?"

                r "You mean between your world and mine? Well, your world is great and all with all the technology, but there is no place like home."

                r "...even if the home is me camping out inside cursed forests. Even then, home is home."

            "Do you even know how to use a gun?":
                p "I remember seeing you with a gun before. Do you know how to use that thing?"

                r "Of course! Little miss Queen taught me herself. I did some tweaks and adjustments myself as well, so I got the hang of it pretty quickly."

                p_i "Wait, Shiori knows how to use a gun? Either she's more well-versed in fighting than I imagined, or she went with something like 'so you point this over there, press the trigger, and go pew pew!' when she taught him."

                p "Well, as long as it works, I guess."

        "I'm about to ask another question, but get cut short by the growl of Rook's stomach. He laughs and grabs his mug from the table."

        show rook muglaugh

        r "Haha! Well, man cannot survive by drink alone, I suppose. I'm going to go grab a bite to eat. Have to be full of energy for later, you know. You may join me if you wish, but just be sure to take things easy today, ok kid?"

        "He pats my shoulder and sets off from the lounge on his next quest for the day, having successfully turned off the game console while completely forgetting to turn off the television."

        hide rook muglaugh

    if downtime == 2:
        "From the map, the red dot was in one of the rooms in the castle's left wing, but is moving towards the dining room now."

        p_i "That must be Knight. Let's follow that."

        if blunder:
            p_i "Because of me, she lost her weapon. Even if she doesn't want to see me, I at least want to apologize properly."

        else:
            p_i "I wanna talk to her about how long she's been here, and I really wanna ask her how she was able to be so nimble and quiet in metal armor, too. I might be able to use that."

        "I walk from the ritual room towards the dining hall, using the map as a guide. After a while, I managed to make it without getting lost."
        stop music fadeout 0.5
        play music "audio/From SoL route/2 Study Session L.ogg" loop fadein 0.75
        show bg dininghall with fade 

        "As the door creaks and swings open, the sight of a large clearing fills my vision. Long tables and chairs are aligned neatly, far more than required to seat our little quartet. Chandeliers hang silently from the ceiling, illuminating the entire room with a soft glow." 
        
        "Lining the walls at the back are multiple kegs stacked horizontally on top of each other, their contents unlisted but immediately known to all enjoyers of alcohol."

        "Speaking of which, one such enjoyer is standing right in front of a keg, pouring a healthy amount of drink into her cup."

        if blunder:
            p "Uh, h- hi..."

            k "What are you here for?"

            "Knight responds without turning around."

            p "I wanted to say I'm sorry..."

            k "Sorry? For what?"

            p "Because of my mistake, you had to cover for me and lost your sword."

            "After I mutter those words, Knight turns around to look at me. However, I didn't expect what would come next."

            show knight beer

            k "Look, Bishop."

            "Knight points to her scabbard by her waist. Instead of an empty sheathe, a blade sits soundly within it."

            k "Losing a sword is nothing much. Losing another person that could fight by our side is worse. This one isn't as strong as my old one since it still lacks Queen's enchantments, but it will do for now."

            k "I said some harsh things back there too, but it's fine, trust me."

            "Even if I can't see her face, I feel like she's smiling lightly."

            k "Although... If I had to say something, learn how to be better at being in the dream. Your power is immense, but it is easily affected by your naivety and intrusive thoughts."

            k "I reckon Rook and Queen mentioned it to you already, but you were safe only because it was me who was there. The next time you go in, it's Rook who will be joining you, and he can't save you the same way I can."

            p_i "She's right. Even Rook himself said he isn't as agile as her. Plus, I can't expect people to keep fixing my own mistakes."

            "While I stand silent, thinking about Knight's words, she looks at me, taking sips of her drink."

            k "Well, if there's something else I can tell you..."

            "Knight paces her mug down onto a nearby counter and walks up to me before placing a hand on my shoulder."

            show knight weapon

            k "Have some faith in yourself. You're not that amazing yet, but you have a lot of potential. Even after that mess-up, you're still someone Queen placed her faith in. Reflect on your weakness and make up for it."

            "After speaking, she walks towards the door, preparing to leave."

            k "Oh, right. Since you mustered up the courage to come talk to me despite your mistake, maybe I should reward it with something."

            "She turns around to look at me once again."

            k "Is there anything you want to know? If so, now is the time. I'll only let you ask one thing, though."

            menu:
                "Why are you not angry at me?":
                    p "Why are you not angry at me?"

                    k "Is that all you wanted to ask? I said so already, didn't I? Losing you would be worse than a sword. I might have been angry during the moment, but I'm more than willing to let you off the hook as long as you don't fail again."

                    k "But don't worry, if it's my fury you want, you'll get plenty of it if anything happens to Rook."

                    "Her tone makes my hair stand on end. Even if it's a joke, I can feel the intensity behind her words."

                "Enchantment? What did Shiori do?":
                    p "You said that your old sword was enchanted by Shiori? Was that how you were able to fight the monster?"

                    k "That is correct. As Queen of our order, she holds the power to bless her soldiers with divine power. The power comes in the form of an intricate enchantment, and it allows us ordinary people to harm the creature."

                    k "Well, I say 'divine power', but it's roots are from that weird book she has. I doubt that it's a spell exclusive to her, but I also doubt that anyone is crazy enough to steal it from her."

                    k "Anyway, the only problem with it is that the enchantment takes quite a while to do, way longer than a couple of days, so I'm stuck with a normal sword for now."

                "Could I really redeem myself?":
                    p "Is it even possible for me to redeem myself after the trouble I've caused?"
                            
                    k "If it isn't possible, why would Queen continue to keep you around? Even with that amazing power, she would have kicked you out if there was no hope left for you. And if she didn't, I would have."

                    k "So judging by me not taking you out the front door myself, you should know what we expect from you in the next expedition, right?"

            "Knight then turns away from me."

            k "Also, just a little suggestion for next time: don't stop for a coffee break during a fight, ok?"

        else:
            p "Hello there."

            "I walk up to where Knight is standing."

            k "Hm? Oh, it's you."

            show knight beer

            "Knight turns around to look at me before leaning against the kegs."

            p "Have you recovered enough to be drinking already?"

            k "Just enough. I take it Queen told you about Dream Fatigue, didn't she? Spare me your concern, this much isn't going to slow me down."

            "She lifts up her cup and drinks the beer, once again through her mask."

            k "Mhm, same taste as ever. Always great after every job."

            p "As ever? Knight, if you don't mind me asking, how long have you been here?"

            k "3 years. Long before any of this made it into our world. It was a chance encounter with Shiori back during a school festival. I snuck out from my class to read some novels alone, and I found her. Or rather, she found me."

            k "She was pretty easy to get along with, all things considered. A bit weird at times, but her passion for books was the real deal."

            "As Knight reminisces about her meeting with Shiori, she takes another swig of her beer."

            k "That passion was what led us to talking about 'Hunter of Nightmare' in the first place."

            "A name I recognize pops up yet again. Knight seems to be able to read the confusion on my face."

            k "I know what you're thinking, and you would be right. It's the very same story we're dealing with right now."

            p "But I thought none of this happened yet? Why would you two have been talking about it already?"

            "Knight lets out a light chuckle."

            k "It's a real, published story, dummy. Back then we were just geeking out on the same novel, but now it's turned into this. Even now I don't know how or why the story manifested itself in our world."

            p "So then why did you become Shiori's guard if there wasn't any danger yet?"

            k "Well, to be honest, I like the girl. Mysterious people are the best to hangout with, and she's at the top of the charts. There's just so much you can learn from and about her that no day is ever boring."

            p "I see... By the way, was Rook already here when you joined?"

            k "No, I was the first, actually. Rook only joined after the first time I went into the Dreamscape. Apparently, Queen knew about what was to come, so we leapt into the dream to assess the situation. That's how we all met."

            p "So that's how it all happened, huh? Wait, Shiori can go into the dream world too?"

            k "What do you mean? Of course she can. It's just a huge risk for her to be in there, that's all, since she's the only one who can open and close portals."

            "Knight takes another sip of her drink before chugging the rest down."

            k "Ah yeah! That hit the spot!"

            "After slamming her mug down on a nearby counter, Knight prepares to leave."

            show knight weapon

            k "I'll be going back to my room now, then. Feeling like sleeping a bit more. Got anything else you wanted to ask?"

            menu:
                "How are you so nimble?":
                    p "How are you so nimble? Back in the cave, you barely made any noise at all. I know your armor's designed to be light, but it's still metal. Plus, how can you run so fast in heels?"

                    k "Oh, is that all you wanted to ask?"

                    "Knight points to one of her pauldrons, and it suddenly becomes transparent."

                    k "This armor is actually just a stronger illusion magic. Whatever I create with this will work just as well as the real thing. The only downside is it only works close to me, so I just use it for armor that I don't need to repair."

                    k "As for the heels, well... that's just a skill you pick up when you do something for a long time."

                "What did you mean 'Shiori knew'?":
                    p "You said that Shiori already knew about this situation before you two met, right? How did she know, anyway?"

                    k "Honestly, I'd like to know that too. She never told me the particulars of it, but she already had that magic book with her by then. That might be why."

                    k "Then again, who knows what she does and doesn't know? I wouldn't be that surprised if she knew the meaning of life, either."

                "Any tips for the next mission?":
                    p "Since you're more experienced, got any tips for being in the Dreamscape?"

                    "Knight takes a moment to consider her answer."

                    k "To tell you the truth, any tip I can think of is obsolete in light of your power. Now that I've seen it for myself, I'm fully convinced you could get past anything as long as you're creative and brave enough."

                    k "So to sum it up, have some more confidence, I guess. The power's only as strong as the one using it, after all."

        hide knight weapon

        "After answering my question, Knight turns to leave the hall. Once again, I am met with a still silence, alone with my thoughts."

    p_i "Well, I suppose I should rest up, too. Might as well spend some time being lazy before going back for yet another exciting and not at all scary dive."

    scene black
    stop music
    stop sound
    stop voice

    "..."

    scene bg ritual with dissolve_fast

    play music "audio/3 Fantasy/1 Relaxed Exposition Track L 2.ogg" loop fadein 0.5

    "Some time has passed since the morning conversations. Now, it's time for the next expedition."

    "Once again, I find myself standing in the middle of the ritual circle. Rook stands next to me, a pillow in hand. Knight leans against one of the walls with her arms crossed, while Shiori prepares her chants."

    show rook weapon with dissolve_fast

    r "You ready, kid?"

    p "As much as I'll ever be, I guess."

    hide rook weapon with dissolve_fast
    show shiori smug at left with moveinleft
    
    shi "Well you better be! I'm just about done with the spell!"

    "The ritual circle begins to shine slightly. It is time."

    "Knowing what to do, I lay down in the center and try to fall asleep. It doesn't take long for my consciousness to drift away, and my mind becomes blank once again."

    hide shiori smug with dissolve_fast
    hide rook weapon with dissolve_fast

    show bg void with fade

    stop music fadeout 0.5
    play music "audio/3 Fantasy/3b Gatherer piano L.ogg" loop fadein 0.5

    "..."

    "Again I am falling through darkness. However this time I know nothing will happen to me and I wait until my feet hit the ground."

    "It was such an odd feeling, I fell from a high height but I felt no impact whatsoever. As if I had become a feathe-"

    "I clap my cheeks to stop the thought. If my every thought here manifests, it wouldn't be a good idea to let my mind wander to something like that."

    r  "What are you doing? Is this some kind of mental preparation from your world?"

    show rook arms

    "Rook tilts his head in confusion, watching me behave strangely."

    p "N-nothing, don't mind me. Just trying to put myself together for the mission. Speaking of which, what should we do this time?"

    r  "How responsible of you. Yes, keeping oneself centered is crucial when on a hunt. As for the mission, I will let her majesty explain things."

    shi "...He...e? Can you hear me?"

    "Shiori's voice rings in my head, as if she was talking from inside of it."

    p  "Shiori? Is that you? How are you doing this?"

    shi "Good, the connection works. How do I do this, you ask? Magic of course! I can communicate with you as long as you don't get any deeper into the Dreamscape."

    shi "But only for a short time, so I'll explain the goal here quickly."

    shi "You've already discovered weaknesses of the monster and found its lair. However there is one more thing that needs to be done."

    shi "When we corner the creature in the Dreamscape, it will try to escape into the real world, where your powers will not work and it may have an advantage over us. Unless we prepare."

    p "Really? Didn't you mention I might pull things from dream into reality?"

    shi "In theory, yes. But even if you can, we don't know how effective it will be. It is something that requires a lot of practice and time, both of which we don't have."

    shi "So we decided to search for a weapon from the real world that is stuck in the Dreamscape."

    p "...What?"

    shi "I see you are surprised. We aren't the first ones who tried to defeat the monster. There were many adventurers, knights and heroes who tried to slay it." 
    
    shi "They all failed, but many of them had magically enhanced artifacts to aid them in combat. They're still in there somewhere, and if you can find them, we can use them in the real world."

    p "How do you know that? Knight said nothing in the book worked, and there's no telling if anything else will until we actually try it, right?"

    shi "Rook told me. There's more to it than was written in the book."

    "Rook nods, agreeing with her words. It was hard to tell what was on his mind, as the helmet hid his face. Come to think of it, both Rook and Knight hide their faces."

    shi "I can't maintain the link any longer, but he should be able to fill in any gaps. Good luck out there. Rook, please make sure you both come back safe."

    r "You needn't worry. I will protect Bishop at all costs."

    "Shiori's voice trails off. The connection has been cut, and we're now left alone in the Dreamscape."

    "Now to find these artifacts to fight the monster. But what were they, and where are we supposed to look for them?"

    "I glance at Rook hoping to receive a hint."

    r "You needn't be so anxious. Just do what you did before, follow your intuition, and I'm sure it will lead us toward the objective."

    p "Oh come on, at least give me something to start with."

    show rook armslaugh

    "The helmet muffles Rook's chuckle."

    show rook arms

    r "Alright. I think the monster is unable to dispose of the weapons, so they would have been left where their wielders fell. As for the location? I can't say. You can see for yourself that we stand suspended above the infinite abyss."

    r "But because this place has no definitive form, you can shape it and make it so the items we look for are somewhere within. Oh! I know, think of a place you know well."

    r "Make it as real and solid as possible, and maybe then we will be able to find what we need. That's what my intuition tells me."

    hide rook arms

    "This wasn't very reassuring, but there weren't many alternatives, so I might as well try."

    p_i " A place that I know well? Hmm... Maybe my old high school?"

    scene black with fade

    "I try to imagine the huge building where I spent several years of my life. I have closed my eyes to help myself picture it, when I hear Rook's voice."

    r "Oh? What manner of fortress is this?"

    show bg hallway with fade

    "I open my eyes to see what he's talking about. The landscape had completely changed. Instead of on a path snaking through the void, we stood in the entry of my old school. It seemed more solid and less hazy than the forest had been."

    p "This is my old school."

    show rook arms

    r "A school? So you are nobility then, or perhaps the child of a wealthy merchant?"

    p "No, it's just a normal school. Pretty much everyone in our world attends one."

    r "Astounding, it is truly a different world. Let us proceed then."

    hide rook arms

    "Together, we walked down the main hallway. It was eerily silent, with the only sound heard being the muted echoes of our footsteps."

    "The hallways feel narrower than they used to, and some that I look down on either side had a distinctly organic undulation to them that made my skin crawl. For all I tried, I wasn't able to replicate things perfectly, and the Dreamscape seemed happy to fill in any gaps in my memory."

    "It is dark. I look up and the lights are clearly on, a few even flickered a bit, but they are putting out very little light. I can't help but wonder if this is some subconscious memory worming its way in, or if I had just never thought about the lights being what actually illuminated the whole building."

    r "This is no good, I can hardly see five paces in front of me."

    "I close my eyes again. Maybe I can fix that. I focus on the ceiling and force the hall lights to brighten even more."

    #school hallway, 130% brightness - no. robsawn

    r "Much better."

    "We then proceed to reach the main hall, from here we could access any part of the school."

    show rook arms

    r "So, do you have any ideas where to look?"

    p_i "I honestly have no idea, if only there was something that showed us the way. In games there are always map markers telling you where to go, or at least a compass showing the general direction." 

    stop music fadeout 0.5
    play music "audio/3 Fantasy/3 Gatherer L.ogg" loop fadein 0.5

    "I feel a weight in my hand. It was so unexpected I almost dropped it by reflex. I look down to see a compass set in a heavy bronze box. It doesn't have anything to mark the cardinal directions, but it does have three arrows slightly offset from one another."

    p_i "How convenient. Everything seems possible in dreams."

    r "What is this? A compass?"

    p "You don't have those in your world?"

    r "We do, they just look different. This one seems more complex than ours. Hmm, do you think it will lead us to the weapons?"

    p "I just wanted something to guide us. So I would guess it shows where the artifacts are? But that's just a theory."

    "Rook pats me on the shoulder and gives a thumb up."

    r "Good job kid, now let's follow where it's showing."

    p "I hope it will help us. What do we do if the monster shows up? Do we run or keep looking?"

    show rook weapon

    r "Don't worry, if it attacks, I will distract it long enough for you to find the weapons. With this thing that Queen gifted me, I feel as if I could take on three such creatures at once!"

    "Rook lovingly pats the gun. Seriously, where did Shiori even get something like that?"

    "I sigh. It would take too much time to explain what death flags are and why no one should boast how strong they are during the 'slay the monster' quest..."

    p "Ok then, let's keep moving."

    "We walk in the approximate direction the arrows are pointing. As we come to the major crossroads of the halls, the three arrows drift to point in three different directions." 

    r "Oh! It stopped. Do you know where it leads?"

    hide rook weapon

    "I choose one of the arrows. If I remember correctly, in this direction, we had..."

    menu:
        "Left arrow - Homeroom":
            $ wep_3 = 0

        "Middle arrow - Pool":
            $ wep_3 = 1

        "Right arrow - Lab":
            $ wep_3 = 2

    if wep_3 == 0:
        "My old homeroom. The left arrow leads us that way."

        "We turn to the left. The further we go, the more solid the building becomes, the haze retreating with each step. This place is much more accurate, probably because I remember it the best."

        "We reach the door to the classroom and slowly open it."

        show bg classroom with fade

        "The room is almost the same as I remember. Multiple tables sitting in line. A big green board. The teacher's table near the window. It almost feels nostalgic, but one small difference bothers me."

        "It is full of skeletons."

        "They are lying all over the room, wearing armor and robes of different colors."

        "In the middle of the homeroom, a golden sword sticks out of the central table. One of the skeletons sits beside it"

        p "What the..."

        show rook arms

        r "All who tried to defeat the creature. The Lord of Nightmares has terrorized people for many years."

        "Rook kneels to give final honors to the fallen warriors."

        hide rook arms

        "I don't want to interrupt him, so I step gingerly across the bodies up to the sword."

        "The silvery-white blade glows with a pale, warm light and radiates a calming aura. It's stuck deep into the table, but from the part that is visible, I can distinguish script running down the center of the blade."

        p_i "I have no idea what this says. This must be the language from the fantasy world."

        "I grab the handle with both of my hands and try to pull it out."

        "It doesn't flinch."

        "I try again, applying more strength, but no matter how hard I try, it might as well be stuck in stone."

        "Maybe I can try to make the table disappear? Or break it?"

        "I imagine it disappearing or melting away."

        "Nothing happens. My powers do not affect the sword or the table. Pulling it out seems like the only option."

        "Rook finishes paying his respects and joins me."

        show rook arms

        r "Having trouble? No wonder, that sword is stuck deep in there."

        p "Is this some kind of special sword? It looks like it to me. I hope we don't need a chosen one to pull it out."

        r "A chosen one? No, it is a magic sword for sure, but anyone can pull it out given enough skill or strength."

        "Rook approaches it, puts one hand on the haft, another on the crossguard, a foot against the table, and strains against it. I can hear him grunting in exertion. It's clear he's using all his strength."

        "Then, the sword dislodges slightly."

        "Little by little it pulls free, and the glow becomes brighter until Rook finally draws it from the table, filling the room with a warm radiance."

        r "Here kid, you take it."

        p "Me? I don't even know how to use it."

        r "Hit the monster with the sharp side. I have my own weapon already and I am content with it."

        "I take the weapon from his hands. It's heavy, but not as much as I expected."

        r "Let's go, I want to see more of this school."

        "We both head out to the exit, but before we leave I turn to have a last look at the room."

        "And the skeletons are gone."

        "I blink in surprise and run after Rook. Better leave this place as fast as possible."

    elif wep_3 == 1:
        "The pool, yes. The middle arrow shows the way to the school's natatorium. I look over to see Rook inspecting a sign that has just grown from the wall." 

        show rook arms

        r "Natatorium? What is this?"

        p  "It's a big room with an indoor pool where students can learn how to swim or compete against one another in races."

        r "So everyone can swim here? In my world, most folk try to avoid setting foot in anything deeper than a small pond or stream. Even then it's usually to bathe, only the innocent or the bold go swimming for recreation."

        p "You don't have lakes and oceans?"

        r "We do. But they're infested with monsters like merrows and sea serpents and the like. Even traveling by ship is risky and done mostly close to shore."

        hide rook arms

        "As we walk through the corridors, Rook tells me more about the fantasy world he came from. I'm thankful for the distraction."

        "Although it isn't completely dark anymore, there are still pockets of dark shadows. I couldn't shake the feeling that something was about to pounce on me from one of them."

        "Finally, we reach the big double door that leads to the natatorium. Rook slowly opens it, looking inside to be sure it is safe and enters, giving me a signal."

        show bg pool with fade

        "The pool is full of water, and the floor around it is slippery and wet. I look around for any sign of some kind of fantastical object."

        "But other than the water, it was an empty natatorium."

        show rook arms

        r "So this is the place you learn how to swim. Too bad we don't have the time for me to try it out."

        "I look closer at the compass, which is pointing directly at the pool."

        p_i "Oh please don't tell me this thing is at the bottom of the pool..."

        "I peer over the edge into the water. Yes, I see something glowing with a deep blue light at the bottom of the deep end."

        p "Guess there's no other choice. Time to go for a swim."

        r "I will stand guard up here. If you stay under for too long though, I will jump in after you."

        hide rook arms

        "I nod. I take off my shoes and outer layer of clothing and, after some hesitation, I jump into the water. It was cold."

        play sound "audio/sfx/water splash.ogg"

        p_i "Is it really a dream? This feels way too real to me." 

        "Taking a breath, I dive."

        show bg underwater with slideup

        "I swim toward the light, deeper and deeper down. The pool is deeper than it looked from above, but I think I'll manage."

        "Then I feel something, or someone, touch my leg. I yelp in surprise, losing most of my air. I look up with worry. I had swum down fairly deep already and I don't know if I have enough to make it back to the surface."

        "To my surprise, nothing happens. My lungs don't burn for air and I have no issues remaining underwater."

        p_i  "I can't forget, I don't need to worry about things like this as long as I keep my head. Still, what touched me? It couldn't have been like a fish or seaweed."

        "That was a mistake. As soon as the thought passed through my mind, the bottom of the pool cracked open and a forest of kelp grew up around me, obscuring the light I was swimming after. A glittering school of fish takes me by surprise as they swim in front of me."

        "I wave them away and make my way to the bottom, pulling away the kelp that has wrapped around the light. The brilliant cyan glow blinds me for a second, and I see the artifact I'm looking for."

        "It is a truly beautiful weapon. A barbed trident made of a blue-green sea glass that lay at the bottom of the pool."

        "I grab it and swim upwards. It takes me way less time to get back to the surface."

        play sound "audio/sfx/water splash.ogg"

        show bg pool with slidedown

        show rook weapon

        r "There you are kid, I saw some movement in the water. You had me worried."

        p "It was just some fish, no big monsters to worry about."

        "I set the trident up on the side and try to climb out, but something wraps around my waist and drags me away."

        "Rook tries to catch me, but the floor and my arm are both too wet. He can't keep his balance and I slip from his grasp as an enormous tentacle hoists me into the air above the pool."

        "Rook grabs his weapon and whips around, slicing into the tentacle with the axe bolted to the barrel of the gun. His swing nearly severs it in two, and the tentacle drops me back into the water before sliding back into the depths."

        play sound "audio/sfx/water splash.ogg"

        show rook arms

        "Rook heaves me out of the water and sets me beside the pool. He retrieves a towel hanging nearby and hands it to me along with my clothes. He picks the trident up from the ground and waits as I dry myself off."

        show rook armslaugh

        r "Well now, that was exciting. Maybe your pools do have monsters then, eh?"

        show rook arms

        "He chuckles, and I can't tell if he's being genuine or if this is sarcasm. He hands the trident back to me after I redress, and we quickly exit the natatorium before the tentacle decides to come back."

    else:
        "A lab for the science classes."

        "We turn to the right and smell a strange acrid scent coming from the end of the hall."

        show rook arms

        r "This smell reminds me of magic workshops where alchemists combine different ingredients."

        p "It's coming from the lab room.That's probably why."

        r "Lab? What is that?"

        p "It's a place where students do experiments in chemistry and physics. Does that help?"

        r "So this is also an academy of sorcery. Well, considering you studied here I am not surprised."  

        hide rook arms

        "While I was trying to explain that it was not a magic school, we hear a popping sound from the lab, and a strong wind blows the doors open before we can even reach it."

        p "What is going on in there?"

        show bg lab with fade

        "I look inside to a scene out of a fantasy movie."

        "The lab is bigger than I remember it, much bigger. Desks, chairs, beakers, flasks, and a bunch of other lab equipment float around the room. And in the middle of it, a levitating staff glows with a purple light."

        show rook weapon

        r "Good find. Unfortunately, it appears to be in defensive mode. Reaching it will not be easy." 
        
        p "Whoa, a real magic staff, I want it."

        "I step into the room and start to figure out how to get to it. The staff's glow intensifies and it creates several fireballs that orbit around it."

        r "Careful!"

        play sound "audio/sfx/Fireball 2.ogg"

        "Rook yanks me back out of the room and around the corner. I barely clear the doorway before the wall shakes from the three explosive impacts."

        "Peeking back inside, the wall isn't cracked or even scorched despite the force and heat of the blast."

        p "This is a problem, how do we get to something that's so high off the ground and shoots spells at us?"

        p "Can you shoot it down?"

        r "I won't risk damaging it. Better try something else."

        "Staying out of the doorway, I analyze the room for clues."

        "Conveniently, some of the floating desks and chairs line up with the staff, so I may be able to jump across them."

        p_i "Maybe one of us can distract the staff while the other runs for it."

        "I step into the room again. The staff glows and creates fireballs."

        r "Wait Bishop, no. What are you doing?"

        "A few tables drift together in front of me to shield me from the flames. Just as before, the fireballs explode violently, but the tables remain unscathed."

        play sound "audio/sfx/Fireball 2.ogg"

        p  "Just as I thought, if I focus on moving something in the Dreamscape, it actually moves a bit to follow that. Do you think it would work with the staff?"

        "I try to imagine the staff falling, but it doesn't happen. As if in chastisement, it shoots another salvo of fireballs at me."

        play sound "audio/sfx/Fireball 2.ogg" 

        r "That's a good idea, but don't bother to affect it with your powers."

        r "Shield me with furniture and I will run to it. You shouldn't risk approaching it. Unlike any old object from the Dreamscape, this can and will hurt you."

        hide rook weapon

        "I watch as Rook jumps from table to chair to table, all the while trying my best to intercept the fire from the staff."

        play sound "audio/sfx/Fireball 2.ogg"

        "This is nerve wracking. Exposing myself is one thing, but now Rook's life depends on me. I take a deep breath and refocus."

        "Rook braces himself and I try to push the desk beneath him for a bit of a boost as he makes a last leap towards the staff."

        "The instant his finger touches the staff, the glow vanishes, and everything in the room, including Rook, falls."

        "I try to throw the furniture away from Rook as he tucks into a roll to land. It hits the ground with a loud crash, echoing down the halls."

        show rook arms

        "Rook stands up from the debris and brushes some shattered glass off his armor. He waves with the staff and gives me a thumbs up."

        r "Way to go, kid."

        "We have what we came for. It's time to leave."

    show bg hallway with fade

    "Now that we have one weapon, we could leave now or try to go get another."

    "As we walk back through the halls, Rook looks around at the flyers and photos on the walls."

    r "Oh, what is this? What about that?"

    "He asks me questions every time he sees something new."

    "He finds every little detail of our world fascinating. I find it amusing, considering I am just as interested in his."

    p "Hey Rook, given the chance, would you return to your world?"

    "He stops, surprised by this question. After a bit of reflection, he nods."

    r "I would certainly like to, your world is like a faerie tale to me. Everything is so different."

    r "But still, I would like to go back to my world. Being a guest is good, but being at home is better."

    "But can he go back? I don't voice this concern. He's probably asked himself the same question."

    "The lights in the hall suddenly turned off, plunging us into darkness."

    #hallway background to 20% brightness - no. robsawn

    p "Uh, w- what was that?"

    show rook weapon at left_third

    r "It seems it's finally caught up to us. We need to leave. Follow me, I remember the path back."

    "Rook holds his gun up against his shoulder, ready to shoot. I clutch the new artifact, and we slowly and deliberately move toward the exit."

    play sound "audio/sfx/monster steppies.ogg"

    "Somewhere in the building we hear heavy steps echo throughout the halls. It is after us, inside the school."

    "We're almost at the exit, we just need to pass the last hallway. I turn around and freeze."

    #bg up to 40% brightness - no. robsawn

    show emberback zorder 5
    show embermid zorder 15

    show monster calm at right_third

    "The monster is standing in the middle of the hall. It is also bigger this time. Did it grow, or did the hallway shrink?"

    "I couldn't tell. The only thing clear to me now is that it's going to be nearly impossible to pass it by."

    "The monster lumbers towards us, its flickering fiery mane casting erratic shadows across the walls and floor."

    p_i "We need to do something."

    r "Listen here, kid. I'll act as a distraction and lure it away from you. You take that weapon and run for it."

    p "What about you? I am not leaving you here!"

    r "Don't worry, I'll be right behind you. Just take care of your new weapon."

    "As much as I hate the thought, he has more experience in this kind of situation, and I can't come up with a better option."

    "I nod, agreeing with his plan, and duck into a corner where the shadows are even deeper."

    "Rook then stands to his full height, aims at the monster, and fires his weapon."

    play sound "audio/sfx/Rook_s gunshot.ogg"

    r "Hey, ugly! Want to have a rematch? I'm right here!"

    "His shot clips the monster's chest, but that just seems to enrage it."

    show monster angry at right_third

    play sound "audio/sfx/monster lunge.ogg"

    "The monster's head erupts in flame and it rushes him with a roar that makes my blood run cold."

    "The monster passes me in a fury, and I watch as Rook engages it in melee."

    "Now was the time. If I was going to run, this would be my only chance."

    p_i "But should I?"

    menu:
        "Escape":
            $ rook_inj = True
        "Help Rook":
            $ rook_inj = False

    if rook_inj:
        p_i "I need to leave, now! Rook is baiting the monster away, right now is the only chance I'll ever get to run. Even if the worst happens, as long as I can get out of this place, his sacrifice will not be in vain!"

        if blunder:
            p_i "I'm sorry, Knight, but I need to make it back safe with the weapon! If you lash out at me later, so be it!"

        "I look around the corridor for a way forward, the one that would be the shortest and safest. I manage to spot a path unblocked by the two combatants, and I scurry towards it as quickly and quietly as possible."

        p_i "Come on, don't notice me now!"

        hide rook arms
        hide monster angry

        "The monster is completely preoccupied with Rook behind me. All I can hear are gunshots and the sounds of a struggle. I can only hope Rook comes out on top."

        "I don't look back. I can't afford to, not when the exit's right there. With a final sprint for the doors, I make it out of the school, leaving Rook behind."

        hide emberback
        hide embermid
        scene bg cursedforest with dissolve_fast

        "I run through the courtyard as fast as I can, and hide behind the trees outside, waiting for the fighting to stop. With the indistinct sounds as my only guide, I don't know how long it's going to last. But then..."

        show rook injuredblood

        r "Ugh... Got me pretty good, didn't you?"

        "Rook staggers out of the corridor, using his gun to brace himself like a cane."

        r "Oi, kid! It's safe now!"

        "Rook shouts into the air, correctly assuming I am still in the area."

        p "Rook! You beat it- wait, those wounds!"

        "Rook, battered and bleeding, has wounds across his entire body, with a large gash in his chest covered by old bandages."

        r "It's fine, kid. What doesn't kill you makes you- UGH!"

        "Rook groans in pain. He needs medical treatment as soon as possible."

        p "Just hold on, Rook, I'll fix it!"

        p_i "Come on mud-for-brains, there must be something you can do! Think! Bandages, plasters, potions, something!"

        "I try to think of something, anything that could help Rook as blood slowly seeps from his armor. Then, a small vial containing a mysterious red liquid appears in my hand, alongside a roll of bandages."

        p_i "Could this be a healing potion?"

        "I quickly hand the vial to Rook. He seems to recognize it as a potion and drinks it down without a word. The bleeding slows and comes to a stop, but the wound is still there."

        p "Did it work?"

        r "A bit, it must have been a low potion."

        p_i "A low?! Why did my power only create such a weak potion?!"

        r "Oi, kid!"

        "I turn towards Rook, who seems to be reading my face."

        r "I don't know what you're thinking, but that potion still helped. Significantly. Don't let it get you down now, we're still not out of the woods yet. I'll be fine."

        r "Now, let's get that weapon out of here!"

        show rook injured

        "Spurred on by Rook, I start leading the way back towards the exit portal. Along the way, Rook stumbles as he walks, but manages to stay on his feet. Partway there we stop so I can assist in changing his bandages in hopes that it would help."

    else:
        p_i "No. I can't leave him behind! If Rook falls here, the monster will chase after me anyway. Standing our ground is the only option!"

        if blunder:
            p_i "I won't run now, not when I have to make up for before. I'm not running from my past mistakes, and I refuse to make more!"

        else:
            p_i "I fought this thing before when I was with Knight, I can do it again!"

        "Throwing caution to the wind, I grab my weapon tightly and run into the fray."

        if wep_3 == 0:
            p "Brace yourself!"

            "Even though the sword felt heavy just minutes ago, I am able to lift it easily into a stance. I run towards the monster's legs and swing my sword into it."

            "The blade easily slashes into the beast's joint, causing a gout of flames to burst from the wound. I leap back to avoid the blast, and the monster whirls on me."

            p "Come and get me!"

            "The monster swings out with a claws hand to try to take off my head. Instead of dodging this one, I brace my blade and parry its hand away."

            p "Rook, hit it!"

            r "Got it, kid!"

        elif wep_3 == 1:
            p "Rook!"

            "I call out to Rook, who is blocking lashes of the monster's tail with his weapon."

            p "Push it towards me!"

            r "Kid!"

            "Rook knocks the tail aside again, drops a shoulder down, and bullrushes the monster. As it stumbles backward, I brace my trident and harpoon one of its knees to cripple it."

            p "Say goodbye to your kneecaps! Rook, now!"

            r "Aye! You got it, kid!"

        else:
            p "Let's see you dodge this!"

            "I aim my staff as if it were a rifle, and flames climb up its length before forming arrows of gleaming light at the end."

            p "Rook, jump back!"

            "Hearing my shout, Rook leaps backwards. The monster brings both claws down into the space he had occupied a moment before, and it begins to turn toward the sound of my voice. The spell flies from my staff towards the monster, peppering it with bolts of light."

            "The monster tries to shield itself with its arms and tail, but leaves itself wide open in doing so."

            p "Rook, now!"

            r "Got it, kid!"

        show rook weaponeyeglow at left_third

        "While the monster is fixated on me, Rook leaps into the air and swings his axe into the beast. The blade carves deep into its shoulder and embeds itself with the barrel of the gun pointing at the monster's face." 
        
        "Then Rook, holding onto his weapon, uses it to swing up onto the monster's body, where he grabs the trigger and shoots the monster in the head point-blank."

        play sound "audio/sfx/Rook_s gunshot.ogg"

        hide monster angry
        show rook weaponeyeglow at center
        with MoveTransition(1.0)

        hide emberback
        hide embermid

        "The monster falls to the floor, its flames petering out. The fight is over."

        p "Is it down?"

        show rook weapon

        r "Looks like it, kid. For now, at least."

        show rook armslaugh

        r "That was a nice fight. But tell me, kid, why did you run back? I told you to run away, didn't I? Or is this old man too unreliable for you?"

        p "No, Rook, you're one of Shiori's guards. There's no way you're unreliable. It's just, when I was gonna run away, I hesitated. I didn't want to run from the monster. I wanted to run from my cowardice."

        p "The monster will come for us even if we run. I'm done being prey."

        if blunder:
            p "Plus..."

            p_i "Plus, I can't let Knight down a second time."

            r "Hm? What was that, kid?"

            p "Nothing."

        show rook arms

        r "Well then, I suppose we should get going."

        p "Right. Shiori and Knight might worry if we take any longer."

        show bg cursedforest with dissolve_fast

        "We walk out of the school's main entrance, leaving the incapacitated monster behind as we head back to our exit portal."

    "After some time, we manage to make it back to where we entered. Both of us step onto the spell circle, with me holding on tight to my newfound weapon."

    "Once more, the circle shines blindingly bright, and the scenery goes black."

    if rook_inj:
        hide rook injured
    else:
        hide rook arms

    show black with fade
    stop music

    "Again, it takes a while for us to come back to reality. Like waking up from a dream, I'm inclined to lie still for just a bit more..."

    scene bg ritual with flash_white
    show shiori neutral

    play music "audio/3 Fantasy/1 Relaxed Exposition Track L 2.ogg" loop fadein 0.5

    shi "... Hey, are you awake?"

    "Shiori pokes my face with her finger, trying to wake me up."

    show shiori neutral at left_third
    with MoveTransition(1.0)
    show knight weapon at right_third

    k "Oi, how long are you gonna sleep, Bishop! Rook's already up!"

    "Knight takes a more forceful approach to get me up by kicking me in the ribs."

    p "Ow ow ow, okay I get it! I'm up!"

    "I get up from the ritual circle and walk towards Shiori. Rook is already sitting in a chair against the wall, leaning on the table next to him."

    show shiori neutral at center
    with moveinleft
    show rook arms at left_third
    with moveinleft

    r "Oh, that was exhausting. At least these old bones can still keep up with the young'uns."

    k "What happened in there, Rook?"

    if not rook_inj:
        show rook armslaugh

        r "Well, outside of the monster coming to us to get beaten up, it was quite peaceful. Hahaha!"

        r "And the kid showed great promise as well! Even helped me take down the thing!"

        if blunder:
            k "Heh, see, Bishop? You really can do it if you just try. Good job. Anyways, what did you guys find?"

        else:
            k "I see you enjoyed yourself, you old knight. So, what did you guys find?"


    if rook_inj:
        r "Well, the monster ambushed us when we were about to leave, so I had to fight it off while I had Bishop take the weapon away. It might have been after the weapon, after all. Having the kid run away with it was safest for the mission."

        k "So you got hurt? How bad's the phantom pain this time around?"

        show rook injuredeyeglownoblood

        r "Gash down my side, but that's about it. It hurts when I move, but at least the wound's not there now. Don't worry much, this old man's still tough!"

        show rook injured

        k "Well, at least you can still move around. Since it's your decision, I suppose I won't fault Bishop for it. Anyways, what did you find?"

    if wep_3 == 0:
        p "We found this glowing sword stabbed into a desk. From what Rook said, it was once used by a fallen knight."

        r "Aye. One of the lost souls who fought against the blasted beast. The sword is ours now, and we have inherited its will to fight. It's our duty to finish the job."

        hide knight weapon
        hide rook injured

    if wep_3 == 1:
        p "We took this trident from the bottom of a pool. It stabs good, and that's about it."

        hide knight weapon
        hide rook injured
        show shiori surprised

        shi "Hey, give me that! Lemme take a look."

        "Shiori takes the trident from my hands."

        show shiori neutral

        shi "Huh, are you sure you didn't steal this from somewhere? Because this looks similar to the trident someone I know owns. It's blue, it's sharp, and it's kinda stinky."

        p "... Shiori, the point of your mission was to steal something from the dream."

        show shiori wink

        shi "... Oh yeah, I forgot about that. Teehee~"

    if wep_3 == 2:
        p "We got this staff that can shoot fireballs or anything that's close enough."

        k "Well would you look at that, we finally have a mage."

        hide rook injured
        show shiori mad at left_third
        with move

        shi "Hey! I cast spells too, y'know?"

        k "Queen, you know that's not how I meant it..."

        hide knight weapon

    show shiori satisfied

    shi "Well, since we got a new weapon in the end, I'd call this mission a success! Yay!"

    "We all give a loud celebratory cheer."

    show shiori smile

    shi "Alright then, everyone, we've prepared as much as we can. Today's the fourth day of the assault, which means that the night of reckoning will soon be upon us."

    shi "Rest up as much as you can. Steel your nerves, grab your weapons tight and your fears even tighter. Everything will be decided tonight."

    show knight weapon at right_third

    k "Soon, huh? Good!"

    show rook armseyeglow at left_third

    r "Yes, soon… At long last!"

    "Knight and Rook both express anticipation of the grand finale. Then, Shiori turns towards me."

    show shiori neutral

    shi "How about you, [player_name]? How are you feeling?"

    p "I'd be lying if I said I'm not scared, but we've come this far already. I can't give up now!"

    show shiori satisfied

    shi "Nice answer. Well then, let us prepare for the night. I'll see you guys here again at the same time this evening."

    hide shiori neutral with dissolve_fast
    hide rook armseyeglow with dissolve_fast
    hide knight weapon with dissolve_fast

    "After saying that, Shiori dismisses us to finish our preparations. Rook, Knight, and Shiori all set out in different directions, leaving me alone in the ritual chamber. An opening of the map tells me that they've retreated to the same places as last time."

    "Perhaps they want to take a long break. Perhaps they want some time alone. Perhaps they are trying to come to terms that tonight may be the last time we see each other alive. I cannot say what they are thinking, but the same kind of thoughts are running through my head."

    "Either us or the monster, one of us will die under the light of their last moon."

    "With that revelation ringing deep in my thoughts, I head towards my room to prepare for the final fight."

    "There's no turning back now."
