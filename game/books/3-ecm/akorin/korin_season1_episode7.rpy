label korin_season1_episode7:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_bar_off at bg
    play music ecmkorintheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Later that night, I'm with Korin and the other trainees as we enter a crowded club called The Catalyst."

    show korin casual pin smile at centre
    ko "Okay, everyone listen up! Tonight, your assignment is..."
    "Everyone leans in, eager and ready to find out what Korin has planned for us."
    ko "To unwind and have fun!"
    "We laugh and lean back, relaxing."
    ko "You can get a drink or two and put it on the D.I.V.A.A. tab, but {i}do not go overboard{/i}."
    ko "I fought hard to budget for this, okay? Don't give them an excuse to take it away from me!"

    show ecmc nojacket_v1 pin basic at left3
    show korin casual pin smile at right3
    "The group rushes for the bar, and I sidle up to Korin."

    show ecmc nojacket_v1 pin surprised at left3
    mckorin "D.I.V.A.A. let you have a budget for this?"
    ko "Of course! At this stage in training, Hatchlings are usually all stressed out and need to cut loose a bit."

    show korin casual pin smirk at right3
    ko "{i}Some{/i} of my trainees have had it harder than others..."
    "She gives me a pointed look."
    ko "...So I'm going to keep a special watch over them and make sure they enjoy themselves tonight."

    hide ecmc
    hide korin
    $menuhideborder = True
    menu korins1e7c1:
        "A. I don't know if I can.":
            $menuhideborder = False
            show ecmc nojacket_v1 pin sad at left3
            show korin casual pin sad at right3
            mckorin "I don't know if I can enjoy myself in a place like this..."
            ko "But we just got here. You can try, can't you? For me?"
            "(I know I can't say no when she asks like that.)"

        "B. I'll do my best!":
            $menuhideborder = False
            show ecmc nojacket_v1 pin basic at left3
            show korin casual pin smile at right3
            mckorin "I'll do my best! Just gotta keep a mind open to new experiences..."
            ko "Scraps, that's what I love to hear. You got this!"

        "C. You need to enjoy yourself too.":
            $menuhideborder = False
            show ecmc nojacket_v1 pin smile at left3
            show korin casual pin smirk at right3
            mckorin "You need to enjoy yourself too, you know."

            show korin casual pin smile at right3
            ko "Who says I'm not?"

    show ecmc nojacket_v1 pin basic at left3
    show korin casual pin basic at right3
    "I'm quiet for a moment."

    hide korin
    hide ecmc
    show ecmc nojacket_v1_cu blush_cu embarrassed_cu at ecmc_cu
    "(It's a little weird seeing Korin out of uniform, but...she looks so good.)"
    hide ecmc

    show ecmc nojacket_v1 pin surprised at left3
    show korin casual pin basic at right3
    "To stop myself from stealing glances at her shoulders, I look down at my own clothes."

    hide korin
    hide ecmc
    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(It feels weird being in something a little more casual around her. Not bad, just...different.)"
    hide ecmc

    show ecmc nojacket_v1 pin basic at left3
    show korin casual pin basic at right3
    "Lights pulse and sweep the dance floor in time to electronic club music."

    show ecmc nojacket_v1 pin sad at left3
    mckorin "There's a {i}lot{/i} of people here."

    show korin casual pin smirk at right3
    ko "Sure, but the people in our group aren't really strangers, are they?"
    mckorin "Well..."
    "I look at the crowd of other trainees and realize..."

    hide korin
    hide ecmc
    show ecmc nojacket_v1_cu sad_cu at ecmc_cu
    "(I don't really know any of them.)"
    hide ecmc

    show ecmc nojacket_v1 pin sad at left3
    show korin casual pin smirk at right3
    "Already, they're pairing off into their own friend groups and couples."

    show korin casual pin smile at right3
    ko "Okay, well, even if they are...is that so bad?"

    hide korin
    hide ecmc
    show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
    "(I guess not. Everyone's a stranger...until they aren't.)"
    hide ecmc

    show ecmc nojacket_v1 pin sad at left3
    show korin casual pin smirk behind ecmc at right3:
        easein 0.6 xoffset -220
    "Korin nudges me."
    ko "Here, come find a table with me."

    hide ecmc
    hide korin
    "We find a hightop table on the edge of the dance floor. I take a seat on one of the stools."

    show ecmc nojacket_v1 pin basic at left3
    show korin casual pin sad at right3
    ko "I really didn't mean for this night to make you more anxious. I thought..."

    show ecmc nojacket_v1 pin surprised at left3
    mckorin "It's okay, really!"

    show ecmc nojacket_v1 pin smile at left3
    mckorin "Honestly, everything here...it's a good distraction! It forces me to think about other things."

    show korin casual pin smile at right3
    ko "Well, I'm glad. But I hope I can do a little more than that and get you to {i}enjoy{/i} yourself, too."
    "I fight hard to keep a straight face."

    show korin casual pin smirk at right3
    ko "Tall order, huh? That's okay. I don't give up easily."

    show ecmc nojacket_v1 pin surprised at left3
    show korin casual pin surprised at right3
    "Both of us look up as someone calls Korin's name."
    trainees "Korin!! Come dance with us!"

    show korin casual pin surprised at right3:
        ease 0.4 xoffset -80
    "Korin hops off her stool."

    show korin casual pin smirk at right3:
        xoffset -80
    ko "Dancing might take your mind off it for a bit, you know. It works for me..."

    show ecmc nojacket_v1 pin sad at left3
    "I'm shaking my head before she even finishes her sentence."
    mckorin "You go on. I still need to acclimate."

    show ecmc nojacket_v1 pin basic at left3
    "I look over at the carefree and bouncing group."

    show ecmc nojacket_v1 pin determined at left3
    mckorin "I'm just a little nervous at the thought of dancing right now."

    show korin casual pin smile at right3:
        xoffset -80
    ko "Fine. But don't go anywhere! I'm coming back for you."

    show korin casual pin smirk behind ecmc at right3:
        xoffset -80
        ease 0.6 xoffset -220
        pause 0.1
        parallel:
            ease 0.8 xoffset 50
        parallel:
            linear 0.8 alpha 0.0
    "She brushes her hand against my arm, and my skin tingles after her touch is gone."
    hide korin
    "I order a drink for myself and sip it as I watch the dance floor."

    hide ecmc
    show ecmc nojacket_v1_cu angry_cu at ecmc_cu
    "(Relax, [genericfn]. You have to relax. RELAX!)"
    hide ecmc

    show korin casual pin smile at centre
    "My eyes find Korin in the crowd."

    show korin casual pin smile at centre:
        easein 0.5 xoffset -50
        easein 0.5 xoffset 0
    "She's bouncing to the beat, shaking her body to the rhythm. Her hair shimmers in the circling lights."
    "Looking at her...I find I can catch my breath again."


    hide korin
    show ecmc nojacket_v1_cu smile_cu at ecmc_cu
    "(Huh. Maybe Korin was right about this sort of thing being therapeutic.)"
    hide ecmc

    stop music
    play music ecmcalmeveryday3
    "After a few songs, the music shifts to something slower and smoother."

    show korin casual pin smile at centre
    "Some of the trainees take the opportunity to take a break, but Korin's still out there...and I'm still watching her."

    hide korin
    show korin casual_cu smirk_cu at korin_cu
    "Her eyes find mine. She winks at me and keeps dancing."
    hide korin

    show korin casual smile at centre:
        easein 0.6 xoffset 30
        easein 0.6 xoffset -50
        easein 0.4 xoffset -30
    "I'm fixated. Her movements are slow, silky...she's exactly in her element."
    "I don't know what to do, but I don't look away from her."
    "For a moment, it feels like we're two different people. Just strangers catching each other's eyes across the club."

    hide korin
    show ecmc nojacket_v1_cu sad_cu at ecmc_cu
    "(I could just...make my way to her and start dancing with her.)"
    hide ecmc

    stop music
    play music ecmaction2

    show ecmc nojacket_v1 pin surprised at centre
    "And just as the thought enters my head, the song ends, and something more upbeat begins."

    hide ecmc
    show korin casual smile at centre
    "And to my surprise, Korin stops dancing."

    hide korin
    show ecmc nojacket_v1 pin determined at left3
    show korin casual smile at right3:
        alpha 0.0 xoffset 150
        parallel:
            linear 0.6 alpha 1.0
        parallel:
            easein 0.6 xoffset 0
    "Our eyes still locked, she thinks for a moment...then nudges through the crowd and makes her way straight toward me."
    "She's grinning, breathless."
    ko "Tell me you're acclimated enough, now."

    show ecmc nojacket_v1 pin surprised at left3
    mckorin "Huh?"
    ko "Come dance with me!"

    show ecmc nojacket_v1 pin sad at left3:
        easein 0.4 xoffset 30
        easein 0.4 xoffset -30
        easein 0.4 xoffset 0
    "I look around, anxious."

    show ecmc nojacket_v1 pin surprised at left3
    mckorin "...Me?"
    "I notice that all the rest of the trainees have paired off with one another or returned to the bar."

    hide ecmc
    hide korin
    show korin casual_cu smile_cu at korin_cu
    ko "Just us. You don't have to worry about anybody else."
    "She holds out her hand to me."
    hide korin

    $menuhideborder = True
    menu korins1e7c2:
        "A. Dance with Korin." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin casual_cu smile_cu at korin_cu
            "I take Korin's hand. She pulls me, but I resist, just for a second..."
            hide korin

            show ecmc nojacket_v1_cu sleep_cu at ecmc_cu
            "...As I throw back the rest of my drink."

            show ecmc nojacket_v1_cu smile_cu at ecmc_cu
            mckorin "Okay, let's do this."
            hide ecmc

            show korin casual_cu smile_cu at korin_cu
            ko "Atta girl!"
            hide korin

            show ecmc nojacket_v1 pin smile at left3:
                pause 0.2
                easein 0.4 xoffset 180
            show korin casual smile behind ecmc at right1:
                ease 0.4 xoffset 100
            "I stumble after Korin, but her hand stays steady in mine, and after a second it feels like I'm gliding."
            "She stops when we're fully in the thick of it, surrounded by other people."

            show ecmc nojacket_v1 pin surprised at left3:
                xoffset 180
                ease 0.2 xoffset 230
                easein 0.2 xoffset 220
            "I plant my feet to stop myself from colliding with her."

            hide ecmc
            hide korin
            show korin casual_cu smile_cu at korin_cu
            "She smiles and leans in so I can hear her over the noise."
            ko "You need my help?"
            hide korin

            show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
            "I nod eagerly."
            hide ecmc

            show ecmc nojacket_v1 pin surprised at left1:
                pause 0.2
                easein 0.4 xoffset 50
            show korin casual smile behind ecmc at right1:
                easein 0.4 xoffset 50
            "She takes my hands in hers and starts making small movements to the rhythm of the song."

            stop music
            play music ecmmctheme

            hide korin
            hide ecmc
            show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
            mckorin "I can't dance!"
            hide ecmc

            show korin casual_cu smile_cu at korin_cu
            ko "We're not dancing! We're just moving to the beat."
            hide korin

            show ecmc nojacket_v1 pin surprised at left1
            show korin casual smile behind ecmc at right1:
            "She pulls back and keeps eye contact with me, and I feel myself start to loosen up."

            show korin casual smile behind ecmc at right1:
                xoffset 0
                ease 0.6 xoffset 40
                ease 0.6 xoffset 0
                repeat
            ko "Back and forth, right? Now, move your shoulders a bit..."
            show ecmc nojacket_v1 pin determined at left1
            "I watch her and keep watching her."

            stop music
            play music ecmupbeateveryday4
            show ecmc nojacket_v1 pin surprised at left1
            show korin casual smile behind ecmc at right1
            "Korin snickers at me and puts her hand on my shoulders, willing me to follow her movements."

            show ecmc nojacket_v1 pin surprised at left1:
                ease 0.4 xoffset 80
            "And the only reason I give in is to take my mind off of how much I just want to slip my arms around her waist and move closer."

            hide ecmc
            hide korin
            show korin casual_cu smile_cu at korin_cu
            ko "Yeah, like that! Now..."
            "My heart beats faster as Korin crosses around behind me, trailing her hand down my arm."

            show korin casual_cu smirk_cu at korin_cu
            ko "Keep moving. Acclimating, right?"
            "I nod, then lurch a bit as I feel Korin gently nudge the back of my knees with her leg."

            show korin casual_cu smile_cu at korin_cu
            ko "Easy, Scraps. I got you...but you've got to bend your knees to loosen up next!"
            ko "You want to be able to bounce...like this!"

            hide korin
            show ecmc nojacket_v1 pin determined at left1plus
            show korin casual smile at right1plus
            "She steps away from me to give herself some room and illustrates what she means."

            show ecmc nojacket_v1 pin sad at left1plus:
                ease 0.4 yoffset 20
                ease 0.4 yoffset 0
            show korin casual sad at right1plus
            "I try bending my knees, bouncing...but hesitate. Korin leans in, looking concerned."

            hide ecmc
            hide korin
            show korin casual_cu sad_cu at korin_cu
            ko "What's up?"
            hide korin

            show ecmc nojacket_v1_cu sad_cu at ecmc_cu
            mckorin "It just feels so weird! Like I'm going to do it wrong..."
            hide ecmc

            show korin casual_cu sleep_cu at korin_cu
            "Korin shakes her head, insistent."

            show korin casual_cu smile_cu at korin_cu
            ko "There's no wrong way! You're doing great!"
            hide korin

            show ecmc nojacket_v1_cu smile_cu at ecmc_cu
            "I give in to the rhythm, following other dancers and throwing my arms over my head."
            hide ecmc

            show korin casual_cu smile_cu at korin_cu
            "Korin dances with me, stunning with more playful and confident moves."

            stop music
            play music ecmkorintheme

            "As the beat changes to something even faster, Korin gets close to me again."
            ko "You've got some moves, Scraps!"

            hide korin
            show ecmc nojacket_v1_cu surprised_cu at ecmc_cu
            "(I do??)"
            hide ecmc

            show korin casual_cu smile_cu at korin_cu
            ko "When you're not thinking about it, and you just lose yourself in the music..."

            show korin casual_cu smirk_cu at korin_cu
            ko "You look kind of amazing."
            hide korin

            window hide
            scene bg ecm_korin_s1_ei3 with fade:
                zoom 1.35 align(0.5, 1.0)
                linear 4.0 yoffset 1160
            pause
            window show
            "Those words from her are the confidence boost I need to keep going, dancing faster, completely losing myself in the music."
            "We aren't dancing too close, and I can't tell from the flashing lights..."
            "But it feels like she's looking right at me. Not watchful, like she's protecting me, but..."
            "Like she's interested in seeing the real me come out of my shell."
            "And like magic, I feel my concerns about D.I.V.A.A. just slip away."
            "And it feels like it's just me, Korin, and the music. And it's everything I need right now."

            scene bg ecm_bar_off at bg
            show korin casual_cu smirk_cu at korin_cu
            with fade
            stop music
            play music ecmintrotrack
            "The song changes again. Korin looks at me, testing to see if I've had enough yet."
            "But I shake my head and adjust to the new tempo."

            show korin casual_cu smile_cu at korin_cu
            "Korin grins and does the same."
            hide korin

            show ecmc nojacket_v1_cu smile_cu at ecmc_cu
            "(I feel like this is some crazy alternate universe...)"
            "(Like we really are just two people who met tonight and are hitting it off on the dance floor.)"

            show ecmc nojacket_v1 pin smile at left1plus
            show korin casual pin smile at right1plus
            "Finally, I have to take a break. I signal to Korin, and together we make our way out of the thick of it."
            ko "That was amazing! You did great!"

            show ecmc nojacket_v1 pin surprised at left1plus
            "I stop to catch my breath."
            mckorin "I feel like I was holding you back...you were amazing."

            show ecmc nojacket_v1 pin smile at left1plus
            "Korin shakes her hair back and flashes me a brilliant smile."
            ko "Well, it helps when you have a good partner."
            "She looks back over her shoulder at the dance floor, then gives me a wink."

            show korin casual pin smirk at right1plus
            ko "Come find me if you decide you want to dance again."

        "B. Stay a wallflower.":
            $menuhideborder = False
            show ecmc nojacket_v1 pin surprised at left3
            show korin casual sad at right3
            mckorin "I can't! No way..."
            "Korin pouts. It's exaggerated to make me laugh, but I can see she's a little dejected too."
            show korin casual smirk at right3
            ko "Fine. I'll be right out there if you change your mind, though..."

    hide ecmc
    hide korin

    stop music
    play music ecmcalmeveryday2
    "The rest of the night passes in a blur."

    show ecmc nojacket_v1_cu smile_cu at ecmc_cu
    "(Okay. Even if I couldn't fully unwind tonight, I'm glad Korin brought me out.)"
    hide ecmc

    scene bg ecm_office_hq_on at bg with wiperightdissolve
    stop music
    play music ecmcalmeveryday1
    "The next day, I search for the missing hard drive around the office."

    show ecmc nojacket_v2 pin angry at centre:
        easein 0.6 yoffset 50
    "I pick through trash cans when others aren't looking, and even get brave and check under desks and chairs when I'm able."
    "I'm doing my best to stay out of trouble."

    show ecmc nojacket_v2 pin surprised at centre:
        yoffset 50
    trouble "Hey, what are you doing under my desk?!"

    show ecmc nojacket_v2 pin sad at centre:
        yoffset 50
        easein 0.3 yoffset 0
        easein 0.3 yoffset 40
        easein 0.6 yoffset 0
    "I bump my head on the underside and pull myself up, wincing--and hear laughter."

    show ecmc nojacket_v2 pin sad at left3
    show enver casual smile at right2
    en "Did I scare ya?"
    mckorin "I'm in enough trouble already. Yes."
    "I explain to him that I'm looking for the missing hard drive."

    show enver casual sad at right2
    en "Yeah, Korin pulled me aside yesterday and told me to keep an eye out for it."

    show enver casual smile at right2
    en "You're really lucky to have her in your corner, you know?"

    show ecmc nojacket_v2 pin smile at left3
    mckorin "No, I know. Last night was so fun..."
    "Enver raises his eyebrows."
    en "Last night?"

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "I mean...everyone had fun! Korin made sure we all had fun."

    show enver casual sad at right2
    "Enver stares at me for a moment, before tipping his head back."

    show enver casual smile at right2
    en "Ohhh, the rookie...outing thing! That was last night..."
    en "I thought you were saying you went on a date with Korin, or something."

    show ecmc nojacket_v2 pin angry at left3
    "Mortified, I shush him loudly."
    en "Where'd she take you guys?"

    show ecmc nojacket_v2 pin basic at left3
    mckorin "It was this club called the Catalyst, or something. I don't know."
    en "But you had fun?"

    show ecmc nojacket_v2 pin angry at left3
    mckorin "I didn't say that."
    en "You...literally did. When I said how lucky you were to have Korin in your corner."
    mckorin "Yeah, well, I was just stating the obvious! It is nice to have her in my corner."
    en "And she was in your corner last night, huh?"

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "Don't say it like...!"

    show ecmc nojacket_v2 pin blush angry at left3
    "I huff and look around, but nobody else nearby seems to be paying attention."

    show ecmc nojacket_v2 pin blush embarrassed at left3
    mckorin "The outing was fun."

    hide enver
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(Because Korin made it fun.)"
    hide ecmc

    show ecmc nojacket_v2 pin blush embarrassed at left3
    show enver casual smile at right2
    mckorin "I had a good time..."

    hide enver
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(I wouldn't have had a good time without Korin. I wouldn't have set foot in a place like that without her.)"
    hide ecmc

    show ecmc nojacket_v2 pin angry at left3
    show enver casual smile at right2
    mckorin "That's it. End of story."

    show enver casual angry at right2
    "Enver narrows his eyes at me and sips his coffee."

    show enver casual smile at right2
    "When he lowers his cup, I see the grin plastered on his face and point my finger at him."
    mckorin "Don't say it. Don't you dare."
    en "I didn't say anything."
    mckorin "A person can admire someone and not...not be..."
    mckorin "Crushing? Crushing hard?"

    hide ecmc
    hide enver
    $menuhideborder = True
    menu korins1e7c3:
        "A. I am NOT crushing":
            $menuhideborder = False
            show ecmc nojacket_v2 pin angry at left3
            show enver casual smile at right2
            mckorin "I am NOT crushing! What is this, the third grade? Grow up."
            en "Aww. What are you gonna do, tell the teacher on me? Oh, wait..."

        "B. It's just a tiny...something":
            $menuhideborder = False
            show ecmc nojacket_v2 pin angry at left3
            show enver casual smile at right2
            mckorin "I...I just admire her!"
            mckorin "She's cool, and smart, and charming, and funny, and pretty, and..."
            "I trail off, realizing the hole I'm digging myself into."
            en "...No, go on. You're doing great!"

        "C. Say nothing":
            $menuhideborder = False
            show ecmc nojacket_v2 pin angry at left3
            show enver casual smile at right2
            "I fold my arms and give him my most withering look."
            en "Can't even respond, huh? Oooh, you got it BAD!"

    show ecmc nojacket_v2 pin angry at left3
    show enver casual smile at right2
    "I shush him. Trying to stifle his laugh only makes him laugh harder."
    en "Look, I get it. Korin's really cool, and you've been working closely together. She must be on your mind a lot..."
    mckorin "No more than normal."
    "Enver raises an eyebrow at me."
    en "Have you noticed you've checked that trash can for that hard drive three times since you've been standing here?"
    en "Either she has some effect on your concentration, or you're not cracked up to be a real detective, after all."

    show ecmc nojacket_v2 pin blush surprised at left3
    mckorin "Maybe I'm just being thorough!"
    en "Why don't you go talk to her? Tell her what a good time you had? I bet it'd mean a lot to her."

    hide ecmc
    show ecmc nojacket_v2 pin sad at left3
    mckorin "No. She knows it was fun, and...I don't want to bug her."

    show enver casual sad at right2
    "Enver cups a hand to his face and boos me."

    show enver casual smile behind ecmc at right2
    en "Come on! You miss all the shots you don't take! Go find Korin and carpe that diem!"

    show ecmc nojacket_v2 pin angry at left3:
        easein 0.4 xoffset 290
    "I've had enough. I roll my eyes and shove him--but not too hard."
    mckorin "Don't you have work to do?"

    show enver casual smile at right2:
        parallel:
            ease 0.4 xoffset 200
        parallel:
            linear 0.4 alpha 0.0
    "Enver checks the time and darts off."

    hide enver
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Is he right? Do I really have a crush?)"
    hide ecmc

    scene bg ecm_records_room_on at bg with wiperightdissolve
    stop music
    play music ecmkorintheme
    "To my surprise, I do as Enver suggests and seek out Korin."

    show korin nojacket pin basic at centre
    show bird normal at birdbob:
        pos (710, 260)
    "She's not in her office. I find her in the records room, where I found her once before."

    show korin nojacket pin smile at centre
    "She gives me a cheeky smile as I approach."

    show ecmc nojacket_v2 pin smile at left3
    show korin nojacket pin smile at right2
    show bird normal at birdbob:
        pos (900, 260)
    ko "Let me guess. You need my help, and this time you have the guts to just ask me about it?"
    mckorin "Actually, no."

    show ecmc nojacket_v2 pin embarrassed at left3
    "I look up into her soft brown eyes, and suddenly my courage is sapped from me."
    "I look down at Baby Bird, who is interfacing with a bank of servers."

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "But, um...what are you doing here? BB getting some files for you?"
    ko "Same as when you found me here before, yeah."
    mckorin "Do you...I mean, is BB...have you noticed any other issues with it since I last fixed it?"

    show korin nojacket pin smirk at right2
    "Korin raises an eyebrow at me."

    hide korin
    hide bird
    hide ecmc
    show ecmc nojacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(Oh, no. She can see right through me!)"
    hide ecmc

    show ecmc nojacket_v2 pin embarrassed at left3
    show korin nojacket pin smirk at right2
    show bird normal at birdbob:
        pos (900, 260)
    ko "[genericfn], what's up? Is this about last night?"

    show ecmc nojacket_v2 pin sleep at left3
    "I let out the breath I've been holding."

    show ecmc nojacket_v2 pin determined at left3
    mckorin "Yeah."

    show korin nojacket pin sad at right2
    ko "Look, if it wasn't your speed, I'm--"

    show ecmc nojacket_v2 pin surprised at left3
    mckorin "No! That's not it."
    mckorin "I mean, it wasn't my type of place at all. But..."

    show ecmc nojacket_v2 pin smile at left3
    mckorin "I just came by to say thanks for making it feel like it could be. I had a lot of fun."

    show korin nojacket pin smile at right2
    "Korin takes in my words...and smiles."
    ko "Well, maybe we'll do it again sometime."

    show ecmc nojacket_v2 pin smile at left3:
        linear 0.6 xoffset -100
    "I nod and make ready to head for the door."

    show ecmc nojacket_v2 pin surprised at left3:
        xoffset -100
    show korin nojacket pin surprised at right2
    ko "Hey, wait...you're leaving?"

    show ecmc nojacket_v2 pin surprised at left3:
        easein 0.4 xoffset 0
    "Eagerly, I turn back."

    show ecmc nojacket_v2 pin embarrassed at left3
    mckorin "I don't {i}have{/i} to. I just thought you were busy."

    show korin nojacket pin basic at right2
    "Korin shrugs and shakes her head."

    show korin nojacket pin smile at right2
    ko "I've always got time for you."

    show ecmc nojacket_v2 pin smile at left3
    "I mirror her, leaning against one of the support beams. Her next question melts the grin from my face."
    ko "How's the search going?"

    show ecmc nojacket_v2 pin embarrassed at left3
    mckorin "It's...going. No strong leads yet."

    show korin nojacket pin smirk at right2
    ko "I've already let some friends know you could use a little extra help."
    mckorin "Yeah, Enver said as much. I appreciate it."
    mckorin "Just...remember to be careful, okay? I don't want you to get in trouble for helping me."

    show korin nojacket pin smile at right2
    "Korin smiles in grim acknowledgment and shrugs off her worries."
    ko "Look, I think you should go see Eko at the lab."
    ko "I discussed some options with her this morning. I think she might have worked out how to find the drive."

    scene bg ecm_office_lab_on at bg
    show eko casual pin glasses smile at centre
    with wiperightdissolve

    stop music
    play music ecmekotheme

    "I head up to Eko straight away. She excitedly tells me what she's figured out."

    show ecmc nojacket_v2 pin basic at left3
    show eko casual pin glasses smile at right3
    ek "After talking it over with Korin, I recalled that all evidence is electronically logged with a tamper-proof RFID tag."
    mckorin "Right. I know about those."

    hide eko
    hide ecmc
    show ecmc nojacket_v2_cu angry_cu at ecmc_cu
    "(Those damn tags can make a Scrapper's life hell sometimes.)"
    hide ecmc

    show ecmc nojacket_v2 pin surprised at left3
    show eko casual pin glasses smile at right3
    "Eko is about to explain something further when an idea strikes me."
    mckorin "Wait, yeah. Couldn't we use those sensors to reverse the process with some kind of geolocation program?"

    show ecmc nojacket_v2 pin smile at left3
    show eko casual pin glasses smile at right3:
        easein 0.2 yoffset -30
        easein 0.2 yoffset 0
    ek "Those were my thoughts exactly!"
    ek "I implement that search myself, but seeing as you're a trainee, I saw it as a potentially valuable learning experience."
    mckorin "If I can poke around in the tagging system--"
    ek "--With my supervision."

    show ecmc nojacket_v2 pin headset smile at left3
    "I nod, pulling on my ARCware."
    mckorin "I can write up a program and find it!"

    hide eko
    hide ecmc
    "Eko flits around the lab for the next hour or so, occasionally checking back over my shoulder and giving me pointers."

    show ecmc nojacket_v2 pin headset determined at left1plus
    show eko casual pin glasses basic at right1plus
    "Finally, when I think it's ready, I run the program."

    show ecmc nojacket_v2 pin headset surprised at left1plus
    "On our first try--we get a hit!"
    mckorin "It's...on the roof?"

    show eko casual pin glasses surprised at right1plus
    "Eko tilts her head, clearly confused. She straightens up."
    ek "That's...odd."

    show ecmc nojacket_v2 pin headset surprised at left1plus:
        easein 0.4 xoffset -55
        linear 0.2 xoffset -50
    "I get to my feet, but she puts up a hand."

    show eko casual pin glasses smile at right1plus
    ek "I have roof access. There's sensitive equipment up there, so I'm going to ask that you remain here while I retrieve the drive."

    hide eko
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Right. Probably smart not to risk ruining some other piece of important equipment for D.I.V.A.A..)"
    hide ecmc

    show ecmc nojacket_v2 pin headset smile at left1plus:
        xoffset -50
    show eko casual pin glasses basic at right1plus
    "Eko sweeps a hand across my terminal and gives me access to a hidden set of files."

    show ecmc nojacket_v2 pin headset surprised at left1plus:
        xoffset -50
    mckorin "Is this...security cam footage?"
    ek "If you'd like to check who was headed for the roof on the day it went missing."
    ek "Meanwhile, I'll be right back..."

    show eko pin glasses basic at right1plus:
        parallel:
            easein 0.6 xoffset 150
        parallel:
            linear 0.6 alpha 0.0
    pause 0.4
    "I find the file I'm looking for. I click to open it..."
    hide eko
    hide ecmc

    stop music
    play music ecmplottwist2

    "{i}BZZT!!{/i}"

    show white at bg with dissolve
    hide white with dissolve
    "...And my terminal overloads and blows apart."

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
