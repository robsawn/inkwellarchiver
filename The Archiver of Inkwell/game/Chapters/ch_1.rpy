init:
    image rainbacklight:
        Snow("Helpers/effects/rain2.png",750,800,0)
    
    image rainmidlight:
        Snow("Helpers/effects/rain2.png",350,800,0)

    image rainbackheavy:
        Snow("Helpers/effects/rain3.png",3000,1500,0)
    
    image rainmidheavy:
        Snow("Helpers/effects/rain3.png",1750,1500,0)

    image rainfront:
        Snow("Helpers/effects/rain3.png",50,800,0)

label ch_1:
    scene bg bedroom with dissolve_fast
    play music "audio/From SoL route/2 Study Session L.ogg" loop fadein 0.5

    "It's finally the weekend, but I don't really get to relax this week. I have to go to the library and try to find books for that research report." 

    "I double check what books my professor recommended and make a note of them in my phone."

    "With the books noted, I leave for the library with a grimace, feeling like a couple of them might be difficult to find."
    
    stop music fadeout 0.25
    scene bg street with dissolve_fast
    play music "audio/0 Prologue/Outside Music.ogg" loop fadein 0.5 volume 0.65
    play voice "audio/Ambient/rain1.ogg" loop fadein 0.5

    "Walking down the street, I feel a calm wash over me as I listen to the soft drumming of the light rain against my umbrella."

    "A grin sneaks its way onto my face, seeing the kids in the area play in the puddles again, their laughter ringing out between the buildings."

    "I can't help but remember the woman I met in the cafe the other day. Despite the cloudy skies, she was blindingly bright."

    p_i "I should see if I can find some of those recommendations she had for me, too..."
    
    "Luckily, it doesn't take long to get to the library and I step inside right as the rain starts coming down harder."
    
    stop sound fadeout 0.25
    scene bg library with dissolve_fast
    stop music fadeout 0.25
    define librarytracks = ['audio/1 Act 1/Library.ogg','audio/From SoL route/1 Hallway + Lecture Hall L.ogg','audio/From SoL route/2 Study Session L.ogg']
    $ renpy.random.shuffle(librarytracks)
    $ renpy.music.queue(librarytracks,channel='music',loop=True,clear_queue=False,fadein=0.5,tight=True)

    "Briefly waving at the front desk worker as I step inside, I shake out my umbrella and set it in the umbrella rack by the door. I wipe my shoes and walk further in."

    "I check the note on my phone, nodding to myself; I put it back in my pocket and head toward the reference section in the back of the building."

    "As I move through the library, I appreciate the smells of the books, and the sounds of pages being turned."

    "Finally reaching the section for the references I need, I start searching for the first book on my list." 

    "I search for a while without any luck, and give up for now, moving on to the next book on my list."

    "This cycle ends up repeating for what feels like hours. But, checking my phone, I see I've only been here for about an hour and a half."

    p_i "Still... I can't believe I can't find any of these books..." 

    "I sigh to myself, look around for a table to sit down at, and see if I can find where they are on the library's website on my phone."

    "Glancing around, I finally find an empty seat. Surprisingly, the woman sitting at the table is a familiar one."

    "I take a deep breath, bracing myself a bit, and walk over."

    show shiori neutral

    p "Long time, no see, huh?"

    "I stand there a little awkwardly, just now noticing that she's focusing on the same book as she was before."

    p "Uh... Hello?"

    show shiori surprised

    shi "Hm? Oh! It's you! Hi!"

    show shiori neutral

    p "Hey, mind if I sit with you?"

    "She nods, and I let myself fall into the seat with a deep exhale. All the wandering in this part of the library has been exhausting, and the dust from the shelves makes my nose itch." 

    p_i "Seems this place isn't very popular..." 

    p_i "But wouldn't the people working here usually at least dust the shelves?"

    "I sneeze and reach into my pockets for a pack of tissues, but come up empty."

    p_i "Great, not only can I not find what I came for, but I'm gonna be sniffling..."

    "With a sigh, I see the girl, distracted from her book, glance up at me and start looking in her bag for something. After some rustling, she offers me a roll of toilet paper."

    "The sudden gesture surprises me, but feeling an incoming sneeze, I take it without too much thought."

    p "Thanks."

    show shiori happy

    shi "You're welcome, your sneezes were a little distracting, so I have no choice but to sacrifice my tissues. *giggle*"

    "As I turn away to blow my nose, she focuses back on her book again."

    "After a few minutes of checking the library catalog on my phone, I get up with a light sigh."

    p_i "Guess I'll start searching again..."

    hide shiori happy

    stop sound
    show bg libraryovercast with dissolve_slow
    play voice "audio/Ambient/rain4.ogg" loop fadein 1.0 volume 0.35

    "It seems the weather is getting worse. Outside, I can see more of the automatic lights turning on."

    "I keep searching, but I can't seem to find any of the references for my report no matter how hard I look."

    "As I wander the aisles, it dawns on me how unusually empty it is today."

    p "I guess people are staying home today."

    p "Or are doing other things."

    "I see the girl again and sigh, a little frustrated. Maybe I could ask the library workers for advice? But, other than the front desk worker, there are no signs of them anywhere."

    show shiori neutral
    
    "I sit back down, and the girl glances back up at me over the edge of her book."

    show shiori frown
    shi "Are you ok? You've been mumbling about something and walking back and forth for a while."

    p "Oh, I'm just trying to find some books for a report. But I have no idea where they are."

    if bookhate:

        show shiori smile

        shi "I see. Well, no wonder you look like a child lost in a store."

    if booklove: 

        show shiori happy

        shi "Really? And I thought someone who loves books so much would take to libraries like a fish takes to water."

    if bookneutral:

        show shiori smile

        shi "So, is this your first time here? Well, this is a pretty big library. It's easy to get turned around here."

    p "So you do remember me!"

    show shiori frown
    shi "Of course I do, it was just recently. It's not like I'm a goldfish, after all." 

    p "In that case, I should introduce myself. I'm [player_name]." 

    "She tilts her head and then closes her book after a moment."

    $ shiori_name = "Shiori"

    show shiori smile

    shi "Shiori Novella at your service. Nice to officially meet you."

    show shiori elated

    shi "*giggle* 'Officially', 'fish'."

    "She giggles to herself for a moment, before looking at you again."

    show shiori neutral

    shi "Have you asked anyone for help, since you've been looking for so long?"

    p_i "If I could find an employee, I might've asked them, or even one of my friends if they were here. But I'm not sure I've got it in me to walk up to a stranger and ask for help. Even me talking to Shiori is unusual."

    p "N-no... I couldn't find an employee, and you're the only person I know at least a little bit here right now."

    show shiori wink

    "I watch her expression go from curious to a more smug one."

    shi "Suuure... In that case, you can ask me. I'm here pretty often, so I know this place like the back of my hand." 

    show shiori neutral

    shi "But first, I need to know what books you're looking for, and what your report's on."

    "I explain my project to her, as she listens carefully and nods to herself."

    shi "I researched it for fun once. Maybe I can help!"

    hide shiori neutral with dissolve_fast

    "She leaves her book on the table and walks to a library computer to look for something."

    "While she types away, I sneak a peek at the unusual book. Just like before, it keeps drawing my attention. The black clover, purple spikes, and a large eye logo in the middle of the cover."

    "The longer I look at it, the more I feel pulled to it."

    show bg libraryovercast with flash_white
    play sound "audio/sfx/thunderstorm 1.ogg"

    p_i "What? What was that?" 

    p_i "Did the book... blink?"

    "I shake my head and rub my eyes and look at the book again." 

    p_i "Was it just my imagination?"

    p "Hey, what did you say this book was about again?" 

    show shiori frown with dissolve_fast

    shi "Just a story I love, what about it?"

    p "If you don't mind, could I take a peek? I'm curious about it."

    show shiori sad

    "Shiori turns and watches me, her gaze alternating between me and the book after a moment." 

    p_i "Maybe I shouldn't have asked..."

    show shiori frown

    shi "Yeah, you're welcome to try, but I don't think it'll be helpful for you."

    p "Why not? It looks interesting!"

    "I reach toward the book, but I hesitate for a moment."

    menu: 
        "You know what, maybe later...":
            p "You know what, maybe later..."

            show shiori neutral

            "Shiori's face relaxes, but she seems a little disappointed, too."

        "Open the book.":
            "I open the strange book. Just like before, every time I flip a page, one of the visible pages is empty and the other is covered in those strange symbols."

            p "What language is that? Latin? Sanskrit? Or something else entirely?"

            show shiori surprised

            shi "So, how is it? Can you read any of it?" 

            p "Nope, not at all. What language is that?"

            show shiori neutral

            shi "Oh... I don't know myself. That's why I've been trying to decipher it."

            "I can't help but notice the hesitation before she answers, but drop it for now."

            p_i "Didn't she say her friend helped with it, though...?"

    shi "Well, enough about the book, we can discuss my hobbies at another time. Let's go. You still don't have any of the books you're looking for."

    "With that, Shiori gets up, puts her book away, and gestures for me to follow her. I hastily get up, pushing the book out of my mind for now."

    shi "So why the interest in my book? Is it familiar to you?"

    p "Honestly, no. I've never seen anything like it, but it makes my brain feel... itchy, I guess? That's not quite it, but it feels like I should recognize it, or... Actually, you know what? Nevermind."

    show shiori frown

    shi "Really? Interesting."

    "She hums quietly, bringing a forefinger to her chin in apparent thought, before shaking her head."

    show shiori smile

    shi "Well, we can worry about that later."

    shi "Anyway, once we find those reference books for you, what kind of story do you want to read for fun?"

    "I think for a moment, remembering she'd offered me a few recommendations."

    menu:
        "I've always been interested in Lovecraft stories.":
            $ route_lc = True
        "Magic is pretty cool.":
            $ route_fantasy = True

    if route_lc:

        p "I've always been interested in Lovecraft stories." 

        show shiori surprised

        shi "Oh? Lovecraft mysteries? Well, I'm certainly a fan of those works."
        
        p "I've never read them, but I've heard how weird, creepy, and crazy they can get. I can't imagine being a character in one of those stories."
        
        show shiori frown

        shi "Being in that kind of story, huh..."

        show shiori happy

        "Her eyes gleam as a grin stretches across her face."

        shi "Who knows? It could be a bit fun."
        
        p "Y-Yeah, I guess."

        "As I look at her smile, I feel a chill run up my spine and I gulp."

        show shiori satisfied

        shi "C'mon! Don't you think it's exciting to be involved with weird cults, unknown deities, and mysteries beyond our imaginations?"
        
        "Those words sound so innocent, but something is telling me to stop this conversation from going any further."
        
        p "It just... seems scary to deal with all of that."

        show shiori neutral

        "Her smile fades, and she sighs. Then, she puts on the same soft smile from before."

        shi "When you put it that way, I guess it can be a bit much for some people who aren't ready for those kinds of stories."
        
        "She waves her hand, as if waving away an intrusive thought and shakes her head."

        shi "Anyways, enough of that. You said you needed some books, right?"
        
        p_i "I'm glad she changed the subject. She was starting to sound a bit too enthusiastic about Lovecraft. Of course, there's nothing wrong with that, but.... Her words just felt off to me." 

        p_i "It's probably nothing."
        
        p "Right! I wrote them down. Let's see..."
        
        shi "It's 'Le Morte d'Arthur', Pollard's 'Warwick the Kingmaker', and 'Historie of the Arrivall of Edward IV in England and the Finall Recouerye of His Kingdomes from Henry VI.'"
        
        p_i "She listed every book I needed... I didn't even pull my phone out yet..." 

        "Just to double check, I look through my list, and find she's named the books I noted before, and the one I'd forgotten to note."
        
        p "Yeah... how did you...?"
        
        show shiori satisfied

        shi "Oh, you know."

        shi "I just happen to have eyes everywhere."

        "I let out a small chuckle at her weird joke."
        
        p "G-Good one. You really had me going."

        show shiori neutral

        shi "Heh, I'm glad it worked then."
        
        p_i "That still doesn't explain how or why she knows what books I need though... And the more time I spend with her, the more things feel off. She's more unsettling? No, unnerving? I don't know."

        p "Well, thanks for helping me."
        
        show shiori frown

        shi "... I figured as much."
        
        "I barely caught Shiori's whisper."

        p "What do you mean?"

        show shiori neutral

        shi "Ah, don't worry about it."
        
        p "Well, considering you know what I'm looking for, would you still help me find those books?"
        
        show shiori satisfied

        shi "Hmm? What makes you think I would help you out? *giggle*"
        
        p_i "She's got a point. She has no reason to help me out when it's not her responsibility to find these books."
        
        p "Ah... sorry. You're right."

        show shiori wink

        shi "Don't be like that. I didn't say I wouldn't help you."
        
        show shiori smile

        "She turns around and leans forward slightly. Then, she squints her eyes as she grins at me a little."

        show shiori neutral

        shi "I just have to ask, if you're interested, why haven't you read any Lovecraft stories?"

        p_i "She's really fixated on that. Weird, but what's the harm in indulging her anyway? She is helping me, after all."

        p "No particular reason, I just never got around to it. Besides, don't they all have rough endings, partially because no one really has any control...?"
        
        shi "Aww, but who said all stories need a happy ending? Sometimes, things don't go as planned no matter how hard somebody tries."

        p "I do."
        
        shi "Hmm?"
        
        p "I say all stories should have a happy ending. The world's depressing enough, don't you think?"
        
        p_i "Sure, I say that, but what am I even talking about? Maybe I'm just in a mood."
        
        show shiori frown

        shi "The world, huh?"

        "Shiori reaches out and pulls a book off a shelf to her right, her hand hesitating, as if she's expecting something more."

        "She hands the book to me. It's 'Le Morte d'Arthur', but it's oddly dusty, as if it hadn't been touched in years. I look back up to see her smiling softly."

        show shiori smile

        shi "Maybe... maybe the world could use more happy endings."
        
        p "Yeah. Everyone deserves a happy ending, especially for the characters stuck in Lovecraft stories."
        
        show shiori frown

        shi "Even..."
        
        "She lowers her head as her voice trails off."

        shi "... the ones who can't escape their own fate?"
        
        stop voice
        play voice "audio/Ambient/rain4.ogg" loop volume 0.5

        "I struggle to find an answer to that as the rain fills the void of silence between us, battering against the window as we walk by."
        
        p_i "It's a really heavy question to answer, especially to someone I don't  know at all. I can't tell if she wants a serious or lighthearted answer."

        p "If that's the case, then they need someone to come along and help them out."
        
        "She stops right before turning into the next aisle of books, and just looks at me and blinks a few times."

        show shiori satisfied

        shi "*giggle* If only it was so simple..."
        
        p "Hey, you asked."

        show shiori neutral

        shi "I know, I know."
        
        p "It really can be as simple as someone just reaching a hand out sometimes."
        
        "She pauses in front of the shelf, and for a brief second her smile falters, her eyes blinking rapidly. Taking a deep breath to compose herself, she darts her hand to the left without looking and withdraws it, book in hand. I look down to see a golden cover, with the title of 'Arrival' embossed on the front."
        
        shi "Oh, you're serious?"
        
        p "Of course I'm serious. I can't imagine giving up on someone who's struggling with stuff like that."

        show shiori frown

        shi "Is that so? Good to know..."
        
        "She taps her index finger on her chin as she strides confidently down the next aisle."

        show shiori neutral
        
        shi "You know what? Maybe you're right. But it would take someone who isn't scared of all that eldritch stuff."
        
        "She stops in front of a seemingly random bookshelf and turns to look at me."
        
        shi "You still need a book, now that I think about it."
        
        "Smiling, she hops up and tries to grab a book off the top shelf, her finger pulling on the spine just enough to make the book fall toward her. Before I can think, I quickly reach up and catch the book before it drops on her."

        show shiori satisfied

        "I look down at her and am met with sheepish grin, and glance at the book to see the last title I needed."

        p "I'm guessing that didn't go the way you wanted?"

        show shiori happy
        
        shi "It's fiiiiiiiiiiiiiine."

        show shiori neutral
        
        "We walk back over to the table with the books, Shiori trailing behind me. I set them down one at a time."
        
        p "Huh?"
        
        "As I place the third book down, there's a fourth book that we didn't talk about." 

        "It's Shiori's book from earlier. Just as I reach for it, Shiori slams her hand down onto it, making me jump."

        show shiori surprised
        
        shi "Don't look!"
        
        "She slides it off the table and hides it behind her back."
        
        p "O...kay then."
        
        p_i "That was weird."

        show shiori smile

        shi "Anyways! It wasn't that hard to find your books. I think you should be fine now."
        
        p "Ah, yeah. Thanks. I guess it was a lot easier than I thought."
        
        shi "See you around then?"
        
        p "I'll be around on campus, so we'll probably run into each other at some point."
        
        hide shiori smile with dissolve_fast
        
        "She smiles and waves at me as I prepare to leave. I wave back and turn toward the exit."
        
        shi "Just be careful."
        
        "Her cheery voice fades into a more serious tone."
        
        stop voice
        play voice "audio/Ambient/rain4.ogg" loop volume 0.6

        shi "It's going to be raining for a while."
        
        p "Ah yeah. Good thing I still have my umbr—"
        
        "When I look over my shoulder, I don't see anyone."
        
        p_i "Huh? Wait. But she was just..."
        
        "I try looking around some more, even checking behind a couple of the nearby shelves to see if she's pranking me." 

        "Nobody. It's as if she simply vanished without a trace."
        
        p "What the?"
        
        "The longer I stand there, the more uneasy I feel. Shrugging, I check out the books at the front desk and grab my umbrella on the way out."

        stop music fadeout 0.5
        stop voice 
        scene bg college with slideright
        play music "audio/0 Prologue/Outside Music.ogg" loop fadein 0.25 volume 0.65
        play voice "audio/Ambient/rain1.ogg" loop fadein 0.25
        
        p_i "That was... interesting."
        
        "Before I can fully open my umbrella, a strong gust of wind knocks it out of my hand. It lands in a puddle on the sidewalk, handle down."
        
        "I sigh and step out into the pouring rain, grabbing my umbrella. Right as I bend over, I notice somebody in a yellow raincoat walking toward me in the reflection of the puddle. I quickly pick up my umbrella and turn around. Once again, there's nobody there."
        
        p_i "I guess I'm just tired. "
        
        "As I walk home, listening to the rain drumming on the umbrella, my skin crawls as I go over my conversation with Shiori in my head. As I round a corner on the final stretch before reaching home, I feel eyes boring into my back and I whip around. I stand stock still, looking around. However, the feeling is gone, and there's no one around."
        
        "I try to calm my breathing and focus on taking one step at a time away from this place."
        
        p_i "Why do I feel like I'm being watched?"

    if route_fantasy:
    
        p "I love fantasy, with magic, knights and adventures! I think it would be cool if we had spells in real life, or even dragons flying around."
        
        p "I often let my mind escape from this gray and rainy city  into the green hills of an imaginary world, full of things you would never see here."
        
        show shiori frown
        
        shi "You're quite enthusiastic about this, huh? No worries, I get it.  A lot of people love this genre. I wish I could share your enthusiasm, though."
        
        p "What's wrong? You're not a fan of fantasy? I thought you'd be interested in it too, since you're always carrying that book around with you."
        
        "Shiori shakes her head."

        show shiori satisfied
        
        shi "No no, I don't hate it. In fact, I love a lot of fantasy games."
        
        "Shiori looks at me with a conflicted face, thinking of what to say."
        
        shi "Let's just say sometimes reality isn't as good and happy as stories portray it."
        
        "With these words, she quickened her pace, leaving me to catch up with her. What an odd reaction."
        
        p "True, still I can't help but wonder how it would feel to be in the shoes of the great heroes from those books."
        
        "We continue to chat about more tropes and tales while passing through the aisles  of the library. As we approach the stairs to the second floor, she turns to me."

        show shiori neutral
        
        shi "Could you remind me what books you needed again? Otherwise, we'll be spending the rest of the day talking about unrelated topics, and your project will never get started."
        
        p_i "Ah true, almost forgot about that. But talking about anything other than studying is much more fun."
        
        "I check the note on my phone, and reading the two titles, I realize I forgot to write down the last of the three books I need."
        
        p "Let's see... There's 'Le Morte d'Arthur', Pollard's 'Warwick the Kingmaker', and uh..."
        
        p "I don't remember the last name. Uh, well, it doesn't matter. I can search for it later."
        
        shi "Oh, let me help you."
        
        show shiori satisfied
        
        "She closes  her eyes and puts her fingers to her temples, murmuring something under her breath."

        show shiori neutral
        
        "After a moment, she opens her eyes again."
        
        shi "Your third book is 'Historie of the Arrivall of Edward IV in England and the Finall Recouerye of His Kingdomes from Henry VI.'"
        
        p "Huh? You're right, but how did you know?"
        
        show shiori happy

        shi "Magic! How else?"
        
        show shiori satisfied
        play sound "audio/shiogiggles/Shio giggles 2.ogg"
        
        shi "I'm actually a fairy that can read minds and travel through dreams."

        show shiori happy
        
        "She makes a proud face and puffs out her chest as if she was bragging."
        
        p "Magic it is."
        
        "I'll humour her. She probably guessed the third book based on the previous two I mentioned. Probably..."
        
        p "In any case, yes, these three books are the ones I am looking for. The professor said we should be able to find copies of all of them in this library."

        show shiori neutral
        
        shi "Yep, I checked earlier.  I know where they are. I don't mind showing you... if you answer my questions."
        
        p_i "What is she, a sphinx or something? Well, no harm in it." 
        
        "I nod to her and she looks around cautiously as if checking for listening ears.."
        
        shi "So, if you could, would you go on an adventure like in those fantasy stories?"
        
        "She looks into my eyes with anticipation."
        
        menu:
        
            "Of course!":
        
                p "Of course! Who wouldn't want to experience a fantasy world for themselves? It's a dream come true!"

                show shiori frown
                
                shi "Oh? And so, hypothetically speaking, if some princess were to require your assistance, would you help her?"
                
                p "A damsel in distress? Classic. Sure, I'd probably try to help her if I could."
                
                "Shiori makes a light smile."

                show shiori smile
                
                shi "Well that's reassuring to hear. Good to know you are willing to help."
                
                p "That was a bit of a strange response. What do you mean?"
        
            "Probably not.":
        
                p "Hmm... Probably not. I'd love to go on adventures myself, but I wouldn't be brave enough to face any dangers out there."

                show shiori frown
                
                shi "Even if there was a princess in need of rescue?"
                
                p "A damsel in distress? I guess I could try helping, but wouldn't she have knights of her own? I wouldn't stack up to any of them."
                
                shi "Oh, I see. Well, that's a shame. Sorry in advance then."
                
                p "Sorry for what?"
        
        "But she doesn't respond, just winks as she starts up the stairs."

        show shiori neutral
        
        shi "Don't worry about it. Come on, catch up."
        
        "We stop at another shelf and she stands on her tiptoes, trying to reach a thick slate-gray book, eventually resorting to hopping up to grab at it." 
        
        "She manages to knock it down with her finger, and it tumbles off the shelf. I dart forward and catch it right before it drops onto her head. I look down at it and see that I'm holding a copy of 'Le Morte d'Arthur'." 
        
        p "Better be careful, you won't be able to read if you hit your head too often."

        show shiori happy
        
        shi "Oh I know. My knights tell me that all the time. It happens pretty often, but they always catch the books that fall on me. I guess I got too complacent."

        show shiori surprised
        
        "She seemed to realize something and clapped her hands over her mouth."
        
        p "Your knights?"
        
        shi "Friends! I meant friends, he he."
        
        "Is she into roleplaying? Maybe she's secretly an even bigger fantasy nerd than I am and just shy about it. All these questions and slip-ups. And the book that keeps coming to mind."

        show shiori neutral
        
        "You walk to another shelf where she reaches for another book from the list and gives it to you."
        
        show bg libraryovercast with flash_white
        
        "The abrupt crack of thunder almost made us jump. The weather was getting worse."
        
        p "Ugh, I hope it's not still stormy tonight. How will I fall asleep when it's so loud?"
        
        "I complained mostly to myself, but it made Shiori side-eye me."

        shi "It should get better soon. If we succeed, that is."
        
        "No telling what that meant, but she seemed to be talking to herself either way."
        
        "We reach our last stop and she drops another pair of books onto the two I already have in hand. 'Arrivall' and another I don't recognise."
        
        "It has a green cover, featuring some knights fighting a flaming monster, and was titled 'Hunter of Nightmare'. It looked like a storybook."
        
        p "What's this one? Did you just pull it out of your bag?"

        show shiori happy
        
        shi "This is one of my favorite books. Since you love fantasies so much, I decided to recommend it to you. All these boring history books about British people must wait, read it as soon as you can. It's really quite interesting."
        
        "She says it in a jokingly, but there is a slight seriousness in her tone."
        
        "I opened the book and quickly skimmed the inside front cover for context. It was a story about a fantasy world, as expected, about a group of knights and a princess who hunt for a monster in a cursed forest."
        
        p "Sure, it looks like something I would enjoy. But... how do I return it to you?"
        
        shi "My number's on the bookmark. Let me know when you finish it, or just find me here again. We'll meet again soon, so be sure to read it all." 
        
        show shiori satisfied

        shi "If you want to survive, that is."

        "She giggles, enjoying her joke."

        show shiori smile

        p "O-ok, I will, but I should start heading home. The weather is getting worse and I don't want to be stuck here for the night."
        
        shi "Ok, bye-bye then, and safe travels."

        "She waves at me as I go toward the exit."

        p_i "What a strange person. Not that I mind, though."

        "I turn around at the exit to look at her as I leave. She was reading that strange book again."
        
        hide shiori smile with dissolve_fast
        show bg libraryovercast with flash_white
        play sound "audio/sfx/thunderstorm 1.ogg"

        "Another lightning strike, much closer this time, makes me jump as a gust of wind hits the door, nearly knocking me to the ground. I look back up sheepishly, hoping that went unnoticed, only to see that Shiori was gone."

        p_i "I guess she moved deeper back into the library."

        "With that thought, I grab my umbrella and get ready to run home through the storm." 

    stop sound fadeout 1.0
    stop music fadeout 1.0
    stop voice fadeout 1.0
    scene black with Dissolve(1.0)
