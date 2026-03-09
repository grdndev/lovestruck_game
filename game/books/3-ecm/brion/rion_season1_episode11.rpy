label rion_season1_episode11:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_generic_office_on at bg with fade
    play music ecmcalmeveryday4

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show rion black pin sleep at centre
    "I stand up and look around the room and find Rion right behind me, leaning against the wall with his eyes closed."

    hide rion
    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(Is he...sleeping?!)"
    hide ecmc

    show rion black pin sleep at centre
    "Rion's arms are folded across his chest and his mouth is open slightly as his head rolls to one side."
    hide rion

    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(He must have dozed off as soon as he put his jacket on me!)"
    hide ecmc

    show rion black pin sleep at left3
    show ecmc nojacket_v1 pin smile at right2
    "I can't help but laugh as I watch Rion."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu smile_cu at ecmc_cu
    "(Of course Rion wouldn't sleep like a normal person!)"
    "(I don't know if it's cool that he sleeps like this, or ridiculous, or both...)"
    hide ecmc

    show ecmc nojacket_v1 pin smile at centre
    "I carefully fold Rion's jacket over the chair, then I walk over to the window and look out at the city scape."

    hide ecmc
    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(The sun's almost up. We've been here all night!)"
    hide ecmc

    show ecmc nojacket_v1 pin sad at centre
    "I look down at my crumpled clothes and wrinkle my nose."
    hide ecmc

    show ecmc nojacket_v1_cu determined_cu at ecmc_cu
    "(There's no point in going home now. I'll just have to stay in this all day.)"

    show ecmc nojacket_v1_cu sad_cu
    "(I could definitely use some coffee, though.)"
    hide ecmc

    show ecmc nojacket_v1 pin sad at centre
    "I order some coffee to be delivered, then while I wait I look back out at the city, my thoughts swirling around in my head."

    hide ecmc
    show ecmc nojacket_v1_cu angry_cu at ecmc_cu
    "(I still can't believe someone at D.I.V.A.A. could be the serial killer that Rion's been chasing!)"
    hide ecmc

    "I get a notification that my coffee order has arrived so I head to the front doors to collect it before making my way back to Rion's office."

    show rion black pin sleep at centre
    "He's still standing exactly where I left him, snoring lightly."
    hide rion

    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(I wonder how long he's been sleeping like that. Surely it can't be comfortable?)"
    hide ecmc

    show rion black pin sleep at left3
    show ecmc nojacket_v1 pin basic at right2
    "I place the coffee tray on Rion's desk then I walk over to him."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu determined_cu at ecmc_cu
    "(Hmm...how should I wake him?)"
    hide ecmc

    $menuhideborder = True
    menu rions1e11c1:
        "A. Splash water in his face.":
            $menuhideborder = False

            show rion black pin sleep at left3
            show ecmc nojacket_v1 pin basic at right2:
                pause 0.1
                easein 0.4 centre
            "I grab my water bottle and shake some water onto Rion's face."

            show rion black surprised
            ri "Huh? What?"
            "Rion blinks his eyes open, sputtering slightly as water drops fly off his face."
        "B. Call his name":
            $menuhideborder = False

            show rion black pin sleep at left3
            show ecmc nojacket_v1 pin basic at right2:
                pause 0.1
                easein 0.4 centre
            mcrion "Rion?"
            "Rion doesn't stir, so I lean in towards his ear."

            show ecmc nojacket_v1 angry
            mcrion "Rion, WAKE UP!"

            show rion black surprised
            ri "Huh? What?"
            "Rion blinks his eyes open and stares at me in confusion."
        "C. Shake his arm.":
            $menuhideborder = False

            show rion black pin sleep at left3
            show ecmc nojacket_v1 pin basic at right2:
                pause 0.1
                easein 0.4 centre
            "I grab Rion's arm and shake it."

            show ecmc nojacket_v1 angry
            mcrion "Rion, WAKE UP!"

            show rion black surprised
            ri "Huh?"
            "Rion shakes me off his arm, then blinks his eyes open in confusion."
    ri "[genericfn], what are you doing?"

    show ecmc nojacket_v1 basic
    mcrion "It's almost time for the work day to start."

    show rion black sleep
    "Rion groans and rubs his eyes."

    show rion black angry
    ri "I can't believe we stayed through the night. Today is going to be rough."

    show ecmc nojacket_v1 smile
    "I pick up Rion's coffee and hand it to him."
    mcrion "Here. This might help."

    show rion black surprised
    ri "Where did you get this?"
    mcrion "Just from the cafe on the corner. They deliver."

    show rion black smirk
    ri "Hmm...Data Drip is my favorite, but let's see how this compares."

    show rion black surprised
    "I grab my own coffee and take a sip as Rion tastes his own."
    mcrion "So...what's the verdict?"

    show rion black smile
    ri "This is actually really good!"
    ri "It's not from Data Drip, but you got the order right!"
    "I smile at Rion, then I glance over at my ARCware."

    show ecmc nojacket_v1 determined
    mcrion "We should get back to work."

    show rion black smile at left3:
        pause 0.1
        easein 0.4 left1plus
    show ecmc nojacket_v1 determined at left1:
        pause 0.1
        easein 0.4 right1
    "I start to head back to the desk, when Rion grabs my arm."
    ri "Not so fast, [genericfn]."

    show ecmc nojacket_v1 surprised
    "I try to ignore the sparks that shoot through my arm as I turn back to face Rion."
    mcrion "Is something wrong?"

    show rion black smirk
    ri "Nothing's wrong, but I think we should both take a moment to enjoy our coffee!"
    ri "I know you want to solve this case, as much as I do, but if you push too hard you'll  burn out, especially after an all-nighter."

    show ecmc nojacket_v1 sleep
    "I sigh and nod as Rion drops his hand."

    show ecmc nojacket_v1 angry
    mcrion "You're right, but it's hard to relax knowing that there could be a serial killer in this very office!"
    "I study Rion, who's sipping his coffee calmly, and narrow my arms."

    show ecmc nojacket_v1 surprised
    mcrion "How are you staying so calm?"
    ri "Because I know that stressing and panicking isn't going to help the situation."

    show rion black smile
    ri "If we're going to crack this case, we need to stay level headed."
    "I nod and take a shaky sip of my coffee, but I continue to shuffle around in agitation."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu angry_cu at ecmc_cu
    "(I know Rion's right, but I really feel so useless right now!)"
    "(I feel like we should at least be doing {i}something{/i}!)"

    show rion black pin smile at left1plus
    show ecmc nojacket_v1 pin basic at right1
    ri "So, how often do you go scrapping? Is it something you do every week?"
    mcrion "I try to. Saturday mornings are usually the best because most of the junkyards get deliveries on Fridays."

    show ecmc nojacket_v1 determined
    mcrion "So I try to go every Saturday morning, otherwise Skye will beat me to the good stuff!"

    show rion black smirk
    "Rion chuckles and takes another sip of his coffee."
    ri "What's the deal with you and Skye anyway?"

    show ecmc nojacket_v1 basic
    "I shrug and sip my own coffee."
    mcrion "I guess you can say we're frenimies."

    show ecmc nojacket_v1 determined
    mcrion "We've known each other a long time and we get along..."
    mcrion "But we're usually always fighting over who has the best tech and who's the better scrapper."

    show rion black smile
    ri "Be honest. Who is the better scrapper."

    show ecmc nojacket_v1 surprised
    mcrion "Me, of course! Skye wouldn't know good tech even if it hit him on the head."

    show ecmc nojacket_v1 smile
    "Rion chuckles and I grin back at him."
    mcrion "You're a lot chattier this morning."

    show rion black smirk
    ri "I got you calm, didn't I?"
    "Rion smirks at me as he finishes off his coffee and my eyes widen."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu smile_cu at ecmc_cu
    "(Rion's right! I am a lot more relaxed.)"
    hide ecmc

    "After Rion and I finish our coffees, we get back to work analyzing the data Enver pulled."

    show rion black pin basic at left3
    show ecmc nojacket_v1 pin headset determined at right2
    "After a couple more hours, Rion leans back in his chair and turns to look at me."
    ri "There. That's the last of the data."

    show ecmc nojacket_v1 surprised
    mcrion "But the list we've just compiled with all the D.I.V.A.A. employees and agents with suspicious fiances is almost just as long!"
    ri "It'll take us weeks to pursue every employee on this list."

    show ecmc nojacket_v1 sad
    "I groan and lean forward on the table, my head in my hands."
    mcrion "This is hopeless!"

    show rion black sad
    ri "I wouldn't call it hopeless...but it's definitely frustrating."

    show rion black angry
    ri "Now that Blythe is missing I'm sure the killer is covering their tracks as fast as possible."
    ri "We don't have {i}weeks{/i} to go through a list..."
    "Rion lets out a frustrated huff and tugs on his hair which is a bit tousled from when he was sleeping against the wall."
    ri "Everytime I think we're getting closer, it's as if we take ten steps back!"
    ri "The killer is slipping right through our fingers and there's nothing we can do about it."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu headset_cu surprised_cu at ecmc_cu
    "(Rion seems so frustrated. What would be the best course of action?)"
    hide ecmc

    $menuhideborder = True
    menu rions1e11c2:
        "A. Start going through the list now.":
            $menuhideborder = False
            show rion black pin angry at left3
            show ecmc nojacket_v1 pin headset determined at right2
            mcrion "Well, we might as well start going through this list now."
            mcrion "Maybe it'll be quicker than we think?"
            ri "This just seems like such a waste of time."

        "B. Think of ways to narrow the list down.":
            $menuhideborder = False
            show rion black pin angry at left3
            show ecmc nojacket_v1 pin headset angry at right2
            mcrion "There must be a way to narrow the list down."
            mcrion "Maybe we can take a deeper dig at the dates of the transactions?"
            mcrion "If someone doesn't have a weird transaction around the same time Skye sold that device, we can eliminate them."
            ri "That will still take a long time to sort through!"

        "C. Suggest getting more help.":
            $menuhideborder = False
            show rion black pin angry at left3
            show ecmc nojacket_v1 pin headset determined at right2
            mcrion "Rion, I know you didn't want to involve too many people, but maybe it's time to do so?"
            mcrion "I'm sure Eko would be able to help us narrow this list down really quickly."

            show rion black sleep
            "Rion lets out a defeated sigh and gives me a small nod."

            show rion black angry
            ri "You might be right. I guess it's something I'll need to consider."

    play sound "<from 0 to 0.5>audio/sfx/phone 02.mp3"
    show rion black surprised
    show ecmc nojacket_v1 determined
    "Rion drums his fingers on the desk in concentration, when we both get a ping on our ARCware."

    show ecmc nojacket_v1 surprised
    mcrion "It's Eko! It looks like Skye's data is ready."

    hide ecmc
    hide rion
    show rion black_cu smile_cu at rion_cu
    "Rion gets up abruptly and helps me to my feet, his hand lingering on mine a moment longer than necessary."
    ri "Come on. Let's go to the lab."

    scene bg ecm_office_lab_on at bg
    show eko casual glasses pin basic at centre
    with wiperightdissolve
    stop music
    play music ecmekotheme

    "Rion and I reach the lab where Eko's waiting for us."

    show rion jacket pin smile at left3
    show eko casual basic at right3
    ri "Hi, Eko. Thank you for recovering that data so quickly."

    show eko casual smile
    ek "It's no problem. The wipe actually wasn't as bad as I initially thought."
    ek "Plus, I knew how important this was to your case, so I made it a priority."
    ri "I really appreciate it, Eko. You're a lifesaver!"

    hide rion
    show ecmc nojacket_v1 pin smile at left3
    mcrion "Thanks, Eko. We were at a bit of a standstill, so this should really help."

    hide ecmc
    show rion jacket pin basic at left3
    ri "We're going to take a look at this now."

    show rion jacket sad
    ri "I'm sorry, Eko, but do you mind giving us a bit of privacy?"
    ek "Sure, but do you just want the privacy to work?"
    "Eko winks at us."

    show rion jacket surprised
    "I feel my face flush with embarrassment and even Rion seems a little tongue-tied."

    show eko casual basic at right3, out_right
    pause 0.4
    "Before either of us can respond, Eko heads over to the other side of the lab and starts doing some work."
    hide eko

    show rion jacket basic
    show ecmc nojacket_v1 pin blush embarrassed at right2
    ri "Okay, let's go take a look at Skye's list."
    "I follow Rion over to a terminal, my face still feeling a little red."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu blush_cu embarrassed_cu at ecmc_cu
    "(I know Eko was just joking, but the thought of Rion and I wanting privacy for {i}other{/i} reasons makes me feel so embarrassed!)"
    "(Although...I can't deny the thought excites me as well.)"
    hide ecmc

    show rion jacket pin basic at left3
    show ecmc nojacket_v1 pin determined at right2
    "I push my thoughts out of my head and sit down beside Rion."

    show rion jacket angry
    ri "Alright, I think what we can do is cross-reference the list of D.I.V.A.A. agents we compiled before with Skye's list."
    ri "Maybe we can match up some of the purchase amounts from the anonymous buyers?"
    mcrion "That sounds like a good place to start."
    "Rion downloads Skye's list and we quickly run a program to compare the amounts on Skye's list with the amounts from the purchase listing."

    show rion jacket smirk
    ri "This is definitely narrowing things down."

    show ecmc nojacket_v1 surprised
    mcrion "This is strange. Most of Skye's anonymous deals actually seem to go back to the same person."
    mcrion "Almost all of those transactions can be cross referenced to our D.I.V.A.A. list!"

    show rion jacket basic
    ri "Unfortunately, whoever made the purchases here managed to keep their log in private."
    ri "It looks like they used a common terminal from the records room."

    show ecmc nojacket_v1 determined
    mcrion "I wonder if it's being used right now? Maybe we can access the terminal and find out who's used it?"
    ri "Let's take a look."
    "Rion runs a scan and remotes into the terminal in the records room."

    show rion jacket angry
    ri "Someone's using the terminal right now! And...it appears they've hidden their login credentials."

    show ecmc nojacket_v1 surprised
    "I look at Rion in shock."
    mcrion "Do you think it's the killer?"
    ri "There's only one way to find out!"

    show rion jacket angry at out_right
    show ecmc nojacket_v1 surprised at out_right
    "Without another word, Rion and I jump to our feet and rush out of the lab."

    scene bg ecm_records_room_on at bg with wiperightdissolve
    stop music
    play music ecmtense1
    "Rion and I race into the records room and find the terminal, but there's no one to be seen."

    show rion jacket pin basic at left3
    show ecmc nojacket_v1 pin determined at right2
    mcrion "This is strange..."

    show rion jacket angry
    ri "Maybe whoever was here just left, but we should still be cautious."

    show ecmc nojacket_v1 headset determined with dissolve
    "I put my ARCware on and slowly make my way towards the terminal."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu headset_cu angry_cu at ecmc_cu
    "(Nothing seems out of place...)"
    hide ecmc

    show rion jacket pin angry at left3:
        pause 0.1
        easein 0.4 left1
    show ecmc nojacket_v1 pin headset determined at right2
    "Rion reaches the terminal and presses a few buttons."

    show rion jacket smirk
    ri "Whoever just used this is still logged in! Let's figure out who it was."

    show rion jacket surprised
    show ecmc nojacket_v1 surprised

    show white at full_size with dissolve:
        alpha 0.9
    hide white
    show smoke_effect behind rion:
        alpha 0.6
    with dissolve
    "Rion is about to tap another button, when suddenly the metal doors shut with a bang and strange gas starts entering the room from the vents."
    mcrion "What's going on?"

    show rion jacket angry
    ri "This was a trap!"

    show ecmc nojacket_v1 surprised at right2:
        pause 0.1
        easein_back 0.4 right4
    "I frantically race to the door and yank on it."

    show ecmc nojacket_v1 angry
    mcrion "It won't budge!"

    show rion jacket angry at left1:
        pause 0.1
        easein 0.4 centre xoffset 40

    play sound "<from 0 to 0.5>audio/sfx/phone 02.mp3"
    "Rion starts to run to my side, when his ARCware pings"
    ri "I think someone's calling me."
    mcrion "Tell them to get help!"

    stop music
    play music ecmplottwist2
    hide rion
    hide ecmc
    show anton casual basic at holo_mask, anton_holo, centre
    hide anton with dissolve
    show anton casual basic at holo_mask, anton_holo, centre
    "Rion answers the call and a hologram of Anton appears in front of us."

    show rion jacket pin angry at left3
    show anton casual smile at holo_mask, anton_holo, right4
    ri "Anton? What do you want?"
    an "To gloat, of course."

    show rion jacket surprised
    ri "Gloat?"
    "Rion looks momentarily confused, then his facial expression morphs into one of anger."

    show rion jacket angry
    ri "YOU! It was you this entire time!"
    an "Of course it was, Rion."
    an "I was in front of your face the entire time, but you were too blind to see it."
    an "I always thought your reputation as being one of D.I.V.A.A.'s best wasn't warranted."

    hide rion
    show ecmc nojacket_v1 pin angry at left3
    mcrion "Anton, why are you doing this? Why are we trapped in here?"
    an "Because the two of you were finally getting close to catching me."
    an "I've gone to great lengths to get away with my experiments and stay hidden..."
    an "And I have no problem killing any agents who get in my way."

    hide ecmc
    show rion jacket pin angry at left3
    ri "You're not as smart as you think you are, Anton."
    ri "You've just outed yourself. Now we all know you're the killer!"
    an "It doesn't matter. It's not like the two of you have any chance of escaping before that gas kills you."

    hide rion
    hide anton
    show anton casual_cu smile_cu at holo_mask, anton_holo, anton_cu
    "Anton smirks, his eerie facial expression lit up by the hologram."
    an "Once the two of you are gone, no one will know it was me this whole time."
    an "Even if they figure it out, I'll be so far away that it won't matter."
    hide anton

    show ecmc nojacket_v1 pin angry at left3
    show anton casual smile at holo_mask, anton_holo, right4
    mcrion "Why did you call us?"
    an "The two of you have been a thorn in my side for the past couple of weeks."
    an "Now I finally get to watch you suffer for the problems you've caused me!"

    show ecmc nojacket_v1 surprised
    mcrion "Problems?! You're the problem, Anton."

    show ecmc nojacket_v1 angry
    "I pull my badge out and glare at him."
    mcrion "Doesn't this mean anything to you?"
    mcrion "You're a traitor, Anton. You never deserved to wear D.I.V.A.A.'s badge."

    hide ecmc
    show rion jacket pin angry at left3
    ri "I always thought you were scum, Anton, but it turns out you're even worse."
    ri "I can't believe you would just kill innocent people, for what? Fun?"

    show anton casual angry at holo_mask, anton_holo, right4
    an "Fun?!"
    "Anton actually looks offended as he glares back at Rion."
    an "Killing people was never about fun. I killed for something much bigger than that."
    an "A greater purpose if you will."

    hide rion
    show ecmc nojacket_v1 pin determined at left3
    mcrion "What greater purpose?"

    show anton casual smile at holo_mask, anton_holo, right4
    an "As if you would understand. Your mind is too simple, [genericfn]."
    an "But Blythe and her patrons understood me. You see, there's so much more to consciousness than anyone's realized before."
    an "With cybernetic technology, there's so much that we can do. So much we can unlock."

    show anton casual angry at holo_mask, anton_holo, right4
    an "My experiments are only just getting started and I won't let anyone get in the way of that!"

    hide ecmc
    show anton casual angry at holo_mask, anton_holo, centre
    pause 0.2
    hide anton with dissolve
    pause 0.4
    "Anton abruptly ends the call, his hologram disappearing from the room."

    show rion jacket pin angry at left2
    show ecmc nojacket_v1 pin sad at right2
    "I turn to Rion in fear as more gas fills the room."

    show ecmc nojacket_v1 angry
    mcrion "Rion, we need to get out of here. Call someone for help!"
    "Rion pulls out his phone and curses."
    ri "No signal. Anton must have jammed it after he hung up."
    mcrion "I think I can unlock the door. It can't be that difficult."

    show rion jacket sleep
    "Rion shakes his head."

    show rion jacket angry
    ri "I know this building well. The locking system looks simple, but it's extremely intense."
    ri "I have a plan, but it'll take trust and time."

    hide ecmc
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    "Rion looks me in the eye, holding my gaze as if he's trying to read me and reassure me at the same time."
    hide rion

    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(I'm not sure what Rion's plan is. Should I trust that he knows what he's doing?)"
    hide ecmc

    show rion jacket_cu angry_cu at rion_cu
    ri "I trust you, [genericfn]. You need to trust me too."
    ri "We can escape if we work together and I'll need your tech skills."

    show rion jacket_cu smirk_cu
    ri "Please, [genericfn]? My plan won't work unless you help me."
    hide rion

    $menuhideborder = True
    menu rions1e11c3:
        "A. Trust Rion and escape the room." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show ecmc nojacket_v1_cu determined_cu at ecmc_cu
            mcrion "I trust you, Rion."
            hide ecmc

            show rion jacket_cu smirk_cu at rion_cu
            "I close the gap between us as Rion's face lights up."
            hide rion

            show rion jacket pin smirk at left1plus
            show ecmc nojacket_v1 pin determined at right1plus
            mcrion "What's your plan?"
            ri "If we both trip the right circuits, we can get the locks on the door to fail."

            show rion jacket angry
            ri "I need your help because there are two panels. If you take the ones on the left, I'll take the ones on the right."

            show ecmc nojacket_v1 angry
            "Gas starts to creep into my lungs and I let out a cough."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu angry_cu at ecmc_cu
            "(We don't have much time!)"

            show rion jacket pin angry at left1plus
            show ecmc nojacket_v1 pin determined at right1plus:
                pause 0.1
                easein 0.4 right4
            "I race to the left and find the access panel."
            mcrion "How do I get this off?"
            ri "We'll need to share my omnipick. That should do it."

            show rion jacket angry at left1plus:
                pause 0.1
                easein 0.4 centre xoffset 40
            "Rion hastily undoes his panel then he races across the room to hand it to me."

            hide ecmc
            hide rion
            show rion jacket_cu angry_cu at rion_cu
            "Our hands brush and despite the situation, my heart flutters and I momentarily forget the situation as I look into Rion's eyes."
            ri "[genericfn], quick!"
            hide rion

            show rion jacket pin angry at centre:
                xoffset 40
            show ecmc nojacket_v1 pin blush surprised at right4
            "I blush as I snap out of it and hastily remove the panel."
            ri "Do you know what you're doing?"

            show ecmc nojacket_v1 angry
            mcrion "If I had time I'd be able to figure it out, but I'm not familiar with this circuit!"
            ri "Each circuit board in this room controls just half of the electricity. So be careful to only disconnect the doors."

            show rion jacket angry at centre:
                pause 0.1
                easein 0.4 left2 xoffset 0
            "I nod and Rion hurries back to the other panel to start work."
            ri "Do you have tools to snip the wires?"

            show ecmc nojacket_v1 surprised
            mcrion "I should have something."

            hide rion
            show ecmc nojacket_v1 determined at centre
            "I dig through my backpack until I find what I need, then I turn my attention back to the circuit board."

            hide ecmc
            show ecmc nojacket_v1_cu determined_cu at ecmc_cu
            "(Alright, I can do this! I've worked on plenty of circuit boards before. This can't be that tricky!)"
            hide ecmc

            show ecmc nojacket_v1 pin determined at centre
            "I try to wrap my head around the wire puzzle in front of me, but the gas is getting thicker now and it's getting harder to breathe."

            hide ecmc
            show ecmc nojacket_v1_cu sad_cu at ecmc_cu
            "(Oh my bot! We're not going to make it!)"
            hide ecmc

            show ecmc nojacket_v1 pin sad at centre
            "I start to panic, my vision getting cloudy, as I shakily reach for one of the wires."

            hide ecmc
            show ecmc nojacket_v1_cu sad_cu at ecmc_cu
            "(I don't know what I'm doing! We're going to die!)"
            hide ecmc

            show rion jacket_cu angry_cu at rion_cu
            ri "[genericfn]!"
            "I'm snapped out of my spiraling thoughts by Rion's voice and I look up to see him beside me."
            ri "You're panicking. You need to focus on your breathing. Take a deep breath."

            show rion jacket_cu basic_cu
            "I nod and close my eyes as I take a deep breath, then Rion continues to talk, his soothing voice helping to calm me down."
            ri "Now keep breathing in and out. Forget about the gas, [genericfn]. Focus on the wires."

            show rion jacket_cu smile_cu
            ri "You {i}know{/i} how circuits work. You've got this. Just keep breathing."
            "When my breathing is regular again, I open my eyes and give Rion a weak smile."
            hide rion

            show ecmc nojacket_v1_cu smile_cu at ecmc_cu
            mcrion "Thanks, Rion."
            hide ecmc

            show rion jacket_cu angry_cu at rion_cu
            ri "I'd better get back to my panel. Let me know if you need any help."
            hide rion

            show ecmc nojacket_v1 pin determined at centre
            "Rion races back to his panel, and I take another deep breath"

            hide ecmc
            show ecmc nojacket_v1_cu determined_cu at ecmc_cu
            "(Rion's right. I know how these panels work.)"
            "(I need to start with the green wire.)"
            hide ecmc

            show ecmc nojacket_v1 pin surprised at centre
            "I cut the green wire and hear a click at the door."

            hide ecmc
            show ecmc nojacket_v1_cu smile_cu at ecmc_cu
            "(Perfect.)"
            hide ecmc

            show rion jacket pin angry at left2
            show ecmc nojacket_v1 pin surprised at right2
            ri "Remember to avoid the red wires, [genericfn]. They could electrocute you."
            ri "They're all fake wires put in as a trap for intruders."

            show ecmc nojacket_v1 determined
            mcrion "I've got this, Rion."
            "I keep snipping the wires as Rion does the same."
            ri "Done!"

            show rion jacket angry at left2:
                pause 0.1
                easein 0.4 left1
            pause 0.4
            "I hear the sound of half the door disconnecting, then Rion starts to walk to my side."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu angry_cu at ecmc_cu
            "(I need to hurry! I'm almost there!)"
            hide ecmc

            show rion jacket pin angry at left1
            show ecmc nojacket_v1 pin determined at right3
            "The gas is so thick now that it stings my eyes, making it hard to see."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu angry_cu at ecmc_cu
            "(Almost...there...)"
            hide ecmc

            show rion jacket pin angry at left1
            show ecmc nojacket_v1 pin sad at right3
            "I'm about to cut the last wire, when my hands start shaking uncontrollably."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu sad_cu at ecmc_cu
            "(One...more...)"
            hide ecmc

            "My hands fall to my side and my eyes start to close."
        "B. Struggle alone with the door.":
            $menuhideborder = False
            # [Visual effect - Purple smoke]

            show rion jacket pin angry at left2
            show ecmc nojacket_v1 pin determined at right2
            mcrion "I still think the door is the way to go."

            show ecmc nojacket_v1 determined at right2:
                pause 0.1
                easein 0.4 right4
            "Before Rion can protest, I run to the door and pull out my tools."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu angry_cu at ecmc_cu
            "(I've broken several locks before. This can't be too hard!)"
            hide ecmc

            show rion jacket pin angry at left2:
                pause 0.1
                easein 0.4 left4
            show ecmc nojacket_v1 pin determined at right4
            "Behind me, Rion runs to one of the circuit boards and starts cutting wires."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
            "(I think he's trying to disconnect the door. There's no way he'll be able to get that done before the gas fills the room!)"
            hide ecmc

            show ecmc nojacket_v1 pin determined at centre
            "I continue to try and break the door open, but to no avail."
            hide ecmc

            show ecmc nojacket_v1_cu sad_cu at ecmc_cu
            "(This is impossible!)"
            hide ecmc

            show ecmc nojacket_v1 pin determined at centre
            "The gas is thick and heavy in the room and now I'm struggling to breathe."
            hide ecmc

            show ecmc nojacket_v1_cu sad_cu at ecmc_cu
            "(I just...need...to...hold on.)"

    hide ecmc
    "The world around me starts to go black as I crumple to the floor."
    "As I feel myself fade into nothingness, one face flashes in my mind."

    show ecmc nojacket_v1_cu sad_cu at ecmc_cu
    "(Rion...)"
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

