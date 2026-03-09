label fiona_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_town_streets_night at bg
    show fog_effect:
        alpha 0.4
    play music wllsomber1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show fiona hood sad_hood at right1
    show wllmc coat_hat surprised at left1plus
    "Fiona's fingers stroke my wrist gently, and her eyes gaze into mine, bright and clear as sunlight."
    mb "Don't go."
    show wllmc coat_hat angry
    mcfiona "Give me one reason why I should stay."
    show fiona hood surprised_hood
    "Fiona hesitates, then an idea makes her eyes light up."
    show fiona hood smile_hood
    mb "Give me a chance to explain. We'll go to the boarding house. I'll answer any questions you have."
    mb "And if you still want to leave after, I'll give you the money for your ticket myself."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    "(Well that's a deal I'm not gonna pass up.)"
    hide wllmc
    show fiona hood smile_hood at right1plus
    show wllmc coat_hat basic at left1plus
    mcfiona "Fine."
    hide wllmc
    hide fiona
    show donna casual basic at centre
    "The three of us head down the street to the boarding house, where a kind, solid-looking woman stands smoking outside."
    show fiona hood grin_hood at left3
    show donna casual basic at right3
    mb "Donna, I have a present for you."
    hide fiona
    show wllmc coat_hat surprised at left3
    "She sets her hand in the middle of my back and gives me a gentle nudge forward. Donna looks unimpressed."
    hide wllmc
    show fiona hood grin_hood at left3
    show donna casual angry at right3
    bo "This won't be a repeat of your last, will it? This is a respectable boarding house, not a bordello."
    show fiona hood smirk_hood
    mb "Don't worry, [genericfn] here is a colleague. Nothing untoward at all."
    bo "Mm-hmm."
    "She looks deeply skeptical, but waves us through anyway."
    hide fiona
    hide donna
    show wllmc coat_hat_cu smirk_cu at wllmc_cu
    "(She might pretend, but I don't think she's immune to Fiona's charming ways.)"

    scene bg_wll_common_room_night_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wlleverydaycalm1 fadein 1.0
    "We get to the common room, and I make an immediate beeline for the little shelf of alcohol in the corner."
    hide wllmc
    show wllmc coat sleep at centre
    "The spirit I uncork is barely a grade above rotgut, but the burn as it hits my throat is the first thing that makes me feel fully real again."
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(I didn't know just how spooked I was until now, but at least my brain is working again.)"
    hide wllmc
    show sascha belt basic at left3
    show fiona cloak basic at right3
    "Sascha sprawls across an armchair, and Fiona tucks herself into the corner of a couch like a prim cat."
    hide sascha
    show wllmc coat angry at left3
    mcfiona "Right. Tell me everything."
    show fiona cloak smirk
    mb "You know, I really thought it was an act."
    mb "I was so sure you were playing your own game, but no. It turns out that a sleeping witch really did fall right into my lap."
    hide fiona
    show sascha belt smirk at right3
    sasch "Witch? Come up with something more believable. There hasn't been a witch in a hundred years."
    show wllmc coat sad
    "A faint trace of disappointment lingers on my tongue like the final burn of the alcohol."
    hide sascha
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(I hoped they were about to be really honest with me.)"
    show wllmc coat_cu angry_cu
    "(But if this is the way they want to play it, I'll play along.)"
    hide wllmc
    show wllmc coat smirk at left3
    show fiona cloak basic at right3
    mcfiona "What's supposed to make me a witch? I've no pointy hat, no cat, and I've never once cursed a baby."
    show fiona cloak grin
    "I grin, and Fiona laughs her bright, sweet laugh."
    hide wllmc
    hide fiona
    show sascha belt basic at centre
    sasch "Witches are some of the most powerful supernatural creatures this world knows."
    sasch "If you believe the rumors, they can do just about anything."
    hide sascha
    show wllmc coat_cu angry_cu at wllmc_cu
    "(More of this 'you're so special nonsense'. I can't believe they're laying it on so thick.)"
    hide wllmc
    show fiona cloak_cu angry_cu at fiona_cu
    "Fiona narrows her eyes at me."
    mb "Stop pretending. You don't believe a word of this, do you?"
    hide fiona

    $menuhideborder = True
    menu fionas1e5c1:
        "Lie.":
            $menuhideborder = False
            show wllmc coat smirk at left3
            show fiona cloak angry at right3
            mcfiona "I mean, it's a lot to take in, you know? But I'm listening. I did just see a ghost, after all."
            show fiona cloak smile
            "Fiona tilts her head sideways."
            mb "You're so careful to avoid tells when you're lying, it's a tell all by itself."
            show wllmc coat angry
            "My mouth twists at that, but I can't exactly argue."
        "Equivocate.":
            $menuhideborder = False
            show wllmc coat angry at left3
            show fiona cloak basic at right3
            mcfiona "I'm not making any judgments. I need more information before I make up my mind."
            show fiona cloak sad
            mb "But your thoughts are racing, and I'm not sure I like the direction they're going."
        "Be honest?":
            $menuhideborder = False
            show wllmc coat surprised at left3
            show fiona cloak angry at right3
            "I open my mouth to lie, but something about the look in Fiona's eyes stops me."
            show wllmc coat angry
            mcfiona "Fine, you're right. I think this is nonsense."
    show fiona cloak surprised
    mcfiona "Look, what's more likely? That there's a whole secret world people don't know about, hidden from everyone?"
    mcfiona "Or that I just got tricked by two deft con artists?"
    show fiona cloak smirk
    mb "The part where you saw an actual ghost?"
    "I roll my eyes."
    show wllmc coat smile
    mcfiona "I can think of about five different ways of making that happen. Mushroom extract in my beer most likely."
    hide wllmc
    hide fiona
    show fiona cloak_cu basic_cu at fiona_cu
    "Fiona looks up at me, eyes bright and curious."
    hide fiona
    show wllmc coat smile at left3
    show fiona cloak smile at right3
    mb "Do you want that train ticket?"
    show wllmc coat smirk
    mcfiona "Nope. I'm still game."
    show fiona cloak smirk
    mb "Even though I might be trying to con you?"
    show wllmc coat basic
    "I shrug."
    show fiona cloak smile
    mcfiona "People try and con me all the time. It just means I've got to watch my back."
    show wllmc coat grin
    mcfiona "Plus, I'm desperately curious what could be worth all this effort."
    hide wllmc
    hide fiona
    show fiona cloak_cu grin_cu at fiona_cu
    "Fiona laughs again, and the sound sends a little shiver down my spine."
    hide fiona
    show wllmc coat grin at left3
    show fiona cloak grin at right3
    mb "I'm not going to stop trying to convince you that I'm telling the truth."
    show wllmc coat smirk
    mcfiona "Don't expect you to."
    mb "Well, in that case, drop by the apothecary tomorrow. We have a lot to do."

    scene bg_wll_apothecary_lights at bg
    show fiona cloak grin at centre
    with fade
    stop music fadeout 1.0
    play music wlleverydayupbeat1 fadein 1.0
    "The bell of the apothecary jangles as I step through the door and Fiona beams at me from behind the counter."
    show wllmc coat smallsmile at left3
    show fiona cloak grin at right3
    mb "Good after-morning to you, sunshine."
    show wllmc coat smile
    show fiona cloak smile
    mcfiona "You can't blame a girl for sleeping in a little after a night like last night."
    "I look around the shop as Fiona ducks under the counter, and when she comes back up, she's holding a collection of equipment."
    show wllmc coat surprised
    mcfiona "What's that for?"
    mb "I'm going to brew a potion."
    show fiona cloak basic
    mb "I was thinking about it last night, and maybe the reason I can't see your future is some kind of energy block."
    hide wllmc
    hide fiona
    show fiona cloak_cu basic_cu at fiona_cu
    mb "It might even explain why you're so stubborn about not believing your own eyes."
    hide fiona
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Why does she care so much about what I believe?)"
    hide wllmc
    show wllmc coat smirk at left3
    show fiona cloak basic at right3
    mcfiona "Given my reservations, you really think I'm going to take a strange drink from you?"
    show wllmc coat angry
    mcfiona "I'm not that big a sucker, no matter how cute you are."
    "Fiona gives me a very dry look."
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "I'll drink it first, how about that?"
    hide fiona
    show wllmc coat surprised at left3
    show fiona cloak basic at right3
    mcfiona "How do I know you didn't prepare some kind of pre-antidote for yourself first?"
    show fiona cloak smirk behind wllmc:
        pause 0.1
        easein 0.4 centre
    "I smile as I say it, since it's mostly a joke, but Fiona leans over and flicks my cheek."
    show fiona cloak smile
    mb "I might as well ask why you don't believe me after everything."
    mb "One strange event, I can understand you dismissing, but what about the cards?"
    hide wllmc
    hide fiona
    show fiona cloak_cu basic_cu at fiona_cu
    "She starts to mix her ingredients and gives me a penetrating stare."
    mb "What about the kiss on the train?"
    hide fiona
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(It was surprising. Unforgettable.)"
    hide wllmc
    show fiona cloak basic at centre
    show wllmc coat smirk at left3
    mcfiona "What {i}about{/i} the kiss?"
    show fiona cloak smile
    mb "Didn't you feel it? That moment when the world shifted."
    hide fiona
    hide wllmc
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(I did.)"
    "(I just thought...)"
    hide wllmc
    show fiona cloak smirk at centre
    show wllmc coat smirk at left3
    mcfiona "Maybe. I'd have to try again to know for sure."
    show fiona cloak smile
    "I wink at her, and Fiona's smile softens back into real amusement."
    mb "You're incorrigible. And bullheaded. And completely unpredictable."
    show wllmc coat grin
    mcfiona "Wow, look at you, listing all my charm points."
    mcfiona "Maybe my innate unpredictability is why you can't see my future."
    hide wllmc
    hide fiona
    show fiona cloak_cu grin_cu at fiona_cu
    mb "Maybe. It's certainly been a real diversion, sweet complication."
    hide fiona
    show fiona cloak smirk at centre
    show wllmc coat grin at left3
    mb "If this potion works, I think I'll miss it a little."
    hide wllmc
    hide fiona
    "She lights a fire in a worktop safe container, and sets the potion to boil over it."
    show wllmc coat smile at left3
    show fiona cloak smile at right3
    mcfiona "I'd certainly miss my spontaneity if it was gone."
    mb "It's a novel experience for me. But I don't hate it."
    hide wllmc
    hide fiona
    show fiona cloak_cu basic_cu at fiona_cu
    "She gives me a sparkling glance, up through her eyelashes."
    hide fiona
    show wllmc coat smirk at left3
    show fiona cloak grin at right3
    mcfiona "When you say things like that, it almost makes me believe you."
    "Fiona decants the potion into a glass and offers it to me."
    mcfiona "Uh uh, you first, remember?"
    show fiona cloak sleep
    "Fiona laughs and takes a big gulp of the potion, then does an all body shudder."
    show fiona cloak pout
    mb "I'd forgotten how vile that tastes."
    mcfiona "That doesn't really make me want to drink it."
    show fiona cloak smile
    mb "How can I persuade you, then? Short of convincing you all this is real."
    mcfiona "Hey, you're welcome to try. I love seeing a good hustle."
    hide fiona
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(This could be my chance to catch Fiona out in a lie.)"
    "(Or just while away the time talking to her. That wouldn't be so bad either.)"
    hide wllmc
    show wllmc coat grin at left3
    show fiona cloak smirk at right3
    mcfiona "Why don't you teach me how to make a love potion?"
    show fiona cloak surprised
    mb "You're asking me to perform for you?"
    show wllmc coat smirk
    mcfiona "Are you opposed to that. I thought it was exactly what you wanted."
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "Fiona licks her lips thoughtfully, her mouth curving up into a smile."
    mb "Maybe. If you ask me real nice."
    hide fiona

    $menuhideborder = True
    menu fionas1e5c2:
        "Ask Fiona about love potions really nicely." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show wllmc coat sad at left3
            show fiona cloak smile at right3
            mcfiona "Please? Pretty please with a cherry on top?"
            show fiona cloak grin
            mb "That's what I like to hear."
            hide wllmc
            show fiona cloak grin at centre
            "She comes out from behind the counter and walks over to the back wall of the shop, picking up a little bottle."
            show wllmc coat smile at left3
            show fiona cloak smirk at right3
            mb "What made you ask about love potions? I figured a gal like you would be more interested in something like a philosopher's stone."
            show wllmc coat surprised
            mcfiona "What does that do?"
            mb "As much gold as you want, and immortal life."
            show wllmc coat smirk
            mcfiona "As much gold as I want would just devalue the price of gold. And I'll pass on the second."
            show fiona cloak smile
            mb "Well good, because I don't think you have a spare twenty years to sit around making one."
            show wllmc coat smallsmile
            mcfiona "Sounds like there's quicker and better ways to get rich."
            hide wllmc
            hide fiona
            show fiona cloak_cu grin_cu at fiona_cu
            mb "Exactly."
            hide fiona
            show wllmc coat smallsmile at left3
            show fiona cloak smile at right3:
                pause 0.1
                easein 0.4 right1
            "She hands me the bottle, our fingertips brushing."
            show wllmc coat smile
            mcfiona "Mandrake root."
            "I look through the dark glass, and can just make out the warped and twisted form of the root inside."
            show wllmc coat surprised
            mcfiona "What does this do?"
            mb "It's the basis of a lot of different potions. Almost anything that acts on humans, really."
            mb "Whether you want to make a person ten times stronger, cure an ailment, or grant fertility, it all starts with mandrake."
            show wllmc coat smirk
            mcfiona "It's a horrible little thing, isn't it?"
            show fiona cloak smirk
            mb "Absolutely."
            show wllmc coat smallsmile
            mcfiona "So I've got this. What do I do next?"
            show fiona cloak basic
            mb "Well, it depends. If you want to create a general, non-specific emotion, that's easy enough."
            mb "Rage, for example, is mandrake root plus wormwood plus hot chili powder."
            show wllmc coat surprised
            mcfiona "Why would you want to make someone feel angry?"
            hide wllmc
            hide fiona
            show fiona cloak_cu basic_cu at fiona_cu
            "Fiona gives me a deadpan stare."
            hide fiona
            show wllmc coat surprised at left3
            show fiona cloak basic at right1
            mb "You're telling me you can't think of a time on a job when that would have been useful?"
            show wllmc coat smile
            mcfiona "Point taken. What about love?"
            show fiona cloak smile
            mb "Mandrake root plus honey and attar of roses."
            mb "I saw someone dose themselves with that once. They spent the rest of the day hugging people and being sentimental."
            show wllmc coat surprised
            mcfiona "Why on earth would they do that?"
            mb "Well, they were a pretty reserved person in general. I think they just wanted a break from their own head."
            show wllmc coat angry
            "I make a face."
            mcfiona "Alcohol sounds a lot easier."
            hide wllmc
            hide fiona
            show fiona cloak_cu smirk_cu at fiona_cu
            mb "And here I had you marked as the cuddly type."
            hide fiona
            show wllmc coat grin at left3
            show fiona cloak smirk at right1
            "She taps her hip against mine and I laugh."
            mcfiona "Not that I'm opposed to all embraces, mind you. I just like them to be with the right person."
            show fiona cloak grin
            mb "If you ever want to get more comfortable with them, I'll gladly offer myself as a test subject."
            show wllmc coat embarrassed
            "I look down at her slim curves and my throat gets a bit dry."
            mcfiona "I'll bear that in mind."
            show wllmc coat surprised
            mcfiona "But back to the topic of potions. What if I don't want a general emotion. What if I want X to fall in love with Y?"
            hide wllmc
            hide fiona
            show fiona cloak_cu sad_cu at fiona_cu
            mb "I couldn't do it."
            hide fiona
            show wllmc coat surprised at left3
            show fiona cloak sad at right1
            mcfiona "Why not?"
            show fiona cloak angry
            mb "Besides the fact that it's horribly unethical?"
            show wllmc coat smirk
            mcfiona "What, you're going to let a little thing like a moral compass stop my fun?"
            show fiona cloak pout
            mb "Everyone's got their own lines. Messing with hearts crosses one of mine."
            hide wllmc
            hide fiona
            show fiona cloak_cu smirk_cu at fiona_cu
            "She reaches out and takes my hand, lacing our fingers together."
            mb "And don't try and pretend you don't know what I mean. You're the one who interrupted my reading, after all."
            hide fiona
            show wllmc coat sleep at left3
            show fiona cloak smirk at right1
            "I sigh, and give her hand a little squeeze."
            show wllmc coat smirk
            mcfiona "How very unfair of you to remember something I did yesterday."
            show fiona cloak basic
            mb "Besides, even if making a love potion didn't cross my lines, I couldn't."
            show wllmc coat surprised
            mcfiona "Oh? Why not?"
            show fiona cloak pout
            mb "You have to have felt love to make it into a potion."
            hide wllmc
            hide fiona
            show fiona cloak_cu sad_cu at fiona_cu
            "She shrugs, but her eyes are suddenly trained on the floor."
            show fiona cloak_cu pout_cu
            mb "That's outside my realm of experience."
            hide fiona
            show wllmc coat smirk at left3
            show fiona cloak smile at right1
            mcfiona "Eh, who needs love?"
            hide wllmc
            hide fiona
            show fiona cloak_cu basic_cu at fiona_cu
            "I reach out and tip her chin up, bringing her eyes to mine."
            hide fiona
            show wllmc coat_cu smirk_cu at wllmc_cu
            mcfiona "Especially when you can have fun instead."
            hide wllmc
            show fiona cloak_cu smirk_cu at fiona_cu
            "Fiona's mouth makes that terribly tempting impish smile again."
            hide fiona
            show wllmc coat_cu smirk_cu at wllmc_cu
            "(Could I? Should I?)"
            hide wllmc
            show wllmc coat smirk at left3
            show fiona cloak basic at right1
            "But just as I'm about to leave forward, Fiona's eyes flicker to the counter."
            show wllmc coat surprised
            show fiona cloak embarrassed
            mb "You should really drink that potion before it gets cold. It'll taste even worse if you leave it."
            hide fiona
            hide wllmc
            show wllmc coat_cu surprised_cu at wllmc_cu
            "(Did she ruin the moment on purpose? Or was I the only one who was feeling something right now?)"
            hide wllmc
            show wllmc coat sleep at left3
            show fiona cloak basic at right1
            "Not sure, and not wanting to push it, I take the potion and swallow it down."
            show wllmc coat angry
            mcfiona "Oh, that is really awful."
            show fiona cloak smirk
            mb "I know. I think it's some kind of rule that medicine has to be horrible."
            show wllmc coat basic
            show fiona cloak smirk behind wllmc:
                pause 0.1
                easein 0.4 xoffset -80
            "She claps my shoulder."
            hide wllmc
            hide fiona
            show fiona cloak_cu grin_cu at fiona_cu
            mb "Now, let's get on with our work."
        "Pretend you're not interested.":
            $menuhideborder = False
            show wllmc coat angry at left3
            show fiona cloak smile at right3
            mcfiona "You said we were tight on time, let's leave it."
            show wllmc coat sleep
            show fiona cloak smirk
            "I lift the drink to my lips, down it in one quick swallow, and shudder."
            show wllmc coat sad
            mcfiona "Goddess, that tastes absolutely vile."
            show fiona cloak smirk at right3 behind wllmc:
                pause 0.1
                easein 0.6 right1 xoffset -80
            "Fiona pats my shoulder sympathetically."
            hide wllmc
            hide fiona
            show fiona cloak_cu grin_cu at fiona_cu
            mb "Your heroic effort will be remembered, don't worry."
    hide fiona
    show wllmc coat angry at left3
    show fiona cloak smirk at right1 behind wllmc:
        xoffset -80
    "I wash my mouth out with a long gulp of water, and Fiona starts explaining the plan."

    scene bg_wll_town_hall_lights at bg with clockwise_wipe
    stop music fadeout 1.0
    play music wlleverydaycalm1 fadein 1.0
    "Half an hour later, we're in the town hall, waiting for Diana to appear."
    show fiona cloak smile at right1plus
    show wllmc coat basic at left2
    mb "Remember, today is just reconnaissance. You can treat it like any other two man job."
    hide fiona
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Always nice to be back on familiar ground.)"
    hide wllmc
    show fiona cloak smile at right1plus
    show wllmc coat smallsmile at left2
    mcfiona "Got it. Who's doing what?"
    show fiona cloak basic
    mb "I'll keep her talking while you scope out the joint. Best result is she asks for that reading and gives us the locket, but it's unlikely."
    show wllmc coat surprised
    mcfiona "Oh?"
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(What is so special about this locket? Sure, it might fetch a moderate price, but can it really be worth all this trouble?)"
    hide wllmc
    show fiona cloak smile at right1plus
    show wllmc coat surprised at left2
    mb "It only happens in two per cent of the futures I saw. And that's not taking your messy presence into account."
    show wllmc coat smirk
    mcfiona "I'm flattered. What's my excuse for being here, by the by?"
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "Fiona's grin is pure evil."
    hide fiona
    show fiona cloak grin at right1plus
    show wllmc coat smirk at left2
    mb "Why darling, you're my girlfriend, of course. And I just can't bear to be parted from you for a moment."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(You really think that's going to work?)"
    hide wllmc
    show diana casual basicglasses at centre
    "I don't actually get a chance to ask, because at that moment Diana comes in."
    show fiona cloak smile at left1
    show wllmc coat smallsmile at left5
    show diana casual surprisedglasses at right4
    fc "Ms. Eichen! I got your note, and I'm so curious."
    show diana casual smileglasses
    "Her eyes track to me and she gives me a beaming smile."
    fc "And [genericfn]. Lovely to see you again."
    show wllmc coat smile
    show fiona cloak smile:
        pause 0.1
        easein 0.4 left1plus
    "Fiona loops her arm through mine and leans her head against my shoulder."
    show wllmc coat smallsmile
    mb "Diana. Thank you for meeting me. I want to talk to you about that locket."
    show diana casual surprisedglasses
    fc "The locket again? I thought I made it clear that I'm not interested in giving it away."
    hide wllmc
    hide fiona
    hide diana
    show diana casual_cu surprisedglasses_cu at diana_cu
    fc "It's of both historical and sentimental significance, and will be part of the display for the celebration."
    hide diana
    show diana casual surprisedglasses at right4
    show fiona cloak smile at left1plus
    show wllmc coat surprised at left5
    "She gestures to where it sits in a display cabinet."
    show fiona cloak angry
    mb "I respect your decision not to go ahead with the reading, Diana, but the situation has changed."
    hide diana
    hide wllmc
    hide fiona
    show fiona cloak_cu angry_cu at fiona_cu
    mb "After doing some research, I realized that your locket has a powerful curse on it."
    hide fiona
    show diana casual sadglasses at right4
    show fiona cloak angry at left1plus
    show wllmc coat angry at left5
    fc "That's impossible."
    show wllmc coat sad
    "Her face grows cold, and her hands knot together. I see her rubbing the band of her wedding ring."
    hide diana
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(She was doing that last night, too. It's a tell of some kind, but I don't know her well enough to guess what it means.)"
    hide wllmc
    show diana casual sadglasses at right4
    show fiona cloak angry at left1plus
    show wllmc coat sad at left5
    fc "That locket is an heirloom that Sunmok—my wife—gave me. There's no curse attached to it."
    show fiona cloak sad
    mb "I know it's hard to hear, but I have proof. It's calling ghosts to it."
    show fiona cloak angry
    show wllmc coat surprised
    show diana casual surprisedglasses
    mb "One of them attacked my precious treasure [genericfn] last night."
    hide wllmc
    hide fiona
    hide diana
    show diana casual_cu surprisedglasses_cu at diana_cu
    "I don't know who looks more surprised, Diana or me."
    hide diana
    show diana casual surprisedglasses at right4
    show fiona cloak angry at left1plus
    show wllmc coat surprised at left5
    fc "A ghost? What was it like?"
    "There's an edge of hunger in her voice."
    hide diana
    hide fiona
    hide wllmc

    $menuhideborder = True
    menu fionas1e5c3:
        "It spoke to me.":
            $menuhideborder = False
            show fiona cloak angry at left1plus
            show wllmc coat angry at left5
            show diana casual surprisedglasses at right4
            mcfiona "It spoke to me. It was looking for something. Some kind of key."
            mcfiona "And then it got angry."
        "It was scary.":
            $menuhideborder = False
            show fiona cloak angry at left1plus
            show wllmc coat sad at left5
            show diana casual surprisedglasses at right4
            mcfiona "It was scary. It made the air feel so cold."
            "I add a little shiver, and let my voice quaver on the word cold."
        "I couldn't see its face.":
            $menuhideborder = False
            show fiona cloak angry at left1plus
            show wllmc coat sad at left5
            show diana casual surprisedglasses at right4
            mcfiona "I couldn't see its face properly."
            mcfiona "I just got a sense of it. It seemed sad, but also dangerous."
    show wllmc coat angry
    show fiona cloak sad
    mb "You see why this is so dangerous. That ghost could have hurt my pearl. Please. Help us."
    show diana casual sadglasses
    fc "No. I'm sorry, but I need to ask you to leave. We have nothing more to discuss."
    hide fiona
    hide diana
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(She shut that down real fast. Too fast. She's definitely hiding something.)"
    scene bg_wll_town_streets_sunset at bg with wiperightdissolve
    "We head back onto the street, and I give Fiona a look."
    show wllmc coat_hat smirk at left3
    show fiona cloak basic at right3
    mcfiona "So. On to plan B?"
    show fiona cloak surprised
    "Fiona doesn't answer. Her eyes are wide, staring straight into the sinking sun."
    show wllmc coat_hat surprised
    mcfiona "Hey, you shouldn't do that. It's bad for your eyes."

    scene fiona_s1_mini4 at bg
    with fade
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    show cinema_fov at cinema_fov_in
    pause 1.0
    show fiona_s1_mini4 at bg as pulse_effect:
        align(0.5, 0.5) alpha 0.2 zoom 1.1 transform_anchor True
        linear 0.5 zoom 1.5 alpha 0
    "But as I say the word eyes, hers light up, shining with terrible power."
    "On her forehead, another eye appears, and it too glows deathly bright."
    show cinema_fov at cinema_fov_out
    scene bg_wll_town_streets_sunset at bg
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    with fade
    "(What is this?)"
    hide wllmc
    show wllmc coat_hat surprised at left3
    show fiona cloak surprised_purple at right3
    mcfiona "Fiona? Fiona, what's happening?"
    hide wllmc
    hide fiona
    show fiona cloak_cu angry_purple_cu at fiona_cu
    mb "In the beginning was the end and the end was a cold room and an unlit hearth and tears spilling tears falling like stars..."
    hide fiona
    show wllmc coat_hat surprised at left3
    show fiona cloak angry_purple at right3
    "Her face twists with what looks like agony, and her hand is gripping mine so hard I think my bones will break."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu sad_cu at wllmc_cu
    "(Is this what magic does to you?)"
    "(How on earth do I help her? How do I get this to stop?)"
    hide wllmc

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
