label maxime_season1_episode10:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_beach_bar_sunset at bg
    play music mschappytimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show maxime casual basic at centre:
        xoffset 60
    show dawn jacket grin behind maxime at left2
    show trina casual smile behind maxime at right4
    "After Wikus announces me and the other finalists, Dawn and Trina haul Maxime and me back to Jerry's beach bar for celebrations."
    hide dawn
    hide trina
    hide maxime
    show maxime casual_cu angry_cu at maxime_cu
    "Maxime is deep in thought though, a faint frown creases his brow for a moment."
    hide maxime
    show trina casual smile at centre
    so "Clear way, clear the boardwalk, we've got a finalist coming through—VIPs only!"
    show dawn jacket grin behind mscmc at left3:
        pause 0.2
        ease 0.4 xpos stagepos[1]-140
    show trina casual smile behind mscmc at right3:
        pause 0.2
        ease 0.4 xpos stagepos[1]+140
    show mscmc jacket_hairdown grin at right1:
        pause 0.2
        ease 0.4 xpos stagepos[1]+20
    pause 0.6
    "Dawn slings their arms fondly over my shoulders and Trina's, pulling us in for a clumsy hug."
    dw "What'll you have, Ms. Finalist? My treat, you deserve it."
    show mscmc jacket_hairdown surprised
    so "I say we order one of those entire drink stands—you know, the trees with the drinks!"
    show mscmc jacket_hairdown grin
    so "What's that special called, 'Lovely Brunch of Coconuts'?"
    so "Hey Jerry!"
    hide trina
    hide dawn
    hide mscmc
    show jerry casual smile at centre
    "She waves furiously at Jerry, who's looking calm as ever even as a gaggle of surfers swarm him for drinks."
    hide jerry

    scene bg msc_beach_bar_night_lights at bg with clockwise_wipe
    play music mscjavier
    show javier casual grin blush at centre
    "As the sunset gives way to tnight, Javier and his team also stake their spots along the bar, clinking bottles of beer in celebration."
    jv "[genericfn]!"
    show mscmc jacket_hairdown smile at left3
    show javier casual smile blush behind mscmc at centre,right_in
    "Javier breaks off from the group, his cheeks flushed happily as he claps me on the shoulder."
    show javier casual grin blush
    jv "A hearty congratulations."
    show mscmc jacket_hairdown grin
    show javier casual smile blush
    mcmax "Congratulations to you too! You look like you've been having a good time."
    jv "It's been party central since I heard my name on the finalist's list, {i}and{/i} I get to duke it out with my favorite nemesis once again."
    show javier casual embarrassed blush
    mcmax "Ha! May the best surfer win this one, and I hope you're ready to go head-on in SurfFest this fall."
    show javier casual grin blush:
        ease 0.4 xoffset 40
        ease 0.4 xoffset 0
    pause 0.8
    "Javier grins, raising his bottle to me even as he sways in the night breeze."
    jv "That's what I like to hear! 'Scuse me for a sec... I was supposed to be getting drinks."

    show javier casual grin blush at out_right
    hide javier
    play music mscmaxime
    show mscmc jacket_hairdown basic
    "He leans on the counter, calling for another round, and I look around for Maxime."
    hide mscmc
    show maxime casual basic at centre
    "I find him learning against the side of the bar, watching everyone's antics with his arms crossed."

    hide maxime
    $menuhideborder = True
    menu maximee10c1:
        "A. Offer Maxime a beer.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at centre
            "I order a beer from Jerry, and make my way towards Maxime."
            show mscmc jacket_hairdown smile at left1, left_in
            show maxime casual angry at right4
            mcmax "Hey there. Need a little something to take the edge off?"
            show maxime casual smile
            "I smile coyly, holding up the bottle, and Maxime breaks out in a thankful smile."
            mx "That obvious, huh? Thanks, [genericfn]."
        "B. Get Maxime to laugh.":
            $menuhideborder = False
            show dawn jacket smile at left3
            show trina casual smile at right3
            "I glance at Trina and Dawn's drinks stand, a monstrosity of hollowed-out coconuts that takes up most of the counter."
            hide trina
            hide dawn
            show mscmc jacket_hairdown smile at left1, left_in
            show maxime casual angry at right4
            "Smiling to myself, I grab a coconut drink and walk over to Maxime."
            show mscmc jacket_hairdown grin
            show maxime casual embarrassed
            mcmax "I saved you one!"
            show maxime casual smirk
            "Maxime arches an eyebrow, but he can't bite back a laugh at the ridiculous coconut concoction."
            mx "What on earth is that?"
            mcmax "Trina's favorite, the 'Lovely Brunch of Coconuts' platter. Fair warning, I'm pretty sure it's one-third whipped cream."
            show maxime casual smile
            "Maxime shakes his head, amused."
            mx "I'll pass, but thanks."
        "C. Go somewhere quiet.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at centre
            "I beckon to Maxime, stepping back to where the boardwalk meets the sand."
            show mscmc jacket_hairdown smile at left1
            show maxime casual basic at right4,right_in
            "He follows me as we lose the raucous voices at the bar underneath the sound of the surf."
            show maxime casual embarrassed
            mcmax "You looked like you could use a breath of fresh air."
            show maxime casual smile
            "He smiles, taking a moment to enjoy the sight of the ocean."
            mx "You're right—this is nice."

    show mscmc jacket_hairdown smile at left1
    show maxime casual smile at right4
    "I place my hand on my hip, and look up at him quizzically."
    show maxime casual surprised
    mcmax "What's wrong? I can tell you're moping, rather than being your usual strong, silent self."
    show maxime casual basic
    "Maxime shakes his head apologetically."
    show mscmc jacket_hairdown surprised
    show maxime casual sad
    mx "I didn't want to detract from the fun. I'm so proud of you, [genericfn], but I'm worried too."
    show maxime casual basic
    mx "More than anything, I want to take you somewhere far away from Wikus."
    show maxime casual sad
    mx "But I don't want to deprive you of the opportunity to win this thing."
    show maxime casual basic behind mscmc
    show mscmc jacket_hairdown sad:
        ease 0.6 xoffset 80
    pause 0.6
    "I reach out, squeezing his hand in mine."
    show maxime casual embarrassed
    mcmax "I get you. It means a lot, knowing you're looking out for me."
    show mscmc jacket_hairdown embarrassed
    show maxime casual smile
    mcmax "I'm going to see the tournament through, but maybe when this is all over, I can take you up on that secret getaway offer."
    show mscmc jacket_hairdown smile
    show maxime casual embarrassed
    "Maxime lights up, his cheeks coloring pleasantly."
    mx "I'd like that."
    show maxime casual smile
    mx "And I know you don't back down from anything. That's what drew me to you."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "He reaches out, gently brushing my cheek with his fingers and sending my heart pounding."

    hide maxime
    play music mschappytimes
    show trina casual smile at centre
    so "Hey, you two! Finish up your tender loving moment and help us with these coconuts!"
    hide trina
    show mscmc jacket_hairdown embarrassed at left1:
        xoffset 80
    show maxime casual surprised behind mscmc at right4
    mcmax "{i}Trina!{/i}"
    show maxime casual smile
    "I'm mortified, my entire face bathed in heat, but Maxime just laughs."
    show mscmc jacket_hairdown surprised
    mcmax "I am {i}so{/i} sorry. I should have known that coconut special would be her downfall."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime shakes his head, placing his hand on my back as we head over."
    mx "Nah, it's alright. She's funny and it's nice to see everyone having fun."
    mx "C'mon, I'll give the coconut thing a fair try."

    hide maxime
    scene bg msc_labeach_day at bg with clockwise_wipe
    play music mscsurftraining
    show mscmc surfer_hairup grin at left3
    show maxime shorts smile at right4
    "On our last day of training before the finals, I look out to the ocean from the beach, bouncing on my toes in the sand."
    mx "Jitters?"
    mcmax "Not exactly. I'm just hoping I can summon enough of that 'pizzazz' we keep talking about."
    mcmax "Since it's, you know, my last chance to win this thing tomorrow."
    show mscmc surfer_hairup embarrassed
    show maxime shorts smile behind mscmc:
        ease 0.8 xpos stagepos[1]
    pause 0.8
    "Maxime lays a hand on my shoulder, and when I look at him, then calmness in his eyes soothes me."
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    mx "What do I keep saying when we talk about 'pizzazz'?"
    "I take a deep breath, counting off on my fingers."
    show mscmc surfer_hairup angry at left3
    show maxime shorts smile behind mscmc at centre
    mcmax "Focus on the water; don't think about the judges; and just be myself."
    show mscmc surfer_hairup sleep
    show maxime shorts smirk
    mx "There you go, sounds like good advice."
    show mscmc surfer_hairup grin
    show maxime shorts smile
    mx "Now, get out there."
    show mscmc surfer_hairup grin:
        parallel:
            easeout 0.4 zoom 1.05 xoffset -15 yoffset -60
            easeout 0.4 zoom 1.05 xoffset -15 yoffset 0
        parallel:
            linear 0.8 alpha 0.0
    pause 0.8
    "I heft my board, and we run into the shallows and hop on our boards to paddle out."

    hide maxime
    scene bg msc_ocean_wide_day at bg with wiperightdissolve
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 190
        ypos 360
    show mscmc surfer_hairup basic at centre:
        xoffset 90
        yoffset 100
        pause 0.2
        ease 0.4 xoffset 0
    pause 0.6
    "I scan the horizon, free to take my pick of the waves."

    hide mscmc
    hide surfboard_acc_back
    $menuhideborder = True
    menu maximee10c2:
        "A. Focus on the feel of the ocean.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(Just like Maxime said, what's important now is my relationship with the ocean.)"
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            show mscmc surfer_hairup sleep at centre:
                yoffset 100
            "I pause on my board, laying my hand to my heart and slowing my breathing, imagining syncing up with the waves."
            show mscmc surfer_hairup smile
            "When I open my eyes, I notice an absolutely beautiful wave beginning to form and roll towards me, like a gift from the sea."
            hide mscmc
            hide surfboard_acc_back
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(It's perfect!)"
        "B. Don't think about the competition.":
            $menuhideborder = False
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            show mscmc surfer_hairup basic at centre:
                yoffset 100
            "It's difficult at first, but with every stroke through the water I shed my worries about Wikus, and the judges' panel."
            show mscmc surfer_hairup smile
            "By the time I've reached deep water, my mind is clear, and I look around sharply, sizing up the waves that are forming."
            hide mscmc
            hide surfboard_acc_back
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Bingo, you're just the wave I need!)"
        "C. Just be yourself!":
            $menuhideborder = False
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            show mscmc surfer_hairup smile at centre:
                yoffset 100
            "I admire the glint of the sunlight on the waves, my mind drifting back to my very first surf classes..."
            "And how magical it felt to finally be able to fly over the water."
            hide surfboard_acc_back
            hide mscmc
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(Like I was always meant to be here, to come back here...)"
            show surfboard_acc_back behind mscmc:
                zoom 0.8
                xpos 190
                ypos 360
            show mscmc surfer_hairup smile at centre:
                yoffset 100
                ease 0.4 yoffset 70
            "I start paddling, prepareing to catch my wave, and pop up."
            
    show mscmc surfer_hairup grin:
        yoffset 70
        ease 0.4 xoffset 80
        ease 0.4 xoffset 0
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 190
        ypos 360
        pause 0.2
        ease 0.4 xoffset 80
        ease 0.4 xoffset 0
    pause 1.0
    "I start with a turn as I ride it, but time seems to slow, and I feel I could pull off something more complicated, have more fun."
    show mscmc surfer_hairup grin:
        xanchor 0.55
        ease 0.4 rotate -15 rotate_pad True yoffset 80
    pause 0.4
    "I cutback, dipping my hand into the water and pivoting around once again, my board leaps off the wave and I land it!"
    play sound splash03
    show mscmc surfer_hairup grin:
        xanchor 0.55
        ease 0.4 rotate 0 rotate_pad True yoffset 70
        ease 0.4 yoffset 700
        ease 0.4 xanchor 0.43 xoffset 110 yoffset 125
    pause 1.2
    "I step off my board near the shore, as Maxime enthusiastically heads towards me."
    hide mscmc
    hide surfboard_acc_back
    show maxime shorts smile at centre
    mx "[genericfn]! Wow!"
    show surfboard_acc_back behind mscmc:
        zoom 0.8
        xpos 50
        ypos 360
    show mscmc surfer_hairup embarrassed at centre:
        yoffset 125
        ease 0.6 xoffset 90 yoffset 100
    show maxime shorts smile behind mscmc at right5
    pause 0.6
    "I grin ecstatically, taking his offered hand and standing."
    mcmax "Good pizzazz levels?"
    "Maxime shakes his head, eyes shining as though I've produced a piece of art."
    show maxime shorts embarrassed
    mx "I don't want to talk lightly about such a beautiful performance. You were magnificent."
    
    hide mscmc
    hide maxime
    hide surfboard_acc_back
    scene bg msc_labeach_sunset at bg with wiperightdissolve
    "The sun sets as I drag my board up the bank, flushed and revelling. Suddenly, I hear a squeal from down the beach."
    show mscmc surfer_hairup surprised at centre
    $sidecharone = "Tiny Voice"
    sid1 "Excuse me!"
    show mscmc surfer_hairup smile
    "I turn to find a young girl, no more than seven, in a bright pink swimsuit running towards me."
    show mscmc surfer_hairup grin
    "She claps her hands when she reaches us, smiling wide."
    $sidecharone = "Little Girl"
    sid1 "Excuse me, but you are {i}so cool!{/i} I watched you surf from the beach."
    sid1 "I think you're the coolest surfer ever."
    mcmax "Thank you! That's really nice of you to say."
    show mscmc surfer_hairup grin:
        ease 0.6 yoffset 70
    pause 0.6
    "I bend down so I'm at her eye level, smiling encouragingly."
    mcmax "Surfers always like it when people tell us we're doing good."
    "She nods enthusiastically."
    sid1 "I want to be a surfer when I grow up! Can I do that?"
    mcmax "Of course you can! You just have to practice a lot."
    sid1 "I can do that!"
    "I grin, offering her my fist for a quick fist-bump."
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    "When she skips away, I turn to find Maxime smiling with an almost dreamy look in his eyes."
    show maxime shorts_cu embarrassed_cu
    mx "Well, that was officially the cutest thing I've ever seen."
    show mscmc surfer_hairup grin at left3
    show maxime shorts smile at right3
    mcmax "I know, she was cute as a button."
    mx "And seeing you with kids is cute. You've got a way with them."
    hide mscmc
    show maxime shorts_cu embarrassed_cu at maxime_cu
    "He turns, still grinning, and I'm surprised to notice a faint blush on his cheeks."
    hide maxime
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(So, Maxime has a soft spot for the world's little surfers. I'll just file that information away for later.)"
    show mscmc surfer_hairup grin at left3
    show maxime shorts smirk at right3
    mx "You deserve a treat after a job well done. Want to grab a beer back at the studio?"
    show maxime shorts basic
    mx "Only one, though, since it's the night of the final."
    show maxime shorts smile
    "He waggles a finger at me teasingly."
    show mscmc surfer_hairup smile
    mcmax "I could go for one, singular beer."
    show maxime shorts smirk
    mx "Oh, and there might be a little surprise waiting for you there."
    show mscmc surfer_hairup surprised
    "He keeps his voice nonchalant, but I know something's up."
    show mscmc surfer_hairup embarrassed
    mcmax "A surprise?"
    show mscmc surfer_hairup surprised
    mx "Mm-hm. It's a secret, though."
    show mscmc surfer_hairup grin
    mcmax "Alright, let's discover your secret! Now you've got me curious."
    mcmax "Not everything has to be a top-secret spy mission, you know."
    show maxime shorts smile behind mscmc
    show mscmc surfer_hairup grin:
        ease 0.4 xpos stagepos[1]-80
    pause 0.4
    "I poke his arm teasingly, and Maxime smiles, answering mildly."
    hide mscmc
    show maxime shorts_cu embarrassed_cu at maxime_cu
    mx "I know, but it's more fun if I get to surprise you."

    hide maxime
    scene bg msc_maxime_studio_sunset at bg with wiperightdissolve
    play music mscmaxime
    "When we reach his studio, Maxime opens the door, flicking on a light."
    show mscmc jacket_hairdown surprised at centre
    mcmax "Ohh my goodness."
    show mscmc jacket_hairdown embarrassed
    "I lay my hand on my chest, suddenly pleasantly short of breath."
    "Maxime has set a cushioned massage table up in the center of the room, with jars of body oil laid out beside it."
    mcmax "That's some surprise."
    show mscmc jacket_hairdown embarrassed at left3
    show maxime casual smile at right3
    mx "I told you, I did a course in sports medicine."
    "I nod rapidly, surrounded by images of me, nearly naked, and Maxime's big gentle hands running up and down my curves."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Yes, very medicinal, definitely!)"
    show mscmc jacket_hairdown smile at left3
    show maxime casual smile at right3
    "Maxime smiles gently, keeping his tone casual."
    mx "Of course you don't have to. It's the night before the tournament, and I want you to do whatever will make you comfortable."
    show mscmc jacket_hairdown embarrassed
    mx "But if you think a full body massage would help you loosen up for the big day, that's something I can do for you."
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    "He clears his throat, growing a bit flustered for the first time."
    show maxime casual_cu basic_cu
    mx "I can, ah, step out for a minute while you get ready, and you can call me back in..."
    "Now we're both blushing, as I imagine me in my bikini, and his hands pressing down on my skin."
    show maxime casual_cu smile_cu
    "He forces himself to look at me, smiling shyly."
    mx "Would you like a massage, [genericfn]?"

    hide maxime
    $menuhideborder = True
    menu maximee10c3:
        "A. Get oiled up and have Maxime massage you!" (paidchoice="paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown embarrassed at left3
            show maxime casual smile at right3
            mcmax "S-sure! That sounds good!"
            "My attempts to sound casual fall apart as my voice hitches awkwardly."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Oh my God, get it together, [genericfn]. You cannot be wigging out the entire massage!)"
            "(Though how I'm going to keep from losing it with Maxime's hands all over my bare skin, I have no idea.)"
            show mscmc jacket_hairdown embarrassed at left3
            show maxime casual smile at right3
            "Maxime smiles, setting me blushing again."
            show maxime casual basic
            mx "Great. Just call me when you're ready."
            show mscmc jacket_hairdown surprised
            show maxime casual embarrassed at out_right
            pause 0.4
            "He ducks out, leaving me alone in the studio."
            hide maxime
            hide mscmc
            "I slide my shirt and shorts off quickly, folding them and setting them on a nearby table."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I know I'm technically wearing my bathing suit, but... I'm basically standing around in my underwear in his studio.)"
            "(I am completely losing my cool, and yet, I could definitely get used to this.)"
            show mscmc bikini_hairdown sleep at centre
            "I take a deep breath and exhale, before climbing on top of the massage table."
            show mscmc bikini_hairdown smile
            "It's plush and comfy, and I can't believe this is really happening. Thank you, goddess."
            show mscmc bikini_hairdown embarrassed
            mcmax "Uh, come on in!"
            "I bury my head in my arms, just to hide any rogue blushes as he walks in."
            show mscmc bikini_hairdown embarrassed at left1
            show maxime casual smile at right3, right_in
            mx "All good?"
            play music mscromance
            "His voice is gently and soothing, and I relax, sinking into the cushioned table."
            mcmax "Very good! I {i}have{/i} been feeling a little stiff since that last trick."
            show mscmc bikini_hairdown smile
            show maxime casual basic
            mx "Where?"
            show maxime casual smile
            "I point to the space just below my shoulder blades."
            show mscmc bikini_hairdown basic
            mcmax "I think I may have leaned over too sharply."
            show mscmc bikini_hairdown embarrassed
            show maxime casual smirk
            mx "Don't worry, we'll get that all sorted before the finals."
            show maxime casual basic:
                ease 0.4 xpos stagepos[1]+270
            pause 0.4
            "I turn my head, watching as he picks a bottle of massage oil up from the nearby table."
            "He washes his hands at the kitchenette sink before pouring oil in his palm and rubbing them together."
            show maxime casual smile
            mx "We'll do a full-body, and then we'll get into working those knots out. Does that sound alright to you?"
            show mscmc bikini_hairdown grin
            mcmax "That sounds heavenly."
            show mscmc bikini_hairdown embarrassed
            show maxime casual smile behind mscmc:
                ease 0.4 xpos stagepos[1]+100
            pause 0.4
            "He places his warm hands on my skin, applying a light pressure to my back and working methodically."
            show mscmc bikini_hairdown sleep
            show maxime casual basic
            "His strong hands give me just the right of force, and I hum happily, letting my eyelids flutter shut."
            show mscmc bikini_hairdown embarrassed
            mx "Still good?"
            show mscmc bikini_hairdown_cu sleep_cu at mscmc_cu:
                xoffset -140
            show maxime casual_cu smile_cu behind mscmc at maxime_cu:
                xoffset 140
            "He leans over to talk to me, and the gravel of his voice sends a pleasurable shiver up my spine."
            show mscmc bikini_hairdown_cu embarrassed_cu
            mcmax "Mm-hmm!"
            show maxime casual_cu basic_cu
            mx "Alright. Let me know if you'd like a firmer touch, or anything at all."
            show maxime casual_cu smile_cu
            "He gradually works his hands to my arms, teasing the muscles out and releasing tension I never realized I was carrying."
            hide mscmc
            hide maxime
            "I feel like I'm floating with Maxime bent over me, his breath warm on the back of my neck, and his strong hands sending me to heaven."
            "When he starts to massage my calves, I practically ooze into the cushion."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            mcmax "Ohh, that's perfect."
            "I hadn't intended for a genuine moan to escape my lips, and I'm instantly mortified, hiding my face again."
            show mscmc bikini_hairdown_cu surprised_cu
            mcmax "Ahh, I'm sorry, that sounded so...!"
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime just chuckles, unbothered as he continues up to my thighs."
            mx "Don't worry, it tells me I'm doing a good job. Do you want me to work on that knot between your shoulders?"
            hide maxime
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            mcmax "Please do!"
            hide mscmc
            "He leaves my limbs feeling smoothed and cleansed with oil... I don't know if I'll be able to walk after this."
            "He kneads the spot between my shoulders, putting more force behind his touch."
            show mscmc bikini_hairdown_cu sleep_cu at mscmc_cu
            "(That's good, but it's not {i}quite{/i} there yet...If he pressed a little harder, I think it would release—!)"
            mcmax "Mm, harder—!"
            "My words come out as a mumble, while I'm distracted by the firm pressure and rhythm of Maxime's hands."
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "For the first time his fingers stumble, and his voice hitches when he responds."
            mx "Ah, harder...?"
            hide maxime
            "I have to muffle a giggle in my arm."
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(Finally, he's the flustered one!)"
            show mscmc bikini_hairdown_cu embarrassed_cu
            mcmax "Yes, you're so close!"
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "I sneak a glance around my shoulder, gratified to find him looking hot under the collar."
            hide maxime
            "He keeps the intensity of his massage up, pressing down on my back with his palms."
            "There's a satisfying 'pop', and we both forget our embarrassment, and cheer."
            show maxime casual_cu smile_cu at maxime_cu
            mx "There, that sounded good!"
            hide maxime
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            mcmax "Thank goodness, I was afraid that knot would become permanent."
            show mscmc bikini_hairdown grin at left1
            show maxime casual embarrassed behind mscmc at right1:
                xpos stagepos[1]+100
                pause 0.2
                ease 0.4 xpos stagepos[1]+270
            "I stretch on the table, leaning up into a cobra pose and enjoying how light and loose my back feels."
            show mscmc bikini_hairdown embarrassed
            mcmax "That felt so good. Thank you, Maxime."
            "I smile at him, aware I'm still flushed—and so is he, as he busies himself putting away the oils."
            mx "Of course. Anytime."
            hide mscmc
            hide maxime
        "B. Thank you, but no.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            mcmax "Thank you, but no."
            hide mscmc

    scene bg msc_boardwalk_night_lights_people at bg with clockwise_wipe
    play music mscdanger
    "After we finish up at his place, Maxime walks me back across the beach, his eyes somewhat wary as he scans the boardwalk."
    show mscmc jacket_hairdown basic at left2
    show maxime casual angry at right2
    mx "Stay close to Trina tonight. I don't want you alone, not with Wikus planning something."
    show mscmc jacket_hairdown smile
    mcmax "Don't worry, I promise."
    show maxime casual surprised
    mcmax "You should take your own advice, though. If Wikus thinks you know something..."
    "I half expect him to protest, but he smiles, the moonlight lighting up his face."
    show maxime casual embarrassed
    mx "You're right, I promise I'll be safe too."
    mx "Thanks for looking out for me."
    show mscmc jacket_hairdown embarrassed
    show maxime casual embarrassed behind mscmc:
        ease 0.4 xpos stagepos[1]
    "He touches my arm briefly, in place of holding my hand, and we spend a moment lost in each other's eyes in front of the surf shop."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    mx "I'll see you at the finals tomorrow."
    "(Damn, he's beautiful.)"
    show mscmc jacket_hairdown grin at left2
    show maxime casual smile behind mscmc at centre
    mcmax "Yes, {i}my{/i} final—because I'm going to win it!"
    hide mscmc
    hide maxime

    scene bg msc_surfcompetition_day_people at bg with clockwise_wipe
    play music mscsurfcompetition
    show mscmc surfer_hairup smile at centre
    "The finalists are lined up along the water's edge, all wearing our surfing best, and our boards waxed to perfection."
    show mscmc surfer_hairup basic
    "I run my fingers along the edge of my sturdy steed, studying the water as the sea breeze seems to invite me in."
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Time to win this thing!)"
    hide mscmc

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.