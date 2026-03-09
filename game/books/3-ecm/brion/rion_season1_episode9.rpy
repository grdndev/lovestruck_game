label rion_season1_episode9:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_restaurant_day at bg with fade
    play music ecmcalmeveryday4

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Rion leads me to a Korean restaurant a couple blocks away."
    "We sit down at one of the tables with several dishes spread out in front of us."

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "The physical evidence may be corrupted, but with the exception of Skye's buyer list, we've at least been able to analyze everything else."
    ri "What we know so far is that Blythe's patrons are being targeted at events like last night."

    show ecmc jacket_v2 surprised
    mcrion "Do you think it has something to do with the art theme? The use of cybernetics and AI?"

    show rion jacket sad
    show ecmc jacket_v2 sad
    ri "I'm sure there has to be some connection."

    show rion jacket basic
    show ecmc jacket_v2 basic
    ri "Once we have Skye's buyer list, we can use D.I.V.A.A.'s programs to figure out who's been buying the kind of components you found on that body."

    show ecmc jacket_v2 smile
    mcrion "That sounds like a start."

    show rion jacket smirk
    show ecmc jacket_v2 basic
    "Rion takes a bite of his food, chewing thoughtfully."

    show rion jacket basic
    ri "It's a start, but I still feel like we're missing a crucial piece to the puzzle."

    show rion jacket sad
    "Rion sighs and drops his fork down on his plate with a light clatter."
    ri "It's frustrating because this is the closest I've ever gotten to cracking this thing."
    ri "But the FDI taking over has caused a real glitch in the system."

    show ecmc jacket_v2 sad
    mcrion "Why do you think they're taking over?"

    show rion jacket basic
    show ecmc jacket_v2 basic
    ri "Interesting that you ask that."
    "Rion picks his fork back up and starts absentmindedly pushing his food around the plate."

    show rion jacket sad
    ri "At first I thought this was just an inter-agency turf thing, but from some of the things Gael has said, I think something else is going on."

    show ecmc jacket_v2 sad
    mcrion "Something more dangerous?"
    ri "Exactly."
    ri "If we could figure out why the FDI took over, that may help our understanding of the case."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "I take a bite of my own food as I mull over Rion's words."

    show ecmc jacket_v2_cu determined_cu
    "(One way or another, I'm going to get that information so we can keep the case moving!)"
    hide ecmc

    show rion jacket pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    "Rion takes a few more bites of his food, then looks at me."

    show rion jacket smile
    ri "What do you think of this place? I should have asked if you liked Korean food before taking you here."

    show ecmc jacket_v2 smile
    mcrion "I think it's great! I've never been here before, but I've walked past several times and always wondered what it's like."
    mcrion "The food is great and I really like the atmosphere."
    ri "This is actually one of my favorite restaurants in the area."

    show rion jacket smirk
    show ecmc jacket_v2 basic
    "Rion points at a beef dish with his fork."
    ri "I haven't been able to find a place that makes bulgogi quite like this anywhere else in LA."

    show rion jacket smile
    "Rion scoops some more food onto his plate as a soft smile spreads across his face."
    ri "When we first moved here, my mom insisted on finding bulgogi like back home."
    ri "We must have tried almost every Korean restaurant in the county until we found this place."

    show ecmc jacket_v2 smile
    "I can't help but smile as Rion's face lights up with the memory."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(That's adorable. It's nice hearing about his past.)"
    hide ecmc

    show rion jacket pin smirk at left1plus
    show ecmc jacket_v2 pin smile at right1plus
    mcrion "It's not quite the same, but my family used to love hunting down our favorite food trucks all over the city."

    show ecmc jacket_v2 surprised
    mcrion "One time, one of our favorites wasn't parked where it usually was and we drove around like half the county just to find it."

    show ecmc jacket_v2 smile
    mcrion "We made it right before it closed!"
    "Rion chuckles then looks at me curiously."

    show rion jacket smile
    ri "What was the food truck?"
    mcrion "Cosmic Icecream Sandwiches! It's my absolute favorite dessert truck."
    "Rion's eyes light up, enthusiastically."
    ri "I love that one!"
    ri "I'm not the biggest fan of sweet things usually, but I'll make an exception for those sandwiches every time."

    hide rion
    hide ecmc
    "Rion and I polish off the rest of the food, then Rion leans back in his chair with a satisfied smile."

    show rion jacket pin smile at left1plus
    show ecmc jacket_v2 pin smile at right1plus
    ri "There. That was the stress relief I needed."
    mcrion "I agree. This was a good call!"

    hide rion
    hide ecmc
    "The waitress comes with our bill. I try to grab the check, but Rion smoothly grabs the folder from the waitress and slips a card inside it."

    show rion jacket pin smirk at left1plus
    show ecmc jacket_v2 pin surprised at right1plus
    "As the waitress walks away, I look at Rion in shock."
    mcrion "You paid? I can pay you back! Let me cover tip at least."
    "Rion smirks at me and shakes his head."
    ri "I didn't pay- D.I.V.A.A. did. I have a company card."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Oh...for a moment this almost felt like a date. I forgot that we're really here as colleagues.)"
    hide ecmc
    "The waitress returns with Rion's card and after he puts it away, he checks the time."

    show rion jacket pin smile at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "You know, it's actually a bit earlier than I thought and the Cosmic Icecream Sandwich food truck is nearby."
    ri "Why don't we grab dessert?"

    show ecmc jacket_v2 sad
    "Rion grins at me, but I feel a pang in my chest."

    show rion jacket sad
    "My face must fall because Rion's smile drops, and he looks at me in concern."
    ri "Is something wrong?"
    mcrion "It's just...Cosmic Icecream Sandwiches is one of my favorites partly because my dad used to visit all the time."
    mcrion "I haven't checked it out since he disappeared."
    "Rion reaches across the table and lightly places his hand on top of mine."

    hide ecmc
    hide rion
    show rion jacket_cu smile_cu at rion_cu
    ri "All the more reason to check it out, then. Let's build some new, good memories!"
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Is D.I.V.A.A. going to pay for that too?"
    hide ecmc

    show rion jacket_cu smirk_cu at rion_cu
    "Rion chuckles and shakes his head, his hand still lightly on top of mine."

    show rion jacket_cu smile_cu
    ri "No, this will be my treat. What do you say?"
    hide rion

    $menuhideborder = True
    menu rions1e9c1:
        "A. Let Rion treat you to dessert." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            mcrion "Dessert sounds great! Let's make some new memories."

            scene bg ecm_sidewalk_day at bg with wiperightdissolve
            stop music
            play music ecmromantic1

            "A few minutes later, Rion and I arrive at the Cosmic Icecream Sandwich truck and join the line."

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            mcrion "I can smell the donuts from here! I love how they use different desserts to make the sandwich 'bread'."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu sleep_cu at ecmc_cu
            "I close my eyes and inhale the aroma, then turn to Rion, feeling a little conflicted."
            hide ecmc

            show rion jacket pin basic at left1plus
            show ecmc jacket_v2 pin sad at right1plus
            mcrion "I'm happy to be back, but being here reminds me of coming with my dad."
            "The line moves and Rion and I shuffle forward."

            show rion jacket smile
            ri "How did you usually do this with your dad? Did you have a routine?"

            show rion jacket smirk
            show ecmc jacket_v2 surprised
            mcrion "We did, actually!"
            mcrion "We'd go every Friday night that Dad wasn't too busy, so that was usually just once or twice a month."

            show ecmc jacket_v2 smile
            mcrion "It still meant a lot that he could find the time in his schedule to take me here."
            mcrion "Then we'd each order our sandwiches, but he'd always let me have the first bite of his."

            show rion jacket smile
            ri "Did your dad have a favorite?"
            mcrion "He did. He'd get half a donut on the bottom, vanilla ice cream with a drizzle of maple syrup, then a waffle on top!"
            ri "That sounds like a great creation!"
            mcrion "It is. Dad pretty much got the same thing every single time!"
            mcrion "I like to mix my orders up."

            hide rion
            hide ecmc
            "The line moves again and Rion and I end up at the front."

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            mcrion "What are you going to order?"

            show rion jacket smile
            ri "I think I'll get my usual favorite."
            "Rion turns to the window."

            hide ecmc
            hide rion
            show rion jacket_cu smile_cu at rion_cu
            ri "I'll take an unglazed donut with a scoop of salted caramel ice cream and some pretzel pieces in between."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "Today I think I'll get a chocolate donut with sprinkles with a scoop of toffee ice cream and some fairy floss fluff!"
            hide ecmc

            sandwichmaker "Perfect. Will that be all today?"

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "Yes-"
            hide ecmc

            show rion jacket_cu smile_cu at rion_cu
            ri "Actually, no."
            hide rion

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v2 pin surprised at right1plus
            "I look at Rion in confusion."

            show rion jacket smile
            ri "Could I also half a donut on the bottom, vanilla ice cream with a drizzle of maple syrup, then a waffle on top?"

            hide rion
            hide ecmc
            sandwichmaker "Coming right up."

            show rion jacket pin smirk at left1plus
            show ecmc jacket_v2 pin surprised at right1plus
            "The cashier heads off to make our creations and I look at Rion in shock."
            mcrion "Why did you order Dad's favorite?"

            show rion jacket smile
            ri "Since this is something you used to do with your dad a lot, I think we should still include him."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(That's sweet...)"
            hide ecmc

            "The cashier comes back with our creations and Rion pays the bill."

            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            ri "Come on, let's grab a clean spot on the curb."

            hide rion
            hide ecmc
            "Rion and I take a seat among a dozen other people eating dessert. Rion places Dad's order between us."

            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "I look down at it, feeling a bit conflicted."
            "(Rion's treating Dad like he's dead and we need to honor his memory.)"
            "(It's kind of sweet...but I still believe he's alive. If I knew where dad was right now, I could pick this up and bring it to him...)"
            hide ecmc

            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin basic at right1plus
            ri "You should take the first bite of your dad's, just like old times."
            "Rion's voice pulls me from my thoughts and I look up at him to see him smiling encouragingly at me."

            show rion jacket smirk
            show ecmc jacket_v2 smile
            mcrion "You're right. I should honor that tradition."
            "I pick dad's sandwich up and take a bite, then I offer it to Rion."
            mcrion "Would you like a bite?"

            show rion jacket smirk
            show ecmc jacket_v2 basic
            "Rion accepts the sandwich and takes a bite, chewing thoughtfully."

            show rion jacket smile
            ri "Not bad. The maple syrup makes it a bit sweeter than I'd like, but overall the flavors are simple and classic."
            "Rion places Dad's sandwich back down and takes a bite of his own."
            ri "I need the saltiness of these pretzels to balance out the sweetness of everything else!"

            show rion jacket smirk
            show ecmc jacket_v2 smile
            mcrion "Well, don't try mine then. It's super sweet, but not as much as that sugar coffee you bought me!"

            show rion jacket smile
            ri "I still feel bad about that!"
            "I laugh and shake my head before taking a bite of my ice cream sandwich."

            show rion jacket smirk
            show ecmc jacket_v2 basic
            ri "You know, your dad used to take the team out to food trucks a lot, but he never took us to this one."

            show rion jacket smile
            ri "Maybe it's because he reserved this for you?"

            show ecmc jacket_v2 smile
            mcrion "He did. He always told me where he took the team for food and he'd reassure me that this truck is our spot."
            "I lick some ice cream off my lip and grin at Rion."
            mcrion "Dad always said it wouldn't be the same going here without me."
            ri "Well, I'm sure you probably feel the same way, but I hope you're still enjoying being here with me!"

            hide ecmc
            hide rion
            show rion jacket_cu smirk_cu at rion_cu
            "I lock eyes with Rion and smile at him, my heart thumping a little faster."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "I definitely am."
            hide ecmc

            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin smile at right1plus
            "Rion and I continue talking as we finish off our ice cream sandwiches."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(I really appreciate Rion bringing me here. It's been a lot of fun!)"
            hide ecmc

            "Finally, both Rion and I finish off our treats and also Dad's, then Rion takes the packaging and throws it in the recycling bin."

            show rion jacket pin smile at left1plus
            show ecmc jacket_v2 pin basic at right1plus
            ri "Come on, we really should get back to the office now."

        "B. Go back to work.":
            $menuhideborder = False
            show rion jacket pin basic at left1plus
            show ecmc jacket_v2 pin basic at right1plus
            mcrion "I really think we should get back to the office."
            show ecmc jacket_v2 smile
            mcrion "I'm anxious to get started!"
            show rion jacket sad
            "Rion's face falls and he pulls back in his seat, removing his hand from mine."
            show rion jacket basic
            ri "Alright, I guess you're right."
            show rion jacket smirk
            ri "I really would like to check that food truck out with you sometime. All you have to do is ask."

    scene bg ecm_office_hq_on at bg with fade
    stop music
    play music ecmtense3
    "A little later that day, I'm in the office studying the D.I.V.A.A. procedure models at my desk while Rion is in his office, working on finding new leads."

    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Rion told me to take it easy for the rest of the day, but I hate feeling useless.)"

    show ecmc nojacket_v2_cu determined_cu
    "(I wonder if there's a way to get more information about the FDI takeover.)"
    hide ecmc

    stop music
    play music ecmcalmeveryday4

    show korin nojacket pin basic at centre, step_in
    show bird normal at centre:
        xoffset 140 yoffset 75
    "Just as I'm about to turn to my computer, Korin walks over with Baby Bird on her shoulder."

    show korin nojacket smile
    ko "Hey, [genericfn]. I thought I'd come check in on you."
    ko "How's everything going?"

    show ecmc nojacket_v2 pin sad at left1plus
    show korin nojacket basic at right1plus
    show bird normal at right1plus
    mcrion "Not too bad, but did you hear what happened to Rion's case evidence?"

    show korin nojacket sad
    "Korin looks at me, sympathetically."
    ko "I did. I'm sure Rion must be feeling awful, this case means a lot to him."

    show korin nojacket smile
    ko "Did you at least manage to get any new evidence at the art show?"

    show ecmc nojacket_v2 smile
    mcrion "We may have found a lead."
    ko "That's great!"

    show korin nojacket sad
    ko "It was nice seeing you there. I'm sorry we didn't really get a chance to chat, but I knew you were working."

    show ecmc nojacket_v2 surprised
    mcrion "Do you usually go to events like that?"

    show korin nojacket smile
    ko "Oh, occasionally. I don't go as often as Anton, though! He's a big fan of that type of exhibition."

    show ecmc nojacket_v2 basic
    show korin nojacket basic
    "Korin looks over at my computer."

    show korin nojacket smile
    ko "What are you working on now?"

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(It probably can't hurt to be honest with Korin. I think I can trust her.)"
    hide ecmc

    show ecmc nojacket_v2 pin sad at left1plus
    show korin nojacket pin basic at right1plus
    show bird normal at right1plus:
        xoffset 140 yoffset 75
    mcrion "Well, I'm supposed to be studying D.I.V.A.A. procedures, but I wanted to look into something else."

    show ecmc nojacket_v2 basic
    "Korin sits down beside me, and I look around before lowering my voice."

    show ecmc nojacket_v2 determined
    mcrion "Rion and I suspect the FDI are taking over the case because of something really bad. I want to find out what that reason is!"

    show korin nojacket sad
    ko "How do you plan on doing that?"

    show ecmc nojacket_v2 sad
    mcrion "I'm not sure."

    show ecmc nojacket_v2 basic
    show korin nojacket smile
    ko "Well, let me give you a hand. I'm not sure how we can figure that out, but you need to make sure you tread carefully when it comes to the FDI."

    show ecmc nojacket_v2 sad
    show korin nojacket basic
    mcrion "I considered just submitting a routine information request, but I doubt that will go through."

    show korin nojacket sad
    ko "If Gael won't tell you what's going on, there's no way that request will be approved."

    show ecmc nojacket_v2 surprised
    mcrion "Well, D.I.V.A.A. has access to some FDI systems, right?"
    hide ecmc
    hide korin
    hide bird

    $menuhideborder = True
    menu rions1e9c2:
        "A. Search the FDI database.":
            $menuhideborder = False
            show ecmc nojacket_v2 pin determined at left1plus
            show korin nojacket pin basic at right1plus
            show bird normal at right1plus:
                xoffset 140 yoffset 75
            mcrion "We could search their database."
            mcrion "Maybe we'll find the case files."
            show korin nojacket sad
            ko "We could try, but D.I.V.A.A. has fairly limited access. I doubt this is something we'd have access to."
        "B. Just ask Gael.":
            $menuhideborder = False
            show ecmc nojacket_v2 pin surprised at left1plus
            show korin nojacket pin basic at right1plus
            show bird normal at right1plus:
                xoffset 140 yoffset 75
            mcrion "Why don't we speak to Gael again?"
            show ecmc nojacket_v2 determined
            mcrion "But instead of beating around the bush, we could just ask her outright."
            show korin nojacket sad
            ko "If Gael hasn't already told you the reason, I doubt harassing her will help."
        "C. Suggest bribery.":
            $menuhideborder = False
            show ecmc nojacket_v2 pin sad at left1plus
            show korin nojacket pin basic at right1plus
            show bird normal at right1plus:
                xoffset 140 yoffset 75
            mcrion "We could bribe an FDI employee?"
            mcrion "Or maybe one of the security bots? They might know the reason?"
            show korin nojacket sad
            ko "You know any FDI employee would be fired for accepting a bribe."

    show ecmc nojacket_v2 determined
    show korin nojacket basic
    mcrion "Ugh, this is hopeless!"

    show ecmc nojacket_v2 sad
    mcrion "I just really wanted to help Rion out. I know he's a bit bummed about the case being taken over."

    show korin nojacket smirk
    "Out of the corner of my eye I spot Korin smirking at me."
    ko "So, are you trying to find out answers for the good of the case, or for Rion?"

    show ecmc nojacket_v2 blush embarrassed
    "My face heats slightly and I do my best to keep my heart rate under control."

    show ecmc nojacket_v2 surprised
    mcrion "For the case, of course!"

    show ecmc nojacket_v2 embarrassed
    "Korin hums, but I can tell she doesn't believe me."

    show korin nojacket smile
    ko "How do you like working with Rion?"
    ko "Are you disappointed you don't get to work with the other supervisors like the rest of the trainees?"

    show ecmc nojacket_v2 -blush smile
    mcrion "Not at all! I'm really enjoying working one on one with Rion!"
    mcrion "I feel like I'm learning so much!"

    show korin nojacket smirk
    "Korin narrows her eyes slightly as she meets my gaze."

    show ecmc nojacket_v2 embarrassed
    ko "So, this is purely a professional relationship?"

    show ecmc nojacket_v2 blush embarrassed
    "I blush slightly but nod my head."
    mcrion "Of course!"

    show ecmc nojacket_v2 -blush smile
    mcrion "It just means a lot to me to be paired up with someone so experienced and who's so...cool."

    show korin nojacket smile
    "Korin smiles knowingly at me."
    mcrion "Plus it's been interesting hearing how Dad helped shape Rion's career."

    hide korin
    hide bird
    hide ecmc
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "As I mention my father, I suddenly recall an old memory."

    show ecmc nojacket_v2 pin surprised at left1plus
    show korin nojacket pin basic at right1plus
    show bird normal at right1plus:
        xoffset 140 yoffset 75
    mcrion "Wait!"

    show ecmc nojacket_v2 determined
    mcrion "I remember dad mentioning a specific contact number within the FDI."
    mcrion "Usually only FDI agents know it, but someone he worked a case with passed it on."

    show ecmc nojacket_v2 surprised
    mcrion "He basically said it was an insider line and there were no real safeguards around it. Have you heard anything about it?"

    show korin nojacket sad
    ko "I have, however, I've never used it."
    ko "How do you know the request won't get flagged and that you won't get in trouble?"

    show ecmc nojacket_v2 sad
    mcrion "I mean, won't it be similar to submitting a regular request? The worst they can do is say no!"
    ko "The FDI may not like that you're digging into matters that don't concern you, [genericfn]."

    show ecmc nojacket_v2 determined
    mcrion "Korin, I really want answers. This may be my only chance!"
    "Korin hesitates for a moment, then she nods."

    show ecmc nojacket_v2 smile
    show korin nojacket smile
    ko "Alright. I'll help you get the paperwork in order."
    ko "I guess it can't hurt."

    hide korin
    hide bird
    hide ecmc
    "Korin and I get all the request documents together and then I fire the request off from my account."

    show ecmc nojacket_v2 pin smile at left1plus
    show korin nojacket pin smile at right1plus
    show bird normal at right1plus:
        xoffset 140 yoffset 75
    ko "Well, let me know how it goes, [genericfn]. I have to get going."
    mcrion "Thanks for your help, Korin."

    show korin nojacket smile at step_out
    show bird normal at right1plus:
        pause 0.2
        parallel:
            linear 0.4 alpha 0.0
        parallel:
            easeout_back 0.4 yoffset 130
    "Korin leaves and I turn back to the D.I.V.A.A manuals just as Enver walks over."

    show ecmc nojacket_v2 basic
    show enver casual sad at right1plus, right_in
    stop music
    play music ecmcalmeveryday3
    en "Heyyyy, [genericfn]. You look stressed. Are you stressed?"

    show ecmc nojacket_v2 smile
    "I raise an eyebrow at Enver and shake my head."
    mcrion "I'm not stressed at all, Enver. I'm literally just reading instruction manuals."

    show ecmc nojacket_v2 basic
    show enver casual smile
    en "Well...I could use a coffee break. Care to join me?"

    hide enver
    hide ecmc
    show rion black pin basic at centre, left_in
    "Just then, I spot Rion walking by."

    show rion black smirk at centre
    ri "Excuse me, Enver? Where's my invite?"

    hide rion
    show ecmc nojacket_v2 pin basic at left1plus
    show enver casual smile at right1plus
    "Enver chuckles and shrugs his shoulders playfully."
    en "You can come too if you want, Rion."

    hide ecmc
    hide enver
    show rion black pin smirk at centre
    ri "As welcoming as that invitation is, I'll take you up on it."

    scene bg ecm_elysian_park_day at bg with fade
    stop music
    play music ecmromantic1

    "Rion, Enver, and I buy our coffees and head to the local park to drink them together."

    show enver casual smile at right3
    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin basic at left5
    en "This is just the stress reliever I needed!"

    show rion jacket smirk
    ri "Stress relief?"

    show enver casual basic
    "Rion snorts and raises an eyebrow at Enver."

    show rion jacket smile
    ri "What do you need stress relief for. It's not like you work hard!"

    show enver casual smile
    en "Please. I happen to work extremely hard."
    en "Maybe you just work too hard! I'm sure you've been overworking the poor hatchling here!"

    hide enver
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "I roll my eyes and playfully push Enver's arm."
    hide ecmc

    show enver casual smile at right3
    show rion jacket pin smile at left1
    show ecmc jacket_v2 pin determined at left4
    mcrion "The 'poor Hatchling' happens to be doing just fine!"

    show enver casual basic
    show rion jacket basic
    show ecmc jacket_v2 basic
    en "So, how's the case going now that the FDI has taken over?"

    show rion jacket sad
    ri "Ugh, let's just say I needed this coffee break!"

    show enver casual smile
    show rion jacket smile
    show ecmc jacket_v2 smile
    "Rion, Enver and I continue talking and laughing, and I can't help but feel a little special."

    hide enver
    hide rion
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I don't think any other Hatchlings are having casual coffee breaks with higher-level D.I.V.A.A agents!)"
    "(Rion and Enver don't treat me like a newbie, either. They both treat me like I'm part of the team.)"
    hide ecmc

    show enver casual smile at right3
    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin basic at left4
    en "So how's the dream team going?"
    "Enver looks at Rion with a smirk."
    en "I have to say, Rion. I was very surprised to hear that you asked to be stuck with just one Hatchling for the rest of the training season!"
    "Rion's face stays stoic, but I notice he shuffles a little awkwardly."

    show rion jacket smile
    ri "[genericfn] has some invaluable knowledge that helps my case."
    en "Uh huh."

    show enver casual sad
    show rion jacket basic
    "Enver turns to me and narrows his eyes."
    en "Why didn't you question it, [genericfn]? Don't you think you'd learn more by working with more supervisors?"

    show ecmc jacket_v2 determined
    "I shake my head."
    hide enver
    hide rion
    hide ecmc

    $menuhideborder = True
    menu rions1e9c3:
        "A. Consistency is helpful.":
            $menuhideborder = False
            show enver casual basic at right3
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin smile at left4
            mcrion "Of course not! I think the consistency is really helpful!"
            "I look at Rion and can't help but smile."
            mcrion "Plus, Rion is teaching me a lot!"

        "B. Rion is very knowledgeable.":
            $menuhideborder = False
            show enver casual basic at right3
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin smile at left4
            mcrion "I'm learning a lot of new techniques by working with Rion."
            mcrion "Plus, working with the same person means that I'm getting consistent feedback."

        "C. Rion works on exciting missions.":
            $menuhideborder = False
            show enver casual basic at right3
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin smile at left4
            mcrion "I don't think I'd get to work on such an exciting case with anyone else!"
            "I look at Rion and can't help but smile."
            mcrion "Plus, Rion is teaching me a lot!"


    show enver casual sad
    show ecmc jacket_v2 basic
    "Enver looks from me to Rion and narrows his eyes a little more."
    en "Hmmm."

    show enver casual smile
    en "Well, I think you make a great team."

    show ecmc jacket_v2 blush embarrassed
    "Enver gives me a very subtle wink and I can't help but blush."

    hide enver
    hide ecmc
    hide rion
    show rion jacket_cu basic_cu at rion_cu
    "I take another sip of my coffee and notice Rion looking at me strangely."
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Is something wrong?"
    hide ecmc

    show rion jacket_cu smirk_cu at rion_cu
    "Rion smiles softly at me and leans a little closer."

    show rion jacket_cu smile_cu
    ri "You have some foam on your lip."
    scene bg ecm_rion_s1_mini1 with dissolve:
        transform_anchor True zoom 1.3 xanchor 0.5 yanchor 0.0 xpos 0.5 ypos -0.5

    "Before I can respond, Rion smoothly places his thumb against my lip."
    "He gently wipes the foam away in one motion."
    en "Okay, what was that???"

    scene bg ecm_elysian_park_day at bg
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    with dissolve
    "Rion pulls away and I blush furiously as I look down at my coffee cup."
    hide ecmc

    show enver casual smile at right3
    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin blush embarrassed at left4
    ri "It was nothing. I was just being helpful."

    show ecmc jacket_v2 -blush embarrassed
    "My heart sinks a little at Rion's dismissal, but Enver scoffs."
    en "Really? Is that all it was?"
    "Enver smirks at Rion then puts some foam on his lip and leans towards Rion as he purses his lips."

    hide rion
    hide ecmc
    hide enver

    show sparkle_effect:
        corner1 (0.25, 0.0) corner2(0.75, 1.0) xpos 0.25
    show enver casual_cu sad_cu at enver_cu
    en "Wipe this off then?"
    hide enver

    show enver casual smile at right3
    show rion jacket pin smirk at left1
    show ecmc jacket_v2 pin smile at left4
    "I burst out laughing as Rion rolls his eyes."

    show rion jacket angry
    ri "Wipe it off yourself, Enver."
    en "Why? I thought you were being helpful?"

    show rion jacket basic
    "Enver smirks and looks at me."

    show ecmc jacket_v2 embarrassed
    en "Why does [genericfn] get special treatment?"

    show ecmc jacket_v2 blush embarrassed
    "I blush even harder and grip my coffee cup a little tighter."

    show ecmc jacket_v2 determined
    mcrion "Enver, stop it!"
    mcrion "You purposely got the foam on your lip so you don't deserve help!"

    hide enver
    hide rion
    hide ecmc
    "My ARCware pings and I gratefully use the distraction to look away from Enver and Rion."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Oh, my FDI request went through! Let's see.)"
    hide ecmc

    "I read the notification and gasp."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(The FDI believes that a D.I.V.A.A. agent is the killer in Rion's case!)"
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

