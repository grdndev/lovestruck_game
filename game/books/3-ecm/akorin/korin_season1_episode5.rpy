label korin_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_office_lab_on at bg
    play music ecmtense3

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu

    "I stare at the message from Dominick Vega, my blood pounding in my ears."
    do "Remember to follow Gael's instructions today."
    hide ecmc

    $menuhideborder = True
    menu korins1e5c1:
        "A. Don't reply":
            $menuhideborder = False
            show ecmc jacket_v2_cu basic_cu at ecmc_cu
            "I close out of the message."
            "(Maybe I'm imagining things. That didn't happen. Did it?)"

            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "But sure enough, I open my ARCware again, and it's still there."

        "B. Thanks, will do!":
            $menuhideborder = False

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "Thanks, will do!"

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "The message sends, and a little check mark tells me that he saw my reply."

        "C. What instructions?":
            $menuhideborder = False
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mckorin "What instructions?"
            do "I wasn't briefed on specifics. Just do whatever she asks of you. This shouldn't be difficult."

            show ecmc jacket_v2_cu angry_cu at ecmc_cu
            "(Okay. Jeez.)"

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "I frantically check my sent history."
    "(My message went to Korin's private channel after all. This was just a bad coincidence...)"
    hide ecmc

    show ecmc jacket_v2 pin sleep at centre
    "I rub my temples and lean against the wall, trying to slow my heart rate."

    play sound question_003

    show ecmc jacket_v2 pin surprised at centre
    "I get another message a second later, this time from Korin."
    ko "Gotcha. Taking trainee class to the central room at HQ. Maybe we'll run into each other?"

    show ecmc jacket_v2 pin surprised at centre:
        easein 0.2 yoffset -30
        easein 0.2 yoffset 0
    "I jump to my feet."

    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(She came through! Time to go meet with her...)"

    scene bg ecm_office_hq_on at bg
    show korin nojacket pin basic behind bird at centre
    show bird normal at centre, birdbob:
        xoffset 100 yoffset 90
    with wiperightdissolve

    "I find Korin, but she's in the middle of instructing the group of trainees."

    hide korin
    hide bird
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(I should be with them. If it weren't for this stupid hard drive...)"
    hide ecmc

    show korin nojacket pin smile behind bird at centre
    show bird normal at centre, birdbob:
        xoffset 100 yoffset 90
    "Korin catches my eye and gives me a subtle gesture with one finger: {i}Just a sec.{/i}"

    hide korin
    hide bird
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(...But Korin was the one who was impressed with how far ahead I was of everyone else.)"
    hide ecmc

    show korin nojacket pin smile behind bird at centre
    show bird normal at centre, birdbob:
        xoffset 100 yoffset 90
    "I listen to her, noting how graceful and passionate she is when she's instructing."

    hide korin
    hide bird
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I'm so lucky she's on my side.)"
    "(I mean, I'm sure she'd do this for anyone else in my situation, but...)"
    hide ecmc

    show ecmc jacket_v2 pin basic at left3
    show korin nojacket pin smile behind bird at right3
    show bird normal at right3, birdbob:
        xoffset 100 yoffset 90
    "Korin wraps up her lesson and lets the trainees get to work. She walks over to me, speaking a little louder than normal."

    show bird normal at right3, birdbob:
        xoffset 100 yoffset 90
        ease 0.2 yoffset 70
        parallel:
            ease 0.4 xoffset 250
        parallel:
            linear 0.4 alpha 0.0
    ko "Hi, [genericfn]! How's that hard drive project going?"
    hide bird

    show ecmc jacket_v2 pin surprised at left3
    "I'm confused...until I see the eyes of trainees and others glancing over at the two of us."
    ko "Bet the lab is really benefiting from your tech expertise, huh?"
    "Some of the wary expressions of other trainees shift to those of envy and reverence."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Korin is...helping me save face with my colleagues?)"
    hide ecmc

    show korin nojacket pin smile at right3
    show ecmc jacket_v2 pin smile at left3
    "A warm feeling spreads inside of me."
    mckorin "Going great! Just needed a little break to stretch my legs and clear my mind..."

    show korin nojacket pin smirk at right3
    ko "Well, I was just about to get coffee for everyone while they get started on our next unit. Want to come with?"

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(It's the perfect excuse to get off-campus and catch up about my meeting with Gael!)"
    hide ecmc

    show korin nojacket pin smirk at right3
    show ecmc jacket_v2 pin smile at left3
    mckorin "Sure! If you're buying!"

    show korin nojacket pin smile at right3
    ko "Oh, you know it! But it'll be nice for you to help me carry everything."
    ko "Here, let me just figure out what everyone wants..."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(This is really happening. She's going to chaperone me at Skye's shop and help me get some sort of lead...)"
    hide ecmc

    show korin nojacket pin smile at right3
    show ecmc jacket_v2 pin smile at left3
    "I let myself indulge a little in the fantasy that I might make it out of this unscathed."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(With Korin by my side, anything seems possible.)"
    hide ecmc

    stop music
    play music ecmsuspense2

    show connie casual basic at centre:
        yoffset 50 alpha 0.0
        parallel:
            linear 0.6 alpha 1.0
        parallel:
            easein 0.4 yoffset -10
            easein 0.2 yoffset 0
    "We're just getting ready to leave, when Connie blocks our path out."

    show connie casual smile at centre
    co "Hi, agents."

    show connie casual smile at right3
    show korin nojacket pin smile at left3
    ko "Hi, Connie!"

    show connie casual angry at right3
    "Connie glares suspiciously between the two of us."
    co "Where are you two going together?"
    ko "We were just going on a coffee run for the group of trainees. Everyone's working hard, so I figured we could all use a treat."
    ko "Can I bring you back something, too? Your usual, maybe?"

    show connie casual basic at right3
    co "Oh. Um..."

    hide connie
    hide korin
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(She doesn't seem to be hiding her frustration very well.)"
    "(And Korin seems intent on killing her with kindness...)"
    hide ecmc

    show connie casual smile at right3
    show korin nojacket pin smile at left3
    co "Fine. Yeah. That'd be great. Thank you."

    show connie casual basic at right3
    ko "You bet. See you soon!"

    scene bg ecm_sidewalk_day at bg
    show korin jacket basic at centre
    with wiperightdissolve

    stop music
    play music ecmcalmeveryday4

    "We make our way across the city. Korin punches in a coffee order into her phone as I tell her everything I can about Skye."

    hide korin
    show korin jacket pin basic at right3
    show ecmc jacket_v2 pin basic at left3
    ko "Okay. We've got a couple balls in the air here, and we can't let them fall."

    show korin jacket pin smirk at right3
    ko "You know this guy better than me, so you know how to open him up, right?"

    show ecmc jacket_v2 pin surprised at left3
    mckorin "Er...well..."
    ko "Okay, that's fine. I'll help you out."
    ko "If I feel like you should butter him up, I'll twist a lock of hair around my finger. Like this."

    show korin jacket pin smile at right3
    "She demonstrates for me, and the effect makes her look..."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Don't say cute. Don't even think it.)"
    hide ecmc

    show korin jacket pin smile at right3
    show ecmc jacket_v2 pin determined at left3
    mckorin "Okay."

    show korin jacket pin smirk at right3
    ko "And when I think it's time to be cold, I'll kind of tug on my earlobe, like this."
    ko "Got it?"
    mckorin "I think so..."

    show korin jacket pin smile at right3
    ko "Trust me, it'll work. You got this!"

    scene bg ecm_pawn_shop_off at bg
    show skye casual basic at centre
    with wiperightdissolve

    stop music
    play music ecmupbeateveryday3

    "Skye looks up from behind the counter as we enter the empty pawn shop."

    show skye casual surprised at centre
    "His eyes are wide with interest at first, but as we get closer, I see his expression tighten into a suspicious scowl."

    show skye casual angry at right3
    show ecmc jacket_v2 pin basic at left3
    mckorin "Hey, Skye..."

    hide skye
    hide ecmc
    $menuhideborder = True
    menu korins1e5c2:
        "A. Long time, no see!":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show skye casual angry at right3
            mckorin "Long time, no see, buddy!"

            show ecmc jacket_v2 pin basic at left3
            show skye casual surprised at right3
            sk "{i}Buddy{/i}?"

            hide skye
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(Worth a shot.)"
            hide ecmc

            show korin jacket pin basic at left3
            show skye casual angry at right3
            "Skye looks at Korin."
            sk "Who's this?"
            hide korin

        "B. Can't believe you're still working here":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left3
            show skye casual basic at right3
            mckorin "Can't believe you're still working at this scrapheap."

            show ecmc jacket_v2 pin basic at left3
            sk "You follow your dad's footsteps, I'll follow mine."

            hide ecmc
            show korin jacket pin basic at left3
            show skye casual angry at right3
            "He nods at Korin."
            sk "Who're you?"

        "C. We need your help":
            $menuhideborder = False
            show ecmc jacket_v2 pin determined at left3
            show skye casual angry at right3
            mckorin "We need your help."

            hide ecmc
            show korin jacket pin basic at left3
            show skye casual angry at right3
            "Skye looks Korin up and down."
            sk "Who's 'we'?"

    hide korin
    show skye casual basic at right3
    show ecmc jacket_v2 pin determined at left3
    mckorin "This is Griffin Detective Korin Reyes, my..."

    hide ecmc
    show korin jacket pin smile at left3
    ko "Partner."
    "I look over at her in surprise, but Korin stays fixated on Skye."

    hide skye
    hide korin
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(...Did she just say what I think she just said?)"
    hide ecmc

    show skye casual basic at right3
    show korin jacket pin smile at left3
    "She offers Skye her hand to shake, but he doesn't take it. He turns back to me."

    hide korin
    show ecmc jacket_v2 pin determined at left3
    sk "Whatever."
    sk "What brings you and your friend here to my shop?"

    hide ecmc
    show korin jacket pin basic at left3
    ko "We were hoping to see if you had any ideas about recovering data from a piece of tech we found."

    show korin jacket pin smirk at left3
    ko "[genericfn] here said you were a whiz with this kind of stuff."

    show skye casual angry at right3
    "Skye looks dubious, but doesn't dispute the claim."
    sk "What've you got?"

    show skye casual surprised at right3
    "Korin rattles off the specs. Skye raises his eyebrows and asks her to repeat herself, and Korin obliges."
    sk "That's...a really unusual type of drive."
    ko "That's what we were thinking. Strange to find it in a junkyard, right?"
    sk "I wouldn't say it's completely unheard of, but...yeah. Definitely weird."

    hide korin
    show ecmc jacket_v2 pin determined at left3
    mckorin "How much do you know about that type of drive?"

    show skye casual basic at right3
    "Skye shrugs, and I can tell he's holding something back."
    sk "About as much as you, probably."

    hide ecmc
    show korin jacket pin basic at left3
    ko "The weird thing about this drive is that it wiped itself. Self-fragmented first. Sabotage, we think."

    show korin jacket pin surprised at left3
    ko "You know anything about how to recover data like that?"

    show skye casual sleep at right3
    "Skye frowns and shakes his head."

    show skye casual basic at right3
    sk "Can't say I do. Sorry."

    show korin jacket pin basic at left3
    "I notice Korin twisting a lock of hair around her finger."

    hide korin
    hide skye
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Oh boy. Time to turn on the charm.)"
    hide ecmc

    show skye casual basic at right3
    show ecmc jacket_v2 pin smile at left3
    "I lean forward casually on the counter, putting my chin in my hands."
    mckorin "Come on, Skye...I know you're just being modest."
    mckorin "I told Reyes here if anyone would know how to crack it, it'd be you. Don't tell me I've been talking you up for nothing."

    show skye casual smug at right3
    "I see the faintest hint of a smile cross his face, as if he likes the idea that I've discussed him when he's not there."
    sk "How do I know this isn't some kind of setup? You're not trying to get me in trouble or something, are you?"

    show ecmc jacket_v2 pin embarrassed at left3
    mckorin "Sheesh, Skye. I would have hoped you thought better of me than that."

    show skye casual surprised blush at right3
    "Skye's cheeks go red. For a second, I think I have him in the palm of my hand..."

    show skye casual basic noblush at right3
    "But he clams up and goes quiet."

    hide skye
    hide ecmc
    show korin jacket_cu smirk_cu at korin_cu
    "Out of the corner of my eye, I see Korin tug on her earlobe."
    hide korin

    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Time to switch tactics.)"
    hide ecmc

    show skye casual basic at right3
    show ecmc jacket_v2 pin sad at left3
    mckorin "Well, whatever."

    show ecmc jacket_v2 pin embarrassed at left3
    "I spread my hands and back away from the counter."
    mckorin "It was worth a shot, but if you can't help us, then you can't help us."

    show ecmc jacket_v2 pin embarrassed at left3:
        easein 0.4 xoffset -80
    "I turn to leave, waving goodbye over my shoulder."

    show skye casual surprised at right3
    mckorin "See you around, Skye. Maybe."

    hide skye
    hide ecmc
    show korin jacket_cu smirk_cu at korin_cu
    "Korin follows me. In my peripheral vision, with both our backs to Skye, she holds up a hand that only I can see and gives me a thumbs up."
    "Then, she holds up her fingers, counting down."
    "{i}Three. Two. One.{/i}"
    hide korin

    show skye casual basic at right3
    show ecmc jacket_v2_cu determined_cu at ecmc_cu:
        xoffset -200
    sk "W-wait! I've maybe got a way you can recover the data. {i}Maybe.{/i}"

    show skye casual surprised at right3
    show ecmc jacket_v2_cu smile_cu at ecmc_cu:
        xoffset -200
    "I hold for a second, then turn around on my heel, patiently waiting for more."
    sk "But look, it's probably better if you guys aren't so particular about what those ways might be."

    hide ecmc
    show korin jacket pin basic at left3
    ko "We don't care what tech it is that you use, Skye. We just want the data recovered."

    hide korin
    show ecmc jacket_v2 pin smile at left3
    show skye casual smug at right3
    "Skye nods at me."
    sk "Then I'll be in touch."
    hide ecmc
    hide skye

    show korin jacket_cu smile_cu at korin_cu
    "Korin catches my eye on our way out and gives me a celebratory fist bump."
    hide korin

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(We did it!)"

    scene bg ecm_office_lab_on at bg with wiperightdissolve
    stop music
    play music ecmcalmeveryday1
    "I spend the afternoon looking over the info Skye sends me on a private channel and doing my own research."

    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(This could work. With Skye's help, I really think I might have a shot at recovering something useful!)"
    "I allow myself the small victory of remembering earlier today as Korin and I rushed back to HQ with our massive coffee order."

    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(We were both breathless. Connie sure looked suspicious, but I think we covered our tracks well enough.)"
    hide ecmc

    show ecmc nojacket_v2 pin surprised at centre
    "My ARCware buzzes with a message from Korin."
    ko "Meet me in my office? ASAP?"

    scene bg ecm_generic_office_on at bg
    show korin nojacket pin sad behind bird at centre
    show bird normal at centre:
        xoffset -20 yoffset 275
    with wiperightdissolve
    "I make it to Korin's office in record time, just to see her slumped over on her desk."

    show korin nojacket pin sad behind bird at right3
    show bird normal at right3:
        xoffset -50 yoffset 275
    show ecmc nojacket_v2 pin sad at left3
    mckorin "What's up?"
    ko "Baby Bird is...unresponsive. I'm at my wit's end."
    mckorin "Well, yeah. Can't imagine a piece of tech that went defunct around the time I was born has a lot of useful help articles."
    "Korin looks up and blows a strand of hair out of her face, her eyes pleading."

    hide ecmc
    hide bird
    hide korin
    show korin nojacket_cu sad_cu at korin_cu
    ko "Can you help?"
    hide korin

    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(With her looking like that? I literally can't say no.)"
    hide ecmc

    show korin nojacket pin sad behind bird at right3
    show bird normal at right3:
        xoffset -50 yoffset 275
    show ecmc nojacket_v2 pin smile at left3
    "Grinning, I pull on my ARCware and open up access to Baby Bird."

    show ecmc nojacket_v2 pin embarrassed at left3
    mckorin "It does look like you're running it on some old firmware, though. Poor thing."

    show korin nojacket pin smile behind bird at right3
    ko "Literally two seconds it took you to figure that out. Where have you been all my life?"

    show ecmc nojacket_v2 pin smile at left3
    "I can't think of some witty response, so I snicker as I work."
    "Korin leans back in her chair, reaching into her bag and pulling out the lunch she's packed."

    show ecmc nojacket_v2 pin embarrassed at left3
    "I subtly look on, envious as she unwraps a homemade sandwich that smells heavenly."

    hide korin
    hide bird
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Someday. Someday I'll be able to plan ahead like her and remember to bring something to eat while I'm working...)"
    hide ecmc

    show korin nojacket pin smirk behind bird at right3
    show bird normal at right3:
        xoffset -50 yoffset 275
    show ecmc nojacket_v2 pin embarrassed at left3
    "As if reading my mind, Korin speaks up."

    show korin nojacket pin smile behind bird at right3
    ko "Here. You get to eat yet?"

    show ecmc nojacket_v2 pin surprised at left3
    "She pushes half her sandwich toward me."
    mckorin "Oh, no, it's fine, I..."
    "But the sudden growl of my stomach betrays me."

    show korin nojacket pin smirk behind bird at right3
    "Korin smirks and opens a desk drawer full of utensils and dinnerware."
    ko "You gotta eat, Scraps. I can't have you falling apart on me, too."

    show ecmc nojacket_v2 pin embarrassed at left3
    "She transfers half the sandwich to a paper plate and insistently pushes it toward me."
    ko "Seriously. It's the least I can do."

    show korin nojacket pin basic behind bird at right3
    show ecmc nojacket_v2 pin basic at left3
    "I open a terminal and idly type commands with one hand and hold my sandwich in the other."

    show ecmc nojacket_v2 pin smile at left3
    mckorin "How's training going?"

    show korin nojacket pin sad behind bird at right3
    ko "I won't lie, we're running into a few issues. Some of them..."

    show korin nojacket pin sleep behind bird at right3
    "She trails off and shakes her head."

    show korin nojacket pin sad behind bird at right3
    ko "You're a trainee, too. Probably shouldn't be venting about the rest of the class to you."
    mckorin "I don't mind if you vent to me. I won't tell."

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "They're just not getting it, or what?"

    show korin nojacket pin basic behind bird at right3
    show ecmc nojacket_v2 pin basic at left3
    "Korin nods."
    ko "I kind of blame you for it, you know."

    show ecmc nojacket_v2 pin surprised at left3
    "I almost drop my sandwich."
    mckorin "Me? Why?!"

    show korin nojacket pin smirk behind bird at right3
    ko "Because you're really quick on the uptake when I explain things. And I've been spending so much time working solo with you..."
    ko "I expect them to be on the same level as you, and get tripped up when they aren't."

    hide korin
    hide bird
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(It's sweet that she cares about her trainees so much.)"

    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(But I wonder if she sees me just as one of them, or if she sees me differently...)"
    hide ecmc

    show korin nojacket pin smirk behind bird at right3
    show bird normal at right3, birdbob:
        xoffset -50 yoffset 275
    show ecmc nojacket_v2 pin basic at left3
    "After working a bit through a comfortable silence and finishing my sandwich half, I speak up."

    show ecmc nojacket_v2 pin smile at left3
    mckorin "Wanna make sure I'm not messing up your settings before I install this?"

    show korin nojacket pin smirk behind bird at right3:
        easein 0.6 xoffset -150
    show bird normal at right3:
        xoffset -50 yoffset 275
        easein 0.6 xoffset -200
    "She hops up and crosses around the desk."

    hide korin
    hide ecmc
    hide bird

    window hide
    scene bg ecm_korin_s1_ei2 with fade:
        zoom 1.3 align(0.5, 1.0)
        linear 4.0 yoffset 510
    pause
    window show
    "She leans down over my shoulder, checking the interface herself..."
    "And my cheeks grow warm as I realize I've never been this close to Korin before."

    window hide
    show bg ecm_korin_s1_ei2:
        zoom 1.3 align(0.5, 1.0)
        linear 3.0 zoom 0.65 yoffset 0
    pause
    window show
    "A curtain of her hair falls forward, and I catch just a hint of its scent--light and flowery, like a morning after rain in springtime."
    "I let myself imagine what it'd be like to stroke her hair back from her face, to fondly tuck it behind her ear like I always see her doing."
    "I stay perfectly still and watch her brown eyes skim over the interface before they light with a smile."
    "I'm hyper-aware as she puts a hand on my shoulder. I feel her thumb stroke twice in a tiny gesture of thanks."

    scene bg ecm_generic_office_on at bg
    show ecmc nojacket_v2_cu surprised_cu blush_cu at ecmc_cu:
        xoffset -230
    show korin nojacket_cu smirk_cu behind ecmc at korin_cu:
        xoffset 270
    with fade
    ko "Looks good, Scraps."

    show ecmc nojacket_v2_cu smile_cu blush_cu at ecmc_cu:
        xoffset -230
    show korin nojacket_cu surprised_cu blush_cu behind ecmc at korin_cu:
        xoffset 270
    "Korin leans away from me and lets out a huge yawn, covering her mouth and looking embarrassed."
    ko "...Sorry!"

    hide korin
    show korin nojacket_cu basic_cu behind ecmc at korin_cu:
        xoffset 270
    mckorin "Long day?"

    show korin nojacket_cu smirk_cu behind ecmc at korin_cu:
        xoffset 270
    ko "{i}Long{/i} day. But it's halfway over..."

    show ecmc nojacket_v2_cu surprised_cu blush_cu at ecmc_cu:
        xoffset -230
    show korin nojacket_cu smile_cu behind ecmc at korin_cu:
        xoffset 270
    "I find myself stifling a yawn as well, and Korin laughs."
    ko "You know, in all the excitement from earlier and trying to cover our tracks, I forgot to order coffee for the two of us..."

    show ecmc nojacket_v2_cu smile_cu blush_cu at ecmc_cu:
        xoffset -230
    ko "But if you have time for a break right now, we could go on a real coffee run together."
    "I grin, remembering earlier."
    mckorin "Run?"

    hide ecmc
    hide korin
    show korin nojacket_cu smile_cu at korin_cu
    ko "Not even a run. But an actual break. Sit and enjoy an actual coffee instead of rushing around."
    ko "How 'bout it?"
    hide korin

    $menuhideborder = True
    menu korins1e5c3:
        "A. Join Korin for a relaxing coffee run." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin nojacket pin smile at right1
            show ecmc nojacket_v2 pin smile at left1plus
            show bird normal at centre:
                yoffset 300
            mckorin "A break sounds really nice right now."
            "I hit a couple inputs on Baby Bird and get to my feet."
            mckorin "BB should be ready with that update by the time we get back."
            ko "Great. My treat, then."

            scene bg ecm_cafe_day at bg with clockwise_wipe
            "Down in the cafe Korin takes me to, one of the baristas knows her by name."

            show korin jacket pin smile at centre
            barista "Hey, Korin! Working hard, or hardly working?"

            hide korin
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(She's so friendly. Everywhere we go, she seems to know somebody...)"
            hide ecmc

            show korin jacket pin smile at centre
            ko "Hey, Cori! You know me. Same as ever..."

            hide korin
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(I'd probably be just as friendly to her if I worked at one of these places.)"
            hide ecmc

            show korin jacket pin basic at right3
            show ecmc jacket_v2 pin smile at left3
            "We get our coffee and grab seats across from one another at a small table."
            mckorin "You really know all the good places within walking distance to D.I.V.A.A., huh?"

            show korin jacket pin smile at right3
            ko "You'll know them too, before long."

            show ecmc jacket_v2 pin basic at left3
            "I sip my coffee and look around, noticing the peaceful environment."
            "Everyone here is chatting quietly, listening to music, reading or working."

            show ecmc jacket_v2 pin surprised at left3
            mckorin "I'm surprised you didn't tell me to bring some work along. This seems like just the kind of place to focus and catch up."

            show korin jacket pin basic at right3
            "Korin looks around."

            show korin jacket pin surprised at right3
            ko "What, here? No way! Never."

            show korin jacket pin smile at right3
            "She brings her coffee to her lips and closes her eyes, inhaling deep before taking a sip, her expression blissful."

            show ecmc jacket_v2 pin basic at left3
            ko "It's so quiet...I can't imagine ruining this peace by forcing myself to work."

            show ecmc jacket_v2 pin smile at left3
            mckorin "I think everyone else in here would disagree with you."
            "She takes a second and looks around at the rest of the cafe before returning her gaze to me."

            show korin jacket pin smirk at right3
            ko "Well, I'd bet my salary that everyone else in here isn't an investigator for D.I.V.A.A.."

            show ecmc jacket_v2 pin surprised at left3
            mckorin "What does that have to do with anything?"
            ko "We didn't have those fancy work cubes you guys have back when I was a rookie."

            show ecmc jacket_v2 pin smile at left3
            mckorin "Right. {i}A hundred years ago,{/i} when you were a rookie..."

            show korin jacket pin smile at right3
            "Korin laughs."
            mckorin "What did you guys have instead?"

            show korin jacket pin sad at right3
            ko "Bullpen. Big, open-office arrangement of desks. Very hard to block out the noise."
            ko "They got the cubes...two years ago, or something?"

            show ecmc jacket_v2 pin surprised at left3
            mckorin "Couldn't you use headphones?"
            "Korin shrugs."
            mckorin "Don't tell me you forgot to bring headphones! You seem like the type to have a backup pair."
            mckorin "And a backup pair for that backup pair."

            show korin jacket pin smile at right3
            "Korin chuckles, flattered."

            show ecmc jacket_v2 pin basic at left3
            ko "I got more annoyed by having to pull them out for all the constant interruptions."
            ko "Eventually, I just adapted to it. I work best when surrounded by chaos."

            show ecmc jacket_v2 pin smile at left3
            mckorin "Then you'll probably do your best work with me on this case."
            "Korin laughs again."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(Who knew it felt so good to make someone laugh?)"
            hide ecmc

            show korin jacket pin smile at right3
            show ecmc jacket_v2 pin smile at left3
            mckorin "That explains why your office door is hardly ever closed, huh?"

            show korin jacket pin smirk at right3
            "Korin nods."
            ko "More than that, it's just good to let people know I'm available if they need me."
            mckorin "You're so nice."

            show ecmc jacket_v2 pin surprised blush at left3
            "The words blurt out before I can stop them. I blush. Korin looks away, too."
            ko "I try to make a friend everywhere I make myself a regular."

            show korin jacket pin smile at right3
            ko "It helps to have contacts all over the city when you're short on leads."

            hide ecmc
            show ecmc jacket_v2 pin determined at left3
            "I put my chin in the palm of my hand, skeptical."

            show korin jacket pin surprised at right3
            ko "What?"
            mckorin "I mean, I'm sure that's part of it. But I think you're just that type of person."

            hide ecmc
            hide korin
            show korin jacket_cu basic_cu at korin_cu
            "She leans forward, meeting my gaze at eye level."

            show korin jacket_cu smirk_cu at korin_cu
            ko "What type of person?"

            hide korin
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "Warm. Kind. The type of person who makes others feel seen."
            mckorin "Not just seen, but like...special."
            hide ecmc

            show korin jacket_cu smirk_cu at korin_cu
            ko "Do I make you feel that way?"
            "I hesitate. I don't know how to put to words the way Korin makes me feel just yet."
            hide korin

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "Yeah! I mean, of course."
            mckorin "I'm sure any of the other trainees could say the same."
            hide ecmc

            show korin jacket_cu smirk_cu at korin_cu
            "Korin lets a thoughtful beat of silence pass between us."
            "My eyes stray to the clock on the wall."
            hide korin

            show korin jacket pin smirk at right1plus
            show ecmc jacket_v2 pin basic at left2
            ko "We should probably be getting back, huh?"

            show ecmc jacket_v2 pin smile at left2
            mckorin "I guess so. But this was really nice."
            scene bg ecm_generic_office_on at bg
            show bird normal at centre, birdbob:
                ypos 150
            with wiperightdissolve
            "We head back to Korin's office to find Baby Bird flitting around, dutifully ready to fill her in on what she missed on our break."

            hide bird
            show ecmc nojacket_v2 pin smile at left3
            show korin nojacket pin smile at right3
            ko "And that's me out of excuses to keep you, Scraps."
            ko "I'm glad we had this time together. Let's do it again sometime, huh?"

        "B. Stay behind and work.":
            $menuhideborder = False
            show korin nojacket pin basic at right1
            show ecmc nojacket_v2 pin sad at left1plus
            show bird normal at centre:
                yoffset 300
            mckorin "You go on without me. I think I'm just gonna power through."
            "Korin shrugs."
            ko "Aw. Well, if you're not going, no reason for me to go."
            hide bird

    stop music
    play music ecmsuspense2

    hide korin
    hide ecmc
    show connie casual basic at centre:
        yoffset 50 alpha 0.0
        parallel:
            linear 0.6 alpha 1.0
        parallel:
            easein 0.4 yoffset -10
            easein 0.2 yoffset 0
    "Just as I turn to leave, Connie appears in the door."
    co "Huh. Just as I suspected."

    show connie casual basic at right3
    show korin nojacket pin smile at left3
    "I do my best to look innocent and confused. Korin keeps her voice light and brisk."
    ko "How can I help you, Connie?"

    hide korin
    show ecmc nojacket_v2 pin surprised at left3
    co "[genericfn], Gael wants you in the lab right now."

    hide ecmc
    show korin nojacket pin surprised at left3
    show connie casual angry at right3
    co "And Korin, I need to have a word with you myself."

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
