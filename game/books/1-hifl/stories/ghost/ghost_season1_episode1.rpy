label ghost_season1_episode1:
    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday
    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show blackscreen at bg with dissolve
    show bg heroine_home_lights at bg
    show hiflmc vestlesscasual happy at centre
    with dissolve
    "Some nights just feel perfect."
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(I mean, my day sucked.)"
    "(What {i}didn't{/i} go wrong? I was late for work. My coworker put an honest-to-god \"kick me\" sign on my back, and I didn't notice for hours.)"
    show hiflmc vestlesscasual_cu sad_cu
    "(I had to make that hard choice between having gas in my truck, and having enough food in the house to feed two people.)"
    show hiflmc vestlesscasual_cu sarcastic_cu
    "(I'll be driving to work hungry tomorrow, I guess.)"
    show hiflmc vestlesscasual happy at right1
    show grace casual basic at left2
    "But right now, I'm curled up on the couch with my sister, watching one of my favorite documentaries."
    show grace casual sad
    "She didn't even poke fun when I told her it was called {i}Ghosts without Borders{/i}, and I could tell she really wanted to."
    show grace casual confused at left2
    gr "So, wait, I'm confused- is this guy saying he's literally possessed? Like, the ghost is talking right now?"
    hide grace
    show hiflmc vestlesscasual_cu basic_cu at hiflmc_cu
    "(The effects are honestly really impressive, even if I also have doubts about the possession thing.)"
    show grace casual basic at left2
    show hiflmc vestlesscasual sarcastic at right1
    ghostmc "That's what he's saying, but in a few minutes he kinda forgets about it and stops doing the spooky voice."
    show grace casual sad 
    gr "Yeah, it sounds like it really hurts his throat."
    show grace casual basic
    gr "How many times have you watched this, again?"
    hide grace
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(...I refuse to answer that question.)"
    hide hiflmc
    play sound knocking
    "And it seems like I won't have to, because at that moment, there's a polite knocking at the front door."
    show hiflmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(At this hour?)"
    hide hiflmc
    show grace casual confused
    gr "At this hour? Who the heck...?"
    show grace casual confused at left2
    show hiflmc vestlesscasual basic at right1
    ghostmc "No idea."
    show hiflmc vestlesscasual basic at slowright2
    "I extricate myself from Grace- she'd been leaning on my shoulder, slowly nodding off like usual- and stand up."
    show hiflmc vestlesscasual at right2
    show grace casual basic
    gr "Wait."
    show grace casual sad
    gr "You're not just gonna open the door, right? You need to check first."
    show hiflmc vestlesscasual surprised
    ghostmc "I know!"
    show hiflmc vestlesscasual sarcastic
    ghostmc "I swear, you do something {i}once.{/i}"
    show grace casual angry
    gr "One time is too many times to let a raccoon in!"
    hide grace
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(Who knew the little guys could knock?)"
    show hiflmc vestlesscasual basic at right2
    show grace casual basic at left2
    ghostmc "I'll be careful."
    hide hiflmc
    hide grace
    "I walk over to the front window and, as promised, part the curtains to peer through to the porch."
    show bg mc_house_ext_night at bg with dissolve
    "It's dark out, of course, but I can still tell there's no raccoons by the door. In fact, nobody's by the door."
    show bg heroine_home_lights
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(Huh?)"
    hide hiflmc
    show bg mc_house_ext_night_light at bg
    "I flick on the porch light, and see..."
    show bg heroine_home_lights
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(Still nothing.)"
    show hiflmc vestlesscasual basic at right2
    show grace casual basic at left3
    ghostmc "Nobody's there."
    show grace casual sad
    gr "Ding-dong ditch?"
    show hiflmc vestlesscasual sarcastic
    ghostmc "Guess so."
    show hiflmc vestlesscasual surprised
    ghostmc "Actually..."
    hide hiflmc
    hide grace
    show bg mc_house_ext_night_light at bg with dissolve
    "On second glance, though, I notice that the porch isn't entirely empty."
    "Set right by the stairs, just barely out of reach of the door, is a plain white envelope."
    show bg heroine_home_lights
    show hiflmc vestlesscasual sarcastic at centre
    ghostmc "They just left a letter and bolted."
    show hiflmc vestlesscasual sarcastic at right2
    show grace casual confused at left3
    gr "A letter?"
    show grace casual basic
    gr "Oh, maybe it was Ernie?"
    show hiflmc vestlesscasual surprised
    ghostmc "The mailman? It's like nine o'clock."
    gr "Mm, he's stopped by late once or twice with packages that didn't make it to us."
    show grace casual happy
    gr "He lives around here, I think. He's nice."
    show hiflmc vestlesscasual sarcastic
    ghostmc "So he dropped the letter on the porch and, what, ran for it? We have a mailbox."
    hide grace
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(Which he'd know.)"
    "(As the mailman.)"
    show hiflmc vestlesscasual basic at right2
    show grace casual sad at left3
    gr "...Yeah, that is a little weird."
    hide grace
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(Incredibly weird. The kind of weird you might end up hearing about on a true crime podcast.)"
    hide hiflmc
    "I'm thinking about just waiting until morning to go outside and learn the mysteries of the envelope, when:"
    show grace casual basic
    $renpy.sound.play("audio/sfx/general/a.mp3", loop=True)
    gr "Oh, wow, listen to the rain."
    hide grace
    "The sky chooses that precise moment to open up, heavy raindrops beating a drum solo on the windows."
    show hiflmc vestlesscasual_cu angry_cu at hiflmc_cu
    stop sound
    "(Well, that's incredible timing. The stupid letter won't even be recognisable as paper by morning.)"
    show hiflmc vestlesscasual_cu sarcastic_cu
    "(I probably can't afford to just let it get washed away- if it's a bill, I need to deal with it sooner rather than later.)"
    show hiflmc vestlesscasual_cu sad_cu
    "(It's hard enough to save up for Grace's college fund without adding late fees into the mix.)"
    show hiflmc vestlesscasual_cu angry_cu
    "(This! This is why we have mailboxes, Ernie!)"
    hide hiflmc
    show bg mc_house_ext_night_light at bg
    show rain
    $renpy.sound.play("audio/sfx/general/a.mp3", loop=True)
    "I wrench open the door, and take a quick look around to make sure the coast is clear- of raccoons and otherwise."
    show hiflmc vestlesscasual_cu basic_cu
    "(Nobody's there.)"
    hide hiflmc
    "I step into the night air, and..."
    hide rain with dissolve
    show bg mc_house_ext_day at bg with dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0
    pause(2)
    play music litegetitdone
    show hiflmc bowling_cu basic_cu at hiflmc_cu with dissolve
    ghostmc "...?"
    "(What was I...?)"
    show hiflmc bowling_cu surprised_cu
    "(Wait, no, what time is it?)"
    show hiflmc bowling angry at centre
    "I look up, squinting right into the judgemental glare of the morning sun."
    show hiflmc bowling sad
    "The very {i}late{/i} morning sun."
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Well, crap.)"
    show hiflmc bowling_cu sarcastic_cu
    "(I've been late for work before, but this is honestly impressive.)"
    show hiflmc bowling_cu sarcastic_cu
    "(Considering that I was late yesterday too, I'm probably about to lose my employee of the month position.)"
    "(Assuming Razi doesn't just fire me.)"
    hide hiflmc
    show bg main_day at bg with dissolve
    "By the time I arrive in town, Havenfall's main street is about as busy as it ever gets."
    show girl1 casual basic at left3
    show boy1 casual basic at right3
    "Which is to say, I can see two whole people as I cross the street to the bowling alley, and they're just coming out of it."
    hide girl1
    hide boy1
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(There's really only two destinations in Havenfall: The bowling alley, and Luce's diner.)"
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(If you're in town, you're either walking between them, or going home.)"
    hide hiflmc
    show girl1 casual basic at left3
    show boy1 casual basic at right3
    "The teens are deep in conversation as I pass them by, so much so they don't make the slightest move to get out of my way."
    $sidecharone = "Loud Girl"
    $sidechartwo = "Quiet Boy"
    sid1 "...told you it was a big deal. That makes {i}three{/i}, now!"
    sid2 "Eh, come on. I still think they just ran off to Indy."
    show girl1 casual angry
    sid1 "No, that's such bullshit! Maybe your shitty friends did, but Naomi wouldn't just leave me like that!"
    hide girl1
    hide boy1
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(...)"
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(If there's kids missing, I hope they {i}did{/i} just run off to the city. Just the thought of Grace up and vanishing one day is...)"
    show hiflmc bowling_cu surprised_cu
    "(...)"
    "(Why do I feel like I'm forgetting something?)"
    hide hiflmc
    "I shrug it off, then push my way into the bowling alley..."
    show bg bowling at bg with dissolve
    stop music fadeout 1
    play music hifleveryday
    show hiflmc bowling surprised at right3
    show tamara casual basic at left2 behind hiflmc
    "...where I immediately walk straight into a complete stranger."
    ghostmc "Oh! Sorry, my bad!"
    $sidecharone = "Cool Jacket"
    hide hiflmc
    show tamara casual basic at centre
    sid1 "..."
    "The young woman's eyes are glazed over, her mouth set in a bored, flat line."
    "Far from being startled, she doesn't even meet my gaze as she drifts past."
    hide tamara
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Well. Okay then. Physical AND social crisis averted.)"
    hide hiflmc
    "I'm about to head to the bar when the woman speaks up."
    sid1 "Ugh, again?"
    show bg bowling_arcade at bg
    show tamara casual sad at centre
    with dissolve
    "I turn to see her leaning over the old {i}Space Mechanoids{/i} arcade cabinet."
    show tamara casual angry  at centre
    "Rather than a handful of quarters, though, she's holding a familiar spray bottle and spritzing the crap out of the controls."
    sid1 "Every day. Every day with the chocolate. Gonna kill that little shit."
    hide tamara
    show bg bowling
    show hiflmc bowling surprised at centre
    "(Normally seeing someone else clean the arcade cabinets means I'm having a great day, because JD is doing their job for once.)"
    "(Watching a complete stranger do it is a little unsettling.)"
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Wait, did I {i}actually{/i} get fired?)"
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(And then... replaced on the same day?)"
    hide hiflmc
    "That seems unlikely, but still I scurry on over to the bar, willing myself out of an anxiety spiral."
    show razi casual basic at centre
    "As expected, Razi's exactly where he should be, behind the bar and doing the magic he does with a rag to keep the glasses sparkling clean."
    show razi casual basic at left3
    show jd casual smirk at right3
    "JD is by the bar, too- exactly where they {i}shouldn't{/i} be, since they're supposed to be cleaning the bathrooms around now."
    show razi casual sad at left3
    show jd casual happy at right3
    "Neither of them see me approach, because JD is enthusiastically regaling Razi with a story that has the man's face set in a wince."
    show jd casual smirk at right3
    jd "And you wanna know the best part?"
    ra "...I really don't think I do, and yet I can't help myself. What's the best part?"
    show jd casual happy at right3
    jd "She still. Hasn't. Found it."
    "This is apparently a punchline, because JD slaps the bar to punctuate every word, before breaking off in a laugh."
    hide razi
    hide jd
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(Sounds like they pulled another prank.)"
    hide hiflmc
    show jd casual happy at right3
    show razi casual angry at left3
    "Based on Razi's scowl- and the way he can't quite keep his mouth from turning up at the corners- it was a good one."
    hide jd
    hide razi
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Razi can't be too mad at me if he's joking around with JD in the middle of the lunch rush.)"
    "(Right?)"
    show jd casual happy at centre behind hiflmc
    show hiflmc bowling sad at right2
    #show hiflmc bowling sad at slowright2
    show razi casual basic at left5
    "I ease myself onto the stool next to JD, and school my face into the most penitent wince it can muster."
    show hiflmc bowling sad at right2
    ghostmc "Hi, Razi..."
    show razi casual happy at left5
    show jd casual angry at centre
    "Razi turns his dazzling customer service smile my way, as JD whips their head around to... glare at me?"
    hide razi
    show hiflmc bowling surprised at right1
    show jd casual angry at left1
    jd "Hey, buddy, think you could sit any closer? Bar's empty."
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Uh?)"
    "(I've heard JD take that tone with pushy customers, but never with me- where's this coming from?)"
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(Still, if they want me to move, then I'll move.)"
    show hiflmc bowling sad at slowright3
    show jd casual angry at left2 behind hiflmc
    pause 1
    "I quickly shuffle over to the stool next to me, trying- and possibly failing- to keep the hurt from showing on my face."
    show hiflmc bowling basic at right3
    ghostmc "Yeah, uh- sorry."
    ghostmc "Anyway, Razi-"
    hide jd
    show razi casual surprised at centre
    hide hiflmc
    "I cut myself off when I notice the look on Razi's face, that radiant smile fading by degrees as his eyes blow open in naked astonishment."
    hide razi
    show jd casual surprised at centre
    jd "What the...?"
    "JD's face is doing something very similar, irritation giving way to shock as they stare at me agape."
    show hiflmc bowling sad
    hide jd
    "I'm... not sure what to make of any of that, so I just self-consciously smooth down my hair."
    hide jd
    hide razi
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(How bad does bedhead have to be to get this kind of reaction?)"
    show hiflmc bowling sarcastic at centre
    ghostmc "Hello to you, too?"
    show hiflmc bowling sad at right4
    show jd casual surprised at centre
    show razi casual surprised at left5
    ghostmc "Hey, listen, Razi- I'm sorry I'm so late. I should have called, but I'm honestly a mess this morning. Let me just-"
    show jd casual angry at centre
    jd "No."
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    hide razi
    "(Uh...?!)"
    hide hiflmc
    show jd casual angry at centre
    jd "Uh-uh. No thank you. Not cool."
    show jd casual angry at right3
    show razi casual surprised at left3
    jd "What the fuck am I looking at, Razi, and how do I make it stop?"
    "When Razi doesn't answer immediately, JD rounds on him."
    jd "Seriously, what? Illusion? Echo?"
    show jd casual surprised
    jd "Could just be an echo, right? We're right on top of the leylines, and she- she was here like every day."
    show razi casual basic
    "Razi shakes his head, still looking like he needs a good reboot."
    hide razi
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(I can relate!)"
    "(Is this the start of another bit?)"
    show hiflmc bowling_cu sarcastic_cu
    "(I'm remembering the time JD spun an emotional story about a medical condition to explain why I had to give them my lunch.)"
    "(Turns out that there aren't any conditions that mozzarella sticks can help, other than the devastating 'skipped breakfast' disease.)"
    hide hiflmc
    show jd casual basic at right3
    show razi casual sad at left3
    ra "I- no, I don't think so, Jordan."
    show jd casual angry at right3
    jd "Then {i}what?{/i}"
    show jd casual at left3
    hide razi
    show hiflmc bowling sarcastic at right3
    ghostmc "What's a 'ley-'"
    hide razi
    show jd casual at left3
    show hiflmc bowling surprised at right3
    play music suspense
    jd "Stop. Talking."
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(...)"
    show hiflmc bowling_cu angry_cu
    "(Excuse me?)"
    show hiflmc bowling angry at right3
    show jd casual angry at left3
    ghostmc "Okay, no, what is your problem, today? Have I upset you, somehow?"
    show jd casual happy
    "JD laughs bitterly."
    show jd casual angry
    jd "Upset me? Oh, you're definitely getting there."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    hide jd
    "(I take it back: I've {i}never{/i} heard JD talk like this.)"
    "(They don't just sound pissed off, like when the Sheriff grills them about doing burnouts at 3 AM.)"
    show jd casual angry at centre
    hide hiflmc
    "They're blinking too quickly, all of a sudden, and their voice is coming out strained through clenched teeth." 
    hide jd
    hide hiflmc
    "I'm not the only one who hears the difference, either."
    hide jd
    hide hiflmc
    show bg bowling_arcade
    show tamara casual sad at centre
    with dissolve
    "I notice more than a few heads turn our way, including that of the woman over by the arcade machine, still dutifully fighting the chocolate stains."
    show bg bowling
    hide tamara
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    hide jd
    "(Great. If she does actually work here now, her first impression of me is gonna be 'that crazy lady who pissed JD off'.)"
    hide hiflmc
    show razi casual angry at centre
    ra "Jordan. Stop."
    show razi casual angry at left3
    show jd casual angry at right3
    "There's a tense standoff, JD and Razi glaring at each other as they communicate... {i}something{/i}, with only narrowed eyes and minute gestures."
    hide razi
    hide jd
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(I sure wish somebody would communicate with me right about now. I have never been this confused in my life.)"
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(The last time I saw JD, they were still having a little giggle fit over the kick-me sign on my back.)"
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(What happened between then and now that made them this angry with me?)"
    hide hiflmc
    show razi casual sad at centre
    "Twice, Razi glances at me and reaches across the bar as if to touch my arm- but both times he quickly retracts it before making contact."
    show razi casual happy
    stop music fadeout 0.5
    pause 0.5
    play music hifleveryday fadein 0.5
    show razi casual happy at centre
    "Finally, he breaks the silence with a shaky, unconvincing little chuckle. The smile returns in full force, even if it doesn't quite reach his eyes."
    ra "Alright, alright. You... you win, [genericfn]."
    hide razi
    show jd casual angry at centre
    "JD scoffs in disgust, for some reason. I do my best to ignore them."
    show hiflmc bowling surprised at right3
    hide jd
    show razi casual happy at left3
    ghostmc "I do?"
    "Razi reaches behind the bar, and pulls out a trio of glasses that clink together noisily between his trembling fingers."
    ra "Absolutely."
    show razi casual smirk
    ra "Sorry, Jordan- I guess [genericfn] saw right through our little prank. Let me make it up to you by treating you both to a drink."
    ghostmc "It's- it's noon."
    hide razi
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Also, what prank?)"
    hide hiflmc
    show razi casual happy at centre
    ra "A non-alcoholic drink, then."
    "I hear JD mutter 'It better not be' under their breath as Razi rummages under the bar, finally pulling out a fancy red bottle."
    "He pours a generous amount of amber liquid into each glass, and pushes one my way."
    show razi casual basic at centre
    "Then, he patiently waits for JD to place their glass back down, and refills it."
    show razi casual basic at left3
    show jd casual angry at right3
    jd "What, you wanna toast or something?"
    show razi casual angry at left3
    ra "That's the plan, yes. Go along with it."
    show hiflmc bowling surprised at right3
    hide jd
    ghostmc "Toast to what?"
    hide hiflmc
    show razi casual basic at centre
    "Razi raises his own glass, tilting it just barely my way."
    ra "To my..."
    show razi casual sad
    "He hesitates, and has to swallow thickly before continuing."
    show razi casual happy
    ra "My employee of the month!"
    hide razi
    show jd casual basic
    "Despite all of the grumbling they've been doing, JD raises their glass to join Razi's."
    show jd casual smirk
    jd "Yeah. To [genericfn]."
    hide jd
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(You know, I think I have dreams like this, sometimes?)"
    "(Like when I'm laid out on the couch, half delirious with a fever.)"
    show hiflmc bowling_cu happy_cu
    "(Screw it. I don't really get it, but I'll drink to me any day.)"
    show hiflmc bowling happy at centre
    "I take my own glass, and lift it up to clink against the others."
    "..."
    "I take my own glass, and I lift it..."
    show hiflmc bowling basic
    "...?"
    "I pick up. My own glass."
    show hiflmc bowling angry
    "I pick. Up. The damn. Glass."
    show hiflmc bowling sad
    ghostmc "I- I don't..."
    hide hiflmc
    "My hand is closed around the glass, but no matter how hard I tug, or push, or shake, it doesn't budge."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(I'm not even moving it enough to make ripples in the drink!)"
    show hiflmc bowling surprised at centre
    ghostmc "Razi, did you-"
    show hiflmc bowling sarcastic
    ghostmc "Did you really just glue this thing to your bar?"
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(At some point, you just have to admire the dedication. This one really got me.)"
    show hiflmc bowling sarcastic at centre
    ghostmc "Very funny. I hope you have a way to get it off, though, because it is really on there."
    show hiflmc bowling angry at centre
    "I try again, fruitlessly, to pull the glass free, but it's completely locked in place."
    show hiflmc bowling happy at centre
    ghostmc "So, do I actually get a drink? Or is this my punishment for being late?"
    show hiflmc bowling sarcastic at centre
    ghostmc "Because yeah, I guess that's fair."
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Aaaand they're both staring at me again.)"
    show razi casual surprised at left5
    show jd casual surprised at centre
    show hiflmc bowling basic at right4
    jd "..."
    show jd casual basic
    jd "Tulpa."
    hide razi
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Huh?)"
    show razi casual basic at left3
    show jd casual basic at right3
    hide hiflmc
    ra "No. Tulpas are corporeal."
    show razi casual sad at left3
    ra "And significantly less polite."
    show jd casual surprised
    jd "So, like I said, an echo. Or an-"
    show razi casual angry
    ra "Echoes aren't conversationalists, and as for illusions- please don't insult me a second time."
    show razi casual sad
    ra "Why are you fighting this so hard, Jordan?"
    show jd casual angry
    jd "Because it's been too {i}long{/i}, Razi! You think I don't want it to be her?"
    jd "But ghosts don't just like... quietly vibe, or whatever! Where has she been?"
    hide jd
    hide razi
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Ghosts? What are they-)"
    show hiflmc bowling_cu sarcastic_cu
    "(Oh.)"
    show hiflmc bowling sarcastic at centre
    ghostmc "You've been talking to Grace."
    hide hiflmc
    show jd casual surprised at centre
    "That gets JD's attention."
    jd "What about Grace?"
    show jd casual surprised at left3
    show hiflmc bowling basic at right3
    ghostmc "Well, I did make her watch an old Arthur Clintock documentary, last night."
    hide jd
    show razi casual sad at left3
    ra "...{i}Ghosts Without Borders{/i}?"
    show hiflmc bowling surprised
    ghostmc "Oh, wow, you know it?"
    ra "I'm... familiar."
    hide razi
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(You think you know a person!)"
    show hiflmc bowling sarcastic at centre
    ghostmc "And now JD's pretending I'm a ghost."
    show hiflmc bowling sarcastic at right3
    show jd casual surprised at left3
    jd "I am doing literally the opposite of that!"
    hide jd
    show razi casual smirk at left3
    ra "Pretending [genericfn] isn't a ghost."
    show hiflmc bowling surprised
    ghostmc "Razi, I can't believe you're in on this one."
    show hiflmc bowling sarcastic
    ghostmc "How many layers does the joke even have? Who's the poor girl you've got cleaning {i}Mechanoids{/i}?"
    show razi casual sad
    ra "[genericfn]..."
    hide hiflmc
    show jd casual sad at right3
    jd "..."
    show jd casual angry
    jd "Shit."
    show jd casual sad at left3
    hide razi
    show hiflmc bowling surprised at right3
    jd "It's really you, huh?"
    show hiflmc bowling sarcastic
    ghostmc "I'd like to think so."
    show hiflmc bowling sad
    ghostmc "Look, joke aside, you seemed pretty genuinely mad. I'm trying to remember what I could have done, but-"
    show jd casual angry
    jd "No, you didn't do anything. I was being a dumbass."
    show jd casual sad
    jd "It's just... really sucked not having you around, you know?"
    show hiflmc bowling sarcastic
    ghostmc "It was like three hours, JD, and you apparently got someone to fill in for me anyway."
    show jd casual angry
    jd "I really didn't."
    hide hiflmc
    show tamara casual sad at right7
    show tamara at slowright3
    "As if to catch them out in a lie, the new hire herself wanders over to the bar, face creased into a worried frown."
    $sidecharone = "New Coworker?"
    show tamara at right3
    sid1 "Hey, JD. Everything okay?"
    show jd casual surprised at left3
    jd "Y-yeah. Yeah! No, everything's cool, Tam."
    jd "No need to come over or anything!"
    show jd casual angry
    jd "In fact definitely don't. Go clean my room."
    show tamara casual angry
    $sidecharone = "Tam"
    sid1 "Only reason I'd go into your room is to steal back the fifty you owe me, you little-"
    hide tamara
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "({i}Tam{/i}?)"
    "(I've never seen her before, which is... weird, honestly, considering how small Havenfall is.)"
    show hiflmc bowling_cu sarcastic_cu
    "(It's not like we get a lot of people from out of town, either.)"
    show hiflmc bowling happy at centre
    show tamara casual basic at right4
    ghostmc "Uh, hey, there! Sorry about the noise, earlier, I think JD was just-"
    show tamara casual basic at slowright2
    "Just like before, Tam doesn't so much as look at me as she approaches."
    show tamara at right2
    show hiflmc bowling basic
    show jd casual surprised at left2
    show razi casual sad at left5 behind jd
    "Her eyes flitter between JD and Razi, skipping right past me like I'm just any other part of the environment."
    show tamara casual sad
    sid1 "Anyway, you sure? You seemed super upset. Rough phone call?"
    show tamara casual happy
    sid1 "Was it another ex? Follow up question: Are they cute?"
    hide jd
    hide razi
    show tamara casual happy at slowright1
    show hiflmc bowling angry at centre
    "Tam walks right up to my stool, and I feel my hackles go up as my personal bubble is invaded."
    ghostmc "Hey, do you-"
    show hiflmc bowling surprised
    "She then tries to sit down on {i}my lap{/i}!"
    ghostmc "W-what!? Hey, get-"
    show tamara casual happy at slowcentre
    hide hiflmc with dissolve
    play music bigbad fadein 0.5
    "A shiver runs down the length of my spine as Tam slips straight through my body."
    show bg insideperson
    hide tamara
    $renpy.sound.play("audio/sfx/general/heartbeat1.wav", loop=True)
    "She's bigger than me, and once she's settled in place- in {i}my{/i} place- my vision goes red."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(...What? Where am I?)"
    hide hiflmc
    "It's dark, and so loud I can barely think."
    "I can't turn my neck, can't find the source of the noise."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Is that my {i}heartbeat{/i}!?)"
    hide hiflmc
    "There's another sound, too- or more like vibrations. A buzzing in my ear that I can just barely parse when I focus on it."
    sid1 "Uh... What, is there something on my face?"
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(I can still hear Tam talking!)"
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(But... where is she? I can't tell where her voice is coming from!)"
    hide hiflmc
    "There's movement. I can see people in front of me, two shadowy figures set against the red, glistening walls."
    show bg insideperson_jd with dissolve
    "..."
    "I recognise them."
    "My horrified gasp is swallowed up by the deafening drumbeat of a pulse in my ears, a pulse that I now know belongs to {i}somebody else{/i}."
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I want to throw up.)"
    hide hiflmc
    "I don't. I know that, impossibly, I'm seeing someone's insides- seeing right back out through their skin- but the expected nausea never arrives."
    "From my position, frozen stock still with fascinated horror, I can hear muted vibrations all around me as Tam continues to chatter away."
    sid1 "Ooh, it's cold over here! Razi, we've got to talk about the air-con."
    "For some reason, that little bit of mundanity is the final straw."
    show bg bowling
    stop sound
    stop music
    play music "<from 4.5>audio/hifl/Sad.mp3"
    show tamara casual happy at left1
    show razi casual sad at left5 behind jd
    show jd casual surprised at left3
    show hiflmc bowling surprised at left1
    show hiflmc bowling at veryfastright
    "The utter wrongness of everything hits me like a truck, and my urge to {i}get out of there{/i} grows strong enough that I practically leap off the stool."
    #show hiflmc bowling sad at centre
    show hiflmc bowling sad at slowfallright3
    hide jd
    hide razi
    hide tamara
    "I hit the floor without a sound, sliding almost frictionless along the carpet for a brief moment before coming to a sudden, unnatural stop."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(It doesn't even hurt. It doesn't feel like {i}anything{/i}.)"
    show hiflmc bowling_cu sad_cu
    "(...I can't feel anything at all.)"
    hide hiflmc
    "I look up at the bar, feeling utterly lost and helpless from my spot on the floor."
    show razi casual sad at left3
    show jd casual surprised at right3
    "JD and Razi are both looking straight at me, sorrow etched into their features."
    show razi casual sad at left4
    show jd casual surprised at left1
    show tamara casual basic at right4
    "Tam notices, and whips her head around to look my way, but once again her eyes don't ever quite focus on me."
    show tamara casual sad
    sid1 "Uh... What are we looking at?"
    hide tamara
    hide razi
    hide jd
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(...She can't see me, can she?)"
    "(She hadn't just been ignoring me earlier, and she's not in on some stupid prank- she literally didn't know I was there.)"
    show hiflmc bowling_cu surprised_cu
    "(Why can't she see me!?)"
    show hiflmc bowling sad at centre
    "My hands tremble as I raise them before my eyes."
    show hiflmc bowling surprised at centre
    "(They're completely translucent.)"
    hide hiflmc
    show heroine_ghost_anime at bg
    "{i}I'm{/i} completely translucent."
    hide heroine_ghost_anime
    show ghostmc bowling surprised at centre
    "(What's happening to me?)"
    hide ghostmc

    $tobecontinued()
    show bg hifltbc
    with fade
    
    pause
    $ resets()
