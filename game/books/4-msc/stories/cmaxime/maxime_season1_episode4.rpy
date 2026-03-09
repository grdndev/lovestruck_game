label maxime_season1_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg
    play music mscsurfshop

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc casual_hairup basic at left2
    show trina casual basic at right2
    "The next morning, Trina asks for my help shifting our couch from the back of the office to the sidewalk."

    show mscmc casual_hairup basic:
        ease 0.5 xoffset 50
    show trina casual basic:
        ease 0.5 xoffset 50
    "We carefully angle the couch through the Surf Shack, avoiding the racks of sunglasses and shirts."
    hide trina
    hide mscmc
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(I'm still thinking about Maxime's suspicions about who kidnapped that surfer...)"
    "(He was quieter than usual when he walked me home last night.)"
    show mscmc casual_hairup sad:
        xpos stagepos[1]-130
    show trina casual basic:
        xpos stagepos[1]+230
    "Even while I worry about our local mystery, Trina has eyes only for the couch."
    show trina casual smile
    so "Goodbye, ancient brown couch I got free on ELyst. And hello soon to my beautiful new couch, with pleating."
    "She sighs happily, picturing the couch she ordered online a few weeks ago."
    show mscmc casual_hairup smile
    mcmax "Now this couch can be someone else's free deal."
    so "How's the competition? I know you felt conflicted after that guy, Raymond, went AWOL."
    show mscmc casual_hairup basic
    mcmax "It's weird that he hasn't contacted his team. I'm going to give the tournament my all, now that I have a spot."
    mcmax "I did the math, and if I score high enough in this tournament, I'll qualify for the Wave Riders Tournament in August."
    so "Then you've hit the big leagues—you could even join the World Surf League!"
    show mscmc casual_hairup smile:
        ease 0.5 xpos stagepos[1]-80
    show trina casual smile:
        ease 0.5 xpos stagepos[1]+280
    "Trina grins as we start to work the sofa through the doorway, pickup up my excitement."
    mcmax "That's the plan! But I have to make the most of this tournament, because there won't be anything at this level again for months."
    show trina casual basic
    mcmax "It's my only chance to get the kinds of scores I need."
    show mscmc casual_hairup angry
    "I furrow my brow, mentally running through the scores I'll need to make the podium, while still sweating under the weight of the couch."
    show trina casual smile
    "Trina laughs at my seriousness."
    so "[genericfn], I know you, and I know you've probably crunched those numbers fifty times by now."
    so "You've got this—don't second guess yourself!"
    show mscmc casual_hairup surprised
    so "Anyway, tell me more about that organizer guy, Wikus. What's he like?"
    so "He looks like a total dweeb, but I hear he's pretty loaded..."
    hide trina
    hide mscmc
    show mscmc casual_hairup_cu angry_cu at mscmc_cu
    "(A rich, dweeby, possibly evil scientist.)"

    hide mscmc
    $menuhideborder = True
    menu maximee04c1:
        "A. Downplay the issue.":
            $menuhideborder = False
            show mscmc casual_hairup basic:
                xpos stagepos[1]-80
            show trina casual smile:
                xpos stagepos[1]+280
            "I shrug, hoping to change the subject quickly."
            hide trina
            show mscmc casual_hairup_cu angry_cu at mscmc_cu
            "(If Wikus is as dangerous as Maxime says he is, I don't want Trina anywhere near him.)"
            show mscmc casual_hairup basic:
                xpos stagepos[1]-80
            show trina casual smile:
                xpos stagepos[1]+280
            mcmax "As a tournament organizer, he's fine I guess."
        "B. Admit he's a little creepy.":
            $menuhideborder = False
            show mscmc casual_hairup sleep:
                xpos stagepos[1]-80
            show trina casual smile:
                xpos stagepos[1]+280
            mcmax "He's a little...what's a nice way to put this..."
            show mscmc casual_hairup basic
            show trina casual basic
            so "Socially awkward?"
            show trina casual sad
            mcmax "That, but worse. He's not nice and shy like Maxime—he'll really get in your face if he wants something."
        "C. It's his tournament that I need.":
            $menuhideborder = False
            show mscmc casual_hairup basic:
                xpos stagepos[1]-80
            show trina casual smile:
                xpos stagepos[1]+280
            mcmax "He's just a guy hosting a tournament. I don't have to particularly like him—it's business. You know what I mean?"
            hide trina
            show mscmc casual_hairup_cu sad_cu at mscmc_cu
            "(Hopefully. I don't want anyone in the tournament to get hurt.)"
            show mscmc casual_hairup angry:
                xpos stagepos[1]-80
            show trina casual basic:
                xpos stagepos[1]+280
            so "I suppose. I guess entrepreneur types like him have that 'cult of personality' thing going."

    show mscmc casual_hairup basic
    show trina casual smile
    so "Alright, enough about Weird Wikus—how's your {i}amazing{/i} trainer Maxime?"
    "Trina waggles her eyebrows at me."
    show mscmc casual_hairup surprised:
        ease 0.5 yoffset 30
        ease 0.5 yoffset 0
    "I nearly drop my end of the couch into the conch shell display, but hastily recover."
    so "Yeesh! All I asked was how he's doing. You've got it bad."
    hide trina
    hide mscmc
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Why must she be so perceptive...)"
    show mscmc casual_hairup smile:
        xpos stagepos[1]-80
    show trina casual smile:
        xpos stagepos[1]+280
    mcmax "It's a good, healthy, professional relationship. We're having a great time."
    so "Have you guys kissed yet?"
    show mscmc casual_hairup surprised
    mcmax "What?!"
    show mscmc casual_hairup surprised:
        ease 0.5 xoffset -100
    "This time, my end of the couch slips throught my fingers, and lands on my toe."
    show mscmc casual_hairup angry
    show trina casual sleep
    mcmax "Ow ow ow!"
    show trina casual smile
    show mscmc casual_hairup angry at hop
    "I wince and start hopping around."
    show mscmc casual_hairup surprised
    "I can hear Trina wheezing on the other side, trying to cover her laughter with her hand."
    show mscmc casual_hairup sleep
    so "Dude. [genericfn]."
    show mscmc casual_hairup angry
    "I glare at her, shaking my aching toe out."
    mcmax "It's your fault for asking me that!"
    show mscmc casual_hairup surprised
    mcmax "And the answer is no. I told you, it's a strictly trainer-trainee relationship!"
    show mscmc casual_hairup embarrassed
    "Trina scoffs, blowing a strand of hair out of her face."
    so "Sure, sure, you're not emotionally involved what-so-ever."
    show trina casual basic
    so "But just so it's on record, if you guys ever break up, you both still have to work at the shop."
    show mscmc casual_hairup surprised
    show trina casual smile
    so "No way am I losing either of my best teachers to nonsense of the heart."
    mcmax "{i}Trina!{/i}"
    show trina casual smile at out_right
    "Trina giggles, stepping over the threshold and finally lifting the couch onto the sidewalk."

    scene bg msc_ocean_wide_day at bg with clockwise_wipe
    play music mscsurftraining
    play sound big_splash
    
    show surfboard_acc_back behind mscmc:
        zoom 0.85
        xpos -115
        ypos 320
    show mscmc surfer_hairup basic at left4:
        pause 0.2
        block:
            parallel:
                ease 1 zoom 0.95
            parallel:
                ease 1 yoffset 25
            parallel:
                ease 1 xoffset 25
        block:
            parallel:
                ease 1 zoom 1
            parallel:
                ease 1 yoffset 0
            parallel:
                ease 1 xoffset 0
        block:
            parallel:
                ease 0.9 zoom 0.95
            parallel:
                ease 0.9 yoffset 25
            parallel:
                ease 0.9 xoffset 25    
        block:
            parallel:
                ease 0.9 zoom 1
            parallel:
                ease 0.9 yoffset 0
            parallel:
                ease 0.9 xoffset 0
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.85
        xpos 415
        ypos 278
    show maxime shorts basic at right4:
        pause 0.2
        block:
            parallel:
                ease 0.9 zoom 0.95
            parallel:
                ease 0.9 yoffset 25
            parallel:
                ease 0.9 xoffset 25
        block:
            parallel:
                ease 0.9 zoom 1
            parallel:
                ease 0.9 yoffset 0
            parallel:
                ease 0.9 xoffset 0
        block:
            parallel:
                ease 1 zoom 0.95
            parallel:
                ease 1 yoffset 25  
            parallel:
                ease 1 xoffset 25
        block:
            parallel:
                ease 1 zoom 1
            parallel:
                ease 1 yoffset 0
            parallel:
                ease 1 xoffset 0
    "I meet up with Maxime later that day for endurance training, basically just paddling along the shore for a couple of miles."
    show mscmc surfer_hairup smile
    mcmax "I assume we need to get to the bottom of the missing surfer—which sounds like the title of one of those teen detective books."
    show maxime shorts smile
    "Maxime chuckles, his broad arms cutting easy strokes through the water."
    mx "It does sound theatrical, doesn't it? I hope it has a happy ending, like a teen detective mystery."
    show maxime shorts smirk
    mx "What do you think, [genericfn]? What should we do next?"
    show mscmc surfer_hairup grin
    "I flush excitedly, delighted to be asked for input on the spy stuff."
    mcmax "Well...We know Wikus' office is above the tournament hall. We could break in and look for clues!"
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    hide maxime
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Just like in a mystery novel.)"
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.85
        xpos 415
        ypos 278
    show maxime shorts smile at right4
    show surfboard_acc_back behind mscmc:
        zoom 0.85
        xpos -115
        ypos 320
    show mscmc surfer_hairup grin at left4
    "Maxime smiles proudly, and my heart feels warm and full."
    show maxime shorts smirk
    mx "It's a good idea. Even if I can't find out what happened to Raymond, I'm sure I'll find something."
    show mscmc surfer_hairup smile
    show maxime shorts basic
    mx "I'll do this alone though, [genericfn]. It'll be risky—and illegal."
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    hide maxime
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(But potentially thrilling.)"
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.85
        xpos 415
        ypos 278
    show maxime shorts smile at right4
    show surfboard_acc_back behind mscmc:
        zoom 0.85
        xpos -115
        ypos 320
    show mscmc surfer_hairup grin at left4
    mcmax "Oh come on, I'll be fine if I'm with you! I want to be part of the dance."
    "Maxime is amused, but unyielding."
    show maxime shorts basic
    mx "It's not a dance, it's breaking into private property, and possibly stealing any evidence found. I don't dance."
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Wait, really?)"

    hide mscmc
    $menuhideborder = True
    menu maximee04c2:
        "A. You don't dance?":
            $menuhideborder = False
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.85
                xpos 415
                ypos 278
            show maxime shorts basic at right4
            show surfboard_acc_back behind mscmc:
                zoom 0.85
                xpos -115
                ypos 320
            show mscmc surfer_hairup surprised at left4
            mcmax "Really? You don't dance?"
            show maxime shorts surprised
            mx "Is that such a surprise?"
            show mscmc surfer_hairup smile
            show maxime shorts embarrassed
            mcmax "Well, I don't see you performing with a dance troupe, but you're athletic and artistic. I bet you'd be pretty good if you tried."
            show mscmc surfer_hairup grin
            "Maxime clears his throat, embarrassed."
        "B. That's too bad.":
            $menuhideborder = False
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.85
                xpos 415
                ypos 278
            show maxime shorts basic at right4
            show surfboard_acc_back behind mscmc:
                zoom 0.85
                xpos -115
                ypos 320
            show mscmc surfer_hairup sad at left4
            mcmax "Oh."
            show maxime shorts angry
            "I pout playfully, jutting out my lower lip."
            show maxime shorts embarrassed
            mcmax "That's too bad. I love dancing."
            show mscmc surfer_hairup grin
            "Maxime flushes, but doesn't seem to know how to respond, as he suddenly becomes very focused on his board."
        "C. I can handle this!":
            $menuhideborder = False
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.85
                xpos 415
                ypos 278
            show maxime shorts basic at right4
            show surfboard_acc_back behind mscmc:
                zoom 0.85
                xpos -115
                ypos 320
            show mscmc surfer_hairup basic at left4
            "I'm tempted to tease him about dancing, but that's not the main concern right now."
            hide surfboard_acc_back
            hide surfboard_maxime_acc_back
            hide maxime
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(I am coming on your spy mission, Maxime, whether you like it or not!)"
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.85
                xpos 415
                ypos 278
            show maxime shorts basic at right4
            show surfboard_acc_back behind mscmc:
                zoom 0.85
                xpos -115
                ypos 320
            show mscmc surfer_hairup grin at left4
            mcmax "You're a tough superspy, but even Mr. Shaken-Not-Stirred could've used an extra pair of eyes and ears sometimes."
            show mscmc surfer_hairup smile
            show maxime shorts smirk
            "Maxime snorts, glancing out over the water."
            show maxime shorts smile
            mx "I am nothing like him. That guy is a terrible spy."

    show mscmc surfer_hairup sad
    show maxime shorts embarrassed
    mcmax "Aw, c'mon."
    play sound big_splash
    show mscmc surfer_hairup smile behind maxime:
        ease 0.75 xoffset 245
        ease 0.4 xoffset 190
    show surfboard_acc_back behind mscmc:
        ease 0.8 xoffset 200
        pause 0.3
        ease 0.8 xoffset 160
    "I bump my board against his to get his attention."
    mcmax "I'm no pushover. You know that—you're the one training me."
    show maxime shorts smirk
    mx "Oh, and have you been trained as a spy?"
    show mscmc surfer_hairup basic
    "I cross my arms on my board, glaring at him stubbornly."
    show maxime shorts smirk:
        ease 0.6 yoffset 30
    "The corner of Maxime's mouth twitches in a small smile, and he leans his elbows on his board, regarding me."
    mx "Alright, here's a compromise: you can be my lookout."
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    hide maxime
    hide mscmc
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Yes!)"
    
    show surfboard_acc_back behind mscmc:
        zoom 0.85
        xpos 45
        ypos 320
    show mscmc surfer_hairup smile at left4:
        xoffset 190
        ease 0.3 xoffset 160
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.85
        xpos 415
        ypos 278
    show maxime shorts smile at right4:
        yoffset 30
    "I inwardly pump my fist, while nodding and listening intensely."
    mx "You stand out in the hallway, and we'll have some sort of signal if you see anyone coming."
    show mscmc surfer_hairup grin
    mcmax "Oh, I learned some Morse Code in Girl Scouts!"
    "I rap the 'SOS' signal on my board, three quick raps for 'S', three drawn out knocks for 'O'."
    show mscmc surfer_hairup smile
    mcmax "It's not really an SOS situation, but it's what I know. I'll tap that out on the wall."
    show maxime shorts embarrassed
    mx "Clever."
    play sound big_splash
    show maxime shorts smile
    show mscmc surfer_hairup smile:
        ease 0.4 xoffset 0
    show surfboard_acc_back behind mscmc:
        ease 0.4 xoffset -160
    "I smirk, turning swiftly to paddle away from him and leave him in my wake."
    show maxime shorts smirk
    mx "Oh, you think you're faster than me now too?"
    show surfboard_maxime_acc_back behind maxime:
        ease 0.4 xoffset -60
    show maxime shorts smirk:
        ease 0.4 xoffset -120
    show surfboard_acc_back behind mscmc:
        pause 0.2
        ease 0.4 xoffset -80
    show mscmc surfer_hairup smile:
        pause 0.2
        ease 0.4 xoffset 80
    "He reaches out and catches my ankle easily in his hand, tugging me back over the water until our boards are side-by side again."
    hide mscmc
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    hide maxime
    show maxime shorts_cu smirk_cu at maxime_cu
    "I feel an electric thrill at his touch and its gentle force."
    hide maxime
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "I shift onto my side, looking at him in excitement."
    mcmax "Wanna find out?"
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    mx "I'd love to. Countdown from three. Ready?"
    show mscmc surfer_hairup grin at left4:
        xoffset 80
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.85
        xpos 355
        ypos 278
    show maxime shorts smile at right4:
        yoffset 30
        xoffset -120
    show surfboard_acc_back behind mscmc,maxime:
        zoom 0.85
        xpos -45
        ypos 320
    pause 0.5
    play sound splash03
    show surfboard_acc_back at out_left
    show mscmc surfer_hairup grin at out_left
    show surfboard_maxime_acc_back at out_right
    show maxime shorts smile at out_right
    "I grip my board, ready to go, and as soon as he counts down we're both off, practically flying across the water and laughing all the way."

    scene bg msc_wikus_office_day at bg with clockwise_wipe
    play music mscsuspense2
    show mscmc jacket_hairup basic at centre
    "We sneak into the tournament building when no one's outside, and I park myself in the hallway just outside of Wikus' office."
    "The building is quiet and deserted—for now."
    show mscmc jacket_hairup_cu smile_cu at mscmc_cu
    "(Wikus and his assistants are out to lunch, so hopefully they'll take a good long while.)"
    hide mscmc
    show maxime casual basic at centre
    "I watch through the office window as Maxime combs it for evidence."
    "I glance up and down the hall, but it's still empty—only closed doors and faint chemical smell."    

    hide maxime
    $menuhideborder = True
    menu maximee04c3:
        "A. Peek in the adjoining room.":
            $menuhideborder = False
            show mscmc jacket_hairup basic at centre
            "I step over to a connecting door and stand on my tiptoes, peering through the narrow window of reinforced glass."
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Another little conference room...Why does he need so many room? There's already two conference halls downstairs.)"
            hide mscmc
        "B. Look down the fire escape.":
            $menuhideborder = False
            show mscmc jacket_hairup basic at centre
            "I look out the window, peering down the rusted metal fire escape."
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Looks like the custodial crew missed a bit of the wall. There's some sort of brown stain at the very bottom.)"
            hide mscmc
        "C. Rifle through the mail.":
            $menuhideborder = False
            show mscmc jacket_hairup smile at centre
            "The wall across from me has an attached mailbox with a couple envelopes poking out, and it's too tempting to resist."
            show mscmc jacket_hairup basic
            "I flip hastily through the mail, but there's nothing that will help Maxime and me."
            show mscmc jacket_hairup_cu basic_cu at mscmc_cu
            "(Mostly junk mail...Car insurance, and some sort of restaurant voucher. Nothing nefarious.)"
            hide mscmc

    # ELEVATOR DING SOUND NEEDED HERE
    "The elevator dings and I hear the doors slowly slide open."

    play music mscaction
    show mscmc jacket_hairup surprised at centre
    "I instinctively press back into the nearest doorway, horrified to hear Wikus and two of his people coming nearer."
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Dang it, they came back early!)"
    show mscmc jacket_hairup surprised at centre
    "I'm terrified to run across the hall with them about the turn the corner."
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(Ugh, I should have been watching the elevator—if Maxime tries to get out now he'll be seen!)"
    show mscmc jacket_hairup surprised at centre
    "I look desperately around the hallway, and my eyes light on the fire alarm."
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(If it works for unhappy high schoolers, it should work for us too!)"
    # fire alarm sound here
    show mscmc jacket_hairup angry at centre:
        ease 0.5 xoffset 80
        ease 0.3 yoffset 50
        ease 0.4 yoffset 0
    "I yank the red lever down, and the fire alarm instantly starts blaring."
    # stop alarm sound here
    show mscmc jacket_hairup surprised
    "I hear Wikus and his team stop in their tracks and start shouting in confusion."
    hide mscmc
    $sidecharone = "Security Guard"
    sid1 "Mr. Sapor, we need to get you outside."
    show mscmc jacket_hairup smile at centre
    "I breathe a sigh of relief as they usher Wikus out."
    show mscmc jacket_hairup_cu smile_cu at mscmc_cu
    "(Thank goodness that worked.)"
    hide mscmc
    show mscmc jacket_hairup basic at centre,step_in
    "I quickly slip into Wikus' office."
    show mscmc jacket_hairup basic at left2
    show maxime casual basic at right3
    mx "What happened?"
    show mscmc jacket_hairup smile
    show maxime casual smile
    mcmax "They came back early, and I had to think on my feet. I've bought us enough time to get out."
    show mscmc jacket_hairup surprised
    show maxime casual basic
    mcmax "Did you find anything?"
    show maxime casual sad
    "Maxime shakes his head."
    show maxime casual basic
    mx "No, I have a feeling this isn't his only office. It's far too tidy, doesn't seem like he uses it for much."
    show maxime casual sad
    "As he speaks, he opens the closet door, the last place he hasn't checked."

    # Another alarm sound
    play music mscsuspense2
    show maxime casual angry
    "Suddenly he tenses, staring at whatever's inside the closet."
    # stop alarm sound 
    mcmax "Maxime, what is it?"
    show mscmc jacket_hairup surprised behind maxime:
        ease 0.3 xoffset 80
    "I peek under his arm that's holding the closet door and gasp."
    "There's a crumpled orange reflective shirt tossed on the ground, with splatterings of what I'm horrified to realize is blood."
    # ANOTHER alarm sound
    hide maxime
    hide mscmc
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Why does it look so familiar...)"
    # stop alarm sound
    show mscmc jacket_hairup surprised behind maxime at left1
    show maxime casual sad at right3
    mcmax "I know this shirt...the missing surfer was wearing it at the opening ceremony the day he went missing!"

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.