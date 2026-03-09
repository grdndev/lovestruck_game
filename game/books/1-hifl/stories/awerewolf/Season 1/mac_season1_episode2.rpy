label mac_season1_episode2:

    $tbc = False
    scene bg lake_moon at bg
    play music mackenziehunt

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False


    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(There’s no way! What is she?)"
    show hiflmc casual surprised at centre
    "My mind supplies the word ‘werewolf’, but the thought is so absurd, I start to laugh."
    show hiflmc casual surprised at left3
    show mac earstank wolfbasic at right3
    "It’s a helpless, confused sort of sound, turning into a yelp when Mackenzie looks at me."
    hide hiflmc
    hide mac

    show hiflmc casual surprised at shake

    "I stumble backwards, tripping over a rock."

    "Mud and grass slips under my hands, stopping me from finding my balance."
    show hiflmc casual surprised at left3
    show mac earstank wolfbasic at right3
    "So all I can do is scoot backwards, trying to put some distance between me and her."
    show hiflmc casual angry
    mcmac "This can’t be real."
    show hiflmc casual sarcastic
    mcmac "If this is a joke because of what I did to your shirt, haha! Real funny."

    mcmac "I’ve known you forever, you can’t just—!"
    show mac earstank wolfbasic at centre
    show hiflmc casual surprised
    "Mackenzie’s steps are slow and deliberate, her entire body moving differently than the way I’m used to."
    show hiflmc casual sad
    "When my back hits a tree, I groan and resign myself to my fate, wondering if it’s better to close my eyes or not."

    "Then she offers me her hand."
    hide mac
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    mcmac "Uh."
    hide hiflmc
    show mac earstank_cu wolfsmirk_cu at mac_cu
    ma "Come on, girl. I don't bite."

    show hiflmc casual surprised at left1
    show mac earstank wolfsmirk at right1 behind hiflmc

    "She doesn’t let my hesitation last, grabbing me by the wrist and helping me to my feet in one strong pull."

    "My knees are still a little wobbly, but Mackenzie lets me clutch at her arm until they’re steady again."
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(It’s still her. She’s not a monster... I think.)"
    show hiflmc casual_cu sarcastic_cu
    "(This doesn’t make any sense!)"
    hide hiflmc
    show mac earstank_cu wolfsmirk_cu at mac_cu behind hiflmc

    "Golden eyes glow with amusement as Mackenzie brushes a few mussed strands of hair away from my face."

    "She’s never touched me like this before, and even with those very sharp nails close to my skin, I shiver."
    show hiflmc casual surprised at left1
    show mac earstank wolfsmirk at right1 behind hiflmc
    mcmac "Sheriff—?"

    ma "Use my name [genericfn]. I still have one."
    show hiflmc casual blush at left1

    mcmac "M-Mackenzie. What is..."
    show hiflmc casual sad

    mcmac "You have fangs and wolf ears and I really don't know how to deal right now."
    show mac earstank wolfbasic
    ma "There's nothing to deal with, alright?"

    ma "This was my secret, and now it's yours too. Ours."
    hide mac
    hide hiflmc
    $menuhideborder = True
    menu mace2c1:
        "1. Argue with her.":
            $menuhideborder = False
            show hiflmc casual angry at left1
            show mac earstank wolfsurprised at right1 behind hiflmc
            mcmac "Woah, I didn't agree to anything. You are a goddamn werewolf!"
            show mac earstank wolfangry
            ma "And I think it's pretty clear why no one else needs to know that."
        "2. Agree.":
            $menuhideborder = False
            show hiflmc casual sarcastic at left1
            show mac earstank wolfbasic at right1 behind hiflmc
            mcmac "Who would I even tell? The cops?"
            show mac earstank wolfsmirk
            ma "Exactly. That's a good thought, keep it in your head."
        "3. Stay quiet.":
            $menuhideborder = False
            show hiflmc casual sad at left1
            show mac earstank wolfbasic at right1 behind hiflmc
            mcmac "..."
            show mac earstank wolfangry
            ma "I'm serious. This isn't something the town can find out about."
    hide mac
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu

    "(No one would believe me if I said anything. I’m half convinced I’m dreaming.)"
    show hiflmc casual_cu angry_cu
    "(But if I’m not, Grace is still missing.)"
    show hiflmc casual basic at left1
    show mac earstank wolfsurprised at right1 behind hiflmc
    mcmac "Are you out here because of my sister? Have you seen her?"

    ma "No. What happened?"
    show hiflmc casual sad
    mcmac "She’s gone. Grace left in the middle of the night and I have to find her—!"
    show hiflmc casual surprised
    show mac drooptank sleep

    "Mackenzie’s head cocks to the side like she’s listening for something, lip curling as she bares her teeth."
    show mac earstank wolfangry
    "Before I can ask what’s wrong, her ears stand straight up."

    ma "Here, really? Hmm."
    show hiflmc casual sad
    mcmac "Sher--Mackenzie, you have to help me."

    mcmac "She went off with some guy and I'm so worried—"
    hide mac
    show hiflmc casual surprised at centre
    "She bolts off before I can finish my sentence, a blur of shadow that sprints right into the brush and out of view."

    "I’m left there staring, trying to figure out what the hell just happened."

    mcmac "I was still talking."
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(Shit. I have to keep looking for Grace.)"
    show hiflmc casual_cu surprised_cu
    "(Who knows how dangerous the lake is if someone like Mackenzie is...)"
    show hiflmc casual angry at centre
    mcmac "No. You know what, that isn't real until I prove it otherwise."

    mcmac "What is real is my sister's phone."
    show hiflmc casual surprised
    "Returning back to the app with slightly shaky hands,"
    show hiflmc casual sad
    "I try and find where the dot was pointing to again, squinting to see in the grass."
    show hiflmc casual angry
    "I run my fingers through it, searching for any sign of the screen, but there's nothing."

    mcmac "It has to be here."

    mcmac "It's the middle of the night, Grace! Where would you even go?"
    show hiflmc casual sad

    "Exhaustion pours into me as I keep looking,"

    "trying to ignore the part of my mind expecting something to jump out of the bushes and tear me to pieces."
    scene bg lake_moon_fog at bg
    show hiflmc casual sad

    "I finally give up when the clouds pass over the moon, stealing what little light I had to begin with."
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(I'll have to come back in the morning.)"
    show hiflmc casual_cu sad_cu
    "(Grace, please be okay.)"

    scene bg road_day at bg with fade
    stop music fadeout 1.0
    play music hifleveryday
    pause
    show truck_back_day at bg
    show hiflmc beaniecasual basic at right2:
        zoom 1.05
    show truck_front_day at bg

    "I barely sleep."

    "Thankfully, it's my day off, so I head right to the lake after forcing myself to eat something that resembles breakfast."
    hide truck_back_day
    hide hiflmc
    hide truck_front_day
    show bg lake_day at bg
    show hiflmc beaniecasual basic at centre

    "Under the sun, everything looks far less creepy, but I'm still cautious as I boot up the app again."
    show hiflmc beaniecasual sad
    "It doesn't seem like Grace's phone has moved, although there's a battery warning flashing for it now."
    show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
    "(I'm kind of surprised it didn't die overnight.)"
    show hiflmc beaniecasual sarcastic at centre

    mcmac "Alright, if I was a phone where would I be?"

    mcmac "You think the charm on it would make it easy to spot. Stupid grass."
    show hiflmc beaniecasual surprised
    unknown "Have you tried calling it?"

    "I barely hold back a scream, whirling around and holding my phone out like a shield to ward off whoever's behind me."
    show hiflmc beaniecasual surprised at left3
    show mac glassescop sad at right3
    "Mackenzie stands there in her uniform, frowning at my little display."

    ma "Easy there, [genericfn]. It's just me."
    show hiflmc beaniecasual angry
    mcmac "Hey, you startled me. Don't be a jerk... Sheriff."
    show hiflmc beaniecasual_cu basic_cu at hiflmc_cu
    hide mac
    "(She said I could call her by name last night. Is that still okay now?)"
    show hiflmc beaniecasual angry at left3
    show mac glassescop sad at right3

    "I search for any signs of what I saw before."

    "Mackenzie's hair, her teeth, the ears...but nothing seems out of the ordinary."
    show hiflmc beaniecasual basic
    "(She looks a little tired, but I can't really throw stones there.)"
    hide mac
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "(Could I really have imagined all that? How?)"

    show hiflmc beaniecasual basic at left3
    show mac glassescop sad at right3
    mcmac "What happened last night?"
    show mac glassescop surprised
    ma "Excuse me?"

    mcmac "You were here, weren't you? Your car was parked by the lake, I saw the tracks."

    "Mackenzie looks back at where her car is right now, in the exact same place as before."

    "If there were any tracks from the other night, they've been run over."
    show hiflmc beaniecasual angry
    mcmac "I saw you here."
    show mac glassescop
    ma "I'm here because Luce told me your sister didn't show up for work."

    ma "And when I went to your house, it was empty."
    hide mac
    show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
    "(I don't know if I believe Mackenzie, but I need her help."
    show hiflmc beaniecasual sad at left3
    show mac glassescop basic at right3
    mcmac "Grace has been gone since last night."

    mcmac "The only way I have to track her is her cell phone, so I need to find it."
    show mac glassescop angry
    ma "Give Grace a call. I'll walk around and help you find the phone."
    hide mac
    show hiflmc beaniecasual sad at centre
    "I nod, dialling her number and putting the phone to my ear."
    show hiflmc beaniecasual surprised
    "There's a faint buzzing from somewhere, but I honestly can't tell the direction."
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "(That has to be it, though!)"
    show hiflmc beaniecasual surprised at left3
    show mac glassescop basic at right3
    mcmac "Mazkenzie, do you see—!"
    hide hiflmc
    hide mac
    show mackenzie_s1_mini2 at bg
    "She crouches down in the grass, hand coming up covered in mud before I see the phone held gingerly between her fingertips."

    "Grace’s charm angles from the side of it, the screen cracked but still lit up."
    hide mackenzie_s1_mini2
    show bg lake_day at bg
    show hiflmc beaniecasual surprised at left3
    show mac glassescop sad at right3
    ma "Looks like it might have been dropped and stepped on."
    ma "But I don't see any sign of your sister."

    mcmac "Can I see it?"
    show mac glassescop basic
    ma "It's evidence now."

    ma "Let me get a bag out of my car so I can bring it back to the station."
    hide mac
    show hiflmc beaniecasual sad at centre
    "I watch as Mackenzie seals the phone up, wanting more than anything to unlock it and see if my message got to Grace."

    "Did she know I've been trying so hard to find her?"
    show hiflmc beaniecasual sad at left3
    show mac glassescop basic at right3
    mcmac "Is this a missing person case now?"
    show mac glassescop sad
    ma "Officially, I'm supposed to wait three days."

    ma "But I know your sister, and I know she's not a runaway. I'll open a file."

    mcmac "Thank you."

    ma "How are you doing with this, [genericfn]?"
    hide mac
    hide hiflmc
    $menuhideborder = True
    menu mace2c2:
        "1. Tell her you're fine.":
            $menuhideborder = False
            show hiflmc beaniecasual sad at left3
            show mac glassescop basic at right3
            mcmac "I'm fine..."
        "2. Be honest.":
            $menuhideborder = False
            hide mac
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(Whatever did happen last night, I know Mackenzie cares. She wouldn't ask if she didn't.)"
            show hiflmc beaniecasual sad at left3
            show mac glassescop sad at right3
            mcmac "I'm scared to death. I've lost so many people."
            mcmac "Our parents, grandparents... I can't lose Grace."
        "3. Time for sarcasm.":
            $menuhideborder = False
            hide mac
            show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
            "(How am I supposed to be doing?)"
            show hiflmc beaniecasual sarcastic at left3
            show mac glassescop sad at right3
            mcmac "Oh, I'm great. Worn out, casually losing my mind."
            mcmac "All I need is a guy showing up to say he has a bridge to sell me."
    stop music fadeout 1.0
    play music hiflliteromance
    hide hiflmc
    show mac glassescop_cu sad_cu at mac_cu
    ma "Hey."

    "Mackenzie reaches out to touch my shoulder, giving it a light squeeze."

    "The touch is brief, but I breathe a little easier after it."
    show mac glassescop_cu basic_cu
    ma "We'll get this sorted out. But I have to get back to the station, alright?"
    hide mac
    show hiflmc beaniecasual_cu happy_cu at hiflmc_cu
    mcmac "Okay. Thanks."
    hide hiflmc
    show mac glassescop basic at centre
    "She goes back to her car and starts up the engine, revving hard to get out of the mud and back towards the main road."

    scene bg road_day at bg
    stop music fadeout 1.0
    play music hifleveryday
    $menuhideborder = True
    pause
    $menuhideborder = False
    show truck_back_day at bg
    show hiflmc beaniecasual basic at right2:
        zoom 1.05
    show truck_front_day at bg


    "I end up following Mackenzie’s car back into town."
    show hiflmc beaniecasual blush at right2:
        zoom 1.05
    "It’s not on purpose—we only have one good road."

    "But at least the view is nice on the way back to Main Street."

    "(Weird dream or not, she’s gorgeous and it’s unfair.)"

    "(If we’d been in high school together, I probably would have gone to her softball games.)"
    scene bg main_day at bg
    show truck_back_day at bg
    show hiflmc beaniecasual basic at right2:
        zoom 1.05
    show truck_front_day at bg
    "Mackenzie makes a sharp turn into the parking lot for the sheriff station  and I slow down to a halt at the nearby red light,"
    "trying to figure out what to do next."
    hide hiflmc
    $menuhideborder = True
    menu mace2c3:
        "1. Follow Mackenzie to the sheriff's office." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc beaniecasual basic at right2 behind truck_front_day:
                zoom 1.05
            "(I want to know what Mackenzie's doing with Grace's phone.)"
            show hiflmc beaniecasual sad
            "(And if I can find out anything more about last night. It felt too real.)"
            show hiflmc beaniecasual basic
            "I wait until Mackenzie goes into the office to bring my car around, hanging on the far side of the parking lot so my car isn't obvious from the front."
            hide truck_back_day
            hide hiflmc
            hide truck_front_day
            show mac glassestank basic at centre
            "I'm ready to cool my heels for a while, but she comes right back out, uniform shirt stripped off."
            hide mac
            show truck_back_day at bg
            show hiflmc beaniecasual surprised at right2:
                zoom 1.05
            show truck_front_day at bg
            mcmac "Huh?"
            show hiflmc beaniecasual blush
            "I've always known Mackenzie was ripped, but it's something to see the flex of bronze muscle as she tosses something ragged and black in the trash."
            show hiflmc beaniecasual surprised
            "A second later, I realise it was a tank top, just like the one she's wearing now."
            stop music fadeout 1.0
            play music mackenziehunt
            "(Wait a second.)"

            "(Why was the other one torn to pieces?)"
            hide truck_back_day
            hide hiflmc
            hide truck_front_day
            show mac glassescop basic at centre
            "She leans back against the car while pulling her uniform shirt back on, doing up the buttons and re-adjusting the radio."
            show mac glassescop sad at centre
            "Then Mackenzie takes out my sister's phone, now wiped clean of mud."
            hide mac
            show truck_back_day at bg
            show hiflmc beaniecasual angry at right2:
                zoom 1.05
            show truck_front_day at bg
            mcmac "Uh, that's supposed to be in an evidence bag."

            mcmac "What the hell is going?"

            "I'm ready to start my engine again, expecting her to get back in the car,"
            hide truck_back_day
            hide hiflmc
            hide truck_front_day
            show mac glassescop basic at centre
            "But Mackenzie walks out of the parking lot."

            "After checking the street both ways, she pockets Grace's phone and crosses over right towards the bowling alley."
            hide mac
            show truck_back_day at bg
            show hiflmc beaniecasual angry at right2:
                zoom 1.05
            show truck_front_day at bg
            mcmac "Okay, this has gone from weird to suspicious."

            mcmac "I'm getting that phone back."
            hide truck_back_day
            hide hiflmc
            hide truck_front_day
            show hiflmc beaniecasual basic at centre
            "After slipping out of my truck, I cross the street too, but round the building towards the employee entrance."

            "Razi doesn't really like me mucking around back there, but I don't want Mackenzie to see me."
            hide hiflmc
            show bg bowling at bg
            show razi casual basic at left3
            show mac glassescop basic at right3
            "With care, I open the door into the bowling alley proper, catching sight of Razi standing next to Mackenzie."
            hide razi
            hide mac
            show diego doctor glassesbasic at centre
            "What's even stranger is Diego Escalona, our town doctor, right in the middle of their conversation."
            hide diego
            show razi casual sad at left3
            show mac glassescop basic at right3
            ra "Are you sure about this, Mac?"
            show mac glassescop angry
            ma "Look, there's one wolf's scent in this town and it's mine. I noticed a second one the other night."

            ma "Someone had shifted near the lake."
            hide razi
            show diego doctor glassesbasic at left3
            di "Do you need our help tracking them down?"
            show mac glassescop sad
            ma "No, this is my territory. I'll find them myself."

            ma "But I thought it was only fair that everyone else knew."
            hide diego
            show razi casual smirk at left3
            ra "Don't want the weres getting a bad rep?"
            show mac glassescop angry
            ma "There's a reason I'm not part of a city pack, alright?"
            hide razi
            show diego doctor glassesbasic at left3
            di "You've never elaborated."

            ma "Just take my word for it, doctor."
            hide diego
            hide mac
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
            "(Pack? Wolf?)"

            "(Holy shit. I wasn't seeing things.)"
            hide hiflmc
            show diego doctor glassesbasic at left3
            show mac glassescop basic at right3
            ma "Honestly, that's not my biggest concern right now."

            di "Dare I ask what's more concerning than that?"
            show mac glassescop sleep
            ma "[genericfn] might have seen me shift during the full moon."
            show diego doctor glassessurprised
            show mac glassescop sad
            di "Ms. [genericln]?"

            ma "Yeah."
            hide diego
            show razi casual sleep at left3
            "Razi reaches up to squeeze the bridge of his nose, the way he does whenever he's particularly stressed."
            show razi casual sad at left3
            ra "Uh, that's kind of a problem."
            show mac glassescop basic
            ma "But I talked to her this morning. She seemed pretty calm."

            ma "I managed to convince her she didn't see anything."
            hide mac
            hide razi
            show hiflmc beaniecasual_cu angry_cu at hiflmc_cu
            "(That's not true! She told me to keep everything secret.)"
            hide hiflmc
            show diego doctor glassesangry at left3
            show mac glassescop basic at right3
            di "How sure are you of that?"
            show mac glassescop smirk
            ma "I don't think she would have let me help her find her sister's phone if she thought I was a werewolf, Diego."
            hide diego
            show razi casual smirk at left3
            ra "Have you considered the fact that you're impressively intimidating?"
            show razi casual happy
            "She rolls her eyes at him and Razi smiles, nudging Mackenzie's shoulder like it's an old joke."
            hide razi
            hide mac
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
            "(I didn't think they knew each other that well. Razi's almost never mentioned her.)"

            unknown "Fascinating stuff, huh?"
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu:
                xpos 250
            show jd tank_cu smirk_cu at jd_cu:
                xpos 750

            "A voice whispers right against my ear and I scream, jumping away and out of the shadows."
            show hiflmc beaniecasual surprised at left3
            show jd tank smirk at right3
            "When I turn around, Jordan is leaning against the doorway, carefree as ever."
            show hiflmc beaniecasual angry
            mcmac "Why did you do that? You scared me half to death!"

            ra "Hey, what's going over there?"

            "The boom in Razi's voice tells me I've been caught..."
            hide hiflmc
            hide jd
            stop music fadeout 1.0
            play music hiflmaintheme
            show mac glassescop_cu angry_cu at mac_cu
            "And when I look back to the group, my eyes lock with Mackenzie's."

            "She crosses her arms and I swallow hard, wondering how I'm going to get out of this."
            hide mac
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu

            "(It's fine. She's just...)"

            "(A werewolf. I am in so much trouble.)"
            hide hiflmc
            $tobecontinued()
            show bg hifltbc
            with fade

            pause
            $ resets()
        "2. Ask around town.":
            $menuhideborder = False
            show hiflmc beaniecasual basic at right2 behind truck_front_day:
                zoom 1.05

            "(She’s already going to take care of the phone. I should do something else with my time.)"
            show hiflmc beaniecasual sad
            mcmac "Maybe Grace got into a car accident with this dude or something?"

            mcmac "Went off to find help..."

            mcmac "She knows I'd be a little pissed off about the phone too."

            mcmac "Guess I should ask around."
            hide truck_back_day
            hide truck_front_day
            hide hiflmc
            show hiflmc beaniecasual basic at centre
            "I know Luce hasn’t seen my sister at work so I make a turn back towards the houses in town and park my truck on a side street."
            show mailman casual basic at centre
            "The mail carrier is on his rounds around town, so I wave to him."
            show hiflmc beaniecasual basic at left4
            show mailman casual basic at right4
            mail "Ms. [genericln]. Mornin'."
            show hiflmc beaniecasual sad
            mcmac "Hey. Sorry to bother you, but have you seen Grace around today?"

            mcmac "Or last night?"

            mail "She was at Luce's in the afternoon when I went for lunch."
            show hiflmc beaniecasual angry
            mcmac "Yeah, she was working."
            show hiflmc beaniecasual basic
            mcmac "But after her shift, Grace left and I wasn't able to find her."

            mail "Did she take your truck too?"

            mcmac "No. The guy she went with must've had a car."

            "He raises a brow, disapproval radiating from his expression."

            mail "I'd ask that boy, then. Maybe he took her up north for one of those college parties."
            show hiflmc beaniecasual angry
            mcmac "Grace doesn't party."

            mail "Plenty of girls don't until a boy asks them to."

            mcmac "You're making it sound like this is her fault."

            mail "I'm saying she's young and that makes kids reckless."

            mail "Got no parents to keep her in line."
            hide mailman
            show hiflmc beaniecasual_cu angry_cu at hiflmc_cu
            "Anger squeezes tight around my heart and I storm away before saying something I'll regret."

            "It takes me a minute by the truck to calm down again, but somehow after a few deep breaths I manage to do it."
            show hiflmc beaniecasual sad at centre
            "I walk down to the next house and knock on the door."

            "Almost everyone says the same thing."

            "If I mention the guy, they assume she ran off to have fun, and the rest mention Grace was always weirdly quiet."
            show hiflmc beaniecasual_cu angry_cu at hiflmc_cu

            "(She’s just shy! God, she wasn’t even ten when our parents died.)"

            "(And everyone started to treat us like we caused it.)"

            "(As if our family’s cursed.)"
            show hiflmc beaniecasual angry at centre
            mcmac "I hate this place."

            mcmac "We wouldn't even live here if I could afford better."

            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "Too wrung out to keep questioning people, I pile back into my truck and head towards the bowling alley."

            "If anyone will be understanding, it’s Razi."

            "There’s a couple of cars in the parking lot, including one I don’t recognise, and I curse under my breath."
            show hiflmc beaniecasual_cu sarcastic_cu
            "(Of all days for us to actually have customers.)"

            scene bg bowling at bg
            stop music fadeout 1.0
            play music mackenziehunt
            "Ducking in through the front, I’m surprised to see the lanes empty."
            show razi casual basic at left3
            show jd tank basic at right3
            "Razi is standing by the counter next to Jordan, but they’re not alone."
            hide jd
            hide razi
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
            "(What is Dr. Escalona doing here? And Mackenzie?)"
            hide hiflmc
            show diego doctor glassesbasic at left3
            show mac glassescop angry at right3
            doc "You realise what kind of problems this could cause?"

            ma "I'm not a fool, Diego."

            ma "Just because I haven't been around as long as you have doesn't mean I can't deal with this."
            hide mac
            hide diego
            show razi casual basic at left3
            show jd tank basic at right3
            jd "It's not just you we have to worry about."

            ra "We're not as obvious, JD."
            show jd tank angry
            jd "Have you ever seen a real witch hunt? It doesn't matter what's obvious."

            jd "They just pick out what looks different."
            hide razi
            show mac glassescop sad at left3
            ma "[genericfn] did see me change, but only partially."

            ma "If I could go full wolf, I probably would have run away instead."
            show mac glassescop basic
            ma "But I had to work with what I had."
            hide mac
            hide jd
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
            "('Full wolf'?)"
            "(I knew it! I wasn't hallucinating at all!)"
            hide hiflmc
            $tobecontinued()
            show bg hifltbc
            with fade

            pause
            $ resets()
