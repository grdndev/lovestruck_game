label fiona_season1_episode7:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_town_streets_night at bg
    play music wllaction1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show sunmok ghost veryangry at centre
    "The ghost draws closer, its eyes burning with a terrible fury."
    hide sunmok
    show wllmc vest_hat angry at left1plus
    show fiona cape angry at right1
    mb "[genericfn], stay back! It's more dangerous now than it was before."
    "I do exactly the opposite. I put myself between Fiona and the ghost, drawing my revolver."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(I still have those silver bullets Sascha gave me. Time to see if they really work.)"
    hide wllmc
    show wllmc vest_hat angry at left1plus
    show fiona cape surprised at right1
    mb "What are you doing?"
    mcfiona "Sascha told me you weren't a fighter."
    mb "But-"
    mcfiona "No time to argue."
    hide wllmc
    hide fiona
    play sound gunshot_2
    show sunmok ghost veryangry at centre
    "I fire off a shot, and see the bullet's trail as it passes through the ghost."
    hide sunmok
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    "(So it has some effect.)"
    hide wllmc
    show sunmok ghost veryangry at right3:
        pause 0.1
        easein 0.4 right1plus
    show wllmc vest_hat surprised at left1plus

    pause 0.5
    show bg_wll_town_streets_night at ghost_touch
    show wllmc vest_hat surprised at ghost_touch
    show sunmok ghost veryangry at ghost_touch
    with dissolve
    "But not nearly enough. The ghost surges forward, and her hands sink into my chest."

    scene bg_wll_town_streets_night at bg
    show fiona cape_cu surprised_cu at fiona_cu
    mb "No!"
    hide fiona
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(That hurts like the nine hells.)"
    hide wllmc
    show sunmok ghost veryangry at right1plus
    show wllmc vest_hat sad at left1plus
    "It's the worst feeling in the world. Not just physical cold, but an overwhelming despair."
    hide sunmok
    hide wllmc
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(I can't.)"
    hide wllmc
    show sunmok ghost veryangry at right1plus
    show wllmc vest_hat angry at left1plus
    "I battle against the tide of grief and misery, and with shaking hands, open the cylinder of my revolver and tip a bullet into my hand."
    hide sunmok
    hide wllmc
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(Give up.)"
    hide wllmc
    show sunmok ghost veryangry at right1plus
    show wllmc vest_hat angry at left1plus
    "I lift my hand and plunge it into the ghost, ignoring the shock of cold, and hold the bullet there."
    show wllmc vest_hat surprised
    show sunmok ghost veryangry:
        pause 0.1
        linear 0.6 xoffset 100 alpha 0.0
    "The ghost hisses, recoils, and vanishes."
    hide sunmok
    mcfiona "Did that work?"
    "My whole body is convulsing with shivers, but I stay on my feet, staring down the road."
    hide wllmc
    show fiona cape sleep_purple at centre
    mb "No. It's coming back for another attack."
    "Her hands are pressed tight against her temples, her eyes screwed shut."
    show wllmc vest_hat surprised at left3
    show fiona cape sleep_purple at right3
    mcfiona "You can see it?"
    mb "I can see what it's going to do, but every time you intervene, the futures shift."
    mb "It's... chaotic."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(The strain on her face tells me she's not having any easier a time than I am.)"
    hide wllmc
    show wllmc vest_hat surprised at left3
    show fiona cape sleep_purple at right3
    mcfiona "If you were with one of the others, what would you do?"
    mb "I'd give them instructions. Tell them where to dodge, how to move."
    show wllmc vest_hat angry
    mcfiona "Okay. Let's try it. It's better than nothing."
    mb "I'll do my best."
    hide wllmc
    show fiona cape sleep_purple at centre
    "She bites down on her lip sharply."
    mb "On your left, about twenty paces away, in three seconds."
    hide fiona
    show wllmc vest_hat angry at centre
    "I slam the cylinder of my revolver shut again and take aim, using both hands to keep the gun steady."
    hide wllmc
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(My movements feel more sluggish than usual, like there's a kind of lethargy on me.)"
    hide wllmc
    play sound gunshot_2
    show sunmok ghost veryangry at centre with dissolve
    "As soon as the ghost appears, I fire."
    hide sunmok
    show fiona cape sleep_purple at centre
    mb "Not enough! It's going to try and do what it did before. Don't let it touch you again."
    hide fiona
    show sunmok ghost veryangry at centre
    "I see the ghost begin to move, and Fiona's sight gives me a moment to react."
    hide sunmok

    $menuhideborder = True
    menu fionas1e7c1:
        "Dodge around it!":
            $menuhideborder = False
            show wllmc vest_hat angry at left4:
                pause 0.2
                easein 0.4 right4
            show sunmok ghost veryangry at right1plus:
                pause 0.1
                linear 0.6 left2
            "I let the ghost come closer, then spin on my heel and sidestep it, so I end up behind it."
            hide sunmok
            hide wllmc
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            "(It's a simple move, but if it works on thugs, it works on ghosts.)"
        "Drop to the ground.":
            $menuhideborder = False
            show wllmc vest_hat smirk at left4
            show sunmok ghost veryangry at right1plus
            "I take a look at the ghosts empty lower half, and a spark of inspiration comes to me."
            hide sunmok
            hide wllmc
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            "(I hope this looks as cool as I think it will.)"
            hide wllmc
            show sunmok ghost veryangry at right1plus:
                pause 0.1
                linear 0.4 left2
            show wllmc vest_hat angry at left4:
                pause 0.2
                easein 0.4 yoffset 500
                pause 0.4
                right4
                easein 0.4 yoffset 0
            pause 1.5
            "I let myself drop to the ground and use my momentum to slide under the ghost as it passes over me."
        "Get behind cover.":
            $menuhideborder = False
            show wllmc vest_hat surprised at left4
            show sunmok ghost veryangry at right1plus
            "I glance around and spot a porch with a solid looking pillar."
            hide sunmok
            hide wllmc
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            "(That'll do.)"
            hide wllmc
            show wllmc vest_hat angry at left1plus
            show fiona cape surprised_purple at right1plus
            "I grab Fiona's arm and pull us both up into the shelter of the building."
            hide fiona

    hide wllmc
    play sound gunshot_2
    show sunmok ghost veryangry at centre
    pause 0.5
    hide sunmok with dissolve
    "I get another shot off, and the ghost vanishes again, but I don't let my guard down."
    show wllmc vest_hat angry at left2
    show fiona cape sad_purple at right1plus
    mb "Bullets aren't enough. Not when the ghost is so... determined. If only I hadn't given back the memoria necklace."
    show wllmc vest_hat surprised
    mcfiona "Is there anything we can use?"
    mb "If we can make it as far as my shop, maybe..."
    show wllmc vest_hat angry
    mcfiona "Then let's go."
    hide wllmc
    hide fiona
    show sunmok ghost veryangry at centre with dissolve
    "But before we can really move, the ghost comes back again."
    hide sunmok
    show wllmc vest_hat angry at left2
    show fiona cape angry_purple at right1plus
    mb "On your right."
    hide fiona
    show wllmc vest_hat surprised at centre:
        pause 0.2
        easein 0.2 xoffset -30
    show sunmok ghost veryangry behind wllmc at right3:
        pause 0.1
        easein 0.4 right2

    pause 0.5
    show bg_wll_town_streets_night at ghost_touch
    show sunmok ghost veryangry at ghost_touch
    show wllmc vest_hat surprised at ghost_touch
    with dissolve
    "I turn, trying to remember how many bullets I've already used, and feel the ghosts not-flesh sink through my body again."

    scene bg_wll_town_streets_night at bg
    show fiona cape surprised_purple at centre
    mb "No."
    hide fiona
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "Dark thoughts rise through my mind like a dust storm, shrouding everything in apathetic despair."
    show wllmc vest_hat_cu sad_cu
    "(What's the point of anything?)"
    show wllmc vest_hat_cu angry_cu
    "({i}No!{/i})"
    "Somewhere deep in my soul, a spark of stubborn grit clings on."
    "(You can't control me like this!)"
    hide wllmc
    show wllmc vest_hat surprised at left2
    show sunmok ghost veryangry at centre:
        pause 0.1
        easein 0.5 right6
    show mc_instinct at full_size:
        alpha 0.0
        easein 0.3 alpha 0.7
        easein 0.3 alpha 0.0
    "I feel a surge of energy and fling out my hands. The ghost is pushed back, and between it and me a shimmering wall appears."
    hide wllmc
    hide sunmok
    show fiona cape grin_purple at centre
    mb "Oh! That's my incredible witch!"
    hide fiona
    show sunmok ghost veryangry at centre:
        pause 0.1
        easein 0.3 left2
        pause 0.2
        easein 0.3 centre
    "The ghost flings itself at the wall, but as soon as it touches the shimmering surface it screams."
    hide sunmok with dissolve
    "Its body fades away into nothingness."
    show wllmc vest_hat angry at left3
    show fiona cape angry_purple at right3
    mcfiona "Is it gone for real this time?"
    show fiona cape smirk_purple
    mb "For now. You dealt it a blow, that's for sure."
    show fiona cape angry_purple
    mb "But it's not banished, and when it returns it'll be angrier than ever."
    show wllmc vest_hat surprised:
        pause 0.2
        easein 0.4 left4
    show fiona cape sad_purple:
        easein 0.4 right1
    "Something burning hot touches me and I jerk away, then realize it was only Fiona's hand."
    mb "Let's leave the ghost alone for now. Your condition is much more urgent."
    show wllmc vest_hat sad
    mcfiona "I'm not going to die, am I? Because that would be a real pain in the ass."
    show fiona cape smile_purple
    "Fiona laughs, but the noise sounds a little forced."
    mb "Not if I have anything to do with it. Now come on, back to the shop."

    scene bg_wll_apothecary_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wllsomber1 fadein 1.0
    "The apothecary is warm and welcoming, but something about it feels distant, like I'm seeing it through leaded glass."
    show wllmc vest_hat sad at left3
    show fiona cape basic at right3
    mcfiona "What's wrong with me?"
    "I look down at my body, but I don't have a single mark on me."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(I just feel like the world is ending.)"
    hide wllmc
    show wllmc vest_hat sad at left3
    show fiona cape sad at right3
    mb "You're ghost-touched. It makes people feel all of the ghost's pain and suffering."
    show fiona cape sad behind wllmc:
        easein 0.6 centre
    "She reaches out and runs a gentle hand over my hair."
    show fiona cape smile
    mb "But don't worry, I'll have you feeling right as rain in no time."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
    "(When was the last time someone was tender with me? When was the last time anyone treated me softly?)"
    hide wllmc

    stop music fadeout 1.0
    play music wlleverydaycalm2 fadein 1.0
    show fiona cape smile at centre
    show wllmc vest_hat smirk at left3
    mcfiona "If you think being nice to me will make me drink more of your vile potions, you've got another thing coming."
    show fiona cape pout
    mb "Still distrustful. I'm wounded."
    mcfiona "I'm just waiting for the other shoe to drop."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu smallsmile_cu at wllmc_cu
    "(I'm operating more on autopilot than anything else, but talking like this does make me feel myself again.)"
    hide wllmc
    show fiona cape surprised at centre
    show wllmc vest_hat smirk at left3
    "Fiona tips her head and gives me a considering look."
    mb "Maybe this would be easier if I speak to you in a language you understand."
    show fiona cape smile at centre:
        easein 0.6 right3
    "She gets something out from under the counter, a wrapped cloth bundle."
    show wllmc vest_hat surprised
    mb "Play a game with me. If I win, you take your medicine, no complaining."
    show wllmc vest_hat smirk
    mcfiona "And if I win? What's in it for me?"
    show fiona cape basic
    "Fiona gives a deliberately exaggerated shrug and pins me with a burning look."
    hide wllmc
    hide fiona
    show fiona cape_cu smile_cu at fiona_cu
    mb "I'll do something you want me to. Anything. You just have to ask."
    hide fiona
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(Is she just playing with me? Or is this part of the treatment? A way of making me feel normal again?)"
    show wllmc vest_hat_cu smile_cu
    "(Either way, the spark of excitement in my chest is the first real feeling I've had since the ghost.)"
    hide wllmc
    show wllmc vest_hat smile at left2
    show fiona cape grin at right2
    mcfiona "So what are we playing? Poker? Dice?"
    show fiona cape smirk
    mb "Yutnori. It's one of my family's favorite games. And the only one they'll play with me since I got my powers."
    show wllmc vest_hat angry
    mcfiona "Hang on, we're playing a game that you know and I don't? Isn't that a bit unfair?"
    mb "Why? Do you think you can't keep up?"
    mcfiona "I think you're stacking the deck in your favor."
    show fiona cape smile
    mb "So unstack it, then. I have complete faith in you."
    show wllmc vest_hat smallsmile
    "She slides a hand down my arm, and I have a sudden, vivid memory of just how close we were in the alley, less than an hour ago."
    hide wllmc
    hide fiona

    $menuhideborder = True
    menu fionas1e7c2:
        "Play Fiona's game." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show wllmc vest_hat smile at left2
            show fiona cape smile at right2
            mcfiona "Right. Teach me the rules."
            hide wllmc
            hide fiona
            "The game turns out to be very simple, using sticks that act as two sided dice, and tokens that move across spaces on a cloth board."
            show wllmc vest_hat_cu smallsmile_cu at wllmc_cu
            "(I played variants on this back in my aunt's boarding house.)"
            hide wllmc
            show wllmc vest_hat smallsmile at left2
            show fiona cape smile at right2
            "The strategy is about trying to get your pieces home as fast as possible, and at the same time forcing your opponent back to the start."
            hide fiona
            hide wllmc
            show wllmc vest_hat_cu smile_cu at wllmc_cu
            "(There's too much chance involved for it to be as intense as chess, but since my brain still feels like Swiss cheese, that's a good thing.)"
            hide wllmc
            show wllmc vest_hat smallsmile at left2
            show fiona cape surprised at right2
            "The first time I send one of Fiona's tokens back to the start, she actually stares at me in shock."
            show fiona cape angry
            mb "How did you do that? You monster!"
            show wllmc vest_hat smirk
            mcfiona "Not used to playing without knowing every move in advance, I see."
            show fiona cape pout
            "She puffs her cheeks out and glares at me."
            mb "It was a fluke! Nothing more."
            hide wllmc
            hide fiona
            "Fiona wins our first game, but not by much."
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            "(Her experience with the game gives her an edge, even though her inability to predict my moves hampers her.)"
            hide wllmc
            show wllmc vest_hat smile at left2
            show fiona cape smile at right2
            mcfiona "Best of three?"
            show wllmc vest_hat surprised
            show fiona cape smirk
            mb "Definitely."
            mcfiona "But let's make it interesting. Every time a piece gets sent back to the start, you can pick truth or dare, and the other person has to do it."
            show fiona cape grin
            mb "Oh? Raising the stakes?"
            show wllmc vest_hat smirk
            mcfiona "I only play when there's something to play for."
            mb "But you're playing with me. There's {i}everything{/i} to play for."
            mcfiona "Exactly."
            show wllmc vest_hat smallsmile
            "We start our next game, and Fiona is the first to win one of our points."
            show fiona cape smile
            mb "Hmmm... Truth. What's your favorite food?"
            mcfiona "I don't know. I've had a rare old hankering for the three sisters soup they serve at the market hall in New Amster though."
            show wllmc vest_hat smile
            mcfiona "What about you?"
            show fiona cape smirk
            mb "You'll have to win a point if you want to find out."
            show wllmc vest_hat smirk
            mcfiona "If I win a point I'm going to use it on something good, not a question I could easily get for free."
            mb "I had to start slow. Didn't want to scare you off too soon?"
            show wllmc vest_hat grin
            mcfiona "You really think you could scare me off? Either you don't know me or you don't know yourself, Fiona Eichen."
            mcfiona "Because I'm the opposite of scared."
            show fiona cape grin
            mb "Well then you better roll the yut-sticks and see what you get."
            show fiona cape pout
            "It doesn't take long for me to score a point on Fiona."
            show wllmc vest_hat smirk
            mcfiona "Well well well, what should I do now?"
            show fiona cape sad
            mb "I'm at your mercy, it's true. Whatever will I do?"
            show wllmc vest_hat smile
            "She presses a hand to her forehead and tries to look sad, but can't fully mask the excitement in her eyes."
            mcfiona "Dare. Come over here, and close your eyes. Don't open them until I tell you to."
            hide wllmc
            hide fiona
            show fiona cape_cu sleep_cu at fiona_cu
            "Fiona does as I ask, coming to stand in front of me, waiting."
            hide fiona
            show wllmc vest_hat_cu smile_cu at wllmc_cu
            "(Her breathing's a little fast. She's excited.)"
            hide wllmc
            show fiona cape_cu sleep_cu at fiona_cu
            "I reach out with one hand and curve it round the slender column of her neck."
            "She shivers as I touch her, but keeps her eyes firmly closed."
            hide fiona
            show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
            "(Goddess, she's so beautiful.)"
            hide wllmc
            show fiona cape_cu sleep_cu at fiona_cu
            "I lean in until my lips are only an inch from hers."
            hide fiona
            show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
            "(I want her.)"
            hide wllmc
            "I can feel my own desire rising, and something else with it, an emotion too fleeting for me to understand."
            show fiona cape sleep at right1
            show wllmc vest_hat surprised at left1plus
            "And then, as if in revenge, I get wracked with an awful wave of the ghost-touched coldness."
            show fiona cape surprised
            mcfiona "Ah!"
            show wllmc vest_hat sad
            "I slump forward against Fiona, clutching my chest."
            show fiona cape sad
            mb "Oh no, oh my pearl, you poor thing."
            mb "I thought the game would help bring you back a little, make the medicine easier to take."
            mb "I'm sorry."
            show wllmc vest_hat basic
            mcfiona "No need to apologize. It was a good idea. And it almost worked."
            show wllmc vest_hat smile
            "I look up at her and smile."
            mcfiona "I was having a lot of fun."
        "Fold.":
            $menuhideborder = False
            "A sudden wave of bleak emotion washes over me, wiping all the fun away."
            show wllmc vest_hat smirk at left2
            show fiona cape surprised at right2
            mcfiona "No. I'm not playing a game with a cheat. Especially a cheat who can see the future."
            show fiona cape smirk
            mb "You keep forgetting I can't see your future."
            show fiona cape angry
            "But then her eyes narrow in concern as she recognizes my slump for what it really is."

    show fiona cape angry
    show wllmc vest_hat basic
    mb "Right. No more messing around. Time for you to drink this."
    "She sets a bottle in front of me and crosses her arms."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(At this point, I'd do anything to feel better.)"
    hide wllmc
    show fiona cape angry at right1
    show wllmc vest_hat sad at left1plus
    "The potion is arguably worse than the one I had yesterday, but it doesn't take long for me to feel it working."
    show wllmc vest_hat surprised
    mcfiona "The ghost touch is fading."
    show fiona cape smile
    mb "I'm glad."
    show wllmc vest_hat sad
    mcfiona "You've still got a line between your eyes, though."
    show fiona cape surprised
    "I poke at her forehead, and her scrunched eyebrows straighten out."
    show fiona cape sad
    mb "I'm just worried. I thought the locket was the key, but the ghost hasn't left. In fact, it's worse than I expected."
    show wllmc vest_hat surprised
    mcfiona "So your vision was wrong?"
    mb "Not necessarily."
    "She lifts her thumb to her mouth and gnaws at her nail absentmindedly."
    mb "There must be more, but why haven't I seen it?"
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(She feels really responsible for all of this.)"
    hide wllmc
    show fiona cape pout at right1
    show wllmc vest_hat surprised at left1plus
    mb "Maybe my patron can't see your future either? No, that's impossible..."
    show wllmc vest_hat sad
    "Guilt gnaws at me."
    mcfiona "It probably is my fault. I've always had bad luck."
    show fiona cape angry
    "Fiona stops biting her thumb and arches an eyebrow."
    mb "Is that self pity? Do you need another dose of medicine?"
    show wllmc vest_hat smile
    mcfiona "Absolutely not, you horrible goblin."
    show fiona cape smile
    "Fiona's hand cups my cheek again, the way it did earlier, but this time it doesn't burn me."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu smile_cu at wllmc_cu
    "(It feels warm. It feels good.)"
    hide wllmc
    show fiona cape_cu smile_cu at fiona_cu
    mb "Sweet complication. I've been calling you that for a reason, but this isn't your fault."
    show fiona cape_cu grin_cu
    mb "You don't have bad luck. You have an amazing power, one that you haven't been taught how to control."
    mb "Once you can, you might be just the answer we've been looking for."

    scene bg_wll_cemetery_day at bg with fade
    stop music fadeout 1.0
    play music wlleverydayupbeat3 fadein 1.0
    "And so Fiona appoints herself my magic teacher."
    show wllmc vest_hat basic at left3
    show fiona capehood smile at right3
    mb "There's a long history between witches and mystics. One of my ancestors was a witch's assistant."
    mb "We're on the same spectrum of power, just at very different points."
    hide wllmc
    hide fiona
    show sascha belt basic_hat at centre
    "We're in the graveyard with Sascha, and I'm getting a crash course on all things supernatural."
    show wllmc vest_hat surprised at left3
    show sascha belt basic_hat at right3
    mcfiona "So it isn't just ghosts you deal with?"
    show wllmc vest_hat basic
    show sascha belt angry_hat
    sasch "No, ghosts are a rarity. Now will o'wisps, those are regular pains in my ass."
    hide sascha
    hide wllmc
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(He says that like I have any idea what those are.)"
    hide wllmc
    "We talk about our ghost too, and what our plans are."
    show fiona capehood basic at left3
    show sascha belt smile_hat at right3
    sasch "The locket was purified."
    show fiona capehood smile
    mb "Yeah, I felt it too."
    hide fiona
    show wllmc vest_hat surprised at left3
    mcfiona "Is there a rule that a ghost can only have one thing tying it to the world?"
    hide wllmc
    show fiona capehood surprised at left3
    "Fiona and Sascha share a thoughtful look."
    mb "That's a good point. Maybe its initial link was the locket, but now there's something else keeping it here."
    show fiona capehood smile
    sasch "Makes sense. It would help if we knew more about the ghost, of course."
    show fiona capehood pout
    mb "It would help if I could see the damn future properly, like my powers are supposed to do."
    hide sascha
    hide fiona
    show fiona capehood angry at centre
    "She slams the book in her lap shut and picks up another one."
    show wllmc vest_hat surprised at left3
    show fiona capehood angry at right3
    mcfiona "What are you looking for?"
    mb "Anything, really? Something I haven't tried yet."
    show wllmc vest_hat smallsmile
    mcfiona "A spell to see things hidden to normal sight, a spell to make someone speak their true name..."
    show wllmc vest_hat smile
    mcfiona "We should try some of these out. Just for fun."
    show fiona capehood smirk
    "I give Fiona a sly sideways glance, and she picks up on it at once, her lips curling up."
    mb "Plus, it'll be good training for you! Let's see how you do."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    "(Oh, I'm going to do it? Well then...)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e7c3:
        "Summon a flock of bats.":
            $menuhideborder = False
            show wllmc vest_hat surprised at centre
            show bg_wll_cemetery_day as pulse_effect:
                align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.2
                linear 0.8 zoom 2.0 alpha 0.0
            "I chant the words of the spell, and with a rush of leathery wings, every bat in Wisp Willow converges on the graveyard."
            hide pulse_effect
            hide wllmc
            show sascha belt angry_hat at centre
            sasch "Away, you horrible flying rats. Away!"
            hide sascha
        "Raise a wind.":
            $menuhideborder = False
            show wllmc vest_hat angry at centre
            show bg_wll_cemetery_day as pulse_effect:
                align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.2
                linear 0.8 zoom 2.0 alpha 0.0
            "I whistle sharp and clear, and soon a wind is swirling through the graveyard..."
            hide pulse_effect
            show wllmc vest_hat smile
            "Making the trees groan and the doors of the mausoleum rattle."
            hide wllmc
            show fiona capehood smirk at centre
            mb "Oh no, the ghooooost is coming back."
            hide fiona
        "Make Sascha's shadow speak.":
            $menuhideborder = False
            show wllmc vest_hat smile at centre
            show bg_wll_cemetery_day as pulse_effect:
                align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.2
                linear 0.8 zoom 2.0 alpha 0.0
            "I say the words, and all at once Sascha's shadow begins whispering, an eerie, rasping voice."
            hide pulse_effect
            show wllmc vest_hat surprised
            $sidecharone = "Sascha's Shadow"
            sid1 "So many secrets I could tell. So many desires I have hidden."
            hide wllmc
            show sascha belt sad_hat at centre
            "Sascha's boot comes down on his shadow's head and the spell ends."
            hide sascha
    show wllmc vest_hat grin at left3:
        pause 0.1
        easein 0.4 left1
    show fiona capehood grin at right3:
        pause 0.1
        easein 0.4 right1
    "Fiona and I burst into giggles, leaning on each other as we howl with laughter."
    hide wllmc
    hide fiona
    show sascha belt angry_hat at centre
    sasch "If the two of you are done being menaces..."
    show fiona capehood smile at left3
    show sascha belt angry_hat at right3
    mb "Never."
    show sascha belt smirk_hat
    sasch "Then perhaps you'd appreciate some helpful advice?"
    show fiona capehood angry
    mb "What were you thinking?"
    hide fiona
    show wllmc vest_hat surprised at left3
    "He looks at me."
    show sascha belt smile_hat
    sasch "How about a ritual bath? Maybe the problem is that your aura is blocked up from years of denial and disbelief."
    show wllmc vest_hat smirk
    mcfiona "It's going to take more than some smelly herbs and hot water to change my mind about magic."
    hide sascha
    show fiona capehood smirk at right3
    mb "But changing your mind is my number one priority."
    show wllmc vest_hat grin
    mcfiona "Higher than getting rid of the ghost?"
    show fiona capehood grin
    mb "Even higher than that. Your magic is beautiful! I want you to love it someday, as much as I love mine."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
    "(That's... I don't know what to say.)"
    show wllmc vest_hat_cu surprised_cu
    "(Have I ever been someone's number one priority before?)"
    hide wllmc
    show wllmc vest_hat grin at left3
    show fiona capehood grin at right3
    mb "The desert hot springs have magical properties, you know. And they're very secluded. We'd have total privacy."
    hide wllmc
    hide fiona
    show fiona capehood_cu grin_cu at fiona_cu
    "Her eyes sparkle, and she leans in closer to me."
    mb "Wouldn't that be nice?"
    hide fiona
    show wllmc vest_hat grin at left3
    show sascha belt smirk_hat at right3
    sasch "It does sound nice. Want a bit of extra company?"
    hide sascha
    hide wllmc
    show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
    "(Oh... I mean, two partners at once is something I've thought about.)"
    hide wllmc
    show fiona capehood angry at left3
    show sascha belt smirk_hat at right3
    "But Fiona puts that idea right to bed."
    mb "I know this is hard to remember, Sascha, but some people have preferences that don't include you."
    show fiona capehood grin
    show sascha belt grin_hat
    "She gives Sascha a cheeky grin, and he laughs at her."
    hide sascha
    hide fiona
    show fiona capehood_cu grin_cu at fiona_cu
    mb "What do you think, [genericfn]?"
    hide fiona
    show wllmc vest_hat smirk at left3
    show fiona capehood smile at right3
    mcfiona "I think it sounds like an excuse to see me naked. Not that I blame you for wanting one."
    hide wllmc
    hide fiona
    show fiona capehood_cu grin_cu at fiona_cu
    "We stare at each other like there's no one and nothing else in the world."
    mb "Are you saying no? Or yes?"
    hide fiona

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
