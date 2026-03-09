label van_season1_episode10:

    $tbc = False
    scene bg abandoned_house_int_moon at bg
    play music hiflsuspense
    pause

    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "After a series of shadow-jumps that each feel like the scariest, coldest roller coaster ride I’ve ever been on..."
    show hiflmc casual surprised at right1
    show li casual basic at left2 behind hiflmc
    "We finally come to a stop."

    "Li drags me into a dusty old house, long-abandoned by the looks of it."
    show hiflmc casual sarcastic
    mcvan "A dilapidated old house on the outskirts of the town?"

    mcvan "Pretty cliched, don’t you think?"
    show li casual angry
    sinli "Silence, girl."
    show hiflmc casual basic
    mcvan "I’m just saying. You have to know this is a huge mistake, right?"
    show hiflmc casual angry
    mcvan "Vanessa’s going to find me."

    mcvan "All you’re doing now is pissing her off."
    show hiflmc casual happy
    mcvan "Do you really want a vengeful Helsing with a grudge coming after you?"
    show hiflmc casual basic
    sinli "That brat? Please."
    show li casual basic
    sinli "I have faced Helsings before, ones who lived up to their name."
    show li casual angry
    sinli "No less irritating, but more competent by leagues."
    show li casual happy
    show hiflmc casual surprised
    sinli "Compared to them, your little girlfriend is but a child playing dress-up."
    hide hiflmc
    hide li
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Do not blush, [genericfn].)"
    show hiflmc casual_cu sarcastic_cu
    "(This is not the time to get flustered over someone calling Vanessa your girlfriend.)"
    hide hiflmc
    show hiflmc casual angry at right1
    show li casual basic at left2 behind hiflmc
    mcvan "Vanessa will make you eat those words."
    mcvan "What do you want with me, anyway?"
    show hiflmc casual sarcastic
    mcvan "This may come as a shock to you, but I have no interest in being a sister-wife, or whatever creepy arrangement you have going on."
    hide li
    hide hiflmc
    show li casual_cu angry_cu at li_cu
    "Li looks at me with cold hatred, so different from the act she’d put on at first."
    hide li
    show li casual angry at centre
    sinli "Believe me, I have just as little desire to see a nobody like you given such an honor."
    sinli "You are unworthy in every regard."
    sinli "Given the choice, I would drain you where you stand."
    show li casual basic
    sinli "However, I will do what it takes to resurrect the Eternal Prince of Darkness, my husband Dracula."
    show li casual angry
    sinli "And for that, I unfortunately have need of you."
    show li casual basic
    sinli "If only for the time being..."
    show li casual angry
    sinli "Regardless of how distasteful I find it, personally."
    hide li
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Did she say Dracula?!)"

    "(And what does she mean, resurrect?)"
    hide hiflmc
    show hiflmc casual surprised at right2
    show li casual basic at left2 behind hiflmc
    mcvan "Why would you need me for that?"
    show hiflmc casual sarcastic
    mcvan "Until literally just now I thought he was a fictional character."
    show hiflmc casual sad
    mcvan "I have no idea how I could possibly be of any use to you with this."

    sinli "You are a direct descendant of his runaway bride."

    sinli "Your ancestor fled from her duty, and the time has come for you to fulfill the responsibility she shirked."
    show hiflmc casual basic
    mcvan "So what happens if I refuse?"
    show hiflmc casual angry
    mcvan "Because there’s no way I’m helping you revive your dead husband."
    show li casual happy
    "For a moment, Li laughs, as if I’ve just said something genuinely funny."
    hide li
    hide hiflmc
    show li casual_cu angry_cu at li_cu
    "In the next instant, she wipes all traces of amusement from her features, her cruel red eyes burning like embers."
    hide li
    show hiflmc casual basic at right2
    show li casual basic at left2 behind hiflmc
    sinli "Do not fool yourself into thinking you have a choice in the matter."

    sinli "You are alive only because of your usefulness to me."

    sinli "Thus, when that expires, your life does as well."
    show hiflmc casual surprised
    sinli "You would do well to remember this."
    hide li
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Okay, that’s terrifying.)"
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(I just have to keep her talking until Vanessa comes to get me.)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e10c1:
        "A. What do you need me for?":
            $menuhideborder = False
            show hiflmc casual angry at right2
            show li casual basic at left2 behind hiflmc
            mcvan "But you still haven’t explained to me what you need me for."
            show hiflmc casual sarcastic
            mcvan "How am I supposed to be used for this, exactly?"
            show li casual angry
            sinli "At the moment, what I need from you is silence."

        "B. Why not mention Dracula earlier?":
            $menuhideborder = False
            show hiflmc casual surprised at right2
            show li casual basic at left2 behind hiflmc
            mcvan "So why wait to bring up the whole Dracula thing?"
            show hiflmc casual sarcastic
            mcvan "Why all the mystery and vagueness?"
            show li casual happy
            "Li laughs mockingly."
            show hiflmc casual surprised
            show li casual happy
            sinli "As if I would mention this around the Helsing spawn."
            sinli "Do I strike you as one who would make such an error in judgement?"
        "C. Why bother with the rest stop?":
            $menuhideborder = False
            show hiflmc casual sarcastic at right2
            show li casual basic at left2 behind hiflmc
            mcvan "If you're so eager to take me who-knows-where and revive Dracula, why even bother with a rest stop?"
            mcvan "Did you just do it for the aesthetic, or...?"
            show li casual angry
            "Li's expressions sours further, like she doesn't want to be here anymore than I do."
            sinli "Rest assured, were I capable of it, we'd be far from this miserable town already."
            show li casual basic
            sinli "Regrettably, even my remarkable powers are not... limitless."
    show li casual angry
    sinli "Now cease with your prattle, it is giving me a headache."
    show li casual happy
    sinli "Unless you would prefer for me to gag you."
    show hiflmc casual surprised
    "She looks sadistically amused by the concept, and I decide keeping my mouth shut is the better option for now."
    hide li
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(Come on, Vanessa, where are you...?)"
    scene bg abandoned_house_int_moon at bg with fade
    show hiflmc casual sad at right4
    show li casual basic at left4
    "We sit in uncomfortable silence for what feels like ages."
    hide hiflmc
    hide li
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Come on, [genericfn], think of something.)"
    "(You have to buy enoughg time for Vanessa to come save you.)"
    hide hiflmc
    show hiflmc casual basic at centre
    "I try to discreetly check my pockets, desperately attempting to remember what weapons Vanessa gave me for self-defense."
    show hiflmc casual sad
    "I feel my fingers close around a knife but that won't be of much use here."
    show hiflmc casual sarcastic
    "Neither will the brass knuckles."
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(There's no way I could get close neough to injure her with something like that...)"
    show hiflmc casual_cu angry_cu
    "(What else, what else?)"
    hide hiflmc
    show hiflmc casual surprised at centre
    "And then, with a jolt of excitement, I remember the blessed water grenade tucked away in one of my vest pockets."
    hide hiflmc
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Thank god for Vanessa's over protectiveness.)"
    hide hiflmc
    show hiflmc casual basic at centre
    "While Li isn't watching, I palm it, feeling out where the pin is."
    hide hiflmc
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Next time she tries something, I'll be ready...)"
    hide hiflmc
    show hiflmc casual basic at right4
    show li casual happy at left4
    "A few long moments later, Li approaches me with a satisfied smirk."
    sinli "That should suffice for now."
    show hiflmc casual surprised
    sinli "Bid farewell to your menial little town. You will never see it again."
    $menuhideborder = True
    menu vans1e10c2:
        "A. Quip at her.":
            $menuhideborder = False
            show hiflmc casual sarcastic at right4
            show li casual happy at left4
            mcvan "Thanks, but my parents taught me to never shadow-warp with strangers."
        "B. Meme at her.":
            $menuhideborder = False
            show hiflmc casual angry at right4
            show li casual happy at left4
            mcvan "Bold of you to assume I'd go anywhere with you."
        "C. Just throw the grenade.":
            $menuhideborder = False
            show hiflmc casual sad at right4
            show li casual happy at left4
            "I'm too nervous to quip, so instead I focus on not doing something stupid, like dropping the grenade."
    show li casual surprised
    show hiflmc casual angry
    "I hold out the grenade and pull the pin, throwing it at Li."
    "I immediately dash away from her, as quickly as I can."
    #white flash
    hide hiflmc
    show li casual angry at centre
    "From behind me I hear the small explosion and Li's pained screech of rage."
    sinli "You'll pay for that you insufferable little..."
    hide li
    show hiflmc casual surprised at centre
    "But I don't stick around to hear what else she calls me."
    show bg abandoned_house_moon_fog at bg with dissolve
    "I run out of the house and down the street as fast as I can, screaming for help."
    hide hiflmc
    show li casual vampireangry at centre
    "Li warps before I can get too far, glaring murder at me."
    sinli "My patience wears thin, [genericln]."
    sinli "Were you anyone else, I would eviscerate you."
    show li casual vampireangry at left4
    show hiflmc casual angry at right4
    mcvan "But you need me, so you can't kill me, can you?"
    show hiflmc casual happy
    mcvan "That must drive you nuts."
    show li casual vampirehappy
    sinli "Oh, trust me child, I can repay the suffering tenfold..."
    hide hiflmc
    show li casual vampireangry at centre
    "She's interrupted by the loud squeal of tires as a pair of familiar headlights come driving straight at her."
    play sound "audio/hifl/sfx/EngineRev_1.mp3"
    stop music fadeout 1.0
    play music hiflaction
    #bats animation
    hide li
    "Li hisses an expletive and vanishes in a swarm of bats."
    show hiflmc casual surprised at centre
    "With a loud screech, the van comes to an abrupt stop just in time to not hit me."
    "(Vanessa came for me!)"
    hide hiflmc
    show vanessa whipcasual angry at centre
    "Vanessa leaps out of the van, righteous fury emanating from her every pore."
    va "Li! You stay the {i}hell{/i} away from her!"
    hide vanessa
    show hiflmc casual surprised at centre
    "I'm captivated by the sight of Vanessa charing in to my rescue."
    "So it takes a moment to register that more people are coming out of the van."
    mcvan "Razi... JD... Everyone?! What are you all doing here?"
    hide hiflmc
    show razi djinn angry at left5
    show jd casualwings devilangry at left1 behind razi
    show mac earstank wolfangry at right1
    show diego casual vampireangry at right5 behind mac
    "They all come rushing out, transformed into their supernatural forms."
    "Together, they make a pretty impressive sight."
    hide razi
    hide mac
    hide diego
    show jd casualwings devilsmirk at centre
    "JD finds the time to joke even as they join the others in forming a protective circle around me."
    show jd casualwings devilhappy
    jd "This is our friend Vanessa and she drove us here!"
    show jd casualwings devilhappy at left3 behind mac
    show mac earstank wolfangry at right3
    Sheriff "Not the {i}time{/i} JD."
    show jd casualwings devilsad
    jd "Yeah, yeah..."
    hide jd
    hide mac
    show li casual vampireangry at centre
    "With Havenfall's finest forming a protective ring around me, Li doesn't dare come close."
    hide li
    show hiflmc casual surprised at right1 behind vanessa
    show vanessa whipcasual angry at left1
    "Vanessa cracks her whip threateningly, putting herself directly between me and Li."
    va "Come face us, coward!"
    va "I guarantee you'll never put a hand on her again."
    hide hiflmc
    hide vanessa
    show li casual basic at centre
    "Li clicks her tongue."
    show li casual surprised
    sinli "Oh, naive young Helsing."
    show li casual happy
    sinli "You mistake me for someone who fears you or cares about your opinion."
    sinli "Until next time."
    #bats
    hide li
    "With a brief, taunting wave, she vanishes into the night."
    show vanessa casual angry at centre
    "Vanessa smacks her palm with her fist, letting out a growl of frustration."
    stop music fadeout 1.0
    play music vanessa
    va "Dammit!"
    va "She got away again."
    hide vanessa
    show diego casual basic at left3
    show mac earstank wolfbasic at right3
    di "Mackenzie, can you track her?"
    Sheriff "No, it's the same problem as before."
    Sheriff "Her scent just vanishes."
    hide mac
    hide diego
    show razi djinn basic at centre
    ra "We'll find her."
    show razi djinn sad
    ra "For now, the important thing is that [genericfn] is safe."
    hide razi
    show vanessa casual sad at left2
    show hiflmc casual surprised at right2
    "Once Li's gone, Vanessa turns to me, frantic."
    va "Are you okay? Did she hurt you?"
    hide hiflmc
    hide vanessa
    show vanessa casual_cu sad_cu at vanessa_cu
    "She pats me down, turning me this way and that in her search for any hidden injuries."
    "Her gaze is so concerned, it makes my heart race with more than just adrenaline."
    hide vanessa
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(With all of her attention on me, it feels like we're the only two people in the world.)"
    hide hiflmc
    show vanessa casual sad at left2
    show hiflmc casual basic at right2
    mcvan "I'm fine. The shadow-travel was not fun, but I'm not hurt."
    show hiflmc casual basic at right3
    show vanessa casual happy at left3
    "When Vanessa's satisfied that I'm not grievously wounded and lying to her about it, she pulls back and flashes me a grin."
    va "I'm so proud of you."
    show vanessa casual smirk
    va "You escaped an ancient vampire without any help."
    va "I don't know many people who could manage that."
    show hiflmc casual happy
    mcvan "Yeah, well, the holy water grenade did most of the work."
    mcvan "I see why you like those things so much."
    show vanessa casual basic
    va "I'm glad, but that resourcefulness was all you. I didn't do anything."
    show hiflmc casual basic
    "I can see the moment she starts to blame herself, so I change the subject."
    show hiflmc casual surprised
    mcvan "What about you all? I can't believe you're all working together."
    mcvan "I never thought I'd see the day."
    show vanessa casual blush
    "A light flush spreads across her cheeks as she looks down."
    mcvan "I couldn't let my pride get in the way of saving you."
    hide vanessa
    hide hiflmc
    show razi djinn sleep at centre
    "Razi breaks the moment with a polite cough."
    hide razi
    show vanessa casual basic at centre
    "Vanessa looks up at all of them, her posture stiffening--though not as badly as it whad the other day."
    va "Thank you for helping me resue [genericfn]."
    show vanessa casual basic at left3
    show diego casual basic at right3
    "She even gives Diego a begrudging nod."
    show vanessa casual sad
    va "And thanks for... patching me up again."
    "Diego nods back."
    hide diego
    hide vanessa
    show razi djinn happy at left3
    show jd casualwings devilhappy at right3 behind razi
    "Out of the corner of my eye I notice JD smirking widely, and even Razi hides a smile behind his fist."
    hide jd
    show razi djinn happy at centre
    ra "We were glad to help. If there's anything more we can do, just let us know."
    hide razi
    show mac earstank wolfbasic at centre
    Sheriff "For now, we'll take care of patrolling the town to keep her away."
    Sheriff "You two go get some rest."
    show mac earstank wolfbasic at left3
    show hiflmc casual sad at right3
    "I nod, the rush of adrenaline beginning to give way to bone-deep exhaustion."
    hide hiflmc
    hide mac
    show diego casual basic at centre
    "Diego nods at us and vanishes into the shadows without a word."
    hide diego
    show razi djinn happy at centre
    "Razi flashes us a grin."
    ra "See you tomorrow, ladies."
    hide razi with dissolve
    "He vanishes in a poof of blue smoke."
    show jd casualwings devilsmirk at centre
    "JD winks, gives us a quick two-finger salute, and flies off."
    hide jd
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(God, that's still so weird.)"
    "(Literal, actual wings.)"
    "(What the hell.)"
    hide hiflmc
    show mac earstank wolfbasic at centre
    "Sheriff Hunt, having said her piece, takes off into the night with a huff."
    hide mac
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Yeah... That'll definitely take some getting used to.)"
    show hiflmc casual basic at right1
    show vanessa casual basic at left1
    "Vanessa puts her hand on my shoulder."
    va "Come on, [genericfn], let's get you home."
    scene bg road_night at bg with fade
    show van_back_night at bg
    show van_middle_night at bg
    show van_front_night at bg
    show hiflmc casual basic at left4 behind van_front_night:
        ypos 725
    show vanessa casual basic at right4 behind van_front_night:
        ypos 725
    stop music fadeout 1.0
    play music hiflsad
    "We drive in silence for a while as the events of the night finally start to sink in."
    show hiflmc casual sarcastic
    "(I really almost got dragged off to resurrect a dead vampire.)"
    show hiflmc casual sad
    "(How is this my life?)"
    show hiflmc casual basic
    "Vanessa's muttering pulls me out of my thoughts."
    show vanessa casual angry
    va "I can't believe I let her get away with you."
    va "I wasn't strong enough, {i}again{/i}, and she took you! Like I wasn't even there!"
    show vanessa casual sad
    va "If we hadn't gotten there in time... if I had lost you..."
    show hiflmc casual sad
    "The look on her face is so haunted, I'd do anything to make her feel better."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e10c3:
        "A. Reassure her.":
            $menuhideborder = False
            show hiflmc casual surprised at left4 behind van_front_night:
                ypos 725
            show vanessa casual sad at right4 behind van_front_night:
                ypos 725
            mcvan "But you did get there in time."
            mcvan "I'm still here and totally unharmed."
            mcvan "You haven't lost me."

        "B. Cut the tension.":
            $menuhideborder = False
            show hiflmc casual surprised at left4 behind van_front_night:
                ypos 725
            show vanessa casual sad at right4 behind van_front_night:
                ypos 725
            mcvan "Are you kidding me? You were a total badass."
            show hiflmc casual happy
            mcvan "You kicked so much vampire butt."

        "C. Stay silent.":
            $menuhideborder = False
            show hiflmc casual sad at left4 behind van_front_night:
                ypos 725
            show vanessa casual sad at right4 behind van_front_night:
                ypos 72
            "Between the exhaustion and the seriousness of the conversation, the right words just won't come to me."
            "(Better to not say anything than say the wrong thing.)"

    show hiflmc casual basic
    show vanessa casual sad
    "She still looks so broken, though."
    show vanessa_s1_mini10 at bg:
        zoom 0.4
    stop music fadeout 1.0
    play music hiflliteromance
    "I can't help but reach out and cover her hand with my own."
    hide vanessa_s1_mini10 with dissolve
    show vanessa casual surprised
    "Vanessa glances at me, eyes wide with surprise."
    mcvan "You saved me tonight."
    show hiflmc casual happy
    mcvan "You can play 'what if' all you want, but the truth is that you did come to my rescue."
    mcvan "So thank you. Seriously."
    show vanessa casual basic
    va "I've never... felt like this before. With any other civilians I've protected."
    show vanessa casual sad
    va "When I think about losing you, it hurts so much more than it ever has before."
    show hiflmc casual blush
    "Heat rushes to my face at her words."
    "(Could she...)"
    "(Could she have the same feelings for me that I do for her?)"
    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
