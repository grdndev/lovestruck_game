define unknown = Character("???",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define Sheriff = Character("Sheriff Hunt",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define mail = Character("Mail Carrier",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define doc = Character("Dr. Escalona",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])

label van_season1_episode3:

    $tbc = False
    scene bg heroine_home_lights at bg
    play music hiflsuspense
    pause

    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show hiflmc bowling surprised at right4
    show vanessa huntress basic at left4
    mcvan "Wait, let's walk this back a little."
    mcvan "Do you swear to protect every human you come across?"
    show vanessa huntress sad
    va "No. There's only so much I can do by myself."
    show vanessa huntress angry
    va "But when I know there's a threat, I get in the way of it."
    va "You have a target on your back a mile wide right now."
    va "I can't walk away."
    va "I won't."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    "(What are my options?)"
    show hiflmc bowling_cu sarcastic_cu
    "(Maybe I could call the police, but it's not like I can tell Sheriff Hunt there are vampires on the loose.)"
    show hiflmc bowling_cu sad_cu
    "(Even if she believed me, they'd just bite her instead.)"
    show hiflmc bowling basic at right4
    show vanessa huntress basic at left4
    mcvan "Okay. I accept."
    stop music fadeout 1.0
    play music vanessa
    show vanessa huntress smirk
    "Vanessa's smile is small, but pleased."
    va "Glad to hear it."
    va "I'll stake myself out on your porch."
    show hiflmc bowling surprised
    mcvan "Won't you be cold?"
    show vanessa huntress basic
    "She gestures to the leather covering her from head to toe."
    va "The cape's lined too. I don't get cold unless I'm knee-deep in snow."
    show hiflmc bowling basic
    mcvan "Let me, at least, make you some coffee."
    show hiflmc bowling happy
    mcvan "Black, right?"
    show vanessa huntress smirk
    va "Please."
    hide vanessa
    show bg heroine_kitchen_night_lights at bg with wiperight
    show hiflmc bowling basic at centre
    "Vanessa slips back out my door and I busy myself in the kitchen, deciding to make enough for two cups."
    show hiflmc bowling sad
    "I should sleep, but my whole body is so tense I don't think I'll be able to."
    hide hiflmc
    show bg mc_house_ext_night at bg with wipeleft
    show vanessa huntress basic at centre
    "Sure enough, Vanessa is sitting on my porch like it's a guard post, using the edge of her cloak to polish the barrel of her pistol."
    show hiflmc bowling happy at right4
    show vanessa huntress basic at left4
    mcvan "Caffeine delivery."
    show hiflmc bowling basic
    "After holstering her gun, she takes the cup from me with both hands."
    show vanessa huntress sad
    "When I sit down next to her, though, Vanessa frowns."
    va "You should be in bed. You need the rest."
    show hiflmc bowling sad
    mcvan "After what I saw tonight..."
    show hiflmc bowling sarcastic
    mcvan "Sleep's not on the menu."
    show hiflmc bowling basic
    va "Fair enough."
    va "But if you do get tired or cold, go back inside."
    show vanessa huntress basic
    va "I'm used to working alone."
    "She sips at her coffee between long stares across the neighborhood, searching through the shadows for anything out of the ordinary."
    show hiflmc bowling sad
    "The quiet doesn't seem to bother Vanessa, but I feel awkward staying so still and silent."
    mcvan "I have something to ask."
    va "Mm?"
    show hiflmc bowling surprised
    mcvan "Are you {i}that{/i} Van Helsing? Because that story is from centuries ago."
    show hiflmc bowling sarcastic
    mcvan "And it's just a story. At least I thought so."
    "Vanessa shrugs."
    show hiflmc bowling basic
    va "Yes and no. That Van Helsing is a relative."
    va "But his story was pretty exaggerated by the time it was put into print."
    show hiflmc bowling sarcastic
    mcvan "The vampire part wasn't exaggerated."
    show hiflmc bowling basic
    va "No, but as you can see, the public didn't figure that out."
    show vanessa huntress smirk
    va "Otherwise old Van would have had some words with Stoker. Le Fanu too."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(If her ancestor was half as dramatic as she looks, I'm not sure how much exaggeration there was.)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa huntress basic at left4
    mcvan "How about the outfit?"
    mcvan "Do all vampire hunters dress like you?"
    show vanessa huntress sad
    va "Ah..."
    stop music fadeout 1.0
    play music hiflliteromance
    show vanessa huntress blush
    "For a split second, Vanessa's face flushes pink."
    show vanessa huntress sleep
    "She recovers her composure with another long sip of coffee."
    show vanessa huntress basic
    va "Most hunters are more subtle."
    show vanessa huntress smirk
    va "I dress to my own taste."
    hide hiflmc
    hide vanessa
    $menuhideborder = True

    menu vane3c1:
        "A. You certainly make an entrance.":
            $menuhideborder = False
            show hiflmc bowling happy at right4
            show vanessa huntress basic at left4
            mcvan "You certainly make an entrance."
            mcvan "Guns blazing and a cool silhouette in the fog."
            show vanessa huntress smirk
            va "I can't take credit for that."
            ma "The moonlight makes me look real good."

        "B. It's a good taste.":
            $menuhideborder = False
            show hiflmc bowling happy at right4
            show vanessa huntress basic at left4
            mcvan "It's a good taste."
            mcvan "I respect anyone who had an aesthetic and sticks to it."
            show vanessa huntress smirk
            va "Thanks."
            va "It took a long time to put it together."

        "C. Vampires beware, huh?":
            $menuhideborder = False
            show hiflmc bowling happy at right4
            show vanessa huntress basic at left4
            mcvan "Vampires beware, huh?"
            mcvan "If you look like that and they don't get out of your way..."
            show vanessa huntress smirk
            va "They should know better?"
            va "Yeah, that's part of it."

    hide hiflmc
    show vanessa huntress smirk at centre
    "Vanessa looks please as a cat with cream, even while downing the last bitter dregs of her cup."
    "Under the stars, she cuts a swathe of black and silver through the night, daring anyone else to come near."
    "But sitting right next to her, I'm not afraid."
    "For a woman who hunts vampires, she seems almost... normal."
    show hiflmc bowling happy at right4
    show vanessa huntress basic at left4
    mcvan "How do you keep from getting bored out here?"
    show vanessa huntress smirk
    va "I'm never bored on the hunt."
    va "And peace is so rare that it's nice to sit and take in everything around me."
    show vanessa huntress basic
    va "I need the calm nights as much as the busy ones."
    "She stacks her cup on top of my empty one, eyes cast up towards the moon."

    scene bg heroine_home_day at bg with fade
    stop music fadeout 1.0
    play music hifleveryday
    pause

    show hiflmc pajamas noglassesbasic at centre
    "I scrape a couple hours of sleep together before I have to get up for work."
    show hiflmc bowling basic with dissolve
    "Vanessa accepts my offer for breakfast, but eats it outside while I'm changing into my uniform."
    mcvan "I wonder how Grace is doing."
    show hiflmc bowling happy
    $sidecharone = "Text from [genericfn]"
    sid1 "Hope you're having a great first day at college! I miss you already."
    show hiflmc bowling basic
    "There's no immediate reply, and chances are that Grace is busy being lost on campus like every other freshman."
    show hiflmc bowling sad
    "My thumb hovers over the keyboard, and I wonder if I should tell her what happened."
    "(I think she'd be glad I'm alive, but the rest sounds like nonsense.)"
    show hiflmc bowling sarcastic
    "(How am I supposed to tell my sister vampires exist?)"
    mcvan "Never mind."
    hide hiflmc
    show vanessa casual basic at centre
    "Vanessa pokes her head in through the front door, empty dishes in hand."
    va "You've got to work soon, right?"
    show vanessa huntress smirk
    va "I'll give you a lift down there."

    show hiflmc bowling happy at right4
    show vanessa casual smirk at left4

    mcvan "Thanks. That'd be great."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I have to find the mechanic's number and get him to tow my truck out of that ditch.)"
    "(My wallet is already crying.)"
    hide hiflmc
    show bg main_day at bg with wipeleft
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    "It's a quick drive back into town, but when Vanessa pulls over to park, I catch a few stares from people coming out of the diner."
    "Most look curious, but a few are cold, judging a car that clearly doesn't belong in Havenfall."
    show hiflmc bowling angry
    mcvan "Jerks."
    show vanessa casual surprised
    va "What's wrong?"
    mcvan "We're getting the 'stranger danger' look from across the street."
    show vanessa casual basic
    va "Oh. I tend to get that everywhere I go."
    show vanessa casual smirk
    va "But in all fairness, I'm a pretty dangerous person."
    va "Just not to humans."
    show hiflmc bowling basic
    "I can't get over the way she says 'humans.'"
    "Every time is a reminder that there's something else, that we're not at the top of the food chain."
    show vanessa casual basic
    mcvan "Thanks for the ride."
    va "Let me walk you inside."
    show hiflmc bowling surprised
    mcvan "You don't have to. The sun is up."
    show vanessa casual sad
    va "..."
    va "And?"
    mcvan "Vampires and sun don't go together?"
    show hiflmc bowling sad
    show vanessa casual basic
    "Vanessa raises an eyebrow, and my heart sinks."
    va "Sorry to burst your bubble, but it's not quite that simple."
    va "Sun weakens them, but it's not a cure."
    show vanessa casual angry
    va "And there's a lot more than vampires to keep an eye out for."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Why am I arguing against a hot and friendly huntress following me around?)"
    "(It's not like I'm full up on company.)"
    hide hiflmc
    show hiflmc bowling happy at right4
    show vanessa casual basic at left4
    mcvan "Okay. Hope you like bowling alleys."
    show hiflmc bowling happy
    "I'm wondering how I should introduce Vanessa as we walk inside."
    hide hiflmc
    hide vanessa
    show bg bowling_regular at bg with wipedown
    show razi casual angry at left4
    show jd casual angry at right4
    "Razi and JD are chatting, but their conversation freezes in place when they see us."
    hide jd
    show razi casual basic at centre
    ra "...Morning, [genericfn]."
    ra "Got a new hire for me?"
    show razi casual basic at left4
    show hiflmc bowling happy at right4
    mcvan "No, just a friend. This is Vanessa."
    hide hiflmc
    hide razi
    show vanessa casual angry at centre
    "I expect Vanessa to say hello back, but she's staring at Razi and JD like the two of them just pulled a gun on her."
    show vanessa casual angry at left4
    show jd casual angry at right4
    "JD returns the look with a bit more heat, eyes narrowed."
    hide jd
    hide vanessa
    show hiflmc bowling surprised at centre
    mcvan "Do you all know each other, or..."
    hide hiflmc
    show jd casual angry at centre
    jd "No, definitely not. I'm JD."
    hide jd
    show razi casual basic at centre
    ra "Razi Nassar. Pleasure."
    hide razi
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Then why are they so stiff?)"
    hide hiflmc
    $menuhideborder = True

    menu vane3c2:
        "A. What am I missing?":
            $menuhideborder = False
            show hiflmc bowling surprised at centre
            mcvan "What am I missing?"
            mcvan "Did everyone wake up on the wrong side of the bed today?"
            show hiflmc bowling sad
            "(Vanessa and I are the ones who barely got any sleep, so what's with them?)"
            hide hiflmc
        "B. Vanessa, you okay?":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show vanessa casual angry at left4
            mcvan "Vanessa, are you okay?"
            show vanessa casual basic
            va "I'm fine."
            va "This just... isn't what I expected."
            hide hiflmc
            hide vanessa
        "C. Sorry for not telling you ahead of time.":
            $menuhideborder = False
            show hiflmc bowling sad at right4
            show razi casual basic at left4
            mcvan "Sorry for not telling you ahead of time, Razi."
            mcvan "I didn't think you'd mind."
            ra "Don't worry about it."
            hide hiflmc
            hide razi
    "The front door swings open swiftly behind us."
    show mac cop sad at centre
    "Sheriff Hunt steps in, looking a little out of breath, and sighs when she sees me."
    Sheriff "So you're okay."
    show mac cop sad at left4
    show hiflmc bowling surprised at right4
    mcvan "Me? Yeah, I'm fine."
    Sheriff "I found your truck on the side of the road empty this morning, and the house was empty too."
    Sheriff "Since it looked like there was a scuffle on the road, I thought something awful might have happened."
    show hiflmc bowling basic
    mcvan "The engine stalled out, Sheriff. I got a little lost in the fog."
    hide hiflmc
    show mac cop basic at centre
    "She nods, but when the sheriff's eyes fall on Vanessa, the concern on her face vanishes."
    show mac cop angry at left4
    show vanessa casual angry at right4
    "Tension coils up in her jaw, and Vanessa returns the look with a defiant stare."
    hide mac
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(What is happening here?)"
    hide hiflmc
    show mac cop basic at left4
    show vanessa casual basic at right4
    Sheriff "I don't think I caught your name, stranger."
    va "I didn't offer it, {i}sheriff{/i}."
    hide vanessa
    hide mac
    show hiflmc bowling basic at centre
    mcvan "We met the other day when I gave her a ride."
    show hiflmc bowling sad
    mcvan "I know this is a small town, but can everyone dial it down a little."
    show hiflmc bowling angry
    mcvan "No one's even pretending to be polite."
    hide hiflmc
    show mac cop sleep at centre
    "Sheriff Hunt clears her throat at that, shoulders relaxing by a few degrees."
    hide mac
    show vanessa casual smirk
    "Bit by bit, Vanessa does the same, summoning a faint smile."
    va "It's Vanessa."
    va "I was just giving [genericfn] a lift to work since her truck is out of commission."
    show mac cop basic at left4
    show vanessa casual smirk at right4
    Sheriff "Awful friendly of you."
    va "I do what I can."
    va "Trying to be a good samaritan and all that."
    hide vanessa
    hide mac
    show razi casual basic at centre
    ra "Mackenzie."
    show razi casual basic at left4
    show mac cop basic at right4
    "The sheriff breaks off her staring contest with Vanessa, looking his way."
    ra "Diego called earlier. Maybe go check up on him?"
    hide razi
    hide mac
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Why would she need to talk to Dr. Escalona?)"
    show hiflmc bowling_cu sarcastic_cu
    "(This is all too weird.)"
    hide hiflmc
    show razi casual basic at left4
    show mac cop basic at right4
    Sheriff "I'll do that."
    Sheriff "Have a good one."
    hide razi
    hide mac
    show vanessa casual angry at centre
    "The front door clangs as Sheriff Hunt pulls it shut behind her, but Vanessa still seems to be on her guard."
    show vanessa casual angry at right3
    show hiflmc bowling basic at left3
    "She leans forward, just enough for me to hear her whisper."
    va "You and I need to talk. Alone."
    show hiflmc bowling surprised
    mcvan "Right now?"
    va "Yes, right now."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(It's not like I mind being anywhere private with her.)"
    show hiflmc bowling_cu sarcastic_cu
    "(Callout for myself: too bi to make sensible decisions.)"
    "(Or stop myself from an internal monologue of innuendo.)"
    hide hiflmc
    $menuhideborder = True
    menu vane3c3:
        "A. Let Vanessa talk to you alone." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc bowling basic at centre
            mcvan "Hey, Razi."
            show hiflmc bowling basic at right4
            show razi casual basic at left4
            mcvan "I'm going to walk my friend back out. I'll start on the lanes in a minute."
            ra "Sure thing."
            hide hiflmc
            show razi casual basic at centre
            "His eyes stay locked on Vanessa until we both leave."
            hide razi
            pause
            show bg main_day at bg
            show hiflmc bowling basic at right4
            show vanessa casual basic at left4
            "She hooks a quick right down the alley between buildings, ducking into the shade there."
            show hiflmc bowling sad
            mcvan "Vanessa, I'm so sorry. I don't know what any of that was about."
            stop music fadeout 1.0
            play music hiflsuspense
            show vanessa casual angry
            va "How long have you known them?"
            show hiflmc bowling surprised
            va "Everyone in the bowling alley. The sheriff too."
            show hiflmc bowling sad
            mcvan "Um."
            mcvan "I mean, Razi's family has been here longer than mine has."
            mcvan "It's the same with Sheriff Hunt."
            show hiflmc bowling basic
            mcvan "JD showed up a couple of years back."
            va "And they're all your friends?"
            hide vanessa
            show hiflmc bowling surprised at centre
            "'Friend' is a weird word to use."
            show hiflmc bowling basic
            "Razi and I are friendly, but at the end of the day, he's still my boss."
            "JD and I only hang out at work, and I saw a lot more of the Sheriff back when we were in school than I do now."
            "If Dr. Escalona didn't have his daily drink at the bowling alley, I wouldn't run into him except for yearly checkups."
            show hiflmc bowling basic at right4
            show vanessa casual basic at left4
            mcvan "Havenfall is tiny. Everybody knows each other."
            show vanessa casual angry
            va "Even so, you need to be careful."
            va "There's a lot here that isn't what it appears to be."
            show hiflmc bowling surprised
            mcvan "What's that supposed to mean?"
            show hiflmc bowling sarcastic
            mcvan "I hope you're not trying to tell me everyone I know is a vampire."
            show hiflmc bowling basic
            show vanessa casual basic
            va "I didn't say anything about vampires."
            va "They're some of the easiest to spot."
            show hiflmc bowling surprised
            mcvan "Then what? Demons? Werewolves?"
            hide hiflmc
            show vanessa casual angry at centre
            "Vanessa crosses her arms, concern drawing her face into sharp angles."
            va "You make it sound like a joke."
            show hiflmc bowling sad at right4
            show vanessa casual angry at left4
            mcvan "I'm not making fun of you. It's just..."
            hide vanessa
            hide hiflmc
            stop music fadeout 1.0
            play music hiflliteromance
            show vanessa_s1_mini4 at bg:
                zoom 0.4
            "Reaching over to Vanessa's shoulder, I give it a light squeeze."
            "There's a surprising amount of muscle under my fingertips, lithe and tense."
            mcvan "Can you trust me, Vanessa?"
            mcvan "I've been trusting you a lot."
            hide vanessa_s1_mini4
            show bg main_day at bg
            show vanessa casual_cu sad_cu at vanessa_cu
            "Vanessa bites her lip, violet eyes settling on my hand."
            show hiflmc bowling blush at right3
            show vanessa casual sad at left3
            "I blush, relaxing my grip and trying to cover for it as quickly as I can."
            mcvan "Sorry, I..."
            hide hiflmc
            show vanessa casual basic at centre
            va "I do trust you."
            va "Plenty of people would have taken the information I gave you and tried to make a quick buck off it."
            va "Or called the first newspaper that might make them famous."
            show vanessa casual smirk
            va "You were scared, but you still kept everything undercover."
            show hiflmc bowling sad at right3
            show vanessa casual basic at left3
            mcvan "I'm not out to spill your secrets, Vanessa."
            va "I know. And I want this to keep going both ways."
            show vanessa casual sad
            va "You don't see what I see. It's not part of who you are."
            va "I have to remember that."
            hide vanessa
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(But what is she seeing?)"
            show hiflmc bowling_cu sad_cu
            "(What's so bad that it sets everyone off the moment they look at her.)"
            show hiflmc bowling basic at right3
            show vanessa casual sad at left3
            va "Will you promise to stay on your guard?"
            show hiflmc bowling happy
            mcvan "Of course."
            show hiflmc bowling sarcastic
            mcvan "Trust me, after what I saw, I'm not dropping it anytime soon."
            show vanessa casual happy
            "Vanessa's smile is small and almost sad."
            "The reason escapes me, though."
            va "Right."
            show vanessa casual basic
            va "Just remember that you have my phone number."
            va "If anything seems out of the ordinary, call me."
            show hiflmc bowling happy
            mcvan "I will."
            mcvan "But don't stress out worrying over me."
            show hiflmc bowling basic
            va "Someone has to."
            show hiflmc bowling surprised
            mcvan "I..."
            hide vanessa
            hide hiflmc
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(She really takes this pledge of protection seriously, huh?)"
            hide hiflmc
            show vanessa casual basic at centre
            va "You're not weak just because I'm looking out for you."
            show vanessa casual smirk
            va "Think of me as a bodyguard."
            va "I'll be in the background, but you don't have to pay me any attention."
            va "I'll intervene when I need to."
            show hiflmc bowling happy at right3
            show vanessa casual basic at left3
            mcvan "It's hard not to pay attention to you. Just putting that out there."
            show vanessa casual smirk
            va "My look isn't subtle, so I'll give you that."
            hide vanessa
            hide hiflmc
            show hiflmc bowling_cu blush_cu at hiflmc_cu
            "(I meant her in general, not the outfit.)"
            show hiflmc bowling_cu basic_cu
            "(Vanessa's life is so far from anything I've ever imagined.)"
            show hiflmc bowling_cu sad_cu
            "(She fights monsters and I...)"
            "(I need to go back inside and rearrange bowling balls by weight.)"
            hide hiflmc
            show hiflmc bowling basic at right3
            show vanessa casual basic at left3
            mcvan "I should start my shift."
            va "Go ahead."
            show vanessa casual angry
            va "But don't go anywhere without your phone."
            stop music fadeout 1.0
            play music hifleveryday
            show hiflmc bowling sarcastic
            mcvan "I never do. I'd die of boredom."
            show hiflmc bowling happy
            show vanessa casual smirk
            "Vanessa's laugh dispels then tension lingering between us, and she shepherds me back to the front door."
            show hiflmc bowling basic
            "I wonder if she's going to sit parked across the street all day, but it seems rude to ask."
            hide vanessa
            hide hiflmc
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(And she probably has better things to do.)"

        "B. Work your shift.":
            $menuhideborder = False
            show razi casual basic at centre
            "Razi is still staring at both of us."
            "I can't walk away from my job right in front of my boss, esxpecially with JD there too."
            hide razi
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(They would never let me live it down.)"
            hide hiflmc
            show hiflmc bowling sad at right3
            show vanessa casual basic at left3
            mcvan "I have to start work."
            mcvan "Can we do this after my shift?"
            va "This is important."
            show hiflmc bowling sarcastic
            mcvan "So are my bills."
            mcvan "My truck isn't getting out of that ditch all by itself."
            show hiflmc bowling basic
            show vanessa casual angry
            "Frustration flares across Vanessa's face, but she relents with a firm nod."
            show vanessa casual basic
            va "Okay."
            va "But if {i}anything{/i} comes up, you have my number. Call me."
            show vanessa casual angry
            va "Even if you just have a bad feeling."
            mcvan "I will. I promise."
            hide hiflmc
            show vanessa casual angry at centre
            "She seems somewhat satisfied with that, but levels one last icy look at Razi and JD before slinking out of the bowling alley."
            hide vanessa
            show hiflmc bowling angry at centre
            "The moment she door closes, I turn around to face them."
            mcvan "That was so rude! She just got here."
            show hiflmc bowling angry at right4
            show jd casual angry at left4
            jd "It's not about being rude, [genericfn]."
            jd "Some people give off the wrong vibe."
            show hiflmc bowling sarcastic
            "I roll my eyes."
            mcvan "JD, you've been kicked out of almost every business in town at least once."
            show jd casual surprised
            jd "Exactly. I'm a wrong vibe expert."
            show hiflmc bowling sad
            mcvan "Well, Vanessa was nice to me. Really nice."
            mcvan "Isn't that worth something?"
            hide jd
            show razi casual sad at left4
            ra "We're not judging you, [genericfn]."
            ra "But when's the last time someone new rolled into town? It's always a little weird, isn't it?"
            mcvan "I guess."
            show hiflmc bowling basic
            mcvan "But that's usually because they're big city tourists and think we're all part of the landscape."
            hide razi
            show jd casual angry at left4
            jd "Your new friend didn't seem to think much of us either."
            show hiflmc bowling sarcastic
            mcvan "She doesn't know you."
            hide jd
            hide hiflmc
            show hiflmc bowling_cu angry_cu at hiflmc_cu
            "(Everyone got off on the wrong foot. Ugh.)"
            show hiflmc bowling_cu sarcastic_cu
            "(Is this why I'm so bad at making friends?)"
            "(My social skills have been rusting since high school.)"
            hide hiflmc
            show razi casual basic at centre
            ra "How about we all get back to work?"
            ra "No harm, no foul."
            hide razi
            show hiflmc bowling sarcastic at centre
            "I was going to show Vanessa around, but now it looks like I have an appointment with the sticky arcade machines."
            "(Anyone who stacks their soda next to the joysticks is my worst enemy.)"
            hide hiflmc
            show jd casual basic at centre
            jd "Work it is."
            show jd casual smirk
            jd "I call rearranging the shoes."
            show jd casual smirk at right4
            show razi casual basic at left4
            ra "As long as you actually pair them together this time, sure."
            show jd casual basic
            jd "There's about a thirty percent chance of me doing that."
            show razi casual sad
            "Razi groans but waves them off towards the shelves."
            hide razi
            hide jd
            show hiflmc bowling basic at centre
            "I hunt down the rags and cleaner, preparing myself to breathe in artificial lemon for the next hour."
            show hiflmc bowling sad
            "(I hope Vanessa wasn't offended by how everyone reacted to her.)"
            "(It was so hard not to say that she saved my life.)"
            show hiflmc bowling sarcastic
            "(That would bring up way too many questions.)"

    scene bg main_fog at bg with fade
    stop music fadeout 1.0
    play music hiflsuspense
    pause

    show hiflmc bowling sad at centre
    "Fog is rolling down Main Street by the time I get out of work, and I shiver, looking for any sign of Vanessa's camper."
    "(She promised to pick me up after my shift.)"
    hide hiflmc
    "Movement ripples through the mist across the street."
    show li casual basic at centre
    "A gray outline stretches into the shape of a woman I've never seen before, wearing a dress of embroidered silk."

    "With every step she takes towards me, her beauty glimmers under the moonlight, surreal and sharp."
    $sidecharone = "Mysterious Woman"
    show li casual happy
    sid1 "Sister."
    sid1 "I have been searching for you."
    "Her voice is musical, slipping into my ears like a spell."
    show li casual_cu happy_cu at li_cu
    "Bright red eyes pierce me through, and my body freezes in place."
    hide li


    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
