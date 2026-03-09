label lexi_season1_episode3:

    $tbc = False
    scene bg msc_beach_bar_day at bg with dissolve
    play music mscsuspense2

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show mscmc jacket_hairdown surprised at left3
    show hannah casual angry at right3
    mclexi "{i}Backstabber{/i}? That's a bit much, isn't it?"
    show hannah casual sleep
    "Hannah purses her lips and rolls her eyes."
    show hannah casual angry
    hj "Hardly. Imagine you get sent to jail for five years because the 'partner' you trusted betrayed you."

    hj "Then, while you rot in a cell, she's off enjoying her life with YOUR money."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(When Hannah puts it that way, I guess Lexi really is an evil backstabber in her eyes.)"
    show mscmc jacket_hairdown_cu basic_cu
    "(There has to be more to the story. Lexi deserves to tell her side too.)"
    show mscmc jacket_hairdown_cu sad_cu
    "(And there's just something about Hannah that doesn't sit right with me.)"
    show mscmc jacket_hairdown basic at left3
    show hannah casual smile at right3
    hj "I'm sure she's {i}already{/i} used you to get something she wanted. I heard from Ned that there was treasure involved."
    show mscmc jacket_hairdown angry
    mclexi "She didn't use me for anything. She asked for my help and I gave it to her, she didn't screw me over."

    hj "Then what? After she got what she wanted, what happened?"
    hide mscmc
    show jerry casual basic at left3
    "As she asks her question, Jerry glances at me seeing if I want him to intervene but I subtly shake my head."
    hide jerry
    hide hannah
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(... Then she disappeared for six months.)"
    show mscmc jacket_hairdown_cu angry_cu
    "(But Lexi isn't just some con-artist that used me. She's my friend, maybe more than that, and I'm going to hear her side of things.)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3
    show hannah casual smile at right3
    mclexi "She left for a bit, but..."
    show mscmc jacket_hairdown sad
    show hannah casual angry
    hj "She's back now, huh? Knowing her, she probably hasn't told you anything about what she's doing here or why she's back."
    hide mscmc
    hide hannah
    menu lexis1e3c1:
        "A. Lie.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show hannah casual basic at right3
            mclexi "She had another job lined up so she had to go."
            show hannah casual smile
            hj "Another job? Hm. You seem new to this lifestyle, but it’s pretty rare for jobs to just be lined up."
            show hannah casual basic
            hj "Treasure and money don’t grow on trees."


        "B. Evade the question.":
            $menuhideborder = False
            show mscmc jacket_hairdown basic at left3
            show hannah casual basic at right3
            mclexi "Why are you in town, Hannah?"
            show hannah casual smile
            hj "Seems like something girlfriends would discuss with each other, like, where they’ll be one day to the next."
            show mscmc jacket_hairdown angry
            show hannah casual angry
            mclexi "Even if we were dating, it’s not like I’m her mom. I don’t need to know everything she does."



        "C. It's none of Hannah's business.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left3
            show hannah casual basic at right3
            mclexi "It's really none of your business what Lexi and I talk about."
            show mscmc jacket_hairdown angry
            hj "I feel like it's my duty to protect naive young women from making the same mistakes I made, namely trusting Lexi."

            mclexi "Well, it's not."

    show mscmc jacket_hairdown angry at left3
    show hannah casual smile at right3
    hj "See? You're defending Lexi even though you can't even give me a straight answer. And now that she's back..."
    show hannah casual sleep
    "Hannah takes a long sip of her mimosa before letting out a delighted sigh."
    show mscmc jacket_hairdown surprised
    show hannah casual smile
    hj "She probably made it seem like it's for you. The reason she's back I mean."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Hannah's almost too good at knowing what to say, what buttons to press. Maybe she's telling the truth about Lexi, but she's hiding something.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show hannah casual basic at right3
    mclexi "She never said she came back for me. We just had a few drinks last night."
    show hannah casual smile
    hj "Sounds like Lexi's started her process of gradual manipulation to get something she wants. Something obtained illegally, most likely."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What is with this woman? Why is she so determined to get into my head about Lexi?)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show hannah casual angry at right3
    mclexi "I think Lexi's changed since five years ago. You don't even know her anymore."
    show hannah casual smile
    "Hannah chuckles half-heartedly."

    hj "There was a time I would have probably said the same thing about someone like her. But look where that got me."
    show mscmc jacket_hairdown surprised
    show hannah casual basic
    hj "You seemed really interested in that spherical mer antique."

    hj "Almost as if you've been casing it out."

    mclexi "That orb is from the mer world? Wait, you think I'm planning to steal it?"

    "Hannah shrugs and takes another sip of her drink acting unconcerned, bet her fingers gripping the champagne flute are all very tensed."
    show hannah casual smile
    hj "If a certain someone were to steal it and then blame you, it would look awfully suspicious how much you've been hanging around there."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Is Hannah implying that Lexi set her up?)"
    show mscmc jacket_hairdown_cu sleep_cu
    "(Whatever, I'm done listening to her.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show hannah casual smile at right3
    mclexi "I have to go."
    show mscmc jacket_hairdown basic at left3
    "I slide off of my barstool and start heading towards the boardwalk."
    show mscmc jacket_hairdown angry
    hj "I'm on your side. Oh, and one more thing..."
    show hannah casual smile
    "I half-turn back to face Hannah, who is holding out my unfinished smoothie."
    hide mscmc
    hide hannah
    show hannah casual_cu basic_cu at hannah_cu
    hj "Don't forget your smoothie. I can't imagine your hangover after drinking so much last night."

    "She smiles sweetly at me as I quickly, and maybe a little roughly, grab the to-go cup from her."

    hj "See you around..."
    hide hannah
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Hopefully not...)"
    scene bg msc_surf_shop_day at bg
    "I trudge to the surf shop as Hannah's words echo in my mind."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Trina's dated some shitty people. Maybe she'll know if Lexi is a red flag.)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3
    show trina casual basic at right3
    mclexi "Triiiiina..."
    show mscmc jacket_hairdown sad:
        easein 0.4 xpos stagepos[1]+50
    show trina casual smile
    "I whine my bestie's name as I plop down next to her behind the checkout counter."
    show trina casual sad
    so "Oh boy. What's going on? I haven't seen you this down since Lexi left."
    hide mscmc
    hide trina
    show lexi casual surprised at centre
    lx "Yeah, what's going on?"

    "I snap around and look behind me to see Lexi standing in the shop door."
    show mscmc jacket_hairdown surprised at left3
    show lexi casual surprised at right3
    stop music fadeout 1.0
    play music mscbeach
    mclexi "I... I have a hangover from last night is all. Do you not?"
    show mscmc jacket_hairdown smile
    show lexi casual smile
    "Lexi shrugs and takes a sip from a water bottle she's holding."

    lx "Dunno. But I'm glad you're here! I came looking for you earlier, but Trina said you'd gone out."
    show mscmc jacket_hairdown embarrassed
    mclexi "I just went to get a smoothie from Jerry's."
    hide lexi
    show trina casual smile at right3
    so "Hangover Blaster?"

    "I nod and sip the half-finished smoothie."
    show mscmc jacket_hairdown grin
    mclexi "Hangover Blaster."

    so "I can't remember the last time you needed one of those!"
    hide mscmc
    show lexi casual smile at left3
    lx "I guess we partied a little hard last night."

    "Trina chortles in response, they seem to get along."

    so "She needed it. All [genericfn]'s been doing since you left is been surfing, surfing, surfing."
    show lexi casual surprised
    so "When she's not out on the waves, she's reading about it, or obsessively taking care of her board."
    hide lexi
    show mscmc jacket_hairdown angry at left3
    show trina casual sleep
    mclexi "You make it sound like that's all I do! I do other stuff too!"
    hide trina
    show mscmc jacket_hairdown grin
    show lexi casual bigsmile at right3
    lx "Oh? Like what?"

    menu lexis1e3c2:
        "A. I help with the shop!":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left3
            show lexi casual bigsmile at right3
            mclexi "I help with the shop!"
            hide lexi
            show trina casual smile at right3
            so "Yeah, my surf shop. Where I sell surfboards and surfing paraphernalia."
            show mscmc jacket_hairdown embarrassed
            "My cheeks flush from embarrassment and annoyance."
            show mscmc jacket_hairdown smile
            mclexi "It’s not my fault that’s what you sell! And what’s wrong with reading a surf magazine..."



        "B. I visit the museum!":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi casual bigsmile at right3
            mclexi "I've been going to the museum a lot!"
            show lexi casual smile
            "Lexi's eyebrow arches slightly at the mention of the museum, but she doesn't say anything."
            hide lexi
            show mscmc jacket_hairdown smile
            show trina casual smile at right3
            so "Ok, that's true, you have been going there a lot lately."
            show trina casual angry
            so "But it doesn't change the fact that as soon as you get back you're focused on surfing again, all the time!"
            show trina casual smile
            mclexi "At least it's something!"



        "C. Stuff!":
            $menuhideborder = False

            mclexi "I do stuff!"

            so "Whoa, calm down there killer. Don’t be too specific or anything."

            "I glare at Trina and give her a playful shove."

            mclexi "I have to be in tip-top shape. Stop judging me!"
    hide mscmc
    hide trina
    hide lexi
    show mscmc jacket_hairdown grin at left3
    show lexi casual bigsmile at right3
    lx "I mean, as long as you love what you spend your time doing, that's all that matters, right?"
    hide mscmc
    hide lexi
    show trina casual_cu smile_cu at trina_cu
    "Trina nods as if Lexi just said something super profound."
    hide trina
    show mscmc jacket_hairdown smile at left3
    show lexi casual bigsmile at right3
    lx "Anyways, I'll be right back. Bathroom break!"
    show lexi casual bigsmile at out_right
    hide lexi
    "As Lexi disappears into the back of the shop, Trina grabs my hand and pulls me closer to her."
    hide mscmc
    show trina casual_cu basic_cu at trina_cu
    so "So, Lexi's back. How are you feeling? You ok?"

    "Trina whispers the question while keeping an eye on the back to make sure Lexi doesn't surprise us."
    show mscmc jacket_hairdown sleep at left2
    show trina casual basic at right2
    mclexi "I don't know. She got back last night. I mean we had fun, but she ghosted me for six months. I don't know if I can trust her?"
    show mscmc jacket_hairdown smile
    so "That's valid and I'm not a fan of ghosting. But you seem happy, and you actually went out last night."
    show mscmc jacket_hairdown surprised
    mclexi "I am happy! It's just complicated."
    show trina casual smile
    so "Don't overthink things for now. Have fun being happy. She gets you out of your comfort zone, which you need."
    show mscmc jacket_hairdown embarrassed
    mclexi "It was fun..."
    show trina casual smile behind mscmc:
        easein 0.4 xpos stagepos[1]-15
    "Trina nods and gives me a tight hug."
    hide mscmc
    hide trina
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I need to tell Lexi about seeing Hannah this morning.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left3
    show trina casual basic at right2:
        xpos stagepos[1]-15
    show lexi casual smile at right3, right_in
    lx "I'm back! What'd I miss?"
    show mscmc jacket_hairdown sleep
    show trina casual smile
    show lexi casual surprised
    so "Nothing much! Just babying my bestie here through a funk."
    show mscmc jacket_hairdown smile
    show lexi casual basic
    "Trina gives my hand one more small squeeze before letting me go."
    show lexi casual sad
    lx "Aw... and here I was hoping [genericfn] would want to hang with me."
    show mscmc jacket_hairdown embarrassed
    show lexi casual embarrassed
    so "No! Y'all should hang! Just make sure she drinks some water. [genericfn] is thirsty."
    show mscmc jacket_hairdown smile
    show lexi casual bigsmile
    mclexi "Yeah, Lexi, I'm down to hang."
    show mscmc jacket_hairdown sleep
    so "Get out of here you crazy kids!"
    scene bg msc_mchomeentryway_lightson at bg with wiperight
    stop music fadeout 1.0
    play music mscromance
    "Lexi and I walk through the employee-only door at the back of the surf shop that leads to the rest of the building."
    show mscmc jacket_hairdown embarrassed at left2
    show lexi casual smile at right2
    mclexi "I can just grab some things and we can go out and do something. Do you want to come up?"

    lx "I'd follow you anywhere, lead the way."
    show mscmc jacket_hairdown embarrassed at left2, out_left

    "I blush a little as I start heading towards the stairs, expecting her to follow."
    hide mscmc
    show lexi casual smile at centre
    lx "Hey."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu:
        xpos 300
    show lexi casual_cu embarrassed_cu at lexi_cu:
        xpos 775
    "Lexi slinks towards me, then puts her hands on my shoulder and lightly pushes me up against the hallway wall."
    show mscmc jacket_hairdown_cu embarrassed_cu
    show lexi casual_cu smile_cu
    mclexi "Wh-?"

    "She leans her face in close to mine, her glistening red lips hovering so near to mine that I feel a shiver run through my whole body."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Whenever we're this close I can't think straight. Her smell, the way she feels pressed against me... She's intoxicating.)"
    show mscmc jacket_hairdown_cu sleep_cu
    "(Lexi, please, just freaking kiss me already.)"
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu:
        xpos 300
    show lexi casual_cu embarrassed_cu at lexi_cu:
        xpos 775
    lx "I want you to know how much I missed you. I wondered for a while if I was just romanticizing us, our time together, in my head..."
    show mscmc jacket_hairdown_cu embarrassed_cu
    lx "...but last night proved I didn't. Whenever I'm with you, everything is more vibrant somehow."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She thought about me while she was gone. I didn't make up this thing between us.)"
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
        xpos 300
    show lexi casual_cu embarrassed_cu at lexi_cu:
        xpos 775
    "I try to steady my breathing as I think about Lexi missing me, but my racing heart doesn't make it easy."
    show lexi casual_cu smile_cu
    "I wrench my eyes away from Lexi's lips and meet her gaze."
    show mscmc jacket_hairdown_cu sleep_cu
    "I can feel her soft breaths gently caressing my lips and it sends electricity running through my body, I press myself against her."
    show mscmc jacket_hairdown_cu embarrassed_cu
    "There's hunger in her eyes as they search mine, and I know my own must be reflected."
    show lexi casual_cu embarrassed_cu
    mclexi "I thought about you too, I wanted you to come back."

    mclexi "When you disappeared I almost thought what we had was all just a beautiful dream."
    show mscmc jacket_hairdown_cu grin_cu
    show lexi casual_cu smile_cu
    lx "I am pretty dreamy..."
    show mscmc jacket_hairdown_cu embarrassed_cu
    "We grin at each other, as I feel her hands explore my sides until one finds its way to my face and cups my cheek."
    show mscmc jacket_hairdown_cu surprised_cu
    lx "So, are you going to make a move?"

    mclexi "What do you mean?"
    show mscmc jacket_hairdown_cu embarrassed_cu
    lx "I want you to leave me without any doubt of your intentions."
    show mscmc jacket_hairdown_cu surprised_cu
    "I bite my lower lip, trying to find words to say."
    show mscmc jacket_hairdown_cu embarrassed_cu
    "I move to kiss her but she holds one finger up to my lips right before our mouths meet."
    hide mscmc
    hide lexi
    show lexi casual_cu smile_cu at lexi_cu
    lx "I want to play a game. You try and get me to give in to my desire for you first, and I'll try to get you to give in to yours first."

    lx "Don't worry, it's a game you learn by playing, do you want to play with me?"
    hide lexi
    $menuhideborder = True
    menu lexis1e3c3:
        "A. Play Lexi's sexy game!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xpos 300
            show lexi casual_cu embarrassed_cu at lexi_cu:
                xpos 775
            mclexi "I want you to give in to how much you want me. I want you to satisfy your longing for me."
            show mscmc jacket_hairdown_cu sleep_cu
            lx "What do you want me to do to you?"
            show mscmc jacket_hairdown_cu embarrassed_cu
            "I bring my lips to Lexi’s ear, I can see her pulse in her neck beating quickly and we’ve both started to pant a little."

            show lexi casual_cu smile_cu
            mclexi "I like it when you pin me against the wall like this, when you don’t hold back."

            lx "If you like that, I have some other things in mind that may… give you pleasure."
            show mscmc jacket_hairdown_cu embarrassed_cu
            show lexi casual_cu embarrassed_cu
            mclexi "I’ve got a few ideas of my own. You’re not the only one who likes to give."
            hide mscmc
            hide lexi
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi places her arm on the wall beside my head, boxing me in, as our hips press forcefully against each other."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "You said you missed me, didn’t you?"
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "I run my hand up Lexi’s arm that’s boxing me in and feel goosebumps form at my touch."

            lx "Do you want to hear me say it again?"
            show lexi casual_cu smile_cu
            "Lexi smiles rogueishly at me, as my hands travel over her shoulders up her long neck, and get lost in her hair."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(If she wants to tease me, I’ll tease her back, we’ll see who begs for it first.)"
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "I encircle Lexi’s lower waist with my arms and pull her as close as humanly possible, as she moans low and excited into my neck."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I want you and I know you want me, Lexi."
            show mscmc jacket_hairdown_cu sleep_cu
            "(I am so horny right now in this hallway.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi licks her lips before speaking huskily against my neck."

            lx "You like playing my game too though, the delayed gratification. How long can you hold out? Which one of us will give in first?"
            show lexi casual_cu embarrassed_cu
            "Lexi tilts her chin down and looks up at me, her bright eyes like beacons through her dark lashes."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I want all of her, right now, right here. I want to make her scream my name.)"

            mclexi "I’m having a hard time not giving in at this point, I’ll be honest."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "There’s a devious glimmer in Lexi’s eyes as she caresses my cheek, running her thumb over my lips, obviously pleased by my words."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her skin is always so warm. I want to touch everywhere that warmth emanates from.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "I like it when you’re feisty like this, you’re only like this when we’re alone. It’s very hot."

            "Lexi licks her lips as we trade glances at each other’s eyes and lips, both breathing heavily."

            "I tilt my head back slightly as she delicately traces her index finger down the length of my neck and then my chest."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "You bring it out of me."
            show mscmc jacket_hairdown_cu sleep_cu
            "I moan as Lexi wraps her hand firmly around my neck and brings her lips to my ear."
            hide mscmc
            show lexi casual embarrassed_cu at lexi_cu
            lx "We should find out what else I can bring out of you."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Oh god, yes, please Lexi, let’s do that.)"

            mclexi "Destroy me, I want it."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi cocks an eyebrow at my response and licks her lips with her perfect pink tongue."

            lx "Well, if you beg, I’ll consider it…"
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I can do that.)"
            hide mscmc
            "Lexi places a deep kiss at the corner of my mouth, still teasing me, not giving me her full mouth. Her lips are luscious against my skin."

            "My body trembles slightly as I wait for Lexi’s next move, my heart pounding in my ears with anticipation."
            show lexi casual_cu smile_cu at lexi_cu
            lx "I think I’ve got you right where I want you."

            "She whispers the words tauntingly, each sultry syllable sending jolts of bliss though my body."
            show lexi casual_cu embarrassed_cu
            lx "Say it. Say, ‘kiss me, Lexi.’"

            "I try to answer, but my lips tremble and my breath catches in my throat."
            show lexi casual_cu smile_cu
            lx "No? Well, maybe another time."

            lx "Don’t worry, I will kiss you, I’ll have all of you, I promise you that."

            "Lexi releases her hand from my neck and pulls back a very small amount so she still has me pressed to the wall."

            lx "We are connected after all, we’ve kissed under a full moon."
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu
            "I’d forgotten the mer-folklore Lexi had told me months ago in the middle of the night between kisses the beach under a full moon until now."

            "(Kissing under the full moon connects us for life… I didn’t think Lexi believed that though.)"
            hide mscmc
            show mscmc jacket_hairdown smile at left3
            show lexi casual embarrassed at centre:
                easein 0.4 xoffset +100
            "Lexi steps away form me, motioning our game is over, causing me to sigh as the sexual tension filling the hall begins to evaporate."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "If she doesn’t stay this time maybe I can leave with her when she goes."
            show mscmc jacket_hairdown smile at left3
            show lexi casual embarrassed at centre:
                xpos stagepos[1]+20
            mclexi "So the game just ends? Was there a winner?"
            show mscmc jacket_hairdown surprised
            show lexi casual smile
            lx "I think it was a win-win. Maybe you’ll get your winner’s prize upstairs…"
            show mscmc jacket_hairdown embarrassed at left3
            show lexi casual smile at centre
            pause
            show lexi casual:
                easein 0.4 xpos stagepos[1]+10
            "Lexi turns away and starts making her way up the stairs, swaying her hips as she goes and looking back over her shoulder at me smirking."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(She's such a tease!)"
            hide mscmc
            show mscmc jacket_hairdown embarrassed at left3
            show lexi casual bigsmile at centre:
                xpos stagepos[1]+30
            lx "Are you coming?"
            show mscmc jacket_hairdown grin
            show lexi casual embarrassed
            mclexi "I’ll follow you anywhere."
            show lexi casual embarrassed at right3, step_out

            "Lexi tries to hide her blush but I catch it as I follow her up to my room."
            hide lexi
        "B. Choke.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu:
                xpos 300
            show lexi casual_cu smile_cu at lexi_cu:
                xpos 775
            mclexi "Only bec-."
            show lexi casual_cu surprised_cu
            "I hold back a cough as I nervously swallow and choke on my own saliva."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Smooth, [genericfn], smooth.)"
            hide mscmc
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu:
                xpos 300
            show lexi casual_cu bigsmile_cu at lexi_cu:
                xpos 775
            lx "Ha! Are you okay?"
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu:
                xpos 300
            show lexi casual_cu smile_cu at lexi_cu:
                xpos 775
            mclexi "I'm fine."
            hide lexi
            hide mscmc
            show lexi casual bigsmile at right2, step_out
            show mscmc jacket_hairdown grin at left2, step_out

            "I try to laugh it off as Lexi leads the way and we head up the stairs to my room."
    scene bg msc_mc_bedroom_day at bg with wiperight
    stop music fadeout 1.0
    play music mscmctheme
    "In my room, I sit down on the bed for a moment to try and gather my thoughts."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I still need to tell Lexi that I met Hannah this morning!)"

    "(I need to communicate openly with her if I ever want there to be a chance of us having a deeper relationship.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2
    show lexi casual surprised at right2
    lx "Are you okay?"
    show mscmc jacket_hairdown sad
    mclexi "Yeah, I'm fine. I just... there's something I need to talk to you about."
    show mscmc jacket_hairdown basic
    show lexi casual basic:
        easein 0.4 xoffset -100
    "Lexi sits down next to me, more serious than I've seen her and giving me her full attention."

    lx "Okay, what's going on?"
    show mscmc jacket_hairdown sleep
    "I take a deep breath, steeling myself for the conversation to come."

    mclexi "I bumped in to Hannah this morning."
    show lexi casual sad
    "A slight frown appears on Lexi's face, but she doesn't say anything and lets me continue."
    show mscmc jacket_hairdown sad
    show lexi casual surprised
    mclexi "She said that you're back to steal a mer antique from the museum... and that you're only hanging with me to use me to get to it."
    show lexi casual angry
    "Lexi lets out an irritated sigh, but I can tell it's not directed at me."

    lx "Ugh. Of course she's trying to turn you against me."
    show mscmc jacket_hairdown surprised
    mclexi "I don't {i}think{/i} you'd use me like that, but are you only back to steal that orb that's on display?"

    lx "No."

    "Her response is sharp."
    show mscmc jacket_hairdown basic
    show lexi casual basic
    lx "I'll admit, when they first put it on display I did consider stealing it since it's mer in origin and that's kind of interesting..."

    lx "...but that didn't seem like a good enough reason to go after it. I'm not even sure it's worth that much on the deep market."
    show mscmc jacket_hairdown smile
    show lexi casual bigsmile
    lx "I like collecting things, but I also want other people to get to experience history, too. So I'm cool leaving some stuff to the museums."

    mclexi "It was made by merfolk. Does that mean it's magic?"
    show lexi casual sad
    lx "Not necessarily, and honestly, I couldn't tell you. I just recognize that it's mer craftsmanship but I'm not sure what it even is."
    show lexi casual basic
    lx "The orb is old, I don't know if there's any existing records of its original purpose. No one that's alive would remember, that's for sure."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Remember...)"
    scene bg msc_mcs_vision at bg
    stop music fadeout 1.0
    play music mscmcvisions
    "Remember... Remember... Suddenly, I'm falling backwards through water, deeper and deeper."

    "(How did I get here? I was just in my room, wasn't I?)"

    "My chest is screaming for air as I do everything I can to hold my breath, but it's too late."

    "Bubbles burst from my mouth as I exhale..."

    "But I can breathe! I'm at the bottom of the ocean but I can breathe!"

    "I look up and see the bright surface of the water and a figure circling slowly..."

    "It's a mermaid! I try to call out to them...."

    "But no sound comes out of my mouth."

    "I try to yell louder, but as I do strange music fills my ears and mind until I can't focus on anything else."

    "I feel like I'm suspended in an abyss, but I also feel calm, held."

    "A muffled voice seems to break through the fog in my mind."

    lx "[genericfn]! Hey!"

    "(Lexi's voice is so melodic. She sounds so far away...)"

    lx "Come back to me!"
    show lexi casual_cu surprised_cu at lexi_cu:
        alpha 0.5
    lx "[genericfn]!"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
