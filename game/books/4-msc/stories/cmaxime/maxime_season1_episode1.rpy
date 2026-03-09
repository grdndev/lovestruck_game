label maxime_season1_episode1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_ocean_wide_day at bg
    play music mscmctheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc surfer_hairup basic surfboard at centre
    "The waves lap gently under my board, and I close my eyes, playing the next few weeks' competition out in my head."
    show mscmc surfer_hairup_cu sad_cu -surfboard at mscmc_cu
    "(No biggie, it's just a multi-day tournament with all the biggest sponsors watching.)"
    show mscmc surfer_hairup_cu grin_cu
    "(You've got this, [genericfn]. Breathe.)"
    show mscmc surfer_hairup sleep surfboard at centre
    "I inhale and exhale with the lull of the waves, and remember Maxime's advice on that beautiful moonlit night by the cove."

    scene white at bg
    pause 0.5
    scene bg msc_underwater_night at bg, grayscale
    show maxime mermaid_cu smile_cu at maxime_cu, grayscale
    play music mscromance
    mx "Merfolk are one with the ocean, so our breathing is always in sync." 
    mx "Place your hand over my heart and I'll help you listen. Is that alright?"
    hide maxime
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu, grayscale
    "I nod, the water keeping from blushing too much, and he takes my hand, laying it over his strong chest."
    show mscmc bikini_hairdown sleep at right1, grayscale:
        zoom 1.25
    show maxime mermaid basic behind mscmc at left2, grayscale:
        zoom 1.25
    "I feel the steady rhythm of his heart beneath my palm, and shut my eyes, focusing on our touch and the way the water rushes past us."
    show mscmc bikini_hairdown surprised
    "Suddenly, I feel a blossoming in my mind as I fully grasp just how vast the ocean is—a living, breathing thing, constantly in motion."
    show mscmc bikini_hairdown embarrassed
    show maxime mermaid smile
    mx "You've got it!"
    scene white 
    pause 0.2
    scene bg msc_ocean_wide_day at bg with dissolve
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(...I wish Maxime were here.)"
    "(I liked him, maybe more than liked... and he turned out to be an undercover mer superspy.)"
    show mscmc surfer_hairup_cu embarrassed_cu
    "(He taught me to trust my own skills. Swimming next to Maxime made me feel like I was one with the ocean.)"
    show mscmc surfer_hairup_cu grin_cu
    "(Not that that's surprising, coming from a merman.)"
    play music mscaction
    show mscmc surfer_hairup smile surfboard at centre
    "I square my shoulders, noting the beginnings of a wave on the horizon."
    show mscmc surfer_hairup_cu smile_cu -surfboard at mscmc_cu
    "(Alright, game face. You can never practice enough, especially before a major tourament!)"
    hide mscmc
    show surfboard_acc_back behind mscmc:
        zoom 0.9
        xpos 135
        ypos 400
    pause 0.3
    show mscmc surfer_hairup basic at centre, step_in with dissolve
    "I pop-up easily onto my board, my legs fluid as I remember Maxime's technique lessons on the sand."

    hide surfboard_acc_back
    show mscmc surfer_hairup smile surfboard
    "My legs are firmly planted and my arms are steady and sure as I ride the wave."
    "It's a freeing sensation—I toss back my head, letting the wind beat my cheeks, but all the while something nags at the back of my mind."

    play music mscsadtimes
    show mscmc surfer_hairup_cu sad_cu -surfboard at mscmc_cu
    "(What more do I want? What could be better than this?)"
    show surfboard_acc_back behind mscmc:
        zoom 0.9
        xpos 135
        ypos 400
    show mscmc surfer_hairup sad at centre
    play sound splash04
    show surfboard_acc_back:
        ease 0.6 xoffset -100
    show mscmc:
        parallel:
            ease 0.6 xpos stagepos[1]+100
        parallel:
            block:
                linear 0.3 yoffset -20
                linear 0.3 yoffset 130
    "I hop off my board as I hit the shallows, dissatisfied with my ride in a way I can't pin down."

    hide surfboard_acc_back
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu:
        yanchor 177
    "(Well, time for my shift at the surf shop. Maybe I'll feel better after a break.)"

    hide mscmc
    scene bg msc_surf_shop_day at bg with fade
    play music mscsurfshop
    show trina casual sad at centre
    "I enter the surf shop to find Trina standing in front of her lessons schedule and pursing her lips."
    show mscmc casual_hairdown smile at left1plus
    show trina casual basic at right1plus
    mcmax "Hey Trina! Everything okay?"
    show trina casual smile
    "Trina smiles over her shoulder, a little distracted."
    show mscmc casual_hairdown basic
    so "Oh, nothing I can't handle—just trying to divide up what used to be Maxime's surf class."
    show trina casual sad
    so "Er, I mean—!"
    "She stiffens, realizing what she just said, and looks at me worriedly."
    hide trina
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(Because Trina thinks we've got unresolved romantic attraction. She doesn't know about the merman angle.)"
    show mscmc casual_hairdown smile at left1plus
    show trina casual sad at right1plus
    "I roll my eyes, batting a hand as I take my place behind the counter."
    show mscmc casual_hairdown grin
    mcmax "Trina, you can talk about Maxime around me. It's not a big deal."
    mcmax "I mean, he was just training me for the one surf competition. I asked him to, because he's a pro. That's all there was to it."
    hide trina
    play music mscmaxime
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Well, not really, but...)"

    hide mscmc
    scene white
    pause 0.2
    scene bg msc_labeach_night at bg, grayscale with dissolve
    show mscmc jacket_hairdown surprised at left2, grayscale
    show maxime casual sad at right2, grayscale
    mx "I'm a spy for the mer government and spying isn't a line of work where you can get close to people."
    show mscmc jacket_hairdown sad
    mx "I've made this bed, so now I've got to sleep in it."
    mcmax "You've helped me so much, and even now, you're still looking out for me."
    show maxime casual basic
    mcmax "I hope I've helped you too, even if I was your confidant for only a few days."

    hide maxime
    hide mscmc
    scene white
    pause 0.2
    scene bg msc_surf_shop_day at bg with dissolve
    play music mscsadtimes
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(I still can't believe he trusted me with the secret of his true occupation. He didn't even tell Dawn, his best friend.)"
    show mscmc casual_hairdown_cu sad_cu
    "(I thought that meant I was special to him. But...he left anyway.)"
    hide mscmc
    play sound "audio/msc/bell-store-entrance-ding.mp3"
    play music mscmctheme
    "The bell above the door jingles, and I have to train myself not to look up hopefully."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(For weeks after Maxime left, I kept expecting him to walk through the door like nothing had changed.)"
    "(Ugh, get over it, [genericfn]. Find something useful to do.)"
    
    hide mscmc
    $menuhideborder = True
    menu maximee01c1:
        "A. Refold the ahola shirts.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            "(I'll make sure our aloha shirt section is nice and tidy. Customers never get the folds quite right.)"
            hide mscmc
            "I step quickly around the counter, reaching for a rumpled shirt."
        "B. Stock the new sunscreen.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(Oh, that new sunscreen brand just came in! I should set up a display.)"
            hide mscmc
            "The box of sunscreen is large enough to obstruct my view as I heft it up."
        "C. Set out free samples.":
            $menuhideborder = False
            # missing :(

    "I'm vaguely aware of whoever just entered, but I'm so through with being disappointed that I studiously ignore them."
    show maxime casual basic with dissolve:
        yanchor 105
        xpos stagepos[1]-110
        zoom 1.25
        ease 0.3 zoom 1.33
        ease 0.3 zoom 1.30
    play music mscloveinterest
    "When I straighten up, I nearly slam into a wall of solid muscle and sculpted pecs behind a button-up shirt."
    hide maxime
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Wait a minute...)"
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    mx "Hey, [genericfn]."
    "I look up, my jaw dropping at the sight of Maxime's familiar, slightly sheepish smile."
    hide maxime
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(It's him...and he's just as tall and chiseled as I remember, with those beautiful eyes...)"
    show mscmc casual_hairdown surprised at left2
    show maxime casual smile at right2
    "Maxime chuckles nervously."
    mx "We've really got to stop meeting like this, don't we?"
    "His voice is a deep rumble in my chest, robbing me of any further words."
    hide maxime
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(This is too much. My brain is misfiring.)"
    "(I need air.)"

    hide mscmc
    $menuhideborder = True
    menu maximee01c2:
        "A. Freudian slip about fish!":
            $menuhideborder = False
            show mscmc casual_hairdown surprised at left2
            show maxime casual basic at right2
            mcmax "Wow, uh...I wasn't expecting you. Can you give me a minute? Otherwise I'm going to keep staring at you like a fish."
            mcmax "Not to randomly bring up fish. Okay, be right back."
            hide mscmc
            hide maxime
        "B. Start babbling!":
            $menuhideborder = False
            show mscmc casual_hairdown surprised at left2
            show maxime casual basic at right2
            "I start babbling, frantic to make him understand."
            mcmax "Holy cow, it's really good to see you, but I never thought I'd see you again, and it's a lot to process..."
            mcmax "Can you just give me a minute? I promise I'll be right back."
            hide mscmc
            hide maxime
        "C. Customer service skills to the rescue!":
            $menuhideborder = False

    "I promptly scurry for the door, taking deep gulps of sea air as soon as I'm outside."
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(It's fine! That was totally natural!)"
    show mscmc casual_hairdown smile at centre
    "I smooth my locs back, trying not to picture Maxime's surprised expression."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(But he's got to understand—I accepted that I would never see him again, to always be wondering 'what if'.)"
    show mscmc casual_hairdown_cu surprised_cu
    "(And now he's suddenly back, just like I wanted!)"
    show mscmc casual_hairdown_cu sad_cu
    "(But why? What's going on?)"

    play music mschappytimes
    hide mscmc
    "I force myself to breathe deep, then turn and step back into the shop, the only place I'll find any answers."
    show maxime casual smile at centre
    "Maxime is still standing quietly by the counter, and gives me an apologetic, sympathetic smile."
    show mscmc casual_hairdown grin at left2
    show maxime casual basic at right2
    mcmax "Hi, I'm back. Needed to restart my brain for a moment there."
    show mscmc casual_hairdown smile
    show maxime casual sad
    mx "I don't blame you. I wasn't sure you'd want to see me."
    show mscmc casual_hairdown surprised
    show maxime casual basic
    mcmax "No, no, I'm really glad you're here—!"
    hide maxime
    hide mscmc
    show trina casual smile at centre with dissolve
    "Trina pokes her head out from the back of the shop, face lit up with a grin."
    so "{i}Maxime!{/i} Always so good to see you!"
    hide trina
    show mscmc casual_hairdown smile at left2
    show maxime casual smile at right2
    "Maxime smiles warmly at Trina, but takes a look around the shop, seeming to realize it's not the most private spot for a chat."
    show maxime casual basic
    mx "Look, I don't want to interrupt your work day. Can we talk at my place once you're off? I'm staying at the beach cottage again."
    show maxime casual smile
    mx "I'll make dinner. I feel like it's the least I can do."
    hide maxime
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(The answer is one-hundred-percent yes. Of course I want to talk to him privately, and ask him a million questions...And have dinner together...)"
    show mscmc casual_hairdown sad at left2
    show maxime casual basic at right2
    "Some small, petty part of me hesitates."
    hide maxime
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Maybe I want him to stew a little, since he's the one who went away.)"
    "(I don't want to get my hopes up if he's just going to leave again.)"
    hide mscmc
    show trina casual smile at centre
    "I bite my lip, but Trina enthusiastically pipes up on my behalf."
    so "Yes, [genericfn] would {i}love{/i} to have dinner with you!"
    "She cups her hand around her mouth, fake-whispering."
    so "She really likes pasta!"
    hide trina
    show mscmc casual_hairdown basic at left2
    show maxime casual smile at right2
    "I give Trina an unimpressed look, and Maxime chuckles, but turns to me, gently inquiring."
    mx "Is that alright with you, [genericfn]?"
    show mscmc casual_hairdown smile
    show maxime casual basic
    "I nod, breaking out in a smile despite myself."
    show mscmc casual_hairdown grin
    show maxime casual smile
    mcmax "I'll have dinner with you, Maxime. I'm off around 7."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime's face lights up, setting my heart thumping."
    mx "Great, I'll see you then. Pasta it is."

    play sound "audio/msc/bell-store-entrance-ding.mp3"
    show maxime casual basic at centre, out_right_slow
    "He nods to each of us gallantly, then ducks out of the shop. the bell jangling again."
    show mscmc casual_hairdown basic at left2
    show trina casual smile at right2
    "As soon as he's gone, Trina turns to me, jaw dropping."
    so "Ohmygooosh—!"
    show mscmc casual_hairdown sad
    mcmax "Please don't."
    show mscmc casual_hairdown smile
    "I roll my eyes fondly, making a shushing motion with my hand."
    mcmax "It's just dinner. For all we know he might have to leave tomorrow. It doesn't mean anything."
    "Trina snorts dubiously, turning back to count the money in the cash register."

    scene bg msc_maxime_studio_sunset at bg with clockwise_wipe
    play music mscmctheme
    "After locking up the surf shop, I walk across the beach to Maxime's apartment and enter his studio, my palms sweaty."
    "I'm drawn forward by the welcoming lights in the windows, and something that smells absolutely delicious cooking."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mcmax "Hello?"
    hide mscmc
    show maxime casual basic at centre
    "I find Maxime's broad shoulders hunched over a small kitchenette in the side of the studio."
    hide maxime
    "He's got this phone propped up on the cutting board beside him, with a video of an elderly woman in a frilly apron playing."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(How sweet that he looked up a cooking video for a pasta dish! Even sweeter that it's by a little old grandma.)"
    show mscmc jacket_hairdown smile at left2
    show maxime casual smile at right2
    "Maxime straightens up, excited and flustered."
    mx "[genericfn]! I'm just putting the finishing touches on the sauce, and then I'll get the pasta going."
    "He wipes his hands on his apron, taking stock of everything."
    show maxime casual smirk
    mx "I hope you like {i}frutti del mare{/i}."
    "I stand on my tiptoes to peer over his shoulder, my stomach rumbling."
    show mscmc jacket_hairdown grin
    show maxime casual basic
    mcmax "Handmade pasta and mussels? You're spoiling me."
    show mscmc jacket_hairdown smile
    show maxime casual embarrassed
    "Maxime chuckles, his cheeks darken."
    show maxime casual smile
    mx "Well, once you know how to make your own pasta, you never want to go back."
    "He straightens up, suddenly excited."
    mx "Hey, since you're here, you can be my taste-tester!"

    hide mscmc
    hide maxime
    scene bg msc_maxime_s1_mini1 at bg with dissolve
    play music mscromance
    mx "It's, ah, the first time I've tried this recipe, so I want to make sure the arrabiata is just right."
    "He dips his spoon into the bright red tomato sauce, letting it cool before holding it out to me hopfully."
    "(Oh gosh, how's that for a cute, romantic gesture?)"

    $menuhideborder = True
    menu maximee01c3:
        "A. Be Maxime's taste-tester!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            scene bg msc_maxime_studio_sunset at bg with dissolve
            "I lean forward, taking a gentle taste from Maxime's spoon."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmax "Mm, that's delicious!"
            "The heat of the peppers warms me up inside, bringing a light into my eyes."
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime breaks into a delighted smile."
            mx "Really? It's not too spicy?"
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmax "I'm Jamaican, I love spicy food! What's that little kick I'm tasting?"
            show maxime casual smile
            mx "Red hot chili flakes, just like 'CookingNana1954' recommends."
            show mscmc jacket_hairdown surprised
            mcmax "Can we add more? Er, unless you're not so into chili peppers."
            "Maxime shakes his head, grinning."
            show mscmc jacket_hairdown smile
            mx "Nah, we are definitely on the same page here. Chili all the way."
            show maxime casual basic
            "He eagerly sprinkles more pepper flakes over the sauce before giving it a good stir."
            show maxime casual smirk
            mx "It's nice to have a friend who appreciates spicy food. Every time I cook for Dawn I have to make sure I have a carton of milk handy."
            show mscmc jacket_hairdown grin
            show maxime casual smile
            mcmax "I know, them and their 'mild burritos'. Like, what's the point?"
            "We laugh together, while I feel a bit giddy he called me a 'friend.'"
            "Maxime offers me the spoon again."
            mx "How's that for spice-levels?"
            hide mscmc
            hide maxime
            "I take another taste, and instantly give a thumbs-up, the spice dancing over my tongue."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmax "That's chef's-kiss worthy."
            show mscmc jacket_hairdown smile at left2
            show maxime casual basic at right2
            show mscmc jacket_hairdown smile behind maxime:
                ease 0.5 xpos stagepos[1]-140
            "I take the opportunity to inch closer to him, our arms almost brushing as I watch 'CookingNana' prepare her shrimp."
            hide mscmc
            hide maxime
            $sidecharone = "Viral Sensation CookingNana"
            sid1 "Now, my grandson—hi, Andre, I love you Sweetie!—like his frutti del mare good and spicy."
            $sidecharone = "CookingNana"
            sid1 "So I'm going to sprinkle a bit of those pepper flakes over the shrimp, just to make sure the flavor really sinks in."
            sid1 "And this is where making your own pasta really pays off, because that fresh dough will balance the spice. Mmm!"
            show mscmc jacket_hairdown grin behind maxime at left1plus
            show maxime casual basic at right2
            mcmax "Where did you find this lady? She's adorable."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Isn't she? She's my favorite chef on the net, hands-down."
            mx "Apparently her grandson showed her how to film a recipe one day, and it all blew up from there."
            "I hide a smile, noticing the way his shoulders relax and he seems to practically glow with enthusiasm."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Maxime is a CookingNana fanboy. This is too cute for words.)"
            show mscmc jacket_hairdown smile behind maxime at left1plus
            show maxime casual smile at right2
            mx "She's always talking about her grandkids while she cooks."
            mx "She made a unicorn cake for her granddaughter, and one of the kids has celiac, so she's got a whole playlist with recipes he can eat."
            show mscmc jacket_hairdown embarrassed
            "He rests his chin on his palm, watching CookingNana with a fondness that makes my heart completely melt."
            hide maxime 
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I bet he's great with grandparents. I mean, of course he is—he's Maxime. My grandma would {i}love{/i} his gentlemanly ways.)"
            show mscmc jacket_hairdown grin behind maxime at left1plus
            show maxime casual basic at right2
            mcmax "Do you cook a lot?"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Not as much as I probably should. I like to cook, but it's difficult to find the motivation when you're only cooking for youself."
            mx "That's why I like to cook for other people and find out what their favorite dishes are. For instance, now I know that you love a good pasta..."
            show mscmc jacket_hairdown grin
            mcmax "I do. Trina's out here sharing all my secrets."
            show mscmc jacket_hairdown embarrassed
            show maxime casual basic
            "I rest my elbows on the counter, close enough that my arms brushes his firm muscles as he stirs the sauce."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Suddenly, I'm struck anew by how mich I missed him these past months...Iwish I could stand even closer to him.)"
            show mscmc jacket_hairdown basic behind maxime at left1plus
            show maxime casual basic at right2
            "I clear my throat quickly, keeping my voice light."
            show mscmc jacket_hairdown surprised
            mcmax "Can I help with anything?"
            show mscmc jacket_hairdown smile
            "Maxime surveys the counter thoughfully, then grabs another small bowl full of freshly baked brussel sprouts."
            show maxime casual smile
            "Actually, I made a glaze for these, if you want to put it on. Fresh balsamic."
            show mscmc jacket_hairdown surprised
            mcmax "Whoa, did you make everything from scratch?"
            "Maxime chuckles at my amazement."
            mx "Well, not the shrimp and mussels. The ocean did that."
            hide mscmc
            hide maxime
            "I drizzle the brussel sprouts in balsamic carefully, trying to make CookingNana and Maxime proud."
            "It's a nice, cozy feeling to stand side-by-side in the kitchen, while preparing food and exchanging smiles at CookingNana's video."
            "When Maxime ladles out the pasta and sauce, the smell fills the room and sets my mouth watering again."
            show mscmc jacket_hairdown smile at left1plus
            show maxime casual smile behind mscmc at right2
            mx "I think we're ready!"
            "He reaches around, pulling a stool for me to sit on."
            show mscmc jacket_hairdown embarrassed
            "I settle down, looking up at him shyly."
            show mscmc jacket_hairdown grin
            mcmax "Such a gentleman, like always."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Whoa there, when did I become such a smooth operator? It must be the atmosphere...)"
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "He flushes, laughing nervously, though he can't hide a smile as he turns back to the pasta."
            hide maxime

        "B. Decline the tasting.":
            $menuhideborder = False

    play music mscloveinterest
    "I watch as Maxime tidies the kitchenette and grabs garnishes, salt and pepper from the cabinet."
    "He brings me a steaming bowl of pasta and a beer from the fridge, pulling a crate up beside me."
    show mscmc jacket_hairdown smile at left2
    show maxime casual smile at right2
    mx "I'm still unpacking in the dining room, so we can set up here. Call it rustic."
    show maxime casual basic
    "He tugs another crate between us, creating a makeshift table."
    show mscmc jacket_hairdown grin
    mcmax "I like eating with all your paintings around. I missed them."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I missed {i}you{/i}.)"
    show mscmc jacket_hairdown smile at left2
    show maxime casual basic at right2
    "I take a bite of pasta to distract myself, and hum happily, enjoying the garlic and pepper flakes."
    show mscmc jacket_hairdown grin
    mcmax "Mm, that's delicious. Now I can add 'amateur cook' to the neverending list of your talents."
    show maxime casual embarrassed
    "Maxime chuckles, bashful but gratified."
    show mscmc jacket_hairdown smile
    show maxime casual smile
    mx "So, what's going on with you? Have you entered the new competition?"
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What's going on with me? What's going on with {i}you{/i}, Mister Super-Spy?)"
    show mscmc jacket_hairdown smile at left2
    show maxime casual basic at right2
    "I swallow my questions, forcing myself to be patient."
    show mscmc jacket_hairdown grin
    mcmax "'Beach Battle Surf Showdown'? I am, actually."
    show maxime casual smile
    mx "And how are you feeling about it?"
    show mscmc jacket_hairdown basic
    show maxime casual basic
    "I shrug, reminded of my less-than-satisfactory practice that morning."
    show mscmc jacket_hairdown surprised
    mcmax "I think I'm well-prepared, though I definitely want to polish my tricks before the first round of events on Monday."
    show mscmc jacket_hairdown grin
    mcmax "Since it's privately funded, there's going to be a lot of sponsors and big names watching. Trina thinks this could be my big break."
    show maxime casual smile
    "I glance up at Maxime, and find his expression a strange mix of pride, but also uncertainty."
    show mscmc jacket_hairdown smile
    "I set my bowl down gently."
    show mscmc jacket_hairdown sad
    show maxime casual basic
    mcmax "Maxime, you know I'm really, really happy to see you again, but I have to ask..."
    show mscmc jacket_hairdown surprised
    show maxime casual sad
    mx "Why am I here?"
    show mscmc jacket_hairdown smile
    show maxime casual smile
    "He chuckles ruefully."
    
    play music mscsuspense
    show maxime casual basic
    mcmax "It's business, isn't it?"
    show maxime casual sad
    "I keep my voice clear of judgement, but he winces all the same."
    mx "The local mer government is investing Wikus Sapor, the man who's bankrolling the surf tournament. He's one of ours."
    show mscmc jacket_hairdown surprised
    mcmax "Wikus Sapor is a mer? I thought he was just some rich, {i}human{/i} entrepreneur!"
    mx "He was a famous academic back in Maritas—the mer city—but he got thrown out of the university for... unethical experiments."
    show maxime casual basic
    mx "I don't know all the details, but he's definitely a person of interest..."
    show maxime casual sad
    mx "And no one's quite sure why he's suddenly so enthusiastic about human surfing competitions."
    show mscmc jacket_hairdown basic
    show maxime casual basic
    mcmax "And you've been sent to keep an eye on him?"
    show mscmc jacket_hairdown smile
    show maxime casual sad
    "I smile, but Maxime ducks his head."
    show mscmc jacket_hairdown basic
    mx "Here's where it gets difficult. Do you remember Camilla?"
    show mscmc jacket_hairdown surprised
    mcmax "Your mean boss lady? She's hard to forget."
    show mscmc jacket_hairdown basic
    show maxime casual smile
    "Maxime has to bite back a surprised laugh."
    show maxime casual sad
    mx "Yes. Camilla wants me to ask to be your trainer again, but what I'm not supposed to tell you is that it would be a cover to spy on Wikus."
    mx "Obviously, I'll tell her you aren't interested, but I didn't want you to be in the dark about what's going on, or Camilla's plan."

    play music mscmaxime
    show mscmc jacket_hairdown surprised
    "I open my mouth to protest, then take a moment to think."
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Knee-jerk reaction: of course I want Maxime to be my trainer again!)"
    show mscmc jacket_hairdown_cu sad_cu
    "(Because he's a great trainer, and I don't want to say goodbye again just yet, not if I can help it.)"
    show mscmc jacket_hairdown_cu surprised_cu
    "(Of course, spying on Wikus sounds dangerous, but isn't it better to face danger with Maxime around?)"
    show mscmc jacket_hairdown grin at left2
    show maxime casual basic at right2
    mcmax "Wait, I've got a better idea."
    show maxime casual surprised
    "Maxime's eyes widen and he leans forward, waiting intently."
    hide maxime
    hide mscmc

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.