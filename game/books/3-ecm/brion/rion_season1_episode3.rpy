label rion_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_junkyard_day at bg with fade
    play music ecmaction1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "The walls around us close in as I continue to scream for help."
    hide ecmc

    show skye casual_cu surprised_cu at skye_cu
    sk "We're going to die!"

    show skye casual_cu sleep_cu
    "Skye starts to shake, his eyes squeezed shut."
    hide skye

    show rion jacket_cu surprised_cu at rion_cu
    ri "[genericfn]!"
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "I look up in relief to see Rion at the top of the compactor."

    show ecmc jacket_v2_cu sad_cu
    mcrion "Rion! There's no way to climb out!"
    hide ecmc

    show rion jacket_cu surprised_cu at rion_cu
    ri "Hang on! Let me find something to toss down."
    hide rion

    "Rion returns swiftly with a rope and throws it down."

    show skye casual surprised at left1plus
    show ecmc jacket_v2 pin surprised at right1
    mcrion "Skye, you go first. I'll come up behind you."

    show skye casual basic at left1plus:
        linear 0.4 alpha 0.0 yoffset -200
    show ecmc jacket_v2 basic
    "Skye starts climbing as quickly as he can as the walls narrow, the compactor's hydraulics roaring in my ears."
    hide skye

    hide ecmc
    show rion jacket_cu angry_cu at rion_cu
    ri "Grab on!"
    hide rion

    "I try to grab the rope but my hands start to spasm."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "My hands!"

    "I look at my hands in agitation, then I suddenly have an idea."

    show ecmc jacket_v2_cu determined_cu
    "Using my mouth to help, I wrap the rope around my wrists and thread the end through."
    hide ecmc

    show rion jacket_cu angry_cu at rion_cu
    ri "Good thinking, [genericfn]. Now hold on as best you can."
    ri "I'm going to pull you out!"
    hide rion

    "I realise Skye's just made it to the top. Rion grunts, then yanks on the rope as hard as he can, pulling me up to the top."
    "I make it over the edge, then collapse on the ground beside Skye just as the compactor shuts with a bang."

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin sad at right1plus
    ri "Just made it..."

    hide ecmc
    hide rion
    show skye casual surprised at centre
    sk "I can't believe you almost killed us!"
    hide skye

    stop music
    play music ecmcalmeveryday4

    show rion jacket pin angry at left1plus
    show ecmc jacket_v2 pin angry at right1plus
    mcrion "It's your fault! I told you not to run!"

    hide ecmc
    hide rion
    show skye casual angry at centre
    sk "You WOULD say that! I don't want to go to jail!"
    hide skye

    show rion jacket pin angry at left2
    show skye casual basic at right2
    ri "Kid! I'm not here to arrest you! Hustling hardware isn't our jurisdiction."

    show rion jacket basic
    ri "I just have some questions."

    show skye casual surprised
    sk "Why should I go with you?"

    show rion jacket angry
    ri "Because I'm a D.I.V.A.A. agent, and if you help us you'll be helping to save a lot of lives."

    show rion jacket smirk
    ri "And, we'll buy you a big meal someplace nice to sweeten the pot."

    show skye casual surprised
    "Skye studies both of us for a moment."
    sk "Fine."

    hide skye
    hide rion
    show ecmc jacket_v2 pin surprised at centre, step_in
    "I stand up and suppress a gasp as a sharp, searing pain shoots through my ankle."
    hide ecmc

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Damn, I think I twisted it when I landed in the compactor.)"

    show ecmc jacket_v2_cu angry_cu
    "I grit my teeth as I follow behind Rion and Skye as quickly as I can."

    show ecmc jacket_v2_cu sad_cu
    "(My hands are already misfiring, I refuse to let my ankle slow me down too!)"

    stop music
    play music ecmcalmeveryday3
    scene bg ecm_restaurant_day at bg with wiperightdissolve

    "Skye, Rion, and I sit at a nearby restaurant, with huge plates of food in front of us."

    show rion jacket pin basic at left2
    show skye casual smug at right2
    sk "This looks great. Scrapper-work always makes me hungry!"

    show rion jacket surprised
    ri "We didn't just bring you here to eat, Skye."
    ri "I need you to tell us everything you know about that part with the marking on the device I showed you."

    show skye casual angry
    "Skye stops eating and glares at Rion."
    sk "I never promised to tell you everything."

    show skye casual smug
    sk "Some secrets are meant to be scrapped. After all, there's a reason I find the best hardware!"

    hide rion
    show ecmc jacket_v2 pin smile at left2
    show skye casual basic
    mcrion "Skye, how about we make a deal?"
    mcrion "If you open up to us now, I won't dive in pile C in that junkyard for a whole month."
    mcrion "We both know that's the best area."

    show skye casual smug
    sk "Make it two and we have a deal."

    show ecmc jacket_v2 determined
    mcrion "A month and a half."

    show skye casual surprised
    "Skye stares at me for a couple moments and I hold his gaze, unwavering."

    show skye casual angry
    sk "Fine. We have a deal."

    hide ecmc
    hide skye
    show rion jacket pin basic at centre
    "I look over at Rion, but he's still looking at Skye, his face impassive."
    hide rion

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I can't tell if he liked my negotiation tactic or not.)"

    show ecmc jacket_v2_cu blush_cu embarrassed_cu
    "(I wonder what it takes to get Rion to compliment someone?)"
    hide ecmc

    show rion jacket pin basic at left2
    show skye casual angry at right2
    ri "Okay, so we have a deal."

    show skye casual basic
    "Rion pulls the device from his backpack and slides it across the table to Skye."
    ri "You see that polymer casing? It has the junkyard's marking on it. What do you make of it?"
    "Skye studies the restraint for a moment, then leans back in his chair."
    sk "I actually picked this specific part myself, the casing that is. I sold it to an anonymous buyer months ago."
    sk "The rest of the parts must've come from different junkyards, or underground tech markets."

    show rion jacket surprised
    ri "Can you tell us anything about the anonymous buyer?"

    show skye casual angry
    sk "Sorry, I don't ask my anonymous buyers any questions."

    show skye casual basic
    ri "Well, did they know exactly what you have on offer, or do they have to go to you first?"
    sk "A bit of both. They know I'm the person to have this kind of thing."
    ri "So you don't ask anonymous buyers questions. You still keep records?"

    show skye casual smug
    sk "Of course, I run a substantial operation."

    hide skye
    show ecmc jacket_v2 pin basic at right1
    show rion jacket basic
    "Rion glances at his watch, then turns to me."

    show rion jacket smile
    ri "We should get back to HQ, we have what we came for."

    hide ecmc
    show rion jacket angry
    show skye casual basic at right2
    ri "Skye, if I come asking questions again, don't run."
    "Skye rolls his eyes as he shovels in another mouthful of food."
    sk "I promise."

    hide rion
    hide skye
    "We say goodbye to Skye, then Rion and I leave the restaurant."

    stop music
    play music ecmromantic3
    scene bg ecm_sidewalk_day at bg
    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin sad at right1
    with clockwise_wipe
    mcrion "Did we really get what we came for? Skye didn't know much."

    show ecmc jacket_v2 basic
    ri "We got plenty. I've never been able to source a part before now. That opens doors to future investigations, or even laying a trap."
    ri "And Skye's buyer list will have a lot of metadata we can use to draft a list of suspects."
    ri "Eko will come up with some options to parse it all."

    show ecmc jacket_v2 surprised at right1:
        parallel:
            easein_circ 0.4 right1plus
        parallel:
            easein 0.2 yoffset -20
            easein 0.2 yoffset 0
    "As I take my next step, pain shoots through my leg and I stumble."

    show rion jacket surprised behind ecmc at left1plus:
        easein 0.6 left1 xoffset 25
    show ecmc jacket_v2 embarrassed
    ri "[genericfn], something wrong?"

    hide ecmc
    hide rion
    show rion jacket_cu sad_cu at rion_cu
    "Rion gently holds my arms to steady me as he looks into my eyes with concern."
    hide rion

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    mcrion "It's no big deal. I hurt my leg when I landed in the compactor."
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    ri "Where does it hurt?"
    hide rion

    show rion jacket pin basic behind ecmc at left1:
        xoffset 25
    show ecmc jacket_v2 pin sad at right1plus
    "I bend down and run my hand over my shin."
    mcrion "Around here."
    ri "Is it a stabbing pain or a dull pain?"
    mcrion "More like a stabbing pain."
    ri "Why don't you use me like a crutch. We don't have to walk far, anyway."

    show ecmc jacket_v2 embarrassed
    mcrion "I'm fine, Rion. I can walk."

    show rion jacket smirk
    ri "Didn't we talk about teamwork earlier, [genericfn]?"
    ri "Besides, it'll be quicker."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(I really want to prove myself today, but I could make it worse if I keep walking on my leg.)"

    show ecmc jacket_v2_cu embarrassed_cu blush_cu
    "(Besides...if I lean on Rion I'll get a chance to be right up close with him.)"
    hide ecmc

    show rion jacket_cu smirk_cu at rion_cu
    "As if reading my mind, Rion shoots me a smirk as he offers me his arm."
    ri "Don't be so hard on yourself, Hatchling."
    hide rion

    $menuhideborder = True
    menu rions1e3c1:
        "A. Lean on Rion while you walk." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show rion jacket pin smirk behind ecmc at left1:
                xoffset 25
            show ecmc jacket_v2 pin smile at right1plus
            mcrion "Alright, alright...but only because I don't want to slow you down."

            show rion jacket smirk at left1:
                xoffset 25
                easein 0.6 centre xoffset 0
            pause 0.2
            show ecmc jacket_v2 blush embarrassed at right1plus:
                transform_anchor True rotate 0
                linear 0.4 rotate 3
            "Rion carefully wraps his arm around my waist and I rest against him"

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "(My body's pressed up against his...I can feel everything tensing as he walks.)"
            hide ecmc

            show rion jacket_cu pin_cu basic_cu at rion_cu:
                transform_anchor True
                zoom 0.63 xpos 180 ypos -50
            show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu:
                transform_anchor True
                zoom 0.65 xpos 450 ypos 1.0
            ri "Do you feel steady?"

            show rion jacket_cu basic_cu at rion_cu:
                xpos 180 ypos-50
                easein_back 0.4 xoffset 50
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu:
                xpos 450 ypos 1.0
                easein_back 0.4 xoffset -50
            "Rion's grip tightens slightly as he pulls me even closer."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "(I've never been held like this before...)"
            "(He smells like coffee, and a bit like fresh paper.)"

            show ecmc jacket_v2_cu sleep_cu
            "I realise I'm blushing and I do my best to keep my breathing even."

            show ecmc jacket_v2_cu smile_cu -blush_cu
            mcrion "I do."
            show ecmc jacket_v2_cu blush_cu sad_cu
            "As nice as things are, I can't help feeling useless."
            hide ecmc

            show rion jacket pin basic at left1:
                xoffset 25
            show ecmc jacket_v2 pin embarrassed at right1:
                xoffset -20
            mcrion "This is so frustrating! I finally get to be on the field and I'm practically out of commission."
            mcrion "First my hands have completely glitched up and now it's like my leg is short circuiting too!"

            show rion jacket smirk
            ri "You're doing the best you can, [genericfn]. Despite the pain, you've been persevering."
            show ecmc jacket_v2 sad
            mcrion "I just feel like I'm not doing enough. I shouldn't be letting minor injuries hold me back."
            ri "Don't be silly, Hatchling. We're a team, and we have each other's backs, remember?"

            show ecmc jacket_v2 smile
            "Rion smiles at me and I give him a small smile back."

            show ecmc jacket_v2 embarrassed
            show rion jacket basic
            mcrion "This team feels very one-sided. You've really had to pick up my slack."

            show rion jacket smirk
            ri "It's only your second day. And you've seen way more action than a trainee normally should."
            ri "Besides, even seasoned agents need help sometimes."

            show rion jacket basic
            ri "I actually can't stand agents who try to put on the tough guy facade and do things on their own."

            show ecmc jacket_v2 sad
            mcrion "I know...I just wish I could hist fast forward on recovery."

            hide ecmc
            hide rion
            show rion jacket_cu basic_cu at rion_cu
            "Rion stops walking for a moment and turns to face me, his hands lightly grasping my hips to keep me steady."
            hide rion

            show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
            "My skin pulses under Rion's touch, and I instinctively lean towards him, already missing having his body against mine."
            hide ecmc

            show rion jacket_cu sad_cu at rion_cu
            ri "I understand your frustration, [genericfn]. I've been injured in the field plenty of times."
            ri "It's definitely a bug in your system to take a backseat while your colleagues pick up the slack."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "I can't picture you getting injured. You seem indestructible."
            hide ecmc

            show rion jacket_cu smirk_cu at rion_cu
            "Rion chuckles as he looks at me, his eyes sparkling with amusement."
            ri "No one's indestructible, [genericfn]. Even the toughest agents fall."
            ri "But what makes you truly tough is the resolve to get up again and keep going."
            hide rion

            show ecmc jacket_v2_cu blush_cu basic_cu at ecmc_cu
            "Rion lightly grasps my shoulders and gives them a gentle squeeze."
            hide ecmc

            show rion jacket_cu smirk_cu at rion_cu
            ri "Despite two injuries, you're determined not to let the team down and that's important."

            show rion jacket_cu basic_cu
            ri "But don't be afraid to lean on your team members. That's what we're here for."
            hide rion

            show rion jacket pin basic at left1:
                easein 0.4 xoffset 25
            show ecmc jacket_v2 pin basic at right1:
                xoffset -20
            "Rion wraps his arm around me again and I once more lean on him, letting him support my weight."

            show ecmc jacket_v2 blush embarrassed
            mcrion "Thanks, Rion."

            hide ecmc
            hide rion
            show rion jacket_cu basic_cu at rion_cu
            "I sneak a peek at Rion when he's looking straight ahead, careful to avoid any bumps in the street."
            hide rion

            show ecmc jacket_v2_cu blush_cu surprised_cu at ecmc_cu
            "(He's even more attractive up close...)"

            show ecmc jacket_v2_cu embarrassed_cu
            "My heart beats a little faster as I realise just how close I am to Rion, and I quickly look back at the road as we continue walking."

            show rion jacket_cu pin_cu smirk_cu behind ecmc at rion_cu:
                transform_anchor True
                zoom 0.63 xpos 230 ypos-50
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu:
                transform_anchor True
                zoom 0.65 xpos 450 ypos 1.0
                easein_back 0.4 xoffset -50
            "Rion doesn't say a word, but he holds me a little tighter so I press up against him a little more."

        "B. Walk on your bad leg.":
            $menuhideborder = False
            show rion jacket pin basic behind ecmc at left1:
                xoffset 25
            show ecmc jacket_v2 pin embarrassed at right1plus
            mcrion "I'm really fine, Rion."

            show ecmc jacket_v2 pin embarrassed at right1plus, out_right
            "I turn and walk down the street, ignoring the pain shooting up my leg."
            hide ecmc
            ri "Alright, have it your way, [genericfn], but you have a lot to learn about partnership so you may want to re-think this later."

    stop music
    play music ecmcalmeveryday3
    scene bg ecm_office_hq_on at bg with clockwise_wipe

    "Rion and I make it back to HQ, and he leaves me in the main office to handle some minor logistics work while he deals with the case."

    show enver casual basic at centre, step_in
    "I'm sitting at a desk, working, when Enver walks in."

    show enver casual smile
    en "Hey, [genericfn]. What are you doing back without Rion?"

    show ecmc jacket_v2 pin surprised at right2
    show enver casual basic at left1plus
    mcrion "After all the excitement we had today, Rion told me to take it easy."

    show ecmc jacket_v2 basic
    show enver casual sad
    en "Oh yeah, he told me about the junkyard!"
    en "I heard you got injured after the chase. How's your ankle?"

    show ecmc jacket_v2 smile
    show enver casual basic
    mcrion "I'm okay. I'm still limping a bit, but the medical team thinks I'll be fine by tomorrow."
    en "Alright, but take it easy."

    show ecmc jacket_v2 basic
    show enver casual sad
    "Enver narrows his eyes at me."

    show enver casual angry
    en "I also heard that your hands are still all buggy. You shouldn't have downplayed it to me yesterday!"

    show ecmc jacket_v2 embarrassed
    mcrion "I'm sorry! I really didn't think it was that bad."

    stop music
    play music ecmkorintheme

    hide ecmc
    hide enver
    show anton casual basic at left2, step_in
    show korin nojacket pin basic at right2, step_in
    show bird normal at right2:
        xoffset 130 yoffset 80
    "Just then, two more D.I.V.A.A. agents enter."
    "One seems bubbly and energetic, a robotic bird sitting on her shoulder as she carries on the conversation."
    "The other seems a bit more quiet and reserved and I notice that he's not saying much."
    "They spot Enver and I and head over."

    show korin nojacket smile
    bubblyenergetic "Oh, you must be [genericfn]. We heard what happened at the junkyard and came to check on you!"

    hide korin
    hide anton
    hide bird
    show ecmc jacket_v2 pin basic at right2
    show enver casual smile at left1plus
    en "[genericfn], this is Korin and Anton."

    hide ecmc
    hide enver
    show anton casual basic at left2
    show korin nojacket pin smile at right2
    show bird normal at right2:
        xoffset 130 yoffset 80
    ko "We heard your first twenty-four hours with D.I.V.A.A. have been pretty eventful."

    show anton casual angry
    an "If you hadn't broken into the junkyard, then you wouldn't have gotten hurt."

    hide anton
    hide korin
    hide bird
    show ecmc jacket_v2 pin embarrassed at right2
    show enver casual sad at left1plus
    en "Relax, Anton. [genericfn] is fine and Rion knows what he's doing."

    hide ecmc
    hide enver
    show anton casual angry at left2
    show korin nojacket pin basic at right2
    show bird normal at right2:
        xoffset 130 yoffset 80
    an "You mean he {i}thinks{/i} he knows what he's doing."

    hide anton
    hide korin
    hide bird
    show ecmc jacket_v2 pin basic at right2
    show enver casual smile at left1plus
    en "Okay, enough. I want to hear about [genericfn]'s day!"

    show ecmc jacket_v2 sad
    show enver casual basic
    "I turn to Enver with a sigh."
    mcrion "Today was intense. I'm glad I finally get to be on the field, but I'm worried my injuries are holding me back."
    mcrion "It's frustrating because I know I can do better."

    show enver casual smile
    en "Hey, the fact that you're working through your injuries shows how determined you are."

    hide ecmc
    hide enver
    show anton casual basic at left2
    show korin nojacket pin basic at right2
    show bird normal at right2:
        xoffset 130 yoffset 80
    ko "Getting injured is just part of the job! I broke my leg during my Hatchling training."

    show anton casual angry
    an "You'd get injured less if you actually followed proper protocols."

    hide anton
    hide korin
    hide bird
    show ecmc jacket_v2 pin embarrassed at right2
    show enver casual angry at left1plus
    en "Leave her alone, Anton. She was following her trainer's instructions."

    show ecmc jacket_v2 sad
    show enver casual basic
    mcrion "Well, I tried, but he's not exactly open with compliments. I'm not always sure I'm on the right track with him."

    show enver casual smile
    en "That's just Rion. Don't take it personally. He values his privacy and just needs time to get to know you."
    mcrion "I just wish I could at least tell whether he liked my work or not."
    en "He actually said something to me earlier."

    show ecmc jacket_v2 surprised
    mcrion "Really?! What did he say?"

    show ecmc jacket_v2 determined
    "Enver chuckles and shoots me a smirk."

    show ecmc jacket_v2 basic
    en "He's very amused that you're a scrapper!"

    show ecmc jacket_v2 embarrassed
    mcrion "That doesn't make things any clearer!"
    mcrion "I wish trainees could have the same trainer for more than a day."
    mcrion "I'd really like to learn more from Rion."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(And maybe I'd learn how to read him better as well.)"

    stop music
    play music ecmromantic3
    scene bg ecm_sidewalk_day at bg with fade

    "The next day, on my way to work I spot Rion inside a cute coffee shop, talking and laughing with some cafe patrons."

    show rion black pin smile at centre
    "The elder gentleman next to him must have said something funny as Rion tips his head back slightly and laughs."

    hide rion
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(He seems a lot more relaxed here than when he's in the office.)"
    hide ecmc

    "I start to head inside to say hi."

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "But when my hand reaches the doorknob, I freeze."
    "(Enver mentioned that Rion values his privacy. I should probably leave him be.)"
    hide ecmc

    show ecmc jacket_v2 pin basic at centre
    "I continue walking down the street to the office."
    hide ecmc

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I wish Rion could be my trainer again. I'd really like to learn more from him.)"

    stop music
    play music ecmmctheme
    scene bg ecm_office_cafe_on at bg  with clockwise_wipe

    "Later that morning, I wait with the other trainees for my next trainer assignment."
    enthustrainee "Did you hear about Rion?!"
    enthustrainee "He rescued another trainee yesterday!"
    oncaffeine "Actually, I heard it was the same trainee as the day before!"

    show ecmc jacket_v2 pin basic at centre
    "The other trainees turn to glare at me, then they resume gossiping."
    hide ecmc

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I really wonder who my trainer will be today.)"
    "(Korin seemed nice yesterday, but that Anton guy was so rigid.)"
    hide ecmc

    stop music
    play music ecmromantic1

    show sparkle_effect:
        corner1 (0.25, 0.0) corner2(0.75, 1.0) xpos 0.25
    show rion black pin basic at centre, step_in
    "Just then, Rion saunters in and the other trainees turn to stare at him in awe."
    hide rion

    enthustrainee "He's so mysterious! He's the only trainer who didn't have a bio on the virtu-net."

    show ecmc jacket_v2 pin basic at right1plus
    show rion black pin smirk at left1plus, left_in
    "Rion spots me and immediately starts heading over, then nonchalantly leans back against the wall as he gives me a casual nod."

    show ecmc jacket_v2 embarrassed
    ri "Hey, [genericfn]."

    show ecmc jacket_v2 smile
    mcrion "Hey!"

    show ecmc jacket_v2 blush smile
    "I respond a bit too enthusiastically and I feel my face heat slightly in embarrassment."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(At least I didn't fumble my words today!)"
    hide ecmc

    show rion black pin smirk at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "How are your ankle and hands?"

    show ecmc jacket_v2 smile
    mcrion "They're both a little better."
    mcrion "I visited the medical staff yesterday and they said my hands should be better in a day or two."
    mcrion "They also said my ankle will be fine. It's just a light sprain so I just need to keep weight off it."
    ri "That's good."

    show ecmc jacket_v2 basic
    ri "So, I wanted to give you an evaluation of your work yesterday."

    show ecmc jacket_v2 surprised
    mcrion "Like an official evaluation?!"

    ri "No, just some friendly feedback."

    hide rion
    hide ecmc

    $menuhideborder = True
    menu rions1e3c2:
        "A. Please be gentle!":
            $menuhideborder = False
            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin surprised at right1plus
            mcrion "Please...don't be too harsh!"
            ri "Don't worry, Hatchling."

        "B. Please be tough.":
            $menuhideborder = False
            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            mcrion "I really want to know what I need to improve!"

        "C. Should I be worried?":
            $menuhideborder = False
            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin surprised at right1plus
            mcrion "Do you have any really harsh feedback?"

            show rion black smile
            ri "Not at all, but there was room for improvement."

    show ecmc jacket_v2 basic
    show rion black basic
    ri "I noticed that you were very fixated on following protocols."
    show rion black smirk
    ri "Sometimes rules and protocols need to be bent depending on the situation."

    show rion black basic
    ri "Plus, you were a little soft on people. Make sure to keep your guard up, especially around potential suspects."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu basic_cu at ecmc_cu
    "(Not too bad, that's all fair criticism.)"
    hide ecmc

    show rion black pin smirk at left1plus
    show ecmc jacket_v2 pin smile at right1plus
    mcrion "I understand, I can work on those things. Thank you!"

    show ecmc jacket_v2 basic
    ri "Oh, don't thank me, [genericfn]."

    show ecmc jacket_v2 surprised
    "I look at Rion in confusion while he smirks back at me."
    mcrion "Why? Is something wrong?"

    show rion black basic
    ri "Well, the way I see it, you're going to get tired of my notes in a few days."
    mcrion "Huh? What are you talking about?"

    show rion black smirk
    ri "Yesterday was like a trial run. Today I'm going to be extra attentive."
    mcrion "Aren't I supposed to have a different trainer today?"
    ri "I had a meeting with some of the other Phoenix Detectives and Griffin Detective Vega."
    ri "I requested to be your trainer for as long as my investigation is open, and that just got approved this morning."

    hide ecmc
    hide rion
    show rion black_cu smirk_cu at rion_cu
    "Rion crosses his arms over his chest, his muscles straining slightly against his shirt as his smirk grows."
    ri "Looks like you're stuck with me for at least another week, Hatchling. Maybe even two."
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Oh my Bot! At least another week?!)"

    show ecmc jacket_v2_cu blush_cu surprised_cu
    "(I wonder why he requested me?! Does he...like me?)"
    hide ecmc

    show rion black_cu basic_cu at rion_cu, step_in
    "Rion straightens up from the wall and takes a step towards me."
    ri "I requested you specifically because I just need your 'scrapper' expertise."

    show rion black_cu smirk_cu
    ri "We may need to talk to your friend Skye again."

    ri "And you might have more insights into the restraint, or similar devices from past crime scenes."
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Oh...of course."
    hide ecmc

    show rion black_cu basic_cu at rion_cu
    ri "Anyway, we should get going. I made a major breakthrough in the case and I want to follow up on it."
    ri "Are you ready to go, Hatchling?"
    hide rion

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "I nod, trying not to show just how excited I feel."
    mcrion "I'm ready."
    hide ecmc

    show rion black_cu smirk_cu at rion_cu
    ri "Good."
    hide rion

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    "Rion starts to walk to the door, then he pauses and looks back at me, his expression unreadable."

    show rion black surprised
    ri "This is going to be pretty tough. I'm really taking a risk with this request."

    show ecmc jacket_v2 smile
    mcrion "Don't worry, Rion. I'll do my best and I promise I won't let you down."

    show rion black smirk
    ri "Good. Then let's go."

    show rion black smirk at left1plus:
        easein 0.6 xoffset 80
    show ecmc jacket_v2 embarrassed
    "Rion lightly places his hand on my lower back as he guides me out of the room."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "Just that subtle touch is enough to light my skin on fire, and I do my best to keep my expression neutral."

    show ecmc jacket_v2_cu smile_cu
    "(I can't believe Rion asked to work with me!)"

    show ecmc jacket_v2_cu embarrassed_cu
    "(I know he said he wanted my scrapper experience, but it could be more than that...)"
    hide ecmc

    show rion black pin smirk at left1:
        xoffset 30
    show ecmc jacket_v2 pin blush embarrassed at right1:
        xoffset -10
    "I walk alongside Rion as a million questions run through my mind."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu basic_cu at ecmc_cu
    "(I wonder what breakthrough Rion had.)"

    show ecmc jacket_v2_cu surprised_cu
    "(Where are we going?)"

    show ecmc jacket_v2_cu embarrassed_cu
    "(And why is he still touching my back?!)"
    hide ecmc
    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

