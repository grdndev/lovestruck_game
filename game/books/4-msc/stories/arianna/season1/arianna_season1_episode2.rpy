label arianna_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mc_bedroom_day at bg
    play music mscmctheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Something soft against my arm snaps me awake."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "What the fu-?!"
    show mscmc embarrassed_cu
    "(Oh right--Arianna!)"
    hide mscmc
    show arianna dress_cu sleep_cu at arianna_cu
    "Arianna is facing me, her eyes still closed as she moves her hand up towards her chin."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(I certainly wouldn't complain if this was my first sight every morning.)"
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna yawns and then blinks her eyes open, a tired smile on her face."
    ai "I'm so hungry."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Good morning to you too. Want to go eat?"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Yes please."
    show arianna dress sleep at centre:
        yoffset 100 alpha 0.5
        pause 0.1
        linear 0.5 yoffset 0 alpha 1.0
    "It takes Arianna a solid amount of time to be awake enough to get up, but she eventually does."

    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    scene bg msc_surf_shop_day at bg with wipeleftdissolve
    "When we head downstairs, Trina is unboxing a new set of swimsuits."
    show trina casual smile at centre
    so "Good morning, sunshine."
    hide trina
    show arianna dress grin at centre
    ai "Morning."
    hide arianna
    show trina casual sad at centre
    "Trina looks up confused and gasps."
    show trina casual smile at left2
    show arianna dress grin at right2
    so "Arianna? Hey, girl. What's, uh, all this about?"
    hide trina
    hide arianna

    $ menuhideborder = True
    menu ariannas1e2c1:
        "A. What's what?":
            $ menuhideborder = False
            show mscmc casual_hairdown embarrassed at left2
            show trina casual basic at right2
            mcarianna "What's what about?"
            hide trina
            show mscmc casual_hairdown_cu sleep_cu at mscmc_cu
            "(Not in front of Arianna, Trina. Please.)"
            show mscmc casual_hairdown smile at left2
            show trina casual smile at right2
            so "I don't know man, you tell me."
        "B. Arianna spent the night.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            "(We can get into this {i}later{/i}.)"
            show mscmc casual_hairdown grin at left2
            show arianna dress smile at right2
            mcarianna "Arianna spent the night."
            ai grin "Yep."
            hide mscmc
            hide arianna
            show trina casual smile at centre
            so "Mmhmm."
        "C. Trina...":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            "(All I can do is sigh.)"
            "(It's too early for this discussion.)"
            mcarianna sleep_cu "Trina..."

    show mscmc casual_hairdown grin at left2
    show trina casual basic at right2
    mcarianna "We're getting breakfast. Wanna come?"
    so smile "Don't need to ask me twice."

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    scene bg msc_beach_bar_day at bg with fade
    "As the three of us walk to Jerry's, Trina is uncomfortably quiet--though her narrowed eyes speak volumes."
    show trina casual basic at centre
    so "Seems like you two had a good night. Nice and cozy."
    hide trina
    show arianna dress grin at centre
    ai "It was! [genericfn] has the best pillows."
    hide arianna
    show trina casual basic at centre
    so "I'm surprised you slept over, Arianna. I had no idea you guys met up."
    show mscmc jacket_hairdown basic at left1plus
    show trina casual basic at right2
    "Trina turns to me as she says that with a very pointed look."
    mcarianna surprised "Yeah, she {i}called{/i} me and I figured I'd give her a place to stay."
    mcarianna basic "If it weren't for you, Arianna, Trina would've lost her shop. Right, Trina?"
    mcarianna smile "Arianna's done a lot for us, hasn't she?"
    show trina sleep
    "I can tell from the suddenly blank look on Trina's face that she's fighting not to roll her eyes, but I think she got the message."
    hide trina
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(She knows I'm right. Arianna saved the day last time she was here.)"
    "(Time to let it go that you think she ghosted me, Trina.)"

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    hide mscmc
    show trina casual smile at left2
    show arianna dress basic at right3
    "That blank look switches to one of acceptance as she smiles at Arianna."
    so "Yeah, honestly, I would've been screwed without you. Thanks."
    ai grin "Please, you don't need to give me that much credit. Everything worked out for all of us."
    ai "How has the shop been doing?"
    so "Pretty good. Business is stable and I got to hire a new surf instructor."
    ai "Oh, really?"
    hide trina
    show mscmc jacket_hairdown grin at left2
    show arianna smile
    mcarianna "Maxime. He's a chill guy."
    show mscmc smile
    ai grin "Is he as talented as you are?"
    mcarianna grin "He's pretty damn good and the kids all love him."
    hide mscmc
    show trina casual smile at left2
    show arianna smile
    so "Really quiet though. I couldn't tell you a thing about his personal life."
    ai grin "Maybe he just likes to keep things private."
    so "So long as he does his job, he could be a secret spy for all I care."
    ai "Well, it's nice to see your shop is thriving."
    show arianna basic
    so angry "Hamish is still a thorn in my side though."
    hide trina
    show mscmc jacket_hairdown sad at left2
    show arianna sad
    "Arianna grimaces as she catches my eye."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Yeah, Hamish definitely ruined a lot of things last time she was here.)"
    "(He's the one who made her decide to leave.)"
    show mscmc jacket_hairdown sad at left1plus
    show trina casual angry at right2
    so "Hamish keeps posting all these dumb things about my shop!"
    so "He's clogging up the reviews online."
    mcarianna "You'd think he has better things to do."
    show mscmc basic
    so "That man has literally nothing better to do. There's no doubt in my mind."
    show mscmc smile
    show trina sleep
    "Trina takes a long winded sip from her drink."
    show mscmc basic
    so smile "How long are you planning on staying in town, Arianna?"
    hide mscmc
    hide trina
    show arianna dress smile at centre
    ai "I'm not sure. Kind of in a, 'go with the flow' type state right now."
    hide arianna
    show mscmc jacket_hairdown surprised at left1plus
    show trina casual smile at right2
    so "Well, [genericfn] would looove it if you stuck around for a bit."
    hide trina
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Sometimes Trina is like an embarrassing parent!)"
    show mscmc jacket_hairdown smile at left1plus:
        pause 0.1
        easein 0.3 xoffset 60
    show trina casual sad at right2:
        pause 0.2
        easein_back 0.5 right3
    "I give Trina a well-deserved kick under the table."
    show mscmc grin
    so angry "Keep your hands and feet to yourself!"
    show trina smile
    mcarianna "Ignore her."
    hide mscmc
    hide trina
    show arianna dress grin at centre
    ai "I don't know if I want to."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    scene bg msc_boardwalk_sunset_people at bg with dissolve
    "When the sun starts to set, Arianna and I go for a stroll on the boardwalk."
    show arianna dress surprised at left1
    show mscmc jacket_hairdown basic at right1plus:
        xoffset 20
    ai "Can I say something kind of stupid?"
    show arianna grin
    mcarianna grin "Go for it."

    scene arianna_01_s1e2 at bg:
        align(0.5, 1.0)
    with fade
    show arianna_01_s1e2 at bg:
        transform_anchor True
        linear 4.0 align(0.5, 0.0) yoffset -50
    pause 4.0
    "Arianna puts her arm through mine and pulls me close to her side as she eagerly looks around the pier in excitement."
    ai "Walking around like this makes me feel like a human."
    mcarianna "Is that a good thing?"
    ai "I really like it on land. There's beer and new sights."
    ai "And some of the humans can be pretty cute."
    "(I've forgotten how to act in the face of zero subtlety.)"
    window hide
    show arianna_01_s1e2 at bg:
        transform_anchor True align(0.5, 0.0) yoffset -50
        linear 3.0 zoom .5 yoffset 0
    pause 3.0
    "I turn away from her with an awkward laugh as my chest buzzes."
    "(Arianna, you just might end up killing me.)"

    scene bg msc_boardwalk_sunset_people at bg
    show arianna dress grin at left1
    show mscmc jacket_hairdown smile at right1plus:
        xoffset 20
    with fade
    ai "I'm actually really excited about these commissions."
    mcarianna grin "Good, you should be."
    show mscmc basic
    ai sad "My people don't have a lot of respect for the arts like humans do."
    ai "Especially my kind of art--using discarded things for sculptures."
    show mscmc surprised
    ai "Our government sort of suppresses the arts."
    show mscmc smile
    ai smile "Maybe I should just spend more time on land."
    ai grin "I like it well enough and humans seem to take interest in my art, at least this Emporia person."
    show arianna smile
    mcarianna grin "There's plenty of room up here if you want to hang around."
    mcarianna "I think you should go where you'll be happy and feel appreciated."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I also wouldn't mind getting to see her more often.)"
    show arianna dress grin behind mscmc at left1:
        pause 0.1
        ease 0.3 left2
    show mscmc jacket_hairdown smile at right2:
        xoffset 20
    "Arianna smiles at me as she slips her arm from mine so that she can lean against the pier railing."
    ai smile "As much as I would love to see other parts of land, I don't think I could live just anywhere."
    ai grin "I would need to be on a beach--somewhere near the water."
    mcarianna grin "There's a lot of beaches."
    ai "Yeah."
    show arianna smile
    show mscmc smile
    "She stares out at the water, falling quiet."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Moving from living underwater to living on land would be a huge change.)"
    show mscmc sad_cu
    "(It's like moving to a completely different world.)"
    show arianna dress sad at left2 behind mscmc
    show mscmc jacket_hairdown smile at right2:
        xoffset 20
    "Arianna shrugs, throwing a hand up as she turns away from the waves."
    ai basic "But whatever. It's the only thing I've been able to think about all day."
    ai sad "It's starting to make my head hurt."
    show arianna smile
    "She points to something behind me and raises a brow in question."
    ai grin "What's that?"
    mcarianna grin "The mirror maze?"
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(That might be something fun to do with Arianna to take her mind off stuff.)"
    show arianna dress grin behind mscmc at left2
    show mscmc jacket_hairdown grin at right2:
        xoffset 20
    ai "A maze of mirrors?"
    mcarianna "Yeah, you don't have them?"
    ai "We have a reef maze, but I get the feeling it's very different."
    mcarianna "It's basically a walking puzzle. The walls are mirrors and glass so it's hard to figure out the right direction."
    mcarianna "The goal is to not get confused and to find your way back out."
    "Arianna gives me an excited grin."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Sounds fun--can we try it?"
    ai embarrassed_cu "I'll buy your ticket."
    "She winks at me."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(It would be a good way to distract her from her worries.)"
    "(Plus, showing her human things is always nice.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "So you wanna?"
    hide arianna

    $ menuhideborder = True
    menu ariannas1e2c2:
        "A. Navigate the mirror maze with Arianna!"(paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mscbeach fadein 1.0
            show arianna dress grin at left2
            show mscmc jacket_hairdown grin at right2:
                xoffset 20
            mcarianna "Why not? C'mon."
            hide arianna
            hide mscmc
            "I gesture towards the building and lead the way, Arianna happily beside me."
            show arianna dress grin at left1
            show mscmc jacket_hairdown grin at right2
            ai "Humans have such cool little places. It's all so exciting."
            mcarianna "You think a lot of stuff is exciting."
            show mscmc smile
            ai "Because it is! I bet you'd be saying the same thing if we were underwater."
            ai smile "I can still picture your face when I took you to my studio."
            mcarianna surprised "Well, that's...yeah, you're right."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I know for a fact that I would be constantly awestruck if I were in the mermaid city.)"
            "(Of course, I don't mind Arianna being so excited. It's really sweet actually.)"

            stop music fadeout 0.5
            play music mscaction fadein 1.0
            scene bg msc_mirror_maze_lightson at bg with dissolve
            "We go into the maze and are met with loud music and bright rainbow colored lights."
            show arianna dress surprised at left1plus
            show mscmc jacket_hairdown smile at right2
            "On all sides of us we're surrounded by reflections of ourselves."
            ai grin "This is more intense than I thought it'd be."
            "Arianna looks around with a laugh."
            show mscmc grin
            ai "There's so many of us. I don't want to lose you!"
            mcarianna embarrassed "I'll stick close."
            show mscmc grin:
                easein_back 0.4 right1plus
            show arianna:
                easein_back 0.4 left1
            "Arianna takes my hand and pulls me as she starts to move forward."
            show mscmc embarrassed
            ai "Just a preventative measure."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Mirror maze, thank you for your service.)"
            hide mscmc
            "We're met with an intersection that branches off into three paths."
            show arianna dress smile at left1
            show mscmc jacket_hairdown grin at right1plus
            mcarianna "Which way?"
            ai grin "Left!"
            mcarianna "Left it is."
            hide arianna
            hide mscmc
            "We take the left side, Arianna's hand tightening around mine as she laughs again."
            show arianna dress grin at left1
            show mscmc jacket_hairdown grin at right1plus
            ai "How long are these usually?"
            mcarianna "It depends on how often you get turned around."
            show mscmc smile
            ai "This is easy work for someone like me."
            show mscmc basic
            show arianna surprised:
                easein_back 0.3 left1plus
            "Arianna goes to turn again and bumps into a sneaky glass pane."
            show arianna sad
            mcarianna grin "Oh yeah, easy work. I can see you're a pro."
            ai angry "That's just cheap."
            show arianna smile
            show mscmc smile
            "She rubs at her shoulder that hit the glass and smirks at me."
            ai "You're the human here. Lead the way."
            mcarianna grin "I'm thinking...."
            hide arianna
            hide mscmc
            "I gently run my fingers along the mirrors as I walk, doing my best to not leave any finger smudges."
            "There's a real break in the wall."
            show arianna dress smile at left1plus
            show mscmc jacket_hairdown grin at right1plus
            mcarianna "This way."
            ai surprised "Isn't that cheating?"
            show arianna smile
            mcarianna "Would it be better if I ran into every wall like you?"
            ai grin "It was a delicate bump."
            show arianna smile
            mcarianna "Uh huh."
            hide arianna
            hide mscmc
            "We follow down the narrow path, watching ourselves walk alongside us."
            show arianna dress surprised at left1plus
            show mscmc jacket_hairdown smile at right1plus
            ai "Do you do these a lot?"
            mcarianna grin "Not at all. The last time I walked through one was a few years ago with Trina."
            show arianna smile
            mcarianna "Trina has the worst directinal sense I've ever seen."
            mcarianna "You're doing much better than she was."
            ai grin "Call it mermaid's intuition."
            hide arianna
            hide mscmc
            "The path opens up into a large room with the music playing much louder."
            show arianna dress grin at left1plus
            show mscmc jacket_hairdown grin at right1plus
            ai "Oooo, the party room!"
            ai "This music isn't half bad either."
            mcarianna "Really, you like the music?"
            hide mscmc
            show arianna at centre:
                easein 0.3 xoffset 5
                block:
                    easein 0.6 xoffset -5
                    easein 0.6 xoffset 5
                    repeat
            "Arianna lets go of my hand and starts nodding her head to the beat."
            ai "Kinda makes me want to dance."
            hide arianna
            show mscmc jacket_hairdown smile at centre
            mcarianna "I don't think staying in the maze is the goal."
            hide mscmc
            show arianna dress grin at centre:
                pause 0.1
                easein 0.3 xoffset 5
                block:
                    easein 0.6 xoffset -5
                    easein 0.6 xoffset 5
                    repeat
            ai "It could be."
            show arianna dress grin at left3:
                xpos 300
                pause 0.3
                block:
                    ease 0.8 xpos 740 knot 280 knot 760 knot 740
                    pause 0.3
                    ease 0.8 xpos 300 knot 760 knot 280 knot 300
                    pause 0.3
                    repeat
            show mscmc jacket_hairdown smile at centre
            "Arianna starts dancing around me with the most cheesy clumsy moves she can muster."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "You know you want to."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Alright, alright."
            show mscmc jacket_hairdown smile at centre:
                easein 0.4 yoffset -12
                easein 0.4 yoffset 0
                easein 0.2 yoffset -6
                easein 0.2 yoffset 0
                repeat
            "I start slowly at first, opting for a basic bobbing dance."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                yoffset 0
            "(It would be a little embarrassing if someone else walked in here.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "You're barely dancing!"
            hide arianna
            "Arianna takes my hand again and spins me around."
            show arianna dress_cu grin_cu at arianna_cu
            ai "That's more like it."
            hide arianna
            "She takes my other hand and sways our arms as she dances us around the room."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Arianna is hard to resist.)"
            show mscmc jacket_hairdown grin at left2:
                easein 0.2 yoffset -10
                pause 0.1
                block:
                    easein 0.6 yoffset 4
                    easein 0.6 yoffset -10
                    repeat
            show arianna dress grin at right2:
                easein 0.2 yoffset -8
                pause 0.1
                block:
                    easein 0.5 yoffset 2
                    easein 0.5 yoffset -6
                    repeat
            "I crack and Arianna shouts a cheer as I start getting into it."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu:
                yoffset 0
            mcarianna "This what you wanted?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "It's all I ever wanted!"
            hide arianna
            "We dance until we both have sweat beading on our foreheads."
            show arianna dress grin at left1plus
            show mscmc jacket_hairdown grin at right1plus
            ai "Okay, now then, let's beat this maze."
            hide arianna
            hide mscmc
            "Arianna is surprisingly quick at finding the right paths and turns this time."

            stop music fadeout 0.5
            play music mscbeach fadein 1.0
            scene bg msc_boardwalk_sunset_people at bg with dissolve
            "We navigate the maze with hands held until we finally break out into the exit."
            show arianna dress grin at left1plus
            show mscmc jacket_hairdown smile at right1plus
            ai "We did it!"
            mcarianna grin "Congrats on your first mirror maze."
            ai "This human stuff isn't too hard."
            mcarianna "Wait until you get on a rollercoaster. That'll blow your mind, I bet."
            hide mscmc
            hide arianna
            "We look out at the sun starting to lower above the water."

            stop music fadeout 0.5
            play music mschappytimes fadein 1.0
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(That was a lot of fun, but we should talk business for a minute.)"
            show arianna dress basic at left1plus
            show mscmc jacket_hairdown basic at right1plus
            mcarianna "Should we call Emporia?"
            ai surprised "Right now?"
            mcarianna smile "The sooner the better."
            show arianna sad
            "Arianna blows out an anxious breath."
            ai basic "You're right. The sooner the better."

        "B. Say no.":
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mschappytimes fadein 1.0
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(But, it's getting late and we still have some things we need to do.)"
            show arianna dress basic behind mscmc at left2
            show mscmc jacket_hairdown basic at right2:
                xoffset 20
            mcarianna "I don't think we really have time."
            ai sad "Awwwww, why not?"
            mcarianna sad "I'm sorry, I just think we need to call Emporia--set up a meeting and stuff."
            show mscmc basic
            ai smile "I know you're right, I just wanted to explore some human stuff."
            show arianna basic
            mcarianna "There'll be time later, okay?"
            show mscmc sad
            "Arianna blows out an exaggerated breath."
            show mscmc smile
            ai smile "Okay."

    scene bg msc_beach_bar_sunset at bg with fade
    "Arianna and I leave the pier and go to the beach bar to make our call."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown grin at left1
    mcarianna "Don't worry so much about it. You were excited!"
    ai smile "I know, it's just...it's my first time doing this kind of thing."
    show mscmc surprised
    "Arianna looks down at her hands as she picks at her nails."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I feel bad seeing her so anxious over this. It'll be good for her though.)"
    mcarianna grin_cu "Hey, you're not gonna be alone through it. I'll be here the whole way."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna's eyes meet mine and I feel like I'm rooted to the spot."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Her eyes are like a cloudy sky or maybe the moon.)"
    show mscmc surprised_cu
    "(Focus, brain!)"
    show arianna dress basic at right1plus behind mscmc
    show mscmc jacket_hairdown smile at left1
    mcarianna "Do you have the number Trina gave you?"
    show mscmc surprised
    ai sad "Yeah, but I don't think I can call her."
    mcarianna grin "Yes, you can. It'll be okay."
    show mscmc basic
    ai smile "No, I mean my shellphone can't connect to human phones. I really can't do it."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Ah, the shellphone.)"
    show arianna dress basic at right1plus behind mscmc
    show mscmc jacket_hairdown grin at left1
    mcarianna "Give the number here--I can do it. The power of human cellphones."
    ai surprised "{i}Cell{/i}phone?"
    mcarianna "Cellular."
    show mscmc smile
    show arianna smile
    "Arianna makes a hum of thought as she passes me a crumpled paper."
    show arianna:
        easein 0.4 centre xoffset 34
    "I type in the number and Arianna leans in to listen, her hair tickling my hand."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's so close to me.)"

    hide mscmc
    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    "Nasally Voice" "Emporia Lid's phone. This is her assistant, who am I speaking with?"
    show arianna dress smile at right1
    show mscmc jacket_hairdown grin at left1
    mcarianna "Hi, my name is [genericfn], can I speak with Emporia?"
    hide mscmc
    hide arianna
    "Emporia's Assistant" "For what purpose?"
    show arianna dress smile at right1
    show mscmc jacket_hairdown grin at left1
    mcarianna "I'm here with Arianna Nitida and we're calling about Emporia's art commission request."
    show arianna grin
    "Arianna nods as I speak."
    hide mscmc
    hide arianna
    "Emporia's Assistant" "One moment."
    "There's a click, silence, and then another click that brings a new voice."
    bn "This is Emporia Lid speaking."
    show arianna dress smile at right1
    show mscmc jacket_hairdown grin at left1
    mcarianna "Hi, my name's [genericfn] [genericln]. I'm Arianna's manager."
    hide arianna
    hide mscmc
    "The line goes quiet and I look at Arianna with a frown."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Did she hang up already?)"
    hide mscmc
    bn "Manager? I thought I would be speaking directly with Arianna."
    show arianna dress smile at right1
    show mscmc jacket_hairdown grin at left1
    mcarianna "Yes well, I handle all of her scheduling. She's a very busy woman these days."
    hide arianna
    hide mscmc
    bn "Too busy to even give me a call herself? Isn't that poor business?"
    bn "How am I to settle the commission when I haven't even spoken to the artist?"
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(She sounds weirdly pissed off about speaking to a manager for someone who had an assistant answer the phone for her.)"
    show arianna dress surprised at right1 behind mscmc
    show mscmc jacket_hairdown basic at left1
    "I can tell by Arianna's confused face that she's thinking the same thing."
    hide arianna
    hide mscmc
    bn "Well, no matter. I would like to set up a meeting in person with the artist to discuss it."
    bn "I would like to commission three sculpture pieces."
    show arianna dress basic at right1
    show mscmc jacket_hairdown grin at left1
    mcarianna "Arianna will be free around noon tomorrow if you'd be available then."
    mcarianna "One in the afternoon, maybe?"
    hide arianna
    hide mscmc
    bn "I'll clear my schedule."
    bn "Will Arianna be coming to the meeting alone or will you accompany her?"
    show arianna dress basic at right1
    show mscmc jacket_hairdown sad at left1
    "The tone of her voice causes a weird pit to form in my stomach."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Why does she sound weird about meeting Arianna? Are these sculptures that big of a deal?)"
    show arianna dress smile at right1 behind mscmc
    show mscmc jacket_hairdown basic at left1
    mcarianna "As her manager, I will be accompanying her."
    show arianna basic
    "Another long silence."
    hide mscmc
    hide arianna


    $ menuhideborder = True
    menu ariannas1e2c3:
        "A. Wait the silence out.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(These weird silences seem to be Emporia's thing.)"
            "(Is she just thinking it over or...?)"
            show mscmc jacket_hairdown basic at left1
            show arianna dress basic at right1 behind mscmc
            "I wait it out until I hear a sharp breath from the other end."
        "B. Say something.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
            "(What is with this woman?)"
            show mscmc jacket_hairdown surprised at left1
            show arianna dress sad at right1 behind mscmc
            mcarianna "Does that work?"
            hide mscmc
            hide arianna
            "There's no reply."
        "C. Look at Arianna.":
            $ menuhideborder = False
            show mscmc jacket_hairdown basic at left1
            show arianna dress sad at right1 behind mscmc
            "I glance at Arianna and she shrugs."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(We're both confused over this bizarre phone call.)"
            "(And Emporia had that audacity to come for Arianna's business ethic.)"

    hide mscmc
    hide arianna
    bn "Very well then."
    show arianna dress basic at right1
    show mscmc jacket_hairdown basic at left1
    "I take my phone from my ear and look at it as a click indicates Emporia has hung up."
    mcarianna surprised "She hung up."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Emporia was kinda rude, wasn't she?)"
    show arianna dress grin at right2 behind mscmc
    show mscmc jacket_hairdown basic at left1plus
    "Arianna looks nothing but pleased as she squirms in her seat."
    show mscmc smile
    ai "This is so awesome! I feel like a real artist!"
    mcarianna grin "You are a real artist, Arianna. Commissions or not."
    show mscmc smile
    ai "But this is a job, [genericfn]! Emporia wants three pieces from me."
    ai "That's huge."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I don't want to bring Arianna's mood down by talking about how odd Emporia sounded, but...)"
    show mscmc angry_cu
    "(Why was she acting like that?)"
    show mscmc sleep_cu
    "I do my best to ignore the growing pit in my stomach."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
