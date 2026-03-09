label mac_season2_episode6:

    $tbc = False
    scene bg heroine_home_lights at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show hiflmc casual basic at centre
    "Razi texts me after sundown, inviting me to a dinner with everyone at the bowling alley, and I can guess why."

    "I waffle on the invitation for ten minutes before messaging Mackenzie, asking if she’s going too."
    show hiflmc casual sad
    "It’s a yes."
    hide hiflmc
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Alright, I can be a good sport. Plus free food.)"
    scene bg bowling_cosmic at bg with fade
    show hiflmc casual surprised at centre
    "I’m the last one to get to the bowling alley, but as soon as the door opens, I smell something delicious."

    "Someone’s pushed all the tables together, and the amount of food balanced on them is staggering."

    mcmac "Oh my god."
    hide hiflmc
    show mac tank smirk at centre
    ma "Looks good, huh?"
    show mac tank happy
    "I turn to see Mackenzie leaning against the wall, and she gives me a little wave."
    show mac tank happy at left3
    show hiflmc casual happy at right3
    mcmac "Were you waiting for me?"

    ma "Of course I was."
    show mac tank smirk
    ma "We better grab a plate, though. JD’s chomping at the bit."
    hide hiflmc
    hide mac
    show jd tank angry at centre
    jd "I heard that, sheriff!"
    hide jd
    show diego casual smirk at centre
    di "That’s because Razi kicked them out of the kitchen earlier for taste-testing."
    show diego casual smirk at left3
    show hiflmc casual basic at right3
    "Diego greets me with a smile, raising his glass."
    show hiflmc casual happy
    "The dark stain lingering in the bottom of it is unmistakably blood, but I swallow my knee jerk reaction and smile back."
    hide diego
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(It’s not his fault. He kind of needs it to live.)"
    hide hiflmc
    show gwen casual happy at centre
    gwe "You’re all kind of like one big family, huh?"

    "Gwen’s voice comes from behind me, still light and energetic despite a long day at the diner."
    hide gwen
    show razi casual smirk at centre
    "Razi appears right after, a saucepan in hand."

    ra "Everyone ready to eat?"
    hide razi
    show jd tank happy at centre
    jd "Please."
    hide jd
    show razi casual smirk at right3
    show gwen casual happy at left3
    gwe "Razi, this looks amazing!"
    show razi casual happy
    "He winks, but the warmth in Razi’s smile isn’t a tease."
    hide razi
    hide gwen
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(It’s always nice to have appreciation for your work, right?)"
    hide hiflmc
    show razi casual happy at right3
    show gwen casual happy at left3
    ra "Just something I whipped together."

    ra "Eating food in a new place helps you settle into it, you know."
    hide razi
    hide gwen
    show hiflmc casual happy at right2
    show mac tank basic at left2
    "We jostle for seats around the table, and Mackenzie snags one right next to me."
    hide hiflmc
    hide mac
    show gwen casual surprised at centre
    "Gwen is on her other side beside Razi, still openly gawking at the meal."
    hide gwen
    show diego casual happy at centre
    di "You’re welcome to my share, Gwen. I’ll appreciate from a distance."
    hide diego
    show gwen casual happy at centre
    gwe "Thanks, doc."
    hide gwen
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Doc? She doesn’t even know him.)"
    hide hiflmc
    show hiflmc casual basic at centre
    "Refusing to let my irritation get in the way of dinner, I gather my share onto a plate and start eating."
    show hiflmc casual surprised
    "Everything is delicious, but the last dish is so spicy that my eyes start to water."
    show hiflmc casual surprised at left3
    show razi casual sad at right3
    ra "[genericfn], you okay? I think you went a little heavy on the sauce."
    hide razi
    show jd tank smirk at right3
    jd "Yeah, that’s supposed to go over everything else."
    show hiflmc casual sad
    mcmac "Oh."
    hide jd
    show hiflmc casual sad at right2
    show mac tank smirk at left2
    "My answer comes out like a wheeze, and Mackenzie snags a piece of bread from the centre of the table before offering it to me with a smile."

    ma "Eat this real quick."
    show hiflmc casual basic
    "The first bite cools my tongue down a little, and by the time I’ve eaten the rest, it doesn’t feel like my mouth is burning anymore."
    hide hiflmc
    hide mac
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(My dignity, however, packed up and left for greener pastures.)"
    hide hiflmc
    show hiflmc casual basic at right2
    show mac tank smirk at left2
    ma "You okay?"
    hide hiflmc
    hide mac
    $menuhideborder = True
    menu macs2e6c1:
        "A. I'm a mess.":
            $menuhideborder = False
            show hiflmc casual sarcastic at right2
            show mac tank smirk at left2
            mcmac "I'm kind of a mess."
            ma "You're a cute mess."
            hide mac
            hide hiflmc
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(And now I’m blushing at the dinner table.)"

        "B. Now I am.":
            $menuhideborder = False
            show hiflmc casual happy at right2
            show mac tank smirk at left2
            mcmac "Now I am."
            mcmac "Thanks for the save."
            show mac tank happy
            ma "That's what I'm here for, right?"
            hide mac
            hide hiflmc
        "C. Too embarrassed to live.":
            $menuhideborder = False
            show hiflmc casual sarcastic at right2
            show mac tank smirk at left2
            mcmac "Just too embarrassed to live."
            mcmac "I'll probably recover at some point."
            ma "You'll be fine. Don't worry about it."
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(This is really not the time and place I wanted to make a fool of myself.)"
    hide hiflmc
    show hiflmc casual basic at left4
    show gwen casual basic at right4
    gwe "So, [genericfn]. I have a question."

    mcmac "...Yeah?"

    gwe "Are you really human?"
    hide hiflmc
    hide gwen
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(I thought we weren’t supposed to ask that. What kind of double standard?)"
    hide hiflmc
    show hiflmc casual sarcastic at left4
    show gwen casual basic at right4
    mcmac "Last time I checked, Yeah."
    show gwen casual surprised
    gwe "This must be so weird, then."
    show gwen casual basic at right5
    show hiflmc casual basic at left1
    show mac tank smirk at left5
    ma "She took to it pretty well, actually."
    show hiflmc casual happy
    "I reach for Mackenzie’s hand under the table, grateful for the backup."
    show hiflmc casual sad
    "Still there’s something undeniably awkward about having my humanity pointed out."
    hide hiflmc
    hide mac
    hide gwen
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(I shouldn’t be the odd duck here when she’s the new girl!)"
    show hiflmc casual_cu angry_cu at hiflmc_cu:
        xpos +50
    show mac tank_cu basic_cu at mac_cu:
        xpos -50
    "An irritated comment is on the top of my tongue when Mackenzie leans over and whispers in my ear."

    ma "Play nice. She’s young."
    show hiflmc casual_cu basic_cu
    mcmac "Make me, alpha wolf."
    show mac tank_cu basic_cu
    "Her eyes light up with the challenge, fingers tensing around mine."
    show mac tank_cu surprised_cu
    ma "I could if you really wanted me to."
    hide hiflmc
    hide mac
    show mac tank_cu smirk_cu at mac_cu
    "Mackenzie’s gaze is so intense that I can’t look away."

    "Even without her eyes shifted to gold, I can sense the wolf right under the surface, waiting for my answer."
    hide mac
    show razi casual smirk at centre
    "Then Razi clears his throat."
    hide razi
    show jd tank smirk at right5
    show hiflmc casual blush at left1
    show mac tank smirk at left5
    "I blush, looking away from Mackenzie just in time to catch JD rolling their eyes."
    hide hiflmc
    hide mac
    show jd tank smirk at centre
    jd "If you two feel so competitive right now, hope about a game?"
    show jd tank smirk at right5
    show hiflmc casual basic at left1
    show mac tank surprised at left5
    ma "What kind of game would that be?"
    show jd tank happy
    jd "Clearly the most high-strung sport there is. Air hockey."
    show mac tank smirk
    show hiflmc casual happy
    "Despite the interruption, it’s hard not to laugh when JD sounds so serious."
    show jd tank smirk
    jd "Razi and I will take you and the sheriff on. Pair versus pair."
    show mac tank surprised
    show hiflmc casual surprised
    jd "And if we win, you two take the mating games down a notch."

    mcmac "It’s not—!"
    show mac tank blush
    "I don’t think I’ve ever seen Mackenzie blush so hard in her life."
    show hiflmc casual blush
    hide jd
    show jd tank smirk at right5
    show hiflmc casual blush at left1
    show mac tank smirk at left5
    "When Gwen giggles behind her hands, I start turning red too."
    hide gwen
    show jd tank smirk at right5
    ma "Davies, I swear..."

    jd "Listen, I know how werewolves work."

    jd "So play at home or play here. Either way I’ll make my point."
    hide hiflmc
    hide jd
    hide mac
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(It wouldn’t be JD if they weren’t trying to rile Mac up. I wish their timing was better, though.)"
    hide hiflmc
    show jd tank smirk at right5
    show hiflmc casual basic at left1
    show mac tank happy at left5
    ma "You’re on."
    hide jd
    show mac tank happy at left3
    show hiflmc casual basic at right3
    "Mackenzie turns to me, the fire burning in her eyes now with the spirit of competition."

    "She’s eager to win, and wants me to help her prove it."
    hide hiflmc
    hide mac
    show mac tank_cu smirk_cu at mac_cu
    ma "Come on, partner. You in?"
    hide mac
    $menuhideborder = True
    menu macs2e6c2:
        "A. Prove you're Mac's mat-! ...Partner." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mac tank happy at left3
            show hiflmc casual happy at right3
            mcmac "Are you kidding? I'm going to kick JD's ass."
            hide mac
            show jd tank smirk at left3
            jd "You're dreaming."
            show jd tank happy
            jd "But if you mean it, take me out to the back alley sometime."
            hide jd
            show razi casual smirk at left3
            show hiflmc casual blush
            "They wink and Razi chuckles, tipping my confidence over into a deep blush."
            hide razi
            show mac tank happy at left2
            show hiflmc casual blush at right2
            "Mackenzie slips her arm around my shoulder, giving them a light squeeze."

            ma "We've got this."
            hide mac
            hide hiflmc
            show razi casual basic at centre
            ra "Alright, I'm turning on the table."
            show razi casual sad at right3
            show jd tank basic at left3
            ra "I swear, Jordan, you've got to give a man a warning before roping him into something."
            show jd tank smirk
            jd "Do I? No, I don't think that's the basis of our friendship at all."
            hide jd
            hide razi
            show diego casual basic at left3
            show gwen casual basic at right3
            "I laugh, noting out of the corner of my eye when Gwen takes a seat next to Diego."

            "He pointedly moves his glass away from Gwen's before refilling hers with soda."
            show gwen casual happy
            gwe "Go get 'em, JD!"
            hide gwen
            hide diego
            show mac tank happy at left3
            show hiflmc casual basic at right3
            ma "Uh oh. They've got a cheerleader."

            mcmac "Diego, can you shimmy a little for us to make things even?"
            hide hiflmc
            hide mac
            show diego casual smirk at centre
            di "Don't you wish."
            hide diego
            show bg bowling_arcade_cosmic at bg
            show hiflmc casual basic at right3
            show mac tank basic at left3
            "Mackenzie passes me a striker as the air hockey table starts to him, and JD flips the puck down into the center."
            show hiflmc casual angry
            "They get reader next to Razi, but I dare to make the first move."
            hide hiflmc
            hide mac
            show jd tank angry at centre
            "The puck zigzags towards the goal, but JD is right there to counter it, and sends the puck back so fast I can't even see it."
            hide jd
            show mac tank smirk at centre
            "Mackenzie blocks just a split second faster."
            hide mac
            show jd tank angry at centre
            jd "Damn it."
            hide jd
            show mac tank smirk at centre
            ma "I'm onto you, Davies."
            hide mac
            show jd tank smirk at centre
            jd "We'll see about that."
            hide jd
            show hiflmc casual surprised at centre
            "I'm having to block and move almost without thinking."
            hide hiflmc
            show jd tank angry at left3
            show razi casual angry at right3
            "My only saving grace is that Razi and JD keep going for the same strikes, and half the time, it sends the puck spinning wildly into the center."
            hide jd
            hide razi
            show hiflmc casual angry at right3
            show mac tank basic at left3
            "Behind my hectic defense is Mackenzie's fluid offense and we're up two points before the puck zooms back my way."
            show hiflmc casual surprised
            "I block it, but the striker pops right out of my hands and rolls off the side of the table."
            hide hiflmc
            hide mac
            show bg bowling_cosmic at bg
            show diego casual basic at centre
            di "Please don't injure each other. I'm not on the clock right now."
            hide diego
            show bg bowling_arcade_cosmic at bg
            show hiflmc casual sarcastic at centre
            mcmac "Oh, come on. It didn't hit anyone!"
            show hiflmc casual sad
            "I quickly duck under the table to snag the striker, but it's so far underneath now that there's no way to get it."
            show mac tank basic at left2
            show hiflmc casual surprised at right2
            "Mackenzie taps my arm, drawing my attention back to the game."
            show mac tank smirk
            ma "One more point and we win this."
            show hiflmc casual sad
            mcmac "But I don't have anything to hit the puck with."
            hide hiflmc
            show mac tank_cu happy_cu at mac_cu
            ma "You trust me?"
            hide mac
            show hiflmc casual_cu happy_cu at hiflmc_cu
            mcmac "With my life."
            hide hiflmc
            show hiflmc casual basic at right2
            show mac tank smirk at left2
            ma "Then this game's in the bag."
            hide hiflmc
            hide mac
            show mackenzie_s2_mini7 at bg
            "Mackenzie brings her hand over mine, locking it on the striker that's left."
            hide mackenzie_s2_mini7
            show bg bowling_arcade_cosmic at bg
            show jd tank angry at centre
            "JD feints with the puck, looking for an opening when my fingers tense."
            hide jd
            show hiflmc casual basic at right1 behind mac
            show mac tank basic at left1
            ma "Let's move together."

            mcmac "Okay."
            show hiflmc casual surprised
            "Agreeing doesn't really prepare me for how fast Mackenzie's reflexes really are."

            "When JD makes a move, she counters with one tap, then urges me forward on the offensive."
            hide mac
            hide hiflmc
            show razi casual surprised at centre
            "Razi deflects by centimeters, but surprise shows on his face."
            hide razi
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(Can we really do this?)"
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(...Hell yeah, we can.)"
            hide hiflmc
            show hiflmc casual surprised at right1 behind mac
            show mac tank angry at left1
            "JD manages to score one point, but when Mackenzie leads me in a quick feint, our next shot slips right in the gap between Razi and JD's strikers."
            hide mac
            hide hiflmc
            show jd tank sad at left4
            show razi surprised at right4
            jd "Son of a... sacrificial goat."
            show razi casual smirk
            ra "Unorthodox, but impressive."
            show jd casual angry
            jd "They only had one striker!"
            show razi casual basic
            ra "Which put them at a disadvantage. We lost, JD."
            hide razi
            hide jd
            show bg bowling_cosmic at bg
            show diego casual smirk at centre
            di "And with no injuries. I'm ecstatic."
            hide diego
            show gwen casual happy at centre
            gwe "Good job, you two!"
            hide gwen
            show bg bowling_arcade_cosmic at bg
            show mac tank smirk at left2
            show hiflmc casual blush at right2 behind mac
            "Mackenzie's hand relaxes around mine, but her fingers trace up the line of my arm."

            "Instead of celebrating the win with everyone else, her attention is wholly centered on me."
            hide hiflmc
            hide mac
            show mac tank_cu smirk_cu at mac_cu
            ma "We should claim our prize, right?"

            ma "Win one game, go right back to another."
            hide mac
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(Except she's not playing, and I'm so, so glad.)"
            hide hiflmc
            "She dips me back into a deep kiss, one hand capturing my wrist and the other a warm pressure against my shoulder blades."

            "It's like I'm floating, flush with victory as I match the desire between her lips with my own."
            show jd tank smirk at centre
            jd "Is it hot in here or is it just me?"
            show jd tank smirk at left3
            show razi casual smirk at right3
            ra "Cut them a break, JD. You're the one who made the bet."
            show jd tank sad
            jd "Because I thought I'd win."
            hide razi
            show hiflmc casual happy at right3
            "Breaking away from the kiss, I smirk at them."

            mcmac "Better luck next time."
            hide jd
            show mac tanki happy at left3
            ma "Let's leave them to the party, [genericfn]. We can take this back to my place."
            hide mac
            hide hiflmc
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(Fun as teasing JD is, I'm not turning down that offer.)"
            hide hiflmc
            show mac tank happy at left2
            show hiflmc casual happy at right2 behind mac
            "Standing up again, I slip my arm around Mackenzie's waist, catching my fingers in the back of her belt."

            mcmac "Have fun, everyone. We'll get out of your hair."
            hide hiflmc
            hide mac
            show bg bowling_cosmic at bg
            show diego casual smirk at right4
            show mac tank happy at left4
            show hiflmc casual happy at left2 behind mac
            "Diego raises his glass in a mock toast as Mackenzie and I walk out of the bowling alley, and I'm smiling by the time we see starlight."

        "B. Sit out the game":
            $menuhideborder = False

            "(I’m not really in the mood for games after the rest of today.)"

            mcmac "Sorry, Mac."

            mcmac "We just ate, and it’s been a really long day."

            "I see Mackenzie try to hide her disappointment,  but if she was wolfed out, I’m pretty sure her ears would have just drooped."

            gwe "I’ll help you out, sheriff!"

            "(Oh, for fuck’s sake.)"

            jd "Ooh, wild card. I’ll allow that."

            "Mackenzie gives me a sheepish smile before getting to her feet."

            "I don’t want her to have to lose because I stepped away, but I wish she had any other partner helping her out."

            ra "Let me get the table set up."

            di "I’m not refereeing this one. Passion will win the day."

            "There’s a subtle hum as Razi turns it on, and the strikers start drifting across the smooth surface of the table."

            "JD catches the puck when it pops out, giving it a spin on their fingertips."

            gwe "I’ve never played this before."

            ma "Don’t worry. It’s more about relying on reflex than anything else."

            ma "And we’ve got a cheerleader on our side, right?"

            "Mackenzie looks over her shoulder at me, and although I’m feeling far from cheery, I want Mackenzie to know I have her back."

            "When I mimic a pair of pom-poms, she laughs and picks up her striker."

            ra "Try to lay off the powers, huh?"

            jd "Is that directed to me or them?"

            ra "Everyone. But if you get scorch marks all over this table, you’re scrubbing them off."

            "JD offers a sarcastic little salute with one hand, then drops the puck with the other."

            "Their first strike is a whip-fast blur of movement."

            "Mackenzie blocks it from the goal by centimetres, and JD scowls, but Razi is ready on the defence."

            "She goes back and forth with him for a good minute before Gwen accidentally bumps her arm."

            jd "Sorry. I thought I could catch it in time."

            ma "Don’t worry about it."

            "The faint growl in Mackenzie’s voice says otherwise, and the competition only heats up from there."

            "Mackenzie managed to tie things up, but JD snags one last point by ricocheting the puck right behind Gwen’s striker."

            ma "Damn it."

            jd "Sorry, sheriff. That’s game."

            ma "It sure is."

            "She offers a handshake of commiseration, and JD accepts with a firm squeeze."

            ra "You want to go another round one on one, Gwen? I'll give you a few pointers."

            gwe "Thanks. That'd be great."

            "Mackenzie comes back over to where I'm sitting, settling down next to me."

            "Frustration is written in the line of her shoulders, and I wish I could relieve it."

            mcmac "You want to head back to your place?"

            ma "Yeah. Once it's polite."

            "(I'll be counting down the minutes.)"
    scene bg mackenzie_bedroom_lights at bg
    show mac tank basic at centre
    "Mackenzie is quiet the whole way back to her place."

    "It's not an uncomfortable silence, but there's something deeper under it, tension spreading under the surface."

    "The moment she closes the door to her room, I can feel it about to boil over."
    show mac tank basic at left4
    show hiflmc casual surprised at right4
    mcmac "Mac, are you ok-!"
    show mac tank surprised
    ma "I wanted to say—!"
    show mac tank sad
    ma "Sorry."
    show hiflmc casual sad
    mcmac "No, I'm sorry. What's going on?"
    show hiflmc casual basic
    show mac tank blush
    "She shifts from foot to foot, looking serious before a blush spreads across her face."
    show hiflmc casual surprised
    ma "I want you to be my girlfriend."
    show mac tank basic
    show hiflmc casual basic
    mcmac "Mac, I..."

    "Mackenzie holds up her hand for a pause, and I stop there."

    ma "I've never dated anyone who knew what I was."

    ma "The fact is, any werewolf we meet is going to register two things first. That I'm an alpha, and that we have a bond."
    show mac tank sad
    ma "They'll say 'partner', no matter what you and I call each other. But between us, I want..."
    show mac tank blush
    ma "Will you go out with me? Can we do what everyone else does?"
    show hiflmc casual happy
    "That silence fills the room again, but so does a giddy feeling like a hundred fireworks going off in my chest at once."
    show mac tank sad
    "Concern spills into Mackenzie's eyes, and I speak up before it eclipses her gaze completely."
    show mac tank surprised
    mcmac "Yes! Mac, of course, yes."
    show hiflmc casual blush
    mcmac "Let's go out. I mean, okay, tonight I'd rather stay in, but as your girlfriend."
    show hiflmc casual happy
    mcmac "As your girlfriend, I want to stay in tonight."
    show mac tank happy
    ma "Yeah?"

    mcmac "Oh, yeah."
    show mac tank happy at left2 behind hiflmc
    show hiflmc casual happy at right2
    "I rush to close the distance between us with a kiss, throwing my arms up around Mackenzie's shoulders."

    "Her body presses against mine, all muscle and tightly coiled heat."
    hide hiflmc
    hide mac
    show mac tank_cu smirk_cu at mac_cu
    ma "Do you know what else I want?"
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    mcmac "I'm listening."
    hide hiflmc
    show mac tank_cu smirk_cu at mac_cu
    ma "You. In my bed."
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "I don't even have to think about it."

    mcmac "Then what are you waiting for?"
    hide hiflmc
    show mac tank happy at left2 behind hiflmc
    show hiflmc casual happy at right2
    "One kiss melts into the next as Mackenzie walks me backwards, chasing my mouth each time we break apart for breath."

    "Once the back of my legs hit the mattress, her fingers find the hem of my shirt and slip right underneath it."

    mcmac "You want that off?"
    show mac tank smirk
    ma "Yeah, I do."

    mcmac "Then take it."
    show hiflmc naked happy
    "She does, pulling my vest off and tugging the shirt right up over my head."
    show hiflmc naked noglassesblush
    "My glasses are left askew, but Mackenzie captures those next, trading custody of them for a kiss."

    ma "Where do you want these?"
    show hiflmc naked noglasseshappy
    mcmac "Anywhere they won't break."

    "That ends up being her bedside table, and I take the chance to get rid of my jeans before Mackenzie comes back to me."

    "When I reach for her tank top, though, she brushes my hands away."
    show  mac tank smirk
    ma "No, I think I want you to watch that part."
    show hiflmc naked noglassesblush
    "A growl rasps the end of that last syllable, and I shiver."

    "Mackenzie pushes me down against the bed and I kiss her again, only to protest when she pulls back from me."
    hide hiflmc
    show mac naked smirk at centre
    "Any argument I have vanishes in thin air as Mackenzie starts to strip away her tank top, slow enough for me to appreciate every bared inch."

    "The path of her hands back down dares me to follow them to the button of her pants, and the zipper as it's undone."
    hide mac
    show hiflmc naked noglassesblush at centre
    mcmac "God."
    hide hiflmc
    show mac naked smirk at centre
    ma "I'm not even naked yet."
    hide mac
    show hiflmc naked noglassesblush at centre
    mcmac "I'm not sure if I'm going to survive you getting that far."
    hide hiflmc
    show mac naked smirk at centre
    ma "You better."
    scene mac6 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 8 yanchor 0.1
    "Mackenzie grins, bringing both arms up as the tight uniform pants fall down past her thighs."
    "It's like she's sculpted out of bronze, but it's her eyes I can't look away from, green as spring, or the forest I've seen her run through."
    mcmac "You are so beautiful."
    "The raw confidence in Mackenzie's pose doesn't fade, but when her body relaxes, there's a shift in intent."
    scene bg mackenzie_bedroom_lights at bg
    show mac naked_cu smirk_cu at mac_cu
    "When the bed gives beneath her weight, she moves over me on all fours, and claims a kiss that steals a moan from my throat."
    show mac naked_cu basic_cu
    ma "If this is ever too much…"
    hide mac
    show hiflmc naked_cu noglasseshappy_cu at hiflmc_cu
    mcmac "Mac, I want all of you."

    mcmac "No qualifiers, no holding back. I know exactly who you are."
    hide hiflmc
    show mac naked_cu smirk_cu at mac_cu
    "Her next breath is a whisper of my name, and Mackenzie kisses down my jaw to the line of my throat."

    "The warmth of her mouth becomes the graze of teeth, and every touch that wanders down my skin brings a rush of pleasure with it."
    hide mac
    $menuhideborder = True
    menu macs2e6c3:
        "A. Ask for more.":
            $menuhideborder = False

        "B. Tease Mac a little.":
            $menuhideborder = False
            show hiflmc naked_cu noglasseshappy_cu at hiflmc_cu
            mcmac "Be careful with those teeth. You might leave a mark."
            hide hiflmc
            show mac naked_cu smirk_cu at mac_cu
            ma "I was considering it."
            hide mac
            show hiflmc naked_cu noglassesblush_cu at hiflmc_cu
            "(Oh.)"
            hide hiflmc
        "C. Let her keep going.":
            $menuhideborder = False

            "(If she stops, I'm gonna lose my mind.)"

            mcmac "Mackenzie…"

            "That and a moan is enough encouragement to send her lower, and lower still."
    show mac naked_cu smirk_cu at mac_cu
    "One firm tug takes away the barrier between Mackenzie's hands and where I need her the most."

    "Grasping at her shoulders gives me an anchor when my hips jerk upward off the bed."
    hide mac
    show hiflmc naked_cu noglassesblush_cu at hiflmc_cu
    mcmac "Mac, please…"
    hide hiflmc
    show mac naked_cu smirk_cu at mac_cu
    ma "We're just getting started."

    ma "I can last all night. And I bet you can too."
    hide mac
    show hiflmc naked_cu noglasseshappy_cu at hiflmc_cu
    "That's a bet I'm desperate to prove, but right now there's nothing I can focus on but this moment."
    hide hiflmc
    show mac naked_cu happy_cu at mac_cu
    "How good Mackenzie feels to touch, how she moves with me like we've done this a hundred times before."
    hide mac
    "I don't know if it's because of our bond, or instinct, or something else. But the reason doesn't matter."

    "What matters is that we're together."
    scene bg mackenzie_bedroom_night at bg
    show hiflmc naked noglassesbasic at centre
    "A loud creak stirs me from sleep, and I sit up before rubbing my jaw."
    show mac naked sleep at left3
    show hiflmc naked noglassesblush at right3
    "Blushing at the cause, I expect to see Mackenzie getting up for water or something, but she's passed out beside me."
    hide mac
    hide hiflmc
    show hiflmc naked_cu basic_cu at hiflmc_cu
    "(What was that sound, then?)"
    show mac naked sleep at left3
    show hiflmc naked noglassessurprised at right3
    "There's another creak, closer this time, and my heart jumps up into my throat."
    hide mac with dissolve
    hide hiflmc with dissolve
    "A shadow in the far corner moves, taking solid shape and lunging towards the bed."

    "Sharp, knife-like claws cut through the darkness, but they're not slashing at me."
    show mac naked sleep at centre
    "They're aiming right at Mackenzie, ready to tear into her throat."
    hide mac
    show hiflmc naked_cu noglassessurpised_cu at hiflmc_cu
    mcmac "Mac, wake up!"

    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
