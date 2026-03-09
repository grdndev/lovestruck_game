label rion_season1_episode12:

    $tbc = False
    scene bg ecm_records_room_on at bg
    show smoke_effect:
        alpha 0.6
    play music ecmplottwist3

    pause

    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    "As I start to regain consciousness, I'm aware that it feels like the ground's moving below me."
    show ecmc nojacket_v1_cu pin_cu surprised_cu at ecmc_cu
    "(What's going on?)"
    hide ecmc
    stop music
    play music ecmriontheme
    window hide
    hide smoke_effect
    show bg ecm_rion_s1_ei4 at bg:
        zoom 0.9
        yanchor 0.6
        linear 8 yanchor 0.1
    with fade
    pause
    "I slowly blink my eyes open to find that Rion's carrying me, his arms wrapped tightly around me as he strides out of the room."

    "I smile up at him, tiredly, then snuggle into his chest."

    ri "Good, you're awake."

    "Rion smiles down at me with a genuine smile that causes my heart to beat a little faster."

    ri "You fainted. I was going to take you to the medical room."
    scene bg ecm_records_room_on at bg
    show ecmc nojacket_v1_cu pin_cu smile_cu at ecmc_cu
    with fade
    mcrion "I think I'm alright for now. I could probably walk!"
    hide ecmc
    show rion jacket_cu pin_cu angry_cu at rion_cu
    ri "Let me get us out of the room first."
    scene bg ecm_dorm_hallway_on at bg with wiperightdissolve
    stop music
    play music ecmemotional3
    pause
    "When we reach the hallway, Rion sets me down on my feet and we both double over as we cough up the gas in our lungs."
    show rion jacket pin angry at left3
    show ecmc nojacket_v1 pin sad at right3
    mcrion "Ugh."

    ri "Damn Anton! He almost killed us!"
    show rion jacket pin angry at left3 behind ecmc:
        easein 0.5 xoffset 90
    show ecmc nojacket_v1 pin sad at right3:
        easein 0.5 xoffset -140
    "Rion looks up at me, then he spontaneously pulls me in for a hug, crushing me against his chest."
    hide ecmc
    hide rion
    show rion jacket_cu pin_cu sad_cu at rion_cu
    ri "Are you alright? I really thought I almost lost you..."
    hide rion
    show ecmc nojacket_v1_cu pin_cu angry_cu at ecmc_cu
    mcrion "I'm fine!"
    hide ecmc
    show rion jacket pin sad at left3 behind ecmc:
        xoffset 90
    show ecmc nojacket_v1 pin angry at right3:
        xoffset -140
    "I pull back and look into Rion's eyes."

    mcrion "Forget about me for now. We need to go after Anton."
    show rion jacket pin angry
    ri "I think he's somewhere in the building, but apart from that, we have no idea where he is!"

    ri "I could alert D.I.V.A.A. secruty but that would take too much time."

    mcrion "I think I could find him, but I need access to your ARCware."
    show rion jacket pin surprised
    "Rion looks at me, hesitantly, and turns his ARCware over in his hands."

    ri "I've never given anyone full accessx to my ARCware before."
    show ecmc nojacket_v1 pin blush determined
    mcrion "Rion..."
    hide ecmc
    hide rion
    $menuhideborder = True
    menu rions1e12c1:
        "A. Convince Rion he can trust me.":
            $menuhideborder = False
            show rion jacket pin surprised at left2 behind ecmc:
                xoffset 90
            show ecmc nojacket_v1 pin determined at right2:
                xoffset -140
            mcrion "Rion, after all we've just been through together, you know you can trust me."

            mcrion "I only want to use your ARCware to track down Anton. Nothing more."
            show rion jacket pin smirk
            "Rion studies me for a moment then nods, a small smile tugging at his lips."

            ri "I trust you, [genericfn]."

        "B. Point out that Anton's getting away!":
            $menuhideborder = False
            show rion jacket pin surprised at left2 behind ecmc:
                xoffset 90
            show ecmc nojacket_v1 pin determined at right2:
                xoffset -140
            mcrion "We don't have time for this, Rion."
            show ecmc nojacket_v1 pin angry
            mcrion "Anton's going to get away and using your ARCware might be the only way to track him down."
            show rion jacket pin smirk
            "Rion looks at me for a moment, then gives me a small nod."



        "C. Reassure him that you'll only use it to track Anton.":
            $menuhideborder = False
            show rion jacket pin surprised at left2 behind ecmc:
                xoffset 90
            show ecmc nojacket_v1 pin determined at right2:
                xoffset -140
            mcrion "I only want to use your ARCWare to track down Anton, Rion. I promise I won't use it for anything else."
            show rion jacket pin smirk
            ri "I know you won't, [genericfn]."

            "Rion holds my gaze for a moment, then he gives me a small nod."

    show rion jacket pin smirk at left2 behind ecmc:
        xoffset 90
    show ecmc nojacket_v1 pin determined at right2:
        xoffset -140
    ri "I don't mind you using my ARCware, but only because it's you."
    show ecmc nojacket_v1 pin smile
    "I can't help but smile at that as I take Rion's ARCware from him and connect my own to it."
    show rion jacket pin surprised
    ri "What are you doing?"

    mcrion "I'm running a special data analysis program to analyze the phone call."

    mcrion "I should be able to track down the coordinates of the device Anton used to make the call to your ARCware."
    show ecmc nojacket_v1 pin surprised
    "I make a few adjustments to the codes, then I see a light start blinking on the office map."

    mcrion "I found him! He's near the lobby, but he's about to leave."
    hide ecmc
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    "Rion takes my hand and starts to direct me down the hallway."

    ri "Stay close to me, [genericfn]."

    ri "We're going to catch Anton! There's no way we can let him leave!"
    scene bg ecm_office_hq_on at bg
    stop music
    play music ecmaction1

    show anton casual basic at centre
    with wiperightdissolve
    "Rion and I sprint down the hallways then we burst into the main room just as Anton is about to escape the building."
    hide anton
    show ecmc nojacket_v1 pin angry at right3
    show rion jacket pin angry at left3
    mcrion "He's getting away!"

    ri "Anton! Stop!"
    hide ecmc
    hide rion
    show anton casual basic at centre, step_out
    "Rion yells after Anton, but Anton breaks into a sprint as he heads from the doors."
    hide anton
    show rion jacket pin angry at centre
    ri "There's no way I'm letting you get away now!"
    show anton casual angry at centre:
        pause 0.2
        easein 0.2 xoffset 50
        pause 0.1
        easein 0.5 yoffset 540
    show rion jacket pin angry at left4 behind anton:
        easein_back 0.4 xoffset 200
        pause 0.1
        easein 0.3 yoffset 540
    "Rion sprints as fast as he can, then just jumps on Anton, tackling him to the ground."
    hide rion
    hide anton
    show ecmc nojacket_v1 pin surprised at centre
    mcrion "Rion!"
    hide ecmc
    show ecmc nojacket_v1_cu pin_cu surprised_cu at ecmc_cu
    "(I should contact security!)"
    hide ecmc
    show ecmc nojacket_v1 pin angry at centre
    "I push the emergency button as Rion and Anton wrestle on the floor."
    hide ecmc
    "After struggling for a bit, Anton manages to get to his feet, but Rion expertly knocks him down."

    show ecmc nojacket_v1_cu pin_cu surprised_cu at ecmc_cu
    "(This reminds me a bit of the struggle at the dumpster on my first day.)"
    show ecmc nojacket_v1_cu pin_cu angry_cu
    "(Of course, I didn't know the masked man was Anton then.)"
    hide ecmc
    show ecmc nojacket_v1 pin angry at centre
    "Part of me wants to jump in and join Rion, but I know this is his fight."
    show ecmc nojacket_v1 pin surprised
    "As I watch, more D.I.V.A.A. employees come out and start to form a circle around the guys as everyone watches in shock."
    hide ecmc
    show rion jacket pin angry at left2
    show anton casual angry at right2 behind rion
    ri "You're not getting away, Anton. You're finally going to pay for all those deaths!"
    hide rion
    hide anton
    show anton casual_cu angry_cu at anton_cu:
        zoom 1.1 xpos 800
    show rion jacket_cu angry_cu at rion_cu:
        xpos 0
    an "They weren't just deaths, Rion. Everything I did was for the greater good."

    an "You're just not intelligent enough to see that."
    hide anton
    hide rion
    show rion jacket_cu pin_cu angry_cu at rion_cu
    "I hear the shocked gasps and explanations from my colleagues around me, but I tune them out as I focus on Rion."
    hide rion
    show anton casual angry at right1plus:
        pause 0.2
        easein 0.3 yoffset 250
    show rion jacket pin angry at left1:
        easein_back 0.3 xoffset 50
    "Anton once more manages to get to his feet, but Rion sweeps his legs out from under him."

    ri "It's over, Anton."
    show rion jacket angry:
        easein 0.5 yoffset 100
    "Rion rolls Anton onto his stomach and quickly cuffs him."

    ri "You're not getting out of this one."
    show anton casual smile
    "Anton turns his head to look up at Anton with a smirk."

    an "Well, it took you long enough."

    an "I was right under your nose the entire time, but you needed the help of a {i}Hatchling{/i} to get me!"

    "Anton scoffs, mockingly, as he continues to smirk at Rion."

    an "So much for being one of D.I.V.A.A.'s best agents."
    show anton casual angry
    "Rion doesn't respond, but he digs his knee forcefully into Anton's back."

    ri "Where is Blythe?"
    show anton casual smile
    "Anton laughs and shrugs his shoulders under Rion's hold."

    an "As if I'd tell you that."

    "Anton's smirk gets wider."
    hide rion
    hide anton
    show anton casual_cu smile_cu at anton_cu
    an "You may think I'm a bad person, Rion, but we both know that you've had to deal with someone even worse in your past."

    an "My crimes could never compare to {i}his{/i}."
    hide anton
    show rion jacket_cu pin_cu angry_cu at rion_cu
    "I watch as Rion's eyes flash in anger, but he manages to keep calm."
    hide rion
    show ecmc nojacket_v1_cu pin_cu surprised_cu at ecmc_cu
    "(I wonder what happened in Rion's past? We've never really spoken about that.)"
    hide ecmc
    show ecmc nojacket_v1 pin surprised at centre
    "Just then, I hear footsteps and I turn to see the security guards finally arriving."
    hide ecmc
    show rion jacket pin angry at left3
    show anton casual angry at right3
    "They walk straight over to Anton and lift him up. He struggles against them, but with the cuffs on, he's unable to fight."

    an "I'll get you for this, Rion."
    show rion jacket pin smirk
    "Rion smirks at Anton and shakes his head."

    ri "It's over, Anton. I beatr you and there's no chance you're ever getting off the hook."

    scene bg ecm_dominick_office_day at bg
    stop music
    play music ecmmctheme

    show gael uniform glasses basic at left3
    show dominick uniform pin headpiece basic at right3
    with wiperightdissolve

    "Later that day, I'm summoned into Dominick's office and when I enter I'm surprised to see Gael standing beside Dominick's desk."
    hide gael
    show ecmc jacket_v2 pin basic at left3
    mcrion "You wanted to see me, Dominick?"

    do "Yes, Hatchling. There's a couple things I'd like to talk to you about, but first, Gael would like to say something."
    hide dominick
    show gael uniform glasses smile at right3
    "I turn to face Gael, who smiles at me in a friendly way."

    ga "[genericfn], since you were so invested in the recent case, I wanted to personally give you an update."

    ga "The F.D.I. now considers the case closed and the F.D.I. takeover complete."

    ga "While you and Rion didn't exactly follow our protocols, I can't deny that things worked out."

    ga "I've already spoken to Rion, and he spoke very highly of you."

    ga "He made it clear that this investigation would not have been solved so quickly if it wasn't for you."
    show ecmc jacket_v2 pin smile
    "I can't help but grin at Gael's words."
    hide gael
    hide ecmc
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu

    "(Rion really said that?)"

    hide ecmc
    show gael uniform glasses smile at right3
    show ecmc jacket_v2 pin basic at left3
    mcrion "Thanks, Gael."
    hide gael
    show dominick uniform pin headpiece basic at right3
    do "Rion also spoke to me, [genericfn]."

    "I turn to look at Dominick, whose expression stays stoic."

    do "Rion has officially recommended you for a promotion, which I'll begin reviewing as soon as possible."

    do "However, before that is completely reviewed and before it's approved- IF it's approved- there's something else we need to discuss."
    show ecmc jacket_v2 pin surprised
    mcrion "What's that?"

    do "As you know, typically Hatchlings are required to work with different trainers."

    do "At Rion's request, I made a special exemption for you, however now that the case has been solved, that will be coming to an end."
    show ecmc jacket_v2 pin sad
    "I feel my heart sink, but I do my best to not show my disappointment on my face."
    show ecmc jacket_v2 pin determined
    mcrion "I understand."

    do "Good. So tomorrow morning, you'll be expected to meet with the other trainees in the meeting area for your new trainer assignment."

    "I nod, still doing my best to not show my true feelings."
    hide ecmc
    hide dominick
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(I knew it had to come to an end eventually... but I wasn't expecting it to end so soon!)"
    show ecmc jacket_v2_cu pin_cu sad_cu
    "(I'm sure the others trainers are great, but none of them will compare to Rion.)"
    hide ecmc
    show ecmc jacket_v2 pin determined at left3
    show dominick uniform pin headpiece basic at right3
    do "Well, that's all I needed to talk to you about, [genericfn]. You may leave."
    hide dominick
    show ecmc jacket_v2 pin surprised
    show gael uniform glasses basic at right3
    "I'm about to walk out of Dominick's office when Gael stops me."
    show ecmc jacket_v2 pin determined
    ga "Before you leave, I just wanted to give you an official thank you on behalf of the F.D.I. for contributing to solving the case."
    hide ecmc
    hide gael
    show gael uniform_cu glasses_cu smile_cu at gael_cu
    ga "Gael gives me a real, genuine smile, her eyes twinkling."

    "Something tells me we'll cross paths again, [genericfn]."
    hide gael
    show ecmc jacket_v2 pin sad at centre
    "I nod, then turn and leave Dominick's office, my heart still sinking."
    hide ecmc
    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(Even though I knew my arrangement with Rion was temporary, I kind of forgot about the time limit.)"

    "(I wish it didn't have to end.)"
    scene bg ecm_dorm_hallway_on at bg
    stop music
    play music ecmcalmeveryday1
    show rion jacket pin basic at centre
    with wiperightdissolve

    "I reluctantly walk out of Dominick's office to find Rion right outside, leaning against the wall."
    hide rion
    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin surprised at right3
    mcrion "Rion! I wasn't expecting to see you."
    show rion jacket pin smirk
    ri "I thought I'd check on you to see how you're doing."

    ri "It's been an eventful day."
    show rion jacket pin sad at left3:
        easein 0.4 xoffset 120
    "Rion moves off the wall and takes a few steps toward me, his eyes filled with concern."

    ri "Are you okay, [genericfn]? Youy don't have any injuries do you? I should have checked before."
    hide rion
    hide ecmc
    $menuhideborder = True
    menu rions1e12c2:
        "A. Reassure Rion that I'm fine.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at right3
            show rion jacket pin sad at left3
            mcrion "I'm fine, Rion. I've already been checked out by the medical team."

            mcrion "All my injuries have healed and the gas won't do any lasting damage."

        "B. Tell Rion that I'm just tired.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at right3
            show rion jacket pin sad at left3
            mcrion "I'm fine Rion. Just a bit exhausted after everything that happened today and our all-nighter last night!"

            ri "That's understandable."


        "C. Tell Rion to stop fussing.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at right3
            show rion jacket pin sad at left3
            mcrion "I'm fine, Rion. You don't need to make a fuss."

            mcrion "You know I've already been checked out by the medical team."

            ri "I know, but I still worry about you."
            show ecmc jacket_v2 pin surprised
            show rion jacket pin smirk
            "Rion gives me a lopsided smile that causes my hear to beat faster."

            mcrion "Well, there's nothing to worry about. I'm completely fine."

    show ecmc jacket_v2 pin smile at right3
    show rion jacket pin angry at left3
    "Rion narrows his eyes at me as he studies my face."

    ri "I can tell something's bothering you."

    ri "What's going on, [genericfn]?"
    show ecmc jacket_v2 sad
    "My face heats a little as I think about what's bothering me."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I can't tell Rion the truth! I don't want him to think I'm clingy or anything.)"
    hide ecmc
    show ecmc jacket_v2 pin surprised at right3
    show rion jacket pin angry at left3
    mcrion "It's nothing. I was just... thinking about my new trainer assignment tomorrow."
    hide ecmc
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    "Rion's gaze meets mine and I see something pass in his eyes."
    show rion jacket_cu smirk_cu
    ri "I have an idea. Why don't we grab coffee together tomorrow morning before the trainer assignments are handed out?"

    ri "We can call it a celebration."
    hide rion
    show rion jacket pin smirk at left3
    show ecmc jacket_v2 pin embarrassed at right3
    mcrion "Do you mean like... actually meet you inside?"

    "Rion smirks and nods."

    ri "Yes. We can grab coffee together at Data Drip."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Oh my Gosh! I can't believe rion's finally inviting me to get coffee with him!)"
    hide ecmc
    show rion jacket pin smirk at left3
    show ecmc jacket_v2 pin smile at right3
    mcrion "Sure! I'd love that!"
    show ecmc jacket_v2 blush smile
    "I blush as I realize how enthusiastic I sound."
    show ecmc jacket_v2 embarrassed
    mcrion "I mean... that sounds good."
    show rion jacket smile
    ri "Great. I'll see you tomorrow, bright and early."

    scene bg ecm_sidewalk_day at bg
    stop music
    play music ecmromantic3
    show ecmc jacket_v2 pin embarrassed at centre
    with wiperightdissolve
    "I show up at Data Drip, bright and early, buzzing a little from a mixture of nerves and excitement."
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Hmm... I can't see Rion inside. I guess I'll just wait for him out here.)"
    hide ecmc
    show ecmc jacket_v2 pin embarrassed at centre:
        easein 0.2 yoffset -30
        easein 0.2 yoffset 0
    "I bounce a little in excitement and try to calm myself down."
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I shouldn't get my hopes up. I'm sure rion was just being polite.)"
    show ecmc jacket_v2_cu surprised_cu
    "(I know no one's acxtually gone to Data Drip with him yet, but I'm sure it's not a big deal... right?!)"
    hide ecmc
    show ecmc jacket_v2 pin embarrassed at centre
    "I start to nervously adjust my outfit, hoping it looks perfect, while I shuffle from one food to the other."
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I wonder if Rion will invite me to have coffee with him again? Or will this just be a one off?)"
    hide ecmc
    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin embarrassed at right3
    "I'm so caught up in my thoughts, that I don't see Rion walk up to me."
    show rion jacket smile
    ri "Good morning, [genericfn]."
    show ecmc jacket_v2 surprised at right3:
        easein 0.2 yoffset -30
        easein 0.2 yoffset 0
    "I jump slightly and turn it to Rion with a grin."
    show ecmc jacket_v2 smile
    mcrion "Good morning, Rion."

    ri "Ready to go inside?"

    "I nod, not trusting myself to speak, then I follow Rion into the cafe."

    scene bg ecm_cafe_day at bg
    show rion jacket pin smile at centre
    with wiperightdissolve
    "As I walk into Data Drip with Rion, I can't help but notice that he seems more relaxed than normal."

    $sidecharone = "Elderly Hipster"
    sid1 "Rion! It's good to see you."

    sid1 "Did you catch the Invaders game? I always think of you when they lose."
    show rion jacket smirk
    "Rion chuckles and smirks at the older man."

    ri "So that means you think about me every time they play!"

    "Rion chuckles, then he leads me to the counter, saying hello to a few people on the way."
    show rion jacket smirk at left3
    show ecmc jacket_v2 pin surprised at right2
    mcrion "Do you know everyone here?"
    show rion jacket smile
    ri "Just the regulars, but most people who come here are regulars."
    show ecmc jacket_v2 smile
    "We reach the counter and the barista's face lights up."

    $sidechartwo = "Barista"

    sid2 "Rion! It's so nice to see you after you didn't show up yesterday."
    show rion jacket smirk
    ri "Sorry, Flora. Duty called."

    "The barista's eyes stray to me, then they widen in understanding."
    show ecmc jacket_v2 surprised
    sid2 "Is this the Hatchling you've been talking about?"
    show ecmc jacket_v2 blush embarrassed
    ri "Rion nods and I blush."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(Rion's been talking about me?!)"
    hide ecmc
    show rion jacket pin smirk at left3
    show ecmc jacket_v2 pin blush embarrassed at right2
    "Rion goes to order, but instead of his own drink, he orders mine."
    show rion jacket smile
    ri "I know your order off by heart now."
    show rion jacket smirk
    show ecmc jacket_v2 -blush smile
    "I laugh and order Rion's order in return."
    show ecmc jacket_v2 blush smile
    mcrion "And now I know yours."
    show rion jacket basic
    show ecmc jacket_v2 -blush basic
    "After the barista makes our drinks, I follow Rion to a quiet corner of the cafe."
    show rion jacket smile
    ri "This is my regular spot. I always sit here if I can."

    "I sit down across from Rion, who then holds up his coffee cup."

    ri "Cheers to finally solving the case."
    show ecmc jacket_v2 smile
    "I lightly clink my cup with Rion's before taking a sip."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Oh, this is good! I can see why Rion likes it!)"
    hide ecmc
    show rion jacket pin smile at left3
    show ecmc jacket_v2 pin smile at right2
    ri "So, I wanted to thank you again for all your hard work on the case, [genericfn]."

    ri "Your knowledge of electrionics and hardware really came in handy."

    mcrion "Thanks, Rion. It was a pleasure working with you too."

    "I trail off as I remember that our time working together is about to come to an end."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(It was fun while it lasted.)"
    hide ecmc
    show rion jacket pin smile at left3
    show ecmc jacket_v2 pin determined blush at right2
    mcrion "So.. do you come here to Data Drip every morning?"
    show ecmc jacket_v2 -blush smile
    ri "Pretty much. The only time I don't is when I'm stuck in the office overnight like last time."
    show rion jacket smirk
    show ecmc jacket_v2 blush embarrassed
    "Rions winks at me and I blush a little more."

    ri "I've never actually brought anyone in here before."
    show rion jacket smile
    ri "I like to come here every morning to start each day with relaxation and a clear mind."
    show ecmc jacket_v2 -blush surprised
    mcrion "Have you tried any other cafes?"

    ri "A few. I've definitely been to every cafe near the office."
    show rion jacket smirk
    ri "This is the only one that makes my coffee {i}perfectly{/i} every single time."
    show ecmc jacket_v2 basic
    "I take another sip of my coffee when Rion pulls a small, pretty box out of his pocket."
    show rion jacket smile
    ri "I have something for you, [genericfn]. This was a long time coming."
    show ecmc jacket_v2 surprised
    "I stare at the box, as my mind starts racing frantically."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(What's that?! What could it be? Is it jewelry? It looks like jewelry!)"

    "(I didn't know Rion and I were at the gift-giving stage of our relationship??? Maybe I should have gotten him something?)"

    "(Wait! We're not even in a relationship!)"
    hide ecmc
    show rion jacket pin smile at left3
    show ecmc jacket_v2 pin smile at right3
    "I try to push my spiraling thoughts away as I smile at Rion."

    mcrion "Thank you, Rion, but you didn't have to get me anyhthing!)"

    ri "A successful first case deserves a reward, [genericfn]."
    show rion jacket smile at left3:
        pause 0.1
        easein 0.5 left1
    "Rion smiles at me, then he reaches across the table to put his hand on top of mine."

    ri "You don't need to open it now. You can open it later when you're alone, if you'd like. But I really would like to see you open it in front of me."
    hide ecmc
    hide rion
    show rion jacket_cu smile_cu at rion_cu
    "Rion grins at me."

    ri "I want to see if I got it right!"
    hide ecmc
    hide rion
    $menuhideborder = True
    menu rions1e12c3:

        "A. open Rion's gift right now!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show rion jacket pin smile at left1
            show ecmc jacket_v2 pin smile at right3:
                pause 0.1
                easein 0.4 right1plus
            "I take the box and grin back at Rion."

            mcrion "I'll open it right now!"
            show ecmc jacket_v2 surprised
            "I open the box and gasp when I see a badge inside."

            "I pick it up carefully, inspecting the intricate buttons and engraved lines."
            hide rion
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(This is light... but I know it's extremely strong. I won't be able to break it easily.)"
            hide ecmc
            show rion jacket pin smile at left1
            show ecmc jacket_v2 pin surprised at right1plus
            "I turn to Rion in shock, the bracelet in my hand."

            mcrion "Did you seriously get me a Bot & Co OmniTool?!"
            show ecmc jacket_v2 smile
            "I stare at the badge in wonder, taking in the sleek black metal and red and cyan accents that almost match Rion's earrings."
            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(This is absolutely stunning. I can't believe Rion really got this for me!)"
            hide ecmc
            show rion jacket pin smirk at left1
            show ecmc jacket_v2 pin smile at right1plus
            ri "Technically, {i}I{/i} didn't buy it. Well, most of it, anyway."

            ri "I used the D.I.V.A.A. training budget for the bulk, then I covered the rest."
            hide ecmc
            hide rion
            show rion jacket_cu smile_cu at rion_cu
            "I start to put the badge on, then Rion leans across the table."

            ri "Let me."

            "Rion deftly fastens the badge to my lapel and I tense slightly at his proximity, my heart beating slightly faster."
            hide rion
            show rion jacket pin smirk at left1
            show ecmc jacket_v2 pin surprised at right3:
                xoffset -140
            "After a couple moments, Rion pulls back, and I look down at my new badge in awe."

            mcrion "I can't believe you got me an omni tool! This thing is supposed to be amazing!"
            show ecmc jacket_v2 smile
            mcrion "I'll be able to store and execute all kinds of data scripts, plus I'll be able to unlock anything your omnipick can!"
            show rion jacket smile
            ri "Don't forget all the other tasks it can do. It even as a soldering iron!"

            mcrion "Data tasks will be much easier too. This bracelet can even safely buffer ARCware to terminal connection!"

            "I look at my new bracelet in awe, then I turn to Rion."

            mcrion "Thank you, Rion. This was a great gift!"

            mcrion "It will obviously be helpful for work, but it'll be useful for scrapping as well!"

            "Rion smiles at my excitement."
            hide ecmc
            hide rion
            show rion jacket_cu blush_cu smile_cu at rion_cu
            ri "I'm glad I bought you something that you actually like!"

            "As Rion speaks, a slight blush stains his cheeks."
            hide rion
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(Is Rion actually blushing? Or is that a trick of the light?"
            show ecmc jacket_v2_cu smile_cu
            mcrion "I really do like it, Rion."

            "I look down at my bracelet, my heart feeling warm."

            "(I know Rion said he used the training budget for this, but it still feels like a real gift from him.)"

            "(He clearly put a lot of thought into it.)"

            mcrion "This is the perfect gift, but you shouldn't have!"
            hide ecmc
            show rion jacket_cu smirk_cu at rion_cu
            "Rion shakes his head."

            ri "After all the hard work you did, you deserve it."
            show rion jacket_cu smile_cu
            ri "While working together, it was clear to me that you were due for an upgrade! The toold you had were too basic for our missions."

            ri "If you feel weird accepting a gift, consider this a work tool."

            "I lightly run my fingertip over the smooth metal of the took."
            hide rion
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(I'd definitely rather think of it as a gift. I still can't believe Rion bought me something so sweet and thoughtful.)"

        "B. Open it later.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at right3
            show rion jacket pin smile at left1
            mcrion "If you don't mind, Rion, I think I'll open it at home later when there's less pressure."
            show rion jacket pin basic
            "Rion shrugs."
            show rion jacket pin smirk
            ri "Alright, but you {i}will{/i} need to open it soon."
            show ecmc jacket_v2 pin smile at right3:
                easein 0.4 xoffset -140
            "I take the box from Rion, my curiosity piqued."
            hide rion
            hide ecmc
            show ecmc jacket_v2 pin_cu surprised_cu at ecmc_cu
            "(I really wonder what's inside!)"
            hide ecmc
    show rion jacket pin basic at left1 behind ecmc
    show ecmc jacket_v2 pin basic at right3:
        xoffset -140
    "Rion and I finish off our coffees, then he glances at his watch."
    show rion jacket pin smile
    ri "We should go. It's almost time to get back to work."
    show ecmc jacket_v2 pin sad
    "I feel a pang in my chest as I realize that this could be the last time I see Rion for a while."
    show ecmc jacket_v2 pin smile
    mcrion "Well... Thank you, Rion. I really appreciate you taking me under your wing for the case."
    show ecmc jacket_v2 pin embarrassed
    "I pause as I try to think of what to say."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu pin_cu embarrassed_cu at ecmc_cu
    "(I want Rion to know that I'd like to still see him... but I don't want it to sound awkward.)"
    hide ecmc
    show rion jacket pin smile at left1 behind ecmc
    show ecmc jacket_v2 pin embarrassed at right3:
        xoffset -140
    mcrion "It would be... nice... to see you around again."
    show ecmc jacket_v2 pin blush embarrassed
    "I blush at how awkward that sounded and twist my hands in my lap."
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(Why do I always have to fumble things in front of Rion?)"
    hide ecmc
    show rion jacket pin smile at left1 behind ecmc
    show ecmc jacket_v2 pin blush embarrassed at right3:
        xoffset -140
    "Rion looks me in the eyes, his expression thoughtful."
    stop music
    play music ecmintrotrack
    "Finally, he speaks, a slight smirk tugging on his lips."

    ri "Well, you'll definitely see me around again, [genericfn]."

    "Rion's smirk gets a little wider."

    ri "I cleard this with Dominick yesterday. You're going to be my trainee until you're fully promoted to Fledgling."
    hide ecmc
    show ecmc jacket_v2 pin surprised at right3:
        xoffset -140
    "I stare at Rion in shock."

    mcrion "What?! How is that even allowed?"

    "Rion winks at me."

    ri "I have my ways."

    "Rion stands up and helps me to my feet."
    hide ecmc
    hide rion
    show rion jacket_cu pin_cu smile_cu at rion_cu
    ri "Now come on. We have to go or we'll be late!"
    hide rion
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    mcrion "Late for what?"
    hide ecmc
    show rion jacket_cu pin_cu smile_cu at rion_cu
    ri "There was a huge case involving a rogue android that I had to put on pause to follow leads on the Anton case."

    ri "We have to work fast before this case goes cold!"
    hide rion
    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    "I follow Rion out of Data Drip, my heart bursting with a mixture of excitement and anxiety."

    "({i}Yes!{/i} Another case with Rion. and I can't believe he's going to be my trainer until I get promoted!)"

    "(I wonder what's in store for us next...)"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
    #                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
