label van_season1_episode11:

    $tbc = False
    scene bg heroine_home_lights at bg
    play music hiflgetitdone
    pause

    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show hiflmc casual basic at centre
    "When we get back to my house, I make us each a cup of hot chocolate just to have something to do with my hands."
    mcvan "So what's the next step here?"
    show hiflmc casual sad
    mcvan "What do we do now?"
    show hiflmc casual sad at right3
    show vanessa casual basic at left3
    va "Did she say anything about what she's planning or what she wants from you?"
    show hiflmc casual surprised
    "I facepalm."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(In all the commotion, I almost forgot about the whole Dracula thing.)"
    hide hiflmc
    show hiflmc casual sarcastic at right3
    show vanessa casual basic at left3
    mcvan "Yeah, apparently that letter we found was from my ancestor, who was engaged to Dracula, but ran away before he could marry her."
    show hiflmc casual angry
    mcvan "And now Li needs me for {i}something{/i} so that she can resurrect him."
    show vanessa casual surprised
    "Vanessa stares at me with blank shock."
    show vanessa casual sad
    va "Sorry, could you repeat that?"
    va "I thought I heard you say she needs you to resurrect Dracula."
    show hiflmc casual basic
    mcvan "... Yeah, that's pretty much it."
    show vanessa casual angry
    va "But that makes no sense!"
    va "Dracula is dead!"
    show vanessa casual surprised
    va "You can't resurrect dead vampires--it's not possible."
    show hiflmc casual sarcastic
    mcvan "Well, Li sure seems to think it is."
    show vanessa casual angry
    "Vanessa swears."
    show vanessa casual sleep
    "She closes her eyes, rubbing her temples as she thinks."
    show vanessa casual basic
    va "I have to report this to Headquarters."
    va "They need to know about this, and maybe they'll have some answers."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Headquarters?)"
    "(Like, the bosses that discourage working with other people?)"
    hide hiflmc
    show hiflmc casual sad at left3
    show vanessa casual basic at right3
    "I'm wary, but ultimately Vanessa is right--if anyone needs to know about this, it's the Helsing Order."
    va "We'll need to go back to my van--I have a secure private WIFI connection there."
    scene bg mc_house_ext_night at bg with dissolve
    show vanessa casual basic at left3
    show hiflmc casual sad at right3
    "I'm still feeling jumpy as we head back to her van, gripping a stake tightly in my hand."
    "Just in case."
    hide vanessa
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(It's probably going to be a while berfore I can go outside at night without worrying about getting jumped by vampires.)"
    show vanessa casual basic at left3
    show hiflmc casual basic at right3
    "I stay close to Vanessa's side and she gives me a reassuring glance."
    show vanessa casual angry
    va "I won't let her get you again, [genericfn]."
    show vanessa casual angry at left2
    show hiflmc casual sad at right2
    "I huddle even closer, comforted just by her nearness."
    scene bg van_interior_lights at bg with wipedown
    show vanessa casual basic at centre
    "Inside the van, Vanessa starts fiddling with the monitors, signing into a million different identification measures."
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    "I take a seat on the cushions by the table so I can watch her."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e11c1:
        "A. Nice setup.":
            $menuhideborder = False
            show hiflmc casual surprised at right3
            show vanessa casual basic at left3
            mcvan "That's a pretty cool setup you have."
            va "I suppose."
            va "Mostly I just use it for research or contacting Headquarters."
            show hiflmc casual happy
            mcvan "Really? You never use any of these monitors to watch TV?"
            show vanessa casual blush
            "Vanessa avoids my eyes, a faint blush appearing on her cheeks."
            va "I don't know what you're talking about."
        "B. A rolling chair?":
            $menuhideborder = False
            show hiflmc casual surprised at right3
            show vanessa casual basic at left3
            mcvan "Wait, you have a rolling chair in your van?"
            show vanessa casual surprised
            "Vanessa raises an eyebrow at me."
            va "Yes?"
            show vanessa casual smirk
            va "It has footstops to keep it still, it's not like it just rolls around back here when I drive."
            hide vanessa
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(That still seems really Extra to me...)"
        "C. This van is huge.":
            $menuhideborder = False
            show hiflmc casual surprised at right3
            show vanessa casual basic at left3
            mcvan "I can't get over how huge your van really is."
            mcvan "I mean you've got a whole computer area and everything."
            show hiflmc casual basic
            mcvan "You'd never think it, from how small your 'bedroom' is."
            "Vanessa shrugs."
            va "It's my home for all intents and purposes."
            show vanessa casual sad
            va "I think I'd get claustrophobic if it were any smaller than this."

    hide hiflmc
    hide vanessa
    show vanessa casual basic at centre
    "Vanessa finally finishes with the security procedures."
    show vanessa casual sad
    "She gives me an apologetic glance."
    va "I'm going to have to wear headphones for this--it's confidential."
    show vanessa casual sad at left3
    show hiflmc casual basic at right3
    mcvan "That's totally fine, I understand."
    mcvan "I'll just... watch, I guess."
    show vanessa casual smirk
    "Vanessa smiles at me and puts on her headphones, turning towards one of the monitors."
    show vanessa casual basic
    "From this angle, I can't see who's on screen."
    "Still, it's a good opportunity to watch Vanessa in her element, doing a part of her job I haven't really seen before."
    show vanessa casual angry
    "As soon as the call starts, there's an immediate shift in her body language."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(It's like she's a totally different person from who she iss when we're alone, or even when she's interacting with the rest of the gang.)"
    hide hiflmc
    show vanessa casual basic at centre
    "Instead, she's stiff as a board, any trace of exhaustion or emotion hidden away as she makes her report."
    hide vanessa
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(I just want to give her a hug and let her know that being herself is more than enough.)"
    "(She doesn't have to be some robotic superwoman who never sleeps and has no weaknesses.)"
    show hiflmc casual_cu happy_cu
    "(She's already amazing just the way she is.)"
    hide hiflmc
    show hiflmc casual surprised at centre
    "The thought registers, and I blink."
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(I thought I was just attracted to her, but...)"
    "(Could I have developed real feelings for her without even realizing it?)"
    hide hiflmc
    show vanessa casual sleep
    "Vanessa ends the call, her posture immediately relaxing."
    show vanessa casual sad
    "I must still be staring at her, because she gives me a weird look."
    va "What? Is something wrong?"
    show vanessa casual sad at left3
    show hiflmc casual blush at right3
    "I shake my head quickly."
    mcvan "No. Nope. Everything is fine."
    scene bg heroine_home_lights at bg with clockwise_wipe
    stop music fadeout 1.0
    play music vanessa
    "Before we get back to planning, we head back into the house and get comfy on the couch."
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    mcvan "Soo..."
    mcvan "What did they say?"
    show vanessa casual sad
    "Vanessa frowns, looking troubled."
    va "They were just as shocked as I was about the Dracula development."
    show vanessa casual angry
    va "It {i}really{/i} should not be possible to resurrect a vampire that's been dusted already."
    show vanessa casual sad
    va "So this whole situation--and our lack of information about it--is unsettling to say the least."
    show hiflmc casual sad
    mcvan "I can imagine."
    show hiflmc casual basic
    mcvan "So there's no research on it or anything?"
    mcvan "It's really never happened before?"
    show vanessa casual basic
    va "As far as I know, no."
    show hiflmc casual surprised
    va "There might be some research on it, but none they had readily available during the conference."
    show hiflmc casual basic
    va "But don't worry."
    show vanessa casual smirk
    va "HQ has access to a lot more resources and manpower than I do."
    va "If anyone can dig up something useful, it's them."
    mcvan "If you say so, then I trust you."
    show hiflmc casual surprised
    mcvan "Have they ever encountered Li before?"
    mcvan "Was there anything they could tell us about her?"
    mcvan "She keeps mentioning how she's faced Helsings before."
    show vanessa casual sad
    va "Not as far as I know."
    show vanessa casual basic
    va "They didn't have much pertinent information about her."
    show vanessa casual smirk
    show hiflmc casual basic
    "Vanessa smirks proudly at me."
    va "Or at least, they didn't have much pertinent information that you hadn't already discovered."
    show hiflmc casual blush
    "I blush, ducking my head."
    mcvan "I didn't really do anything except get attacked and captured."
    show hiflmc casual sarcastic
    mcvan "I'm not sure that's anything to be proud of."
    show vanessa casual surprised
    va "Are you kidding?"
    va "You {i}survived{/i} getting attacked and captured."
    show vanessa casual smirk
    va "And you got away with new information that gives us an advantage over her."
    va "You should be extremely proud of yourself."
    show vanessa casual happy
    va "I know I'm proud of you."
    show hiflmc casual sad
    "I hesitate before asking the next question, biting my lip."
    show vanessa casual basic
    mcvan "And... your orders?"
    mcvan "What did they tell you to do now?"
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(Please don't say they told you to leave.)"
    "(I don't think I could handle this without you.)"
    hide hiflmc
    show vanessa casual sad at left3
    show hiflmc casual basic at right3
    "Vanessa's brow furrows unhappily."
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(I wish I knew what happened in that conversation to make her look like that...)"
    hide hiflmc
    show vanessa casual basic at left3
    show hiflmc casual basic at right3
    va "They're still making a decision."
    stop music fadeout 1.0
    play music hiflliteromance
    va "But in the meantime, I'll keep doing exactly what I have been: protecting you."
    show vanessa casual angry
    va "To my dying breath, if that's what it takes."
    show hiflmc casual surprised
    mcvan "Vanessa..."
    va "I will not fail you again, [genericfn]."
    show hiflmc casual basic
    show vanessa casual sad
    va "Li getting her hands on you..."
    show vanessa casual angry
    va "I can't let it happen again."
    va "I won't."
    show hiflmc casual surprised
    va "You're too important."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(I don't know what to say...)"
    "(I don't want her to die for me, but the fact she's willing to, that she has such strong feelings about it...)"
    show hiflmc casual_cu blush_cu
    "(I can't help but think that maybe she cares about me as much as I care about her.)"
    hide hiflmc
    show hiflmc casual surprised at right3
    show vanessa casual basic at left3
    "I search for the right words to respond with, but I'm at a loss."
    hide hiflmc
    show vanessa casual surprised at centre
    "The silent stretches on for long enought that Vanessa seems to realize exactly what she said."
    show vanessa casual blush
    "She blushes a deep red."
    va "Actually, you know what?"
    va "I'm gonna go. Um. Shower?"
    va "Yeah. Showering is a good plan."
    va "I'm going to go do that."
    "She standsa jerkily, so different from her usual effortless grace."
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Wait, no.)"
    show hiflmc casual_cu sad_cu
    "(I don't want her to leave yet...)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e11c2:
        "A. I need you, Vanessa." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc casual surprised at centre
            mcvan "Wait!"
            show hiflmc casual surprised at right3
            show vanessa casual blush at left3
            "Vanessa turns to me, still visbily flustered."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(Quick, [genericfn], think of some kind of reason for her to stay!)"
            hide hiflmc
            show hiflmc casual surprised at right3
            show vanessa casual blush at left3
            stop music fadeout 1.0
            play music hifllitecomedy
            mcvan "There's a... bag of coffee on top of the fridge that I need help reaching."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(Oh my god, really?)"
            show hiflmc casual_cu sad_cu
            "(She's going to see right through that.)"
            show hiflmc casual blush at right3
            show vanessa casual blush at left3
            mcvan "I'm... craving it right now."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(This is it. This is how I die.)"
            show hiflmc casual_cu sarcastic_cu
            "(Not being murdered by a vampire, but from the sheer mortification of my complete inability to flirt with the girl I like.)"
            hide hiflmc
            show vanessa casaul smirk at centre
            va "No problem! I can totally do that."
            show bg heroine_kitchen_night_lights at bg with dissolve
            "She goes straight to the kitchen without hesitation."
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(Does she... does she not realize I'm taller than her?)"
            show hiflmc casual_cu happy_cu
            "(Oh well. Better for me that she doesn't, I guess.)"
            hide hiflmc
            show vanessa casual basic at centre
            "She reaches up, going up on her toes even more than her high heels already lift her."
            show hiflmc casual basic at right3
            show vanessa casual smirk at left3
            "She grabs the bag of coffee and hands it to me with a flourish."
            "Now that she's gotten to do something useful, she seems to have regained some of her composure."
            va "Your coffee, as requested."
            show vanessa casual sad
            va "Though I'm not sure caffeine is the greatest idea, this late at night."
            show hiflmc casual surprised
            mcvan "You know what? You're right."
            show hiflmc casual basic
            mcvan "Coffee isn't a great idea right now."
            show hiflmc casual happy
            mcvan "Ice cream is much more appropriate."
            hide vanessa
            show hiflmc casual basic at centre
            "I pull out the pint of mint chocolate chip ice cream I've got stored in the freezer."
            show hiflmc casual happy
            mcvan "Do you want to help me demolish the rest of this?"
            show hiflmc casual basic at right3
            show vanessa casual sad at left3
            "Vanessa bites her lip, tooking terribly tempted."
            va "I really shouldn't--there's no room in my diet for ice cream."
            show vanessa casual blush
            va "But... that is my favorite flavor."
            show hiflmc casual happy
            "I can't help the smirk that spreads over my face as I grab a spoon and open the carton."
            mcvan "Well, if you can't have any, I'd hate to tempt you away from your diet..."
            show vanessa casual sad
            "I take a big spoonful and eat it, licking it thoroughly clean."
            show hiflmc casual basic
            mcvan "But I will say you're missing out."
            show hiflmc casual happy
            mcvan "It's so good."
            "Vanessa gulps, and I suppress the grin that wants to spread over my face."
            mcvan "Maybe I'll just eat it all by myself, since you don't want any..."
            "I can pinpoint the exact moment that she caves in, and I give an internal crow of victory."
            va "Wait."
            show vanessa casual smirk
            va "I guess one night of indulgence can't hurt too much."
            mcvan "That's the spirit."
            show vanessa casual basic at left2
            show hiflmc casual basic at right2
            "I motion for her to come closer, which she does immediately."
            show hiflmc casual happy
            "I scoop another spoonful and grin at her."
            mcvan "Open wide."
            show vanessa casual blush
            "Vanessa's face goes beet red, but she opens her mouth anyway."
            va "Aahn."
            show hiflmc casual surprised
            stop music fadeout 1.0
            play music hiflliteromance
            "The second her lips close around the spoon I freeze, an electric tingle shooting down my spine."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(I maybe did not totally think tyhis all the way through.)"
            hide hiflmc
            show hiflmc casual blush at right2
            show vanessa casual blush at left2
            "Now that my attention is on her lips, it's nearly impossible to look away."
            hide hiflmc
            hide vanessa
            show vanessa casual_cu blush_cu at vanessa_cu
            "She swallows, and I remove the spoon, teariny my gaze from her lips and catching her gorgeous eyes with my own."
            "They're almost magnetic, pulling me in closer the longer the moment stretches on."
            hide vanessa
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(She's so close, I could just lean over right now...)"
            hide hiflmc
            show hiflmc casual blush at right2
            show vanessa casual blush at left2
            "Once the thought enters my head, all I can think about is how much I want to kiss her."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(Her lips look so soft...)"
            "(And she'd taste like mint chocolate chip ice cream.)"
            show hiflmc casual_cu surprised_cu
            "(I think she might feel the same way?)"
            show hiflmc casual_cu happy_cu
            "(Maybe I should just lean over and do it?)"
            hide hiflmc
            show vanessa casual_cu sad_cu at vanessa_cu
            "One look at the rest of her face, though, and  I know it's not in the cards for tonight."
            "Vanessa looks completely overwhelmed."
            "Her eyes are wide, her cheeks flushed, and her lips are nearly white from how hard she's pressing them together."
            hide vanessa
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(She looks like she's going to combust if I get any closer.)"
            show hiflmc casual_cu happy_cu
            "(Probably best to take it slow, then.)"
            hide hiflmc
            show hiflmc casual happy at right3
            show vanessa casual basic at left3
            "I pull away and give her a little more space..."
            "I smile at her in a way that I hope is reassuring, and not like I was just thinking about jumping her bones."
            mcvan "I told you it was good."
            mcvan "How about I grab another spoon, and we finish this off together?"
            show vanessa casual sleep
            "Vanessa takes a deep breath, and it occurs to me that she may not have breathed at all for the duration of our pseudo-staring contest."
            hide vanessa
            hide hiflmc
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(Oh, Vanessa.)"
            hide hiflmc
            show hiflmc casual happy at right3
            show vanessa casual happy at left3
            "She smile shakily back at me."
            va "Yeah, that sounds great."
        "B. Let her go.":
            $menuhideborder = False
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(... But I shouldn't keep her here if she's uncomfortable.)"
            hide hiflmc
            show vanessa casual blush at left3
            show hiflmc casual surprised at right3
            mcvan "Oh, uh, sure. No problem."
            mcvan "Have... a nice shower?"
            hide vanessa
            show hiflmc casual surprised at centre
            "But Vanessa's already gone, practically sprinting out of the room."
            hide hiflmc
            show hiflmc casual_su sarcastic_cu at hiflmc_cu
            "(Way to go, [genericfn], you handled that great."
            hide hiflmc
            show hiflmc casual sarcastic at centre
            show bg heroine_kitchen_night_lights at bg with dissolve
            "I head to the kitchen, barely resisting the urge to stick my head in the freezer."
            show hiflmc casual angry
            "Instead, I just bang my head against the fridge lightly, goraning at my own social awkwardness."
            show hiflmc casual sad
            "(Maybe it's better that she didn't stick around.)"
            "(I definitely need some time to cool off and regroup after... all of that.)"
            show hiflmc casual sarcastic
            mcvan "Why am I incapable of talking to her like a normal person."
            show hiflmc casual angry
            "I bang my head on the refrigerator again, lightly."
            show hiflmc casual blush
            mcvan "She really needs to stop with the dramatic declarations aqbout protecting me to her dying breath."
            mcvan "There's only so much of that a girl can take."
    scene bg bowling at bg with fade
    stop music fadeout 1.0
    play music hifleveryday
    show hiflmc bowling sad at centre
    "Unfortunately, I can't afford another mental health day, despite everything that's going on."
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    "Vanessa goes with me to the bowling alley."
    "And I realize I'm almost used to the whole constant bodyguarding thing at this point."
    show hiflmc bowling happy
    "It's made easier by the fact that she's significantly more relaxed around the others now."
    mcvan "It's nice that you've made friends with them. It makes me happy."
    show vanessa casual angry
    "Vanessa harumphs."
    show hiflmc bowling surprised
    va "We're not {i}friends{/i}."
    show vanessa casual sleep
    va "But they have proves themselves... reliable, in combat."
    show vanessa casual angry
    show hiflmc bowling happy
    va "And more trustworthy than any other supernaturals I've met."
    "Her expression is defensive, and dangerously close to a pout."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(Sometimes she's so cute, it's ridiculous."
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual angry at left4
    "I can't resist the urge to tease her a little bit."
    show hiflmc bowling happy
    mcvan "Like I said, I'm glad you're all getting along better."
    hide vanessa
    show hiflmc bowling basic at centre
    "She wanders off to the bar to sulk, while I get to work cleaning the counters."
    hide hiflmc
    show jd casual happy at centre
    "JD is predictabloy not doing any work, and looks about ready to target Vanessa as their source of entertainment for the moment."
    hide jd
    $menuhideborder = True
    menu vans1e11c3:
        "A. Tell JD to do their job.":
            $menuhideborder = False
            show hiflmc bowling sarcastic at right4
            show jd casual smirk at left4
            mcvan "You know, JD, you could actually do your job and like... help me."
            show jd casual sad
            jd "Aww, but that's boring."
        "B. Protect Vanessa.":
            $menuhideborder = False
            show hiflmc bowling basic at right4
            show jd casual smirk at left4
            mcvan "Come on, JD. Leave Vanessa alone."
            show jd casual surprised
            jd "Seriously?"
            jd "But I've never gotten to prank a Helsing before."
            show hiflmc bowling happy
            mcvan "Guess you'll have to wait until another day for that opportunity."
            hide jd
            show vanessa casual happy at left4
            "Vanessa flashes me a grateful smile, and I grin back at her."
        "C. Let Vanessa handle it.":
            $menuhideborder = False
            show jd casual smirk at right4
            show vanessa casual basic at left4
            "JD barely gets within five feet of her before Vanessa puts up a hand."
            show jd casual surprised
            va "Nope."
            jd "You didn't even-!"
            show vanessa casual angry
            va "Yesterday was one of the longest days of my life."
            va "Do you really want to test my patience right now?"
            hide vanessa
            hide jd
            show hiflmc bowling_cu blush_cu at hiflmc_cu
            "(Why is she so hot when she's angry? That's so unfair.)"
    hide hiflmc
    hide jd
    hide vanessa
    show razi casual sleep at centre
    "Razi sighs."
    show razi casual basic
    ra "Why don't you go set up the pins."
    show razi casual basic at left4
    show jd casual angry at right4
    jd "Fine, but if I set them up in funky shapes, you have only yourselves to blame."
    hide razi
    hide jd
    show vanessa casual surprised
    "Vanessa looks adorably baffled by the entire exchange."
    show vanessa casual surprised at left4
    show razi casual basic at right4
    va "How do you operate a business when one of your two employees refuses to do their job?"
    show razi casual happy
    "Razi laughs good-naturedly."
    ra "We make it work."
    ra "It helps that [genericfn] more than makes up for it by being so diligent."
    hide vanessa
    show razi casual smirk at centre
    "He winks at me."
    hide razi
    show hiflmc bowling blush at right4
    show vanessa casual happy at left4
    "I feel myself blush at the praise, and then at the soft look Vanessa directs at me."
    hide hiflmc
    hide vanessa
    show diego doctor glassesbasic at centre
    "Just then, Diego comes in and sits down at the opposite end of the bar from Vanessa."
    show diego doctor glassesbasic at right4
    show vanessa casual angry at left4
    "Razi slides him his regular, and Vanessa stiffens, her shoulders going rigid."
    show diego doctor glassessmirk
    "He seems to take note of Vanessa's reaction, and shoots her a sardonic smile."
    di "Don't worry, Helsing."
    di "It's all ethically sourced donor blood."
    hide diego
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(...Oh.)"
    "(It hadn't even occurred to me that his regular wasn't really red wine.)"
    hide hiflmc
    show diego doctor glassesbasic at right4
    show vanessa casual basic at left4
    "Vanessa still looks uncomfortable, but some of the tension slides out of her."
    va "Oh. Well, good."
    scene bg bowling at bg with fade
    show hiflmc bowling basic at centre
    "The morning passes by with lots of conversation, and not much work."
    show hiflmc bowling happy
    "It's refreshing, getting to talk to everyone without them having to hide anything."
    hide hiflmc
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(I'm glad they're getting along better with Vanessa now, too.)"
    show hiflmc bowling_cu sad_cu
    "(Having to pick between them {i}sucked{/i}."
    hide hiflmc
    show mac cop basic at centre
    stop music fadeout 1.0
    play music mackenziehunt
    "Around lunchtime, Sheriff Hunt stops by on her break."
    Sheriff "Now that we're all here, what can you tell us about the threat?"
    "Sheriff Hunt looks dead serious."
    "It's a harsh contrast to the relatively more lightehearted mood from earlier."
    hide mac
    show hiflmc bowling sad at centre
    "I explain the Dracula situation and my apparent connection to it to the best of my ability."
    hide hiflmc
    show razi casual sad at left5 behind jd
    show jd casual surprised at left1
    show diego glassesdoctor basic at right5 behind jd
    show mac cop angry at right1
    "Their reactions range from stunned to contemplative, but none of them seem to be having the obvious reaction."
    hide mac
    hide razi
    hide jd
    hide diego
    show hiflmc bowling sarcastic at centre
    "Namely: the fact that there's no way I could really be related to some runaway bride of Dracula."
    show hiflmc bowling surprised
    mcvan "But that's ridiculous, right?"
    mcvan "She has to be mistaking me with someone else."
    show hiflmc bowling sad
    mcvan "Do you guys know anything that could help clear this up?"
    show hiflmc bowling surprised at right3
    show diego doctor glassesbasic at left3
    mcvan "Diego, this kind of your area of expertise, right?"
    show diego doctor glassessad
    "Diego is already shaking his head before I can finish the sentence."
    di "Dracula is an old world vampire. He sticks mostly to Europe."
    show hiflmc bowling sad
    show diego doctor glassesbasic
    di "I've spent the vast majority of my life in the new world, so vampires like Dracula are really not my forte."
    hide diego
    hide hiflmc
    show razi casual basic at centre
    ra "The illusion that you mentioned Li can cast..."
    ra "You said that only you saw it? Vanessa didn't?"
    hide razi
    show hiflmc bowling basic at right3
    show vanessa casual basic at left3
    "I look at Vanessa, who nods."
    va "That's correct."
    hide hiflmc
    hide vanessa
    show razi casual sleep at centre
    "Razi hums thoughtfully."
    show razi casual basic at left3
    show hiflmc bowling basic at right3
    mcvan "Do you know how to break it?"
    show razi casual sad
    ra "Her illusions seem different from my own, so I'm not quite sure how they work."
    show razi casual basic
    ra "But as far as I know, a strong emotional response can stimulate the brain into breaking free of all types of illusions."
    ra "Or really, most magic in general."
    hide razi
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Strong emotional response, huh?)"
    show hiflmc bowling_cu sarcastic_cu
    "(I guess the panic at seeing my sister captured by Li isn't the kind of emotional response he's talking about.)"
    hide hiflmc
    show razi casual basic at left3
    show hiflmc bowling basic at right3
    mcvan "I'll keep that in mind."
    hide hiflmc
    hide razi
    show vanessa casual basic at centre
    "Just then, Vanessa's phone rings."
    show vanessa casual surprised
    "Her eyes go wide."
    va "I only ever receive calls from the Order on this phone."
    show vanessa casual basic
    va "I have to go take this."
    "She vanishes into the arcade to answer it."
    hide vanessa
    show hiflmc bowling sad at centre
    "We stand around in awkward silent waiting for her to return, too tense to joke around like we were earlier."
    hide hiflmc
    show vanessa casual basic at centre
    "After several long moments, Vanessa returns."
    "Her expression is unreadable as she approaches, laser-focused in on me."
    va "[genericfn]..."
    va "The Helsing Order has extended an offer of full protection."
    va "They're asking that you come with me to Headquarters."

    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
