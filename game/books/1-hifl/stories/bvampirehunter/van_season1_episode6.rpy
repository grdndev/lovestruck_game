label van_season1_episode6:

    $tbc = False
    scene bg mc_house_ext_fog at bg
    play music hiflsuspense
    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show hiflmc bowling angry at centre
    "Vanessa's outstretched hand just barely misses my shirt."
    hide hiflmc
    show bg heroine_home_lights at bg
    show vanessa casual angry at centre
    va "[genericfn], don't!"
    hide vanessa
    show bg mc_house_ext_fog at bg
    show hiflmc bowling angry at centre
    "But all I can focus on is Grace."
    show hiflmc bowling surprised
    "(How did Li get her?!)"
    hide hiflmc
    show grace casual basic at centre
    hide grace with dissolve
    pause
    "The moment I'm out the door, Grace disappears."
    show hiflmc bowling surprised at centre
    mcvan "Where's Grace?! What did you do with her?!"
    show hiflmc bowling surprised at right1
    show li casual basic at left1 behind hiflmc
    "Li vanishes in an instant, reappearing behind me."
    "She grabs me in her supernaturally strong arms, her grip like a vise."
    show li casual happy
    sinli "This was much easier than I had anticipated."
    "You fell for that so readily, rushing in to protect your sister."
    show li casual surprised
    "She clicks her tongue."
    sinli "How noble... Foolish, but noble."
    show li casual happy
    "There's an edge of mockery in her frosty, disaffected tone."
    hide li
    hide hiflmc
    show vanessa_s1_mini1 at bg:
        zoom 0.2
    "Vanessa rushes toward me, wearing the most intense glare I've ever seen."
    hide vanessa_s1_mini1
    show vanessa casual angry at centre
    va "Let go of [genericfn], and I'll end you painlessly."
    hide vanessa
    show hiflmc bowling surprised at left2
    show li casual basic at left4 behind hiflmc
    show vanessa whipcasual angry at right3
    "She lashes out with her whip, but Li holds me in front of her like a human shield."
    hide vanessa
    hide li
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Damn, Vanessa can't get a good angle like this.)"
    show hiflmc bowling angry at right1
    show li casual basic at left1 behind hiflmc
    mcvan "Just tell me what you did with my sister!"
    show li casual happy
    "Li chuckles."
    sinli "Naive girl... She was never here to begin with."
    show li casual basic
    sinli "I simply needed a good illusion to draw you out. Your sister was the most effective choice."
    hide li
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(An illusion?!)"
    hide hiflmc
    show hiflmc bowling surprised at right1
    show li casual basic at left1 behind hiflmc
    mcvan "What do you mean?"
    show li casual surprised
    "Li sighs impatiently."
    show li casual basic
    sinli "I am infinitely older and more powerful than you. I have the ability to make you see whatever I wish."
    show li casual angry
    sinli "It is truly not that difficulty to understand."
    hide hiflmc
    hide li
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Okay, she was already the worst, but I'm really tired of the whole {i}I'm so much better and more powerful than you are{/i} schtick.)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e6c1:
        "A. Try to escape.":
            $menuhideborder = False
            show hiflmc bowling_cu basic_cu at hiflmc_cu
            "(But maybe I can use her smug monologuing as a distraction.)"
            "(What were those self-defense moves Grace and I studied, again...?)"
            "(Step on the foot, then elbow the solar plexus, right?)"
            hide hiflmc
            show hiflmc bowling sad at right2
            show li casual happy at left1 behind hiflmc
            "Unfortunately, her arms are like steels bands around me."
            sinli "Did you think escape would be that easy?"
        "B. Press Li for answers.":
            $menuhideborder = False
            show hiflmc bowling sarcastic at right2
            show li casual happy at left1 behind hiflmc
            mcvan "We get it. You're so much better than us."
            mcvan "But if that's really the case, why do you even need me in the first place?"
            sinli "You need not be in such a rush."
            sinli "I will tell you what you wish to know, as soon as Helsing is out of my way."
        "C. Call Vanessa for help.":
            $menuhideborder = False
            show hiflmc bowling sad at right2
            show li casual basic at left1 behind hiflmc
            "I look to Vanessa hopefully."
            mcvan "I could really use some rescuing, right about now."
            hide li
            hide hiflmc
            show vanessa whipcasual basic at centre
            "Vanessa shoots me a reassuring glance."
            show vanessa whipcasual angry
            va "I'll get you out of this, [genericfn]. I just need to find an opening."
            hide vanessa
            show hiflmc bowling sad at right2
            show li casual happy at left1 behind hiflmc
            sinli "So confident, Helsing, but can you live up to your boasting?"
    hide li
    hide hiflmc
    show hiflmc bowling sad at right2
    show li casual happy at left1 behind hiflmc
    "Li laughs derisively."
    sinli "To think I have such a rare opportunity!"
    sinli "Take [genericln] and kill a Helsing, all in one night."
    hide li
    hide hiflmc
    show vanessa whipcasual sad at left3 behind li
    show li casual angry at right1
    "She strikes out at Vanessa faster than she can react, but I feel like I'm watching it happen in slow-motion."
    "Li slashes at Vanessa's exposed shoulder, drawing a deep, painful-looking gouge."
    hide li
    hide vanessa
    show hiflmc bowling surprised at centre
    mcvan "VANESSA!"
    hide hiflmc
    show vanessa whipcasual angry at centre:
        linear 0.095 xoffset -90 #-offset to keep Character in place
        linear 0.095 xoffset +0 #+offset to move Character
        repeat 4 #Repeats
    "{i}Vanessa sways.{/i}"
    "She sways in her place but continues fighting."
    "Still, Vanessa's next few attacks are slower, more sluggish."
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(This fight needs to end soon, so Vanessa can get medical attention...)"
    hide hiflmc
    show vanessa whipcasual sad at centre
    "On her next strike, she overextends herself and loses her balance."
    "She falls, landing on her wrist."
    show vanessa whipcasual angry
    va "Agh!"
    hide vanessa
    show li casual happy at centre
    "I watch, helpless, as Li rears back to deal the finishing blow."
    hide li
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Someone, anyone, please come help us.)"
    show hiflmc bowling_cu sad_cu
    "(Please don't let Vanessa die protecting me!)"
    hide hiflmc
    stop music fadeout 1.0
    play music hiflaction
    show diego casual vampireangry at left2
    show mac earscop wolfangry at right2
    "Like they were summoned right out of my thoughts, Sherriff Hunt and Dr. Escalona run to our rescue."
    "Except they're... different."
    hide mac
    hide diego
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Since when has Sheriff Hunt had wolf ears?!)"
    "And those eyes, and fangs... is Dr. Escalona a vampire too?!)"
    "(What is happening?!)"
    show hiflmc bowling_cu angry_cu
    "(Is this another one of Li's illusions, or...?)"
    hide hiflmc
    show diego casual vampireangry at left4
    show li casual vampireangry at centre
    show mac earscop wolfgrowl at right4
    "They attack her in tandem, and with the element of surprise on their side, they're more than a match for Li."
    "Her eyes glow more brightly for a moment, a menancing snarl on her lips..."
    hide li
    hide mac
    hide diego
    #show bat animation
    "And she disappears without a word in a swarm of bats."
    stop music fadeout 1.0
    play music diego
    show diego casual basic at left2
    show mac earscop wolfbasic at right2
    "Immediately, Sheriff Hunt turns to Dr. Escalona."
    Sheriff "Diego, take care of them. I'm going after her."
    hide diego
    show mac earscop wolfbasic at centre
    "He nods, and Sheriff Hunt takes off, running faster than humanly possible into the night."
    hide mac
    show hiflmc bowling surprised at right2
    show vanessa casual basic at left2
    "I rush to Vanessa's side."
    mcvan "Are you okay?! How badly did she hurt you?"
    show vanessa casual angry
    va "It's just a flesh wound."
    "But rather than charmingly self-assured her tone is guarded and cold."
    hide vanessa
    hide hiflmc
    show diego casual basic at centre
    "Dr. Escalona squats in front of us."
    doc "Let me take a look at your wound. You may need stitches."
    show diego casual basic at left3
    show vanessa casual angry at right3
    "Vanessa gives him a look of the utmost loathing."
    va "I'd rather die than let you touch me, bloodsucker."
    "I expect him to look offended, but he continues to stare at her coolly, unfazed."
    doc "You can either let me look at your wound, or you can bleed out."
    show diego casual sad
    doc "As you've sworn to protect [genericfn] until the threat is dealt with..."
    show diego casual basic
    doc "I would think that letting me patch you up would be the better option."
    "Her expression remains unchanged, ans she flinches back when he tries to move closer."
    show diego casual sleep
    "Dr. Escalona rolls his eyes and stands up, backing away."
    hide vanessa
    show diego casual basic
    show hiflmc bowling basic at right3
    doc "Alright, maybe you can convince her."
    hide hiflmc
    hide diego
    $menuhideborder = True
    menu vans1e6c2:
        "A. He is a real doctor.":
            $menuhideborder = False
            show hiflmc bowling sad at right3
            show vanessa casual angry at left3
            mcvan "Listen, Vanessa, I know that he's a vampire and that you don't trust him..."
            mcvan "But he did just help save our lives. And he is a real doctor."
            show vanessa casual sad
            "She gives me that look again, the one that says she thinks I'm painfully naive."
            show vanessa casual basic
            va "Supernatural creatures having real jobs doesn't make them any less dangerous."
        "B. Don't die because of me.":
            $menuhideborder = False
            show hiflmc bowling sad at right3
            show vanessa casual angry at left3
            mcvan "You got injured because of me."
            mcvan "Please, don't die because you were protecting me."
            show vanessa casual sad
            "She scoffs and looks away, but she looks less angry and more sulky."
            va "Don't exaggerate, I'm not going to die. Like I said, it's a flesh wound."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(Wasn't she the one who said she was going to die in the first place...?)"
            hide hiflmc
        "C. You don't have to trust him":
            $menuhideborder = False
            show hiflmc bowling sad at right3
            show vanessa casual angry at left3
            mcvan "I'm not saying you have to be best friends or even that you have to trust him."
            mcvan "But you're injured, and he can help. Be practical."
            va "Good, because I don't trust him."
    show vanessa casual sleep at left2
    show hiflmc bowling basic at right2
    "She sighs loudly, put-upon."
    show vanessa casual basic
    va "But fine."
    va "I guess I'll let the vampire treat me, just this once."
    va "To ease your mind."
    show hiflmc bowling happy
    "I fight to suppress my smile."
    hide hiflmc
    show vanessa casual angry at right3
    show diego casual basic at left3
    "Dr. Escalona examines her shoulder, emotionless despite Vanessa's glare."
    doc "Well, the good news is you don't need stitches."
    doc "But we should still get this cleaned out and bandaged as soon as possible."
    hide vanessa
    hide diego
    show hiflmc bowling surprised at centre
    mcvan "I have a first aid kit inside."
    show hiflmc bowling sad at right1 behind vanessa
    show vanessa casual basic at left1
    "I help Vanessa stand up and wrap my arm around her waist, helping her inside."
    scene bg heroine_home_lights at bg with dissolve
    show hiflmc bowling sad at right1 behind vanessa
    show vanessa casual basic at left1
    "I settle her on the couch and turn around, looking for Dr. Escalona, and realize he's still standing at the door."
    hide vanessa
    show hiflmc bowling surprised at centre
    mcvan "Oh, right, sorry! Please, Dr. Escalona, please come in."
    show hiflmc bowling surprised at right3
    show vanessa casual surprised at left3
    va "What are you doing?!"
    show hiflmc bowling sarcastic
    mcvan "Well, he's not going to be much help if he's standing out there and you're in here."
    show hiflmc bowling basic
    mcvan "Besides, if he was going to hurt us, he's had plenty of opportunities."
    hide hiflmc
    hide vanessa
    show diego casual basic at centre
    doc "Thank you for the vote of confidence."
    show diego casual sleep
    doc "And you might as well start calling me Diego."
    hide diego
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(I guess I do know his big secret now, after all.)"
    hide hiflmc
    show diego casual basic at left3
    show vanessa casual angry at right3
    "Diego stands in the corner of the room, ignoring Vanessa’s death glare while I run and get the first aid kit."
    show diego casual basic at left2 behind vanessa
    show vanessa casual angry at right2
    "He comes forward and cleans off the shoulder wound, bandaging it efficiently."
    "Vanessa doesn’t show a hint of pain –not a wince or anything, despite how much the disinfectant must burn."
    hide diego
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Oh! But she injured her wrist, too.)"
    hide hiflmc
    show hiflmc bowling basic at right3
    show vanessa casual basic at left3
    mcvan "How's your wrist?"
    va "It's fine -I just twisted it. Not a big deal."
    show hiflmc bowling sad
    mcvan "Let me wrap it anyway, just in case."
    hide hiflmc
    hide vanessa
    stop music fadeout 1.0
    play music hiflliteromance
    show vanessa_s1_mini6 at bg with dissolve:
        zoom 0.4
    "I pick up a roll of gauze and kneel in front of her."
    "I hold her hand, gently wrapping her wrist."
    mcvan "How's that? Too tight, too loose?"
    hide vanessa_s1_mini6
    show vanessa casual_cu sad_cu at vanessa_cu
    "When I look up, her expression is so much softer than her earlier cold glare at Diego."
    hide vanessa
    show hiflmc bowling blush at right1
    show vanessa casual sad at left1 behind hiflmc
    "I feel myself start to blush."
    show vanessa casual happy
    va "No, it's perfect."
    hide hiflmc
    hide vanessa
    show diego casual sleep at centre
    "Diego coughs."
    stop music fadeout 1.0
    play music hifleveryday
    show diego casual basic
    di "It appears as though the vampires hunting you know where you live, [genericfn]."
    di "I suggest that you find other lodging for the time being, since Helsing over there isn’t in any shape to fight."
    show diego casual basic at left3
    show vanessa casual angry at right3
    va "Watch it, vampire."
    show diego casual sad
    di "If your goal is to protect [genericfn], you need to be in top fighting form."
    show diego casual basic
    di "Which means resting and letting your body heal."
    show vanessa casual basic
    va "We’ll stay in my van, then. It’s impenetrable and fully stocked."
    hide diego
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Well, I’ve definitely slept in worse places than a tricked-out van.)"
    show hiflmc bowling_cu basic_cu
    "(And if Vanessa says it’s the safest place, I believe her.)"
    hide hiflmc
    show vanessa casual basic at left3
    show hiflmc bowling basic at right3
    mcvan "Sounds good to me. I'll drive."
    show vanessa casual angry
    "Vanessa looks like she’s going to argue, but I beat her to it."
    show hiflmc bowling sad
    mcvan "You've lost a lot of blood. You're in no condition to drive."
    mcvan "Just let me do this, okay?"
    show vanessa casual sad
    show hiflmc bowling basic
    "Vanessa pouts, just the tiniest bit, but hands over the keys."
    show vanessa casual basic
    va "I never let other people drive my van, but... I suppose I can make an exception."
    show hiflmc bowling happy
    mcvan "Well, you can put your faith in me. I’m a very careful driver."
    scene bg mc_house_ext_fog at bg with fade
    show hiflmc bowling basic at right1 behind vanessa
    show vanessa casual basic at left1
    "I help her up and keep an arm around her in support as we walk to her van, Diego trailing behind us."
    hide vanessa
    show hiflmc bowling basic at left3
    show diego casual basic at right3
    "Once I have her settled as comfortably as possible in the passenger seat, I turn to Diego."
    show hiflmc bowling sad
    mcvan "Thank you, for saving us. And for patching up Vanessa."
    di "Yes, well. The Hippocratic oath dictates I must help the injured and sick if I’m able."
    di "Even if she is a Helsing."
    show hiflmc bowling happy
    mcvan "Well, whatever the reason is, thank you. And thank Sheriff Hunt for me, too."
    di "Sure. I’ll tell Razi and JD what happened, as well."
    show diego casual sad
    show hiflmc bowling basic
    di "You should drive to the bowling alley –it’s safer, and you’ll have the both of them close at hand."
    mcvan "I'll do that."
    scene bg road_night at bg
    stop music fadeout 1.0
    play music hiflsad
    show van_back_night at bg
    show van_middle_night at bg
    show van_front_night at bg
    pause
    show hiflmc bowling sad at right3 behind van_front_night
    show vanessa casual basic at left3 behind van_front_night
    "I try to concentrate on driving instead of worrying over Vanessa, but I wind up looking over at her every few seconds anyway."
    "I park in my usual spot and turn, giving Vanessa my full attention."
    show hiflmc bowling basic
    mcvan "Come on, you should lie down."
    va "Really, I’m fine. I’ve had worse injuries than this."
    "But she doesn’t stop me from helping her into her bed in the back of the van."
    scene bg van_interior_loft_night at bg with fade
    pause
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Vanessa’s trying to be tough, but she’s clearly in worse shape than she wants me to think.)"
    hide hiflmc
    show vanessa casual basic at left2
    show hiflmc bowling happy at right2
    mcvan "Are you going to let me check your bandages, or are you too badass and cool for that?"
    show vanessa casual happy
    "She smiles slightly and shakes her head."
    va "I have no objection to you tending my wounds."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(There’s absolutely no reason for my heart to be racing like that.)"
    "(She just means that she doesn’t mind if it’s me because I’m a human.)"
    "(It’s not because I’m special or anything.)"
    hide hiflmc
    show vanessa casual basic at left2
    show hiflmc bowling basic at right2
    "I check the bandage on her shoulder wound and make sure the wrapping on her wrist is still comfortably tight."
    hide hiflmc
    hide vanessa
    show vanessa casual_cu basic_cu at vanessa_cu
    "Her gaze almost burns me with its intensity, and a blush rises to my cheeks as I fumble with the bandages."
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Does she have to stare at me like that?)"
    "(It’s so hard to concentrate...)"
    hide hiflmc
    show vanessa casual basic at left2
    show hiflmc bowling blush at right2
    "I pull back."
    show hiflmc bowling basic
    mcvan "Well, the bandages look good. How are you feeling?"
    show vanessa casual angry
    va "Like I’ve been saying, I’m fine."
    va "One lucky hit isn’t enough to take me out of commission."
    show hiflmc bowling sad
    "Even as she talks, beads of sweat start to appear on her forehead."
    "She doesn’t move her shoulder at all, either, and seems to be avoiding putting pressure on it."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(She must be in so much pain...)"
    hide hiflmc
    show vanessa casual angry at left2
    show hiflmc bowling sad at right2
    mcvan "Can I at least get you a painkiller, or some water, or anything?"
    show vanessa casual basic
    va "I’m really fine. I hate painkillers."
    va "But actually... there should be a mini-fridge behind you with a PowerUp, the sports drink, in it."
    va "Would you mind passing me one?"
    show hiflmc bowling surprised
    "I scramble to get her a bottle, and she takes a long swig, draining almost half of it."
    show hiflmc bowling basic
    mcvan "Do you need anything else?"
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I just want to take care of her.)"
    "(She got hurt for my sake, and she refuses to take care of herself...)"
    "(I just don’t want to leave her alone.)"
    hide hiflmc
    show vanessa casual smirk at left2
    show hiflmc bowling sad at right2
    va "Honestly, I just need to rest a little, and I’ll be back to normal."
    show vanessa casual sad
    "I start to leave... only to see her wince again as she reaches to put the bottle down on the table."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I shouldn't leave her like this.)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e6c3:
        "A. Stay with Vanessa." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling basic at right2
            mcvan "Okay, well. You rest, and I’ll stay here in case you need anything."
            show hiflmc bowling basic at right1
            "I settle in beside her, taking care not to agitate her shoulder."
            show hiflmc bowling surprised
            "It's... a pretty tight space."
            show hiflmc bowling blush
            "Our sides are flush against each other, and I work hard to fight a blush."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu angry_cu at hiflmc_cu
            "(This isn't the time, [genericfn]! She's hurt!)"
            "(Control your thirst!)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling surprised at right1
            mcvan "Sooo... this van doesn’t really seem made for having company."
            mcvan "Where do you normally put guests?"
            show vanessa casual smirk
            "Vanessa laughs humorlessly."
            show hiflmc bowling basic
            va "I don't have guests."
            show vanessa casual basic
            va "I told you, I work alone."
            show hiflmc bowling sad
            mcvan "Doesn't that... I mean, don't you ever get lonely."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Grace has only been gone a few days and I know I’m already feeling lonelier.)"
            "(I can’t imagine being alone all the time.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling basic at right1
            va "That doesn’t matter."
            show vanessa casual angry
            va "This is my destiny, my calling."
            show vanessa casual basic
            va "What’s the point in dwelling on my feelings about it? It doesn’t change anything."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(That’s... one of the saddest things I’ve ever heard.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling surprised at right1
            mcvan "Does that mean you’ve never gotten to have friends or a normal life?"
            show vanessa casual sleep
            "She shrugs her uninjured shoulder."
            show vanessa casual basic
            va "Not really, though I guess it depends on your definition of ‘normal.'"
            show hiflmc bowling basic
            mcvan "You know, hanging out with other kids, goofing off, complaining about school, or your parents..."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Not that I got to do much of any of those things after my parents died, either.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling basic at right1
            mcvan "That kind of normal."
            show vanessa casual sad
            va "I mean. I was around other people, sometimes."
            va "But I was mostly homeschooled because I was traveling around so much..."
            va "So there wasn’t much time for any of those ‘normal’ things."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Oh.)"
            hide hiflmc
            show vanessa casual smirk at left2 behind hiflmc
            show hiflmc bowling basic at right1
            va "I did get to go to Hebrew school for a year, and have my bat mitzvah and a party and everything..."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(She’s Jewish? I guess that would explain the necklace.)"
            hide hiflmc
            show vanessa casual sad at left2 behind hiflmc
            show hiflmc bowling basic at right1
            va "But... well, I wouldn’t exactly say I made any friends."
            va "And anyway, I had to leave a week later to continue my training."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(I don’t know what to say. I thought I had it bad.)"
            "(I mean, I know her experiences don’t invalidate mine, but wow.)"
            "(I don’t think she even really understands how sad her story is.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling happy at right1
            mcvan "Well, at least you got to travel a lot, I guess?"
            mcvan "That must've been kinda cool."
            show vanessa casual sad
            show hiflmc bowling basic
            va "There’s not much time for sightseeing when you’re traveling around to train or hunt monsters."
            show vanessa casual happy
            va "I do enjoy getting to experience new cultures, though."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(She’s so dedicated...)"
            hide hiflmc
            show vanessa casual smirk at left2 behind hiflmc
            show hiflmc bowling basic at right1
            va "Besides, I always learn a new skill or fight a new creature, which is the important part."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(I can’t tell if she’s saying that to make me feel better, or to make herself feel better.)"
            show hiflmc bowling_cu basic_cu
            "(Then again.)"
            show hiflmc bowling_cu sad_cu
            "(She might really believe it.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling surprised at right1
            mcvan "How long have you been training, then?"
            mcvan "You make it sound like you were training even as a teenager..."
            show vanessa casual surprised
            "She looks at me like I’m missing something obvious."
            show vanessa casual basic
            va "I’ve been training since I was a kid. For as long as I can remember."
            va "This is my destiny."
            va "Why would I have wasted time playing around?"
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(... Wow.)"
            show hiflmc bowling_cu sad_cu
            "(That's... a lot.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling basic at right1
            va "I don’t regret it. I’d gladly sacrifice having a ‘normal’ life to protect humanity."
            "The depth of her belief and dedication shines through in her eyes, especially this up-close."
            hide vanessa
            hide hiflmc
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(She really believes that, doesn’t she?)"
            "(She might be the strongest person I’ve ever met.)"
            hide hiflmc
            show vanessa casual basic at left2 behind hiflmc
            show hiflmc bowling surprised at right1
            mcvan "I know... I mean, we’ve only known each other for a few days."
            mcvan "And you’ve mostly just been protecting me."
            show hiflmc bowling sad
            mcvan "You got injured protecting me."
            mcvan "I’m guessing you’ll have to leave as soon as the vampires are dealt with."
            show hiflmc bowling basic
            mcvan "But... I'm here for you."
            mcvan "I just want you to know that."
            show vanessa casual surprised
            "She looks at me with wide eyes, stunned speechless."
            "I’m a little stunned by my own words, too."
            "I hadn’t planned on blurting all of that out, but... everything I said was true."
            hide vanessa
            hide hiflmc
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(I just hope she believes me.)"
            hide hiflmc
        "B. Leave her alone.":
            $menuhideborder = False
            show hiflmc bowling basic at right2
            show vanessa casual basic at left2 behind hiflmc
            mcvan "Of course. I'll just get out of your hair..."
            "I move to leave, to give her space to get some sleep."
            show vanessa casual sad
            "As I turn, though, Vanessa grabs my wrist and tugs."
            show hiflmc bowling surprised
            "I turn back immediately."
            show hiflmc bowling basic
            mcvan "What's up?"
            show hiflmc bowling basic at right1
            "She pulls me closer."
            show vanessa casual blush
            "A blush dusts her cheeks, and for a moment she drops the tough girl act, looking at me shyly."
            va "Just... thanks, for taking care of me."
            hide vanessa
            hide hiflmc
            show hiflmc bowling_cu blush_cu at hiflmc_cu
            "(Oh god, her face is so close...)"
            hide hiflmc
            show vanessa casual blush at left2 behind hiflmc
            show hiflmc bowling surprised at right1
            "My voice comes out raspy."
            show hiflmc bowling blush
            mcvan "Yeah, of course. You’re welcome."
            hide hiflmc
            hide vanessa
    stop music fadeout 1.0
    play music hiflliteromance
    show vanessa casual_cu basic_cu at vanessa_cu
    "In the following silence, I realize just how little space there is between us."
    "Our faces are so close, I could almost count her eyelashes."
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(That’s probably not helping Vanessa get any rest.)"
    hide hiflmc
    show vanessa casual basic at left2 behind hiflmc
    show hiflmc bowling blush at right1
    "I blush and try to back up, but there’s not really anywhere to go."
    "I end up lying on my side, facing Vanessa, inches apart."
    mcvan "Well.. Good night. Try to get some sleep."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Not that I’m going to be able to sleep, lying so close to her...)"
    hide hiflmc
    show vanessa casual surprised at left2 behind hiflmc
    show hiflmc bowling basic at right1
    "Suddenly, Vanessa’s eyes go wide."
    hide hiflmc
    hide vanessa
    show vanessa casual_cu surprised_cu at vanessa_cu
    "Her expression lights up like she’s just had an epiphany."
    "She grabs my hand and leans in even closer, close enough that I can feel her breath on my lips."
    "I feel my heart rate spike."
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Is she going to-?!)"
    $tobecontinued()
    scene bg hifltbc at bg
    with fade
    pause
    $ resets()
