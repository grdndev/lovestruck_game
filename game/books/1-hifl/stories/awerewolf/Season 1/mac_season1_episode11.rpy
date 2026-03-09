##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode11:
    $tbc = False

    ##Change these to suit the story
    scene bg main_day at bg
    play music hifleveryday

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show police_back_day at bg
    show police_grate_day at bg
    show hiflmc beaniebowling basic at left3:
        zoom 1.05
    show mac tank smirk  at right3:
        zoom 1.05
    show police_front_day at bg
    "It’s a work day, though I don’t usually get a sheriff’s escort to the bowling alley."
    show hiflmc beaniebowling happy
    "Mackenzie told me she wanted to fill everyone in about what happened with Damien, but I’m not complaining about the company."
    show hiflmc beaniebowling blush
    "(Having breakfast together was nice too, even if I had to tell myself not to put too much thought into it.)"

    "(We’re not really dating, we just kiss sometimes.)"

    "(And I dream about having a shower that would actually fit two people.)"
    show hiflmc beaniebowling basic
    ma "Ready to head inside?"
    show hiflmc beaniebowling sarcastic
    mcmac "Don’t I look like the picture of excitement?"
    show mac tank happy
    ma "Come on, it won’t be so bad."

    ma "At least you work with friends."
    show hiflmc beaniebowling happy
    mcmac "That's true."
    scene bg bowling_regular at bg
    pause
    show diego casual basic at centre
    show razi casual smirk at left4
    show jd tank basic at right4
    "Razi, Diego, and JD are already settled around a table when we come through the front door."

    "But it’s a surprise to see an empty bottle lying down in the center of it."
    hide razi
    hide jd
    hide diego
    show hiflmc beaniebowling happy at centre
    mcmac "Did you three have a sleepover with Spin the Bottle and not tell me?"
    show hiflmc beaniebowling happy at left4
    show jd tank angry at right4
    "JD rolls their eyes."

    jd "Diego insisted the maker’s mark inside this bottle is Spanish."

    jd "I’m telling him it’s not."
    hide hiflmc
    show diego casual basic at left4
    di "It’s a bastardization of an old noble crest."

    di "Half the symbols in this country once had an entirely different meaning."
    hide diego
    hide jd
    show hiflmc beaniebowling happy at right4
    show razi casual basic at left4
    ra "I’m just glad they paid me for the liquor before dumping it out in the sink to argue over this."
    hide hiflmc
    show jd tank angry at right4
    jd "You said I couldn’t drink on the job!"
    hide jd
    hide razi
    stop music fadeout 1.0
    play music hiflsad
    show mac glassestank basic at centre
    "I laugh, shaking my head, but the mood turns serious when Mackenzie takes a step forward and puts her hands on the table."

    ma "Damien has officially challenged me for the town."

    ma "He said three days, but that was yesterday."
    show mac glassestank basic at left4
    show hiflmc beaniebowling basic at right4

    mcmac "So we’re down to two."
    hide hiflmc
    show razi casual basic at right4
    ra "What does that challenge mean? Is he going to stop ambushing half the town?"
    hide mac
    show diego casual angry at left4
    di "It means a fight to the death, Razi."
    show razi casual smirk
    ra "Well, I wasn’t expecting a game of tic-tac-toe."
    hide razi
    hide diego
    show mac glassestank basic at left4
    show jd tank basic at right4
    jd "Do you actually have to kill him? Not that I’d complain."
    show mac glassestank sleep
    ma "No, but someone has to surrender."
    show mac glassestank sad
    ma "Considering how violent Damien has been already, I don’t think this ends without bloodshed."
    hide jd
    show hiflmc beaniebowling sad at right4
    "Nerves briefly turn my stomach inside out."

    "I know Mackenzie is stronger than him but it’s a cruel trade-off."

    "Either she has to cross that fatal line or Damien will take her out instead."
    hide hiflmc
    show mac glassestank angry at centre
    ma "But that’s why I’m here. I don’t want the fight to stop with me."

    ma "If I lose, Havenfall still needs protectors."
    show mac glassestank basic
    ma "I’m asking everyone here to take on that responsibility."
    hide mac
    show hiflmc beaniebowling_cu surprised_cu at hiflmc_cu
    "(Does she really think she’s going to —?!)"
    stop music fadeout 1.0
    play music hifleveryday
    hide hiflmc
    show razi casual angry at right4
    show mac glassestank surprised at left4
    "Razi seems to share my thoughts, sitting up in his chair and shaking his head."

    ra "First off, you know how long my family has been here. We’re not leaving anytime soon."
    show razi casual smirk
    ra "But second, you won’t need us."
    show razi casual happy
    ra "You’ve got this, Mackenzie."
    hide razi
    show jd tank happy at right4
    jd "He’s right. I know a punk when I see one, Mac."

    jd "In a stand-up fight, Damien is going to crumple."
    show jd tank smirk
    jd "The guy can’t even topple a djinn ward around a bowling alley."
    hide jd
    show diego casual basic at right4
    di "They are both right, but regardless, you have our support."
    hide diego
    show mac glassestank surprised at centre
    "All the harness leaves Mackenzie’s eyes, replaced for a second by honest surprise."

    "Some part of her expected to go through all of this alone, and it’s so hard not to kiss her then and there, promising to never leave her."
    show mac glassestank basic
    ma "...Alright, then. I just feel better with a backup plan."
    show mac glassestank basic at left4
    show jd tank basic at right4
    jd "Fair enough."
    hide jd
    show razi casual basic at right4
    ra "What are you going to do until then?"
    show mac glassestank smirk
    ma "Keep myself in fighting shape."

    ma "Most of my slugfests are with the town , not other werewolves."
    hide razi
    show hiflmc beaniebowling happy at right4
    mcmac "You’ve done a pretty good job so far, babe."
    show hiflmc beaniebowling surprised
    "The affectionate name slips out of my mouth before I think better of it."
    hide mac
    show jd tank smirk at left4
    show hiflmc beaniebowling blush

    "JD makes a little heart sign under the table, making me blush."
    hide jd
    hide hiflmc
    show hiflmc beaniebowling_cu sarcastic_cu at hiflmc_cu
    "(Jerk!)"
    hide hiflmc
    show mac glassestank happy at left4
    show hiflmc beaniebowling basic at right4
    ma "Thanks, but this is the one that counts."

    ma "I think I’m going to work out some."

    ma "Want to join me, [genericfn]?"
    hide mac
    hide hiflmc
    $menuhideborder = True

    menu mace11c1:
        "A. Help Mac train." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mac glassestank happy at left4
            show hiflmc beaniebowling blush at right4
            "(And have the opportunity to watch her flex? Please and thank you.)"

            mcmac "Like work out with you or?"

            ma "Of course, if you want to."

            ma "But I'll need some help with a few exercises in here."
            hide hiflmc
            show razi casual smirk at right4
            ra "Don't destroy my bowling alley please."
            show mac glassestank smirk
            ma "I'll leave the shotput out for the summer, Razi. Promise."
            show razi casual happy
            "He laughs and leaves us be, escorting Diego back out into the daylight."
            hide mac
            hide razi
            show jd tank basic at centre
            "JD retreats to the back, making some excuses about inventory."
            hide jd
            show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
            "(They probably don't want to have to catch another flying bowling ball.)"
            hide hiflmc
            show hiflmc beaniebowling happy at right3
            show mac glassestank basic at left3
            mcmac "So how do I help?"
            show mac glassestank happy
            ma "Just counting for me at first, if you don't mind."
            hide hiflmc
            show mac glassestank basic at centre
            "Mackenzie looks up at the rack of lights we use for Cosmic Happy Hour, gauging them for a second before she jumps straight up."

            "Her fingers hook around the bar, and she rides right into a pull-up, head a few inches from the ceiling."
            show mac glassestank basic at left3
            show hiflmc beaniebowling blush at right3
            mcmac "O-One?"
            hide mac
            hide hiflmc
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(I've never gone to church, but catch me praying in a hot second.)"
            hide hiflmc
            show mac glassestank smirk at left3
            show hiflmc beaniebowling blush at right3
            ma "First one doesn't count."

            ma "I've got to drop all the way down."
            show hiflmc beaniebowling happy
            mcmac "Perfectionist."
            show mac glassestank happy
            ma "I like to think of it as being honest with myself."

            ma "If I don't know the limits of what I can accomplish, how do I do better?"
            stop music fadeout 1.0
            play music hiflliteromance
            show hiflmc beaniebowling blush
            "Any answer I'd have for that escapes my tongue when I see the muscle rippling up Mackenzie's back,"

            "The powerful breadth of her shoulder going taut at the top of the repetition."
            hide mac
            hide hiflmc
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(Counting! You're supposed to be counting.)"
            hide hiflmc
            show mac glassestank basic at centre
            "She does a solid fifty before dropping down to the floor, landing with just a whisper of impact."
            show mac glassestank smirk at left3
            show hiflmc beaniebowling blush at right3
            "Wiping the sweat from her brow, Mackenzie grins."

            ma "The lights up there are real warm."
            show hiflmc beaniebowling happy
            mcmac "Want some water to pour over your head? We could go full Flashdance."
            show mac glassestank smirk
            ma "Are you even old enough for that movie?"
            show hiflmc beaniebowling happy at centre
            "I give her shoulder a playful smack, but my knuckles ache a little for it."

            "This pumped up, Mackenzie feels like she's made of hot steel."

            mcmac "I appreciate the classics."
            show hiflmc beaniebowling happy at right3
            mcmac "What's next?"
            show mac glassestank happy
            ma "Crunches. Just come and hold my feet."
            show mac glassestank basic
            "That sounds easy enough, so I kneel down while Mackenzie gets on her back."

            "I get a firm grip around the top of her boots, but when she leans up into the first crunch, I realise this is a test of endurance."
            show hiflmc beaniebowling blush
            "Every time Mackenzie lays back down, her tank top rides up, revealing a swathe of bronze skin between the hem and her pants."

            "My hands grip tighter, and I bite my lip while enjoying the view, taken and given between every rep."

            ma "What am I up to?"

            mcmac "U-uh, fifteen."
            hide mac
            hide hiflmc
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(Give or take three. Or maybe five.)"
            hide hiflmc
            show mac glassestank basic at left3
            show hiflmc beaniebowling happy at right3
            mcmac "Havenfall should really invest in a gym, huh?"
            show mac glassestank smirk
            ma "It wouldn't do me much good."

            ma "Most equipment doesn't hold up to my stress test."

            mcmac "And lifting a car kind of attracts attention."

            ma "Not the good kind, either."
            show mac glassestank basic
            "I keep count to—roughly—a hundred and Mackenzie takes a brief break to stretch before turning over for push-ups."
            show mac glassestank surprised
            "She glances up at me, eyes curious."
            show mac glassestank happy
            ma "You mind sitting on me?"
            hide mac
            hide hiflmc
            show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
            "(No, I would mind...)"
            show hiflmc beaniebowling_cu blush_cu
            "(Wait, that can't be what she means.)"
            hide hiflmc
            show mac glassestank happy at left3
            show hiflmc beaniebowling blush at right3
            mcmac "Where, exactly?"
            show mac glassestank blush
            "The implication sets in a second later, and Mackenzie blushes, clearing her throat."

            ma "On my back."

            ma "I need the weight or it'll take forever to wear me out."

            mcmac "Oh! That makes…"

            mcmac "Yeah, no problem."
            hide mac
            hide hiflmc
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(If I'm sitting on her back, she can't see me turning red.)"
            hide hiflmc
            show mac glassestank basic at right1
            show hiflmc beaniebowling basic at right3 behind mac
            "The position is a little trickier than I expect, but I end up cross-legged in the center of Mackenzie's back and holding onto her shoulders for balance."
            show hiflmc beaniebowling surprised
            "When she starts doing push-ups, the rhythm is so quick and clean, it's like I'm not even there."

            mcmac "How do you do this at home?"

            ma "Weighted vest."
            show hiflmc beaniebowling happy
            mcmac "Huh. We've got to get you some superhero gravity chamber or something."
            show mac glassestank happy
            "She laughs, and I feel the sound through my whole body with my legs pressed against Mackenzie's back."
            show mac glassestank smirk
            "I sit in silent awe until she's finished, gently tapping my hand to get me to move."

            ma "You have anything I can wipe down with?"

            mcmac "There's some towels behind the bar."

            "Most of the rags are too small to be useful, but I find one big enough for Mackenzie to clean up."
            hide hiflmc
            hide mac
            show mac glassestank_cu smirk_cu at mac_cu
            "Her hand catches my wrist when I hand it over and I'm pulled into a scorching kiss."

            ma "Thanks for being my workout buddy."
            hide mac
            show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
            mcmac "You are so, so welcome."
            show hiflmc beaniebowling_cu blush_cu
            mcmac "Is this a weekly routine or—!"
            hide hiflmc
            show mac glassestank_cu smirk_cu at mac_cu
            ma "I could fit it into my schedule."
            hide mac
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(God is real and she looks after thirsty bisexual girls.)"
            hide hiflmc
            show mac glassestank_cu happy_cu at mac_cu
            ma "I know you have to work at least a little today, so I'm going to pick something up from the house."

            ma "I'll come over after your shift, okay?"
            hide mac
            show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
            mcmac "Don't keep me waiting."
            hide hiflmc
            show mac glassestank_cu smirk_cu at mac_cu
            ma "No chance of that."
            hide mac
            show hiflmc beaniebowling_cu happy_cu at hiflmc_cu
            "(Now I just need a crowd of customers to make this day go by in a blur.)"

        "B. Work your shift at the bowling alley.":
            $menuhideborder = True
            show hiflmc beaniebowling_cu sarcastic_cu at hiflmc_cu
            "(I may have run for my life several times this week, but I’m not sure I could keep up with her.)"
            hide hiflmc
            show hiflmc beaniebowling sad at left4
            show mac glassestank surprised at right4
            mcmac "I should probably work."

            mcmac "You’ve got to focus on the fight, right?"

            mcmac "I don’t want to be a distraction."
            hide mac
            hide hiflmc
            show razi casual smirk at centre
            "In the corner of my vision, I see Razi raise an eyebrow, but thankfully he doesn’t comment."
            hide razi
            show hiflmc beaniebowling sad at left4
            show mac glassestank happy at right4
            mcmac "If you say so. I’m going to head out for a run."
            hide hiflmc
            hide mac
            show mac glassestank_cu basic_cu at mac_cu
            "I want to say goodbye, but Mackenzie leans forward to whisper in my ear, the heat in her voice like a lick of fire under my skin."

            ma "Let me know if you change your mind, though."
            show mac glassestank_cu smirk_cu
            ma "Because you’re my kind of distraction."
            hide mac
            show hiflmc beaniebowling blush at left4
            show mac glassestank happy at right4
            "Mackenzie takes a step back, flashing a smile my way before she turns to leave."

            "A foot in front of the door, she glanced back at me one last time."

            ma "I’ll catch up with you after work, alright?"

            mcmac "Yeah."
            hide mac
            show jd tank happy at right4
            "I’m still thinking about the little twinkle in Mackenzie’s eyes each time she smiles before I hear JD chuckling behind me."
            show hiflmc beaniebowling sarcastic at left4
            mcmac "What’s so funny, JD?"
            show jd tank smirk
            jd "Bet you’ll be trying to jog a marathon by next week."

            mcmac "Oh my god, shut up!"
            hide jd
            hide hiflmc
            show hiflmc beaniebowling_cu blush_cu at hiflmc_cu
            "(I’d have to buy some running shorts first.)"


    scene bg heroine_home_lights at bg
    stop music fadeout 1.0
    play music hifleveryday
    pause
    show hiflmc vestlesscasual sarcastic at centre
    "Work is the same boring slog as always, but I pick up some food from the diner on the way home and settle in with a documentary."
    show hiflmc vestlesscasual surprised
    "This one is all about the historical uses of silver, and I have to stare when the narrator actually mentions werewolves."
    show hiflmc vestlesscasual happy
    mcmac "Of course that’s a myth, Buddy. Keep telling yourself that."
    show hiflmc vestlesscasual sarcastic
    mcmac "...I wish we had real silverware."

    mcmac "I’d stick Damien with it a couple times and see how he likes it."
    show hiflmc vestlesscasual surprised
    "A knock on the door interrupts my little vengeful fantasy, and I tossed my plate into the trash before checking to make sure it’s Mackenzie."
    hide hiflmc
    show bg mc_house_ext_moon at bg
    show mac glassescop sad at centre
    "She’s waiting on the step outside, body tense, so I open up right away to let her in."
    show bg heroine_home_lights at bg
    show mac glassescop basic at left4
    show hiflmc vestlesscasual happy at right4
    mcmac "Hey."

    ma "Hey. How was the grind?"
    show hiflmc vestlesscasual sarcastic
    mcmac "Same old empty lanes."

    mcmac "My only customers were two teenagers who wanted to make out by the arcade machines."
    show hiflmc vestlesscasual happy
    show mac glassescop smirk
    ma "Sounds like a party."
    hide hiflmc
    show mac glassescop sad at centre
    stop music fadeout 1.0
    play music hiflsad

    ma "Can we sit and talk for a little bit?"
    show mac glassescop sad at left2
    show hiflmc vestlesscasual basic at right2
    "Mackenzie looks far too serious for me to even jokingly say no, so I take a seat next to her on the couch."

    "She reaches into her pocket, pulling out a thick, crumpled envelope."

    mcmac "What’s that?"

    ma "Insurance."
    show hiflmc vestlesscasual surprised
    "The envelope is pushed into my hands, and past the top lip of paper, I see a tight roll of fifty dollar bills."

    "I nearly drop it."

    mcmac "Jesus. What am I supposed to do with all this?"

    ma "Leave. If anything happens to me, you leave."
    show hiflmc vestlesscasual sad
    mcmac "Damien’s not going to win."
    show mac glassescop angry
    ma "I’m not leaving that up to chance."
    ma "If he does, you’ll be his first target."
    ma "You could go anywhere you want."
    show mac glassescop sad
    ma "Just buy a ticket and go."
    hide mac
    show hiflmc vestlesscasual sad at centre
    "A month ago, if someone had handed me a stack of cash and told me to leave town..."

    "Well, I wouldn’t have even packed a bag."

    "Grace and I could start over somewhere new, away from Havenfall’s ghosts."
    hide hiflmc
    show hiflmc vestlesscasual_cu angry_cu at hiflmc_cu
    "(But this town is mine too.)"
    "(I’m not running when Mackenzie’s putting her life on the line to defend it.)"
    show hiflmc vestlesscasual_cu sad_cu at hiflmc_cu
    "(I won’t leave her.)"
    hide hiflmc
    show mac glassescop basic at left2
    show hiflmc vestlesscasual angry at right2
    mcmac "No. I don’t need this."
    show mac glassescop surprised
    ma "[genericfn]-!"

    mcmac "Look, I don’t know what you want to call whatever we’ve got going on right now, but it matters to me."
    show hiflmc vestlesscasual sad
    mcmac "I care about you, Mac. I don’t want an out."
    show mac glassescop angry
    "Mackenzie’s jaw tightens, frustration burning bright in her eyes."

    ma "Damien could kill you. Or worse."
    show hiflmc vestlesscasual basic
    mcmac "He’s not going to."
    hide mac
    hide hiflmc
    show mac glassescop_cu angry_cu at mac_cu
    "I drop the money back into Mackenzie’s lap, meeting her gaze dead on."
    hide mac
    show hiflmc vestlesscasual_cu basic_cu at hiflmc_cu
    mcmac "Save that for after."
    stop music fadeout 1.0
    play music hiflliteromance
    show hiflmc vestlesscasual_cu happy_cu
    mcmac "Because if you take me out on a date, I can tell you right now I’ll need new clothes."
    hide hiflmc
    show mac glassescop_cu surprised_cu at mac_cu
    ma "..."

    ma "You want to go out on a date?"
    hide mac
    show hiflmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    mcmac "Of course I do."
    show hiflmc vestlesscasual_cu happy_cu
    mcmac "If this is how you look in uniform, I’m pretty sure seeing you cleaned up would give me a heart attack."
    hide hiflmc
    show mac glassescop_cu smirk_cu at mac_cu
    ma "Hey, no heart attacks."

    "Mackenzie leans forward and cups my cheek, but the weight of her body pins me back against the cushions of the couch."

    "My breath catches, eyes flickering to her mouth in silent invitation."
    stop music fadeout 1.0
    play music hiflheavyromance
    hide mac
    "When she kisses me, it’s fierce and strong, leaving a mark on my lips like a brand."
    show mac glassescop_cu basic_cu at mac_cu
    ma "If you’re mine, I won’t see you hurt."
    hide mac
    $menuhideborder = True
    menu mace11c2:
        "A. I'm yours.":
            $menuhideborder = False
            show hiflmc vestlesscasual_cu happy_cu at hiflmc_cu
            mcmac "Then I'm yours."
            hide hiflmc
            show mac glassescop_cu smirk_cu at mac_cu
            "I swear for a split second Mackenzie’s eyes turn gold, but she shakes it off and kisses me again."
        "B. Trust me.":
            $menuhideborder = False
            "DIALOGUE MISSING"
        "C. Do that again.":
            $menuhideborder = False
            show hiflmc vestlesscasual_cu happy_cu at hiflmc_cu
            mcmac "Do that again."
            hide hiflmc
            show mac glassescop_cu smirk_cu at mac_cu
            "Mackenzie doesn't even hesitate, and there's a smile against my lips before I return the kiss, wanting her to feel the exact same way."

    hide mac
    hide hiflmc
    show hiflmc vestlesscasual_cu blush_cu at hiflmc_cu
    "(I need to get a better couch if she's going to keep coming over.)"
    show hiflmc vestlesscasual_cu happy_cu
    mcmac "Are you staying here?"
    hide hiflmc
    show mac glassescop_cu smirk_cu at mac_cu
    ma "Technically, I’m on patrol right now."
    hide mac
    show hiflmc vestlesscasual sad at right4
    show mac glassescop smirk at left4
    "She sits up enough for me to have some space—even if I don’t really want it —and tugs the wrinkles out of her uniform shirt."
    show mac glassescop happy
    ma "But I’ll keep an eye on the house, alright?"
    show hiflmc vestlesscasual happy
    mcmac "Okay."

    mcmac "Take your money with you, Sheriff."
    show mac glassescop smirk
    ma "Yes, ma’am."

    "Mackenzie does a little hat top with the words,"
    show hiflmc vestlesscasual happy at right1
    show mac glassescop smirk at left1 behind hiflmc

    "And it’s enough to make me laugh and pull her back for one last kiss before she has to leave."
    scene bg diner_lights_on at bg
    stop music fadeout 1.0
    play music hifleveryday
    "I get a call from Mackenzie to go to breakfast, and she picks me up for a quick ride over to the diner."
    show diego casual glassesbasic at centre
    "Diego is waiting in a booth by the corner, as far away from the windows as he can be."
    hide diego
    show mac cop basic at left4
    show hiflmc casual basic at right4
    mcmac "Why did he want to meet up?"

    ma "I’m not sure. I respect him too much to say no."
    hide mac
    hide hiflmc
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Glad to know that whole werewolf/vampire rivalry thing is only part of the movies.)"
    hide hiflmc
    show diego casual glassesbasic at left4
    show mac cop basic at centre
    show hiflmc casual basic at right4
    "Mackenzie snags the seat right across from him, and I sit down next to her, poring over the menu."
    hide mac
    hide hiflmc
    show diego casual glassesbasic at centre
    "Diego has a cup of black coffee right by his hand, but it looks untouched."
    hide diego
    show diego casual glassesbasic at left4
    show mac cop basic at centre
    show hiflmc casual basic at right4
    di "Punctual as always, Sheriff Hunt."
    show mac cop smirk
    ma "You’re a man who’s keenly aware of time, Diego."
    show diego casual glassessmirk
    di "By necessity as much as choice."
    show diego casual glasseshappy
    di "Please, order something first. Business can wait for hunger."
    hide mac
    hide diego
    hide hiflmc
    show luce casual basic at centre
    "I go for a stack of waffles, knowing Luce will use the real syrup, and Mackenzie orders a steak and eggs."

    "Luce doesn't even ask if we want coffee too, she just leaves two cups and a full pot."
    hide luce
    show mac cop happy at left4
    show hiflmc casual happy at right4

    ma "When is that woman getting the key to the city?"

    mcmac "Soon, I hope. She deserves it."
    hide mac
    hide hiflmc
    show diego casual glassesbasic at centre
    "It’s kind of awkward eating with Diego just watching, but he doesn’t seem bothered in the least, silently observing until our plates are clear."
    show diego casual glassesbasic at left4
    show mac cop basic at right4
    ma "So what’s this about?"

    di "A formality."

    di "While I respect your family’s stewardship of this land, it is my home as well, Mackenzie."
    show diego casual glassesangry
    di "And one I do not plan to see overrun by ruffian wolves that don’t know the meaning of diplomacy."

    ma "It won’t be."
    show diego casual glassesbasic
    di "I would like to make sure of that."

    di "With your permission, I could take care of this problem swiftly."

    di "Damien and his entire flock."
    show hiflmc casual sad at centre
    "I look between Mackenzie and Diego for a second, not quite understanding."
    hide hiflmc
    show mac cop angry
    "Mackenzie frowns deeply, holding her hands together before her voice drops to a whisper."

    ma "You'd kill all of them?"
    hide mac
    hide diego
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Holy shit, what?)"
    hide hiflmc
    show diego casual glassesbasic at left4
    show mac cop angry at right4
    di "It is the most efficient solution, but one I would not undertake without your consent."
    show mac cop basic
    ma "That’s very generous."
    hide mac
    hide diego
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(No, it’s not! It’s super scary and bloodthirsty!)"
    hide hiflmc
    show hiflmc casual sad at centre
    "Still, I take a deep breath to calm my nerves."
    hide hiflmc
    show mac cop basic at right4
    show diego casual glassesbasic at left4
    "Mackenzie’s tone is calm, but not the least bit excited or interested."

    ma "But if I can’t defend this land on my own, any claim I have is meaningless."
    show diego casual glassessad
    di "I am familiar with the politics of conquering."

    di "Yet it only felt polite to offer."
    show diego casual glasseshappy
    di "Havenfall would be a lesser place without you."
    show mac cop happy
    ma "Thank you, Diego. That means a lot."
    hide diego
    show mac cop smirk at left2
    show hiflmc casual blush at right2
    "Mackenzie gently nudges my shoulder, her authoritative mask slipping away. "

    ma "Let me out so I can pay."
    hide mac
    show hiflmc casual basic at right4
    show diego casual glassesbasic at left4
    "I scoot out of the way so Mackenzie can head to the register, leaving me alone with Diego."
    hide diego
    hide hiflmc
    show diego casual_cu basic_cu at diego_cu
    "He leans forward, tipping his sunglasses down, clearly not wanting her to overhear."

    di "I had a feeling my suggestion would be unwelcome, but that does not change the reality of things."

    di "Look out for her, [genericfn]."
    show diego casual_cu sad_cu
    di "A man like Damien will happily give Mackenzie a dishonorable death if it means he will win."
    hide diego
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(That's exactly what I'm afraid of.)"
    hide hiflmc
    $menuhideborder = True

    menu mace11c3:
        "A. Of course I will":
            $menuhideborder = False
            show hiflmc casual_cu basic_cu at hiflmc_cu
            mcmac "Of course I will. I have her back a hundred percent."
            hide hiflmc
            show diego casual_cu smirk_cu at diego_cu
            di "As I thought. But I would be remiss in not voicing my concerns aloud."
            hide diego
            hide hiflmc
        "B. He won't survive it.":
            $menuhideborder = False
            show hiflmc casual_cu angry_cu at hiflmc_cu
            mcmac "He won’t survive it if he does."

            mcmac "Unless you're planning on backing down."
            hide hiflmc
            show diego casual_cu angry_cu at diego_cu
            di "Against an uncouth dog like him? No, never."
            hide diego
            show hiflmc
        "C. This is terrifying.":
            $menuhideborder = False
            show hiflmc casual_cu sad_cu at hiflmc_cu
            mcmac "This is terrifying. You know that, right?"
            hide hiflmc
            show diego casual_cu basic_cu at diego_cu
            di "Our world is just like yours."

            di "For every person like Mackenzie who wants to see the world better, someone else wishes it to burn."
            hide diego
            hide hiflmc
    show bg diner_lights_off at bg
    stop music fadeout 1.0
    play music mackenziehunt
    show diego casual glassesbasic at left4
    show hiflmc casual surprised at right4
    "He sits back up when Mackenzie turns around, but then a shadow is cast over Diego’s face."

    "I whirl around in confusion, only to see that every window has gone dark."
    hide diego
    hide hiflmc
    show luce casual basic at centre
    lu "The hell?"
    hide luce
    show mac cop surprised at centre
    "Mackenzie’s radio cracked with static before she taps it, the deputy’s voice straining across the connection."

    $sidecharone = "Deputy"
    sid1 "Sheriff! A whole bunch of people just drove up in the center of town!"

    sid1 "One of them’s got ears and teeth, but he looks like the guy that jumped me the other night and—!"
    show mac cop angry
    ma "Deputy, calm down."

    ma "Do not engage them, do you understand?"

    sid1 "Yeah, Sheriff, but things look bad out here."

    sid1 "Like a storm’s coming."

    ma "What do you mean?"

    sid1 "The sky’s gone black. You can’t even see the sun."
    hide mac
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(Well, that sounds... apocalyptic.)"
    hide hiflmc
    show mac cop basic at centre
    ma "Get the people around you to safety and hang back."

    ma "I’ve got this under control, alright?"

    sid1 "Alright, Sheriff. I trust you."
    show mac cop basic at left4
    show hiflmc casual basic at right4
    "The radio pops off and Mackenzie looks at me, cold determination filling her eyes."

    mcmac "I’m coming with you."

    ma "Then let’s go."
    show bg main_day_fog at bg
    show mac cop surprised at left4
    show hiflmc casual surprised at right4
    "We rush out the front of the diner and find utter chaos."
    hide hiflmc
    hide mac
    show diego casual surprised at centre
    "Diego stares up at the sky, then slowly removes his sunglasses."
    show diego casual surprised at left4
    show hiflmc casual surprised at right4
    mcmac "Doesn’t that hurt?"

    di "No, although it should."
    hide diego
    show mac cop surprised at left4
    ma "The moon is... it’s a goddamn solar eclipse!"
    hide mac
    hide hiflmc
    show damien wolf wolfbasic at centre
    show annabelle wolfcasual wolfbasic at left2 behind damien
    "The outburst surprised me, but not as much as seeing Damien appear with his pack behind him, all of them openly transformed."
    show damien wolf wolfsmirk
    "He cackles, and the other werewolves echo it, nearly falling over each other in their amusement."
    hide annabelle
    show damien wolf wolfsmirk at right4
    show mac cop angry at left4
    dam "Morning, Sheriff, haha!"

    dam "How’s that moonlight feel?"
    hide damien
    show mac cop surprised at centre
    stop music fadeout 1.0
    play music hiflsuspense
    ma "Nn."
    show mac cop angry
    "She staggers to one knee with a shout of pain, grabbing at both sides of her head."
    hide mac
    show mackenzie_s1_mini11 at bg
    "I watch in horror as Mackenzie's eyes flicker from green to gold and back, face twisted in agony."
    hide mackenzie_s1_mini11
    show hiflmc casual surprised at right4
    show mac cop angry at left4
    mcmac "Mackenzie!"
    hide hiflmc
    hide mac

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
