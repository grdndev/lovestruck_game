##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode10:
    $tbc = False

    ##Change these to suit the story
    scene bg main_day at bg
    play music hiflaction

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show truck_back_day at bg
    show hiflmc casual surprised at left3:
        zoom 1.05
    show damien wolf wolfbasic  at right3:
        zoom 1.05
    show truck_front_day at bg
    "Damien rolls up the windows and locks the doors before slamming on the gas to take us out of town."
    show hiflmc casual sarcastic
    "For once, I'm glad my truck is rattling and lurching, keeping from getting too far too fast."
    show bg road_day at bg
    show hiflmc casual angry at left3:
        zoom 1.05
    show damien wolf wolfbasic  at right3:
        zoom 1.05
    show truck_front_day at bg
    mcmac "What the hell do you even want?"
    show damien wolf wolfsmirk
    dam "You've picked up some fire since we first met. It's cute."
    show hiflmc casual sarcastic
    "(Is it somehow possible to crash this truck and only injure him in the process?)"
    mcmac "It's not fire."
    show hiflmc casual happy
    mcmac "It's knowing you're outclassed. Mackenzie knows where I am."
    dam "Does she now?"
    mcmac "Won't be two minutes before you have sirens on your ass."
    mcmac "That is, if she doesn't just tear you through the windshield instead."
    "Sure, it's cocky, but saying the words makes me feel better."
    show hiflmc casual sad
    "I have to think there's a way out of this, and as scared as I am right now..."
    "Damien might be taking me to where Grace has been hidden this whole time."
    dam "I'd love for her to try."
    show hiflmc casual angry
    show damien wolf wolfbasic
    mcmac "Is that why you keep picking on the deputy instead of fighting her face-to-face?"
    mcmac "You're a coward."
    show damien wolf wolfangry
    "Damien's knuckles go white around the steering wheel before he snarls."
    show hiflmc casual surprised
    "I'm forced back against my seat when he puts a set of sharpened nails right against my throat."
    "He's not watching the road, and that's enough to set me on the edge of panic."
    dam "I don't know what Hunt's been telling you, girl, but you're still human."
    dam "I'll be happy to prove it if you keep defaming my reputation."
    show hiflmc casual sad
    show damien wolf wolfbasic
    "The claws retract, and Damien spits a curse under his breath before returning to driving."

    scene bg abandoned_house_day at bg
    stop music fadeout 1.0
    play music hiflsuspense
    "He has to make a swift turn, jostling us both before finally coming to a stop in front of the abandoned house."
    "It looked creepy before, but in the daylight, it's just empty."
    "Empty and quiet."
    show truck_back_day at bg
    show hiflmc casual surprised at left3:
        zoom 1.05
    show damien wolf wolfbasic  at right3:
        zoom 1.05
    show truck_front_day at bg
    "(Wait, where's everyone else? I thought his pack would be here.)"
    dam "End of the line."
    hide truck_back_day
    hide truck_front_day
    hide damien
    hide hiflmc

    show hiflmc casual surprised at right2
    show damien wolf wolfbasic at left3 behind hiflmc
    "Before I can think about it too hard, Damien yanks me out of the truck, dragging me by the arm towards the porch."
    "I kick at him, but he doesn't even flinch, pulling out a polished set of handcuffs."
    show damien wolf wolfsmirk
    dam "I borrowed these from the office."
    dam "Knew they would come in handy at some point."
    show mackenzie_s1_mini9 at bg
    "He pulls me inside and locked me up near the front of the house, arms wrenched tight behind my back."
    scene bg abandoned_house_int_day at bg
    show hiflmc casual angry at left4
    show damien wolf wolfbasic at right4
    mcmac "Where's my sister?"
    dam "..."
    dam "You think I was going to keep you two in the same place?"
    dam "I'm not stupid."
    hide damien
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Then where could she possibly be?)"
    show hiflmc casual_cu sarcastic_cu
    "(There's not many places to hide a teenage girl here.)"
    "(We're alone here. That doesn't even make sense.)"
    show hiflmc casual angry at left4
    show damien wolf wolfbasic at right4

    mcmac "So what now?"
    show damien wolf wolfsmirk
    dam "What do you think?"
    hide hiflmc
    hide damien
    $menuhideborder = True

    menu mace10c1:
        "A. You sweet talk me.":
            $menuhideborder = False
            show hiflmc casual sarcastic at left4
            show damien wolf wolfsmirk at right4
            mcmac "Is this the part where you sweet talk me and say you and Mackenzie aren't so different?"
            mcmac "She just doesn't understand you, blah blah, I don't give a fuck."

        "B. I die of boredom.":
            $menuhideborder = False
            show hiflmc casual angry at left4
            show damien wolf wolfbasic at right4
            mcmac "I die of boredom, probably. You're terrible company."
            mcmac "Which is pretty impressive for a werewolf, in its own way."

        "C. An evil monologue.":
            $menuhideborder = False
            show hiflmc casual angry at left4
            show damien wolf wolfbasic at right4
            mcmac "Ooh, do I get an evil monologue?"
            mcmac "Am I gonna hear about how some alpha hurt your feelings?"
            mcmac "That would hold a lot more weight if you hadn't just kidnapped me, asshole."
    hide damien
    show hiflmc casual sad at centre
    "Anger and fear wage war inside my chest, and I really don't know when Mackenzie's going to show up."
    "All I can do is keep Damien occupied and hope he slips up about Grace."
    show hiflmc casual basic at right4
    show damien wolf wolfbasic at left4
    dam "We're going to be nice and patient waiting for Mackenzie to show up."
    dam "It's just too bad we can't get the messy part over with now."
    hide hiflmc
    hide damien
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(What's that supposed to mean?)"
    hide hiflmc
    show hiflmc casual surprised at right2
    show damien wolf wolfsmirk at left1 behind hiflmc
    "I hear footsteps. Damien must too, because he straigtens me up with a smile, lazily putting an arm around my shoulder."
    show hiflmc casual angry
    "Elbowing him just gets me a raised eyebrow."
    hide damien
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Creep!)"
    hide hiflmc
    stop music fadeout 1.0
    play music mackenziehunt
    show mac earstank wolfsad at centre
    "Mackenzie comes into view, shining with sweat and already transformed."
    show mac earstank wolfangry
    "The second she sees Damien, she makes her move."
    hide mac
    show hiflmc casual surprised at right2
    show damien wolf wolfsmirk at left1 behind hiflmc
    dam "Ah, none of that!"
    "His claws are back at my throat in a blur, each razor-sharp tip pressing into my skin."
    show hiflmc casual sad
    "If I even swallow too hard, it's going to hurt."
    dam "I'm here to talk."
    show damien wolf wolfbasic
    dam "Take another step and she's the first to bleed."
    hide damien
    hide hiflmc
    show mac earstank wolfbasic at centre
    "Mackenzie visibly tenses, still ready to spring forward, but she keeps her distance for now."
    "Just seeing her cuts through some of the tension in my chest."
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(I knew she'd come to find me.)"
    show hiflmc casual sad at left1
    show damien wolf wolfbasic at left4 behind hiflmc
    show mac earstank wolfbasic at right4

    ma "Start talking."
    show damien wolf wolfsmirk
    dam "It's simple, really."
    dam "I'm happy to hand [genericfn] without a scratch."
    dam "Give up the town and she's yours."
    hide damien
    hide mac
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Are you kidding?)"
    hide hiflmc
    $menuhideborder = True
    menu mace10c2:
        "A. Mac, don't do it.":
            $menuhideborder = False
            show hiflmc casual angry at left1
            show damien wolf wolfsmirk at left4 behind hiflmc
            show mac earstank wolfbasic at right4
            mcmac "Mac, don't even think about saying yes to that."
            mcmac "If he takes the town, who knows what will happen to everyone else."
            show hiflmc casual sad
            mcmac "What they'll do to you!"

        "B. He's a liar.":
            $menuhideborder = False
            show hiflmc casual angry at left1
            show damien wolf wolfsmirk at left4 behind hiflmc
            show mac earstank wolfbasic at right4

            mcmac "He's a liar. This can't be his big plan."
            mcmac "The pack isn't even here to see it."

        "C. Try and break free.":
            $menuhideborder = False
            show hiflmc casual angry at left1
            show damien wolf wolfsmirk at left4 behind hiflmc
            show mac earstank wolfbasic at right4
            "I try and pinch my hands together to slip out of the cuffs, praying there's some weak point in the colum I'm locked to,"
            show hiflmc casual sad
            show damien wolf wolfangry
            "But Damien growls, pressing a claw right againt the pulse in my neck."
            dam "Knock it off."
    stop music fadeout 1.0
    play music hiflgetitdone
    hide hiflmc
    hide damien
    show mac earstank wolfgrowl at centre
    "Mackenzie's hands clench into fists, righteous fury burning through golden eyes."
    ma "No deal."
    show hiflmc casual surprised at left1
    show damien wolf wolfangry at left4 behind hiflmc
    show mac earstank wolfgrowl at right4
    ma "You think I'm falling for the oldest trick in the book?"
    ma "That some backwater beta like you can intimidate me?"
    ma "Even if you dared to hurt her, you wouldn't survive it."
    ma "I'd make sure of that."
    ma "Land means nothing if it just becomes your grave, Damien."
    show damien wolf wolfbasic
    "He hesitates."
    "It's just for a split second, but I try not to let an overwhelming wave of relief show on my face."
    hide damien
    hide mac
    hide hilfmc
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(If Damien thought he could win against Mackenzie on his own, he wouldn't have taken me in the first place."
    hide hiflmc
    show hiflmc casual basic at left1
    show damien wolf wolfbasic at left4 behind hiflmc
    show mac earstank wolfgrowl at right4
    dam "..."
    "Mackenzie's fists start to tremble."
    show hiflmc casual sad
    "I can't tell if she's holding back the urge to take him out or exhausted from the run here."
    hide damien
    hide mac
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Then again, it might be both.)"
    show hiflmc casual surprised at left1
    show damien wolf wolfbasic at left4 behind hiflmc
    show mac earstank wolfgrowl at right4
    dam "Three days."
    show mac earstank wolfsurprised
    ma "Excuse me?"
    dam "I'll give her back to you, right now, unharmed, but you fight me in three days."
    dam "Wherever I choose."
    show damien wolf wolfsmirk
    dam "But when I win, this town is mine."
    dam "This land is mine."
    dam "And I'll take the [genericln] girls as a prize."
    hide damien
    hide mac
    hide hiflmc
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Three days? Why does he need three days?"
    hide hiflmc
    show hiflmc casual basic at left1
    show damien wolf wolfbasic at left4 behind hiflmc
    show mac earstank wolfbasic at right4
    ma "I'll fight you alone."
    show mac earstank wolfsmirk
    ma "If you think you can sic your friends on me in the middle of a challenge, you'll show them how weak you really are."
    dam "I won't need them."
    dam "You're untested, Hunt."
    show damien wolf wolfangry
    dam "Do you know how many fights I had to win to even sit next to a Rider?"
    ma "Clearly not enough."
    hide damien
    hide mac
    hide hiflmc
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(I'd high five her if I wasn't in handcuffs right now.)"
    hide hiflmc
    show hiflmc casual basic at left1
    show damien wolf wolfbasic at left4 behind hiflmc
    show mac earstank wolfbasic at right4
    ma "And you give me back [genericfn] and Grace."
    ma "You don't need either one of them if we're bound to a challenge."
    show damien wolf wolfsmirk
    dam "Right, and let you arrest me the second they're tucked away in bed."
    dam "No, you just get this one."
    ma "Then you bring Grace to the challenge."
    show mac earstank wolfangry
    ma "I'm not letting you sacrifice her to save your own ass."
    show damien wolf wolfbasic
    show mac earstank wolfbasic
    dam "..."
    dam "Whatever. Deal."
    dam "We'll meet out here by the lake. No other cops."
    dam "And none of your other magical friends either."
    show mac earstank wolfsmirk
    ma "Found out about that, did you?"
    ma "Let me guess, one of your wolves tried to stick her nose in the bowling alley again and regretted it."
    dam "She's fine. I was just kind enough to give her the day off."
    hide damien
    hide mac
    hide hiflmc
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(He is such a liar!)"
    hide hiflmc
    show hiflmc casual basic at left1
    show damien wolf wolfbasic at left4 behind hiflmc
    show mac earstank wolfbasic at right4
    ma "Deal. Now let [genericfn] go. Right now."
    show hiflmc casual surprised at right1
    "He fishes out the key and unlocks the cuffs, giving me a shove towards Mackenzie."
    "Her eyes stay locked on Damien until I'm by her side, waiting for any kind of trick."

    dam "Get out of here."
    hide damien
    show hiflmc casual sad at left2
    show mac earstank wolfbasic at right2 behind hiflmc
    "Mackenzie gently runs her knuckles down my arm, keeping her claws away from me."
    ma "Hop in the truck. I'll be in right after you."
    mcmac "Okay."
    scene bg abandoned_house_day at bg
    show truck_back_day at bg
    show hiflmc casual sad at left3:
        zoom 1.05
    show mac earstank wolfbasic  at right3:
        zoom 1.05
    show truck_front_day at bg
    "Damien was kind enough to leave my keys in the ignition, so I start the engine and slide into the passenger seat,"
    "watching as Mackenzie rounds the car to get in and drive."

    scene bg abandoned_house_day at bg
    show damien wolf wolfsmirk at centre
    "Before we pull away, Damien blows me a kiss."
    dam "See you soon, sweetheart."
    hide damien
    show truck_back_day at bg
    show hiflmc casual sad at left3:
        zoom 1.05
    show mac earstank wolfbasic  at right3:
        zoom 1.05
    show truck_front_day at bg
    "Mackenzie can't drive fast enough."
    scene bg road_day at bg
    show truck_back_day at bg
    show hiflmc casual sad at left3:
        zoom 1.05
    show mac earstank wolfbasic  at right3:
        zoom 1.05
    show truck_front_day at bg
    stop music fadeout 1.0
    play music hifleveryday
    pause
    show mac drooptank sleep
    "Once the house is out of sight, Mackenzie shifts back, the energy it takes is clear,"
    "sweat soaking through her tank top even while she focuses on the road."
    show mac tank sad
    mcmac "Did you sprint the whole way here?"
    ma "I had to."
    show mac tank angry
    ma "I couldn't risk Damien hearing the service car and running off with you again."
    show mac tank sad
    ma "Are you okay?"
    hide mac
    hide hiflmc
    $menuhideborder = True

    menu mace10c3:
        "A. Now that you're here.":
            $menuhideborder = False
            show hiflmc casual happy at left3 behind truck_front_day:
                zoom 1.05
            show mac tank sad  at right3 behind truck_front_day:
                zoom 1.05
            mcmac "I'm fine now that you're here."
            show hiflmc casual sarcastic
            mcmac "But the rest of the morning sucked, not gonna lie."

        "B. I will be.":
            $menuhideborder = False
            show hiflmc casual sad at left3 behind truck_front_day:
                zoom 1.05
            show mac tank sad  at right3 behind truck_front_day:
                zoom 1.05
            mcmac "I will be. I just want to go home."
            show hiflmc casual sarcastic
            mcmac "That bastard spilled my coffee all over the street."
        "C. My wrists hurt.":
            $menuhideborder = False
            show hiflmc casual sad at left3 behind truck_front_day:
                zoom 1.05
            show mac tank sad  at right3 behind truck_front_day:
                zoom 1.05

            mcmac "My wrists hurt from the cuffs, but otherwise, yeah."
            show hiflmc casual happy
            mcmac "He's a lot more bark than bite."
    show hiflmc casual sad
    "I sink back against my seat, letting out a deep breath."
    "I'm fine and Mackenzie's fine, we just have to figure out where to go from here."
    "Then curiosity hits me."
    show hiflmc casual surprised
    mcmac "So you didn't have a car, but you tracked me all the way here?"
    show hiflmc casual blush
    show mac tank smirk
    ma "I know your scent pretty well by now, [genericfn]."
    show mac tank sad
    ma "And... I felt it. The moment you were gone."
    show hiflmc casual sad
    mcmac "Felt what?"
    ma "A pull in my chest, like a compass drawing north."
    show mac tank blush
    ma "Which is definitely new."
    show mac tank smirk
    ma "I guess being an alpha really does have a lot of benefits."
    show hiflmc casual blush
    "(Is that because she's an alpha? Or because we kissed?)"
    show hiflmc casual happy
    mcmac "Getting a little more used to it?"
    show mac tank basic
    ma "I'm trying to. It's still not exactly comfortable."
    scene bg mc_house_ext_day at bg
    show truck_back_day at bg
    show hiflmc casual happy at left3:
        zoom 1.05
    show mac tank basic  at right3:
        zoom 1.05
    show truck_front_day at bg
    ma "Mackenzie pulls the truck up in front of my house and parks, handing me the keys once the engine's off."

    scene bg heroine_home_day at bg
    pause
    "After a night away, it's nice to see the place, but everything is still way too quiet."
    show hiflmc casual surprised at centre
    mcmac "Did you want some coffee or something-!"
    stop music fadeout 1.0
    play music hiflliteromance
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    "I'm cut off by Mackenzie drawing me into a tight hug."
    "I wrap my arms back around her in an instant, pressing my face against her shoulder, every drop of fear and stress in my body drains away."
    ma "In a minute."
    ma "I just had to prove you were alright."
    hide mac
    "I tilt my head up, eyes wanting, and Mackenzie leans down to kiss me."
    "Each time I seek a little more, kissing her back until we're resting against each other, brows lightly touching."
    show hiflmc casual_cu happy_cu at hiflmc_cu
    mcmac "I'm okay. You weren't too late."
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    ma "I never want to be too late."
    ma "And I'm sorry I couldn't take Grace back with us."
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    mcmac "Don't be sorry."
    mcmac "I don't think anything you said would have changed that."
    mcmac "Damien was acting really strange whenever I brought her up."
    hide hiflmc
    show mac tank_cu surprised_cu at mac_cu
    ma "What kind of strange?"
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    mcmac "I thought he'd take me where she was, right?"
    mcmac "But instead we went back to that house."
    mcmac "No pack, no Grace."
    show hiflmc casual_cu sarcastic_cu
    mcmac "Why did Damien even kidnap me if he had her as a bargaining chip?"
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "That's a good question."
    ma "I assume he was trying to bait me, but I would have gone if Damien threatened her too."
    hide mac
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    mcmac "And why does he need three days? For what?"
    hide hiflmc
    show mac tank_cu angry_cu at mac_cu
    ma "I couldn't figure out that either. Or what it has to do with any eclipse."
    "Mackenzie lets out a frustrated huff, and I feel it down to my bones."
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "Damien's been dragging us around by the neck, and it doesn't seem like we're any closer to stopping him."
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "It doesn't matter."
    show mac tank_cu smirk_cu
    ma "If he wants a fight, he'll get one."
    ma "Damien can't beat me in a stand-up match, I'm sure of it."
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    mcmac "That's what I'm worried about."
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    mcmac "You really think he's going to suddenly start playing fair?"
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "No, but if he loses in front of everyone else, his leadership means nothing."
    show mac tank_cu smirk_cu
    ma "All his rogue friends are going to go running for greener pastures."
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    mcmac "I don't want you getting hurt if he plays dirty, Mac."
    hide hiflmc
    show mac tank_cu happy_cu at mac_cu
    ma "I won't. You've got my back, don't you?"
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    mcmac "Every step of the way."
    hide hiflmc
    show mac tank_cu happy_cu at mac_cu
    ma "Then I'll be fine."
    hide mac
    show hiflmc casual basic at right4
    show mac tank smirk at left4
    "She presses another kiss to my forehead before taking a step back."
    "Mackenzie looks down at her tank top and raises an eyebrow, tugging at the fabric."
    ma "Mind if I take a shower? I'm not fit for duty right now."
    show hiflmc casual happy
    mcmac "Sure thing. It's just through the hall there."
    show mac tank happy
    ma "Thanks."
    hide mac
    show hiflmc casual blush at centre
    "It's not until she walks away that I realize what taking a shower entails."
    "The image that's seared into my mind leaves me blushing until Mackenzie pokes her head out to ask for a towel."
    mcmac "Uh, one second!"

    hide hiflmc

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
