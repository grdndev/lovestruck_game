##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode9:
    $tbc = False

    ##Change these to suit the story
    scene bg main_fog at bg
    play music mackenziehunt

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show hiflmc casual basic at left4
    show mac cop basic at right4
    "Mackenzie gets us back to town in record time, but she drops me off at the bowling alley, insisting I stay with the others to be safe."
    hide mac
    show hiflmc casual sad at centre
    "That doesn't stop me from stealing a glance at the sheriff's office."

    "This time, they just ripped the door clean off."

    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(How long is it going to be before Damien shows up with torches and pitchforks?)"
    hide hiflmc
    show hiflmc casual surprised at centre
    ra "Syd?"
    hide hiflmc
    show bg bowling_cosmic at bg
    show razi casual surprised at centre
    "Razi looks surprised to see me standing at the front, but that doesn't stop him from waving me over."

    show razi casual surprised at left4
    show hiflmc casual basic at right4

    ra "What's up? Where's Mackenzie?"

    mcmac "Across the street."
    show hiflmc casual sarcastic
    mcmac "That werewolf she arrested got broken out."

    hide razi
    show jd casual shadesbasic at left4
    jd "Oh, we figured out that much."
    show hiflmc casual surprised
    mcmac "What?"
    stop music fadeout 1.0
    play music hiflgetitdone
    hide jd
    hide hiflmc
    show damien casual smirk at left3
    show annabelle casual basic at right3

    "Jordan silently points towards the lanes in the back, and I'm stunned to see Damien and the other werewolf casually bowling strikes."

    "Each time the pins topple down, they laugh and make a big show of it."
    hide damien
    hide annabelle

    show jd casual shadesbasic at left4
    show hiflmc casual angry at centre
    show razi casual angry at right4

    "Squeezing myself out of sight, next to Razi, I drop my voice."
    mcmac "How long have they been here?"

    jd "About twenty minutes."
    show jd casual shadesangry
    jd "Mr. Buckskin over there dropped a hundred on the counter and said he wanted to bowl all night."
    show jd casual shadesbasic
    show hiflmc casual sarcastic
    mcmac "That's Damien. He's the one in charge."
    show hiflmc casual angry
    mcmac "We have to tell Mackenzie."
    show razi casual sad
    ra "I know that, but I thought she would be with you."
    show hiflmc casual blush
    "I know he doesn't mean it that way, but I suddenly flash back to the kiss and feel my face flush bright red."
    mcmac "N-No. She had to make sure her deputy was okay."
    show jd casual shadessad
    jd "You look... unreasonably warm."
    $menuhideborder = True
    hide jd
    hide hiflmc
    hide razi

    menu mace9c1:
        "A. Don't worry about it":
            $menuhideborder = False
            show jd casual shadessad at left4
            show hiflmc casual blush at centre
            show razi casual sad at right4
            mcmac "Don't worry about it. I'm fine."
            ra "If there's anything you're not telling us-!"
            show hiflmc casual happy
            mcmac "Hah, like that's ever happened."
            hide hiflmc
            show hiflmc casual_cu blush_cu at hiflmc_cu

        "B. Blame the adrenaline.":
            $menuhideborder = False
            show jd casual shadessad at left4
            show hiflmc casual basic at centre
            show razi casual sad at right4
            mcmac "Blame the adrenaline."
            show hiflmc casual angry
            mcmac "I just walked in here and the guy who took my sister is bowling."
            show jd casual shadesbasic
            jd "Alright, that's fair."
            jd "But we're not making a move on him unless you're safe and sound, alright?"
            show hiflmc casual happy
            mcmac "Thanks, JD."
        "C. Focus, JD.":
            $menuhideborder = False
            show jd casual shadessad at left4
            show hiflmc casual sarcastic at centre
            show razi casual sad at right4
            mcmac "Can we focus on the werewolf problems and not my problems?"
            hide hiflmc
            hide jd
            hide razi
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(Okay, there's a big part where the streams cross there, but they don't need to know that.)"
            hide hiflmc
            show jd casual shadessad at left4
            show hiflmc casual sarcastic at centre
            show razi casual sad at right4
            jd "Just checking on you."
            show hiflmc casual basic
            mcmac "I know, but we've got to focus."

    hide hiflmc
    hide jd
    hide razi
    show damien casual smirk at centre
    "Damien lets out a cheeky howl when he rolls another strike."
    hide damien
    show jd casual shadesbasic at left4
    show hiflmc casual angry at centre
    show razi casual sad at right4
    mcmac "Why aren't you two going after him?"
    show razi casual basic
    ra "Because my family would kill me for sticking my neck into werewolf politics without a good reason."
    ra "Unless Mackenzie clears it, the most I can do is keep an eye on them."
    show jd casual shadesangry
    jd "And stop them from leaving."
    show jd casual shadeshappy
    jd "I'm ready to break out the booze and work a little magic if that's what it takes."
    show hiflmc casual sad
    mcmac "Have they said anything about Grace?"
    show razi casual angry
    ra "No, just a lot of swagger and smiles like they own the place."
    hide hiflmc
    hide jd
    hide razi
    show annabelle casual basic at centre
    $sidecharone = "Werewolf"
    sid1 "Hey, boss!"
    hide annabelle
    show jd casual shadesangry at left2
    show hiflmc casual sad at right1
    show razi casual angry at right4
    "Razi turns around, eyes ice cold, and Jordan does the same."
    hide jd
    hide hiflmc
    hide razi
    show damien casual smirk at left4
    show annabelle casual basic at right4
    "I stay behind them, but I can see Damien and the other werewolf, who has a fifteen pound ball balance on her fingertips."
    hide damien
    show razi casual angry at left4
    ra "Can I help you?"

    sid1 "Maybe."
    sid1 "Catch!"
    hide annabelle
    hide razi
    show mackenzie_s1_mini8 at bg
    "She hurls the ball like it weighs nothing, sending it right towards Razi's head."
    hide mackenzie_s1_mini8
    show jd casual angry at left1
    show razi casual angry at left4 behind jd
    show annabelle casual basic at right4

    "JD's hand snaps up into the air, glasses clattering to the floor as they catch the ball before it even touches Razi."

    "Anger flashes in their eyes, glowing like an ember."

    hide annabelle
    show damien casual basic at right4

    dam "Just like I thought."
    dam "This isn't just wolf country, but you other types are a little hard to flesh out."

    jd "You could have asked."
    show jd casual smirk
    jd "I'd be happy to detail my abilities at length. Including a demonstration."

    dam "You and the man in charge there, right?"

    show razi casual smirk
    ra "The fact that you don't even know my name tells me how laughably out of your league you are."
    hide damien
    show annabelle casual angry at right4
    sid1 "Rude. Have a little hospitality."
    hide annabelle
    show damien casual smirk at right4
    dam "And come out from hiding, sweetheart."
    show jd casual angry
    show razi casual angry
    dam "I could smell you the moment you walked in."
    hide jd
    hide razi
    hide damien
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Damn it.)"
    hide hiflmc
    show hiflmc casual basic at left3
    show damien casual smirk at right4
    "I step out in front of Razi and Damien smiles, looking far too pleased with himself."
    dam "Did you finally get smart?"

    dam "You could just come with me if you want to see your sister."
    show razi casual angry at left5 behind hiflmc
    show jd casual angry at centre
    ra "That's not happening."
    jd "Not a chance in hell."
    "I'm infinitely grateful that both of them have my back."
    hide jd
    hide hiflmc
    hide razi
    show annabelle casual basic at right2
    show damien casual smirk at left2 behind annabelle
    "But Damien doesn't seem bothered in the least, throwing his arm around the other werewolf's shoulders."
    dam "When the eclipse comes, don't plan on running into Mackenzie's arms."
    stop music fadeout 1.0
    play music hiflsuspense
    dam "Because if you do, I'm going to watch her tear you to pieces."
    hide damien
    hide annabelle
    show hiflmc casual surprised at centre
    "A horrified chill creeps up my spine."
    show hiflmc casual surprised at left4
    show damien casual smirk at right4
    mcmac "What are you talking about?"
    dam "You'll see."
    dam "Now I'm going to walk out of here, and if any of you try to stop me, I'm painting the walls red."
    hide hiflmc
    show annabelle casual basic at right2
    show damien casual smirk at left2 behind annabelle
    "He gives us a mocking salute before turning to walk out of the alley."
    hide damien
    hide annabelle
    show hiflmc casual surprised at centre
    show razi casual angry at left4 behind hiflmc
    show jd casual angry at right4
    "I look at Razi and JD, who are almost twitchy with tension."
    mcmac "Are we-!"
    show razi casual sleep
    ra "Let them go. We need Mackenzie."
    show razi casual basic
    jd "Damn right we do."
    scene bg bowling_cosmic at bg
    stop music fadeout 1.0
    play music hiflgetitdone
    pause

    show mac cop angry at centre
    "Mackenzie practicaclly storms into the bowling alley, anger crackling through the air."
    "I can't blame her, especially since underneath the constant veneer of worry, I'm so pissed I can barely think."
    hide mac
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Who does Damien think he is?!)"
    hide hiflmc
    show mac cop angry at centre
    ma "Hey, is everyone alright?"
    show mac cop angry at left4
    show hiflmc casual sad at right4
    mcmac "Yeah."
    mcmac "He didn't touch us, but it was still pretty bad."
    show mac cop surprised
    ma "Razi said something about a bowling ball over the phone?"
    hide hiflmc
    show jd casual sad at right4
    jd "I caught it. The side is a little cracked now, though."
    hide jd
    show hiflmc casual sad at right4
    mcmac "Is your deputy okay?"
    show mac cop sad
    ma "Physically, yeah. But he's terrified out of his mind."
    ma "Damien tied him up and tossed him in the closet before the breakout."

    ma "Took him half an hour to work his radio in the dark."
    hide hiflmc
    show jd casual basic at right4
    jd "You know, I'm never one to advocate for more cops, but it seems like you need some help over there, Mac."
    show mac cop smirk
    ma "Going to turn over a new leaf and go into law enforcement, Davies?"
    show mac cop sad
    ma "More boots on the ground don't help me if they're ignorant to what's going on."
    hide jd
    show razi casual basic at right4
    ra "Who is this guy exactly, Mac?"
    show razi casual angry
    ra "He's another werewolf, I got that, but this kind of aggression sticks out like a sore thumb."
    show mac cop sleep
    ma "Well, there's several packs in Illinois. Big ones."
    show mac cop basic
    ma "Up north from them are the Riders."
    ma "Wisconsin mostly, but they have some other patches of territory."
    show mac cop angry
    ma "Damien claims he's part of them, but I'm not so sure about that."
    hide razi
    show hiflmc casual surprised at right4
    mcmac "Why?"
    ma "Because none of the werewolves he's with belong to that pack."
    ma "Why would you leave your family to pick up some stragglers and go to war?"

    hide hiflmc
    show jd casual surprised at right4
    jd "You think he's faking?"
    ma "I think he got kicked to the curb, and taking this land will put him back in their good graces."
    ma "If the Riders had Indiana and Wisconsin, they could put a lot of pressure on the packs that share a border."
    hide jd
    show razi casual basic at right4
    ra "And Damien would be the pack's new darling."
    ma "Exactly. Except he doesn't care about collateral damage."
    hide mac
    hide razi
    show hiflmc casual_cu sad_cu at hiflmc_cu

    "(My sister, the diner, the sheriff's office. What's next?)"
    stop music fadeout 1.0
    play music hiflsad
    hide hiflmc
    show hiflmc casual sad at right4
    show mac cop angry at left4
    mcmac "Damien said something else too."
    show mac cop surprised
    ma "What?"
    show mac cop surprised at left4
    show hiflmc casual sad at centre
    show razi casual surprised at right4

    "Razi gives me a surprised look, but I choke past the knot of worry in my throat."

    hide razi
    show mac cop surprised at left4
    show hiflmc casual sad at right4
    mcmac "That when the eclipse comes, you would turn on me."
    ma "Turn on you? Why would I ever-!"
    mcmac "I don't know!"
    mcmac "But god, Mac, he sounded so sure."
    hide mac
    show razi casual sad at left4
    ra "That doesn't sound like her at all."
    hide razi
    show jd casual basic at left4
    jd "It really doesn't."
    jd "The only reason we know Mackenzie is a werewolf is because she told us."
    jd "She's always been in total control over her shifting."
    jd "Every full moon."
    hide jd
    show hiflmc casual sad at centre
    "I believe them, I really do, but why would Damien go out of his way to make such a hollow threat?"
    hide hiflmc
    $menuhideborder = True

    menu mace9c2:
        "A. He must be lying.":
            $menuhideborder = False
            show jd casual basic at left4
            show hiflmc casual sad at right4
            mcmac "He must be lying to rattle me."
            show hiflmc casual sarcastic
            mcmac "I mean, Damien's already a violent kidnapper."
            hide jd
            show razi casual basic at left4
            ra "That's a good point."
            hide hiflmc
            hide razi
        "B. Maybe it's a trick?":
            $menuhideborder = False
            show jd casual basic at left4
            show hiflmc casual sad at right4
            mcmac "Maybe it's a trick to get us to split up?"
            mcmac "He pulls whatever this eclipse business is, I run from Mackenzie, and then Damien takes me."
            jd "Cruel, but I wouldn't put it past him."
            hide hiflmc
            hide jd

        "C. Damien knows something.":
            $menuhideborder = False
            show jd casual basic at left4
            show hiflmc casual sad at right4
            mcmac "Damien has to know something we don't."
            hide jd
            show mac cop surprised
            ma "What's that supposed to mean?"
            mcmac "About the eclipse. Whatever it is, he thinks it'll hurt you."
            hide mac
            hide hiflmc
    show razi casual sleep at centre
    "Razi rubs his temples, mouth twisting into a frown."
    show razi casual sad
    ra "I've never heard of anything like this."
    ra "Werewolf bonds are some of the strongest that exist."
    show razi casual sad at left4
    show mac cop basic at right4

    ma "Between packmates."
    ma "We certainly seem happy to take on anyone who isn't in the special club."

    hide mac
    hide razi
    show hiflmc casual sad at centre
    "I remember what Mackenzie said about packs, how I've teased that I might be part of hers, but at the end of the day I'm still human."

    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(What if it's not enough?)"
    hide hiflmc
    show mac cop angry at right4
    show razi casual sad at left4
    ma "If Damien shows up again, call me immediately. Understand?"
    show razi casual basic
    ra "I will. And now that I've seen him, I can ward off the bowling alley."
    hide mac
    show hiflmc casual surprised at right4
    mcmac "Ward?"
    show razi casual smirk
    ra "A bit of magic to keep him from entering the building."
    ra "He won't be able to play his little game twice."
    hide hiflmc
    show jd casual basic at right4
    jd "Don't forget to wall out his hanger-on too."
    show razi casual angry
    ra "Trust me, I haven't forgotten her."
    show razi casual happy
    ra "But after all that, I think we need to get some rest."
    hide razi
    hide jd
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(I couldn't agree more.)"

    scene bg main_night at bg
    show mac cop basic at left2
    show hiflmc casual sad at right2
    "Mackenzie and I step out of the bowling alley so Razi can get the place sealed off, but tension hangs in the air after the front door clicks shut."
    "The coolness of the fall breeze is countered by her hand being barely an inch from mine."
    show mac cop sad
    ma "It's still not safe for you to go home."
    mcmac "I know. Damien's still running around off the leash."
    ma "I should have come in with you."
    show mac cop angry
    ma "I would have seen him and put an end to this."
    show hiflmc casual surprised
    mcmac "No, that's not even close to your fault."
    mcmac "Grace wasn't with him."
    show hiflmc casual sad
    mcmac "And you would have had to make sure he hadn't killed your deputy."
    show mac cop basic
    ma "The deputy was fine."
    mcmac "But you didn't know that."
    mcmac "You went to protect him because you care."
    show mac cop surprised
    mcmac "Don't close your heart on me, Mac."
    mcmac "It's part of who you are."
    ma "..."
    hide hiflmc
    show mac cop sad at centre
    "She looks away from me and up to the night sky."
    "Stars twinkle past the shroud of the clouds overhead, and the moon is still full enough to shine through them."
    hide mac
    show mac cop_cu sad_cu at mac_cu
    ma "Are you coming home with me tonight?"
    $menuhideborder = True
    hide mac

    menu mace9c3:
        "A. Go home with Mac." (paidchoice = "paidchoice"):
            $menuhideborder = False
            stop music fadeout 1.0
            play music hiflliteromance

            show mac cop sad at left3
            show hiflmc casual happy at right3
            mcmac "As long as that's okay with you."
            show mac cop happy
            "Her smile makes my heart fly right up into my throat."
            ma "I wouldn't have it any other way."
            show mac cop smirk
            ma "Let's get going."
            ma "I have a feeling tomorrow's gonna be a long day."

            scene bg road_night at bg
            "The drive back is quiet, but I use it to appreciate the stars until Mackenzie pulls up in front of her house and kills the engine."

            scene bg mackenzie_bedroom_lights at bg

            "We head inside together, going right to her bedroom."

            show mac cop basic at left3
            show hiflmc casual basic at right3
            "She moves her laptop so I can sit down right next to her on the end of the bed, and now that we're inside, I feel like I can finally relax."
            show mac cop smirk
            ma "Kind of left off on a complicated note, didn't we?"
            show hiflmc casual blush
            mcmac "Complicated? It felt pretty good to me."
            show mac cop blush
            ma "...It did to me too."
            ma "Everything felt right. So right."
            show hiflmc casual surprised
            "Something almost like wonder pervades Mackenzie's voice, and it hits me like a bolt to the heart."
            show hiflmc casual basic
            "I have to ask her, I can't just leave it at what happened."
            show mac cop surprised
            mcmac "Mac, why did you kiss me?"
            show mac cop smirk
            ma "Because I wanted to, first and foremost."
            show hiflmc casual happy at centre
            "I nudge her shoulder, laughing softly."
            mcmac "I wanted you to, too. That's not what I meant."
            show mac cop sad
            ma "I keep waiting for you to run away."
            show hiflmc casual surprised
            mcmac "...What?"
            ma "The night of the full moon, when you saw exactly what I was, I remember the fear in your eyes."
            show mac cop happy
            ma "But then you looked past the wolf and realized it was me."
            ma "You found out my deepest secret and just accepted it."
            show mac cop sad
            ma "Sharing myself with you feels so easy."
            ma "I have to stop myself from blurring the lines."
            mcmac "Between me and your job?"
            show mac cop sleep
            ma "Yeah."
            show mac cop smirk
            ma "But I still want you in the equation."
            ma "That's an understatement."
            show mac cop blush
            ma "I want you altogether."
            show hiflmc casual blush
            "A rich blush darkens her face, but I can't stop myself from getting flustered either."
            "For lack of the right words, I reach over and snag Mackenzie's hand holding it tight in my own."
            show hiflmc casual happy
            mcmac "Maybe accepting you're an alpha is changing how you feel."
            show mac cop surprised
            ma "You think so?"
            mcmac "I think you've held back for a long time."
            show mac cop sad
            ma "...I thought it was the only way I could keep everything held together."
            ma "But in the interrogation room, I felt that change."
            ma "I realized how much untapped power I'd thrown aside."
            mcmac "I saw it too."
            mcmac "And I know you'll keep me safe. I don't care what Damien said."
            show mac cop sleep
            "Mackenzie's face tenses a little at his name, gbut she nods, gently running her thumb over the line of my knuckles."
            show mac cop basic
            ma "I still have to sort this out. What's the wolf and what isn't."
            hide mac
            hide hiflmc
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Both sides of her seem to want me close, but I can't blame her for wanting to know why.)"
            hide hiflmc
            show hiflmc casual happy at right2
            show  mac cop basic at left3
            mcmac "I know. I'll wait for you."
            show mac cop happy
            show hiflmc casual blush
            "A yawn catches me off-guard and Mackenzie smiles, letting go of my hand."
            ma "Let's get to bed."
            show hiflmc casual happy
            mcmac "Definitely. Do you have like an air matress or..."
            show mac cop surprised
            show hiflmc casual blush
            "Her raised eyebrow is the only 'no' I need, and when the pieces fall together..."
            "I'm not sure if I've just been plunged into my best fantasy or my worst torment."
            ma "It's a pretty big bed."
            hide hiflmc
            hide mac
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(A bed I have to share with someone gorgeous while pretneding I don't want things to go further!)"
            hide hiflmc
            show hiflmc casual blush at right4
            show mac naked basic at left4
            "My internal monologue dies down to a squeak as Mackenzie starts stripping down, and I get a full view of the muscle in her legs too."
            "As she settles back across the pillows, every flex and shift only improves my view."
            "(I have no idea what her routine is, but I'd love to be a part of it.)"
            show mac naked smirk
            ma "Lights are going out in five."
            hide mac
            show hiflmc casual sarcastic at centre
            "That knocks me out of my stupor, although I nearly trap my head in my own shirt trying to get undressed."
            show hiflmc pajamas noglassessurprised
            "When I get onto the bed, I'm surprised to find only a single thing blanket, despite the chill of the season."
            show bg mackenzie_bedroom_night at bg
            show mac naked basic at left3
            show hiflmc pajamas noglassessurprised at right3
            "It doesn't seem to biother Mackenzie in the least, and she rolls over to turn off the bedside lamp."
            show hiflmc pajamas noglassessad
            "If everything wasn't already awkward enough, I start shivering after a few minutes in the dark."
            mcmac "How are you not cold?"
            show mac naked basic at centre behind hiflmc
            show hiflmc pajamas noglassesblush
            "I didn't mean to say it out loud, but then Mackenzie turns from her side and pressed up against my back."
            "The moment her arm slips around my stomach, I have to bite my lip to keep from making a very inappropriate sound."
            show mac naked smirk
            ma "I'm never cold."
            show mac naked sleep
            "She falls asleep a moment later, but my heart is going too fast for me to even think about closing my eyes."
            "(I don't mind it. Feeling Mac this close is totally worth it.)"
            hide mac
            hide hiflmc
        "B. Stay at the bowling alley":
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(I want to. I desperately want to.)"
            "(But I wouldn't be doing it to be safe. I wouldn't be doing it for Grace.)"
            hide hiflmc
            show hiflmc casual basic at right4
            show mac cop sad at left4
            mcmac "Damien and his friend won't be able to get into the bowling alley anymore."
            show hiflmc casual sad
            mcmac "I don't want them trashing your house trying to find me."
            show hiflmc casual happy
            mcmac "I'll just crash in the back."
            hide hiflmc
            show mac cop surprised at centre
            "For a second, I think Mackenzie is going to ask me if I'm sure, but she gives a short nod instead."
            show mac cop basic
            "With a soft goodbye, she takes her keys and walks off to her car."
            hide mac
            show hiflmc casual sad
            "I shudder with the next gust of wind, suddenly freezing, and duck back through the bowling alley door."
            show bg bowling_cosmic at bg
            show hiflmc casual surprised at right4
            show razi casual basic at left4
            "Razi's hands are glowing blue, but the light fades when he meets my eyes."
            hide razi
            hide hiflmc
            show hiflmc casual_cu basic_cu at hiflmc_cu
            "(So that's new. Just going to roll with it.)"
            hide hiflmc
            show hiflmc casual basic at right4
            show razi casual basic at left4
            ra "Did you leave your phone or something, [genericfn]?"
            show hiflmc casual sad
            mcmac "I was going to stay here tonight, if that's okay."
            mcmac "Mackenzie doesn't think my house is safe."
            hide razi
            show jd casual basic at left4
            jd "It probably isn't. But why aren't you with her?"
            show hiflmc casual surprised
            mcmac "Because..."
            hide hiflmc
            hide jd
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(God, how much should I even explain? Does Mac care if they know we-!)"
            hide hiflmc
            show jd casual basic at left4
            show hiflmc casual sad at right4
            mcmac "Being that close to her is complicated right now."
            show jd casual smirk
            show hiflmc casual surprised
            jd "Yeah, you have a crush. We got that part."
            show hiflmc casual blush
            mcmac "Uh!"
            hide jd
            show razi casual smirk at left4
            ra "And you've been living inside her personal space for days now."
            ra "It's clear she doesn't mind."
            hide razi
            hide hiflmc
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(All I need right now is Diego to sweep in from the ceiling and drag me to complete the circle of embarrassment.)"
            hide hiflmc
            show hiflmc casual sad at left4
            show razi casual basic at right4
            mcmac "I'm not a werewolf, Razi. There's only so much I can do."
            hide razi
            show jd casual sad at right4
            jd "On the night another werewolf accused her of wanting to go feral on you, what she probably needed was your trust."
            hide jd
            hide hiflmc
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Ouch. I probably deserved that.)"
            hide hiflmc
            show jd casual sad at left4
            show hiflmc casual sarcastic at right4
            mcmac "Can we talk less about my love life and more about the fact you can catch a speeding bowling ball."
            show jd casual basic
            show hiflmc casual sad
            jd "I could have caught five of them and juggled, [genericfn]. That's not the point."
            hide jd
            show razi casual basic at left4
            ra "Mackenzie shouldn't be alone either."
            mcmac "I know. Even though she keeps trying to be."
            hide hiflmc
            hide razi
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(And then I let her. Ugh.)"
            hide hiflmc
            show razi casual basic at left4
            show hiflmc casual sad at right4
            mcmac "I'll talk to Mac in the morning, okay?"
            mcmac "It wasn't about trusting her. It was about trusting myself."
            mcmac "If something I did stopped Grace from being found..."
            "I don't have to finish my sentence."
            show razi casual sad at centre
            show jd casual basic at left4
            "JD nods, and Razi gives me a soft pat on the shoulder."
            hide jd
            ra "You know where the break room cot is."
            ra "Go and get some sleep."
            ra "I'll head upstairs and do the same."
            hide razi
            hide hiflmc
            show jd casual basic at centre
            jd "I'm going for a quick walk around town."
            jd "Just to make sure everything stays quiet."

            show jd casual basic at left4
            show razi casual basic at right4
            ra "Watch out for Damien."
            show jd casual angry
            jd "Oh, I will."
            show jd casual happy
            jd "He might have the moonlight, but it's almost the devil's hour."
            hide razi
            show jd casual happy at centre
            "Jordan turns to leave without another word, a new swagger in their step."
            hide jd
            show hiflmc casual noglassessad at centre
            "Exhaustion settles over me as soon as Razi heads upstairs, and I turn in."
            show hiflmc casual noglasseshappy
            "When I dream, it's of Mackenzie."
            hide hiflmc
    scene bg main_day at bg
    stop music fadeout 1.0
    play music hifleveryday
    pause

    show hiflmc casual basic at centre
    "I have to get up early to move my truck. and I make a stop at the corner store to snag something quick for breakfast."
    show hiflmc casual happy
    "After a second thought, I buy a cup of coffee for Mackenzie and head back out to the street."
    stop music fadeout 1.0
    play music hiflaction
    show hiflmc casual surprised
    "A foot from my car, I catch sight of a familiar face in my side mirror and freeze in place."
    show damien casual smirk at left2 behind hiflmc
    dam "Morning, [genericfn]."
    mcmac "Mac-!"
    hide hiflmc
    hide damien
    show damien casual_cu basic_cu at damien_cu
    "He lunges forward, clapping a hand over my mouth to cut off the scream."
    show damien wolf_cu wolfbasic_cu at damien_cu
    "When Damien pushes me back against the car, his eyes snap to gold."
    dam "You're going to be quiet. And you're going to give me your keys."
    show damien wolf_cu wolfsmirk_cu
    dam "Or the next thing I do is tell my girl to kill Grace."
    "With trembling fingers, I drop the keys into his open hand."
    hide damien
    show truck_back_day at bg
    show hiflmc casual surprised at left3:
        zoom 1.05
    show damien wolf wolfsmirk at right3:
        zoom 1.05
    show truck_front_day at bg
    "He takes hold of me and opens the door, shoving me into the passenger seat."
    dam "Now we're going for a ride."
    hide damien
    hide hiflmc
    hide truck_back_day
    hide truck_front_day

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
