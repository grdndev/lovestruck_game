define unknown = Character("???",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define Sheriff = Character("Sheriff Hunt",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define mail = Character("Mail Carrier",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define doc = Character("Dr. Escalona",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])

label mac_season1_episode1:

    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show blackscreen at bg with dissolve
    show bg road_day at bg

    show truck_back_day at bg
    show hiflmc bowling sarcastic at right2:
        zoom 1.05
    show grace waitress basic at left2:
        zoom 1.05
    show truck_front_day at bg
    with dissolve
    "Indiana doesn’t have much to look at on the sides of the road."

    "I’ve been passing the same twenty fields my whole life, broken up by the occasional car sale, and
    there’s no signs of it getting any better."
    show hiflmc bowling happy at right2:
        zoom 1.05
    "(At least I have company in the car.)"
    mcmac "You’ve been fiddling with the radio for twenty minutes, sis."
    show grace waitress happy at left2:
        zoom 1.05
    gr "We’ve got to get one of those adapters for the car so I can play music through my phone."

    gr "This thing's ancient."
    show hiflmc bowling sad at right2:
        zoom 1.05
    mcmac "I know. Unfortunately, anything with an engine in this century is out of my price range."
    show grace waitress sad at left2:
        zoom 1.05
    gr "Any way I can help?"

    "I sigh, trying not to tense up."

    "She's only eighteen; it shouldn't be her responsibility to try and crowdfund me a new truck."
    show hiflmc bowling sad at right2:
        zoom 1.05
    "(Except we're all each other has left in the world.)"

    "(And Grandma sold off her sedan right before she passed away.)"
    show hiflmc bowling happy at right2:
        zoom 1.05

    show grace waitress happy at left2

    mcmac "Let me worry about that. We’ve got to get you to work."

    hide truck_back_day
    hide grace
    hide hiflmc
    hide truck_front_day


    show bg main_day at bg
    show truck_back_day at bg
    show hiflmc bowling basic at right2:
        zoom 1.05
    show grace waitress happy at left2:
        zoom 1.05
    show truck_front_day at bg

    "I turn onto Main Street and hunt down a parking space right by the diner, doing a double-check of
    my uniform before getting out."
    hide grace
    hide truck_back_day
    hide truck_front_day
    show hiflmc bowling basic at centre:
        zoom 0.8
        xoffset 90
        yoffset -200
    "It should have been washed last night, but I was too tired to babysit the finicky drier."
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Whatever. No one is going to notice anyway.)"
    scene bg diner_lights_on at bg with fade

    pause

    show grace waitress happy at centre

    "Grace heads inside first, giving a friendly wave to her manager."
    show grace waitress happy at left4
    show luce casual basic at right4

    lu "Mornin', Grace."

    hide grace
    hide luce


    show mac glassescop basic at centre

    "This early, the only other person in the diner is Sheriff Mackenzie Hunt, nursing a cup of coffee
    in the corner."

    show hiflmc bowling happy at left4

    show mac glassescop surprised at right4

    "I flash a smile at her - everyone knows the sheriff - but she gives me a cool once over before
    visibly sniffing the air."

    show hiflmc bowling surprised

    show mac glassescop angry
    "From her raised brow, she's none too impressed, eyes falling away from mine."
    hide mac
    hide hiflmc

    show hiflmc bowling_cu sad_cu at hiflmc_cu

    "(God, if there's any chance of a groundhog-style redo of this day, I'd take it right now.)"

    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Way to make the hot cop think you're such a slob, [genericfn]!)"
    hide hiflmc

    show hiflmc bowling_cu sad_cu at hiflmc_cu

    "Resisting the urge to sink right into the floor, I retreat to the counter to get some
    caffeine of my own."
    hide hiflmc

    show hiflmc bowling sad at left2

    show grace waitress happy at right2

    gr "Coffee to go?"
    show hiflmc bowling happy at left2
    mcmac "Please. You're a lifesaver."
    hide hiflmc
    hide grace

    show damien casual smirk at centre

    unknown "I'd love a cup of black while you're back there workin', miss."

    "A tall man in a buckskin jacket slides up to the counter, smiling like he's just won the lottery."

    show damien casual smirk at left2
    show grace waitress basic at right2

    "My sister turns around, her polite work mask in place as she flips the coffee machine back to
    brewing."

    gr "You bet."

    gr "New to town? I don't think I've seen you before."

    unknown "Just came in. Liked the look of the place."

    unknown "Not to mention the pretty girl working here."
    hide damien
    show hiflmc bowling surprised at left2
    show grace waitress sad at right2
    "My jaw drops slightly, and I catch Grace's eyes going wide."
    show grace waitress happy at right2
    "She recovers with a little laugh, fumbling to get the lid of my cup on."
    hide hiflmc
    show damien casual smirk at left2
    gr "The coffee's only ninety-nine cents. You don't have to flirt for a discount."

    "He reaches into his pocket and plucks out a five dollar bill, dropping it right into the
    tip jar."

    unknown "Guess the rest goes to you, sweetheart."

    unknown "Two sugars if you please."
    hide grace
    hide damien

    show hiflmc bowling_cu angry_cu at hiflmc_cu

    "(This guy's being kind of aggressive. Does he even know how old she is?"

    "(I should probably say something-!)"
    hide hiflmc

    show damien casual basic at left5
    show grace waitress basic at right1
    show mac glassescop basic at right5

    stop music fadeout 1.0
    play music hiflmaintheme

    Sheriff "Grace. I hope this gentleman isn't giving you any trouble."

    hide damien
    hide grace
    show mac glassescop smirk at centre

    "The sheriff leans against the counter, a casual sort of grace in her posture, but the
    warmth in a small smile that doesn't reach vivid green of her eyes."

    "She's on alert too, and that makes me feel a little better."
    hide Mac

    show damien casual basic at left5
    show grace waitress basic at right1
    show mac glassescop smirk at right5

    gr "No, Mackenzie. I'm okay, promise."

    show mac glassescop happy

    "When the man doesn't say a word, she relents with a nod, smile growing a bit wider."
    hide damien
    hide grace
    hide mac

    show grace waitress basic at left2
    show mac glassescop happy at right2

    Sheriff "I usually only go by Mackenzie off-duty, you know."
    show grace waitress happy
    gr "Bet you'll forgive me if I refill your coffee."

    Sheriff "Got me there."
    hide grace
    hide mac

    show damien casual basic at centre
    "My sister passes over my cup too, and the mysterious man decides to take up a booth in the
    back."
    hide damien

    show hiflmc bowling sad at left2

    show mac glassescop surprised at right2

    "I let out a little sigh of relief, one the sheriff catches with a look."

    Sheriff "You doing okay this morning?"
    hide mac
    hide hiflmc
    $menuhideborder = True
    menu mace1c1:
        "1. Admit you're tired":
            $menuhideborder = False
            show hiflmc bowling sad at left2

            show mac glassescop surprised at right2
            mcmac "Kind of."

            mcmac "Staying up with the late-night shark week marathon was probably a mistake."
        "2. Mention the truck":
            $menuhideborder = False
            show hiflmc bowling sad at left2

            show mac glassescop surprised at right2
            mcmac "Same old, same old."

            mcmac "My sister wishes I had a car manufactured before Pluto stopped being a planet."
        "3. Talk about your sister.":
            $menuhideborder = False
            show hiflmc bowling sarcastic at left2
            show mac glassescop surprised at right2
            mcmac "Yeah, just caught a little off-guard by... that."
            show hiflmc bowling angry
            mcmac "Usually the only guys who flirt with Grace are drunk truckers."
    hide mac
    hide hiflmc
    show hiflmc bowling_cu happy_cu at hiflmc_cu

    "(If she doesn't mention my uniform, I'll have gotten out of this conversation intact.)"
    hide hiflmc

    show grace waitress happy at right2
    show hiflmc bowling surprised at left2
    gr "Sis, you're going to be late."
    hide grace
    show mac glassescop basic at right2
    mcmac "Shit. Sorry, Sheriff. I'm out of here."
    hide mac
    hide hiflmc

    show mac glassescop surprised at centre:
        zoom 1.25
        xoffset 50
    show hiflmc bowling surprised at centre:
        zoom 1.25
        xoffset -300
        yoffset 130
    "I grab my coffee without thinking, my elbow knocking against hers."

    "When the lid pops off and spills right onto her clean police blues, I go full-on deer
    in the headlights."
    hide mac
    hide hiflmc

    show mac glassescop_cu surprised_cu at mac_cu

    Sheriff "..."
    hide mac

    show hiflmc bowling_cu surprised_cu at hiflmc_cu

    mcmac "I am SO sorry. Let me get a napkin and I'll-!"
    hide hiflmc
    show mac glassescop_cu angry_cu at mac_cu


    Sheriff "Get to work. I'll take care of it."
    hide mac
    show hiflmc bowling surprised at left2
    show mac glassescop angry at right2

    "The growl in her words puts a kick in my step, and I duck out of the diner before I get
    filed away as a category five disaster."
    hide mac
    hide hiflmc

    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu


    "(Of all the people to embarrass myself in front of. No wonder I can't get a date.)"

    show blackscreen at bg with dissolve
    scene bg bowling at bg
    with dissolve
    stop music fadeout 1.0
    play music hifleveryday
    pause


    show hiflmc bowling sarcastic at centre

    "I pick up an energy drink from the corner store so I don’t spend the whole day as a zombie."

    show hiflmc bowling sad at centre

    "But there's honestly only so much pep I can have for opening up a bowling alley."

    hide hiflmc
    show razi casual basic at left2
    show hiflmc bowling sad at right2

    "Razi is already behind the counter after I flip the sign, scrubbing a rack of glasses clean."

    show hiflmc bowling happy at right2

    mcmac "Hey, Razi. Hope I didn't miss a party."

    show razi casual smirk at left2

    ra "It wouldn't start until you walked in."

    mcmac "Thanks, boss. What's on the agenda today?"

    show razi casual basic

    ra "Setting up the racks mostly. I've got the back cleaned up."

    ra "And JD has been making playlists on the jukebox for the last twenty minutes."

    hide hiflmc
    show jd casual smirk at right2

    jd "It's a crime that you don't have {i}It's Not Unusual{/i} on this thing."
    show razi casual angry

    ra "The crime is me paying you nine dollars an hour to perfect your disaffected lean
    against my wall."

    hide jd
    hide razi
    show jd casual happy at centre

    "Jordan's smile is the most frustrating thing in the world."

    "They know exactly how eye-catching they are, and just how far to push before Razi
    throws a dish towel."

    hide jd
    show hiflmc bowling_cu happy_cu at hiflmc_cu

    "(But hey, I don't get paid to stand around looking pretty either.)"
    hide hiflmc

    show hiflmc bowling basic at left2
    show jd casual happy at right2


    mcmac "Come on, JD. Help me set up the pins."

    show jd casual sad

    jd "You realize neither of us can set up the pins."
    show jd casual smirk

    jd "Eventually, Razi will do it because he cares about the reputation of this little
    establishment."
    show hiflmc bowling happy

    mcmac "I wouldn't do that because I like Razi."
    show jd casual basic

    jd "I like Razi too. What I don't like being is a gofer."
    hide hiflmc
    show razi casual angry at left2

    ra "And Razi is telling you to go set up pins before you get your ass booted out onto
    the street."
    show jd casual angry
    ra "The sheriff wouldn't be too thrilled with that, would she?"
    show jd casual sad
    jd "...Right."
    hide jd
    hide razi
    show hiflmc bowling_cu basic_cu at hiflmc_cu

    "(JD's on parole or something."
    show hiflmc bowling_cu sad_cu
    "(I've never gotten the details, but they're not really into full disclosure.)"
    show blackscreen at bg with dissolve
    scene bg bowling at bg
    pause

    show razi casual happy at left3
    show hiflmc bowling happy at centre
    show jd casual happy at right3

    "It's a slow afternoon, slow enough that all three of us perk up when the front doors open."
    stop music fadeout 1.0
    play music hiflgetitdone
    hide razi
    hide hiflmc
    hide jd
    show mac glassescop basic at centre


    "The last person I expect to see is Sheriff Hunt—Mackenzie—although I'm glad to see
    she found a replacement for her uniform shirt."
    hide mac
    show razi casual sad at left3
    show jd casual basic at right3

    "Razi is less enthused."

    ra "What did JD do this time?"
    show jd casual angry
    jd "Isn't the phrase 'innocent until provent guilty', Razi?"
    show razi casual angry
    show jd casual sad
    ra "Not when she's making a beeline for you. I know that look."
    hide razi
    show mac glassescop basic at left3
    ma "So do they."

    ma "This is the second time in a month you've ripped someone off at the gas station, Davies."
    show jd casual basic

    "JD wipes their face of any expression, but the defensive cross of their arms says enough."

    jd "I'm not a thief. You know that."

    ma "No, talking someone into a raw deal makes you a con artist."

    ma "Although whether that's a step up or down depends on your lawyer."
    hide mac
    show razi casual basic at left3
    ra "Which you don't have, JD."
    show jd casual smirk
    jd "I speak for myself."
    hide razi
    show mac glassescop angry at left3
    jd "And what I received was a gift. Are you looking for a cut?"
    hide jd
    hide mac
    show mackenzie_s1_mini11 at bg
    "Mackenzie's eyes narrow at the implication, and I take a small step away."
    hide mackenzie_s1_mini11
    show mac glassescop angry at left3
    show jd casual smirk at right3
    "Her presence fills the room with unquestional authority, but Jordan doesn't back down."

    ma "Say that again."
    show jd casual happy
    jd "It was a joke."

    ma "A bad one. I can't keep covering for you, JD."
    hide mac
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Covering? I'm surprised she's not arresting them on the spot.)"
    hide hiflmc
    show mac glassescop angry at left3
    show jd casual angry at right3
    jd "I never asked you to—!"
    show mac glassescop sad
    ma "You know better. And you know why."
    hide mac
    show razi casual angry at left3
    ra "Part of you working here is keeping a low profile. Cut the sheriff some slack."
    hide razi
    show mac glassescop sad at left3
    jd "..."
    show jd casual sad
    jd "No one notices but you, Mac. They don't know any better."
    show mac glassescop angry
    ma "This is my damn town. If I notice, it matters."
    hide mac
    hide jd
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(It must be hard for her. She works almost completely alone.)"
    show hiflmc bowling_cu sarcastic_cu
    "(Usually it’s just kids drag racing or DUIs on the Fourth...)"
    show hiflmc bowling_cu happy_cu
    "(But I remember hearing she ripped a shotgun right out of a guy’s hands after he robbed the corner store.)"
    hide hiflmc
    show mac glassescop basic at left3
    show jd casual basic at right3
    jd "Fine. I'll keep my hands to myself."
    show mac glassescop angry
    ma "Good, because you’re working my last nerve."
    hide jd
    show hiflmc bowling basic at right3
    "Razi sends Jordan to the back with a wave, but curiosity gets the better of me when Mackenzie turns
    to leave."
    $menuhideborder = True
    hide mac
    hide hiflmc
    menu mace1c2:
        "1. Ask about her shirt.":
            $menuhideborder = False
            show mac glassescop surprised at left3
            show hiflmc bowling sad at right3
            mcmac "Hey, I just wanted to say I'm sorry about this morning."
            mcmac "Did you have a backup shirt at the station?"
            show mac glassescop basic
            ma "Thankfully. But it's nothing that won't come out in the wash."
            show mac glassescop happy
            ma "Don't worry about it."
        "2. Bring up JD.":
            $menuhideborder = False
            show hiflmc bowling sad at right3
            show mac glassescop basic at left3
            mcmac "Um, is everything okay with JD?"
            mcmac "I know they've had a couple run-ins with the cops, but..."
            show mac glassescop angry at left3
            ma "That's my business to handle, [genericfn]."
            show mac glassescop basic at left3
            ma "They're not violent or anything, so don't stress."
        "3. Mention your sister.":
            $menuhideborder = False
            show hiflmc bowling sad at right3
            show mac glassescop basic at left3
            mcmac "Was my sister doing okay when you left the diner?"
            show mac glassescop basic
            ma "She's just fine. I left her a nice tip."

            mcmac "Sorry. I probably sound a little overbearing."
            show mac glassescop happy
            ma "Not at all. Family's important."

    hide mac
    hide hiflmc
    show hiflmc bowling basic at centre
    "Mackenzie checks her phone and tells me she had to run, so I go back to my shift."
    show hiflmc bowling sarcastic
    "Razi tries to keep things exciting, but it's a real drudge until close, and after locking up,
    I get in my truck to pick up Grace."



    scene blackscreen at bg with dissolve
    stop music fadeout 1.0
    play music mackenziehunt
    show bg diner_lights_off at bg with dissolve

    show hiflmc bowling basic at left3
    show luce casual basic at right3

    "The diner's empty by the time I get there, but I find Luce, the owner, closing out the register."

    "When I glance around, my sister’s nowhere to be seen."
    show hiflmc bowling happy
    mcmac "Hey. She in the back cleaning or something?"
    show hiflmc bowling basic
    lu "Grace? I let her off fifteen minutes early."

    mcmac "Were things that slow?"

    lu "Yeah. A friend picked her up and they went off."
    show hiflmc bowling surprised
    "That stops me short."

    "I love my sister, but she's always been painfully shy, and I'm pretty sure all of her friends are
    online."
    show hiflmc bowling angry
    mcmac "Which friend?"

    lu "Tall guy. Nice jacket."

    mcmac "Buckskin?"

    lu "That's the one. I know she doesn't get a lot of chances to go out much."

    hide luce
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu

    "(Not when both of us work to keep everything paid for.)"

    "(I shouldn't be paranoid.)"

    "(Grace would kill me if I ruined her first chance for a boyfriend since high school.)"

    hide hiflmc
    show hiflmc bowling sad at left3
    show luce casual basic at right3

    lu "Everything okay?"
    $menuhideborder = True
    hide luce
    hide hiflmc
    menu mace1c3:
        "1. I hope so.":
            $menuhideborder = False
            show hiflmc bowling sad at left3
            show luce casual basic at right3
            mcmac "I hope so..."
        "2. Overprotective sister habits.":
            $menuhideborder = False
            show hiflmc bowling happy at left3
            show luce casual basic at right3
            mcmac "Overprotective sister habits die hard."
            mcmac "I'm used to being the only one looking out for her, you know?"
        "3. Don't worry about it, Luce.":
            $menuhideborder = False
            show hiflmc bowling sad at left3
            show luce casual basic at right3
            mcmac "Don't worry about it, Luce."
            show hiflmc bowling sarcastic at left3
            show luce casual basic at right3
            mcmac "I'll probably find her crashed out on the couch for a gossip session in an hour."

    hide hiflmc
    hide luce
    show hiflmc bowling basic at centre
    "Just in case, I send her a text to check in and leave the diner to drive home."

    scene blackscreen at bg with dissolve
    stop music fadeout 1.0
    play music hifleveryday
    show bg heroine_home_lights at bg with dissolve
    pause

    show hiflmc pajamas basic at centre

    "The house feels cramped as always, but I fall into my evening routine and grab something from the
    freezer, tossing it into the microwave."
    show hiflmc pajamas sarcastic
    mcmac "Thanks, radiation."
    show hiflmc pajamas basic
    "My next stop is the couch, flipping on the TV so I can stream a documentary."
    show hiflmc pajamas sad
    "There's a new one on France I haven’t seen, and just the intro makes me wish I could hop on a plane and be anywhere but here."
    hide hiflmc
    show hiflmc casualnovest_cu sad_cu at hiflmc_cu
    "(I had the chance once, after college. Coming home from that gap year sucked.)"
    hide hiflmc
    show bg heroine_home_night at bg with dissolve
    pause

    show hiflmc pajamas noglassessarcastic at centre
    "I doze off, waking up a few hours later to a dark room and a new documentary next to auto play."

    "Staring at a pair of wolves rolling around in grass and trying to figure out how that relates to Paris, I reach for my phone to check the time."

    mcmac "Two a.m. Ugh."
    show hiflmc pajamas noglassesbasic
    mcmac "Better check on Grace."
    hide hiflmc
    show hiflmc casualnovest_cu noglassessad_cu at hiflmc_cu
    "(She hates when I sleep on the couch.)"
    hide hiflmc
    show hiflmc pajamas noglassesbasic at centre
    "Ducking my head into her dark room, I fumble for the light."
    show bg heroine_home_lights at bg with dissolve
    show hiflmc pajamas noglassessurprised
    stop music fadeout 1.0
    play music mackenziehunt
    "When it flickers on, revealing her untouched and empty bed, my blood turns cold."


    mcmac "Sis?"
    show hiflmc pajamas noglassesangry
    mcmac "This better not be a trick."
    hide hiflmc
    show hiflmc casualnovest_cu noglassessarcastic_cu at hiflmc_cu
    "(As if she’s ever played a prank in her life.)"
    show hiflmc casualnovest_cu noglassessad_cu
    "(Where the hell is she?)"
    hide hiflmc
    show hiflmc pajamas noglassesbasic at centre

    "The first thing I do is call her cell."

    "It goes to voicemail, and after a second try, I search through my apps for the Phone Finder we both installed a while back."
    hide hiflmc
    show hiflmc casualnovest_cu noglassessad_cu at hiflmc_cu

    "(She left her phone at a coffee shop in the city and panicked for three hours before I found it.)"

    "(Didn’t want that happening a second time.)"
    show mackenzie_s1_mini1 at bg with wiperight

    "It takes a second for the app to load, but the GPS starts pinging right away."

    "I frown while bringing my face close to the screen, making sense of the map."
    show bg heroine_home_lights at bg
    show hiflmc pajamas noglassesangry at centre
    hide mackenzie_s1_mini1
    mcmac "What is she doing at the lake this late?"

    mcmac "I don’t care if she’s with a cute guy. I’m picking her up right now."

    scene blackscreen at bg with dissolve
    show road_moon at bg with dissolve
    show truck_back_night at bg
    show hiflmc casual angry at right2:
        zoom 1.05
    show truck_front_night at bg
    pause


    "Thankfully, my truck starts up without any trouble, and I head right for the lake."

    "It’s almost too dark to see, but between my headlights and the full moon, I find a path close to the water's edge."
    scene bg lake_moon at bg
    show hiflmc casual surprised at centre


    "When I kill the engine and get out, I notice another set of tracks in the mud, following them up to a police car hidden just behind the bushes."
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Not a police car. The police car.)"

    "(Our town only has one.)"
    show hiflmc casual surprised at centre

    mcmac "Why would Sheriff Hunt be out here? No one lives back this way."
    show hiflmc casual basic
    mcmac "...Hell, maybe she can help me find Grace."

    "Following the blinking path on the phone app, I walk around the edge of the water, keeping my eyes and ears open for any signs of her."
    show hiflmc casual surprised

    "When a branch snaps in the distance, I tense up, the crunch of leaves getting loud and close."

    mcmac "Right on the dot."

    mcmac "Sis, is that you?"

    "A shadow darts by me, the silhouette much taller than my sister's ever been."

    hide hiflmc
    show mackenzie_s1_mini11 at bg


    "I stumble back, startled by a flash of gold under the moonlight, glowing brighter and brighter."

    "It’s a pair of eyes I know."
    hide mackenzie_s1_mini


    stop music fadeout 1.0
    play music hiflsuspense
    scene mac1 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 8 yanchor 0.1

    "Mackenzie doesn’t seem to see me, but I see a pair of furred ears sprout from the top of her head and I almost drop my phone."
    show mac1 at bg:
        yanchor 0.1
    "(The fuck?!)"

    "She throws her head up towards the sky, letting out a blood-curdling howl."

    "Claws burst from her fingertips, muscle bulging with even more strength, and all I can do is stare."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
