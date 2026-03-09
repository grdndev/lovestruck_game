label jd_season1_episode2:

    $tbc = False
    scene bg mc_house_ext_moon at bg
    play music hiflsuspense

    show jd casualwings devilangry at centre
    "I don't have time to figure it out before JD tosses the fire right at Grace's feet, putting a blazing line between us."
    hide jd
    show hiflmc casual surprised at right3
    show grace waitress basic at left3
    "Grace doesn't even flinch, but I do."
    mcjd "JD, don't hurt my sister!"
    mcjd "I don't know what's wrong with her, but stop!"
    hide hiflmc
    hide grace
    show jd casualwings devilbasic at centre
    jd "That's not your sister."
    jd "It's just wearing her face."
    hide jd
    show hiflmc casual surprised at right3
    show grace waitress basic at left3
    mcjd "What?"
    show grace waitress basic at left2
    "Shock locks me in place as 'Grace' walks straight through the flame towards me,"
    show grace waitress basic at left1
    "Not showing a single hint of pain as the fire jumps across her legs."
    hide grace
    hide hiflmc
    show jd_s1_mini11 at bg
    jd "[genericfn], get ouf of the way."
    hide jd_s1_mini11
    show hiflmc casual surprised at right3
    show grace waitress basic at left1
    mcjd "No, but I..."
    mcjd "I don't understand."
    hide hiflmc
    hide grace
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(This has to be a nightmare.)"
    "(How do I wake up?)"
    hide hiflmc
    show hiflmc casual surprised at right3
    show grace waitress basic at left1
    "Pinching myself doesn't do anything but hurt, and I'm forced to back up to the sidewalk as the thing that looks like Grace keeps moving towards me."
    hide hiflmc
    hide grace
    show jd casualwings devilangry at centre
    jd "One."
    jd "More."
    jd "Goddamn."
    jd "Step."
    "A white-hot surge of fire explodes from both of JD's hands, eyes ablaze with the same light."
    hide jd
    show grace waitress sad at centre
    "'Grace' looks up at them, head tilting as if in curiosity, and then bolts."
    hide grace
    show jd casualwings devilangry at centreee
    jd "Yeah, you better run."
    "With a snap of their fingers, the growing inferno around JD is snuffed out,"
    "And they slowly descend to the ground, boots touching the floor with a whisper of sound."
    hide jd
    show hiflmc casual surprised at centre
    "For a second, all I can do is stare."
    hide hiflkmc
    $menuhideborder = True
    menu jds1e2c1:
        "A. You have wings.":
            $menuhideborder = False
        "B. Are you really JD?":
            $menuhideborder = False
            show hiflmc casual surprised at centre
            mcjd "Are you really JD?"
            show hiflmc casual sarcastic
            mcjd "Because right now, I don't know what to think."
            hide hiflmc
            show jd casualwings devilsmirk at centre
            "A hint of a smile tugs at the edge of their mouth."
            jd "Real as can be."
            hide jd
        "C. This isn't possible.":
            $menuhideborder = False

    show jd casualwings_cu devilbasic_cu at jd_cu
    "JD closes the distance between us, one hand cupping my cheek."
    "There's a sharp metallic scent clinging to their skin, like iron and ash."
    jd "You don't want this to be true, right?"
    show jd casualwings_cu devilhappy_cu
    jd "It would be better if none of this had happened at all."
    show jd casualwings_cu devilsad_cu
    jd "Like a dream."
    hide jd
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "I nod, feeling tears start to break at the corner of my eyes."
    hide hiflmc
    show jd casualwings_cu devilbasic_cu at jd_cu
    jd "Then you're going to go inside and go to sleep."
    show jd casualwings_cu devilhappy_cu
    jd "You'll wake up and won't remember a thing."
    "There voice is heavy and warm, different than I'm used to hearing."
    "As the world starts to blur at the edges, JD leans forward and pressed a kiss to my brow."
    show jd casualwings_cu devilsad_cu
    jd "Sorry, [genericfn]."

    scene bg heroine_home_day at bg with dissolve
    pause
    "My back hurts."
    show hiflmc pajamas noglassesangry at centre
    "Groaning as I stretch out on the couch, I try to figure out the culprit,"
    "And eventually my fingers catch on the remote, caught between the cushion and my spine."
    show hiflmc pajamas noglassessarcastic
    mcjd "Ow. No wonder."
    show hiflmc pajamas noglassesbasic
    mcjd "Grace, are you up yet?"
    show hiflmc pajamas noglassessurprised
    "A glance at my phone reveals I'm up half an hour late, and I scramble to get dressed."
    show hiflmc vestlesscasual basic
    "Ducking my head into Grace's room, I flick on the light switch to get her up too."
    show hiflmc vestlesscasual sad
    mcjd "Hey, I'm so sorry for waking up late, but are you..."
    hide hiflmc
    show hiflmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(She's not here.)"
    "(Did Grace have an early shift and not tell me?)"
    hide hiflmc
    show hiflmc vestlesscasual basic at centre
    "There's nowhere else Grace could be."
    show hiflmc bowling basic at centre
    "After brushing my teeth and putting myself together, I hope in my truck and head right to the diner."

    scene bg diner_lights_on at bg with fade
    pause
    show luce casual basic at centre
    lu "Morning, girl. Here for coffee?"
    show luce casual basic at left3
    show hiflmc bowling basic at right3
    mcjd "I was looking for Grace, actually."
    show luce casual angry
    "Luce frowns at me before glancing at the clock on the back wall."
    luc "Well, she's about to run late. Aren't you her ride?"
    show hiflmc bowling sad
    mcjd "..."
    mcjd "Yeah, I am."
    hide luce
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Where the hell is my sister?)"
    hide hiflmc
    show hiflmc bowling sad at centre
    "I rack my mind about where I saw her last, but everything's hazy after I left work last night."
    "Ignoring Luce's confused stare, I leave the diner and run next door to the sheriff's office."

    scene bg hifl_sheriff at bg with wipeleft
    show mac cop basic at left3
    show hiflmc bowling sad at right3
    "Sheriff Hunt is sitting behind her desk, and goes on high alert when she sees me."
    show mac cop sad
    ma "Hey, are you alright?"
    mcjd "I..."
    mcjd "Grace is gone."
    show mac cop surprised
    ma "Your sister?"
    mcjd "She should have been in the house this morning, but she's not, and she's not at the diner..."
    mcjd "I drove my car herfe, so she didn't take it."
    mcjd "I..."
    "Everything's such a jumble that I know I'm not making sense."
    show mac cop sad at left2
    "Concern bleeds through Mackenzie's eyes, and she stands up to touch my shoulder."
    ma "Take a deep breath."
    ma "I need you to start from the beginning."
    hide mac
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(But where is the beginning?)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "The low rumble from a motorcycle engine carries down Main Street, and suddenly my thoughts are filled with fire."
    "Fire and wings."

    scene bg main_day at bg with fade
    pause
    show hiflmc bowling surprised at centre
    "I run out of the sheriff's office, carried by the image burning through my mind."
    "The whole picture is flickering, fractured, but I remember a motorcycle."
    "I remember JD."
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(What do they have to do with Grace, though?)"
    "(And fire?)"
    "(Was there an explosion or something? A crash?)"
    hide hiflmc
    show jd casual shadesbasic at centre
    "They stop their bike right outside the bowling alley, and it looks untouched."
    "JD doesn't even spare a glance at me, pocketing their keys before checking something on their phone."
    $menuhideborder = True
    menu jds1e2c2:
        "A. Ask them about last night." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc bowling_cu angry_cu at hiflmc_cu
            "(I have to ask.)"
            "(Even if they tell me I've lost it, I need JD to tell me to my face that nothing happened.)"
            hide hiflmc
            show jd casual shadesbasic at left2
            show hiflmc bowling angry at right2
            "With a few quick steps, I cross the street and grab JD's wrist, interrupting their texting."
            show jd casual shadesangry
            jd "Hey, back o-!"
            show jd casual shadessurprised
            jd "[genericfn]."
            jd "What's up?"
            mcjd "What did you do to me last night?"
            jd "..."
            show jd casual shadesbasic
            "Their guard goes up instantenously, but the split-second glimpse of surprise in JD's face tells me everything."
            "I know when they've been caught out."
            jd "Let's talk about this inside."
            mcjd "Why?"
            jd "Why?"
            show jd casual shadesangry
            jd "Whatever you remember, whatever you think you remember, does it seem like gossip we should share with the whole neighborhood?"
            hide jd
            hide hiflmc
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(If even half my memories are real, no.)"
            hide hiflmc
            show jd casual shadesangry at left2
            show hiflmc bowling basic at right2
            mcjd "Probably not."
            show jd casual shadesbasic
            jd "Then let's go."
            hide jd
            hide hiflmc
            show bg bowling at bg with wiperight
            show jd casual basic at left2
            show hiflmc bowling basic at right2
            "They shuffle me inside the bowling alley, and I don't think I've ever seen JD look this serious in my life."
            "With a clipped hello to Razi, they keep walking em all the way back to the arcade,"
            show bg bowling_arcade at bg
            show jd casual basic at left2
            show hiflmc bowling basic at right2
            "Where the constant beeps and chirps of the machines can cover our conversation."
            jd "Tell me what you saw."
            show hiflmc bowling sad
            mcjd "You... you came by on your motorcycle last night."
            mcjd "Because... someone attacked me."
            mcjd "Something."
            hide jd
            hide hiflmc
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Why is it all broken up in my head?)"
            "(There was so much fire everywhere.)"
            hide hiflmc
            show jd casual basic at left2
            show hiflmc bowling sad at right2
            mcjd "You were flying."
            mcjd "I don't know how."
            hide hiflmc
            hide jd
            show jd casual_cu angry_cu at jd_cu
            "JD's brow tightens with tension, and their hand presses against my face, cupping my jaw."
            "The warmth is familiar, even if I don't know why they're touching me."
            hide jd
            show hiflmc bowling_cu basic_cu at hiflmc_cu
            mcjd "Hey..."
            hide hiflmc
            show jd casual_cu basic_cu at jd_cu
            jd "No one was flying."
            jd "And you're okay, aren't you?"
            jd "You're not hurt."
            jd "There's no monsters in the dark."
            hide jd
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            mcjd "But Grace-!"
            hide hiflmc
            show jd casual_cu basic_cu at jd_cu
            jd "Just look at me."
            jd "Listen."
            "A hypnotic quality weaves through their voice, drawing me under."
            "I want to listen, but I know it's not true."
            hide jd
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            mcjd "I..."
            show hiflmc bowling_cu angry_cu
            mcjd "I know what I saw!"
            hide hiflmc
            show jd casual surprised at left2
            show hiflmc bowling angry at right3
            "The protest snaps off my tongue like a firecracker, and JD pulls their hand away from me with the twinge of reflex."
            mcjd "What were you just doing to me, JD?"
            show jd casual sad
            jd "... Trying to make you forget."
            jd "But it didn't work this time."
            show hiflmc bowling surprised
            mdjd "This time?"
            show hiflmc bowling angry
            mcjd "You did it last night too, didn't you?"
            jd "Yeah, I did."
            show jd casual basic at left4
            "Regret twists JD's expression for a moment before they swallow it back, taking a step away from me."
            jd "I thought it was for the better."
            show jd casual sad
            jd "You looked so damn scared."
            jd "Like your world had just been torn apart."
            show hiflmc bowling surprised
            mcjd "But how is that possible?"
            mcjd "You can't just... make people forget things."
            mcjd "That's like magic."
            show jd casual basic
            jd "That's one word for it."
            jd "But whatever you want to call what I did, yes, I made you forget."
            show jd casual sad
            jd "Most of it anyway."
            "JD bites their lip, then lets out a weak laugh."
            jd "This is actually the first time that hasn't worked."
            jd "I don't have a good line."
            hide jd
            hide hiflmc
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(Okay.)"
            show hiflmc bowling_cu sarcastic_cu
            "(Setting aside the fact that JD can hypnotize people with a look or something, my sister is still gone.)"
            hide hiflmc
            show jd casual sad at left4
            show hiflmc bowling angry at right3
            mcjd "Where did Grace go?"
            mcjd "I brought her home from work and then you..."
            show jd casual basic
            jd "You didn't bring your sister home."
            jd "You brought someone who looked like her home."
            show hiflmc bowling surprised
            mcjd "That's impossible, she was right outside the diner-!"
            hide jd
            hide hiflmc
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(And didn't talk the entire way back.)"
            hide hiflmc
            show hiflmc bowling surprised at centre
            "The memory of the cold silence pervading my truck sinks in, and a shiver of fear follows right up my spine."
            "I remember the alien look in Grace's eyes before she attacked me, before she-!"
            "I reach down to grasp my wrist, and the faint ache of a bruise lingers there."
            show hiflmc bowling surprised at right3
            show jd casual basic at left3
            mcjd "It wasn't Grace."
            mcjd "But what the hell came after me?"
            show jd casual smirk
            jd "Technically, I was the hell that came after you."
            show jd casual basic
            jd "But I was trying to keep you safe."
            hide jd
            show hiflmc bowling surprised at centre
            "Everything comes back in one wild rush."
            "JD rising off their bike in a pillar of flame, their wings casting shadows on the street."
            "They flew above me, scaring off the creature that had Grace's face."
            "Then JD had come down to the ground, touched my face and..."
            show hiflmc bowling surprised at right3
            show jd casual basic at left3
            mcjd "I forgot the whole thing."
            mcjd "I woke up like none of it had happened."
            jd "I know."
            jd "That's what I wanted."
            hide hiflmc
            hide jd
            show jd casual_cu basic_cu at jd_cu
            jd "What you'ce just figured out, [genericfn]?"
            jd "You're supposed to be oblivious to."
            hide jd


        "B. Pretend like nothing happened.":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(I have to be overthinking this.)"
            "(What do I even say to them?)"
            show hiflmc bowling_cu sarcastic_cu
            "('Hey JD, do you know if something fiery with wings showed up and took away my sister last night? Thanks.')"
            hide hiflmc
            show hiflmc bowling sad at centre
            "I shoot off a quick text to Grace, praying that she'll answer to tell me she went off last night to party or something."
            "It would be out of character, but I'd take sudden teenage rebellion over the worst."
            hide hiflmc
            show jd casual shadesbasic at centre
            "When I look up again, JD is heading through the front door, and I follow behind as cautiously as I can."
            hide jd
            show bg bowling at bg with wipeleft
            show razi casual happy at centre
            ra "Morning, you two."
            show razi casual happy at left3
            show jd casual basic at right3
            jd "You saw me like an hour ago, Razi."
            show razi casual smirk
            ra "Isn't it your rule that it's not morning until you've been caffeinated."
            jd "...Good point."
            hide jd
            hide razi
            show hiflmc bowling_cu basic_cu at hiflmc_cu
            "(They're the same.)"
            show hiflmc bowling_cu sad_cu
            "(Something would be different if I was remember right, wouldn't it?"
            hide hiflmc
            show hiflmc bowling basic at centre
            "The only thing I can do is act normally, hoping the rest of the pieces will fall together."
            show hiflmc bowling sad
            "Checking my phone every five minutes doesn't do much for my anxiety, but at least I get the lanes set up."
            hide hiflmc
            show razi casual angry at left3
            show jd casual basic at right3
            ra "JD, why is the sheriff texting me at ten in the morning?"
            hide razi
            hide jd
            show hiflmc bowling sad at centre
            "I swallow hard, realizing that I booked it out of Mackenzie's office without any sort of explanation."
            hide hiflmc
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(She must think I lost my mind.)"
            show hiflmc bowling_cu sarcastic_cu
            "(Great.)"
            "(Most of this town already thinks I'm weird.)"
            hide hiflmc
            show razi casual angry at left3
            show jd casual smirk at right3
            jd "I don't know, Razi."
            jd "Why is the sheriff texting you at ten in the morning?"
            show razi casual sleep
            "Razi sighs, waving JD off so he can read the rest of the message."
            hide razi
            show jd casual smirk at centre
            "They laugh under their breath, picking up one of the bowling balls and spinning it before setting it back on the rack."
            hide jd
            show hiflmc bowling_cu basic_cu at hiflmc_cu
            "(JD has a reputation for trouble, but they've never done anyting awful I've heard about.)"
            show hiflmc bowling_cu happy_cu
            "(They just like pushing boundaries, seeing how far people will let them go.)"
            "(Especailly if it's a rule that sucks.)"
            hide hiflmc
            show razi casual basic at left3
            show hiflmc bowling basic at right3
            ra "[genericfn]."
            mcjd "Yeah?"
            show razi casual sad
            show hiflmc bowling surprised
            ra "You doing okay over there?"
            ra "Looked like you were staring off into space."
            hide razi
            hide hiflmc
            show jd casual_cu basic_cu at jd_cu
            "JD is staring right at me, and I search their eyes for something, any sign that I didn't hallucinate all of last night."
            "The taste of ash is sudden and sharp on the back of my tongue."
            hide jd
            show razi casual sad at left3
            show hiflmc bowling surprised at right3
            mcjd "I just..."
            show hiflmc bowling sad
            mcjd "Can I take five?"
            mcjd "I didn't sleep much last night."
            show razi casual happy
            ra "Of course."
            ra "Snag a soda and rest your feet."
            hide razi
            hide hiflmc
            show bg bowling_arcade at bg
            show hiflmc bowling sad at centre
            "I grab the first can I seee behind the bar and retreat back over to the arcade, hiding myself behind the machines."
            "Gulping down cold carbonation isn't exactly a miracle cure, but at least the sugar pushes back my building headache."
            mcjd "Grace, just text me back."
            mcjd "Tell me what happened."
            mcjd "Because I know something did."
            hide hiflmc
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Her bed wasn't even slept in.)"
            hide hiflmc
            show hiflmc bowling sad at centre
            mcjd "And JD..."
            "Every time I try to think about what happened last night, it's like clawing at a word that just slipped away."
            "There's a blank space, a sense of knowing without being able to remember exactly what's missing."
            show hiflmc bowling basic
            mcjd "I didn't drink."
            show hiflmc bowling sarcastic
            mcjd "And I don't think I took anything weird."
            show hiflmc bowling surprised
            mcjd "I'm halfway through considering that my truck backfired carbon monoxide into my lungs when a hand presses up against my back."
            show hiflmc bowling surprised at right1
            show jd casual basic at left1 behind hiflmc
            "Holding in a yelp, I jerk around and meet JD's eyes."
            "They were full of fire then."
            "I was afraid, running from something too terrifying to comprehend."
            "Then JD came down in a blaze of vengeance to save me."
            mcjd "You saved me."
            mcjd "Last night, JD, you saved my life."
            mcjd "Why can't I remember the rest?"
            show jd casual sad
            jd "..."
            jd "We need to talk."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(What do I even say?)"
    hide hiflmc
    show hiflmc bowling happy at right3
    show jd casual basic at left3
    mcjd "You were amazing, JD."
    mcjd "I've never seen anything like that before."
    mcjd "It was kind of scary, not going to lie, but in the awe-inspiring kind of way."
    show jd casual angry
    mcjd "What are you, like a fallen angel or something?"
    "It sounds unbelievable coming out of my mouth, but everything about this is unbelievable."
    hide jd
    hide hiflmc
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(JD has superpowers!)"
    hide hiflmc
    show hiflmc bowling happy at right3
    show jd casual angry at left3
    jd "No."
    jd "I'm nothing like that."
    jd "Angels can get stuffed."
    jd "You and me? We've known each other for years, okay?"
    jd "Of course I'm going to step in if something tries to eat your face."
    jd "It doesn't make me a hero."
    show jd casual sad
    jd "And Razi is going to strangle me now that you've found out."
    show hiflmc bowling surprised
    mcjd "Razi knows too?"
    show jd casual basic
    jd "[genericfn], we live in the same house."
    show hiflmc bowling blush
    mcjd "Okay, fair."
    show hiflmc bowling basic
    mcjd "But hero or not, you're... something special, JD."
    mcjd "How did it even happen?"
    show jd casual sleep
    "They shrug, brushing it off."
    show jd casual basic
    show hiflmc bowling sad
    "I'm used to a degree of casual arrogance from JD, playful and smug, and this insistent humility makes me feel uneasy."
    jd "I was born like this."
    jd "And before you ask, the story's not pretty."
    show jd casual sad
    jd "Just take my word for it."
    show hiflmc bowling sad
    mcjd "Like your parents and..."
    show jd casual angry
    show hiflmc bowling surprised
    jd "Don't."
    jd "You and I both got snake eyes with family stuff."
    show jd casual smirk
    jd "It's one of the reasons I like you."
    show hiflmc bowling blush
    "I blush, caught off-guard by the last comment."
    hide jd
    hide hiflmc
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(They don't mean 'like' in that way.)"
    "(I mean, right?)"

    $hidemenuborder = True
    menu jds1e2c3:
        "A. Sorry, JD.":
            $menuhideborder = False
        "B. Is that why we get along so well?":
            $menuhideborder = False
            show jd casual angry at left3
            show hiflmc bowling happy at right3
            mcjd "Is that why we get along so well? Parent issues?"
            show jd casual smirk
            jd "I'd like to think I have a certain charm."
            show jd casual sad
            jd "Separate from the part where I actually tried to charm you, that is."
        "C. You still saved me.":
            $menuhideborder = False

    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(So JD is something not human.)"
    "(Let me file that away so I can focus on the problem at hand.)"
    hide hiflmc
    show jd casual basic at left3
    show hiflmc bowling sad at right3
    mcjd "If a monster took my sister's face, where is Grace now?"
    show jd casual sad
    jd "I don't know."
    jd "It must have gotten close enough to take her appearance, but the fact that she's gone still..."
    show jd casual basic
    jd "Chances are, the creature planned to stay like her for a while."
    show jd casual angry
    jd "Hell if I know why."
    show hiflmc bowling basic
    mcjd "It flipped out when I realized it wasn't Grace."
    mcjd "Went from quiet to attacking me on the spot."
    show jd casual basic
    jd "Yeah, things like that don't like being caught."
    show hiflmc bowling surprised
    mcjd "How do you know this?"
    mcjd "Is it like your job to punch monsters that go bump in the night?"
    show jd casual happy
    "JD laughs, shaking their head."
    jd "No, it's not my job."
    show jd casual smirk
    jd "Razi is the only one that would ever hire me for anything."
    show hiflmc bowling sarcastic
    mcjd "Same here."
    show jd casual angry
    jd "That's because Havenfall is full of sanctimonious prayer-on-Sunday, sin-on-Monday types."
    jd "They need someone to look down on, or they can't feel good about themselves."
    show jd casual smirk
    jd "Kind of funny they picked a human, though."
    show hiflmc bowling happy
    mcjd "Pff, as if the church ladies like you either."
    jd "Oh, they hate me."
    jd "But see, I think it's funny."
    show jd casual sad
    show hiflmc bowling surprised
    jd "It actually makes your life miserable."
    hide jd
    hide hiflmc
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(I didn't even do anything.)"
    "(Why does having your parents die mean you're suddenly the freak?)"
    show hiflmc bowling_cu sarcastic_cu
    "(It's not like I killed them.)"
    hide hiflmc
    show jd casual basic at left3
    show hiflmc bowling sarcastic at right3
    mcjd "You can say that again."
    show hiflmc bowling basic
    mcjd "But I have Grace."
    show hiflmc bowling sad
    mcjd "I... had..."
    mcjd "JD, there has to be a way to find her."
    mcjd "To get her back."
    jd "I know."
    show jd casual sad
    jd "That's what I was going to do, but I didn't want you getting suspicious if I didn't show up to work."
    hide hiflmc
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Oh.)"
    show hiflmc bowling_cu sad_cu
    "(They would have disappeared at the same time Grace did.)"
    "(Bad assumptions all around.)"
    hide hiflmc
    show jd casual basic at left3
    show hiflmc bowling sad at right3
    mcjd "You didn't have to wipe my memory."
    mcjd "I want to help you."
    mcjd "She's my sister, JD."
    show jd casual sad
    jd "That's not how things work here."
    show jd casual basic
    jd "Anyone that's like me keeps it under wraps."
    jd "It's how we survive."
    show hiflmc bowling surprised
    mcjd "Like you how?"
    hide jd
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Don't tell me half the town secretly has wings of fire and I didn't know about it.)"
    hide hiflmc
    show jd casual basic at left3
    show hiflmc bowling basic at right3
    jd "Supernatural, inhuman, cryptid."
    show jd casual smirk
    jd "Whatever you want to call it."
    show jd casual basic
    mcjd "What should I call you, then?"
    hide hiflmc
    show jd casual happy at centre
    "JD grins, hesitating just long enough for anticipation to prick like a thorn under my skin."
    jd "Me?"
    show jd casual smirk
    jd "I'm the fucking Jersey Devil."

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False



    pause
    $ resets()
