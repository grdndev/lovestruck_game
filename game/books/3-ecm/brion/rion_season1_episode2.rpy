label rion_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_office_lab_on at bg with fade
    play music ecmromantic1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Rion fills me in on his case as we enter Eko's lab."

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "As you likely gathered from yesterday, I'm tracking a serial killer."
    ri "I've been on his tail for years. Every one of his victims shows signs of heavy cybernetic experimenting."
    ri "Yesterday was the closest I've come to catching him."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "I feel a pang in my gut as I recall Rion turning away from the masked man to help me."
    "(If only I could've told him to just chase the suspect. Then again, that restraint might've been doing more damage than I realized.)"

    hide ecmc
    show eko casual pin glasses basic at centre
    "We see Eko bent over her lab table, looking through a microscope."

    show eko casual smile
    "She looks up as we approach and smiles warmly at Rion."

    show rion black pin basic at left2
    show eko casual basic at right2
    ek "Rion! It's great to see you."

    hide rion
    show ecmc jacket_v2 pin basic at left2
    show eko casual smile
    ek "It's a pleasure to see you again as well, [genericfn]."

    show ecmc jacket_v2 smile
    mcrion "Good to see you too, Eko!"

    hide ecmc
    show rion black pin basic at left2
    show eko casual basic
    ri "Hey, Eko. I brought you something."
    "Rion reaches into his backpack and pulls out a packet of Hardwired Scipops."

    show rion black smirk
    ri "I spotted these in that small corner store just outside the city."
    ri "Their shells are hard but the filling is soft and sweet, I figured the textures would be new to you."

    show eko casual smile
    ek "Thank you, Rion! I can't wait to process this!"

    show rion black basic
    ri "If I find any more rare snacks I'll send them your way."

    hide rion
    hide eko
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "Jealousy rises up and I do my best to squash it."

    show ecmc jacket_v2_cu angry_cu
    "(I'm here to work! Not to crush on my trainer...)"

    show rion black pin basic at left4 behind ecmc
    show ecmc jacket_v2 pin basic at left1:
        xoffset 10
    show eko casual pin glasses basic at right4
    ri "Alright, [genericfn], the killer has access to unique and high-end tech."

    show eko casual thinking
    ek "Yes, you should see some of the gadgets that Rion's recovered from the scenes."
    ek "Their craftsmanship is quite impressive, but their purpose is never good."

    show ecmc jacket_v2 surprised
    show eko casual basic
    mcrion "What about the device that was on me?"
    ri "Let's take a closer look at that now."

    hide rion
    hide ecmc
    hide eko
    "Rion finds the device and brings it over to Eko's lab table."

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "I hope to hear feedback on how well the evidence was processed, but push away my disappointment when it doesn't come."

    show rion black pin basic at left4 behind ecmc
    show ecmc jacket_v2 pin basic at left1:
        xoffset 10
    show eko casual pin glasses sad at right4
    ek "This piece has been designed to incapacitate someone quickly, or slowly kill them."

    show rion black surprised
    ri "You got lucky, Hatchling. It's a good thing we were able to get this thing off you straight away."

    show rion black basic
    show ecmc jacket_v2 embarrassed
    mcrion "It's a good thing you were there to remove it! All my muscles were seizing, I could barely turn my head."

    hide ecmc
    hide eko
    hide rion
    show rion black_cu basic_cu at rion_cu
    "Rion gives me a searching look, then takes some gloves and slowly starts turning the device over."
    hide rion

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right2
    ri "Notice anything unusual?"
    "I look closely at every piece of the restraint, searching for something familiar or identifiable."

    show ecmc jacket_v2 surprised
    mcrion "Huh, there's a marking on one of the parts."

    show ecmc jacket_v2 blush basic at right2:
        easein 0.6 right1
    pause 0.6
    "I lean forward and take a better look at the marking, trying to ignore the goosebumps that prick on my skin as I lightly brush up against Rion."

    show ecmc jacket_v2 surprised -blush
    mcrion "Oh! I've seen this before!"
    mcrion "Junked items are often tagged to show which junkyard they're supposed to go to."
    mcrion "This marking belongs to that huge lot on the East side of town."
    ri "What do you think that means then, Hatchling?"
    "Rion steps back and studies me intently, his eyes staring into mine, as I swallow nervously."
    mcrion "Well, maybe..."
    hide rion
    hide ecmc

    $menuhideborder = True
    menu rions1e2c1:
        "A. It fell out of a garbage truck.":
            $menuhideborder = False
            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin surprised at right1
            mcrion "This part could've been someone's trash and fallen out of the truck. Maybe the suspect found it on the road?"
            ri "That seems a bit unlikely."

        "B. It was found in the junkyard.":
            $menuhideborder = False
            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin surprised at right1
            mcrion "The suspect could've found this part in the East junkyard."
            show rion black surprised
            ri "That's a possibility, but they'd have to know a lot about searching junkyards to find something like this."

        "C. It was taken out of someone's trash.":
            $menuhideborder = False
            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin surprised at right1
            mcrion "The suspect could've stolen this from someone's trash, maybe the manufacturer's rejection pile?"
            show rion black surprised
            ri "Plausible, but those tend to be well guarded."

    hide rion
    hide ecmc
    "I mull the marking over a little longer, and suddenly a lightbulb goes off."

    show ecmc jacket_v2 pin surprised at right1
    show rion black pin basic at left1plus
    mcrion "They could've bought it from a scrapper! Scrappers dig through junkyards all the time and sell refurbished hardware."

    show ecmc jacket_v2 determined
    mcrion "That would've been the easiest way for the suspect to source something like this."
    "Rion evaluates the restraint, mulling over my argument."

    show ecmc jacket_v2 basic
    show rion black smirk
    ri "Your logic seems to fit."

    hide rion
    hide ecmc
    show eko casual_cu glasses_cu smile_cu at eko_cu
    "Eko looks at me and beams."
    hide eko

    show ecmc jacket_v2_cu blush_cu basic_cu at ecmc_cu
    "I blush and Eko's smile gets wider."
    hide ecmc

    show eko casual_cu glasses_cu smile_cu at eko_cu
    ek "Oh, [genericfn], you're blushing!"
    ek "Did you know that Rion is standing 12.7cm closer to you than he does with other trainees?"
    hide eko

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin blush embarrassed at right1
    "I feel my blush get darker and I do my best to stay calm. Rion shakes his head at Eko, a half-amused smile on his face."
    ri "Thank you, Eko."

    show ecmc jacket_v2 basic -blush
    "Rion picks the device up and looks at me."
    ri "Alright, Hatchling, what should our next step be?"

    show ecmc jacket_v2 smile
    mcrion "I think we should check out the East junkyard and case it for local scrappers."
    mcrion "I've been there a few times, I might see an acquaintance or two who can point us in the right direction."
    ri "Sounds like a plan, let's do it."

    scene bg ecm_junkyard_day at bg
    show android casual basic at centre:
        ypos 100
    with wiperightdissolve

    stop music
    play music ecmmctheme

    "Rion and I arrive at the junkyard and approach the guard-bot watching the front gate."

    hide android
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(Oto-55's on guard duty today? Lucky us.)"
    hide ecmc

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1
    "I lean in to whisper to Rion."

    show ecmc jacket_v2 smile
    mcrion "This guard-bot knows me. I scrounge around here all the time!"

    show rion jacket smirk
    ri "You're a scrapper?"
    mcrion "Yeah! You can get some of the coolest tech on the cheap in these junkyards."

    hide rion
    hide ecmc
    show android casual basic at centre:
        ypos 100
    guardbot "Sorry, [genericfn], this isn't public visiting hours. Come back later."

    show ecmc jacket_v2 pin smile at left3
    show android casual basic at right2
    mcrion "Come on, Oto. I'll give you first dibs on my find, just like always."
    "Oto's eye focuses on each of our D.I.V.A.A. badges."
    guardbot "Are you trying to bribe a guard on duty? That is highly illegal."

    hide android
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Ugh! That's such a lie. He lets me in all the time!)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show android casual basic at right2:
        ypos 100
    mcrion "It's not like that, Oto. I'm here as a D.I.V.A.A. Hatchling. My trainer and I just need to look around."
    guardbot "Not without a warrant."

    hide ecmc
    hide android
    "I turn to Rion in frustration and lean in."

    show ecmc jacket_v2 pin sad at right1
    show rion jacket pin basic at left1plus
    mcrion "He must be worried we'll discover the junkyard doing something illegal."
    ri "The L.A. police are the contract holders for investigating municipal junkyards."

    show rion jacket surprised
    ri "We can petition for a warrant, but if the PD gets territorial about it they can block it for weeks. Will anything else motivate him?"
    mcrion "If Oto won't take a bribe, I really don't know."

    show rion jacket smirk
    ri "Okay, I have an idea."

    hide rion
    hide ecmc
    show android casual basic at centre:
        ypos 100
    "Rion faces Oto and gives him a curt nod."

    show rion jacket pin smirk at left3
    show android casual basic at right3:
        ypos 100
    ri "Good job, lil' bot. You were programmed well."
    show rion jacket pin smirk at left3, out_left
    "Rion turns and strides away and I hurry to follow him."

    scene bg ecm_sidewalk_day at bg with fade
    stop music
    play music ecmupbeateveryday2

    "Rion and I walk slowly along the side of the junkyard."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Does Rion know how to fast track a search warrant or something?)"
    hide ecmc

    show rion jacket pin basic at centre with dissolve
    "Suddenly, Rion stops and looks up at the fence."
    ri "This looks good."

    show rion jacket basic at left1plus
    show ecmc jacket_v2 pin surprised at right1plus
    mcrion "Good...? What are you talking about?"
    ri "The other side looks clear. We can just hop over."
    mcrion "Hop over? We can't just break in!"
    ri "Sometimes you need to be flexible to get things done."

    show ecmc jacket_v2 sad
    mcrion "But D.I.V.A.A has protocols, and I'm still a Hatchling."
    ri "If we get in trouble, I'll take the fall."
    ri "You're my responsibility today, remember?"
    mcrion "Well..."
    ri "We need to follow this lead before the trail goes cold again. Worst we can do is tick off a guard-bot."
    mcrion "I guess that's true."

    hide rion
    hide ecmc
    show rion jacket pin basic at centre:
        xoffset 20 yoffset -5 alpha 0.0
        parallel:
            linear 0.4 alpha 1.0
        parallel:
            easein_circ 0.6 xoffset 0 yoffset 0
    "Rion gives me a reassuring nod, then turns back to the fence and expertly mounts it."

    hide rion
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(He makes it look so easy...)"
    hide ecmc

    "As soon as I grip the fence and try to pull myself up, my hands spasm and I fall to the ground."

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    mcrion "Oof!"
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    ri "You okay, Hatchling?"
    hide rion

    show ecmc jacket_v2 pin sad at right1plus
    show rion jacket pin basic at left1plus, left_in
    "Rion quickly climbs back over the fence and looks at me in concern."
    mcrion "My hands..."

    show rion jacket surprised
    mcrion "I didn't think I'd have this much trouble with them today."

    show rion jacket basic behind ecmc
    show ecmc jacket_v2 surprised blush at right1plus:
        easein 0.4 right1 xoffset -40
    "Rion gently takes my hands in his and I try not to shiver from the contact."

    show ecmc jacket_v2 embarrassed
    "He lightly traces his fingertips over my palms, searching for anything overtly wrong."
    ri "Still on the fritz from the restraint?"
    mcrion "I think so."
    "Rion gently starts to massage my palms and fingers, the warm pressure reassuring."

    show ecmc jacket_v2 embarrassed -blush
    ri "Does this hurt?"
    mcrion "A little..."
    ri "Can you make a fist and squeeze?"

    show ecmc jacket_v2 sad
    "I do as Rion says, and wince."
    ri "You're going to struggle getting over the fence if you can barely make a fist."

    show rion jacket smirk
    ri "I can hoist you up."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "I feel a blush creep onto my cheeks as I think of Rion holding my body."
    hide ecmc

    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin blush smile at right1:
        xoffset -40
    mcrion "It's okay. I'm sure I can manage."
    ri "I want to help you, [genericfn]."

    show rion jacket surprised
    show ecmc jacket_v2 basic
    ri "If you get injured while breaking the rules because I asked you to, it'll become a huge 'me' problem."
    ri "Technically, you've already gotten hurt on my watch once. I don't want that to happen again."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(I really wouldn't mind Rion's strong hands on me.)"
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    ri "I won't let you fall."
    hide rion
    $menuhideborder = True
    menu rions1e2c2:
        "A. Accept Rion's help over the fence." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show rion jacket pin smirk at left1
            show ecmc jacket_v2 pin smile at right1:
                xoffset -40
            mcrion "Thanks, Rion. I could definitely use the help."
            ri "Why don't you show me what you can do first."

            show ecmc jacket_v2 basic
            "I nod, then try to pull myself up, but my hands go numb."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            mcrion "Ah...!"
            hide ecmc

            show ecmc jacket_v2 pin surprised at right1:
                alpha 0.0 transform_anchor True zoom 1.2 yoffset 100
                linear 0.4 alpha 1.0 yoffset 180
            pause 0.2
            show rion jacket pin basic behind ecmc at left1:
                transform_anchor True zoom 1.2 alpha 0.0
                linear 0.4 alpha 1.0
            "I start to fall, but Rion catches me and gingerly sets me to my feet, his hands lingering on my skin."
            "I instinctively lean into Rion's touch, my skin heating where his hands still linger."

            show rion jacket smirk
            show ecmc jacket_v2 blush embarrassed
            ri "Careful."
            "I sheepishly look up at Rion who's smirking at me, but I can see a hint of tenderness in his gaze."

            show rion jacket smirk behind ecmc at left1:
                easein_circ 0.4 left1plus
            "He then drops his hands from my waist and I immediately feel cold and as if something's missing."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu embarrassed_cu blush_cu at ecmc_cu
            "(It felt nice to be in Rion's arms, even if just for a moment.)"
            hide ecmc

            show rion jacket pin surprised at left1plus
            show ecmc jacket_v2 pin basic at right1plus
            ri "So that didn't work."

            show ecmc jacket_v2 sad
            mcrion "I hate feeling useless... Maybe I should just wait here and keep watch?"

            show rion jacket smirk
            show ecmc jacket_v2 basic
            ri "I need your scrapper expertise. We'll find a way to make this work."
            ri "What if I hold you up until you're high enough to hook yourself over the top of the fence?"

            show ecmc jacket_v2 surprised
            mcrion "I think that could work."

            show ecmc jacket_v2 embarrassed
            mcrion "Thanks, Rion. I'm not sure how I'd get over without your help."
            ri "Of course, [genericfn]. We're a team, and teamwork is the most important thing in the field."
            ri "You never know when you'll need to rely on a partner."

            show ecmc jacket_v2 smile
            mcrion "Well, I'm glad I have you to rely on today."
            ri "Always."

            show rion jacket basic
            ri "You ready?"
            mcrion "Yes. Let's do this."

            hide ecmc
            hide rion
            "Rion comes up behind me and firmly grips my hips, the contact instantly making me feel warm again."

            show rion jacket_cu basic_cu at rion_cu
            ri "Brace yourself."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "I take a deep breath and steady myself, feeling a little more confident with Rion's hands holding me steady."
            mcrion "I'm ready."
            hide ecmc

            "Rion effortlessly hoists me up as if I don't weigh anything."
            "As Rion lifts me higher, my shirt shifts slightly and Rion's fingers brush over my bare skin."

            show ecmc jacket_v2_cu blush_cu surprised_cu at ecmc_cu
            "(Don't think about it! Focus on the fence!)"
            hide ecmc

            show rion jacket_cu basic_cu at rion_cu
            ri "Alright, Hatchling, hook your leg over."
            "I manage to straddle the fence, Rion supporting the left side of my body."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "Now what? Should I just jump?"
            hide ecmc

            show rion jacket_cu basic_cu at rion_cu
            ri "Hang on. Let me help you."
            hide rion

            "Rion effortlessly climbs up and over, lands, then holds his arms out."

            show rion jacket_cu basic_cu at rion_cu
            ri "Try climbing down. I'll catch you if you slip."
            hide rion

            show ecmc jacket_v2_cu sleep_cu at ecmc_cu
            "I take a deep breath then slowly start to make my way down the fence."

            show ecmc jacket_v2_cu surprised_cu
            "My hands suddenly spasm and I let go of the fence."

            scene bg ecm_sidewalk_day at bg
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            with hpunch
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu:
                transform_anchor True rotate 0
                parallel:
                    linear 0.8 alpha 0.0
                parallel:
                    easein 0.4 yoffset -80
                    easein 0.4 yoffset 100
                parallel:
                    easein_circ 0.4 rotate 5

            "I fall to the ground, crashing into Rion before he has time to react."

            scene bg ecm_junkyard_day at bg
            show rion jacket_cu basic_cu at rion_cu
            with fade
            pause 0.4

            show rion jacket_cu sleep_cu blush_cu
            "Rion lets out a small grunt. I turn to face him and realize that our bodies are partly entangled."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "I'm so sorry!"
            hide ecmc

            "I try to stand up, but I trip over Rion and fall right back down."

            show rion jacket_cu smile_cu at rion_cu
            "Rion chuckles as he gently grasps my arms and looks into my eyes."
            hide rion

            show ecmc jacket_v2_cu surprised_cu blush_cu at ecmc_cu
            "My heart hammers out of my chest as I meet his gaze."
            hide ecmc

            show rion jacket_cu smile_cu at rion_cu
            ri "No harm done. Come on."
            hide rion

            show rion jacket pin smile at left1, step_in
            "Rion carefully stands up and extends his hand."

            show ecmc jacket_v2 pin blush embarrassed at right1, step_in
            "I sheepishly take it, trying to ignore the sparks I feel when our hands connect."

            hide rion
            hide ecmc
            "Once on my feet, I dust myself off and look around the junkyard."

            show rion jacket_cu smile_cu at rion_cu
            ri "Well, that was entertaining."
            hide rion

            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "(My face must be bright red right now...)"
            hide ecmc

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v2 pin basic at right1
            ri "Let's omit that from the report."
            mcrion "I wish my hands would just work normally."

            show ecmc jacket_v2 embarrassed
            mcrion "I'm sorry, Rion. I feel like I'm slowing you down."
            ri "We did it, partner. Don't sweat."
            ri "We can still get the job done with your hands out of action."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(He called me \"partner\"!)"

            show ecmc jacket_v2_cu blush_cu embarrassed_cu
            "(I guess technically we {i}are{/i} work partners right now.)"
            hide ecmc

        "B. Attempt the climb alone.":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin blush smile at right1:
                xoffset -40
            mcrion "It's fine, Rion. I'm sure I can manage on my own."
            ri "You sure? Mounting the fence isn't as easy as it looks, even for people without injured hands."
            mcrion "I'm sure."
            ri "Alright. Follow me."
            "Rion once more effortlessly mounts the fence and I take a deep breath."
            "(I can do this.)"
            "I try to climb the fence, but my hands are so weak that I can't get a firm enough grip."
            ri "Hang on. Let me find something to help."
            "Rion runs into the junkyard and returns a few moments later with thin, steel shelving and sets it over the fence."
            ri "Try this."
            "I climb as quickly as I can to get to the other side."

    show rion jacket pin smirk at left1plus
    show ecmc jacket_v2 pin basic at right1
    ri "Alright, [genericfn], where do you think we should start first?"

    show ecmc jacket_v2 angry
    "I look around at the expansive junkyard, then look shyly back to Rion."

    show ecmc jacket_v2 embarrassed
    mcrion "What do you think?"
    ri "I'm asking you, Hatchling."

    show ecmc jacket_v2 basic
    ri "You're familiar with this junkyard. How is the junk sorted? Where would we find scrappers?"

    show ecmc jacket_v2 smile
    mcrion "There are certain spots in this junkyard where they usually store the more high-end stuff."
    ri "Lead the way."

    hide rion
    hide ecmc
    "As we draw closer to high-value spot, I see a familiar face."

    show skye casual smug at centre
    sk "Fancy seeing you here, [genericfn]."

    stop music
    play music ecmtense2

    hide skye
    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin smile at right1
    mcrion "Skye, I see you bribed your way in as usual."

    hide rion
    hide ecmc
    show skye casual angry at centre
    "Skye's gaze drifts to Rion and he stares at him nervously."
    sk "Who's this?"

    show skye casual basic at right4
    show rion jacket pin basic at left4
    show ecmc jacket_v2 pin smile at left1:
        xoffset 15
    mcrion "Skye, this is my D.I.V.A.A. trainer, Rion."
    mcrion "Rion, this is Skye."

    hide skye
    hide rion
    hide ecmc
    $menuhideborder = True
    menu rions1e2c3:
        "A. We're both scrappers.":
            $menuhideborder = False
            show skye casual basic at right4
            show rion jacket pin basic at left4
            show ecmc jacket_v2 pin smile at left1:
                xoffset 15
            mcrion "He's a fellow scrapper."
            sk "'Fellow' scrapper? Please, [genericfn], I would never associate with you among scrappers."

        "B. We're sort of frenemies.":
            $menuhideborder = False
            show skye casual basic at right4
            show rion jacket pin basic at left4
            show ecmc jacket_v2 pin smile at left1:
                xoffset 15
            mcrion "We've known each other a long time, but we're also kind of rivals."

            show skye casual smug
            sk "Pfft. We'd only be rivals if she was on my level."
            sk "The things I find are actually useful, unlike the junk you find."

        "C. We've known each other a long time.":
            $menuhideborder = False
            show skye casual basic at right4
            show rion jacket pin basic at left4
            show ecmc jacket_v2 pin smile at left1:
                xoffset 15
            mcrion "I met Skye a long time ago when we were both searching through the same junk yard."
            mcrion "We realized we had a lot in common since we're both dedicated scrappers."

    show skye casual basic
    mcrion "We both know I'm a better scrapper. I always find the best retrotech."

    show skye casual smug
    show ecmc jacket_v2 basic
    sk "And {i}how{/i} in demand is retrotech?"
    sk "What are you looking for, anyway?"

    show skye casual basic
    show rion jacket smirk
    ri "Actually, kid, maybe you'll be able to help."

    show skye casual surprised
    sk "'Kid'?!"

    hide rion
    hide ecmc
    hide skye
    "Rion pulls the brutal, scratch-built restraint out of his backpack and shows it to Skye."

    show skye casual basic at right4
    show rion jacket pin basic at left4
    show ecmc jacket_v2 pin basic at left1:
        xoffset 15
    ri "Do you know anything about this?"

    show skye casual angry
    sk "You're asking a 'kid' for help? Let me see."
    "Skye takes a closer look then his face pales."
    sk "Why are you asking me about this?"
    sk "Something like this would be highly illegal to sell..."

    stop music
    play music ecmaction1
    show skye casual angry at out_right
    "Skye trails off as he looks from me to Rion, then before I can say anything, he turns and runs away."
    hide skye

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Skye!"
    hide ecmc

    show rion jacket_cu angry_cu at rion_cu
    ri "Tch!"
    hide rion

    "Before I can stop Rion, he sprints after Skye."
    "I follow, hoping to cool Skye off before he hurts himself."
    "I try to talk Skye down as all three of us scramble over small hills of scrap metal."

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    mcrion "Skye! Stop running! You're making things worse!"
    mcrion "We just want to talk!"
    hide ecmc

    show skye casual_cu surprised_cu at skye_cu
    sk "I don't want to talk to you!"

    show skye casual_cu angry_cu
    sk "You're not going to catch me, [genericfn]."
    sk "Trying to arrest your competition is low, even for you!"
    hide skye

    "Skye doesn't let up. Rion and I follow him over more piles of junk, covering nearly the junkyard's entire length."

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    mcrion "Skye, stop!"
    hide ecmc

    "Skye breaks for a small tunnel of junk."

    show rion jacket_cu angry_cu at rion_cu
    ri "Kid, you're not doing yourself any favors."
    hide rion

    show skye casual_cu basic_cu at skye_cu
    sk "I'm not a 'kid'!"

    show skye casual_cu basic_cu at skye_cu, out_left
    "Skye ducks into the tunnel and scurries away."
    hide skye

    show rion jacket pin surprised at left1plus
    show ecmc jacket_v2 pin basic at right1
    ri "There's no way I'll fit in that. I'll have to run around this pile and cut him off ahead."

    show ecmc jacket_v2 angry
    mcrion "I'll follow him!"

    hide rion
    hide ecmc
    "I squirm in after Skye and move as quickly as I can."
    "When I get out of the tunnel, I see Skye running towards one of the junkyard compactors."

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    mcrion "Skye! Stop! The compactor is auto-cycling! You'll get hurt!"
    hide ecmc

    show skye casual angry at centre
    "Skye hesitates, but as he turns back to look at me, he stumbles and falls."

    show skye casual surprised at centre:
        transform_anchor True rotate 0
        parallel:
            linear 0.8 alpha 0.0
        parallel:
            easein 0.4 yoffset -30
            easein 0.4 yoffset 100
        parallel:
            easein_circ 0.4 rotate 5
    sk "AHH!"
    hide skye

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Skye!"
    hide ecmc

    "Without thinking, I jump in after him and land at the bottom of the compactor. A sharp pain shoots up my ankle, but I try to ignore it."

    show ecmc jacket_v2_cu surprised_cu
    "I look up and gasp."

    show ecmc jacket_v2_cu angry_cu
    mcrion "The walls are too high... and there's nothing to hold onto!"
    hide ecmc

    show skye casual_cu surprised_cu at skye_cu
    "Skye's face drops in horror at the situation, mirroring my own."
    sk "What are we going to do?!"
    hide skye

    "The walls start closing in around us as a fresh cycle begins, and I do my best not to panic."

    show skye casual surprised at left1
    show ecmc jacket_v2 pin angry at right1
    mcrion "We'll get crushed if we don't climb out!"

    hide skye
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Rion should be coming this way any minute!)"

    show skye casual_cu surprised_cu at skye_cu
    sk "HELP, somebody!!"
    hide skye

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "RION! Help us, Rion!"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
