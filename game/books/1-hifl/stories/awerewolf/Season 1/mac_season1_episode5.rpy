##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mycharacter2 = Character("books.names[macfn2]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode5:
    $tbc = False

    ##Change these to suit the story
    scene bg heroine_home_day at bg
    play music hifleveryday

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show hiflmc pajamas noglassessad at centre

    "When I wake up on the couch, my head is full of hazy dreams."

    "Each one slips away from me as I try to remember the details."
    show hiflmc pajamas noglassessurprised at centre
    "But for a moment I feel Mackenzie’s presence in the room, and that snaps me into sitting up."

    show hiflmc vestlesscasual_cu noglassessarcastic_cu at hiflmc_cu
    "(Of course she’s not here. What was I thinking?)"
    show hiflmc pajamas noglassessarcastic at centre
    mcmac "I really need to stop falling asleep out here."
    show hiflmc pajamas noglassesblush at centre
    mcmac "Not that I'd mind waking up next to—"
    show hiflmc vestlesscasual_cu noglassesblush_cu at hiflmc_cu
    "(Okay, it’s too early to be THAT thirsty. Go get some breakfast, self.)"
    show hiflmc pajamas noglassesbasic at centre
    "Toast and eggs isn’t anything spectacular, but with another cup of coffee I’m human again."

    "It’s early enough that I can make my shift at the bowling early with time to spare."
    show hiflmc pajamas noglassessad at centre
    "Razi would probably let me duck out, but I still have bills to pay."
    show hiflmc pajamas noglassessarcastic at centre
    mcmac "I left that damn work shirt somewhere..."

    scene bg bowling at bg with fade
    pause
    show jd casual shadessmirk at centre
    "The music’s already on by the time I slip through the front door,"
    "but there’s no one there except for JD, who is rolling gutter balls to amuse themself."
    hide jd
    show razi casual basic at centre
    "Razi appears a moment later, a pair of freshly polished shoes in his hands."
    show razi casual happy at left4
    show hiflmc bowling basic at right4
    ra "Hey, [genericfn]."

    ra "Wasn't sure if I was going to see you today."
    show hiflmc bowling happy

    mcmac "And miss all this action? Who do you take me for?"

    "He smiles, warm and bold, but then his expression turns a little more serious."
    show razi casual sad
    show hiflmc bowling surprised
    ra "Really, though. Are you holding up okay?"

    ra "Between Grace and getting a little window into our other world, I can only imagine how you feel right now."

    "I am exhausted, but it still surprises me to hear Razi being so open."

    "It's hard not to look him up and down, to see some signs that I've missed in all the years I've known him."
    hide razi
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(There's nothing. He's just good ol' Razi.)"
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(Razi... who also happens to be a djinn.)"
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(I probably should have looked up more on that last night.)"
    show razi casual sad at left4
    show hiflmc bowling sad at right4
    mcmac "It's stressful, but Mackenzie's doing everything she can to help me find Grace."

    mcmac "I know it's just a matter of time."
    show razi casual basic
    show hiflmc bowling happy
    mcmac "As for the rest, um—!"

    menu mace5c1:
        "1. I think it's awesome.":
            show hiflmc bowling blush
            mcmac "Honestly, it's kind of awesome."
            show hiflmc bowling happy
            mcmac "This little town's a lot more interesting than I thought it was."
            show razi casual smirk
            ra "That's one way to put it."
            show razi casual basic
            ra "Unfortunately, we can't afford to be too flashy."

        "2. Nothing's sunk in yet.":
            "MISSING CHOICE"

        "3. It's pretty weird.":
            show hiflmc bowling sarcastic
            mcmac "It's pretty weird, not going to lie."
            show razi casual happy
            ra "If it makes you feel better, I felt the same way when I found out about everyone else."
    hide razi
    hide hiflmc
    show jd casual shadessmirk at centre
    jd "There's a reason why 'may you live in interesting times' is a curse."
    show jd casual shadessmirk at left4
    show hiflmc bowling basic at right4
    "I turn around to see JD leaning against the bar counter, a faint smile on their lips."
    show jd casual shadessad
    jd "I've been keeping an eye out for your sister, by the way. But no luck yet."
    show hiflmc bowling happy
    mcmac "Thanks, JD."

    jd "It's the least I can do, although tracking by scent is a little difficult these days."
    show hiflmc bowling surprised
    mcmac "Why?"
    show jd casual shadesangry
    jd "Because everything smells like territorial werewolf."
    show jd casual shadessmirk
    jd "Including you, by the way."
    hide jd
    show hiflmc bowling blush at centre
    "I blush at the implication, wondering if it's from Mackenzie touching me the night before."
    show hiflmc bowling surprised
    "But I realise they probably don't know about Damien yet."
    show hiflmc bowling basic at right4
    show jd casual shadessurprised at left4
    mcmac "That's because Mackenzie and I ran into the other werewolf last night."

    mcmac "The two of them got into a fight."
    hide jd
    show razi casual angry at left4
    "Razi raises an eyebrow, mouth tightening in concern."

    ra "Over what?"
    show hiflmc bowling sarcastic
    mcmac "This town, I guess. He said he wants to take it over for his pack."
    hide razi
    show jd casual shadesangry at left4
    show hiflmc bowling basic
    jd "That wolf's got stones of steel if he thinks that's going to happen."
    hide jd
    show razi casual angry at left4
    ra "No kidding."

    ra "The Hunt family has had claim to this area since the town was founded."

    ra "The disrespect of even trying."
    show hiflmc bowling sad
    mcmac "It's bad news?"
    show razi casual basic
    ra "He's either foolish or has a nasty trick up his sleeve."
    ra "I hope Mac's on her guard."
    hide razi
    show hiflmc bowling surprised at centre
    "Then I spy a car moving past the front door."

    "It's the sheriff's vehicle with Mackenzie in the driver seat, hands tense around the steering wheel."
    show hiflmc bowling basic at right4
    show razi casual basic at left4
    mcmac "Me too."

    mcmac "And I'll... be right back."
    scene bg main_day at bg with fade
    pause

    stop music fadeout 1.0
    play music hiflgetitdone

    show hiflmc bowling basic at centre

    "Razi lets me leave without comment, but the moment I step out of the bowling alley..."
    show hiflmc bowling basic at right4
    show mac glassescop basic at left4
    "Mackenzie sees me and leans over to the passenger side door like she's going to lock it."
    hide mac
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(Hey!)"
    show hiflmc bowling angry at right4
    show mac glassescop sad at left4
    "I put my hands on the roof of the car outside, staring into the driver's side window with a frown until Mackenzie sighs and rolls it down."

    mcmac "What's going on?"

    ma "Police business."
    show hiflmc bowling sarcastic
    mcmac "Police business in this town is someone knocking over a cow."

    mcmac "It doesn't make you look like you're about to go on the warpath."
    show mac glassescop smirk
    ma "You'd be surprised  who I arrest some nights, [genericfn]."
    show mac glassescop angry
    ma "The point is, what's going on is dangerous, and thus doesn't involve you right now."
    hide mac
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(There's only one source of danger here right now.)"
    show hiflmc bowling surprised at right4
    show mac glassescop angry at left4
    mcmac "You found Damien."

    ma "..."
    show hiflmc bowling sad
    mcmac "Mac-! Sheriff, come on."

    mcmac "You can't patch a girl up in her own house and give me the cold shoulder the next day."
    show mac glassescop basic
    ma "It's just a suspicious report."
    show hiflmc bowling sarcastic
    mcmac "One you're about to check up on."

    ma "Yes."
    show hiflmc bowling angry
    mcmac "Then I'm coming with you."
    show mac glassescop angry
    ma "No. Out of the question."
    hide hiflmc
    show mac glassescop_cu angry_cu at mac_cu
    "I open my mouth to protest, but Mackenzie levels me with a hard stare."

    "The steel in her eyes freezes me in place until I'm force to look away."
    hide mac
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I know what her job is. I know she doesn't want me getting hurt.)"
    show hiflmc bowling_cu sarcastic_cu
    "(But god, there's nothing I hate more than feeling helpless.)"
    show hiflmc bowling sad at right4
    show mac glassescop angry at left4
    mcmac "I can't just stand here and wait until Grace comes home."

    mcmac "I showed up at work because I was supposed to, but she was the first thing I talked about."

    mcmac "She's going to be until I know she's safe. So please, if you could just-!"
    show hiflmc bowling surprised
    show mac glassescop sad
    "Mackenzie shakes her head before tapping the button to unlock the doors again."

    ma "Get in. Put your belt on."
    show hiflmc bowling happy
    mcmac "Thank you! Thank you so..."
    show mac glassescop angry
    ma "Inside. Now."
    hide hiflmc
    hide mac
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg
    show hiflmc bowling surprised at left4 behind police_front_day:
        zoom 1.05
    show mac glassescop angry at right4 behind police_front_day:
        zoom 1.05
    "I shuffle to get into the passenger side before she decides to drive off without me."

    "The second my seatbelt is on, she revs the engine and starts zipping down Main Street."

    ma "I don't like this at all."

    mcmac "If it's so dangerous, why were you going without backup."

    ma "I turn into my backup, [genericfn]."

    ma "The deputies don't know what I am."
    show hiflmc bowling angry
    mcmac "But there's Razi and JD."
    show hiflmc bowling sarcastic
    mcmac "I don't know if Diego has some 'do no harm' thing going on, but he IS a vampire."
    show hiflmc bowling basic
    show mac glassescop sad
    ma "If this was just to find Grace, I'd think about it."

    ma "But it's not that simple."

    ma "If I don't defend this land on a werewolf's terms, Damien won't be the last one to try and take it out."
    $menuhideborder = True
    hide mac
    hide hiflmc
    menu mace5c2:
        "1. Have you told your family?":
            show mac glassescop sad at right4 behind police_front_day:
                zoom 1.05
            show hiflmc bowling sad at left4 behind police_front_day:
                zoom 1.05
            mcmac "Have you told your family's what's going on?"

            ma "My mother knows there's another wolf in town, but besides that, no."

            ma "I don't need them worried, and I really don't want them trying to make decisions for me."
        "2. Is there anything I can do?":
            show mac glassescop sad at right4 behind police_front_day:
                zoom 1.05
            show hiflmc bowling sad at left4 behind police_front_day:
                zoom 1.05
            mcmac "Is there anyhthing I can do to help?"
            mcmac "I'm just a human in the equation, right?"

            ma "Right now, the best thing you can do is not disappear on me."
            ma "Damien threatened you, and I'm not forgetting that any time soon."
        "3. That's a lot of responsibility.":
            show mac glassescop sad at right4 behind police_front_day:
                zoom 1.05
            show hiflmc bowling sad at left4 behind police_front_day:
                zoom 1.05
            mcmac "That's a lot of responsibility."
            show mac glassescop basic
            ma "It comes with the blood. I've never really had a choice in the matter."
            show mac glassescop angry
            ma "But if Damien thinks he's taking a single inch of this territory, he'll get what's coming to him."

    show mac glassescop angry
    show hiflmc bowling sad
    "Frustration brew in Mackenzie's expressionm before she falls quiet, eyes locked on the road and away from me."

    "I wish I could reach over and take her hand, offer any kind of comfort, but the last thing she needs is that kind of distraction."

    mcmac "Are you okay?"

    mcmac "The answer doesn't have to be yes."
    show hiflmc bowling happy
    mcmac "I'm really asking, not doing that thing where someone brings it up to make themselves feel better."
    show mac glassescop smirk
    ma "Heh."

    ma "I'll be fine, [genericfn]."
    show mac glassescop basic
    ma "When I've done my job, then everything will be okay."
    show mac glassescop happy
    ma "So try not to make it more difficult, alright?"
    show hiflmc bowling blush
    "She's smiling a bit when she speaks, and I hope the heat tapering on my face doesn't show very much."

    mcmac "You got it, Sheriff."

    scene bg lake_day at bg
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg
    pause

    show mac glassescop angry at right4 behind police_front_day:
        zoom 1.05
    show hiflmc bowling basic at left4 behind police_front_day:
        zoom 1.05

    "We do two or three full loops around the lake before Mackenzie's mood starts to trun grim."
    hide police_back_day
    hide police_grate_day
    hide police_front_day
    hide hiflmc
    hide mac
    show mac glassescop angry at centre
    "She parks the car under a tree and gets out, sniffing the air and bending down to check for any track that aren't her own."
    hide mac
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg
    show hiflmc bowling sad at left4 behind police_front_day:
        zoom 1.05

    mcmac "Anything?"
    hide police_back_day
    hide police_grate_day
    hide police_front_day
    hide hiflmc
    show mac glassescop basic at centre
    ma "Damien's scent is still old, so I don't think he's been here again."
    show mac glassescop sad
    ma "And the only sign of your sister was that phone."
    hide mac
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg
    show hiflmc bowling sad at left4 behind police_front_day:
        zoom 1.05
    mcmac "That's not good."
    show hiflmc bowling basic
    mcmac "What exactly did the report say?"
    hide police_back_day
    hide police_grate_day
    hide police_front_day
    hide hiflmc
    show mac glassescop basic at centre
    ma "A fisherman saw someone skulking around the trees."

    ma "He said he didn't recognize them at all."

    ma "Definitely a stranger, and when he tried to get their attention, they bolted."
    hide mac
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg
    show hiflmc bowling sarcastic at left4 behind police_front_day:
        zoom 1.05
    mcmac "Our town's suddenly a real popular place."
    hide police_back_day
    hide police_front_day
    hide police_grate_day
    hide hiflmc
    show mac glassescop smirk at centre
    ma "That would be lovely if I ran the tourism division."
    hide mac
    show hiflmc bowling basic at centre
    "I unbuckle my belt and get out of the car too, trying to see if anything out of the ordinary stands out."

    "Except for the worn-down house in the distance, the lake looks placid and isolated, like no one's here but us."
    show hiflmc bowling surprised
    "Then a thought hits me."
    show hiflmc bowling surprised at left4
    show mac glassescop basic at right4
    mcmac "There's nothing in the water, right?"

    ma "There's fish."
    show hiflmc bowling basic
    mcmac "No, I mean like the Loch Ness monster or something."
    show mac glassescop surprised
    ma "Oh."
    show mac glassescop basic
    ma "Well, the Lady of the Lak used to live here, but she got run out by mermaids."

    "Mackenzie's expression is so neutral, I can't tell whether or not she's kidding."
    $menuhideborder = True
    menu mace5c3:
        "1. Want to introduce me?":
            show hiflmc bowling happy at left4
            show mac glassescop basic at right4
            mcmac "You want to go ahead and introduce me? I bet they're cute."
            show mac glassescop smirk
            ma "You'd like that, wouldn't you?"

        "2. Yeah, right.":
            show hiflmc bowling sarcastic at left4
            mcmac "Yeah, right. Just because there's devils and djinn doesn't mean there's-!"
            show hiflmc bowling sad
            "(Okay, suddenly I'm not so sure.)"

        "3. Mermaids?!":
            show hiflmc bowling surprised at left4
            show mac glassescop basic at right4
            mcmac "We have mermaids? This is a land-locked state!"

            ma "Coastal property is terribly expensive, you know."

    show mac glassescop happy
    show hiflmc bowling happy
    "When she starts to smile, I know I've been had, but Mackenzie's full-bodied laugh makes it all worth it."

    mcmac "Thanks, Sheriff Jerk."
    show mac glassescop smirk
    ma "Just trying to lighten the mood a little bit."
    stop music fadeout 1.0
    play music hiflaction
    show mac glassescop surprised
    show hiflmc bowling surprised
    "I want to tease her to prove it worked, but something snaps behind us and we both go quiet."

    "Mackenzie whirls around just in time for a clawed hand to swipe through the air, and I let out a scream."
    show hiflmc bowling surprised at left6
    show mac glassescop angry at right1
    show annabelle wolfcasual wolfangry at right6

    "A set of golden eyes meet mind before Mackenzie shoulder-checks the new werewolf, sending her sprawling."
    hide mac
    show hiflmc bowling surprised at left4
    show annabelle wolfcasual wolfangry at right4
    "She rolls back to her feet and shoves Mackenzie hard, then makes a beeline straight for me."
    hide hiflmc
    hide annabelle
    show mac glassescop angry at centre
    ma "[genericfn], run! Get away from her!"
    hide mac
    show hiflmc bowling surprised at left4
    show annabelle wolfcasual wolfbasic at right4
    $sidecharone = "Werewolf"
    sid1 "Sorry, girl. Damien asked for you in particular."
    show hiflmc bowling angry
    mcmac "Damien can go fuck himself."
    show annabelle wolfcasual wolfbasic at left2
    show hiflmc bowling surprised at left5 behind annabelle
    "Unfortunately, this werewolf is even faster than we was, and my sprint is cut shot by her pinning me right to the ground."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu:
        xpos 0.35
    show annabelle wolfcasual_cu wolfangry_cu at annabelle_cu behind hiflmc:
        xpos 0.75
    "I feel sharp teeth right above the nap of my neck and tremble, remembering Mackenzie's warning about their bite."

    sid1 "You're out of your league, human."

    sid1 "Now stay still before I-!"
    show annabelle wolfcasual_cu wolfsurprised_cu
    "Her threat turns into a yelp of shock, and suddenly the werewolf's weight is off me."
    show hiflmc bowling surprised at left4
    show annabelle wolfcasual wolfsurprised at right2:
        ypos 0.995

    show mac earscop wolfgrowl at right6 behind annabelle
    "When I roll over on my back, arms held up to protect myself, Mackenzie is holding her with both arms right over her head."
    hide mac
    hide annabelle
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Woah.)"
    show hiflmc bowling surprised at left4
    show annabelle wolfcasual wolfsurprised at right2:
        ypos 0.995
    show mac earscop wolfsmirk at right6 behind annabelle
    ma "I hope Damien taught you how to swim."
    show mac earscop wolfbasic
    "With a burst of strength, Mackenzie tosses the other werewolf right into the lake."
    hide mac
    hide hiflmc
    show annabelle wolfcasual wolfsurprised at centre
    "She hits the water flat on her stomach, and I hear a choked gasp of pain before she starts trying to find purchase in the water."

    scene mac2 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 3.5 yanchor 0.1
    pause

    "Mackenzie's hand locked around my wrist before she pulls me right to my feet and up into her arms."

    "I feel weightless for a moment, startled that she can carry me without even a hint of strain."

    "Startled, and a little distracted."

    "(I  guess I'm nothing compared to an angry werewolf.)"

    mcmac "Where are we going?"

    ma "I'm putting you in the car. We're leaving right now."

    mcmac "Don't you want to ask her questions? She could be a witness."

    ma "Doesn't matter."

    ma "There's at least six other wolves here."

    mcmac "What?"
    show mac2 at bg:
        yanchor 0.1
        linear 3.5 yanchor 0.6
    "A rumbling growl from the treeline catches my ear, and when I dare to look back over Mackenzie's shoulder,"

    "Several sets of gold lupine eyes stare back from the shadows there."
    hide mac2
    scene bg lake_day at bg
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg
    show hiflmc bowling surprised at left4 behind police_front_day:
        zoom 1.05
    show mac earscop wolfbasic at right4 behind police_front_day:
        zoom 1.05
    "When she sets me down I throw myself into the passenger seat, mashing the button to lock the door when Mackenzie starts the engine."
    show bg road_day at bg
    "She slams on the gas, sending us right onto the mud-splatter road, and takes a sharp turn back towards town."
    show hiflmc bowling sad
    mcmac "Are they going to come after us?"

    ma "I don't know. Just hold on."
    hide mac
    hide hiflmc
    hide police_back_day
    hide police_grate_day
    hide police_front_day

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
