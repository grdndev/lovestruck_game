label arianna_season1_episode9:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_boardwalk_day_people at bg
    play music mscsadtimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show arianna dress basic at right1
    show mscmc jacket_hairdown sad at left1
    "As we walk down the boardwalk, I feel safe enough to tell Arianna about Emporia's threat just now."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It was like a switch flipped in Emporia the second Arianna was gone. It was nuts!)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress basic behind mscmc at right1
    mcarianna "Hey, uh, when you went to the bathroom...something happened."
    show arianna sad
    "Arianna stops, a tense frown already forming."
    show arianna angry
    mcarianna "Emporia told me to stay away from you. She got in my space like she was actually threatening me."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I knew Emporia was up to something, but that was some unhinged shit.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress angry behind mscmc at right1
    mcarianna "It was, like, as soon as you were gone."
    ai "What? She can't talk to you like that! Are you okay?"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "Arianna puts her hands on my shoulders, looking into my eyes."
    hide arianna

    $ menuhideborder = True
    menu ariannas1e9c1:
        "A. I'm fine.":
            $ menuhideborder = False
            show arianna dress sad at right1
            show mscmc jacket_hairdown surprised at left1
            mcarianna "Yeah, yeah, I'm fine--it was just weird as hell."
            mcarianna sad "I'm not scared of someone like her."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I've dealt with bigger bullies in my lifetime.)"

        "B. It's you I'm worried about.":
            $ menuhideborder = False
            show arianna dress sad at right1
            show mscmc jacket_hairdown sad at left1
            mcarianna "I'm more worried about you, honestly. She's super weird about you. I don't like any of this and I don't trust her."
            mcarianna "The way she talks to you and about you...I hate it."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Even when she looks at Arianna, I feel like there could be something else behind it.)"

        "C. I didn't know what to do.":
            $ menuhideborder = False
            show arianna dress sad at right1
            show mscmc jacket_hairdown sad at left1
            mcarianna "I didn't really know what to do or say. It was so out of the blue."
            mcarianna "I was kind of thinking she might hit me."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(She had her fists clenched and...something about her feels like she could get violent.)"


    show mscmc jacket_hairdown sad at left1
    show arianna dress sad behind mscmc at right1
    mcarianna "Arianna, I'm starting to get really worried about all this."
    "Ariann slides her hands from my shoulders to my wrists, loosely holding me."
    ai "I won't go to the dinner. I already didn't want to, but now Emporia is just too much."
    ai "I shouldn't have gone to the bathroom, I could've held it."
    show mscmc smile
    "I try not to laugh because of how serious Arianna sounds."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I'm not mad she went to the bathroom.)"
    show mscmc sad_cu
    "(I knew there was something up with Emporia, but that threat was on another level.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress basic behind mscmc at right1
    mcarianna "What're you gonna do about getting paid? She wanted to give you your check at the dinner."
    ai surprised "I can go over during the day tomorrow, pick it up, and leave. I won't even go inside."
    ai sad "There's no way I'd ever have dinner alone there now."
    show arianna smile
    "Arianna shakes my wrists for emphasis before letting go of me."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Emporia pushing for alone time with Arianna makes me sick to my stomach.)"
    "(What does she want with her so badly?)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress sad behind mscmc at right1
    ai "Would you come with me to get the check, though? Just...in case."
    mcarianna surprised "Of course, I'm not letting you go over by yourself."
    show arianna basic
    mcarianna basic "But, uh, maybe it's for the best if Emporia doesn't see me with you. I'll stay out of sight."
    show mscmc sad
    ai angry "I wouldn't let her hurt you."
    show mscmc embarrassed
    "The burning in Arianna's eyes makes my chest flutter."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(And I'll protect Arianna too.)"
    show mscmc jacket_hairdown grin at left1
    show arianna dress smile behind mscmc at right1
    mcarianna "I'll just hide in the bushes or something."
    show mscmc smile
    "Arianna nods in agreement, her hand going to her necklace."
    ai surprised "Let's call her now so I can tell her I'm not going to her dinner."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Emporia won't be happy.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    "I get my phone out, call the number on speaker, and brace myself."
    bn "Hello, [genericfn]."
    show arianna dress surprised at right1
    show mscmc jacket_hairdown basic at left1
    ai "Um, hi...Emporia. It's Arianna."
    hide arianna
    hide mscmc
    bn "Arianna, what a delight to hear your voice."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Just her voice gives me the chills now.)"
    hide mscmc
    bn "I hope this call is an answer about my dinner invitation."
    show arianna dress sad at right1
    show mscmc jacket_hairdown basic at left1
    ai "It is, and I won't be able to make it. I'm way too busy."
    ai surprised "I was hoping I could stop by tomorrow and pick up the check during the day."
    show arianna sad
    "Arianna and I both stare at the phone, waiting for the inevitable outburst."
    hide arianna
    hide mscmc
    bn "The busy life of an artist. It can't be helped! I understand completely."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What? I don't see her as the type to take rejection well.)"
    hide mscmc
    bn "Please, come by the house any time tomorrow and I'll have the check ready for you."
    show arianna dress surprised at right1
    show mscmc jacket_hairdown basic at left1
    ai "Oh, um, thank you. I'll just grab it from you then, won't have time to come in or anything."
    hide arianna
    hide mscmc
    bn "Perfectly fine. Just give the doorbell a ring when you arrive."
    show arianna dress surprised at right1
    show mscmc jacket_hairdown basic at left1
    ai "Sure, okay. See you tomorrow."
    hide arianna
    hide mscmc
    bn "Ta-ta."
    show arianna dress basic at right1
    show mscmc jacket_hairdown basic at left1
    "Emporia hangs up and Arianna shrugs."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(She was {i}too{/i} calm.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress surprised behind mscmc at right1
    ai "That was easy?"
    mcarianna "In and out tomorrow."

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    scene bg msc_mc_bedroom_sunset at bg with clockwise_wipe
    "Later that evening, Arianna, Trina, and I are sitting on my bedroom floor."
    show arianna dress smile at left1
    show mscmc casual_hairup smile at left4
    show trina casual smile at right4
    "Trina rummages in the plastic bag beside her and holds a bag of candy out to Arianna."
    ai grin "What are these?"
    hide arianna
    hide trina
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(Arianna is in for a real treat tonight. Literally.)"
    show mscmc casual_hairup smile at left4
    show arianna dress grin behind mscmc at left1
    show trina casual smile at right4
    so "Sour gummy worms? Only the best candy in existence."
    ai surprised "Really?"
    so "Girl, have you seriously never had one?"
    hide arianna
    hide trina
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(Arianna fits in so well most of the time that I forget a lot of human stuff is new to her.)"
    show mscmc casual_hairup grin at left4
    show arianna dress grin behind mscmc at left1
    show trina casual smile at right4
    mcarianna "Blue and red is the best flavor."
    "Arianna opens the package and takes a worm, squeezing it before popping it in her mouth."
    so "Weeeelll?"
    hide arianna
    hide trina
    show mscmc casual_hairup_cu basic_cu at mscmc_cu
    "(She doesn't look like she likes them.)"
    show mscmc casual_hairup smile at left4
    show arianna dress sad behind mscmc at left1
    show trina casual basic at right4
    ai "It's not bad, but I can't see myself eating a ton, so acidic."
    show arianna smile
    so sad "Man, I used to eat so many as a kid I would just have total sugar overload."
    show trina smile
    mcarianna grin "Let her try some chocolate."
    hide arianna
    hide trina
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(Chocolate seems much more up Arianna's alley.)"
    show mscmc casual_hairup smile at left4
    show arianna dress smile behind mscmc at left1
    show trina casual smile at right4
    so "Alright, here. At least you've had these, right?"
    "Trina hands a bag of caramel chocolates to Arianna and she takes one out."
    ai surprised "Nope."
    show arianna surprised
    so sad "Good god, woman! [genericfn], show your girl some culture!"
    hide arianna
    hide trina
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(Trina...she's not my woman. For now.)"
    show mscmc casual_hairup smile at left4
    show arianna dress grin behind mscmc at left1
    show trina casual smile at right4
    "Arianna eats the chocolate and starts nodding in contentment."
    hide arianna
    hide trina
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(That's a good sign!)"
    show mscmc casual_hairup smile at left4
    show arianna dress grin behind mscmc at left1
    show trina casual smile at right4
    ai "Better. Much better."
    so "Here. You two do your own masks."
    "Trina hands me face mask packets and Arianna leans in and rests her chin on her hands."
    hide trina
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Put it on for me?"
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(As in, touch her face in a super intimate and fun way?)"
    show mscmc grin_cu
    mcarianna "Come here."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        transform_anchor True zoom 0.90
        linear 1.0 zoom 1.0
    "She scooches herself closer with a grin and Trina whistles."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(Don't get lost in her eyes.)"
    hide mscmc
    "I rip the pack open with my teeth and squirt some of the mixture onto my fingers."
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    mcarianna "Stay still."
    hide mscmc
    "I press my fingers to her cheek, dragging the goop under her eyes and around her jaw."
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "It's cold."
    "I'm delicate with my application, though I'm in no rush to stop touching her face."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with dissolve
    "Face masks and candy finished, night falls as the sun disappears over the horizon."
    show mscmc casual_hairup smile at left4
    show arianna dress smile behind mscmc at left1
    show trina casual smile at right4
    so "Okay, ladies, now for a sleepover classic. It's MASH time!"
    so "We're doing all the OG sleepover stuff tonight."
    hide arianna
    hide trina
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(God, I used to have so much fun playing that.)"
    show mscmc casual_hairup grin at left4
    show arianna dress smile behind mscmc at left1
    show trina casual basic at right4
    mcarianna "I haven't played MASH since I rode the school bus."
    show mscmc smile
    ai surprised "What's MASH?"
    so sad "You don't know what MASH is either?"
    mcarianna surprised "She was homeschooled."
    show mscmc basic
    ai sad "And my parents were health freaks. We never had candy in the house."
    hide arianna
    hide trina
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(Good save.)"
    show mscmc casual_hairup smile at left4
    show arianna dress smile behind mscmc at left1
    show trina casual smile at right4
    so "Daaaang. Well, don't worry--it's loads of fun."
    so "MASH predicts your future."
    show arianna grin
    "Arianna's face lights up."
    ai "I wanna play!"
    hide arianna
    hide trina
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(God, will it ever get old seeing how amped up she is to try human stuff?)"
    show mscmc casual_hairup smile at left4
    show arianna dress smile behind mscmc at left1
    show trina casual smile at right4
    so "Okay, we need paper and a pen and--!"
    play sound phone_ringing
    show trina sad
    "Trina's phone rings and she answers it with a sigh."
    hide arianna
    hide mscmc
    show trina casual_cu basic_cu at trina_cu
    so "Hello?"
    so "...yeah. Be right there."
    hide trina
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Uh oh.)"
    show mscmc casual_hairup sad at left4
    show arianna dress sad behind mscmc at left1
    show trina casual sad at right4
    so "Sorry guys, this stupid shipment for the shop just got here."
    so "I gotta let these guys in. Might be a while but y'all keep sleepover-ing without me!"
    show trina at out_right
    "Trina shoves her phone into her pocket and leaves with a sigh."
    hide trina
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    ai "Aw, I wanted to play MASH."
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Awwww. She sounds so sad.)"
    show mscmc casual_hairup basic at left1
    show arianna dress surprised behind mscmc at right1plus
    ai "Do you need three people to play?"
    mcarianna smile "Nah."
    ai grin "Want to still play?"
    show arianna smile
    "She looks back up at me with a smirk."
    hide arianna
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(I mean, we {i}could{/i}. Trina leaving doesn't have to end the fun.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "What if it says we'll be friends forever or something?"
    ai "I hope it does."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(Arianna wants to know about {i}us{/i}.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas1e9c2:
        "A. Show Arianna your future together!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "(It might be a silly game, but I wouldn't mind thinking about a future with Arianna.)"
            show mscmc casual_hairup grin at left1
            show arianna dress grin behind mscmc at right1plus
            mcarianna "Alright, let's play."
            ai "Yay!"
            "I get out a notebook and pen."
            show mscmc smile
            ai surprised "How do you play?"
            hide arianna
            show mscmc casual_hairup_cu smile_cu at mscmc_cu
            "(I think I remember how to play this game the right way. It's not that complicated.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile behind mscmc at right1plus
            mcarianna "We make a list of four or so different categories with four choices in each."
            mcarianna "So, like, one is the type of home that you'll live in."
            mcarianna "Let's keep it classic: mansion, apartment, shack, and house."
            "I write it out on the paper, letting Arianna see."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Everytime I show her something, she {i}really{/i} pays attention.)"
            "(She's so cute and eager to learn.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile behind mscmc at right1plus
            mcarianna "That's why the game is called MASH."
            ai grin "Okay, I'm following."
            show arianna smile
            mcarianna "Right, we'll do three other categories now."
            mcarianna "Number of kids...we'll just do 1, 2, 3, and 4."
            mcarianna "Name four people."
            show mscmc embarrassed
            ai grin "You and..."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Good to know I'm number one on the list.)"
            show mscmc casual_hairup smile at left1
            show arianna dress sad behind mscmc at right1plus
            "Arianna puts a hand to her chin in thought."
            ai grin "I'll pick people you know, so Trina, Maxime, and Dawn."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "(It's a game, but...I will be pissed if my name doesn't get picked.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile behind mscmc at right1plus
            mcarianna "Now give me four locations."
            show mscmc smile
            ai grin "The beach, a swamp, underwater, and on top of a mountain."
            show arianna smile
            mcarianna grin "Okay, now you're gonna close your eyes and I'm going to go down the list like this."
            show mscmc smile
            "I tap my pen over each location."
            mcarianna grin "I'll stay within each category and you'll tell me when to stop."
            mcarianna "Then I'll circle whatever I land on."
            ai grin "Who knew seeing the future would be so easy?"
            hide arianna
            show mscmc casual_hairup_cu smile_cu at mscmc_cu
            "(If only it were. I'd have my whole life figured out from the age of seven.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile behind mscmc at right1plus
            mcarianna "The wonders of human magic."
            ai grin "I love it."
            mcarianna "Close your eyes."
            show arianna sleep
            "Arianna folds her hands on her lap and closes her eyes."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Her eyelashes are so long.)"
            show mscmc casual_hairup grin at left1
            show arianna dress sleep behind mscmc at right1plus
            mcarianna "Tell me when."
            "Mansion. Apartment. Shack. House. Mansion. Apartment. Shack. House."
            show mscmc smile
            ai "Stop."
            hide arianna
            show mscmc casual_hairup_cu smile_cu at mscmc_cu
            "(Okay. Okay. So far so good.)"
            show mscmc casual_hairup smile at left1
            show arianna dress sleep behind mscmc at right1plus
            "I circle the choice and move down to kids."
            mcarianna grin "Okay."
            show mscmc smile
            ai "Stop."
            mcarianna grin "Next is who you're gonna marry."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(It better be my name. I don't want to imagine her with any other name she picked.)"
            hide mscmc
            show arianna dress_cu sleep_cu at arianna_cu
            ai "I hope it's who I want it to be."
            show mscmc casual_hairup embarrassed at left1
            show arianna dress sleep behind mscmc at right1plus
            "I'm glad her eyes are closed and she can't see the way I blush to myself."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Me too.)"
            show mscmc casual_hairup basic at left1
            show arianna dress sleep behind mscmc at right1plus
            "I wait for Arianna to call it, but she stays silent."
            "And silent."
            stop music fadeout 0.5
            play music mscromance fadein 1.0
            show mscmc surprised
            "And more silence."
            hide arianna
            show mscmc casual_hairup_cu surprised_cu at mscmc_cu
            "(Is she...zoning out? Falling asleep?)"
            show mscmc casual_hairup surprised at left1
            show arianna dress sleep behind mscmc at right1plus
            "You need to tell me when to stop."
            ai "I'm waiting for the right moment. I'm channeling it."
            show mscmc grin
            "I go over a few more times, laughing more with every second that passes of her being quiet."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(It's like she's trying to telepathically see where my pen is at.)"
            hide mscmc
            show arianna dress_cu sleep_cu at arianna_cu
            ai "Stop!"
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "Circling my own name is as rewarding as I hoped it'd be."
            show mscmc embarrassed_cu
            "(She really did channel it.)"
            show mscmc casual_hairup grin at left1
            show arianna dress sleep behind mscmc at right1plus
            mcarianna "Last one."
            show mscmc smile
            ai "Stop."
            show arianna smile
            "I circle the final answer and Arianna peeks open one eye."
            mcarianna grin "Ready for your future?"
            ai grin "Yes!"
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Time to see our future together.)"
            show mscmc casual_hairup grin at left1
            show arianna dress grin behind mscmc at right1plus
            "She claps her hands together and nods eagerly."
            mcarianna "You'll live in a mansion."
            ai "Ooooooo. I'm gonna be rich."
            mcarianna embarrassed "It'll be on the beach and...you're going to marry me."
            show mscmc grin
            show arianna surprised
            "Arianna feigns shock, putting her hand to her mouth."
            ai embarrassed "Is this a proposal?"
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(The things she does to me.)"
            show mscmc casual_hairup grin at left1
            show arianna dress embarrassed behind mscmc at right1plus
            mcarianna "You wish."
            ai grin "And how many lovely half-mermaid kids will we have, honey?"
            hide arianna
            show mscmc casual_hairup_cu surprised_cu at mscmc_cu
            "The pen drops out of my hand, the pet name sending tingles down my spine."
            show mscmc embarrassed_cu
            "({i}Wow{/i}.)"
            show mscmc casual_hairup smile at left1
            show arianna dress smile behind mscmc at right1plus
            "I clear my throat and look down at the paper."
            mcarianna embarrassed "Three."
            show mscmc grin
            ai grin "That's a lot of mouths to feed."
            show arianna smile
            mcarianna "We'll live in a mansion--we'll have money."
            show mscmc embarrassed
            ai surprised "Do we teach them how to walk or swim first?"
            show arianna smile
            mcarianna grin "If we have a house on land, I think walking makes more sense."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Actually, little half-mer babies would be sooo cute.)"
            show mscmc casual_hairup embarrassed at left1
            show arianna dress grin behind mscmc at right1plus
            ai "You're a surfer, we're gonna be in the water a lot."
            mcarianna surprised "That's a fair point."
            show mscmc smile
            "I tap the pen to my mouth."
            mcarianna grin "Actually, I feel like kids can swim before hey walk anyways."
            mcarianna "So maybe we {i}should{/i} teach them to swim first."
            show arianna embarrassed
            "Arianna takes my hand and squeezes it."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "I'm so lucky to have a total babe as a future wife."
            show arianna grin_cu
            "Her hand envelopes mine in a pocket of warmth."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            mcarianna "Me too."
            hide mscmc

        "B. It's just a kids game.":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc casual_hairup basic at left1
            mcarianna "It doesn't really predict the future. It's just a kids' game."
            show arianna sad
            "Arianna rolls her eyes and clicks her tongue."
            show mscmc smile
            ai "I know that...It sounds fun is all."
            mcarianna "You make your own future, Arianna. You're living real life MASH right now."
            ai "But I crave the instant gratification of knowing."
            mcarianna grin "One day, we'll both know."
            hide arianna
            hide mscmc


    "I stuff all the face mask packs and candy wrappers back into the plastic bag."
    show arianna dress smile at right1plus
    show mscmc casual_hairup smile at left1
    mcarianna "I'm getting kinda tired. Almost ready for bed?"
    ai surprised "Can we fall asleep watching a movie?"
    mcarianna grin "You want to watch Half Moon, don't you?"
    ai "I {i}have{/i} to know what that red-head vampire does."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Ah, yes. She's fallen for the Midnight movie franchise trap. Good.)"
    "(It's so bad, and yet is the best series ever made.)"
    show mscmc casual_hairdown grin at left1
    show arianna dress grin behind mscmc at right1plus
    mcarianna "Let me get my laptop."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    scene bg msc_mansion_exterior_day at bg with clockwise_wipe
    "When the next afternoon rolls around, Arianna and I go to Emporia's for the last time to pick up the check for the job."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(I can't wait until this is all over with. I'm sick of Emporia, she stresses me out.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas1e9c3:
        "A. Offer Arianna your pepper spray.":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown sad at left1
            mcarianna "Here. Take my pepper spray."
            show arianna smile
            "I try to hand it to Arianna, but she pushes my hand away with a smile."
            ai "Don't worry. I'm not even going inside."
        "B. Are you gonna be okay?":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown sad at left1
            mcarianna "Are you gonna be okay talking to her?"
            ai smile "I'll be as calm and cool as ever."
            ai grin "I won't let her see how I really feel."

        "C. What if she tries something?":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown sad at left1
            mcarianna "What if she tries something?"
            mcarianna "What if she, like, gets in your face too, or-?"
            ai smile "I'll keep my guard up."

    ai grin "I'll be safe and quick and defend myself if I have to."
    show arianna smile
    mcarianna basic "I'll see if there's a good hiding bush around back. I hope she doesn't have cameras."
    ai grin "Who cares? We won't see her after this."
    show arianna smile
    mcarianna "Shout if you need me, okay?"
    show mscmc smile
    ai grin "I will. Now, go find your bush and let's finish this."
    hide arianna
    hide mscmc
    "As Arianna walks up to the door, I duck around the side of Emporia's place."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I hate leaving Arianna to talk to Emporia alone.)"
    hide mscmc
    "Hugging the side of the building and ducking beneath windows, I peer around to the backyard."
    "There's an old, rundown stables."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Emporia doesn't strike me as an animal person.)"
    hide mscmc
    "I creep up to the stables and peek in one of the windows."
    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    "As expected, there are no animals, but something on the far wall catches my eye."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What is that?)"
    hide mscmc
    "It almost looks like some kind of makeshift altar."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Emporia also doesn't strike me as the religious type.)"
    "(I may as well check it out.)"

    scene bg msc_stables_day at bg with dissolve
    "I push the door open as quietly as I can, wincing with every creak it makes."
    "The door closes softly behind me and I move into the back of the stables."
    "My blood turns to ice."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    mcarianna "What the hell...?"

    scene arianna_s1_mini3 at bg with dissolve
    "There are pictures of Arianna stuck to the wall and one in the middle surrounded by candles."
    "I bend down to look at the framed photo and there are ominous x's over Arianna's eyes."
    "My stomach knots as every alarm goes off in my body."
    mcarianna "Okay. Holy shit."
    "(This is bad. Really bad.)"
    show arianna_s1_mini3 as pulse_effect:
        align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.2
        linear 0.8 zoom 2.0 alpha 0.0
    pause 0.8
    stop music fadeout 0.5
    play music msctense fadein 1.0
    scene bg msc_mansion_exterior_day at bg
    "Throwing caution to the wind, I book it out of the stables."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Arianna is talking to Emporia {i}right now{/i}! I need to get her out of here.)"
    hide mscmc
    "I run around to the front, praying to see Arianna at the front door."
    "But I feel even sicker as I stop in my tracks."
    "Arianna is nowhere to be seen."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Where is she?! She wouldn't have left without me.)"
    hide mscmc
    "The door is closed and there's no sign of anyone."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I have to get in there. I have to save her. What if Emporia has her tied up or worse?)"
    "(Arianna's been kidnapped...)"
    hide mscmc
    "My heart is beating in my throat, panic is making me sweat, and my lungs feel tight."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(I should break a window or bang on a door or call the cops.)"
    show mscmc sad_cu
    "(Shit, I can't call the cops because if they look into Arianna and can't find any human records on her, we're screwed!)"
    "(Arianna needs me. I can't make a mistake.)"
    mcarianna "Okay. Okay."
    "(I can't just shatter a window...yet. I need to be smart about this.)"
    show mscmc angry_cu
    "(Arianna's in danger.)"
    "(And I'm gonna need more than pepper spray to save her.)"

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    scene bg msc_mc_bedroom_day at bg with dissolve
    "I burst into my room."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcarianna "I can't believe this is happening."
    "(Am I really gonna have to fight Emporia to save Arianna?! Oh my god. I need to find a weapon.)"
    show mscmc angry_cu
    "(I'll do it of course, but shit!)"
    hide mscmc

    play sound "audio/sfx/bubbles_003_6397.mp3" loop
    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    "My shellphone rings and my heart leaps."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna?! She's okay?!)"
    hide mscmc
    stop sound fadeout 0.5
    "I grab the phone with a shaky hand and answer."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Arianna?!"
    hide mscmc
    "All I hear is a low cackle on the other end."
    bn "Arianna is mine now."
    "Then there's a click as the call ends."

    scene bg msc_msctbc at bg with fade

    $ tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
