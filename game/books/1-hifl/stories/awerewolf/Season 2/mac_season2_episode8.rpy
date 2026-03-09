label mac_season2_episode8:

    $tbc = False
    scene bg bowling at bg
    play music mackenziehunt

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show mac cop sad at centre
    "Work is slow as usual the next day, but when I sit down at the bar to unpack my lunch, Mackenzie comes in through the front."
    show mac cop sat at left4
    show hiflmc bowling basic at right4
    "A tense, nervous energy rolls off her in waves, and she approaches me with her hands in her pockets."
    show mac cop basic
    ma "Hey, you got a minute?"
    show hiflmc bowling surprised
    mcmac "Of course. Is something wrong?"

    ma "No. No, not wrong just..."
    show mac cop sad
    ma "..."
    hide hiflmc
    show jd casual shadessmirk at right4
    "I hear JD chuckle from over by the arcade. and Mackenzie shoots a glare their way."
    show mac cop angry
    ma "No one asked you, Davies."

    jd "You sure about that?"
    show jd casual shadeshappy
    jd "Because I remember getting some texts asking about-!"
    hide jd
    hide mac
    show mackenzie_s1_mini11 at bg
    "Her eyes narrow to a sliver of gold, and JD lets out a laugh taking a step back."
    hide mackenzie_s1_mini11
    show mac cop angry at left4
    show jd casual shadeshappy at right4
    jd "Doing something you hadn't trained for. Which you know, is a big deal."
    hide jd
    show mac cop basic
    show hiflmc bowling sarcastic at right4
    mcmac "Okay, I'm missing something."
    show hiflmc bowling basic
    mcmac "If you need help with something. Mac. I can ask Razi to take off the rest of my shift."
    hide hiflmc
    hide mac
    show razi casual smirk at centre
    "The man in question peeks his head in from the back, holding a crate of cheap craft beer in his arms."

    ra "I've been summoned."
    show razi casual happy
    ra "Oh hey, Mac."
    hide razi
    show hiflmc bowling basic at right4
    show mac cop basic at left4
    ma "Hey."
    show mac cop blush
    show hiflmc bowling surprised
    "She blushes, and I can't figure out why, unless Mackenzie wanted privacy for whatever favor she's asking for."
    hide hiflmc
    hide mac
    show razi casual happy at centre
    ra "If you want the night off, [genericfn], go for it."
    show hiflmc bowling surprised at right4
    show mac cop blush at left4
    mcmac "Uh...sure."

    mcmac "Does anyone want to fill me in on what I'm doing?"
    show mac cop basic
    ma "I need you with me tonight. On...patrol."
    show hiflmc bowling basic
    mcmac "I've been on patrol with you before."

    mcmac "Is there something different about this time?"
    show hiflmc bowling sad
    "I'm actually starting to get a little worried."

    "It's not like Mackenzie to hesitate like this, and I wonder if she's found something out she doesn't want to share with the others."
    hide mac
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Something about Grace, maybe? Or Gwen?)"
    hide hiflmc
    show diego doctor sleep at centre
    "Diego sighs from where he's been brooding at the corner of the bar, draining the last of the blood out of his glass before putting it down."
    show diego doctor basic
    di "Mackenzie is trying to ask you on a date."

    di "She just happens to be incredibly nervous about it, as is evident by the farce of the last five minutes."
    hide diego
    show hiflmc bowling surprised at right4
    show mac cop blush at left4
    "Mackenzie coughs, reaching to rub at the back of her neck."

    ma "Yeah."

    ma "Thanks for the assist, Diego."
    hide mac
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Oh.)"
    show hiflmc bowling blush at right4
    show mac cop blush at left4
    mcmac "Oh."

    "After a few seconds to process, I'm blushing as hard as Mackenzie is."
    show mac cop sad
    ma "Is that okay?"

    ma "I know I just made a total mess of things."
    show hiflmc bowling happy
    mcmac "Of course I want to go out on a date with you, Mac."

    mcmac "Even if it kind of sounded like a trip to the batcave up until now."
    show mac cop happy
    "All the tension rushes out of Mackenzie's posture, and she smiles wide at me."

    ma "Great."

    ma "How about I pick you up after work?"

    mcmac "Well, apparently I'm getting off early, so don't wait too long."

    ma "I won't. Promise."
    hide hiflmc
    show mac cop happy at centre
    "Mackenzie gives me a little wave before turning around, trying to walk back casually to the front door."
    show mac cop blush
    "When her boot hits the edge of it with a clang, she sighs and curses under her breath before leaving the bowling alley."
    hide mac
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(God, she's cute.)"
    hide hiflmc
    show hiflmc bowling sarcastic at right4
    show jd casual shadeshappy at left4
    "JD hasn't stopped smiling, but I raise an eyebrow right back at them."

    mcmac "So you all knew about this, huh?"
    hide hiflmc
    hide jd
    $menuhideborder = True
    menu macs2e8c1:
        "A. Go after JD.":
            $menuhideborder = False
            show hiflmc bowling angry at right4
            show jd casual shadeshappy at left4
            mcmac "You shouldn't be teasing Mac when she's nervous, JD."
            show jd casual shadessmirk
            jd "Hey, I did the sheriff a solid when she messaged me last night."

            jd "It's not my fault spitting it out is the hard part."
            hide jd
            hide hiflmc
        "B. Bug Razi.":
            $menuhideborder = False

        "C. Thank Diego.":
            $menuhideborder = False

            mcmac "At least Diego was upfront with me."
            mcmac "Thanks, doc."

            di "It's the least I could do, considering."

    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(What are friends for, right?)"
    hide hiflmc
    show razi casual smirk at left4
    show hiflmc bowling basic at right4
    ra "Honestly, it's impressive."
    ra "If you weren't human, I'd say you cast a spell on our fine sheriff."
    show razi casual happy
    show hiflmc bowling blush
    "Razi winks, and I blush bright red."

    mcmac "I didn't do anything!"
    hide hiflmc
    show jd casual shadeshappy at centre
    jd "I don't know about that. We better keep an eye on her, Razi."
    hide jd
    hide razi
    show hiflmc bowling blush at centre
    "I know they're both teasing, but that doesn't stop how warm my face is."
    show hiflmc bowling blush at right4
    show diego doctor smirk at left4
    di "If you happen to have a spell to make them both behave, let me know."
    hide hiflmc
    show razi casual surprised at right4
    ra "Wait, including me?"
    hide razi
    hide diego
    show hiflmc bowling blush at centre
    "After that interruption, the three of them fall into a playful debate, and I rest my elbows on the bar counter to daydream a little."
    hide hiflmc
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(A date, huh?)"
    scene bg main_night at bg
    show truck_back_night at bg
    show hiflmc beaniecasual basic at left2:
        zoom 1.05
    show mac tank basic at right2:
        zoom 1.05
    show truck_front_night at bg
    "Mackenzie drives me back home so we can pick up my car, then promptly asks if she can borrow the keys."

    "I hand them over in exchange for a kiss, and she takes us down the opposite end of Main Street."

    mcmac "Where exactly are we going?"
    show mac tank smirk
    ma "It's a surprise."
    show hiflmc beaniecasual happy
    mcmac "Is it also a surprise what's in the bag you brought?"

    ma "Uh-huh."

    "She looks far too pleased for me to try and spoil things, so I clamp down on my anticipation"
    scene bg drivein_theater_moon at bg
    "—until a fenced-in field appears in the distance, with a huge screen propped up in the back."
    scene bg main_night at bg
    show truck_back_night at bg
    show hiflmc beaniecasual surprised at left2:
        zoom 1.05
    show mac tank smirk at right2:
        zoom 1.05
    show truck_front_night at bg
    mcmac "The drive-in theater? We're going to see a movie?"
    show mac tank happy
    ma "We are. And only us."

    ma "I paid for an exclusive showing."
    show hiflmc beaniecasual happy
    "(That's so sweet!)"

    mcmac "Mac..."
    show mac tank smirk
    ma "You told me to save that money for a date, yeah?"

    ma "I could have had us get all dressed up and head into the city, but this seemed like more our speed."

    "(She's right. I wouldn't want to spend two hours in the car just to get dinner.)"
    "(This way, it's just us.)"

    "Mackenzie backs into the space right in the center, giving us the best view of the screen."
    show mac tank happy
    "After she kills the engine, I get a wink before she grabs the bag."

    ma "We'll have to get in the back to watch."

    ma "I brought blankets and stuff."
    #scene bg

    "Blankets and popcorn, as it turns out, making for a cozy spot in the bed of the truck."

    "Mackenzie checks the time on her phone, then pats the space beside her."

    ma "It should start in just a minute."

    "Snuggling in next to her, I crack open the popcorn and delve in for a handful."

    "It's both salty and sweet at the same time, which surprises me until I check the label."

    mcmac "Chicago-style? Nice."

    ma "It's good stuff."

    "The projector whirrs in the distance, queuing up the movie, and I smile once the screen comes to life."

    mcmac "So what kind of movie is this? Another comic book one?"

    ma "I thought a romance would be better for a date."

    ma "I hope you like it."

    mcmac "I bet I will."

    "The story starts with a single girl in the city, but I stare in shock when a lightning strike transports her to a fantasy world."

    "There's a lot of sword and sorcery for a romance, but then the love interest shows up."

    mcmac "Oh, she's super cute."

    ma "And super powerful."

    mcmac "Wishing you could cast spells now?"

    ma "Being a werewolf is enough, thank you."

    "I laugh and turn my attention back onto the screen."

    "When the two women have their first kiss, I catch Mackenzie blush out of the corner of my eye."

    "(Maybe the movie's giving her some inspiration?)"

    "(I could definitely help with that.)"

    $menuhideborder = True
    menu macs2e8c2:
        "A. Get frisky with Mac." (paidchoice = "paidchoice"):
            $menuhideborder = False

            mcmac "Hey, Mac."

            ma "Hmm?"

            "I push the popcorn out of the way, then run my fingers along the outside of her arm, tracing the striation of muscle there."

            mcmac "Want to get a little acting practice in?"

            "It might be the cheesiest thing I've ever said in my life, but Mackenzie's sharp smirk sends a bolt of warmth through me from head to toe."

            "She turns in one fluid movement, fingers framing my jaw before I'm drawn into a deep kiss."

            mcmac "Mm!"

            mcmac "Someone wasn't focusing on the movie."

            ma "Like I can really focus on anything else when you're around."

            "The growl at the end of Mackenzie's words leaves me dazed for a second, but I catch my breath and delve back into the kiss."

            "A subtle push against my back guides me forward, and I straddle Mackenzie's hips to bring our bodies together."

            mcmac "Guess I should be careful when you're working, then."

            mcmac "Don't want to be too much of a distraction."

            "(Okay, that's kind of a lie.)"

            ma "Yeah, right."

            ma "I see the way you look at me too, you know."

            "Her teeth graze my lower lip, and I let out a soft sound while my face flushes red."

            "(It's not that I mind being caught. I just didn't expect her to be so direct about it.)"

            mcmac "Mac, have you seen you?"

            ma "Only in the mirror every morning."

            mcmac "Mark me down as jealous of your mirror."

            "Mackenzie chuckles and kisses me again, leaving me to chase the warmth of her mouth until I have to break away to catch my breath."

            ma "There's an easy way to fix that, you know."

            mcmac "Oh? I'm listening."

            ma "If I wake up next to you in the morning, you beat the mirror to the punch."

            "(That's my kind of solution.)"

            mcmac "I like the way you think."

            mcmac "Guess I'll be seeing your bed a lot more often."

            "The first time was wild enough—in the best of ways."

            "I can't remember ever being touched like that before, by someone devoted to learning every inch of me."

            "And when I got to return the favor..."

            "(Mac makes really, really good noises when my hands are on her.)"

            ma "Now who's having trouble focusing?"

            "Mackenzie smiles against my lips, and I fumble a reply for a second before finding my words."

            mcmac "I was thinking about you. That doesn't count."

            ma "Oh, yeah?"
            ma "What about me?"

            mcmac "I, um…"
            mcmac "The other night. When we were together."

            "Broad hands make their way down my back in a slow caress,"

            "and the subtle shift of Mackenzie's hips sends an answering stir of heat under my skin."

            "Being in her lap is something else, especially with those powerful arms surrounding me."

            ma "I can't really blame you for that."

            ma "It was amazing."

            mcmac "You think so?"

            "I cough softly, realizing how that must have sounded."

            mcmac "It was for me, I mean. I hope it was the same for you too."

            "(Woof. Insecurity strikes again.)"

            "Mackenzie is stunned for a second, but she recovers with a smile."

            ma "Of course it was good for me."

            ma "If I didn't make that clear then, I'd be happy to make up for it now."

            mcmac "You don't have to."

            mcmac "But I definitely wouldn't say no."

            "Mackenzie kisses me again, hard enough to feel the hunger behind it."

            "Hunger for me, a need too strong to be so easily sated."

            "But I want to. I want to work for it, and leave Mackenzie as spent as she left me then."

            "(Werewolf endurance puts Olympians to shame.)"

            "My fingers search for her belt, tugging the bottom of her tank top up and out of the way as I return the kiss."

            "Mackenzie's abs flex under the pressure of my palm, the power in her whole body scarcely contained."

            "A groan escapes from between clenched teeth as I kiss down the hard line of Mackenzie's jaw to the softness of her throat,"

            "mixing tongue and teeth until her hands grasp hard at my back."

            ma "[genericfn]..."

            mcmac "You already took care of the date."

            mcmac "Let me take care of this. I got you, alpha."

            "I whisper the last few words and Mackenzie shivers, arms locking tight around my body to keep me close."

        "B. Keep watching the movie.":
            $menuhideborder = False
            "(Although a make-out session might not be what Mac wanted out of the date.)"

            mcmac "Enjoying the movie?"

            "Mackenzie clears her throat, and after a soft, embarrassed huff, she nods."

            ma "The...special effects are really good."

            "Her hand gives my shoulder a light squeeze, and I offer Mackenzie a bit of popcorn, blushing when the edge of her teeth catch on my fingertips."

            ma "Sorry."

            mcmac "Don't worry about it."

            "It's hard to focus on the movie when I'm flustered, but the story is sweet."

            "Mackenzie and I watch as the pair takes out a wicked queen together, then celebrate the victory with a long night in bed."

            "(Ahem. Wow.)"

            mcmac "What's this movie rated?"

            ma "Good question. I was just wondering that too."

            mcmac "The...cinematography is top-notch."

            ma "Uh-huh."

            ma "I'll have to check out what other films the director has done."

            "I laugh softly, then let out a sigh as Mackenzie turns to nuzzle against my neck."

            "Relaxing into the feeling is nice, and when the credits start to roll, I turn to give her a kiss on the lips."

            mcmac "This date has been so nice."

            ma "Yeah? I'll keep that in mind for the future."

            mcmac "Good thing. I'd hate for it to be one-hit wonder,"

    "Something stretches the screen from behind, catching my attention."

    "It warps the instant claws burst through, tearing through the moving image."

    "A shadowy figure lunges through the gap and lands on the front of my truck."

    "Metal groans at the impact, and the idle thump of footsteps carry up the windshield until the creature is leaning on top of the cab."

    "In a split second, I recognize her."

    mcmac "Gwen?!"

    "She smiles. There's nothing but a distant amusement in her eyes, the rest swept away by cold calculation."

    gwe "I kept telling myself it would be hard to sneak up on a werewolf."

    gwe "Your kind's a real pain, you know that, sheriff? You can smell everything."

    gwe "Not to mention the healing."

    "Mackenzie's entire posture shifts, putting her on all fours in the truck bed."

    "She hasn't changed yet, but I can feel the energy waiting to explode bared and eyes narrowed."

    ma "...It was you the other night."

    gwe "Did it really take you that long to figure out?"

    gwe "You small town hicks are something else."

    mcmac "Why are you doing this?"

    "Gwen laughs before rolling her eyes."

    gwe "Why do you think I'm doing this?"

    $menuhideborder = True
    menu macs2e8c3:
        "A. You hate werewolves.":
            $menuhideborder = False
            mcmac "I don't know, you have something a personal against werewolves?"

            mcmac "Are they your natural-born enemy or something?"

            gwe "No, I don't really care who I kill, really."

        "B. Teenage rebellion?":
            $menuhideborder = False
            mcmac "Some violent teenage rebellion?"

            gwe "God, do you really think I'm eighteen?"

            gwe "Next thing you'll be telling me Dr. Vampire just moisturizes really well."

        "C. An old grudge.":
            $menuhideborder = False

            mcmac "Let me guess, it's an old grudge."
            mcmac "The Hunt family did something to piss yours off."

            gwe "Nice try, but I'm not the one with the grudge."

    "(Then why is she trying to kill Mac?)"

    ma "There's another option."

    ma "You were paid to do it."

    gwe "You had to get it right eventually, I suppose."

    gwe "But yeah, your hide is worth a whole lot of money, Sheriff. All I have to do is tear it off you."

    "Gwen slowly twirls her wrist, making the flickering light of the projector glint against her claws."

    gwe "As for you, MC?"

    gwe "Your death is just a bonus. I don't like you."

    gwe "I don't like the way you look at me, and I don't like humans who know too much."

    mcmac "You don't like me because I was suspicious from the start."

    gwe "That doesn't help."

    gwe "But really, the meddling gets old fast."

    gwe "So now that the three of us are alone..."

    "She crouches as if to lunge at us, but Mackenzie transforms in the blink of an eye."

    "Her tackle lands before Gwen's feet even leave the truck, pinning her down hard against the roof."

    ma "I don't know what you are, but I don't have to."

    ma "You lost your chance to get the jump on me."

    gwe "Ooh, scary."

    gwe "You don't have the teeth to take me out, wolf."

    ma "I found them the second you threatened my girlfriend."

    "Mackenzie brings her head down, slamming it right against Gwen's."

    "It stuns her for a second, but then she draws her claws back into her hand, giving just enough room to bring them right under Mackenzie's ribs."

    mcmac "Mac, get off her!"

    "Gwen's claws jut out again, ready to pierce her through, only for Mackenzie to roll down the windshield and onto the hood."

    "A hiss of irritation pops between Gwen's teeth."

    gwe "Fine then."

    gwe "I'll just kill your human first."

    "Saying that was definitely a mistake."

    "Mackenzie's hand snaps forward, wrapping tight around Gwen's ankle."

    "A hard tug steals her balance, but the next surge of strength sends her flying."

    "Gwen hits the steel frame around the movie screen with a clang, falling to the ground in a tangle of limbs."

    "She starts to get to her feet, but when Mackenzie tenses, Gwen darts up and over the back fence."

    mcmac "She's getting away!"

    ma "Yeah, but we need to too."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
