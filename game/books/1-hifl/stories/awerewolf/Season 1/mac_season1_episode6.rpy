##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[macfn1]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[macfn2]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode6:
    $tbc = False

    ##Change these to suit the story
    scene bg road_day at bg
    show police_back_day at bg
    show police_grate_day at bg
    show police_front_day at bg

    play music hiflsad

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show hiflmc bowling basic at left4 behind police_front_day:
        zoom 1.05
    show mac earscop wolfbasic at right4 behind police_front_day:
        zoom 1.05
    "With every passing second, the lake fades from view, but I remember how fast I’ve seen Mackenzie run..."

    "How fast the werewolf that attacked me could move."
    show hiflmc bowling sad
    "Would a car even make any difference?"
    show mac earscop wolfsad
    ma "Are you okay? Did she hurt you?"
    show hiflmc bowling happy
    mcmac "Just some mud on my clothes."
    show hiflmc bowling sad
    mcmac "I thought she was going to bite me."
    show mac earscop wolfangry
    "Mackenzie bnares her teeth at that, which are still sharp."

    "We're heading right into town when she's shifted, but I wouldn't want to change back either when there might be a pack chasing after us."
    show mac droopcop sleep
    ma "I can't believe I let Damien bait me that easily."
    show mac earscop wolfsad
    ma "Of course he recruited others to his cause."

    ma "Plenty of wandered out there would jump at the chance for an easy fight."
    show hiflmc bowling surprised
    mcmac "But why? What do they get out of it?"
    show mac earscop wolfbasic
    ma "Depends on what deals he made."

    ma "Might be territory, might be their pick of someone in the town to change."

    ma "Even money is enough for some."
    show hiflmc bowling sarcastic
    "(Great. Just what this place always needed: werewolf mercenaries.)"
    show hiflmc bowling basic
    ma "But that means he's dead serious about getting rid of me."
    show hiflmc bowling surprised
    ma "The fact that he took Grace means he might kidnap anyone if it would lure me into an unfair fight."
    show hiflmc bowling sad
    "(This is unreal.)"
    show hiflmc bowling basic
    mcmac "Why does he want this particular town so much?"
    show hiflmc bowling sarcastic
    mcmac "Like, no offense to the place where I was born, but there's not a lot here."

    mcmac "There never has been."
    show hiflmc bowling basic
    ma "There could be two sticks propping up a tent here and Damien would still challenge me over both of them."
    show mac earscop wolfsurprised
    ma "It's not about the town itself so much as..."
    show mac droopcop sleep
    "Mackenzie shakes her head, dismissing whatever was about to come out of her mouth."
    show mac earscop wolfsad
    ma "When I know we're safe, I'll tell you."
    show mac earscop wolfbasic
    ma "Right now, it doesn't matter."

    ma "What matters is that you're okay and that we find Grace."
    $menuhideborder = True
    hide hiflmc
    hide mac


    menu mace6c1:
        "A. It matters to me.":
            $menuhideborder = False
            show hiflmc bowling sad at left4 behind police_front_day:
                zoom 1.05
            show mac earscop wolfbasic at right4 behind police_front_day:
                zoom 1.05
            mcmac "It matters to me. You matter to me."
            show hiflmc bowling sarcastic
            "(Hopefully that's not coming on too strong, but whatever, I mean it.)"
            show hiflmc bowling sad
            ma "I appreciate that, [genericfn], but it's very complicated."

            ma "We're talking about struggles that started before you or I were born."

        "B. But I'm worried about you.":
            $menuhideborder = False
            show hiflmc bowling sad at left4 behind police_front_day:
                zoom 1.05
            show mac earscop wolfbasic at right4 behind police_front_day:
                zoom 1.05
            mcmac "But I'm worried about you."
            mcmac "You're doing all this for Grace and I, but you're still at risk too."
            show hiflmc bowling surprised
            mcmac "Hell, you're at more risk."
            show hiflmc bowling sarcastic
            mcmac "You have to keep this big secret while Damien's running around without giving a damn."
            show hiflmc bowling sad
            ma "He won't out himself in public."
            ma "The only reason he let you see him was because he planned to take you."
            show mac earscop wolfsad
            ma "History's proven that when it comes down to one werewolf versus a mob, the mob usually wins."

        "C. I know that.":
            $menuhideborder = False
            show hiflmc bowling sad at left4 behind police_front_day:
                zoom 1.05
            show mac earscop wolfbasic at right4 behind police_front_day:
                zoom 1.05
            mcmac "I know that. I'm not trying to write a werewolf research paper."

            mcmac "It just feels like the more I know about what's going on, the more control I have over the situation."

            ma "I get that. Trust me, I'm not trying to stall you out."
            ma "But this situation doesn't come with Cliff Notes."

    show hiflmc bowling basic
    show mac earscop wolfbasic
    mcmac "I got it."
    show hiflmc bowling surprised
    mcmac "Are you... going to change back, though?"
    show mac droopcop sleep
    "Mackenzie lets out a deep breath."
    show bg main_day at bg
    "The town's first streetlight is just a few feet in front of us, and she's gripping the steering wheel so tight I think it might break."

    "(Can she not do it? That would be really bad.)"
    stop music fadeout 1.0
    play music hifleveryday
    show hiflmc bowling surprised
    show mac earscop wolfbasic

    "On the next breath in, the shift ripples through Mackenzie's skin,"
    show mac cop basic
    "Golden eyes bleeding back to green as the ears disappear, fangs and claws suddenly sheathed."

    "She's just the sheriff again, like nothing happened at all."
    show hiflmc bowling happy
    mcmac "I know you're used to it, but I don't think I'll ever stop being impressed by that."
    show mac cop smirk
    "Her hands relax around the steering wheel, a smile curving her lips."

    ma "Thanks."
    show mac cop happy
    ma "It's a lot easier now than when I was nineteen, that's for sure."
    show hiflmc bowling surprised
    "(Nineteen?!)"
    show hiflmc bowling sarcastic
    "(Hi, welcome to adulthood, you're a werewolf now.)"
    show hiflmc bowling sad
    mcmac "So you're okay?"

    ma "We're both in one piece. I'm just fine."
    show mac cop smirk
    ma "Let's get inside and off the street."
    scene bg bowling_cosmic at bg
    show hiflmc bowling basic at left3
    show mac tank basic at right3
    "I expected Mackenzie to take me to the police station instead of the bowling alley, but she had to leave her uniform shirt in the car."

    "The back of it was shredded open from the change, and there's no easy way to cover that."
    show hiflmc bowling surprised
    mcmac "Do you want to talk to Razi or-!"
    show mac tank basic at right1
    ma "No, I want to talk to you."

    "It's cosmic happy hour, so the lights are on and spinning overhead."
    show bg bowling_arcade_cosmic at bg
    "They cast us in a constant neon flux as Mackenzie leads me back past the bar and to the arcade."
    stop music fadeout 1.0
    play music hiflliteromance
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    "She corners me back there by the machines, stealing a glance over her should to make sure we're alone."
    hide mac
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    mcmac "What's going on?"
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "Tell me the chance of your boss coming out of the back to interrupt us."
    hide mac
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    mcmac "Um-!"
    show hiflmc bowling_cu basic_cu
    mcmac "Not very high, I don't think. Unless a customer comes in."
    hide hiflmc
    show mac tank_cu smirk_cu at mac_cu
    ma "Good."
    hide mac
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(What does she want with me?)"
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    "Mackenzie reaches up to brush a few strands of hair back behind my glasses, her other hand pressed against the wall over my shoulder."

    "I'm not boxed in, not quite, but it's close enough to leave me breathless."

    "She leans forward, lips inches from mine, and my throat goes dry as green eyes sweep across my face, openly curious."
    hide mac
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    mcmac "Mackenzie..."
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    ma "I had to make sure you were really okay."

    ma "You smell like her, but there's no blood. No signs of a change."
    hide mac
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Right. Of course.)"
    show hiflmc bowling_cu blush_cu
    "(Then why is she close enough to kiss me?)"
    show hiflmc bowling_cu happy_cu
    mcmac "You going to take care of me this way every time another werewolf shows up?"

    mcmac "I could get used to this sort of attention."
    hide hiflmc
    show mac tank_cu happy_cu at mac_cu
    "I'm expecting her to pull back or tell me I'm wrong, but Mackenzie chuckles."

    "It's a warm sound, thick enough to bottle, and I wish she could do it again."
    show mac tank_cu sad_cu
    ma "I owe you an explanation."

    ma "I've owed it to you since the full moon."
    hide mac
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    mcmac "Is this about keeping things a secret? Everyone here knows you're a werewolf."
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "They do."
    stop music fadeout 1.0
    play music mackenziehunt
    show mac tank_cu sad_cu
    ma "What they don't know--and don't need to know--is that I'm an alpha."
    hide mac
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    mcmac "A what? Is that like a different species of werewolf or something?"
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "No. It's just genetic, as far as I can tell."

    ma "Some people are born with curly hair."

    ma "Some have the perfect proportions for certain sports."
    show mac tank_cu sad_cu
    ma "And some werewolves are alphas."

    ma "We're only born, not made."

    "She sounds so serious, but I'm not exactly sure what the problem is."
    hide mac
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    mcmac "That doesn't sound like a bad thing."
    show hiflmc bowling_cu sad_cu
    mcmac "Why are you keeping it from everyone."
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    ma "Because if my family knew, it would mean certain obligations."

    ma "And if the wolves next door in Chicago knew, I'd get dragged up in front of them and asked why I've kept my mouth shut for so long."

    ma "We're rare, [genericfn]."

    ma "Only alphas can form pack bonds, and those bonds hold our society together."
    hide mac
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    mcmac "Are you the only one here?"
    hide hiflmc
    show mac tank_cu basic_cu at mac_cu
    ma "In this state? Yeah."

    ma "I mean, I'm the first to be able to shift inside my family since my great-grandparents."
    $menuhideborder = True
    hide mac

    menu mace6c2:
        "A. So you wouldn't have a choice.":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            mcmac "So you wouldn't have a choice but to take the lead?"
            hide hiflmc
            show mac tank_cu sad_cu at mac_cu
            ma "More likely than not."
            show mac tank_cu basic_cu
            ma "The worst thing is my mom and dad would probably be real proud."
        "B. I had no idea.":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            mcmac "I didn't have a clue, Mackenzie."

            mcmac "I mean, I can't really tell werewolves apart."
            hide hiflmc
            show mac tank_cu sad_cu at mac_cu
            ma "No, but you saw how I changed. My behavior, my personality..."
            show mac tank_cu basic_cu
            ma "It's all a part of that."

        "C. But that sounds awesome.":
            $menuhideborder = False
            show hiflmc bowling_cu happy_cu at hiflmc_cu
            mcmac "But that sounds awesome."
            mcmac "You're not just a werewolf, but the rarest kind."
            show hiflmc bowling_cu sarcastic_cu
            "(Don't say a rarewolf. Don't say a rarewolf.)"
            hide hiflmc
            show mac tank_cu basic_cu at mac_cu
            ma "I wouldn't mind if it didn't threaten to upend my whole life."

    hide mac
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Wait a second.)"

    mcmac "Does that mean if Damien takes you out, he gets the whole state? Not just the town."
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    ma "... Yeah."

    ma "Chances are, the Rider alpha would divvy up the land to make the pack happy, but my family couldn't stay."

    ma "Exile at best."
    hide mac
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I don't want to know what the 'worst' option is in that equation.)"
    show hiflmc bowling_cu surprised_cu
    mcmac "But if Damien has a pack, where's yours?"

    mcmac "Can't you shine a signal up at the moon or something?"
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    ma "I don't have one."
    show mac tank_cu sleep_cu
    ma "If I did, everyone would know what I am."
    show mac tank_cu sad_cu
    ma "There's other wolves running around Indiana, but they're definitely not mine."

    "Mackenzie sounds so guilty, eyes averting away from mine until I reach out to take her hand."

    "I squeeze tight and she sighs, giving a small squeeze back."

    ma "I just want to protect the people I care about."

    ma "Being in command is something else."
    hide mac
    stop music fadeout 1.0
    play music hiflliteromance
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    mcmac "You're not really alone, you know."
    hide hiflmc
    show mac tank_cu surprised_cu at mac_cu
    ma "What do you mean?"
    hide mac
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    mcmac "You said this was werewolf business, but come on."

    mcmac "Would Razi really leave you to challenge an entire pack alone."

    mcmac "JD's been in more fights than I can count, and Diego's ancient."

    mcmac "I bet he'd scare the hell out of them."
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    ma "That's not exactly a pack."
    hide mac
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    mcmac "It doesn't have to be, Mackenzie. It's help."

    mcmac "You're not weak to be asking for it. I'm here for you too."
    hide hiflmc
    show mac tank_cu sleep_cu at mac_cu
    "Mackenzie straightens up, pensive for a long moment before she nods."
    show mac tank_cu basic_cu
    ma "You're right, [genericfn]."
    show mac tank_cu happy_cu
    ma "Thank you."
    show mac tank_cu surprised_cu
    "I'm about to ask Mackenzie another question when her phone rings."

    stop music fadeout 1.0
    play music hiflgetitdone
    hide mac
    hide hiflmc
    show hiflmc bowling sad at left3
    show mac tank angry at right3
    "She holds up a finger to have me wait and answers it, tensing up after the first few words."

    ma "What happened? When?"

    ma "Deputy, you've got to slow down."
    show mac tank surprised
    "Green eyes go wide."

    ma "My radio? It's..."

    ma "Shit, it's in my car. I'll be right there, just hang tight."
    show mac tank basic
    "She hangs up and tosses the phone in  her pocket, moving to leave."

    "I run to catch up, not wanting to lose track of Mackenzie."

    mcmac "Hey, what's going on?"
    show mac tank angry
    ma "We need to get across the street."
    scene bg main_day at bg
    show hiflmc bowling surprised at centre
    "Mackenzie’s out the door before I can ask why, but the reason is clear the second I step out onto the sidewalk."

    "The window in the front of the sheriff's office is shattered, glass everywhere, and I can see desks overturned inside."

    "Several people are warily gathering around the edge of the mess."

    "But they move when Mackenzie walks by, looking scared but offering respectful greetings."

    "When I step around the car to get closer, it’s obvious the back bumper was smashed in."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Who would do this in broad daylight?! There are people everywhere.)"
    hide hiflmc
    show mac tank angry at right4
    show hiflmc bowling surprised at left4
    ma "Hey, this is now an active crime scene."

    ma "I'm sure what just happened is worrying for a lot of you, but I need everyone to back up."

    ma "Unless you're a witness, go back to your business."
    $sidecharone = "Deputy"
    hide hiflmc
    hide mac
    show elmer casual basic at centre


    sid1 "Sheriff!"

    "The deputy limps out of the cracked front door, holding one of his shoulders."

    "A dark stain is seeping through the sleeve of his uniform, and I'm pretty sure it's not sweat."
    show elmer casual basic at right5
    show mac tank surprised at left5
    ma "Jesus. Are you alright?"

    sid1 "I don't know."
    sid1 "I don't even know what just happened."
    show mac tank sad at centre
    "Mackenzie moves to stand in front of the deputy, looking him right in the eyes."

    "I remember what she said about her deputies being just out of college, and seeing his fear, I can believe."
    hide mac
    hide elmer
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(The guy definitely isn't any older than me.)"
    hide hiflmc
    show mac tank sad at left3
    show elmer casual basic at right5
    ma "Start from the beginning deputy?"

    sid1 "I was doing paperwork at my desk when something hit the window."
    sid1 "First thing I thought it was a bird or something, but I look up and someone's slamming their first right into it."
    sid1 "I get up to go and ask what the hell he's doing, except the next punch shatters the whole window."
    sid1 "That stuff's supposed to hold up against a car, Sheriff."

    sid1 "It doesn't make any sense."
    show mac tank basic
    ma "We'll figure that out later. Tell me what happened next."

    sid1 "The guy had some friends with him."

    sid1 "They came in through the window and went right for me."

    sid1 "Pinned me under my own desk."
    sid1 "It was almost crushing my shoulder."

    sid1 "I heard them making a royal mess bit I couldn't get up."
    hide mac
    hide elmer
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(He's here now. Poor guy probably froze up.)"
    hide hiflmc
    show mac tank sad at left3
    show elmer casual basic at right5
    ma "Did they take anything?"

    sid1 "Hell, Sheriff, it would be easier to make a list of what they didn't take."
    sid1 "One of the case file drawers is missing."
    sid1 "We're missing evidence, criminal records..."
    hide elmer
    show mac tank basic at centre
    "Mackenzie’s face transforms into a cold, controlled mask, but I know exactly what she’s thinking."

    "Only Damien and his pack could be responsible for this."
    hide mac
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(The question is why? If they’re not from here, what good would all those files do?)"
    hide hiflmc
    show mac tank surprised at left3
    show elmer casual basic at right5
    sid1 "I tried to radio you when I was under the desk, Sheriff, but you never answered."

    sid1 "Where were you? The car's right out front."

    sid1 "And you're... not even dressed for work."
    hide mac
    hide elmer
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Of course Mackenzie would hire someone observant.)"

    "(Good job, dude. You'll make detective as long as your boss isn't outed as being a werewolf.)"
    hide hiflmc
    show mac tank angry at centre
    "I expect her to have an explanation at the ready, but Mackenzie’s shoulders are locked up, jaw so tight I’m not sure she can speak."
    hide mac
    $menuhideborder = True


    menu mace6c3:
        "A. Help Mackenzie out." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc bowling happy at left4
            show elmer casual basic at right4
            mcmac "She was helping me out."

            "The deputy blinks, turning to look at me as if he just noticed I was here."

            sid1 "You? With what?"
            show hiflmc bowling angry
            mcmac "I'm [genericfn] [genericln]. My sister went missing the other night."
            show hiflmc bowling basic
            sid1 "Grace, right?"

            sid1 "I thought we couldn't look into that yet, sheriff."
            hide hiflmc
            hide elmer
            show mac tank basic at centre
            "Mackenzie snaps out of her stasis, an authoritative mask falling back across her eyes."

            ma "Let's take this inside."
            scene bg hifl_sheriff at bg
            show mac tank basic at left4
            show elmer casual basic at right4
            ma "A girl went missing on my watch, deputy."

            ma "You think I'm not keeping an eye out just because of regulations."

            "The look makes his posture straighten up, even though the deputy winces right after his shoulder shifts."

            sid1 "Of course not, sheriff."

            sid1 "I think you've escorted every tipsy driver we see home for the last five years."
            hide mac
            show hiflmc bowling sad at left4
            mcmac "There was a rumor my sister was out by the lake so we went looking for her."

            mcmac "I was so worked up over not finding Grace that Sheriff Hunt took me across the street to cool down a little bit."
            hide elmer
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(Also a werewolf jumped me and that was super terrifying, but let's leave that highlight out.)"
            show hiflmc bowling sad at left4
            show elmer casual basic at right4
            sid1 "Right. You've got a job there, don't you?"

            "I nod and he nods back, muttering something under his breath before smiling a little."

            sid1 "I shouldn't go crying to my boss when I signed up for a badge, huh?"
            hide hiflmc
            show mac tank sad at left4
            ma "It's alright to get scared, deputy."

            ma "What matters is what you do with it."
            show mac tank happy
            ma "Now let me take a look at that arm so I can send you home and have you rested up in the morning, alright?"
            show mac tank basic
            "She directs the deputy into one of the still-upright chairs before disappearing through the ruins of the office,"

            "Coming back a moment later with a first aid kit."

            "When Mackenzie opens up his sleeve, there's a nasty cut underneath, but he grins and beard it while she cleans him up."

            ma "Get on out of here. I'll clean things up."

            sid1 "Are you sure?"
            show mac tank smirk
            ma "You better get moving if you want that leave paid for, son."
            hide elmer
            show mac tank sad at centre
            "That's all it takes to have him scrambling out of the office, and Mackenzie sighs once he's gone."

            "I can't imagine how stressful this is for her, much less how long it's going to take to handle the mess."
            hide mac
            show hiflmc bowling_cu happy_cu at hiflmc_cu
            "(At least that part I can help with.)"
            show mac tank sad at left4
            show hiflmc bowling basic at right4
            mcmac "Do you have a broom somewhere?"

            ma "Utility closet. But I need to set all the furniture up again."

            ma "Otherwise we'll just end up pouring more glass onto the floor."
            hide mac
            show hiflmc bowling basic at centre
            "I go to fetch the broom while Mackenzie fixes the desks,"
            hide hiflmc
            show mac tank angry at centre
            "But when I come back, she's holding an empty file drawer in her hand, the side dented in."

            ma "Goddamn it."
            show mac tank angry at left4
            show hiflmc bowling surprised at right4
            mcmac "Mackenzie?"

            ma "Everything that was taken was mine. He must have known by scent."

            ma "This wasn't about scaring the local cops. It was hiking his leg on my lawn."

            "Mackenzie sets the drawer down on top of one of the shelves, but from the tremble in both arms, I can tell she wanted to throw it."
            show hiflmc bowling sad
            mcmac "I'm sorry."
            show mac tank sad
            ma "Don't be sorry. You stood up for me when you shouldn't have had to do."

            ma "This isn't your mess to take care of."
            show hiflmc bowling basic
            mcmac "Yeah, it is."
            show hiflmc bowling sarcastic
            mcmac "Even if Grace wasn't missing, I don't want asshole werewolves taking over the town."
            show hiflmc bowling sad
            mcmac "I don't think anyone wants that. So let me watch over your back."
            show hiflmc bowling happy
            mcmac "I'll even howl at the moon a little if it makes you feel better about the formalities."
            show mac tank surprised
            "Mackenzie raises a brow."

            ma "Howling is a terrible idea. Wolves aren't native to this state, remember?"
            show hiflmc bowling sad
            mcmac "Right."
            stop music fadeout 1.0
            play music hiflsad
            hide mac
            show hiflmc bowling sad
            "The joke falls flat and I start busying myself with the broom, trying to get the mess out from under Mackenzie's desk first."

            "Once I dumped out a pan of glass, I glance up at her again."
            hide hiflmc
            show mac tank sad at centre
            "There's a look on Mackenzie's face I've never seen before as she stares out past the destroyed window, sorrow twisted up in the mix with pain."

            "It's like someone's ripped her heart out, to the point that she can't even be angry."
            hide mac
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(What would have happened if she hadn't told me she was an alpha?)"

            "(Would we have been able to stop Damien? Would it have never happened?)"
            hide hiflmc
            show mac tank sad at centre
            "Mackenzie's boots crunch against glass as she makes a whole circle through the office."

            "A grim mood settles over the room as she crouches down and picks up a little shred of leather."

            "I recognize the color."
            hide mac
            show hiflmc bowling_cu angry_cu at hiflmc_cu
            "(It must have come off Damien's jacket when he came in through the window.)"
            show mac tank sad at left4
            show hiflmc bowling sad at right4
            ma "This is only the beginning, isn't it?"
            show mac tank angry
            ma "He'll burn this whole place down to the ground if that's what it takes."

            mcmac "We'll find a way to stop him."
            ma "I will."
            show hiflmc bowling surprised
            mcmac "But I-!"
            show mac tank sad
            ma "I know what you said, and I appreciate it, but this..."

            "Mackenzie gestures back and forth between us, as if that explains it all."

            ma "I have to protect everyone here. And I need to get your sister back."

            ma "Right now my focus has to be on that, not playing buddy cop. Okay?"
            show hiflmc bowling sad
            "My heart sinks."

            "Mackenzie doesn't have to take all this on herself, but I think she's determined to shoulder the whole load, even if it crushes her."

            mcmac "..."
            show hiflmc bowling happy
            mcmac "Needs of the many, huh?"
            show hiflmc bowling sad
            "I don't even get a smile back. Ouch."
            ma "Something like that."

            ma "Go home, [genericfn]."

        "B. Stay quiet instead.":
            $menuhideborder = False
            show mac tank basic at left4
            show elmer casual basic at right4
            ma "..."

            ma "I was working another case."

            sid1 "Which one?"

            ma "[genericln]'s. She's still missing."

            sid1 "I thought you said we couldn't touch the file on that. It hasn't been long enough."
            show mac tank surprised
            ma "I..."
            show mac tank sad
            ma "Come on, deputy, do you think I'm really going to wait when a teenage girl ups and vanishes."

            "He frowns and I swallow hard, praying the deputy doesn't try to call her out further."
            show mac tank sleep
            ma "That being said, I should have had my radio on me."
            show mac tank sad
            ma "This wouldn't have happened if I didn't."

            sid1 "... Yeah."
            sid1 "Althought I guess there's not much you could have done against six of them."
            hide mac
            hide elmer
            show hiflmc bowling_cu happy_cu at hiflmc_cu
            "(I think he'd be surprised.)"
            hide hiflmc
            show mac tank sad at left4
            show elmer casual basic at right4
            ma "Maybe not."

            ma "Let me go see the damage for myself."

            scene bg hifl_sheriff at bg
            stop music fadeout 1.0
            play music hiflsad
            show mac tank sad at centre
            "Mackenzie's boots crunch against glass as she makes a whole circle through the office."

            "A grim mood settles over the room as she crouches down and picks up a little shred of leather."

            "I recognize the color."
            hide mac
            show hiflmc bowling_cu angry_cu at hiflmc_cu
            "(It must have come off Damien's jacket when he came in through the window.)"
            show mac tank sad at left4
            show hiflmc bowling sad at right4
            ma "This is only the beginning, isn't it?"
            show mac tank angry
            ma "He'll burn this whole place down to the ground if that's what it takes."

            mcmac "We'll find a way to stop him."
            ma "I will."
            show hiflmc bowling surprised
            mcmac "But I-!"
            show mac tank sad
            ma "I know what you said, and I appreciate it, but this..."

            "Mackenzie gestures back and forth between us, as if that explains it all."

            ma "I have to protect everyone here. And I need to get your sister back."

            ma "Right now my focus has to be on that, not playing buddy cop. Okay?"
            show hiflmc bowling sad
            "My heart sinks."

            "Mackenzie doesn't have to take all this on herself, but I think she's determined to shoulder the whole load, even if it crushes her."

            mcmac "..."
            show hiflmc bowling happy
            mcmac "Needs of the many, huh?"
            show hiflmc bowling sad
            "I don't even get a smile back. Ouch."
            ma "Something like that."

            ma "Go home, [genericfn]."

    hide mac
    hide hiflmc
    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
