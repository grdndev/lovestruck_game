label fiona_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_train_station_sunset at bg
    play music wlleverydaycalm3 fadein 1.0
    # TODO : music

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "As the train slows to enter the station, I take Fiona's hand in mine and the two of us throw ourselves off the train."
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    "(It's been years since I last did this with someone else.)"
    hide wllmc
    show fiona hood_cu grin_hood_cu at fiona_cu
    "We roll down the tracks together in a tangle of limbs, and land with Fiona lying on my chest, grinning cheerily at me."
    hide fiona
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    mcfiona "Better than a fairground ride, wouldn't you say?"
    hide wllmc


    stop music fadeout 1.0
    play music wllaction1 fadein 1.0
    show fiona hood_cu smirk_cu at fiona_cu
    mb "Absolutely. But we're not out of the woods yet."
    hide fiona
    show wllmc coat_hat basic at left2
    show fiona hood smirk_hood at right1plus
    "She jumps up and holds out a hand, pulling me to my feet."
    show fiona hood surprised_hood
    mb "Quick, over here."
    show wllmc coat_hat surprised at left2:
        pause 0.2
        easein 0.5 xoffset 130
    show fiona hood angry_hood at right1plus:
        easein 0.5 xoffset 80
    "She drags me behind a stack of crates, and a few seconds later, a couple of guards run by."
    show wllmc coat_hat smirk
    mcfiona "You've got skills."
    mcfiona "What name do you operate under? Maybe I've heard of you before."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "I have many names. Names are flexible, you know? Pick the right one for the right circumstances."

    scene bg_wll_town_streets_sunset at bg with wiperightdissolve

    stop music fadeout 1.0
    play music wlleverydaycalm3 fadein 1.0
    "We duck out of the train station and begin walking through the town."
    show wllmc coat_hat basic at left2
    show fiona hood basic_hood at right1plus
    mb "But while we're asking questions, I have a few."
    show wllmc coat_hat smile
    mcfiona "Oh yeah? What do you want to know?"
    show fiona hood smile_hood
    mb "How do you feel about silver?"
    show wllmc coat_hat smirk
    mcfiona "Not quite what I was expecting."
    hide wllmc
    hide fiona
    show fiona hood_cu smile_hood_cu at fiona_cu
    mb "Humor me."
    hide fiona
    show wllmc coat_hat smallsmile at left2
    show fiona hood smile_hood at right1plus
    mcfiona "It's alright. I think gold suits my complexion better, but silver's more useful currency. Hard to fence gold."
    show fiona hood grin_hood
    mb "Hmmm... How about full moons? Do they send a shiver through your blood?"
    show wllmc coat_hat smirk
    mcfiona "I've been known to dilly-dally under a full moon. But it's risky."
    mcfiona "Easier to see what you're doing, but easier for others to see you too."
    show fiona hood smirk_hood
    mb "You do play your cards close to your chest, don't you?"
    show wllmc coat_hat grin
    mcfiona "Only way to play, you should know that."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "I know many ways to play."
    "She gives me a look, up through her lashes, and the smolder in her eyes makes me shiver."
    hide fiona
    show wllmc coat_hat smallsmile at left2
    show fiona hood smirk_hood at right1plus
    mcfiona "I can't tell if you're real good at flirting, or really, really bad."
    show wllmc coat_hat grin
    mcfiona "That last line worked, but the weird questions before were more funny than swoon-worthy."
    show fiona hood grin_hood
    mb "Maybe I need a demonstration."
    hide wllmc
    hide fiona
    show fiona hood_cu grin_hood_cu at fiona_cu
    mb "Why don't you use those slick New Amster skills and sweep me off my feet?"
    hide fiona
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(I never told her I was from New Amster! Does she have that good an ear for accents, or do I have some other tell?)"
    hide wllmc
    show wllmc coat_hat surprised at left2
    show fiona hood smile_hood at right1plus
    "Either way, Fiona's boundless confidence is wearing a little thin. Time I put her on the back foot for a change."
    mcfiona "Are you sure you know what you're asking for?"
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "I'm sure I can handle whatever you dish out."
    hide fiona
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    "(Well then, the game is afoot.)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e2c1:
        "Show Fiona what real flirting looks like!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show wllmc coat_hat smirk at left2
            show fiona hood smirk_hood at right1plus
            mcfiona "See, if I wanted to flirt with you, I'd ask something like 'do you always kiss girls you just met?'"
            show wllmc coat_hat surprised
            show fiona hood surprised_hood
            mb "If you wanted to flirt with me? Are you saying you don't?"
            hide wllmc
            hide fiona
            show fiona hood_cu sad_hood_cu at fiona_cu
            "Her sudden look of sadness is as convincing as it is fake."
            hide fiona
            show wllmc coat_hat smirk at left2
            show fiona hood sad_hood at right1plus
            mcfiona "If I have to tell you, is it really flirting?"
            show fiona hood smirk_hood
            mb "What was it you said to me? 'Have a little subtlety.' You have to reel a girl in slowly."
            show wllmc coat_hat angry
            "I point an accusing finger at her."
            mcfiona "Hang on, that's my point."
            mcfiona "There's no approach less subtle than locking lips. Especially when we hadn't said five words to each other."
            show fiona hood surprised_hood
            mb "That's not true! We said a lot more than five words."
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            mb "And you know, sometimes bodies speak louder than tongues in any case."
            hide fiona
            show wllmc coat_hat surprised at left2
            show fiona hood smirk_hood at right1plus
            "She runs a finger down my arm and I shiver, which makes her look very smug."
            show wllmc coat_hat smile
            mcfiona "I think it depends on what those tongues are doing."
            show fiona hood smile_hood
            mb "Usually they're running away with themselves."
            mcfiona "Maybe yours was. I'm always in command of my tongue."
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            "I give her a look, hoping to see her flush a little, but her sly smile doesn't waver."
            hide fiona
            show wllmc coat_hat_cu smile_cu at wllmc_cu
            "(She likes to play the game, that's clear, but it's hard to know exactly how much of an effect I'm having.)"
            hide wllmc
            show wllmc coat_hat smile at left2
            show fiona hood grin_hood at right1plus
            mcfiona "But you never answered the question. Do you always kiss girls you just met?"
            show fiona hood smirk_hood
            mb "Certainly not always. I mean, how could I ever buy groceries if I tried to dizzy every counter girl I came across?"
            hide fiona
            hide wllmc
            show wllmc coat_hat_cu angry_cu at wllmc_cu
            "(Has this woman ever given a straight answer to a question in her life?)"
            show wllmc coat_hat_cu surprised_cu
            "(Though come to think of it, she might have cause to ask the same question of me.)"
            hide wllmc
            show wllmc coat_hat smirk at left2
            show fiona hood smirk_hood at right1plus
            mcfiona "So you have criteria then?"
            show fiona hood grin_hood
            mb "Naturally. Credit me with the most basic of human graces."
            mcfiona "No one working a job, no one obviously taken?"
            show fiona hood smile_hood
            mb "Exactly. No one too deep under the influence of any mind-altering substance."
            show wllmc coat_hat grin
            mcfiona "Those are good ground rules. But that still leaves you with a wide field. How do you narrow your selections?"
            "I want to push her out of her comfort zone, so I let myself ask the real question, just to see what happens."
            show wllmc coat_hat smallsmile
            mcfiona "If it could be any girl, why me?"
            hide wllmc
            hide fiona
            show fiona hood_cu grin_hood_cu at fiona_cu
            mb "I mean, you were the one who walked into {i}my{/i} train car. Who am I to deny the Goddess's bounty when it falls into my lap?"
            hide fiona
            show wllmc coat_hat smirk at left2
            show fiona hood grin_hood at right1plus
            mcfiona "Is that what you remember? Because it felt to me more like fighting sword to sword."
            show fiona hood smirk_hood
            mb "And you don't think that can be alluring?"
            mb "That moment when you draw close, blades straining against each other, your bodies close enough to touch..."
            mcfiona "Maybe we should test out that theory some time."
            hide fiona
            hide wllmc
            show wllmc coat_hat_cu angry_cu at wllmc_cu
            "(This conversation is starting to feel like a bucking horse. It's taking everything I have just to stay in control.)"
            show wllmc coat_hat_cu smirk_cu
            "(Turns out, I don't hate that at all.)"
            hide wllmc
            show wllmc coat_hat smirk at left2
            show fiona hood smirk_hood at right1plus
            mb "A tempting invitation. With you, I'm sure my abilities would be tested to their very limits."
            show fiona hood smile_hood
            mb "It's rare I meet anyone who makes me feel like I might lose."
            show wllmc coat_hat grin
            mcfiona "Does it thrill you? Do you enjoy the doubt?"
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            mb "A little exhilaration is good for the blood. Makes you feel more alive."
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu:
                xpos 630
            show wllmc coat_hat_cu smirk_cu at wllmc_cu:
                xpos 30
            "A look passes between us, and I know that we're both feeling that rush right now..."
            hide wllmc
            hide fiona
            show wllmc coat_hat smirk at left2
            show fiona hood smirk_hood at right1plus
            "Even though these are only words, even though it's only a game."
            show wllmc coat_hat smallsmile
            show fiona hood smile_hood
            mcfiona "The moment when you think, I do this, or I die. And then you do it."
            mcfiona "Or you die the little death, and come out feeling more alive."
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            mb "Oh, so you do want to kill me."
            hide fiona
            show wllmc coat_hat smile at left2
            show fiona hood smirk_hood at right1plus
            "She laughs as she says it, a gurgling giggle, delightfully unrestrained."
            show fiona hood smile_hood
            mcfiona "I know I'd like to hear you scream."
            show wllmc coat_hat surprised
            "Something in my stomach flips."
            hide fiona
            hide wllmc
            show wllmc coat_hat_cu surprised_cu at wllmc_cu
            "(Even I can't believe I just said that!)"
            hide wllmc
            show wllmc coat_hat surprised at left2
            show fiona hood smile_hood at right1plus
            "But everything feels so natural, so in tune, that it's almost inevitable."
            mb "I think you'll get your chance some day."
            show wllmc coat_hat smile
            mcfiona "Wouldn't that be nice. What makes you so sure?"
            mb "You're not like anyone else I've ever met. And that makes me curious."
            mb "And when I'm curious I want to know everything."
            hide wllmc
            hide fiona
            show fiona hood_cu grin_hood_cu at fiona_cu
            mb "I'm a woman who hates to leave a secret undiscovered."
            hide fiona
            show wllmc coat_hat smirk at left2
            show fiona hood grin_hood at right1plus
            mcfiona "I have a lot of secrets."
            show wllmc coat_hat smile
            "Fiona smiles that bright, unflustered smile again."
            mb "Then I'll have to work very hard."

        "Let the moment pass.":
            $menuhideborder = False
            show wllmc coat_hat smirk at left2
            show fiona hood smile_hood at right1plus
            mcfiona "Now now, I can't go giving away my tricks for free."
            mb "Oh, are you asking to be paid?"
            show wllmc coat_hat smile
            mcfiona "That silver tongue of yours can turn to a dagger in a flash, huh?"
            hide fiona
            hide wllmc
            show wllmc coat_hat_cu angry_cu at wllmc_cu
            "(And here I told myself I wasn't going to flirt!)"
            hide wllmc
            show wllmc coat_hat smile at left2
            show fiona hood grin_hood at right1plus
            mb "Well it is my best weapon. I have to keep it honed."

    scene bg_wll_town_streets_night_lights at bg
    show wllmc coat_hat smile at left2
    show fiona hood grin_hood at right1plus
    with dissolve
    "We both laugh, and the last shreds of our tense escape vanish into thin air with the sun."
    show wllmc coat_hat smallsmile
    show fiona hood smile_hood
    mcfiona "Seriously though, that scam you pulled on the conductor was definitely something."
    show wllmc coat_hat grin
    mcfiona "I can't believe you called me sugar plum!"
    mb "What, you don't think that suits you?"
    show wllmc coat_hat smile
    mcfiona "I feel I deserve something more dignified. Just a smidge."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "I'll bear that in mind, my sweet angel."
    hide fiona
    show wllmc coat_hat smile at left2
    show fiona hood grin_hood at right1plus
    "I roll my eyes at her, and she beams."
    mcfiona "And how'd you just happen to have two fake tickets?"
    show fiona hood smile_hood
    "Fiona shrugs."
    mb "I always have what I need. Call it a talent."
    hide wllmc
    hide fiona
    show fiona hood_cu smile_hood_cu at fiona_cu
    "She taps her forehead knowingly."
    hide fiona
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    "(Guess she's not ready to let me in on all her outlaw secrets.)"
    hide wllmc
    show wllmc coat_hat smile at left2
    show fiona hood smile_hood at right1plus
    mcfiona "Do you think you could use that talent to get me what I need?"
    show fiona hood smirk_hood
    mb "Depends on what it is you need."
    show wllmc coat_hat smallsmile
    mcfiona "A job. I had something lined up in Serpent's River, but I can't imagine there's much here for me in a one-horse town like Wisp Willow."
    show fiona hood smile_hood
    mb "I'll have you know we have at least four horses."
    show fiona hood grin_hood
    mb "But I take your point. Consider yourself owed a job."
    "She takes my hand in hers and bows over it, and the gesture sends a little shiver down my spine."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    "(I like the way that looks.)"
    hide wllmc
    show wllmc coat_hat smile at left2
    show fiona hood grin_hood at right1plus
    mcfiona "Well, if you're going to be generous, I can be too."
    "I pull her client's pocketbook out and offer it to her."
    show wllmc coat_hat smirk
    show fiona hood surprised_hood
    mcfiona "Want to split the contents?"
    "Fiona looks at the pocketbook, up at me, then back down at the pocketbook again."
    show fiona hood grin_hood
    "A bright smile of disbelief lights up her face."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "When did you get that? I didn't see it happening at all!"
    hide fiona
    show wllmc coat_hat grin at left2
    show fiona hood smirk_hood at right1plus
    mcfiona "I guess I've got defter fingers than you thought."
    show wllmc coat_hat smirk
    show fiona hood pout_hood
    "Fiona narrows her eyes at me."
    hide wllmc
    hide fiona
    show fiona hood_cu pout_hood_cu at fiona_cu
    mb "How annoying!"
    hide fiona
    show wllmc coat_hat smirk at left2
    show fiona hood pout_hood at right1plus
    "Her lips purse for a moment, but it's only a cloud passing across the sun of her smile."
    show fiona hood smirk_hood
    mb "What a delightful complication you are."
    show fiona hood smile_hood
    mb "Come on. Let's get you to Ada. If anyone will have an idea about a job for you, it's her."

    scene bg_wll_saloon_night_lights_people at bg with wiperightdissolve

    stop music fadeout 1.0
    play music wlleverydayupbeat3 fadein 1.0
    "The bar Fiona leads me to is hopping, the crowd spilling out onto the street."
    show wllmc coat smallsmile at left2
    show fiona cloak smile at right1plus
    mb "Let's wait here. Ada will be out in a minute anyway."
    show wllmc coat surprised
    mcfiona "You know that for sure?"
    show fiona cloak smirk
    mb "I know lots of things for sure."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(She really is the most infuriatingly evasive person I've ever met.)"
    show wllmc coat_cu smirk_cu
    "(It's annoying how much I like it.)"
    hide wllmc
    show ada hat basic at centre
    "A honey-blonde woman comes out with a huge tray of drinks."
    hide ada
    show wllmc coat_cu smallsmile_cu at wllmc_cu
    "(That must be Ada.)"
    hide wllmc
    show wllmc coat smallsmile at left2
    show fiona cloak smirk at right1plus
    mb "Bet you I can tell which order is for which person before they take it."
    show wllmc coat smile
    mcfiona "So? I could do the same."
    mb "Let's have a little competition then."
    show wllmc coat smirk
    mcfiona "What are the odds?"
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "Give me something sweet when I win."
    hide fiona
    show wllmc coat_cu smile_cu at wllmc_cu
    mcfiona "Okay. That guy over there is going to take the whiskey."
    hide wllmc
    show wllmc coat surprised at left2
    show fiona cloak smirk at right1plus
    mb "Wrong. The whiskey is for the woman in the blue dress. That man ordered the drink with the little paper umbrella."
    show wllmc coat angry
    "The customers take exactly the drinks Fiona predicted, and I look at her, eyes narrowed."
    mcfiona "You knew they were going to do that. They must be regulars."
    show fiona cloak grin
    mb "Then let's try again."
    show wllmc coat surprised
    "We play another round, but the result is exactly the same."
    show wllmc coat angry
    mcfiona "Damn, and I thought I was good at cold reading. How do you do it?"
    show fiona cloak smirk
    mb "I'm not using cheap tricks, [genericfn]. I'm a mystic."
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "She taps her forehead again, right in the middle where her bangs split."
    hide fiona
    show wllmc coat_cu angry_cu at wllmc_cu
    "(She can't be serious.)"
    hide wllmc
    show ada hat smile at centre
    "As I struggle to find words, Ada comes over to us, a friendly smile on her face."
    hide ada
    show wllmc coat smallsmile at left3
    show ada hat smile at right3
    st "Well if it isn't my favorite Bluebell. And her new friend, I see. Nice to meet you, Snowdrop!"
    mcfiona "Likewise."
    hide wllmc
    hide ada
    show ada hat_cu smile_cu at ada_cu
    st "What can I get the two of you?"
    hide ada
    show wllmc coat smile at left3
    show ada hat smile at right3
    mcfiona "Something sweet for Fiona. And she can probably tell you my order."
    st "She is just the best at guessing, it's true."
    hide wllmc
    show fiona cloak pout at left3
    mb "Not for [genericfn], I'm afraid. She's the one person I can't predict."
    "Something in her manner makes me hesitate."
    hide fiona
    show wllmc coat smallsmile at left3
    mcfiona "In that case, a beer for me."
    hide ada
    show wllmc coat angry
    show fiona cloak pout at right3
    "Ada heads off to get our drinks, and I give Fiona a sharp look."
    mcfiona "What happened to being a 'mystic'? Powers not working all of a sudden?"
    show fiona cloak sad
    "Fiona looks momentarily downcast."
    mb "That's just it - they aren't. You're the one person my eye refuses to see."
    show wllmc coat surprised
    mcfiona "Wait, so you admit that card reading on the train was bullshit?"
    show fiona cloak smile
    "Fiona's smile is ambiguous and evasive."
    mb "No. Those cards didn't tell me your future, just your present. And they work a little differently to my whispers anyway."
    show wllmc coat angry
    mcfiona "Or it's all a sham, and you're spinning empty words as quick as you can think 'em."
    hide wllmc
    hide fiona
    show fiona cloak_cu grin_cu at fiona_cu
    mb "Wouldn't you rather believe you're just that special?"
    hide fiona
    show wllmc coat smirk at left3
    show fiona cloak grin at right3
    mcfiona "Who says I need your help to feel special? I know how amazing I am."
    show fiona cloak smile
    "Fiona gives me a long, slow, admiring look."
    mb "You certainly do."
    hide wllmc
    hide fiona
    show ada hat basic at centre
    "Ada comes back out with our drinks, and I take a long, refreshing gulp of my beer."
    show fiona cloak smile at left3
    show ada hat basic at right3
    mb "Say, Ada, my new friend is in need of some assistance. You wouldn't know of any work going?"
    show ada hat sad
    st "Work? Nothing particular comes to mind."
    show ada hat smile
    st "But I'm surprised you're not jumping at the chance to pick her up yourself, Fiona."
    st "You're always complaining about the Wardens being too busy."
    show fiona cloak surprised
    "Fiona's eyes widen."
    mb "You know, I hadn't thought of that at all."
    hide fiona
    hide ada
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Wardens? Is that some kind of law force? But Fiona's an outlaw through and through.)"
    "(What's she doing running with the local Pinkertons?)"
    hide wllmc
    show fiona cloak basic at left3
    show ada hat smile at right3
    mb "I do need to check in with them. I'll mull it over on the way."
    hide ada
    hide fiona
    show fiona cloak_cu sad_cu at fiona_cu
    "She hesitates, and moves her hand ever so slightly, her pinky finger brushing mine."
    hide fiona
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(It almost feels... vulnerable. I haven't seen anything like that from her before.)"
    hide wllmc
    show fiona cloak_cu smile_cu at fiona_cu
    mb "If I leave for a bit, will you wait here?"
    hide fiona

    $menuhideborder = True
    menu fionas1e2c2:
        "I've got nothing better to do.":
            $menuhideborder = False
            show wllmc coat smile at left1plus
            show fiona cloak smile at right1plus
            mcfiona "Why not? It's not like I've got anything better to do."
            st "There are plenty of ways to entertain yourself at my bar, don't you doubt it."
        "If you give me something to wait for.":
            $menuhideborder = False
            show wllmc coat smirk at left2
            show fiona cloak smile at right1plus
            mcfiona "That depends. Will you give me something to wait for?"
            show fiona cloak grin
            mb "How does another drink sound?"
            show wllmc coat smile
            mcfiona "It sounds just fine, thank you."
        "You'll just have to find out.":
            $menuhideborder = False
            show wllmc coat smile at left2
            show fiona cloak smile at right1plus
            mcfiona "I guess you'll just have to find out. Live in anticipation like the rest of us."
            hide fiona
            hide wllmc
            show wllmc coat_cu smirk_cu at wllmc_cu
            "(I'm not convinced Fiona has any power beyond cunning and wiles, but I'm not above teasing her about it.)"
            hide wllmc
    show wllmc coat smile at left2
    show fiona cloak grin at right1plus
    mb "Well then. I'll see you as soon as I can."

    hide wllmc
    hide fiona
    with dissolve

    stop music fadeout 1.0
    play music wlleverydaycalm2 fadein 1.0
    "Fiona walks off, leaving me and Ada alone."
    show wllmc coat basic at left3
    show ada hat smile at right3
    st "Come into the bar with me, we can chat more comfortably there."
    "I take a seat at the counter, and as Ada begins pouring drinks, we chat."
    st "You known Fiona long?"
    show wllmc coat smile
    mcfiona "Just met her today. Is she always the type to warm up so quickly?"
    st "She's a friendly gal, that's for sure. But she rarely runs quite as hot as she seems to with you."
    hide ada
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Then maybe I have a shot. Having someone to warm my bed would certainly make the time I spend here less tedious.)"
    hide wllmc
    show wllmc coat smile at left3
    show ada hat smile at right3
    mcfiona "She's an odd fish. I can't get a read on her, honestly."
    st "But you'd like to."
    hide wllmc
    hide ada
    show ada hat_cu smile_cu at ada_cu
    "She smirks at me, and I feel a little flush on my cheeks."
    hide ada
    show wllmc coat embarrassed at left3
    show ada hat smile at right3
    mcfiona "I wouldn't say no."
    show ada hat basic
    st "Just make sure you've got a tight rein on your heart. Fiona is generous, but she doesn't do long-term. Or serious."
    hide ada
    hide wllmc
    show wllmc coat_cu smile_cu at wllmc_cu
    "(I stopped listening after generous.)"
    hide wllmc
    show wllmc coat surprised at left3
    show ada hat basic at right3
    "A sudden thought invades my mind, of Fiona lying bare against cool white sheets, her hair unraveled from those prim, missish braids."
    hide ada
    hide wllmc
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(I wonder what kind of noises she makes when you touch her right.)"
    hide wllmc
    show wllmc coat surprised at left3
    show ada hat angry at right3
    play sound glass_shattering
    "A sudden pop sounds, and then another, as several bottles of alcohol boil and shatter."
    show wllmc coat surprised:
        easein 0.4 yoffset 180
    show ada hat angry:
        easein 0.4 yoffset 180
    "Ada and I duck down, hiding from the raining shards of glass."
    hide ada
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Dust in my mouth and sun in my eyes, my bad luck is back.)"
    hide wllmc
    show wllmc coat surprised at left3:
        yoffset 180
    show ada hat basic at right3:
        yoffset 180
    st "Are you alright?"
    show wllmc coat sad
    mcfiona "Yes. Sorry. Things like this just happen around me sometimes."
    show ada hat smile
    st "I wouldn't be too quick to take the blame, Snowdrop. This ain't even the oddest thing to happen this week."
    hide wllmc
    hide ada
    "I go grab the broom hanging on the back of the door, and Ada and I begin to clear up the mess."
    show wllmc coat smallsmile at left3
    show ada hat smile at right3
    st "Wisp Willow is a funny place full of strange people."
    show wllmc coat smirk
    mcfiona "You included?"
    st "I suppose so! I certainly fit in here better than I ever did back East."
    st "Though wait until you meet the rest of Fiona's crew. They give even her a run for her money."
    hide wllmc
    hide ada

    $menuhideborder = True
    menu fionas1e2c3:
        "Are they dangerous?":
            $menuhideborder = False
            show wllmc coat surprised at left3
            show ada hat smile at right3
            mcfiona "Is that a warning? Are they dangerous?"
            st "Everyone out here is dangerous. But they're certainly not people I'd cross in a hurry."
        "No way. Fiona's special.":
            $menuhideborder = False
            show wllmc coat angry at left3
            show ada hat smile at right3
            mcfiona "No way. There's something special about Fiona."
            "Ada raises an eyebrow at me."
            st "I wouldn't disagree, Snowdrop."
            st "You've seen the way she seems to know everything. She reminds me of my grandmother. People used to say she had the Knack."
            hide ada
            hide wllmc
            show wllmc coat_cu surprised_cu at wllmc_cu
            "(Does she mean... magic?)"
            hide wllmc
        "I'm not sure I can handle that.":
            $menuhideborder = False
            show wllmc coat grin at left3
            show ada hat smile at right3
            mcfiona "I'm not sure I can handle that. One mischievous goblin is more than enough."
            show wllmc coat smirk
            "Ada laughs."
            st "No, not like that. They're all unique characters, but the others tend more solemn and serious. Except maybe Sascha."
    show wllmc coat surprised at left3
    show ada hat smile at right3
    mcfiona "Do you think I'd be doing the right thing, taking a job with them?"
    show ada hat basic
    "Ada considers the question as she dumps the shattered glass into a nearby bucket."
    st "As long as you keep your wits about you, sure."
    st "I don't understand exactly what the Wardens do, but even the Sheriff doesn't cross them."
    hide ada
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Is that so? In that case, maybe I can use them to my advantage. They might be able to wipe my ledger clean.)"
    hide wllmc
    show wllmc coat smallsmile at left3
    show ada hat basic at right3
    "I sit back down at the bar, and Ada hands me another beer. But just as I'm about to take a sip..."
    hide wllmc
    hide ada


    stop music fadeout 1.0
    play music wlltense2 fadein 1.0
    $sidecharone = "Familiar Voice"
    sid1 "It's you! I was hoping to run into you again, but I didn't think I actually would."
    show diana casual basicglasses at centre
    "I turn around and see Fiona's lost client from the train, standing a few feet away and staring right at me."
    hide diana
    show wllmc coat_cu sad_cu at wllmc_cu
    "(Oh no.)"
    hide wllmc
    show wllmc coat sad at centre
    "The stolen pocketbook tucked away in my trousers suddenly seems much heavier than before."
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Have I been nicked already?)"
    show wllmc coat_cu sad_cu
    "(Sorry, Fiona. Looks like I might not be able to keep our appointment after all.)"
    hide wllmc

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
