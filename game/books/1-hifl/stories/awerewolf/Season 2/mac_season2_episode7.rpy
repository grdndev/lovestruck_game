label mac_season2_episode7:

    $tbc = False
    scene bg mackenzie_bedroom_night at bg
    play music hiflaction

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show mac naked sleep at centre
    "Mackenzie stirs from sleep, but not fast enough."
    show mac naked surprised at left5 behind hiflmc
    show hiflmc naked noglassessurprised at left2
    "I throw myself towards her with all the force I can muster, the desperate tackle knocking us both off the bed."

    "The sound of fabric being roughly shredded meets my ears, but after the missed attack, I hear a low growl of frustration."

    "Whisper-soft footsteps carry out the door of Mackenzie's room before it's slammed shut."
    hide mac
    hide hiflmc naked_cu noglassessurprised_Cu at hiflmc_cu
    "(What the hell was that?!)"

    "(Who the hell was that?!)"
    stop music fadeout 1.0
    play music mackenziehunt
    hide hiflmc
    show mac naked surprised at left5 behind hiflmc
    show hiflmc naked noglassessurprised at left2
    mcmac "Mac, are you okay?"
    hide hiflmc
    hide mac
    show mac naked_cu basic_cu at mac_cu
    "Looking down at her, my eyes adjust enough to the dark to make out her face."

    "There's no blood, no sign of pain or injury."
    show mac naked_cu angry_cu
    "But she looks pretty pissed."

    ma "Yeah, I'm fine."

    ma "Except for the part where someone just broke into my house to shred me in two."
    hide mac
    show mac naked angry at left4
    show hiflmc naked noglassessad at right4
    "I get up off of her to sit on the edge of the bed and calm the adrenaline making my heart ricochet inside of my chest."

    "Mackenzie settles next to me, letting out a deep breath before her hands relax from clenched fists."
    show mac naked basic
    ma "Did you see anything? Any hint of who it was?"
    show hiflmc naked noglassesbasic
    mcmac "Just some really big claws."
    show hiflmc naked noglassessad
    mcmac "That's all I could focus on, especially after I saw them aimed at you."
    mcmac "Do you think it was Beau? Or one of his pack?"

    ma "That was the first thing that came to mind."
    show mac naked sad
    ma "Except there's one problem. The only wolf's scent in this air is mine."
    show hiflmc naked noglassessurprised
    mcmac "What's it smell like then?"
    show mac naked sleep
    "Mackenzie shakes her head, frustration creasing her brow."
    show mac naked angry
    ma "Nothing."

    ma "Nothing except for you. So whoever just made their move is smart."
    hide mac
    hide hiflmc
    show hiflmc naked_cu noglassessurprised_cu at hiflmc_cu
    "(They hid their scent before coming after Mac?)"

    "(That's scary. That means they knew exactly who they were up against.)"
    hide hiflmc
    show mac naked basic at left4
    show hiflmc naked noglassesbasic at right4
    mcmac "Is there anything we can do?"
    show mac naked angry
    ma "I'm not going to go running around in the middle of the night for someone who just tried to kill me."

    ma "That's asking to be led into a trap. Or wearing myself out before tomorrow."
    show hiflmc naked noglassessurprised
    "For a moment, I'm quietly amazed. Even after something like this, Mackenzie's keeping a cool, logical head on her shoulders."
    show hiflmc naked noglasseshappy
    "Underneath all her kindness and courage is a core of iron, absolutely unshakeable."
    show mac naked basic
    ma "You should go back to sleep."
    hide mac
    hide hiflmc
    $menuhideborder = True
    menu macs2e7c1:
        "A. Are you going back to sleep?":
            $menuhideborder = False
            show mac naked basic at left2
            show hiflmc naked noglasseshappy at right2
            mcmac "Are you going back to sleep?"

            ma "I'll be laying down in bed."

            ma "Not sure the wolf is going to be quiet enough to let me pass out again, though."
            hide mac
            hide hiflmc
        "B. Give Mackenzie a hug.":
            $menuhideborder = False
            show mac naked basic at left2
            show hiflmc naked noglasseshappy at right2
            "I wrap my arms around Mackenzie's shoulders, giving them a tight squeeze."
            show mac naked sleep
            "She sighs, leaning her head back against mine, and her next breath sounds a little less tense."
            hide mac
            hide hiflmc
        "C. I'm so awake.":
            $menuhideborder = False
    show hiflmc naked_cu noglassesbasic_cu at hiflmc_cu
    "(I can at least make the attempt to sleep.)"
    hide hiflmc
    hide mac
    show hiflmc naked noglassessurprised at centre
    "At least until I see the ragged state of Mackenzie's pillow."
    show mac naked basic at left4
    show hiflmc naked noglassessad at right4
    mcmac "Um, you might need to toss that one out."

    ma "Yeah."

    ma "I'll just share with you if you don't mind."
    show hiflmc naked noglasseshappy
    mcmac "Of course, Mac. It's your bed."
    show mac naked smirk
    "I catch a hint of a smile as she balls up the destroyed pillow and tosses it towards the little garbage can on the opposite end of the room."

    "It lands with a muffled thump of cotton, out of the way until tomorrow."
    show mac naked basic at left2 behind hiflmc
    show hiflmc naked noglassesbasic at right2
    stop music fadeout 1.0
    play music hiflliteromance
    "Once I'm laying down and tucked under the blankets again, Mackenzie presses against my back and loops one of her arms around my stomach."
    show mac naked sleep
    "She takes in my scent with a slow inhale along my nape, letting out a soft sound afterwards."
    show hiflmc naked noglasseshappy
    show mac naked smirk
    mcmac "What was that little grin for?"
    show mac naked happy
    ma "Because I like thinking about you in my bed."

    ma "But since we're sharing, I guess it's our bed, huh?"
    show hiflmc naked noglassesblush
    "My face turns pink at the thought, but I nod, cupping my hand over Mackenzie's and giving it a small squeeze."
    show mac naked basic
    show hiflmc naked noglassessad
    mcmac "You sure you'll be okay?"

    ma "I'm good, just on high alert."

    ma "Get some sleep. We'll figure this out in the morning."
    hide mac
    hide hiflmc
    "For a while, I just lay there with my eyes closed. But eventually, Mackenzie's warmth lulls me back to sleep."
    scene bg bowling at bg
    stop music fadeout 1.0
    play music hifllitegetitdone
    pause
    show mac glassescop sad at left4
    show hiflmc bowling sad at right4
    "Mackenzie escorts me to the bowling alley the next morning, and even the warm coffee in our hands can't quite stave off the fatigue."
    hide hiflmc
    hide mac
    show razi casual basic at left4
    show diego doctor basic at right4
    "Razi and Diego are waiting by the bar when we walk in, with JD standing on a table in the middle, swapping out one of the cosmic lights."
    hide razi
    hide diego
    show jd tank basic at left4
    show gwen casual surprised at right4
    "Gwen is holding the box of bulbs by their feet, looking up like she expects the whole thing to fall."
    hide gwen
    show hiflmc bowling happy at right4
    mcmac "Having fun up there?"
    show jd tank smirk
    jd "What's a morning without the chance of electrocution?"
    show hiflmc bowling basic
    show jd tank sad
    jd "Or whatever happened to you last night. You look exhausted, [genericfn]."
    hide hiflmc
    show mac glassescop sad at right4
    jd "You too, Sheriff."
    hide mac
    show hiflmc bowling angry at right4
    mcmac "Someone tried to kill Mac while we were sleeping."
    show jd tank surprised
    "The bulb in JD's hand cracks, and they carefully take their fingers off it before jumping down off the table."

    jd "Run that by me one more time."
    hide jd
    hide hiflmc
    show mac glassescop basic at left4
    show razi casual surprised at right4
    ra "Did you say 'kill'?"
    show mac glassescop angry
    ma "Claws aiming for my throat gives a pretty clear message."
    hide razi
    show diego doctor basic at right4
    "Diego immediately gets up out of his seat, eyes sweeping over Mackenzie with a doctor's analytic intensity."
    show mac glassescop basic
    ma "They missed."

    ma "The only victim was my pillow, thankfully."
    show diego doctor angry
    di "Well, I'm glad to hear that, but it doesn't downplay the gravity of the attempt."
    hide mac
    hide diego
    show gwen casual surprised at centre
    "There's a loud jangle as Gwen drops the box of bulbs on the table, shrinking back into herself with guilt written all over her face."

    gwe "It's because of me, isn't it?"

    gwe "Beau knows you're protecting me, so he sent someone to hurt you for it."
    show mac glassescop happy at right4
    show gwen casual surprised at left4
    "Mackenzie flashes a tired but genuine smile her way."

    ma "Don't blame yourself for that, Gwen."
    show mac glassescop basic
    ma "I knew what risks I was taking when I offered to keep you safe."
    hide mac
    hide gwen
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I'd definitely prefer if Mackenzie didn't get torn up over some girl we barely know, though.)"
    hide hiflmc
    show razi casual basic at right4
    show mac glassescop basic at left4
    ra "What do you think, Mac? Any chance it's Damien?"
    show mac glassescop sad
    ma "I honestly don't know."

    ma "There was no scent for me to track, and I didn't even see them. [genericfn] did."
    hide mac
    hide razi
    show hiflmc bowling sad at centre
    mcmac "I saw claws. Really scary claws."
    hide hiflmc
    show jd tank sad at centre
    jd "Well, that definitely doesn't rule out another werewolf."
    hide jd
    show diego doctor basic at centre
    di "I'm not sure the culprit is Damien, however."

    di "If he was smart enough to mask his scent, I think he would have done it long before now."
    hide diego
    show razi casual angry at centre
    ra "Unless he's getting advice from Papa Wolf now."
    hide razi
    show mac glassescop basic at centre
    ma "I'd be surprised if Beau gave Damien anything more than a very unpleasant drive in the back of his truck."

    ma "He won't be trusted anymore, not after losing to me. I was untried, Damien was experienced."
    show mac glassescop basic at left4
    show jd tank basic at right4
    jd "He was fighting an alpha."

    ma "Which is why he lost. But it still makes the whole Rider pack look bad."
    hide jd
    hide mac
    $menuhideborder = True
    menu macs2e7c2:
        "A. They deserve it.":
            $menuhideborder = False
            show mac glassescop basic at left4
            show hiflmc bowling angry at right4
            mcmac "They deserve to look bad."
            mcmac "Everyone was minding their business in Havenfall before Damien showed up and took Grace."
            mcmac "The Riders should have stayed in Wisconsin."
            hide hiflmc
            hide mac
        "B. So now Beau wants revenge.":
            $menuhideborder = False
            show mac glassescop basic at left4
            show hiflmc bowling basic at right4
            mcmac "So now Beau wants revenge."
            show hiflmc bowling angry
            mcmac "To what, put a band-aid over his bruised ego?"
            hide mac
            show diego doctor sad at left4
            di "That, unfortunately, is why many men have gone to war."
            hide diego
            hide hiflmc
        "C. Don't these guys give up?":
            $menuhideborder = False
            mcmac "Don't these guys ever give up?"

            mcmac "They had Mac outnumbered and still lost. What can one assassin do?"

            jd "Ambush her, I guess. But I guess they should have gotten someone better."
    show razi casual basic at left2
    show gwen casual surprised at right2
    "The more we talk, the more uncomfortable Gwen looks, and Razi intervenes by putting a hand on her shoulder."

    ra "This doesn't change anything, okay?"

    ra "We've all just got to keep an eye out."
    hide razi
    hide gwen
    show diego doctor basic at centre
    di "Agreed. Anyone who has been targeted should avoid being alone."
    hide diego
    show jd tank basic at left4
    show hiflmc bowling basic at right4
    jd "That includes you, [genericfn]."
    show jd tank angry
    jd "Just because that whackjob went for Mackenzie first doesn't mean they wouldn't have taken you out second."
    hide jd
    show mac glassescop angry at left4
    ma "They're right."
    hide mac
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Oof, I hadn't even thought about that.)"
    hide hiflmc
    show mac glassescop basic at left4
    show hiflmc bowling basic at right4
    mcmac "I'll be safe here at work."
    hide mac
    hide hiflmc
    show diego doctor basic at left4
    show gwen casual basic at right4
    di "And I can escort you to the diner, Gwen."
    show gwen casual happy
    "She gives him a little smile."

    gwe "Thanks."
    hide gwen
    hide diego
    show mac glassescop basic at left4
    show jd tank smirk at right4
    jd "Want me to walk across the street with you, sheriff? I'll even pretend to be arrested if it makes you feel better."
    hide jd
    show mac glassescop smirk at left1
    show hiflmc bowling blush at right2
    "Mackenzie rolls her eyes before turning to give me a firm kiss."

    "It lasts a little longer than I expect, and I hear Razi clear his throat."
    hide mac
    hide hiflmc
    show razi casual smirk at centre
    ra "If I didn't know better, I think she wants to take [genericfn] with her."
    hide razi
    show mac glassescop smirk at left1
    show hiflmc bowling happy at right2
    ma "Tempting."
    show mac glassescop happy at left4
    show hiflmc bowling happy at right4
    ma "But I'll be fine."

    "She pulls away from me with a cheeky grin, ignoring JD's imitation of a wolf's howl on Mackenzie's way out of the bowling alley."
    hide mac
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I miss her already.)"
    show hiflmc bowling_cu basic_cu
    "(Oh, well. Time for work.)"
    scene bg bowling_cosmic at bg with clockwise_wipe
    stop music fadeout 1.0
    play music hifleveryday
    show hiflmc bowling basic at centre
    "My shift is completely boring, which is a mercy for once."

    "I keep running over the attack from last night, trying to pick out any detail or clue about the would-be assassin."
    show hiflmc bowling sad
    "(But there's nothing.)"
    show hiflmc bowling basic
    "To cheer myself up, I go to the diner to pick up some food for me and Mackenzie."
    scene bg diner_lights_on at bg with wipeleft
    show luce casual basic at centre
    "Today's special is burgers, and Luce seems to have the milkshake machine up and running today."
    hide luce
    show hiflmc bowling basic at centre
    mcmac "Hey, can I get two specials to go?"

    mcmac "And two milkshakes, one chocolate and one strawberry."
    hide hiflmc
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(I'm not sure of Mac's favorite, but I like both, so I'll drink whichever one she doesn't want.)"
    hide hiflmc
    show luce casual basic at centre
    lu "Sure thing."
    show luce casual basic at left4
    show gwen waitress basic at right4
    lu "Gwen, can you handle the grill while I get more ice cream out of the back?"
    show gwen waitress happy
    gwe "You bet, boss."
    show gwen waitress basic
    show hiflmc bowling basic
    "Luce disappears behind the far door, leaving me alone with Gwen while she works behind the counter."

    "After tossing two beef patties onto the grill, she looks back over her shoulder at me."
    show gwen waitress happy
    gwe "You want the works? Tomatoes and everything?"

    mcmac "Yeah, that's fine."

    "Gwen rolls two tomatoes out of the nearby bag onto a cutting board."
    hide hiflmc
    hide gwen
    show mackenzie_s2_mini8 at bg
    stop music fadeout 1.0
    play music mackenziehunt
    "Then a set of razor-sharp claws pop out of her fingertips, slicing the first fruit into half a dozen juicy, red pieces."
    hide mackenzie_s2_mini8
    show bg diner_lights_on at bg
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(The fuck?!)"
    hide hiflmc
    show hiflmc bowling surprised at left4
    show gwen bansheewaitress bansheebasic at right4
    mcmac "Gwen, what are you doing?"

    "'What are you' is on the tip of my tongue, but I bite it back."

    "She gives me an innocent look, flicking the seeds off the claws with a twitch of her wrist."
    show gwen bansheewaitress bansheehappy
    gwe "Doing it faster."

    gwe "I mean, Luce isn't here."
    show hiflmc bowling angry
    mcmac "She could be any second. You can't use your powers in public."

    mcmac "...Whatever they happen to be."
    show gwen bansheewaitress bansheebasic
    gwe "But you know I'm not human."

    $menuhideborder = True
    menu macs2e7c3:
        "A. I'll tell Mackenzie.":
            $menuhideborder = False
            show hiflmc bowling angry at left4
            show gwen bansheewaitress bansheebasic at right4
            mcmac "I'll tell Mackenzie if you do that again."

            mcmac "You know she won't be happy that you're revealing yourself."

        "B. Rules are rules.":
            $menuhideborder = False
            show hiflmc bowling angry at left4
            show gwen bansheewaitress bansheebasic at right4
            mcmac "Rules are rules."

            mcmac"People can see you through the diner windows too, you know."

        "C. That doesn't matter.":
            $menuhideborder = False

    gwe "..."
    show gwen waitress basic at right4 with dissolve
    "Her claws slide back out of view, and for a long moment I stare at Gwen's fingers."
    show hiflmc bowling surprised
    "There's no sign of the change at all; her nails aren't even sharp."
    hide gwen
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(So why is my heart beating so fast?)"

    "(Were Gwen's claws like the ones I saw? Were they more like Damien's?)"
    hide hiflmc
    show bg mackenzie_bedroom_night at bg with dissolve
    "I close my eyes, trying to picture the scene all over again."
    show bg diner_lights_on at bg with dissolve
    show hiflmc bowling sad at centre
    "It was such a blur in the dark, a split second view before I moved to protect Mackenzie."

    mcmac "I just don't know."
    show hiflmc bowling sad at left4
    show luce casual basic at right4
    stop music fadeout 1.0
    play music hifleveryday
    lu "Something wrong with your order, girl?"
    show hiflmc bowling surprised
    "I snap to alertness at Luce's voice."

    "She's standing right in front of me, the bag of burgers and shakes right next to the register."
    show hiflmc bowling basic
    mcmac "No, I'm ready to pay. Sorry."

    lu "Doesn't look like you're getting enough sleep."

    mcmac "Something like that."

    mcmac "Had a long night."

    lu "I see."

    "She takes my money and hands back the change with the receipt."

    "A curious glint enters Luce's eyes, and I gulp."
    hide hiflmc
    hide luce
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Nothing's more persistent than a Midwest woman chasing a rumor.)"
    hide hiflmc
    show hiflmc bowling basic at left4
    show luce casual basic at right4
    lu "It seems like you and Sheriff Hunt have been spending a lot of time together lately."

    mcmac "I...uh."
    hide hiflmc
    hide luce
    show hiflmc bowling_cu normal_cu at hiflmc_cu
    "(Mac didn't say we couldn't be public, but she and didn't talk about it either.)"
    hide hiflmc
    show hiflmc bowling happy at left4
    show luce casual basic at right4
    mcmac "Yeah, I guess. She's pretty great."
    show hiflmc bowling angry at left5
    show luce casual basic at right3
    show gwen waitress happy at right5
    "I catch Gwen snickering into her hand behind Luce, and narrow my eyes, hoping she feels my glare burning through her back."
    hide gwen
    show hiflmc bowling basic at left4
    show luce casual basic at right4
    mcmac "Why does it matter?"

    lu "It doesn't."

    lu "You've just always been a loner, is all. Change stands out."
    hide hiflmc
    hide luce
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(But my sister being gone doesn't.)"

    "(I've been a loner because being the designated 'weird girl' since grade school means trying to make friends wasn't worth it.)"
    hide hiflmc
    show hiflmc bowling basic at left4
    show luce casual basic at right4
    mcmac "Guess so."
    mcmac "Thanks for the food."
    hide luce
    show hiflmc bowling basic at centre
    "I sweep the bag up into my arms and head for the door."
    show hiflmc bowling happy
    "Unsettled as I am, I still have dinner with Mackenzie to look forward to."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
