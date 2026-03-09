label korin_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_dorm_hallway_on at bg
    play music ecmemotional2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show ecmc jacket_v2 pin surprised at centre
    "My words catch in my throat."
    hide ecmc

    show korin nojacket pin smile at left3
    show anton casual basic at right4
    ko "Thanks, Anton. I'll take it from here."

    show korin nojacket pin basic at left3
    "They both look expectantly at me."

    show anton casual angry at right4
    an "You're still in my way!"

    hide korin
    hide anton
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Oh. Glitch.)"
    hide ecmc_cu

    stop music
    play music ecmcalmeveryday1

    scene bg ecm_generic_office_night_on at bg
    show korin nojacket pin basic at right1
    show ecmc jacket_v2 pin basic at left1
    with doors_close
    "Korin gently touches my back, guides me inside her office, and shuts the door."

    show korin nojacket pin sad at right1
    ko "Was Anton right?"

    show ecmc jacket_v2 pin sad at left1
    "Slowly, I nod."
    mckorin "I need your help with my report."
    mckorin "I know you're busy, and I know asking for your time after-hours is... a lot."
    "I think about how to sweeten my request and recall what Enver said earlier."

    show ecmc jacket_v2 pin surprised at left1
    mckorin "I can pay for dinner or something, to thank you!"

    show korin nojacket pin smile at right1
    "She breaks into a smile, looking as charmed as she is amused."
    ko "Don't worry, Scraps. No need to bribe me with food. I was just about to head out and get some work done away from the office, anyway."
    ko "There's a great place nearby that'd be perfect for us to knock that report out!"

    stop music
    play music ecmupbeateveryday2

    scene bg ecm_restaurant_night_lights at bg
    show korin jacket pin basic at right2
    show ecmc jacket_v2 pin basic at left3
    with wiperightdissolve

    "We find a booth in a little diner just off the street that passes by HQ."

    show ecmc jacket_v2 pin basic at left3:
        ease 0.4 left2
    "A waiter stops by and pulls up the menu on a holo display. I lean in, interested..."

    show ecmc jacket_v2 pin surprised at left2
    show korin jacket pin basic at right2:
        ease 0.4 right1plus
    "But Korin reaches out and swipes the menu off the table."

    show korin jacket pin smile at right1plus
    ko "Two Shirley temples, please."
    "Korin catches my slightly puzzled look after the waiter leaves."
    ko "This place makes the best Shirley Temples. They use high quality grenadine and gourmet maraschino cherries."
    ko "It's my go-to drink when I need to {i}get work done{/i}."

    show korin jacket pin smirk at right1plus
    show ecmc jacket_v2 pin smile at left2
    "Korin waggles her eyebrows at me."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Right... we're not here to have fun.)"
    hide ecmc

    show korin jacket pin smile at right1plus
    show ecmc jacket_v2 pin smile at left2
    ko "My treat!"
    mckorin "Thank you!"
    ko "Now, let's get cracking!"

    show korin jacket pin basic at right1plus
    show ecmc jacket_v2 pin basic at left2
    "I pull out my datapad. Drinks come. We order dinner, food comes."

    hide ecmc
    hide korin
    "We keep at it, and by the time the dishes go, we're nearly done with my report."

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(This went by way faster than I thought it would. And I've learned a {i}lot{/i}.)"
    hide ecmc

    show ecmc jacket_v2 pin basic at left2
    show korin nojacket pin basic at right1plus
    ko "Okay. I'm going to read this section out loud..."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I can't believe this is how my first day turned out.)"
    "(But then again, if it hadn't turned out this way, I'd never have ended up here with Korin...)"
    hide ecmc

    show ecmc jacket_v2 pin embarrassed at left2
    show korin jacket pin basic at right1plus
    "Korin looks up, and I quickly glance away."
    mckorin "Well? How is it?"

    show korin jacket pin sad at right1plus
    ko "I'm not going to lie to you... this is a tough spot to be in."
    ko "I don't know how Dom's going to react."

    show ecmc jacket_v2 pin sad at left2

    "I absentmindedly shred a napkin to pieces in my lap."

    show korin jacket pin smirk at right1plus
    ko "But, I will say that this report is sterling."

    show korin jacket pin sad at right1plus
    "Korin tilts her head to the side, scrutinizing me."
    ko "How are you feeling about all this?"
    mckorin "I'm in the best shape I can be, considering the circumstances."

    show ecmc jacket_v2 pin determined at left2
    mckorin "I never thought my first day as a Hatchling would turn out this way."
    "Korin gives a small sigh."
    ko "Sometimes you try your best, you do everything right, and life still smacks you down."

    show korin jacket pin smile at right1plus
    ko "But, what do you do? You get back up everytime."
    "The way she says it, I can tell she believes it... but there's a wistfulness there, too."
    ko "Your dad taught me that."

    show ecmc jacket_v2 pin smile at left2
    mckorin "Yeah... it sounded pretty familiar."
    "Korin catches my smile and fiddles with the melting ice in her glass."
    ko "Guess I'm preaching to the choir, huh?"
    mckorin "It's nice to hear it from someone else, if he's not here to say it. Even someone so different from him."

    show korin jacket pin sad at right1plus
    ko "Different is right. He really knew his stuff. I've got a lot to live up to without him here..."
    hide korin
    hide ecmc

    $menuhideborder = True
    menu korins1e3c1:
        "A. I miss him, too.":
            $menuhideborder = False
            show korin jacket pin sad at right1plus
            show ecmc jacket_v2 pin determined at left2
            mckorin "I miss him too, you know."
            "Korin nods."
            "Probably more than anyone, I imagine."
        "B. I think he'd be proud.":
            $menuhideborder = False
            show korin jacket pin sad at right1plus
            show ecmc jacket_v2 pin determined at left2
            mckorin "I think he'd be proud."
            show korin jacket pin smile at right1plus
            ko "Damn right, he would. Look at you!"
            show ecmc jacket_v2 pin smile at left2
            show korin jacket pin surprised at right1plus
            mckorin "I meant he'd be proud of {i}you{/i}."

        "C. This drink isn't strong enough for this kind of talk":
            $menuhideborder = False
            show korin jacket pin sad at right1plus
            show ecmc jacket_v2 pin determined at left2
            mckorin "This drink isn't strong enough for this kind of talk."
            "Korin fiddles with the ice in her Shirley temple some more before nodding with me."
            ko "Damn right."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(She looks like she needs some cheering up.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left2
    show korin jacket pin sad at right1plus
    mckorin "Korin, I don't know how to thank you for all your help. From orientation this morning, to the junkyard, and now this..."
    mckorin "You're like, the best trainer ever. Seriously."

    show korin jacket pin smirk at right1plus
    "She leans back, her expression brightening."
    ko "Thanks, Scraps. But really, you're worth the effort."
    "Her words travel straight to my heart, but I reroute them to the logical portion of my brain."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Like all the cadets. Not me specifically.)"

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(...Right?)"
    hide ecmc

    show korin jacket pin smile at right1plus
    show ecmc jacket_v2 pin smile at left2
    ko "If we make it through this, you're gonna have a hell of a career here. Not many cadets show as much promise as you did today."
    ko "Those who did have gone on to do fantastic things here at D.I.V.A.A."

    show ecmc jacket_v2 pin basic at left2
    "I think back on what Enver told me about Korin's skills."

    show ecmc jacket_v2 pin smile at left2
    mckorin "What tech is to me... people are to you. Right?"
    show korin jacket pin smirk at right1plus
    "She tries to hide a smile."
    ko "I think I know where you're going with this, but go on."
    mckorin "I mean, Connie was scary as hell. And that Anton guy in the hallway..."
    mckorin "Both of them got me completely scuffed up."

    show korin jacket pin smile at right1plus
    "Korin laughs and shakes her head at me."
    ko "Of {i}course{/i} a couple of grumpy superiors would trip you up! That's adorable!"

    show ecmc jacket_v2 pin determined at left2
    "I roll my eyes good-naturedly at her teasing."
    mckorin "When I get away from situations like that, I'm always flooded with all the things I {i}could{/i} have said."

    show ecmc jacket_v2 pin sad at left2
    mckorin "And if I had asked for your help finishing this report when I knew I needed it, we'd have finished hours ago."

    show korin jacket pin smirk at right1plus
    ko "Are you asking for my help again?"

    show korin jacket pin smile at right1plus
    ko "Because I do have a few tricks about staying cool in stressful situations, if you're interested."

    show ecmc jacket_v2 pin smile at left2
    mckorin "Any help you can offer would be much appreciated."

    show korin jacket pin basic at right1plus
    show ecmc jacket_v2 pin sad at left2
    "Korin puts her chin in her hand and stares at me for a moment. I shift in my seat."
    mckorin "Um... what are you doing?"

    show korin jacket pin smirk at right1plus
    ko "Trying to get a read on you."
    mckorin "You look like you're about to treat me as a hostile witness."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    "Korin grins and shrugs."
    ko "Maybe I am."
    hide korin

    $menuhideborder = True
    menu korins1e3c2:
        "A. Learn how Korin stays cool under fire." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin jacket_cu smile_cu at korin_cu
            "I hold Korin's gaze for as long as I can."
            hide korin

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mckorin "Request granted, Phoenix Detective. Let's see if you can get me to crack."
            hide ecmc

            show korin jacket_cu angry_cu at korin_cu
            "Korin narrows her eyes."
            ko "Oh, I'll do more than that, Hatchling."
            hide korin

            show korin jacket pin angry at right1plus
            show ecmc jacket_v2 pin smile at left2
            "She leans back."

            show korin jacket pin smirk at right1plus
            ko "Wait, we're trying to teach how {i}not{/i} to crack."
            "We both laugh, breaking the tension."
            mckorin "Well?"
            ko "Well, you seem to have good awareness."

            show ecmc jacket_v2 pin sad at left2
            "I cringe."
            mckorin "Except when I'm standing in someone's way in the middle of the wallway."

            show korin jacket pin smile at right1plus
            "Korin laughs. She thumps her hand down on the table next to mine."
            ko "Scraps, you're too hard on yourself."
            ko "You grew up here. You graduated from the academy. So I know Connie and Anton can't be your first brush with confrontation."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(I guess not...)"
            hide ecmc

            show korin jacket pin smirk at right1plus
            show ecmc jacket_v2 pin basic at left2
            ko "Where do you feel anxiety? Physically."

            show ecmc jacket_v2 pin sad at left2
            ko "Maybe your hands start to shake? Legs go numb?"
            ko "Your chest might feel tight, your pulse might race..."
            "And race it does, as her fingers skate over my wrist in her gesticulation."

            show korin jacket pin surprised at right1plus
            ko "When Connie yelled at you, where did you feel your anxiety?"
            "I think about it, then put a hand on my chest."

            show ecmc jacket_v2 pin surprised at left2
            mckorin "I swear, I'm not normally like this... I'm normally a functioning human being. Most days."

            show korin jacket pin basic at right1plus
            ko "But it's your first day at your important new job."
            ko "Warning signs, right? What were they?"

            show ecmc jacket_v2 pin sleep at left2
            "I close my eyes for a second."
            mckorin "I remember the sound drowning out. All the other conversations, the noise of the city..."
            mckorin "All I could hear was Connie's voice and the blood in my ears. And I could feel that racing feeling in my chest."

            show ecmc jacket_v2 pin basic at left2
            "I open my eyes. Korin's expression is unreadable."

            show korin jacket pin smile at right1plus
            ko "Let's order something."

            show ecmc jacket_v2 pin surprised at left2
            mckorin "Like... what? Like dessert?"

            show korin jacket pin smirk at right1plus
            ko "Mm, dessert sounds good. What do you want?"
            "She taps the table. Lights dance on the holo display as she pulls up the dessert menu."

            show ecmc jacket_v2 pin determined at left2
            mckorin "Um--"

            show korin jacket pin smile at right1plus
            ko "Not sure? Well, how about another drink?"
            "She taps the table again, pulling up the cocktail menu."

            show ecmc jacket_v2 pin surprised at left2
            ko "You know? Maybe I'm still hungry."
            "Another menu: dinner, the text layered over the other two menus. Holo displays of popular dishes twirl before us."

            show korin jacket pin basic at right1plus
            ko "But maybe I'm feeling something like breakfast instead. How about it?"

            show korin jacket pin angry at right1plus
            ko "We don't have all night, [genericfn]. Pick what you want!"
            mckorin "Um--"

            hide ecmc
            hide korin
            show korin jacket_cu angry_cu at korin_cu
            ko "C'mon, pick!"
            hide korin

            show korin jacket pin angry at right1plus
            show ecmc jacket_v2 pin angry at left2
            mckorin "I can't!"
            "I slap my hands on the table."

            show ecmc jacket_v2 pin sad at left2
            mckorin "I can't."

            show korin jacket pin basic at right1plus
            "Korin sits back and gives me a second to breathe."

            show ecmc jacket_v2 pin surprised at left2
            mckorin "Jeez, you weren't kidding about treating me as hostile!"

            show korin jacket pin sad at right1plus
            ko "Not me, Scraps. These menus, and me? We're your thoughts. Your emotions."
            "I look at the spinning menus."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(She's right. It's all so much.)"
            hide ecmc

            show korin jacket pin basic at right1plus
            show ecmc jacket_v2 pin surprised at left2
            ko "So how do you untangle from this? What can you do?"

            show ecmc jacket_v2 pin determined at left2
            mckorin "I could be impulsive, just pick something."

            show korin jacket pin smile at right1plus
            "Korin tilts her head, agreeing with me..."
            ko "You could..."
            mckorin "...But who knows if I'd even pick something I really wanted."

            show korin jacket pin smirk at right1plus
            ko "Exactly. So, you could..."
            "Korin whisks her hands across the display and jumbles all the menus together..."
            "Then sweeps them dramatically to the side and looks across the empty space at me."
            ko "...Turn your attention to something else."

            show ecmc jacket_v2 pin smile at left2
            "I hold her gaze, and just for a moment, the anxiety vanishes."
            "I snap out of it and gesture to the mess at the far end of the table."
            mckorin "But it's still there. Waiting for me to do something."

            show korin jacket pin basic at right1plus
            ko "But you have a second. Sit back from it. Acknowledge that it's there, but... these menus aren't demanding anything from you, are they?"
            mckorin "Dessert"
            ko "No, YOU want dessert. The menus are just telling you what's available."

            show korin jacket pin angry at right1plus
            ko "When someone like Connie tries to climb up my ass, or some jerk like Anton decides to try and ruin my day..."

            show ecmc jacket_v2 pin surprised at left2
            "She pulls the holo mess back to the center of the table."

            show korin jacket pin basic at right1plus
            ko "My brain tries to take all this hostile information and give me a whole banquet of ways I can respond."
            ko "But, really..."
            mckorin "I just want dessert."

            show korin jacket pin smirk at right1plus
            "Korin taps her forehead."
            ko "And you're the only one who gets to give the orders up here."

            show korin jacket pin smile at right1plus
            "Korin smiles. She reaches up to help me start closing the other menus and displays, one by one."

            show ecmc jacket_v2 pin basic at left2
            "But I triple-tap a display button on the corner of the table and close all the menus at once."
            "Korin laughs."
            ko "See? You're even more efficient than me."
            ko "But now that you've got that early warning system we talked about..."

            hide ecmc
            hide korin
            show korin jacket_cu sad_cu at korin_cu
            "She puts her hand to her chest one more time and gives me a meaningful look."
            ko "Try to start closing those thoughts before they even pop up."

            show korin jacket_cu smile_cu at korin_cu
            ko "And focus on what's really important."
            hide korin

            show korin jacket pin smile at right1plus
            show ecmc jacket_v2 pin basic at left2
            "I open up the menu again."

            show ecmc jacket_v2 pin smile at left2
            mckorin "Right. Dessert."
            "I order for both of us, confident of my choice."
            "But that racing-pulse feeling doesn't go away..."
            "At least, not until long after I say my goodnight to Korin and thank her for all her help."
        "B. Struggle with it alone.":
            $menuhideborder = False
            show korin jacket pin sad at right1plus
            show ecmc jacket_v2 pin basic at left2
            mckorin "I appreciate it, but... you've helped me enough tonight. I'll just try and learn as I go."
            ko "No need to take everything on the hard way, Scraps."
            ko "But I understand. You let me know if you ever change your mind later."

    stop music
    play music ecmtense3

    scene bg ecm_dominick_office_day at bg with wiperightdissolve

    "A couple days after submitting my report, I'm summoned to Griffin Dominick Vega's office."

    show dominick uniform pin headpiece basic at centre
    "Dominick gets right to the point."
    do "Good morning, cadet. I have official feedback on your report that I wanted to share with you and Korin, here."

    hide dominick
    show korin nojacket_cu sad_cu at korin_cu
    "I look to Korin, but she won't meet my eyes."
    hide korin

    show ecmc jacket_v2 pin surprised at left3
    show dominick uniform pin headpiece basic at right3
    mckorin "Um... was there something wrong with my report?"
    do "The report was spotless."
    "From Dominick's expression, I think I must have misheard him."
    do "Far better than what I would expect from a Hatchling, but that's beside the point."

    hide ecmc
    hide dominick
    show dominick uniform_cu headpiece_cu basic_cu at dominick_cu
    "His eyes pass between me and Korin, but whatever judgment he's passing on us remains unsaid for now."
    hide dominick

    show ecmc jacket_v2 pin smile at left3
    show dominick uniform pin headpiece basic at right3
    mckorin "Thank you, sir."

    hide dominick
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(That's not the full story though, is it?)"
    hide ecmc

    show ecmc jacket_v2 pin basic at left3
    show dominick uniform pin headpiece angry at right3
    do "As soon as our techs connected with the drive to salvage the corrupted data, the drive started erasing it completely."

    show ecmc jacket_v2 pin surprised at left3
    "My eyes go wide."
    mckorin "W-what?! How?"
    do "We were hoping you might have some sort of explanation. Phoenix Reyes here was at a loss."
    mckorin "I could see the drive becoming corrupted from some sort of dormant virus, but..."
    mckorin "To self-wipe completely? How could it have done that?!"
    do "In this line of work, Hatchling, the simplest answer is almost always the correct one."
    do "And in this case, the simplest answer is that you were the last one who had your hands on the open evidence."

    hide dominick
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(He's saying this is MY fault.)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at left3
    show dominick uniform pin headpiece angry at right3
    mckorin "B-but..."

    hide ecmc
    show korin nojacket pin basic at left3
    "Korin intervenes."
    ko "Dom, [genericfn] managed to stop the corruption before the drive completely bricked itself."
    do "Her skills aren't in question here, Korin."

    show korin nojacket pin sad at left3
    ko "And you know that's not my point, Dom."

    show dominick uniform pin headpiece sleep at right3
    "Dominick gives a little sigh, and Korin turns to me."

    hide dominick
    hide korin
    show korin nojacket_cu sad_cu at korin_cu
    ko "What Dom here is trying to say is that at this point, it's about accountability. Especially since..."

    show korin nojacket_cu sleep_cu at korin_cu
    "She takes a deep breath."

    show korin nojacket_cu sad_cu at korin_cu
    ko "...That cold case is now heating up."
    hide korin

    show korin nojacket pin sad at left3
    show dominick uniform pin headpiece basic at right3
    "Dominick nods in agreement."

    hide korin
    hide dominick
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(We've reopened the case? Isn't that a good thing?)"
    hide ecmc

    show ecmc jacket_v2 pin determined at left3
    show dominick uniform pin headpiece basic at right3
    mckorin "Look, if you can give me an hour with it, and the proper equipment, I can--"

    show dominick uniform pin headpiece smirk at right3
    "Dominick's sharp, disbelieving laugh makes me still at once."
    do "Now isn't the time to be over-promising on your skills, Hatchling."
    mckorin "With all due respect, sir, I'm not."

    show ecmc jacket_v2 pin sad at left3
    show dominick uniform pin headpiece angry at right3
    "He looks sharply at me, and I can't help but feel like I've walked into some kind of trap."
    do "Good. Because the F.D.I. has managed to wrestle this case away from us."
    do "Because we are very lucky, they're allowing D.I.V.A.A. personnel to advise their agent."
    do "We'll look totally feckless on this case unless we can find a substantial lead. But we can't spare an active agent on this."

    show dominick uniform pin headpiece basic at right3
    do "So, you think you can do that? Find something useful from the hard drive?"
    mckorin "The alternative being...?"

    hide ecmc
    hide dominick
    show dominick uniform_cu headpiece_cu angry_cu at dominick_cu
    do "Your termination from D.I.V.A.A."
    hide dominick

    show ecmc jacket_v2 pin surprised at left3
    show dominick uniform pin headpiece angry at right3
    "My vision practically bluescreens."
    do "I'll tell you very plainly that this offer is only on the table partly because of who your dad is..."
    do "And partly because Phoenix Reyes here seemed to think so highly of you."
    "I shake my hair out of my eyes."

    show ecmc jacket_v2 pin smile at left3
    mckorin "Thank you. I appreciate the opportunity."

    hide dominick
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(And I can't let Korin down.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show korin nojacket pin smile at right3
    "Korin gives me a brisk and encouraging nod."
    ko "Okay, let's start with--"

    hide ecmc
    hide korin
    show dominick uniform pin headpiece angry at centre
    do "No, Korin. You won't be helping her."

    show korin nojacket pin angry at left3
    show dominick uniform pin headpiece at right3
    "Korin freezes, her voice on edge."
    ko "Yes, I will."
    do "You have other trainees to focus on. [genericfn] here will instead be working with Gael."
    "Korin folds her arms."
    ko "You're gift-wrapping this case for them, you know."
    do "And if they get wind that she's getting cues from her dad's former partner, how's that going to look?"

    hide korin
    hide dominick
    show dominick uniform_cu headpiece_cu angry_cu at dominick_cu
    do "If I catch even a minute of your time being spent helping MC..."
    do "I'll write you up and just skip to the firing for her. No hesitation."
    do "She needs to clean up her own mess without taking resources from our other operations."
    hide dominick

    show korin nojacket pin angry at left3
    show dominick uniform pin headpiece angry at right3
    "Aggravated, Korin runs her fingers through her hair... but stays silent."
    "Dominick waves a hand."
    do "You have my orders. You're both dismissed."

    scene bg ecm_dorm_hallway_on at bg with wiperightdissolve
    "Korin and I leave the office, and I have to walk double-time just to keep up with her."

    show korin nojacket pin angry at right3
    show ecmc jacket_v2 pin basic at left3
    ko "The worst part about all of this is that Dom's right."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "He is?"
    ko "Damaging evidence in any way makes us look bad enough, but if the F.D.I. gets a whiff of nepotism, too..."

    show korin nojacket pin sleep at right3
    "She shakes her head."

    show korin nojacket pin sad at right3
    ko "There's just too much at stake for the future of D.I.V.A.A."

    show ecmc jacket_v2 pin sad at left3
    mckorin "Korin... I'm not sure if I can give Dominick what he's asking for."
    mckorin "I'm good with tech, but..."
    "Korin nods, understanding at once and finishing my sentence for me."
    ko "But he might be asking for the impossible."

    show ecmc jacket_v2 pin embarrassed at left3
    show korin nojacket pin sad at right3:
        easein 0.4 centre
    "She reaches for my hand. My heart leaps..."
    "But she just reassuringly pats the back of it."

    show korin nojacket pin smile behind ecmc at centre
    ko "Well, look, part of being an investigator is seeing obstacles as opportunities rather than barriers."
    ko "Even when the trail's gone completely cold, you have to keep searching for your next step forward."

    show ecmc jacket_v2 pin determined at left3
    "I look up at her... and realize she's right."

    show korin nojacket pin basic at centre
    ko "So, level with me."
    ko "How sure are you that the drive you scanned couldn't have been corrupted by your own misstep?"

    show ecmc jacket_v2 pin sad at left3
    "I look her in the eyes."
    mckorin "Korin... you're not supposed to be helping me. You'll get in trouble."

    show korin nojacket pin smile at centre
    ko "Not helping! Just asking!"

    show ecmc jacket_v2 pin determined at left3
    mckorin "Fine. I'm dead certain. Something's up with that drive, and I'm at least reasonably confident that I can figure it out."

    show korin nojacket pin sad at centre
    "Korin shakes her head and looks away from me."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "What?"
    ko "That look you had in your eye just now..."
    ko "I remember your dad having that same look when he had a feeling about a case."

    show korin nojacket pin smile at centre
    ko "It never steered us wrong before."

    show ecmc jacket_v2 pin smile at left3
    "I give a shaky laugh."
    mckorin "Well, don't go counting on that as foolproof just yet."

    show ecmc jacket_v2 pin sad at left3
    mckorin "And I don't know what it's going to be like working with this Gael. I haven't heard anything about her..."

    show korin nojacket pin basic at centre:
        ease 0.4 right3
    show ecmc jacket_v2 pin sad at left3
    "We reach the door to Korin's office. She gestures for me to follow her inside."

    show korin nojacket pin sad at right3
    ko "Yeah, cards are really stacked against you with her..."

    scene bg ecm_generic_office_night_on at bg
    show korin nojacket pin sad at right3
    show ecmc jacket_v2 pin sad at left3
    with doors_close
    "Korin lets the door shut with a soft hiss."
    ko "...Which is why I'm still going to help you."

    show korin nojacket pin sad at right3
    show ecmc jacket_v2 pin surprised at left3
    "My eyes widen. Korin puts a finger to her lips and lowers her voice."
    ko "But it's gotta be on the down-low, understand?"

    hide korin
    hide ecmc
    $menuhideborder = True
    menu korins1e3c3:
        "A. You'd do that for me?":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left3
            show korin nojacket pin sad at right3
            mckorin "You'd really do that for me?"
            show korin nojacket pin smirk at right3
            "I catch a hint of a smile that Korin tries to hide."
        "B. I understand.":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad at left3
            show korin nojacket pin sad at right3
            mckorin "I understand it's got to be on the down-low... but you're really putting yourself at risk, here."
        "C. I can't accept that.":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad at left3
            show korin nojacket pin sad at right3
            mckorin "I can't accept that. D.I.V.A.A. needs you more than it needs me, and with your name on the line..."

    show ecmc jacket_v2 pin sad at left3
    show korin nojacket pin sleep at right3
    "Korin takes a deep, contemplative breath."

    show korin nojacket pin basic at right3
    ko "I know the stakes, MC. I just want to make sure you know them, too."
    ko "Worst case scenario, we're both fired."

    show korin nojacket pin smile at right3
    ko "Best case, we get you off the hook, preserve D.I.V.A.A.'s reputation, and solve this cold case."

    hide ecmc
    hide korin
    show korin nojacket_cu smile_cu at korin_cu
    "She puts both hands on her desk and leans down so her eyes are level with mine."
    ko "What do you say, Scraps. Are we in this together?"


    scene bg ecm_tbc at bg with fade


    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

