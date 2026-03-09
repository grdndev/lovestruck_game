label fiona_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_saloon_night_lights_people at bg
    play music wlltense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show wllmc coat angry at centre
    "My eyes flit to the exits I noted when I first came in."
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Hopping over the bar and into the back room is my best bet, I think.)"
    hide wllmc
    show wllmc coat angry at left3
    show diana casual smileglasses at right3
    "But as my muscles tense to move, the client smiles at me."
    show wllmc surprised
    $sidecharone = "Client"
    sid1 "I'm so glad I ran into you! I've been looking everywhere for Fiona Eichen. Do you know where she is?"
    "My hackles don't lower one bit."
    hide diana
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Never give a fellow away. That's rule one, and I'm not about to break it.)"
    hide wllmc
    show wllmc coat angry at left3
    show diana casual smileglasses at right3
    mcfiona "I know she's not here. Why are you asking?"
    show wllmc basic
    sid1 "Well I was hoping to get that reading from her."
    hide wllmc
    hide diana

    stop music fadeout 1.0
    play music wlleverydayupbeat3 fadein 1.0
    show diana casual_cu smileglasses_cu at diana_cu
    sid1 "I honestly couldn't believe it when I met THE Fiona Eichen. It was like destiny."
    hide diana
    show wllmc coat surprised at left3
    show diana casual smileglasses at right3
    mcfiona "'The' Fiona Eichen? Is she famous?"
    show diana surprisedglasses
    sid1 "Don't you know? She's the only psychic that the skeptic Rolf Wagner couldn't prove was fake."
    hide diana
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Damn, Fiona, you have some mighty fine skills.)"
    hide wllmc
    show wllmc coat surprised at left3
    show diana casual basicglasses at right3
    sid1 "You have to admit, it makes one very curious to know how she did it."
    show wllmc smallsmile
    mcfiona "I'm sure it does."
    hide diana
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(Fiona, are you sure you know what you got yourself into?)"
    hide wllmc
    show wllmc coat smallsmile at left3
    show diana casual basicglasses at right3
    "I do the only thing there is to do in the circumstances, and play at being dumber than a sack of rocks."
    mcfiona "I wouldn't know anything about that, though. Never been one for spirits and ghouls."
    show wllmc smile
    mcfiona "I'm just looking to make a simple life for myself out west."
    show diana surprisedglasses
    sid1 "Oh really? That was my wife's dream too. She always wanted us to have our own little homestead out here."
    show wllmc coat smile at left3:
        pause 0.1
        easein 0.4 left1
    mcfiona "She sounds like a lovely woman. I'm [genericfn], by the way. Don't think I ever introduced myself."
    show diana casual smileglasses at right3:
        pause 0.1
        easein 0.4 right1plus
    "The woman takes my hand and beams at me."
    sid1 "Delighted, [genericfn]. I'm Diana Castillo. Are you in Wisp Willow for the celebration?"
    show wllmc surprised
    mcfiona "Celebration?"
    fc "Oh, hadn't you heard? It's the fiftieth anniversary of Wisp Willow's founding. I'm actually here to help organize the festivities."
    fc "I was so delighted to be asked, really. We're theming the event around all the mysterious rumors about the town."
    fc "I was actually hoping to have Ms. Eichen as one of my performers, but the schedule was already booked out."
    hide diana
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Gotta keep the conversation away from Fiona.)"
    hide wllmc
    show wllmc coat smirk at left1
    show diana casual smileglasses at right1plus
    mcfiona "Rumours, you say? What kind?"
    hide wllmc
    hide diana
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    show diana casual_cu smileglasses_cu at diana_cu
    fc "So many! The Bones of the Leviathan, the Ghost Rider, the Screaming Tree, and oh, more than I can remember."
    hide diana

    $menuhideborder = True
    menu fionas1e3c1:
        "Bones of the Leviathan, huh?":
            $menuhideborder = False
            show wllmc coat smirk at left1
            show diana casual smileglasses at right1plus
            mcfiona "Bones of the Leviathan, huh? Sounds pretty spooky."
            fc "It's a geological formation near here. You should ride out and see it some time."
            fc "It really does put you in mind of some immense, long-dead beast."
        "I've heard of Ghost Riders before.":
            $menuhideborder = False
            show wllmc coat smirk at left1
            show diana casual smileglasses at right1plus
            mcfiona "I've heard of Ghost Riders before. There seems to be one in the paper every other week or so."
            fc "They are popular, aren't they?"
            fc "But what makes this one interesting is how specific and similar all the different accounts are."
        "What in the nine hells is a screaming tree?":
            $menuhideborder = False
            show wllmc coat surprised at left1
            show diana casual smileglasses at right1plus
            mcfiona "What in the nine hells is a screaming tree?"
            fc "It's a twisted black walnut, alone on a high hill."
            show diana sadglasses
            fc "People say that on the full moon, you can hear it screaming like a man in pain."

    hide wllmc
    hide diana
    show ada hat sad at centre
    "Ada shakes her head."
    st "All nonsense, in my opinion. The kind of stuff people tell for fun on a cold winter night."
    hide ada
    show wllmc coat sad at left1
    show diana casual smileglasses at right1plus
    "Diana doesn't look embarrassed at all."
    fc "My wife would have agreed with you. She always used to laugh at what she called my 'little fascinations.'"
    show wllmc surprised
    mcfiona "Used to?"
    show diana sadglasses
    fc "She died last year. I'd give anything to see her again."
    show wllmc coat sad
    "She runs a finger over the locket around her neck, and something in my stomach lurches."
    hide diana
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(I can't imagine what that must be like. To love someone, and then lose them.)"
    hide wllmc
    show wllmc coat sad at left1
    show diana casual sadglasses at right1plus
    "Guilt bites down hard on my heart, and the pocketbook feels even heavier than before."
    hide diana
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Fine. I guess I'll starve and sleep on the street.)"
    scene fiona_s1_mini1 at bg with fade
    show cinema_fov at cinema_fov_in
    pause 1.0
    "As Diana asks Ada another question about the town's history, I pull her pocketbook out and tuck it back where it belongs."
    show cinema_fov at cinema_fov_out
    scene bg_wll_saloon_night_lights_people at bg
    show wllmc coat_cu smirk_cu at wllmc_cu
    with fade
    "(With luck, she'll never know it was missing to begin with.)"
    hide wllmc

    stop music fadeout 1.0
    play music wlleverydayupbeat2
    show ada hat smile at centre
    st "Fiona, there you are!"
    hide ada
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Damn it! I was hoping to get Diana gone before Fiona showed up.)"
    hide wllmc
    show nathan redcoat_hat basic_hat at left4
    show sascha belt basic_hat at right1
    show fiona cloak basic at left1plus
    show cecelia coat basic_hat at right5
    "I turn my head just a shade quicker than I like, and see Fiona walking through the crowd with three other people."
    hide nathan
    hide sascha
    hide fiona
    hide cecelia
    show wllmc coat_cu angry_cu at wllmc_cu
    "(They're not exactly wearing uniforms, but something in the way they move together tells me they're a unit.)"
    show wllmc coat_cu surprised_cu
    "(These must be the other Wardens.)"
    hide wllmc
    show wllmc coat basic at left3
    show fiona cloak smile at right3
    mb "Long time no see, my darling complication."
    mb "I was hoping to keep you to myself, but they insisted on seeing you firsthand."
    mb "This is Cayde, Cecelia, and Sascha."
    "She points to each of them in turn."
    hide fiona
    show nathan redcoat_hat basic_hat at right4
    $sidecharone = "Cayde"
    sid1 "It ain't every day Fiona finds a person so fascinating."
    show nathan smile_hat
    "He tips his hat to me with a wry smile, and a shiver runs down my spine."
    hide nathan
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(It's not fear, just a feeling like the air in here suddenly got thirty degrees colder.)"
    hide wllmc
    show wllmc coat smallsmile at left3
    show cecelia coat smirk_hat at right3
    vr "We trust Fiona's judgment, but that doesn't mean we don't want to form our own opinions."
    vr "Ada, will you serve the others their usuals? First round's on me tonight."
    show cecelia sleep_hat
    "She doesn't order anything for herself, but unclasps a metal flask and takes a long sip."
    hide cecelia
    show sascha belt smile_hat at right3
    show wllmc surprised
    sasch "Don't worry, we don't bite. Unless you want us to, of course."
    "He smiles a very suggestive smile, and I can't help noticing how many people around us suddenly flush and tug at their collars."
    hide sascha
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(He certainly has magnetism, I'll give him that.)"
    hide wllmc
    show fiona cloak smile at right3:
        pause 0.1
        easein 0.4 centre
    show wllmc coat smallsmile at left3
    "Fiona sidles up to me and wraps an arm around my waist."
    mb "Don't mind them. They're menaces, one and all, but nothing you and I can't handle."
    show wllmc coat grin
    "I lean into the embrace and wink at her."
    mcfiona "You missed me, huh?"
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "I was pining for you every moment I was gone."
    hide fiona
    show diana casual smileglasses at centre
    "Diana presses a hand to her cheeks and beams at us."
    fc "How sweet you are! It reminds me of when I first met my wife."
    hide diana
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Slow down a little, Diana. This is just some good casual fun.)"
    hide wllmc
    show fiona cloak smile at left3
    show diana casual smileglasses at right3
    "Fiona doesn't miss a beat."
    mb "Diana Castillo. I told you we'd meet again."
    fc "You did. And if you're willing, I'd love to get that reading we were discussing."
    show fiona grin
    mb "Of course. But I do have to tell you, the cost is the same."
    show diana casual surprisedglasses
    fc "An item of emotional value?"
    show fiona smile
    show diana sadglasses
    "Fiona nods, and Diana bites her lip."
    mb "Think it over. Take as long as you need."
    hide diana
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "Turning her head slightly, she brings her lips to my ear."
    mb "She won't take it."
    "I lean in so I can whisper back."
    hide fiona
    show wllmc coat_cu angry_cu at wllmc_cu
    mcfiona "You're wrong about that. Be careful, Fiona, she wants something from you."
    hide wllmc

    $menuhideborder = True
    menu fionas1e3c2:
        "She's cleverer than she let on.":
            $menuhideborder = False
            show wllmc coat_cu angry_cu at wllmc_cu
            mcfiona "She's cleverer than she let on back on the train, and that's never a good sign."
            mcfiona "Means she's playing you. Or at least trying to."
        "She knows a lot about you.":
            $menuhideborder = False
            show wllmc coat_cu angry_cu at wllmc_cu
            mcfiona "She knows a lot about you. Mentioned about how you proved some famous skeptic wrong and everything."
            mcfiona "It might be she's looking to do what he couldn't."
        "My intuition is telling me this is fishy.":
            $menuhideborder = False
            show wllmc coat_cu angry_cu at wllmc_cu
            mcfiona "My intuition is telling me this is fishy."
            mcfiona "And say what you like about your skills, my intuition got me through my whole life. It's reliable."
    hide wllmc
    show fiona cloak_cu smile_cu at fiona_cu
    "Fiona gives me a look so gentle it makes me uncomfortable."
    mb "Why [genericfn], are you looking out for my best interests?"
    hide fiona
    show wllmc coat_cu smirk_cu at wllmc_cu
    mcfiona "It's a professional courtesy."
    hide wllmc
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "What a romantic you are. But don't worry. Unlike you, Diana is an open book to me."
    hide fiona
    show fiona cloak basic at left3
    show diana casual sleepglasses at right3
    "And sure enough, after another minute of deliberation, Diana sighs and shakes her head."
    show diana casual sadglasses
    fc "As curious as I am, this locket isn't something I can give up."
    hide fiona
    hide diana
    "She says her goodbyes and leaves, Fiona watching her the whole way."
    show wllmc coat basic at left3
    show fiona cloak smirk at right3
    mb "Well, it was worth a try. Now I can focus on making another plan."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Why does Fiona want that locket so bad anyway?)"

    scene bg_wll_saloon_night_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wllhappy1 fadein 1.0
    "As the night draws in the bar empties out, and I find myself sitting at a table playing poker with Fiona and her Warden friends."
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Not that I'm complaining. No better way to get to know people than to play a few hands with them.)"
    hide wllmc
    "It quickly becomes obvious that Fiona and I are the best players."
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Cecelia has a great poker face, but she plays too conservative and doesn't take the necessary risks.)"
    "(Cayde has a good head for numbers, but he's much too straightforward to be successful at bluffing.)"
    "(And Sascha is more interested in provoking others than winning - he'll go all in even when he has bad cards, just to raise the stakes.)"
    hide wllmc
    "The banter stays light while we play, and though I try and get a better sense of what 'Warden' means, it remains frustratingly evasive."
    show fiona cloak grin at right1
    show wllmc coat smallsmile at left1plus
    "Eventually, the alcohol begins to have an effect on Fiona, and she becomes even more talkative and giggly."
    hide fiona
    hide wllmc
    show wllmc coat_cu smile_cu at wllmc_cu
    "(I thought her dials for both were already at maximum output, but apparently she has a secret extra setting.)"
    hide wllmc
    show fiona cloak embarrassed at right1
    show wllmc coat smallsmile at left1plus
    mb "I just don't understand why my powers aren't working. Maybe I haven't tried the right thing yet."
    "She's already tucked against my side, but now she reaches out and takes my hand, bringing it close to her face."
    hide wllmc
    hide fiona
    show fiona cloak_cu embarrassed_cu at fiona_cu
    mb "Maybe your palm will give me the answers I need."
    hide fiona
    show fiona cloak embarrassed at right1
    show wllmc coat smirk at left1plus
    mcfiona "The only thing I've ever learned from my palm is that it gets chapped when it spends too much time in soapy water."
    show fiona cloak grin
    mb "Lines on your hand, lines in the sand, the leylines bind us to the earth and the hidden lines in the sky speak our futures."
    hide wllmc
    hide fiona
    show fiona cloak_cu smile_cu at fiona_cu
    "Her slim fingers trace shapes across my skin, and all I want to do is lift them to my mouth so I can taste them."
    hide fiona
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(Maybe the alcohol is having a bit of an effect on me, too. Or maybe it's just Fiona.)"
    hide wllmc
    show fiona cloak grin at right1
    show wllmc coat smirk at left1plus
    mcfiona "Fiona, you want to get out of here?"
    mb "In a moment, darling complication. I feel like I'm on the verge of breakthrough."
    scene fiona_s1_mini2 at bg
    with fade
    show cinema_fov at cinema_fov_in
    pause 1.0
    "She runs her finger down my heart line, and that same spark I felt when we kissed kicks to life."
    show cinema_fov at cinema_fov_out
    scene bg_wll_saloon_night_lights at bg
    show wllmc coat_cu surprised_cu at wllmc_cu
    with fade
    "(Not here, not now! Not with so many people watching.)"
    hide wllmc
    show fiona cloak surprised at right1
    show wllmc coat surprised at left1plus
    show mc_instinct at full_size with dissolve:
        alpha 0.7
    hide mc_instinct with dissolve
    "But my bad luck doesn't take orders from me. The world shudders, the wind rises, and the piano keys create a sudden jangle of noise."
    hide wllmc
    hide fiona
    show nathan redcoat surprised at centre
    $sidecharone = "Cayde"
    sid1 "What was that?"
    hide nathan
    show wllmc coat surprised at left3
    show cecelia coat smirk at right3
    vr "You might want to rein yourself in, [genericfn]. We like to keep a low profile."
    hide cecelia
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    mcfiona "I, uh...Should probably-"
    hide wllmc
    show wllmc coat sad at centre
    "A horrible, trapped feeling fills me, and I do the only reasonable thing I can think of - leave."
    hide wllmc
    show fiona cloak surprised at right1
    show wllmc coat surprised at left1plus
    "But it doesn't work. As soon as I stand up, Fiona grips my hand tight and holds me where I am."
    show fiona smile
    mb "Don't leave. One little hiccup doesn't make a difference to us."
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "She gives me that heart-stopping smirk."
    mb "I'm not done with you yet, [genericfn]."
    hide fiona
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Is she telling the truth? Is it really alright for me to stay?)"
    hide wllmc
    show fiona cloak smirk at right1
    show wllmc coat sad at left1plus
    "I hesitate, torn between hope and experience in a way that almost never happens."
    hide wllmc
    hide fiona
    show sascha belt smirk at centre
    sasch "Please, do as Fiona asks. Her aura's a shade of red I haven't seen since I was last in Madame Rosemerta's fine establishment."
    sasch "I don't want to deal with the mood she'll be in if she goes unsatisfied."
    show fiona cloak angry at left3
    show sascha belt smirk at right3
    "Fiona glares at Sascha and sticks her tongue out."
    mb "Keep that nose of yours to yourself, Sascha. It's none of your business what color my aura is."
    hide sascha
    show cecelia coat smirk at right3
    vr "You must admit, Fi dearest, that this level of interest is rare for you."
    show fiona sleep
    "Fiona sighs."
    hide cecelia
    hide fiona
    show fiona cloak_cu pout_cu at fiona_cu
    mb "You don't understand. This might be my one chance to actually read a romance novel start to finish."
    mb "Instead of knowing the last page before I've even opened the book."
    "She looks at me as she speaks, and my heart lurches."
    hide fiona
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(What do I do?)"
    show wllmc sad_cu
    "(I can pretend I didn't understand the conversation, and it would even be half true.)"
    "(Because following it means accepting the most absurd premise - that Fiona's companions accept her powers as real.)"
    hide wllmc
    show fiona cloak_cu smile_cu at fiona_cu
    "Fiona's thumb strokes over the soft skin of my inner wrist as the rest of the Wardens turn back to their own conversations."
    mb "Won't you sit down again, my darling complication? I've got a nice warm spot right here for you."
    "She pats the seat next to her, her eyes sweetly beseeching me."
    hide fiona

    $menuhideborder = True
    menu fionas1e3c3:
        "Find comfort beside Fiona." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show wllmc coat_cu angry_cu at wllmc_cu
            "(I don't know what the truth is, but I do know that I'm not ready to let this go.)"
            hide wllmc
            show fiona cloak smile at right1
            show wllmc coat smallsmile at left1plus
            "I plop back down in my seat and slide my free arm around Fiona's waist."
            show wllmc smile
            mcfiona "Well you wanted me and now you have me, even though I don't feel I understand half of you, Fiona Eichen."
            "That wild undercurrent is still there, swirling in the air around me, but the typhoon force of it is spent."
            show fiona smirk
            mb "I think you're making me out to be much more complicated than I am. At heart I'm a simple woman with simple needs."
            show wllmc smirk
            mcfiona "Who reads cards and palms and knows what people want before they do themselves."
            mb "What some people want."
            hide wllmc
            hide fiona
            show fiona cloak_cu smile_cu at fiona_cu
            "She smiles at me, and takes my hand again."
            mb "I never thought I could describe a hand as secretive, but yours sure is."
            mb "I can see a little of its past, but nothing of its future."
            hide fiona
            show fiona cloak smile at right1
            show wllmc coat smallsmile at left1plus
            "Having already thrown my lot in with this pretense, it can't hurt to play along."
            show wllmc smile
            mcfiona "What do you see in my past?"
            show fiona smirk
            mb "Not much I couldn't tell just by looking at you."
            mb "You spent time in a boarding house, that's for sure."
            show fiona grin
            mb "Not your parents', but a relative - your aunt?"
            show wllmc sad
            "I shift uncomfortably, feeling more seen than I'm used to."
            hide fiona
            hide wllmc
            show wllmc coat_cu sad_cu at wllmc_cu
            "(I was prepared for general teasing, but not for such cutting insight.)"
            hide wllmc
            show fiona cloak grin at right1
            show wllmc coat smile at left1plus
            mcfiona "All that's in my hand?"
            show fiona smirk
            mb "And in your posture. The way you sit, the way you place your drink. The neatness of your lapels."
            "She gestures in my general direction. Strangely, it makes me relax a little."
            show wllmc smirk
            mcfiona "I knew you had cold reading skills."
            show fiona grin
            mb "Of course."
            mb "Most people don't really want to know the future, you know."
            mcfiona "No? Seems like it would be pretty useful."
            hide wllmc
            hide fiona
            show fiona cloak_cu sad_cu at fiona_cu
            mb "And if you found out that you were going to die tomorrow?"
            mb "Or that the truth was that the rest of your life would be slow and boring, each day the same as the one that came before?"
            hide fiona
            show fiona cloak sleep at right1
            show wllmc coat surprised at left1plus
            "She sighs."
            show fiona cloak sad
            mb "Nine times out of ten, it's better to give people an optimistic dream than a cold reality."
            hide fiona
            hide wllmc
            show wllmc coat_cu smile_cu at wllmc_cu
            "(That's almost... sweet.)"
            hide wllmc
            show fiona cloak sad at right1
            show wllmc coat smile at left1plus
            mcfiona "So you tell them what they want to hear?"
            show fiona smirk
            mb "If I'm on my game, I can do one better, and tell them what they need to hear."
            show wllmc smirk
            mcfiona "So it's not magic. Just a sharp eye and a kind heart."
            hide fiona
            hide wllmc
            show wllmc coat_cu sad_cu at wllmc_cu
            "(Why do I feel so oddly disappointed?)"
            hide wllmc
            show fiona cloak grin at right1
            show wllmc coat smirk at left1plus
            mb "Oh, don't get me wrong. There's more to this world than meets the eye."
            mb "Can't you feel it?"
            hide wllmc
            hide fiona
            show fiona cloak_cu grin_cu at fiona_cu
            "She leans in close."
            mb "I've known there was something special about you since the moment I laid eyes on you."
            "I catch another waft of the incense smell that lingers on her, and the subtler scents underneath."
            hide fiona
            show wllmc coat_cu smile_cu at wllmc_cu
            "(Herbs and old books and something bright and peppery.)"
            mcfiona "I feel something, that's for sure."
            show wllmc coat_cu smirk_cu
            "(It would be impossible not to. Every inch of the air between us is buzzing with energy.)"
            hide wllmc
            show fiona cloak grin at right1
            show wllmc coat smallsmile at left1plus
            mcfiona "But I wouldn't call it anything supernatural. There's a much simpler word."
            show fiona cloak smirk
            mb "Two things can be true at once."
            show wllmc coat grin
            mcfiona "So you admit it's true."
            mcfiona "You want me."
            show fiona cloak grin
            mb "Have I ever hidden that?"
            hide wllmc
            hide fiona
            show fiona cloak_cu smirk_cu at fiona_cu
            "Her thumb makes slow, teasing circles on my palm."
            mb "The lines on your hand are no guide for me."
            show fiona cloak_cu grin_cu
            mb "Wherever we end up together, it'll be Terra Incognito."
            mb "A new world, just for us."
            hide fiona
            show wllmc coat_cu embarrassed_cu at wllmc_cu
            "(I never met a woman whose words dripped such sweet honey.)"
            hide wllmc
            show fiona cloak grin at right1
            show wllmc coat smirk at left1plus
            mcfiona "I've always forged my own path. Think you can keep up?"
            show fiona cloak smirk
            mb "I have no idea. That's what's so exciting."
            hide wllmc
            hide fiona
            "She lifts my hand to her mouth and kisses, first my heart line, then my life line."
            "Her lips are so soft, and each kiss is careful and delicate. Almost reverent."
            show fiona cloak_cu smile_cu at fiona_cu
            mb "I'm ready to follow your lead."
            hide fiona
            show wllmc coat_cu surprised_cu at wllmc_cu
            "(But where do I want to go?)"
            hide wllmc
            show fiona cloak smile at right1
            show wllmc coat surprised at left1plus
            "The blatant intimacy of Fiona's gesture is more shocking than anything else. My hand burns where her lips touched me."
            hide fiona
            hide wllmc
            show wllmc coat_cu angry_cu at wllmc_cu
            "(Remember Ada's warning. Keep your wits about you, [genericfn]!)"
            "(Don't play your hand too fast or too eager.)"
            hide wllmc
        "Pull away.":
            $menuhideborder = False
            show wllmc coat_cu angry_cu at wllmc_cu
            "(Someday soon, I'm going to have to deal with this magic bullshit. There's a reckoning coming, years in the making.)"
            "(But it doesn't have to be now. I can put off knowing just a little longer.)"
            hide wllmc
            show wllmc coat angry at left1plus:
                pause 0.1
                easein 0.3 left2
            show fiona cloak surprised at right1:
                pause 0.3
                easein 0.2 right1plus
            "I tug on my hand, and Fiona lets it go with a jerk, startled."
            show wllmc sad
            mcfiona "Sorry, the alcohol must have hit me harder than I thought."
            show wllmc basic
            mcfiona "I don't think I caught one word in ten of that."

    show wllmc coat smallsmile at left2
    show fiona cloak smirk at right1plus
    mcfiona "Not that this evening hasn't been nice and all, but it's getting close to my bedtime and I've no job and no place to stay."
    show fiona sad
    mb "You've no work, and I've too much work. Isn't it tragic?"
    "She gives me the woebegone look she's perfected."
    show wllmc smirk
    mcfiona "Has anyone in the world ever suffered more than us?"
    show fiona smirk
    mb "Unlikely. But you know, maybe we can help each other out."
    mb "Combine our talents, see if we can't make something special happen."
    show wllmc surprised
    mcfiona "What exactly are you suggesting?"
    show fiona smile
    mb "Can't you tell? I'm asking if you want to do it with me."
    hide wllmc
    hide fiona

    stop music fadeout 1.0
    play music wlltense2 fadein 1.0
    show fiona cloak_cu smile_cu at fiona_cu
    "The molten gold of her eyes is hotter than the sun at noon as she looks at me."
    hide fiona
    show wllmc coat_cu grin_cu at wllmc_cu
    "(I want nothing more than to spend hours lost in those eyes.)"
    "(And it seems like I might be about to get the chance.)"
    show wllmc coat_cu embarrassed_cu
    "(Surely a girl as... flexible as Fiona knows that work is better when you mix it with play.)"
    hide wllmc
    show fiona cloak_cu grin_cu at fiona_cu
    mb "What do you say, partner?"
    hide fiona

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
