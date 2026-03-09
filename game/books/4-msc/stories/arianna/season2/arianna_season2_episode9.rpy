label arianna_season2_episode9:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_beach_bar_night_lights at bg
    play music mscromanceconfession

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna leans forward, her lips almost to mine before she stops, and shifts her gaze to look into my eyes."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Kiss me. Kiss me. Kiss me.)"
    "The ruckus of the bar is muted by the pounding of my heart in my ears."
    hide mscmc
    show arianna dress_cu smile_cu at truecenter:
        transform_anchor True anchor (0.5, 0.43)
    pause 0.4
    show arianna sleep_cu with Dissolve(0.4):
        transform_anchor True anchor (0.5, 0.43)
        pause 0.4
        linear 0.5 zoom 1.08 alpha 0.0
    "Finally, she presses her petal soft lips to mine and its like we're the only two people in the world."
    "It's slow and sweet, she tastes like nectar."
    "Then Arianna's hand is on my cheek until herhand cups the back of my neck, pulling me in deeper."
    "The desperation of waiting for so long seeps between our lips and breath."
    "Arianna gasps into my mouth and her tongue teases mine."
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "I stand and move in between her legs as she sits on the bar stool and we continue to exchange kisses."
    hide mscmc
    show arianna embarrassed_cu:
        transform_anchor True anchor (0.5, 0.43)
        linear 0.5 zoom 1.0 alpha 1.0
    "Our breath mingles as we part, panting."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(We kissed. We actually kissed. And it was perfect.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna dress_cu basic_cu at arianna_cu
    ai "I'm sorry."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "Arianna's brows furrow and my heart sinks as confusion settles over me."
    mcarianna "Huh?"
    "(This is something we've both been wanting.)"
    show mscmc jacket_hairdown surprised at left1
    show arianna dress basic at right1 behind mscmc
    "She shakes her head and stands, looking off towards the water."
    show arianna sleep
    mcarianna "What...?"
    show arianna sad:
        pause 0.3
        parallel:
            linear 0.4 alpha 0.0
        parallel:
            easein 0.4 xoffset 100
    "Arianna looks at me, her eyes heavy with pain until she turns and walks towards the beach."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She's the one who kissed me... What's going on?)"
    hide mscmc
    "The music feels too loud for the first time that night as I cash out our drinks and pay."

    stop music fadeout 0.5
    play music mscpassionateromance fadein 1.0
    scene bg msc_labeach_night at bg with dissolve
    "My stomach is in knots as I walk onto the beach to see Arianna sitting in the sand a little ways away with her knees to her chest."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I want to give her space if she needs it but I also just want to make sure she's ok.)"
    show mscmc jacket_hairdown sad at left1plus
    show arianna dress sad at right1plus
    mcarianna "Is it ok if I sit with you? I don't have to, just want to make sure you're alright."
    show arianna smile
    "Arianna looks over her shoulder at me with a sad smile."
    ai "Of course you can sit. I want you to, even."
    show arianna sleep
    show mscmc surprised:
        pause 0.2
        easein 0.4 left1
    "I sit beside her with my legs crossed and rubbing my hands together."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I can't rememeber the last time I was this nervous talking to her.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress surprised at right1plus
    mcarianna "Um...did I do something?"
    show arianna sad
    "It feels like my heart is in my throat."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Have I been misreading everything?)"
    show mscmc jacket_hairdown surprised at left1
    show arianna dress sad at right1plus
    ai "You didn't do anything wrong."
    show mscmc embarrassed
    ai smile "Kissing you was amazing and...way better than I imagined..."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She {i}did{/i} want to kiss me.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress embarrassed at right1plus
    "She smiles briefly, a hint of a blush there until she frowns and shakes her head."
    show mscmc sad
    ai sad "It's my fault, I shouldn't have kissed you. We can't...cross that line."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(We both have feelings for each other. Don't we?)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress sad at right1plus
    mcarianna "Why not?"
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Everything between us feels so right, I don't understand.)"
    show mscmc jacket_hairdown surprised at left1
    show arianna dress basic at right1plus
    ai "I, I...can't do a relationship right now."
    ai sad "My past relationships, whatever, weren't like this, weren't like you...but, and you do, you mean so much to me."
    show mscmc smile
    ai "I mainly just hookup with people and then never see them again. It just keeps things convenient, I guess."
    show mscmc embarrassed
    ai "But how I feel about you..."
    show arianna sleep
    "Arianna sets her chin on her knees."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(She's scared of taking the next step.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress surprised at right1plus
    mcarianna "What are you afraid of?"
    show mscmc sad
    ai sad "A lot of people who claim to care want to change me or want me to change. It feels like people end up wanting me to be less me."
    ai "Not just in relationships, but my family, except Queenie. My parents don't talk to me right now."
    show arianna smile
    "Arianna laughs ruefully but her frown returns quickly."
    ai basic "I know you don't want to change me now. You're different and accepting."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I'm glad she knows I think she's amazing just the way she is.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress sleep at right1plus
    ai "My mom thinks I'll settle down in the right relationship, but I don't want that."
    ai surprised "I never want either of us to end up feeling caged by the other."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She's not ready for a relationship in her life right now. I understand.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress sad at right1plus
    "I let out a sigh, tonight's been a rollercoaster. My hands rest in the sand near Arianna's and I try not to think about the feel of her fingers."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I don't know how I feel right now, just kind of sad I guess, but also glad that we're moving forward with whatever we are.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress surprised at right1plus
    mcarianna "You mean a lot to me too. I don't want you to feel pressure to be someone you're not."
    show mscmc sad
    ai basic "I don't want to lose you. In relationships, people end up resenting one another."
    show mscmc basic
    show arianna sleep
    "Arianna sighs, her eyes focused on the waves."
    show mscmc smile
    ai "I'm sorry if I led you on. I do really like you, I just, I need to work through some of my own shit..."
    show mscmc surprised
    ai sad "I can't be your girlfriend right now, not the girlfriend you deserve, and I understand if you don't want to be friends anymore."
    "Arianna's voice hitches and she turns her head away from me."
    hide mscmc
    hide arianna

    $ menuhideborder = True
    menu ariannas2e9c1:
        "A. It's okay, all is good.":
            $ menuhideborder = False
            show mscmc jacket_hairdown grin at left1
            show arianna dress surprised at right1plus
            mcarianna "Hey...it's okay."
            show arianna smile
            mcarianna smile "Take the time you need. I'll be here."

        "B. I'll be whatever you need right now.":
            $ menuhideborder = False
            show mscmc jacket_hairdown smile at left1
            show arianna dress surprised at right1plus
            mcarianna "Then, I'll be whatever you need right now."
            mcarianna grin "We don't need to change anything about us. We're good."

        "C. You really think I'd stop being your friend?":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I never want to lose her—I don't need her to be my girlfriend, I just want her in my life.)"
            show mscmc jacket_hairdown grin at left1
            show arianna dress surprised at right1plus
            mcarianna "Do you really think I'd stop being your friend?"
            show arianna smile
            mcarianna smile "You can't get rid of me at this point. I'll always be your friend."

    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(My heart hurts but there's also a little hope in it.)"
    show arianna dress grin at right1plus behind mscmc
    show mscmc jacket_hairdown grin at left1
    ai "You're so important to me, I hope you know that."
    show arianna sad
    mcarianna smile "I do know it. Thank you for being honest with me."
    show arianna:
        easein_back 0.4 centre
    show mscmc surprised:
        pause 0.1
        easein_back 0.4 left1plus
    "Arianna throws her arms around me in a tight hug."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    ai "Thank you."
    hide arianna
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "We stay there on the beach, holding on to each other in silence as the waves lap at the shore, and my heart feels heavy."

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with fade
    "Our walk back to my room is quieter than usual, neither of us saying much."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(Regardless of where we stand romantically, I want to be in her life and I want her in mine if she wants that too.)"
    show mscmc sad_cu
    "(But I was technically just rejected, right?)"
    show mscmc casual_hairdown basic at left1plus
    show arianna dress basic at right2 behind mscmc
    "Arianna clears her throat and sits on the very edge of the bed."
    show mscmc smile
    ai smile "Tomorrow's the big day. The resistance is gonna be {i}public{/i} public."
    "Her voice is nonchalant and I appreciate her trying to lighten the mood."
    hide arianna
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(I can do this, I can just be her close friend.)"
    show mscmc casual_hairdown grin at left1plus
    show arianna dress smile at right2 behind mscmc
    mcarianna "Yeah, do you think the resistance has already set the sculpture up in the square in Maritas?"
    show mscmc smile
    ai basic "They'll probably wait a few more hours. They can't do it if anyone's around so we usually set up our projects dead of night."
    show mscmc basic
    show arianna sad
    "I sit on the other side of the bed and Arianna glances over at me before looking away."
    show arianna basic
    mcarianna smile "It's a big deal, a serious accomplishment."
    show mscmc embarrassed
    ai smile "It is. This is like a real step towards significant change. And we did it together, that means a lot to me."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna meets my eyes and holds my gaze for the first time since our talk on the beach."
    hide arianna
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    mcarianna "Yeah. We did. Thanks for trusting me with your world."
    show mscmc casual_hairdown surprised at left1plus
    show arianna dress smile at right2 behind mscmc:
        xoffset 100 alpha 0.0
        pause 0.1
        parallel:
            easein 0.5 xoffset 0
        parallel:
            linear 0.5 alpha 1.0
    "Arianna breaks eye contact as she reaches into her bag by the bed and pulls out a comically big container of shea butter."
    show arianna surprised
    mcarianna "That's a lotta butter!"
    show mscmc grin
    ai "When merpeople are on land for extended periods of time, ok don't laugh, our skin gets really dry!"
    show arianna grin
    "I can't help but let a little laugh escape and Arianna smiles at me."
    ai sleep "It's true! I'm so freaking dry right now."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Things don't feel as bad now that we're joking around with each other again.)"
    show mscmc casual_hairdown basic at left1plus
    show arianna dress smile at right2 behind mscmc
    "Arianna opens the lid and delicately scoops out some shea butter. She spreads it up her arms, pushing back the sleeves of her dress."
    show mscmc sleep
    "Her hands are dainty but strong and they move with purpose over her pearly, smooth skin."
    show mscmc surprised
    "I look away when I realize I'm staring."
    show mscmc sad
    ai grin "Oh my god this feels amazing."
    mcarianna basic "Cool, cool, cool."
    show mscmc smile
    "Arianna offers the shea butter to me."
    ai "Here, want some?"
    mcarianna basic "Sure."
    hide mscmc
    hide arianna
    "I spread some across my shoulders and think I feel Arianna's eyes on me but when I look up she's looking away."
    show arianna dress sad at right2
    show mscmc casual_hairdown surprised at left1plus
    "Arianna straightens up as if debating saying something. I stay quiet and let her decide if she wants to say what's on her mind."
    show mscmc basic
    ai smile "Hey..., can I ask you something?"
    mcarianna smile "Ask away."
    show arianna grin
    "Arianna laughs, but there's a blush on her cheeks."
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Oh?)"
    show mscmc casual_hairdown surprised at left1plus
    show arianna dress embarrassed at right2 behind mscmc
    ai "Okay, let me know if this isn't like...something friends do, or you just don't want to because I would understand."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's trying to make sure I'm comfortable and ok. Which is funny cause I just want her to be comfortable and ok.)"
    show mscmc casual_hairdown grin at left1plus
    show arianna dress smile at right2 behind mscmc
    mcarianna "What's up?"
    show mscmc surprised
    ai sad "Well, it's kind of hard to reach my back and I wouldn't ask but my skin is so freaking dry right now."
    show mscmc grin
    show arianna basic
    "She watches my face to see my reaction as she talks."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(I think I can handle putting shea butter on her in a friend way, yeah, I got this.)"
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    "Arianna fiddles with the sleeve of her dress and laughs again."
    ai "I'd...you know...need to take my dress down a bit, it's really my whole back."
    ai smile_cu "Again, you can so no, but, I wouldn't ask if I didn't really want this. Will you?"
    hide arianna

    $ menuhideborder = True
    menu ariannas2e9c2:
        "A. Spread shea butter on Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(Sure. Totally. I've done this with friends. We're good.)"
            show mscmc casual_hairdown smile at left1plus
            show arianna dress grin at right2
            mcarianna "I don't want your back to suffer so I guess this is what friends are for."
            mcarianna embarrassed "We're just good...chums. Pals. Buds. Bros."
            show arianna smile
            mcarianna "I do this for a lot of friends. Friend code, you know."
            hide arianna
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(I'm blabbering, oh god, I should shut up.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna pulls her dress down her shoulders and it falls away to reveal the elegant curve of her back as she holds it up in front."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "My eyes follow the dress down but I tear them away as soon as I realize and plaster them on the far wall."
            show mscmc basic_cu
            "(Stop staring! Only staring in a friends way!)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "But it's hard to look away from how the muscles in her back move as she straightens her posture and shakes back her hair from her face."
            ai "I really owe you one. My skin is crying, or it would be if it had any moisture at all in it."
            show arianna embarrassed_cu
            "With her dress hanging partway off, Arianna glances back over her shoulder at me."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(She is so crazy beautiful.)"
            "My mouth feels dry as I swallow hard."
            mcarianna basic_cu "You can lay down if you want."
            hide mscmc
            "Arianna stretches out onto her stomach and props herself up on her elbows."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(I am not thinking about the fact that she is gorgeous.)"
            show arianna dress smile at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown smile at right4:
                xoffset 20
            ai "I know this is a strange request, but thanks. Seriously."
            show arianna basic
            mcarianna grin "Nah, it's not strange. I put sunscreen on Trina's back. I get it."
            show arianna grin
            mcarianna smile "Arms were not designed to reach every part of our bodies. Which I think is a flaw."
            show mscmc:
                easein 0.5 right1 xoffset 20
            "I take some shea butter into my hand and sit on the bed next to Arianna."
            hide arianna
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu:
                xoffset 0
            "(Why does she have such a nice back?)"
            show arianna dress grin at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown smile at right1:
                xoffset 20
            ai "How are you feeling, buddy?"
            show arianna embarrassed
            mcarianna grin "Completely friendly, my guy."
            show mscmc embarrassed
            ai "Cool. Me too."
            hide arianna
            hide mscmc
            "I place my hands on Arianna's back. Her skin is cool and just as soft as I expected. If it's dry I can't tell."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "My cheeks burn as I run my hands over her back and sides but I tell myself it's because I got too much sun today."
            show mscmc basic_cu
            "(It's definitely {i}not{/i} because of how sensual this all is.)"
            show arianna dress grin at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown smile at right1:
                xoffset 20
            "As I start to rub my hands over Arianna's lower ribs, she giggles."
            show mscmc embarrassed
            ai smile "You can press a bit harder, I really want it to soak in."
            show arianna sleep
            "So do I. My hands run up and down the length of her torso and over her shoulder blades."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(It's just a back. I've seen loads of backs.)"
            show arianna dress embarrassed at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown smile at right1:
                xoffset 20
            mcarianna "Do mers ask their friends to get their back?"
            show arianna grin
            "Arianna laughs again."
            show mscmc grin
            ai "I would only ask a close friend."
            mcarianna "Honored that position is mine."
            show mscmc embarrassed
            ai "It always will be."
            hide arianna
            hide mscmc
            "I rub my hands down to the small of Arianna's back and she moans very quietly, breathy and drawn out."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(Do. Not. Swoon.)"
            show arianna dress embarrassed at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown embarrassed at right1:
                xoffset 20
            ai "Sorry, it just...it does feel really good."
            show mscmc grin
            "Arianna puts her hands over her face and laughs."
            hide arianna
            show mscmc casual_hairdown_cu sleep_cu at mscmc_cu:
                xoffset 0
            "(Man, this isn't like putting sunscreen on Trina's back at all.)"
            show arianna dress smile at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown embarrassed at right1:
                xoffset 20
            mcarianna "I never thought about your skin getting dry being on land."
            show mscmc smile
            ai grin "It's not a problem most merpeople have to deal with considering most don't come to land, but yeah, it is dry up here."
            show mscmc embarrassed
            "My hand moves over the outward curve of her hip and Arianna squirms and laughs."
            show mscmc grin
            ai "I'm ticklish!"
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Of course she is, she's already the cutest ever so of course she's also ticklish, which just makes her even cuter.)"
            show arianna dress grin at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown grin at right1:
                xoffset 20
            mcarianna "What a small price to pay for a well hydrated back."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Though, her back is already sooo smooth. And soft. And toned.)"
            show arianna dress smile at centre:
                yoffset 80 xoffset -70
            show mscmc casual_hairdown basic at right1:
                xoffset 20
            mcarianna "Alright, all done."
            show mscmc grin
            ai grin "I feel so much better. Ugh, thank you so much. I felt like I was going to turn into a dried fish."
            show arianna:
                easein_back 0.4 yoffset 0
            show mscmc smile
            "Arianna pushes herself up and pulls her dress back over her shoulders."

        "B. Sorry,  but no.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(Touching Arianna's bare back? Yeah, I can't handle that tonight.)"
            show mscmc casual_hairdown smile at left1plus
            show arianna dress smile at right1plus behind mscmc
            mcarianna "Uh...yeah, I don't think I can do that for you."
            show mscmc grin
            show arianna grin
            "I laugh and so does Arianna, but there's something left unsaid in the air between us."
            hide arianna
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(My heart just can't take it right now.)"
            show mscmc casual_hairdown basic at left1plus
            show arianna dress embarrassed at right1plus behind mscmc
            ai "Yeah. Of course. Silly of me to ask, really."
            show arianna smile
            mcarianna sad "Will your back be okay?"
            show mscmc grin
            ai grin "My back will survive!"

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    scene bg msc_mc_bedroom_night at bg with dissolve
    "As I turn off the light, Arianna is noticeably further over on her side than usual."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(We're friends. It's not weird.)"
    "I turn onto my side and close my eyes to try and drift off."
    show mscmc casual_hairdown sleep at left1plus
    show arianna dress sleep at right3 behind mscmc
    ai "I don't know if I'm gonna be able to sleep tonight thinking about the sculpture going live."
    show arianna smile
    mcarianna smile "Tomorrow will be exciting."
    show arianna sleep
    "I hear her breathing fall into a pattern after a little while, I'm glad she's able to sleep after all."
    hide arianna
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "I just keep replaying our conversation on the beach in my head over and over."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    scene bg msc_arianna_studio_day at bg with fade
    "It's a restless night, but in the morning Arianna and I race over to her studio to turn on the mer news."
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(Awkward friend stuff aside, this is a big day! All of our hard work is going public and mer people will have some access to magic!)"
    show arianna siren grin at right2 behind mscmc
    show mscmc bikini_hairup smile at left1
    "Arianna pulls out a small TV that was stashed under a work table and sets it up in the corner."
    mcarianna grin "Oh wow, your TV looks just like mine."
    ai "Right? I was shocked too."
    hide mscmc
    hide arianna
    "Arianna and I sit in front of it as she switches on the news."
    show arianna siren grin at right2 behind mscmc
    show mscmc bikini_hairup smile at left1plus
    ai "This is it!"
    show arianna:
        easein_back 0.5 right1 xoffset 20
    show mscmc grin:
        pause 0.1
        easein 0.2 xoffset -20
        easein 0.2 xoffset 0
    "Arianna bumps me and grins. Her eager anticipation is contagious."
    hide arianna
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(Not only is it a step for the resistance, but this is a piece Arianna made and planned!)"
    "(It must be exciting to know her work is gonna affect so many and change lives.)"
    hide mscmc
    "A coiffed mermaid on the screen reads off the weather reports as headlines scroll across the bottom of the screen."
    "Newscaster" "And later today, there's going to be-"
    "The anchor stops and puts a hand to her ear, nodding."
    "Newscaster" "Pardon me, but it seems we're getting some breaking news."
    show arianna siren grin at right2
    show mscmc bikini_hairup grin at left1
    "Arianna nudges her tail against me looking like she can barely contain herself."
    hide arianna
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(Oh shit! This is it!)"

    stop music fadeout 0.5
    play music mscaction fadein 1.0
    show arianna siren grin at right2 behind mscmc
    show mscmc bikini_hairup grin at left1
    ai "This is us! It has to be us!"
    hide arianna
    hide mscmc
    "Newscaster" "It appears that an illegal art piece has appeared in the central square!"
    "Newscaster" "The perpetrators are thought to be the active art resistance."
    "Newscaster" "We are getting live footage from the area now."
    "The screen flashes to the central square and there in the middle is the serpent with its scales glistening!"
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(I swell with pride. It feels good to be part of something bigger than myself.)"
    hide mscmc
    "The camera circles around the serpent as merpeople swim around it in awe."
    show arianna siren grin at right2
    show mscmc bikini_hairup grin at left1
    mcarianna "It looks awesome!"
    ai "We did that! How cool is that?"
    hide arianna
    hide mscmc
    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    "The camera goes around to the front of the sculpture which seems to have something draped over its face. A banner of some sort?"
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(Did the resistance add that after they brought it there? I don't remember anyone mentioning it.)"
    show arianna siren angry at right2 behind mscmc
    show mscmc bikini_hairup surprised at left1
    "Arianna tenses beside me and when I look over I see her glaring at the screen, her hands are balled into fists and her breathing shallow."
    mcarianna sad "What is it?"
    hide arianna
    hide mscmc
    "I look back at the news as the camera zooms in on the banner."
    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    "Words are scrawled on it, and I squint at the screen, the banner reads, \"We sentence the government tyrants to death.\""
    show arianna siren angry at right2
    show mscmc bikini_hairup sad at left1
    ai "I knew we shouldn't trust him."
    mcarianna surprised "Who?"
    show mscmc sad
    ai "Casper"
    hide arianna
    hide mscmc
    "There's more written underneath the main bold slogan in smaller script."
    "I read Casper, Arianna, and Queenie's full names, it's been made to look like they all signed this death threat."
    show mscmc bikini_hairup_cu sad_cu at mscmc_cu
    "(Casper, why?)"
    show arianna siren angry at right2 behind mscmc
    show mscmc bikini_hairup sad at left1
    mcarianna "I thought he wanted to help."
    mcarianna "You told him specifically why the resistance was staying anonymous. I can't believe he did this."

    show arianna:
        linear 0.5 xoffset 100 alpha 0.0
    "Arianna springs into action and grabs a bag from a shelf and starts filling it with stuff from around the studio."
    hide arianna
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    ai "We need to go. This place isn't safe anymore."
    hide arianna

    $ menuhideborder = True
    menu ariannas2e9c3:
        "A. Ask her what she's doing.":
            $ menuhideborder = False
            show arianna siren angry at right2
            show mscmc bikini_hairup basic at left1
            mcarianna "What're you doing?"
            show mscmc sad
            ai basic "Packing. We can't leave some of this stuff."
        "B. Why?":
            $ menuhideborder = False
            show arianna siren angry at right2
            show mscmc bikini_hairup sad at left1
            mcarianna "Why? Do you really think they'd come here?"
            ai "Maxime already showed up once asking about this place."
            show mscmc surprised
            ai "They know I work out of here."

        "C. Watch the news in disbelief.":
            $ menuhideborder = False
            "I turn back to the screen and watch as the camera pans out again, the banner hanging over the statue's eyes."
            show arianna siren angry at right2
            show mscmc bikini_hairup sad at left1
            mcarianna "Oh shit."
            ai "Yeah, oh shit."


    hide mscmc
    hide arianna
    "Arianna starts stuffing leftover scales and anything related to the piece into her bag, she looks up at me and smiles sadly."
    show mscmc bikini_hairup_cu sad_cu at mscmc_cu
    "(We need to get out of here. This is not how I thought today was going to go.)"
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    ai "It would've taken the government a few days to take the sculpture down 'cause they wouldn't have detected the magic, if not for this."
    show mscmc bikini_hairup sad at left1 behind arianna
    show arianna siren smile at right1plus
    "Arianna closes the bag and throws it over her shoulder as she looks back at me, motioning towards the exit."
    hide arianna
    show mscmc bikini_hairup_cu sad_cu at mscmc_cu
    "(The government is going to come after Arianna directly now. She's wanted.)"
    show mscmc bikini_hairup sad at left1 behind arianna
    show arianna siren angry at right1plus
    mcarianna "But since the sculpture came with a death threat towards government officials I'm guessing they're going to come after the resistance hard."
    ai "The resistance is going to be labeled as terrorists for this, the government will want to make an example out of taking us down."
    show mscmc angry
    ai "And to top it off, my full name's on there. And so is my grandma's."
    hide arianna
    show mscmc bikini_hairup_cu angry_cu at mscmc_cu
    "(I can't lose Arianna.)"
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    ai "Let's go, a unit is probably on their way here now. I will make Casper answer for this."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
