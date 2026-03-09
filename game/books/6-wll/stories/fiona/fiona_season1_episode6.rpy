label fiona_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_town_streets_sunset at bg
    play music wllspookymysterious1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show wllmc coat_hat surprised at left3
    show fiona cloak angry_purple at right3
    mcfiona "Fiona? Fiona? Come on, come back to me."
    hide wllmc
    hide fiona
    show fiona cloak_cu angry_purple_cu at fiona_cu
    "Fiona's eyes are still glowing. I pull my hand out of hers, and set it on her shoulder."
    hide fiona
    show wllmc coat_hat sad at left3
    show fiona cloak angry_purple at right3
    mcfiona "Fiona, please."
    mb "A stone sits in the same place for five hundred years, and then a farmer's foot pushes it and starts an avalanche."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(How do I snap her out of this?)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e6c1:
        "Shake her shoulders.":
            $menuhideborder = False
            show wllmc coat_hat sad at left3 behind fiona:
                pause 0.1
                easeout 0.6 left1
            show fiona cloak angry_purple at right3
            "I give Fiona a gentle shake, but the way her body jerks back and forth limply only makes me feel worse."
            hide fiona
            hide willmc
            show wllmc coat_hat_cu sad_cu at wllmc_cu
            "(If I try any harder I might hurt her.)"
        "Cup her cheek.":
            $menuhideborder = False
            show wllmc coat_hat sad at left3 behind fiona:
                pause 0.1
                easeout 0.6 left1
            show fiona cloak angry_purple at right3
            "I reach out and press my hand to Fiona's cheek, rubbing my thumb over her cheekbone."
            hide fiona
            hide wllmc
            show wllmc coat_hat_cu sad_cu at wllmc_cu
            "(She didn't even register the touch.)"
        "Stroke her hair.":
            $menuhideborder = False
            show wllmc coat_hat sad at left3 behind fiona:
                pause 0.1
                easeout 0.6 left1
            show fiona cloak angry_purple at right3
            "I stroke the top of Fiona's head, hoping the repetitive, soothing motion will help."
            hide fiona
            hide wllmc
            show wllmc coat_hat_cu sad_cu at wllmc_cu
            "(I might as well not have done anything, for all the reaction I get.)"
    hide wllmc
    show wllmc coat_hat sad at left1
    show fiona cloak angry_purple at right3
    mb "The squirrel hunting nuts for winter doesn't see the claws of the owl at sunset."
    show wllmc coat_hat surprised
    "Now I'm getting really nervous."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(Maybe... It's stupid fairytale bullshit, but apparently I live in a nonsense magical world.)"
    "(It's worth a try.)"
    hide wllmc
    show fiona cloak angry_purple at right3
    show wllmc coat_hat sleep at left1 behind fiona:
        pause 0.1
        easein 0.6 centre
    "I lick my lips and lean in."
    hide wllmc
    hide fiona
    show fiona cloak_cu angry_purple_cu at fiona_cu
    "Just as my mouth is about to connect with hers..."
    show fiona cloak_cu surprised_cu with dissolve
    "The light fades from Fiona's eyes, restoring their soft gold."
    hide fiona
    show wllmc coat_hat surprised at centre:
        pause 0.1
        easein 0.4 left1
    show fiona cloak surprised at right3
    "I feel the air from her gasp across my lips and I jerk back instantly."
    mcfiona "You're back."
    show fiona cloak sad:
        pause 0.1
        easein 0.6 right1plus
    "Fiona presses a hand to her head and leans into me a little."
    show wllmc coat_hat sad
    mb "Oof. That was a rough one."
    "More than anything else I've seen, even the ghost, the way Fiona reacts to what just happened is what changes my mind."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(The macabre and theatrical makes me suspicious, but she's so natural, so normal.)"
    "(Maybe this is all real.)"
    hide wllmc
    show wllmc coat_hat sad at left1
    show fiona cloak sad at right1plus
    mcfiona "What just happened?"
    mb "It was... We established that you're a witch."
    show wllmc coat_hat angry
    mcfiona "I don't remember establishing any such thing."
    "I slide an arm around Fiona's waist so she can lean on me as we walk."
    show fiona cloak pout
    mb "We can fight about it later, my pearl. Just go with me for now."
    show wllmc coat_hat smirk
    mcfiona "My pearl? I thought that was a bit for Diana."
    show fiona cloak embarrassed
    mb "It was, but I kinda like it. It suits you."
    "She reaches a hand up and twists it through a lock of my hair."
    show wllmc coat_hat grin
    mcfiona "I need a pet name for you too. My horrible goblin, maybe."
    show fiona cloak grin
    "Fiona laughs."
    mb "Perfect. So, your horrible goblin is a Mystic."
    show fiona cloak basic
    mb "Mystics are people given gifts by...patrons."
    show wllmc coat_hat surprised
    mcfiona "What does that mean?"
    mb "Some people call them spirits, or eudaemons, or little gods.."
    mcfiona "Yours gave you the power to see the future? Why?"
    show fiona cloak sad
    mb "Good question. I wish I knew. Mostly, it just gives me passive skills. Palmistry, tarot readings, all that."
    show fiona cloak basic
    mb "But sometimes, when it's important, it speaks to me directly."
    show fiona cloak sad
    mb "It's always an... intense experience."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(Doesn't sound like a good deal to me.)"
    hide wllmc
    show wllmc coat_hat sad at left1
    show fiona cloak sad at right1plus
    mcfiona "So what did this vision say?"
    mb "It was in the nature of a warning, and an instruction. That locket is really, really important."
    mb "A lot of the images were about something small affecting everything around it in a very big way."
    show fiona cloak sleep
    "She closes her eyes for a moment, looking genuinely exhausted."
    show fiona cloak sad
    mb "I don't want to think about what my patron considers 'big consequences' to be."
    show wllmc coat_hat surprised
    mcfiona "So what do we have to do?"
    show fiona cloak angry
    mb "We're going to have to steal it."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu sad_cu at wllmc_cu
    "(I was afraid of that.)"
    hide wllmc
    show wllmc coat_hat angry at left1
    show fiona cloak angry at right1plus
    mcfiona "You know that's a really shitty thing to do, right? Diana said herself it was a memento from her wife."
    mcfiona "And as sure as I am that she's up to something, she ain't lying about how important that is to her."
    show fiona cloak sad
    mb "I know. I think I'll be able to return it afterwards, though I can't promise it won't be damaged."
    show fiona cloak angry
    mb "If you can't do it, it's fine. I won't ask you to cross your lines for me."
    hide wllmc
    hide fiona
    show fiona cloak_cu angry_cu at fiona_cu
    mb "But if my patron calls me to action. I must answer."
    hide fiona
    show wllmc coat_hat surprised at left1
    show fiona cloak angry at right1plus
    mb "There are always things bigger than ourselves at play."
    show wllmc coat_hat sleep
    "I take a breath and then let it out slowly."
    show wllmc coat_hat sad
    mcfiona "No. If... If this is really necessary, then I'll see it through."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(I can't let Fiona go it alone after seeing how vulnerable she becomes while her...{i}patron{/i} is speaking with her.)"
    hide wllmc
    show wllmc coat_hat smirk at left1
    show fiona cloak angry at right1plus
    mcfiona "Besides, it'll go a lot smoother if you have me alongside."
    hide wllmc
    hide fiona
    show fiona cloak_cu smile_cu at fiona_cu
    mb "Oh? Well, I can't argue with that."

    scene bg_wll_town_hall_lights_off at bg with fade
    stop music fadeout 1.0
    play music wllmctheme1 fadein 1.0
    "In the end, stealing the locket is probably the easiest heist I've ever done in my life."
    show wllmc vest_hat smirk at left3
    show fiona capehood basic at right3
    mcfiona "I noticed this window had a broken sash when we met Diana earlier."
    hide wllmc
    hide fiona
    "I boost Fiona up to climb through, and if I enjoy the moment when she's sitting on my shoulders a little too much, no one has to know."
    show fiona capehood smile at centre
    mb "Alright, I'm throwing the rope out."
    hide fiona
    "The rope comes slithering down to me, and I'm in too."
    show wllmc vest_hat basic at left3
    show fiona capehood smile at right3
    "From there, it's only a matter of picking the pathetically cheap lock on the display case."
    show wllmc vest_hat smirk
    mcfiona "Once we're done with this, we should persuade Diana to invest in some better protections."
    hide wllmc
    hide fiona
    show fiona capehood_cu smirk_cu at fiona_cu
    mb "Are you thinking of starting a new life as a security expert, my peerless treasure?"
    hide fiona
    show wllmc vest_hat smirk at left3
    show fiona capehood smirk at right3
    mcfiona "Maybe. Are you doubting my ability, villainous imp?"
    show fiona capehood grin
    mb "Not at all, oh queen of grace and beauty."

    scene bg_wll_cemetery_night_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    "The two of us have to muffle our giggles as we sneak down the road to the cemetery, where Sascha stands waiting for us."
    show sascha belt smirk_hat at centre
    sasch "Well, I'm glad you ladies are having fun."
    hide sascha
    "He takes us back through the graveyard to where a neat circle has been cut into a clear patch of grass."
    show fiona capehood basic at left3
    show sascha belt basic_hat at right3
    sasch "I got everything you asked for, Fiona."
    show fiona capehood smile
    mb "And I have the rest."
    hide fiona
    hide sascha
    "She pulls a few different bottles from various pockets and sets to work building a fire."
    show wllmc vest_hat basic at left3
    show fiona capehood angry at right3
    mb "I know the ghost is coming. Can see that clear as day. But the rest is muddied."
    show fiona capehood sad
    "She gives me a look."
    mb "So all I can say is be careful."
    hide wllmc
    hide fiona
    "Sascha gestures for me to take my place on one side of the circle, and positions himself on the other."
    show wllmc vest_hat basic at left3
    show sascha belt basic_hat at right3
    sasch "We can all fight, but only Fiona can do what she does, so it's up to the rest of us to keep her safe."
    show wllmc vest_hat angry
    "I nod, and check to make sure my revolver is in working order."
    sasch "Here, take these."
    hide wllmc
    hide sascha
    show sascha belt_cu basic_hat_cu at sascha_cu
    "He tosses me a bag of silver bullets, and I slot them into my gun skeptically."
    hide sascha
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(I really don't see how this will help.)"
    hide wllmc
    show fiona capehood angry at centre
    "Fiona begins the ritual, which seems to consist of boiling the locket in a brew over a fire. I can hear her chanting under her breath."
    hide fiona
    show wllmc vest_hat_cu basic_cu at wllmc_cu
    "(Doing mystical rituals in a graveyard at midnight. This is what my life is now, huh?)"
    hide wllmc
    show fog_effect:
        alpha 0.5
    "A low moan sounds, and the graveyard starts to fill with mist."
    show sascha belt angry_hat at centre
    sasch "Here it comes."
    hide sascha
    show sunmok ghost basic at centre with dissolve
    "Sure enough, the ghost emerges from nothingness, a strange echo of a person."
    hide sunmok
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(It's scary for sure, but it's also so damn sad.)"
    hide wllmc
    show sunmok ghost sad at centre
    $sidecharone = "Ghost"
    sid1 "Give me... help... need..."
    hide sunmok
    show sascha_demon_effect
    show sascha belt_demon angry_demon at centre
    "It moves single mindedly towards Fiona, arms reaching, and then Sascha steps between them, his hand suddenly burning hot."
    hide sascha_demon_effect
    hide sascha
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(Sascha?! Are those horns?)"
    hide wllmc
    show sunmok ghost sad at centre:
        pause 0.1
        easein 0.4 right1
    "The ghost recoils."
    hide sunmok
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(That's not going to be enough to stop it, though.)"
    hide wllmc
    show fiona capehood angry at centre
    mb "Almost there. Just a little longer."
    hide fiona
    show sascha_demon_effect
    show sascha belt_demon angry_demon at centre
    "I can see the strain it's putting on Sascha, the ghost's ferocious cold fighting against his heat."
    hide sascha_demon_effect
    hide sascha
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(What can I do? How can I help?)"
    hide wllmc
    show wllmc vest_hat angry at centre
    "Just like last night, when push comes to shove, I don't hesitate."
    "My powers, whatever they are, are untested, but that doesn't mean I won't use them."
    hide wllmc

    $menuhideborder = True
    menu fionas1e6c2:
        "Distract the ghost.":
            $menuhideborder = False
            show wllmc vest_hat_cu surprised_cu at wllmc_cu
            "(Maybe I can lift some small stones?)"
            hide wllmc
            show wllmc vest_hat surprised at centre
            "I try and do it, but all that happens is that they rattle on the ground."
        "Try to beef up Sascha.":
            $menuhideborder = False
            show wllmc vest_hat_cu surprised_cu at wllmc_cu
            "(I wonder if I can help Sascha?)"
            hide wllmc
            show wllmc vest_hat smirk at left1plus
            show sascha belt_demon angry_demon at right3
            "I reach out and slap a hand on his back, but all it does is make him yelp and glare at me."
        "Shield everyone from the cold.":
            $menuhideborder = False
            show wllmc vest_hat_cu surprised_cu at wllmc_cu
            "(Can I make some kind of shield?)"
            hide wllmc
            show wllmc vest_hat surprised at centre
            "I imagine warm winter coats wrapped around me, Sascha and Fiona. Nothing happens."
            hide wllmc
            show wllmc vest_hat_cu sad_cu at wllmc_cu
            "(If anything, it just got colder.)"

    scene white at bg with dissolve
    scene bg_wll_cemetery_night_lights at bg, ghost_touch
    show fog_effect at ghost_touch
    show sunmok ghost angry at centre, ghost_touch:
        anchor(0.5, 0.5)
        linear 0.8 zoom 1.3 yoffset 80
    with dissolve
    "I don't have any real effect, but I do get the ghost's full attention, and it reaches out for me."
    hide sunmok
    show wllmc coat_hat_cu sad_cu at wllmc_cu, ghost_touch
    "(If only that didn't hurt so much.)"
    hide wllmc
    show wllmc vest_hat sad at centre, ghost_touch
    "I feel like I just stepped into a midwinter blizzard in my underthings. It takes every ounce of strength I have to keep standing."
    scene white with dissolve
    scene bg_wll_cemetery_night_lights at bg
    show fog_effect:
        alpha 0.5
    show fiona capehood angry at centre
    with dissolve
    mb "In the name of the dead who rest here peacefully, and the spirits who hold this place dear, relinquish your hold."
    "She lifts the locket out of the boiling liquid, drops it into a vat of salt, and rings a bell."
    hide fiona
    show sunmok ghost sad at centre:
        pause 0.1
        linear 0.6 alpha 0
    show fog_effect:
        linear 0.6 alpha 0
    "A strange, sucking silence ripples out in the wake of the bell, and the ghost vanishes."
    hide sunmok
    hide fog_effect
    stop music fadeout 1.0
    play music wlleverydayupbeat3 fadein 1.0
    show wllmc vest_hat surprised at left3
    show fiona capehood surprised at right3
    mcfiona "It worked?"
    show fiona capehood grin
    mb "It worked!"
    show wllmc vest_hat sad
    show fiona capehood sad
    "She pulls the locket out of the salt and looks at its tarnished surface regretfully."
    mb "I'll give it back to Diana in the morning. With my apologies."
    show wllmc vest_hat smirk
    mcfiona "It's a shame she didn't get to see this. It would have wowed her. She loves all this weird stuff."
    hide wllmc
    hide fiona
    show fiona capehood_cu smile_cu at fiona_cu
    mb "How are you feeling about the weird stuff?"
    hide fiona
    show wllmc vest_hat smile at left3
    show fiona capehood smile at right3
    mcfiona "I might be reconsidering a few of my preconceptions."
    show fiona capehood grin
    mb "That's good enough for me. Let's go celebrate!"
    show wllmc vest_hat smallsmile
    mcfiona "Right, but first..."
    hide wllmc
    hide fiona
    show sascha_demon_effect
    show sascha belt_demon surprised_demon at centre
    "I turn to Sascha and point a finger at him."
    show wllmc vest_hat angry at left3
    hide sascha_demon_effect
    show sascha belt_demon surprised_demon at right3
    mcfiona "What the hells?!"

    scene bg_wll_saloon_night_lights_people at bg with fade
    stop music fadeout 1.0
    play music wlleverydayupbeat1 fadein 1.0
    "After the dark and eerie graveyard, Ada's bar feels like the most homely and comforting place imaginable."
    show wllmc vest smallsmile at left3
    show fiona cape grin at right3
    mb "First round's on me. No need to give orders."
    show wllmc vest surprised
    mcfiona "What about me?"
    hide wllmc
    hide fiona
    show fiona cape_cu smirk_cu at fiona_cu
    mb "I predict you're going to enjoy a glass of Ada's top shelf brandy."
    hide fiona
    show wllmc vest smirk at left3
    show fiona cape smirk at right3
    mcfiona "I want to argue, but that sounds like heaven right now."
    show fiona cape grin
    mb "I told you before I'm always right, my pearl."
    show wllmc vest grin
    mcfiona "Meddlesome sprite."
    hide wllmc
    hide fiona
    show nathan redcasual_bandana smile at left3
    show cecelia bluevest smirk at right3
    "I wander over to where Cecelia and Nathan are in the middle of a friendly arm wrestling match."
    show nathan redcasual_bandana smirk
    show cecelia bluevest surprised
    wc "Looks like I've got you beat, Cecelia."
    show cecelia bluevest smirk
    vr "We'll see about that."
    show cecelia bluevest angry
    "She narrows her eyes, which darken to a pitch black, and her nails lengthen into predatory claws."
    hide nathan
    hide cecelia
    show wllmc vest_cu surprised_cu at wllmc_cu
    "(Looks like her teeth got longer too.)"
    hide wllmc
    show nathan redcasual_bandana surprised at left3
    show cecelia bluevest angry at right3
    "With newfound strength she pushes Nathan's hand back and back, but just before it hits the table he seems to become transparent."
    show nathan redcasual_bandana smirk
    show cecelia bluevest surprised
    "Cecelia's hand slides through his to thump against the wood."
    wc "If you're cheating, I will too."
    hide nathan
    hide cecelia
    show wllmc vest surprised at left3
    show fiona cape smirk at right3
    mb "Didn't take predictive powers to see how that one would end."
    show wllmc vest smallsmile:
        pause 0.1
        easein 0.4 left1plus
        easein 0.4 left3
    show fiona cape smile:
        pause 0.1
        easein 0.4 right1plus
        easein 0.4 right3
    pause 1
    "She passes me my brandy and we clink glasses."
    mcfiona "I think it's time I had a proper explanation of what exactly this cabal's deal is."
    hide wllmc
    show cecelia bluevest smile at left3
    show fiona cape grin at right3
    "Fiona laughs, and to my surprise, Cecelia does too."
    hide cecelia
    show wllmc vest smallsmile at left3
    mb "We're part of a larger organization called the Ward."
    hide fiona
    show cecelia bluevest smile at right3
    vr "Wardens exist to keep the supernatural world separate from everyday life, and to punish those who hurt the innocent."
    show wllmc vest surprised
    mcfiona "Oh, so you are Pinkertons. Supernatural Pinkertons."
    hide cecelia
    show fiona cape pout at right3
    mb "I've never been so insulted in my life."
    show wllmc vest smirk
    mcfiona "But if you only have jurisdiction over the supernatural, you can't actually give me a pardon, can you?"
    hide wllmc
    hide fiona
    show fiona cape_cu sad_cu at fiona_cu
    "Fiona looks momentarily downcast."
    hide fiona
    show wllmc vest smirk at left3
    show fiona cape sad at right3
    mb "No. I'm sorry. I didn't mean to lead you astray. At that point, I still thought you were hiding actual knowledge of the supernatural."
    hide fiona
    hide wllmc
    show wllmc vest_cu sad_cu at wllmc_cu
    "(I can't blame her for being fooled, not when I was so cagey.)"
    hide wllmc
    show wllmc vest basic at left3
    show cecelia bluevest smirk at right3
    vr "If you ever run into future problems, though, you can call on us. We can't forgive everything, but we help our friends."
    hide cecelia
    show wllmc vest smallsmile
    show fiona cape angry at right3
    "She casts an eye toward Fiona who is intensely focused on her drink and hums suspiciously."
    hide fiona
    hide wllmc
    show wllmc vest_cu sad_cu at wllmc_cu
    "(That's not a bad offer. Now I know this world exists, chances are I'll end up causing trouble in it.)"
    hide wllmc
    show wllmc vest sad at left3
    show fiona cape sad at right3
    mcfiona "Well, that's one half of my bargain off the table."
    show fiona cape smile
    "I give Fiona a speculative look."
    show wllmc vest smirk
    mcfiona "How close are you to being finished with that drink of yours?"
    show wllmc vest surprised
    "Fiona thinks about that for a second, then pours what's left of her drink into Sascha's cup."
    show fiona cape smirk
    mb "Oh look at that, it's all gone."
    hide fiona
    hide wllmc
    show wllmc vest_cu surprised_cu at wllmc_cu
    "(The way she did that was... hmmm... wow.)"

    scene bg_wll_town_streets_night_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wlleverydaycalm1 fadein 1.0
    "We stand up and wave a brief goodbye to the others, then amble out into the street."
    show wllmc vest_hat smallsmile at left3
    show fiona cape smile at right3
    mb "It's terrible to admit, but I've been thinking about this so much it almost feels like I have seen the future."
    show wllmc vest_hat smirk
    mcfiona "Oh yeah? Want to tell me about those visions of yours?"
    hide wllmc
    hide fiona
    show fiona cape_cu pout_cu at fiona_cu
    mb "They aren't the kind of things you say in a street, sweet complication. They're best saved for private rooms and drawn curtains."
    hide fiona
    show wllmc vest_hat grin at left3
    show fiona cape pout at right3
    mcfiona "Oh really? Because some of mine are just a dark alley away."

    stop music fadeout 1.0
    play music wllromanceheavy2 fadein 1.0
    scene fiona_s1_ei2 at bg with fade:
        align(0.5, 1.0)
        linear 5.0 yoffset 1350 xoffset 30
    pause
    "Fiona's eyes smoulder, and before I know it I'm standing in one of those dark alleys, Fiona's arm pinning me against a wall."
    mb "Tell me more."
    "I reach out and pull one of her long braids over her shoulder, letting the smooth silk of it slither through my fingers."
    mcfiona "Are you sure this is what you want? Not a soft bed and candlelight, but a tuppenny upright behind the saloon?"
    "Fiona licks her lips."
    scene bg_wll_town_streets_night_lights at bg
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    with fade
    mb "I want you. What are you stalling for? What do you want?"
    "My whole body is on fire. Every inch of air between us is electric."
    show wllmc vest_hat_cu embarrassed_cu
    "(If this energy doesn't go somewhere I'm going to burn from the inside out.)"
    mcfiona "I want... I want you to..."
    hide wllmc

    $menuhideborder = True
    menu fionas1e6c3:
        "Kiss me, Fiona." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            mcfiona "Kiss me."
            hide wllmc
            "Fiona doesn't need me to ask twice. Her lips are on mine in an instant, ravenous and insistent."
            show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
            "(Just like the first time, our kiss seems to shift the whole world.)"
            hide wllmc
            "I slide my arms around her waist and pull her flush against me, groaning at the feel of her soft and pliant curves."
            show fiona cape_cu smirk_cu at fiona_cu
            mb "You're wound as tight as a spring, aren't you? Just ready to come apart at the seams for me."
            hide fiona
            "Her thumb traces across my jaw, down the column of my neck, and into the hollow between my collarbones."
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            mcfiona "Doesn't seem to me that you've got any high ground to be talking from. You're the one who dragged me into this alley, after all."
            mcfiona "You just couldn't keep your hands off me for another second."
            hide wllmc
            "I slide a hand down her back, over her curves, and push her upwards so her mouth is closer to mine."
            show wllmc vest_hat_cu grin_cu at wllmc_cu
            mcfiona "Don't worry, I'll take real good care of you."
            hide wllmc
            "I kiss her again, slow and teasing, taking my time as I notice every little thing that makes her gasp and wriggle."
            show fiona cape_cu embarrassed_cu at fiona_cu
            mb "Mmm, just like that, yes, keep going."
            hide fiona
            "She reaches for my free hand and interlaces our fingers..."
            "And then in one swift movement lifts it up and over my head, pinning it against the wall."
            show fiona cape_cu smirk_cu at fiona_cu
            mb "Did you think I was going to let you lead for the whole dance?"
            mb "I'm much too greedy for that, I'm afraid."
            hide fiona
            "I make a half-hearted attempt to get out of the pin, but it's only for show and both of us know it."
            show fiona cape_cu smirk_cu at fiona_cu
            mb "I want to know what your face looks like when you're so wracked with pleasure you can't even remember your own name."
            hide fiona
            "Her legs snake around my thighs and lock together, giving her the support she needs to drop her lips to mine."
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            mcfiona "Well aren't you a bad girl, Fiona Eichen?"
            mcfiona "Impatient, bossy, overly confident... Seems to me you need someone who doesn't give in to you too easily."
            hide wllmc
            "I take one of her braids and do what I've been wanting to do for two days, wrapping it around my hand like a rope."
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            mcfiona "This is what you really want, isn't it? For someone to lead you. Show you exactly where they want you?"
            hide wllmc
            show fiona cape_cu grin_cu at fiona_cu
            "Fiona laughs, and the way the vibrations ripple through our joined bodies is so good I nearly lose my mind."
            show fiona cape_cu smirk_cu
            mb "Do you think you've caught me? Oh sweet thing, you're the fish hooked on my line."
            hide fiona
            "She moves her body against me, a careful push and pull that amps up the desire building in my stomach."
            show fiona cape_cu smirk_cu at fiona_cu
            mb "Every move reels you in a little more."
            hide fiona
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            mcfiona "Are you sure you know what you're pulling in? Because you might think I'm a minnow, but I warn you, I'm a shark."
            hide wllmc
            "I let her braid go, shimmy my hand out of her grip, and start unhooking the buttons of her dress."
            show wllmc vest_hat_cu embarrassed_cu at wllmc_cu
            "(Goddess, her skin is soft as velvet.)"
            hide wllmc
            "My fingers brush a ticklish spot, and Fiona wriggles against me."
            show wllmc vest_hat_cu smirk_cu at wllmc_cu
            mcfiona "I'm going to find every vulnerable spot on your body and sink my teeth into them, until you're so ravished you won't be able to walk."
            hide wllmc
            show fiona cape_cu smirk_cu at fiona_cu
            mb "And you call me overconfident. Be careful you're not leaving yourself open."
            hide fiona
            "Her lithe fingers run up and down my sides, and the feathery touches leave me quaking and trembling with laughter."
            show wllmc vest_hat_cu grin_cu at wllmc_cu
            mcfiona "Oh mercy, mercy, you little demon."
            hide wllmc
            show fiona cape_cu grin_cu at fiona_cu
            mb "Do you yield to me, my treasure?"
            hide fiona
            show wllmc vest_hat_cu smallsmile_cu at wllmc_cu
            "She stops tickling and waits for my answer."
            show wllmc vest_hat_cu smirk_cu
            mcfiona "Hmm, actually... No."
            hide wllmc
            show fiona cape_cu surprised_cu at fiona_cu
            "I spring a counter-attack on her, and make her shriek."
            show fiona cape_cu smile_cu
            mb "How evil you are, sweet complication. Will you accept a temporary truce?"
            hide fiona
            show wllmc vest_hat_cu smile_cu at wllmc_cu
            mcfiona "A temporary truce is acceptable. Until we get to a room with a door that locks."
            hide wllmc
            "Fiona laughs, and unhooks her legs from my hips, dropping back down to the ground."
            show fiona cape_cu smirk_cu at fiona_cu
            mb "I like the sound of that. I want to be absolutely filthy with you, and I don't mean dirt."
            hide fiona
            show wllmc vest_hat_cu smile_cu at wllmc_cu
            mcfiona "Well then, for once we're on the same page."
            hide wllmc
            "I lean and give her one last kiss, sweet and gentle, a promise of more to come."
        "Give me some space.":
            $menuhideborder = False
            show wllmc vest_hat_cu sad_cu at wllmc_cu
            mcfiona "Give me some space."
            hide wllmc
            show wllmc vest_hat sad at left3
            show fiona cape surprised at centre:
                pause 0.1
                easein 0.4 right3
            "Fiona steps away at once."
            mb "That's really not what I thought you were going to say."
            show wllmc vest_hat smirk
            mcfiona "Well I don't want you getting dirt on your nice clothes."
            show fiona cape grin
            "That gets a laugh from her, and a teasing curl of her lips that makes me regret my choice."
            hide wllmc
            hide fiona

    scene bg_wll_town_streets_night at bg with dissolve
    stop music fadeout 1.0
    play music wllsuspense1 fadein 1.0
    "As we step out of the alleyway, every light on the street goes out, leaving us fumbling in darkness."
    show wllmc vest_hat surprised at left3
    show fiona cape surprised at right3
    mcfiona "Fiona, what's happening?"
    show fiona cape angry
    mb "Stay close to me! This is bad."
    hide wllmc
    hide fiona
    show sunmok ghost angry at centre
    "From out of the darkness, the ghost appears again, and this time I can see palpable fury on her face."
    show sunmok ghost veryangry
    sid1 "You... tried to send me... Suffer! You will... scream..."
    hide sunmok
    show wllmc vest_hat surprised at left3
    show fiona cape angry at right3:
        pause 0.1
        easein 0.4 centre
    "Fiona leaps between me and the ghost as the dreadful cold comes back."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(I thought the cleansing worked!)"
    "(What do we do now?)"
    hide wllmc

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
