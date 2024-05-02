init: 
    image rainbackheavy:
        Snow("Helpers/effects/rain3.png",max_particles=5000,speed=1750,wind=0)
    
    image rainmidheavy:
        Snow("Helpers/effects/rain3.png",max_particles=2750,speed=1750,wind=0)

    image rainfront:
        Snow("Helpers/effects/rain3.png",max_particles=50,speed=800,wind=0)

label ch_13:
    scene black

    #pulse if possible

    play music "audio/4 Lovecraftian/2B/1 Normal Life L.ogg" loop fadein 1.0
    play ambient "audio/Ambient/1 Subtrack L.ogg" loop fadein 1.0
    
    "My head's pounding. I can't move or open my eyes, but I can feel it. My surroundings and everything around me. More than anything though, I just want to lie here, in the dark and silence of... wherever I am." 

    "I have no idea where I am. I don't know what my condition is. I feel like I have no sense of touch. I know I'm on something cushiony, but that's all I can tell."

    "I try to move, starting from my fingers. I can feel them slowly curl. Doing the same with my toes, I wince and slowly open my eyes."

    p_i "At least I can move something. Hurts like hell, though."

    scene bg bedroomnight with dissolve_slow
    "I look around and try not to move my head too much. Feels like there's an ice pick sticking in the back of my skull. Taking a deep breath, I groan as my neck seizes and creaks with each minute movement, the throbbing ache dulling my thoughts."

    "Taking a moment, I realize I'm actually in my apartment. Somehow."

    
    p_i "How'd I get here...?"

    "There's a clock staring at me from the corner of my room."

    p_i "I don't remember turning it toward the bed. It was turned toward my desk before… How'd that happen?"

    "The time says 3:00 AM."

    p_i "It's still really early. Explains why it's dark, I'm not usually up this early anymore."

    p_i "Why does moving just a little hurt so much, though?"

    "I open and close my hands a little but it's erratic and uneven, like my joints are old, rusty hinges. As I move a bit more, the ache starts to fade, but not completely."

    "I take a deep breath and brace myself again. Slowly and deliberately, I push myself off the mattress before turning and sitting on my bedside."

    "Panting a bit, I slowly bring my hand to massage the back of my neck. It feels hard, like it's not even flesh anymore, but I can still feel the touch of my fingers on my neck."

    "I stop and watch my hand as I clench and unclench it."

    p_i "It looks darker than I expected… Must just be because I'm not usually up this early anymore, not used to seeing what I look like when it's dark out."

    "The darkness goes away after another minute or so, so it must have been my imagination."

    "I'm still a little dazed, and there's still a bit of a dull ache throughout my body, but I feel alright enough to actually get up. My legs feel unsteady under me as I haul myself up and I balance myself against the wall." with hpunch

    p "What was in that drink Shiori gave me? And why does it feel like I haven't had anything to drink in weeks...?"

    "I wobble to the kitchen, and get myself a bottle of water from the fridge."

    "Gulping it down, it tastes amazing, and the cold water feels like a cooling balm for my throat. The fog in my head clears, and the ache disappears as soon as I swallow the water."

    show bg bedroom with dissolve_slow
    stop ambient fadeout 1.0

    p "That was… It's just water… Why was it so good?"

    "Shaking my head, I set the bottle down."

    p_i "My head doesn't hurt anymore... Maybe I was just dehydrated. Huh. Whatever."

    "I look at the counter and notice a bookmark with an eye on it. I pick it up, turning it over in my hands."

    "On the other side, I see what looks like a call number for a book, a date and time, and a couple letters…" 

    $ bookmark = show_time(1714701600)

    p_i "'FIC 65006074'? Huh. And [bookmark]? That's a really specific time... This writing feels familiar, too. Is someone telling me to find this book? But what's with the time?"

    p "'Meet me - SN'? Is that supposed to be Shiori? She's the only person I know who has a name starting with 'S'. And 'Meet me'? But why? What happened?"

    "I put the bookmark in my pocket, and get ready to leave."

    "Slipping on my shoes, I grab my umbrella, and make sure that I have my wallet, keys, and phone." 
    
    scene bg street with slideleft
    stop music fadeout 1.5
    play music "audio/3 Fantasy/3b Gatherer piano L.ogg" loop fadein 1.5

    show rainbackheavy
    show rainmidheavy
    show rainfront onlayer front
    play nature "audio/Ambient/rain4.ogg" loop fadein 1.0

    "I step outside, lock my door, and turn around. The rain seems heavier somehow. Not that it's raining more, but it feels like each drop has more weight."

    play ambient "audio/Ambient/1 Subtrack L.ogg" loop fadein 0.5 volume 0.65

    "I can feel myself being watched, but it doesn't feel like before, it feels less... creepy. Comforting almost."

    "I look around, trying to see if I can find who's watching me, and notice that there's a strange flower in the shadows at the end of the walk in front of the apartment. I rub my eyes and look again, and it's gone."

    p_i "Was that an eye watching me? Must have imagined it… That feeling is still there, but I can't see anything watching me. Weird."

    stop music fadeout 1.5
    play music "audio/4 Lovecraftian/2B/2 Getting Stalked By Hooded Figures L.ogg" loop fadein 0.5

    "I start walking to the library, but, on the way, I feel unease and comfort in equal measure." 

    show cultist at right

    "Out of the corner of my eye, I can see those yellow raincoats staring at me from some windows lurking inside some of the buildings. Outside, I can occasionally catch glances of those weird flowers again, but when I look back, they're gone again."

    p_i "Thankfully, the people in yellow coats keep away from me, so maybe this is what Shiori was talking about?"

    hide cultist

    hide rainbackheavy
    hide rainmidheavy
    hide rainfront onlayer front
    stop nature fadeout 1.0

    scene bg libraryovercast with fade

    "I finally reach the library, making sure to greet the front desk worker as I deposit my umbrella and walk by. I can't help but notice the yellow raincoat draped on the chair behind them."

    p_i "What an... interesting trend. I guess I shouldn't be too paranoid about it, even if some people wearing them are kind of weird."

    p_i "That said, I get the sense that I shouldn't ask about where these numbers lead, book-wise."

    stop music fadeout 0.5
    play music "audio/4 Lovecraftian/3B/2 Cult Lore Dump, Unveiling Mystery Track L.ogg" loop fadein 0.5

    "Pulling the bookmark out of my pocket, I make my way over to a computer and search the numbers in the library catalog."

    p_i "'The Complete Sherlock Holmes' by Arthur Conan Doyle. Hm. Guess I'll go find it."

    "It takes me about an hour or so, but I find it on a shelf near the end of an aisle."

    "I pull it down off the shelf, and am greeted with more bookmarks inside." 

    "Opening the book to each of the bookmarks, I find that the first is on a story called 'A Study in Scarlet', the second is on 'The Adventure of the Blue Carbuncle', the third is on 'The Adventure of the Beryl Coronet', the fourth is on 'The Adventure of the Speckled Band', and the last is on 'The Adventure of the Second Stain'."

    p "What the heck?"

    "Each bookmark looks like it has a number on it. The first and the second each have a '2', then the third one has a '3', the fourth has a '1', and the last has a '5'." 

    "On a whim, I open to the inside cover, and find a comment written in the same handwriting as all of the bookmarks."

    p "'Follow the years, first is last'? Huh?"

    p_i "Looks like the numbers are important, too… Hm… So, I'm supposed to 'follow the years, first is last', and these bookmarked stories are important, and those numbers have to mean something."

    p_i "So, the bookmarks for 'A Study in Scarlet' and 'The Adventure of the Blue Carbuncle' each have a '2'. The bookmark for 'The Adventure of the Beryl Coronet' has a '3'. The one for 'The Adventure of the Speckled Band' has a '1', and finally, the bookmark for 'The Adventure of the Second Stain' has a '5'."

    menu: 
        "'Adventure of the Second Study'? I guess?":
            p "'Adventure of the Second Study'? I guess?"
            $ correctstudy = True

        "The fifth study room has speckled walls, so…":
            p "The fifth study room has speckled walls, soooo... I guess the fifth one?"
            $ correctstudy = False
            $ studycheck = 5

        "The only one without a color in the name is the last one, so…":
            p "The only one without a color in the name is the last one, soooo... I think the first study room had a couple ceiling stains?"
            $ correctstudy = False
            $ studycheck = 1

    if correctstudy:
        p "I feel pretty good about that, actually. It feels more Lupin-esque than Holmes-ian, but it makes sense." 

        p "Also, I might not know her that well yet, but what a 'Shiori' way to say 'go to the second study room'."

    if studycheck == 1:
        p "I don't feel great about that, actually. I guess I'll check them in order?"

        "I walk over to the first study room, and poke my head in, and see a group of students studying inside. I look up at the ceiling and see a couple stains."

        "I smile nervously, wave, and dip my head back out of the room. I sigh, shaking my head."

        p "I can't believe I tried to get by with that kind of logic. Why would that have been the answer?" 

        p "I'll just check the next one, I suppose."

    elif studycheck == 5:
        p "I don't feel great about this, but it's the best guess I have right now. No idea what those numbers were for, though."

        "On checking the fifth study room, I see that it's dark, and nothing to indicate that it's the right or wrong room."

        p_i "Was it the wrong room after all? Guess I'll check the others, too, just to be safe."

        "I walk over to the next couple rooms, and see that they're in use, students studying in each, reminding me that there was a test pretty soon."

        p_i "Not like I have the time to deal with that right now, though, what with those weirdos showing up everywhere. It's probably nothing, but... Weird timing."

        p_i "Well, just the second and first study rooms to check now, anyway."

    "I make my way over to the second study room, and find it empty except for that weird book Shiori had with her, sitting on the center of the table, and one of those weird flowers in the corner of the room."

    "I blink, and the flower's disappeared again."

    p "I definitely need more sleep. Those can't be real, what flower has eyes?"

    "I rub my eyes vigorously and sit down at the table, facing the door. I pick up the book and look at the cover, flipping it over to glance at the back as well."

    p "What'd she say the name of this book was again? I still can't read this. But that itchy feeling is worse than it was before. Strange."

    "I set the book back down and pull out my phone to check the time."

    if correctstudy:
        p "Well, I've got a while until we're supposed to meet. Maybe I'll read some of those stories."

        "Right as I get up and leave, I turn back to look at the book."

        p_i "I... should take it with me. Just to be safe."

        "I grab the book, and then go back to where that Sherlock book was."

        show cultist with dissolve_fast

        "I look down the aisle, and see a person in a yellow jacket looking at the books. They don't seem to have noticed me yet. I quickly slide it off the shelf, and then return to the study room."

        hide cultist with dissolve_fast

        "Before I close the door all the way, I sneak a peek outside. Safe. I breathe a sigh of relief and sit back down."

        p "I didn't know that was the order those stories were written in, though. That's interesting."

        "With a small grin, I start reading each Sherlock Holmes story bookmarked."

    if studycheck == 1:
        p "Well, I have some time left. I spent a bit of time thinking about that puzzle, but at least I only needed to check one room. It's still weird to me how far apart these study rooms are from each other. It'd suck if I'd decided to start checking from the last one."

        "I tap a few buttons and begin reading one of the books I downloaded onto my phone."

        p_i "Even though it's my third time reading 'The Devil Aspect', it's still interesting. I know what'll happen, but still. There's something comforting about just enjoying the ride."

    elif studycheck == 5:
        "Thankfully, it seems like this is the right room. I just wish it hadn't taken me so long to get here."

        p_i "I only have a couple hours, so I guess I'll just read some of the fanfictions I follow. I won't get far, but some progress is better than none."

    "Just as I'm getting invested in what I'm reading, I hear a soft click. The door opens, and I look up to see a golden eye peering through the crack."

    stop music fadeout 0.5
    stop ambient fadeout 0.5
    play music "audio/4 Lovecraftian/2B/3 Study Room Conversation With Shiori L.ogg" loop fadein 0.5

    "A golden eye meets my gaze. The crack is just big enough that I see a glimpse of a familiar smile. After another moment, the door opens all the way, revealing Shiori."

    show shiori smile with dissolve_fast

    if correctstudy:
        shi "Oh, you're reading Sherlock!"

        p "Yep. I just got to 'The Adventure of the Speckled Band', and, while it's interesting enough, I still think 'A Study in Scarlet' is better."

        show shiori elated

        shi "Me too! It's easier to ship Holmes and Watson in that one! It was the first one written too, so it had to introduce the characters really well!"

        "I just nod, confirming to myself that it was Shiori that left that puzzle for me."

        p "So that {b}was{/b} what you meant by 'follow the years', good to know."

        show shiori satisfied

        shi "Yep! Hopefully it wasn't too hard!"

        p "Nah, it's fine. Easier than I expected, to be honest."

        show shiori elated

        shi "Oh, yeah? Maybe if we do this again, I'll make it harder for you!"

        p "Sure, let's see what you've got! Always kind of liked puzzles."

    else:
        shi "Glad to see you got here. Hopefully the puzzle wasn't too hard?"

        p "I uh…"

        p_i "I don't want to admit that I got it wrong..."

        show shiori sad

        shi "Ah, maybe it was? Sorry, I needed to make sure that those people in the yellow jackets wouldn't figure it out."

        p "It's ok. Just frustrated at myself not getting it more than anything else."

        show shiori smile

        shi "Well, I hope you'll be ready next time, because it'll probably be a bit harder!"

        p "Please, go easy on me."

        show shiori smug

        shi "No can do! You'll just have to be ready!"

        p " *sigh* Fine, I'll try to be."

    stop music fadeout 0.25
    play music "audio/4 Lovecraftian/3B/2 Cult Lore Dump, Unveiling Mystery Track L.ogg" loop fadein 0.5

    show shiori smile

    shi "Anyway, about those people in the yellow jackets."

    p "Yeah?"


    "Shiori tenses up for a moment before letting out a deep exhale."

    show shiori neutral

    shi "Alright, I mentioned before that those people are dangerous, right?"

    shi "Well, they seem to follow and worship this 'thing' called the 'Void Wyrm'. I still don't know much about it, but the eye on their coats? It's supposed to be that thing's eye."

    p "There's an eye on their coats? Uh huh."

    show shiori neutral

    shi "I get it, but I need you to trust me on this." 

    p "Alright, alright. I trust you."

    p_i "It has to be some joke or something. I know I thought this before, but a cult? Here? C'mon."

    shi "Anyway, it seems like they're getting ready for something big."

    p "Right."

    shi "So, we'll need to lay low until we know more. We're the only ones who can stop them right now."

    p_i "Oh. I get it. She's chuuni. At this age though? Just a number, I guess. Surprising, though. That would explain the hair and what I'm guessing are color contacts."

    p "Ok, got it. I'll go along with you on this."

    p_i "If I play along, it should be fine. Not like any of what she's talking about is real."

    show shiori smile

    shi "I'm gonna see what else I can find out, though. Try to keep a low profile and avoid the people in the yellow coats as best you can, ok?"

    p "Alright, I'll try. Not that it's a hard ask. They're uncomfortable to be around anyways."

    p "What about your book?"

    show shiori neutral

    "We both look at the book resting on the table between us."

    shi "For now, keep it with you. It's 'holding everything together' right now. It'll also keep track of some stuff, but I'm not sure how it writes itself yet."

    p "Sorry, what? It writes itself?"

    show shiori wink

    shi "Yep! No idea how, but it does!"

    show shiori smile

    p "Alright. So, how long am I holding onto this?"

    shi "At least until I can figure out more, and we can meet up again. Same time tomorrow? I should have more info then."

    p "That soon? I thought you'd need a couple days at least." 

    show shiori happy
    play sound "audio/shiogiggles/Shio giggles 5.ogg"

    shi "*giggle* Don't underestimate Archivers!"

    p "Archivers...? Okay. Here, tomorrow, same time. Got it."

    show shiori smile

    shi "Yep, see you then!"

    show shiori neutral

    shi "Oh, and don't leave right after me. Wait a bit, ok?"

    show shiori smile
    hide shiori smile with dissolve_fast

    "I nod and she turns around and opens the door slowly, looking around. She nods to herself, as if to psych herself up, and leaves, closing the door softly behind her."

    "I wait a few minutes, and then head out as well. Walking past the front desk, the worker and the rain coat are gone. "

    p_i "It's gotta be some new fashion thing. That worker seems stylish, so it'd make sense."

    show bg street with fade
    show rainbacklight
    show rainmidlight
    play nature "audio/Ambient/rain1.ogg" loop fadein 1.0

    "On my way home, I don't see a soul. Not a single yellow jacket or those flowers from earlier."

    p_i "Yeah, I figured. I just needed some more time to wake up. Was definitely just imagining things."

    hide rainbacklight
    hide rainmidlight
    stop nature fadeout 1.0

    scene bg librarynight with fade
    stop music fadeout 0.25
    play music "audio/4 Lovecraftian/3B/3 Shiori Missing Track L.ogg" loop fadein 0.5

    "I swing by the study rooms the next day, but Shiori never shows up."

    p "Maybe she just got busy? I mean, I'm still not convinced about any of this, anyway."

    p "I mean, seriously. A cult? Here? As if."

    p "I'll just come back tomorrow, I guess."

    "I leave for the day, an hour after when we were supposed to meet. Strange. On my way out, I notice that the front desk worker's missing. They're usually here. In fact, I haven't seen them miss a day of work. "

    p "Off day to study for a test, I suppose."

    scene bg bedroomnight with dissolve_slow

    "I make it back to my apartment, and, once again, I don't see a single flower or person in a yellow coat."

    "I should be relieved. I'm not seeing things anymore. But what's this sense of unease? "

    p "I'm probably just nervous about how soon that report's due. Not like I have anything bigger to worry about right now."

    "I end up coming back each day for about a week, but she never showed."

    p "The front desk worker has been missing for the same amount of time. It's midterms, though."

    "I shrug, but then shake my head."

    p "No, this feels off. Where is Shiori...?"

    p "I'm actually a bit worried, now… She seemed to be a student, so maybe I'll ask around. Someone must've seen her. There's no way anyone can miss her with the way she stands out."

    stop sound fadeout 1.0
    #stop music fadeout 1.0
    stop nature fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
