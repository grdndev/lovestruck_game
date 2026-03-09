label van_season1_episode9:
    $tbc = False
    scene bg van_interior_loft_lights at bg
    play music vanessa
    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show vanessa casual basic at centre
    "By the next morning, Vanessa seems to have fully recovered."
    va "I’m not happy about skipping my workout yesterday."
    show vanessa casual smirk
    va "But now I’m at a hundred percent, and I need to get back into my daily routine."
    hide vanessa
    show hiflmc casual_cu basic_cu at hiflmc_cu
    "(Vanessa doing her training regimen?)"
    show hiflmc casual_cu happy_cu
    "(I definitely want to see that.)"
    hide hiflmc
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    mcvan "Can I watch?"
    show vanessa casual surprised
    va "Of course!"
    show vanessa casual sad
    va "I’m not going to leave you by yourself– that would defeat the whole purpose."
    show vanessa casual basic
    va "Actually... teaching you some basic fighting techniques might not be a bad idea."
    show hiflmc casual surprised
    mcvan "Really? That’d be pretty cool."
    show hiflmc casual basic
    show vanessa casual smirk
    va "We passed a field the other day that should work perfectly as a training ground."
    va "Let’s get going."
    scene bg road_day at bg with fade
    pause 0.5
    show van_back_day at bg
    show van_middle_day at bg
    show van_front_day at bg
    show hiflmc casual blush at left4 behind van_front_day:
        ypos 725
    show vanessa casual basic at right4 behind van_front_day:
        ypos 725
    "Sitting in the front seat with her as we drive, I can’t help but feel kind of heightened awareness."
    "Like spending the night sleeping in her arms has made me hypersensitive to everything about her."
    "I search for something to say to fill the silence."
    show hiflmc casual surprised
    "I notice a small silver and blue hand hanging from her rear-view mirror."
    mcvan "Hey... what’s that charm?"
    mcvan "I’ve never seen anything like it."
    show vanessa casual smirk
    "Vanessa looks at where I’m pointing and smiles slightly."
    va "Oh, that."
    scene vanessa_s1_mini8 at bg with wipedown:
        zoom 0.4
    va "It’s a Hamsa."
    va "It represents the hand of Hashem, or the hand of Miriam, depending on who you ask."
    va "Like... half-lucky charm, half-protective amulet."
    scene bg road_day at bg with wipedown
    pause 0.5
    show van_back_day at bg
    show van_middle_day at bg
    show van_front_day at bg
    show hiflmc casual basic at left4 behind van_front_day:
        ypos 725
    show vanessa casual basic at right4 behind van_front_day:
        ypos 725
    va "I don’t know if it’s actually effective as an amulet, but I feel safer having it."
    show vanessa casual smirk
    va "The van is fully armored and has defense systems in place, but I like having it anyway."
    show hiflmc casual happy
    mcvan "Well, it’s beautiful."
    show hiflmc casual surprised
    mcvan "Speaking of the defense systems and weapons, though, how did you make that first vampire burn like that?"
    mcvan "Did you use silver bullets or something?"
    show hiflmc casual basic
    va "Close, but silver bullets are effective on werewolves, not vampires."
    va "For vampires, I have special blessed bullets."
    va "Generally hard to come by, but I know a guy."
    show hiflmc casual surprised
    "(She knows a guy who blesses bullets?)"
    scene bg road_day at bg with clockwise_wipe
    "We finally get to a stretch of empty grass that Vanessa deems suitable."
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    va "Why don’t you stretch while I run through my exercises?"
    show hiflmc casual surprised
    "I do my best to focus on stretching, but Vanessa’s workout is... distracting."
    show hiflmc casual blush
    "Her lithe muscles shift and flex as she goes through her routine, and I bite my lip."
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(I’m definitely staring, and I absolutely don’t care.)"
    hide hiflmc
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    "When she’s done, she jogs over to me."
    show vanessa casual smirk
    va "Okay! Let’s teach you some fighting moves."
    va "First up: punching."
    show vanessa casual basic
    va "The key to throw a really good punch is using your hips."
    va "You want your left foot forward and your right foot back, in a wide and low stance."
    va "Then twist your hips as you throw the punch."
    show vanessa casual smirk
    va "It’ll make a world of difference."
    show vanessa casual basic
    show hiflmc casual surprised
    "That’s easy enough for her to say, but it takes the better part of an hour just for Vanessa to be pleased with my footwork."
    show vanessa casual sad
    show hiflmc casual basic
    "Once I get that down, it takes ages before she’s satisfied with my right cross."
    show vanessa casual basic
    va "I think you’re getting the hang of the basic form, at least."
    show vanessa casual smirk
    va "Why don’t we try breaking holds next?"
    show vanessa casual basic at right1 behind hiflmc
    show hiflmc casual basic at left1
    "She stands behind me and wraps her arms around me in a chokehold."
    show hiflmc casual blush
    "Her entire front is pressed against my back. I resist the urge to lean back into her."
    va "To break free of this, you want to crouch on the balls of your feet, leaning forward."
    va "Then elbow your attacker in the gut to wind them, and stand up quickly and twist to the side."
    va "If I have my right arm choking you, you want to twist out of it to your right, and vice versa."
    show hiflmc casual surprised
    mcvan "Okay, I think I got that."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(Though, with Vanessa’s arms around me, escape is really the last thing on my mind.)"
    hide hiflmc
    show hiflmc casual surprised at right3
    show vanessa casual basic at left3
    "Still, I do my best to follow her instructions, and I do actually manage to escape after a few attempts."
    show vanessa casual happy
    va "Great job, [genericfn]!"
    show vanessa casual smirk
    show hiflmc casual basic
    va "Let’s keep this going– keep coming at me."
    va "Don’t be afraid to fight dirty. Just keep moving, and get creative."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e9c1:
        "A. Throw a punch.":
            $menuhideborder = False
            show hiflmc casual angry at right3
            show vanessa casual smirk at left3
            "Using the form she taught me, I aim a punch at her face, but she dodges with a grin."
            va "Nice form, but more quickly next time!"
        "B. Sweep the leg.":
            $menuhideborder = False
            show hiflmc casual_cu angry_cu at hiflmc_cu
            "(What won’t she expect?)"
            hide hiflmc
            show hiflmc casual angry at right3
            show vanessa casual basic at left3
            "I dart forward and lash out with a kick, hoping to sweep her legs out from under her."
            show hiflmc casual surprised
            "She gets knocked off balance, but rolls back into a standing position quickly."
            show vanessa casual smirk
            va "Good ! The element of surprise is your friend."

        "C. Wait for her to make the first move.":
            $menuhideborder = False
            show hiflmc casual basic at right3
            show vanessa casual basic at left3
            "I move around, waiting for an opening or for her to make the first move."
            show vanessa casual angry
            "She clicks her tongue."
            va "I thought you were going to come at me, [genericfn]."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Wait– she’s got a wide opening on her right side!)"
    hide hiflmc
    show hiflmc casual angry at right3
    show vanessa casual basic at left3
    "I aim a punch right for the hole in her defense."
    show vanessa casual smirk
    "Vanessa flashes me a mischievous grin."
    va "Got you."
    hide hiflmc
    hide vanessa
    show vanessa casual_cu smirk_cu at vanessa_cu
    "She blocks the punch and grabs my arm, and in the blink of an eye, she’s flipped me."
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(How did she do that?!)"
    hide hiflmc
    show vanessa_s1_mini9 at bg with dissolve:
        zoom 0.4
    stop music fadeout 1.0
    play music hiflliteromance
    "She lies on top of me, hands pinning mine to the ground above my head, panting."
    "(Not quite how I imagined her pinning me to the ground, but I’m definitely not complaining.)"
    hide vanessa_s1_mini9
    show vanessa casual_cu smirk_cu at vanessa_cu
    "The victorious smirk on her face is sexier than it has any right to be, especially when it’s so close to my own."
    va "I win."
    "We stay there, lying on the ground for a long moment as we catch our breath."
    hide vanessa
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(Does she have any idea what she’s doing to me right now?)"
    hide hiflmc
    show hiflmc casual blush at right2
    show vanessa casual blush at left2
    "I wiggle a little bit to get her to notice our position, and she blushes a deep red, rolling off of me immediately."
    va "...Sorry about that."
    show hiflmc casual surprised
    mcvan "You should be!"
    mcvan "I can’t believe you didn’t go easy on me in my first fight ever."
    show hiflmc casual basic
    show vanessa casual basic
    va "Your enemies won’t go easy on you, so neither will I."
    show hiflmc casual happy
    mcvan "Yeah, yeah... I think you just like winning."
    show vanessa casual happy
    "She flashes me another grin."
    va "Guilty as charged."
    show vanessa casual smirk
    va "How about another round?"
    hide hiflmc
    hide vanessa
    "Just then, a patrol car rolls up."
    show mac cop basic at centre
    "Sheriff Hunt steps out, looking like she usually does– no wolf ears in sight."
    hide mac
    show vanessa casual angry at centre
    "Vanessa goes tense next to me, the playfulness dropping from her demeanor."
    hide vanessa
    show hiflmc casual surprised at centre
    mcvan "Sheriff Hunt! What are you doing here?"
    show hiflmc casual surprised at right3
    show mac cop basic at left3
    Sheriff "I was on patrol and thought I’d check in on you, see how you’re holding up."
    Sheriff "What are you two up to?"
    show hiflmc casual basic
    mcvan "Vanessa was just teaching me how to fight."
    hide hiflmc
    show mac cop angry
    show vanessa casual basic at right3
    "She shoots Vanessa a look of disapproval."
    Sheriff "Shouldn’t you be teaching her how to defend herself, not to attack?"
    show vanessa casual angry
    va "The best defense is a good offense."
    "They stare each other down for a long, tense moment, before Sheriff Hunt sighs and turns to me."
    hide vanessa
    show mac cop basic
    show hiflmc casual basic at right3
    Sheriff "I still think you should learn some self-defense as well."
    Sheriff "If you want, I can teach you some moves."
    hide mac
    show vanessa casual angry at left3
    "Vanessa goes even more tense beside me, her expression unreadable."
    hide vanessa
    show mac cop basic at left3
    mcvan "Maybe next time? My schedule’s all booked up by Vanessa today."
    hide mac
    show vanessa casual basic at left3
    show hiflmc casual happy
    "I shoot Vanessa a grin."
    show vanessa casual happy
    "She smiles back at me, brightening slightly."
    hide vanessa
    hide hiflmc
    show mac cop basic at centre
    Sheriff "Alright. Call if you need me. I’ll be patrolling."
    hide mac
    show vanessa casual sleep at centre
    "As soon as she’s gone, all the tension drains out of Vanessa’s shoulders."
    stop music fadeout 1.0
    play music hifllitegetitdone
    show vanessa casual smirk at left3
    show hiflmc casual basic at right3
    "She turns to me eagerly."
    va "Well?"
    show vanessa casual happy
    va "You up for more training?"
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Is it just me or does she look happier than usual right now?)"
    hide hiflmc
    show hiflmc casual happy at right3
    show vanessa casual smirk at left3
    mcvan "Absolutely. And you need to show me how you did that flip thing earlier."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Let the training montage begin."
    scene bg road_night at bg with dissolve
    pause
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    "We spend the next several hours sparring, Vanessa working out on her own whenever I get too tired and need a break."
    "By the end of the day, we’re both exhausted, sweaty messes."
    show hiflmc casual sarcastic
    mcvan "God, I would kill for a hot shower right now."
    "Vanessa looks down at herself."
    show vanessa casual sad
    va "I could use one of those myself."
    show hiflmc casual basic
    mcvan "How do you usually shower?"
    mcvan "You don’t have a bathroom in the van."
    show vanessa casual basic
    "Vanessa gestures to the top of the van."
    va "I have a solar-powered water tank up there, hooked up to a shower head on the back of the van."
    show hiflmc casual surprised
    mcvan "Okay, that’s actually pretty cool."
    show hiflmc casual happy
    mcvan "But also, unnecessary."
    mcvan "I have a perfectly decent indoor shower at my house."
    mcvan "And I never invited Li in, remember? So it should be safe."
    show hiflmc casual basic
    mcvan "And I can grab some of my stuff."
    "Vanessa thinks for a moment."
    va "Alright, that should be fine."
    show van_back_night at bg
    show van_middle_night at bg
    show van_front_night at bg
    show hiflmc casual basic at left4 behind van_front_night:
        ypos 725
    show vanessa casual hatbasic at right4 behind van_front_night:
        ypos 725
    "On the drive back, we’re both too exhausted for conversation, so we ride in comfortable silence."
    scene bg heroine_home_lights at bg with fade
    show hiflmc casual surprised at centre
    "Actually going inside my house again feels weirder than I expected."
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(It’s only been a couple of days, but it feels like a lifetime...)"
    hide hiflmc
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    mcvan "You should take the first shower."
    mcvan "Clean towels are in the closet."
    show vanessa casual sad
    va "Are you sure?"
    mcvan "Yeah, I need to check my bills and stuff anyway."
    show vanessa casual basic
    va "If you insist."
    hide vanessa
    show hiflmc casual basic at centre
    "While Vanessa showers, I sort through my mail and clean the old takeout out of the fridge."
    show hiflmc casual sarcastic
    "(Bill, bill, bill... I can practically hear my bank account crying.)"
    hide hiflmc
    show vanessa casual basic at centre
    "After a while, Vanessa comes out, toweling her hair dry."
    show vanessa casual basic at right3
    show hiflmc casual basic at left3
    "I show her how to turn on the TV, and then I take my own hard-earned shower."
    scene bg heroine_bathroom_lights at bg with dissolve
    show hiflmc naked_cu noglasseshappy_cu at hiflmc_cu
    "(Hot water feels so nice after all that exercise.)"
    show hiflmc naked_cu sad_cu at hiflmc_cu
    "(I’m going to be so sore tomorrow, though...)"
    scene bg heroine_home_lights at bg with dissolve
    show vanessa casual basic at centre
    "When I get back into the living room, I find Vanessa perusing my DVD rack of cryptid documentaries."
    show hiflmc vestlesscasual basic at right3
    show vanessa casual basic at left3
    va "You have quite the collection, here."
    show hiflmc vestlesscasual happy
    mcvan "Yeah. They’re kind of my nerdy guilty pleasure."
    show vanessa casual surprised
    va "Oh? What do you like about them?"
    show vanessa casual basic
    show hiflmc vestlesscasual basic
    mcvan "Up until I knew supernatural creatures were actually real, they just made the world seem a little more magical, you know?"
    mcvan "Like, my life might be dull and ordinary, but out there the world is filled with so much more."
    show vanessa casual smirk
    va "I can understand the appeal of that."
    va "Do you have a favorite?"
    show hiflmc vestlesscasual surprised
    mcvan "Not really? I like them all for different reasons."
    mcvan "Why, did you want to watch one?"
    show hiflmc vestlesscasual basic
    va "Well, you did say you’d watch an anime I recommended when you have the time."
    show vanessa casual happy
    va "It seems only fair that I watch a documentary that you recommend."
    $menuhideborder = True
    hide hiflmc
    hide vanessa
    menu vans1e9c2:
        "A. Akkorokamui.":
            $menuhideborder = False
            show hiflmc vestlesscasual happy at right3
            show vanessa casual basic at left3
            mcvan "You like Japanese stuff, right?"
            mcvan "We could watch the documentary about Akkorokamui."
        "B. Mothman.":
            $menuhideborder = False
            show hiflmc vestlesscasual happy at right3
            show vanessa casual basic at left3
            mcvan "The Mothman documentary is definitely in my all-time top five, to be honest."
        "C. Sasquatch.":
            $menuhideborder = False
            show hiflmc vestlesscasual happy at right3
            show vanessa casual basic at left3
            mcvan "I mean, you can’t go wrong with the Sasquatch. It’s a classic."
    show hiflmc vestlesscasual happy at right3
    show vanessa casual smirk at left3
    va "I’ll admit, that does sound interesting."
    show hiflmc vestlesscasual happy at right2
    show vanessa casual smirk at left2
    "I grab a couple of sodas from the fridge, and we settle in together on the couch."
    "Watching a movie together, laughing and relaxing after a long day... I can’t help but wonder if she’s gotten to do anything like this before."
    scene bg heroine_home_lights at bg with fade
    show hiflmc vestlesscasual basic at right3
    show vanessa casual basic at left3
    stop music fadeout 1.0
    play music hifleveryday
    "After a full day of working out and a few hours of watching documentaries, we’re both exhausted."
    mcvan "Are you sure we need to spend the night in your van again?"
    show vanessa casual angry
    va "Just because you haven’t invited Li in, doesn’t mean that your house is safe."
    show vanessa casual basic
    va "Regardless, my van is even safer."
    va "Unless your house also has armor plating and rocket launchers?"
    show hiflmc vestlesscasual surprised
    mcvan "Rocket launchers?"
    mcvan "I genuinely can’t tell if you’re joking."
    show vanessa casual smirk
    "Vanessa just laughs."
    hide hiflmc
    hide vanessa
    show hiflmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(Yeah, that doesn’t help clear things up at all.)"
    hide hiflmc
    show hiflmc vestlesscasual basic at right3
    show vanessa casual basic at left3
    "Eventually, I cave in and pack a day bag with pajamas and a change of clothes."
    scene bg mc_house_ext_night at bg with dissolve
    show hiflmc casual surprised at right3
    show vanessa casual angry at left3
    stop music fadeout 1.0
    play music hiflsuspense
    "The moment we walk out the door, we’re surrounded."
    hide hiflmc
    hide vanessa
    show vampguy casual angry at centre
    "It’s impossible to tell how many vampire goons surround us with the way they keep moving in the shadows."
    hide vampguy
    show boy1 casual vampireangry at left3
    show girl1 casual vampireangry at right3
    "However many it is, we’re clearly extremely outnumbered."
    hide boy1
    hide girl1
    show hiflmc casual surprised at centre
    mcvan "I don’t see Li anywhere, but she has to be behind this, right?"
    show hiflmc casual surprised at right3
    show vanessa casual angry at left3
    va "I don’t see her either, but keep an eye out."
    show vanessa whipcasual angry at left3
    "Vanessa pulls out her whip immediately, not a trace of exhaustion showing on her features despite how tired I know she is."
    hide vanessa
    hide hiflmc
    show vampguy casual surprised
    "She cracks the ground in front of her, and a couple of the vampires back up nervously."
    hide vampguy
    show vanessa whipcasual angry at centre
    va "None of you will live to regret the mistake you made coming here tonight."
    show hiflmc casual surprised at right3
    show vanessa casual basic at left3
    "She crouches slightly and pulls out a sharp wooden stake, then tosses it to me."
    show vanessa casual angry
    "I catch it with a surprisingly minimal amount of fumbling."
    hide hiflmc
    show vanessa whipcasual angry at centre
    va "Remember what I taught you, [genericfn]."
    "She stands back up and cracks the whip again, simultaneously intimidating the vampires and giving herself time to pull out her gun."
    show vanessa whipcasual sad
    "It works, but the vampires don’t notice what I do– the near-imperceptible grimace she makes as she moves her shoulder."
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(She was acting so normal, I forgot she was still hurt!)"
    show hiflmc casual_cu sad_cu
    "(She probably aggravated it after pushing herself all day, too...)"
    hide hiflmc
    show vanessa whipcasual angry at centre
    "Unfortunately, the intimidation tactic doesn’t work for long."
    hide vanessa
    show vampguy casual basic at centre
    show boy1 casual vampirebasic at right3
    show girl1 casual vampirebasic at left3
    "The vampires begin to close in on us."
    "The closer they get, the more terrifying the sheer quantity of them seems."
    hide vampguy
    hide boy1
    hide girl1
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(She’s still injured and exhausted from training.)"
    "(I have to help her!)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e9c3:
        "A. Use your new skills to protect Vanessa." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show vanessa whipcasual angry at left2
            show hiflmc casual angry at right2 behind vanessa
            "I move closer to Vanessa, standing back to back with her as the vampires close in on us."
            va "I’ll get us out of this."
            va "I promised to protect you, didn’t I?"
            mcvan "I’ll follow your lead."
            hide hiflmc
            hide vanessa
            show boy1 casual vampireangry at centre
            "Immediately, one of the vampires darts forward, grabbing me."
            show boy1 casual vampireangry at left2
            show hiflmc casual surpriserd at right3
            stop music fadeout 1.0
            play music hiflaction
            "Without thinking, I knee him as hard as I can in the stomach."
            hide hiflmc
            show boy1 casual vampireangry at centre
            "He doubles over in pain."
            hide boy1
            show vanessa whipcasual smirk at left3
            show hiflmc casual surprised at right3
            va "Good job, [genericfn]."
            hide hiflmc
            show vanessa whipcasual angry at centre
            va "Get him while he’s distracted!"
            hide vanessa
            show hiflmc casual angry at right2
            show boy1 casual vampireangry at left3
            "Following her advice, I slam the stake right into his heart."
            hide boy1 with dissolve
            "He explodes into dust."
            hide hiflmc
            show vanessa whipcasual smirk at centre
            va "Nicely done, [genericfn]."
            "The pride in her voice drowns out some of the terror I’m feeling."
            show vanessa whipcasual angry
            "My minor victory seems to galvanize her as well, as she starts fighting even more aggressively, knowing that I’m watching her back."
            show vanessa whipcasual angry at left3
            show girl1 casual vampireangry at right3
            "Vanessa lashes her whip, ensnaring one vampire and slamming her into another."
            hide vanessa
            show girl1 casual vampireangry at left3
            show vampguy casual angry at right3
            "They lose their balance, falling into a groaning heap on the ground."
            show jdfire:
                xpos 0

            "She shoots with perfect aim once, then twice, and both vampires burst into flames."
            hide jdfire
            hide jdfire
            hide girl1
            hide vampguy
            show hiflmc casual happy at centre
            mcvan "Way to go, Vanessa!"
            hide hiflmc
            show vampguy casual angry at centre
            "One of the vampires glares murder at her."
            $sidecharone = "Vampire Goon"
            sid1 "You act all high and mighty, but you’re nothing compared to-!"
            show vampguy casual surprised at right3
            show vanessa casual angry at left1
            "She punches him right in the face."
            hide vampguy
            hide vanessa
            show hiflmc casual sad at centre
            mcvan "Ooh, that had to hurt."
            hide hiflmc
            show vampguy casual angry at centre
            "He gets back up, rubbing his sore jaw and spitting blood onto the ground."
            sid1 "You'll pay for that."
            show vampguy casual angry at left3
            show hiflmc casual happy at right3
            mcvan "Will she?"
            mcvan "Because from where I’m standing she’s beating you pretty easily."
            hide hiflmc
            hide vampguy
            show vanessa whipcasual angry at centre
            "Vanessa dodges out of the way of another punch and cracks her whip into one of the vampires’ faces."
            show vanessa whipcasual basic
            va "Don’t get distracted by banter, [genericfn]."
            show vanessa whipcasual angry at left3
            show boy1 casual vampireangry at right3
            "He stumbles backward as she slams the butt of her gun down on another vampire’s head."
            hide boy1
            show vanessa whipcasual angry at centre
            va "On your right!"
            hide vanessa
            show hiflmc casual surprised at right3
            show girl1 casual vampireangry at left3
            "A vampire leaps at me, but thanks to Vanessa’s warning I dodge out of the way just in time."
            hide girl1
            hide hiflmc
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(She’s fighting four vampires by herself, and she still has the time to watch out for me.)"
            hide hiflmc
            show heroine_s1_mini1 at bg
            "Out of the corner of my eye, I spot the garden rake that we almost never use."
            hide heroine_s1_mini1
            show hiflmc casual surprised at centre
            "(That wouldn’t work, would it...?)"
            show hiflmc casual surprised at right3
            show girl1 casual vampireangry at left3
            "The next time the vampire lunges at me, I drop to the ground and grab it, holding it upside-down to shield my face."
            show girl1 casual vampireangry
            "She stares at me, baffled."
            show girl1 casual vampireangry
            show jdfire at left3 behind girl1:
                xpos -300
            "The distraction gives Vanessa time to fire off another perfectly aimed shot, and the vampire burns."
            hide girl1
            hide jdfire
            show hiflmc casual surprised at centre
            mcvan "Not exactly how I saw that going, but at least it worked."
            show hiflmc casual basic at right1 behind vanessa
            show vanessa whipcasual basic at left1
            "I move, standing shoulder-to-shoulder with Vanessa."
            show vanessa whipcasual angry
            va "Let's end this."
            "The rake does make it easier to block their attacks."
            hide vanessa
            show girl1 casual vampireangry at left2
            show hiflmc casual angry at right2
            "One comes at me, trying to push me to the ground."
            show girl1 casual vampireangry at left3
            show hiflmc casual angry at right3
            "While she’s busy trying to overpower me with her arms, I’m able to knock her off balance by hitting her legs with the rake."
            hide hiflmc
            hide girl1
            show vanessa_s1_mini1 at bg with wiperight
            "As soon as she hits the ground, Vanessa shoots."
            hide vanessa_s1_mini1
            show hiflmc casual happy at centre
            mcvan "Nice teamwork!"
            hide hiflmc
            show vampguy casual surprised at centre
            "The remaining vampires finally start to look nervous, realizing how badly this fight is going for them."
            show vampguy casual surprised at left4
            show hiflmc casual angry at right3
            mcvan "Not so brave without numbers on your side, huh?"
            hide hiflmc
            hide vampguy
            show vanessa whipcasual angry at centre
            "With a flick of her wrist, Vanessa snaps the whip around one of the goons, dragging him to his knees."
            "Vanessa fires two loud shots in quick succession."
            hide vanessa
            show jdfire at centre:
                xpos 0
            "He bursts into flame, along with another behind me who I hadn’t noticed."
            hide jdfire
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(That one nearly got me while I was distracted!)"
            "(Vanessa makes multitasking look so much easier than it is...)"
            hide hiflmc
            show hiflmc casual angry at centre
            mcvan "Teleporting in the middle of a fight? Rude."
            show hiflmc casual basic at right3
            show vanessa whipcasual angry at left3
            va "Rude or not, they have that ability and will absolutely use it."
            va "Try to keep better track of your surroundings!"
            show hiflmc casual angry
            mcvan "Noted!"
            hide hiflmc
            hide vanessa
            show girl1 casual vampireangry at centre
            "There’s only one vampire left."
            "She snarls at us with the most violent look of hatred on her face, before turning around and attempting to flee."
            hide girl1
            show vanessa whipcasual angry at centre
            va "Oh, it’s too late for that."
            show vanessa whipcasual angry at left3
            show girl1 casual vampireangry at right3
            "With one last perfect swing of her arm, the whip arcs out and wraps around the vampire’s middle, keeping her in place."
            "Vanessa shoots her gun once more."
            hide girl1
            show jdfire at right3
            "The vampire erupts into fiery ash and embers."
            hide jdfire
            show hiflmc casual sad at right3
            show vanessa whipcasual sad
            "We stand there for a moment, panting."
            show hiflmc casual surprised
            mcvan "We really did it!"
            show hiflmc casual happy
            show vanessa whipcasual basic
            "I grin at Vanessa, expecting her to be glowing with victory, but her expression is as serious as I’ve ever seen it."
            show hiflmc casual surprised
            show vanessa whipcasual angry
            va "Celebrate later, run now!"
            va "Get to the van as quickly as you can!"
            va "I’ll be right behind you."
        "B. Defend yourself.":
            $menuhideborder = False
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Then again... she’s got a lifetime of training.)"
            "(I’d probably just get in her way.)"
            show hiflmc casual_cu sarcastic_cu
            "(Besides, I have enough to worry about over here.)"
            hide hiflmc
            show boy1 casual vampireangry at right3
            show girl1 casual vampireangry at left3
            "While most of the vampires converge on Vanessa, pegging her as the bigger threat, a couple of them approach me."
            hide girl1
            hide boy1
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Thank god Vanessa taught me those moves today!)"
            hide hiflmc
            show hiflmc casual surprised at right3
            show vampguy casual angry at left3
            stop music fadeout 1.0
            play music hiflaction
            "One of them lunges at me, but I dodge back and he misses by a hair."
            show hiflmc casual angry
            mcvan "Not today, you horror movie reject."
            show hiflmc casual angry at right2
            show vampguy casual surprised at left2
            "In the brief opening, I punch him as hard as I can in the sternum, doing my best to twist my hips the way Vanessa taught me."
            hide hiflmc
            show vampguy casual surprised at centre
            "He staggers back and doubles over."
            hide vampguy
            show hiflmc casual sad at centre
            mcvan "Ow, jeez."
            "I shake my hand out, grimacing."
            show hiflmc casual sarcastic
            "(Vanessa didn’t tell me how badly actually punching people hurts your hand...)"
            show hiflmc casual suyrprised at right3
            show girl1 casual vampireangry at left3
            "Another vampire swipes at me while I’m distracted."
            $sidecharone = "Vampire Goon"
            sid1 "You little..."
            show hiflmc casual angry at right1
            "I manage to block her with the stake just in time."
            "Using the technique Vanessa taught me, I grab the vampire’s wrist and flip her."
            hide hiflmc
            show girl1 casual vampireangry at centre
            sid1 "Ngh!"
            "She lands on her back with a stunned look on her face."
            hide girl1
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(I can’t believe that worked!)"
            hide hiflmc
            show hiflmc casual angry at right3
            show girl1 casual vampireangry at left1
            "Before she has a chance to get up and recover, I slam down and drive the stake into her, as hard as I can."
            hide girl1 with dissolve
            "She disappears into a poof of dust."
            show hiflmc casual surprised
            mcvan "Holy shit, I actually staked one."
            hide hiflmc
            show vanessa whipcasual angry at centre
            "I look over to where Vanessa is fighting half a dozen vampires by herself."
            "She seems to be holding her own just fine, despite her injury."
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(If even I could dust one, that’s nowhere near her level.)"
            hide hiflmc
            show vanessa whipcasual angry at centre
            "Even the sheer number doesn’t seem to bother her, as she uses their disorganization and lack of teamwork against them."
            hide vanessa
            show hiflmc casual_cu angry_cu at hiflmc_cu
            "(She really is amazing at this.)"
            hide hiflmc
            show hiflmc casual surprised at right4
            show vampguy casual angry at left3
            "I don’t get to admire her for long before more vampires come swinging at me."

            mcvan "Yikes."
            hide vampguy
            show jdfire at left5:
                xpos -500
            "Before one gets a chance to hit me, a shot rings out and he disintegrates into burning embers."
            hide jdfire
            show hiflmc casual angry at centre
            mcvan "I’m no one’s midnight snack!"
            hide hiflmc
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(Even in the middle of her own fight, she’s still watching out for me...)"
    hide hiflmc
    hide vanessa
    stop music fadeout 1.0
    play music hiflsuspense
    show li casual basic at centre with dissolve
    "Just then, Li steps out of the shadows, directly in front of Vanessa."
    show li casual vampireangry
    "She clicks her tongue."

    li "I see my underlings have failed to kill you."
    show li casual vampireangry at right3
    show vanessa whipcasual angry at left3
    va "Did you really think your lackeys could take me out?"
    show li casual vampirebasic
    li "I had hoped they would prove more competent, true."
    li "But alas, it seems good help is hard to find."
    li "I suppose the saying is true..."
    show li casual vampireangry at centre
    show vanessa whipcasual sad
    "Before I can do anything, Li slashes Vanessa in the shoulder, reopening her injuries from the other day."

    li "If you want something done right, do it yourself."
    hide li
    hide vanessa
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(That underhanded-!)"
    hide hiflmc
    show vanessa casual sad at centre
    "Vanessa cries out in pain, dropping to her knees."
    hide vanessa
    show li casual vampireangry at left1 behind hiflmc
    show hiflmc casual surprised at right1
    "I reach out for her, but Li appears next to me in an instant."

    hide li with dissolve
    hide hiflmc with dissolve
    "Her cold hands clamp down on my arm as we disappear into frigid darkness."
    $tobecontinued()
    scene bg hifltbc at bg
    with fade
    pause
    $ resets()
