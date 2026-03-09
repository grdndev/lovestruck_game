label maxime_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_sunset at bg
    play music mscromance

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show maxime shorts basic at centre
    "The next morning, Maxime is waiting for me on the beach, lacing up his running shoes."
    show maxime shorts smile
    mx "Good morning. You game for a warm-up run?"
    hide maxime
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    mcmax "Aye-aye, coach."
    hide mscmc
    "I salute playfully, and we take off at a slow jog along the waterline."
    "Neither of us speaks much, but I'm happy with it, just sharing the peace and solitude of the early-morning beach with Maxime."

    scene bg msc_labeach_day at bg with dissolve
    "As the sun starts to rise over the waters, Maxime picks up speed, though he's hardly breaking a sweat."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Here we go!)"
    show mscmc surfer_hairup basic at left2, running
    show maxime shorts smile at right2, sprinting
    "I increase my own pace to match, though he breaks into a sprint as soon as I've caught up."

    hide mscmc
    hide maxime
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    mcmax "Seriously?"
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    "Maxime laughs at my unimpressed look, jerking his chin towards a stretch of rocks ahead."
    mx "First one to the wall wins...Go!"
    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    mcmax "Hey, my legs are considerably shorter than yours!"
    hide mscmc
    "I protest, huffing and puffing to keep up with him, though inside I'm delighted."
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Maxime being playful? I live for it!)"
    hide mscmc
    "I put on an extra burst of speed and hit the rocks just as he does slapping my palm on a large border."
    show maxime shorts_cu smile_cu at maxime_cu
    mx "Not bad! You're pretty fast."
    hide maxime
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "I glare up at him from where I'm catching my breath."
    show mscmc surfer_hairup_cu grin_cu
    mcmax "Making allowances for leg size, I won."
    show mscmc surfer_hairup grin at right2
    show maxime shorts smile at left2
    "He just laughs, flopping onto the sand beside me."
    mx "Alright, I won't fight you for it. Catch your breath, and then we'll cool off in the water."

    hide mscmc
    hide maxime
    $wavy_transition("bg msc_labeach_day", "bg msc_ocean_wide_day")
    scene bg msc_ocean_wide_day at bg with dissolve
    play music mscbeach

    show surfboard_maxime_acc_back behind maxime:
        zoom 0.6
        xpos 135
        ypos 348
    show maxime shorts basic at centre:
        zoom 0.67
        ease 0.3 yoffset -5
        ease 0.3 yoffset 0
    with dissolve
    "Out to sea, I'm surprised and delighted when Maxime half-rises onto his own board, studying the waves."
    hide maxime
    hide surfboard_maxime_acc_back
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    mcmax "Are you going to join me?"
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    mx "Of course! I'm no armchair quarterback."
    hide maxime
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.6
        xpos 185
        ypos 348
        pause 0.5
        parallel:
            ease 0.5 xoffset -200
        parallel:
            linear 0.5 alpha 0.0
    show maxime shorts smile at centre:
        zoom 0.67
        xoffset 50
        pause 0.5
        parallel:
            ease 0.6 xoffset -200
        parallel:
            block:
                linear 0.3 yoffset -40
                linear 0.3 yoffset 0
        parallel:
            linear 0.6 alpha 0.0
    "He winks, then pops-up for a wave I hadn't even sensed. I start paddling to catch up."

    scene bg msc_maxime_s1_ei1 at bg with fade:
        subpixel True top zoom 1.6
        pause 1.2
        linear 6 zoom 0.9
    pause
    mcmax "Wait for me!"
    "I catch the wave alongside him, laughing as the sea spray whips around us."
    "For a moment we're side-by-side, surfing the wave together."
    "(Damn, he really is so good.)"

    scene bg msc_ocean_wide_day at bg with fade
    "The wave finishes breaking and I slip beneath the water."

    play music mscloveinterest
    show maxime shorts basic surfboard at left2
    show surfboard_acc_back behind mscmc:
        zoom 0.7
        xpos 435
        ypos 420
    show mscmc bikini_hairup smile at right3 with dissolve:
        yoffset 200
        ease 0.5 yoffset 135
        ease 0.5 yoffset 155
    "I burst up for air and look expectantly at Maxime, who's seated on his own board."
    hide maxime
    hide mscmc
    hide surfboard_acc_back
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    mcmax "What do you think, coach?"
    show mscmc bikini_hairup_cu smile_cu
    "(No mistakes, anyway.)"

    show surfboard_maxime_acc_back behind maxime:
        zoom 0.7
        xpos 25
        ypos 328
    show maxime shorts smile at left2:
        xoffset 30
        pause 0.6
        ease 0.5 xoffset 0
    show surfboard_acc_back behind mscmc:
        zoom 0.7
        xpos 445
        ypos 420
    show mscmc bikini_hairup smile at right3:
        xoffset 30
        yoffset 60
        pause 0.5
        parallel:
            ease 0.5 yoffset 0
        parallel:
            ease 0.5 xoffset 15
        ease 0.5 xoffset 0

    "Maxime smiles, helping me back onto my board with a strong arm."
    mx "I can tell you've been working hard since I last saw you. You're right, your technique is pretty flawless."

    play music mscmctheme
    show maxime shorts sad
    mx "And I think I know what's irking you."
    show mscmc bikini_hairup surprised
    "I look up hopefully while wringing my locs out."
    mcmax "Really?"
    show maxime shorts basic
    "He nods."
    show maxime shorts smile
    show mscmc bikini_hairup basic
    mx "Now that you're such a solid waterwoman, you could stand to add a little...flair, or personal touches, to your rides."
    show mscmc bikini_hairup surprised
    mx "It'd take you to the next level in competitions. Get creative with it!"

    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    hide mscmc
    hide maxime
    $menuhideborder = True
    menu maximee03c1:
        "A. Isn't technique more important?":
            $menuhideborder = False
            show maxime shorts basic surfboard at left2
            show mscmc bikini_hairup surprised surfboard at right3
            mcmax "Surely, if my technique and tricks are all on point..."
            show maxime shorts smile surfboard
            mx "A little flare would put you above some of the other competitiors, make your rides really special."
        "B. That's not what they told us in surf school.":
            $menuhideborder = False
            show maxime shorts basic surfboard at left2
            show mscmc bikini_hairup basic surfboard at right3
            mcmax "Funny, when I was in surf school they used to discourage us from showing off."
            show maxime shorts smirk surfboard
            "Maxime smirks."
            mx "That's because no one wants their group of newbies showboating while they're still learning the ropes."
            show mscmc bikini_hairup smile surfboard
            show maxime shorts smile surfboard
            mx "This is different, you're practically a professional now."
        "C. I don't think I'm that creative.":
            $menuhideborder = False
            show maxime shorts basic surfboard at left2
            show mscmc bikini_hairup surprised surfboard at right3
            mcmax "Hmm, I was never the creative kid in school...Always the athlete."
            show mscmc bikini_hairup grin surfboard
            mcmax "Is that why you're so good, because you're an artist {i}and{/i} a surfer?"
            show maxime shorts smile surfboard
            "Maxime chuckles."
            show mscmc bikini_hairup embarrassed surfboard
            mx "You don't give yourself enough credit. You put a lot of heart into your surfingm, and that's what you need to run with."

    show maxime shorts smile surfboard
    show mscmc bikini_hairup basic surfboard
    "Noting my dubious expression, Maxime just smiles and shakes his head."
    mx "Alright, back to work—we'll talk more about your 'personal flare' later."
    show mscmc bikini_hairup grin surfboard
    mcmax "Oh, fine."
    "I roll my eyes and laugh before laying on my board and paddling further to sea, excited for the tournament's first round tomorrow."

    hide mscmc
    hide maxime
    scene bg msc_surfcompetition_day_people at bg with clockwise_wipe
    play music mscaction
    "The next day, every competing surfer lines up along the beach, and I can practically feel the sand vibrating with excitement."
    show dawn casual grin at left2
    show trina casual smile at right2
    "Dawn and Trina wave to me excitedly from the spectator's bleachers, and I raise my hand in response."
    hide trina
    hide dawn
    show maxime casual_cu smile_cu at maxime_cu
    mx "[genericfn]!"
    show maxime casual basic at left3
    show mscmc surfer_hairup smile at right2
    "Maxime ducks under the boundary tape, flashing his trainer's badge at security, and strides over to me."
    show maxime casual smile
    mx "How are you feeling?"
    show mscmc surfer_hairup grin
    "I grin at him, bouncing on my heels."
    mcmax "Pumped! Amped up! Like I'm going to kill this!"
    show maxime casual smile behind mscmc:
        ease 0.6 xpos stagepos[1]-140
    "He smiles and takes my hands in his, cradling them gently and startling me out of my tourament day jitters."
    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Hand-holding again...I can't get over how small my hands feel in his!)"

    play music mscromance
    hide mscmc
    show maxime casual_cu surprised_cu at maxime_cu
    mx "Oh, you're trembling!"
    show maxime casual_cu smile_cu
    "He's surprised, then shifts into a teasing grin."
    mx "You must be nervous...That's kinda cute."
    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "I glower at him, but don't pull my hands away."
    show mscmc surfer_hairup_cu grin_cu
    mcmax "Of course I'm nervous—this is a big deal!"
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime chuckles, and that warm sound soothes me."
    mx "Alright, alright. I want to try a breathing execise to help you be more aware of your body. Are you game?"
    show maxime casual_cu basic_cu
    mx "It's a whike sports psychology thing. I learned it when I was studying physio."
    show maxime casual_cu smile_cu
    "He chuckles wryly, while I can't peel my eyes away from our interlocked hands."

    hide maxime
    $menuhideborder = True
    menu maximee03c2:
        "A. Keep holding his hand and do Maxime's exercise!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc surfer_hairup smile behind maxime at right1plus
            show maxime casual basic at left1plus
            "I shift my hands in Maxime's, looking up at him trustingly."
            show mscmc surfer_hairup grin
            mcmax "Of course! What's you top-secret meditation technique?"
            show mscmc surfer_hairup smile
            show maxime casual smile
            "My agreeing seems to have lifted his spirits, and he graces me with a beautiful smile."
            mx "Well, I won't claim 'top-secret', but it works well for me."
            show maxime casual smirk
            mx "Like any mindfulness exercise, it's all about counting out your breathing."
            show maxime casual smile
            mx "But I've always found visualization helpful, and I like to imagine ripples spreading outwards towards the shore."
            mx "I thought you might too, since you've already heard the Breath of the Ocean."
            show mscmc surfer_hairup embarrassed
            "He grins, clearly proud of me, and my heart flutters happily."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(The only thing better than achieving a connection with the ocean was getting to share it with Maxime.)"
            "(He was so happy to have someone he could open up to, someone who understands his relationship with the water.)"
            "(I'm glad that person is me.)"
            show mscmc surfer_hairup smile behind maxime at right1plus
            show maxime casual basic at left1plus
            "I nod, showing that I'm focused and ready."
            show mscmc surfer_hairup grin
            mcmax "I understand. So where are the ripples—out on the ocean?"
            show mscmc surfer_hairup smile
            show maxime casual smile
            mx "Wherever feels right for you."
            mx "You want to imagine a stretch of water that's all you own; your favorite spot on the beach, a private pond, out on the open water."
            hide maxime
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(Well, that's an easy choice.)"
            hide mscmc
            "I automatically envision our special cove, where I first discovered Maxime is a merman and learned how to breathe with the ocean."
            show mscmc surfer_hairup grin behind maxime at right1plus
            show maxime casual basic at left1plus
            mcmax "Alright, I'm imagining a little cove with a pebbled, sandy shore. Now what do I do?"
            show mscmc surfer_hairup smile
            show maxime casual smile
            mx "Now take a deep breath in, counting up to four, and breathe out, counting back down."
            mx "When you inhale, imagine that you've reached down to tap the water, and think about how it would feel against your fingertips."
            mx "On the exhale, those ripples are spreading out, slowly growing broader until they touch the edge of the shore."
            mx "And then you do it again, breathing in time."
            hide mscmc
            hide maxime
            $wavy_transition("bg msc_surfcompetition_day_people", "bg msc_underwater_night")
            scene bg msc_underwater_night at bg with dissolve
            show mscmc surfer_hairup_cu sleep_cu at mscmc_cu
            "I shut my eyes, feeling his palms pleasantly rough against mine, and guide my breath, mentally counting the ripples just like he told me."
            "As I repeat the exercise, I become aware of the rise and fall of my own chest, and how much air I'm taking in."
            show mscmc surfer_hairup_cu surprised_cu
            "(I hadn't realized it before, but I was taking shallow breaths. I guess nerves are infectious in a competition.)"
            hide mscmc
            show maxime casual_cu sleep_cu at maxime_cu
            "Maxime is breathing along with me, and even with my eyes shut I can sense the movement of his broad chest, and feel the muscles in his arms relax."
            hide maxime
            "As I breathe, an anxieties sweep away, and the bustle of the crowd recedes to dull background noise."
            "Suddenly, it's easy to imagine that it's just the two of us and the ocean, without another soul in sight."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(And all I want to think about are Maxime's hands...So strong and confident but so gentle.)"
            "(It's like my hands were made to fit cradled in his.)"
            hide mscmc
            $wavy_transition("bg msc_underwater_night", "bg msc_surfcompetition_day_people")
            scene bg msc_surfcompetition_day_people at bg with dissolve
            show maxime casual_cu smile_cu at maxime_cu
            mx "Alright, one last, deep breath."
            "I open my eyes to find them locked with Maxime's deep, golden-brown gaze."
            hide maxime
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "The hubbub on the beach mixes with the steady thrum of the waves, gradually returning, but giving us a few more moments together."
            hide mscmc
            show maxime casual_cu basic_cu at maxime_cu
            "None of it sems to matter as we just stare at each other, quietly studying the contours of each other's face."
            play sound air_horn
            play music mscsurfcompetition
            hide maxime
            show wikus casual smile at centre
            "The klaxon finally breaks us out of our meditation, followed Wikus ordering everyone to the starting line."
            hide wikus
            show mscmc surfer_hairup surprised behind maxime at right1plus
            show maxime casual embarrassed at left1plus
            "I blink rapidly as Maxime chuckles and blushes."
            mcmax "Wow, I was in another world for a moment there. That's some technique you got!"
            hide maxime
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "I grin up at him, mostly to disguise the fact that I'm feeling a little flustered myself."
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime returns my smile, reluctantly releasing my hands from his."
            show mscmc surfer_hairup smile at right2
            show maxime casual smile behind mscnc at left2
            mx "So, you liked it?"
            show mscmc surfer_hairup grin
            mcmax "I did! It was just what I needed, keeping my focus on the ocean, and you and your training."
            "He laughs again, still bashful, and claps me on the shoulder."
            show maxime casual smirk
            mx "Great. You've got this, tiger. Go get 'em."
            show mscmc surfer_hairup grin:
                ease 0.5 xpos stagepos[1]-100
            show mscmc surfer_hairup grin at out_right
            "I return the friendly punch to the shoulder, hefting my board off the sand."
            hide maxime
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcmax "You got it, coach—I'll make you proud."
            show mscmc surfer_hairup_cu grin_cu:
                linear 1 alpha 0.0
            "I wave one last time before turning and hurrying across the sand to the starting line."
            hide mscmc
        "B. It won't help.":
            $menuhideborder = False
            play music mscsurfcompetition
            show mscmc surfer_hairup_cu basic_cu at mscmc_cu
            mcmax "It won't help."
            hide mscmc

    show wikus casual smile at centre
    "Wikus hops on a megaphone and finally tells us to prepare, and I grip the edges of my board, eyes firmly fixed on the ocean."
    ws "At the sound of the klaxon...Three...two...one..."
    play sound air_horn
    hide wikus
    $wavy_transition("bg msc_surfcompetition_day_people", "bg msc_ocean_wide_day")
    scene bg msc_ocean_wide_day at bg with dissolve
    "The klaxon blares, and I race to the water with every other surfer, all of us hopping on our boards and furiously paddling out."
    show javier swim smile at centre
    "A few contestants manage to get rides off, but it's Javier who captures my attention, practically springing onto his board for a beautiful wave."
    hide javier
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Wow, he's gotten amazing since I last saw him compete!)"
    "(He's so fluid on the board, his cutbacks look like he's dancing over the water...How does he do that?)"
    hide mscmc
    "I force my gaze back to the horizon and notice the beginnings of a large wave forming."
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(You're going to be mine!)"
    hide mscmc
    show surfboard_acc_back behind mscmc:
        zoom 1.3
        xpos -30
        ypos 400
    pause 0.3
    show mscmc surfer_hairup basic at centre with dissolve:
        xoffset 100
        yoffset 100
        parallel:
            ease 0.6 xoffset 0
        parallel:
            linear 0.4 yoffset -20
            linear 0.2 yoffset 0

    play music msctense
    "I pop-up onto my board, easily assuming my stance, but the memory of Javier's almost theatrical poses nags at me."
    hide surfboard_acc_back
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(I must look so stiff compared to him!)"

    play sound splash03
    show surfboard_acc_back behind mscmc:
        zoom 1.3
        xpos -30
        ypos 400
        ease 0.2 xoffset 20
        ease 0.8 xoffset -200
        ease 0.2 xoffset -180
    show mscmc surfer_hairup surprised at centre:
        pause 0.2
        parallel:
            block:
                linear 0.4 yoffset -40
                linear 0.4 yoffset 20
        parallel:
            linear 0.8 xpos stagepos[1]+100
        parallel:
            xanchor 0.6
            linear 0.8 rotate_pad True rotate 15
        parallel:
            linear 0.8 alpha 0.0
    "I attempt a carve, leaning my weight onto my back foot, but somehow, as I shift, the wave bucks under me."
    hide surfboard_acc_back
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Damn it!)"
    hide mscmc
    show surfboard_acc_back behind mscmc:
        zoom 1.3
        xpos -90
        ypos 400
        ease 0.4 xoffset -20
    show mscmc surfer_hairup sad at right1plus with dissolve:
        yoffset 150
        parallel:
            block:
                ease 0.2 yoffset 100
                ease 0.2 yoffset 130
        parallel:
            ease 0.4 xoffset -20
            ease 0.2 xoffset -30
    "I come up sputtering and cling to my board, mentally kicking myself."
    hide surfboard_acc_back
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Seriously, [genericfn]—wiping out in the first round?)"
    "(Javier's making me nervous.)"
    show mscmc surfer_hairup_cu surprised_cu
    "(Or maybe a little personal 'flair', like Maxime said, would have helped.)"

    hide mscmc
    scene bg msc_surfcompetition_day_people at bg with dissolve
    play music mscsadtimes
    "I kick back towards the shore and drag my board from the shallows, where Maxime is already waiting for me."
    show mscmc surfer_hairup sad at right1
    show maxime casual basic behind mscmc at left2:
        ease 0.4 xoffset 100
    "I search his face for any disappointment, but he just wraps me in my towel, handing me a water bottle."
    hide mscmc
    hide maxime
    show wikus casual smile at centre
    ws "The results are in; these sixteen surfers will move on to round two!"
    hide wikus
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "I grip my towel, listening in agony as he counts down."
    hide mscmc
    show wikus casual smile at centre
    ws "In sixteenth place, Raymond Church...In seventeenth place, [genericfn] [genericln]!"
    hide wikus
    show mscmc surfer_hairup sad at right1
    show maxime casual basic behind mscmc at left1:
        xoffset 20
    "I groan, my shoulders drooping, as Raymond Church's team cheers and bounces around him. I didn't make it to the next round."
    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Oh, it's that young surfer who was talking to Wikus at the opening ceremony in the orange shirt.)"
    show mscmc surfer_hairup_cu smile_cu
    "(Well, good for him, I guess.)"
    show mscmc surfer_hairup sad at right1
    show maxime casual basic behind mscmc at left1:
        xoffset 20
    "I turn to Maxime, probably looking like a sad, half-drowned puppy."
    mcmax "Well...will you help me work on my 'artistic flair' a little more?"
    show maxime casual smile:
        ease 0.3 xoffset 30
    "He puts his arm around my shoulders, giving me a gentle squeeze and taking some of the bad away."
    show mscmc surfer_hairup smile
    mx "Of course."

    hide mscmc
    hide maxime
    scene bg msc_beach_bar_sunset at bg with clockwise_wipe
    play music mschappytimes
    "We catch up with Trina and Dawn for a round of commiseration drinks at the Beach Bar."
    show mscmc jacket_hairdown sad at left2
    show trina casual smile at right2
    so "It's alright, hon, you can't win them all—you know that."
    hide trina
    hide mscmc
    show dawn jacket smile at centre
    "Dawn shrugs over a ridiculous-looking drink in a large hollowed-out pineapple."
    show dawn jacket grin
    dw "Yeah, but every pro is entitled to a little wallowing sometimes. It's like the law, or something."
    hide dawn
    show maxime casual smile at centre
    mx "Sounds reasonable."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I manage to smile at their banter, but I'm a little distracted, sipping my drink and absently scrolling through my phone."
    hide mscmc
    play sound phone_vibrating
    "It buzzes suddenly, alerting me to an email from the Beach Battle competition team."

    play music mscsuspense2
    "('URGENT NOTICE FOR ALL SURF COMPETITIORS'?)"
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "I open it quickly, my eyes widening as I read through the sparse official email."
    show mscmc jacket_hairdown surprised at left2
    show maxime casual surprised at right2
    "Maxime peers across the counter at me, instantly on alert."
    show maxime casual basic
    mx "What's wrong?"
    mcmax "It's a mass email. Apparently a competitor—Raymond Church, is missing."
    show maxime casual surprised
    mcmax "They're asking if any of us have information about what happened to him."

    hide maxime
    hide mscmc
    $menuhideborder = True
    menu maximee03c3:
        "A. Try to stay positive.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "I shudder, my own woes seeming small by comparison."
            mcmax "That's terrible. Surely they'll find him, though?"
            mcmax "He might have gotten lost? Or, he went to a party and didn't tell anyone, htere are always parties the first night of a tournament."
            hide mscmc
        "B. Spread the word.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show maxime casual surprised at right2
            mcmax "I'll take a screenshot and share the post on social media. It's the least I can do."
            hide maxime
            show mscmc jacket_hairdown basic
            show trina casual basic at right2
            so "Forward it to me—I'll print something out for the Surf Shop bulletin board."
            show trina casual sad
            so "Here's hoping they find him quickly."
            hide mscmc
            hide trina
        "C. Look up more info.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "I quickly start searching for any information online, mostly out of concern, but with a small tinge of morbid curiosity."
            show mscmc jacket_hairdown sad at left2
            show trina casual sad at right2
            so "Are there any more details than that?"
            mcmax "Not really. He's only been missing a few hours, so the police aren't getting involved yet. His team is organizing a search party."
            hide mscmc
            hide trina

    show maxime casual sad at centre
    "I glance at Maxime, who's gone quiet and thoughtful, a frown forming as he stares striaght ahead."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(This could be worse than anyone realizes, and only Maxime and I know the whole of it.)"
    hide mscmc
    "I glance at the email again, squinting at the grainy picture they've attached."
    show mscmc jacket_hairdown sad at left2
    show maxime casual sad at right2
    mcmax "He came in sixteenth today at the event. I saw him chatting with Wikus on opening day."
    show mscmc jacket_hairdown surprised
    show maxime casual basic
    play sound phone_vibrating
    "Maxime stiffens, his eyes brieftly meeting mine, but we're interrupted as my phone starts buzzing again with an incoming call."
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcmax "Hello?"
    hide mscmc
    ws "[genericfn]? It's Wikus Sapor. Great news: you've been bumped up to sixteenth place, you're in the next round!"
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcmax "Oh..."
    hide mscmc
    ws "You've probably heard about Raymond—isn't that an awful thing? But, are you ready for tomorrow?"
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcmax "Well, yes..."
    hide mscmc
    ws "Great, that's the kind of attitude I like!"
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "He hangs up abruptly, leaving me staring at my phone."
    show mscmc jacket_hairdown surprised at left2
    show trina casual basic at right2
    so "Now what?"
    mcmax "Well, with Raymond missing...I just got bumped into round two of the tournament."
    show mscmc jacket_hairdown sad
    mcmax "Which feels...not great."
    hide trina
    show maxime casual sad at right2
    "Maxime catches my eye, nodding understandingly."
    hide mscmc
    hide maxime
    show dawn jacket_cu sad_cu at dawn_cu with dissolve
    "Dawn leans between us, squinting at the grainy photo of Raymond still pulled up on my phone."
    show maxime casual basic at left2
    show dawn jacket surprised at right2
    dw "Actually...I may have seen that guy last night."
    show maxime casual surprised
    mx "Last night? Are you sure?"
    show maxime casual basic
    show dawn jacket sad
    dw "I mean, it was dark, but pretty sure. I was walking along the boardwalk and heard some dudes arguing in an alley."
    show dawn jacket basic
    dw "Then Raymond there came running like a bat out of hell, plowed into me, and didn't say sorry."
    show dawn jacket sad
    dw "I made tracks, because my momma didn't raise a dumbass. Sorry I didn't catch any names or faces."
    mx "Did you see..."
    hide maxime
    hide dawn
    show javier tank_cu smile_cu at javier_cu
    jv "Hey guys."
    hide javier
    show maxime casual basic at left4
    show dawn jacket basic at right4
    show javier tank smile at centre with dissolve
    "Javier appears suddenly, flopping down between Maxime and Dawn."
    show dawn jacket surprised
    dw "Oh, 'sup. You heard about the disappearance of Raymond Church? Heavy stuff."
    show dawn jacket basic
    show javier tank sad
    "Javier nods, lowering his voice."
    show javier tank angry
    jv "I did. My money's on Wikus as the culprit."
    show maxime casual angry
    show dawn jacket surprised
    show javier tank smile

    play music mscdanger
    "Maxime raises his head slowly, his eyes narrowing in suspicion."
    show dawn jacket basic
    mx "And why do you say that?"
    show maxime casual basic
    show javier tank grin
    "Javier turns, meeting Maxime's serious gaze, and breaks out in a laugh."

    hide maxime
    hide dawn
    show javier tank_cu grin_cu at javier_cu
    play music msctense
    jv "Just a joke—trying to add a little levity. My bad."
    show maxime casual sad at left2
    show javier tank basic at right2
    "Maxime doesn't return his smile, instead rising from the counter."
    show maxime casual sleep
    show javier tank smile
    mx "I should be headed home. Goodnight, everyone."
    hide maxime
    hide javier
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcmax "I'll go with you!"
    hide mscmc
    "I stand up before anyone can ask questions, slamming my money on the counter and hurrying after him."

    scene bg msc_labeach_night at bg with dissolve
    show maxime casual basic at right1plus
    pause 0.3
    show mscmc jacket_hairdown sad behind maxime at left1plus with dissolve:
        ease 0.6 xoffset 20
    "Maxime and I fall into step, and I catch his arm when we're a little ways from the bar."
    show maxime casual sad
    "He drops his gaze to my hand before looking at me seriously."
    mcmax "You think Raymond's disappearance is connect to your mission, don't you? That Wikus is up to something."
    "Maxime seems to carefully consider his words, speaking softly."
    mx "I'm not sure."
    mx "If there's anything shady going on, Wikus is probably involved, but your 'nemesis', Javier, could also be involved."
    hide mscmc
    show maxime casual_cu sad_cu at maxime_cu
    mx "What I don't like is that they're both uncommonly interested in you."

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
