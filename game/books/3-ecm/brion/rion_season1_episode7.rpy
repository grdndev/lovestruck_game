label rion_season1_episode7:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_office_hq_on at bg with fade
    play music ecmtense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show gael uniform_cu angry_cu glasses_cu at gael_cu
    ga "Rion, I need you to give me access to all your evidence related to this case."
    hide gael

    show rion black pin angry at centre
    "Beside me Rion stiffens, clearly thrown off-guard by the FDI's sudden appearance."
    ri "Right now?"

    show rion black pin angry at left3
    show gael uniform glasses angry at right3
    ga "Yes. Before the FDI can continue the investigation, I need to make a full evaluation of everything you've got."
    "Rion lets out a frustrated huff and crosses his arms over his chest."
    ri "Oh, come on, Gael. You know I can't just drop everything I'm working on. We're losing time here."
    ga "Sorry, Rion, but I can't wait."
    ga "I'm going to be doing the work at D.I.V.A.A. until all everything is fully catalogued and transferred to the FDI HQ."
    "Rion's shoulders lift slightly, the tension practically rolling off him in waves."

    hide rion
    hide gael
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Rion definitely seems upset.)"
    "(It must be frustrating when he's finally getting close to catching the guy, and now there's a huge delay!)"
    hide ecmc

    show rion black pin angry at left3
    show gael uniform glasses angry at right3
    ri "Gael, Once you start your investigation, everything's going to come to a halt."
    ga "I get it, Rion, but my hands are tied."

    show rion black basic
    show gael uniform sad
    ga "But hey, we've done this enough times now. You make this easy on me, and I'll compromise with you."

    hide rion
    hide gael
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(If Gael wasn't here to take over the case, she might actually be cool.)"
    hide ecmc

    show rion black pin sad at left3
    show gael uniform glasses basic at right3
    ri "Why don't you at least let [genericfn] and I analyze the latest data we collected?"

    hide rion
    hide gael
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(He must be talking about Skye's buyer data.)"
    hide ecmc

    $menuhideborder = True
    menu rions1e7c1:
        "A. Back Rion up.":
            $menuhideborder = False

            show ecmc jacket_v2 pin surprised at left3
            show gael uniform glasses basic at right3
            mcrion "The latest evidence has a lot of background context."

            show ecmc jacket_v2 determined
            mcrion "It won't make a lot of sense on its own, so I think it's better that Rion and I go over it first."

            show ecmc jacket_v2 sad
            show gael uniform sad
            ga "If I have any questions, I'll just ask you directly."

        "B. Suggest you and Rion get one more day.":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left3
            show gael uniform glasses basic at right3
            mcrion "Or maybe we could get one more day just to get everything together?"
            mcrion "It will be much easier for you to go through the evidence if it's properly organized."
            show gael uniform sad
            ga "I'm sure I can manage."

        "C. Try and calm Rion down.":
            $menuhideborder = False
            show rion black pin sad at left3
            show ecmc jacket_v2 pin sad at right3
            mcrion "Rion, as long as the evidence is still here at D.I.V.A.A., I'm sure we'll be able to look at it."
            ri "It's not the same!"

    hide ecmc
    show rion black pin sad at left3
    show gael uniform glasses sad at right3
    ga "I'm sorry, Rion, but this isn't up to me."
    ga "I'm on strict FDI orders so this needs to all be done by the book as much as possible."

    show rion black angry
    ri "Okay, so you have to take everything right away."
    ri "And that'll take days, so if some new evidence happens to pop up at the tail end of your time here, no one would notice, right?"

    show rion black basic
    "Gael hesitates for a moment, then gives Rion a brief nod."
    ga "You have a point."
    "Gael looks around then lowers her voice a fraction."
    ga "Rion, as long as you don't cause any problems and report any findings to me as soon as possible, I won't be watching too closely."
    "Rion nods in understanding."

    show rion black smile
    ri "Thanks, Gael."

    show gael uniform smile
    ga "We'll figure this case out, Rion. I promise."

    stop music
    play music ecmcalmeveryday2
    show gael uniform smile at out_right
    pause 0.4
    show rion black basic at left3:
        pause 0.2
        easein_back 0.4 left1
    show ecmc jacket_v2 pin basic at right1, right_in
    pause 0.4
    "Gael walks away and Rion takes my arm and gently pulls me aside."
    hide gael

    show ecmc jacket_v2 blush embarrassed
    "My arm burns slightly at the contact, and even after Rion drops his hand, I can still feel his lingering touch."

    show rion black surprised
    show ecmc jacket_v2 basic -blush
    ri "Well, that's something at least."

    show ecmc jacket_v2 surprised
    mcrion "What's the plan?"

    hide ecmc
    hide rion
    show rion black_cu basic_cu at rion_cu
    "Rion turns to face me, then looks at me with determination."

    show rion black_cu smirk_cu
    ri "If we can't access what we've got, then we'll just have to look for more."
    "Rion smirks at me and crosses his arms over his chest."

    show rion black_cu smile_cu
    ri "I hope you're ready to see more of that cybernetic art, because we're going to crash Blythe's show!"

    scene bg ecm_artgallery_night_lights at bg with fade
    stop music
    play music ecmromantic1

    "Later that night, Rion and I get to the art gallery to find the show in full swing."

    show rion jacket pin smirk at left1plus
    show ecmc jacket_v1 pin headset embarrassed at right1plus
    ri "Are you ready, [genericfn]?"
    "I turn to look at Rion and bite my lip, nervously."

    show ecmc jacket_v1 surprised
    mcrion "I'm a little nervous. This is my first time going on a live investigation with a bunch of people!"

    show ecmc jacket_v1 embarrassed
    "I look down at my D.I.V.A.A. uniform and blush slightly."
    mcrion "Plus, I feel a little out of place in uniform while everyone else is so dressed up."

    show rion jacket smile
    ri "Don't worry about that, [genericfn]. At least we stick out together."

    show ecmc jacket_v1 basic
    "Rion grins at me, reassuringly, then looks around the room."
    ri "This is the perfect opportunity to scope out Blythe's clientele. We just need to schmooze with some art snobs."

    show rion jacket smirk at left1plus:
        pause 0.1
        easein_back 0.4 left1
    show ecmc jacket_v1 embarrassed at right1plus:
        pause 0.3
        easein_back 0.4 right1
    pause 0.4
    "Rion takes my hand, sending a reassuring spark shooting through me, and leads me over to a nearby display."

    hide rion
    hide ecmc
    "Inside a glass cabinet is a 3D painting with mechanical components threaded through it that slowly rotate, causing the image to move and twist."

    show rion jacket pin surprised at left1
    show ecmc jacket_v1 pin headset basic at right1
    ri "I don't get it. Why would you waste expensive tech like this?"

    show ecmc jacket_v1 surprised
    mcrion "I think it's kind of cool. I mean, I've always found technology fascinating, but it's interesting to see this take on cybernetics."

    show rion jacket basic
    show ecmc jacket_v1 basic
    "Rion shrugs and I can tell he's not all that impressed just as a hostess walks past, a tray of canapes in her hand."

    hide rion
    hide ecmc
    hostess "Welcome to the show, Sir. Can I offer you or your girlfriend something to eat?"

    show ecmc jacket_v1_cu headset_cu blush_cu surprised_cu at ecmc_cu
    "(Girlfriend?!)"
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    "My face heats at the thought and I sneak a glance at Rion who seems completely calm."
    hide rion

    show rion jacket smile at left1
    show ecmc jacket_v1 pin headset surprised at right1
    ri "No, I'm fine thank you."
    ri "[genericfn], would you like something?"

    show ecmc jacket_v1 basic
    "I shake my head, and the waitress walks off."

    hide rion
    hide ecmc
    show ecmc jacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
    "(Why didn't Rion correct her?)"
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    "I sneak another glance at Rion who's looking around the room and my heart does a little flip."
    hide rion

    show ecmc jacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
    "(Did it mean something? Or was that just his cover story?)"
    hide ecmc

    show rion jacket pin basic at left1
    show ecmc jacket_v1 pin headset basic at right1
    ri "We should start talking to some patrons and see what we can find out."
    hide rion
    hide ecmc

    stop music
    play music ecmcalmeveryday3
    show anton casual basic at left1plus, step_in
    show korin casual pin basic at right2, step_in
    "Just then, I see Korin and Anton making their way through the crowd."

    show korin casual smile
    ko "Oh, Rion! [genericfn]! Fancy seeing you both here!"

    show korin casual sad
    ko "I heard Gael took over the case, so I figured you'd be busy."

    hide anton
    hide korin
    show rion jacket pin basic at left2
    show ecmc jacket_v1 pin headset basic at right1plus
    ri "We're just following up on something. What are you two doing here?"

    hide rion
    hide ecmc
    show anton casual basic at left1plus
    show korin casual pin smile at right2
    ko "Oh, we just came to enjoy the show!"

    show anton casual angry
    "Korin beams at us while Anton screws up his face as if he smells something bad."

    show korin casual basic
    an "Rion, I really wouldn't have thought that this was your scene."
    an "You'd both better not make D.I.V.A.A. look bad in front of important people!"

    hide anton
    hide korin
    show rion jacket pin angry at left2
    show ecmc jacket_v1 pin headset basic at right1
    ri "If anyone's going to make D.I.V.A.A. look bad, Anton, it will be you."
    ri "Both [genericfn] and I are professionals and [genericfn] can talk tech with the best of them."

    hide rion
    hide ecmc
    show anton casual_cu angry_cu at anton_cu
    "Anton scowls as I look at Rion, my heart fluttering slightly."
    hide anton

    show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
    "(I really hope I don't let Rion down tonight!)"
    hide ecmc

    show rion jacket pin smirk at left2
    show ecmc jacket_v1 pin headset basic at right1
    ri "Now if you'll both excuse us, [genericfn] and I have work to do!"

    show rion jacket smirk at out_right
    pause 0.2
    show ecmc jacket_v1 basic at out_right
    stop music
    play music ecmcalmeveryday2
    "Rion lightly grasps my arm and leads me away from Korin and Anton, his touch through my clothes still causing goosebumps to prick on my skin."

    hide ecmc
    hide rion
    show rion jacket_cu sad_cu at rion_cu
    "I turn my head slightly and notice that Rion's standing quite rigid, his muscles tense."
    hide rion

    show ecmc jacket_v1_cu headset_cu sad_cu at ecmc_cu
    "(I really don't think this is Rion's scene.)"
    hide ecmc

    show rion jacket pin smile at right1
    show ecmc jacket_v1 pin headset basic at left1
    ri "Come on. Let's go talk to a few people and find out what they know."

    hide rion
    hide ecmc
    "Rion sticks closely by my side as we speak to different groups of people, but we don't find out anything interesting."
    "Eventually, Rion leads me away from the crowd and over to the snack table."

    show rion jacket pin sad at right1
    show ecmc jacket_v1 pin headset sad at left1
    ri "Time for a break, I hope the food's good at least."

    show rion jacket basic
    show ecmc jacket_v1 surprised
    mcrion "Oh, they have mini pizzas!"

    show rion jacket smile
    show ecmc jacket_v1 smile
    ri "They look great."

    show rion jacket sad
    show ecmc jacket_v1 basic
    "Rion eyes the rest of the table and wrinkles his nose in disgust."
    ri "I definitely won't be touching that caviar. You'd think price and flavour would increase hand in hand."

    show ecmc jacket_v1 sad
    mcrion "Yeah, I'll take a pass."

    hide rion
    hide ecmc
    "I help myself to a mini pizza as another patron walks over and looks down at the table of food."
    snobbyrichm "Well, this is all rather disappointing."
    snobbyrichm "It's definitely not as elaborate as the spread at the gallery opening I went to last week."

    stop music
    play music ecmemotional2
    show rion jacket pin basic at right1
    show ecmc jacket_v1 pin headset sad at left1
    "I sneak a glance at Rion, who's purposely ignoring the man as he pops a mini pizza into his mouth."

    hide rion
    hide ecmc
    "The man turns to look at Rion, as if looking for someone to agree with him, then he lets out a gasp."
    snobbyrichm "Your eye! I've never seen anything quite like it before."
    snobbyrichm "It's a work of art!"

    stop music
    play music ecmemotional1
    show rion jacket_cu basic_cu at rion_cu
    "Rion starts to tweak his eye as the man waves more patrons over."
    hide rion

    snobbyrichm "Portia, you have to see this guy's eye!"
    wealthyh "Oh, how stunning! It's so chic!"
    wealthyh "Where did you get a hold of a model this advanced?"

    show rion jacket_cu sad_cu at rion_cu
    "Rion shrugs casually, but he tweaks his eye even harder in response."
    hide rion

    show rion jacket pin sad at right1
    show ecmc jacket_v1 pin headset sad at left1
    ri "I have a few contacts that pulled some strings."

    show ecmc jacket_v1 smile
    "Rion looks directly at me as he speaks and I smile back at him reassuringly."

    hide rion
    hide ecmc
    show ecmc jacket_v1_cu headset_cu sad_cu at ecmc_cu
    "(I think Rion's purposely avoiding everyone else's gaze.)"
    hide ecmc

    "As the other patrons continue to question Rion about his eye, I glance down at my ARCware and notice a faint signal on the monitor."

    show ecmc jacket_v1_cu headset_cu determined_cu at ecmc_cu
    "(Hmm...that's odd. I should tell Rion about that as soon as we're alone.)"
    hide ecmc

    "Patrons trickle over to gawk at Rion's eye, and his shoulders tense more and more."

    show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
    "(They're treating Rion like {i}he's{/i} the art exhibit!)"
    hide ecmc

    show rion jacket pin angry at centre
    "I watch as an older lady covered in diamonds gets right into Rion's face. He recoils slightly."
    eccolderl "It's certainly a fascinating piece of technology! Can you take it out so we can take a better look?"

    hide rion
    show rion jacket_cu sad_cu at rion_cu
    "Rion looks over at me very intently."

    stop music
    play music ecmcalmeveryday4
    show rion jacket_cu smile_cu
    ri "Hey, [genericfn], I just noticed an interactive art exhibit across the room."
    hide rion

    show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
    "Rion locks his gaze with mine and I can tell he'd really like to get away from the patrons."
    hide ecmc

    show rion jacket_cu smile_cu at rion_cu
    ri "It looks like it deals with mood visualisation or something."
    hide rion

    "I look over and see the exhibit he's referring to, and it's completely free of people."

    show ecmc jacket_v1_cu headset_cu smile_cu at ecmc_cu
    "(I'm sure Rion could use some breathing room!)"

    show ecmc jacket_v1_cu embarrassed_cu
    "(The exhibit sounds interesting...and I think it would be a good chance to get some time alone with Rion.)"
    hide ecmc

    show rion jacket_cu smile_cu at rion_cu
    ri "Let's check it out."
    hide rion

    $menuhideborder = True
    menu rions1e7c2:
        "A. Escape the crowd with Rion." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show rion jacket pin smirk at right1
            show ecmc jacket_v1 pin headset smile at left1
            mcrion "Sure! Let's go."

            stop music
            play music ecmromantic1
            show rion jacket smirk at step_out
            pause 0.2
            show ecmc jacket_v1 smile at step_out
            "Rion takes my hand and pulls me away from the crowd that's now arguing about the benefits of prosthetics."

            hide rion
            hide ecmc
            show rion jacket pin sad at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            ri "Finally. I thought I'd never get away from that mob."

            show rion jacket smile
            ri "Glad you came with. Always a good idea to stick with your team when on a mission."

            show ecmc jacket_v1 smile
            "Rion turns his head to smile at me and I beam back, my heart fluttering slightly."

            hide rion
            hide ecmc
            show ecmc jacket_v1_cu headset_cu smile_cu at ecmc_cu
            "(Hearing Rion say that makes me feel as if he sees me more as an equal and not just the rookie he has to train.)"
            hide ecmc

            "I follow Rion over to the art exhibit."
            happystaff "Hi there! Welcome to the exhibition."

            show rion jacket pin smile at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            ri "What exactly does this do?"

            hide rion
            hide ecmc
            happystaff "This is an interactive display which uses the power of cybernetics to bring people together."
            happystaff "These headpieces will transmit your thoughts and feelings to a digital board which will turn them into patterns, shapes, and colours."

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset surprised at right1plus
            mcrion "So, it's like a giant mood ring that makes digital paintings?"

            hide rion
            hide ecmc
            happystaff "I guess you could say that! But it's a lot more advanced."

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            "Rion turns to me with a smirk."

            show rion jacket smile
            ri "I'm game if you are."

            show ecmc jacket_v1 smile
            mcrion "Let's do it."

            hide rion
            hide ecmc
            "The staff member leads Rion and I over to a booth and gets us to sit facing each other, so close that our knees touch."

            show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
            "(I wonder how this display will work. Rion can't hide his thoughts and feelings from the display, right?)"
            hide ecmc

            happystaff "Alright, so I'm going to start off with some basic questions to calibrate the device."
            happystaff "Do you prefer sweet or savoury food?"

            show rion jacket pin smile at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            ri "Definitely savoury."

            show ecmc jacket_v1 determined
            mcrion "Hmm...sweet."

            hide rion
            hide ecmc
            "I watch as the canvas behind Rion and I starts to form a simple pattern."
            happystaff "Straight forward answers give straight forward results!"
            happystaff "Let's try something else. What's your favourite hobby?"

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset smile at right1plus
            mcrion "Scrapping. I love finding retro tech!"

            hide rion
            hide ecmc
            "The canvas explodes in excited color, but the pattern is still quite simple."

            show rion jacket pin smile at left1plus
            show ecmc jacket_v1 pin headset smile at right1plus
            ri "Soccer."

            hide rion
            hide ecmc
            happystaff "Alright, time to kick things up a fraction."
            happystaff "What physically attracts you most to a person?"

            hide rion
            hide ecmc
            show ecmc jacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
            "I immediately blush and do my best to avoid Rion's gaze, even though he's sitting right in front of me."
            "(I don't want to make it obvious that I'm attracted to Rion, but at the same time, I don't want to lie and make it sound like he's not my type!)"
            hide ecmc

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            "Across from me, Rion looks completely calm, his face scrunched up a little in thought."

            show rion jacket smile
            ri "Eyes. Eyes can tell you a lot about a person."

            hide rion
            hide ecmc
            "Behind us, interesting patterns start to emerge on the canvas."

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset smile at right1plus
            mcrion "I guess I'd say the same thing. Eyes are very unique."

            hide rion
            hide ecmc
            show ecmc jacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
            "I peek at Rion's cyber eye and quickly glance away as my face heats."
            hide ecmc

            show rion jacket_cu  smirk_cu at rion_cu
            "Out of the corner of my eye, I notice Rion smirking."
            hide rion

            happystaff "Alright, what personality traits attract you to a person?"

            show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
            "(I like someone courageous, a little daring and also caring, but then I'd be describing Rion!)"
            hide ecmc

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset embarrassed at right1plus
            "I shift awkwardly as Rion meets my gaze."

            hide rion
            hide ecmc
            show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
            "(Oh my bot! I hope he doesn't realize I'm thinking about him.)"
            hide ecmc

            show rion jacket pin smile at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            ri "Confidence, and people who aren't afraid to be themselves. Genuine people."

            hide rion
            hide ecmc
            "Again, the canvas explodes into patterns I can't discern."

            show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
            "(Do they have a guide to what this all means or something?)"
            hide ecmc

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset smile at right1plus
            mcrion "I guess I like people who are strong, but not afraid to show a sensitive side."

            hide rion
            hide ecmc
            "The canvas continues to fill with color, but I stare at the patterns caused by Rion's responses."

            show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
            "(When I talk the canvas practically explodes, but when Rion responds everything's...restricted.)"

            show ecmc jacket_v1_cu embarrassed_cu
            "(Is he purposely holding back? Maybe I'm reading too much into this?)"
            hide ecmc

            "Before I can ponder any more, the staff member removes the device from my head."
            happystaff "Time's up! There are other guests waiting."
            happystaff "But if you'd like to keep your painting, you can purchase it later tonight."

            show rion jacket pin basic at left1plus, step_in
            pause 0.2
            show ecmc jacket_v1 pin headset embarrassed at right1plus, step_in
            "I follow Rion out of the exhibit, still feeling a bit confused."

            hide rion
            hide ecmc
            show ecmc jacket_v1_cu headset_cu embarrassed_cu at ecmc_cu
            "(I wish I knew what those patterns meant! Maybe it's all nonsense?)"
            hide ecmc

            show rion jacket pin basic at left1plus
            show ecmc jacket_v1 pin headset basic at right1plus
            "Rion turns to face me, disrupting my thoughts."

            show rion jacket smile
            ri "Right, that was an interesting break, but we have to get back to work."
            ri "Let's go talk to some more people."

        "B. Focus on the people.":
            $menuhideborder = False

            show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
            "Some more people walk over and I lose my train of thought as they start firing even more questions at Rion."
            hide ecmc

            show rion jacket pin sad at centre
            "Rion shuffles awkwardly as the crowd presses in."
            ri "Well, this has been interesting, but I have to go meet someone. Excuse me."

            show rion jacket sad at step_out
            "Rion extracts himself from the crowd and briskly walks away."
            hide rion

            show ecmc jacket_v1_cu headset_cu sad_cu at ecmc_cu
            "(Where did he go?! I guess I'll have to catch up with him later.)"
            "(Rion likely just wanted some time to himself.)"

    hide rion
    hide ecmc
    "After milling around the gallery for a bit longer, I lead Rion over to a quiet corner of the gallery."

    stop music
    play music ecmupbeateveryday2
    show rion jacket pin basic at left2
    show ecmc jacket_v1 pin headset surprised at right1
    mcrion "Rion, I have something I need to tell you."
    mcrion "Earlier on, when that mob was looking at your eye, I picked up a strange signal on my ARCware."

    show ecmc jacket_v1 sad
    mcrion "It was really faint, so I couldn't make anything of it."

    show rion jacket surprised
    ri "Is it still coming up?"
    mcrion "Yes, but it's been fading in and out all night."

    show rion jacket basic
    show ecmc jacket_v1 basic
    ri "Hmm...let's go talk to some more guests and analyze it. Maybe we'll get a stronger signal if we talk to the right people."

    hide rion
    hide ecmc
    show blythe casual angry at centre, step_in
    pause 0.2
    "Rion and I start to approach a new group of patrons when Blythe approaches us, her eyes blazing."
    bh "Well, fancy seeing you two here."
    bh "I'd say I'm happy to see you, but we'd all know that's a lie."
    hide blythe

    show rion jacket pin basic at left2
    show ecmc jacket_v1 pin headset basic at right1
    ri "Don't worry about us, Blythe. We're just here to enjoy the show."

    hide rion
    hide ecmc
    show blythe casual angry at centre
    bh "In your uniforms? I'm not stupid."
    bh "You'd better not be disrupting my guests!"

    hide blythe
    show ecmc jacket_v1_cu headset_cu determined_cu at ecmc_cu
    "(I need to give Rion a chance to investigate the signal.)"
    hide ecmc

    $menuhideborder = True
    menu rions1e7c3:
        "A. Mention the cables used in a painting.":
            $menuhideborder = False
            show ecmc jacket_v1 pin headset smile at left2
            show blythe casual basic at right2
            mcrion "Blythe, I happened to notice that this painting uses X2D cables."
            mcrion "Those are extremely rare. How did the artist source them?"
            show blythe casual smile
            bh "Many of our artists have high quality connections around the globe."

        "B. Discuss the computer hardware in a sculpture.":
            $menuhideborder = False
            show ecmc jacket_v1 pin headset smile at left2
            show blythe casual basic at right2
            mcrion "Blythe, I love the use of the old Interzone 3K2 hard drive in this futuristic sculpture!"
            mcrion "It seems like the perfect mix of a now obsolete technology with something more future focused."
            show blythe casual smile
            bh "That's exactly what the artist was going for."

        "C. Comment on the robotic parts used in a portrait.":
            $menuhideborder = False
            show ecmc jacket_v1 pin headset smile at left2
            show blythe casual basic at right2
            mcrion "The use of R4B robot pieces in this portrait is really interesting."
            mcrion "The portrait on its own seems quite old, but the robotic components give it a futuristic vibe."

    show ecmc jacket_v1 smile
    show blythe casual smile
    "Blythe turns to me, a huge smile suddenly on her face."

    hide ecmc
    hide blythe
    show rion jacket pin basic at centre
    pause 0.2
    show rion jacket basic at step_out
    "Rion sneaks away."
    hide rion

    show ecmc jacket_v1_cu headset_cu smile_cu at ecmc_cu
    "(Hopefully Rion can track that signal down.)"

    show ecmc jacket_v1_cu determined_cu
    "(I need to keep Blythe talking so she doesn't chase after him to complain.)"
    hide ecmc

    show ecmc jacket_v1 pin headset smile at left2
    show blythe casual smile at right2
    mcrion "I think it's {i}so{/i} interesting how the artist has combined AI and cybernetics with more traditional art."
    bh "Precisely! Their blend of mediums is...inspired."
    "Blythe looks at me, curiously."

    show ecmc jacket_v1 basic
    bh "I'm grateful that {i}some{/i} D.I.V.A.A. agents like Anton share my views. You seem to be among them."

    hide blythe
    hide ecmc
    show ecmc jacket_v1_cu headset_cu surprised_cu at ecmc_cu
    "(Anton?! I didn't realize Blythe knew him so well.)"
    hide ecmc

    show blythe casual basic at right3
    show ecmc jacket_v1 pin headset basic at left4
    show rion jacket pin basic behind ecmc at left1plus, step_in
    "Just then, Rion rushes back over."

    show rion jacket sad
    ri "Blythe, I'm sorry to interrupt, but I have a D.I.V.A.A. issue I need to speak to [genericfn] about."

    show blythe casual angry at out_right
    pause 0.2
    "Blythe harumphs and walks briskly away as Rion leads me to the side of the room."
    hide blythe

    hide rion
    hide ecmc
    show ecmc jacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
    "I shiver at the contact, instinctively leaning into Rion as we walk away."
    hide ecmc

    show rion jacket pin smile at right1
    show ecmc jacket_v1 pin headset basic at left1
    ri "Good running interference, Hatchling. Must've been tedious."

    stop music
    play music ecmromantic3
    show ecmc jacket_v1 smile
    mcrion "It wasn't so bad, but I'm glad you came back when you did!"

    hide rion
    hide ecmc
    "After making sure no one's listening in, Rion and I huddle up in a corner."

    show rion jacket pin basic at right1
    show ecmc jacket_v1 pin headset basic at left1
    ri "Alright, I was able to pick up the signal. It's emitting from a few different ARCware headsets."

    show ecmc jacket_v1 surprised
    mcrion "A few? Do you...do you think that people are being electronically tagged?"

    stop music
    play music ecmtense2
    show rion jacket sad
    "Rion looks at me, his mouth set into a grim line."
    ri "That's what I'm thinking. I have a suspicion that the killer is tagging potential victims at this event, so somebody here could be next."

    hide rion
    hide ecmc
    play sound "<from 1.5 to 3>audio/sfx/phone_ringing.mp3"
    "Before I can say anything, Rion's holophone starts ringing. He pulls it out and groans."

    show rion jacket pin sad at right1
    show ecmc jacket_v1 pin headset basic at left1
    ri "Yes, Gael?"

    show rion jacket angry
    show ecmc jacket_v1 surprised
    ga "Rion, you and [genericfn] need to get back to D.I.V.A.A. HQ right away."
    ga "There's a major problem!"
    hide rion
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

