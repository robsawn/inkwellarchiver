label ch_12:
    show bg classroom with fade
    play music "audio/4 Lovecraftian/2B/1 Normal Life L.ogg" loop fadein 1.0

    "Looking outside from my seat, I continue to think about the rain. Well, the lack of it. I can't even remember the last time it wasn't raining. Instead, everything's turned hazy, making it difficult to see very far. I can see the building across the field, but that's about it."

    p_i "Mist, huh?"

    "There's still a bit of time before class starts. I let my gaze wander across the view outside. Several students huddle together, moving in close-knit groups, chatting and seemingly not bothered by the lack of rain; others, moving alone, stay close to the buildings, the familiar landmarks offering some small comfort in the strange mist."

    stop music fadeout 1.0
    play music "audio/4 Lovecraftian/2B/2 Getting Stalked By Hooded Figures L.ogg" loop fadein 0.5

    show cultist at center

    "I catch myself spacing out and staring at a person standing outside. I blink and finally notice the bright yellow raincoat they're wearing. It seems familiar, but I can't quite put my finger on where I've seen it before. As I watch, I notice that they're not moving, and are just standing there."

    p_i "Interesting fashion choice..."

    s "Hey, mind if I sit here?" with vpunch

    "I jump a little and I look over toward the voice. Seeing my classmate, I just nod and look back out the window."

    p "What the...?"

    image cultist2 = "images/lovecraft/cultist.png"
    show cultist2 at right_third

    "I notice a second person in a yellow coat, this time in between the buildings."

    hide cultist
    hide cultist2

    "I hear a scraping from my side as my classmate leans forward to look out the window as well. I lean back in my chair and stretch, my back popping as it arches."

    s "Oh, I've been seeing more of those yellow coats lately. Tacky, right?"

    p "Oh, is it some fashion thing, then?"

    s "I'm not sure. Maybe?"

    "I shrug and look back outside, but those two are gone. Glancing around, I can't see any trace of them."

    p_i "Guess they left."

    s "You didn't notice? They've been popping up more and more lately."

    p "I guess not? I don't really pay attention to that kind of thing."

    s "That's fair, I guess. We do have the report due soon."

    "The professor walks in, and the conversations quiet down throughout the room as they get ready. As they move to their podium, the conversations stop completely and the professor starts."

    show bg college with fade

    "Class is finally over. No matter how hard I tried to listen to the lecture, my eyes kept drooping. Makes sense seeing as how I couldn't sleep at all." 

    "I tried getting up and working on the report, and the books Shiori helped me find were really useful, but I couldn't get anything done. No rest and wasted effort."

    "Yawning, I head to my next class in another building. On exiting, I notice the mist is heavier, like a fog. It's clinging to me and weighing me down. Feeling isolated and exposed, I carefully walk ahead, doing my best to stay on the path."

    show cultist at right_third with dissolve_slow

    "As I continue moving, a figure emerges from the mist, standing to the side. Closing in, I see that it's someone in a yellow raincoat. Facing me."

    hide cultist

    "I don't have time to deal with this new fad, or these weirdos, or whatever. I need to get to class."

    "Thankfully, the rest of my day is as normal as can be."

    "The only thing that was strange was my classmate who usually sits next to me was absent for the day..."

    p_i "Didn't they have perfect attendance?"

    show bg classroom with fade

    "I go into class the next day, but the talkative classmate who usually sits next to me isn't here yet."

    "By now there should be people filing in, but the room is still empty. I pull out my phone to check the time."

    p_i "Tch. 1%%." 

    p_i "Forgot to charge it, I guess."

    "I finally actually check the time: 3:45 PM... Class was supposed to start fifteen minutes ago. And the phone shuts down, the battery depleted."

    p "I guess I'll leave? No one's here, after all."

    "Standing up, I look around again and the room is still empty. Suddenly, my back twitches as a chill runs down my spine. After it passes, I shoulder my bag and start heading home."

    p "Maybe I'll stop by the library to try to get some of the report done."

    show bg hallway

    "Walking down the eerily empty halls, I glance out the window and see a familiar head of black and white hair."

    show shiori neutral

    p "Isn't that...?"

    p_i "I should say hi, it'll be nice to walk with someone anyway."

    hide shiori neutral

    "I push open the door to exit the building, picking up the pace."

    show cultist

    p "Oh, shi-! Sorry!"

    "I barely duck around the person. I must be more excited to talk to Shiori, or anyone for that matter, than I thought." 

    hide cultist

    "Not even waiting for a reply, I continue toward Shiori. But, rounding the corner to where she should be, she's gone."

    p "Where'd she go? Wasn't she right here?"

    show shiori smile:
        zoom 2.0 xalign 0.5 
    with dissolve_fast

    "Shrugging, I turn around and my vision is filled with a pair of golden eyes."

    shi "Boo!" with vpunch

    hide shiori smile

    show shiori happy at center

    stop music fadeout 0.5
    play music "audio/4 Lovecraftian/2B/3 Study Room Conversation With Shiori L.ogg" loop fadein 0.5

    "My heels leave the ground as I jump, my heart thumping in my chest, a low drumbeat to underscore my surprise."

    p "Jeez... You scared me!"

    show shiori satisfied
    play sound "audio/shiogiggles/Shio giggles 1.ogg"

    "Shiori giggles in reply and grins."

    shi "Gotcha!"

    "I smile at her, composing myself as the moment passes."

    p_i "I should be annoyed but I can't bring myself to be upset at her."

    p "You really did, good job."

    show shiori elated

    shi "Yay! Anyway, I'm surprised to see you here, usually all the classes in this building are in session now. Was yours canceled or something?"

    p "Honestly? Not sure. No one showed up, so I suppose so."

    show shiori frown

    "Shiori tilts her head and frowns a little."

    p "You wouldn't happen to have a friend in one of those classes who might know, would you?"

    show shiori neutral

    shi "No, sorry. I don't get out much, so..."

    p "Ah, no, it's ok, I get it. I like staying in too."

    "As our chat drifts into a comfortable lull and we turn to walk down the path, I notice footsteps behind me. Looking back, I see a figure in the mist approaching. A few steps and a yellow jacket becomes more noticeable."

    show cultist at right_third 
    
    stop music
    play music "audio/4 Lovecraftian/2B/2 Getting Stalked By Hooded Figures L.ogg" loop fadein 0.5
    play ambient "audio/Ambient/1 Subtrack L.ogg" loop volume 0.25 fadein 0.5

    p_i "Oh, did they have a class canceled too?"

    show shiori stare 

    "I turn back toward Shiori. She's watching the person with a frown and narrowed eyes."

    p "What? Their class was probably canceled."

    hide cultist 
    play sound "audio/sfx/footsteps.ogg"

    "Shiori shakes her head and grabs my wrist, walking away at a quick pace. I nearly trip over my feet being pulled away so suddenly." with hpunch

    p "W-What? Where are we-"

    show shiori neutral

    shi "Just come on!" with hpunch

    "As Shiori pulls me along, I notice several people in the same yellow rain jackets peering through windows and doors."

    p "I guess it is popular, huh?"

    show shiori mad

    shi "What? No, it's not that, I mean, yes, but no! Just come on!"

    show bg librarynight with slideright

    "We approach the library, but we're entering a side entrance I've never used."

    show shiori neutral

    "Pulling me inside, Shiori closes the door behind us and continues dragging me along. Soon, we duck into one of the side rooms and she slams that door too, locking it with the deadbolt."

    p "What's going on? Why did you pull me like that? Why are we-"

    show shiori frown
    
    shi "... thought ... time..."

    "I only catch part of what she said as she shakes her head and moves to sit down."

    p "What?"

    show shiori wink

    shi "Oh, don't worry about it..." 

    "She pulls out the same book I saw the other day. Where did she even fit that?"

    show shiori sad

    shi "... Is what I'd like to say, but it seems like they're looking at you, too, now."

    p "Huh? What do you mean?"

    "Shiori sighs in response and looks at me apologetically."

    show shiori neutral

    shi "Well, where to start... Um... Hm. Now that I think about it, I don't really know much myself."

    p "Well, what do you know? Besides, I'm pretty sure that guy just had a canceled class and was heading somewhere else."

    show shiori surprised

    shi "Wait, what? That's it?"

    show shiori neutral

    "A look of confusion, shock, and guilt washes over her face for a moment, before passing the next."

    shi "Hm. Ok. Well, I know enough to know that there's a problem here."

    p "Uh, yeah, you just kind of pulled me with no explanation. It's not a big deal, I just don't know why..."

    shi "No, not that. I mean... Those people in the yellow coats? They're weird, right?"

    p "It's just a strange fad or something."

    shi "Not quite. I think this book has something to do with it."

    "She holds the book up for me to see."

    p "The book you've been reading?"

    show shiori neutral

    "Shiori nods."

    shi "Trying to, anyway."

    show shiori frown

    shi "I've seen the coat people gathering around seemingly random strangers, who then disappear pretty soon after. It's like they're looking for something."

    p "This is mostly a college town, Shiori. People come and go all the time. Sounds like a bunch of coincidences."

    show shiori mad

    shi "But everyone gathered had the same yellow raincoat!"

    "Shiori raises her voice as she continues, but clasps a hand over her mouth, as if to quiet herself."

    show shiori neutral

    shi "That doesn't strike you as weird?"

    p "People like to be trendy, so it's probably just a new style or something. Maybe from some show or game?"

    show shiori frown

    "Shiori sighs in apparent exasperation."

    p_i "I guess I shouldn't be so dismissive. I'll hear her out at least."

    p "Ok, let's say it isn't a fashion thing. What do you think it is?"

    shi "If I'm being honest, it seems kind of cult-y. It seems too coincidental to be anything good."

    p "Alright, so, are they following us? Do we need to do something about it?"

    shi "I see them a lot, but doing something about it... I'd like to."

    show shiori smile
    
    "Shiori watches me expectantly. That look. How can I say no?"

    p "Alright, so what do we do?"

    show shiori neutral

    "Shiori puts a finger to her chin in thought."

    shi "We could get them to back off? It'd give us a chance to maybe try to figure stuff out."

    p "Sure, we get them to back off, but how?"

    shi "I'll be ok, but..."

    "Shiori reaches into her coat and slowly withdraws a small ink bottle, setting it on the table."

    "It's a small bottle, the size of one of those cups used for taking cough medicine, but as I look at it, I see faint purple and gold hues swirling, catching the light."

    p "So... That looks interesting. What is it?"

    shi "Do you remember when I asked if you wanted to be a Novelite?"

    "It takes me a moment to rack through my head, but I do remember her asking me that on our first meeting as I was leaving."

    p "Yeah, and?"

    show shiori smile

    shi "Well, you'll need to be one. Let's say this is in- a juice. Juice. Admittedly, a bad-tasting juice. But you'll be ok, you'll be fine!"

    p "Seems like you were saying something else."

    shi "Nope! It's juice. Just juice. You'll be fine."

    "I look back at the small bottle and grab it. For something so minute, there's a surprising weight to it. It's much heavier than I expected. I hesitate for a moment, and then remove the cork."

    p "I just need to drink this?"

    show shiori elated

    "Shiori looks around for a moment, her eyes lighting up as she stands and walks over to one of the shelves."

    "She turns around, cup in hand."

    shi "Would this make it easier?"
    
    show shiori smile

    "Shiori smiles at me, setting the small tea cup on the table. There's no saucer, but it's weird enough that there's a random tea cup in here."

    p "Uh... I'll just use the bottle, at least it's clean. We have no idea how long that cup's been here, or who used it."

    show shiori frown

    shi "Aw, that's no fun. It's fiiiine." 

    show shiori serious

    "Shiori's expression shifts to a much more serious one."

    shi "Jokes aside, you should drink that."

    "I look at the bottle in my hand and take a deep breath."

    p "Like a shot of something. Got it."

    show shiori smile

    shi "I don't drink, but sure."

    "I bring the bottle to my lips, and immediately gag at the smell. It's like a mix of gasoline, rotting meat, and sewage."

    p "That smells... awful. Ok. Down the hatch."

    show shiori frown

    "Shiori eyes me warily, her body tensing. Our gazes lock, hers scrutinizing for the smallest change."

    "The 'juice' passes my lips. My tongue feels like it is on fire as the weird substance chunkily slides down my throat. I barely manage to suppress coughing it all back up. Slowly, the bottle empties into my mouth." 

    "The bottle falls to the floor as my grip loosens. My vision wavers, blurring and darkening around the edges. I have to lean on the table to keep myself upright. Shiori rushes over." with hpunch

    p "Wh... What was that... No way that juice was safe... What did you do?"

    show shiori smile

    "Shiori just smiles at me. Or at least it looks like she is. It's getting harder to tell as my vision fails me and I crumple onto a chair, but then fall sideways out of it onto the floor."

    "Shiori kneels and gently rests a hand on my shoulder."

    shi "It's not really safe, now that I think about it. But, you'll be ok. You'll get through this. I believe-"

    "Everything's fading. I can barely make out Shiori or her voice."

    "Except one last word."

    shi "-Novelite."

    stop sound fadeout 1.0
    stop music fadeout 1.0
    stop nature fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(1.0)
