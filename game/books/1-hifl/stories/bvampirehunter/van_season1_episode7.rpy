label van_season1_episode7:

    $tbc = False
    scene bg van_interior_loft_night at bg
    play music hiflliteromance
    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Is she going to-?!)"
    hide hiflmc
    show vanessa casual_cu surprised_cu at vanessa_cu
    "She pauses, staring at my face in wonder"
    va "You really are just like her..."
    hide hiflmc
    hide vanessa
    show hiflmc bowling surprised at right2
    show vanessa casual surprised at left2
    stop music fadeout 1.0
    play music hifllitecomedy
    "I pull back, raising an eyebrow."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Okay... not where I was expecting that to go.)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show vanessa casual basic at left2
    mcvan "Who am I like?"
    show vanessa casual happy
    va "My favorite character!"
    va "The protagonist of my favorite shoujo anime!"
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Her favorite what?)"
    show hiflmc bowling surprised at right2
    show vanessa casual happy at left2
    "My confusion must show, because she continues explaining."
    show vanessa casual smirk
    va "She’s this ordinary girl, who works at a boring office job, right?"
    va "And then she gets sucked through a portal and ends up in a total fantasy land."
    show vanessa casual happy
    va "Of course, when she gets there she meets a bunch of people and most of them fall in love with her..."
    "She’s talking animatedly, but with a little distance, I can see how her eyes are a little glazed over."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(She must be completely exhausted.)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show vanessa casual happy at left2
    mcvan "That sounds really cool, Vanessa."
    mcvan "Maybe you can tell me about it some more after you get some rest."
    show vanessa casual sad
    "Vanessa huffs."
    show vanessa casual angry
    va "I don’t need to rest, I’m fine."
    va "I can take care of myself."
    mcvan "I know you can."
    show hiflmc bowling sad
    mcvan "But I also know that you’re injured and you need to sleep it off."
    show vanessa casual sad
    "Vanessa looks like I just kicked her puppy."
    show hiflmc bowling sleep
    "I sigh."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Maybe talking about this will help tire her out?)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show vanessa casual sad at left2
    mcvan "Okay... tell me more about this character, then."
    mcvan "What’s she like?"
    show vanessa casual happy
    "Vanessa lights up."
    va "Okay well she’s totally a bishoujo, you know?"
    va "She’s pretty calm and practical, most of the time, but she can also be playful..."
    va "And she’s so kind-hearted."
    show hiflmc bowling smirk
    va "That’s why the other characters all fall for her."
    va "Even though some of them are really tsundere about it at first."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(I don’t really understand what she’s talking about, but it sounds like she’s complimenting me?)"
    hide hiflmc
    show hiflmc bowling surprised at right2
    show vanessa casual smirk at left2
    mcvan "And you think I’m like her?"
    va "Absolutely!"
    show vanessa casual happy
    va "I mean, she’s a little more deredere than you are, but she’s also a fictional character, so."
    show vanessa casual sleep
    "Vanessa yawns loudly."
    show hiflmc bowling happy
    mcvan "You can explain what that means tomorrow, after you get some sleep."
    va "Okay..."
    "She mumbles, already falling asleep."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(It’s amazing how she can go from being tough and cool to ridiculously cute in the blink of an eye...)"
    show hiflmc bowling basic at right2
    show vanessa casual sleep at left2
    "Until now, her confidence and the weight of her responsibilities have made her seem so mature and world-weary."
    "But looking at her like this, relaxed in her sleep, she looks much younger."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(Maybe even younger than me.)"
    hide hiflmc
    show hiflmc bowling blush at right2
    show vanessa casual sleep at left2
    "The fact that she’s letting me see this side of her gives me a serious case of the butterflies."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Okay, [genericfn], that’s enough staring at her in her sleep like a creeper.)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show vanessa casual sleep at left2
    "I look around the van instead, brimming with curiosity."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Maybe this is a chance to learn more about Vanessa?)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e7c1:
        "A. Look at the table.":
            $menuhideborder = False
            "My gaze lands on her table, which is the most disorganized part of the van."
            "It’s littered with stacks of small, pastel-colored books, boxes of soe candy labeled ‘pocky’, and empty cup ramen containers."
            "To the side, I spot a figurine as well. I can’t make out much more than a shock of pink hair, though."
        "B. Check out the weapon wall.":
            $menuhideborder = False
            show bg van_interior_night at bg with dissolve
            "My eyes drift toward the wall covered in weapons."
            "(Hard to believe she got so excited about my parents’ stuff when she has all of this.)"
            hide bg van_interior_night
        "C. Examine the decor.":
            $menuhideborder = False
            show hiflmc bowling sad at centre
            "The thought of looking through her stuff feels like an invasion of privacy..."
            "But looking at what she’s put out on display can’t hurt."
            "The van is all beige and black leathers and dark woods, except for the cherry blossom curtains and small throw-pillows."
            show hiflmc bowling surprised
            "(I wouldn’t have expected florals as part of her aesthetic, but they’re really pretty.)"
            show hiflmc bowling happy
            "(They definitely make it feel homier and less like a batcave on wheels, too.)"
    scene bg van_interior_loft_night at bg
    show hiflmc bowling sad at centre
    "My jaw cracks with the force of my yawn."
    "(It is really late, and today has been super intense.)"
    show hiflmc bowling basic
    "I look around for a pillow to use, but..."
    "The only big pillows that Vanessa isn’t currently sleeping on are a body pillow, and a throw pillow, both with cartoon girls on them."
    show hiflmc bowling sarcastic
    "(Yeah, no.)"
    show hiflmc bowling basic
    "(Guess I’m making due with the small cherry-blossom throw pillows.)"
    "I drag the two pillows to the backseat, careful not to disturb Vanessa."
    hide hiflmc
    "Despite the lack of a blanket, exhaustion knocks me out in minutes."
    scene bg van_interior_loft_lights at bg with fade
    show hiflmc bowling noglassessurprised at centre
    stop music fadeout 1.0
    play music hifleveryday
    "When I wake up, it takes me a few moments to remember where I am, and what happened the day before."
    scene bg van_interior_lights at bg with dissolve
    show vanessa casual basic at centre
    "Vanessa’s already awake, sharpening a small pile of weapons in the back of the van."
    show vanessa casual basic at left3
    show hiflmc bowling surprised at right3
    mcvan "How long have you been up?"
    show hiflmc bowling smirk
    "Vanessa smiles at me."
    va "Only an hour or so."
    va "I woke up at six and you were still out, so I thought I’d let you keep sleeping."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Way to go [genericfn], you slept in later than the injured girl.)"
    hide hiflmc
    show vanessa casual smirk at left3
    show hiflmc bowling basic at right3
    mcvan "Thanks, but shouldn’t you have slept a bit longer too?"
    show hiflmc bowling sad
    mcvan "Don’t you need more rest?"
    show vanessa casual basic
    "Vanessa shakes her head."
    va "That was a long night’s sleep, believe me."
    va "Lack of sleep is kind of an occupational hazard when your job involves hunting vampires."
    show hiflmc bowling basic
    mcvan "I guess that makes sense."
    show hiflmc bowling sad
    mcvan "Are you sure you’re ready to work already, though?"
    mcvan "You were pretty out of it last night."
    show vanessa casual surprised
    "Vanessa’s eyebrows shoot up."
    va "I was? What did I say?"
    va "I don’t remember much that happened after we left your house."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(Hmm... she was really cute last night, but I don’t want to embarrass her.)"
    show vanessa casual basic at left3
    show hiflmc bowling basic at right3
    mcvan "Oh, nothing much."
    mcvan "I just drove us here and got you into bed."
    show hiflmc bowling happy
    mcvan "And I got to know a little bit more about you."
    mcvan "Nothing bad, I promise."
    show vanessa casual sad
    "She gives me a long, skeptical look."
    "I try to look as innocent as possible."
    show vanessa casual sleep
    "She sighs and relents."
    show vanessa casual basic
    va "Well, that’s a relief."
    show hiflmc bowling surprised
    mcvan "So... now that you’re, you know, more coherent..."
    mcvan"I’m curious."
    show hiflmc bowling basic
    mcvan "What {i}do{/i} you do in your free time?"
    show vanessa casual sad
    "Vanessa frowns thoughtfully."
    va "The hunt keeps irregular hours, so I don’t have much spare time to begin with."
    show vanessa casual basic
    va "When I’m not working, though, I’m mostly training and keeping in shape."
    va "And doing equipment maintenance."
    "She gestures to the pile of weapons in front of her and the whetstone."
    show vanessa casual smirk
    va "You’d be surprised how much work goes into proper weapons upkeep."
    show vanessa casual basic
    va "After all, going into battle with faulty equipment is akin to being unarmed."
    show hiflmc bowling surprised
    "She says it like she’s quoting someone, but that same blazing intensity shines through."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(As much as I admire her dedication to her work, though...)"
    "(I want to see more of the girl from last night.)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e7c2:
        "A. Pick up the figurine.":
            $menuhideborder = False
            show vanessa casual basic at left3
            show hiflmc bowling happy at right3
            "I reach over and pick up the pink-haired figurine I spotted last night, presenting it with a grin."
            mcvan "What about her?"
        "B. Point out the books.":
            $menuhideborder = False
            show vanessa casual basic at left3
            show hiflmc bowling surprised at right3
            "I gesture to the stack of books on the table, which in the daylight are clearly those Japanese graphic novels."
            show hiflmc bowling basic
            mcvan "And those? Are they training manuals?"
        "C. Mention the body pillow.":
            $menuhideborder = False
            show vanessa casual basic at left3
            show hiflmc bowling surprised at right3
            "I nod to her bed."
            show hiflmc bowling happy
            mcvan "Where do body pillows with cartoon girls on them factor into that?"
    show vanessa casual blush at left3
    show hiflmc bowling happy at right3
    "Vanessa blushes deeply, but stares back at me defiantly."
    show vanessa casual angry
    va "Okay, yes, I like to relax with anime and manga when I have the time."
    va "Is that a problem?"
    show hiflmc bowling surprised
    mcvan "Not at all! I mean, I really don’t know anything about anime."
    mcvan "So I can hardly judge it."
    show hiflmc bowling happy
    mcvan "Besides, it’s kinda nice that you have something you like so much, aside from your work."
    show vanessa casual sad
    "She stares at me for a moment, wide-eyed."
    va "...Oh."
    mcvan "If you want to recommend me something, I’ll definitely check it out."
    show hiflmc bowling sarcastic
    mcvan "Once I, you know, have free time again."
    show hiflmc bowling basic
    va "Really?"
    show hiflmc bowling happy
    mcvan "Absolutely!"
    mcvan "If you like it, there’s got to be a reason, right?"
    show vanessa casual happy
    "A dazzling smile breaks slowly over her face."
    "It makes everything about her softer, warmer."
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Oh great, now I’m the one blushing.)"
    "(Her smile is just as lethal as any of her weapons.)"
    hide hiflmc
    show vanessa casual happy at left3
    show hiflmc bowling blush at right3
    va "Thanks for not judging me."
    mcvan "O-Of course."
    show hiflmc bowling happy
    mcvan "It was literally the least I could do."
    show vanessa casual basic
    "Vanessa shakes her head."
    show vanessa casual smirk
    va "Still. I appreciate it."
    va"I don’t get to talk about it much."
    mcvan "Well, I’m here to listen."
    mcvan "About anime, or anything else."
    va "Thanks, [genericfn]."
    show vanessa casual basic
    show hiflmc bowling basic
    "She looks back down at the forgotten pile of weapons."
    va "I really should finish sharpening these before we do anything else."
    show vanessa casual smirk
    va "Feel free to grab a granola bar if you’re hungry."
    show hiflmc bowling blush
    "As if on cue, my stomach growls loudly."
    "I decide to take her up on her suggestion as I wait for her to finish."
    scene bg van_interior_lights at bg with fade
    show hiflmc bowling basic at centre
    "By the time Vanessa’s done, I’m itching to talk to Razi, JD, and the others."
    mcvan "I think we should go in and talk to the rest of the group."
    mcvan "There’s safety in numbers, right?"
    hide hiflmc
    show vanessa casual basic at centre
    "Vanessa’s busy arming herself to the teeth, concealing more weapons than I can count like some kind of magician."
    "It almost looks like nothing happened yesterday, like she wasn’t badly injured."
    show vanessa casual angry
    va "Not if the numbers aren’t trustworthy."
    va "They’ve been lying to you the entire time you’ve known them."
    va "We can’t rely on them to have our backs, which makes them a liability, or worse, an active danger."
    show vanessa casual angry at left3
    show hiflmc bowling surprised at right3
    mcvan "They saved our lives! They all did."
    mcvan "Diego patched you up when you were injured!"
    show vanessa casual basic
    va "Wanting to trust someone doesn’t mean that it’s a good idea."
    show hiflmc bowling surprised
    mcvan "I don’t care if they’re supernatural creatures, or if they lied to me."
    show hiflmc bowling angry
    mcvan "They’re my friends, and I’m going to give them the benefit of the doubt."
    show vanessa casual sad
    va "You’re naïve."
    show vanessa casual angry
    va "You can never trust a supernatural creature."
    show hiflmc bowling sarcastic
    mcvan "Well maybe {i}you{/i} can’t, but I can and I do."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(I can’t believe she’s being so stubborn about this!)"
    show hiflmc bowling_cu sarcastic_cu
    "(Especially after they’ve all saved both of our lives.)"
    hide hiflmc
    show vanessa casual basic at left3
    show hiflmc bowling basic at right3
    mcvan "I’m going."
    mcvan "You can stay in here, since you’re so determined not to work with them."
    hide hiflmc
    hide vanessa
    show vanessa_s1_mini7 at bg with dissolve:
        zoom 0.4
    "I turn to leave, but I only make it a few steps before Vanessa catches my wrist."
    stop music fadeout 1.0
    play music hiflliteromance
    hide vanessa_s1_mini7
    show vanessa casual_cu sad_cu at vanessa_cu
    va "Wait..."
    "Her jaw is set stubbornly, but her eyes have softened a little."
    show vanessa casual_cu basic_cu
    va "If you’re this determined... I won’t let you go alone."
    show vanessa casual_cu angry_cu
    va "Who knows what will happen if I’m not there to protect you."
    "She looks ready to fight every supernatural in Havenfall for me."
    "Even though I disagree with her current choice of enemy, that protectiveness makes my heart race."
    scene bg bowling at bg with fade
    stop music fadeout 1.0
    play music hiflgetitdone
    show vanessa casual angry at left2
    show hiflmc casual basic at right2
    "We enter the bowling alley together after I stop by my house for a change of clothes, Vanessa hovering warily at my side."
    hide hiflmc
    hide vanessa
    show razi casual angry at left5 behind jd
    show jd casual angry at left2
    show diego glassesdoctor angry at right2 behind jd
    show mac cop angry at right5
    "Razi, JD, Diego, and Sheriff Hunt are all gathered, arguing with each other too intensely to notice us."
    hide razi
    hide diego
    hide mac
    show jd casual surprised at centre
    jd "Seriously, I can just erase her memories, problem solved."
    show jd casual surprised at right3
    show diego glassesdoctor basic at left3
    di "That’s not feasible."
    di "She’s interacted with us too much at this point."
    show diego glassesdoctor angry
    di "Wiping [genericfn]’s memories would likely cause extensive brain damage."
    hide diego
    hide jd
    show razi casual sad at centre
    ra "{i}Please{/i} don’t give my only good employee brain damage."
    show razi casual sad at left3
    show jd casual surprised at right3
    jd  "Hey!"
    hide jd
    hide razi
    show mac cop basic at centre
    Sheriff "We can figure out what to do about [genericfn] after we’ve dealt with the more pressing matter."
    show mac cop angry
    Sheriff "Namely, the vampires."
    hide mac
    show vanessa casual basic at left2
    show hiflmc casual basic at right2
    "Vanessa gives me a pointed ‘I told you so’ look, but I ignore her."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e7c3:
        "A. Be sarcastic.":
            $menuhideborder = False
            show hiflmc casual sarcastic at centre
            mcvan "Sorry to interrupt your whole 'talking about [genericfn] behind her back party..."
        "B. Ask for an explanation.":
            $menuhideborder = False
            show hiflmc casual basic at centre
            mcvan "An explanation sure would be nice, right about now."
        "C. Get angry.":
            $menuhideborder = False
            show hiflmc casual angry
            mcvan "What the hell is going on, here?!"
    hide hiflmc
    show razi casual basic at left5 behind jd
    show jd casual basic at left2
    show diego glassesdoctor basic at right2 behind jd
    show mac cop basic at right5
    "They all freeze and turn to me in unison."
    show razi casual sad
    show jd casual sad
    show diego glassesdoctor sad
    show mac cop sad
    "Their expressions range from indifferent to sheepish to outright guilty."
    hide razi
    hide jd
    hide diego
    hide mac
    show hiflmc casual sarcastic at centre
    mcvan "Setting aside the whole mindwiping thing for now, because I don’t even know how to begin to deal with that..."
    show hiflmc casual angry
    mcvan "Is everyone in this town a supernatural being?"
    show hiflmc casual sarcastic
    mcvan "Is Luce a witch?"
    show hiflmc casual angry
    mcvan "Or the mail carrier."
    show hiflmc casual angry
    mcvan "Let me guess: he’s Bigfoot?"
    show jd casual basic at left3
    show hiflmc casual sarcastic at right3
    jd "Actually, Bigfoot’s not real."
    show hiflmc casual angry
    "I glare at them."
    mcvan "{i}So{/i} not in the mood, JD."
    show jd casual sad
    jd "I'm serious though."
    hide jd
    hide hiflmc
    show razi casual basic at centre
    ra "It really is only the four of us."
    show razi casual basic at left3
    show hiflmc casual sarcastic at right3
    mcvan "And?"
    mcvan "Any other major secrets you’re hiding from me?"
    show hiflmc casual angry
    mcvan "Better just get it all out of the way now, while I’m already annoyed."
    show razi casual sad
    ra "No, that’s it. No more big secrets."
    show razi casual basic
    ra "What you choose to do now that you know... that’s up to you."
    hide hiflmc
    hide razi
    show razi casual basic at left5 behind jd
    show jd casual basic at left2
    show diego glassesdoctor basic at right2 behind jd
    show mac cop basic at right5
    "Suddenly everyone’s attention feels much more pointed."
    "Even Diego and Sheriff Hunt look to me expectantly."
    hide jd
    hide razi
    hide diego
    hide mac
    show vanessa casual sad at left3
    show hiflmc casual basic at right3
    stop music fadeout 1.0
    play music hiflsad
    "I look at Vanessa, expecting her to have a snide comment at the ready, but she’s frozen in place."
    "Her expression is completely shuttered, but I can see the tiniest flash of fear in her eyes."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu basic_cu at hiflmc_cu
    "(Oh.)"
    show hiflmc casual_cu surprised_cu
    "(Oh.)"
    "(They’re asking me to... choose? Between them and Vanessa?)"
    hide hiflmc
    show vanessa casual basic at left3
    show hiflmc casual basic at right3
    va "If you’d rather be with them, I won’t hold you against your will."
    va "You’ve known them longer and you’re probably more comfortable with them, anyway."
    show vanessa casual sad
    va "I couldn’t even... I couldn’t protect you yesterday."
    va "Not without their help."
    show vanessa casual basic
    show hiflmc casual surprised
    va "So I understand if you want to work with them instead, [genericfn]."
    "It clearly pains her to say all of this, despite the stoic front she’s putting up."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(Oh, Vanessa...)"
    $tobecontinued()
    scene bg hifltbc at bg
    with fade
    pause
    $ resets()
