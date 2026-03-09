label rion_season1_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_sidewalk_day at bg with fade
    play music ecmriontheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show rion jacket pin basic at right2
    show ecmc jacket_v2 pin surprised at left2, left_in
    "I hurry along beside Rion as he strides down the street."
    mcrion "Rion, where are we going?"
    "Rion doesn't even look at me as he walks, his eyes straight ahead."
    ri "An art gallery."
    mcrion "Why?"

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(I feel annoying being so pushy, but Rion really isn't giving me much...)"
    hide ecmc

    show rion jacket pin surprised at right2
    show ecmc jacket_v2 pin basic at left2
    "Rion finally shoots a quick glance my way, furrowing his brow slightly."

    show rion jacket basic
    ri "I checked the background of the victim you found in the alley."
    ri "They're a patron of an art gallery owned by a woman named Blythe."

    show ecmc jacket_v2 surprised
    mcrion "Okay...but what does that have to do with the case?"

    show rion jacket surprised
    ri "I did some digging yesterday, and I finally confirmed something I've suspected for a while."

    show rion jacket angry
    ri "Every case victim is connected to this gallery in some way."

    show ecmc jacket_v2 basic
    ri "Blythe isn't a suspect at the moment, nothing points to her, but I have a hunch that we'll find something useful if we go."

    show rion jacket angry at out_right
    "Rion turns his gaze forwards again and continues to stride ahead."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(He seems so focused...but it feels a little awkward walking together in silence.)"

    show ecmc jacket_v2_cu surprised_cu
    "(He has to respond to {i}something{/i}.)"
    hide ecmc

    show rion jacket pin basic at right2
    show ecmc jacket_v2 pin surprised at left2
    mcrion "Rion..."

    hide rion
    hide ecmc
    $menuhideborder = True
    menu rions1e4c1:
        "A. Chat about the weather.":
            $menuhideborder = False

            show rion jacket pin basic at right2
            show ecmc jacket_v2 pin surprised at left2
            mcrion "It's very...sunny."

            show ecmc jacket_v2 blush embarrassed
            "I mentally facepalm as my face flushes."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "(That's so lame! I could have come up with something better.)"
            hide ecmc

            show rion jacket pin smirk at right2
            show ecmc jacket_v2 pin blush embarrassed at left2
            "Rion doesn't look at me, but the corner of his lips turns up very slightly into a smirk."
            ri "Yes. At least we don't have to walk in the rain."

        "B. Ask about basketball.":
            $menuhideborder = False
            show rion jacket pin basic at right2
            show ecmc jacket_v2 pin surprised at left2

            mcrion "Did you watch the basketball game yesterday?"
            mcrion "I heard it was a close one."

            show rion jacket smile
            show ecmc jacket_v2 basic
            ri "I didn't. I like playing basketball, but I'd rather watch soccer."

        "C. Mention a new restaurant in town.":
            $menuhideborder = False

            show rion jacket pin basic at right2
            show ecmc jacket_v2 pin smile at left2
            mcrion "Have you been to the new Chinese restaurant?"
            mcrion "I was thinking of checking it out."

            show rion jacket smile
            ri "I went the other day. It's not bad."

    show rion jacket basic
    show ecmc jacket_v2 -blush basic
    "We resume walking in silence."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I can't tell if he's focusing on work, if he's not one for small talk, or if he finds me annoying.)"
    hide ecmc

    show rion jacket pin basic at right2
    show ecmc jacket_v2 pin surprised at left2
    "I'm about to blurt out another question when I glance at Rion and stop myself."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(He doesn't look agitated or uncomfortable. I think I'm overthinking this.)"
    hide ecmc

    show rion jacket pin basic at right2
    show ecmc jacket_v2 pin basic at left2
    "A few minutes later Rion stops walking."

    show rion jacket smile
    ri "Here we are."

    show rion jacket basic
    show ecmc jacket_v2 surprised
    mcrion "Can we just go in?"

    show ecmc jacket_v2 basic
    "Rion walks up to the door and takes a look."

    show rion jacket angry
    ri "It's locked."

    show rion jacket basic
    show ecmc jacket_v2 surprised
    mcrion "Maybe we can wait for--"

    show rion jacket smirk
    ri "No need."
    "Rion pulls a chrome omni-lockpick out of his pocket."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(How did he get that model?! That can't be D.I.V.A.A. standard issue.)"
    hide ecmc

    show rion jacket pin smirk at right2
    show ecmc jacket_v2 pin surprised at left2
    mcrion "Wait! Don't we need a warrant?"
    "Rion shrugs and casually twirls the omni-lockpick in his hand."

    show rion jacket smile
    ri "I've already applied for it, so we should be fine. It's just a formality at this point."

    show rion jacket smirk
    show ecmc jacket_v2 embarrassed
    mcrion "Are you sure this is a good idea? Maybe we should wait?"

    show ecmc jacket_v2 basic
    ri "It's best we get to the scene while it's fresh."

    show rion jacket angry
    ri "If we wait, the owner may tamper with evidence, even if she doesn't realise it."

    show rion jacket smirk
    show ecmc jacket_v2 embarrassed
    mcrion "I guess that makes sense..."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(I don't think we should be breaking procedure, but Rion's in charge.)"

    show rion jacket pin basic at right2
    show ecmc jacket_v2 pin basic at left2
    "Rion casts a furtive look down the street, then quickly unlocks the door with the omni-lockpick."

    show rion jacket smirk
    ri "I'll go in first to make sure it's clear. Follow me."

    stop music
    play music ecmtense2
    scene bg ecm_artgallery_day at bg with wiperightdissolve

    "I cautiously follow Rion into the gallery, watching out for any traps or alarms."

    show rion jacket pin surprised at right2
    show ecmc jacket_v2 pin basic at left2
    ri "The coast looks clear. Nothing seems out of place."

    show rion jacket angry
    ri "Stay close to me, Hatchling. Don't touch anything."

    show rion jacket basic
    show ecmc jacket_v2 surprised behind rion at left2:
        easein_back 0.4 left1 xoffset 20
    "I move a little closer to Rion and accidentally brush my arm up against him."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Oh!)"

    show ecmc jacket_v2_cu blush_cu surprised_cu
    "I suppress a gasp as goosebumps prick on my skin."

    show ecmc jacket_v2_cu embarrassed_cu
    "(I need to focus! We're here on an investigation.)"
    hide ecmc

    show rion jacket pin basic at right1plus
    show ecmc jacket_v2 pin basic at left1plus
    "Rion doesn't even seem to notice my reaction as he heads towards a twisted statue."

    hide rion
    hide ecmc
    "It's made of scrapped parts welded together in the shape of an android. The more I look the more unnerving it gets."

    show rion jacket pin surprised at right1plus
    show ecmc jacket_v2 pin basic at left1plus
    ri "That's...interesting. Someone's got a thing for robots and junk."

    show rion jacket basic
    show ecmc jacket_v2 surprised
    mcrion "It's kind of fascinating. I could never make something this sculpted with all the scrap I find."

    show rion jacket surprised
    show ecmc jacket_v2 basic
    ri "The components are great, but I don't understand the point of it."
    ri "Feels like a waste."

    hide rion
    hide ecmc
    "I'm about to reply when footsteps echoing down the hallway cause me to freeze."

    show ecmc jacket_v2 pin surprised behind rion at centre:
        pause 0.4
        easein 0.4 xoffset 70
    show rion jacket pin angry at centre:
        pause 0.4
        easein 0.4 xoffset -50
    "Rion mutters under his breath, then moves slightly in front of me as a woman appears in the doorway."

    hide rion
    hide ecmc
    show blythe casual angry at centre
    "She glares at Rion and I, then immediately pulls out her holophone."
    snootyw "Who are you and how did you get in here?"
    snootyw "Make it quick before I call the police."
    hide blythe

    show ecmc jacket_v2 pin basic at centre:
        transform_anchor True rotate 0
        xoffset 70 rotate 3
    show rion jacket pin basic at centre:
        xoffset -50
    "Rion confidently whips out his badge, his body still angled slightly in front of mine."
    ri "We're D.I.V.A.A. agents here on an investigation."
    ri "You must be Blythe?"

    show blythe casual angry at left3
    show rion jacket basic at right3
    show ecmc jacket_v2 basic at right3
    bh "Correct. Now, what's this investigation about?"

    show rion jacket angry
    ri "I can't divulge that information right now, but neither you or the gallery are being implicated."
    bh "Do you at least have a warrant?"

    show rion jacket smirk
    ri "Just waiting for the ink to dry."
    bh "Hmm..."
    ri "Someone will follow up with you later on in the day. They'll have a report for you and I'll make sure they show you the warrant then."
    "Blythe crosses her arms over her chest as she sizes Rion up and down."

    hide blythe
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Rion seems so relaxed! I guess he's playing it cool to squash Blythe's suspicion.)"
    hide ecmc

    show blythe casual angry at left3
    show ecmc jacket_v2 pin basic at right3:
        transform_anchor True rotate 0
        xoffset 70 rotate 3
    show rion jacket pin basic at right3:
        xoffset -50
    bh "I'll give you the benefit of the doubt for now, but only because I know D.I.V.A.A.'s done good work recently."

    show blythe casual smile
    bh "Plus, some of your agents have genuine appreciation for what we do here."

    show rion jacket surprised
    "Rion raises his eyebrow just a fraction, but it's enough for me to notice his surprise at the statement."

    hide blythe
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I wonder who Blythe knows?)"
    hide ecmc

    show blythe casual_cu angry_cu at blythe_cu
    bh "It's still extremely rude for you to come here without a warrant in hand."
    hide blythe

    show blythe casual basic at left3, left_in
    show ecmc jacket_v2 pin basic at right3:
        transform_anchor True rotate 0
        xoffset 70 rotate 3
    show rion jacket pin basic at right3:
        xoffset -50
    "Blythe walks into the room, her gaze still fixated on us. She throws me a glance, then looks back at Rion in fascination."

    show blythe casual smile
    bh "Your eye is certainly unique. I've never seen anything quite like it."
    bh "It's cutting-edge, chic. A real work of art."
    "Rion doesn't respond, but he moves to adjust his eye as he stares Blythe down."
    bh "It's easily the best thing about you."

    show rion jacket smirk
    "Rion gives Blythe a tight-lipped smile, without uttering a sound."

    hide rion
    hide blythe
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Must...change...topic...)"
    hide ecmc

    "I look around the gallery and notice a sign about an upcoming exhibition."

    show blythe casual basic at left3
    show rion jacket pin basic at right3:
        xoffset -50
    show ecmc jacket_v2 pin surprised at right3:
        transform_anchor True rotate 0
        xoffset 70 rotate 3
    mcrion "Can you tell us about the show opening soon?"
    "Blythe tears her gaze away from Rion and I notice his shoulders sag a little in relief."

    show ecmc jacket_v2 basic
    bh "Oh, yes, do be careful."

    show blythe casual smile
    bh "It'll be one of the {i}biggest{/i} events in L.A., and it's crucial that none of the works are interfered with."
    "Blythe gives Rion a pointed look as she sneers slightly."

    show ecmc jacket_v2 surprised
    mcrion "What's the exhibition about?"

    show blythe casual sad
    show ecmc jacket_v2 basic
    "Blythe takes a deep breath and gets a wistful look in her eye."
    bh "The {i}mystery{/i} of consciousness and identity in this robotic age."
    bh "I doubt you'd understand. This kind of art appeals to a more...{i}refined{/i} pallet."

    show rion jacket surprised
    "Rion cocks his eyebrow at that."

    show blythe casual basic
    ri "What kind of clientele does your gallery usually attract?"

    show blythe casual smile
    show rion jacket basic
    bh "Oh, a very specific one."
    bh "Most of my patrons are rogue thinkers who are passionate about cybernetics, and the {i}full{/i} potential of them."
    "Blythe waves her hand around, indicating all of the pieces on display, as she speaks."

    show ecmc jacket_v2 surprised
    mcrion "What does that mean, exactly?"

    show blythe casual angry
    show ecmc jacket_v2 basic
    "Blythe scoffs, looking down her nose at me."
    bh "Of course you don't understand."
    bh "But essentially, this collection looks at the purity of robotics and how technology can be used to improve and enhance human qualities."

    hide blythe
    hide ecmc
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    "Rion flinches at that, and I turn my head slightly to look at him as the pieces start to fit together."
    hide rion

    show blythe casual angry at left3
    show rion jacket pin basic at right3:
        xoffset -50
    show ecmc jacket_v2 pin basic at right3:
        transform_anchor True rotate 0
        xoffset 70 rotate 3
    bh "Alright, I've wasted enough time on this. I have a lot of work to do."

    show blythe casual smile
    bh "Maybe when I get more information from the report you mentioned, we can arrange a longer session."
    "Blythe smirks at Rion as she narrows in on his eye."

    hide rion
    hide ecmc
    hide blythe
    show blythe casual_cu smile_cu at bly
    bh "If you ever want to be useful, you can donate that eye. I know some artists who would love to use it."
    hide blythe

    show rion jacket_cu angry_cu at rion_cu
    "Rion ignores Blythe, but his shoulders tense as he tweaks his eye just enough for me to notice."
    hide rion

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "Come on, [genericfn]. We're done here."

    stop music
    play music ecmemotional2

    scene bg ecm_sidewalk_day at bg with fade

    show rion jacket pin basic at right1plus
    show ecmc jacket_v2 pin basic at left1plus
    "Rion and I leave the gallery and begin walking towards the train station to ride back to HQ."

    show rion jacket angry
    "Rion's silent, but his feet hit the pavement harder than normal and his hands are visibly tense."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I've never seen Rion like this before. Something's definitely up.)"
    hide ecmc

    show rion jacket pin basic at right1plus
    show ecmc jacket_v2 pin surprised at left1plus
    mcrion "So...do you think Blythe could be involved in the case?"

    show rion jacket angry
    ri "That witch?"
    "Rion turns to look at me, his face contorted in annoyance."
    ri "Wouldn't surprise me. 'Refined pallet' my ass."
    ri "She wouldn't know what that meant if it hit her in the face."
    ri "Having money doesn't give you good taste."

    show rion jacket angry:
        linear 0.4 right3
    show ecmc jacket_v2 sad
    "Rion stomps a little harder, huffing slightly in agitation."
    "After a few more steps, Rion lets out a frustrated sigh and stops walking, turning to face me instead."

    stop music
    play music ecmcalmeveryday4

    hide ecmc
    hide rion
    show rion jacket_cu basic_cu at rion_cu
    "He sighs as he looks at me and his expression softens."
    ri "I'd really like to walk around for a bit, just clear my head."

    show rion jacket_cu smirk_cu
    ri "One of my old stomping grounds is nearby, it's a good place to relax."
    hide rion

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(It sounds like he does need a breather, and I can only imagine what sorts of places he used to spend time in.)"
    hide ecmc

    show rion jacket_cu smirk_cu at rion_cu
    ri "You up for it, Hatchling?"
    hide rion

    $menuhideborder = True
    menu rions1e4c2:
        "A. Learn more about Rion on a walk." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "Sure! A walk sounds refreshing!"
            "(And maybe it will get Rion to open up.)"
            hide ecmc

            stop music
            play music ecmromantic2
            show rion jacket_cu smirk_cu at rion_cu
            ri "Come with me."
            hide rion

            "I walk by Rion's side as he guides us towards an unfamiliar neighbourhood."

            show rion jacket pin basic at left2
            show ecmc jacket_v2 pin surprised at right2
            mcrion "Where are we?"
            "Rion doesn't say anything and at first I think he didn't hear me, but then I realise he's deep in thought."

            show rion black pin angry at left2 with dissolve
            "After taking his jacket off in agitation, he lets out an angry huff."
            ri "Man! Some people!"

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(He must be talking about Blythe.)"
            hide ecmc

            show rion black pin angry at left2
            show ecmc jacket_v2 pin sad at right2
            mcrion "Yeah, she was a piece of work."
            ri "I get that no one's really happy to see D.I.V.A.A. agents unexpectedly show up, but she took it to a whole different level."
            mcrion "I agree. She was completely condescending."
            mcrion "She was acting like we were children!"
            ri "I can't stand people {i}that{/i} self-important."
            ri "She's human, just like you and me."

            show ecmc jacket_v2 angry
            mcrion "Yeah, I couldn't stand how she talked down to us!"

            show rion black basic
            show ecmc jacket_v2 basic
            ri "Well, that's just how some people are. They think they're better than anyone they consider 'beneath' them."
            "Rion sighs, then gestures around the neighbourhood."
            ri "People like Blythe have trouble connecting with regular people."

            hide rion
            hide ecmc
            "I look around the neighbourhood and notice the run down buildings and chipped pavement."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(We're in one of the poorer areas of L.A.. I've never been to this neighbourhood.)"
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "I look over at Rion whose hands are in his pockets, his shoulders loose."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(He's definitely more at home here than the art gallery.)"
            hide ecmc

            show rion black pin basic at left2
            show ecmc jacket_v2 pin sad at right2
            mcrion "I think a lot of rich people are like that."
            mcrion "I wish they could get a dose of reality, anything to put them in-touch with how everyone else lives."

            show rion black sad
            ri "Yeah..."

            show rion black sleep
            "Rion lets out a sigh then grits his teeth slightly as he replies."

            show rion black sad
            ri "The elite-art world's always been out of touch."
            ri "But part of the problem is the elite-art clientele don't care about mixing with those beneath them."
            ri "They don't care about understanding the wants and needs of people that aren't like them."

            show ecmc jacket_v2 surprised
            mcrion "Well, it's their loss. You can't experience the world if you live in a bubble."

            show ecmc jacket_v2 sad
            mcrion "High-art may be beautiful, but it can also be soulless."
            "Rion nods, his gaze drifting around the neighbourhood."

            hide rion
            hide ecmc
            "Across the street, a homeless man is sitting on a step, a paper cup in his hand."
            "A little boy walks past and throws some money in the box by the man's feet, and Rion flashes his first genuine smile of the day."

            show rion black pin smile at left2
            show ecmc jacket_v2 pin smile at right2
            ri "Good to know that some people in this world still have compassion."

            show rion black sad
            show ecmc jacket_v2 basic
            "Rion sighs and turns to look at me, his expression unreadable."

            hide ecmc
            hide rion
            show rion black_cu basic_cu at rion_cu
            ri "You ready to get out of here?"
            hide rion

            show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
            "I look into Rion's eyes and chew on my bottom lip."

            show ecmc jacket_v2_cu smile_cu
            mcrion "Are you? If you'd like to walk a little more, I'm not in a rush."
            hide ecmc

            show rion black_cu smirk_cu at rion_cu
            ri "Just wanted to clear my head. Coming out here helped."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "Do you come here often?"
            hide ecmc

            show rion black_cu smirk_cu at rion_cu
            ri "Every now and then."
            ri "I like this part of the city. I know it may not be the nicest but it's always felt comfortable."

            show rion black_cu sad_cu
            "A brief look of vulnerability flashes in Rion's eyes."
            hide rion

            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(Rion likes high-quality things like tech, but something tells me that he didn't have much growing up.)"
            "(I wonder if he grew up somewhere like here.)"
            hide ecmc

            show rion jacket pin sad at left2
            show ecmc jacket_v2 pin basic at right2
            "Rion puts his jacket back on and straightens up as he nods at the direction we came from."

            show rion jacket smile
            ri "Come on. Let's head back to HQ."

            show rion jacket basic at left2, step_out
            pause 0.2
            show ecmc jacket_v2 basic at right2, step_out
            "I follow behind Rion, almost having to run as he strides purposely down the pavement as if unable or unwilling to look at me."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(I feel like Rion just let me in on a secret...)"

        "B. Let him stew.":
            $menuhideborder = False

            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            mcrion "Actually, I'd rather just go straight back to HQ."
            hide ecmc

            show rion jacket pin basic at right2
            show ecmc jacket_v2 pin sad at left2
            "Rion purses his lips slightly, but gives me a curt nod."
            ri "Fine. I have paperwork to deal with, anyway."
            ri "We can head back."

    scene bg ecm_traincar_on at bg with fade

    "Rion leads me to the train station and we get on the next train."

    stop music
    play music ecmupbeateveryday2
    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin surprised at right3
    mcrion "Couldn't we have used a car? Catching a train during the lunch rush is torture!"

    show rion jacket smirk
    ri "This is faster."
    "Rion turns his head and smirks at me teasingly."
    ri "Besides, it's not that bad."

    show rion jacket smirk
    show ecmc jacket_v2 embarrassed:
        easein 0.4 right1 xoffset 26
    pause 0.4
    "More people get on the train and I shuffle a little closer to Rion, my arm lightly grazing against his."

    show ecmc jacket_v2 smile
    mcrion "Yeah...I guess it really isn't that bad."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "The train takes off again and I'm suddenly aware that my hip is brushing up against Rion's thigh."
    hide ecmc

    show rion jacket pin smirk at left1
    show ecmc jacket_v2 pin blush embarrassed at right1:
        xoffset 26
    "I blush slightly but I stay where I am, enjoying the very light contact."

    hide ecmc
    hide rion
    show rion jacket_cu basic_cu at rion_cu
    "Out of the corner of my eye, I look at Rion. He's staring straight ahead, his mouth in a straight line as if deep in thought."
    hide rion

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Rion's always so hard to read.)"

    show ecmc jacket_v2_cu smile_cu
    "(I don't think he's one for small talk, but there has to be {i}something{/i} I can say to get him to open up!)"
    hide ecmc

    "My eyes wander around the packed train car."

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I could talk about...)"
    hide ecmc

    $menuhideborder = True
    menu rions1e4c3:
        "A. The robot monkey.":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin smile at right1:
                xoffset 26
            mcrion "Oh, look! Someone has a robot monkey!"
            mcrion "I wonder what kind of tasks it does?"

        "B. The advertisement for new holo computers.":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin smile at right1:
                xoffset 26
            mcrion "Did you hear the new HoloBook Pro is coming out soon?"
            mcrion "I wish I could afford the upgrade!"

        "C. The cybershoes.":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin smile at right1:
                xoffset 26
            mcrion "Oh, that kid over there has the new Cybershoe! Apparently this model can train kids to walk much faster."

    show ecmc jacket_v2 basic
    "Rion lets out a grunt in response, his shoulders shrugging slightly."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Hmm...that didn't work.)"
    hide ecmc

    "I look around again until I spot a poster for an upcoming soccer match."

    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin smile at right1:
        xoffset 26
    mcrion "Oh, the game between the D.W.D Invaders and the C.T Cyborgs is this weekend."

    show ecmc jacket_v2 surprised
    mcrion "I don't see the point in watching. Everyone knows the Invaders never win a match!"

    show rion jacket surprised
    "Rion suddenly turns to me, his eyes blazing."
    ri "The Invaders are a strong team. They just need to get it together."
    mcrion "You're an Invaders fan?"

    show rion jacket angry
    ri "They're my favourite team."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Bingo!)"
    hide ecmc

    show rion jacket pin angry at left1
    show ecmc jacket_v2 pin surprised at right1:
        xoffset 26
    mcrion "But they always lose!"

    show rion jacket smile
    ri "That's partly why I like them."

    show ecmc jacket_v2 basic
    "Rion's lips quirk up in a slight smile and he looks over at the poster."
    ri "People always underestimate the underdogs."
    ri "But, I respect a team that keeps doing their best no matter what."

    show ecmc jacket_v2 smile
    mcrion "I guess that makes sense."
    mcrion "Do you watch all their games, then?"
    ri "I haven't missed one in years! I've even taken paid time off to see their games live."

    show rion jacket basic
    show ecmc jacket_v2 sad
    mcrion "Doesn't it get frustrating just seeing them lose time and time again?"
    mcrion "One of the best things about going to live sporting events is the excitement in the crowd!"
    mcrion "I can't imagine it would be the same for a team that always loses."

    show rion jacket smirk
    "Rion chuckles and looks at me in amusement, his eyes crinkling."

    show ecmc jacket_v2 basic
    ri "Well, the excitement to me, [genericfn], is that you really never know."
    ri "Maybe the first time the invaders will win a game is the one I'm watching right at that moment."

    show rion jacket smile
    ri "I'd hate to miss a game only for them to finally have that win."

    show ecmc jacket_v2 smile
    "Rion's eyes light up enthusiastically and I can't hold back my own smile."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(It's nice to see Rion so passionate.)"
    hide ecmc

    "The train begins to come to a stop."

    scene bg ecm_traincar_on at bg with hpunch
    "Just then, a passenger aggressively pushes past me, his elbow harshly knocking into my side."

    stop music
    play music ecmriontheme
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "AH!"
    hide ecmc

    show rion jacket pin basic behind ecmc at centre:
        xoffset -30 transform_anchor True rotate 0
        pause 0.2
        easein_back 0.4 left1plus
        linear 0.2 rotate 2
        parallel:
            easein 0.4 yoffset 100
        parallel:
            linear 0.4 alpha 0.0
    show ecmc jacket_v2 pin surprised at right2:
        transform_anchor True rotate 0
        pause 0.1
        easein_back 0.4 left1
        linear 0.4 rotate 5
        parallel:
            easein 0.4 yoffset 100
        parallel:
            linear 0.4 alpha 0.0
    pause 1.4
    scene bg ecm_traincar_on at bg with hpunch
    "I stumble into Rion, knocking us both off balance."
    "We fall to the ground in a heap."
    "As I steady myself, I realise I can feel my legs between his, as my hands are pressed against his chest."

    show ecmc jacket_v2_cu blush_cu surprised_cu at ecmc_cu
    "(Oh my bot! I'm right on top of him!)"
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

