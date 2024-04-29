label ch_14:
    #Fade in #Heavy rain sfx 

    "The rain hasn't let up since the day Shiori vanished and the campus is unsurprisingly scarce. Most students and even faculty just haven't shown up. Just making my way around on a day like this has become a maddening process of trudging through ankle high puddles as the older streets overflow. If I wasn't trying to find someone, I wouldn't have bothered showing up either."

    "Even so, she's worth it, isn't she? Making sure she's ok? Things have gone too far to be just a coincidence, right? Perhaps it's a prank by those fashion forward 'cultists'? But what if it's more than that?"

    "The few people I have run into so far today have either been wearing one of the yellow raincoats or have not said anything helpful. Nevertheless, I decide to push forward as I see another person."

    p "Excuse me! Have you seen a goth girl lately?"

    fs "Huh? What? Is that your type?"

    p "No, I mean she's a student! With black and white hair and these bright piercing golden eyes?"

    fs "Sounds Chunni..."

    p_i "I feel like I'm being judged for my choice of words here. Then again, I'm not any better, am I?"

    fs "Wait, I know who you're talking about. The weird girl that feeds the stray cats? I think she was arguing with that raincoat clique last time I saw her. Haven't seen her since though."

    p "Oh. Thanks, that helps."

    "It really doesn't. And I swear I can hear them muttering something unpleasant as they wave me away and vanish into the rain. But it's the first lead I have." 

    p_i "Lead? What am I now, a detective? Either way, it seems like a bad idea to just confront potential kidnappers, but what else can I do? Coax information out of cats?"

    menu:
        "Look for 'Cultists'":
            p_i "The raincoat clique knows something..."
            $ followcultists = True
        "Follow the cats":
            p_i "I have nothing else to go on..."
            $ followcats = True
            $ ending += 1

    if followcultists:

        #Fade out/fade in

        "With a bit of legwork it doesn't take me long to find a small cluster of 'cultists'. In fact, they are just hanging out by the vending machines."

        p_i "Maybe they really are just a harmless clique?"

        "They haven't noticed me yet, but I can't just sit around and wait until they do! I dive behind the closest hiding spot I can find. A trashcan might not be ideal, but it will do in a pinch. While at first glance they all seem content with standing about menacingly with that all too familiar vacant stare, after a while, I manage to catch them talking. Initially it just sounds like muttering, so I take my chances and move a little closer."

        fc "All I'm saying is we have the archiver, right? Shouldn't we be back at headquarters, y'know, rejoicing in the coming of the Void Wyrm? Eating the cake the others were working on for the ritual?"

        sc "I think you underestimate the archiver. She is tricky, and has a way of causing trouble when you least expect it. We must remain vigilant."

        "That comment catches me off guard for a moment, but I remember to stay hidden. While Shiori is certainly... unique, that's still a far cry from the clumsy, book loving goober I have gotten to know. Is she really the sort of person that requires 'vigilance'?"

        fc "So we are just going to stand around and wait for something to happen? Lame."

        sc "Ensuring the success of our ritual is not 'lame'. Can we not rejoice in the purification of this forsaken world, right here?"

        fc "Stop twisting my words! I'm rejoicing as much as anyone! I just want to do it with cake."

        sc "There is a vending machine right behind you."

        "Wait? Shiori was right?! The conversation went from 0 to 100 faster than I could process, with rituals, contingency plans, and even just how they view Shiori. They're really a cult?! In a flash, the whole world spins around me. Partly due to the revelations, yes, but I had also failed to notice the frustrated cultist taking their anger out on a can, kicking it in my direction."

        fc "You know what I-"

        p "ow"

        fc "Wait! What was that?"

        p_i "Oh no. Have they noticed me?"

        sc "It sounded like a meow, but we can't be too cautious."

        "The most eager of the group quickly darts in my direction and begins to round the corner. Not wanting to take any chances with them, I make a break for it. I can hear them yelling and chasing after me, but it is oddly easy to lose them in the deluge of rain."

        p_i "At least I figured out that they have some kind of headquarters... I bet that's where Shiori is."

        "I can still barely make out the bright yellow of their coats through the rain. I think they are circling the area in hopes of finding me."

        "I keep my distance for now, trying to track their movements through the downpour. If I can hold out long enough, I could figure out where their base is... Right?"

        #fade in/fade out

        "This twisted game of cat and mouse stretches on with no end in sight, in fact it's getting harder to see at all. Both my pursuers and the buildings on the horizon seemingly melt into the rain. For a moment, I even think I pass by the science building only to find a flooding pond."

        p_i "I must be really turned around."

        "My attention is drawn to the book Shiori gave me as serendipity compels me to open it. Huh. It's mostly full of scribbles that are difficult to read, but I can make out details about a cult of the 'Void Wyrm'. There are numerous doodles of their symbol, as well as something about a ritual to call the creature into our world."

        p_i "It's a bit much, to be honest. Was this even here before?"

        #fade out/fade in

        "This 'chase' is starting to get to me as the campus feels more and more surreal. Isolated, desolate and overrun with floodwater. I could swear things are blending together now, the scenery bleeding away like ink from a page."

        p_i "Where did that last cultist even go? They didn't just disappear!"

        "Unfortunately, I am quickly proven right as the cultist leaps out of what I assumed was shallow flood water. It's difficult to react as they tackle me to the ground."

        vc "Hey! Over here! I found the Archiever's companion!"

        "The startling bellow of the cultist draws the others in, racing into my vision past the curtain of rain."

        vc "What's the plan here? Do we still need them around for something?"

        "I don't like the sound of that question, and worse still, is the dagger under their raincoat I can see them reaching for. This will not end well for me."

        cc "Huh? I don't think so...? Wait! We should probably take this one alive! Just in case."

        p "Take? Alive? I don't like where this conversation is going, and I'm not going to stick around for the rest of it."

        "I reach into my pocket for something. Anything at all, really. Anything that can be used as a weapon!"

        "In a single moment of desperation, I swing my arm, splashing the face of the attacker with my chosen weapon as I feel a blade graze my shoulder."

        "Hearing a yelp in surprise, I push the cultist off of me, getting only a brief look before proceeding to run for my life. Ink? I guess Shiori must have left the bottle with me."

        p_i "This was a terrible plan. But I guess I know they aren't 'harmless' now."

        "While I can't sense the cultists giving further chase, I don't rest until I'm absolutely certain I've lost them."

        "Once I have, I take another opportunity to look at the book. Was this page there before? There are more scribbles about the cult, and a detailed diagram of the dagger I saw."

        p_i "This book… It isn't really writing itself… is it?"


    if followcats:

        "Despite the fact that the rain is constant, the local cat population has never been too keen on it. Of course that makes it difficult to find them, because the strays are never out in the open. I had picked something up to help lure them out but it was to no avail. So I begin my search looking through bushes, under awnings, and trees, any place a cat could stay dry, really."

        cat "Mroooooow~"

        "Just as I'm starting to feel stupid poking my face into hedges, I finally notice a cat up ahead. It walks along the ledge of a school by a window, just barely managing to avoid the falling rain as it hops to the next one."

        "I keep my steps light and follow at a distance as the cat leisurely makes its way over ledges, through shrubbery, and under floorboards until it reaches a destination. A gathering spot for strays like itself."

        "In reality, it was just a bench under a shady tree in the abandoned part of the campus. However it is relatively dry and I could see the sun overhead were it not for the cloud cover."

        "The place is crawling with cats, all clambering and pawing at the bench as if waiting for something. Or someone."

        p "I guess you were all hoping to find Shiori here, huh? Sorry, but she can't make it right now."

        "It is about then that a familiar sensation washes over me. Am I being watched? I look up and my eyes are immediately drawn to a peculiar flower growing near what looks like a food bowl. The flower inexplicably blinks. I blink. And then it vanishes.. Shaking my head, I walk over."

        p "Ha.The stress must be getting to me… I must be going crazy, seeing strange flowers and talking to cats."

        "The cats simply circle around warily, unsure if they can trust someone who isn't Shiori."

        p "Oh! I know!"

        "I remember a packet of tuna I had prepared for the occasion, and pour it into the bowl. I thought that it would take more to earn their trust, but no. I am instantly swarmed before I can finish pulling my hand back."

        "A few nips here and a couple of swipes there in the chaos but my hand seems none the worse for wear. And more importantly, one of the frenzying furballs seems to have left me with a gift. A folded up piece of notebook paper. Signed Shiori."

        p_i "Surely the cats didn't give me this on purpose, right?"

        "I unfurl the note and at first it seems like a bunch of random scribbles, but the more I look at them, the more familiar they seem. They remind me of the book Shiori left with me."

        p_i "Is this a cypher?"

        "I take a seat on the bench, the cats mildly protesting this as an act of sacrilege. Leave it to Shiori to find the perfect spot on campus for reading. The leaves of the tree are soaked through and provide little protection, but propping up my umbrella is an easy fix."

        p_i "So this is the book Shiori felt was so important...?"

        "Admittedly I had gotten curious and tried peeking at the book before, but it was mostly unintelligible scribbles until now. The cypher reveals an obtuse yet flowery prose full of vignettes and 'first hand accounts'. All of them seem to involve a cult and a 'creature beyond mind or matter' that they worship, known as the Void Wyrm."

        p_i "Is this what Shiori thinks that clique is about? Do they really believe in this thing?"

        "It reads like a sci-fi anthology with a large chunk of the pages being just blank. Still there is some consistency across all of the stories and the descriptions of the town itself are fairly spot on. It even mentions parts of the campus I've been to, and the cafe where I met Shiori."

        p "The details in this are impressive. Whoever wrote this must have been obsessed. Wait, if that's the case, maybe I can use this!"

        "Going back over the material, there are mentions of the cult having a base. If the clique is anything like this cult, then they may be holding Shiori in a similar location."

        "Picking myself back up from the bench, I head into town. The rain turns into a complete downpour as each drop pounds against the pavement harder and faster. Part of me wishes I had chosen a better day to play detective."

        "It is easy to get turned around on a day like this, visibility is low and places are blending together. Honestly the scenery is starting to look like it's bleeding away... like ink from a page..."

        p_i "This can't be right."

        "Shielding it with my umbrella like a cherished heirloom, I pull out the book and go through it again. And there it is. And there. And there. And there. 'bleeding away like ink from a page'."

        p_i "It's probably a coincidence. Or just something I picked up subconsciously. Yeah. That's it."

        "I close the book and refocus on my search. But I can't shake the feeling that things are eerily empty. Silent. Missing."

        "Everything in the book suggests that the cult would be somewhere old. Somewhere opulent. Somewhere that people don't look too closely at."

        "After a couple hours of walking around, 'appreciating the town's abundance of Victorian architecture', out of the corner of my eye, I start to see more of those flowers. For a moment, they blink and move like an old rubber hose animation before sinking into the earth without a trace."

        p "I'm starting to think these might be... No. That would be absurd. Unless…"

        "As I make my way over to investigate where I saw flowers, a manor across the street catches my eye. It's old, but not worn down, like it's been renovated a few times. It could easily be an upscale club or lodge of some sort. Or... Even a meeting place for a cult."

        p_i "There is only one way to tell if this is what I'm looking for."

        "I slow down and mask my footsteps as best I can, trying to find cover to obscure myself. The torrential downpour makes it much easier to go unnoticed, but that doesn't mean I should take my chances here."

        "It doesn't take long before my suspicions are confirmed. A good 20 minutes is all it takes for a couple of the raincoated cultists to walk up to the building in question. They give a brief rhythmic knock before they are welcomed in by another of their clique."

        p_i "This is it! This must be the place where they have Shiori! I can't believe I figured it out! But, now what?"

        "Frankly, I hadn't thought too hard about this part. They probably won't let me in to see Shiori if I ask nicely. If the book's contents are to be taken seriously, that might even get me stabbed. But I also can't hide out here for too long. They could notice me."

        p_i "Hmmm... A place this big has to have somewhere they aren't looking, right?"

        "I duck under the sightlines as I circle the property from a distance, while scouting for open windows, storm cellars, unguarded doors, or any vulnerability really. For a moment I feel like I'm 'casing the joint' for a big heist."

        "Not seeing many other ways in, I steel myself and steadily approach one of the doors. It's unlocked."

        p_i "That's convenient..."

        "The hinges creak as I pry the door open slowly, trying to keep the noise to a minimum. I manage to slip in and carefully close it behind me. Almost immediately lavish furnishings and the distant hymn of classical music shift the atmosphere from dreary to invitingly decadent." 

        "While there is no one in my immediate vicinity, I can hear the murmur of voices from every which way. There isn't much time, so I rummage through the room I made it into, grabbing journals, pamphlets, letters, and whatever small odds and ends might go unnoticed."

        p_i "My first B&E, mom would be *so* proud."

        "I can hear the makings of a conversation getting closer. I'm tempted to stay and listen as they mention 'the archiver'. But it's too big a risk, and my feet carry me away before I can give it serious thought."

        "I run away from the compound as fast as I can, never looking back until I really feel in the clear. I barge into a cafe that's still open. It feels somewhat like Halloween or Christmas as I scatter my 'haul' on the table."

        p "There better be something useful here after all of that."

        "Part of it is already soaked as I hadn't been as careful as I would have liked. That said, there's still enough for me to go through, and the more of it I read the more things fit together."

        p "Shit, they really are a cult."

        "It's all here, the raincoats, the Void Wyrm, the secret knocks and handshakes. There is even something written about Shiori here. I think. They keep referring to her as The Archiver, and it's written like they've been trying to get their hands on her for decades."

        p_i "She can't be that old. She literally can't be. ...These letters are, though."

        "My attention is drawn to the book Shiori gave me as serendipity compels me to open it. I wanted to compare notes but the comparison has been made for me already. All of the various details I found through my investigation are now filling pages of the book which were blank before."

        p "What is this? This can't be real..." 

    "It has been an overwhelming day to say the least. I feel like I barely made it out in one piece. The cult is a 'thing' and they mean business. There's just too much to ignore. Not to mention they definitely have Shiori. Yet I'm almost ashamed to say that my batteries are drained. It might be best to call it a night and regroup after getting some rest."

    menu:
        "Get some rest":
            p "I'm sure the world won't end if I get a night's rest..."
            $ getrest = true
            $ ending += 1
        "Push through exhaustion":
            p "This cult is dangerous, I can't leave that be!"
            $ exhaustion = True

    if getrest:

        "It is oddly quiet as I make my way back to the dorms. It's peaceful, even. As I drift off to sleep, however, I'm hounded by bizarre dreams of abstract concepts and choices I could have made. In the haze of it all, I find myself wondering: What if I had gone with Shiori? Would the cult still have her? Or would I just be locked away somewhere too?"

        "It isn't exactly a full eight hours, but I find myself waking restlessly around the crack of dawn. With a yawn I decide that for whatever sleep I'm lacking, coffee can make the difference. I rush right back out the door, hoping to pick some up at the cafe."

    if exhaustion:

        p_i "It's important to stay vigilant. I don't understand why this cult is doing any of what they are, but they have kidnapped at least one person already."

        "I start the night off meandering around town, taking notes of whatever cultists I spot and what they are doing. Most are just standing around or moving around in simple patterns. For the life of me, I can't figure out why though. But I at least have an idea of where they tend to go and when.

        This predictably leads me to the old manor they are operating out of. Realizing that the building across the street is empty, I force my way in and set myself up to keep watch. I take notes on the comings and goings of its raincoat occupants, but it's hard to make out any more than that. Furthermore, whenever I try to compare my notes with the book, it is already updated." 

        p "Frustratingly useful." 

        "By the crack of dawn I more or less have a list of every instance someone entered or left the building, as well as a vague idea of their numbers. There are more than I thought there would be."


        p_i "I think I'm going to need coffee for this."

        "Though the streets are still flooded, I end up stopping for coffee at a local cafe. At first I'm just surprised it is open at all, but when I lock eyes with the person behind the counter, I feel a piercing sense of dread. Is the barista with 'them'? I don't see a raincoat on them, but that doesn't mean anything. And what about the other customers? I can feel them looking at me. Staring. Do they know something? Are they plotting something?"

        "Before the situation can escalate any further, I leave money on the counter and sprint out the door. I can't take any more chances. I don't know who I can trust. Or if I can't trust anyone. I need to take action. I need to figure out what they are planning and stop it."

    if getrest:

        "I take a moment to clear my head. Action is one thing, but without a plan, it doesn't mean much does it?"

        p_i "Now that I think about it, the library might have more information on the cult."

        "I end up taking a more winding path, just in case someone really did follow me from the cafe. It's funny, I'm pretty sure I've been this way before but I can hardly recognize anything at all. I should have passed by a grocery store and a pharmacy by now. Yet there are hardly any buildings now."

        "As confusing and convoluted as the way back appears to be, I make it to the library just fine. Aside from the growing 'moat' around the building, everything looks as it should be. Somewhat of a relief all things considered."

        p_i "I've become rather fond of this place."

        "I trudge ahead and peek through the doors. I think the librarian at the front desk had a yellow raincoat last time. While I can see the coat still draped on the chair, it's hard to tell for sure if it's 'one of those' raincoats. And more importantly they are seemingly preoccupied with their phone, swinging it to and fro in the telltale dance of trying to get a signal."

        p_i "That should make this a bit easier."

        "While the front desk worker is distracted by the failings of modern technology, I sneak past them. Entering the library proper, I consider my options. If the cult has done anything like this before, there has got to be a record of it somewhere."

        p_i "...Unless they can cover such incidents up."

        "I let that intrusive thought sit for a moment before brushing it aside. I'm here to do research, not form conspiracy theories. Trying to ignore the sinking feeling in my gut, I make my way deeper into the aisles."

        "I mostly pick up old news articles and books on the town's history as well as a few books on conspiracies. Just to cover my bases! But once I have enough materials, I sequester myself in the same study room as before."

        p_i "I guess it really was the adventure of the second study, huh."

        "I chuckle, allowing myself a brief respite before manically going over everything I've collected thus far. It takes me a good few hours to piece everything together, and by the end of it, Shiori's book has several new pages that have started to resemble a conspiracy board. But more importantly, I have noticed a few things."

        "First of all, there are a lot of disappearances in this town. It traces back to its founding in the 1800s. Second is that symbol from the raincoats. I've found traces of it as well as other iconography of the Void Wyrm littered throughout odd pictures." 

        "Finally, there is the weather. I can't figure out why but rainfall has been increasing consistently every 20 years or so. If these records are right, this place should have been a desert when it was founded."

        p "Shiori was really onto something big, wasn't she?"

        "No sooner than those words escape my lips do I hear shifting behind me. A rustling at the door. Someone is here! Has the cult tracked me down? Figured me out? I grab what I can and prepare to bolt, but study room 2 has only one way in and out."

        qs "Hello? Is someone there?"

        "The door creaks open and I am met with a plain and unassuming face with disarming features. Seemingly another student. Seemingly harmless. *Seemingly.* Who would be here in this weather? Plus there should be plenty of other study rooms. Why this one, why mine?!"

        s "Oh. Sorry. Are you using this room?"

        "Our eyes meet as I try to discern their intentions. However, their eyes drift towards the desk, still partially cluttered with research I had undertaken. When their eyes finally move towards Shiori's book, I wind up my arm and deliver a uniquely solid blow for someone of my athleticism. I don't waste time either, and I leap over their limp form, sprinting for the nearest exit."

    if exhausted:

        "Since the only way to find out what they are doing is up close and personal, I double back towards the cult's headquarters. The streets are fairly empty on the way there. Everything feels empty, in fact. And while I'm not too familiar with this part of town, I feel like something is missing from it. Not that I would be able to place what is where."

        p_i "I have a cult to worry about, who cares if a couple things have moved around?"

        "With a better idea of when and where to expect cultists, it's a simple enough task to find a window that is relatively safe to enter from. And in an old place like this, it's actually pretty simple to pop the screen out of its frame and open it up. The hard part is of course getting around the building undetected. Hiding behind cracked doors, furniture or random objects. Anything to slip by while no one is looking."

        p_i "Everyone in here seems busy, maybe they are up to something?"

        "While it is tedious to maneuver myself around, the cultists being distracted works to my advantage. I make my way deeper into the compound and find an entrance to the basement."

        p_i "If movies have taught me anything about this sort of thing it's that everything they don't want you to see happens in the basement."

        "As I descend the stairs, I am greeted by the sounds of running water and the low hum of chanting. Not in any language I know but nonetheless familiar. I don't think they have noticed me yet, but I keep myself nimble just in case. It is nearly in vain as I spot a group of cultists in the room when I reach the bottom of the steps-I froze up.. It is only due to the cultists' focus on the ritual that I continue to go unnoticed."

        "What I see in this room is beyond description. I had come expecting blood and bones, arcane symbols, or prayers to an uncaring god. But this is *different*. The basement is flooded, but the water is not pouring in from outside. Instead, it is trickling up the walls. It's all so clear. So clean. So empty. All swirling out from a circle at the center of everything. I watch as the cultists take one of their own and submerge them. And nothing comes up. Not a soul, not a person, not even a body. Nothing ever comes up."

        "They begin turning towards my direction but I am already on my way up the stairs. Did they see me? I don't know. I don't care. I run. I just keep running. I keep going until I'm back out the window and down the street."

        p_i "What did I just witness? Did they melt a body? Was it some kind of magic trick? Do I even want to know the answer?"

    "Not too far off, I spot another one of those 'unique' flowers. I have begun to associate them with Shiori for whatever reason. I begin walking towards it as it blinks at me in recognition. Or is it supposed to be a wink? It only has one eye. Much like the others, it sinks back into the ground, but this time another pops up in the distance. Realizing what these things are doing, I follow their lead. Behind me I can hear a ruckus, probably the consequences of my own actions, so I pick up my pace."

    p "Wherever you're leading me, please let it be safe…"

    "While the path twists and turns like that of a cat, sure enough, I am led away from the cultists, to a friendly bench at a bus stop. Was Shiori trying to tell me to leave town? Was this really her intention? Can I even know it's her?"

    p "Ah-"

    "I try to call out to the flower but it vanishes without a trace, leaving me alone with my thoughts. With nothing else to do, I pull out the book and begin poring over everything in hopes of figuring something out."

    "As far as I can tell, the cult has been around for about as long as the town has, performing rituals in secret and making people disappear. Every few decades they offer something to this 'Void Wyrm' to strengthen it. But they have always lacked something to unleash it upon our world. Something that only 'The Archiver' knows."

    p "That's why they were after Shiori! That's why, I'm hoping, she's still alive!"

    "But since they have Shiori, that means they are probably preparing the ritual to summon their god. This at least gives me an idea of where they will be. I pull myself up from the bench and start running. I try to pay it no mind as I charge right through empty street corners that I know had been home to convenience stores and pawnshops. My legs are killing me by the time I reach my destination."

    "I arrive at their compound and it feels… wrong. The torrential rain has more or less hit its peak, erupting into a furious storm, yet this place remains tranquil. It is awash with cultists moving things around, setting up chairs, booths and picnic blankets amongst the arcane sigils and ornate pillars."

    "In the distance I can even see a woman tied up, being submerged into an eerily pristine tank of water as the cultists around her chant and dance performatively."

    "Even with all the commotion, there are far too many cultists to just force my way through. And even more are still filing in. I need a plan."

    p_i "Let's see.. . If I could just get my hands on one of those raincoats, I might get far enough to find Shiori. Or maybe if the police get involved, I could find her in the chaos?"

    menu:
        "Get a new coat":
            p_i "It can't be that easy, right?"
            $ grabcoat = True
            $ ending += 1
        "Call the cops!":
            p_i "Just tell them something that would make them come here..."
            $ callpolice = True

    if grabcoat:

        "The plan is to catch one of them by surprise and steal their coat. However, hiding spots are at a premium. For the time being, I dive behind a stray crate, but that won't be an option for much longer."

        "My eyes soon lock onto a familiar face, The librarian from the front desk! I knew it! I knew they were part of the cult! And more importantly they seem just as carefree with their coat as before. Hanging it over a nearby folding chair instead of wearing it properly."

        p_i "Ok, while it's not the best plan, it's as good as any."

        "I don't have much of an opening here so I reach up from behind the crate and tap the librarian on the shoulder before moving to the opposite side. While they are distracted, I quickly relieve them of their raincoat and put it on before walking away."

        p_i "I probably don't have too long."

        "As if to prove my point, I begin to hear shouts of distress behind me, so I quicken my pace and enter the building. There are a good number of people gathered here, but most of them are out back preparing for the ritual. Just in case, I grab a small box of supplies lying around to look busy."

        "It's somewhat surprising how lively everything is here. There is music in the background, people drinking and celebrating. A couple of people even stop to open doors for me and my prop."

        p_i "Come to think of it… What if I just ask?"

        p "Excuse me, I'm supposed to put these outside the cells, but I'm a bit lost."

        hc "The cells? They are in the basement of course. It's down the hall and to your left."

    if callpolice:

        p_i "The police should be able to handle this."

        "Or at least that's what I tell myself. In all honesty I'm exhausted. Tired of playing detective and conspiracy theorist. I have enough evidence collected. All I need to do is get the police over here. So I pick up the phone and fidget about, until I get a signal. What would get the police over here quickly, though? I dial the number, consider my options, and wait for someone to pick up."

        o "Hello, 911, what's your emergency?"

        p "Ah, yes! I'd like to report a robbery in progress? Someone is using the storm as cover to rob the manor up on the hill!"

        #fade out/fade in

        "It wasn't my best plan, admittedly, but it is at least believable. All I had to do now was wait. The police will come in, they will see the cult's activities, and Shiori will be freed. That is how I assumed it would go. The police do in fact, show up, sirens blaring and everything. However, they step out of the vehicle wearing bright yellow raincoats."

        "My heart freezes and the moment slows to a crawl. I no longer have any idea of what I'm doing, but I have to run. Without thinking, I head right for the closest way into the building I can find. The window."

        "Jumping through a window isn't like in movies. It's always dangerous and could get you seriously injured. However, as I brace myself for the piercing sensation of glass striking my fleshy body, it instead clatters harmlessly against me and scatters across the floor."

        p_i "Ok, no time to think about that. I'm pretty sure the cops saw me."

        "The sound of footsteps behind me confirms my suspicion as I start running for all my legs are worth."


    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.0)