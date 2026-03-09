label maxime_season1_episode11:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_ocean_wide_day at bg
    play music mscsurfcompetition

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc surfer_hairup basic surfboard at centre:
        yoffset 70
    "The beach itself seems to shiver with anticipation on the day of the final, as the competition finalists bob out on the water."
    hide mscmc
    show javier swim_cu smile_cu at javier_cu
    "Javier can't resist throwing me a roguish wink under his salt-streaked bangs."
    show mscmc surfer_hairup smile surfboard at left3:
        yoffset 70
    show javier swim smile at right3
    jv "You ready, hotshot? You look ready. Like you're operating on some plane of existence I don't even know about."
    "I smile secretively as we wait for the perfect waves."
    mcmax "It's something like that."
    show javier swim grin
    jv "You going to let me in on your secret?"
    show mscmc surfer_hairup smile surfboard:
        ease 0.4 yoffset 100
    "I lay down on my board, dipping my palms into the water."
    "I know Dawn and Trina are cheering for me on the beach, and Maxime is watching, intense and hopeful."
    show mscmc surfer_hairup grin surfboard
    show javier swim angry
    mcmax "Nope. Catch you at the finish line, Javier."
    show javier swim grin at out_right
    pause 0.4
    "He rolls his eyes and paddles away, leaving me alone to assess the water."
    hide mscmc
    play sound air_horn
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "The klaxon sounds, and I narrow my eyes, blocking out everything but the horizon and the feeling of the waves under my board."
    show mscmc surfer_hairup_cu sleep_cu
    "(Just me and the sea. That's what's important right now.)"
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 190
        ypos 360
    show mscmc surfer_hairup angry at centre:
        yoffset 70
    "Scanning the horizon I feel a little bit of worry enter the back of my mind but I push it away."
    show mscmc surfer_hairup surprised
    "I see the beginnings of a huge wave bulging beneath the water."
    show mscmc surfer_hairup angry
    "I know the wave is all mine when I start paddling, seemingly alone in the blue without anyone in my peripheral vision."
    hide surfboard_acc_back
    hide mscmc
    play music mscmctheme
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Just like we did yesterday, ocean—only this time, I promise there'll be no tension or hesitation from me.)"
    "(I'm going to show them me.)"
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 190
        ypos 360
    show mscmc surfer_hairup grin at centre:
        yoffset 70
        pause 0.2
        ease 0.5 yoffset 0
    pause 0.7
    "I pop=up onto my board effortlessly, reaching to plunge my hand into the wall of wave and execute a complicated cutback."
    show mscmc surfer_hairup grin:
        ease 0.4 xoffset 100
    show surfboard_acc_back behind mscmc:
        pause 0.2
        ease 0.4 xoffset 120
    "I pivot, shifting my weight and carving into the breadth of the vertical water as I ride the wave to shore at a breathtaking rate."
    mcmax "Woohoo!"
    "I shout, though no one can hear me over the ocean's roar, I feel as though nothing could ever hold me back."
    show mscmc surfer_hairup grin:
        ease 0.6 yoffset 700
    show surfboard_acc_back:
        ease 0.4 xoffset 0
    play sound crowd_applause_growing
    pause 0.4
    "As I hit the shallows, I leap neatly off my board, assailed by a wall of sound as spectators explode into cheers."
    hide mscmc
    hide surfboard_acc_back

    scene bg msc_surfcompetition_day_people at bg with wiperightdissolve
    "I look up and down the beach for Maxime as I drag my board towards the wooden lifeguard tower but I don't see him anywhere."
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(I'm glad I did well, but he's the person I want to see—!)"

    play music mscmaxime
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    "I'm suddenly enveloped in a pair of strong, warm arms, as Maxime pulls me behind the tower."
    show maxime shorts_cu basic_cu
    "He presses me back against the lifeguard tower, his body flush with mine, and looks down at me, his eyes peering deeply into mine."
    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Yes, Maxime.)"
    hide mscmc
    scene bg msc_maxime_s1_mini4 at bg with dissolve
    "He grabs me around the waist, one hand wrapped around my face, claiming my lips in a deep, passionate kiss."
    "As our mouths move together, hungrily, I instinctively melt into his arms, lifting one foot off the sand."
    "(Oh Lord, don't let this kiss ever end!)"
    "His lips are sweet and smooth, and it feels as though we were made to fit together."
    scene bg msc_surfcompetition_day_people at bg with dissolve
    show maxime shorts_cu smile_cu at maxime_cu
    "I cling to the back of his shirt, not wanting to pull away, but we eventually have to come up for air, staring at each other and breathing rapidly."
    show maxime shorts_cu embarrassed_cu
    "Everything around us seems quiet and muffled—and no one can see us behind the lifeguard tower."

    hide maxime
    $menuhideborder = True
    menu maximee11c1:
        "A. Keep kissing Maxime!" (paidchoice="paidchoice"):
            $menuhideborder = False
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mcmax "Oh Maxime, you don't know how long I've been waiting for this."
            hide mscmc
            play music mscromance
            "I grab the collar of his shirt, yanking him down to my height so I can claim his lips in another possessive kiss."
            show maxime shorts_cu smile_cu at maxime_cu
            "Maxime sighs, a happy rumble in his chest, and slides his hands around my waist, his muscular arms encircling me."
            mx "Yeah...me too."
            show maxime shorts_cu smirk_cu
            "I tilt my head, still hungrily kissing him, and he reaches up to cup my cheek, stroking my jawline with his thumb."
            hide maxime
            "My time on the water fades from memory, and the ocean sounds around us dull to the beat of our hearts, our chests pressed together."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(I almost don't care what haoppens with the competition...His lips on mine is the best reward I could hope for!)"
            hide mscmc
            show maxime shorts_cu embarrassed_cu at maxime_cu
            "Maxime chuckles at my hunger, shifting from kissing my lips to leaving a trail of kisses down my jaw."
            "He lingers on my neck, his soft lips brushing over my skin."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mcmax "Ohh, just like that..."
            hide mscmc
            "I relax into his touch, letting him push against me even further as I am pressed up against the wall of the lifeguard tower."
            "His hands close around my sides, thumbs brushing the inner curve of my hip bones."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "I tilt my head, letting out a fluttery gasp."
            hide mscmc
            show maxime shorts_cu embarrassed_cu at maxime_cu
            mx "Too much...?"
            "Maxime's voice is flustered as he turns his head, whispering in my ear."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mcmax "Just right."
            hide mscmc
            "I lay my hand over his, guiding him to press his palm flat against my lower abdomen."
            "He moans softly into my neck as his fingertips brush my damp skin where the fabric of my sun shirt ends."
            "His hands are warm on my cool, damp skin, and I cuddle up to him, my breath steaming from the salt spray and our shared body heat."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(Funny how I'm still damp from my surf, but I don't feel cold at all.)"
            "(Quite the opposite, in fact. He has me on fire, in the best way possible.)"
            hide mscmc
            "Maxime slides his hands under my thighs, hiking my up as I straddle his waist and close our height difference."
            "We continue to kiss, slower now, not so desperate but more curious, like we want to taste all of each other and leave nothing behind."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(Ooh yes, I love how big and strong he is, he lifted my up like it's nothing—!)"
            hide mscmc
            show maxime shorts_cu embarrassed_cu at maxime_cu
            "Maxime chuckles, his lips still brushing mine."
            show maxime shorts_cu smirk_cu
            mx "Mm...I'd better be careful, or I could see myself stuck like this forever with you."
            show maxime shorts_cu embarrassed_cu
            mx "It's certainly tempting."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mcmax "I'm more than okay with spending the rest of forever behind this lifeguard tower, with you..."
            hide mscmc
            "He presses a sweet kiss to my temple in response, letting his lips linger, taking his time as we both catch our breath."
            "I hum happily, as he brings his mouth once again to mine."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(He kisses so passionately for someone who is so sweet.)"
            "(We savor each other's taste as we get accustomed to one another. I love this.)"
            hide mscmc
            show maxime shorts_cu embarrassed_cu at maxime_cu
            "I press my forehead to his, opening my eyes to smile, and he grins back."
            show maxime shorts_cu smirk_cu
            "Then he tilts his head, claiming my lips in another passionate kiss..."
            "It's like the first time all over again, and I'm swept up in the passion and heat between us."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(Nestled in Maxime's arms like this, it's so easy to forget that there's a world around us...)"
            "(For so long, I've forced myself to keep my focus only on my career.)"
            "(But I've got a second dream now, and that dream is being with Maxime Okun.)"
            hide mscmc
            show maxime shorts_cu smile_cu at maxime_cu
            "Maxime brushes a kiss to my cheek, whispering in my ear."
            mx "I'm proud of you, [genericfn]."
            "I hug him tighter, my thoughts swirling happily."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mcmax "And I'm happy to be here with you, Maxime. This is everything."
            hide mscmc
        "B. Start babbling about surfing.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            mcmax "So how about surfing, huh? Pretty great right?"
            hide mscmc

    play music mschappytimes
    show trina casual smile at centre, step_in
    so "[genericfn]? [genericfn]!"
    show trina casual smile:
        ease 0.4 xoffset -60
    "I peer around the lifeguard tower and see Trina running up and down the sand, calling for me."
    show dawn casual smile behind trina at right3, step_in
    "Dawn follows at a more leisurely pace, tripping over the sand and shielding their eyes."
    hide trina
    hide dawn
    show mscmc surfer_hairup smile at left1
    show maxime shorts smile behind mscmc at right1plus
    "I look back at Maxime, and we reluctantly pull away from each other in silent agreement."
    mx "Time to return to your finalist duties."
    hide maxime
    hide mscmc
    show trina casual smile at centre:
        xoffset -60
    show dawn casual grin behind trina at right3
    dw "Ey, there they are!"
    "Dawn finally spots us and waves."
    dw "Hiding out from her legions of adoring fans, probably."
    so "Too bad, this fan wants to give you a big hug!"
    hide dawn
    hide trina
    show trina casual_cu smile_cu at trina_cu2
    "Trina pounces on me, hugging me tight and pulling me back towards the judge's podium."
    so "Come on, they're about to announce the final scores, you amazing girl!"
    hide trina
    show mscmc surfer_hairup grin at centre
    "I feel much less nervous than I did waiting for the semifinal results. I'm pracatically floating along the beach from happiness."
    hide mscmc
    show wikus casual smile at centre
    "Wikus is already mounting the podium, switching on his microphone to announce the winner."
    ws "The judges have confirmed their final tallies. I'll start with our winner so as not to keep you all in suspense."
    ws "The final winner, the surfer who'll take home the gold medal, is...[genericfn] [genericln]!"
    hide wikus
    show maxime shorts_cu embarrassed_cu at maxime_cu
    show trina casual_cu smile_cu behind maxime at trina_cu2:
        xoffset -280
    show dawn casual_cu grin_cu behind maxime at dawn_cu:
        xoffset 320
    "Maxime sweeps me up in an hug that lifts me off the sand, and Trina squeals and she and Dawn leap up and join in a big group hug."
    hide maxime
    hide trina
    hide dawn
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "For my part, I start babbling, still wrapping my head around it."
    show mscmc surfer_hairup_cu grin_cu
    mcmax "I did it—I really did it! I won!"
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    "Maxime laughs, open and happy."
    mx "You sure did, superstar!"

    scene bg msc_event_venue_lightson at bg with clockwise_wipe
    play music msclexiclub
    show mscmc jacket_hairdown smile at centre
    "My good mood carries over through the awards ceremony and afterparty where people I've never even met come up to congratulate me."
    show mscmc jacket_hairdown embarrassed
    "I flit around the hall with a glass of champagne in hand, feeling like royalty. And Maxime and I kissed!"
    show mscmc jacket_hairdown grin at left3
    show dawn jacket grin at right3
    dw "[genericfn]!"
    show dawn jacket embarrassed behind mscmc:
        ease 0.4 xpos stagepos[1]
    "Dawn catches my shoulder, and I turn to find them flushed and babbling happily..."
    hide mscmc
    show dawn jacket_cu grin_cu at dawn_cu
    "Filled with what must be more than a few glasses of champagne."
    show dawn jacket_cu sad_cu
    dw "I am {i}so proud{/i} of you...so proud. You are a beautiful sea princess."
    hide dawn
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcmax "Aw, Dawn!"
    show mscmc jacket_hairdown_cu grin_cu
    "I hug them back, ignoring their hiccups."
    mcmax "Had a bit to drink, huh?"
    hide mscmc
    show dawn jacket_cu embarrassed_cu at dawn_cu
    dw "Yeah, there's no limit on the bar. But I mean it."
    show mscmc jacket_hairdown smile at left3
    show dawn jacket sad behind mscmc at centre
    "They lean back, looking at me proudly with tears pricking their eyes."
    dw "I'm so priv...privileged to have watched you grow."
    show dawn jacket grin
    dw "Okay, I'm gonna eat some food before I faceplant."
    show mscmc jacket_hairdown grin
    show dawn jacket grin at out_right
    "I wave them off, taking the opportunity to glance around the hall."
    hide mscmc
    hide dawn
    "Everyone is laughing and enjoying the free drinks, except for one table, who are sitting morosely, their champagne glasses untouched."
    show mscmc jacket_hairdown surprised at centre
    "I recognize Raymond's trainer among them, and notice a girl sitting a little ways away, sniffling into her hands."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Poor thing...I think I saw Raymond dancing with her at the opening party.)"
    show mscmc jacket_hairdown smile at centre
    mcmax "Hey there."
    "I approach, smiling gently."
    "She looks up, blinking."
    $sidecharone="Raymond's Girlfriend"
    sid1 "Oh, hey, you're the winner—congrats! Um, sorry, let me just..."
    "She tries to wipe her eyes, streaking her mascara."

    hide mscmc
    $menuhideborder = True
    menu maximee11c2:
        "A. Offer a tissue.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at centre
            mcmax "Here, take this."
            show mscmc jacket_hairdown smile:
                ease 0.4 xpos stagepos[1]+100
            pause 0.4
            "I pull a tissue pack from my pocket, and she takes it thankfully, blowing her nose long and hard."
            sid1 "Thanks, I'd run out of tissues. I keep expecting Raymond to talk through the door like everything's normal, and then I remember."
        "B. Offer a makeup touch-up":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at centre
            "She looks at her black-streaked hand in disgust, and I quickly reach into my purse, grabbing my makeup wipes."
            show mscmc jacket_hairdown smile:
                ease 0.4 xpos stagepos[1]+100
            sid1 "Oh, thank you."
            "She dabs under her eyes, taking a deep breath and struggling to compose herself."
            sid1 "I'm such a mess."
        "C. Offer anything she needs.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at centre
            mcmax "This must be hard for you. Is there anything I can get you—water, something to eat?"
            sid1 "No, I..."
            "She hesitates, speaking up shyly."
            show mscmc jacket_hairdown smile
            sid1 "Actually, some water would be really nice. I haven't been taking great care of myself since Raymond disappeared."
            mcmax "We've got to keep you hydrated."
            show mscmc jacket_hairdown smile:
                ease 0.4 xpos stagepos[1]+100
            pause 0.4
            "I flag down a passing waiter, grabbing one of his iced water bottles and hand it to her."

    show mscmc jacket_hairdown smile at right1
    "She smiles up at me thankfully."
    sid1 "It's nice of you to check on me during your big night. I think I might head home—I haven't gotten much sleep recently."
    show mscmc jacket_hairdown grin
    mcmax "Can I walk you to your car?"
    sid1 "Thanks."
    "I'm relieved that she lets me go with her, since Wikus and his smug, knowing smile are never far from my mind."
    hide mscmc
    "I see her safely to her car, and as I make my way back down the hall..."
    show mscmc jacket_hairdown surprised at centre
    "I notice two familiar figures in close, whispered conversation near the water fountain."

    hide mscmc
    play music msctense
    show maxime casual basic at left3
    show camilla casual angry at right3
    "Maxime glances over Camilla's shoulder and spots me, a silent communication passing between us."
    "I flatten myself against the nearest wall, listening in."
    cm "Tech finally got into those files Wikus left in Maritas."
    show maxime casual angry
    cm "It's like something out of a bad horror film: he's been theorizing ways to turn humans into mers."
    show camilla casual smirk
    cm "Oh, and mind control too. Because he wasn't enough of a freak before."
    hide maxime
    hide camilla
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Sorry, he WHAT and WHAT?!)"
    hide mscmc
    show maxime casual surprised at left3
    show camilla casual angry at right3
    "Maxime raises his eyebrows, thoughts clearly racing."
    show maxime casual angry
    mx "And you wouldn't have wanted to talk so urgently if this was all purely theoretical."
    "Camilla nods, her eyes bright with vindication."
    hide maxime
    show camilla casual_cu angry_cu at camilla_cu
    cm "Wikus wouldn't have gone to the trouble of kidnapping a test subject if he wasn't ready to put his theory into practice."
    show maxime casual angry at left3
    show camilla casual angry at right3
    cm "I've got to contact HQ. Can you...?"
    mx "I won't let Sapor hurt anymore of these people. I'll do what I have to to draw him out."
    show camilla casual basic
    "Camilla nods sharply, readying to go."
    cm "Good. You have carte blanche to do whatever you think best."
    show camilla casual basic at out_right
    "Once she's left, Maxime gestures to me, and I peel off from the wall."
    hide camilla
    show maxime casual_cu sad_cu at maxime_cu
    "He's all business, but his eyes soften when he sees me."
    show mscmc jacket_hairdown surprised at left3
    show maxime casual sad at right3
    mx "Did you catch all that?"
    show mscmc jacket_hairdown sad
    mcmax "Still processing, but yeah...We need to think of something fast. Let me lure Wikus to the beach, and you can get him talking."
    show mscmc jacket_hairdown basic
    show maxime casual angry
    "I'm half-afraid Maxime will protest, but he nods, casting a wary eye back at the festivities."
    show mscmc jacket_hairdown surprised
    mx "Alright. I trust you—but be careful."
    hide maxime
    show mscmc jacket_hairdown basic at centre
    "When I make my way to Wikus, the crowd parts for me."
    hide mscmc
    show wikus casual_cu smile_cu at wikus_cu
    "He turns to me, flush with success and champagne."
    hide wikus
    show mscmc jacket_hairdown surprised at left3
    show wikus casual smile at right3
    ws "Ah, there's my champion! Were you finally able to escape all the autograph hounds?"
    show mscmc jacket_hairdown basic
    "I don't like the smug curl of his smile, but I force myself to respond casually."
    show mscmc jacket_hairdown smile
    mcmax "Actually, Maxime and I have been looking for you."

    hide mscmc
    hide wikus
    $menuhideborder = True
    menu maximee11c3:
        "A. Offer a special toast.":
            $menuhideborder = False
            show mscmc jacket_hairdown basic at left3
            show wikus casual smile at right3
            mcmax "He's got some special whiskey he's been saving for a special occasion—care to join us?"
            ws "Vintage whiskey? Don't mind if I do—lead the way, Miss [genericfn]."
        "B. Suggest a commemorative photograph.":
            $menuhideborder = False
            show mscmc jacket_hairdown basic at left3
            show wikus casual smile at right3
            mcmax "He wants to take a commemorative photo with you and I on the beach—could you spare us a few moments?"
            ws "For my gold medalist? Anything."
        "C. Tell him there's trouble on the beach":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left3
            show wikus casual smile at right3
            "I screw up my expression, seemingly apologetic."
            mcmax "I'm sorry to drag you away from the party, but there's a commotion on the beach."
            show wikus casual angry
            mcmax "Just some drunk kids fooling around on the judge's podium."
            show mscmc jacket_hairdown basic
            "Wikus sighs loudly."
            ws "Ugh, my work is never done."

    show mscmc jacket_hairdown grin at out_left
    show wikus casual basic at out_left
    "He thrusts his champagne glass at the nearest waiter and follows me out."
    hide wikus
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(That went better than I thought it would.)"
    show mscmc jacket_hairdown_cu angry_cu
    "(If Wikus is as close to enacting his 'experiment' as Camilla thinks he is...)"
    "(Maybe he's feeling preemptively victorious—and letting his guard down.)"

    hide mscmc
    scene bg msc_labeach_night at bg with wiperightdissolve
    play music mscsuspense2
    show maxime casual angry at centre
    "Once we've left the event hall behind and are walking across the beach, I see Maxime already waiting for us, watching Wikus coldly."
    hide maxime
    show mscmc jacket_hairdown basic at left3
    show wikus casual basic at right3
    "Wikus quickly realizes something's up, and he stuffs his hands in his pockets, seemingly unaffected."
    show mscmc jacket_hairdown angry
    ws "Interesting. What could possibly be the reason for this ruse?"
    hide mscmc
    show wikus casual angry
    show maxime casual angry at left3
    mx "You know the answer to that already, Sapor."
    "Wikus regards Maxime, then me, studying us in the moonlight."
    show wikus casual smile
    "Then he laughs, his face splitting into a smile that's unnervingly piranha-like."
    ws "Ah, I get it now!"
    ws "Honestly, I ought to have seen it before—you've got 'government grunt' written all over you, Okun."
    "Maxime cuts him off impassively."
    mx "I'm not interested in any of your villain monologuing. We already know what you're planning and what you've done."
    mx "What I want to know is, who's pulling your strings? Who's the man behind your curtain?"
    show wikus casual angry
    "I watch Wikus closely, wondering if Maxime's rattled him."
    hide maxime
    show wikus casual_cu smile_cu at wikus_cu
    "Wikus' expression is unreadable, then he smiles and starts to chuckle again, crowing until his laughter echoes off the water."
    hide wikus

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
