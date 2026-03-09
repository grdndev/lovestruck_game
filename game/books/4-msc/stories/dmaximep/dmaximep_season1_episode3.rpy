label dmaximep_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg
    play music mscsurfshop

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(I guess Maxime doesn't care about my seal pup eyes because he walked away the other night without giving me an answer.)"

    hide mscmc
    "It's been 3 days since I last saw Maxime and discovered merfolk are real."
    "I sigh, resting my chin on my arms as I hunch over the counter."
    "It's been deserted of customers all day, so Trina's taken the opportunity to run a quick errand."

    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(And I have nothing to distract me from constantly thinking about you-know-who.)"

    hide mscmc
    "Maxime and his tales of mermaid cities under the sea have been swirling in my mind since we parted at the lagoon."

    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(The fact that he hasn't contacted me since then only makes it worse. I guess he did leave town.)"
    "(I've just learned that magic and mermaids are real, and I'm already back to life-as-usual at the surf shack.)"

    hide mscmc
    "I shake my head, trying to knock some sense into myself."

    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Come on, [genericfn]. Did you really think life was about to go all fantasy novel?)"

    show mscmc casual_hairdown_cu sad_cu
    "(You've already got a plan and a passion! What more could you need?)"

    hide mscmc
    "I straighten up, resolving to focus on surfing and practice later that evening, when the bell above the door rings."

    show mscmc casual_hairdown grin at centre
    mcmaxime "Welcome to Trina's surf shop, can I hel- Maxime!"

    hide mscmc
    show maxime casual basic at centre
    "I gape at Maxime, who seems to have suddenly materialized."

    show maxime casual smile
    "He smiles faintly at my look of shock, then approaches the counter, slow and easy."
    mx "Morning, [genericfn]. You up for some practice after you get off work?"

    hide maxime
    show mscmc casual_hairdown surprised at centre
    "I start to babble, caught between delight and irritation."

    show mscmc casual_hairdown angry at left2
    show maxime casual basic at right2
    mcmaxime "Why didn't you say something sooner?! I thought you'd left!"

    show mscmc casual_hairdown grin
    mcmaxime "And yes, of course I'm still interested!"

    show maxime casual surprised
    mx "One condition, though."

    show maxime casual basic
    "He holds up his hand, and I wait with baited breath."

    show maxime casual sad
    mx "I won't watch the competition the day of--it brings back too many bad memories for me. Please don't be offended."

    show mscmc casual_hairdown surprised
    "I wait, but Maxime has fallen silent, watching me searchingly."
    mcmaxime "That's it? Of course, that's fine!"

    show maxime casual smile
    mx "Good."

    show mscmc casual_hairdown smile
    show maxime casual sad
    "He nods, but seems a bit embarrassed, suddenly becoming interested in a net full of beach balls."

    show mscmc casual_hairdown grin
    show maxime casual basic
    mcmaxime "I promise you won't regret this! I'm one of the best surfers at the pier."

    show maxime casual smile
    "I lean on the counter, puffing out my chest proudly, and Maxime chuckles."
    mx "I know--I saw you on the water."

    show mscmc casual_hairdown surprised
    mcmaxime "Oh!"
    hide mscmc
    hide maxime

    $menuhideborder = True
    menu maximee3c1:
        "A. Pretty good, wasn't I?":
            $menuhideborder = False
            show mscmc casual_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "Pretty smooth, wasn't I?"
            mcmaxime "I mean, I don't know if you were watching this morning..."
            mcmaxime "My timing was just a little off on one my dismounts, but I've blocked in some time to practice before my usual drills."
            hide mscmc
            hide maxime
        "B. What did you think?":
            $menuhideborder = False
            show mscmc casual_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "So, what did you think?"
            "I try to keep my voice neutral, even while I lean in and watch his face for any sign of approval."
            hide mscmc
            hide maxime
        "C. Hopefully not that time I wiped out.":
            $menuhideborder = False
            show mscmc casual_hairdown sad at left2
            show maxime casual basic at right2
            mcmaxime "Geeze, I hope you didn't see me wipe-out while surfing with Trina."
            mcmaxime "I promise, that's not the usual me--we were just talking, and I let myself get distracted."
            hide mscmc
            hide maxime

    show mscmc casual_hairdown smile at left2
    show maxime casual smile at right2
    mx "You were great, [genericfn]."

    show mscmc casual_hairdown embarrassed
    mx "That's part of the reason I came back. You've got real talent."
    "I can feel myself blushing from my toes to my cheeks, made worse by the way he's watching me, dark eyes containing multitudes."
    "I kick myself in the shin as a sharp reminder."

    hide maxime
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Come on [genericfn], focus! This is all about the competition, remember?)"

    show mscmc casual_hairdown_cu smile_cu
    "(You've got a dream to fulfill!)"
    hide mscmc

    scene bg msc_labeach_day at bg with fade
    play music mscbeach

    "The next day, Maxime and I set up on an empty portion of the beach."
    show mscmc surfer_hairup basic at left2
    show maxime shorts basic at right2
    "I'm ready to carry my board down to the water, but Maxime waves his hand, indicating I should set it in the sand."
    "He unfurls a beach towel for himself, settling down comfortably."

    show mscmc surfer_hairup surprised
    mcmaxime "Wait, are we really just going to do exercises on the sand?"

    show mscmc surfer_hairup smile
    show maxime shorts smile
    mx "What's wrong with praciticing on the sand? I've seen you teaching the kids on the beach. You're great with them."
    "He grins infuriatingly."

    show mscmc surfer_hairup surprised
    show maxime shorts basic
    mcmaxime "Well, of course, but I'm not a kid. I'm a professional, well almost. I don't a course in mounting my board."
    mcmaxime "Otherwise I'd probably have drowned yesterday."

    show mscmc surfer_hairup basic
    "Maxime sits cross legged, completely unconcerned."

    show maxime shorts smile
    mx "I know you're a strong swimmer."
    mx "But if you want to perfect your technique, you've got to start from the beginning--we can't gloss over anything."
    mx "So, let me see your pop up."

    hide mscmc
    hide maxime
    "I roll my eyes but decide to humor him, lying down on my board as if I was paddling."

    show surfboard_acc_back:
        zoom 1.25
        xpos -13
        ypos 451
    show mscmc surfer_hairup basic at centre, step_in with dissolve
    "I press up and leap onto my feet neatly."

    hide surfboard_acc_back
    show mscmc surfer_hairup surprised surfboard
    mcmaxime "Satisfied now?"

    hide mscmc
    show maxime shorts smile at centre
    "Maxime shakes his head, still infuriatingly mellow."
    mx "Hell no, you've only done one rep! Go again."

    hide maxime
    "I place my hands on my hips."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    mcmaxime "You've got to be kidding. You've seem me take waves!"

    show mscmc surfer_hairup_cu sad_cu
    mcmaxime "Shouldn't we at least practice mounting on the water?"

    hide mscmc
    show maxime shorts basic at centre
    "Starting back at the beginning makes it easier to notice your blindspots."

    hide maxime
    "I rear up, offended."

    show mscmc surfer_hairup angry surfboard at left2
    show maxime shorts basic at right2
    mcmaxime "What 'blindspots'? If I'm doing something wrong, just tell me so I can fix it!"
    "I peer suspiciously at Maxime, trying to read some clue to his expression."

    show mscmc surfer_hairup basic surfboard
    "He's as tranquil as ever, like the deepest part of the sea."

    show maxime shorts surprised
    mx "...Actually, I was going to say you worry too much about what other people see when they watch you surf."
    mx "You need to learn to block everything else out."
    mx "Surfing in the competition shouldn't feel any different than when it's just you, your board, and the ocean."

    show mscmc surfer_hairup sad surfboard
    show maxime shorts basic
    "(Easy for him to say, since he avoids surfing at competitions at all costs.)"

    show mscmc surfer_hairup angry surfboard
    mcmaxime "So I'm distracted? That's my blindspot?"
    mcmaxime "Fine, I'll block the rest of the beach out."

    hide maxime
    hide mscmc
    "I grumble, dropping back onto my belly and preparing to jump up on the board."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(And doesn't that mean I should block him out too?)"

    hide mscmc
    "I can't quiet my thoughts before I leap, and realize as I'm in the air that my timing's off."
    "I correct myself, managing to mount the board in a perfect pose."

    play music mscsuspense
    "But a spike of pain up my left leg tells me something went very wrong in how I caught my weight."

    $menuhideborder = True
    menu maximee3c2:
        "A. Oww!!!":
            $menuhideborder = False
            "(I can't help myself--I break out in a yelp, instinctively clutching my calf, which feels tight and hot.)"
        "B. Oof...":
            $menuhideborder = False
            "I grit my teeth to keep from crying out, managing a faint groan."
            "I lean down, trying to massage my calf as my muscles beg me to stop."
        "C. It's nothing.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "(Whatever happens, I {i}cannot{/i} let Maxime know I strained something.)"
            "(Or twisted something. I'm not really sure.)"
            hide mscmc
            "I press my lips together, but find it difficult to straighten up."


    "Maxime is on his feet instantly, putting a hand under my arm to help me balance."

    show maxime shorts_cu sad_cu at maxime_cu
    mx "Are you ok? What hurts?"

    hide maxime
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    mcmaxime "I just landed a little too hard...I'll be fine in a minute."

    hide mscmc
    "I gingerly lower myself to the sand, but by how long it's taking me, I can tell I'm not fooling Maxime."
    "I glance up, humiliated, but find him merely bending over me with concern."

    show mscmc surfer_hairup sad at left2
    show maxime shorts sad at right2
    mx "My place isn't far from here. If you don't mind hobbling a bit, we can get you some ice."

    show maxime shorts basic
    "He offers me his arm, while I try to hide my hot face behind my hair."
    mcmaxime "It's really fine..."

    show maxime shorts smile
    mx "But ice will make it better, and we don't want to take any chances before the competition."

    show maxime shorts basic
    "I sigh, nodding reluctantly."
    mcmaxime "Okay. Thank you."

    hide maxime
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(He knows how to get me, I'd never do anything that could spoil my chance at the competition.)"

    hide mscmc
    "Maxime lifts me gently, one rough hand against my waist, and helps me limp across the sand."

    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(He's so warm and solid.)"

    show mscmc surfer_hairup_cu smile_cu
    "(Between the stabs of pain, I can't stop thinking about how closely we're pressed together.)"
    hide mscmc

    scene bg msc_maxime_studio_day at bg with fade
    play music mscmaxime

    "Maxime leads me to a pleasant beachfront cottage, rustic and painted ocean-blue."
    "When he opens the door, I get a whiff of the strange paint smell I noticed on him when we first met."

    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Woah!)"

    hide mscmc
    "I glance around the room as Maxime settles me on a nearby crate."

    show mscmc surfer_hairup basic at left2
    show maxime casual smile at right2
    mx "This is my studio. Let me just get you some ice from the kitchen."

    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Damn, it sure is. And if this is his studio, that means he painted everything here?)"

    hide mscmc
    "The walls are covered with abstract oil and acrylic paintings. some hanging, some propped against the floorboards."
    "Paint brushes, palettes, and textuizers are scattered across every paint-splattered surface, adding to the faint aroma."
    "I shift on the crate, gingerly keeping my leg elevated, and notice a painting sitting on an easel right beside me."

    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(This looks like it could be in a gallery!)"

    show mscmc surfer_hairup_cu embarrassed_cu
    "(I seriously can't believe this guy. 'Man of mustery' and 'unfairly multi-talented' doesn't even begin to describe him.)"

    hide mscmc
    "I rest my chin on my fist, taking my time to admire the painting."
    "It's abstract and heavily textured with many strokes of paint, all blending together like foam on the shore."

    show mscmc surfer_hairup smile at left2
    show maxime casual smile at right2
    mx "That one's not done yet."
    "Maxime steps back into the room, cradling an ice pack in one hand."
    "He glances at the painting, blushing."

    show mscmc surfer_hairup surprised
    show maxime casual basic
    mcmaxime "Really? I couldn't tell, it's so pretty already."

    show mscmc surfer_hairup smile
    show maxime casual smile
    "He smiles, a little embarrassed, and kneels beside me."

    show maxime casual sad
    mx "How's the leg?"

    show mscmc surfer_hairup sad
    "I scowl, remembering our 'lesson'."

    show maxime casual basic
    mcmaxime "It's tense, but that's because I was worrying about screwing up the incredibly basic move you had me doing."
    "I sulk, but can't find it in myself to be anything more than annoyed."
    "(How can I, when he's been such a gentleman and brought me back to his place for ice?)"
    "I settle for grumbling playfully."

    show mscmc surfer_hairup grin
    mcmaxime "Don't make me unsure before the competition. If anything, you should teach me some of your elite merman moves."

    show maxime casual smirk
    "Maxime merely raises his eyebrows, as I try to flex my leg."

    show mscmc surfer_hairup sad
    show maxime casual basic
    mcmaxime "Ooh, ow...I think I'm going to leave this ice for a bit, if that's okay."

    show maxime casual smile
    mx "Of course. The good news is, it doesn't seem sprained, so you probably just pulled a muscle."
    mx "Do you mind if I feel the muscle? I took some physical therapy classes back in the day."

    hide maxime
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Of course you did. What don't you do?)"

    hide mscmc
    "I bite back my retort, realizing he's waiting for permission."

    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Oh god, now I'm thinking about his big, rough hands rubbing up and down my leg...)"

    hide mscmc
    $menuhideborder = True
    menu maximee3c3:
        "A. Let Maxime massage your leg." (paidchoice = "paidchoice"):
            $menuhideborder = True
            "I glance down at my leg. It's not like I don't know how to treat a cramp but he really does look like he's worried and wants to help."
            show mscmc surfer_hairup grin at left2
            show maxime casual basic at right2
            mcmaxime "Got for it."
            hide mscmc
            hide maxime
            scene bg msc_maxime_s0_mini3 at bg
            "He lifts my leg gingerly, one hand under my knee, the other cupping my ankle."
            "(It really throws into perspective just how much taller he is than me...I bet he could pick me up like I was nothing.)"
            mx "Where's most of the pain?"
            scene bg msc_maxime_studio_day at bg
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            mcmaxime "Up and down the calf. It's worse when I stand on it."
            hide mscmc
            show maxime casual_cu basic_cu at maxime_cu
            "He nods and gently begins to to massage along my calf muscle."
            "I shiver pleasantly, my nerves dancing at the sudden relief. His hands are large and sure."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(It still hurts a little, but it's more of a pleasant ache, like he's loosening my muscles up.)"
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            mx "Does that feel better?"
            hide maxime
            "Maxime doesn't meet my eye, focused entirely on his hands and my leg."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mcmaxime "That's a lot better. Thank you, Maxime."
            hide mscmc
            "I speak gently, and he finally looks up, surprised. My breath hitches when we lock eyes."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "I smile, a bit ruefully."
            show mscmc surfer_hairup_cu sad_cu
            mcmaxime "I'm sorry for being a brat back on the beach. I know you're just trying to help."
            show mscmc surfer_hairup_cu smile_cu
            mcmaxime "And I'm sorry I got you so wrong when we first met."
            hide mscmc
            "He furrows his brow, confused, and I can see him mentally running thorugh our first meeting at the surf shack."
            show maxime casual_cu basic_cu at maxime_cu
            mx "At the store? As I recall, we just bumped into one another and had to pick up sunglasses."
            hide maxime
            "We share a laugh that pleasantly fills the sunny studio."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcmaxime "I thought you were kind of a jerk at the time, but you've been good to me, and I like talking to you."
            hide mscmc
            show maxime casual_cu sad_cu at maxime_cu
            mx "You thought I was a jerk?"
            hide maxime
            "He's not upset, but seems genuinely caught off-guard, trying to figure it all out."
            show mscmc surfer_hairup basic at left2
            show maxime casual sad at right2
            mx "Because I ran into you?"
            show mscmc surfer_hairup surprised
            show maxime casual surprised
            mcmaxime "What? No, I ran into {i}you!{/i}"
            show mscmc surfer_hairup sad
            show maxime casual basic
            mcmaxime "You barely exchanged a word with me and Trina. I thought you were mad at me for spilling the water shoes and sunglasses everywhere."
            show maxime casual embarrassed
            "Maxime frowns, still massaging my leg, then flushes, looking at the ground."
            mx "Oh, uh...I'm sorry if I was curt. I wasn't expecting anyone else to be there, except Trina."
            mx "I'm not great with meeting new people. I get shy."
            show mscmc surfer_hairup surprised
            show maxime casual sad
            "Now it's my turn to stare at him in astonishment."
            mcmaxime "You're telling me you're {i}shy?{/i}"
            hide maxime
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(Actually, that explains a lot about him--his silence, his preference for quietly reading at the bar, his modesty about being a former pro.)"
            show mscmc surfer_hairup_cu sad_cu
            "(But I still have a hard time picturing it.)"
            hide mscmc
            show mscmc surfer_hairup surprised at left2
            show maxime casual smile at right2
            "Maxime actually laughs at my shock."
            show mscmc surfer_hairup basic
            mx "What, is that so surprising?"
            show mscmc surfer_hairup embarrassed
            mcmaxime "Well, no. It's just a good-looking guy like you, with secret mermaid powers...It seems like you've got everything under control."
            hide mscmc
            hide maxime
            "Maxime's blush deepens with every compliment. which is what I was secretly hoping for."
            "His hands on my leg never falter or hesitate."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(It feels like heaven, I don't want this moment to ever end.)"
            hide mscmc
            "When he speaks, his words are less steady than usual, even--dare I say it--flustered."
            show maxime casual_cu embarrassed_cu at maxime_cu
            mx "Well, uh...I've always been more of an introvert. I never know what to say in social situations."
            hide maxime
            "He grins up at me, so easy and open that my heart skips a beat."
            show maxime casual_cu grin_cu at maxime_cu
            mx "I'm glad you don't think I'm a jerk anymore. And I'm glad you gave me a chance, even though you didn't know what to make of me."
            hide maxime
            "Now it's my turn to blush, but before I can respond, Maxime stands up, beckoning at my leg."
            show mscmc surfer_hairup smile at left2
            show maxime casual smile at right2
            mx "Try putting some weight on it. I want to see if that helped."
            hide mscmc
            hide maxime
            "I brace one hand on the wall, just to be safe, and slowly rise from the crate."
            "To my delight, I don't feel a spike of pain even when I shift my posture, just that pleasant, loose ache that indicate my muscles are un-tensing."
            "I give Maxime a thumbs-up."
            show mscmc surfer_hairup grin at left2
            show maxime casual basic at right2
            mcmaxime "It feels great, Mr. Master Masseuse. If you ever get tired of teaching kids how to surf, maybe you can become the pier's own physical therapist."
            show maxime casual smile
            "I'm half-joking, but Maxime seems genuinely pleased with the compliment."
            mx "Well, you know I always like to keep my options open."
            hide maxime
            hide mscmc
            "He nods towards a cluster of paintings, bunched up beside a vintage, decorative surfboard."
        "B. Do it youself.":
            $menuhideborder = True
            show mscmc surfer_hairup sad at left2
            show maxime casual basic at right2
            "I flush hotly, shaking my head."
            show mscmc surfer_hairup grin
            mcmaxime "I've got it."
            hide mscmc
            hide maxime
            "I instantly regret saying that, wondering if I sounded clipped."
            "Maxime nods in understanding, settling on his painting stool beside me."
            "I gingerly move the ice pack aside, gently rubbing at my sore calf with my fingers."
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "(It hurts, but it hurts so good...)"
            hide mscmc

    play sound knocking
    play music mscantagonist
    "Maxime opens his mouth to say something else, but a knock at the door makes us both startle."
    "I look over to find Maxime has gone ashen, halfway out of his chair and staring furiously at the clock."
    "Suddenly, he grips my arm, gentle but urgent."
    show mscmc surfer_hairup surprised at left2
    show maxime casual surprised at right2
    mx "Damn it, I didn't realize how late it is--you're not supposed to be here!"
    show maxime casual basic
    mcmaxime "Uh, but you invited me...?"
    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Just how strict is your landlord, dude?)"
    hide mscmc
    show mscmc surfer_hairup surprised at left2
    show maxime casual sad at right2
    mx "Look, I'm sorry, please hide!"
    hide mscmc
    hide maxime
    "He hurries me up, making sure to support my bad leg, and nudges me towards a folding closet door."
    "I protest halfway through the closet doors."
    show mscmc surfer_hairup angry at left2
    show maxime casual angry at right2
    mcmaxime "Can't you at least tell me why you're shoving me in a closet? Because out of context, it's suss as hell."
    show maxime casual surprised
    "Maxime stares at me, more desperate than anything, then seems to realize what I've said."
    show mscmc surfer_hairup basic
    mx "No, no, it's not that--I'm single, I'm not like that!"
    show maxime casual angry
    mx "This is for your own good, [genericfn]. There's people from the mer world who you're better off avoiding."
    show maxime casual sad
    mx "I promise I'll explain everything later."
    show mscmc surfer_hairup basic at out_left with dissolve
    "Seeing his eyes large and pleading makes me nod, slipping into the closet."
    hide maxime
    "I crouch and peer through the slats, watching Maxime hurry to his front door."
    show maxime casual_cu surprised_cu at maxime_cu
    mx "Just a moment!"
    hide maxime
    show camilla casual basic at centre with dissolve:
        zoom 0.9
        ease 1.25 zoom 1
    "He throws open the door, and a pretty woman in an expensive-looking outfit pushes him aside, walking like she owns the place."
    show camilla casual angry
    "She levels him with a glare."
    show camilla casual_cu angry_cu at camilla_cu
    $sidecharone = "Menacing Woman"
    sid1 "How dare you make me wait, Maxime Okun. Where is your report?"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
