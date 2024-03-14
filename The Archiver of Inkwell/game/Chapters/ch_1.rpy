$ renpy.include("Helpers/characters.rpy")
$ renpy.include("Helpers/trackers.rpy")
$ renpy.include("Helpers/particles.rpy")

label ch_1:
    #fade in from black
    "It's finally the weekend, but I don't really get to relax this week. I have to go to the library and try to find the books for that research report."

    "I double check what books my professor recommended and make a note of them in my phone."

    "With the books noted, I leave for the library with a grimace, feeling like a couple of them might be difficult to find."

    #light rain sfx
    "Walking down the street, I feel a calm wash over me as I listen to the soft drumming of the light rain against my umbrella."

    "A grin sneaks its way onto my face, seeing the kids in the area play in the puddles again, their laughter ringing out between the buildings."

    "I can't help but remember the woman I met in the cafe the other day. Despite the cloudy skies, she was as blindingly bright as the sun."

    p "{i}I should see if I can find some of those recommendations she had for me, too...{/i}"

    "Luckily, it doesn't take long to get to the library and I step inside right as the rain starts coming down harder."

    "Briefly waving at the front desk worker as I step inside, I  shake out my umbrella and set it in the umbrella rack by the door. I wipe my shoes and walk further in."

    "I check the note on my phone, nodding to myself; I put it back in my pocket and head toward the reference section in the back of the building."

    "As I move through the library, I appreciate the smells of the books, and the sounds of pages being turned."

    "Finally reaching the section for the references I need, i start searching for the first book on my list."

    "I search for a while without any luck, and give up for now, moving on to the next book on my list."

    "This cycle ends up repeating for what feels like hours. But, checking my phone, I see I've only been here for about an hour and a half."

    "{i}Still... I can't believe I can't find any of these books...{/i}"

    "I sigh to myself, look around for a table to sit down at, and see if I can find where they are on the library's website on my phone."

    "Glancing around, I finally find an empty seat. Surprisingly, the woman sitting at the table is a familar one."

    "I take a deep breath, bracing myself a bit, and walk over."

    p "Long time, no see, huh?"

    "I stand there a little awkwardly, just now noticing that she's focusing on the same book as she was before."

    p "Uh... Hello?"

    shi "Hm? Oh! It's you! Hi!"

    p "Hey, mind if I set with you?"

    "She nods, and I let myself fall into the seat with a deep exhale. All the wandering in this part of the library has been exhausting, and the dust from the shelves makes my nose itch."

    p "{i}Seems this place isn't very popular...{/i}"

    p "{i} But wouldn't the people working here usually at least dust t he shelves?{/i}"

    "I sneeze and reach into my pockets for a pack of tissues, but come up empty."

    p "{i}Great, not only can I not find what I came for, but I'm gonna be sniffling...{/i}"

    "With a sigh, I see the girl, distracted from her book, glance up at me and start looking in her bag for something. After some rustling, she offers me a roll of toilet paper."

    "The sudden gesture surprises me, but feeling an incoming sneeze, I take it without too much thought."

    p "Thanks."

    #shiori nod/smile, giggle sfx
    shi "You're welcome, your sneeze and sniffles were a little distracting, so I have no choice but to sacrifice my tissues. *giggle*"

    "As I turn away to blow my nose, she focuses back on her book again."

    "After a few minutes of checking the library catalog on my phone, I get up with a light sigh."

    p "{i}Guess I'll start searching again...{/i}"

    #fade in heavy rain sfx
    "It seems the weather is getting worse. Outside, I can see more of the automatic lights turning on."

    "I keep searching, but I can't seem to find any of the references for my report no matter how hard I look."

    "As I wander the aisles, it dawns on me how unusually empty it is today."

    p "I guess people are staying home today."

    p "Or are doing other things."

    "I see the girl again and sigh, a little frustrated." 
    
    p "{i}Maybe I could ask the library workers for advice? But other than the front desk worker, there are no signs of them anywhere.{/i}"

    "I sit back down, and the girl glances back up at me over the edge of her book."

    shi "Are you ok? You've been mumbling about something and walking back and forth for a while."

    p "Oh, I'm just trying to find some books for a report. But I have no idea where they are."

    if bookhate:
        #smug shiori
        shi "I see. Well, no wonder you look like a child lost in a store."
    
    if booklove:
        #teasing shiori
        shi "Really? And I thought someone who loves books so much would take to libraries like a fish takes to water."

    if bookneutral:
        #shiori nod?
        shi "So, is this your first time here? Well, this is a pretty big library. It's easy to get turned around here."
    
    p "So you do remember me!"

    #Shiori pout
    shi "Of course I do, it was just recently. It's not like I'm a goldfish, after all."

    p "In that case, I should introduce myself. I'm [p.name]."

    "She tilts her head and then closes her book after a moment."

    $ shi.name = "Shiori"

    shi "Shiori Novella, at your service. Nice to officially meet you."

    #shiori giggle
    shi "*giggle* 'Officially', 'fish'."

    "She giggles to herself for a moment, before looking at you again."

    shi "Have you asked anyone for help, since you've been looking for so long?"

    p "{i}If I could find an employee, I might've asked them, or even one of my friends, if they were here. But I'm not sure I've got it in me to walk up to a stranger and ask for help. Even me talking to Shiori is unusual.{/i}"

    p "N-no... I couldn't find a librarian, and you're the only person I know at least a little bit here right now."

    "I watch her expression go from curious to a more smug one."

    #shiori smug here
    shi "Suuuure... In that case, you can ask me. I'm here pretty often, so I know this place like the back of my hand."

    #shiori smile here
    shi "But first, I need to know what books you're looking for, and what your report's on."

    "I explain my project to her, as she listens carefully and nods to herself."

    shi "I research that for fun once. Maybe I can help!"

    "She leaves her book on the table and walks to a library computer to look for something."

    "While she types away, leaned over the computer, I sneak a peek at the unusual book. Just like before, it keeps drawing my attention. The bloack cover, purple spikes, and a large eye logo in the middle of the cover."

    "The longer I look at it, the more I feel pulled to it."

    #Flash of lightning and eye on book blinks
    #thunder sfx a second later
    p "{i}What? What was that?{/i}"

    "I shake my head and rub my eyes and look at the book again."

    p "{i}Was it just my imagination?{/i}"

    p "Hey what did you say this book was about again?"

    shi "Just a story I love, what about it?"

    p "If you don't mind, could I take a peek? I'm curious about it."

    #shiori complicated expression (whichever fits best)
    "Shiori turns and watches me, her gaze alternating between me and the book after a moment."

    p "{i}Maybe I shouldn't have asked...{/i}"

    shi "Yeah, you're welcome to try, but I don't think it'll be helpful for you."

    p "Why not? It looks interesting!"

    "I reach toward the book, but I hesitate for a moment."

    menu:
        "You know what, maybe later...":
            p "You know what, maybe later..."

            "Shiori's face relaxes, but she seems a little disappointed, too."
        
        "Open the book.":
            "I open the strange book. Just like before, everytime I flip a page, one of the visible pages is empty and the other is covered in those strange symbols."

            p "What language is that? Latin? Sanskrit? Or something else entirely?"

            #shiori eye sparkle or something expression
            shi "So, how is it? Can you read any of it?"

            p "Nope, not at all. What language is that?"

            shi "Oh... I don't know myself. That's why I've been trying to decipher it."

            "I can't but notice the hesitation before she asnwers, but drop it for now."

            p "{i}Didn't she say her friend helped with it, though...?{/i}"
    
    shi "Well, enough about the book, we can discuss my hobbies another time. Let's go. You still don't have any of the books you're looking for."

    "With that, Shiori gets up, puts her book away, and gestures for me to follow her. I hastily get up, pushing the book out of my mind for now."

    shi "So why the interest in my book? Is it familiar to you?"

    p "Honestly, no. I've never seen anything like it, but it makes my brain feel... itchy, I guess? That's not quite it, but it feels like I should recognize it, or..."

    p "Actually, you know what? Nevermind."

    shi "Really? Interesting."

    "She hums quietly, bringing a forefinger to her chin in apparent thought, before shaking her head."

    shi "Well, we can worry about that later."

    shi "Anyway, once we find those reference books for you, what kind of story do you want to read for fun?"

    "I think for a moment, remembering she'd offered me a few recommendations."

    menu:
        "Sweet stories about a couple people.":
            $ route_slice = True
        "I've always like the mysteries in Lovecraft stories.":
            $ route_lc = True
        "Magic is pretty cool.":
            $ route_fantasy = True
    
    if route_slice:
        shi "Couple? *giggle* What? Are you trying to rizz me up?"

        p "Ah, no, I just mean..."

        "I feel my face heat up as I realize what I said."

        #shiori giggle
        shi "I'm kidding! I'm curious why that's your answer though. You've got a whole library here, but you're more interested in the stories we can create off the page, huh?"

        p "{i}It's a bit embarrassing t ohear it pointed out like that. But, stories have to come from somewhere after all.{/i}"

        p "Well, I just thought that life could have some pretty interesting moments, don't you think so?"

        "She pauses, looking upwards, as if searching for an answer. Then, she smiles and gives a small chuckle."

        shi "You're certainly not wrong there."

        "She opens her mouth again as if she were going to say something, but she decides not to."

        shi "Anyways, speaking of stories and libraries, what books did you need again? We'll be here all day if you have to listen to more of my tangents."

        p "{i}Right, that was the whole point of why I came here in the first place. Although, I wouldn't have minded listening to her tangent all day. It would probably be much more fun than having to search for those books in this maze.{/i}"

        p "Oh, uh..."

        "I check the note on my phone, and reading the two titles, I realize I forgot to write down the last of the three books I need."

        p "Let's see... There's 'Le Morte D'Arthur', Pollard's 'Warwick the Kingmaker', and uh..."

        p "{i}Shoot. What was the last one?{/i}"

        shi "'Historie of the Arrivall of Edward IV in England and the Finall Recouerye of His Kingdomes from Henry VI', right?"

        p "Yeah! That's... How'd you know that?"

        #shiori giggle sfx
        shi "*giggle* Lucky guess?"

        "I think for a couple seconds, but considering the other books I need, it makes sense she'd guess correctly. Especially since she comes to the library a lot."

        p "Well, thanks, you saved me. I couldn't remember it... at all."

        shi "Really? That's interesting."

        p "How so?"

        shi "Oh, nevermind. I was just thinking of something. But you might be right, life definitely has some nice moments."

        p "{i}I'm not sure what she means by that, but she seems proud of herself, considering her beaming face.{/i}"

        p "Alright then. Well, can you help me find the those books? You already know I'm not the best at navigating here."

        shi "Hmm... On one condition."

        p "{i}Oh no, what have I just gotten myself into...{/i}"

        "I sigh and slump my shoulders, ready to  accept whatever this woman asks of me. It's either that, or I fail this report."

        p "Uh... Fine. Not like I have much of an option."

        #animate to sly shiori face
        shi "What...."

        #zoom in a little on shiori's face
        shi "...do...."

        #zoom in a little more
        shi "...you..."

        #zoom in even more until only her eyes are seen
        shi "... think of slice of life stories?"

        p "W-what?"

        "She steps closer, and I instinctively take a step back."

        #shiori zoomback out to normal
        "She stares at me for a moment, then turns around and marches off."

        shi "C'mon! You can answer me while we look for your books. That's my condition!"

        "I quickly follow after her so I don't lose sight of her."

        p "Why slice of life?"

        shi "Oh, I was just thinking about what you said, and it got me thinking about slice of life stories. It's like cake. Cake slices. Hopefully you get a good piece, or else the entire thing is ruined."

        p "I... don't know if the genre is named after cake slices."

        shi "What if it was? Think about it! There are layers to a slice of life; there are layers to a cake. Slice of life usually starts off sweet at the top, like frosting on a cake."

        "She stops suddenly, turning to her left and kneels down to pull a red-spined book from the bottom shelf."

        shi "Then, as you get deeper in, there is less frosting and more of that fluff that can be any flavor. Sure it can be bland..."

        "She hands me a book titled 'Warwick the Kingmaker'."

        shi "... But sometimes you get that really good slice with ice cream in the middle. Just like with slice of life stories that really hit close to home."

        p "{i}Now that she explains it like that, I guess a slice of life story could be like cake then. Although, that doesn't really answer why she's interested in them, nor why she asked me what I thought about them.{/i}"

        p "Ah, thanks! Alright, let's say slice of life is like slices of a cake. I'm not sure I've ever given it that much thought."

        shi "I'm sure there's something you like about it!"

        "She whirls around, guiding us around a corner and up a staircase."

        p "It's just... All the cheesy and chance encounters don't really appeal to me, you know?"

        shi "I can agree with you on the romance part. It's not really my thing either. But the stories are still comfy, since they don't have any world ending stakes or political drama."

        "We stop at another shelf and she stands on her tiptoes, trying to reach a thick, slate-gray book, and eventually resorts to hopping up to grab at it."

        "She manages to knock it down with her finger, and it tumbles off the shelf. I dart forward and catch it right before it drops onto her head. I look down at it and see that I'm holding a copy of 'Le Morte D'Arthur'."

        p "Phew... That was close. Are you okay?"

        shi "I'm fine. Happens more often to me than you'd think."

        p "{i}Hold on, how many books have fallen onto her then?{/i}"

        shi "Anyways! Pure romance is just boring and too restrictive. I prefer the ones where I can ship myself with the characters. Oh! But sometimes I like to ship characters together, too."

        p "Is... that really your reason for liking slice of life?"

        p "{i}This girl is something else...{/i}"

        shi "Part of it, at least."

        "She walks over to the stairway, looks around for a moment, then goes downstairs, turning left at the last bookshelf."

        shi "Another thing is that a slice of life story would be nice to experience. you know, just being able to spend time with someone without anything threatening daily life."

        "We make our third stop at the very back of the first floor. This time, the book is within the reach, easily letting her grab the heavy-looking chronicle and hand it to me."

        shi "And well... sometimes, it owuld be nice to just be able to have a relaxing, memorabble day with people I'm fond of."

        "With 'Arrivall' joining the other two books in my hands, I am now set for the all-nighter later on. However, what Shiori said caught my attention."

        p "{i}Isn't she already living a normal life?{/i}"

        p "Well, at least it won't be too difficult to get something like that. I doubt college life is that different from any slice of life scenario."

        "Shiori looks as if she was going to say something like before, but then stops and looks away. She mutters something under breath."

        shi "If... things... easy..."

        p "Hm? What was that?"

        shi "Ah! Nothing. Well, we got your books. Job well done, right?"

        p "{i}I guess I'll move on from that then if she didn't want to dwell on it.{/i}"

        p "Yeah, thank you so much. Couldn't have done it without you."

        shi "Heh, don't mention it. I practically live here, so finding stuff like this is pretty easy."

        "We walk back over to the front counter, grabbing a short slice of life story on the way, where I check out my books and then turn to Shiori."

        p "Well, thanks again. Maybe I'll see you around whenever I visit that cafe or the library again."

        #teasing shiori
        shi "Looking forward to it. Maybe you'll be able to tell me more about 'sweet stories about couples' next time."

        p "Ah, that... I didn't really..."

        p "{i}It's not like I was that serious with that answer in the first place. But she seems so interested in that concept I pulled out of thin air. She really is something else.{/i}"

        p "You know what? Yeah, maybe next time, then."

        "She smiles and waves."

        shi "See ya later then!"

        "I wave back and walk out. After being in that labyrinth of books, it feels nice to be outside again, and the rain has even lightened up. I walk back home, already dreading the amount of caffeine I'm going to need to drink to stay awake through tomorrow."
    
    if route_lc:
        #lc content goes here
        pass
    
    if route_fantasy:
        #fantasy content goes here
        pass

    return