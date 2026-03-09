label arianna_season1_episode8:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mc_bedroom_night_lights at bg
    play music mscsadtimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much wcasualever, so long as you leave resets() and tobecontinued() at the bottom.

    show arianna dress_cu sad_cu at arianna_cu
    "Back at my room, Arianna throws herself on the bed and groans."
    show mscmc jacket_hairdown basic at left2
    show arianna dress sad at right2
    ai "What should I do about Emporia's dinner?"
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Why did Emporia request taht Arianna go without me?)"
    "(It gives me such a bad feeling.)"
    show mscmc jacket_hairdown sad at left2
    show arianna dress sad at right2
    "She covers her face with her hands."
    ai "This is getting so weird! Why does Emporia have to act like this?"
    mcarianna "I don't know, but I really really hate it."
    ai "Should I just end it?"
    show arianna behind mscmc
    show mscmc:
        easein 0.5 left1
    "Arianna drops her hands from her face as I sit next to her."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Of course I'm worried about Arianna going to the dinner. Why wouldn't I be?)"
    "(But this {i}is{/i} a big deal to her.)"
    show arianna dress sad behind mscmc at right1plus
    show mscmc jacket_hairdown sad at left1
    ai "As in, don't finish the pieces? Don't get paid? Bail on my first big commission?"
    mcarianna "You've been working really hard on them, but I don't know."
    ai "Ugh, I know! And I'm proud of them and how they're turning out."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She was so excited when she got this commission.)"
    "(I don't want her to regret bailing on Emporia.)"
    show arianna dress basic behind mscmc at right1plus
    show mscmc jacket_hairdown surprised at left1
    mcarianna "You don't sound like you want to call it."
    mcarianna sad "I support you in whatever you choose, but don't do this if you don't want to or have a bad feeling about it."
    mcarianna grin "There will be other commissions. You don't need Emporia to feel legit."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(That's like what Arianna was saying to me about the sponsorship.)"
    show mscmc sad_cu
    "(We're both in these weird places in our careers right now.)"
    "(Like we're close to making some kind of break, but it's not easy.)"

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0

    show arianna dress smile behind mscmc at right1plus
    show mscmc jacket_hairdown smile at left1
    ai "Thanks."
    show arianna sad
    "Arianna puffs out a sigh, her hands folded on her stomach."
    mcarianna sad "What're you thinking?"
    show mscmc basic
    ai basic "I think I should just finish the job. I'm almost done anyway."
    ai "I don't want all of this to be for nothing."
    mcarianna smile "Okay."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(This is her choice and I'll stick with her through it.)"
    show arianna dress angry behind mscmc at right1plus
    show mscmc jacket_hairdown smile at left1
    ai "But I'm done dealing with Emporia once the job's done. Even if she offers me millions of dollars for more pieces."
    show arianna basic
    show mscmc surprised
    "I put a hand to my chin, acting as though that would be too much to turn down."
    mcarianna "Hmm, I dunno. {i}Millions{/i} of dollars."
    show mscmc smile
    ai sad "It would be tempting."
    ai grin "I'll take you out to dinner once I get paid."
    hide mscmc
    hide arianna

    $menuhideborder = True
    menu ariannas1e8c1:
        "A. Like...a date?":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(A fancy meal between Arianna and me...)"
            show arianna dress grin behind mscmc at right1plus
            show mscmc jacket_hairdown grin at left1
            mcarianna "As in a date?"
            "I wink at Arianna and she giggles."
            ai embarrassed "Hmm...who knows what it'll be?"
        "B. Don't spend money on me.":
            $menuhideborder = False
            show arianna dress smile at right1plus
            show mscmc jacket_hairdown grin at left1
            mcarianna "That's sweet, but don't spend your freshly earned money on me."
            ai grin "It's my money and I can spend it how I want."
            ai "And how I want is to repay you for everything you've done."
        "C. I'll hold you to it.":
            $menuhideborder = False
            show arianna dress smile at right1plus
            show mscmc jacket_hairdown grin at left1
            mcarianna "You know, that does sound pretty nice."
            ai grin "We'll go to the fanciest restaurant around."
            mcarianna embarrassed "We might have to get dressed up."
            ai embarrassed "I would love to see you in a dress or a tux."

    show mscmc basic
    show arianna surprised
    "Arianna sits up with a gasp."
    ai grin "You need to send in your surf videos to High Tide."
    show arianna basic at out_right
    show mscmc smile
    "Arianna gets up to grab the camera from out of my bag."
    hide arianna
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "How does this work? You plug it into your laptop?"
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown smile at left1
    "I get my laptop from my nightstand and Arianna hands me the camera."
    show arianna smile
    mcarianna grin "Yeah, I'll download it, slap some basic editing on there, and email it to them."
    hide arianna
    hide mscmc
    "Once it's downloaded, I click through the videos and photos."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(They're actually really really good. I'm definitely impressed with Arianna.)"
    show arianna dress smile behind mscmc at right1plus
    show mscmc jacket_hairdown grin at left1
    mcarianna "I look badass."
    show arianna:
        easein_back 0.4 xoffset -15
    "Arianna nudges me with her elbow."
    ai grin "You like?"
    mcarianna "I do."
    ai "What're you gonna do if you get the sponsorship?"
    mcarianna "Piss my pants with joy."
    ai sleep "Very sexy."
    show arianna basic
    mcarianna "I'll get gear that I would usually buy for free, which is nice."
    show arianna grin
    mcarianna "They'll help with costs all around and help with competition fees and that sort of thing."
    show mscmc smile
    "I gesture around with my hands, weighing the imaginary possilities."
    ai "That sounds like it'll be a huge help."
    mcarianna grin "Yeah, for real."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(My bank account will be much happier.)"
    show arianna dress grin behind mscmc at right1plus:
        xoffset -15
    show mscmc jacket_hairdown grin at left1
    ai "And tomorrow's when you'll hear back?"
    mcarianna "Yep."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I've been trying so hard not to overthink it all.)"
    show arianna dress grin behind mscmc at right1plus:
        xoffset -15
    show mscmc jacket_hairdown smile at left1
    ai "Remember, good vibes only."
    mcarianna grin "I'm full of good vibes. I'm gonna get it."

    scene bg msc_labeach_day at bg with clockwise_wipe
    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    "The next day, Arianna and I are hustled out to the beach by Trina who is dead set on having an employees (and friends) retreat for the day."
    show trina casual smile at left2
    show arianna dress basic at right2
    so "Arianna, what kind of cocktails do you like? I have all the stuff for Sex on the Beach."
    ai surprised "Uh...huh?"
    "Trina pulls all her liquor bottles out of her cooler, wedging them into the sand temporarily."
    mcarianna "It's the name of a drink."
    ai "Oh, I've never tried it before."
    so "Really?! Well, you're about to try it if you want."
    so "I'm about to make the most fire drink you've ever had then."
    hide arianna
    hide trina
    show mscmc jacket_hairdown grin at centre
    mcarianna "And by that, she means she's going to pour a shit ton of alcohol in there."
    hide mscmc
    show trina casual smile at left2
    show arianna dress smile at right2
    so "The only way to do it, baby!"
    hide trina
    hide arianna
    show maxime casual basic at left2
    show dawn casual smile at right2
    "Maxime and Dawn walk towards our setup, a cooler bag in Maxime's hand."
    hide maxime
    hide dawn
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I didn't know Dawn was coming! They come into the shop sometimes with Maxime.)"
    hide mscmc
    show maxime casual basic at left2
    show dawn casual grin at right2
    dw "Glad to see the drinks are almost ready!"
    "Dawn pumps their fist in the air and then brushes back their blonde hair."
    hide maxime
    hide dawn
    show trina casual smile at centre
    so "Hey! Come join the fun!"
    hide trina
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I haven't seen Maxime since I heard he's a merperson.)"
    show dawn casual smile at right5:
        xoffset 50
    show arianna dress smile behind mscmc at left2
    show maxime casual basic behind arianna at right2
    show mscmc jacket_hairdown smile at left5
    dw "What's shakin'?"
    show dawn grin
    mcarianna grin "Guys, this is Arianna. Dawn and Maxime."
    mcarianna "Dawn's a professional windsurfer and hangs out at the shop sometimes."
    show arianna grin
    "Arianna shoots them a smile, then raises a brow at me in a 'that's Maxime?' way and I nod slightly."
    dw "Haven't seen you around before."
    show mscmc smile
    ai "I'm from out of town--just visiting [genericfn]."
    hide arianna
    hide maxime
    hide dawn
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(We'll need to come up with an actual state Arianna is from soon. Just in case.)"
    show dawn casual grin at right5:
        xoffset 50
    show arianna dress smile behind mscmc at left2
    show maxime casual smile behind arianna at right2
    show mscmc jacket_hairdown smile at left5
    mx "Nice to meet you."
    show maxime basic
    "Maxime gives Arianna a short nod and a tiny wave."
    hide arianna
    hide mscmc
    hide dawn
    show trina casual sad at left2
    so "Maxime, please tell me you brought those delicious brownies."
    show maxime smile
    "Maxime holds the cooler up."
    show trina smile
    mx "Right here."
    so "I can die happy and full now."
    hide maxime
    show trina at right4
    show arianna dress basic at left1
    show mscmc jacket_hairdown basic at left4
    "Trina brings two very full cups over to me and Arianna."
    so "Let's get wasted!"
    hide trina
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "({i}They{/i} can get wasted, but I definitely won't.)"
    show mscmc sad_cu
    "(Arianna and I are going to Emporia's later to drop off the last art piece.)"
    show mscmc jacket_hairdown basic at left1plus
    show arianna dress grin behind mscmc at right1plus
    ai "Oooo, this drink is good."
    mcarianna smile "Isn't it?"
    play sound phone_vibrating
    show mscmc surprised
    "My phone buzzes in my pocket making me jump."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(It has to be High Tide Sports! They said they would call me around this time to let me know.)"
    show mscmc jacket_hairdown surprised at left1plus
    show arianna dress smile behind mscmc at right1plus
    "I whip it out of my pocket and, sure enough, it is."
    show arianna grin
    show mscmc smile at out_left
    "Arianna gives me a thumbs up and I step away from the festivities."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcarianna "Hello?"
    hide mscmc
    $sidecharone = "Phil"
    sid1 "Hello, [genericfn]! We reviewed your footage and photos."
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(Please. Please. Please.)"
    hide mscmc
    sid1 "And I am happy to let you know that we want to take you on as a brand ambassador!"
    sid1 "Congratulations!"
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "All the stress in my hunched shoulders evaporates."
    "(I did it. I'm one step closer to my dream.)"
    mcarianna "Oh my god, thank you so much! That's great news."
    hide mscmc
    sid1 "There are a few introductory steps that we'll need to take, but those will be arranged."
    sid1 "Do you have any questions for me?"
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcarianna "None right now."
    hide mscmc
    sid1 "Welcome to the team!"
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown grin at left1
    "As I hang up, Arianna comes up to stand next to me."
    mcarianna "I got the sponsorship!"
    hide arianna
    hide mscmc
    show trina casual smile at centre
    so "That's my girl!"
    hide trina
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown grin at left1
    ai "I knew you would!"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna scoops me up in a hug, lifting me as she twirls me around."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(First the sponsorship and now getting held by a big, tall lady. Could this day get any better?)"
    show mscmc jacket_hairdown grin at left1:
        xoffset 30 yoffset -30
        pause 0.3
        parallel:
            linear 0.4 yoffset 0
        parallel:
            easeout_circ 0.4 xoffset 0
    show arianna dress grin behind mscmc at right1:
        xoffset -40
        pause 0.3
        linear 0.4 xoffset 0
    "Arianna sets me down with a laugh, though her hands are resting on my shoulders."
    hide arianna
    hide mscmc
    show trina casual smile at centre
    so "I knew they'd see your talent."
    so angry "Oh geez, and if it isn't the vermin himself."
    hide trina
    show hamish casual basic at centre:
        transform_anchor True zoom 0.65 yoffset 110
    "Trina's proclamation makes us all look up to see Hamish on the boardwalk."
    hide hamish
    show trina casual_cu smile_cu at trina_cu
    so "Guess who just got sponsored by High Tide Sports?"
    show mscmc jacket_hairdown basic at left2
    show trina casual smile at right2
    "Trina jabs a finger towards me as she shouts up at Hamish."
    show mscmc grin
    so "Yeah, that's right! Scurry on back to your shitty brand!"
    mcarianna surprised "Trina!"
    hide trina
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(It does feel good to have it shoved in Hamish's face.)"
    hide mscmc
    show hamish casual angry at centre
    "Hamish spots us and it looks like he considers shouting back but then he just sneers and scurries off."
    hide hamish
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "I have a well-deserved laugh at watching him scuttle away."
    "(Ya do love to see it.)"
    hide mscmc
    show trina casual smile at left2
    show dawn casual grin at right2
    dw "Now it's really time to celebrate. Pop the bottles, Trina!"
    so "Duh!"
    hide trina
    hide dawn
    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show arianna dress grin at right1
    show mscmc jacket_hairdown smile at left1
    "As Trina starts pouring more drinks, Arianna's hand slides down my arms."
    mcarianna grin "Hey."
    show arianna:
        easein 0.4 xoffset -30
    "Arianna takes my hands and bends down so that her lips are at my ear."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        xoffset 0
    ai "Wanna walk with me along the beach for a bit?"
    ai embarrassed_cu "I want to tell you a secret."
    hide arianna

    $menuhideborder = True
    menu ariannas1e8c2:
        "A. Be alone with Arianna and hear her secret!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show arianna dress_cu grin_cu at arianna_cu
            "My heart beats in my throat as she stares into my eyes, still leaning over."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her lips are so close to mine. There's barely any distance between us.)"
            mcarianna grin_cu "Sure."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna's eyes light up, a giddy curve to her lips."
            ai "Come on."
            hide arianna
            "She guides me away from the others."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(God, she's enchanting.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "There's a goofy embarrassed grin on her face as she walks backwards, waiting for me."
            show arianna dress grin at right1plus
            show mscmc jacket_hairdown grin at left1plus
            mcarianna "Okay, what is this secret?"
            ai "You wanna know?"
            mcarianna "Yes!"
            "Arianna lowers her head and raises a brow at me."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "You really wanna know?"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(It's killing me!)"
            mcarianna "C'mon! I really do!"
            show mscmc jacket_hairdown grin at left3:
                pause 0.1
                easein 0.6 left1
            show arianna dress grin behind mscmc at right1
            "Arianna beckons to me with her finger and I close the space between us."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(She's always so dramatic, but in the best way possible.)"
            "(The suspense is really getting to me.)"
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            "Arianna, now seeming bashful, glances down at our feet."
            ai grin_cu "I was thinking about it when I saw how excited you were on your phone call."
            ai "How your face lit up and you were smiling to yourself."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "It's a little embarrassing when you say it like that."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "I didn't want to take my eyes off you for a second. I still don't."
            show arianna embarrassed_cu
            "Arianna meets my eyes now, a pale blush on her cheeks that I'm sure matches mine."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "Is that it?"
            "(Because she can look as much as she wants.)"
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "No, I feel more creative when I'm around you."
            ai "Like, you're sending off this aura that opens me up."
            show arianna grin_cu
            "Arianna throws her arms out in a grand gesture."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She said I make her more creative...I like that.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "I just want to create things and explore different aspects of my art."
            ai "Stuff I've been scared of doing, and wih you I just want to go for it."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "My heart melts at the idea that I inspire her."
            "(She is so precious.)"
            show mscmc jacket_hairdown grin at left1
            show arianna dress grin behind mscmc at right1
            mcarianna "That was your big secret?"
            show arianna embarrassed
            "Her face tints a darker red."
            ai "Was it lame?"
            show mscmc embarrassed
            "Feeling like the mood is right, I reach out to take Arianna's hand and slot my fingers through hers."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(It was anything but lame, and seeing her be so open with me makes me feel special.)"
            mcarianna grin_cu "It was sweet."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Her fingers tighten around mine and she laughs."
            ai "You feel like a good luck charm but for creativity."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Glad that I can be of use to you."
            show mscmc embarrassed
            "(That's the first time anyone has ever said something like that to me before.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna bumps our arms together."
            ai "And what about you?"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "What about me?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Do I inspire you?"
            "She bats her lashes at me with a soft chuckle."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Seeing as I can't get her out of my head, I definitely feel like she does.)"
            mcarianna grin_cu "Maybe."
            hide mscmc
            show arianna dress_cu surprised_cu at arianna_cu
            "Arianna fakes a shocked gasp."
            ai "Maybe? That's cold."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Of course that's not how I really feel.)"
            mcarianna grin_cu "It felt really nice when you were filming me yesterday."
            mcarianna embarrassed_cu "I felt like I could do anything with you there."
            show mscmc jacket_hairdown embarrassed at left1
            show arianna dress embarrassed behind mscmc at right1
            "Arianna swings our hands back and forth."
            ai grin "Well, I'm glad I made you feel that way."
            ai "And I'm happy that you got the sponsorship."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Yeah, thank god for that. I'm happy as can be right now.)"
            show mscmc jacket_hairdown grin at left1
            show arianna dress grin behind mscmc at right1
            mcarianna "It was all the good vibes."
            ai "It was all {i}you{/i}."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna pulls on my hand to stop me from walking and forces me to face her."
            ai "I'm proud of you and you should be proud of yourself."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I am. This is what I worked for.)"
            mcarianna "Thank you. Really."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Onto bigger and brighter reefs now, huh?"
            ai "Feel any different?"
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "I pause, pretending to check myself out."
            mcarianna grin_cu "I thiiiiink...I feel exactly the same."
            "(It's like when people ask you if you feel older on your birthday.)"
            "(It hasn't really set in fully.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Well, you're a brand ambassador now. Congrats."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "I'll be surfing with the big dogs soon enough. At least, I hope."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "I know you will."

        "B. Stay with the group.":
            $menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown basic at left1
            mcarianna "I feel bad about leaving the group. They're celebrating me afterall."
            show mscmc sad
            show arianna sad
            "Arianna gives an exaggerated sigh."
            show mscmc basic
            ai grin "I guess you'll never know my secret then."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I do still want to know...)"
            show mscmc jacket_hairdown grin at left1
            show arianna dress smile behind mscmc at right1plus
            mcarianna "You could tell me later?"
            show mscmc sad
            ai grin "The door has closed."
            mcarianna smile "I'll get you next time."

    scene bg msc_mansion_interior_day at bg with clockwise_wipe
    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    "After Trina's small party and a drink, Arianna and I are back at Emporia's"
    show arianna dress basic at right1
    show mscmc jacket_hairdown basic at left1
    "I rub my hands over my thighs, trying my best to not look bothered."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Thank god this is almost over with.)"
    hide mscmc
    "Arianna's final piece is sitting on the coffee table in front of us, waiting for judgement."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It doesn't feel like that piece is going to be the only thing judged here today.)"
    "(For some reason, it seems like Emporia really doesn't like me.)"
    show mscmc angry_cu
    "(I mean, likewise, but still.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress surprised behind mscmc at right1
    ai "Last piece."
    show arianna basic
    mcarianna sad "Thank god."
    play sound heel_click
    hide arianna
    hide mscmc
    show emporia casual basic mask at centre with dissolve
    "The heels down the hallway signal Emporia's arrival. She enters and her eyes immediately zone in on Arianna."
    show emporia smile at left4
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress basic at right5
    bn "Wonderful to see you again."
    ai smile "And you."
    hide emporia
    hide arianna
    hide mscmc

    $menuhideborder = True
    menu ariannas1e8c3:
        "A. Say hi.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(I'll be civil.)"
            show emporia casual basic mask at left4
            show mscmc jacket_hairdown smile at right1plus
            show arianna dress smile at right5
            mcarianna "Hello, Emporia."
            bn smile "Nice to see you as well."
            hide arianna
            hide emporia
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Is it? Really? I wasn't even expecting a response.)"
        "B. Remain silent":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(I already know the drill. Emporia dislikes me for some reason.)"
            show emporia casual basic mask at left4
            show mscmc jacket_hairdown basic at right1plus
            show arianna dress smile at right5
            "I opt not to say anything to avoid the inevitable scowl I know I'll get."
            bn smile "And how are you doing today, [genericfn]?"
            show mscmc surprised
            "I'm sure my eyes are wide with visible shock at her actually addresing me."
            mcarianna "Uh, I'm good."
        "C. Bring up how this is the LAST piece.":
            $menuhideborder = False
            show emporia casual basic mask at left4
            show mscmc jacket_hairdown grin at right1plus
            show arianna dress smile at right5
            mcarianna "Last piece, Emporia. Looks like the commissions are done with."
            show mscmc basic
            bn "How sad it will be when our time together is over."
            bn smile "I've begun looking forward to our chats."
            hide arianna
            hide emporia
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Ew. Why is she being fake nice?)"

    show emporia casual smile mask at left4
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress basic at right5
    "Emporia circles the coffee table, a smile on her face."
    bn "This is the final piece?"
    ai grin "Yup!"
    show emporia basic
    show arianna basic
    "Emporia purses her lips as she inspects the sculpture."
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(She better not be rude this time.)"

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show emporia casual smile mask at left4
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress basic at right5
    bn "I love it."
    ai grin "Really?"
    bn "It's everything I wanted. You captured my mind's eye perfectly."
    ai "That's what I aim to do."
    "Arianna looks at me with a content smile."
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I shouldn't be overthinking how normal and nice Emporia is being, but I can't help it.)"
    show mscmc angry_cu
    "(Why's Emporia acting so nice now? I don't trust it.)"
    show emporia casual smile mask at left4
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress basic at right5
    bn "Have you thought about my dinner party, Arianna? I can give you your check for the comissions then."
    bn "And again, there is still someone I'd love for you to meet who is considering placing an order with you."
    bn "They have a lot of connections in the art world."
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Again about the dinner. Ugh. I really don't want Arianna to go to that.)"
    "(Something about it feels off.)"
    show emporia casual basic mask at left4
    show mscmc jacket_hairdown basic behind emporia at right1plus
    show arianna dress surprised at right5
    ai "I have some tentative plans in the air that I need to figure out."
    ai smile "But, I'll let you know."
    show arianna basic
    bn smile "Please, no pressure."
    show mscmc:
        easein 0.8 xoffset-80
    "Feeling like it's the end of the meeting, I move to stand."
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu:
        xoffset 0
    "(Time to get out of here.)"
    show emporia casual basic mask at left4
    show mscmc jacket_hairdown grin at right4
    mcarianna "Well, Emporia, it's been nice working with you."
    mcarianna "We have a busy day ahead of us."
    hide mscmc
    show arianna dress surprised at right4
    ai "Actually, would it be alright if I used the restroom?"
    show emporia smile
    "Emporia claps her hands, summoning her butler who seems to appear out of thin air."
    bn "Show her to the restroom."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Oh great, now I'm going to be alone with Emporia.)"
    show emporia casual smile mask at left4
    show arianna dress grin at right5
    show mscmc jacket_hairdown basic behind arianna at right1plus
    ai "I'll be right back."
    show arianna at out_right
    mcarianna smile "Take your time."
    hide emporia
    hide mscmc
    "I stand by the hallway, arms crossed as I look after Arianna."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Should I say something? No. It's better in silence.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    show emporia casual sad mask at centre
    bn "You."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "What?"
    hide mscmc
    show emporia casual_cu sad_cu mask_cu at emporia_cu
    "Emporia steps towards me, her eyes narrowed and any trace of her \"kindness\" gone."
    "Her whole body is tense and her lips are curved down."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Whoa, what is happening?!)"
    hide mscmc
    show emporia casual_cu angry_cu mask_cu at emporia_cu
    bn "Stay away from her."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Excuse you?"
    show mscmc angry_cu
    "(Is she talking about Arianna?)"
    hide mscmc
    show emporia casual_cu sad_cu mask_cu at emporia_cu
    "Emporia closes the gap between us, towering over me as I step back."
    bn angry_cu "Consider this your first and last warning."
    "Her voice is a venomous hiss and her hands are clenched into fists at her sides."
    bn "Get out of Arianna's life. And. Stay. Out."


    scene bg msc_msctbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
