label korin_season1_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_generic_office_on at bg
    play music ecmtense3

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "I hesitate, feeling torn."
    "(I want to prove myself, and I don't want Korin to get in trouble.)"
    "(On the other hand...)"

    show ecmc jacket_v2_cu smile_cu
    "The possibility of a secret rendezvous with Korin spurs something inside of me."
    "(Her helping me and getting to spend extra time with her...)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show korin nojacket pin basic at right3
    mckorin "I'm in."

    show korin nojacket pin smirk at right3
    ko "This is a stressful situation for sure, but we may have a shot at solving things with our heads together."
    mckorin "It's just getting our heads together without being noticed that's the problem."

    show korin nojacket pin smile at right3
    ko "Let's meet up tonight."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "R-Really?"
    ko "Yeah, we'll go to MegaBites."
    ko "Dom and Connie will be eagle-eyed about making sure I'm not helping you, so everything's got to happen outside of HQ."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(Is she really taking me out?)"

    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Don't phrase it like that. It's not a date!)"
    hide ecmc

    show korin nojacket pin smile at right3
    show ecmc jacket_v2 pin determined at left3
    mckorin "Now I just have to figure out how to stay focused and work with all eyes on me while I'm here..."

    show korin nojacket pin smirk at right3

    ko "Look, Dom may come off as a jerk, but he genuinely has D.I.V.A.A.'s best interests in mind."
    ko "And with the F.D.I. muscling in on this case..."
    mckorin "I know, I know. I understand why he's doing what he's doing."

    show korin nojacket pin sad at right3
    ko "Sorry it all has to be secret. That must be kind of annoying for you."

    hide ecmc
    hide korin
    $menuhideborder = True
    menu korins1e4c1:
        "A. Only a little bit.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin sad at right3
            mckorin "Only a little bit. If it were secret meetings with anyone else, it'd be worse."
            mckorin "Since it's with you..."

            show korin nojacket pin smile at right3
            ko "Oh, stop flattering me."

        "B. It's part of the job.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin sad at right3
            mckorin "If I had a problem with secret meetings, being an investigator was probably the wrong line of work to begin with."

            show korin nojacket pin smile at right3
            ko "It doesn't have to be all stress, you know. If you can, try and see it as an opportunity to relax a bit."

        "C. Actually, it's kind of exciting.":
            $menuhideborder = False

            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin sad at right3
            mckorin "Actually, I'm kind of excited. This is what being an investigator is all about, right?"

            show korin nojacket pin smile at right3
            ko "Atta girl! Positive attitude. That's what I like to hear."

    mckorin "What should I do in the meantime?"
    ko "You should probably go meet Eko to get briefed on what happened to the hard drive."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "Eko?"
    "The name seems faintly familiar, but I can't place it."

    show ecmc jacket_v2 pin basic at left3
    mckorin "Any advice on what to expect from this Eko?"

    show korin nojacket pin smirk at right3
    ko "She's scary serious about her lab, so just be considerate about that."

    show ecmc jacket_v2 pin sad at left3

    mckorin "Right. Another person who's going to hate me for destroying something that was no fault of my own..."

    show korin nojacket pin smile behind ecmc at right3:
        easein 0.4 centre
    ko "Remember, Scraps--we'll get through this together, okay?"

    hide ecmc
    hide korinleft2
    show korin nojacket_cu smile_cu at korin_cu
    "Korin's hand is soft in mine, warm and reassuring...and I'm surprised at how reluctant I am to let it go."
    hide korin

    "But as soon as I realize that, I drop it, say my goodbyes, and head for the lab."

    scene bg ecm_office_lab_on at bg with wiperightdissolve
    stop music
    play music ecmupbeateveryday4

    "On my way to the lab, I try to walk with my shoulders squared and my game face on."

    show eko jacket pin basic glasses at centre
    "I stop as I recognize the cheerful android I ran into while looking for Korin the other night."

    show eko jacket pin smile glasses at right3
    show ecmc jacket_v2 pin basic at left3

    ek "Hatchling [genericln]! Welcome to the lab."

    show ecmc jacket_v2 pin smile at left3
    mckorin "Um, hi! That's right, you're Eko..."
    ek "It must be hard to keep up with all the new names you're learning this week."
    mckorin "So I'm guessing you know why I'm here?"

    show eko jacket pin basic glasses at right3
    ek "I could make an educated guess based on gossip I happened to overhear from some detectives, but Korin briefed me on the details."

    show eko jacket pin smile glasses at right3
    ek "And don't worry! I don't find it productive to make the bad-faith assumptions about you that many of my colleagues did."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "Oh...thanks?"
    ek "You're welcome!"

    show ecmc jacket_v2 pin basic at left3
    mckorin "I've been tasked with recovering 'something useful' from the drive. A piece of evidence, or..."

    show eko jacket pin basic glasses at right3
    ek "Something that will keep this case in the hands of D.I.V.A.A.. I see."

    show ecmc jacket_v2 pin determined at left3
    mckorin "Do you have any ideas about what could have wiped the hard drive?"

    show eko jacket pin thinking glasses at right3
    ek "It's an unusual situation, to be sure. But yes, I have a couple theories, and even more questions."
    "Eko and I throw questions and ideas back and forth for nearly an hour or so."

    show eko jacket pin basic glasses at right3
    ek "I think the assessment that your ARCware didn't wipe the hard drive is definitely correct."
    ek "But since it's 'bricked', it will be difficult to prove that. Recovering data would require tech only available from black market dealers."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "...And you don't have anything like that here? I'd have thought this lab would have the most up-to-date stuff."

    show eko jacket pin sad glasses at right3
    "Eko stiffens a little."
    ek "My lab is up to date on all {i}licensed and approved{/i} means of extraction."

    hide eko
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Hmm. I can work with that.)"
    hide eko

    show eko jacket pin sad glasses at right3
    show ecmc jacket_v2 pin smile at left3
    mckorin "Okay, I understand. Thanks again! This has been really helpful."

    show eko jacket pin smile glasses at right3
    ek "Wonderful! Then I wish you the best of luck and hope to see you in my lab under better circumstances in the future."

    show ecmc jacket_v2 pin smile at left3:
        parallel:
            easein 0.4 xoffset -150
        parallel:
            linear 0.4 alpha 0.0
    "I thank Eko and head out of the lab, filled with purpose."

    hide eko
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Time to reach out to Skye.)"

    stop music
    play music ecmupbeateveryday3

    scene bg ecm_restaurant_night_lights at bg
    show ecmc jacket_v2 pin basic at left3
    show korin jacket pin basic at right3
    with wiperightdissolve
    "After work, Korin and I meet up at MegaBites."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(You know? I could get used to this.)"
    hide ecmc

    show korin jacket pin basic at centre
    "The server stops by to take our drink orders."
    server "Korin! Good to see you again. Hope they're not keeping you too busy over at HQ?"

    show korin jacket pin smirk at centre
    show korin jacket pin smirk at centre
    "Korin waves a hand and rolls her eyes."
    ko "You know how it is, Rhys. Same song, different dance."
    server "Well, let's get the night started off right, then. We've got some in-house cocktails...or maybe a bottle of wine to share?"

    show korin jacket pin smile at centre
    show korin jacket pin smile at centre
    ko "Two shirley temples, please."
    server "Aw, c'mon. Nothing to help you two unwind?"

    show korin jacket pin sleep at centre
    "Korin shakes her head."

    show korin jacket pin smile at centre
    ko "My colleague and I have to stay sharp for now."
    "I catch a mild hint of surprise from the server as he jots down the order."
    server "You got it, boss. Shirley temples, coming up."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Wait, did he think we were on a date?)"
    hide ecmc

    show korin jacket pin basic at right3
    show ecmc jacket_v2 pin determined at left3
    "The thought loops in my head as Korin and I peruse the menu for something to eat."

    show korin jacket pin smirk at right3
    ko "They {i}do{/i} have a good drink selection here, though."

    show ecmc jacket_v2 pin smile at left3
    mckorin "I wouldn't mind checking them out."
    "We get our drinks, order our food, and it's time to brainstorm."

    show ecmc jacket_v2 pin basic at left3
    show korin jacket pin basic at right3
    "I catch Korin up on my meeting with Eko."

    show ecmc jacket_v2 pin determined at left3
    mckorin "Eko said nothing in the lab could help me."
    mckorin "But I get the feeling there's some unregulated tech out there that can start the recovery process."

    show korin jacket pin smirk at right3
    ko "Brilliant. I can pull a few favors..."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "Actually...I have a contact of my own that might be able to help."
    "Korin raises her eyebrows, seeming impressed with me."

    show ecmc jacket_v2 pin smile at left3
    mckorin "Skye. He's a Scrapper, like me...but with different areas of expertise."

    show korin jacket pin sad at right3
    ko "That's a promising start...but in my experience, Scrappers don't usually do favors for free."
    mckorin "Not unless they really like someone."

    show korin jacket pin angry at right3

    "Korin sips her drink with an expression like she's connecting something in her head."
    mckorin "And by that I mean that Skye's had a huge crush on me since...forever. We grew up together."

    show korin jacket pin smirk at right3
    ko "Hmm. Not your type?"

    show ecmc jacket_v2 pin embarrassed blush at left3
    "I catch myself before I stumble on my words."
    mckorin "He's just...my annoying kid neighbor. I don't think I could see him that way."
    "Korin nods, thinking for a moment before she goes on."

    show korin jacket pin sad at right3
    hide ecmc
    show ecmc jacket_v2 pin determined at left3
    ko "For liability reasons, trainees aren't allowed out on official case business without a chaperone."

    show korin jacket pin basic at right3
    ko "Since Gael is your point of contact, you should get in her good graces and ask her to go with you to meet Skye."

    show ecmc jacket_v2 pin sad at left3
    "I grimace."
    mckorin "I really need her to chaperone, huh?"

    show korin jacket pin sad at right3
    ko "Technically, any D.I.V.A.A. agent could do it. But I doubt you'd have many volunteers."
    mckorin "Are you sure Gael will be cool if I tell her I'm trying to utilize illegal tech?"

    show korin jacket pin basic at right3
    ko "It's not illegal, just not at the standards that D.I.V.A.A. and the F.D.I. enforce."

    show korin jacket pin smirk at right3
    ko "And technically, {i}you're{/i} not using the tech. Skye is."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I get the feeling that Korin has done something like this herself before.)"
    "(She's already helping me so much. I should just take her advice and go with it.)"
    hide ecmc

    show korin jacket pin smirk at right3
    show ecmc jacket_v2 pin smile at left3
    mckorin "Alrighty. Gael will be Plan A."

    show korin jacket pin smile at right3
    ko "Sorry, Scraps. Better to try the official channels first. Given the circumstances, I think Gael will understand."

    show korin jacket pin smile behind ecmc at right3:
        easein 0.4 centre
    "She affectionately bumps my fist with her shoulder."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    ko "Don't worry. I think you got this!"
    hide korin

    show ecmc jacket_v2 pin embarrassed blush at left3
    show korin jacket pin smile behind ecmc at centre
    "I'm quiet as my heart swells with emotion. I want to tell her how much it means to me that she's helping me..."

    hide ecmc
    show ecmc jacket_v2 pin surprised at left3
    show korin jacket pin surprised behind ecmc at centre
    ko "What's on your mind?"

    show ecmc jacket_v2 pin sad at left3
    mckorin "It's just...you must really love this job, huh?"
    mckorin "To help out a trainee as much as you're helping me..."

    show korin jacket pin sad behind ecmc at centre
    "Korin lets out a little sigh."
    ko "As much as I try to keep my personal and professional lives separate, D.I.V.A.A. is like family to me."

    show korin jacket pin smile behind ecmc at centre
    ko "There's a lot of reasons for that, and I'm not gonna get into it tonight, but...that's why."

    show ecmc jacket_v2 pin basic at left3
    "I nod, getting it."

    show ecmc jacket_v2 pin smile at left3
    mckorin "You may not always agree with family, but you've got to be there for them no matter what."

    show korin jacket pin surprised behind ecmc at centre
    "Korin looks surprised at my insight."
    mckorin "I just hope..."

    show ecmc jacket_v2 pin sad at left3
    "For a second, I think about swallowing my words, changing the subject..."
    "But I meet Korin's eyes, and I can't help it. I say what I need to say."

    show ecmc jacket_v2 pin smile at left3
    mckorin "I just hope that when it really matters, that D.I.V.A.A. and the people who work there are there for you in the same way."

    hide ecmc
    hide korin
    "The night passes...and I feel a shift in our conversation."

    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(It's like she's letting her guard down around me. Not much, but enough that I can tell.)"
    hide ecmc

    show ecmc jacket_v2 pin basic at left3
    show korin jacket pin surprised behind ecmc at centre
    server "We change our minds on those drinks yet?"

    show korin jacket pin basic behind ecmc at centre
    "Korin gives me a thoughtful look."

    show korin jacket pin smirk behind ecmc at centre
    ko "Yeah...why not? It's been a stressful week. We've earned it."
    server "What can I get you?"

    show ecmc jacket_v2 pin surprised at left3
    "Korin pushes the menu toward me like a challenge."

    hide ecmc
    show korin jacket_cu smile_cu at korin_cu
    ko "What's your poison, Scraps?"
    hide korin

    $menuhideborder = True
    menu korins1e4c2:
        "A. Black Hat Martini.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk behind ecmc at centre
            mckorin "I'll have a Black Hat Martini."
            "The server lets out a low whistle. He points at me, but looks at Korin."
            show korin jacket pin smile behind ecmc at centre
            server "Watch out with this one. She's trouble."
            "Korin laughs him off."

        "B. DDOSmopolitan.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk behind ecmc at centre
            mckorin "The DDOSmopolitan sounds good."
            server "Does it?"
            show korin jacket pin smile behind ecmc at centre
            server "Just kidding. It's one of our best."

        "C. Meme-osa.":
            $menuhideborder = False

            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk behind ecmc at centre
            mckorin "Meme-osa for me, please."
            "The server looks up with a smirk and taps his forehead with his pointer finger."

            hide ecmc
            show ecmc jacket_v2_cu surprised_cu behind ecmc at ecmc_cu
            hide korin
            "(Uh...that must mean it's a good pick?)"
            hide ecmc

    show korin jacket pin smile behind ecmc at centre
    show ecmc jacket_v2 pin smile at left3
    ko "Ooh, that sounds good. I'll have the same."

    show ecmc jacket_v2 pin basic at left3
    "I try to get my nerves under control. The drinks, when they arrive, certainly help."

    show korin jacket pin smirk behind ecmc at centre
    ko "Ooh. Good choice, [genericfn]."
    ko "And hey, just...don't go mentioning that I bought us drinks back at HQ."

    show ecmc jacket_v2 pin smile at left3
    mckorin "Yeah...no promises. I'm telling everybody."

    show korin jacket pin smile behind ecmc at centre
    ko "Oh, come on! You'll just make the other trainees jealous."
    mckorin "Didn't you realize this was all just a long con into blackmailing you to helping me on my case after all?"

    show korin jacket pin sad behind ecmc at centre
    "Korin puts a hand to her chest in mock anguish."
    ko "Oh, nooo! Your cruel whims have left me with no choice...but to keep helping you in secret!"

    show korin jacket pin smile behind ecmc at centre
    "I enjoy the pleasant buzzing sensation, bantering back and forth with Korin until the server comes back..."
    server "Another round of drinks, detectives?"

    show ecmc jacket_v2 pin surprised at left3
    "I expect Korin to correct him on me not being an investigator yet, but..."
    ko "I think we're good, if you've got the check."

    show ecmc jacket_v2 pin smile at left3
    "He hands it over with a smile."
    server "You sure? You don't want to relive your wild days at the academy, huh?"
    "Korin laughs and shakes her head."
    ko "Nooo way."
    server "That wasn't so long ago, you know..."

    show korin jacket pin surprised behind ecmc at centre
    "Korin glances my way, then back to him with a mock whisper."
    ko "Shh! She's not supposed to know about that!"

    show korin jacket pin smirk behind ecmc at centre
    "Korin takes the check, signing off on the bill for both of us. The server looks at me."

    show ecmc jacket_v2 pin surprised at left3
    server "You want dirt on Korin, you come back again and talk to me."
    ko "This is extortion, right? I pay, you go away?"
    server "Yeah, you tip it, I zip it."

    show ecmc jacket_v2 pin basic at left3
    server "But your {i}colleague{/i} looks like she's got a solid lead..."
    "Korin shoves the bill at him, her voice sing-song like she's trying to tell him to go away."

    show korin jacket pin smile behind ecmc at centre
    ko "Have a good night, Rhys!"
    "The server bids us goodnight. I know it's late, and I could go home, but..."

    show korin jacket pin basic behind ecmc at centre
    ko "So, the secret's out. I'm not the buttoned-up hardass that you thought I was."

    show ecmc jacket_v2 pin smile at left3
    mckorin "Right. Because {i}that{/i} was my impression of you."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(Still...it's like a whole new side of her that's opened up to me.)"
    hide ecmc

    show korin jacket_cu smirk_cu at korin_cu
    ko "The stories I could tell you...even just one story..."
    "Her voice tantalizingly trails off."
    ko "Well, I'll leave that up to you. I know it's late."
    hide korin

    $menuhideborder = True
    menu korins1e4c3:
        "A. Listen to Korin about her wild academy days." (paidchoice = "paidchoice"):
            $menuhideborder = False
            hide korin
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "I mean, it'd be irresponsible of me not to follow up on a lead."

            show ecmc jacket_v2_cu basic_cu at ecmc_cu:
                xoffset -230
            show korin jacket_cu smile_cu at korin_cu:
                xoffset 250
            "Korin laughs and brushes her hair back from her face as she leans in and starts her story."
            ko "So, I know how this is going to sound..."
            ko "But being a club rat in my academy days was my way of letting off steam."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "I can't hide the surprise on my face, and Korin rushes to explain herself."

            show korin jacket_cu surprised_cu at korin_cu
            ko "Not like...I mean, there was a bit of drinking involved, sure!"

            show korin jacket_cu smile_cu at korin_cu
            ko "But that's not why I went. I liked dancing. I still do, actually. And it was the perfect way to de-stress."
            mckorin "Dancing? Really?"

            show korin jacket_cu surprised_cu at korin_cu
            ko "In my final year at the academy, you know...things get pretty stressful. So I went dancing like...five nights a week?"
            "My jaw drops."

            show korin jacket_cu smirk_cu at korin_cu
            ko "Back then, it was just the perfect way to turn off my brain and get physical, you know?"

            show ecmc jacket_v2_cu determined_cu at ecmc_cu
            "I allow myself to imagine it: the flashing lights, the pounding beat..."
            "And Korin at the center of it all, happy and carefree...shaking her hair, moving her body..."

            hide korin
            show ecmc jacket_v2_cu embarrassed_cu blush_cu at ecmc_cu:
                xoffset 0
            "(Speaking of turning off my brain...)"
            hide ecmc

            show korin jacket_cu embarrassed_cu blush_cu at korin_cu:
            "Korin covers her face, embarrassed."

            show korin jacket_cu surprised_cu at korin_cu:
                xoffset 250
            show ecmc jacket_v2_cu smile_cu at ecmc_cu:
                xoffset -230
            ko "That look you're giving me. Oh my god."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mckorin "N-No! It's just..."
            "I grasp frantically for something to say. Something that isn't the truth."

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "I just didn't figure you were the type."

            hide korin
            show korin jacket_cu smirk_cu at korin_cu:
                xoffset 250
            show ecmc jacket_v2_cu basic_cu at ecmc_cu
            "Korin folds her arms."
            ko "What, the {i}cool{/i} type?"

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "No, no. I knew you were the cool trainer."

            show korin jacket_cu sleep_cu at korin_cu
            "Korin shakes her head."

            show korin jacket_cu basic_cu at korin_cu
            ko "Not now. No training happening here. This story is the opposite of instructive, believe me."

            show ecmc jacket_v2_cu basic_cu at ecmc_cu
            ko "My habits didn't really change when I started as a trainee."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mckorin "I don't know how you managed to keep up the energy to show up for work the next day."

            show korin jacket_cu smirk_cu at korin_cu
            "Korin gives me a knowing look."
            ko "So we were assigned this group project where we had to do a physical field exam with fellow trainees."

            show korin jacket_cu sad_cu at korin_cu
            show ecmc jacket_v2_cu basic_cu at ecmc_cu
            ko "My team just...wasn't clicking."

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "Do you think it was because one group member was going clubbing five nights a week, or...?"

            show korin jacket_cu smirk_cu at korin_cu
            "Under the table, I feel Korin's foot nudge my shin in response to my teasing her."
            ko "Hey, I made it work. You wouldn't imagine how many leads come your way when people think you're just a drunk party girl."

            show korin jacket_cu basic_cu at korin_cu
            show ecmc jacket_v2_cu basic_cu at ecmc_cu
            ko "But it was more than that. Our personalities clashed. There wasn't a lot of trust."

            show korin jacket_cu smile_cu at korin_cu
            ko "So...I took it upon myself to change that. Through the wholesome power of clubbing."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mckorin "And that...worked?"
            ko "Why do you doubt my methods? You think I'd be where I am today if it didn't work? Of course it worked!"

            show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
            mckorin "Sorry, sorry. I need to learn to trust the process. Go on."
            ko "I took them out dancing with me. I got everyone drinks, got people to loosen up a bit..."

            show korin jacket_cu sad_cu at korin_cu
            ko "Well, one of the group members got a little rowdy, and mouthed off to a bouncer."
            ko "She was about to get thrown out, and I stepped in."

            show korin jacket_cu smirk_cu at korin_cu
            "She puts her hands on her hips and thrusts back her shoulders."

            show korin jacket_cu angry_cu at korin_cu
            ko "I was like, 'You're interfering in official D.I.V.A.A. business!' And somehow, that's what it took."

            show korin jacket_cu smirk_cu at korin_cu
            show ecmc jacket_v2_cu basic_cu at ecmc_cu
            ko "Someone else from the group stepped in, pretended to be my partner..."
            ko "Somehow talked them into getting us a VIP room and comped drinks."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mckorin "No way."

            show korin jacket_cu sad_cu at korin_cu
            ko "Which was a huge mistake. We drank way too much."

            show korin jacket_cu smirk_cu at korin_cu:
                xoffset 250
            show ecmc jacket_v2_cu basic_cu at ecmc_cu:
                xoffset -230
            ko "But somehow, when the end of the night came, that managed to pull us closer together."
            ko "Someone in the group said we could crash at their place nearby if someone else covered the ride..."
            ko "We got there, everyone helped each other in finding places to sleep..."

            show korin jacket_cu smile_cu at korin_cu
            ko "I made sure everyone was hydrated, set our alarms, and even set up breakfast for delivery in the morning."

            hide korin
            show ecmc jacket_v2_cu smile_cu at ecmc_cu:
                xoffset 0
            "(Even in training, she was the responsible one.)"

            show korin jacket_cu smile_cu at korin_cu:
                xoffset 250
            show ecmc jacket_v2_cu basic_cu at ecmc_cu:
                xoffset -230
            ko "So the next day, when we had our bright and early field exam..."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mckorin "...Everyone passed?"

            show korin jacket_cu smirk_cu at korin_cu
            ko "{i}Barely{/i}. But yeah, we did."

            show korin jacket_cu smile_cu at korin_cu
            ko "And that's why I always try to have people's backs. You never know when it might pull you together for something amazing."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu:
                xoffset 0
            "(That's why she helped me.)"

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(I wonder if she thinks this is as amazing as I do?)"
            hide ecmc

            "It's then that we both notice the time, and start making motions to head out."

        "B. Call it a night.":
            $menuhideborder = False
            show korin jacket pin sad behind ecmc at centre
            show ecmc jacket_v2 pin sad at left3
            mckorin "Let's call it. You're right, it is late..."
            "Korin's face falls, and she nods."

    show korin jacket pin surprised at centre
    show ecmc jacket_v2 pin basic at left3
    ko "Okay. But, before you go..."

    play sound "audio/sfx/phone 02.mp3"

    show korin jacket pin basic at centre
    show ecmc jacket_v2 pin surprised at left3
    "She pulls out her ARCware and sends a pulse to mine. It's an invitation to chat..."
    mckorin "...Your private channel?"

    hide ecmc
    hide korin
    show korin jacket_cu smirk_cu at korin_cu
    ko "This way we won't get caught if you need to message me something important."
    hide korin

    "She says it so casually, but as I say goodnight and head home..."
    "I can't help the feeling that it means so much more than that."

    stop music
    play music ecmtense3

    scene bg ecm_office_lab_on at bg
    show gael uniform basic glasses at centre
    with wiperightdissolve
    "I meet Gael for the first time the following day."

    hide gael
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Jeez...I knew she was an F.D.I. agent, but I really didn't think she'd be {i}this{/i} uncooperative.)"
    hide ecmc

    show gael uniform basic glasses at right3
    show ecmc jacket_v2 pin basic at left3
    "I explain to her my idea about meeting with Skye."

    show ecmc jacket_v2 pin smile at left3
    mckorin "...Just for an interview. Ideas on how I can recover this drive myself. And I'd like you there as a chaperone."

    show gael uniform angry glasses at right3
    "Gael gives an impatient little sight."
    ga "Look, I'm still trying to catch up on all these files related to this case. I'd have to determine if that'd be an appropriate use of our time."

    show ecmc jacket_v2 pin embarrassed at left3
    mckorin "So..."
    ga "So I don't know. I'll get back to you, someday. How about that?"

    show gael uniform angry glasses at right3:
        parallel:
            easein 0.4 xoffset 150
        parallel:
            linear 0.4 alpha 0.0
    show ecmc jacket_v2 pin sad at left3
    "Gael dismisses herself, and I'm left feeling helpless."

    hide gael
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Okay. So much for Plan A... I can't just wait for her to be free.)"
    hide ecmc

    show ecmc jacket_v2 pin determined at centre
    "I open up my ARCware and send my first message to Korin on her private channel."
    mckorin "Hey Korin, Plan A with Gael didn't work. Any chance you're still willing to be my backup?"

    show ecmc jacket_v2 pin determined at centre:
        easein 0.6 xoffset 50
        easein 1.2 xoffset -50
    "I pace, waiting for a reply."

    play sound "audio/sfx/phone 02.mp3"

    show ecmc jacket_v2 pin surprised at centre
    "My heart leaps as I get a message back."
    "I freeze."
    "It's from Dominick Vega."

    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "({i}...DID I JUST SEND THAT MESSAGE TO DOM?{/i})"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
