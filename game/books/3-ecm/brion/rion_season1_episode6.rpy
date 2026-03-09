label rion_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_rooftop_sunset at bg with fade
    play music ecmromantic3
    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "You knew my dad?"
    hide ecmc

    show rion black_cu smirk_cu at rion_cu
    ri "He's the one who helped get me the job at D.I.V.A.A.."
    hide rion

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    "Rion looks out at the skyline thoughtfully, then back at me, his lips slightly downturned."
    ri "I'm really sorry that he disappeared."

    show ecmc jacket_v2 smile
    mcrion "Oh...thank you."
    "I give Rion a small smile, but I avoid his gaze."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(He's been missing for over a year and there's no sign of him.)"
    "(I believe he's alive, though. Half the reason I joined D.I.V.A.A. was to find him.)"
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin sad at right1plus
    "I sigh and walk over to the rooftop edge, leaning on the railing as I look out at the skyline."
    "Rion silently joins me, standing straight up beside me with his hands in his pockets."

    show ecmc jacket_v2 sleep
    "I take a deep breath, then look up at Rion."

    show ecmc jacket_v2 surprised
    mcrion "How well did you know him?"

    show rion black smile
    show ecmc jacket_v2 basic
    ri "Fairly well.After he helped me get the job, he also made an effort to make sure I was settling in well."
    "Rion rests a hand against the railing as he turns to face me."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I knew Dad was helpful towards other D.I.V.A.A. coworkers, but he rarely went into detail.)"
    "(It's nice hearing it from Rion directly.)"

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin surprised at right1plus
    mcrion "What was he like to work with?"

    show rion black smile
    "Rion smiles fondly as he looks into the distance."

    show ecmc jacket_v2 basic
    ri "He was great.This job can be really tense and difficult, but your Phoenix [genericln] always lightened the mood."
    ri "For example, there was this one employee who kept stealing everyone's food, but no one could figure out who it was."
    ri "This person always targeted sweets, so one day your dad comes in with this candied apple."
    ri "He made a big show of it and put it in the fridge. Later that day, we heard someone gagging."
    ri "It turns out that your dad had actually covered an onion in the candy."

    show ecmc jacket_v2 smile
    "I laugh and grin back at Rion."

    show rion black smirk
    mcrion "I actually remember that!"
    mcrion "I was upset he only made one candied apple that day, then he told me what it was for."

    show rion black smile
    ri "Your dad was great to work with. I always enjoyed being on his team."

    show ecmc jacket_v2 surprised
    mcrion "What was your favorite case to work on with him?"
    ri "Probably the time we went undercover as children's entertainers."
    ri "We were trying to bust a huge illegal hardware sale that was going down at a birthday party, and it was the best way in."
    ri "Your dad was dressed as a clown, and everytime I looked at him I kept laughing."

    show ecmc jacket_v2 smile
    mcrion "What were you dressed as?"

    show rion black smirk
    ri "I was supposed to be a ventriloquist. I had the dummy and everything."

    show rion black smile
    ri "I almost broke our cover a few times, but your dad was very good at smoothing things over."
    mcrion "Did my dad ever have to get you out of hot water?"
    ri "Oh, all the time."
    "Rion grins, lost in thought."

    show ecmc jacket_v2 basic
    ri "I was a bit rebellious when I first started at D.I.V.A.A. and I hated following the rules."
    ri "Your dad would often cover for me so I wouldn't get fired, but then he'd give me a warning."
    ri "One of the reasons I started toeing the line was because I didn't want to get him into trouble!"

    show rion black smirk
    "Rion leans back against the railing, his hands in his pockets, as he looks at me curiously."

    show rion black smile
    ri "So did you join up with D.I.V.A.A. because of your dad?"

    show rion black smirk
    show ecmc jacket_v2 surprised
    mcrion "Sort of. I was inspired by him, but he always encouraged me to follow my own path."

    show ecmc jacket_v2 smile
    mcrion "But Dad always made being a D.I.V.A.A. agent sound so amazing that I never wanted much else."

    show rion black smirk at left1plus:
        easein_back 0.4 left1
    show ecmc jacket_v2 blush embarrassed
    "Rion nods and turns back around, his arm lightly brushing up against mine as he looks out over the horizon."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(This is nice. For the first time, I feel like Rion actually wanted to get to know me better.)"

    show ecmc jacket_v2_cu blush_cu embarrassed_cu
    "(But maybe that's just what good trainers do?)"
    hide ecmc

    show rion black pin smirk at left1:
        pause 0.1
        easeout_back 0.4 left1plus
    show ecmc jacket_v2 pin blush embarrassed at right1plus
    "Rion's arm brushes up mine again, lingering a little longer than necessary, before he pulls away."

    show ecmc jacket_v2 -blush sad
    "Thoughts swirl around my head and I let out a sigh."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(I think I'm overthinking everything.)"
    "(Maybe Rion just wants to look out for me because he feels he owes something to my dad?)"

    show rion black pin surprised at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "Alright."

    show rion black sad
    "I turn my head as Rion moves back from the railing with a sigh."
    ri "It's time to pack it up for the day. I need to think about how we're going to approach this FDI situation."

    show ecmc jacket_v2 surprised
    mcrion "What's the plan for tomorrow?"

    show rion black smile
    ri "Meet me at Data Drip tomorrow morning at eight and we can get started."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Data Drip? That's the same cafe I saw Rion at the other day!)"

    show ecmc jacket_v2_cu smile_cu
    "(He seemed to be a regular there! Will I actually get to spend time with him inside?)"

    scene bg ecm_rooftop_sunset at bg with fade
    pause 0.2
    scene bg ecm_rooftop_night at bg with Dissolve(2.0)
    pause 0.4
    stop music
    play music ecmromantic1
    scene bg ecm_sidewalk_sunset at bg with dissolve
    pause 0.2
    scene bg ecm_sidewalk_day at bg with Dissolve(2.0)

    "The next morning, I rush towards Data Drip, my heart beating a little faster in excitement."

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(This must be Rion's favorite cafe.)"
    hide ecmc

    show rion jacket pin basic at centre
    "My heart sinks when I spot Rion leaning against the wall outside as he finishes off a donut, a coffee in his other hand."

    hide rion
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Oh...he went in without me.)"
    hide ecmc

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus, right_in
    "I try not to show my disappointment as I walk over. He looks up as I approach and pops the last bite of the donut into his mouth."

    show rion jacket smile
    ri "Hey, [genericfn]."

    show ecmc jacket_v2 smile
    mcrion "Good morning, Rion."

    show rion jacket basic
    show ecmc jacket_v2 basic
    ri "I spoke to a few people this morning to try and find out when the FDI will be arriving."
    ri "I haven't been able to get a concrete answer, so I'm not sure how much time we'll have before Gael comes and hits the brakes."
    ri "Since our time is limited, I want to go speak to Skye now and get his client list."
    "Rion continues to sip on his coffee as he talks."

    show rion jacket smirk
    ri "You know Skye, so I want you to warm him up so he gives us access."
    hide rion

    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I'm glad Rion's giving me some responsibility. It almost feels like we're actual D.I.V.A.A. partners!)"
    hide ecmc

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin surprised at right1plus
    mcrion "How did you want to approach this? We don't want Skye to run away again."

    show rion jacket smirk
    show ecmc jacket_v2 basic
    ri "We'll just need to make it clear that we don't care about any shady dealings that Skye is undertaking."
    ri "We also don't care about anyone else on the list, only the person who bought that part."

    show rion jacket basic
    "Rion drains the last of his coffee, then he removes his arm from the wall to toss the paper cup in the trash, revealing another coffee cup."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(How much coffee does Rion drink?)"
    hide ecmc

    show rion jacket pin surprised at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    "Rion looks back at the wall and his eyes widen slightly."
    ri "Completely forgot."

    show rion jacket smirk:
        linear 0.4 xoffset 65
        pause 0.2
        linear 0.4 xoffset 0
    "Rion picks up the cup and hands it to me."

    show rion jacket sad
    ri "I bought you a coffee too, but it's probably cold now. It's one of their best brews."
    "Rion looks at me apologetically as I take the cup from him."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(It would've been nice to join him inside, but I'm glad he thought about me!)"
    hide ecmc

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin smile at right1plus
    mcrion "That's alright. I'm sure it still tastes good."
    "I take a sip of the coffee and it's still a little warm."
    mcrion "Mmm...that's delicious! I think I get a hint of cinnamon."

    show rion jacket smile
    ri "Come on. You can finish that on the way."

    stop music
    play music ecmriontheme
    scene bg ecm_pawn_shop_off at bg with clockwise_wipe

    "Rion and I reach Skye's pawnshop and head inside."

    show skye casual angry at centre
    sk "Oh, you two."

    show rion jacket pin basic at left4
    show ecmc jacket_v2 pin smile at left1
    show skye casual basic at right4
    mcrion "Don't sound so excited, Skye."

    show skye casual angry
    sk "I have better things to do than deal with time-wasters like you."

    show ecmc jacket_v2 determined
    mcrion "Please. It's not like you actually have anything worth looking at."

    hide ecmc
    hide skye
    show rion jacket basic at centre
    "As I banter with Skye, Rion wanders around the store, inspecting the different tech."

    show rion jacket basic at left2
    show skye casual angry at right2
    sk "Why are you bothering me today, anyway."

    show rion jacket smirk
    ri "Nothing to worry about, just following up on some leads."
    "Rion walks over to the counter and casually leans against it."

    show rion jacket surprised
    show skye casual basic
    ri "You mentioned the other day that you sold that device to an anonymous buyer."
    ri "Do a lot of your customers purchase anonymously?"

    show rion jacket basic
    show skye casual angry at right2:
        easein 0.4 right3
    pause 0.4
    "Skye narrows his eyes at Rion and straightens up, subtly putting a little more distance between them."
    sk "Why do you want to know?"

    hide rion
    hide skye
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Rion clearly wants to ease into this.I should help.)"
    hide ecmc

    show skye casual angry at right2
    show ecmc jacket_v2 pin determined at left3
    mcrion "Skye, we're just trying to figure out if it's normal for buyers to be anonymous."
    sk "It's fairly common."

    show skye casual basic
    sk "A lot of my sales are made through the Z-net so people prefer to stay anonymous."

    hide skye
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Of {i}course{/i} Skye sells on the Z-net. I've only listed my finds on the virtu-net, but all of my stuff is above-board.)"
    hide ecmc

    show rion jacket pin basic at left2
    show skye casual basic at right2
    ri "What kind of tech do you sell on the Z-net?"
    sk "Unusual things. Items that seem to be quite rare, or not yet licensed."
    sk "It's easier to reach choice patrons on the Z-net than here in the store."
    ri "Do you keep records of all your sales?"

    show skye casual angry
    "Skye narrows his eyes at Rion."
    sk "Is that what this visit is about?"

    hide rion
    show ecmc jacket_v2 pin determined at left3
    mcrion "Skye, we could really use those records."
    hide ecmc
    hide skye

    $menuhideborder = True
    menu rions1e6c1:
        "A. Bribe Skye with hardware.":
            $menuhideborder = False

            show skye casual basic at right2
            show ecmc jacket_v2 pin smile at left3
            mcrion "If you hand them over, I'll give you the retro mp3 player collection that I found last week."

            show skye casual angry
            sk "That's not good enough. No one cares about such mundane technology anymore."

            show ecmc jacket_v2 determined
            sk "I want that Calablazer 7 that you found last week in the junkpile."
            mcrion "No! I've been looking for that forever."
            mcrion "How about the Omnibike I found last month? I've already made all the repairs."

            show ecmc jacket_v2 basic
            show skye casual smug
            sk "Hmm...you have yourself a deal."

        "B. Fluff up Skye's ego.":
            $menuhideborder = False

            show skye casual basic at right2
            show ecmc jacket_v2 pin smile at left3
            mcrion "You're known for always finding the best and most unique tech."
            mcrion "No one else would attract the same type of buyers that you do, so you're the only one that can help us."

            show skye casual smug
            "Skye smirks at me and drums his fingers on the counter."
            sk "Would you say that makes me the best scrapper in the city?"

            hide skye
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(This will be worth it if we get the records.)"
            hide ecmc

            show skye casual smug at right2
            show ecmc jacket_v2 pin smile at left3
            mcrion "Yes, Skye. You're the best scrapper in the city."
            sk "Flattery won't get you everywhere, [genericfn], but I suppose I can do you a favor just this once."

        "C. Beg.":
            $menuhideborder = False
            show skye casual basic at right2
            show ecmc jacket_v2 pin sad at left3
            mcrion "Please, Skye?"
            mcrion "You're the best lead we have! I just need this one favor."

            show skye casual angry
            sk "Hmm...I can, but it won't be free."
            mcrion "What do you want?"

            show skye casual smug
            sk "Pile C in the junkyard? Forget one and a half months. I want it to be mine for three."

            show ecmc jacket_v2 angry
            mcrion "What? No. Two max."
            sk "Two and a half."
            mcrion "Fine. We have a deal."

    show skye casual angry
    show ecmc jacket_v2 basic
    sk "You can have my records. I had nothing to do with your case, so if this helps clear my name, then I'll cooperate."
    "Skye presses a few buttons on his terminal, then hands us a small hard drive."

    show ecmc jacket_v2 smile
    "I try to suppress the huge grin that wants to spread on my face."
    mcrion "Thanks, Skye. This will be helpful."

    hide ecmc
    show rion jacket pin basic at left2
    "Rion gives a calm nod."

    show rion jacket smile
    ri "Thanks for your time, Kid."

    stop music
    play music ecmmctheme
    scene bg ecm_sidewalk_day at bg with clockwise_wipe

    "Rion and I leave Skye's pawnshop and start heading down the street."

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "Hmm...we're pretty close to the junkyard."

    show ecmc jacket_v2 smile
    "My eyes light up and I turn to Rion with a grin."
    mcrion "Ooh! Last time we were there, I noticed a {i}really{/i} cool piece of tech when I was chasing after Skye."

    show ecmc jacket_v2 sad
    mcrion "I couldn't believe someone just threw it out!"

    show rion jacket smirk
    ri "Interesting. You think it'd be worth checking out?"

    show ecmc jacket_v2 smile
    mcrion "I do! That piece of tech could be a game changer if used for the right purpose."
    ri "It's amazing what techies do with spare parts. That the kind of thing you're into?"
    mcrion "Yeah! That's part of the fun.I love to find things and adapt them for different purposes."
    "Rion stops walking and turns to face me."

    hide ecmc
    hide rion
    show rion jacket_cu smirk_cu at rion_cu
    ri "Hmm...you convinced me.I'm curious to see what you found."
    hide rion

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(It would be nice to spend a bit more time with Rion, maybe I can actually impress him for once.)"
    hide ecmc

    show rion jacket_cu smirk_cu at rion_cu
    ri "You ready to dazzle me with your expertise?"
    hide rion

    $menuhideborder = True
    menu rions1e6c2:
        "A. Impress Rion with your tech expertise." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            mcrion "Sure! I'd love to show you around!"

            stop music
            play music ecmcalmeveryday3
            scene bg ecm_junkyard_day at bg with wiperightdissolve

            "Rion and I head to the junkyard and manage to get past Oto with no issues this time."

            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin basic at right1plus
            ri "So, where's the part you saw?"

            show rion jacket basic
            "I lead Rion over to a junk pile and pull my gloves on before I start digging."

            show ecmc jacket_v2 smile
            mcrion "Hopefully it's still here...aha!"
            "I triumphantly start to yank out the piece I found until I have it in my hands."

            show rion jacket surprised
            ri "A servo?"
            "Rion scrunches his nose up in confusion."
            ri "Is there something about this one that makes it special?"
            mcrion "Yes. It's actually quite rare."

            show ecmc jacket_v2 smile at right1plus:
                easein 0.4 xoffset -70
            show rion jacket basic
            "I walk over to Rion and stand beside him, my shoulder lightly grazing his arm."

            show ecmc jacket_v2 blush embarrassed
            "I tense a little at the contact, my heart racing slightly faster, but I do my best to control my breathing."

            show ecmc jacket_v2 smile
            mcrion "See this serial number? This particular servo is over a decade old and it was a limited edition model."

            show ecmc jacket_v2 -blush surprised
            mcrion "It was used in a whole new generation of vehicles, but it was quite costly to produce, so it was phased out."

            show ecmc jacket_v2 smile
            mcrion "There's some very advanced tech in this so some scrappers believe that this model could even be improved to handle large walkers!"
            mcrion "It has so much potential so I'm looking forward to seeing what I could do with it!"

            show rion jacket smirk
            "Rion looks at me with a smirk."
            ri "So you're a big mecha fan, huh?"
            mcrion "I am. I just think technology has so many possibilities!"
            ri "So, that servo there, what else could we use it for?"
            mcrion "This would be great to power something that moves."
            ri "Could we make an office go-kart and use the servo to power that?"
            mcrion "Sure."

            show rion jacket smile
            "Rion's face lights up, then he looks around the junkyard."
            mcrion "Does anything catch your eye?"

            hide rion
            hide ecmc
            "Rion wades through a junk pile and pulls out a robot arm."

            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin smile at right2
            ri "This is interesting. I can see there's high quality parts in here, but it looks like they tried to repair it with poor quality materials."
            ri "That's probably why it's here."
            mcrion "I didn't realize you knew so much about technology?"

            show rion jacket basic
            show ecmc jacket_v2 basic
            "Rion shrugs as he tosses the arm aside and picks up a monitor."

            show rion jacket smile
            ri "I'm no expert, but I know quality."

            show rion jacket smirk
            show ecmc jacket_v2 embarrassed
            "Rion smirks at me, then takes a good look at the monitor."

            show ecmc jacket_v2 basic
            ri "It's good to know what's high end and what isn't when you try and buy things on the street. You don't want to get ripped off."

            show ecmc jacket_v2 basic at right2:
                easein 0.4 xoffset -110
            pause 0.4
            "I walk over to Rion and take a closer look at the monitor he's holding, my hand lightly brushing his."

            show ecmc jacket_v2 surprised
            mcrion "What do you think of this?"

            show rion jacket smile
            ri "I can tell the glass is extremely high quality. It could be worth something."

            show ecmc jacket_v2 smile
            mcrion "You're right. This glass is extremely high quality."

            show rion jacket basic
            show ecmc jacket_v2 sad
            mcrion "Unfortunately, I can't say the same for the monitor. This model had a lot of problems."

            show rion jacket surprised
            show ecmc jacket_v2 basic
            ri "What kind of hardware do you collect? You seem to have a lot of knowledge?"

            show ecmc jacket_v2 smile
            mcrion "I like all kinds, but I really like retro tech!"

            show rion jacket sad
            "Rion scrunches up his face in distaste."
            ri "Retro-tech? You mean the old stuff?"

            show ecmc jacket_v2 smile at right2:
                easein_back 0.4 xoffset -140
            show rion jacket smirk at left1plus:
                pause 0.2
                easein_back 0.4 xoffset -10
            "I laugh and playfully push his arm."
            mcrion "The stuff from the past is the best! It's really fascinating to see how far technology has advanced."
            "Rion shrugs, then gives me a half smile."

            show rion jacket smile
            ri "Well, if you have a collection, I'd love to see it some time."
            mcrion "That can be arranged."

            show rion jacket sad
            show ecmc jacket_v2 basic
            "Rion glances at his watch and sighs."
            ri "We've been here a bit longer that I anticipated. We really should head back to HQ."

            show ecmc jacket_v2 smile
            mcrion "I agree."

            show rion jacket basic at left1plus:
                pause 0.2
                easein_back 0.4 xoffset 30
            show ecmc jacket_v2 basic at right2:
                easein 0.4 xoffset -80
            "I start to walk, but Rion takes my arm."

            show rion jacket smile
            ri "Let me help you. I noticed you were still hobbling a bit and this pile is uneven!"

            show ecmc jacket_v2 blush embarrassed
            "Rion's hand gently grasps my forearm as he helps me get down from the junk pile."
            "I still feel his warmth when he lets go of my arm and I immediately crave his touch again."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "(I'm glad I came to the junkyard with Rion.)"
            "(I hope we get more moments like this in the near future.)"

        "B. Leave awkwardly.":
            $menuhideborder = False

            show rion jacket pin basic at left1plus
            show ecmc jacket_v2 pin embarrassed at right1plus
            "I shuffle a little awkwardly and look at the ground."
            mcrion "Ah, maybe some other time. Shouldn't we do some work?"

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(I feel a little awkward showing Rion that part of myself. What if I say something wrong and sound silly?)"
            hide ecmc

            show rion jacket pin sad at left1plus
            show ecmc jacket_v2 pin embarrassed at right1plus
            "Rion's face falls a little, but he shrugs."

            show rion jacket smile
            ri "Alright, [genericfn], but if you ever want to show off what you know, I'm interested."

    stop music
    play music ecmcalmeveryday3
    scene bg ecm_office_hq_on at bg with fade

    "Rion and I head back into the office."

    show rion black pin smirk at left2
    show ecmc jacket_v2 pin basic at right2
    ri "Alright, Hatchling, since I'm the only trainer you'll be having for a while, we're going to be doing some daily evaluations."

    show ecmc jacket_v2 embarrassed
    "My stomach knots a little as I nod at Rion."

    show rion black smile
    ri "Don't worry, it's nothing bad. But you do have room to improve."
    ri "I said it before, but don't be so focused on rules and protocols."
    ri "You don't need to follow the book to the letter."
    ri "Your people skills could also use some work."
    ri "You seemed to freeze up a little with Blythe, but you were more relaxed with Skye since you know him."
    ri "You can't let the suspects pick up on your nerves."
    mcrion "I understand."
    ri "Also, you really should be more confident in your abilities."

    show rion black smirk
    "Rion gives me a crooked smile."

    show rion black smile
    ri "You're doing a decent job, Hatchling. You just second-guess yourself a bit too much."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Rion has a point. I just don't want to screw this up!)"
    hide ecmc

    show rion black pin smirk at left2
    show ecmc jacket_v2 pin embarrassed at right2
    "I nod and look Rion in the eyes."

    show ecmc jacket_v2 smile
    mcrion "I agree. I'll work on all of that."

    show rion black smile
    ri "Good."

    show ecmc jacket_v2 basic
    ri "On a positive note, your knowledge and insights on tech have been invaluable to this case."
    ri "You're also quite good at piecing together information to come to solid conclusions."

    show ecmc jacket_v2 smile
    "My stomach starts to settle and I let out a small sigh of relief."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I'm glad I'm not doing a terrible job! I really want to impress Rion.)"

    show rion black pin smile at left2
    show ecmc jacket_v2 pin basic at right2
    ri "Finally, I think you're doing a good job rolling with the punches."
    ri "You've been dealing with a lot of turbulence taking on this role with me!"

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "My heart flutters a little as Rion grins at me, but I try not to look too excited."

    show ecmc jacket_v2_cu smile_cu -blush_cu
    "(Rion's just being a good trainer and giving me both good and constructive feedback.)"

    show ecmc jacket_v2_cu blush_cu embarrassed_cu
    "(I really need to stop reading into things...)"
    hide ecmc

    stop music
    play music ecmsuspense2
    show gael uniform glasses angry at centre, step_in
    "We're almost at Rion's office, when a muscular lady in an FDI uniform comes blazing down the hallway."
    fdia "Rion, there you are."

    hide gael
    show rion black pin angry at left2
    show ecmc jacket_v2 pin surprised at right2
    "Rion mutters under his breath, his body tensing a bit."
    ri "Oh, malware. It's Gael."

    hide rion
    hide ecmc
    show gael uniform glasses angry at centre
    ga "I need access to all your case files and documentation."
    ga "Have you already run all the victims through our database to see if they've ever been associated with other crimes?"
    ga "Have you used proper protocols to log all the evidence?"

    hide gael
    show rion black pin basic at left2
    show ecmc jacket_v2 pin surprised at right2
    "Rion turns to me and even though his expression is neutral, his eyes are knit together in annoyance."

    show rion black angry
    ri "We're lucky we got Skye's data when we did, because everything's about to grind to a halt."
    hide rion
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

