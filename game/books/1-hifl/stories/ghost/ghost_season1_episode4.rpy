
label ghost_season1_episode4:
    $tbc = False
    scene bg blackscreen at bg
    show ov phn at bg
    play music gracehunter

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() at the bottom.
    "The phone rings once. Twice. Then-"
    show bg motel_night at bg
    show grace casual_cu basic_cu at grace_cu behind ov
    gr "Grace [genericln] speaking."
    show bg bowling at bg
    hide ov
    hide grace
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...Oh.)"
    hide ghostmc
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu basic_cu at grace_cu behind ov
    "Grace's voice is like a punch to my gut, and her face..."
    hide ov
    hide grace
    #show grace casual_cu basic_cu at grace_cu with CropMove(0.2, mode="wipeleft")
    show bg bowling
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(It's not like I hadn't believed Razi, when he told me how long I'd been gone.)"
    show ghostmc casual_cu sad_cu
    "(Part of me... already knew to begin with, I think.)"
    hide ghostmc
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu basic_cu at grace_cu behind ov
    "But as I peer down at the woman on the other end of the line, it's plain as day- even if physically, she looks the same as the last time I saw her."
    show bg bowling at bg
    hide ov
    hide grace
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(It's her eyes.)"
    hide ghostmc
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu sad_cu at grace_cu behind ov
    "Grace always had kind eyes, and the kindess is still there- but there's a sharpness, now, a hunted expression that's alien on her sweet features."
    show grace casual_cu sad_cu
    gr "I'm a little busy, Mac. What's up?"
    show bg bowling at bg
    hide ov
    hide grace
    show mac cop basic at centre
    ma "[genericln], if you're asking me to call back when you're not busy, you'll never hear from me again."
    hide mac
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu sad_cu at grace_cu behind ov
    gr "...Isn't that the truth."
    show grace casual_cu happy_cu
    gr "It {i}is{/i} good to hear from you, Sheriff. How can I help?"
    hide grace
    hide ov
    show bg bowling at bg
    "That's about as long as I can wait before I'm sticking my face directly in front of the phone's camera."
    show ghostmc casual surprised at centre
    ghostmc "Grace? Can-"
    show ghostmc casual sad
    ghostmc "Can you hear me?"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(I know I shouldn't. I know it's just going to hurt, but...)"
    "(That's my sister.)"
    hide ghostmc
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu basic_cu at grace_cu behind ov
    "There's no response for a long beat."
    gr "Uh. Mac? Hello?"
    hide grace
    hide ov
    show bg bowling at bg
    show ghostmc casual sad at centre
    ghostmc "Grace, sweetheart, I'm right here."
    ghostmc "...Please. I need you to answer me, okay? Tell me you're okay."
    hide ghostmc
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu basic_cu at grace_cu behind ov
    gr "Hellooo?"
    show grace casual_cu angry_cu
    gr "Mac, remember how I said I was busy? I wasn't like, joking, or whatever."
    hide grace
    hide ov
    show bg bowling at bg
    show mac cop sad at left1
    show ghostmc casual basic at right1
    show ghostmc casual basic at right2 with ease
    "I step away from the phone."
    hide mac
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(That's that, I guess.)"
    "(She can't see me.)"
    hide ghostmc
    show mac cop sad at centre
    ma "I'm sorry."
    "She says it while looking right at me."
    hide mac
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(I know.)"
    hide ghostmc
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu basic_cu at grace_cu behind ov
    gr "It's fine. Everything okay over there?"
    hide grace
    hide ov
    show bg bowling at bg
    show mac cop sad at centre
    "Mackenzie sighs."
    ma "Let's just say that things are getting complicated."
    hide mac
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu angry_cu at grace_cu behind ov
    gr "Oh, let me guess."
    gr "Labasque accepted your offer, and is respecting your authority."
    gr "She's also giving out free massages."
    hide grace
    hide ov
    show bg bowling at bg
    show mac cop angry at centre
    ma "She can't accept an offer she won't deign to listen to."
    show mac cop sad
    ma "I'll be honest, Grace- I ran out of rope a month ago. And with everything going on today-"
    hide mac
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu confused_cu at grace_cu behind ov
    gr "What about today? I knew something else was up."
    gr "What's got you spooked, Mac?"
    hide grace
    hide ov
    show bg bowling at bg
    show jd casual smirk at centre
    "I appreciate the herculean effort it must have taken JD to not laugh."
    hide jd
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(And fair's fair: I guess I am pretty spooky, now.)"
    hide jd
    hide ghostmc
    show mac cop surprised at centre
    "Mackenzie takes a few seconds to recover, herself."
    show mac cop sad
    "She looks at me questioningly, and I can guess what she's asking."
    hide mac
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Should we tell her about me?)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I'm out of touch, but I'm pretty sure 'Your dead sister is a ghost but you'll have to take my word on it' isn't something you say over the phone.)"
    show ghostmc casual sad at centre
    ghostmc "Not... Not yet."
    "My reply comes out as a whisper, and immediately afterwards I just want to laugh."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(What's the point of whispering? Grace can't hear me either way.)"
    hide ghostmc
    show mac cop sad at centre
    ma "...It's a long story."
    show mac cop basic at centre
    ma "I honestly don't think you'll believe it, either, not over the phone."
    hide mac
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu happy_cu at grace_cu behind ov
    gr "Why, Sheriff- if I didn't know better, I'd say you were trying to entice me into a job."
    show grace casual_cu happy_cu at grace_cu behind ov
    gr "You know I won't give you a discount just because you make it sound interesting."
    hide grace
    hide ov
    show bg bowling at bg
    show mac cop smirk at centre
    ma "Yeah, yeah, I hear you. Razi says he'll fix us up something nice, if you show up."
    show mac cop smirk at left3
    show razi casual smirk at right3
    ra "Does he, now?"
    hide mac
    hide razi
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu happy_cu at grace_cu behind ov
    gr "Oh! Hi, Razi!"
    gr "I'll come over for some more of that stroganoff."
    hide grace
    hide ov
    show bg bowling at bg
    show razi casual basic at centre
    "Razi makes a thoughtful sound, like he's seriously weighing his options."
    show razi casual smirk at centre
    ra "Very well. Your wish is my-"
    hide razi
    show bg motel_night at bg
    show ov phn at bg
    show grace casual_cu sad_cu at grace_cu behind ov
    "Grace groans theatrically."
    show grace casual_cu angry_cu at grace_cu behind ov
    gr "You can't just say that whenever! I didn't even wish for anything!"
    hide grace
    hide ov
    show bg bowling at bg
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...I don't think I can keep listening to this.)"
    hide ghostmc
    "My mind made up, I quietly amble over to the door."
    "When I get there, though, I meet with what is becoming my least favourite recurring obstacle."
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(This is getting very old, very quick.)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I wonder if I could convince Razi to just prop the door open with a brick?)"
    show ghostmc casual basic at centre
    ghostmc "Hey, JD."
    "I call over to them, this time paying no mind to my volume."
    show ghostmc casual sad at centre
    ghostmc "Can you get the door again, please?"
    hide ghostmc
    show jd casual surprised at centre
    "But JD's already been sucked into the conversation, and they don't seem to hear me."
    jd "Wait, you're banned from The Witching Hour? Since when?"
    "Grace's answer is faint, but I can vaguely hear her laughing, tinny as it is through the connection."
    hide jd
    show ghostmc casual sarcastic at centre
    ghostmc "Guys? Literally anyone with hands will do."
    hide ghostmc
    show diego glassesdoctor happy at centre
    "In the end, it's Diego who comes to my rescue."
    show diego glassesdoctor happy at left3
    show ghostmc casual basic at right3
    "He holds the door open for me, and makes a grand sweeping gesture."
    show diego glassesdoctor smirk at left3
    di "Ladies first."
    hide diego
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Chivalry really isn't dead.)"
    "(Just me.)"
    hide ghostmc
    show bg main_day at bg with dissolve
    stop music fadeout 0.5
    pause 0.5
    play music hifleveryday
    "I emerge onto the street, and just like before, I feel a sense of almost-calmness wash over me."
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(It's like how you can feel like the world is ending late at night, but feel okay in the morning.)"
    show ghostmc casual_cu sarcastic_cu
    "(Are ghosts claustrophobic? Or is being indoors just inherently depressing?)"
    hide ghostmc
    show diego glassesdoctor basic at centre
    "Surprisingly, the doc opts to remain outside with me."
    show diego glassesdoctor basic at left3
    show ghostmc casual basic at right3
    ghostmc "Not gonna chat with Grace?"
    show ghostmc casual angry at right3
    ghostmc "Should I be offended on her behalf? You know that she's great, right?"
    show diego glassesdoctor smirk at left3
    di "Someone has to let you back in."
    show ghostmc casual sad at right3
    ghostmc "...Oh. Yeah."
    hide diego
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(It's official: This is now humiliating, as well as all the other things.)"
    hide ghostmc
    show diego glassesdoctor sleep at centre
    "Diego sighs."
    show diego glassesdoctor sad
    di "That was unkind of me. I apologise."
    show diego glassesdoctor sad at left3
    show ghostmc casual sarcastic at right3
    ghostmc "It's true, though."
    show diego glassesdoctor basic
    di "Even more reason to employ tact."
    di "...Truth be told, even though I do care very much for your sister-"
    show ghostmc casual basic
    ghostmc "Careful, doc."
    show diego glassesdoctor sleep
    di "-in a strictly platonic sense-" 
    show diego glassesdoctor basic
    di "I find it difficult to listen to some of her stories."
    show ghostmc casual sad
    ghostmc "...The ones where she, um. Hunts vampires?"
    hide diego
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Ten minutes ago, I'd have laughed at the idea of Grace hunting anything.)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(She always let the spiders out of the house, rather than squish them.)"
    "(Razi said she was happy, but... I know my sister, and she just looked exhausted.)"
    hide ghostmc
    show diego glassesdoctor basic at centre
    di "Yes, but not for the reason you're imagining. I'm not prone to sentimentality towards other vampires."
    show diego glassesdoctor angry at centre
    di "Coven vampires, least of all."
    show ghostmc casual surprised at right3
    show diego glassesdoctor angry at left3
    ghostmc "What's wrong with covens?"
    show diego glassesdoctor angry
    di "Considering that vampire covens typically keep humans as cattle? There is an exhaustive list of things wrong with covens."
    hide diego
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Oh, there's no way that isn't exactly as horrifying as it sounds.)"
    hide ghostmc
    show diego glassesdoctor angry at centre
    "Seeing the queasy look on my face, Diego nods his head firmly."
    di "Believe me- If I slept, I wouldn't lose any of it over the types of vampire Grace [genericln] would see fit to hunt down."
    hide diego
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "('Grace [genericln]'.)"
    "(Mackenzie did the same thing earlier, referring to Grace by her full name, as if the name itself should invoke respect.)"
    show ghostmc casual_cu sarcastic_cu
    "(I'm getting the impression that my sister might actually be a celebrity.)"
    show ghostmc casual sad at centre
    ghostmc "So... why do Grace's stories bother you, then?"
    show diego glassesdoctor sad at left3
    show ghostmc casual sad at right3
    di "They're very... confronting, I suppose."
    di "You might have guessed that I'm not exactly part of the greater vampire community."
    show ghostmc casual sarcastic at right3
    ghostmc "I literally just learned that vampires exist, dude- I haven't really developed my prejudices yet."
    show diego glassesdoctor sleep at left3
    di "You know what I mean."
    show diego glassesdoctor basic at left3
    di "Vampires have an image, and popular culture isn't exactly far from the mark."
    show diego glassesdoctor sad at left3
    di "And here I am, playing at doctor for a town with exactly zero other vampires resident. Covenless and cut off."
    show ghostmc casual basic
    ghostmc "Kinda sounds like that's the better option, though."
    show diego glassesdoctor sad at left3
    di "Perhaps. Or perhaps I'm just allowing our sins to become someone else's..."
    show diego glassesdoctor surprised at centre
    hide ghostmc
    "Diego suddenly catches himself, and clears his throat uncomfortably."
    show diego glassesdoctor sad at centre
    di "I... suspect that this isn't the kind of conversation you were hoping for, when you made your escape."
    show diego glassesdoctor sad at left3
    show ghostmc casual sad at right3
    ghostmc "I really don't mind."
    hide diego
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(If anything, hearing about his problems makes it very hard to think about mine, and I absolutely do not want to do that.)"
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(I've never heard the doc talk so much in my life- I wonder if it's easier to vent to a dead person?)"
    hide ghostmc
    show diego glassesdoctor basic at centre
    di "...Well, at any rate, that's why I felt the need to leave the room."
    show diego glassesdoctor sad
    di "Might I ask why you felt the same?"
    show ghostmc casual angry at right3
    show diego glassesdoctor sad at left3
    ghostmc "Why do you think?"
    show ghostmc casual sad
    ghostmc "It just... really sucks not being able to talk to her."
    show diego glassesdoctor basic at left3
    "Diego gives me a pitying look- but it's the kind of pity you give to someone who's just said something especially stupid, not the sympathetic kind."
    di "I don't doubt it, but..."
    show diego glassesdoctor sad at left3
    "He hesitates."
    di "Mere minutes ago, you were extremely interested in Grace's life. You could be learning all about it right now, from her own lips."
    di "And yet, here you stand, listening to the town doctor complain about his self-imposed exile."
    show ghostmc casual angry
    ghostmc "If you're about to tell me I'm being a shitty sister, then maybe you should shove it-"
    show diego glassesdoctor angry
    di "That's not what I'm saying, [genericfn]. I just know that there's more going on, here."
    di "You don't have to tell me, but you do need to-"
    hide diego
    hide ghostmc
    play music suspense
    show vampguy casual_cu humanbasic_cu at vampguy_cu with CropMove(0.5, "wipeleft")
    "But what I have to do is left to my imagination, because at that moment, a whole person suddenly appears inches from my face!"
    show vampguy casual humanbasic at left1
    show ghostmc casual surprised at right1
    ghostmc "Holy shit!"
    show ghostmc casual surprised at right3 with ease
    "I quickly stumble back, pulling my hand out of the newcomer's chest cavity as I go."
    hide vampguy
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Who the heck is this!? Did he just {i}teleport{/i}??)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(That is so dangerous! He's going to end up losing an arm!)"
    show vampguy casual humanbasic at centre
    hide ghostmc
    "If he's particularly bothered by the fact that a stranger just had her fingers all up in his ribcage, he doesn't let it show."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    hide vampguy
    "(Can he not see me, either? But he's absolutely supernatural!)"
    hide ghostmc
    show vampguy casual humanangry at centre
    "Supernatural or not, he looks right through me in a way I'm growing very familiar with, to fix Diego with an absolutely filthy glare."
    $sidecharone = "Teleporting Dude"
    sid1 "Apostate."
    show vampguy casual humanangry at right3
    hide ghostmc
    show diego glassesdoctor sleep at left3
    "Diego sighs wearily."
    show diego glassesdoctor basic at left3
    di "Is she actually calling me that?"
    show diego glassesdoctor basic at left3
    show vampguy casual humanangry at right3
    sid1 "...No. It is {i}his{/i} name for you."
    sid1 "My master shows you more respect than you deserve."
    show diego glassesdoctor angry
    di "Your master has attempted to trick me into drinking animal blood on no fewer than four occasions."
    hide vampguy
    show diego glassesdoctor basic
    show ghostmc casual surprised at right3
    "Diego's gaze flickers my way, and he holds my gaze as he continues talking to the newcomer."
    di "I don't recommend letting the Sheriff catch you wandering the streets- you know very well how she feels about your little coven."
    hide diego
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Oh, this must be one of the 'vampire problems' Mackenzie was talking about.)"
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(He apparently can't even see me- which is kinda concerning on its own, to be honest, but one problem at a time- so I don't think I'm in danger here.)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Diego, on the other hand...)"
    show ghostmc casual sad at right3
    show diego glassesdoctor basic at left3
    ghostmc "Is everything okay, doc? Is this gonna be a fight?"
    show diego glassesdoctor smirk
    di "Not a long one."
    hide diego
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Not really the answer I was hoping for, but I guess I'll take it.)"
    show vampguy casual humansurprised at centre
    hide ghostmc
    $sidecharone = "Vampire Problem"
    sid1 "What was that?"
    show vampguy casual humanangry at centre
    sid1 "Who are you talking to?"
    show vampguy casual humanangry at right3
    show diego glassesdoctor basic at left3
    di "Just you, regrettably."
    show diego glassesdoctor angry at left3
    di "On that subject: Why {i}are{/i} you here?"
    show vampguy casual humanbasic at right3
    sid1 "I bring a message."
    show diego glassesdoctor sleep
    di "Which I await with bated breath, I assure you."
    show vampguy casual humanangry
    sid1 "Then keep waiting- It's not for you. It's for your mutt."
    hide diego
    hide vampguy
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Woah!)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(I'm pretty new to this whole thing, but even I can tell that last bit wasn't okay.)"
    hide ghostmc
    show diego glassesdoctor vampireangry at centre
    "Diego seems to agree with me on that one, his eyes flashing a dangerous red as a pair of wicked fangs make their appearance."
    show diego glassesdoctor vampireangry at left3
    show vampguy casual angry at right3
    "The other vampire follows suit, and I reflexively take a step back out of the way of the imminent brawl."
    hide diego
    hide vampguy
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Honestly, other than the fangs, this escalation just feels like watching the boys back in middle school.)"
    "(God forbid we try to talk out our problems.)"
    play sound doorthud
    hide ghostmc
    "Before anyone can do anything stupid, though, there's a sudden explosion of sound from the bowling alley, the front door near flying off its hinges."
    play music mackenziehunt
    show mac cop angry at centre
    ma "I think I've given you more than enough time to work out that you're in the wrong place."
    show mac cop angry at centre
    show diego glassesdoctor vampireangry at left3 behind mac
    show vampguy casual angry at right3 behind mac
    show mac cop angry at centre with ease
    show diego glassesdoctor vampireangry at left5
    show vampguy casual angry at right5 
    with ease
    "With that, Mackenzie storms out into the street, planting herself firmly between the doc and an increasingly outmatched vampire."
    show mac cop angry at right3
    hide vampguy
    show diego glassesdoctor vampireangry at left3
    ma "Cool off, Diego. Nobody's picking a fight in my town- Especially not its damn doctor."
    show diego glassesdoctor basic at left3 with dissolve
    di "Fair enough."
    hide mac
    $sidecharone = "Vampire"
    show vampguy casual angry at right3
    sid1 "Your obsequence to the dog shames you, apostate."
    show diego glassesdoctor angry at left3
    di "...Forgive me, Mackenzie. I'm a healer, but-"
    hide vampguy
    show mac cop angry at right3
    ma "But nothing."
    show vampguy casual angry at right3
    show mac cop basic at left3
    hide diego
    ma "Labasque had a perfectly good opportunity to speak with me this morning- an opportunity that she passed up."
    sid1 "My master had more pressing matters to attend to."
    show mac cop basic
    ma "I have no doubt. What's the message?"
    show vampguy casual humanangry with dissolve
    "The vampire refuses to look at Mackenzie, still glaring a hole through Diego's head- but the fangs do slip back into his mouth."
    hide vampguy
    show ghostmc casual_cu sad_cu at hiflmc_cu
    hide mac
    "(Phew.)"
    "(Things were looking a little tense, there.)"
    show ghostmc casual_cu sarcastic_cu
    "(It's not like I was going to be any help, either.)"
    show vampguy casual humanbasic at centre
    hide ghostmc
    sid1 "My master's patience wanes."
    show vampguy casual humanbasic at right3
    show mac cop basic at left3
    ma "Wonderful. We finally have something in common."
    show vampguy casual humanangry
    sid1 "She is no longer asking, Hunt. Her demands are as follows:"
    show mac cop angry
    ma "Now, just wait a-"
    show vampguy casual humanbasic at centre
    hide mac
    "As if Mackenzie hadn't said anything, the vampire forges on, tonelessly reciting his master's message."
    sid1 "You will leave Havenfall, along with the djinn and the demon child, forfeiting the town to the Labasque coven."
    sid1 "You will do this by midnight tonight, or we will come for you in force."
    hide vampguy
    hide mac
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Holy shit.)"
    "(Mackenzie said things were getting complicated, but this? This is an actual coup!)"
    hide ghostmc
    show mac cop basic at right3
    show diego glassesdoctor basic at left3
    "If the demands are at all shocking to Mackenzie and Diego, they don't let it show."
    show mac cop sad at centre
    hide diego
    "Mackenzie looks... almost resigned, like she knew this was coming sooner or later."
    hide mac
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Actually, she probably did. That's why she called in my sister.)"
    hide ghostmc
    show diego glassesdoctor surprised at centre
    di "...What about me?"
    show diego glassesdoctor surprised at left3
    show vampguy casual humanangry at right3
    "The vampire had never actually stopped glaring at Diego, and the answer he gives him is ground out hatefully, through clenched teeth."
    sid1 "As I said. My master shows you more respect than you deserve. You may remain in her town."
    show diego glassesdoctor smirk
    di "Quite generous of her."
    sid1 "Do not get the wrong idea- if you stand against her, she will drain you dry with the rest."
    hide diego
    show vampguy casual humanangry at centre
    "There's a beat, in which the vampire probably expects Mackenzie to say something tough and threatening."
    show vampguy casual humanangry at right3
    show mac cop basic at left3
    "She doesn't."
    hide mac
    hide vampguy
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(She just looks tired.)"
    hide ghostmc
    show vampguy casual humanbasic at centre
    sid1 "That is my message."
    show vampguy casual humanangry at centre
    sid1 "You have until midnight."
    hide vampguy with CropMove(0.5, "wipeleft")
    "And with those parting words, he vanishes from sight."
    
    stop music fadeout 0.5
    pause 0.5
    play music hifleveryday
    "As soon as he's gone, the door to the bowling alley opens once again- much more sedately, this time."
    show razi casual basic at right3
    show jd casual angry at left3
    "Razi steps out and joins the growing crowd on the street, trailed by a stormy-faced JD."
    hide jd
    hide razi
    show mac cop surprised at centre
    "Mackenzie turns to them both, perking up hopefully."
    ma "Grace?"
    show mac cop surprised at right3
    show razi casual sad at left3
    "Razi winces."
    ra "At least a day's drive away."
    show mac cop angry
    ma "...Damn it."
    hide razi
    show mac cop angry at centre
    ma "Labasque's shifting gears. Now she says she wants us out of the town by midnight, or things get bloody."
    hide mac
    hide razi
    show jd casual happy at centre
    "For some reason, this actually earns a laugh from JD."
    show jd casual happy at left3
    show mac cop angry at right3
    ma "There a joke I'm not seeing here, Davies?"
    show jd casual smirk at left3
    jd "Pretty sure the joke's gonna be on Liliane Labasque, when my old man finds out she's the one who kicked me out of Havenfall."
    hide mac
    show razi casual surprised at right3
    ra "...I hadn't even thought about that."
    show razi casual smirk
    ra "Think we could get her to back off by telling her your dad will beat up her dad?"
    hide razi
    hide jd
    show mac cop basic at centre
    ma "Diego, you know her best- is she actually going to stick to her deadline?"
    hide mac
    show diego glassesdoctor sleep at centre
    "Diego pulls from his coat an actual pocketwatch, because of course he does. He inspects it, humming thoughtfully."
    show diego glassesdoctor basic
    di "I think we can trust her to keep her promises, if nothing else. We have nine hours."
    hide diego
    show ghostmc casual surprised at centre
    ghostmc "Nine hours to do what?"
    hide ghostmc
    "Everyone turns to me, blinking in surprise like they'd forgotten I was there."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(If I'm being honest, {i}I{/i} had kinda forgotten.)"
    show ghostmc casual_cu sad_cu
    "(It's a little hard to describe. Part of me is perfectly content to just... watch things happen, without providing any input.)"
    show ghostmc casual_cu sarcastic_cu
    "(The other, more familiar part of me is freaking out, because I'm apparently watching a horror movie.)"
    show ghostmc casual sarcastic at centre
    ghostmc "Just so I'm clear: is this Labasque person straight up threatening a war?"
    show jd casual basic at left3
    show ghostmc casual sarcastic at right3
    jd "Pretty much, yeah."
    hide jd
    show mac cop sad at left3
    ma "...Yes. And at this point, I don't see any way to avoid bloodshed."
    show ghostmc casual surprised 
    ghostmc "What happens if she gets the town? Do we need to like, evacuate, or something?"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    hide mac
    "(I know that if I was one of the townspeople, I'd be pretty interested in getting the fuck out, if I knew a vampire coven was moving in.)"
    show ghostmc casual_cu sad_cu
    "(Maybe that's just my 'killed by a vampire' bias talking.)"
    show diego glassesdoctor sad at centre
    hide ghostmc
    di "Realistically, no. And I'm not sure we could even justify doing so."
    show diego glassesdoctor basic
    di "Liliane's not the type to let her people slaughter humans. In the short term, nothing would change."
    show diego glassesdoctor basic at left3
    show ghostmc casual sad at right3
    ghostmc "...And in the long term?"
    show diego glassesdoctor sad
    di "That's a different story."
    di "Havenfall's a small town, and her coven is rather large. There's just not enough blood in people's veins to make it work safely."
    di "People {i}will{/i} get sick."
    show diego glassesdoctor angry
    di "Of course, Liliane knows that. I genuinely cannot imagine why she'd go through all of this trouble for such a limited food source."
    hide diego
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "('Food source'.)"
    show ghostmc casual_cu angry_cu
    "(Oh my god, I was {i}food{/i}!)" 
    "(Everything's been happening so quickly I hadn't even really thought about {i}why{/i} those vampires killed me.)"
    "(Can vampires get indigestion? I hope my iron-deficient ass gave them the fucking runs.)"
    show ghostmc casual basic at centre
    ghostmc "Okay. Wow. Okay."  
    show ghostmc casual sad
    ghostmc "I really hate to ask, but, um. Is this a fight you can win?"
    show ghostmc casual surprised at right3
    show mac cop angry at left3
    ma "I'm not running."
    "The response comes quickly and fervently, like the idea- even just the merest implication of the idea- is a dangerous one, to be swiftly quelled."
    hide ghostmc
    show mac cop basic at centre
    ma "I know you're new to all of this, [genericfn], so let me make this clear:"
    show mac cop angry
    ma "This is Hunt land- my territory. No vampire gets to chase me off of it, no matter how old she is-"
    show mac cop angry at right3
    show diego glassesdoctor basic at left3
    di "At least one thousand years old, for the record."
    hide mac
    hide diego
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Holy shit.)"
    hide ghostmc
    show mac cop surprised at centre
    "Even Mackenzie looks taken aback by that, the wind leaving her sails mid-rant."
    hide mac
    show jd casual angry at centre
    jd "Great, she's a millennial. No wonder she's trying to kill us."
    hide jd
    show ghostmc casual surprised at centre
    ghostmc "Is her being obscenely old a problem?"
    show ghostmc casual sarcastic
    ghostmc "I take it vampires don't have to deal with arthritis."
    show ghostmc casual sarcastic at right3
    show razi casual sad at left3
    ra "With folks like us, 'old' tends to mean 'powerful'. Vampires especially."
    hide razi
    show diego glassesdoctor basic at left3
    di "Yes, but that actually works in our favor, in this case- I sincerely doubt there's a single other vampire in that coven as old as a century."
    hide diego
    hide ghostmc
    show mac cop angry at centre
    ma "I'm less worried about their ages than I am their numbers. I have no idea how many people she's got skulking around in the forest."
    show mac cop angry at right3
    show jd casual surprised at left3
    jd "Can't you like, smell them? Hear their footsteps? Do wolfy stuff?"
    show mac cop basic
    ma "If I was physically in the forest, I could probably pinpoint up to a couple dozen, sure. Any more than that and it gets trickier."
    show mac cop sad
    ma "...There's going to be more than a couple dozen. On top of that, entering the forest at this point just starts the fight early, and on Labasque's turf."
    hide mac
    hide jd
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(It sounds like we need a way to figure out what Labasque's up to, without starting a huge fight then and there.)"
    show ghostmc casual_cu surprised_cu
    "(...Oh!)"
    show ghostmc casual_cu happy_cu
    "(I have a brilliant idea.)"

    # hide diego
    # hide ghostmc
    # "But suddenly, I really DO want to tell him."
    # show ghostmc casual_cu glassesbasic_cu at hiflmc_cu
    # "(The doctor should have just kept talking, because now?)"
    # show ghostmc casual_cu glassesangry_cu at hiflmc_cu
    # "(I want to {i}scream{/i} it at him.)"
    # play music sad
    # show ghostmc casual glassesangry at centre
    # ghostmc "Razi makes her dinner!"
    # hide ghostmc
    # show diego glassesdoctor surprised at centre
    # "Diego's mouth snaps shut, and he blinks owlishly in surprise."
    # di "...On occasion, yes."
    # show diego glassesdoctor surprised at left3
    # show ghostmc casual glassesangry at right3
    # ghostmc "All of you sit down and you... you have dinner together!"
    # "This is spat out, like an accusation, and Diego flinches back at my tone."
    # show diego glassesdoctor sad
    # di "I... well, I can't eat, but. Yes, we do sit down together."
    # show diego glassesdoctor basic
    # di "And, yes, if Grace is in town, we always ask her to join us."
    # ghostmc "Oh, I bet!"
    # hide diego
    # show ghostmc casual glassesangry at centre
    # "I reach up to shift my glasses, so I can wipe away the angry tears that always bead up in the corners of my eyes when I'm about to really get going."
    # show ghostmc casual glassessurprised at centre
    # "Nothing happens. The hand passes right through the glasses' frame, not moving them an inch."
    # show ghostmc casual_cu glassesangry_cu at hiflmc_cu
    # "(Of course. Another basic fucking thing I just can't do anymore.)"
    # "(And it doesn't even matter, because I! Can't! Cry!)"
    # show ghostmc casual glassesangry at centre
    # ghostmc "Goddamn it!"
    # hide ghostmc
    # "I sink down to the sidewalk, my knees smacking silently and painlessly into the hard concrete."
    # show diego glassesdoctor sad at left3
    # show ghostmc casual glassesangry at right3
    # "Diego follows me down, face pinched with concern."
    # di "Are you okay?"
    # show ghostmc casual glassessurprised at right3
    # ghostmc "It's too much. This is too much, I can't {i}take{/i} this anymore!"
    # ghostmc "I- I can't- I-"
    # hide ghostmc
    # hide diego
    # "The words won't come out- I don't even know what I'm trying to say."
    # show ghostmc casual_cu glassessurprised_cu at hiflmc_cu
    # "(I feel like I'm on the cusp of a panic attack, or passing out, or even just straight up dying again, but {i}nothing's happening{/i}!)"
    # show ghostmc casual_cu glassessad_cu at hiflmc_cu
    # "(Like drifting down a river to the edge of a waterfall, but never quite going over the edge.)"
    # show ghostmc casual_cu glassesangry_cu at hiflmc_cu
    # "(And of course I don't! Panic and death are things that happen to a body, and I don't get to have one of those anymore.)"
    # "(This sucks. This isn't fair. I've been a ghost for all of an hour and I want to stop. I want the lights to go out. This isn't living.)"
    # show diego glassesdoctor sad at left3
    # show ghostmc casual glassessurprised at right3
    # "We sit like that for some time- Diego silently keeping me company as I, just as silently, fail to experience any kind of emotional climax."
    # show ghostmc casual glassessleep at right3
    # "And then, after a few minutes, and in the least satisfying way imaginable, I finally drift away from the waterfall's edge."
    # hide diego
    # show ghostmc casual_cu glassesbasic_cu at hiflmc_cu
    # "(I didn't do anything to calm myself down. I'm still in the river.)"
    # show ghostmc casual_cu glassessarcastic_cu
    # "(I can still absolutely feel that yawning chasm stretching out beneath me- but with effort I can {i}pretend{/i} I can't, which is almost like feeling better.)"
    # show ghostmc casual glassessad at centre
    # ghostmc "...I'm sorry I shouted at you."
    # show ghostmc casual glassessad at right3
    # show diego glassesdoctor basic at left3
    # "Diego's response comes promptly, as if I hadn't put the conversation on hold to experience feelings."
    # di "No need to apologise."
    # show ghostmc casual glassesangry
    # ghostmc "Yes, there is. I don't even know why I'm mad at you."
    # show ghostmc casual glassessad
    # ghostmc "...Or I guess, I do know, but it's for an awful reason."
    # ghostmc "God, am I really mad that my sister has {i}friends{\i}? Is that what this is?"
    # show diego glassesdoctor sad at left3
    # di "I think it's understandable, in your case."
    $ tobecontinued()
    hide ghostmc
    show bg hifltbc at bg
    with fade
    pause

    $ resets()
