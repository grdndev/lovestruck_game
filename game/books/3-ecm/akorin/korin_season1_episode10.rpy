label korin_season1_episode10:
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

    "I twist my head to the side and finally see who my attacker is."
    
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(Anton!)"
    hide ecmc
    $ menuhideborder = True
    menu korins1e10c1:
        "A. I knew it!":
            $ menuhideborder = False
            show anton casual basic at left2
            show ecmc nojacket_v2 pin angry at right2
            mckorin "I knew it was you!"
        "B. I can't believe it!":
            $ menuhideborder = False
            show anton casual basic at left2
            show ecmc nojacket_v2 pin surprised at right2
            mckorin "Anton, come on--there's got to be some kind of mistake!"
        "C. Wait, seriously?":
            $ menuhideborder = False
            show anton casual basic at left2
            show ecmc nojacket_v2 pin surprised at right2
            mckorin "Wait, seriously? it was just you the whole time?"
    
    "Anton ignores me."
    "He fiddles with the terminal, and I see that he's attempting to stop the data recovery and disengage the hard drive."

    hide anton
    hide ecmc
    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "(He's going to try and take it! I can't let that happen!) "
    hide ecmc
    
    show anton casual basic at left2
    show ecmc nojacket_v2 pin angry at right2
    mckorin "What is your deal with me? Do you have some sort of grudge against my dad, or something?"

    show anton casual smile at left2
    an "It's nothing personal, really. You just found the wrong piece of evidence at the wrong time."

    show ecmc nojacket_v2 pin surprised at right2
    "The realization hits me."
    mckorin "You tried to get rid of the drive in the junkyard."
    mckorin "You put in that protocol that triggered self-corruption when it was scanned!"
    an "Yes, I did. Isn't that a fun little way to destroy some random Hatchling's career?"
    an "Unfortunately for me, you're not just some random Hatchling, and your father's connections kept Dom from firing you on the spot."

    show anton casual sad at left2
    "He raises an eyebrow."
    an "That and...whatever Reyes seems to see in you."

    show ecmc nojacket_v2 pin determined at right2
    "Hearing Korin's name makes me stop and think."

    hide anton
    hide ecmc
    show ecmc nojacket_v2_cu determined_cu at ecmc_cu
    "(What would Korin do if she were here right now?)"
    hide ecmc
    
    show anton casual basic at left2
    show ecmc nojacket_v2 pin determined at right2
    mckorin "You know if you stop the drive now, the auto-backup is going straight to D.I.V.A.A.'s servers--"

    show anton casual angry at left2
    an "I {i}know{/i} where it's going. Shut up!"

    hide anton
    hide ecmc
    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "(I have to play on Anton's weaknesses. Lure him into a false sense of security.)"
    hide ecmc

    show anton casual angry at left2
    show ecmc nojacket_v2 pin determined at right2
    "I think of the times I've encountered him before: in the hall outside Korin's office, and in the lab with Gael..."

    hide anton
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(There's nothing he likes more than having people under his thumb.)"
    hide ecmc

    show anton casual angry at left2
    show ecmc nojacket_v2 pin determined at right2
    "The terminal beeps at him."
    an "Damn it. Stupid piece of...how do I...?"

    show ecmc nojacket_v2 pin surprised at right2
    "After a moment, he brandishes something at me: a taser."
    "I can tell just from looking at it that it isn't D.I.V.A.A.-issued."

    show anton casual smile at left2
    show ecmc nojacket_v2 pin sad at right2
    an "Here's what's going to happen."
    an "You're going to wipe all the data for good."

    show ecmc nojacket_v2 pin angry at right2
    mckorin "Or what?"

    show ecmc nojacket_v2 pin surprised at right2:
        easein 0.2 yoffset -30 
        easein 0.2 yoffset 0
    "Anton activates the taser, and I jump at the loud, buzzing sound."
    an "Or I'm going to fry the drive the old-fashioned way, and you with it."

    show ecmc nojacket_v2 pin surprised at right2:
        ease 0.4 right4
    "I cower, scooting away from him and putting my hands between us, palms up in surrender."
    mckorin "Okay, I'll disengage the drive. I can even show you how to wipe it for good."

    show ecmc nojacket_v2 pin sad at right4
    mckorin "Just please don't hurt me."

    show anton casual angry at left2
    "He shakes his head, irritated."
    an "I should have just destroyed the hard drive when I took it the first time."
    "I look down at my cuffed wrists."
    mckorin "Um...Anton? I need both my hands."

    show anton casual basic at left2
    "Anton squints at me, suspicious."
    mckorin "D.I.V.A.A.'s done with me no matter what. I don't care about that anymore. I just don't want to die, okay?"

    show ecmc nojacket_v2 pin angry
    mckorin "But if you want me to help before that data is recovered and auto-saved, you have to let me go, and I need to work {i}fast{/i}."

    show anton casual angry at left2
    an "If you try anything, you'll be very, very sorry."

    show anton casual angry at left2:
        linear 0.4 centre xoffset -30
    show ecmc nojacket_v2 pin surprised at right4
    "He swipes his badge across the release, and my hands are suddenly free."

    show ecmc nojacket_v2 pin surprised at right4:
        easein 0.2 right2 xoffset 20
    "Anton kicks the base of my stool, moving me so I'm in reach of the terminal."

    hide ecmc
    hide anton
    show anton casual_cu angry_cu at anton_cu
    an "Well? Do it!"
    hide anton

    show anton casual angry at centre:
        xoffset -30
    show ecmc nojacket_v2 pin determined at right2:
        xoffset 20
    "An odd sort of calm washes over me, and my fingers start flying."

    show anton casual angry at centre:
        xoffset -30
        linear 0.5 left1
    "Anton has his attention split--he keeps glancing toward the door."
    an "How much longer?"

    show ecmc nojacket_v2 pin sad at right2:
        xoffset 20
    mckorin "Almost done. I swear."

    show anton casual basic at left1
    "I watch out of the corner of my eye as he pulls out his own ARCware and swipes through the interface with one hand."
    "I can't stop to see what he's doing, but..."

    hide anton
    hide ecmc
    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "(He's distracted. It's now or never!)"
    hide ecmc

    show anton casual angry at left1
    show ecmc nojacket_v2 pin angry at right2:
        xoffset 20
    "I execute the command to eject the drive. Anton whips his head toward me."
    an "Wait, did you just--?"

    stop music
    play music ecmplottwist2
    
    show ecmc nojacket_v2 pin angry at right2:
        xoffset 20
        easein 0.4 right1 xoffset 0
    show anton casual angry at left1:
        linear 0.2 left1
        easein 0.4 left2
    "I grab the drive, and with my free arm, hit him under the chin with the sharp point of my elbow."

    show ecmc nojacket_v2 pin angry at right1:
        easein 0.2 centre
    show anton casual angry at left2:
        easein 0.2 left2
        easein 0.3 left6
        easein 0.1 left5

    "I turn on my seat, brace on the counter, and drive my foot into his kneecap."

    show anton casual angry at left5:
        alignaround (394, 949) transform_anchor True rotate 0
        linear 0.1 rotate -5
        easein 0.4 yoffset +600

    "He staggers backward, hits one of the stools, and topples back on the hard floor."
    hide anton
    mckorin "That's payback for sabotaging the security cam."

    hide ecmc
    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "(Okay--time to run!!)"
    hide ecmc

    show ecmc nojacket_v2 pin surprised at centre
    "I dash for the door and scan my badge to leave--only to find myself colliding with a locked door."
    hide ecmc

    show anton casual smile at centre
    "I turn around. Anton limps towards me...laughing."
    an "Check your ARCware. Go on, do it."
    hide anton

    # TODO [SFX: beep sound] https://youtu.be/DkUEP6Ww9H8?t=199
    play sound question_003

    show ecmc nojacket_v2 pin surprised at centre
    "As he tells me, my ARCware buzzes to life with an override alert."
    "I swipe through, the horror dawning on me..."
    hide ecmc

    show anton casual smile at left2
    show ecmc nojacket_v2 pin sad at right4
    an "That's right. I put an APB out for your arrest."

    hide ecmc
    hide anton
    show anton casual_cu smile_cu at anton_cu
    an "Any minute now, security will be here."
    an "They'll take you into custody, and I'll tell them how you attacked me when I caught you trying to wipe the drive..."
    hide anton

    show anton casual smile at left2
    show ecmc nojacket_v2 pin surprised at right4
    "Panic floods me."

    hide anton
    hide ecmc
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(I had so much trouble making people listen to me before.)"
    "(I can't stay here!)"
    hide ecmc

    show anton casual smile at left2
    show ecmc nojacket_v2 angry pin at right4
    "I took to my right and hit the fire alarm."

    show anton casual angry at left2
    "The magnetic locks at my back click open. I don't bother looking back at Anton's outraged expression."
    
    hide ecmc
    hide anton
    show anton casual_cu angry_cu at anton_cu
    an "You won't make it out of the building!"
    hide anton

    show bg ecm_dorm_hallway_on at bg
    show ecmc nojacket_v2 angry pin at centre
    with wiperightdissolve

    stop music
    play music ecmaction2

    show ecmc nojacket_v2 angry pin at centre
    "I hit the hallway running, my ARCware blasting notices into my holo interface."
    "I swipe them away, trying to keep calm, but..."

    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(It's been sent to all members of D.I.V.A.A., and local law enforcement.)"
    hide ecmc
    
    show ecmc nojacket_v2 pin angry at centre
    "I try to hold back my panic, looking down at what's important..."

    hide ecmc
    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "(I still have the hard drive! I can't let it get back into Anton's hands.)"
    hide ecmc

    show ecmc nojacket_v2 pin angry at centre
    "I keep running and take the first exit I see."
    # TODO [SFX: beep sound]
    play sound question_003 

    show bg ecm_stairway_on at bg with wiperightdissolve

    show ecmc nojacket_v2 pin surprised at centre
    "Just as I step into the stairway, my ARCware lights up with a call. "
    mckorin "Korin!"

    show korin nojacket pin surprised at holo_mask, korin_holo, right3
    show ecmc nojacket_v2 pin surprised at left3
    ko "[genericfn], what's going on? I just got a notice--"

    show ecmc nojacket_v2 pin angry at left3
    mckorin "It's Anton! Anton's the killer, it's his drive, he's trying to frame me!"

    show korin nojacket pin angry at holo_mask, korin_holo, right3
    ko "He {i}WHAT{/i}?!"
    mckorin "The drive was almost recovered. I saved what we have so far, but if the guards catch me and Anton gets his hands on it again--"

    show ecmc nojacket_v2 pin surprised at left3
    ko "I'm coming back. I'm not far! It'll just be a few minutes--"

    show ecmc nojacket_v2 pin angry at left3
    mckorin "Korin, there's no time! D.I.V.A.A. security is gonna be here any second!"
    ko "Okay. Stop! Stop."

    show ecmc nojacket_v2 pin surprised at left3
    "I do as she says, stopping on the landing. In the quiet, between the blaring of overhead alerts, I can hear the distant sound of footsteps."
    "Somewhere below me, I hear someone else enter the stairwell."

    show ecmc nojacket_v2 pin determined at left3
    "I signal for quiet to Korin, and her voice is soft right in my ear."

    show korin nojacket pin sad at holo_mask, korin_holo, right3
    ko "You're still on the third floor, right? Don't go down. Go up."

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(What?!)"
    hide ecmc

    show korin nojacket pin angry at holo_mask, korin_holo, right3
    show ecmc nojacket_v2 pin determined at left3
    ko "Trust me! They're going to be watching the exits."

    show korin nojacket pin sad at holo_mask, korin_holo, right3
    ko "There's no way you'll get out, and like you said, if Anton gets his hands on that drive again..."

    show ecmc nojacket_v2 pin angry at left3
    "I nod at her holo projection, then sneak up the next two flights as quietly as I can."

    show korin nojacket pin angry at holo_mask, korin_holo, right3
    "On Korin's holo display, I can see that she's hurrying as well."
    ko "I'll be there soon. Nobody's going to put you in a cell under my watch..."
    mckorin "They just can't get the drive. Anton's too clever, he'll think of some way to sabotage everything again!"

    show bg ecm_dorm_hallway_on at bg with wiperightdissolve
    "I emerge on the next floor."

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "You're right. This floor is empty...but I hear people coming up the stairs!"
    ko "And you've got to watch the elevators, too..."

    show ecmc nojacket_v2 pin determined at left3
    "I catch my breath, waiting for her next instructions."

    show korin nojacket pin surprised at holo_mask, korin_holo, right3
    ko "Okay. There's a door at the end of the hall. Do you see it?"
    "I nod."
    ko "That's my friend Rion's office. It should be unlocked--"

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "--Since I hit the fire alarm. Got it!!"

    show bg ecm_generic_office_night_off at bg with wiperightdissolve

    show korin nojacket pin basic at holo_mask, korin_holo, right3
    show ecmc nojacket_v2 pin determined at left3
    "I rush for the door and go tumbling inside, shutting it behind me."

    show korin nojacket pin surprised at holo_mask, korin_holo, right3
    ko "Immediately to your left, there should be a vent. Do you see it?"

    show ecmc nojacket_v2 pin sad at left3
    "I look down...and sigh."
    ko "Can you fit inside?"

    show ecmc nojacket_v2 pin sad at left3:
        ease 0.4 yoffset +80
    "I crouch down. The cover comes off easily, and the space inside looks a lot roomier than I thought."
    mckorin "Yes..."

    show korin nojacket pin angry at holo_mask, korin_holo, right3
    ko "Wait. Before you do--pick up Rion's office chair and use it to break the window."

    show ecmc nojacket_v2 pin embarrassed at left3:
        yoffset +80
    "I wince at the thought, but I get Korin's idea: to make it look like I took another path to escape."

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu embarrassed_cu at ecmc_cu
    "(What, am I gonna get in {i}more{/i} trouble than I'm already in?)"
    hide ecmc

    scene bg ecm_airduct_on at bg with wiperightdissolve
    "I do as she says, then duck inside the vent and pull the grate in behind me."

    show korin nojacket pin basic at holo_mask, korin_holo, centre:
        linear 0.3 alpha 0.0
    "Korin's holo projection flickers away suddenly."

    hide korin
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    mckorin "Korin? Hello?"
    "I go suddenly silent as I hear the door open in the office behind me."
    sec "We've got a broken window here!"
    sec "We need teams responding outside. I think she's out on the scaffolding!"

    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "I keep moving through the vents as quietly as I can, taking the first turn I come to."
    hide ecmc

    show korin nojacket_cu basic_cu at holo_mask, korin_holo, korin_cu with dissolve
    "When I do, Korin pops back into view."

    hide korin
    show korin nojacket_cu surprised_cu at holo_mask, korin_holo, korin_cu
    ko "Sorry. Did you go right?"
    hide korin

    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    mckorin "Left."
    hide ecmc

    show korin nojacket_cu basic_cu at holo_mask, korin_holo, korin_cu
    ko "Good. There should be an exit straight ahead."
    
    scene bg ecm_dominick_office_night at bg with wiperightdissolve
    "I emerge..."

    show ecmc nojacket_v2 pin determined at left3
    show korin nojacket pin basic at holo_mask, korin_holo, right3
    ko "You're in Dom's office, right?"

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "Why do you know wo much about the vents in this building?"

    show korin nojacket pin smirk at holo_mask, korin_holo, right3
    ko "Story for another time. Listen, the back stairwell should be right across the hall from you."
    ko "At the bottom of those stairs, you'll take a left, and then the server room will be on your right."
    ko "You can make it, but you'll need to make a break for it when I tell you to. Okay?"

    show ecmc nojacket_v2 pin embarrassed at left3
    mckorin "Okay..."

    show korin nojacket pin surprised at holo_mask, korin_holo, right3
    ko "So get to the stairway...now!"

    show bg ecm_stairway_on at bg with wiperightdissolve

    show korin nojacket pin basic at holo_mask, korin_holo, right3
    "I make it inside as quickly and quietly as I can. Listening for noise at the bottom and hearing nothing, I start my descent."

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "Wait, Korin...the path you told me to get to the records room passes right by reception."
    ko "Yep."
    mckorin "Isn't security going to be posted up down there?"

    show korin nojacket pin smirk at holo_mask, korin_holo, right3
    ko "It'll be risky going, but I can guide you through it, okay?"

    show ecmc nojacket_v2 pin sad at left3
    "My voice shakes."
    mckorin "Korin, I don't know if I can do it without getting caught."

    show korin nojacket pin smile at holo_mask, korin_holo, right3
    ko "You can! Yes, you can."
    ko "[genericfn]. Look at me. Breathe..."
    "She motions with her hands, breathing in with me, and breathing out."

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(I wish she were here with me...)"
    hide ecmc

    show korin nojacket_cu angry_cu at holo_mask, korin_holo, korin_cu
    ko "Okay. Ready? You need to move...now!"
    hide korin

    $menuhideborder = True
    menu korins1e10c2:
        "A. Trust Korin and run to safety." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin nojacket pin smile at holo_mask, korin_holo, right3
            show ecmc nojacket_v2 pin determined at left3
            "I swipe open the door, and it opens with a nearly inaudible hiss."
    
            scene bg ecm_office_hq_off at bg
            show ecmc nojacket_v2 pin surprised at centre
            with wiperightdissolve
            "I enter the open area nearest reception. I see a group of security guards debriefing with one another..."
            sec "No sign of her on the scaffolding..."
            sec "Let's check the roof, then. Come on!"
            show ecmc nojacket_v2 pin determined at centre:
                easein 0.4 yoffset +80
            "I crouch down behind a low wall and wait for the footsteps to recede. "
            show ecmc nojacket_v2 pin determined at centre:
                yoffset +80
                parallel:
                    easein 0.4 xoffset +200
                parallel:
                    linear 0.4 alpha 0.0
            "When they're gone, I bolt for the records room."
            hide ecmc

            scene bg ecm_records_room_on at bg with wiperightdissolve
            "The door is open and dark when I slip inside." 

            show ecmc nojacket_v2 pin surprised at centre
            "My heart stops. There's someone already here."
            hide ecmc

            show korin nojacket_cu surprised_cu at korin_cu
            "Korin swipes the door shut, locks it..."

            show korin nojacket_cu sad_cu at korin_cu
            "...And suddenly, I find myself in her arms. "
            ko "I've got you. It's okay."
            "I stay there, motionless. "
            "She holds me, and I think I'm close enough that I can hear her heartbeat."
            
            hide korin
            "Neither of us dares to breathe as shadows under the doorway slip by outside."
            "But once they're past, I close my eyes and breathe Korin in." 
            "I'm still on high alert, and I know we're not out of trouble yet..."

            show ecmc nojacket_v2_cu sad_cu at ecmc_cu
            "(But with her here, I finally feel safe.)"
            hide ecmc

            show korin nojacket_cu smile_cu at korin_cu
            "When she speaks, it's quiet in my ear, barely reaching over the noise of the servers."
            ko "I'm {i}really{/i} glad you're safe."

            show korin nojacket pin basic at right1
            show ecmc nojacket_v2 pin smile at left1
            "Slowly, we part. Her hands drift down my arms, and when she reaches my hands, she realizes what I'm holding."
        
            show korin nojacket pin surprised at right1
            ko "The hard drive? You still have it?"

            show ecmc nojacket_v2 pin determined at left1
            mckorin "I couldn't leave it with Anton. He'd have destroyed it for good and blamed it on me."

            show ecmc nojacket_v2 pin surprised at left1
            mckorin "Wait, you didn't think I had it, and you were going to help me anyway?"

            show korin nojacket pin smile at right1
            ko "What? Of course I was."

            show ecmc nojacket_v2 pin sad at left1
            mckorin "But...without any evidence..."

            show korin nojacket pin sleep at right1
            "Korin shakes her head."

            show korin nojacket pin smile at right1
            ko "I'd have figured out some other way to protect you."
            "She looks into my eyes, and I gaze up into hers."
            "My poor heart hasn't had a single chance to slow down. I hold on to Korin, keeping myself steady..."

            hide korin
            hide ecmc
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            "(Are we...getting closer? Is she...?)"
            hide ecmc

            show korin nojacket pin angry at right1
            show ecmc nojacket_v2 pin angry at left1
            "We both tense as more shadows pass by the door. When they're gone, I hold up the drive."
            mckorin "We're not out of trouble yet."
            mckorin "If someone gets a hold of Eko, she could use the program we wrote to track this thing by RFID."

            show korin nojacket pin smirk at right1
            ko "Then we just need to make a run for it."

            show ecmc nojacket_v2 pin surprised at left1
            mckorin "Korin...if anyone realizes you're involved..."

            show korin nojacket pin sleep at right1
            "She shakes her head. "

            show korin nojacket pin smirk at right1
            ko "Then I'm involved. And sure, it'll complicate things..."

            show korin nojacket pin angry at right1
            ko "But we can't let this get back in Anton's hands. I think you understand that better than anyone."
            "Her words are so fierce that I'm practically warmed to my core. "

            show ecmc nojacket_v2 pin smile at left1
            mckorin "Korin...I'm so glad you came back for me. I don't know how to thank you."

            hide ecmc
            hide korin
            show korin nojacket_cu smile_cu at korin_cu
            "She smiles and puts a hand on my cheek, stroking it with her thumb."
            ko "Thank me later, Scraps. For now, we need to get out of here."
            hide korin

            show korin nojacket pin angry at right1
            show ecmc nojacket_v2 pin surprised at left1
            "She pops open the console by the door, then rips a couple wires inside."

            show ecmc nojacket_v2 pin sad at left1
            "I wince."

            show korin nojacket pin smile at right1
            ko "What? We're taking the back exit. I just don't want anyone following us."

            show ecmc nojacket_v2 pin surprised at left1
            mckorin "Is there any way we can get ahead of this? So we don't have to, you know...run? Hide?"

            show korin nojacket pin surprised at right1
            ko "Dom or Gael could clear the APB alert. Or any of their direct reports..."

            show korin nojacket pin sad at right1
            ko "I've been messaging Dom, but he's not responding. Because of that alert, he's probably on the line with the F.D.I. right now..."

            show ecmc nojacket_v2 pin sad at left1
            mckorin "God. I'm done for, aren't I?"

            show korin nojacket pin smile at right1
            ko "Not as long as I have anything to say about it."
            "I follow her to the other end of the records room. She stops before the door."
            ko "From here, it's just a short walk down the hall, and then we're out."

            show ecmc nojacket_v2 pin surprised at left1
            mckorin "Wait, we're just going to walk out the front door?"

            show korin nojacket pin surprised at right1
            ko "I was listening in on dispatch. Aren't most of them up checking the roof now?"

            show ecmc nojacket_v2 pin embarrassed at left1
            mckorin "I think so..."

            show korin nojacket pin smile at right1
            ko "Then we walk out the front door and make for my place. Just keep your head down, and everything will be fine."

            hide ecmc
            hide korin
            show korin nojacket_cu smile_cu at korin_cu
            ko "Do you trust me?"
            "I look up into her eyes, and I'm steadied by the confidence that I find there."
            hide korin

            show korin nojacket pin smile at right1
            show ecmc nojacket_v2 pin smile at left1
            mckorin "I trust you. Let's do this."
        "B. Wing it on your own.":
            $menuhideborder = False
            show korin nojacket pin smile at holo_mask, korin_holo, right3
            show ecmc nojacket_v2 pin sleep at left3
            "I shake my head."

            show korin nojacket pin sad at holo_mask, korin_holo, right3
            show ecmc nojacket_v2 pin sad at left3
            mckorin "I can't! I just can't..."
            ko "Okay. Stay where you are and hold tight."
            
            hide korin
            hide ecmc
            "I press myself against the wall and barely dare to breathe." 
            "The door opens..."

            show korin nojacket pin sad at right1
            show ecmc nojacket_v2 pin sad at left1
            ko "[genericfn]?"

            hide korin
            hide ecmc
            "I practically break down, throwing my arms around her in a desperate hug."

            show korin nojacket_cu sad_cu at korin_cu
            "She pulls away sooner than I'd like, and motions for me to be quiet." 
            "I wait, holding her hand in tense silence, and do my best to keep up when she motions for us that it's time for us to get moving. "
    
    show bg ecm_office_hq_off at bg with wiperightdissolve
    stop music fadeout 0.5
    play music ecmemotional1 fadein 0.5

    show korin nojacket pin surprised at right1
    show ecmc nojacket_v2 pin surprised at left1
    "We're almost to the door...when suddenly, from the shadows, someone blocks our path. "
    hide korin
    hide ecmc

    show connie casual smile at centre
    co "Well, well...you're not headed out on another coffee run at this time of night, are you?"

    show connie casual smile at right4
    show korin nojacket pin surprised at left1
    show ecmc nojacket_v2 pin surprised at left4
    "Korin and I skid to a halt. Connie stands before us, resolute and unmovable."
    co "Oh, I'm {i}sooo{/i} glad I decided to work late tonight."

    show korin nojacket pin angry at left1
    ko "So am I. Connie, listen--you have the authority to turn off the APB on Dom's behalf. You have to do it, now!"

    show connie casual angry at right4
    co "And {i}why{/i} would I do that?"

    hide connie
    hide korin
    hide ecmc

    $menuhideborder = True
    menu korins1e10c3:
        "A. Do it for yourself.":
            $menuhideborder = False
            show connie casual angry at right4
            show korin nojacket pin angry at left1
            show ecmc nojacket_v2 pin angry at left4
            "I put up my hand and hold out the hard drive."
            mckorin "You want to go ahead as an investigator and take me in yourself? Fine. You've caught me."
            mckorin "But you can't let anyone else get their hands on this, okay?"
        "B. Do it to impress Dom.":
            $menuhideborder = False
            show connie casual angry at right4
            show korin nojacket pin angry at left1
            show ecmc nojacket_v2 pin angry at left4
            mckorin "I'll surrender right now and wait for Dom if you do. You can tell him you apprehended me yourself."
        "C. It's no use asking you.":
            $menuhideborder = False
            show connie casual angry at right4
            show korin nojacket pin angry at left1
            show ecmc nojacket_v2 pin angry at left4
            mckorin "It's no use asking you to do anything. You've had it out for me since my first day here, haven't you?"
    "Connie opens her mouth, looking confused, but she's interrupted."
    hide connie
    hide korin
    hide ecmc
    
    show anton casual angry at centre
    an "There you are!"
    "We jump. Anton staggers in, still limping."
    an "Give it up, Hatchling. I caught you."

    show connie casual angry at right4
    show anton casual angry at left1
    co "Actually, it was m--"
    an "Secretary, call security. They need to hear all about how she assaulted me and took that hard drive!"

    hide connie
    show korin nojacket pin surprised at right4
    "He points at Korin."
    an "And you, Reyes...what exactly did she do to manipulate you into helping her?"
    an "Or is it just misplaced guilt over your former partner's disappearance?"
    ko "I'm...it's not...!"

    hide anton
    hide korin
    show korin nojacket_cu surprised_cu at korin_cu
    "Alarmed, I look over at Korin."
    hide korin

    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(I know that's not why she's helping me. But...she's barely keeping it together right now.)"
    hide ecmc

    show anton casual angry at left1
    show korin nojacket pin angry at right4
    ko "If you want to get to her, you'll have to get through me!"

    show anton casual smile at left1
    "Anton laughs darkly."
    an "You don't want to go down like this, Reyes. Trust me."

    hide korin
    show connie casual angry at right4
    "He looks at Connie."

    show anton casual angry at left1
    an "{i}None{/i} of you do. Call security. NOW!"

    show connie casual basic at right4
    "Connie briskly pulls up her ARCware."

    show connie casual angry at right4
    co "Security to level one."

    hide anton
    show ecmc nojacket_v2 pin surprised at left3
    mckorin "Connie, no! Please..."
    hide connie
    hide ecmc

    show anton casual angry at left2
    show korin nojacket pin angry at right3
    "But Connie ignores me. Anton takes a step towards us, and Korin puts herself between us, protecting me."

    hide anton
    hide korin
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(What do we do? Do we charge at Connie and make a break for it?)"
    hide ecmc

    show connie casual basic at right3
    show anton casual angry at left2
    co "Anton, there's something you should know."
    "He scowls at her."
    an "And what's that?"

    show connie casual angry at right3
    co "I'm not a secretary. I'm Dom Vega's {i}personal assistant{/i}."
    "She finishes typing something in her ARCware interface that none of us can see, and pushes a button."

    # TODO [SFX: beep sound]
    play sound question_003

    hide anton
    hide connie

    show korin nojacket pin surprised at right3
    show ecmc nojacket_v2 pin surprised at left3
    "My ARCware and Korin's buzzes to life. It's an APB notice..."
    "For Anton."
    hide korin
    hide ecmc

    show connie casual angry at right3
    show anton casual angry at left2
    an "Wait--what did you DO?!"
    "But Anton has no time to react as security officers pour in from every entrance."
    hide connie

    show anton casual angry at left2:
        easein 0.3 left1
    show ecmc nojacket_v2 pin sad at right5
    show korin nojacket pin angry at right2

    "He snarls and makes a leap for me. Korin pushes me behind her, ready to face his wrath--"
    hide korin
    hide ecmc

    show anton casual angry at centre:
        easein 0.5 yoffset +600
    "And he's seized by six security personnel and wrestled to the ground."
    hide anton

    stop music fadeout 0.5
    play music ecmemotional3 fadein 0.5

    show connie casual basic at right2
    show korin nojacket pin smile at left3
    "Korin pulls up her ARCware, then breathes a sigh of relief as she turns to Connie."
    ko "You...?"

    show connie casual smile at right2
    co "Yes, I cleared it. That's what you told me to do, isn't it?"

    hide korin
    show ecmc nojacket_v2 pin surprised at left3
    mckorin "But...you...hate me. Don't you?"
    "Connie rolls her eyes."
    co "Even if I did, I'd never let something so petty get in the way of protecting D.I.V.A.A.'s reputation."

    hide ecmc
    show korin nojacket pin surprised at left3
    ko "How did you know you could trust us?"
    co "I've been looking into [genericfn] a lot since her first day."

    show connie casual angry at right2
    "She looks at me, defensive and yet apologetic."
    co "I was trying to come up with what motive you'd have to bring down D.I.V.A.A. by tampering with evidence."
    co "And...I couldn't find anything. So."
    "I nod in the uneasy silence that follows. Connie throws up her hands."
    co "Well, I'm not going to {i}apologize{/i} for investigating a possible suspect. I'm trying to be an investigator too, you know!"

    show korin nojacket pin smirk at left3
    ko "I know. You're off to a promising start so far, Connie. I mean it."
    "Connie's cheeks glow, and I empathize with her."

    hide connie
    hide korin
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(Yeah, compliments from Korin have that effect on people...)"
    hide ecmc

    show connie casual basic at right2
    show korin nojacket pin smirk at left3
    co "Reyes, I should have taken your word on her from the start. I've never known you to be a bad judge of character."

    show korin nojacket pin sad at left3
    "Korin's shoulders sag. She shakes her head."
    ko "Until now. Anton...I had no idea..."
    "Connie looks sympathetic."
    co "It's okay. None of us did."
    "Connie eyes the two of us, then awkwardly clears her throat."

    show connie casual smile at right2
    co "You two seem pretty rattled. I'll clear things up here if you two want to...um...hold hands...elsewhere."
    "That's all the assurance we need to get out of there."

    hide connie
    hide korin
    "I hand off the drive and thank Connie one more time, but Korin doesn't drop my hands as she leads me to the door."

    show korin nojacket_cu smile_cu at korin_cu
    ko "Well...I don't know about you, but I need to blow off some steam."
    ko "Can I buy you a drink, [genericfn]?"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.
    
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

