label jd_season1_episode1:

    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show blackscreen at bg with dissolve
    show bg main_day at bg
    show truck_back_day at bg
    show hiflmc bowling basic at right2:
        zoom 1.05
    show grace waitress basic at left2:
        zoom 1.05
    show truck_front_day at bg

    "The needle on my gas gauge is piercing right through the little red E as I turn onto Main Street,"
    "And I do a mental calculation on how much it would take to fill the tank while we pass the station."
    show hiflmc bowling sad
    "(Why is the answer always 'too much'?)"
    show grace waitress sad
    gr "You okay over there, sis?"
    gr "Frown any hard and your face might get stuck that way."
    show hiflmc bowling surprised
    "I pull myself back to the present, splitting my focus between the road and Grace's voice."
    show hiflmc bowling happy
    "It takes a second, but I manage a smile."
    mcjd "I'm older. That's supposed to be my line to you."
    show grace waitress basic
    gr "But I'm eighteen now. You know, a legal adult?"
    mcjd "Barely. You're still a kid to me."
    show grace waitress sad
    "Grace pouts, but it doesn't last long."
    "She knows I'm teasing her."
    show grace waitress basic
    "(Someone has to, right?)"
    show hiflmc bowling sad
    "(Since our parents passed away, I got the upgrade from Big Sister to Responsible Adult.)"
    show hiflmc bowling basic
    gr "At least I have a job."
    show hiflmc bowling sarcastic
    mcjd "Which is a miracle."
    mcjd "The problem with living a one horse town is that the horse is like the only one guaranteed Social Security."
    show hiflmc bowling happy
    show grace waitress happy
    "It's a bad joke, but Grace giggles anyway, giving my shoulder a playful shove when I pull up to the diner and kill the engine."
    mcjd "Say hi to Luce for me, okay?"
    mcjd "And have a good day at work."
    gr "Fingers crossed for hungover trucker tips."
    gr "They think I'm an angel when I bring the coffee over."
    scene bg main_day at bg with wipeleft
    show hiflmc bowling basic at centre
    "She hops on out and I lock her door before doing the same."
    "There's not much point in moving my truck when the bowling alley is just across the street."
    show hiflmc bowling surprised
    unknown "Hey, girl."
    unknown "What's a hot piece like you doing in a place like this?"
    show hiflmc bowling blush
    "I blush, whirling around to give a piece of my mind to whoever just spoke."
    hide hiflmc
    show jd_s1_mini1 at bg with dissolve:
        zoom 0.4
    stop music fadeout 1.0
    play music jordandavies
    "Then my eyes lock on the sharp steel of familiar piercings and the small skull engraved in a set of headphones."
    hide jd_s1_mini1
    show hiflmc bowling blush at left2
    show jd casual smirk at right2
    "JD's smirk is equal parts wicked and knowing, waiting for whatever was about to come out of my mouth."
    show hiflmc bowling sarcastic
    mcjd "JD, god."
    mcjd "I thought you were some..."
    jd "Some asshole?"
    show hiflmc bowling basic
    mcjd "Yeah, some asshole."
    show hiflmc bowling happy
    show jd casual happy
    "Their grin widens, and I catch myself smiling too."
    mcjd "Jerk."
    show jd casual smirk
    jd "Somehow that feels like a downgrade from 'asshole.' Less punch."
    show hiflmc bowling sarcastic
    mcjd "Give me a break on the barrier. My coffee hasn't kicked in yet."
    jd "Fair enough."
    show hiflmc bowling surprised
    show jd casual basic
    "They lean back against the wall next to the bowling alley, and I raise an eyebrow."
    mcjd "Any reason you're not going inside?"
    show jd casual sad
    jd "..."
    jd "Want to do me a favor?"
    hide hiflmc
    hide jd
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(Those are the magic words leading to regret, but I'm too curious about what they want.)"
    hide hiflmc
    show hiflmc bowling basic at left2
    show jd casual basic at right2
    mcjd "Sure, why not?"
    show jd casual sad
    jd "I pissed Razi off earlier."
    jd "Go in and make sure he's not going to take my head for it."
    show hiflmc bowling surprised
    mcjd "What exactly did you do?"
    show jd casual smirk
    jd "Guess."
    hide hiflmc
    hide jd
    $menuhideborder = True
    menu jds1e1c1:
        "A. You wrote on Razi's face.":
            $menuhideborder = False
            show hiflmc bowling basic at left2
            show jd casual basic at right2
            mcjd "You wrote on Razi's face while he was sleeping?"
            show jd casual smirk
            jd "Actually, no, but I'll keep that in mind for another time."
        "B. Kept him up with your bike.":
            $menuhideborder = False
            show hiflmc bowling basic at left2
            show jd casual smirk at right2
            mcjd "Did you come back at 3am with your motorcycle roaring?"
            show jd casual sad
            jd "...That too."
            jd "But that's not what pissed him off."
        "C. Ran off with his liquor.":
            $menuhideborder = False
            show hiflmc bowling basic at left2
            show jd casual basic at right2
            mcjd "Is all the good booze missing from behind the bar now?"
            show jd casual angry
            jd "It's a bar in a bowling alley."
            jd "None of the booze is good."

    hide hiflmc
    hide jd
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(They're not going to tell me.)"
    "(I might as well find out myself.)"
    hide hiflmc
    show hiflmc bowling basic at left2
    show jd casual basic at right2
    mcjd "Okay. I'll be right back."
    show jd casual smirk
    "JD gives me a half-hearted salute before I head inside the bowling alley."
    scene bg bowling at bg with wiperight
    stop music fadeout 1.0
    play music hifleveryday
    show razi casual angry at centre
    "Razi is grumbling the moment I see him, setting up the register for the day."
    show razi casual angry at left2
    show hiflmc bowling surprised at right2
    mcjd "Uh, good morning?"
    show razi casual basic
    ra "Oh, [genericfn]."
    ra "You're a little early."
    show hiflmc bowling basic
    mcjd "That's because I come bearing a message."
    mcjd "JD wants to make sure you're not going to leave them hanging out to dry."
    show razi casual angry
    "Razi huffs, then pushes the register drawer shut."
    ra "They used all the hot water this morning, which left me stranding in ice when I tried to shower."
    ra "JD doesn't even need hot water, alright?"
    ra "They can heat it up themself."
    show hiflmc bowling surprised
    "I blink, not quite sure what to make of that, but the point is to make sure JD can come inside so I don't spend the day working by myself."
    show razi casual basic
    show hiflmc bowling happy
    mcjd "How about JD cleans behind the arcade machines to make up for it?"
    mcjd "You never want to go back there."
    hide hiflmc
    hide razi
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(And neither do I.)"
    "(That's where soda spills go to die.)"
    hide hiflmc
    show razi casual basic at left2
    show hiflmc bowling basic at right2
    ra "... If they promise to, then yes, that's a fair trade."
    hide hiflmc
    hide razi
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(Success.)"
    scene bg main_day at bg with wiperight
    show hiflmc bowling basic at centre
    "Poking my head back out the front door, I catch JD's attention with a wave."
    show hiflmc bowling basic at right2
    show jd casual basic at left2
    mcjd "You're in."
    show hiflmc bowling happy
    mcjd "Also, you owe me one."
    show jd casual smirk
    "They smirk, then shrug."
    jd "Hit me up any time."
    scene bg bowling at bg
    pause
    "After my attempt at diplomacy in the morning, the rest of my shift is pretty boring."
    show razi casual smirk at left2
    show diego doctor glassesbasic at right2
    "Dr. Escalona comes in for his usual drink and chat with Razi,"
    hide razi
    hide diego
    show hiflmc bowling basic at right2
    show jd casual basic at left2
    "But JD and I are stuck cooling our hells by the lanes waiting for customers."
    mcjd "You ever think we could get more people in here?"
    jd "We're drawing from a pretty small pool anyway."
    show jd casual sad
    jd "Besides, do you really want to deal with more customers?"
    show hiflmc bowling sarcastic
    mcjd "Maybe I'd get a raise if there were more hours to work."
    show jd casual happy
    "JD considers that for a second, then laughs."
    jd "Razi should start offering a free shot with every rental."
    jd "Drunk folks spend more money."
    show hiflmc bowling surprised
    mcjd "You know this from experience?"
    show jd casual smirk
    jd "Do I look like I have money?"
    hide hiflmc
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Touche, JD.)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show jd casual smirk at left2
    jd "I just show my pretty little face and bartenders give it up for free."
    hide jd
    show hiflmc bowling surprised at centre
    stop music fadeout 1.0
    play music hifllitegetitdone
    "I'm about to make a smart comment back when the front door swings open, hard enough to jingle against the back wall."
    hide hiflmc
    show jd casual angry at left2
    show mac glassescop angry at right2
    "Sheriff Mackenzie Hunt walks into the bowling alley with narrowed eyes, and JD spits a curse under their breath."
    hide mac
    show hiflmc bowling basic at right2
    jd "Cover for me."
    show hiflmc bowling surprised
    mcjd "What?"
    jd "Just pretend I'm not here, I'm going to duck in the back."
    show jd casual angry at left3
    show hiflmc bowling surprised at centre
    show mac glassescop angry at right3
    "Unfortunately for them, the sheriff walks right up to us, and JD hasn't made it more than a couple steps."
    hide hiflmc
    show jd casual basic at left2
    show mac glassescop angry at right2
    ma "Jordan Davies."
    show jd casual angry
    jd "Goddamn it."
    show jd casual smirk
    jd "I mean, good afternoon, Sheriff. You look lovely."
    show jd casual happy
    "She raises an eyebrow at them, and JD offers a charming smile back."
    "Unfortunately, Mackenzie's not buying what they're selling."
    show jd casual basic
    ma "I got six calls because of your bike last night. Noise complaints."
    ma "I know it might be hard to see houses from the main road, but they can all hear you breaking ninety before sunrise."
    ma "The limit on that street if fifty, tops."
    jd "It's not like there's anyone to run into out there."
    ma "Tell that to the deer I hauled off the road two weeks ago."
    show jd casual smirk
    jd "That couldn't have been that much of a burden for you."
    ma "..."
    jd "Kidding."
    ma "This isn't Jersey, Jordan."
    ma "Follow the law, or we're going to have a problem."
    hide jd
    show hiflmc bowling sad at left2
    "I swallow hard."
    "Even without the sheriff's eyes on mine, it's hard not to be intimidated."
    hide hiflmc
    hide mac
    show hiflmc bowling surprised at right1
    show jd casual smirk at left1 behind hiflmc
    "JD, on the other hand, doesn't seem bothered in the lasat. They sling an arm around my waist, pulling me close."
    mcjd "JD..."
    show hiflmc bowling blush
    "My face goes red before I can do anything to stop it."
    "(They're a lot stronger than they look.)"
    jd "Be my character witness, [genericfn]."
    show jd casual happy
    jd "I'm a good person, right?"
    mcjd "Um-!"
    hide hiflmc
    hide jd
    $menuhideborder = True
    menu jds1e1c2:
        "A. JD's great.":
            $menuhideborder = False
            show hiflmc bowling happy at right1
            show jd casual happy at left1 behind hiflmc
            mcjd "JD's great."
            mcjd "I mean, that’s why we keep them around, right?"

        "B. It was an honest mistake.":
            $menuhideborder = False
            show hiflmc bowling sad at right1
            show jd casual happy at left1 behind hiflmc
            mcjd "I'm sure the motorcycle thing was an honest mistake."
            mcjd "It's easy to lose track of speed on that old road."

        "C. ...":
            $menuhideborder = False
            show hiflmc bowling sad at right1
            show jd casual happy at left1 behind hiflmc
            mcjd "..."
            hide hiflmc
            hide jd
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(I don't know! They caught me off guard!)"

    hide hiflmc
    hide jd
    show mac glassescop sleep at centre
    "Mackenzie sighs, reaching up to rub the bridge of her nose."
    show mac glassescop basic
    ma "This isn't a trial. You don't need witnesses."
    show mac glassescop sad
    ma "Just watch it in the future, alright?"
    ma "There's already a couple marks on your record."
    show mac glassescop sad at right2
    show jd casual smirk at left2
    jd "What are you going to do, Sheriff? Arrest me?"
    show mac glassescop angry
    ma "No. You'd enjoy that too much."
    show mac glassescop smirk
    ma "But I could stick you in the back of the squad car with my deputy driving."
    ma "Elmer loves showtunes, and singing along to them out of key."
    hide mac
    show hiflmc bowling happy at right2
    show jd casual surprised
    "JD looks nothing short of appalled, and I try not to laugh."
    hide hiflmc
    hide jd
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(Guess the Sheriff got their number.)"
    hide hiflmc
    show mac glassescop smirk at right2
    show jd casual angry at left2
    jd "That's torture and you know it."
    show mac glassescop happy
    "Mackenzie's smile flashes all her teeth."
    ma "I'll do whatever it takes to keep this town safe, Davies."
    show mac glassescop angry
    ma "So behave."
    hide jd
    show mac glassescop angry at centre
    "She doesn't bother letting them get in another remark, turning around to leave."
    hide mac
    show jd casual basic at left2
    show hiflmc bowling basic at right2
    "Once the front door swings shut again, JD's arm slips away from me."
    show hiflmc bowling blush
    "I bite my lip."
    hide jd
    hide hiflmc
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(That actually felt... kind of nice.)"
    show hiflmc bowling_cu basic_cu
    "(But they're just playing around.)"
    show hiflmc bowling_cu sarcastic_cu
    "(JD always does.)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show jd casual basic at left2
    "At least I think so."
    show hiflmc bowling sarcastic
    "For as long as I've known JD, they've never become easier to read."
    hide hiflmc
    hide jd
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(I wonder what it would take for them open up to me.)"
    scene bg road_moon_fog at bg with fade
    stop music fadeout 1.0
    play music hiflsad
    pause
    show truck_back_night at bg
    show hiflmc bowling basic at right2:
        zoom 1.05
    show grace waitress basic at left2:
        zoom 1.05
    show truck_front_night at bg
    pause
    "After work, I pick up Grace from the diner."
    "She's a lot more quiet than usual, hands folded in her lap instead of playing with her phone."
    show hiflmc bowling sad
    mcjd "Bad day at work?"
    gr "Mm."
    "(It really must have been.)"
    "(I know Grace is the only waitress Luce keeps on regular payroll, so she gets all sorts depending on the time of day.)"
    show hiflmc bowling happy
    mcjd "I can make you some hot chocolate when we get home."
    mcjd "And maybe put on a show you like?"
    mcjd "I can leave the documentaries until you're in bed."
    show hiflmc bowling sad
    "Grace nods, and I spend the rest of the drive home trying to figure out what else I can do to cheer her up."
    "(If I had the spare cash, I'd order her something online, but things are really tight right now.)"
    scene bg mc_house_ext_moon_fog at bg with wipedown
    show grace waitress basic at left2
    show hiflmc bowling sad at right2
    "The uneasy silence holds as she and I get out of the truck,"
    show bg heroine_home_lights at bg
    "And I flick the lights on once we're through the front door."
    hide grace
    show hiflmc bowling sarcastic at centre
    "A casual sniff of my work uniform makes me cringe, and quickly becomes the first order of business."
    show hiflmc bowling happy
    mcjd "Let me change and I'll get that hot chocolate going, okay?"
    show hiflmc naked sad
    "Grace doesn't answer, so I sigh and start switching out my clothes."
    show hiflmc casual surprised at left2
    show grace waitress basic at right2
    "Once I feel a little less grunge, I turn around, but my sister hasn't moved from the doorway, standing stone still."
    mcjd "Grace, if something bad happened, you can tell me."
    show hiflmc casual sad
    mcjd "I'm always here to listen to you."
    mcjd "Maybe I'm not Mom, but..."
    gr "..."
    hide hiflmc
    hide grace
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    stop music fadeout 1.0
    play music hiflsuspense
    "(There's something wrong with her eyes.)"
    hide hiflmc
    show hiflmc casual surprised at right2
    show grace waitress basic at left2
    "With the lights on in here, it's painfully obvious."
    "A dark shadow swims behind Grace's gaze, and fear starts bubbling in my chest."
    show hiflmc casual sad
    mcjd "Hey."
    show grace waitress angry at left1
    "I reach out to touch Grace's face, but her hand snaps up to catch my wrist."
    show hiflmc casual surprised
    "The hold is tight enough to hurt, and I try to pull away from her with all my strength."
    mcjd "Grace, what are you doing?"
    show grace waitress angry behind hiflmc
    show hiflmc casual surprised at centre
    "She yanks me forward, and I stumble, pain spreading up my arm."
    "In a panic, I reach for the door latch behind her, swinging it outward."
    show bg mc_house_ext_moon_fog at bg
    hide grace
    "The impact is enough to break Grace's grip, and I sprint through the door and out into the yard."
    hide hiflmc
    show grace waitress basic at centre
    "It's almost pitch black out here, but the light in the house outlines her shape, turning towards me with the slow deliberation of a predator."
    hide grace
    $menuhideborder = True
    menu jds1e1c3:
        "A. Shout for her to stop.":
            $menuhideborder = False
            show hiflmc casual surprised at centre
            mcjd "Stop, okay!"
            mcjd "I don't know what happened, but this is really weird."
            mcjd "Talk to me."
            show hiflmc casual sad
            mcjd "Please talk to me."
        "B. Move further from Grace.":
            $menuhideborder = False
            show hiflmc casual sad at centre
            mcjd "Stay in the house."
            mcjd "Just stay."
            "I move backwards as fast as I can, closing the distance between me and my truck."
        "C. Call 911.":
            $menuhideborder = False
            show hiflmc casual sad at centre
            mcjd "I’m calling the sheriff if you don’t knock this off."
            "My fingers tremble as I try and get my phone out of my pocket."
            "As soon as I do, it slips out of my hands and onto the grass."
            mcjd "Shit."
    show hiflmc casual surprised at right3
    show grace waitress basic at left3
    "Grace keeps walking towards me, footsteps almost perfectly silent."
    play sound motorcycle_drive

    "Racking my brain for what to do to stop her, the sudden roar of a motorcycle engine cuts through my thoughts."
    hide grace
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(I know that bike.)"
    hide hiflmc
    #flame animations
    "Rubber burns on asphalt as both tires are forced to stop, and I turn just in time to see a halo of fire ignite from the street, blinding me."
    show hiflmc casual surprised at centre
    mcjd "What the-!"
    scene jd1 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 8 yanchor 0.1
    stop music fadeout 1.0
    play music jordandavies
    "Shaking the glare away from my vision, I follow the trail of flames upwards, and my jaw drops."

    "Hanging in the air above me is JD—at least, I think so."

    "Massive, blazing wings extend from their back, rippling with burnished color each time they beat against the air."

    "Fire wraps around JD like a cloak, the edges dripping heat down onto the street below."

    mcjd "Holy shit."

    "(Okay, maybe not so holy.)"

    "(They seem to have horns, which is definitely new.)"

    "Drawing an orb of fire into one hand, JD bounces it up off their palm with the ease of a baseball."

    jd "Hey, superfreak."

    jd "Take a step closer to [genericfn] and I'll blow you straight to Hell."

    "(What...what are they?)"

    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
