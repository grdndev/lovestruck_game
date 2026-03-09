label korin_season1_episode11:

    $tbc = False
    scene bg ecm_restaurant_night_lights at bg
    play music ecmcalmeveryday4

    pause

    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    show ecmc jacket_v2 pin smile at left3
    show korin jacket pin smile at right3

    "Korin and I head to our usual haunt."

    "Korin doesn't bother starting with shirley temples this time. Rhys, ever chummy, keeps the drinks coming..."

    "And before long, the both of us are happily buzzed and de-stressing with each other."
    show ecmc jacket_v2 pin surprised
    mckorin "Put it away! Come on, Korin..."
    show korin jacket pin smirk
    "She jots out another quick message on her ARCware, then throws the alerts on silent."

    ko "Sorry, Dom’s got a lot of questions, you know. . ."
    show ecmc jacket_v2 pin determined
    mckorin "And Connie should be able to answer them, like she said she would."

    mckorin "It’s not like we’re both going to see him tomorrow."

    "She catches the tremor in my voice and nudges my foot under the table with her own."
    show korin jacket pin sad
    ko "Hey. Are you still worried about something?"
    show ecmc jacket_v2 pin sad
    mckorin "It’s just. . . what if this isn’t enough for him? What if he’s still going to let me go?"
    show korin jacket pin angry
    "Korin sets her jaw and shakes her head."

    ko "No. That’s not going to happen."
    show ecmc jacket_v2 pin embarrassed
    mckorin "How do you know?"

    ko "If Dom fires you for being framed for destruction of evidence by a serial killer, then. . ."
    show korin jacket pin sad
    "She shrugs."

    ko "Then my time at D.I.V.A.A. is over, too."
    show ecmc jacket_v2 pin surprised
    mckorin "Korin! No..."
    show korin jacket pin angry
    ko "That’s how serious I am about this!"

    "Despite her conviction though, there’s a hint of trouble that doesn’t clear from her expression."

    mckorin "What’s got you worried, Kor?"
    show korin jacket pin sad
    ko "It’s just... Anton. Who could have guessed that?"

    "She takes another drink and shakes her head."

    ko "We should just forget about it for now."

    ko "What matters is that you’re okay, and you made it out of there alive..."

    ko "And I’ve been looking forward to nights like this with you more and more these days."

    "My face is warm, partly from the drinks, but moreso from Korin’s affection."

    mckorin "Is this our last one? Since you’re not going to have to help me anymore..."
    show korin jacket pin surprised
    ko "No!! No way."

    ko "In fact, it’ll all be easier now. No more skulking around..."
    show korin jacket pin sad
    show ecmc jacket_v2 pin determined
    "She sighs again."

    ko "I’m just so glad you’re okay. I might not have shown it, but when it was clear you were in danger with Anton..."
    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(Drinking seems to be making her kind of emotional. I should try and reassure her...)"
    hide ecmc
    show ecmc jacket_v2 pin determined at left3
    show korin jacket pin sad at right3
    mckorin "I mean, reading over the old case files, he wasn’t much of an opportunistic killer."

    mckorin "Definitely a planner, not great with improvisation..."
    show ecmc jacket_v2 pin sad
    mckorin "...Hey. Are you okay?"

    ko "I’ve just got a lot on my mind."

    mckorin "Well... do you want to talk about it?"
    show korin jacket pin smile
    "Korin laughs and takes a long sip of her drink."

    ko "Not really, no."
    show korin jacket pin smirk
    ko "I’d rather just enjoy the night with you."
    show ecmc jacket_v2 pin smile
    mckorin "Come on... thanks to you, nothing happened! Everything turned out for the best..."
    show korin jacket pin sad
    ko "If anything had happened to you, I don’t know what I’d..."

    "She stops herself."
    show ecmc jacket_v2 pin sad
    mckorin "You'd... what?"

    ko "I'd..."

    "On the table between us, her hand twitches toward mine..."
    show korin jacket pin sad at right3:
        easein 0.4 xoffset -140
    "But she stops before she reaches me."

    "She pulls away before I can even think to close the little distance between us."

    ko "I’d... know that I really let down your dad."

    "Dropping the subject, she picks up her drink instead."
    hide ecmc
    hide korin
    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(If I didn’t know Korin as well as I do now, I’d believe her when she said that.)"

    "(But that look in her eye. . . that isn’t what she was going to say.)"
    hide ecmc
    show ecmc jacket_v2 pin sad at left3
    show korin jacket pin sad at right3:
        xoffset -140
    "I let my mind wander to the question I’ve been afraid to ask myself for so long, now..."
    hide ecmc
    hide korin
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(Would it really be so wrong to ask her out?)"

    hide ecmc
    $menuhideborder = True

    menu korins1e11c1:
        "A. No! YOLO!":
            $menuhideborder = False
            show ecmc jacket_v2_cu pin_cu angry_cu at ecmc_cu
            "(No! YOLO! I should just do it!)"
            show ecmc jacket_v2_cu smile_cu
            "(...That’s what Enver would say, anyway.)"

            "(Man, it’s way easier to think like Enver when I’m tipsy.)"

        "B. What if she says no?":
            $menuhideborder = False
            show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
            "(But what if she says no? And then it’s weird between us?)"

            "(Korin wouldn’t make it weird, but I’m sure I wouldn’t be able to help it...)"

        "C. Is this even allowed??":
            $menuhideborder = False
            show ecmc jacket_v2_cu pin_cu embarrassed_cu at ecmc_cu
            "(She’s a trainer, and I’m a trainee...)"
            show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
            "(She’s not that much older than me, but still. Is that even allowed?)"

            "The thought of asking such a thing of Korin or Enver is mortifying."
    hide ecmc
    show ecmc jacket_v2 pin smile at left3
    show korin jacket pin smile at right3
    "The night goes on, both of us talking and laughing and blowing off steam."

    "I can feel the stress of the past few weeks slowly releasing its hold on me."

    "Rhys stops by our table with a check..."
    show korin jacket pin surprised
    show ecmc jacket_v2 pin surprised
    rh "Sorry, but this case is about to close."

    rh "And by that I mean... it’s closing time. You’re the only ones still here."

    ko "Oh, jeez! I didn’t realize the time..."

    rh "Hey, you two gonna make it home together safely?"
    show ecmc jacket_v2 pin smile
    show korin jacket pin smile
    "Korin giggles."
    show ecmc jacket_v2 pin surprised
    mckorin "Oh, we're not..."

    ko "Yeah, we'll be good. Thanks, Rhys."

    rh "I’d suggest finding somewhere else nearby, but most everything nearby is closed down this time of night."
    show ecmc jacket_v2 pin basic
    ko "I’m okay. I can hail a ride, and [genericfn] doesn’t live far from here. . ."
    show ecmc jacket_v2 pin smile
    mckorin "...You could come to my place if you want."
    show korin jacket pin surprised
    "Korin gives me a wide-eyed look."
    show ecmc jacket_v2 pin surprised
    mckorin "I mean... just to sober up, if you want to. We could watch a movie, or something..."
    hide ecmc
    hide korin
    show korin jacket_cu pin_cu smile_cu at korin_cu
    "My heart picks up as Korin looks both relieved and hopeful."

    ko "Really? You’re cool if I come over and hang out? Just so I can get home sober. . ."
    hide korin
    $menuhideborder = True
    menu korins1e11c2:
        "A. Let Korin sober up and relax at your apartment." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smile at right3
            mckorin "Yeah, definitely! Let's go!"
            show korin jacket pin basic
            "As we’re climbing out of our booth, Rhys takes me in a quick aside."

            rh "You’re going to watch out for her, right?"

            "I nod."

            mckorin "After the way she’s watched out for me? Definitely."

            scene bg ecm_mc_dorm_on at bg with slideright
            stop music
            play music ecmromantic1
            pause

            "A short walk later, with much giggling and stumbling, we make it to my apartment."
            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin smile at right3
            "I take Korin’s coat and hang it up as Korin looks around again."

            ko "I didn’t get to say this before, but I love your place! It’s so cute…"
            hide ecmc
            hide korin
            show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
            "(Cute how? Cute like she thinks I’m attractive? Cute like a kitten? How??)"
            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin smile at right3
            "Korin climbs up to the loft and sits on the end of my bed, looking out the window."
            show korin nojacket pin smirk
            ko "Look at that view. It’s so cozy up here…the perfect place to curl up with someone on a rainy evening…"
            show ecmc jacket_v2 pin blush embarrassed
            "I imagine curling up with Korin and swallow hard."

            mckorin "Um... you said something about a movie? Want to pick one, and I’ll make some tea?"
            show korin nojacket pin smile
            ko "Ooh, sounds great!"

            "She follows me back down the stairs and throws herself down on the couch, pulling up the interface for my holo-projector."
            hide ecmc
            show ecmc jacket_v2 pin smile at left3
            "I switch on my kettle, then turn around just in time to see her pick a movie. I snort out a laugh."

            mckorin "{i}Conversion Rate{/i}? Really?"

            "Korin giggles as the blood spattered titles start to roll."
            show korin nojacket pin smirk
            ko "I know it’s corny, and the effects are bad, but…it’s a classic! Who doesn’t love e-zombies?"

            "I grin and shake my head."
            show korin nojacket pin surprised
            ko "What?? I mean, we’re not actually going to watch it, anyway... are we?"
            show ecmc jacket_v2 pin smile at left3:
                easein 0.4 xoffset 140
            "I bring two mugs over to the couch and hand one off to Korin."

            mckorin "What {i}are{/i} we going to do?"
            show korin nojacket pin smirk
            ko "...We don’t have to do anything special. I just like being with you."
            show ecmc jacket_v2 pin embarrassed
            "On the holo-projector screen above us, a zombie reaches through the screen of a computer, and the protagonist screams in horror."
            show ecmc jacket_v2 pin smile
            mckorin "Do you have a zombie plan?"

            "Korin looks over at me."
            show korin nojacket pin surprised
            ko "Like, what I’d do if zombies attacked?"

            mckorin "Yeah. Enver likes movies like this, too. He has this really detailed plan..."
            show korin nojacket pin smirk
            ko "About the floating island survivalist community? Oh, yeah. I’ve heard it."

            "She looks up at the movie, thoughtful as she watches."

            "Onscreen, a group of survivors blindfold themselves as they run through a metro station to shield themselves from the virus-inducing marketing ads."

            ko "I mean, if it were e-zombies specifically, I know I’m running straight for you."
            show ecmc jacket_v2 pin surprised
            mckorin "Me??"

            ko "We already know that you and I make a great team..."
            show ecmc jacket_v2 pin determined
            ko "And if you’re going to save the world by writing some program to stop the virus, you’re going to need me watching your back."
            show ecmc jacket_v2 pin surprised
            mckorin "I’m the one saving the world?? That’s a lot of pressure!"
            show ecmc jacket_v2 pin smile
            ko "Oh, for sure. You’d be all ‘I can’t do it!’ the whole movie. And I’d be like, ‘Of course you can! I believe in you!’"

            ko "And then during the climax you’d look over, and I’d be like..."
            show korin nojacket pin surprised behind ecmc
            "I look over to see her making a blank and zombie-like expression."
            show ecmc jacket_v2 pin smile:
                easein 0.6 xoffset 290
            "Playing along, I gently shake her shoulder."
            show ecmc jacket_v2 pin surprised
            mckorin "Korin, no! Not you, too! Nooo!"

            "She lets out a groan like one of the e-zombies shambling around on screen–but she can’t hold up the facade for long."
            show ecmc jacket_v2 pin smile
            show korin nojacket pin smile
            "We both collapse into a fit of laughter."
            hide ecmc
            hide korin
            "By the end of the movie, my cup is empty, and I’m sure Korin’s is, too…but neither of us remarks on it."
            show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
            "(I could stay up talking to her all night...)"
            hide ecmc
            show ecmc jacket_v2 pin basic at left2
            show korin nojacket pin sad at right2
            ko "Hey, so... with everything that’s happened, if you need to take a day off or something…"
            show ecmc jacket_v2 pin sleep
            "I shake my head."
            show ecmc jacket_v2 pin surprised
            mckorin "What, now that I’m allowed to do my actual job again? No way!"
            hide ecmc
            hide korin
            show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
            "(And miss out on a whole day of learning from Korin? Watching her...)"
            hide ecmc
            show ecmc jacket_v2 pin basic at left2
            show korin nojacket pin smile at right2
            "Korin chuckles, then pulls herself to her feet."

            ko "Well, in that case... I should really take off. You need to get some sleep."

            "I follow her, taking her cup from her."
            show ecmc jacket_v2 pin embarrassed
            mckorin "You do too, you know. If you can’t make it home, you could...um..."
            show korin nojacket pin surprised
            "Korin’s eyes flit to the loft for a second, then the couch. She smiles."
            show korin nojacket pin smile
            ko "It’s okay. I better get home. Thanks for letting me take shelter here for a little while..."
            hide ecmc
            hide korin
            show korin nojacket_cu pin_cu smile_cu at korin_cu
            "She leans forward and hugs me."

            "I hug back as best I can with mugs in either hand, leaning my face into her shoulder."

            "But Korin doesn’t make any motions to move away, and neither do I. My speech is muffled as I tell her..."
            hide korin
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "Come back anytime."
            hide ecmc
            show ecmc jacket_v2 pin smile at left2
            show korin nojacket pin basic at right2
            "And too soon, she pulls away, heading for the door."
            show korin nojacket pin smirk
            ko "Careful. I’ll hold you to that."

            ko "See you around, Scraps."
        "B. Send her home.":
            $menuhideborder = False

            show bg ecm_mc_dorm_on at bg
            show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
            "(Is my place clean? What if I make things weird?? Um...)"

            show bg ecm_restaurant_night_lights at bg
            hide ecmc
            show korin jacket pin basic at left3
            show ecmc jacket_v2 pin surprised at right3
            "Korin catches my indecision and waves me off."
            show korin jacket pin smile
            ko "Hey, no, it’s whatever. I’ll just get a ride home."

            ko "Take care, Scraps. I’ll see you around."


    scene bg ecm_dominick_office_day at bg with slideright
    stop music
    play music ecmcalmeveryday2
    pause

    show connie casual basic at left3 behind dominick
    show dominick uniform pin headpiece basic at left1
    show gael uniform glasses basic at right3
    "The next day, I meet early with Korin, Connie, Gael, and Dom in Dom’s office."

    do "Well, Eko went over the contents of the drive. This cold case is now pretty open and shut..."
    show dominick uniform pin headpiece smirk
    do "And it’s all thanks to you, [genericfn]."
    show gael uniform glasses smile
    ga "Yep. With the drive, and your testimony, and his little stunt from last night, we have everything we need to convict."
    show dominick uniform pin headpiece basic
    ga "As for how this reflects on the F.D.I’s relationship with D.I.V.A.A. ..."

    "I shoot a nervous glance at Dom, who looks equally anxious– though he’s hiding it better."

    ga "...It speaks well that a Hatchling uncovered the plot and got the help she needed from her superior before it was too late. However..."

    do "However, it’s clear we can do better."

    ga "And if I know anything about D.I.V.A.A., it’s that I can hold you to that."
    hide connie
    hide dominick
    hide gael
    show ecmc jacket_v2 pin basic at left3:
        easein 0.5 xoffset 90
    show gael uniform glasses smile at right3 behind ecmc:
        easein 0.5 xoffset -140
    "Gael holds her hand to me, and I shake it."

    ga "Really impressed with your work, [genericfn]. Looking forward to working with you again soon."
    show ecmc jacket_v2 pin smile
    mckorin "Not {i}too{/i} soon though, I hope."

    ga "Hah. Absolutely."
    hide gael
    hide ecmc

    show ecmc jacket_v2 pin basic at left4
    show korin jacket pin basic at right1
    show dominick uniform pin headpiece basic at right5
    "Gael takes her leave, and I’m left with Korin and Dom."
    show ecmc jacket_v2 pin surprised
    mckorin "What was on that drive that was so important for Anton to hide?"
    show korin jacket pin angry
    ko "Basically, he was using D.I.V.A.A. resources to stalk and kill his victims, and the drive had illegal Z-net programs on it that covered his tracks."

    do "Because the drive was D.I.V.A.A.-issued..."
    show dominick uniform pin headpiece angry
    do "Internal failsafes would have been alerted automatically if he had destroyed the evidence himself..."

    do "Either with a virtual re-write, or the old fashioned way of just breaking the drive physically."
    show ecmc jacket_v2 pin angry
    mckorin "Which is why he installed that corruption virus, letting it sit dormant until someone else picked it up..."
    show dominick uniform pin headpiece smirk
    do "And I suppose we should count ourselves lucky that the one who picked it up was you."
    show ecmc jacket_v2 pin smile
    "I grin and straighten up."
    show ecmc jacket_v2 pin surprised
    mckorin "So, does this mean I’m out of probation?"
    show korin jacket pin smirk
    do "That’s right. Welcome back..."
    hide ecmc
    hide korin
    hide dominick
    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    "(Yes!!)"
    show ecmc jacket_v2 pin surprised at left4
    show korin jacket pin smirk at right1
    show dominick uniform pin headpiece smirk at right5
    do "...To the trainee pool."
    show korin jacket pin sad
    "Korin scoffs and shakes her head. Dom points at her."
    show dominick uniform pin headpiece angry
    do "Don’t start, Reyes. You’re lucky my warning for you not to help [genericfn] was just a warning. . ."

    do "And you didn’t break any official policies."
    show korin jacket pin smile
    show ecmc jacket_v2 pin smile
    ko "Hey, it all worked out in the end!"

    do "It did this time. But don’t ever go against my orders again."

    "Dom sighs and looks at me, then back to Korin."
    show dominick uniform pin headpiece smirk
    do "She must be worth the trouble."
    hide ecmc
    hide dominick
    hide korin
    show korin jacket_cu pin_cu smirk_cu at korin_cu
    ko "Oh yeah. Definitely."
    hide korin
    show ecmc jacket_v2 pin blush embarrassed at left4
    show korin jacket pin smirk at right1
    show dominick uniform pin headpiece smirk at right5
    "My heart skips a beat as her eyes settle on me, just for a moment."

    do "Well, don’t let me keep you two. I’m sure you have much to catch up on, [genericfn]."

    do "And I really am looking forward to seeing what the future of your time at D.I.V.A.A. brings."

    scene bg ecm_office_cafe_on at bg with wiperight
    stop music
    play music ecmupbeateveryday1
    pause
    "A short while later, Korin and I hit the cafe at HQ and get coffee for all the other trainees."
    show ecmc jacket_v2 pin smile at left3
    show korin jacket pin basic at right3
    show bird normal at right3:
        xoffset 100 yoffset 90
    mckorin "Pretty weird, going on an {i}actual{/i} run for coffee, with no ulterior motives for once."
    show korin jacket pin smirk
    ko "Do you think it’s going to be weird, going back to normal after all that’s happened?"
    hide ecmc
    hide korin
    hide bird
    $menuhideborder = True
    menu korins1e11c3:
        "A. No, I'm psyched.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right3
            show bird normal at right3:
                xoffset 100 yoffset 90
            mckorin "No, I’m psyched for it. If it doesn’t mean my job is on the line anymore, I’m ready for the monotony!"

        "B. Yeah, it's going to be weird.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right3
            show bird normal at right3:
                xoffset 100 yoffset 90
            mckorin "After going so long having to do everything in secret? Yeah, it’s going to be weird getting back to normal."

        "C. Does 'normal' even exist in this job?":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right3
            show bird normal at right3:
                xoffset 100 yoffset 90
            mckorin "Does normal even exist in this job? Seems to me like it’s just one thing after another..."

    "Korin chuckles and helps me set down the rest of the coffees for everybody."
    show ecmc jacket_v2 pin surprised
    mckorin "Is it going to be weird having me as a trainee again?"

    ko "A little... but not in a bad way."

    mckorin "I can call you Miss Reyes if that’ll help--"
    show korin jacket pin surprised
    "Korin gasps."

    ko "Call me {i}what{/i}?! Never! Never again!"
    show ecmc jacket_v2 pin smile
    ko "I was going to say it’ll be hard not letting on that you’re my favorite, but..."

    mckorin "I’m your favorite? Really?"
    show korin jacket pin angry
    "Korin shushes me."
    show korin jacket pin smirk
    ko "Go, sit! Before someone overhears you."

    mckorin "Oh, should I sit right up front? Since I’m the teacher’s pet..."
    show korin jacket pin smile
    ko "Keep it up! If you’re trying not to be my favorite anymore, you’re off to a great start."

    "But she says it with a smile, and with little conviction."
    hide ecmc
    hide bird
    hide korin
    show ecmc jacket_v2 pin determined at centre
    "I take my coffee and swipe through the day’s material on my ARCware as the rest of the trainees file in, welcoming me back as they do."
    hide ecmc
    show ecmc jacket_v2 pin determined at left3
    show korin jacket pin basic at right3
    show bird normal at right3:
        xoffset 100 yoffset 90
    "Korin starts the lesson, going over the day’s material."

    "I’m rapt with attention, focused intently on Korin. There’s just one problem..."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu pin_cu determined_cu at ecmc_cu
    "(Okay. I need to focus on what she’s actually {i}saying{/i}...)"
    hide ecmc
    show ecmc jacket_v2 pin sad at left3
    show korin jacket pin smile at right3
    show bird normal at right3:
        xoffset 100 yoffset 90
    "But it’s so hard."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu blush_cu pin_cu embarrassed_cu at ecmc_cu
    "(Not like I can help it if my heart races every time her eyes catch mine.)"

    "(Besides, I’m already familiar with a lot of the material we’re covering...)"
    hide ecmc
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(Still. That’s no excuse! I shouldn’t break her concentration...)"
    hide ecmc
    show ecmc jacket_v2 pin blush determined at left3
    show korin jacket pin basic at right3
    show bird normal at right3:
        xoffset 100 yoffset 90
    "I end up having to focus on my notes instead of looking at Korin."
    show korin jacket pin surprised
    "When I finally look up again, she gives me a quizzical look."
    show ecmc jacket_v2 pin surprised
    "I shake my head a tiny bit."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    "(I’m fine, Korin.)"
    hide ecmc
    show ecmc jacket_v2 pin smile at left3
    show korin jacket pin smirk at right3
    show bird normal at right3:
        xoffset 100 yoffset 90
    "Her words falter for just a moment, before she shakes her head with a tiny smile and continues the lecture."

    "And I find myself thinking back to last night."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu pin_cu blush_cu embarrassed_cu at ecmc_cu
    "(This thing with Korin...)"

    "(It’s more than just a crush on my hot instructor.)"
    hide ecmc
    show ecmc jacket_v2 pin sad at left3
    show korin jacket pin smirk at right3
    show bird normal at right3:
        xoffset 100 yoffset 90
    "I let out a slow breath."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(So how am I going to deal with it?)"

    scene bg ecm_generic_office_on at bg with wiperight
    stop music
    play music ecmupbeateveryday3
    pause
    "The next day, I show up to the office bright and early."

    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    "(Here we go. No debriefs with Dom and the F.D.I.. It’s my first normal day as a normal trainee!)"
    hide ecmc
    "But as the rest of us trainees file in, the person who strolls in and takes command of the room is..."
    show enver casual smile at centre
    en "Hey trainees! I’m Enver, I’ll be filling in for Korin today."

    en "So, who’s ready for a pop quiz on ARCware protocol?"

    "The class groans, and I sit up in shock."
    hide enver
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(But. . . where’s Korin?)"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
    #                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
