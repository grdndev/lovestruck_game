label arianna_season2_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_arianna_studio_day at bg
    play music mscsuspense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show casper casual_cu smile_cu at casper_cu
    "Casper stares at me, hand on his chin and his head tilts ever so slightly."
    hide casper
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(What if he {i}really really{/i} hates humans?!)"
    show mscmc bikini_hairdown surprised at right5
    show arianna siren angry at right1
    show casper casual basic at left5
    mcarianna "Um, I, was just...uh..."
    mcarianna "I just came to see Arianna."
    show arianna:
        easein_back 0.4 xoffset 70
    show casper confused:
        ease 0.3 left3
    "Casper swims forward, but Arianna throws her arm out in front of me."
    ai "Stay there, Casper."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Now is totally not the time to be distracted by how hot Arianna is when she's protective.)"
    hide mscmc
    show casper casual basic at left1plus
    show queenie casual basic at right2
    "Queenie reaches a hand towards Casper but doesn't touch him."
    qn "Casper, this is [genericfn]. She's a human, but we trust her."
    "Casper glances at Queenie and nods as he looks at me."
    hide casper
    hide queenie
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(On the bright side, he does seem pretty calm compared to before he saw me.)"

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    show mscmc bikini_hairdown basic at right5
    show arianna siren angry at right1:
        xoffset 70
    show casper casual smile at left3
    cs "Can I talk to the human?"
    show casper basic
    show arianna basic
    "Arianna grimaces then looks at me."
    ai sad "It's up to you."
    show casper smile
    show arianna basic
    mcarianna surprised "Sure. That's fine."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Though, I don't know what he wants to talk about.)"
    show casper casual basic at left3
    show arianna siren angry at right5 behind mscmc
    show mscmc bikini_hairdown basic at right2
    "Arianna drops her arm and moves to my side, eyes glued to Casper as he approaches."
    show mscmc surprised
    cs smile "You're really human? Those are real legs?"
    mcarianna "Yep."
    show mscmc basic
    cs basic "Hm. I've only seen humans from a distance before."
    show arianna sleep
    show mscmc surprised
    cs "You're more attractive up close."
    hide casper
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    "Arianna rolls her eyes, looking to the side momentarily."
    show casper casual basic at left3
    show arianna siren angry at right5 behind mscmc
    show mscmc bikini_hairdown basic at right2
    cs "Do humans feel love?"
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Oh, so he {i}actually{/i} just wants to know about humans. I can roll with that.)"
    show casper casual smile at left3
    show arianna siren angry at right5 behind mscmc
    show mscmc bikini_hairdown basic at right2
    mcarianna "Um, yeah. We do."
    cs "So, you also feel pain?"
    mcarianna smile "Emotional {i}and{/i} physical, yup."
    show casper basic
    show mscmc basic
    "Casper hums, deep in thought."
    show mscmc surprised
    show arianna basic
    cs confused "Can your arms turn into bird wings?"
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Is that a popular misconception about humans in the mer world...?)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e4c1:
        "A. Totally!":
            $ menuhideborder = False
            show casper casual basic at left3
            show arianna siren surprised at right5
            show mscmc bikini_hairdown grin at right2
            mcarianna "Yeah, but only some humans."
            show arianna smile
            show mscmc smile
            cs basic "Fascinating."
            show casper confused
            "Arianna covers a smile behind her hand."
            show mscmc grin
            ai basic "She's kidding."

        "B. I wish.":
            $ menuhideborder = False
            show casper casual basic at left3
            show arianna siren basic at right5
            show mscmc bikini_hairdown grin at right2
            mcarianna "I wish, but sadly that's a no."
            show casper smile
            mcarianna grin "Sure would be cool though."
            show mscmc smile
            cs basic "It would be."

        "C. And our mouths turn into beaks.":
            $ menuhideborder = False
            show casper casual basic at left3
            show arianna siren surprised at right5
            show mscmc bikini_hairdown grin at right2
            mcarianna "Yeah and then our mouths turn into beaks."
            show casper confused
            show arianna grin
            mcarianna "Every seagull above the water right now is actually a human in a disguise."
            show arianna smile
            show mscmc smile
            cs sleep "Your tone tells me that you're joking."
            show casper smile
            show arianna basic
            mcarianna "I am. We can't grow wings, or turn into birds."


    show mscmc basic
    show arianna angry
    cs confused "And your legs...they look rather flimsy."
    cs angry "Those things support your weight when you're on land?"
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Legs may not be as cool as tails, but they get the job done.)"
    show casper casual smile at left3
    show arianna siren basic at right5 behind mscmc
    show mscmc bikini_hairdown smile at right2
    mcarianna "Mhm."
    show mscmc basic
    show arianna angry
    "Casper leans over, inspecting my legs."
    cs "Can I touch your leg?"
    hide casper
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    ai "No, you can't."
    show casper casual basic at left3:
        xoffset -50
        pause 0.1
        ease 0.4 xoffset 0
    show arianna siren angry at right5 behind mscmc:
        xoffset -50
        pause 0.1
        easein_back 0.4 xoffset 0
    show mscmc bikini_hairdown basic at right2:
        xoffset -60
        pause 0.2
        easein_back 0.4 xoffset 0
    "Arianna takes my arm, pulling me back from Casper's poised hand."
    cs confused "I didn't mean to be insensitive."
    hide casper
    hide arianna

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(I was scared of him before, but maybe Casper's just been misguided.)"
    show casper casual basic at left3
    show arianna siren angry at right5 behind mscmc
    show mscmc bikini_hairdown smile at right2
    mcarianna "It's alright. I felt the same way when I first met Arianna."
    cs smile "You live on the beach?"
    mcarianna "Not, like, in the sand, but yeah, pretty much."
    show mscmc surprised
    cs sleep "Do you watch the sunset every night?"
    show casper basic
    mcarianna "Maybe not every night, but I do love watching it."
    show arianna basic
    cs sleep "I've only watched it above water once. It was so...vibrant."
    show mscmc smile
    show casper smile
    "His tone turns gentle, an almost innocent look in his eyes."
    cs sleep "It made me feel..."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(Casper, I want to belive that you're not a bad guy. Maybe I can help Arianna and Queenie right now.)"
    show casper casual smile at left1plus
    show mscmc bikini_hairdown smile at right3
    mcarianna "The world is pretty beautiful, isn't it?"
    show casper angry
    mcarianna basic "The sunset is kind of like nature's art. That's how Arianna's and other people's art makes me feel."
    show casper basic
    mcarianna smile "Warm inside. In awe. Excited."
    show mscmc basic
    "Casper looks down at his hands."
    cs confused "I'm going to ask one more thing."

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show mscmc surprised
    cs angry "How are you able to breathe and talk underwater?"
    hide casper
    show arianna siren_cu basic_cu behind mscmc:
        zoom 0.75 xanchor 0.5 yanchor 1.0 xpos 0.7 ypos 1.0
    show mscmc bikini_hairdown_cu sad_cu:
        zoom 0.75 xanchor 0.5 yanchor 0.95 xpos 0.3 ypos 1.0
    "Arianna and I exchange looks."
    hide arianna
    hide mscmc
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Can we tell him about the magic shell Queenie gave me? He's anti-magic, right?)"
    "(Magic is illegal and Casper fights against its use by anyone other than government officials.)"
    hide mscmc
    show casper casual confused at left1plus
    show queenie casual basic at right2
    qn "Magic."
    show casper angry
    "Queenie swims forward, her eyes set on Casper."
    cs basic "I see."
    hide casper
    hide queenie
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(I guess we're trusting him. But something has definitely changed about his demeanor compared to their earlier conversation.)"
    hide mscmc
    show casper casual basic at left1plus
    show queenie casual basic at right2
    "Casper looks between Queenie and me, his face thoughtful."
    cs "There's more to this resistance than I initially thought."
    cs sleep "Magic and art...and humans."
    hide casper
    hide queenie
    show arianna siren basic at right1plus:
        xoffset 50
        pause 0.1
        linear 0.5 xoffset 0
    show mscmc bikini_hairdown basic at left1:
        xoffset 20
    "Arianna moves closer to me, her arm brushing against mine."
    hide mscmc
    hide arianna
    show casper casual basic at left1plus
    show queenie casual basic at right2
    cs "I need to think all this over."
    cs "I won't turn you in though."
    hide queenie
    show casper casual confused at centre
    "Casper nods at Queenie and Arianna as he swims out the studio, and sends one last confused look my way."
    cs basic "I hope that we can talk again."
    hide casper
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(He's a weirdo but maybe I can help get him on the right side of this fight.)"
    mcarianna basic_cu "Me too, Casper."
    hide mscmc

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show queenie casual smile at centre
    "After Casper leaves, Queenie claps her hands together with a smile."
    qn "Well, that took a turn for the better, didn't it?"
    hide queenie
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(It did! I'm kind of shocked.)"
    hide mscmc
    show arianna siren basic at centre
    "Arianna crosses her arms and shrugs, her eyes on where Casper was last."
    hide arianna
    show queenie casual smile at left2
    show mscmc bikini_hairdown smile at right2
    qn "You handled yourself very well, [genericfn], despite your surprise entrance."
    show mscmc grin
    qn "I can imagine you were worried, but thanks to you, Casper may give us a chance."
    show queenie basic
    mcarianna basic "I hope so."
    hide mscmc
    show arianna siren basic at right1plus
    "Queenie pats the top of Arianna's head and Arianna finally looks away from the entrance, which is really just a hole in the hull."
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Arianna still seems tense for some reason.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show queenie casual basic at left2
    show arianna siren basic at right1plus
    qn "Now, Arianna, you need to finish the resistance project scultpure as soon as you can, we don't want to drag this on."
    show queenie smile
    ai smile "I know. It'll be done soon, only thing left to make are the scales."
    qn basic "I need to head back to the city. I'll see you both soon."
    show arianna sleep
    show queenie:
        linear 0.5 xoffset -100 alpha 0.0
    "Queenie waves to me and leaves, as Arianna pushes her hands through her hair with her eyes closed."
    show mscmc bikini_hairdown basic at left1 behind arianna
    mcarianna "What's wrong?"
    ai basic "That was stressful."
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(If Casper had left before I blew my hiding spot, he could've ruined everything the resistance has been working towards.)"
    show mscmc bikini_hairdown smile at left1
    show arianna siren smile at right1plus
    mcarianna "We made it though."
    "I put my hand on her arm and she smiles briefly."
    show mscmc surprised
    ai sad "Are you okay?"
    mcarianna "I'm fine. Really."
    ai angry "I was so scared that moment after he first saw you."
    show mscmc smile
    show arianna embarrassed
    "I move my hand to her cheek and smile at her."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    mcarianna "I'm okay."
    show mscmc embarrassed_cu
    "(I'm not going anywhere, Arianna.)"
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    "Arianna puts her hand over mine, holding it for a moment before our hands both fall away."
    ai "I got to get to work on these scales. Not every part of being in a resistance is daring and noble, I guess."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(I think her working away down here making tons of scales for some epic protest sculpture is still pretty cool.)"
    show arianna siren smile at right1plus behind mscmc
    show mscmc bikini_hairdown grin at left1
    mcarianna "What's the sculpture of?"
    show mscmc smile
    ai grin "A freaking sea serpent! The scales will be imbued with magic, and detachable from the skeleton, so people can nab some magic."
    hide mscmc
    hide arianna
    "Arianna swims over to one of the tables and holds up a palm sized scale made of some iridescent metal it looks like."
    show arianna siren_cu grin_cu at arianna_cu
    ai "Making {i}all{/i} the scales is gonna take forever but I have to freaking crunch time this thing."
    hide arianna

    $ menuhideborder = True
    menu ariannas2e4c2:
        "A. Wait, how long does it take?":
            $ menuhideborder = False
            show arianna siren basic at right1plus
            show mscmc bikini_hairdown surprised at left1
            mcarianna "Oh...{i}forever{/i}?"
            ai smile "Well, the shaping part of it can take a bit but it's not super bad."
        "B. How many are we talking?":
            $ menuhideborder = False
            show arianna siren basic at right1plus
            show mscmc bikini_hairdown surprised at left1
            mcarianna "And how many are we making?"
            ai grin "Enough to cover every inch of a giant sea serpent."
        "C. We can do this!":
            $ menuhideborder = False
            show arianna siren basic at right1plus
            show mscmc bikini_hairdown smile at left1
            mcarianna "We got this! It'll be done in no time."
            ai grin "Love the energy, but you won't be saying that in a little bit."

    show arianna siren_cu grin_cu:
        xanchor 0.5 yanchor 0.5 xpos 0.7 ypos 0.6
    show mscmc bikini_hairdown_cu embarrassed_cu behind arianna:
        zoom 0.80 transform_anchor True xanchor 0.5 yanchor 0.5 xpos 0.25 ypos 0.6 alpha 0.0
        pause 0.1
        linear 0.4 zoom 0.85 alpha 1.0
    "I swim up beside her and put my hand on her back as I look over her shoulder at the work table, and a smile lights up her face."
    mcarianna grin_cu "How do you make them?"
    show mscmc smile_cu
    ai "We put the metal through a stamp press."
    show mscmc grin_cu
    ai sleep_cu "Then they have to be filed down and shaped."

    hide mscmc
    hide arianna
    stop music fadeout 0.5
    play music mscromance fadein 1.0
    "Arianna beckons me to another table with what I assume is a press on it. She swims up behind me and leans in close."
    "There's a thin sheet of iridescent metal sitting beside the machine that she indicates with her chin, her face next to mine."
    show arianna siren grin at right1plus:
        yoffset 50
        pause 0.2
        parallel:
            easein_circ 0.4 yoffset 20
        parallel:
            linear 0.4 xoffset -105
    show mscmc bikini_hairdown embarrassed at left1:
        yoffset 30
    ai "So, take your material..."
    show arianna siren_cu embarrassed_cu:
        zoom 0.87 align(0.5, 1.0) transform_anchor True rotate 0 xoffset 140 yoffset 80
        rotate 2
    show mscmc bikini_hairdown_cu embarrassed_cu:
        zoom 0.78 align(0.5, 1.0) transform_anchor True rotate 0 xoffset -140 yoffset 70
        rotate -2
    "Arianna lightly rests her chin on my shoulder and her arms settle on the table as they circle around either side of my waist."
    "Arianna puts her hands over mine, and directs my actions so I pick up the metal."
    hide arianna
    hide mscmc
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Oh, she can definitely teach me the whole process like this. She's so steady and strong in the water with her arms around me.)"
    show arianna siren_cu grin_cu behind mscmc:
        zoom 0.87 align(0.5, 1.0) transform_anchor True rotate 0 xoffset 140 yoffset 80
        rotate 2
    show mscmc bikini_hairdown_cu embarrassed_cu:
        zoom 0.78 align(0.5, 1.0) transform_anchor True rotate 0 xoffset -140 yoffset 70
        rotate -2
    ai "Slide it under and pull down the stamp with the lever. It'll juice up when we pull it down."
    hide mscmc
    hide arianna
    "Her hand closes over mine as we push down the lever together onto the metal sheet and I hear a sizzle sound rise up."
    show arianna siren_cu grin_cu:
        zoom 0.87 align(0.5, 1.0) transform_anchor True rotate 0 xoffset 140 yoffset 80
        rotate 2
    show mscmc bikini_hairdown_cu embarrassed_cu:
        zoom 0.78 align(0.5, 1.0) transform_anchor True rotate 0 xoffset -140 yoffset 70
        rotate -2
    ai "There you go. Just like that."
    show mscmc sleep_cu
    show arianna embarrassed_cu
    "Arianna's voice in my ear and her chest pressing against my back makes me shiver."
    hide arianna
    hide mscmc
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Ohhhh, I could think of a much dirtier context in which she would say that to me.)"
    "(Who am I kidding? I'm already picturing it as she leans against me right now. I wonder how you take off a seashell bra?)"
    hide mscmc
    "Arianna moves to pull the lever up as I cough to try and bring myself back from wherever my head just was."
    show arianna siren_cu grin_cu:
        zoom 0.87 align(0.5, 1.0) transform_anchor True rotate 0 xoffset 140 yoffset 80
        rotate 2
    show mscmc bikini_hairdown_cu embarrassed_cu:
        zoom 0.78 align(0.5, 1.0) transform_anchor True rotate 0 xoffset -140 yoffset 70
        rotate -2
    ai "Easy, right?"
    mcarianna "Uh yeah, really great."
    hide arianna
    hide mscmc
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Function, brain.)"
    show arianna siren_cu embarrassed_cu behind mscmc:
        zoom 0.87 align(0.5, 1.0) transform_anchor True rotate 0 xoffset 140 yoffset 80
        rotate 2
    show mscmc bikini_hairdown_cu sleep_cu:
        zoom 0.78 align(0.5, 1.0) transform_anchor True rotate 0 xoffset -140 yoffset 70
        rotate -2
    ai "Then, we sand this guy down."
    show mscmc embarrassed_cu
    "Arianna lets go of me as she grabs the stamped metal."
    hide arianna
    hide mscmc
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(I wish the stamping part lasted longer...But honestly I don't know how much more of that I could've handled.)"
    show mscmc bikini_hairdown grin at left1
    show arianna siren smile at right1plus
    mcarianna "You said before that the magic in these scales will mess up the government's surveillance?"
    show mscmc smile
    ai grin "The government won't be able to track or watch anyone with these on them and it won't set off their alarm bells."
    show arianna smile
    "Arianna begins to sand down the edges of the metal, shaping its harsh edges into soft curves."
    ai basic "Even if no one is doing anything to directly oppose the regime with them, it's still a big deal."
    mcarianna basic "The government shouldn't get to hoard magic for themselves when it's a part of your people."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(I want to fight this fight with her.)"
    show mscmc bikini_hairdown smile at left1
    show arianna siren grin at right1plus
    "I sit beside Arianna at the table and she hands the scale off to me, letting her arm rest on my shoulder after passing off the metal item."
    show arianna basic
    mcarianna basic "There's a lot of injustice in the human world too."
    show arianna grin
    mcarianna grin "A lot of private beaches that I've gotten in trouble for surfing at."
    mcarianna "How is it fair that some people can own a part of the water? The coastline?"
    mcarianna "The world shouldn't belong to anyone but everyone."
    ai embarrassed "Agreed."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_arianna_studio_sunset at bg with clockwise_wipe
    "After pulling the stamp down for what feels like the thousandth time I let out a groan."
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(My hand hurts...)"
    hide mscmc
    show arianna siren sleep at centre
    "Arianna yawns loudly and sets down a scale she's just finished shaping."
    show arianna smile
    "She stretches her arms over her head and arches her back, letting out a soft moan at the peak of her stretch."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(The curve ofher back is art.)"
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    "I raise the lever up hastily as Arianna shoots a look my way and smirks when our eyes meet."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Holy gorgeous mermaid.)"
    hide mscmc
    "A shock of pain sears through me as my hand accidentally brushes the active stamp."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Shit."

    hide mscmc
    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    show arianna siren_cu surprised_cu at arianna_cu
    ai "Are you okay?!"
    show mscmc bikini_hairdown surprised at left1
    show arianna siren basic behind mscmc at right1:
        xoffset 300 yoffset 30 alpha 0.0
        pause 0.1
        parallel:
            linear 0.4 yoffset 0 alpha 1.0
        parallel:
            easein 0.6 xoffset 0 knot 300 knot -30 knot 40 knot 0
    "Arianna rushes over to me and takes my wrist, inspecting my hand."
    mcarianna embarrassed "Yeah, I just burned my finger a little..."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Because I was staring at you.)"
    show mscmc bikini_hairdown smile at left1
    show arianna siren smile at right1 behind mscmc:
        xoffset 26
    "Arianna pulls me over to the back and presses my finger down onto a sea sponge growing off the side of a table."
    "I feel instant relief from the burning sensation."
    show mscmc grin
    ai grin "There's a special healing salve in this. I end up burning myself a lot..."
    mcarianna "Wow, that really worked fast."
    show mscmc embarrassed
    ai embarrassed "Aw, and to think I was going to kiss it better if this didn't work."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Is it too late to take back what I just said about it feeling better?)"
    show mscmc bikini_hairdown grin at left1
    show arianna siren grin at right1 behind mscmc:
        xoffset 26
    mcarianna "Actually, you know, it does still kind of hurt. A little. If you wanted to..."
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    "Arianna brings my hand to her face and presses her lips to my fingers."
    ai "How's it feel now?"
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    mcarianna "...hmm it's a pretty bad burn? Maybe another kiss, just in case?"
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    "She giggles and smiles against my skin."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(She can be so sweet and we feel so close sometimes, I forget for a few seconds sometimes that we're not together.)"

    hide mscmc
    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    show arianna siren_cu grin_cu at arianna_cu
    ai "Are you tired of doing scales? I'm tired."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Break time?"
    hide mscmc
    show arianna siren_cu sad_cu at arianna_cu
    ai "I'm going cross-eyed looking at these things."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I think I have a perfect breaktime plan.)"
    show arianna siren smile at right1 behind mscmc
    show mscmc bikini_hairdown grin at left1
    mcarianna "Want to go surfing with me? You showed me how to do scales, now I can show you how to do surfing?"
    ai grin "You know I love watching you surf."
    mcarianna "I don't want you to just watch! We could both surf if you switch to legs, and then we can grab a beer or something after."
    ai "Oh hell yes."

    hide arianna
    hide mscmc
    $ wavy_transition("bg msc_arianna_studio_sunset", "bg msc_labeach_sunset")
    scene bg msc_labeach_sunset at bg with dissolve
    "My board and bag sit in the sand where I left them by the time we get back to the beach."
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Paying that one nosey kid that's always around a dollar a week to guard my stuff is working out.)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "Human surfing! With legs!"
    hide arianna
    show mscmc bikini_hairdown grin at centre
    mcarianna "It's the best way to do it."
    hide mscmc

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show sparkle_column
    show arianna bikini smile at centre:
        transform_anchor True zoom 0.82 yoffset 30 alpha 0.0
        pause 0.1
        linear 0.4 zoom 0.85 alpha 1.0 yoffset 0
    "Arianna walks out of the water, but this time, she's sporting bikini bottoms. Very tiny and nice ones."
    hide arianna
    hide sparkle_column
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Don't stare at her super long beautiful legs. Her toned thighs. Her...Ok, seriously, get it together.)"

    hide mscmc
    $ wavy_transition("bg msc_labeach_sunset", "bg msc_ocean_wide_sunset")
    scene bg msc_ocean_wide_sunset at bg with dissolve
    show surfboard back at centre:
        transform_anchor True zoom 1.4 yoffset 150
    show mscmc bikini_hairdown embarrassed at left2:
        yoffset 130
    show arianna bikini basic at right3:
        yoffset 300 xoffset 50 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 180
        parallel:
            easein 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    "I set my board in the water and Arianna is at my side in an instant."
    show arianna grin
    mcarianna grin "Why don't you just try popping up on the board first?"
    mcarianna "Start on your stomach and then push yourself up."
    show surfboard:
        easein 0.4 right2
    show arianna:
        pause 0.1
        easein 0.4 right2
    "Arianna lays herself on the board. I try not to glance at her butt in those bottoms but from my peripheral I can tell that they suit her well."
    hide arianna
    hide surfboard
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        yoffset 0
    "(Few things in this world can compare to seeing Arianna happily trying new things, and in small bikini bottoms.)"
    show mscmc bikini_hairdown embarrassed at left2:
        yoffset 130
    show surfboard back at right2:
        transform_anchor True zoom 1.4 yoffset 150 xoffset -20
    show arianna bikini grin at right2:
        yoffset 200
    mcarianna "Chest rises first, then find your footing."
    show arianna smile:
        parallel:
            easein_back 0.6 yoffset 0
        parallel:
            easein 0.6 xoffset 10
    "She wobbles dangerously but she manages to stand briefly."
    ai "Am I a pro yet?"

    play sound splash03
    show mscmc grin
    show arianna:
        transform_anchor True rotate 0
        parallel:
            easeout_back 0.6 yoffset 500
        parallel:
            linear 0.3 rotate 2
        parallel:
            linear 0.6 alpha 0.0
    "As soon as Arianna finishes her sentence, she loses her balance and splashes into the water."
    mcarianna "You're a pro, alright."
    show arianna grin at right4:
        rotate 0
        parallel:
            easein_back 0.4 yoffset 180
        parallel:
            linear 0.4 alpha 1.0
    "Arianna shakes her hair out of her face and laughs."
    hide arianna
    hide surfboard
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        yoffset 0
    "(A pro at being cute, that is.)"
    show mscmc bikini_hairdown smile at left2:
        yoffset 130
    show surfboard back at right2:
        transform_anchor True zoom 1.4 yoffset 150 xoffset -20
    show arianna bikini smile at right4:
        yoffset 180
    ai "The balancing is hard. I haven't been on legs for as long as you."
    mcarianna embarrassed "Maybe it would help if you had someone else to hold on to."
    ai grin "Two people can surf on the same board?"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    mcarianna grin "Yeah!"
    ai "How does that work?"
    mcarianna embarrassed "Well, you would ride in front..."
    hide surfboard
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        yoffset 0
    "(I'm just now realizing the implication of us surfing together and just how much touching there would be.)"

    show surfboard back at centre behind mscmc:
        transform_anchor True zoom 1.8 yoffset 200
    show mscmc bikini_hairdown grin at centre:
        xoffset -54 yoffset 30
    show arianna bikini embarrassed at centre:
        xoffset 54 yoffset 65
    mcarianna "And I would hold onto you like this."
    "I step behind Arianna and put my hands loosely on her hips."
    ai "Mmm...I think I might really enjoy this kind of surfing."
    show mscmc embarrassed
    "She pulls my arms completely around her and leans into me."
    hide surfboard
    hide mscmc
    show arianna bikini_cu grin_cu at arianna_cu:
        xoffset 0 yoffset 0
    ai "Let's do it."
    hide arianna

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    $ menuhideborder = True
    menu ariannas2e4c3:
        "A. Tandem surf with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mscsurfcompetition fadein 1.0
            show surfboard back at centre behind mscmc:
                transform_anchor True zoom 1.8 yoffset 200
            show mscmc bikini_hairdown grin at centre:
                xoffset -54 yoffset 30
            show arianna bikini embarrassed at centre:
                xoffset 54 yoffset 65
            mcarianna "Absolutely."
            hide surfboard
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0 yoffset 0
            "(Be still, my beating heart.)"
            show surfboard back at centre behind mscmc:
                transform_anchor True zoom 1.8 yoffset 200
            show mscmc bikini_hairdown embarrassed at centre:
                xoffset -54 yoffset 30
            show arianna bikini embarrassed at centre:
                xoffset 54 yoffset 65
            "Arianna keeps my arms tight around her as she looks back at me."
            ai "I'm a {i}hands-on{/i} learner."
            show mscmc surprised
            "She purrs her words at me and bats her eyelashes."
            hide surfboard
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0 yoffset 0
            "(I've somehow managed to be on a surfboard, holding the prettiest mermaid in existence.)"
            show surfboard back at centre behind mscmc:
                transform_anchor True zoom 1.8 yoffset 200
            show mscmc bikini_hairdown grin at centre:
                xoffset -54 yoffset 30
            show arianna bikini embarrassed at centre:
                xoffset 54 yoffset 65
            mcarianna "Then it looks like you're in luck."
            show mscmc embarrassed
            ai grin "Trust me, I know just how lucky I am."
            show arianna embarrassed
            "Arianna releases my arms and gestures a hand to the surfboard."
            ai grin "Glad my surfing instructor is a hottie."
            hide surfboard
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0 yoffset 0
            "(How am I ever going to focus with her saying these things to me?)"
            ai grin_cu "It's definitely a plus for you."
            show mscmc bikini_hairdown smile at left1:
                yoffset 30
            show surfboard back at centre:
                transform_anchor True rotate 0 zoom 1.5
                rotate 10 xoffset -35 yoffset 170
            show arianna bikini embarrassed at right3:
                yoffset 150
            "I hold the side of the board, keeping it steady."
            mcarianna grin "You get on first."
            show mscmc smile
            ai grin "So chivalrous."
            show arianna smile:
                parallel:
                    easein 0.5 centre
                parallel:
                    easeout_back 0.5 yoffset 90
            show mscmc embarrassed
            "Arianna flips her hair over her shoulders as she pulls her body onto the board."
            show mscmc grin
            ai grin "Time to find a sick wave, dude."
            mcarianna "Totally, bro."
            show mscmc embarrassed:
                parallel:
                    linear 0.4 xoffset 5
                parallel:
                    easein_back 0.4 yoffset 0
            "I get on the board behind her and I can't help that her legs and elegant back fill my vision."
            hide arianna
            hide surfboard
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Wow, her back is pretty. I've seen it before, but not this close.)"
            "I'm suddenly very glad that Arianna can't see the way that I know I'm blushing."
            "(Getting worked up over a girl's back? Arianna, what have you done to me?)"
            show surfboard back at centre behind mscmc:
                transform_anchor True zoom 1.7 yoffset 200 xoffset -30
            show mscmc bikini_hairdown smile at left1:
                xoffset 5
            show arianna bikini grin at centre:
                yoffset 90
            ai "How is paddling going to work? Can we both do it?"
            mcarianna grin "Yeah, we can."
            show arianna smile
            mcarianna "We can both kneel and paddle or..."
            show mscmc embarrassed
            show arianna embarrassed
            "She looks back at me with an eyebrow quirked."
            ai "Or?"
            hide surfboard
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Something that involves way more touching.)"
            show surfboard back at centre behind mscmc:
                transform_anchor True zoom 1.7 yoffset 200 xoffset -30
            show mscmc bikini_hairdown embarrassed at left1:
                xoffset 5
            show arianna bikini smile at centre:
                yoffset 90
            mcarianna "You lie down on your stomach and I'll lie down over top..."
            ai grin "I want the real experience and that's how I've seen you paddle out by yourself."
            show arianna embarrassed
            "Arianna brings her thumb up to her mouth and nibbles on her nail as she looks at me."
            ai "So, we should do that, right? For the learning process."
            mcarianna grin "Yeah, for sure. That's...what I was thinking too."
            hide surfboard
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Just two girls with sexual tension, tandem surfing. Cool cool. Yeah. Awesome.)"
            hide mscmc
            "Arianna scooches forward and puts her chest down on the board, her legs on either side of me."
            show arianna bikini_cu grin_cu at arianna_cu
            ai "You'll go between my legs?"
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "Yep."
            hide mscmc
            show arianna bikini_cu embarrassed_cu at arianna_cu
            ai "Surfing's more thrilling than I thought."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "I laugh, knowing that if I indulge this talk anymore it will be bad news for my heart."
            show mscmc embarrassed_cu
            "(She's certainly not wrong.)"
            mcarianna grin_cu "This is a serious surfing lesson, got it?"
            hide mscmc
            show arianna bikini_cu embarrassed_cu at arianna_cu
            ai "I'm only ever serious."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Lies."
            hide mscmc
            "I put my hands on the edge of the board around Arianna and lower myself onto her back."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's usually the one at my back, pulling me in for hugs and leaning against me.)"
            "(I could get used to this.)"
            hide mscmc
            "Arianna locks her ankles around my waist, holding me in place there."
            show mscmc bikini_hairdown_cu surprised_cu at left2:
                xanchor 0.5 yanchor 0.5 ypos 0.6 transform_anchor True zoom 0.75
            show arianna bikini_cu smile_cu at right1plus:
                xanchor 0.5 yanchor 0.5 ypos 0.6 transform_anchor True zoom 0.85
            mcarianna "Am I crushing you?"
            ai grin_cu "No, but feel free to crush me."
            mcarianna grin_cu "Ready? We're gonna get that one."
            ai "I'm ready!"
            hide arianna
            hide mscmc
            "We paddle to catch the wave and as it's upon us, I brace my hands on the edge of the board."
            show mscmc bikini_hairdown_cu grin_cu at left2:
                xanchor 0.5 yanchor 0.5 ypos 0.6 transform_anchor True zoom 0.75
            show arianna bikini_cu surprised_cu at right1plus:
                xanchor 0.5 yanchor 0.5 ypos 0.6 transform_anchor True zoom 0.85
            mcarianna "Okay, stand up!"
            ai grin_cu "Ahhh! Okay!"
            hide mscmc
            hide arianna
            show surfboard back at left2:
                transform_anchor True rotate 0
                rotate -50 yoffset 50
            show mscmc bikini_hairdown grin at left1
            show arianna bikini grin at right1:
                xoffset -10
            "Almost seamlessly, we break apart on the board as we both get to our feet."
            "Arianna positions herself with her back against me and I take her waist with my hands."
            ai "I'm surfing!"
            mcarianna "Whooo!"
            "Cool flecks of water spray our bodies as we ride the wave."
            hide surfboard
            hide mscmc
            show arianna bikini_cu grin_cu at arianna_cu
            ai "This is awesome!"
            show mscmc bikini_hairdown grin at left1 behind arianna
            show surfboard back at left2 behind mscmc:
                transform_anchor True rotate 0
                rotate -50 yoffset 50
            show arianna bikini grin at right1:
                xoffset -10
            "We finish out the wave, laughing and shouting the whole way."
            ai "We did it! And I stood up the whole time!"
            mcarianna "That was really fun, wasn't it? I've never surfed with someone like that before."
            ai "Can I be your surfing buddy now?"
            mcarianna "Any time you want."


        "B. That's enough touching...for now.":
            $ menuhideborder = False
            show surfboard back at centre:
                transform_anchor True zoom 1.8 yoffset 200
            show mscmc bikini_hairdown embarrassed at centre:
                xoffset -50 yoffset 30
            show arianna bikini basic at centre:
                xoffset 50 yoffset 65
            "I drop her waist and step back with a shy laugh."
            hide surfboard
            hide arianna
            show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
            "(Maybe that's a little too much for me. I don't think I would be able to focus.)"
            show mscmc bikini_hairdown sad at left1plus:
                yoffset 60
            show arianna bikini basic at right2:
                yoffset 150
            show surfboard back at centre behind mscmc:
                transform_anchor True zoom 1.8 yoffset 200
            mcarianna "I've actually never tandem surfed with someone before."
            mcarianna "I don't know if it'd be the best learning experience for you."
            ai smile "Well, I'll figure the balancing out. Don't worry."

    hide surfboard
    hide mscmc
    hide arianna
    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    $ wavy_transition("bg msc_ocean_wide_sunset", "bg msc_labeach_sunset")
    scene bg msc_labeach_sunset at bg with dissolve
    "After a bit of Arianna attempting to surf on her own, we sit together in the sand."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(That was a well needed break from making scales.)"

    hide mscmc
    play sound "audio/sfx/bubbles_003_6397.mp3" loop
    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    "Then I hear the bubbling of my shellphone from inside my bag."
    show arianna bikini basic at right1plus
    show mscmc bikini_hairdown surprised at left1
    mcarianna "Aren't you the only person who knows I have a shellphone?"
    ai surprised "It's not me calling you."
    stop sound fadeout 0.5
    hide mscmc
    hide arianna
    "I take the shellphone out and put it to my ear."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Hello?"
    hide mscmc
    cs "It's Casper."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
