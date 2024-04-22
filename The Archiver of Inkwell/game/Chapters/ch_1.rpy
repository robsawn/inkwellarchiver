$ renpy.include("Helpers/characters.rpy")
$ renpy.include("Helpers/trackers.rpy")
$ renpy.include("Helpers/particles.rpy")

label ch_1:
    #fade in from black
    "It's finally the weekend, but I don't really get to relax this week. I have to go to the library and try to find books for that research report."

    "I double check what books my professor recommended and make a note of them in my phone."

    "With the books noted, I leave for the library with a grimace, feeling like a couple of them might be difficult to find."

    #light rain sfx
    "Walking down the street, I feel a calm wash over me as I listen to the soft drumming of the light rain against my umbrella."

    "A grin sneaks its way onto my face, seeing the kids in the area play in the puddles again, their laughter ringing out between the buildings."

    "I can't help but remember the woman I met in the cafe the other day. Despite the cloudy skies, she was as blindingly bright as the sun."

    p_i "I should see if I can find some of those recommendations she had for me, too..."

    "Luckily, it doesn't take long to get to the library and I step inside right as the rain starts coming down harder."

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

    p "Long time, no see, huh?"

    "I stand there a little awkwardly, just now noticing that she's focusing on the same book as she was before."

    p "Uh... Hello?"

    shi "Hm? Oh! It's you! Hi!"

    p "Hey, mind if I sit with you?"

    "She nods, and I let myself fall into the seat with a deep exhale. All the wandering in this part of the library has been exhausting, and the dust from the shelves makes my nose itch." 

    p_i "Seems this place isn't very popular..."

    p_i "But wouldn't the people working here usually at least dust the shelves?"

    "I sneeze and reach into my pockets for a pack of tissues, but come up empty."

    p_i "Great, not only can I not find what I came for, but I'm gonna be sniffling..."

    "With a sigh, I see the girl, distracted from her book, glance up at me and start looking in her bag for something. After some rustling, she offers me a roll of toilet paper."

    "The sudden gesture surprises me, but feeling an incoming sneeze, I take it without too much thought."

    P "Thanks."

    #shiori nod/smile, giggle sfx
    shi "You're welcome, your sneezes were a little distracting, so I have no choice but to sacrifice my tissues. *giggle*"

    "As I turn away to blow my nose, she focuses back on her book again."

    "After a few minutes of checking the library catalog on my phone, I get up with a light sigh."

    p_i "Guess I'll start searching again..."

    #fade in heavy rain sfx
    "It seems the weather is getting worse. Outside, I can see more of the automatic lights turning on."

    "I keep searching, but I can't seem to find any of the references for my report no matter how hard I look."

    "As I wander the aisles, it dawns on me how unusually empty it is today."

    p "I guess people are staying home today."

    p "Or are doing other things."

    "I see the girl again and sigh, a little frustrated. Maybe I could ask the library workers for advice? But, other than the front desk worker, there are no signs of them anywhere."

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

    #Shiori pouts
    shi "Of course I do, it was just recently. It's not like I'm a goldfish, after all." 

    p "In that case, I should introduce myself. I'm [p.name]." 

    "She tilts her head and then closes her book after a moment."

    $ shi.name = "Shiori"

    shi "Shiori Novella at your service. Nice to officially meet you."

    #shiori giggle
    shi "*giggle* ‘Officially', ‘fish'."

    "She giggles to herself for a moment, before looking at you again."

    shi "Have you asked anyone for help, since you've been looking for so long?"

    "If I could find an employee, I might've asked them, or even one of my friends if they were here. But I'm not sure I've got it in me to walk up to a stranger and ask for help. Even me talking to Shiori is unusual."

    p "N-no... I couldn't find an employee, and you're the only person I know at least a little bit here right now."

    "I watch her expression go from curious to a more smug one"

    shi "Suuure... In that case, you can ask me. I'm here pretty often, so I know this place like the back of my hand." 

    #shiori smile here
    shi "But first, I need to know what books you're looking for, and what your report's on."

    "I explain my project to her, as she listens carefully and nods to herself."

    shi "I researched it for fun once. Maybe I can help!"

    "She leaves her book on the table and walks to a library computer to look for something."

    "While she types away, I sneak a peek at the unusual book. Just like before, it keeps drawing my attention. The black clover, purple spikes, and a large eye logo in the middle of the cover."

    "The longer I look at it, the more I feel pulled to it."

    #Flash of lightning & eye on book blinks
    #thunder sfx
    p_i "What? What was that?"

    "I shake my head and rub my eyes and look at the book again."

    p_i "Was it just my imagination? I could've sworn that book... blinked..."

    p "Hey, what did you say this book was about again?"

    shi "Just a story I love, what about it?"

    p "If you don't mind, could I take a peek? I'm curious about it."

    #shiori complicated expression (whichever fits best)
    "Shiori turns and watches me, her gaze alternating between me and the book after a moment."

    p_i "Maybe I shouldn't have asked..."

    shi "Yeah, you're welcome to try, but I don't think it'll be helpful for you."

    p "Why not? It looks interesting!"

    "I reach toward the book, but I hesitate for a moment."

    menu: 
        "You know what, maybe later...":
            p "You know what, maybe later..."

            "Shiori's face relaxes, but she seems a little disappointed, too."

        "Open the book.":
            "I open the strange book. Just like before, every time I flip a page, one of the visible pages is empty and the other is covered in those strange symbols."

            p "What language is that? Latin? Sanskrit? Or something else entirely?"

            #shiori eye sparkle or something expression
            shi "So, how is it? Can you read any of it?" 

            p "Nope, not at all. What language is that?"

            shi "Oh... I don't know myself. That's why I've been trying to decipher it."

            "I can't help but notice the hesitation before she answers, but drop it for now."

            p_i "Didn't she say her friend helped with it, though...?"

    shi "Well, enough about the book, we can discuss my hobbies at another time. Let's go. You still don't have any of the books you're looking for."

    "With that, Shiori gets up, puts her book away, and gestures for me to follow her. I hastily get up, pushing the book out of my mind for now."

    shi "So why the interest in my book? Is it familiar to you?"

    p "Honestly, no. I've never seen anything like it, but it makes my brain feel... itchy, I guess? That's not quite it, but it feels like I should recognize it, or... Actually, you know what? Nevermind."

    shi "Really? Interesting."

    "She hums quietly, bringing a forefinger to her chin in apparent thought, before shaking her head."

    shi "Well, we can worry about that later."

    shi "Anyway, once we find those reference books for you, what kind of story do you want to read for fun?"

    "I think for a moment, remembering she'd offered me a few recommendations."

    menu:
        # "Sweet stories about a couple people.":
        #     $ route_slice = True
        "I've always been interested in Lovecraft stories.":
            $ route_lc = True
        "Magic is pretty cool.":
            $ route_fantasy = True

    # if route_slice:

    #     shi "Couple? *giggle* What?"
        
    #     p "Ah, no, I just mean..."
        
    #     "I feel my face heat up as I realize what I said."

    #     #shiori giggle
    #     shi "I'm kidding! I'm curious why that's your answer though. You've got a whole library here, but you're more interested in the stories we can create off the page, huh?"
        
    #     p_i "It's a bit embarrassing to hear it pointed out like that. But, stories have to come from somewhere after all."
        
    #     p "Well, I just thought that life could have some pretty interesting moments. Don't you think so?"
        
    #     "She pauses, looking upwards, as if searching for an answer. Then, she smiles and gives a small chuckle."
        
    #     shi "You're certainly not wrong there."
        
    #     "She opens her mouth again as if she were going to say something, but she decides not to."
        
    #     shi "Anyways, speaking of stories and libraries, what books did you need again? We'll be here all day if you have to listen to more of my tangents."
        
    #     p_i "Right, that was the whole point of why I came here in the first place. Although, I wouldn't have minded listening to her tangent all day. It would probably be much more fun than having to search for those books in this maze."
        
    #     p "Oh, uh..."
        
    #     "I check the note on my phone, and reading the two titles, I realize I forgot to write down the last of the three books I need."

    #     p "Let's see... There's ‘Le Morte D'Arthur', Pollard's ‘Warwick the Kingmaker', and uh..."
        
    #     p_i "Shoot. What was the last one?"
        
    #     shi "‘History of the Arrival of Edward IV. in England and the Final Recovery of His Kingdoms from Henry VI.', right?"
        
    #     p "Yeah! That's... How'd you know that?"

    #     #shiori giggle sfx
    #     shi "*giggle* Lucky guess?"
        
    #     "I think for a couple seconds, but considering the other books I need, it makes sense she'd guess correctly. Especially since she comes to the library a lot."
            
    #     p "Well, thanks, you saved me. I couldn't remember it... at all."
        
    #     shi "Really? That's interesting."
        
    #     p "How so?"
        
    #     shi "Oh, nevermind. I was just thinking of something. But you might be right, life definitely has some nice moments."
        
    #     p_i "I'm not sure what she means by that, but she seems proud of herself, considering her beaming face."
        
    #     p "Alright then. Well, can you help me find those books? You already know I'm not the best at navigating."

    #     shi "Hmm... On one condition."
    #     #animate to sly shiori face
    #     p_i "Oh no, what have I just gotten myself into..."
        
    #     "I sigh and slump my shoulders, ready to accept whatever this woman asks of me. It's either that, or I fail this report."
        
    #     p "Uh... Fine. Not like I have much of an option."
        
    #     #animate to smiling Shiori
    #     shi "Tell me what you think of slice of life stories?"
        
    #     "She steps closer, and I instinctively take a step back."
        
    #     "She stares at me for a moment, then turns around and marches off."
        
    #     shi "C'mon! You can answer me while we look for your books."
        
    #     "I quickly follow after her so I don't lose sight of her."
        
    #     p "Why slice of life?"
        
    #     shi "Oh, I was just thinking about what you said, and it got me thinking about slice of life stories. It's like cake. Cake slices. Hopefully you get a good piece, or else the entire thing is ruined."
        
    #     p "I... don't know if the genre is named after cake slices."
        
    #     shi "What if it was? Think about it! There are layers to a slice of life; there are layers to a cake. Slice of life usually starts off sweet at the top, like frosting on a cake."
        
    #     "She stops suddenly, turning to her left and kneels down to pull a red-spined book from the bottom shelf."
        
    #     shi "Then, as you get deeper in, there is less frosting and more of that fluff that can be any flavor. Sure, it can be bland..."
        
    #     "She hands me a book titled ‘Warwick the Kingmaker'."
        
    #     shi "... But sometimes you get that really good slice with ice cream in the middle. Just like with slice of life stories that really hit close to home."
        
    #     p_i "Now that she explains it like that, I guess slice of life could be like cake then. Although, that still doesn't really answer why she's interested in them, nor why she asked me what I thought about them."
        
    #     p "Ah, thanks! Alright, let's say slice of life is like slices of a cake. I'm not sure I've ever given it that much thought."
        
    #     shi "I'm sure there's something you like about it!"

    #     "She whirls around, guiding us around a corner and up a staircase."
        
    #     p "It's just... All the cheesy romance and chance encounters don't really appeal to me, you know?"
        
    #     shi "I can agree with you on the romance part. It's not really my thing either. But the stories are still comfy, since they don't have any world ending stakes or political drama."
        
    #     "We stop at another shelf and she stands on her tiptoes, trying to reach a thick slate-gray book, and eventually resorting to hopping up to grab at it. She manages to knock it down with her finger, and it tumbles off the shelf. I dart forward and catch it right before it drops onto her head. I look down at it and see that I'm holding a copy of ‘Le Morte D'Arthur'."

    #     p "Phew... That was close. Are you okay?"
        
    #     shi "I'm fine. Happens more often to me than you'd think."
        
    #     p_i "Hold on, how many books have fallen onto her then?"
        
    #     shi "Anyways! Pure romance is just boring and too restrictive. I prefer the ones where I can ship myself with the characters. Oh! But sometimes I like to ship characters together, too."
        
    #     p "Is... that really your reason for liking slice of life?"
        
    #     p_i "This girl is something else..."
        
    #     shi "Part of it, at least."
        
    #     "She walks over to the stairway, looks around for a moment, then goes downstairs, turning left at the last bookshelf."
        
    #     shi "Another thing is that a slice of life story would be nice to experience. You know, just being able to spend time with someone without anything threatening daily life."
        
    #     "We make our third stop at a shelf at the very back of the first floor. This time, the book is within reach, easily letting her grab the golden chronicle and hand it to me."
        
    #     shi "And well... sometimes, it would be nice to just be able to have a relaxing, memorable day with people I'm fond of."
        
    #     "With ‘Arrival' joining the other two books in my hands, I am now set for the all-nighter later on. However, what Shiori said caught more of my attention."
        
    #     p_i "Isn't she already living a normal life?"
        
    #     p "Well, at least it won't be too difficult to get something like that. I doubt college life is that different from any slice of life scenario."
        
    #     "Shiori looks as if she was going to say something like before, but then stops and looks away. She mutters something under her breath, but I can barely make out what she's saying."
        
    #     shi "If... things... easy..."
        
    #     p "Hmm? What was that?"
        
    #     shi "Ah! Nothing. Well, we got your books. Job well done, right?"
        
    #     p_i "I guess I'll move on from that then if she didn't want to dwell on it."
        
    #     p "Yeah, thank you so much. Couldn't have done it without you."
        
    #     shi "Heh, don't mention it. I practically live here, so finding stuff like this is pretty easy."
        
    #     "We walk back over to the front counter where I check out my books and then turn to Shiori."
        
    #     p "Well, thanks again. Maybe I'll see you around whenever I visit that café or the library again."
        
    #     shi "Looking forward to it. Maybe you'll be able to tell me more about ‘Our Story' next time."
        
    #     p "Ah, that... I didn't really..."
        
    #     p_i "It's not like I was serious with that answer in the first place. But she seems so interested in that concept I pulled out of thin air. She really was something else."
        
    #     p "You know what? Yeah, maybe next time, then."
        
    #     "She smiles and waves."
        
    #     shi "See ya later then!"
        
    #     "I wave back and walk out. After being in that labyrinth of books, it feels nice to be outside again, and the rain has even lightened up. I walk back home, already dreading the amount of caffeine I'm going to need to drink to stay awake through tomorrow."

    if route_lc:

        p "I've always been interested in Lovecraft stories." 

        shi "Oh? Lovecraft mysteries? Well, I'm certainly a fan of those works."
        
        p "I've never read them, but I've heard how weird, creepy, and crazy they can get. I can't imagine being a character in one of those stories."
        
        shi "Being in that kind of story huh..."

        #if we get like a big grin and eye effect, this is a good spot for it
        "Her eyes gleam as a grin stretches across her face."
        
        shi "Who knows. It could be a bit fun."
        
        p "Y-Yeah, I guess."
        
        "As I look at her smile, I feel a chill run up my spine and I gulp."
        
        shi "C'mon! Don't you think it's exciting to be involved with weird cults, unknown deities, and mysteries beyond our imaginations?"
        
        "Those words sound so innocent, but something is telling me to stop this conversation from going any further."
        
        p "It just... seems scary to deal with all of that."
        
        "Her smile fades, and she sighs. Then, she puts on the same soft smile from before."
        
        shi "When you put it that way, I guess it can be a bit much for some people who aren't ready for those kinds of stories."
        
        "She waves her hand, as if waving away an intrusive thought and shakes her head."

        shi "Anyways, enough of that. You said you needed some books, right?"
        
        p_i "I'm glad she changed the subject. She was starting to sound a bit too enthusiastic about those kinds of stories. Of course, there's nothing wrong with that, but... Her words just felt off to me." 

        p_i "It's probably nothing."
        
        p "Right! I wrote them down. Let's see..."
        
        shi "It's ‘Le Morte D'Arthur', Pollard's ‘Warwick the Kingmaker', and History of the Arrival of Edward IV. in England and the Final Recovery of His Kingdoms from Henry VI..'"
        
        p_i "She listed every book I needed... I didn't even pull my phone out yet..." 

        "Just to double check, I check my list, and find she's named the books I noted before, and the one I'd forgotten to note."
        
        p "Yeah...how did you...?"
        
        shi "Oh, you know..."
        
        shi "...I just happen to have eyes everywhere."
        
        "I let out a small chuckle at her weird joke."
        
        p "G-Good one. You really had me going."
        
        shi "Heh, I'm glad it worked then."
        
        p_i "That still doesn't explain how or why she knows what books I need though... And the more time I spend with her, the more unnerving she gets."

        p "Well, thanks for helping me."
        
        shi "... I figured as much."
        
        "I barely caught Shiori's muttering."

        p "What do you mean?"
        
        shi "Ah, don't worry about it."
        
        p "Well, considering you know what I'm looking for, would you still help find those books?"
        
        #shio-giggle sfx
        shi "Hmm? What makes you think I would help you out? *giggle*"
        
        p_i "She's got a point. She has no reason to help me out when it's not her responsibility to find these books."
        
        p "Ah...sorry. You're right."
        
        shi "Don't be like that. I didn't say I wouldn't help you."
        
        #switch to Shiori sly face
        "She turns around and leans forward slightly. Then, she squints her eyes as she grins at me a little."

        shi "I just have to ask, if you're interested, why haven't you read any Lovecraft stories?"

        p_i "She seems really fixated on that. Weird, but what's the harm in talking about it anyway? She is helping me, after all."

        p "No particular reason, I just never got around to it. Besides, don't they all have rough endings, partially because of the lack of control...?"

        shi "Aww, but who said all stories need a happy ending? Sometimes, things just don't go as planned no matter how hard somebody tries."

        p "I do."
        
        shi "Hmm?"
        
        p "I say all stories should have a happy ending. The world's depressing enough, don't you think?"
        
        p_i "Sure, I say that, but what am I even talking about? Maybe I'm just in a mood?"
        
        shi "The world, huh...?"
        
        "Shiori reaches out and pulls a book off a shelf to her right, her hand hesitating, as if she's expecting something more."

        "Handing the book to me, it's ‘Le Morte D'Arthur', but it's oddly dusty, as if it hadn't been touched in years. I look back up to see her smiling softly."

        shi "Maybe... maybe the world could use more happy endings."
        
        p "Yeah. Everyone deserves a happy ending, especially for the characters stuck in Lovecraft stories."
        
        shi "Even..."
        
        "She lowers her head as her voice trails off."
        
        shi "... the ones who can't escape their own fate?"
        
        #fade in heavy rainfall sfx
        "I struggle to find an answer to that as the rain fills the void of silence between us as it batters against the window as we walk by."
        
        p_i "It's a really heavy question to answer, especially to someone I don't really know well yet. I can't tell if she wants a serious or lighthearted answer."

        p "If that's the case, then they just need someone to come along and help them out."
        
        "She just looks at me and stops while turning into the next aisle of books, before she blinks a few times."

        #shio-giggle sfx
        shi "*giggle* If only it was so simple..."
        
        p "Hey, you asked."
        
        shi "I know, I know."
        
        p "It really can be as simple as someone just reaching a hand out sometimes."
        
        "She wipes a single tear from her eye as she sniffles. Taking a deep breath to compose herself, she darts her hand to the left without looking and withdraws it, book in hand. I look down to see a golden cover, with the title of ‘Arrival' embossed on the front."
        
        shi "Oh, you're serious?"
        
        p "Of course I'm serious. I can't imagine giving up on someone who's struggling with stuff like that."
        
        shi "Is that so? Good to know..."
        
        "She taps her index finger on her chin as she strides confidently down the next aisle."
        
        shi "You know what? Maybe you're right. But it would take someone who isn't scared of all that eldritch stuff."
        
        "She stops in front of a seemingly random bookshelf and turns to look at me."
        
        shi "You still need a book, now that I think about it."
        
        "Smiling, she hops up and tries to grab a book off the top shelf, her finger pulling on the spine just enough to make the book fall toward her. Before I can think, I quickly reach up and catch the book before it drops onto her."

        "I look down at her to see a sheepish grin, and glance at the book to see the last title I needed."

        p "I'm guessing that didn't go the way you wanted?"
        
        shi "It's fiiiiiiiiiiiiiine."

        "We walk back over to the table with the books, Shiori trailing behind me. I set them down one at a time."
        
        p "Huh?"
        
        "As I set the third book down, there's a fourth book that we didn't talk about." 

        "It's Shiori's book from earlier. Just as I reach for it, Shiori slams her hand down onto it, making me jump."
        
        shi "Don't look at it!"
        
        "She slides it off the table and hides it behind her back."
        
        p "O...kay then."
        
        p_i "That was weird..."

        shi "Anyways! It wasn't that hard to find your books. I think you should be fine now."
        
        p "Ah, yeah. Thanks. I guess it was a lot easier than I thought."
        
        shi "See you around then?"
        
        p "I'll be around on campus, so we'll probably run into each other at some point."
        
        "She smiles and waves at me as I prepare to leave. I wave back and turn toward the exit."
        
        shi "Just be careful."
        
        "Her cheery voice fades into a more serious tone."
        
        #heavy rainfall louder than ever
        shi "It's going to be raining for a while."
        
        p "Ah... yeah. Good thing I still have my umbr—"
        
        "When I turn back to look at her over my shoulder, I don't see anyone."
        
        p_i "Huh? Wait. But she was just..."
        
        "I try looking around some more, even checking behind a couple of the nearby shelves to see if she's pranking me." 

        "Nobody. It's as if she simply vanished without a trace."
        
        p "What the...?"
        
        "The longer I stand there, the more uneasy I feel. Shrugging, I check out the books at the front desk and grab my umbrella on the way out."
        
        p_i "That was... interesting."
        
        "Before I can fully open my umbrella, a strong gust of wind knocks it out of my hand. It lands in a puddle on the sidewalk, handle down."
        
        "I sigh and step out into the pouring rain grabbing my umbrella. Right as I bend over, I notice somebody in a yellow raincoat walking toward me in the reflection of the puddle. I quickly pick up my umbrella and turn around. Once again, there is nobody there."
        
        p_i "I guess I'm just tired already..."
        
        "As I walk home listening to the rain drum on the umbrella above me, my skin crawls as I go over my conversation with Shiori in my head. As I round a corner on the final stretch before reaching home, I feel eyes boring into my back and I whip around. I stand stock still, looking around. However, the feeling is gone, and there's no one around."
        
        "I try to calm my breathing and just focus on taking one step at a time away from this place."
        
        p_i "Why do I feel like I'm being watched?"

    
    if route_fantasy:
        #fantasy content goes here
        pass

    return