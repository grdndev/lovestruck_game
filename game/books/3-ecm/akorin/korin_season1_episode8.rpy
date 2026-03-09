label korin_season1_episode8:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_office_lab_on at bg
    play music ecmemotional1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show korin nojacket_cu sad_cu at korin_cu
    "I wake up on the floor. Standing over me is..."

    scene bg ecm_korin_s1_mini1:
        zoom 1.3 pos(-520, -290)
    ko "[genericfn], can you hear me?! Are you okay?"
    "Korin gently checks my pulse while searching my eyes."
    "If my heart wasn't in trouble before, it is now."
    "(What is she doing here? Is she here for me?)"
    "As thrilled I am at the thought, my pain catches up with me."

    scene bg ecm_office_lab_on at bg
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    with dissolve

    "I wince, feeling the back of my head."
    mckorin "I think I fell out of my chair."


    hide ecmc
    show korin nojacket_cu pin_cu surprised_cu at korin_cu
    ko "It was something worse than that. Eko said the terminal you were at just...exploded!"

    show korin nojacket_cu pin_cu sad_cu at korin_cu
    ko "Maybe I should call someone..."
    hide korin

    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    mckorin "No! It's okay. Don't go."
    hide ecmc

    show korin nojacket_cu pin_cu surprised_cu at korin_cu
    "I reach for her, putting a hand on her arm as I try to sit up."

    show korin nojacket_cu pin_cu sad_cu at korin_cu
    ko "You're shaking..."
    hide korin

    $menuhideborder = True
    menu korins1e8c1:
        "A. I'm fine!!":
            $menuhideborder = False
            show ecmc nojacket_v2_cu smile_cu at ecmc_cu
            mckorin "I'm fine! Really."
            hide ecmc
            show korin nojacket_cu pin_cu sad_cu at korin_cu
            "Korin looks at me, skeptical."
            hide korin

            show ecmc nojacket_v2_cu embarrassed_cu at ecmc_cu
            mckorin "...Can you just help me stand up, please?"
            hide ecmc

        "B. I'm glad you're here":
            $menuhideborder = False
            show ecmc nojacket_v2_cu smile_cu at ecmc_cu
            mckorin "I'm just glad you're here. Definitely worse sights I could wake up to..."
            hide ecmc

            show korin nojacket_cu pin_cu surprised_cu at korin_cu
            ko "Oh, boy. How hard did you hit your head?"
            hide korin

        "C. I'm a little freaked out":
            $menuhideborder = False
            show ecmc nojacket_v2_cu sad_cu at ecmc_cu
            mckorin "I'm a little freaked out...I don't even know what happened!"
            hide ecmc

            show korin nojacket_cu pin_cu sad_cu at korin_cu
            ko "I'm trying to figure that out, too..."
            hide korin

    show korin nojacket pin sad at centre:
        xoffset 80
    show ecmc nojacket_v2 pin sad at centre:
        xoffset -90
    "Korin helps me up, and it takes everything I have not to lean into her touch."
    ko "I'm so sorry. I should have checked in with you sooner."
    hide korin
    hide ecmc

    show eko casual glasses pin sad at centre
    ek "I called you down as soon as I saw what happened."

    show eko casual glasses pin sad at right3
    show ecmc nojacket_v2 pin surprised at left3:
        easein 0.1 yoffset -30
        easein 0.1 yoffset 0
    "I jump. Eko is there, hard drive in hand, looking reproachful."
    mckorin "That's the drive? You found it?"

    show eko casual glasses pin basic at right3
    ek "I did. After Korin said she was coming up to tend to you, I went to the roof to retrieve it."
    "Seeing the puzzled look on my face, she continues."
    ek "Korin asked me to alert her straight away if you ever found yourself in any sort of trouble."

    hide eko
    hide ecmc
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(She did?)"
    hide ecmc

    show korin nojacket pin smirk at centre
    "I look shyly over at Korin, who blows a strand of hair out of her face and folds her arms."
    hide korin

    show korin nojacket_cu smirk_cu at korin_cu
    ko "I mean...what kind of instructor would I be if I wasn't there for my trainees?"
    hide korin

    show korin nojacket pin smirk at left3
    show eko casual glasses pin surprised at right3
    "Eko tilts her head."
    ek "Should I follow the same protocol for other trainees as well, then?"
    ek "From the nature of our discussion, I assumed that this special attention was only warranted for [genericfn]."

    show korin nojacket pin surprised at left3
    "Korin's mouth hangs open for a second."

    hide eko
    hide korin
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(I've never seen her caught off-guard like this!)"

    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(And she won't meet my eye...)"
    hide ecmc

    show korin nojacket pin angry at left3
    show eko casual glasses pin basic at right3
    ko "Eko, look--what I want to know is what happened to [genericfn]!"
    ko "I know how you run your lab. As long as I've been here, you've never had an incident like this happen with our equipment. Right?"

    show eko casual glasses pin sad at right3
    ek "Right..."

    show eko casual glasses pin thinking at right3
    "Eko scans the damaged computer terminal with her ARCware, looking confused."
    ek "I don't exactly understand what happened. Was there any sort of warning...?"

    hide korin
    show ecmc nojacket_v2 pin sad at left3
    "I shake my head."
    mckorin "I was checking the security cam footage, like you suggested."
    mckorin "I opened one of the files, and the next thing I know, I'm on the floor."
    hide ecmc

    show korin nojacket pin sad at left3
    show eko casual glasses pin sad at right3
    "Both Korin and Eko frown in my direction."

    hide korin
    show ecmc nojacket_v2 pin surprised at left3
    mckorin "Maybe it's a case of faulty wiring?"

    show eko casual glasses pin basic at right3
    ek "I take the state of this lab very seriously...but perhaps I have fallen behind on maintenance as of late."

    show ecmc nojacket_v2 pin basic at left3
    show eko casual glasses pin sleep at right3
    "She thinks it over, then shakes her head."

    show eko casual glasses pin sad at right3
    ek "I am very, very sorry, [genericfn]."

    hide eko
    show korin nojacket pin sad at right3
    ko "I wouldn't think a terminal blowing up could be due to faulty wiring..."

    hide korin
    show eko casual glasses pin sad at right3
    ek "I'll research some potential possibilities to ensure that it does not happen again."

    hide ecmc
    show korin nojacket pin basic at left3
    ko "Is there something I can do to help, Eko?"

    show eko casual glasses pin basic at right3
    ek "Oh, no. Thank you. I get distracted from the occasional experiment, so it's possible..."
    "She trails off, then shrugs."

    show eko casual glasses pin smile at right3
    ek "I'll try and get to the bottom of it. In the meantime, I think we have more important things to focus on."

    hide korin
    show ecmc nojacket_v2 pin surprised at left3
    show eko casual glasses pin smile at right3:
        ease 0.4 right1
    "Eko perks up, handing the drive to me."

    show ecmc nojacket_v2 pin determined at left3
    mckorin "So it was just on the roof, out in the open?"
    ek "It was {i}just{/i} outside of sensor range! Very strange, indeed. We're lucky it showed up at all."

    hide eko
    show korin nojacket pin surprised at right3
    ko "And [genericfn], you said you checked the security cam footage of the day it went missing?"
    mckorin "I was about to, and then the terminal blew."

    hide korin
    hide ecmc
    show eko casual glasses pin basic at centre
    "Eko opens her own terminal to access the footage. I hold my breath as she does."

    show eko casual glasses pin basic at right3
    show ecmc nojacket_v2 pin determined at left3
    "She turns to look at me."
    ek "Did you try to move the files first?"
    mckorin "No. I just tried to open the one that fit the timeframe we were looking for."

    show eko casual glasses pin sleep at right3
    "Eko shakes her head, scrolling back and forth."

    show eko casual glasses pin sad at right3
    ek "If that file existed, it's...gone now."

    show ecmc nojacket_v2 pin surprised at left3
    "I look between her and Korin and put up my hands."
    mckorin "I swear, I didn't do anything with it! You have to believe me..."

    hide ecmc
    hide eko
    show korin nojacket_cu smile_cu at korin_cu
    "Korin puts a reassuring hand on my shoulder."
    ko "I believe you."
    hide korin

    show eko casual glasses pin sad at right3
    show ecmc nojacket_v2 pin determined at left3
    ek "I don't see how you could have possibly been responsible, considering what happened at your terminal."

    show eko casual glasses pin sleep at right3
    "She shakes her head."

    show eko casual glasses pin angry at right3
    ek "I'm going to close the lab, except by appointment only. I need to understand what's happening here."
    "I hold up the hard drive."
    mckorin "Eko, since this is back, I can check it out to go off-campus with the permission of a chaperone, right?"
    mckorin "It's important. It's just to start the recovery process, and then I can complete it on a secure terminal back here."

    show ecmc nojacket_v2 pin smile at left3
    mckorin "By appointment, of course. Like you said."

    show eko casual glasses pin smile at right3
    "Eko nods slowly."
    ek "Your chaperone will know the proper procedure for check-out, so be sure to clear it with them first."
    mckorin "Got it. Thanks again!"

    hide eko
    show ecmc nojacket_v2 pin smile at left1plus
    show korin nojacket pin basic at right1plus
    "I look at Korin and speak quietly to her as we walk out of Eko's earshot."
    mckorin "I don't suppose you have some errands that need to be run right now, do you?"

    hide ecmc
    hide korin
    show korin nojacket_cu smirk_cu at korin_cu
    "She winks at me."

    show korin nojacket_cu smile_cu at korin_cu
    ko "I was just about to remember some urgent appointment I have this afternoon. Let's go!"
    hide korin

    stop music
    play music ecmcalmeveryday2

    scene bg ecm_pawn_shop_off at bg
    show skye casual basic at centre
    with wiperightdissolve
    "A short while later, Korin and I meet up with Skye at the shop and hand over the drive."
    "He checks out the specs with his ARCware."

    show skye casual smug at centre
    sk "Hmm. Well...it certainly is everything you described."

    show ecmc jacket_v2 pin smile at left3
    show skye casual smug at right3
    mckorin "Which should be no problem for you, like we talked about. Right?"

    show skye casual basic at right3
    "Skye goes quiet, not looking up at us."

    hide skye
    hide ecmc
    show korin jacket_cu sad_cu at korin_cu
    "Korin shoots me a glance."
    hide korin

    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(She's right: something's up. I need to figure out what it is.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show skye casual basic at right3
    mckorin "Skye, what's your worry?"
    sk "This all just seems kind of weird. Why can't D.I.V.A.A. restore the data, anyway?"

    hide skye
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I can't tell him the whole truth...but I {i}can{/i} say something to inflate his ego a bit.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show skye casual basic at right3
    mckorin "D.I.V.A.A....isn't as modern as they make themselves out to be."

    show ecmc jacket_v2 pin determined at left3
    mckorin "They've got top of the line tech, sure, but everything has to be approved by FDI regulations."

    show skye casual surprised at right3
    sk "So working outside of what's legal is just...okay with you guys?"

    show ecmc jacket_v2 pin surprised at left3
    "Korin and I both hesitate in answering."

    show skye casual angry at right3
    sk "This really just seems like it could be some kind of setup."

    show ecmc jacket_v2 pin angry at left3
    "I feel a flare of annoyance."

    hide ecmc
    hide skye
    show korin jacket_cu smirk_cu at korin_cu
    "But out of the corner of my eye, I see Korin twist a strand of hair around her finger."
    hide korin

    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Right. Can't treat him like my kid neighbor anymore. Better to appeal to his vanity...)"
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show skye casual angry at right3
    mckorin "Look, Skye...setting up honeypot traps for Scrappers has never been in D.I.V.A.A.'s playbook. We both know that."

    show ecmc jacket_v2 pin angry at left3
    show skye casual basic at right3
    "He nods slowly."

    show skye casual angry at right3
    sk "Why me, then?"

    show ecmc jacket_v2 pin surprised at left3
    "I decide to tell him a mollifying version of the truth."

    show ecmc jacket_v2 pin determined at left3
    mckorin "We could have gone with one of Reyes' contacts. She has way more than me."
    mckorin "I insisted on you because I know what you're capable of. I knew if anyone could help with this, it'd be you."

    show ecmc jacket_v2 pin smile at left3
    mckorin "And I knew you wouldn't let me down."

    hide ecmc
    show korin jacket pin smile at left3
    "Korin leans on the counter."
    ko "I admit, Skye...I was skeptical when [genericfn] suggested you at first."

    show korin jacket pin smirk at left3
    ko "But you really know your stuff. Seriously, why would we want to get rid of an asset like you?"

    show skye casual smug blush at right3
    "Skye hides his bashful expression behind the interface of his ARCware."
    sk "So if I needed some favor from D.I.V.A.A. in the future, I could count on you guys?"

    show korin jacket pin smile at left3
    ko "If you help us kickstart recovery on this drive? Of course."

    show skye casual sleep noblush at right3
    "Skye thinks about it, then nods."

    show skye casual smug at right3
    sk "All right. I can start the process."

    hide korin
    hide skye
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(Yes!!)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show skye casual smug at right3
    "I refrain from doing a fist-pump in the middle of the shop."
    sk "Nothing else has been saved over the drive, right?"

    show ecmc jacket_v2 pin basic at left3
    mckorin "No, it's bricked. When I initiated a scan, it started fragmenting and later deleted itself."
    sk "I can get the recovery kickstarted. I just need to keep it for a little bit."
    sk "I know you've got tracking on it, so I won't mess with that."

    hide skye
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Yeah, you better not. I know where you live.)"
    hide ecmc

    show korin jacket_cu smile_cu at korin_cu
    "I look over at Korin, who nods."
    hide korin

    show korin jacket pin smile at left3
    show skye casual smug at right3
    ko "I can clear its release for seventy-two hours, but the sooner you can get it done, the better. Okay?"

    show skye casual angry at right3
    "Skye hisses a breath between his teeth, then cracks his knuckles."

    show skye casual smug at right3
    sk "Yeah, I can work with that. Kick-starting the recovery won't take long, and getting the full thing restored will be a cinch."

    hide skye
    hide korin
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Show-off.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show skye casual smug at right3
    mckorin "I knew you could do it. We'll be in touch, okay?"

    scene bg ecm_sidewalk_day at bg
    show ecmc jacket_v2 pin basic at left3
    show korin jacket pin basic at right3
    with wiperightdissolve

    stop music
    play music ecmupbeateveryday1

    "On our way back to HQ, Korin and I debrief on the plan ahead."
    ko "I've submitted a standing request to Eko to use the lab, and she's approved it."

    show ecmc jacket_v2 pin smile at left3
    "I breathe out a sigh of relief."

    show korin jacket pin smirk at right3
    ko "You really killed it in there with Skye, by the way."

    hide ecmc
    hide korin
    $menuhideborder = True
    menu korins1e8c2:
        "A. It's only thanks to you":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right3
            mckorin "If I did, it's only thanks to your help."
            ko "Eh, I just had to nudge you. You working him over so he agreed? That was all you."

        "B. It helps that I know him":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right3
            mckorin "It helps that I know Skye. I know what he's susceptible to..."
            ko "Maybe, but there's no harm in that."

        "C. I did, didn't I?":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right3
            mckorin "I did, didn't I?"

            show korin jacket pin smile at right3
            "My sudden confidence puts a smile on Korin's face."

    show korin jacket pin smile at right3
    ko "Guess I should be careful around such a charmer, though."
    show korin jacket pin basic at right3
    "I look sideways over at her...and she quickly looks away from me."

    show korin jacket pin blush surprised at right3
    ko "I mean...it's interesting watching you pick up tricks on social engineering. Interesting and rewarding."

    show ecmc jacket_v2 pin blush embarrassed at left3
    "Korin's compliments keep bubbling up inside of me. It used to be hard to handle, hearing her say such nice things about me..."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(But now, I don't really want her to stop.)"
    hide ecmc

    show ecmc jacket_v2 pin blush embarrassed at left3
    show korin jacket pin basic at right3
    "Enver's teasing about my crush comes floating back to me."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Okay...maybe he had a point.)"

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(But there's no use even thinking about it.)"
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show korin jacket pin basic at right3
    "I give a silent sigh as the impossibility of it all looms over me."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(There's just too many complicating factors. Even if Korin {i}did{/i} feel the same way about me.)"
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show korin jacket pin smirk at right3
    ko "Well, since I introduced you to one of my favorite things at the Catalyst last night..."
    ko "It's only fair that you introduce me to one of yours one of these days."

    show ecmc jacket_v2 pin surprised at left3
    "I blink in disbelief."
    mckorin "You mean that?"
    ko "Why not? We could go scrapping, or..."

    show ecmc jacket_v2 pin embarrassed at left3
    "I look shyly over at her."

    show korin jacket pin smile at right3
    ko "...Or something. I'd love to know more about what you get up to in your free time."
    "I'm not sure how to tell her that I feel the same without my words coming out too clumsy."

    show ecmc jacket_v2 pin surprised at left3
    "I'm just figuring out the right way to say it as we pass by a bookstore."

    show korin jacket pin surprised at right3
    "Korin stops in her tracks--and gasps."
    ko "Oh my gosh!! I forgot--it's out today!"
    mckorin "What is?"

    show korin jacket pin smile at right3
    ko "This book I preordered!"
    "She puts her hands to her cheeks, looking in the window at the long line inside."
    ko "It's by this author I got into last year. I've read everything by her now because I'm obsessed."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(Oh my god, she's adorable.)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at left3
    show korin jacket pin smile behind ecmc at right3:
        ease 0.4 xoffset -210
    "Korin reaches for me."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    ko "Here, come with me real quick! We've got time."
    hide korin

    show ecmc jacket_v2 pin sad at left1
    show korin jacket pin surprised behind ecmc at right1
    "I follow her a couple steps, then hesitate."
    mckorin "Don't we need some work-related excuse?"

    show korin jacket pin smirk behind ecmc at right1
    ko "Well, I'll think of one if anyone asks at HQ."

    hide ecmc
    show korin jacket_cu smirk_cu at korin_cu
    "She tucks her hair back from her face and looks at me bashfully."
    ko "If I need an excuse for you, I'm...fresh out. I just thought we could spend some time together."
    hide korin


    $menuhideborder = True
    menu korins1e8c3:
        "A. Join Korin at the bookstore." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show ecmc jacket_v2 pin smile at left2:
                ease 0.4 right3
            show korin jacket pin surprised behind ecmc at centre
            "I snicker, then stride past Korin and hold the door for her."
            mckorin "If you've got time, I've got time. No excuses needed."

            show korin jacket pin smile behind ecmc at centre:
                easein 0.2 yoffset -30
                easein 0.2 yoffset 0
            "Korin gives an adorable jump on the balls of her feet and follows me inside, grinning all the way."

            scene bg ecm_last_bookstore_on at bg with wiperightdissolve
            stop music
            play music ecmromantic1

            "Korin strides past the line, and I step lightly to keep up with her."

            show ecmc jacket_v2 pin surprised at left3
            show korin jacket pin smile at right2
            mckorin "Aren't we picking up your preorder?"
            ko "We'll get it on the way out. I just wanted to see..."

            show korin jacket pin surprised at right2
            "She stops and cranes her neck, looking around at the signs. We've stopped in front of the romance section."
            "A cover catches my eye for a book called {i}Futch Fatale{/i}."
            "Two women, one clearly a private investigator, the other some sort of rogue, are pressed close together in a shadowed alley."
            "Their lips are tantalizingly close, just inches from meeting."

            show ecmc jacket_v2 pin angry at left3
            "Blurred shapes in the foreground give the impression that they're both hiding...but from who?"
            "I tilt my head and imagine one of the women as Korin, and the other one...as me."

            show korin jacket pin smile at right2
            ko "Do you like romance books?"

            show ecmc jacket_v2 pin blush surprised at left3
            mckorin "Um...I don't know! I was just looking!"
            "To my mortification, Korin picks up the book and turns it over."

            show korin jacket pin surprised at right2
            ko "Oh, and it's a detective story? That's interesting..."

            show korin jacket pin smirk at right2
            "She gives me a sly look, then puts it back and continues on. I kick myself to keep up."

            hide ecmc
            show ecmc jacket_v2 pin smile at left3
            mckorin "Do you like detective stories?"
            ko "Of course I do. Who doesn't love a good mystery?"
            ko "True crime, thrillers, mysteries...I love them. But where my heart truly lies is..."

            show korin jacket pin smile at right2:
                ease 0.4 right4
            "She rounds a corner, and I take in the selection of macabre hardbacks."

            show ecmc jacket_v2 pin surprised at left3
            mckorin "Horror?!"

            show korin jacket pin smirk at right4
            "Korin bites her lip, waiting for my reaction."
            mckorin "I just...could not have honestly guessed that about you!"

            show korin jacket pin smile at right4
            ko "I like all horror, but...ghost stories are my favorite."

            show korin jacket pin smile at right4:
                ease 0.4 right2
            "She walks down the aisle, picking them off for me."

            show ecmc jacket_v2 pin basic at left3
            ko "{i}Ghost Writer{/i} is a classic, of course. {i}This Program is Not Responding{/i} is great."
            ko "{i}Parasocial Activity{/i} scared the pants off me. {i}Cargo 200{/i} is by far the most disturbing book I've ever read..."

            show ecmc jacket_v2 pin smile at left3
            "She trails off, noticing the smile that I'm trying to hide."

            show korin jacket pin surprised at right2
            ko "What is it?"
            mckorin "...Ghosts? Really?"

            show korin jacket pin smile at right2
            "Korin laughs."
            ko "I know, I know! We specialized in tech-focused crimes, and I'm enjoying stories about the paranormal in my free time..."
            ko "When I was a teenager, my grandma let me pick whatever books I wanted from her bookshelf. Even the more racy or scary ones. "
            ko "But I was always drawn to books with this specific type of cover..."
            "She picks one up off the shelf and shows me, miming with her body the pose of the woman on the front."
            ko "I call them {i}women running from dark houses{/i} books..."

            show korin jacket pin smirk at right2
            ko "...Also known as gothic romance."

            show ecmc jacket_v2 pin surprised at left3
            "I tilt my head, confused."

            show korin jacket pin smile at right2
            ko "What's that look for?"
            mckorin "Horror, I get. You have to be kind of into the macabre to be in this line of work."
            mckorin "But...gothic romance?"
            ko "Haunted houses, haunted people...brooding and mercurial love interests...the more aloof, the better."

            show korin jacket pin sad at right2
            "She presses her back to the bookshelf and puts a dramatic hand to her forehead."

            show ecmc jacket_v2 pin smile at left3
            ko "And a heroine, tangled in a paradox of feelings, trapped in the orbit of her own desires..."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(Okay, {i}that{/i} I can relate to.)"
            hide ecmc

            show ecmc jacket_v2 pin smile at left3
            show korin jacket pin smirk at right2
            ko "What's not to love?"

            show ecmc jacket_v2 pin determined at left3
            mckorin "I guess I can see the appeal..."

            show korin jacket pin smile at right2
            ko "You should give horror a try sometime. You never know! You might find something you like."
            mckorin "I wouldn't know where to start."

            show korin jacket pin smile behind ecmc at right2:
                ease 0.4 right1
            "She plucks a book off the shelf and shows it to me."

            show ecmc jacket_v2 pin surprised at left3
            ko "Here.{i}Every Night But One{/i} by Sherry Macksen."
            ko "Her book I'm picking up today is called {i}Doomscroll{/i}. It's a ghost story too, but with a more modern setting."

            show ecmc jacket_v2 pin determined at left3:
                ease 0.4 left1
            "When I reach for the book, Korin pulls it out of reach, and I take an involuntary step closer to her."
            "But Korin doesn't back away."

            show korin jacket pin smirk behind ecmc at right1
            ko "My treat, Scraps. And I've got plenty more I can recommend if you end up liking it."

            show korin jacket pin smile behind ecmc at right1
            ko "You just call me if it gets too scary for you. Okay?"

            show ecmc jacket_v2 pin surprised at left1
            mckorin "Too scary...come on!"

            show ecmc jacket_v2 pin smile at left1
            "She giggles, and I follow her back to the register so she can check out with her preorder."

            show korin jacket pin smile behind ecmc at right1:
                ease 0.4 right3
            "On the way, she stops at the romance endcap again, thinks for a second, then picks up {i}Futch Fatale{/i}."

            show ecmc jacket_v2 pin blush embarrassed at left1
            "I feel a rush of heat to my cheeks."
            mckorin "Korin, really, you don't need to...I was just..."

            show korin jacket pin smirk behind ecmc at right3
            ko "Who said I was getting this for you?"
            "She smirks at the look on my face and gives me a wink."

            show korin jacket pin smile behind ecmc at right3
            ko "But maybe I'll let you borrow it when I'm done."

        "B. Rush back to work.":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad at left1
            show korin jacket pin basic behind ecmc at right1
            mckorin "I want to, but...what if we get in trouble?"
            show korin jacket pin sad behind ecmc at right1
            "Korin gives an exaggerated pout, but I can tell that some of her disappointment is real."

    scene bg ecm_mc_dorm_off at bg
    show ecmc casual_v1 basic at centre
    with clockwise_wipe

    stop music
    play music ecmsuspense2

    "Later that night, I'm at home, getting ready to call it a night."

    hide ecmc
    show ecmc casual_v1_cu basic_cu at ecmc_cu
    "(Interesting how a day can turn around so quickly...)"
    "I think about Skye and his recovery efforts."

    show ecmc casual_v1_cu sad_cu at ecmc_cu
    "(Definitely losing my Scrapper street cred, especially with him. But it's all for a good cause.)"

    play sound phone_vibrating
    hide ecmc
    show ecmc casual_v1 surprised at centre
    "Suddenly, my ARCware buzzes to life."

    show ecmc casual_v1 surprised at left3
    show korin jacket pin basic at holo_mask, korin_holo, right2 with dissolve
    mckorin "...Korin? What's up?"

    show ecmc casual_v1 sad at left3
    ko "Hey...are you home? I need to talk to you. It's urgent."
    mckorin "I'm home, what is it?"

    show korin jacket pin sleep at holo_mask, korin_holo, right2
    "I hear a sigh of relief on the other end."

    show korin jacket pin angry at holo_mask, korin_holo, right2
    ko "Good, then you're safe."
    ko "Listen..."

    hide ecmc
    hide korin
    show korin jacket_cu angry_cu at holo_mask, korin_holo, korin_cu
    ko "I think someone's trying to set you up!"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
