label ch_13:
    "There's a pounding in my head as I feel myself wake up. I can't bring myself to move or open my eyes, though. I just want to lie here, in the dark and silence of... wherever I am, for as long as possible." 

    "But I have no idea where I am, or really what my condition is. I feel like I can't feel anything. I know I'm on something cushiony, but that's all I can tell."

    "I try to move, starting from my fingers. I can feel them slowly curl. Doing the same with my toes, I wince and slowly open my eyes."

    p_i "At least I can move something... Hurts like hell, though."

    "I look around and try not to move my head too much, my head feels like there's an ice pick sticking in the back of my skull. Taking a deep breath, I groan as I turn my head with a stuttering movement, the ache dulling my thoughts."

    "Taking a moment, I realize I'm actually in my apartment. Somehow."

    p_i "How'd I get here...?"

    "I see the clock in the corner of what I now realize is my room, turned so I can see it."

    p_i "I don't remember turning it toward the bed. It was turned toward my desk before... How'd that happen?"

    "The time says [show_time(1714654800)]."

    p_i "It's still really early... Explains why it's dark, I'm not usually up this early anymore."

    p_i "Why does just moving a little hurt so much, though?"

    "I open and close my hands a little, again with stuttering movements, like my joints are old, rusty hinges. As I move a bit more, the ache starts to fade, but not completely."

    "I brace myself and take a deep breath again, and slowly raise myself up, turning and sitting on the side of the bed."

    "Panting a bit, I slowly bring a hand up to rub the back of my neck to try to massage it. It feels hard, like it's not even flesh anymore, but I can still feel the touch of my fingers on my neck."

    "I stop and watch my hand as I open and close it. My skin looks darker."

    p_i "It looks darker than I expected... Must just be because I'm not usually up this early anymore, not used to seeing what I look like when it's dark out."

    "The darkness goes away after another minute or so, so it must have been my imagination."

    "I'm still a little dazed, and there's still a bit of a dull ache throughout my body, but I feel alright enough to actually get up."

    "My legs feel unsteady under me as I haul myself up and I balance myself against the wall."

    p "What was in that drink Shiori gave me?"

    p_i "*sigh* My throat feels like I haven't had anything to drink in weeks... Why, though?" 

    "I make my way to the kitchen on unsteady feet, and get myself a bottle of water out of the refrigerator."

    "Gulping it down, it tastes amazing, and the cold water feels like a cooling balm for my throat. It feels like a fog clears out of my head, the ache disappearing as quickly as I swallow the water."

    p "That was... It's just water... Why was it so good?"

    "Shaking my head, I set the bottle down."

    p_i "Oh... My head doesn't hurt. Maybe I was just dehydrated. Huh. Whatever."

    "I look at the counter and notice a bookmark with an eye on it. I pick it up and turn it over in my hands."

    "On the other side, I see what looks like a call number for a book, a date and time, and a couple letters..." 

    p_i "'FIC 65006074'? Huh... And [show_time(1714701600)]? That's this evening. This writing feels familiar, too... 'SN'? Is that supposed to be Shiori? She's the only person I know who has a name starting with 'S'."

    p "Is she telling me to find this book? But what's with the time? Guess I'll find out?"

    "I put the bookmark in my pocket, and get ready to leave."

    "Slipping on my shoes, I grab my umbrella, and make sure that I have my wallet, keys, and phone. I step outside, lock my door, and turn around. The rain seems... heavier somehow. It's not like it's raining more, but it feels like each drop has more weight."

    "I can feel myself being watched, but it doesn't feel like before, it feels less... creepy. It feels almost... comforting?"

    "I look around, trying to see if I can find who's watching me, and notice that there's a strange flower in the shadows at the end of the walk in front of the apartment."

    "It has an eye that seems to be... watching me?"

    "I rub my eyes and look again, and it's gone."

    p "Must have imagined it... That feeling is still there, but I can't see anything watching me. Weird."

    "I start walking to the library, but, on the way, I feel unease and comfort in equal measure." 

    "Out of the corner of my eye, I can see the people wearing those yellow raincoats watching me. Instead of approaching me this time, they're watching from the windows of some of the buildings around me, keeping inside. Outside, I can occasionally catch glances of those weird flowers again, but when I look back, they're gone again."

    p_i "Thankfully, the people in yellow coats keep away from me, so maybe this is what Shiori was talking about?"

    "I finally reach the library, making sure to greet the front desk worker as I deposit my umbrella and walk by. I can't help but notice the yellow raincoat behind them."

    p_i "Maybe it's just a new trend? I guess I shouldn't be too paranoid about it, even if some people wearing them are kind of... weird."

    p_i "That said, I get the sense that I shouldn't ask about where these numbers lead, book-wise."

    "Pulling the bookmark out of my pocket, I make my way over to a computer and try searching the numbers in the library catalog."

    p_i "The numbers show up as the 'The Complete Sherlock Holmes' by Arthur Conan Doyle. Hm... Guess I'll go find it."

    "It takes me about an hour or so, but I do find it, on a shelf near the end of an aisle."

    "I pull it down off the shelf, and find another few bookmarks inside." 

    "Opening the book to each of the bookmarks, I find that the first is on a story called 'A Study in Scarlet', the second is on 'The Adventure of the Beryl Coronet', the third is on 'The Five Orange Pips', the fourth is on 'The Adventure of the Blue Carbuncle', and the last is on 'The Adventure of the Second Stain'."

    p "What the heck?"

    "Looking at the bookmarks, it looks like each one has a number on it. The first and the second each have a '2', then the third one has a '1', the fourth has a '3', then the last has a '5'." 

    "On a whim, I open to the inside cover, and find a comment written in the same handwriting as all of the bookmarks."

    p "'Follow the years'? Huh?"

    p_i "Looks like the numbers are important, too... Hm... So, I'm supposed to 'follow the years', and these bookmarked stories are important, and those numbers have to mean something."

    p_i "So, the bookmarks for 'A Study in Scarlet' and 'The Adventure of the Beryl Coronet' each have a '2'. The bookmark for 'The Five Orange Pips' has a '1'. The one for 'The Adventure of the Blue Carbuncle' has a '3', and finally, the bookmark for 'The Adventure of the Second Stain' has a '5'."

    menu: 
        "'Adventure of the Second Study'? I guess?":
            p "'Adventure of the Second Study'? I guess?"
            $ correctstudy = True

        "The fifth study room has orange walls, so...":
            p "The fifth study room has orange walls, so... I guess the fifth one?"
            $ correctstudy = False
            $ studycheck = 5

        "The only one without a color in the name is the last one, so...":
            p "The only one without a color in the name is the last one, so... I think the first study room had a couple ceiling stains?"
            $ correctstudy = False
            $ studycheck = 1

    if correctstudy:
        p "I feel pretty good about that, actually. It feels more Lupin-esque than Holmes-ian, but it makes sense." 

        p "Also, I might not know her that well, yet, but that feels like a very 'Shiori' way to say 'go to the second study room'."

    if studycheck == 1:
        p "I don't feel great about that, actually... I guess I'll check them in order?"

        "I walk over to the first study room, and poke my head in, and see a group of students studying inside. I look up at the ceiling and see a couple stains."

        "I smile nervously, wave, and dip my head back out of the room. I can't help but sigh at myself."

        p "I can't believe I tried to get by with that kind of logic. Why would that have been the answer?" 

        p "I'll just check the next one..."

    if studycheck == 5:
        p "I don't feel great about this, but it's the best guess I have right now. No idea what those numbers were for..."

        "On checking the fifth study room, I see that it's dark, and nothing to indicate that it's the right or wrong room."

        p_i "Was it the wrong room after all? Guess I'll check the others, too, just to be safe."

        "I walk over to the next couple rooms, and see that they're in use, students studying in each, reminding me that there was a test pretty soon."

        p_i "Not like I feel I have the time to deal with that right now, though, what with those weirdos showing up everywhere. Pretty sure it's just a new trend, but... Weird timing."

        p_i "Well, just the second and first study rooms to check now, anyway."

    "I make my way over to the second study room, and find it empty except for that weird book Shiori had with her, sitting on the center of the table, and one of those weird flowers in the corner of the room."

    "I blink, and the flower's gone again."

    p "I definitely need more sleep. Those can't be real, what flower has eyes?"

    "I rub my eyes a little roughly and sit down at the table, facing the door. I pick up the book and look at the covers, flipping it over to glance at the back as well."

    p "What'd she say the name of this book was again? I still can't read this... But that itchy feeling is worse than it was before..."

    "I set the book back down and pull out my phone to check the time."

    if correctstudy:
        p "Well, I've got a while until that time. Maybe I'll read some of those stories?"

        "I get up, and start to leave, before turning back to look at the book."

        p_i "I get the feeling I should take it with me, just to be safe..."

        "I grab the book, and then go back to where that Sherlock book was."

        "I look down the aisle, and see a person in a yellow jacket looking at the books. They don't seem to have noticed me yet."

        "I quickly grab the book, and then return to the study room."

        "Before I close the door all the way, I sneak a peek outside and let out a sigh seeing that I wasn't followed or noticed."

        "I close the door and sit back down."

        "With a small grin, I start reading the Sherlock Holmes stories that were bookmarked."

    if studycheck == 1:
        p "Well, I have some time left. I spent a bit of time thinking about that puzzle. At least I only needed to check one room... It's still weird how far apart these study rooms are from each other. It'd take a lot more time to check each one if I'd decided to start checking from the last one."

        "I start to read one of the books I downloaded onto it."

        p_i "Even though it's my third time reading 'The Devil Aspect', it's still interesting. I know what'll happen, but still. There's something comforting about just enjoying the ride."

    if studycheck == 5:
        "Thankfully, it seems like this is the right room... I just wish it hadn't taken me so long to get here."

        p_i "I only have a couple hours until that time, so I guess I'll just read some of one of the fanfictions I follow... I won't get far, but some progress is better than none."

    "I'm just getting invested in what I'm reading when I hear a soft click of the door opening, and I look up to see a golden eye peering through the crack."

    "The golden eye and I look at each other, each waiting for the other."

    "After another moment, the door opens all the way to reveal Shiori."

    if correctstudy:
        shi "Oh, you're reading Sherlock!"

        p "Yep. I just got to 'The Five Orange Pips', and, while it's interesting enough, I still think 'A Study in Scarlet' is better."

        shi "Yeah, that makes sense. It's the first one written, and it lets us see more of the characters' quirks than some of the others, where it's assumed you're already familiar with them."

        "I just nod, confirming to myself that it was Shiori that left that puzzle for me."

        p "So that was what you meant by 'follow the years', good to know."

        shi "Yep! Hopefully it wasn't too hard!"

        p "Nah, it's fine. Was a bit easier than I expected, to be honest."

        shi "Oh, yeah? Maybe if we do this again, I'll make it harder for you!"

        p "Sure, let's see what you've got! Always kind of liked puzzles."

    else:
        shi "Glad to see you got here. Hopefully the puzzle wasn't too hard?"

        p "I uh..."

        p_i "I don't want to admit that I got it wrong, but..."

        shi "Ah, maybe it was? Sorry, I needed to make sure that those people in the yellow jackets wouldn't figure it out."

        p "It's ok, I guess. More just frustrated by myself not getting it than anything else."

        shi "Well, I hope you'll be ready next time, because it'll probably be a bit harder!"

        p "Um... Please go easy on me..."

        shi "No can do! You'll just have to be ready!"

        p "Alright... I'll try."

    shi "Anyway, about those people in the yellow jackets..."

    p "Yeah?"

    "Shiori tenses up for a moment before letting out a deep exhale."

    shi "Alright, I mentioned before that those people are dangerous, and are doing dangerous things, right?"

    shi "Well, they seem to follow and worship this thing called the 'Void Wyrm'. I still don't know much about it, but the eye on their coats? It's supposed to be that thing's eye."

    p "Uh huh...."

    shi "I get it, but I need you to trust me on this." 

    p "Alright, alright, I'll trust you."

    p_i "It has to be some... some joke or something. I know I thought this before, but a cult? Here? C'mon."

    shi "Anyway, it seems like they're getting ready for something big."

    p "Right..."

    shi "So, we'll need to lay low until we know more. But we're the only ones who can stop them right now."

    p_i "Oh... I get it... Is this really chuuni? At this age? I mean... It takes all kinds, I guess. Surprising, though."

    p_i "That would explain the hair and what I'm guessing are color contacts, though."

    p "Ok, got it. I'll go along with you on this."

    p_i "If I play along, it should be fine. Not like any of what she's talking about is real."

    shi "I'm gonna see what else I can find out, though, and you lay low. Try to avoid the people in the yellow coats as best you can, ok?"

    p "Alright, I'll try. They're admittedly a bit uncomfortable to be around, anyway."

    p "What about your book?"

    "We both look at the book resting on the table between us."

    shi "For now, keep it with you, it's 'holding everything together' right now. It'll also keep track of some stuff, but I'm not sure how it writes itself yet."

    p "Sorry, what? It writes itself?"

    shi "Yep! No idea how, but it does!"

    p "Alright... So, how long am I holding onto this?"

    shi "At least until I can figure out more, and we can meet up again. Let's meet here again tomorrow, I should have more info then."

    p "That soon? I thought you'd need a couple days at least..." 

    shi "*giggle* Don't underestimate Archivers!"

    p "Archivers...? Alright, sure. Here, tomorrow, same time. Got it."

    shi "Yep, see you then!"

    shi "Oh, don't leave right after me, wait a bit, ok?"

    "I nod and she turns around and opens the door slowly, looking around. She nods to herself and leaves, closing the door softly behind her."

    "I wait a few minutes, and then leave too."

    "On my way out of the library, I don't see the front desk worker, or that yellow coat I saw on my way in."

    p_i "It's gotta be some new fashion thing. That worker does seem to be more of the fashionable type, so it'd make sense, I guess."

    "On my way home, I don't see a single person in those yellow jackets, nor do I see any of those flowers."

    p_i "Yeah, I figured. I just needed some more time to wake up. Was definitely just imagining those."

    "I show up the next day, but Shiori never shows up..."

    p "Maybe she just got busy? I mean, I'm still not convinced about all of this, anyway."

    p "I mean, seriously. A cult? Here? I can't really buy into that..."

    p "I'll just come back tomorrow, I guess?"

    "I leave for the day, an hour after when we were supposed to meet..."

    "On my way out, I notice that the front desk worker isn't here, and the yellow coat is missing too."

    p "I guess it was theirs... Must be a fashion thing, after all."

    "I make it back to my apartment, and, once again, I don't see a single flower or person in a yellow coat."

    "I feel uneasy, but I shrug it off."

    p "I'm probably just nervous about the test coming up. Not like I have anything bigger to worry about right now, after all."

    "I end up coming back each day, but she hasn't shown up even after a week..."

    p "I haven't seen that front desk worker either, wonder if they're focusing on tests, too?"

    "I shrug, but then shake my head."

    p "No, this feels weird. Where is Shiori...?"

    p "I'm actually a bit worried, now... She seemed to be a student, so maybe I'll ask around, see if anyone's seen her? She stands out after all..."
