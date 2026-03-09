label mac_season2_episode3:

    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "The next few days are so quiet I can almost pretend things are back to normal."

    "Mackenzie goes on the hunt for Grace every night, but no matter what direction she searches in, there’s no sign of my sister."

    "I watch the news looking for any report that stands out, waiting and waiting."

    "(I even gave Mac one of Grace’s sheets in the hope that it would help the scent thing.)"

    lu "You want another coffee, honey?"
    mcmac "No, I’m okay."
    mcmac "Just sitting here thinking and letting it get cold. It’s dramatic."

    "Luce smiles at me, but it doesn’t quite reach her eyes."
    lu "I hate to bring this up, but Grace hasn’t come back yet, has she?"
    mcmac "No. Not yet."
    mcmac "I talked to her on the phone the other night, so I know she’s alive, but beyond that..."
    lu "She moved on."
    mcmac "No! Its-!"
    "(I can’t tell her what it’s actually about.)"
    "(‘Sorry Luce, my sister called from somewhere mysterious talking about our dead parents after being kidnapped by a werewolfs’.)"
    lu "[genericfn], it’s okay."
    lu "I did the same thing when I was about Grace’s age. Ran off, tried to put down roots elsewhere."
    lu "It didn’t take for me, but it does for some."
    mcmac "She didn’t run off with some guy, Luce."
    mcmac "He’s a jerk from Wisconsin that got bailed out the other day. Grace wasn’t with him."
    lu "But she isn’t here, either."
    lu "I’m going to have to put out a hiring sign in a day or two if she doesn’t turn up. Too old to run this place myself."
    "(Then I’ll definitely be living off one paycheck. Shit.)"
    mcmac "I know. Sorry, Luce."
    lu "It’s not your fault, girl. Just the way of things."
    "When Luce leaves to top off a truckers coffee, I pull out my phone and the little calculator app, punching in all my expenses."
    "Razi always pays me on time, but my hours have been all over the place lately."
    mcmac "Oof."
    "(I’ll have to pick up some extra shifts this week.)"
    "Guilt twists like a snake through my stomach."
    "Mackenzie's pulling a double shift with her work and hunting for Grace,"
    "but I’m going to have to spend more time rearranging pins than helping her out."
    di "[genericfn]?"
    mcmac "Fuck!"
    "Thankfully my curse doesn’t attract everyone’s attention in the diner, but I’m still surprised enough to drop my phone."
    "Diego catches it between two fingers before it hits the ground, offering it to me."
    di "Sorry. My footsteps must not be loud enough."
    mcmac "You’re pretty light on your feet, doc."
    di "It wasn’t my intention to startle you. But you looked upset."
    di "Is everything alright?"
    $menuhideborder = True
    menu macs2e3c1:
        "A. Never been better":
            $menuhideborder = False
            "(I’m embarrassed enough that he surprised me. Let’s skip the venting.)"
            mcmac "Never been better."
            mcmac "Just needed some caffeine to round off the day."

        "B. Let's go with 'complicated'.":
            $menuhideborder = False
            "(I'm super happy with Mac and miserable without my sister, so it's a real mixed bag right now.)"
            mcmac "Kind of?"
            mcmac "Everything's pretty complicated right now."

        "C. Does it look alright?":
            $menuhideborder = False
            mcmac "Do I seem alright?"
            di "...No, I suppose not."
            di "Otherwise I wouldn't have had reason to express my concern."

    "Diego reaches into his pocket and plucks out a five dollar bill, dropping it on top of the check I haven’t paid yet."
    "Before I can protest, he smiles."
    di "Don’t thank me yet. I’m stealing you away."
    mcmac "What for?"
    di "To go pick up Mackenzie. Her shift is done right about now, isn’t it?"
    mcmac "Yeah, I think so."
    mcmac "Why are you picking her up?"
    "The amusement in Diego’s expression fades, replaced by a serious but otherwise unreadable look."
    "I remember seeing it when we sat across each other before the eclipse, as he offered to take out Damien’s entire pack."
    di "There’s something I want you to see. Mackenzie should be there too."
    "(I’ve learned by now if someone like him is being vague, it means something supernatural that can’t be discussed in public.)"
    mcmac "Then let’s go."
    mcmac "We’ll catch her coming right out the front door."
    "It’s a short walk over to the office, and Mackenzie is locking up the front the moment I see her."
    "She turns at the sound of our footsteps, the serious mask she wears for work melting into a smile when our eyes meet."
    "(If she was shifted right now, I think her ears would have perked straight up.)"
    "(...Then again, if I was a werewolf, mine would have done the same.)"
    ma "Hey. You two catch dinner together at the diner?"
    di "No. I extended her an invitation."
    ma "Isn’t it supposed to be the other way around with you?"
    "Diego coughs, and his cheeks flush pink."
    "(Huh. Vampires can blush.)"
    mcmac "He said he had something to show us."
    mcmac "But it’s nice just to see you."
    ma "It’s nice to see you too."
    "Mackenzie steps forward and I find myself swept into a kiss."
    "It’s brief, but the heat behind it has me grasping at the front of her uniform shirt, and I’m still pressed close until Diego clears his throat behind us."
    di "We do have someone waiting on us."
    ma "Ahem. Let’s get going, then."
    "(I can’t even be that embarrassed. Kissing her feels too good.)"
    "I’m confused when Diego leads us to the bowling alley, and even more so when the cosmic lights are on after hours."
    "For a second, I don’t see anyone, but then Razi and JD pop up behind the table holding a cake."
    $sidecharone = "Razi and JD"
    sid1 "SURPRISE!"
    "Across the front of the cake, written in red frosting, is WE SURVIVED!"
    mcmac "Holy shit."
    mcmac "You two are ridiculous."
    "I start laughing, and for a second I can’t stop."
    "Stressed out or not, the last thing I expected was for them to throw a surprise party."
    di "It was all of us, actually."
    ma "Really?"
    jd "We thought you two deserved a night to relax after everything that happened with Damien."
    ra "I know Grace is still out there, but think of this as a new promise."
    ra "We’re going to drink, we’re going to have fun, and tomorrow the search starts anew."
    "(I have the best boss in the world.)"
    "(He’s a friend, too. They all are.)"

    "I look to Mackenzie, playfully nudging her shoulder."
    mcmac "What do you think first? Cake or alcohol?"
    ma "I’m pretty sure Razi has cake-flavoured vodka in the back."
    jd "He does, but it’s a crime against nature."
    ma "We’ll split the difference, then. You want first slice, [genericfn]?"
    $menuhideborder = True
    menu macs2e3c2:
        "A. Hand it over.":
            $menuhideborder = False
            mcmac "I so do. Hand it over."
            "Razi passes Mackenzie a cutter for the cake, and she snags me a big slice with the WE in the frosting before passing over the plate with a wink."
            ma "I'll help you work the calories off later."

        "B. No, you first.":
            $menuhideborder = False
            mcmac "No, you for first. My appetite's got nothing on yours."

            "The words come out a bit more suggestive than I meant, and when Mackenzie flashes a grin at me, my face turns red."

            "She snags a slice for herself, and I try not to think of all the other possible applications for frosting."

        "C. Let's share it.":
            $menuhideborder = False
            mcmac "Let’s share it."
            ma "That’s asking for a mess."
            mcmac "Yeah, but it’ll totally be worth it."

    "Once Mackenzie and I have taken our fill of the cake, Razi and JD do the same, and Diego even takes a small piece to be polite."

    "The unmistakable pop of a champagne bottle catches my ear, and a cold glass is pressed into my hand."

    ra "Cheers."

    mcmac "What are we drinking to?"
    jd "Whatever comes to mind."
    "I laugh, and take a long sip."

    "One glass quickly becomes several."

    "Mackenzie has me pace myself, insisting that everyone else’s tolerance is a lot higher than mine, but after a couple of hours, it doesn’t really matter."

    ma "You having fun?"

    mcmac "Between the sugar and the liquor, I think I’m floating."

    ma "Is that a good thing?"

    mcmac "It’s a very good thing. It’s my new superpower."

    "She smiles, then leans forward to kiss me. The next word against my lips, rumbling with amusement."

    ma "Congratulations, then."

    "After one more round, JD suggests that we break out the bowling pins, and everyone’s inebriated agreement sends them to set up the lanes."

    "Diego chuckles as JD balanced four pins on top of each other, and I realise something."

    mcmac "Wait, Diego. You can get drunk?"

    di "It’s called blood alcohol level, isn’t it?"

    mcmac "...Huh."

    "I lean back against Mackenzie’s shoulder, quietly pleased when her arm comes around my waist."

    "I’ve been slowly migrating into her lap, but no one else has said anything."

    jd "Alright, we need teams."

    di "I call referee."

    ra "Then I’m with you, devil-may-care."

    jd "How do you figure that?"

    "Razi looks me up and down, and I blush, trying not to giggle."

    "I don’t want to get out of Mackenzie’s lap, but if we’re playing, I have to."

    ra "Because I’m not even going to try to split those two up."

    ma "I’m in for a couple games. No promises on coordination, though."

    "She says that, then picks up the heaviest bowling ball and rolls a strike that sends JD’s meticulously arranged pins flying."

    "(We’re so going to win.)"

    di "Full points! JD, you’re up."

    "I’m about to tease them when a flash of fire brings JD’s wings to life."

    "While I’m too startled to do anything but stare, they manage to hit every pin but one, and groan at Mac’s whoop of victory."

    mcmac "Wait, why are you—!"

    jd "My eyes are better like this."

    mcmac "It’s totally cheating!"

    jd "Yeah, because Mac is holding back on her werewolf strength, I’m sure."

    ma "Full disclosure: I’m not holding back."

    "(God, she’s cute when she’s drunk.)"

    ra "Well, if we’re already dropping the glamour..."

    "Razi winks, and a wave of blue energy blurs my vision before he reappears in full djinn form, covered in silk and tattoos."

    "(Is it really a party if no one’s shirt comes off?)"

    "He manages to match Mac’s strike, leaving the next turn to me."

    "I pick up one of the lighter bowling balls and give it a go, but it veers right into the gutter."

    mcmac "Goddamn it."

    jd "Ooh, [genericfn]. Gonna make Mac carry the team?"

    mcmac "Hey!"

    di "Minus two points for mocking the opposition, JD."

    jd "Who died and made you god of bowling?"

    di "Now It’s minus three."

    "(Thanks for the backup, Diego.)"

    "Mackenzie comes over to kiss my cheek, claiming it’s for good luck before she rolls another clean strike."

    "We’re trailing in points after a couple more rounds, but JD is spending more time debating points with Diego than really playing."

    "(Do I really want to get into this?)"
    $menuhideborder = True
    menu macs2e3c3:
        "A. Sneak off to be alone with Mac." (paidchoice = "paidchoice"):
            $menuhideborder = False
            "(If they're done bowling, I'll find another way to have fun.)"

            "Running my fingers down Mackenzie's arm catches her attention, and after we lock eyes, I tilt my head over in the direction of the arcade."

            "The eagerness in her smile leaves me giddy, and I pull her by the wrist away from the lanes."

            ma "Got something to show me?"

            mcmac "Yeah. It's my favorite game."

            ma "Even better than bowling?"

            mcmac "Way, way better."

            "Once we're back by the machines, I let go of Mackenzie, but she closes the distance between us with another step."

            "My back bumps against the rounded edge of a console, her arms on either side of my head."

            "To anyone else, it might have been intimidating, but my heart's almost beating out of my chest."

            ma "Want to tell me what it's called?"

            "I tilt my head just enough for our lips to meet, prompting a slow but deep kiss."

            "I've just about lost myself in it when I come up with a really good answer."

            mcmac "Pushing your buttons."

            "Mackenzie's laugh is low and warm, so close that I can feel it."

            "I could get drunk on that sound, with the way it sends a shiver up my spine."

            ma "You're way wittier than me when you're tipsy."

            mcmac "I've got to have some kind of advantage on you."

            ma "Yeah?"
            mcmac "Yeah."

            "Another kiss steals my next thought away, and I hook my fingers in Mackenzie's duty belt, tugging to make sure she stays close."

            "(This is the kind of thing I wish I could have gotten away with as a teenager.)"
            "(Fooling around, being fearless. Not worried about what the neighbors might say.)"
            ma "I really should take you on a date sometime, you know."
            ma "Not just this."
            mcmac "Is there something wrong with this?"

            "From the way her lips meet mine, all fever and a little bit of teeth, there's not a damn thing wrong with it."

            ma "No, but I don't want you to think I..."
            mcmac "That you're hot for this but not the rest?"

            ma "Exactly."
            ma "Although I do appreciate every inch of you."
            mcmac "You haven't seen every inch of me."
            "(Yet.)"
            ma "I'm working on it."

            "There's no stopping a blush after the image that pops up in my head, but I hide my flushed face in another kiss, slipping my arms around Mackenzie's back."

            "Her hands stay braced against the machine, never presuming."

            "(We're a little too wasted to go farther than this right now, anyway.)"
            "(But that doesn't make it any less fun.)"

            ma "Where's your head at?"
            mcmac "Your hands."
            mcmac "Ahem, I mean I was thinking about your hands."

            "Mackenzie raises a brow, caught between amusement and interest, and I shush her with a look."
            mcmac "Now you have to tell me what you were thinking about."
            mcmac "Either that, or I sink through the floor in embarrassment."

            ma "No way."
            ma "I come up with the worst jokes in my head when I drink."

            "(Okay, now I have to hear this.)"
            mcmac "I'm liiiistening."

            "Her face heats up, and Mackenzie tries to dodge locking eyes with me for a second before she mumbles something under her breath."
            mcmac "Didn't catch that, Mac."
            ma "I was wondering how to get your high score."
            "I try to hold in my laughter, but a few giggles escape me anyway."
            mcmac "You are such a nerd."
            mcmac "I can't believe I never knew this about you."
            ma "The comic books didn't clear that up?"
            mcmac "I meant before that."
            mcmac "Before I really got to see who you are."
            "My tone gets a little softer, leaving the teasing behind. I want her to know I mean it, that I want every last piece without exception."

            "(Being with Mac has brought me into a new world, but it's a pretty great one.)"
            ma "It goes both ways, you know."
            ma "A lot of my kind think humans can't understand us at all, and vice versa."
            mcmac "What about you?"
            ma "I've learned they're wrong."

            "One hand comes down to cup my cheek, and I lean into that touch, where the soft curve of Mackenzie's palm meets the strength of her fingers."

            "(Can I just stay here forever?)"
        "B. Join the debat.":
            $menuhideborder = False
            "(I’m way better at rhetorical arguments than bowling.)"
            "(When I’m sober, at least.)"
            mcmac "Diego, you’ve already taken..."
            "I have to count on my fingers a couple of times before the math makes sense."
            mcmac "Twenty? I think."
            mcmac "Points from JD, and half of them are for backtalk."
            di "I am merely making a point of my own."
            "He chuckles to himself, and JD rolls their eyes."

            "Razi is still singularly focused on the game, rolling another ball down the lane to recover some points for their side."
            ra "It’s fine, JD. One more strike and we’re even."
            jd "It’s about the principle of the thing!"
            "I look at Mackenzie, expecting to hop into the argument—or at least play peacemaker."

            "Except she sinks back into her seat with another glass of beer before kicking her feet up."
            mcmac "Hey, Mac. Come give us a verdict."
            ma "I am off-duty right now."
            mcmac "Oh, come on. I’ll give you something good if you do."
            "She smirks at me, and the brief show of teeth sends an answering flutter through my chest."
            ma "Are you trying to bribe an officer of the law, Ms. [genericln]?"
            mcmac "I might be."
            mcmac "What happens if I was?"
            "(I don’t even remember what everyone else was arguing about anymore.)"
            ma "Why don’t you come over here and find out?"

    "The sound of the front door being flung open makes me freeze in place."

    "JD and Razi shift in a blink as a girl runs inside, pale and gaping with fear."

    "She’s young—Grace’s age—and concern cuts the edge of my buzz, snapping me right into the moment."

    unknown "I..."
    unknown "Please, I need someone’s help. They’re after me!"
    di  "Who's after you?"
    unknown "Werewolves."


    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
