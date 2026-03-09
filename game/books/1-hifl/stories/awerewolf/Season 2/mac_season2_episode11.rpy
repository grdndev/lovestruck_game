label mac_season2_episode11:

    $tbc = False
    scene bg hifl_sheriff at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show mac cop basic at centre
    "Mackenzie sits down at her desk, expression grim."
    show mac cop angry at left3
    show elmer casual basic at right3
    "The faint click of keys catch her attention, and irritation flares across a furrowed brow when Mackenzie's eyes lock on Elmer's typing."

    ma "Deputy."
    show elmer casual surprised
    elm "...Yes, Sheriff?"

    ma "Go on patrol."

    elm  "Right now?"

    ma "I don't need you uncuffing any more suspects, so yes, right now."
    hide mac
    show hiflmc beaniebowling basic at left3
    "Elmer's chair squeaks as he gets out of it a bit too fast, shuffling past me to go out the door."
    hide hiflmc
    hide elmer
    "Before it closes, though, someone's hand catches it."
    show jd casual shadesbasic at centre
    jd "Yeah, she's in here. Come on."
    hide jd
    show razi casual basic at left3
    show diego casual glassesbasic at right3
    "Diego and Razi follow them into the office, doing a quick scout around to make sure we don't have any company. We don't."
    hide diego
    hide razi
    show mac cop basic at centre
    ma "Is there something I can help y'all with, because my day is not going well."
    show maco cop basic at left3
    show diego casual glasses basic at right3
    di "That's what we're here about, actually."
    hide diego
    show jd casual shadesangry at right3
    jd "Yeah, we caught the crowd outside."

    jd "Then I saw Gwen in the middle of her little entourage."
    hide jd
    show razi casual sad at right4
    ra "I know she made friends fast, but that's a little..."
    hide mac
    hide razi
    $menuhideborder = True
    menu macs2e11c1:
        "A. Twilight Zone?":
            $menuhideborder = False

        "B. Weird for an assassin?":
            $menuhideborder = False
            mcmac "Weird for an assassin?"

            ra "Exactly."

            ra "That's never struck me as a particularly social line of work."

        "C. It's bullshit.":
            $menuhideborder = False
            show hiflmc beaniebowling angry at left3
            show razi casual sad at right3
            mcmac "It's bullshit. She's messing with them."

            ra "I can't say I'm surprised."

            ra "That seems to be a trend with her, doesn't it?"
    hide hiflmc
    hide razi
    show mac cop sleep at centre
    "Mackenzie sighs, trying to rub the tension away from either side of her head."
    show mac cop sad
    ma "It's not about friends."

    ma "If the town doesn't trust me, I can't do my job."

    ma "If I can't do my job, there's no law here."

    ma"And I can't even tell them they're carting a killer around."
    show mac cop angry
    "Frustration bleeds into a growl, and Mackenzie's shoulders lock up."
    show mac cop angry at left3
    show hiflmc beaniebowling sad at right3
    mcmac "Mac, it's not your fault."

    ma "Yes, it is."

    ma "I let her stay here, I invited her."
    hide hiflmc
    show diego casual glassesbasic at right3
    di "Because she came begging for your help, pretended to be vulnerable."

    di "No one here is judging you for following your better nature, Mackenzie."

    di "That's why you're good at what you do."
    hide diego
    show razi casual angry at right3
    ra "And we'll help you stop Gwen."

    ra "Even if the town's got the wrong idea."
    hide mac
    hide razi
    show jd casual shadesangry at centre
    jd "Please, it has to be a power of hers. Does she sing?"

    "Everyone in the room goes quiet, staring at JD for a moment."

    "They raise an eyebrow right back."

    jd "It's a serious question."

    jd "Sirens can seduce the masses with a song."
    hide jd
    show hiflmc beaniebowling_cu basic_cu at hiflmc_cu
    "(I guess they would know.)"

    "(JD has some superpowered persuasion of their own.)"
    hide hiflmc
    show mac cop basic at left3
    show jd casual shadesbasic at right3
    ma "No, I never caught her singing."
    hide mac
    show hiflmc beaniebowling basic at left3
    mcmac "Gwen screamed, though. Right after Mac arrested her."
    show hiflmc beaniebowling sad
    mcmac "Like the definition of 'bloodcurdling' type scream."
    show hiflmc beaniebowling surprised
    jd "Oh. Then she's a banshee."
    hide hiflmc
    show razi casual surprised at left3
    ra "How did you just figure that out?"
    show jd casual shadesangry
    "JD rolls their eyes."

    jd "I'm not from here, remember? I've run into all sorts."
    hide razi
    show diego casual glassessurprised at left3
    di "Are you sure, though? Banshees are quite rare."
    hide diego
    hide jd
    show mac cop surprised at centre
    ma "That's what Gwen said in the interrogation room. That she was rare."
    hide mac
    show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
    "(At least in the middle of this disaster, we're getting some answers.)"
    hide hiflmc
    show hiflmc beaniebowling basic at left3
    show jd casual shadesbasic at right3
    mcmac "So what does a banshee scream do?"

    jd "Traditionally? Warns of an impending death."

    jd "But in practice, it brings people together."

    jd "Draws them close to listen."
    show hiflmc beaniebowling_cu angry_cu at hiflmc_cu
    "(And the whole town of Havenfall is tuned in.)"
    hide hiflmc
    show hiflmc beaniebowling surprised at left3
    show jd casual shadesbasic at right3
    mcmac "And the follow-up on that. Why didn't it affect me?"
    hide hiflmc
    show razi casual basic at left4
    show diego casual glassesbasic at centre
    show jd casual shadesbasic at right4
    "JD, Razi, and Diego simultaneously stare at me, then glance towards Mackenzie."
    hide jd
    hide diego
    hide razi
    show mac cop surprised at left3
    show hiflmc beaniebowling surprised at right3
    mcmac "...Can alpha bonds do that?"

    ma "Apparently."
    show mac cop basic
    ma "I'm afraid I don't have a lot to reference."

    ma "You're my first."
    show mac cop angry
    show hiflmc beaniebowling sad
    "Even with the revelation about Gwen, I can tell the raw edges haven't worn off Mackenzie's mood."
    show hiflmc beaniebowling sad at right2
    show mac cop angry at left2
    "I come around behind her desk, resting my hands on tight shoulders."

    mcmac "How about you take the rest of the day off and relax a little?"

    mcmac "Gwen's trying to mess with your head."

    ma "I can't just drop this."
    hide mac
    hide hiflmc
    show diego casual glassesbasic at centre
    di "You're not going to. We can pick up the slack for now."
    hide diego
    show jd casual shadessmirk at centre
    jd "Yeah, I'll hop on my bike and keep an eye on the townsfolk."

    jd "Make sure they're not getting rowdy."
    hide jd
    show razi casual smirk at centre
    ra "And I'll look into breaking the enchantment."

    ra "Sometimes if there's a will, there's a way."
    hide razi
    show hiflmc beaniebowling basic at right2
    show mac cop sad at left2
    "Mackenzie's quiet for a moment, and I know she's fighting the urge to protest, to be the one on the front line."
    show hiflmc beaniebowling happy
    mcmac "If you're going to take Gwen out, you have to be at your best, right?"
    show mac cop basic
    ma "...Yeah."

    ma "You're right. I'll take a break."
    scene bg mackenzie_bedroom_lights at bg with fade
    show mac cop basic at left3
    show hiflmc beaniebowling basic at right3
    "I drive Mackenzie back to her house, comfortable in the silence until we're back in her room."
    show mac tank basic
    "She sits down on the edge of the bed and starts unbuttoning her uniform shirt."
    show mac tank sad
    ma "I've been worried about something like this since I took this job."
    show hiflmc beaniebowling surprised
    mcmac "Someone like Gwen?"
    show mac tank sleep
    "Mackenzie shakes her head, going to unbuckle her duty belt next."
    show mac tank basic
    show hiflmc beaniebowling basic
    ma "Not her in particular."
    show mac tank sad
    ma "But losing the trust of the town over something I couldn't control."

    ma "Or having to keep what I am secret."

    ma "I can't help them when that happens."

    ma "Worse, I..."

    ma "What am I going to do if they turn on me, [genericfn]?"

    ma "They're human."

    ma "Even if they're under Gwen's influence, these are my neighbors."

    ma "The reason I serve and protect."

    ma "She knows I won't hurt them, but she can hurt me by making them look the other way."
    show mac tank sad at left1 behind hiflmc
    show hiflmc beaniebowling sad at right1
    "I step forward, gently nudging between Mackenzie's knees so I can give her a tight hug."
    show mac tank sleep
    "She presses her face against my chest, eyes closed as she listens to the beating of my heart."
    show mac tank basic
    show hiflmc beaniebowling happy
    mcmac "You're doing the right thing, even if they don't know it."

    mcmac "We're going to stop Gwen. Everyone will go back to how they were."

    mcmac "I know you won't forget what it was like to see them that way, but know that I trust you."

    mcmac "With everything, Mac."

    mcmac "My life, my heart, the whole deal."

    "Mackenzie's arms wrap around the small of my back, clinging tight."
    show mac tank sad
    ma "Thank you."

    ma "I just...I feel like I could have stopped this."
    show hiflmc beaniebowling basic
    mcmac "Babe, Gwen was paid to kill you."

    mcmac "Even if you'd kicked her out first thing, she wouldn't have given up."

    mcmac "The important part is you staying alive."

    mcmac "You're the one Havenfall needs."

    ma "I need you too."

    "The way she says it is so soft I almost miss the words."
    hide mac
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    "I slowly drop down to my knees in front of her, smiling when our eyes meet."
    hide mac
    show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
    mcmac "You've got me."

    mcmac "After fighting off a whole pack of werewolves, a banshee doesn't have a chance in hell, okay?"

    mcmac "I'm not backing down."
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    "Mackenzie's gaze burns with such intensity for a moment that the breath is stolen right out of my lungs."
    hide mac
    show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
    "There's an answering pull in my chest, my hands tensing against Mackenzie's back to bring her closer."
    hide hiflmc
    "The kiss we share is slow, lingering on that single point of connection."
    show mac tank_cu blush_cu at mac_cu
    ma "I..."
    hide mac
    show hiflmc beaniebowling_cu surprised_cu at hiflmc_cu
    mcmac "Yeah?"
    hide hiflmc
    show mac tank_cu blush_cu at mac_cu
    ma "Thank you for staying."

    ma "For coming home with me."
    hide mac
    show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
    mcmac "Anytime."

    mcmac "That's what girlfriends are for, right?"
    hide hiflmc
    show mac tank_cu happy_cu at mac_cu
    "She smiles, letting out a soft laugh."

    ma "Guess I should get used to that then, huh?"

    ma "And follow your advice about relaxing."
    hide mac
    show mac tank sleep at centre
    "Mackenzie leans back and brings her arms overhead in a long stretch."
    show mac tank basic
    ma "I think I'm going to hop in the shower to clear my mind."
    show mac tank smirk
    ma "You want to join me?"
    hide mac
    show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
    "(I can think of a few ways to get her mind off things.)"
    hide hiflmc
    show mac tank smirk at left3
    show hiflmc beaniebowling blush at right3
    "It only takes a second for my face to heat up, and the look Mackenzie gives me wipes away any doubts about what she means."

    "The idea of seeing Mackenzie dripping wet in the shower leaves me so flustered I can't find words for a moment."
    hide hiflmc
    hide mac
    $menuhideborder = True
    menu macs2e11c2:
        "A. Join Mac in the shower."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(I'm not sure it's humanly possible for me to say no to that.)"
            hide hiflmc
            show mac tank smirk at left3
            show hiflmc beaniebowling happy at right3
            mcmac "You bet your sweet ass I do."
            show mac tank happy
            "Mackenzie laughs and disappears into the bathroom, leaving me to follow suit."
            scene bg mackenzie_bathroom_lights at bg with wipediagTLBRdissolve
            show mac naked basic at left3
            show hiflmc beaniebowling happy at right3
            "She's already getting undressed, removing her uniform with the methodical ease of long practice."
            show hiflmc beaniebowling blush
            "From my view, it might as well be a strip tease."
            show mac naked smirk
            ma "You have to get naked too, by the way."

            ma "It's only fair."
            show hiflmc beaniebowling happy
            mcmac "Well, in the interest of fairness…"
            show hiflmc naked happy
            "I put my glasses somewhere out of the way before they get too steamed up to see through,"

            "stealing a glance here and there until my clothes are in a pile on the floor."

            "I'm so distracted by seeing Mackenzie lean over to turn on the water that it takes me a second to realise how damn huge the shower is."
            show hiflmc naked surprised
            mcmac "You could fit a locker room in here."
            show mac naked blush
            ma "It's meant for couples, I think."

            ma "The set-up came with the place, and it was too nice for me to get rid of."
            hide mac
            hide hiflmc
            show hiflmc naked_cu happy_cu at hiflmc_cu
            "(I'm glad she didn't.)"
            hide hiflmc
            show rain at bg
            show smoke at bg
            show mac naked_cu sleep_cu at mac_cu
            "Mackenzie steps under the spray first, letting out a deep sigh of relief as the water soaks through her hair,"
            hide rain
            hide smoke
            "dripping in slow, clear rivulets down the warm brown of her skin."
            show mac naked_cu happy_cu
            "She smiles, and my heart does a backflip."
            hide mac
            show hiflmc naked happy at centre
            ma "Come on in."

            mcmac "Don't mind if I do."
            hide hiflmc
            show rain at bg
            show smoke at bg
            show hiflmc naked_cu happy_cu at hiflmc_cu
            "I have to bite back a groan after slipping beneath the second spray."
            hide rain
            hide smoke
            "The water pressure is perfect, and just warm enough to cut right through the tension in my back."
            hide hiflmc
            show mac naked_cu smirk_cu at mac_cu
            ma "Nice, huh?"

            "She pushes the glass door shut behind us, and I revel in the water a moment longer before offering an expectant look Mackenzie's way."
            hide mac
            show hiflmc naked_cu happy_cu at hiflmc_cu
            mcmac "So, how can I help clear your mind today?"
            hide hiflmc
            show mac naked_cu smirk_cu at mac_cu
            ma "Well, the soap is right behind you."
            show mac naked_cu smirk_cu at mac_cu:
                xpos -300
            show hiflmc naked_cu happy_cu at hiflmc_cu:
                xpos +300
            "It is indeed, along with a dark blue washcloth, and I lather it with a little more soap than I might need before bringing it to Mackenzie's skin."

            "I start slow, washing up one arm, then drawing a necklace a bubbles across her collarbone."

            mcmac "Does this feel good?"
            show mac naked_cu happy_cu
            ma "Better every second."
            show mac naked_cu blush_cu
            "When I start to work lower, there's a subtle catch in Mackenzie's breath, her eyes never leaving me."

            "My fingers follow all the little waterfalls along every divot and curve of muscle, down past Mackenzie's stomach and right between her thighs."

            "But only for a second, long enough for her to shiver, before the cloth slips further down the inside of one leg."

            ma "Tease."

            mcmac "Just washing you up first."
            show mac naked_cu smirk_cu
            ma "What's second?"

            mcmac "Depends on how good your balance is."

            ma "Oh, I can hold onto anything I need to."
            show hiflmc naked_cu blush_cu
            "(I know she can, and god, I want her to.)"
            show mac naked_cu happy_cu
            "My resolve breaks the moment Mackenzie touches me."
            show hiflmc naked_cu surprised_cu
            "I drop the washcloth a second after my back meets the cool tile, the difference between that and the heat of her body making me gasp."
            show mackenzie_s2_mini11 at bg
            "Our first kiss is quick and messy, and I keep myself standing by grasping at Mackenzie's shoulders, nearly up on my toes."
            hide mackenzie_s2_mini11
            show bg mackenzie_bathroom_lights at bg
            show rain at bg
            show smoke at bg
            show mac naked_cu happy_cu at mac_cu:
                xpos -300
            show hiflmc naked_cu blush_cu at hiflmc_cu:
                xpos +300
            mcmac "I thought I was clearing your mind, n-not the other way around."
            hide rain
            hide smoke
            "(But it's difficult to complain.)"

            "(Really, really difficult.)"
            show mac naked_cu smirk_cu
            ma "You still can."

            ma "But I wanted to kiss you more than anything else."
            hide mac
            hide hiflmc
            "I give her one more kiss on the lips for good measure, but the next is on the pulse in Mackenzie's neck, then the base of her throat."

            "My mouth chases the water from her skin, searching out every sensitive spot until I'm on my knees in front of her."
            show mac naked_cu blush_cu at mac_cu
            ma "[genericfn]..."
            hide mac
            show hiflmc naked_cu happy_cu at hiflmc_cu
            mcmac "Just relax, babe."
            hide hiflmc
            "Mackenzie braces her arms against the wall of the shower as my tongue sweeps the hollow of her hip, daring lower until I can really taste her."

            "The moan that echoes above me is like music."

            "With one arm braced around Mackenzie's waist, I can center myself solely on her pleasure, the way"

            "the muscle jumps in her thighs when she's desperately trying to keep still."
            show mac naked_cu blush_cu at mac_cu
            ma "Fuck."
            hide mac
            show hiflmc naked_cu happy_cu at hiflmc_cu
            mcmac "I'll take that as a compliment."
            hide hiflmc
            "The strained gasp I get in return says everything, and it doesn't take much longer for Mackenzie to give in with a heated whisper of my name."

            "I'm pulled right up into another deep kiss, her strength enough to keep me steady even under the water."
            show mac naked_cu smirk_cu at mac_cu
            ma "Now it's your turn."

        "B. Wait in her room.":
            $menuhideborder = False

            "(Knowing me, I'd probably slip on the tile as soon as I got in there.)"

            "(Not very relaxing.)"

            mcmac "Um..."

            mcmac "How about I wait out here and make you some coffee?"

            mcmac "I could cook something too if you're hungry."

            ma "Hungry, not so much."

            "She stands up from the bed, fingertips sparing a soft caress over my hair before Mackenzie walks over to the bathroom."

            "After hesitating in the doorway, Mackenzie glances back over one shoulder."

            ma "But I'm parched."

            ma "Some hot coffee would be great."

            "When she bends down to unlace her boots, I take off my glasses to not to make a more embarrassing sort of sound sickly clear em, trying"

            mcmac "You bet, babe. It'll be right out."
    scene bg main_fog at bg with fade
    pause
    show hiflmc bowling basic at centre
    "I wrap the last couple hours of the night shift for Razi and step out of the bowling alley to lock up."

    "As the key turns with a solid click, my phone buzzes in my pocket."
    hide hiflmc
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(Probably Mac checking up on me.)"

    "(She said she'd pick me up after her patrol.)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "Snagging my phone, I turn the screen to see the message when a tight hold from behind seizes my wrist and twists, hard."

    "The phone hits the ground with a clatter, and I'm shoved against the door of the bowling alley."
    show hiflmc bowling surprised
    "Before I can scream, another cool hand presses hard over my mouth."
    show hiflmc bowling surprised at left2
    show gwen casual basic at right2 behind hiflmc
    gwe "Uh-uh. Stay quiet."
    hide gwen
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Fuck.)"
    hide hiflmc
    show hiflmc bowling surprised at left2
    show gwen casual happy at right2 behind hiflmc
    gwe "This street's not that big, is it?"

    gwe "Sheriff's office is right there."

    gwe "Too bad I saw the squad car leave earlier."
    hide gwen
    hide hiflmc
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(Mac might be away, but Razi and JD are right inside.)"

    "(If I can just—!)"
    hide hiflmc
    show hiflmc bowling surprised at left2
    show gwen bansheecasual bansheeangry at right2 behind hiflmc
    "I shudder as sharp claws extend from both of Gwen's hands, tips pressing against my cheek and the line of my arm."
    show hiflmc bowling sad
    "No matter which way I move, she can hurt me."

    "And she's a hell of a lot stronger than she looks."
    show hiflmc bowling basic
    show gwen bansheecasual bansheebasic
    gwe "Now here's how this is going to work."

    gwe "You're coming with me."

    gwe "I don't care if it's dead or alive."
    show gwen bansheecasual bansheeangry
    gwe "But if you want to see your wolf one last time, stay quiet and follow directions."

    gwe "Got it?"
    show hiflmc bowling sad
    "Swallowing hard, I weigh my options."

    "The knife Mackenzie gave me is still in my back pocket, but I can't reach it—and have no idea if silver does anything to banshees."

    "Living longer is the priority. I nod slowly."
    show gwen bansheecasual bansheehappy
    gwe "That's better."

    gwe "We've got a bit of a walk..."
    show hiflmc bowling basic
    show gwen bansheecasual bansheesurprised
    "Gwen stops short, her body tensing up against my back."

    gwe "That's impossible."
    show hiflmc bowling surprised at left3
    show gwen bansheecasual bansheesurprised at right3
    "It's the last thing she says before I hear a feral snarl, and Gwen's grip is ripped away from me."
    hide gwen
    show hiflmc bowling surprised at centre
    "My wrist stings like hell, but I can breathe again, and turn to press my back against the door and fumble for the knife."

    mcmac "Mac, how did you get-!"
    hide hiflmc
    show gwen bansheecasual bansheesurprised at left2 behind annabelle
    show annabelle wolfcasual wolfangry at right2
    "The werewolf on top of Gwen isn't Mackenzie."

    "It's Annabelle."
    show gwen bansheecasual bansheeangry
    gwe "Get off me, you mongrel!"

    "The answer she gets in turn is a growl, and I hear scraping asphalt before Annabelle lunges for Gwen's throat with teeth bared."
    show gwen bansheecasual bansheeangry at left3
    show annabelle wolfcasual wolfsurprised at right3
    "Gwen dodges the bite before raking red lines across Annabelle's face, a shove sending her sprawling."
    hide annabelle
    show hiflmc bowling angry at right3
    "I open the knife, holding it out in as much of a threat as I can muster."
    show gwen bansheecasual banshee angry at out_right
    "Gwen glowers at me, then disappears down the street in a blur."
    hide annabelle
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(I have no idea what's going on, but Annabelle totally just saved me.)"
    hide hiflmc
    show hiflmc bowling surprised at left3
    show annabelle wolfcasual wolfbasic at right3
    mcmac "Hey, are you okay?"

    ann "I'll be fine."
    show annabelle wolfcasual wolfangry
    "Wincing a little, Annabelle gets to her feet, wiping a bit of blood from her cheek."
    hide annabelle
    hide hiflmc
    show mac earscop wolfangry at centre
    "The squeal of tires from down the street catches my ear, and I see Mackenzie throw herself out of the patrol car, already shifted."

    ma "Get away from her!"
    hide mac
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Shit, she can't smell Gwen.)"

    "(The only thing Mac sees right now is another werewolf and I've got a silver knife out.)"
    hide hiflmc
    $menuhideborder = True
    menu macs2e11c3:
        "A. Drop the knife.":
            $menuhideborder = False
            show hiflmc bowling surprised at centre
            show annabelle wolfcasual wolfsurprised at left2 behind hiflmc
            "I let the knife fall down next to my phone, putting up both hands as a sign of peace."

            mcmac "Mac, it's okay! She's not hurting me."

        "B. Shout for Mac to stop.":
            $menuhideborder = False

        "C. Step in front of Annabelle.":
            $menuhideborder = False
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(Talking might not be fast enough.)"
            hide hiflmc
            show hiflmc bowling angry at centre
            show annabelle wolfcasual wolfsurprised at left2 behind hiflmc
            "I duck in front of Annabelle, then quickly close the knife in my hand."

            "The last thing I want is one of them getting stuck with it."
    hide hiflmc
    hide annabelle

    show hiflmc bowling basic at left3
    show mac earscop wolfbasic at right3
    "Mackenzie stops right in front of me, golden eyes searching for signs of injury, but except for the faint scratch on my arm, I'm okay."
    show hiflmc bowling basic at left4
    show mac earscop wolfbasic at centre
    show annabelle wolfcasual wolfsurprised at right4
    "Annabelle shrinks under Mackenzie's stare when it falls on her."

    ma "What are you doing here?"
    show hiflmc bowling surprised
    mcmac "Mac, she just saved me from Gwen."

    ma "And how did she know where Gwen would be?"
    hide annabelle
    hide mac
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(...Good question.)"
    hide hiflmc
    show hiflmc bowling surprised at left4
    show mac earscop wolfsurprised at centre
    show annabelle wolfcasual wolfbasic at right4
    ann "Because Beau hired the banshee to kill you."

    ann "I didn't find out anything about Grace, but I learned that much."
    show annabelle wolfcasual wolfsurprised
    ann "Please, you've got to believe me."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
