label fiona_season1_episode8:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_desert_springs_day at bg
    play music wllfionatheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Fiona takes me to the hot springs the next day."
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(She said she needed time to prepare)"
    show wllmc skirt_cu smirk_cu
    "(But I wonder if she just wanted me to spend half the night tossing and turning in my bunk with anticipation.)"
    hide wllmc
    show wllmc skirt smallsmile at left2
    show fiona under smile at right2
    mb "I brought some sanctified candles and a mix of potent herbs."
    mb "Combine those with the natural properties of the spring and this should work."
    "She hands me the candles and instructs me to put them around the room while she mixes the herbs into the water."
    show wllmc skirt smile
    mcfiona "I smell mint, lavender, what else?"
    "I set down another candle."
    hide fiona
    hide wllmc
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(Just one more to go.)"
    hide wllmc
    show wllmc skirt smallsmile at left3
    show fiona under grin at right3
    mb "Sage. And star anise."

    scene fiona_s1_ei3 with fade:
        align(0.5, 1.0) transform_anchor True zoom 1.3
        pause 1.0
        linear 5.0 yoffset 1400
    pause
    "I light the final candle and turn around to see Fiona sitting at the edge of the pool, her clothes folded in a neat pile on the ground."
    "(Oh.)"
    "Steam curls around her, leaving faint traces of condensation on her gleaming skin."
    mcfiona "You're very eager, aren't you?"
    "Fiona leans back a little, her braids trailing over her shoulders."
    "(I can see in her eyes how much she's enjoying me staring at her like this.)"

    scene bg_wll_desert_springs_day at bg
    show wllmc skirt smallsmile at left3
    show fiona under basic at right3
    with fade
    mb "I have to be purified first, before I can touch you."
    mb "I'm your acolyte today. I have to be prepared to guide you into wakefulness."
    hide wllmc
    show fiona under basic at centre
    "She stands up, and I get a good long look at her lithe body and taut limbs, and then she dives into the pool."
    hide fiona
    show wllmc skirt_cu embarrassed_cu at wllmc_cu
    "(The steam sure does make it warm in here.)"
    hide wllmc
    show fiona under smile at centre
    "Before I can start taking my own clothes off, Fiona emerges again, dripping wet."
    "I find myself following the path of the water droplets as they glide down her body."
    show wllmc skirt grin at left3
    show fiona under grin at right3
    mb "Don't touch yourself. The ritual demands that you be disrobed by cleansed hands."
    show wllmc skirt smirk
    mcfiona "Oh, the ritual demands it? Is that your excuse?"
    show fiona under smirk
    mb "And isn't it a good one? Because you can't be sure I'm wrong."
    hide wllmc
    hide fiona
    "She moves behind me and begins undoing buttons and laces."
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(Sometimes an imagination is a cursed thing to have.)"
    hide wllmc
    show fiona under smirk at right1
    show wllmc skirt surprised at left1
    "When she pushes back the folds of cloth and lays bare my back I let out a little gasp."
    mcfiona "The air is colder than I thought it would be."
    show fiona under grin
    mb "Soon you'll be very warm."
    "I feel her lips press a kiss to my spine, between my shoulder-blades."
    mb "The spring is heated naturally, you see."
    show wllmc skirt grin
    "I can't help the laugh that bubbles up from deep within me."
    mcfiona "Oh, the spring is heated. Is that what you meant?"
    hide wllmc
    hide fiona
    "Inch by inch, Fiona peels away cloth until I'm as naked as she is."
    show fiona under_cu smile_cu at fiona_cu
    mb "You really are a priceless treasure, my pearl."
    mb "Let's finish the ritual, and then I want you."
    hide fiona
    show fiona under grin at right1
    show wllmc under embarrassed at left1
    "Blood rushes to my face and I don't even try to hide it, but I manage to keep my voice level."
    mcfiona "Whatever happened to keeping me as a reward for yourself?"
    show fiona under smirk
    mb "I'm very impatient. And technically, I only hired you to help me get the locket, you know."
    show wllmc under smile
    mcfiona "I love a good technicality."
    hide fiona
    hide wllmc
    "Fiona steps into the water first, and leads me in after her, helping me to sink slowly deeper until I'm completely immersed."
    show wllmc under_cu surprised_cu at wllmc_cu
    "(I don't feel any different.)"
    hide wllmc
    "The universe, as usual, has an irritating sense of irony, because as soon as I think that, I do feel something."
    show fiona under smile at right1
    show wllmc under surprised at left1
    mcfiona "Something is happening."
    hide fiona
    hide wllmc
    show soft_sparkle_effect
    "Everything around me shimmers, like every object around me is lit from the inside out."
    show wllmc under_cu grin_cu at wllmc_cu
    "(I think I could do anything right now.)"
    hide wllmc
    hide soft_sparkle_effect

    $menuhideborder = True
    menu fionas1e8c1:
        "Make every flame ten feet tall.":
            $menuhideborder = False
            "With barely a thought, with barely a push, I draw every flame from every candle up and up and up."
            show fiona under_cu surprised_cu at fiona_cu
            mb "Incredible!"
            "She glows in the wavering light they create, like some beautiful nymph from an ancient myth."
            hide fiona
        "Shape the steam into a dragon.":
            $menuhideborder = False
            "I gather the steam into a roiling mass and shape it into a huge dragon that opens its massive jaws and roars soundlessly at us."
            show fiona under_cu grin_cu at fiona_cu
            mb "Amazing."
            "The wide-eyed delight in her eyes makes me feel very proud of myself."
            hide fiona
        "Make the water glow gold.":
            $menuhideborder = False
            "I set my hands on the surface of the water, and a ripple spreads, turning the crystalline water to glowing gold."
            show fiona under_cu smile_cu at fiona_cu
            mb "Oh, this is beautiful."
            hide fiona
            show wllmc under_cu embarrassed_cu at wllmc_cu
            "(I'm never going to tell her I was inspired by the color of her eyes.)"
            hide wllmc

    "The magic vanishes as quickly as it came, but it was there."
    show fiona under grin at right1
    show wllmc under surprised at left1
    mb "It worked!"
    show wllmc under smallsmile
    mb "Maybe I can see your future now."
    hide wllmc
    hide fiona
    show fiona under_cu sad_cu at fiona_cu
    "Before I can decide how I feel about that, she tries. I see the distant look come into her eyes for a moment."
    show fiona under_cu angry_cu
    mb "Still nothing. {i}Why{/i}?!"
    hide fiona
    show fiona under angry at right1
    show wllmc under surprised at left1
    mcfiona "Is it really that important?"
    hide wllmc
    hide fiona
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    show fiona under_cu surprised_purple_cu at fiona_cu
    "Fiona doesn't answer. Her eyes are filled with that ferocious light again."
    hide fiona
    show wllmc under_cu surprised_cu at wllmc_cu
    "(Her patron is back.)"
    hide wllmc
    show fiona under sad_purple at right1
    show wllmc under angry at left1
    "I keep her steady in the water until the vision fades."
    show fiona under sad with dissolve
    "The words that fall from her lips are as nonsensical as last time, but when she comes back to herself she explains immediately."
    mb "That was a lot. Things are shifting. A performer booked for the celebration isn't coming."
    mb "Diana is upset. She goes to look for something in her pocketbook. She finds her pocketbook, but the thing she wants isn't there."
    show fiona under angry
    "She looks at me sharply."
    mb "Didn't you steal her pocketbook?"
    show wllmc under sad
    mcfiona "Don't tell anyone, but I gave it back. I was stricken down with a sudden attack of conscience."
    mb "Well, something got left behind."
    hide fiona
    hide wllmc
    "We hop out of the pool, and I rummage through my pockets."
    show wllmc under_cu surprised_cu at wllmc_cu
    "(Aha.)"
    hide wllmc
    show wllmc under surprised at left2
    show fiona under surprised at right2
    mcfiona "It's a photo."

    scene fiona_s1_mini5 at bg with fade
    show cinema_fov at cinema_fov_in
    pause 1.0

    "It's slightly crumpled, but still in pretty good condition."
    mb "That's Diana on the left. Who's the woman on the right?"

    show cinema_fov at cinema_fov_out
    scene bg_wll_desert_springs_day at bg
    show wllmc under sad at left2
    show fiona under surprised at right2
    with fade
    mcfiona "It must be her wife. And..."
    "The last half of the sentence gets stuck in my throat, and Fiona says it for me."
    show fiona under sad
    mb "She's our ghost."

    scene bg_wll_ward_hq_lights at bg with fade
    stop music fadeout 1.0
    play music wlltense2 fadein 1.0
    "Our discovery is urgent enough that Fiona wastes no time in dragging me back to the ward headquarters."
    show wllmc skirt_cu basic_cu at wllmc_cu
    "(It's alright. A bit formal for my tastes.)"
    hide wllmc
    show cecelia dunevest sad at centre
    "Cecelia's frown gets deeper and sharper as we explain what we've found."
    hide cecelia
    show sascha vest sad at centre
    sasch "So the ghost is Sunmok."
    hide sascha
    show nathan redvest sad at centre
    wc "Explains a lot really. She was anticipating a good life, building a home, and then she died."
    wc "That's the kind of unfinished business that tethers you real strong."
    hide nathan
    show fiona cape sad at centre
    mb "Diana said the locket was an heirloom of Sunmok's, so maybe it was something that called to her."
    show fiona cape sad at left3
    show cecelia dunevest basic at right3
    vr "That would explain your vision. But there must be more."
    "I think back to our conversation with Diana, and the tell that wasn't a tell pops out at me again."
    hide fiona
    show wllmc skirt surprised at left3
    mcfiona "Oh, damn, I think it's her wedding ring."
    hide cecelia
    hide wllmc
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(Not just a powerful symbol, but one that Diana herself values. That seems like just the thing magic would latch onto.)"
    hide wllmc
    show wllmc skirt surprised at left3
    show fiona cape surprised at right3
    mb "Of course."
    show wllmc skirt angry
    hide fiona
    show cecelia dunevest angry at right3
    vr "That makes things complicated. If we can't isolate the object, we'll have to perform Canto's nine-star Seal."
    vr "I'll have to call the regional Captain and start requisitioning help and supplies."
    hide wllmc
    show sascha vest surprised at left3
    sasch "Why don't we just steal it?"
    show sascha vest smirk
    sasch "I'm sure Fiona's nimble fingers are up to the task, but I'm happy to take distraction duty."
    show cecelia dunevest surprised
    vr "Hm. That would be simpler...."
    hide sascha
    hide cecelia
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(They're just going to steal it?)"
    hide wllmc
    show nathan redvest angry at centre
    "I see Cayde looking shifty, chewing on his cheek, but he doesn't speak up."
    hide nathan
    show wllmc skirt_cu angry_cu at wllmc_cu
    "(Guess it's on me, then.)"
    hide wllmc
    show wllmc skirt angry at left3
    show cecelia dunevest surprised at right3
    mcfiona "You can't steal her wedding ring!"
    show cecelia dunevest angry
    "Cecelia narrows her eyes at me and gives me an authoritative stare."
    vr "Why not?"
    hide wllmc
    hide cecelia

    $menuhideborder = True
    menu fionas1e8c2:
        "It's important to Diana.":
            $menuhideborder = False
            show wllmc skirt angry at left3
            show cecelia dunevest angry at right3
            mcfiona "It's important to Diana. And she hasn't done anything wrong except lose a wife."
            hide cecelia
            show fiona cape sad at right3
            "Fiona shoots me a sympathetic look but doesn't say anything."
            hide fiona
        "I thought you guys were lawful.":
            $menuhideborder = False
            show wllmc skirt angry at left3
            show cecelia dunevest angry at right3
            mcfiona "I thought you guys were supposed to be on the side of law and justice."
            mcfiona "But it doesn't seem like there's much justice here."
            vr "We are. But our laws take precedence over mortal ones."
            hide cecelia
        "We already took one memento from her.":
            $menuhideborder = False
            show wllmc skirt angry at left3
            show cecelia dunevest angry at right3
            mcfiona "We already took one memento from her. This is the only thing she has left."
            vr "That doesn't change the facts of the situation."
            hide cecelia
    show wllmc skirt sad
    show sascha vest angry at right3
    sasch "The ghost is getting more and more dangerous. There have been other sightings, reports of attacks."
    hide sascha
    show nathan redvest angry at right3
    wc "Sooner or later, someone's going to wind up dead."
    show wllmc skirt angry
    mcfiona "Then at least tell Diana that!"
    hide nathan
    hide wllmc
    show wllmc skirt_cu angry_cu at wllmc_cu
    "(I can't believe I'm the one arguing for honesty here. When did our roles get reversed?)"
    hide wllmc
    show wllmc skirt angry at left3
    show cecelia dunevest angry at right3
    vr "No. Keeping the otherworld secret is our most important task. Some rules don't break for anything."
    hide cecelia
    show fiona cape sad at right3
    "I turn to Fiona, staring at her with every ounce of feeling I've got."
    mcfiona "Fiona, back me up on this! What happened to not crossing the lines we draw for ourselves?"
    "Fiona looks down at the ground for a moment, then back up at me."
    show fiona cape angry
    mb "My patron saw it. The future is a flexible thing. It bends and shifts."
    mb "But when my patron speaks, its words are immutable. What it says always comes to pass."
    show wllmc skirt surprised
    mcfiona "So you just let it lead you? You accept that?"
    mb "I don't fight losing battles."
    hide fiona
    hide wllmc
    show wllmc skirt_cu angry_cu at wllmc_cu
    "(This is bullshit.)"
    hide wllmc
    show fiona cape_cu sad_cu at fiona_cu
    "I clamp down on the thought, but Fiona is too quick for that. She leans over and pats my arm."
    mb "In all my family's history, no one has ever changed my patron's predictions."
    show fiona cape_cu smile_cu
    mb "But then again, in all that time, it's never come up against anyone quite like you, sweet complication."

    scene bg_wll_town_streets_day at bg
    stop music fadeout 1.0
    play music wlleverydayupbeat1 fadein 1.0
    show wllmc coat_hat basic at left3
    show fiona capehood basic at right3
    with wiperightdissolve
    "My unhappiness with the Ward's decision eats at me as we walk to the Town Hall to find Diana."
    show wllmc coat_hat angry
    mcfiona "Cecelia didn't seem very happy with us back there. All those threats about following protocol."
    show fiona capehood smile
    mb "Cece finds rules comforting. That's just one of the things that makes her her."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(We've been given permission to 'scope out the situation', but not much more than that.)"
    "(It's clear Cecelia thinks I'm a bad influence on Fiona.)"

    scene bg_wll_town_hall_lights at bg
    show mcgann coat basic at centre
    with wiperightdissolve
    "At the Town Hall we run into the sheriff, who tells us in no uncertain terms that Diana is unavailable."
    $sidecharone = "Sheriff"
    sid1 "Something went missing from the exhibit, and she's distraught."
    sid1 "She's locked herself up in her office and she's only talking to potential replacement acts for the celebration."
    show fiona cape smile at left3
    show mcgann coat surprised at right3
    mb "I might be able to help you there, Sheriff. I found this on the ground near my shop earlier."
    show mcgann coat smirk
    "She hands him the locket, and the Sheriff nods amicably."
    sid1 "Thanks for turning it in. I'll pass it on to her."
    hide mcgann
    show fiona cape smile at centre
    "He walks off, leaving Fiona and I alone."
    show wllmc coat surprised at left3
    show fiona cape smile at right3
    mcfiona "What now?"
    mb "With any luck, Diana comes out to give us a personal thank you."
    show wllmc coat smile
    mcfiona "And then we talk to her."
    show fiona cape smirk
    mb "And then we steal her ring."
    show wllmc coat angry
    "I clench my jaw and glare at her."
    mcfiona "I thought you were on board with trying to change the future!"
    mb "I admire your guts, my treasure. I really do. But this is a job, and I don't roll dice on a job."
    show fiona cape angry
    mb "I'm not going to take a risk on an uncertainty and burden my team or endanger the town."
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(What can I say to that?)"
    hide wllmc
    show wllmc coat sad at left3
    show fiona cape angry at right3
    "The wrongness of it eats at me, but I haven't got a big high-minded comeback like Fiona, only the wayward impulses of my own heart."
    show fiona cape smirk
    mb "Why is this so important to you anyway? You never struck me as the type to be precious about objects."
    mb "Certainly not other people's, anyway."
    show wllmc coat smirk
    "I have to laugh at that, but I want to explain myself too."
    show wllmc coat basic
    mcfiona "It's not the object, it's what it means."
    hide wllmc
    hide fiona

    $menuhideborder = True
    menu fionas1e8c3:
        "It's her memories.":
            $menuhideborder = False
            show wllmc coat angry at left3
            show fiona cape surprised at right3
            mcfiona "When Diana touches that ring, you can see her thinking back to her wife."
            mcfiona "The ring is a touchstone, the last real, touchable thing she has of a person who's gone forever."
        "It represents commitment.":
            $menuhideborder = False
            show wllmc coat angry at left3
            show fiona cape surprised at right3
            mcfiona "Diana used that ring to make a promise. A promise so big and important, she still honors it even though the person she made it to is dead."
        "I wouldn't take bread from a beggar.":
            $menuhideborder = False
            show wllmc coat angry at left3
            show fiona cape surprised at right3
            mcfiona "It's like, I wouldn't take bread from a beggar. It's one thing to steal money from a bank or jewels from a princess."
            mcfiona "It's another to take away what people hold dear."

    show wllmc coat sad
    mcfiona "I just can't bring myself to steal that ring."
    show fiona cape smile
    "I look right at Fiona, wanting her to see how this gnaws at me, and she looks back, respect in her eyes."
    mb "I confess, I thought you were a cynic through and through. But there's a streak of pure idealism in that heart of yours."
    mcfiona "There's so many in this world who never get love. So many who settle for comfort or companionship or just safety."
    show wllmc coat angry
    mcfiona "So it has to mean something, the people who find love and bet on it despite all the risks."
    mcfiona "I might not have personal experience, but I admire anyone who goes in all or nothing in this life."
    show fiona cape angry:
        easein 0.6 right1
    "Fiona's eyes crinkle, and she slips her hand into mine."
    hide wllmc
    hide fiona
    show fiona cape_cu grin_cu at fiona_cu
    mb "You and me both. We're like hawks up in the blue sky, watching the rabbits down below and wishing we had so many friends."
    mb "I hope someday you get the chance to place your all or nothing bet."
    hide fiona
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(I've never told anyone else that. And even if I had, I don't think they would have understood me the way Fiona does.)"
    show wllmc coat_cu basic_cu
    "(Maybe I could do the same in return.)"
    hide wllmc
    show wllmc coat basic at left3
    show fiona cape grin at right1
    mcfiona "What about you?"
    show fiona cape surprised
    mcfiona "What do you think about love?"
    hide fiona
    hide wllmc

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
