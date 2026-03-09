label rion_season1_episode10:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_generic_office_on at bg with fade
    play music ecmupbeateveryday4

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "After I get the news, Rion, Enver and I rush back to HQ."

    show rion jacket pin angry at left3
    show ecmc jacket_v2 pin determined at right2
    "Rion and I go over everything we know in his office while Enver is at his desk, waiting for instructions."
    ri "I can't believe the F.D.I. thinks that a D.I.V.A.A employee could be behind the murders!"
    "Rion keeps his voice low, but his body is tense with anger."
    ri "All this time I may have been chasing one of our own. No wonder they were always one step ahead of me."
    "Rion groans in frustration."
    ri "The killer could be someone I know well. I could've been giving them case information this entire time!"

    show ecmc jacket_v2 sad
    mcrion "Rion..."
    hide rion
    hide ecmc
    $menuhideborder = True
    menu rions1e10c1:
        "A. Reassure him.":
            $menuhideborder = False
            show rion jacket pin angry at left3
            show ecmc jacket_v2 pin sad at right2
            mcrion "I doubt it."
            mcrion "I know you don't confide in many people. If any D.I.V.A.A got inside information it wasn't from you."

            show rion jacket sad
            ri "I guess you're right."

            show rion jacket angry
            ri "But, I still hate that the killer could have been under my nose this entire time."

        "B. Eliminate certain employees as suspects":
            $menuhideborder = False
            show rion jacket pin angry at left3
            show ecmc jacket_v2 pin determined at right2
            mcrion "Well, the only people you would have spoken in detail to would have been myself, Enver, Eko, and Dominick, right?"

            show rion jacket sad
            ri "I talk to Korin a bit as well, but I know I can trust her."
            mcrion "I doubt Dominick would be behind it, and I would trust Enver with my life."
            ri "And Eko definitely isn't the killer. It's not in her programming."

            show rion jacket sleep
            "Rion lets out a frustrated sigh."

            show rion jacket angry
            ri "Well, that's reassuring, but I still can't believe the killer could have been under my nose this entire time."

        "C. Get angry at the backstabber.":
            $menuhideborder = False
            show rion jacket pin angry at left3
            show ecmc jacket_v2 pin angry at right2
            mcrion "I still can't believe someone at D.I.V.A.A. would betray us like that!"
            mcrion "Whoever it is deserves to pay for tarnishing D.I.V.A.A.'s name."
            "I tense my fists in anger."
            mcrion "I've wanted to work here as long as I can remember and it grinds my gears that someone is taking advantage of working here!"
            ri "I just can't believe the killer could have been under my nose this entire time."

    show ecmc jacket_v2 determined
    mcrion "This definitely makes the case a lot riskier..."

    show ecmc jacket_v2 sad
    "I shiver slightly, suddenly feeling a little scared."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I knew working at D.I.V.A.A. would have its risks, but I definitely didn't expect something like this on my first case!)"
    hide ecmc

    show rion jacket pin angry at left3
    show ecmc jacket_v2 pin sad at right2:
        pause 0.1
        easein 0.4 right1 xoffset -20
    pause 0.2
    "I look around, even though Rion's office door is locked, and walk closer to him as I lower my voice."
    show ecmc jacket_v2 angry
    mcrion "Now we really can't trust anyone. I mean, we probably pass the killer everyday and don't even notice!"
    "Rion's cyber eye twitches slightly as he grips the edge of his desk."
    ri "Well thanks to you, now we know why the F.D.I. has taken over the investigation."
    ri "It all makes sense now."

    show ecmc jacket_v2 sad at right1:
        easein 0.4 xoffset 30 left1
    "I step even closer to Rion, my arm lightly brushing up against his, as I whimper nervously."
    mcrion "What do you think we should do?"

    show rion jacket basic
    ri "We can't let Gael and the F.D.I. know that we know the truth, but we can continue working behind the scenes."

    show rion jacket smirk
    ri "Now that we have this lead, it'll make our investigation a lot easier."
    ri "We already have plenty of info and several tools for the investigation, but we never had any real leads before."
    ri "Knowing the killer could be right here at D.I.V.A.A. narrows the field down."

    show ecmc jacket_v2 surprised
    mcrion "Who do you think at D.I.V.A.A. would buy tech from Skye and be involved in Blythe's art gallery?"

    show rion jacket sad
    ri "I'm not sure."

    hide ecmc
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    "Rion scrunches his face up in contemplation and I look up at him, my heart beating a little faster as I realize how close he is."

    show rion jacket_cu smirk_cu
    "Just then, Rion turns to look at me and my breath hitches as I stare back in his eyes which seem to be drinking me in."
    hide rion

    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(Crap! He caught me staring!)"
    hide ecmc

    show rion jacket pin smirk at left3
    show ecmc jacket_v2 pin blush embarrassed at left1:
        xoffset 30
    "I quickly pull my gaze away, feeling a blush heat my cheeks, and I hear Rion take a deep breath."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Was...was Rion staring at me as well?)"
    hide ecmc

    show rion jacket_cu embarrassed_cu blush_cu at rion_cu
    "I sneak a glance at Rion, but he's looking away from me, his own cheeks slightly pink."
    hide rion

    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin basic at left1:
        xoffset 30
    "A moment later, Rion continues talking as if nothing happened, but his face is still lightly flushed."
    ri "Skye's contact list will be a great resource, but it might still take a day or two for that information to be recovered."
    ri "Our next step should be to talk to Blythe. We can ask her to provide a list of the D.I.V.A.A. agents she's interacted with."

    show ecmc jacket_v2 determined
    mcrion "Would Blythe even know who was with D.I.V.A.A.? The killer may have just pretended to be a client."

    show rion jacket angry
    ri "That's also possible. We'll just need to hope for the best."
    mcrion "Well, we already know that Anton should be on that list. He was at the gallery and seemed to know Blythe."
    ri "Korin would be on that list too, but I really don't think she'll be involved."
    ri "We should also do a deep analysis of some of D.I.V.A.A.'s finances to see if anyone's books don't make sense."
    ri "The tech the killer has been using is extremely expensive and they've accumulated a lot over the years."
    ri "I always assumed the killer was wealthy, but it would make sense for him to have been manipulating their D.I.V.A.A. budget."

    show ecmc jacket_v2 angry
    mcrion "That's horrible! Not only do we have a killer in our midst, but we could also have a thief who was stealing D.I.V.A.A. money for his agenda!"

    show rion jacket sleep at left3:
        easein 0.4 xoffset -80
    "With a sigh, Rion takes a step back and I immediately miss his closeness."

    hide ecmc
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    ri "I'm going to contact Enver and get him to pull all the purchasing records of D.I.V.A.A. agents, then we should head to the gallery."

    scene bg ecm_sidewalk_day at bg with wiperightdissolve
    stop music
    play music ecmcalmeveryday3

    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin angry at right3
    "After Rion contacts Enver, him and I head towards the art gallery to talk to Blythe."
    "(Rion's been quiet since we left HQ. Maybe I should distract him with some small talk?)"
    hide rion
    hide ecmc

    $menuhideborder = True
    menu rions1e10c2:
        "A. Talk about the weather.":
            $menuhideborder = False
            show rion jacket pin basic at left3
            show ecmc jacket_v2 pin smile at right3
            mcrion "So...it's a nice day today."
            mcrion "Perfect for walking."
            "I mentally facepalm but Rion doesn't even seem to be listening to me."

        "B. Ask about new restaurants.":
            $menuhideborder = False
            show rion jacket pin basic at left3
            show ecmc jacket_v2 pin smile at right3
            mcrion "So, have you tried any new restaurants lately?"
            ri "No."
            "Rion's answer is short and clipped, he doesn't even look at me."

        "C. Tell Rion about some new tech I found.":
            $menuhideborder = False
            show rion jacket pin basic at left3
            show ecmc jacket_v2 pin basic at right3
            mcrion "I found some really cool tech recently, but I haven't had a chance to look at it properly yet."

            show ecmc jacket_v2 smile
            mcrion "But I think it's a part from those discontinued robots a few years ago! The CLX models."
            "Rion lets out a grunt, but he doesn't even look at me."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(That didn't work. Maybe I should try bringing up soccer again?)"
    hide ecmc

    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin smile at right3
    mcrion "Did you catch the game the other day?"

    show ecmc jacket_v2 sad
    mcrion "It's a pity the invaders lost."
    "Rion shrugs impassively."
    ri "They always lose."

    hide ecmc
    hide rion
    show rion jacket_cu basic_cu at rion_cu
    "I sneak a glance at Rion, but he's staring straight ahead as if hyper-focused on the pavement."
    hide rion

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Rion seems so deep in thought.)"

    show ecmc jacket_v2_cu surprised_cu
    "(Is he thinking about the case, or is it something else?)"
    hide ecmc

    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin basic at right3
    "I sneak another glance at Rion, but he's still ignoring me, his footsteps a little heavy on the payment as he briskly walks towards the gallery."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(I wish Rion would at least talk to me about {i}something{/i}!)"

    show ecmc jacket_v2_cu sad_cu
    "(This whole situation is so intense and his silence isn't helping!)"

    scene bg ecm_sidewalk_day at bg
    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin surprised at right3
    with wiperightdissolve
    stop music
    play music ecmtense3
    "Rion and I reach the gallery, but to our surprise, it's closed."
    mcrion "This is odd. The gallery should be open at this time."

    show rion jacket angry
    ri "You're right. We need to get inside and take a look."
    mcrion "Are you sure that's a good idea? Maybe they're closed for a reason?"
    mcrion "Like, maybe Blythe is sick or they're doing renovations?"
    ri "You could be right, but we should still check it out to be sure."
    mcrion "But we don't have a warrant!"
    ri "[genericfn], we're running out of time."

    show rion jacket surprised
    show ecmc jacket_v2 sad
    ri "After the news we got earlier, we can't afford any delays."
    ri "The killer already has insider information and will already know the F.D.I. is now on the case."

    show rion jacket angry
    ri "If we delay our investigation any further, we'll just be giving them more time to get away and we'll never be able to track them down."
    mcrion "Well...I guess you do have a point..."

    show ecmc jacket_v2 surprised
    mcrion "But we're breaking a lot of protocols, Rion. We could get in trouble with D.I.V.A.A. {i}and{/i} the F.D.I.!"

    show rion jacket smirk
    ri "If we get in trouble, [genericfn], I'll take the fall."
    "Rion gives me a small, reassuring smile."
    ri "My methods aren't exactly liked by everyone, but I always get results with no major collateral damage."
    ri "Both Dominick and Gael know how I work. They don't always like it, but they tend to turn a blind eye to it when I deliver."

    show ecmc jacket_v2 determined
    "I hesitate for a moment, then nod."
    mcrion "Alright. Let's break in."

    show rion jacket smile
    "Rion grins at me, then pulls his omni-pick out of his bag and quickly opens the gallery door."

    scene bg ecm_artgallery_day at bg with wiperightdissolve

    "I follow him inside, my heart thumping in my chest."

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I hope no one's here! I really don't want to get caught...)"
    hide ecmc

    show rion jacket pin basic at left3
    show ecmc jacket_v2 pin determined at right3
    "Rion and I wander through the gallery, taking everything in."
    mcrion "Nothing seems out of place. Those sculptures are in the exact same spot they were last time."

    show rion jacket angry
    "I look at Rion whose cyber eye is frantically scanning around the room."
    ri "You're right. I also can't see anything broken or damaged."
    ri "Let's take a better look to see if we've missed something more minor."

    show ecmc jacket_v2 headset determined with dissolve
    "I put my ARCware on and follow Rion to the sculptures."

    show ecmc jacket_v2 determined at right3:
        easein 0.4 centre
    "I start to look around the sculptures, and every now and then my arm brushes against Rion's."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu headset_cu surprised_cu at ecmc_cu
    "I try not to jolt at the contact, but every time we brush against one another, I can't help but feel sparks."
    hide ecmc

    show rion jacket_cu angry_cu at rion_cu
    "My mind races with questions about how he feels. I hope he doesn't know that being near him makes my heart pound."
    ri "Alright, there's nothing to see here."
    hide rion

    show rion jacket pin angry at left3
    show ecmc jacket_v2 pin headset surprised at centre
    ri "Let's go look at the paintings."

    show rion jacket basic at left3:
        pause 0.1
        easein 0.4 left1
    show ecmc jacket_v2 determined at centre:
        pause 0.1
        easein 0.4 right2
    "I follow Rion over to the wall and start inspecting the paintings, checking to see if anything has been moved."

    show rion jacket basic at left1:
        easein 0.4 centre xoffset 30
    "Rion reaches over me to show me how to lift the frames without damaging the painting, and our hands touch."

    show rion jacket surprised
    show ecmc jacket_v2 blush embarrassed
    "I blush at the contact, and Rion looks at me in confusion."
    ri "Is everything okay? Are you feeling a bit warm?"

    show ecmc jacket_v2 surprised
    mcrion "Oh, no! I'm fine!"

    show ecmc jacket_v2 embarrassed
    mcrion "Sorry, I was just...thinking about something."

    show rion jacket angry
    ri "Well, make sure you stay focused."

    show rion jacket angry at left1:
        ease 0.4 xoffset 0
    "Rion takes a step back and looks around the gallery."
    ri "Let's go check out the back doors."

    show ecmc jacket_v2 sad -blush
    "I follow Rion to the back, my stomach twisting in nerves and not just from the case."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu headset_cu angry_cu at ecmc_cu
    "(I need to stay focused...I can't let my feelings for Rion distract me.)"
    hide ecmc

    show rion jacket pin angry at left1
    show ecmc jacket_v2 pin headset basic at right2:
        pause 0.1
        easein 0.4 right4
    "I head over to another door and take a closer look."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu headset_cu surprised_cu at ecmc_cu
    "(Hmm...this is strange.)"
    hide ecmc

    show rion jacket pin angry at left1
    show ecmc jacket_v2 pin headset surprised at right4
    mcrion "Rion, I think I found something!"

    show rion jacket angry at left1:
        pause 0.1
        ease 0.4 right1
    "Rion walks up behind me and I try not to shiver at the way his body brushes up against mine."

    show rion jacket surprised
    ri "What have you got there?"

    show ecmc jacket_v2 determined
    mcrion "This lock is broken."
    ri "Hmm... That's interesting. Judging by the markings, it was only broken recently."

    show rion jacket angry
    "Rion glances down and furrows his brow."
    ri "There are scuff marks all around the door. It looks like there was some kind of struggle."
    mcrion "What do you think happened?"
    ri "Based on the fact that the gallery is shut and there's no sign of Blythe, I'm going to assume that she's been kidnapped."

    show ecmc jacket_v2 surprised
    mcrion "What should we do?! We don't even have a warrant! We shouldn't be in here!"

    hide ecmc
    hide rion
    show rion jacket_cu smile_cu at rion_cu
    "I start to panic, so Rion takes my hand and gives it a reassuring squeeze."
    ri "Relax, [genericfn]. Let me handle it."

    show rion jacket_cu smirk_cu
    ri "I'll put in an anonymous missing person's report on Blythe and mention that the art gallery was the last place she was seen."
    ri "After I do that, we should get out of here and head back to HQ."

    scene bg ecm_generic_office_on at bg with wiperightdissolve
    stop music
    play music ecmcalmeveryday2

    "Rion and I head back to HQ and go straight to Rion's office."

    show rion jacket pin basic at left3
    show ecmc nojacket_v2 pin basic at right3
    "Enver managed to pull all the purchasing records for us and he sent Rion a message..."
    "Saying that all the information was sent to Rion's personal terminal."

    show rion jacket smirk
    ri "Alright, thanks to Enver we have the purchasing records."
    ri "Can you use your ARCware to connect to my terminal so we can both access the data?"

    show ecmc nojacket_v2 determined with dissolve
    "I nod and put my ARCware on, then I connect it directly to Rion's terminal."
    mcrion "I'm in."

    show rion jacket basic
    ri "Let's see what we can find."
    "Rion and I both frantically start digging through the purchasing records."

    show rion jacket sad
    "After several minutes, Rion lets out a sigh."
    ri "This is insane. There's so much data to sift through!"
    mcrion "Don't complain. This was your idea!"

    show rion jacket basic
    ri "Well, do you have any better ideas?"

    show ecmc nojacket_v2 sad
    mcrion "Well...no."

    show rion jacket smirk
    "Rion smirks at me, then we both turn our attention back to sorting through the data."

    show rion jacket basic
    show ecmc nojacket_v2 determined
    ri "If Blythe really has been kidnapped then the stakes have just gotten much higher."

    show rion jacket angry
    ri "We need to find her as soon as possible!"

    show ecmc nojacket_v2 angry
    mcrion "I'm going as fast as I can!"
    ri "I've been trying to come up with ways to speed things up, but I'm drawing blanks."
    ri "Do you have any scrappier-genius ideas you can pull to make things go faster?"

    show ecmc nojacket_v2 smile
    "I scoff and look at Rion with a smirk."
    mcrion " Scrappers are experts with hardware, not software."

    show rion jacket sad
    ri "Ugh. I feel like we've barely made a dent."

    show rion jacket smirk
    ri "Maybe we should get Eko involved. Her processing abilities are superhuman."

    show ecmc nojacket_v2 surprised
    mcrion "Do you think that's a good idea?"
    mcrion "I know you trust Eko, but if we get her to help we'll have to explain to her what we're doing."

    show rion jacket sad
    ri "You're right."

    show ecmc nojacket_v2 determined
    ri "For now, we best keep the D.I.V.A.A. double agent info as secret as possible."

    scene bg ecm_generic_office_night_on at bg with wiperightdissolve
    "Several hours later, it's past closing time and most of the other employees have already left for the day."

    show rion jacket pin basic at left3
    show ecmc nojacket_v1 pin headset sad at right3
    mcrion "Ugh, I feel like we haven't made any progress! There's still so much data to parse!"
    ri " This is ridiculous. I knew there'd be a lot of data, but I wasn't expecting this..."

    show rion jacket sleep
    "Rion sighs and leans back in his chair."

    show rion jacket sad
    ri "I need a break."

    show rion jacket smile
    "Rion turns his head to give me a tired smile."
    ri "We've just worked non stop for the past few hours and I'm starving."
    ri "Time for takeout. You in?"

    show ecmc nojacket_v1 surprised
    "Before I can respond, my stomach grumbles."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu headset_cu sad_cu at ecmc_cu
    "(I'm definitely hungry. Rion's right...it's been hours since we ate!)"
    hide ecmc

    show rion jacket pin smile at left3
    show ecmc nojacket_v1 pin headset sad at right3
    mcrion "Oh...it's okay. I don't want to put you out."

    show rion jacket smirk
    show ecmc nojacket_v1 surprised
    ri "Don't be silly, [genericfn]. I'm hungry too."

    show rion jacket smile
    ri "Besides, I want to treat you. I know you've been stressed."
    mcrion "No, I haven't! This case has taken some unexpected turns, but I'm not stressed out."

    show rion jacket smirk
    "Rion smirks at me and raises an eyebrow."
    ri "I know you well enough to know when you're stressed, [genericfn]."

    show ecmc nojacket_v1 embarrassed
    ri "I saw the way you were shuffling awkwardly in my office earlier when you didn't know how to handle the situation."
    ri "And you've been constantly wringing your hands in frustration."
    "I blush and look away."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
    "(I didn't realize Rion was so observant.)"
    hide ecmc

    show rion jacket_cu smile_cu at rion_cu
    ri "Come on, [genericfn]."
    "I look back up at Rion, who's smiling reassuringly at me."
    ri "Let me treat you. You've definitely earned it."
    hide rion

    $menuhideborder = True
    menu rions1e10c3:
        "A. Let Rion treat you to take out." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show rion jacket pin smile at left3
            show ecmc nojacket_v1 pin headset smile at right3
            mcrion "That sounds great, Rion. I could really use some food."
            ri "I knew you couldn't resist."

            show rion jacket smirk
            show ecmc nojacket_v1 determined
            "Rion smirks at me and I roll my eyes playfully."
            mcrion "It would be stupid of me to turn down free food when I haven't eaten all day! I'm starving."
            ri "I bet you I can guess your order."

            show ecmc nojacket_v1 angry
            mcrion "Please. The menu for this place is huge! You'll never guess."

            show ecmc nojacket_v1 smile
            mcrion "I'll give you three tries."

            show rion jacket angry
            "Rion scrunches his face up a bit and chews his bottom lip."
            ri "Let's see..."
            ri "Maybe the pop burger and fries?"
            mcrion "Nope. Strike one."

            show rion jacket surprised
            ri "Pizza?"
            mcrion "Nope. Strike two."
            "I smirk at Rion and poke my tongue out."
            mcrion "You're really doing badly at this for someone who was so confident!"

            show rion jacket smile
            ri "Hey, I still have one more chance!"

            show rion jacket angry
            "Rion furrows his brow in concentration, then he snaps his gaze back to mine."

            show rion jacket smile
            ri "Alright, last attempt."
            ri "Your order is a chicken burrito with a side of tortilla chips {i}and{/i} guacamole and you're going to ask for an extra scoop of guac."

            show ecmc nojacket_v1 surprised
            "I widen my eyes and stare at him."
            mcrion "That's completely correct..."
            mcrion "How did you guess?"

            show rion jacket smirk
            ri "Honestly, I cheated."
            "Rion winks at me as he reaches for his holophone."
            ri "I've noticed you ordering that a couple of times when we've been working together."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
            "(Rion's been paying that much attention to me?!)"
            hide ecmc

            show rion jacket pin smirk at left3
            show ecmc nojacket_v1 pin headset basic at right3
            "Rion places the food order on his phone, then turns back to his computer."
            ri "The food should be here soon. We should keep working in the meantime."

            show rion jacket basic
            "By the time the food arrives, Rion and I still haven't made much progress."

            show rion jacket smile
            "Rion goes to meet the delivery driver and he returns a few moments later with a huge paper bag in his hands."
            "Rion sets the bag down on his desk and starts to take out the containers."

            show ecmc nojacket_v1 surprised
            mcrion "Is there going to be enough room?"

            show rion jacket smirk
            ri "We'll make room."
            "Rion does his best to spread everything out on his desk, but it's far too crowded."

            show ecmc nojacket_v1 sad
            mcrion "This isn't going to work."

            show ecmc nojacket_v1 basic
            mcrion "I'm going to put my containers on the floor and just eat there."

            show rion jacket surprised
            ri "No, you don't have to do that!"

            show ecmc nojacket_v1 smile
            mcrion "It's fine, Rion. I really don't mind."

            show rion jacket basic at left3:
                pause 0.3
                easein 0.4 left1
                easein 0.4 yoffset 80
            show ecmc nojacket_v1 smile at right3:
                pause 0.1
                easein 0.4 yoffset 80
            "I pick my containers up and head over to the floor. Just as I'm setting up, Rion joins me, placing his containers beside mine."

            show ecmc nojacket_v1 surprised
            mcrion "You don't have to join me!"

            show rion jacket smile
            ri "I want to, [genericfn]."

            show ecmc nojacket_v1 basic
            ri "I offered to get you takeout because I wanted to share a meal with you."
            ri "It's not the same if I'm sitting behind a desk!"

            show ecmc nojacket_v1 smile
            "Rion smiles at me and my heart beats a little faster as I smile back at him, shyly."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu headset_cu smile_cu at ecmc_cu
            "(That's sweet...)"
            hide ecmc

            show rion jacket pin smile at left1:
                yoffset 80
            show ecmc nojacket_v1 pin headset smile at right3:
                yoffset 80
            "Rion sits down cross-legged beside me and we dig into the food."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu headset_cu smile_cu at ecmc_cu
            "(Even though we're just eating food on the ground, there's something rather...{i}intimate{/i} about this.)"
            hide ecmc

            show rion jacket pin smile at left1:
                yoffset 80
            show ecmc nojacket_v1 pin headset smile at right3:
                yoffset 80
            ri "This is definitely what I needed."
            mcrion "Thanks for the food, Rion."

            show ecmc nojacket_v1 surprised
            "I look around for some extra sauce when Rion suddenly holds some out to me."

            show rion jacket smirk
            ri "Looking for this? I made sure we got extra."

            show ecmc nojacket_v1 smile
            mcrion "Thank you!"
            "I take a bite of my burrito and some sauce spills down my front."

            show ecmc nojacket_v1 surprised
            mcrion "Ugh!"
            "I look around for a napkin when Rion suddenly holds one out to me."

            show rion jacket smile
            ri "Here. I think you could use this."

            show ecmc nojacket_v1 smile
            "I take it gratefully and smile at him."
            mcrion "Someone's organized."
            ri "I made sure I was prepared when I came to join you."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu headset_cu smile_cu at ecmc_cu
            "(It's sweet how thoughtful Rion is. I'm not sure that he's even trying!)"
            hide ecmc

            show rion jacket pin smile at left1:
                yoffset 80
            show ecmc nojacket_v1 pin headset smile at right3:
                yoffset 80
            mcrion "Rion, thank you."

            show rion jacket surprised
            "Rion furrows his brow in confusion."
            ri "What for?"

            show ecmc nojacket_v1 surprised
            mcrion "Well...for dinner. And for...um...being so thoughtful?"

            show ecmc nojacket_v1 embarrassed
            "Even as I speak, I can tell how awkward that all sounds."

            show rion jacket smile
            ri "Oh, it's nothing. I just like to be prepared."
            "My heart sinks as I nod."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu headset_cu angry_cu at ecmc_cu
            "(I meant to compliment Rion, but I completely glitched things up!)"
            hide ecmc

            show rion jacket pin surprised at left1:
                yoffset 80
            show ecmc nojacket_v1 pin headset surprised at right3:
                yoffset 80
            ri "[genericfn]?"

            hide ecmc
            hide rion
            show rion jacket_cu smile_cu at rion_cu
            "I look up at Rion who gives me a reassuring smile."
            ri "I wanted to tell you that you've been doing a great job on this case so far."
            ri "This is a very difficult situation to be in, especially for a rookie, but you're handling it really well."
            hide rion

            show rion jacket pin smile at left1:
                yoffset 80
            show ecmc nojacket_v1 pin headset smile at right3:
                yoffset 80
            "I grin at Rion, instantly feeling much better."
            mcrion "Thanks, Rion. That means a lot coming from you."
            "Rion gives me a brief smile, then tears his gaze away and looks down at the food."
            ri "Come on. We should finish this off then get stuck back into those records."
        "B. Go hungry":
            $menuhideborder = False

            show rion jacket pin smirk at left3
            show ecmc nojacket_v1 pin headset smile at right3
            mcrion "I'm really fine, Rion. We should finish digging through these records."

            show rion jacket sleep
            "Rion lets out an annoyed huff and leans back towards his computer."

            show rion jacket basic
            ri "Fine, [genericfn], but whenever you're ready to eat dinner like a normal person, you just have to ask."

            hide rion
            hide ecmc
            show ecmc nojacket_v1_cu headset_cu sad_cu at ecmc_cu
            "(Maybe I should have said yes...it's going to be difficult trying to concentrate when I'm so hungry!)"

    hide rion
    hide ecmc
    "The next few hours pass by, and now it's almost midnight."

    show rion jacket pin basic at left1
    show ecmc nojacket_v1 pin headset basic at right2
    ri "It's really late. You should go home and rest up before tomorrow."

    show ecmc nojacket_v1 determined
    mcrion "No, Rion. If you're staying, then I'm staying with you."

    show rion jacket smirk
    ri "Alright, but I won't hold it against you if you leave."

    show ecmc nojacket_v1 sad
    "I nod and turn my attention back to the records, but I feel my eyelids start to droop."

    hide rion
    hide ecmc
    show ecmc nojacket_v1_cu headset_cu sad_cu at ecmc_cu
    "(I'm so tired.)"
    "My eyes get heavier as I start to lean down towards my desk."
    "(Maybe I should rest my eyes. It'll just be five minutes...)"
    hide ecmc

    scene bg ecm_generic_office_on at bg with clockwise_wipe

    "I'm not sure how long I'm out, but I suddenly wake up with a jolt."

    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(Huh?! What?!)"
    "I self-consciously wipe some of the dried drool from the side of my mouth and take a look around."
    "(Hmm...the lights are still on.)"
    "I glance down and realize that Rion's jacket is draped over me as a blanket."

    show ecmc nojacket_v1_cu smile_cu
    "(That's so sweet!)"

    show ecmc nojacket_v1_cu surprised_cu
    "I look around the room again, feeling confused."
    "(I don't think Rion left. The lights are on and I have his jacket...but where is he?!)"
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

