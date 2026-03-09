label maxime_season1_episode9:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg
    play music msctense

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc casual_hairdown basic at centre
    "The following day, I'm at the surf shop for my shift, still trying to process the news."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(I can't believe another competitor went missing... What if Wikus moves too fast for us to stop him? We have to save the missing surfers!)"
    show mscmc casual_hairdown sad at centre
    "I remember Maxime's grim, determined expression when Trina broke the news, and try to console myself."
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(It's alright, [genericfn]. Maxime won't let anything happen to you, and he's going to go after the missing surfers.)"
    show mscmc casual_hairdown_cu sad_cu
    "(I wish he was here, or I was with him, but he had to meet with Camilla about the latest developments.)"
    hide mscmc
    show trina casual basic at centre, step_in
    so "Hey girl."
    "Trina greets me dully as she enters from the back room, looking nothing like her ususal exuberant self."
    show mscmc casual_hairdown sad at left2
    show trina casual basic at right2
    mcmax "Hey. You doing okay?"
    show trina casual sad:
        ease 0.6 xoffset -80
    "She shakes her head, slumping at the counter beside me."

    play music mscsadtimes
    so "I'm worried—actually, I'm scared."
    so "All these disappearances... We've never had anything like this happen here before."
    so "And I'm scared for you because you're a surfer in a competition that keeps having contestants vanish. Is that selfish?"
    mcmax "Aw, Trina, don't talk like that."
    show mscmc casual_hairdown smile behind trina:
        ease 0.4 xoffset 110
    "I reach out, squeezing her shoulder affectionately."
    mcmax "You don't need to be afraid on my behalf."
    mcmax "I can keep myself out of trouble, and I've always got my rockstar trainer as backup."
    show mscmc casual_hairdown grin
    show trina casual basic
    "I grin with a confidence I don't quite feel."
    hide trina
    hide mscmc
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Truth be told, my stomach's in knots too, but I don't want to dwell on it too much. I really want to finish the tournament.)"
    show mscmc casual_hairdown_cu sleep_cu
    "(I can't let fear affect my performance, not when I've come so far.)"
    show mscmc casual_hairdown basic behind trina at left1:
        xoffset 30
    show trina casual basic at right1
    "Trina sighs wistfully."
    so "You're a tough one, [genericfn]. What gets me is not knowing what happened to them. It's all a big question mark."
    show trina casual sleep
    so "Pete at the taco truck thinks they were abducted by aliens, but Pete thinks everything is aliens."
    show mscmc casual_hairdown smile
    show trina casual smile
    mcmax "Trina, I can at lesat promise you it's not aliens."
    "Trina chuckles, and I'm relieved that I at least coaxed a smile out of her."
    show trina casual basic
    so "Yeah, I guess that's something. I've got to go check the books, are you okay out here?"
    show trina casual sleep at out_right
    "I nod, sighing once I'm alone in the store."
    show mscmc casual_hairdown basic
    play sound "audio/sfx/bell-store-entrance-ding.mp3"
    "The silence doesn't last long before the bell above the door jingles."
    hide mscmc
    show javier casual basic at centre, step_in
    jv "Hey, [genericfn]."
    show javier casual sad
    "Even Javier looks deflated, and his perfect beachy hair seems flatter than usual."
    show mscmc casual_hairdown smile at left3
    show javier casual smile at right3
    mcmax "What, no snappy nickname?"
    "He shrugs with a rueful smile."
    show mscmc casual_hairdown basic
    show javier casual basic
    jv "I'm a little on edge."
    show mscmc casual_hairdown surprised
    show javier casual smile
    jv "I actually came to check on you..."
    hide javier
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(Most of the time he's kind of exasperating, in a good way. I forget he can also be sweet.)"
    show mscmc casual_hairdown grin at left3
    show javier casual smile at right3
    "I rummage in Trina's small drinks fridge, and slap a sports drink on the counter in front of him."
    show mscmc casual_hairdown smile
    show javier casual basic
    mcmax "Here, I'm giving you some electrolytes on the house. I'm doing fine, but yeah, it's all a lot."
    show mscmc casual_hairdown grin
    show javier casual smile
    mcmax "We need to get that saucy gleam back in your eye."
    show mscmc casual_hairdown smile
    show javier casual smile:
        ease 0.4 xoffset -30
        pause 0.1
        ease 0.4 xoffset 0
    pause 1.0
    "Javier snickers and accepts the drink."
    show mscmc casual_hairdown grin
    jv "Thanks. I owe you one, ocean princess."
    show mscmc casual_hairdown basic
    show javier casual basic behind maxime:
        ease 0.4 xoffset 40
        ease 0.3 xoffset -80
    show maxime casual basic at right5,right_in
    pause 0.4
    show maxime casual basic:
        ease 0.3 xoffset 60
    "He raises the drink to me before heading out, and nearly bumps into Maxime in the doorway."
    show javier casual smile
    jv "Oh, hey."
    show maxime casual basic
    mx "Hey..."

    play music mscsurfshop
    show mscmc casual_hairdown basic
    show javier casual smile at out_right
    show maxime casual basic:
        ease 0.4 xpos stagepos[1]+180
    pause 0.4
    "Maxime watches him go, then turns all his attention to me."
    show mscmc casual_hairdown basic
    show maxime casual sad
    mx "How are you holding up?"
    show mscmc casual_hairdown sad
    "I consider lying again, but one look in his soft hazel eyes makes me crumple."
    mcmax "Honestly, I could really use someone to talk to—someone who understands what's actually going on."
    show maxime casual sad behind mscmc:
        ease 0.8 xpos stagepos[1]+20
    pause 0.8
    show mscmc casual_hairdown sad:
        ease 0.4 xoffset 50
    pause 0.4
    "Maxime nods, pulling up a chair beside the counter, and takes my hand in his."
    show maxime casual basic
    mx "Talk to me."
    show mscmc casual_hairdown sleep
    "I sigh, half relieved, half ashamed."
    show mscmc casual_hairdown sad
    mcmax "I'm getting scared. Since the second disappearance I've been wondering if maybe I should pull out of the competition."
    "Maxime's voice is gentle and free of judgement when he replies."
    mx "Do you want to pull out?"
    show mscmc casual_hairdown angry
    mcmax "No, of course not—I want to surf in the final and win!"
    hide mscmc
    hide maxime
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime squeezes my hand, his gaze holding mine."
    mx "It's natural to be afraid—we're all on edge. But you're also one of the bravest, boldest people I've ever met."
    show maxime casual_cu basic_cu
    "I scuff my shoe, not fully convinced, as Maxime glances out the window."
    show maxime casual_cu embarrassed_cu
    mx "Actually, do you have a breaking coming up or are you off soon?"
    mx "There's some place special I want to show you. Maybe I can help remind you how brave you are."
    hide maxime
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcmax "A special place?"
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    "Maxime smiles mysteriously and his cheeks redden just the slightest bit."
    mx "I can promise it's somewhere you've never been before. I know you'll like it. Want to find your courage with me?"

    hide maxime
    $menuhideborder = True
    menu maximee09c1:
        "A. Find your courage with Maxime!" (paidchoice = "paidchoice"):
            play music mscmaxime
            $menuhideborder = False
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mcmax "Going somewhere special with you sounds perfect right now!"
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "I succeed in flustering him, but he quickly recovers, and stares into my eyes."
            show maxime casual_cu smile_cu
            mx "Yes! I mean, I'm glad. Let me help you lock up."
            hide maxime
            scene bg msc_labeach_day at bg with wiperightdissolve
            "Maxime leads me along the beach until he takes a sudden turn, walking towards the foothills at the end of the boardwalk."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(I wonder where we're going? As far as I know, there's not much here—no hiking trails or anything.)"
            hide mscmc
            show maxime casual smile at centre
            mx "Over here."
            show mscmc jacket_hairdown surprised at left3
            show maxime casual smile at right3
            "Maxime beckons to me, and I'm surprised to suddenly feel a pebbled path beneath my shoes."
            show maxime casual basic
            mcmax "I didn't know this was here..."
            hide mscmc
            show bg msc_labeach_sunset at bg
            show maxime casual smirk at centre
            "As the sun begins to set, Maxime grasps a large branch and pulls it aside, and it's as though he's drawn back a curtain."
            hide maxime
            show mscmc jacket_hairdown surprised at centre
            mcmax "Oh my god!"
            hide mscmc
            scene bg msc_waterfall_sunset at bg with wiperightdissolve
            "I stare in wonder at the glistening waterfall in front us, watching it splash into a deep rock pool of emerald green."
            show mscmc jacket_hairdown surprised at left3
            show maxime casual smile at right3
            mcmax "There's a waterfall here?! Why have I never seen or heard of this being here before?"
            mx "There are a few spots along the coast that are cloaked in mer magic. It's always been here, but hiding."
            hide mscmc
            show maxime shorts_cu smirk_cu at maxime_cu
            "As he speaks, he tugs his shirt up over his head, the muscles in his arms twisting."
            show maxime shorts_cu embarrassed_cu
            "I stand stock still, watching him, until he looks over his shoulder and notices my big eyes."
            show mscmc jacket_hairdown embarrassed at left3
            show maxime shorts embarrassed at right3
            mx "Well, do you want to go in?"
            mcmax "What? Oh, yes! Let me just..."
            show maxime shorts smile
            show mscmc casual_hairdown embarrassed with dissolve
            "My face is burning hot, and I quickly peel off my jacket."
            show maxime shorts smile:
                ease 0.6 xpos stagepos[1]+140
            pause 0.6
            "Maxime gallantly offers me his arm and I thread my own through his, our sides touch as we stand beside one another."
            show maxime shorts smirk
            mx "You ever jumped off a waterfall before?"
            show mscmc casual_hairdown surprised
            show maxime shorts smile
            mcmax "Coming from midwest farm country, no, I have not."
            show mscmc casual_hairdown basic
            "I eye the top of the waterfall dubiously, watching the spray stream down and spatter the rocks."
            show mscmc casual_hairdown smile
            mcmax "So, is this my bravery test?"
            show mscmc casual_hairdown grin
            show maxime shorts embarrassed
            mx "It's not a test. I already know how brave you are, I just want to help you remember."
            show mscmc casual_hairdown embarrassed
            show maxime shorts smirk behind mscmc:
                ease 0.5 xpos stagepos[1]
            pause 0.5
            "In a rare moment of abandon, he cups my chin with his fingers as he stares deeply into me."
            show maxime shorts embarrassed
            mx "{i}You{/i} are so powerful and determined, I know you can achieve everything you want from life."
            show mscmc casual_hairdown grin
            show maxime shorts smirk
            mcmax "I am also a bit of a thrill-seeker, I'll admit. This is going to be fun!"
            hide mscmc
            hide maxime
            "I carefully pick my way up the slick rocks to the top, as Maxime follows, laying a hand on my lower back occasionally to steady me."
            show mscmc casual_hairdown embarrassed at left1,step_in
            show maxime shorts basic behind mscmc at right1plus,step_in
            "(His touch always feels so warm and sets my heart beating like crazy.)"
            show mscmc casual_hairdown smile
            show maxime shorts smirk
            "At the top, I look down and tremble for a moment. Then, I set my hands on my hips in a power pose, psyching myself up."
            show maxime shorts basic
            mcmax "Are you going to jump with me?"
            show maxime shorts smile
            "Maxime smiles at me and I feel giddy."
            mx "Of course. If you want me to, I'll always be there for you."
            show mscmc casual_hairdown embarrassed
            show maxime shorts embarrassed
            "He winks, and I roll my eyes but can't help but blush despite myself."
            show mscmc casual_hairdown grin
            show maxime shorts smirk
            mcmax "Well, don't let me leave you in the dust. You ready? Let's go om three. One... Two... Three!"
            show mscmc casual_hairdown grin:
                ease 0.4 xoffset -80 yoffset -80
                pause 0.1
                ease 0.4 yoffset 700
            pause 0.9
            "We leap off the ledge, and I feel Maxime's hands envelope mine as my heart swells."
            hide maxime
            hide mscmc
            "Any thoughts I had prior are replaced with the thrill of falling. Everything seems so much simpler when you're falling."
            play music mscromance
            scene bg msc_maxime_season1_ei3 at bg with fade:
                
                yanchor 0.6
                linear 8 yanchor 0.1
            pause
            "Maxime whoops as we fall. I turn slightly in mid-air and we lock eyes, his are full of joy and excitement."
            "(Oh, I wasn't expecting that—he looks so carefree and happy!)"
            "(I do feel brave right now! He makes me feel brave and uplifted, and tingly inside.)"
            mcmax "Woohoo!"
            scene bg msc_waterfall_sunset at bg with fade
            show maxime mermaid smirk at centre
            play sound splash03
            "We hit the ater with a thunderous splash, and I kick to the surface as Maxime swims in an arc, flipping his tail."
            hide maxime
            show mscmc casual_hairdown surprised at left1,step_in
            show maxime mermaid smirk behind mscmc at right1plus,step_in
            "I'm stunned by the water's coolness, but it's not unpleasant, it's refreshing."
            show mscmc casual_hairdown grin
            "I feel as though my entire body as come alive, no longer drained by anxiety."
            hide mscmc
            show maxime mermaid_cu embarrassed_cu at maxime_cu
            mx "Did that feel good?"
            "Maxime puts his arm around my shoulders and pulls me close."
            "The contrast between his warm, bare chest and the cool water makes every part of me yearn for him."
            hide maxime
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(He knows exactly how to make me feel better, and he's hot as hell.)"
            mcmax "I feel great! This was just what I needed, coach."
            show mscmc casual_hairdown_cu grin_cu
            mcmax "Thanks for helping me find my courage."
            hide mscmc
            show maxime mermaid_cu smile_cu at maxime_cu
            mx "You never lost it. You just needed a reminder."
            show mscmc casual_hairdown smile at left1
            show maxime mermaid smile behind mscmc at right1plus
            "He lies back on the water, floating and gently propelling himself around me in a slow circle with small movements of his tail."
            "I float on my back too, admiring the canopy of trees overhead and the color streaked sky."
            show mscmc casual_hairdown embarrassed
            mcmax "You should hold my hand again."
            show maxime mermaid surprised
            mx "What?"
            show maxime mermaid embarrassed
            mcmax "Like sea otters do, so we don't float away from each other."
            hide mscmc
            show maxime mermaid_cu embarrassed_cu at maxime_cu
            "Maxime blushes, and then I feel his hand close around mine."
            hide maxime
        "B. You'd better rest.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            mcmax "I'd better rest."
            hide mscmc

    scene bg msc_surfcompetition_day_people at bg with clockwise_wipe
    play music mscsurfcompetition
    show mscmc surfer_hairup basic at left1
    show maxime casual basic behind mscmc at right1plus
    "Maxime gives me Camilla's tracking device as we arrive at the tournament's semi-finals the next day."
    "The device looks like a seashell necklace, but when I hold it, it feels faintly warm in my palm, gently humming."
    show mscmc surfer_hairup grin
    mcmax "This is the most fashionable tracking device I've ever seen! I don't mind it at all."
    mx "Are you alright with my putting it on you?"
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    "I happily lift my chin, letting him clasp the necklace around my neck, his fingers brusing my collarbone as he tucks it into my sun shirt."
    show maxime casual_cu basic_cu
    mx "So we're clear, this doesn't mean you should seek Wikus out. He's got his little plan, let him come to us."
    show maxime casual_cu angry_cu
    mx "And I definitely don't want you alone with him."
    show mscmc surfer_hairup grin at left1
    show maxime casual angry behind mscmc at right1plus
    "I smile consonlingly, laying my hand on his arm."
    mcmax "I've got a tournament to win, and I'm not letting Wikus get in the way of that."
    show mscmc surfer_hairup angry
    show maxime casual basic
    mcmax "Oh, speak of the devil..."
    hide mscmc
    hide maxime
    show wikus casual smile at centre,step_in
    "I node over Maxime's shoulder as Wikus makes his way across the sand to us, wearing a particularly smarmy smile."
    ws "[genericfn]! And how are we today?"
    show mscmc surfer_hairup grin at left3
    show wikus casual smile at right2
    "I smile, trusting my retail experience to hide my true feelings."
    mcmax "I'm doing pretty well. What about you, Wikus?"
    "He throws his arms up expansively."
    ws "I'm {i}ecstatic{/i}. Everything's going perfectly."
    hide mscmc
    show maxime casual basic at left3
    mx "Everything?"
    show wikus casual basic
    "Maxime quirks an eyebrow warily, and he brushes up against me, moving protectively closer."
    show wikus casual angry
    ws "Well, it's a shame about those surfers who wandered off. But otherwise the tournament's going great!"
    hide maxime
    hide wikus
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(It's all I can do not to physically. I hate him!)"
    "(I can't think about this now. I need to get ready for the tournament.)"
    show mscmc surfer_hairup smile at left3
    show wikus casual smile at right2
    mcmax "I'll catch you boys later. I've got to..."

    hide mscmc
    hide wikus
    $menuhideborder = True
    menu maximee09c2:
        "A. Meditate.":
            $menuhideborder = False
            show mscmc surfer_hairup basic at left3
            show wikus casual smile at right2
            mcmax "I'm going to do a little meditation. Got to be in a good headspace for the competition."
            show mscmc surfer_hairup grin at step_out
            "I wave, skipping off quickly and leaving Maxime to question Wikus."
            hide wikus
            hide mscmc
            show mscmc surfer_hairup basic at centre
            "I settle along the edge of the water, but I'm already breathing easier now that I'm away from Wikus."
            hide mscmc
        "B. Pray.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu angry_cu at mscmc_cu
            "(Heh, this is sure to give Wikus food for thought.)"
            show mscmc surfer_hairup basic at left3
            show wikus casual smile at right2
            mcmax "I've got to give my prayers to Poseidon before the tourament starts."
            ws "Is...that something you do?"
            mcmax "It never hurts to cover your bases."
            hide mscmc
            show maxime casual smile at left3
            show wikus casual surprise at right2
            "I turn and make my way to the edge of the water, leaving behind a bewildered Wikus and an amused Maxime."
            hide maxime
            hide wikus
        "C. Do a convoluted luck ritual.":
            $menuhideborder = False
            show mscmc surfer_hairup basic at left3
            show wikus casual smile at right2
            mcmax "Well, I'd better go do my lucky dance! I always swear by it."
            show mscmc surfer_hairup grin at step_out
            show wikus casual surprise
            "Maxime raises a hand in farewell, and I skip awkwardly down the beach, hopping from foot to foot before bending to pick up a seashell."
            hide wikus
            hide mscmc
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(Yeah, lucky dance is totally plausible.)"
            hide mscmc

    show trina casual smile at centre
    so "[genericfn]!"
    show trina casual basic
    so "Uh, what are you doing?"
    show trina casual smile
    "Trina cocks her head at me."
    show mscmc surfer_hairup surprised at left3
    show trina casual basic at right3
    mcmax "The simplest answer is that I'm trying to clear my head before I go out on the water."
    show mscmc surfer_hairup sad
    mcmax "There's...a lot going on."
    show trina casual smile
    "She smiles understandingly."
    so "I get you. I know everything's weird and scary right now, but you got this."
    show mscmc surfer_hairup smile
    so "The water is your element."
    show trina casual smile behind mscmc:
        ease 0.5 xpos stagepos[1]-60
    pause 0.5
    "She places her hands on my shoulder, and encourages me to take a deep breath."
    show mscmc surfer_hairup sleep
    "I shut my eyes, remembering Maxime and Trina's words."
    hide trina
    show mscmc surfer_hairup_cu sleep_cu at mscmc_cu
    "(Breathe with the ocean...Water is my element...)"
    "(Let go, and be free.)"
    show mscmc surfer_hairup smile at left3
    show trina casual smile behind mscmc at centre:
        xoffset -60
    mcmax "Okay, I think I'm getting there."
    mcmax "Thanks, Trina."
    so "No problem."
    hide mscmc
    hide trina
    show trina casual_cu smile_cu at trina_cu2:
    "She hugs me briefly, then glances at the podium, where the judges are settling in."
    so "You'd better get to the starting line. We'll be cheering for you!"
    so "You've got this, [genericfn]. We all love you not matter what."

    hide trina
    scene bg msc_ocean_wide_day at bg with clockwise_wipe
    show mscmc surfer_hairup basic surfboard at centre
    "I set my shoulders back as competitors line up, my gaze out towards the horizon."
    show mscmc surfer_hairup_cu angry_cu -surfboard at mscmc_cu
    "(Alright, ocean. I'm [genericfn], and I love to surf, so that's what I'm going to do.)"
    "(I'm not going to think about the judges, or the scoring, or Wikus Sapor.)"
    show mscmc surfer_hairup_cu grin_cu
    "(The ocean can't be anything other than itself. And I can't be anyone other than myself.)"
    show mscmc surfer_hairup grin at centre:
        pause 0.2
        ease 0.6 xoffset 180 yoffset 100
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 190
        ypos 360
    pause 0.8
    "When the klaxon blows, I'm ready."
    "I ignore all the colorful surfboards and swimsuits surrounding me, keeping my attention on the incoming waves."
    hide surfboard_acc_back
    hide mscmc
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(I'm not going to obsess about points or scores.)"
    show mscmc surfer_hairup grin:
        xoffset 180
        yoffset 100
        pause 0.2
        ease 0.6 xoffset 30 yoffset 50
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 190
        ypos 360
    pause 0.8
    "I find a good wave with a hefty swell, catch it, and pop up onto my feet."

    hide surfboard_acc_back
    hide mscmc
    $menuhideborder = True
    menu maximee09c3:
        "A. Barrel.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at centre:
                xoffset 30
                yoffset 50
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            "I can sense that the wave is going to have a huge arc."
            hide surfboard_acc_back
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Good opportunity for a barrel roll.)"
            show mscmc surfer_hairup smile:
                ease 0.4 xoffset -40
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
                ease 0.4 xoffset -70
            pause 0.4
            "I don't question my instincts and zoom beneath the lip of the wave as my board cuts the high-arching wall."
            show mscmc surfer_hairup grin:
                parallel:
                    ease 0.4 zoom 1.025 yoffset 5
                parallel:
                    linear 0.4 alpha 0.0
            show surfboard_acc_back:
                parallel:
                    ease 0.4 zoom 0.825 yoffset 10
                parallel:
                    linear 0.4 alpha 0.0
            pause 0.4
            show mscmc surfer_hairup grin:
                parallel:
                    ease 0.4 zoom 1.05 yoffset 20
                parallel:
                    linear 0.4 alpha 1.0
            show surfboard_acc_back:
                parallel:
                    ease 0.4 zoom 0.85 yoffset 20
                parallel:
                    linear 0.4 alpha 1.0
            "I keep my body loose and my eyes focused on the end of the tube."
            hide surfboard_acc_back
            hide mscmc
        "B. Floater.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at centre:
                xoffset 30
                yoffset 50
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            "The wave is thick and frothy, and I take advantage, snapping up to the top and balance on the lip as it plunges forward."
            show mscmc surfer_hairup grin:
                ease 0.4 xoffset 100
                ease 0.4 xoffset 30
            show surfboard_acc_back:
                ease 0.4 xoffset 150
                ease 0.4 xoffset 0
            pause 0.8
            "I don't wipe out, even as the wave crests. So I twist my board back and launch into my next move."
            hide surfboard_acc_back
            hide mscmc
        "C. Snap.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at centre:
                xoffset 30
                yoffset 50
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            "I can feel the steepness of the wave and meet it head on, pivoting onto the lip and shifting my weight to the back of the board."
            show mscmc surfer_hairup grin:
                pause 0.2
                ease 0.4 xoffset -30
                ease 0.4 xoffset 30
            show surfboard_acc_back:
                ease 0.4 xoffset -60
                ease 0.4 xoffset 0
            pause 1.0
            "I snap around, and ride down the front of the wave at high speed."
            hide mscmc
            hide surfboard_acc_back

    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(I'm doing it!)"
    hide mscmc
    scene bg msc_surfcompetition_day_people at bg with wiperightdissolve
    play music mschappytimes
    show mscmc surfer_hairup grin at centre
    "After my ride, I hop ecstatically off my board into the shallows."
    hide mscmc
    show maxime casual smile at centre,step_in
    "Maxime runs to meet me, splashing through the lapping waves."
    hide maxime
    scene bg msc_maxime_s1_mini3 at bg with dissolve
    mx "[genericfn]!! You were amazing!"
    "Before I can fully process what's happening, he's swept me off the ground in possibly the best hug ever."
    "(Oh my God. His arms are so strong.)"
    "(He's so warm and secure...Never put me down, Maxime, I'll just melt right here.)"

    scene bg msc_surfcompetition_day_people at bg with dissolve
    show javier swim grin at centre
    jv "[genericfn]! Those were some pretty slick moves for a small town girl."
    hide javier
    show mscmc surfer_hairup_cu basic_cu at mscmc_cu
    "(NOT NOW, JAVIER.)"
    show mscmc surfer_hairup grin at left1
    show maxime casual smile behind mscmc at right1
    "Maxime sets me down, but he doesn't seem embarrassed at all."
    mx "That's my girl! She's the best on the water."
    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(He called me 'his girl'...I'm melting for real...)"
    show mscmc surfer_hairup grin at left3
    show javier swim grin at right3
    mcmax "Uh, you did good too, Javier! Good job."
    show mscmc surfer_hairup grin:
        ease 0.4 xpos stagepos[1]-145
    show javier swim smile:
        ease 0.4 xpos stagepos[1]+145
    "I give him a small fist bump."
    hide javier
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Sorry, Nemesis—I'm too love-drunk right now to focus on our rivalry right now.)"
    hide mscmc
    scene bg msc_surfcompetition_sunset_people at bg with clockwise_wipe
    show mscmc surfer_hairdown embarrassed at centre
    show dawn jacket grin behind mscmc at left2
    show trina casual smile behind mscmc at right2
    "We join Dawn and Trina by the podium, while I fan my cheeks and pray Maxime doesn't notice my blush."
    show mscmc surfer_hairdown grin
    show trina casual smile at jumps
    pause 0.8
    so "[genericfn], this is so exciting!"
    show trina casual smile at jumps
    pause 0.8
    "Trina jumps up and down, grabbing and squeezing my hand as Wikus walks to the podium to announce who will be in the finals."
    hide mscmc
    hide trina
    show maxime casual smile behind dawn at right2
    dw "Vibes circle! We've got to amplify the good vibes."
    hide dawn
    show maxime casual_cu angry_cu at maxime_cu
    "Dawn grabs my other hand, and offers their free hand to Maxime, but he's preoccupied with glaring at Wikus."
    show dawn jacket basic at left2
    show maxime casual angry behind dawn at right2
    dw "I said good vibes dude, not mildly threatening vibes."
    show dawn jacket grin
    show maxime casual basic
    mx "Don't worry, my vibes are immaculate."

    play music mscdanger
    hide dawn
    hide maxime
    show wikus casual_cu basic_cu at wikus_cu
    "I snicker at their back and forth and look up at the podium, where I suddenly find myself locking eyes with Wikus."
    show wikus casual_cu smile_cu
    "He suddenly grins at me with all his teeth, like he knows something that I don't."
    hide wikus
    show mscmc surfer_hairdown_cu surprised_cu at mscmc_cu
    "(What is he planning?!)"
    hide mscmc

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
