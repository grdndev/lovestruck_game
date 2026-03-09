label lexi_season1_episode10:

    $tbc = False
    scene bg msc_museum_displays_day at bg with dissolve
    play music msclexi


    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show mscmc jacket_hairdown basic at left2
    show lexi casual basic hat sunglasses at right2

    "Lexi and I arrive to find the museum packed with people. I see advertisements for some event today on the front desk."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(This is a lot of potential witnesses. We're just here to assess security for later, but still...)"
    show mscmc jacket_hairdown smile at left2:
        easein 0.4 xoffset +100
    show lexi casual smile hat sunglasses at right2
    "I lean over to whisper to Lexi, but catch sight of her hat's slogan and chuckle. Lexi feigns a shooing motion while she grins at me."
    show lexi casual bigsmile hat sunglasses
    lx "Watch the disguise. Can't have security recognizing me. I'm a little infamous here, remember?"
    show mscmc jacket_hairdown grin
    mclexi "That hat is so silly."

    lx "Aha, so you admit it's distracting you from my face?"
    show mscmc jacket_hairdown smile
    "I fondly roll my eyes, and take another glance around the main room. I lower my voice and lean over again."
    show lexi casual embarrassed hat sunglasses
    mclexi "Should we come back later?"
    show lexi casual bigsmile hat sunglasses
    lx "No, this is perfect. We'll disappear in the crowd."
    hide lexi
    hide mscmc
    show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu at lexi_cu
    "She takes my hand, and from behind the tinted lenses of her sunglasses, I see a devious sparkle in her eye."

    lx "Ready to learn some psychology tricks? People aren't as likely to eavesdrop on us if they think we're touristy girlfriends."
    hide lexi
    show mscmc jacket_hairdown smile at left2:
        xoffset +100
    show lexi casual smile hat sunglasses at right2
    "I smile and squeeze her hand, stepping a bit closer so we're in each other's space."
    show mscmc jacket_hairdown embarrassed
    show lexi casual smile hat sunglasses:
        easein 0.4 xoffset -100
    "Lexi lightly hipchecks me, sending a pulse of excitement through me."

    mclexi "Sounds good. When do we start?"
    show mscmc jacket_hairdown grin
    lx "Let's go with the flow for now. We're just a close pair of art admirers for now."
    show mscmc jacket_hairdown embarrassed
    show lexi casual embarrassed hat sunglasses
    "Our fingers interwoven, we walk leisurely around the displays and exhibits. Lexi's hand is warm and relaxed in my own."
    show mscmc jacket_hairdown smile
    show lexi casual bigsmile hat sunglasses
    lx "Look at the strokes on that painting. Van Gogh has such a unique style, it's unmistakable."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's playing up the artsy tourist ruse, but I also hear genuine excitement in her voice.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left2:
        xoffset +100
    show lexi casual bigsmile hat sunglasses at right2:
        xoffset -100
    mclexi "It's gorgeous, love the colors."

    lx "Wow, look at that one over there!"
    show mscmc jacket_hairdown embarrassed
    show lexi casual embarrassed hat sunglasses
    "She points to another painting, and leans close; I feel her chest and the rest of her body brush against me as she whispers in my ear."
    show mscmc jacket_hairdown smile
    show lexi casual basic hat sunglasses
    lx "See those security cameras? Keep an eye on their rotations, we want to find any blindspots."
    show mscmc jacket_hairdown grin
    show lexi casual smile hat sunglasses
    "Playing into the girlfriend thing, I giggle loudly, as though Lexi is saying something flirtatious."

    "In a low voice, I respond seriously."
    show mscmc jacket_hairdown smile
    mclexi "I see them. Anyplace in particular you'd like a blindspot?"

    lx "Not sure yet, let's walk around a bit more."
    hide lexi
    hide mscmc
    $menuhideborder = True
    menu lexis1e10c1:
        "A. Look for security devices.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left2:
                xoffset +100
            show lexi casual smile hat sunglasses at right2:
                xoffset -100
            "Between giggles and comments on the artwork, I try to sneak glances around."

            "It’s well-hidden, but I do spot a small compartment on the wall."
            show lexi casual embarrassed hat sunglasses
            "I whisper in Lexi’s ear, gently moving some of her hair out of the way."
            show mscmc jacket_hairdown embarrassed
            show lexi casual smile hat sunglasses
            mclexi "Does that compartment over there look like anything?"
            show mscmc jacket_hairdown surprised
            show lexi casual bigsmile hat sunglasses
            "Lexi giggles like I’ve said something naughty, then pulls my hand up to her lips and kisses it."
            hide lexi
            hide mscmc
            show lexi casual_cu embarrassed_cu hat_cu sunglasses_cu at lexi_cu
            lx "Nice find."

        "B. Keep an eye out for guards.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left2:
                xoffset +100
            show lexi casual smile hat sunglasses at right2:
                xoffset -100
            "While Lexi focuses on things like cameras and alarms, I think I’ll have a better show spotting guards."
            show mscmc jacket_hairdown basic
            "As we continue to stroll around the exhibits, I start taking mental notes about patrol routes as best I can."
            show mscmc jacket_hairdown embarrassed
            "Lexi figures out what I’m doing, and fixes some of my hair with a giggle and carefully whispers to me."
            hide lexi
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Good call."

        "C. Be the distraction.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Lexi will know what we're looking for better than me, so I'll cover her.)"
            hide mscmc
            show mscmc jacket_hairdown smile at left2:
                xoffset +100
            show lexi casual smile hat sunglasses at right2:
                xoffset -100
            mclexi "Isn't this museum so beautifully designed too? It doesn't distract from the art, but it's eye-catching in its own right."
            show lexi casual basic hat sunglasses
            "Lexi catches on right away, and takes the opportunity I've given her to get a look at the walls and ceilings around us."
            hide lexi
            hide mscmc
            show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu at lexi_cu
            lx "You're right, it's just lovely. Even the architecture has history."
            show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu
            "She winks at me as a thank-you."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown basic at left2:
        xoffset +100
    show lexi casual basic hat sunglasses at right2:
        xoffset -100
    "As we carry on, Lexi gets quieter. Her face is turned partly away from me, and she seems to be thinking."
    show mscmc jacket_hairdown smile:
        easein 0.4 xoffset +125
    show lexi casual embarrassed hat sunglasses
    "I lean over, touching the tip of my nose to her cheek with an affectionate grin on my face as I whisper."
    show mscmc jacket_hairdown basic
    show lexi casual basic hat sunglasses
    mclexi "Is something wrong?"
    show mscmc jacket_hairdown surprised
    show lexi casual smile
    lx "They've boosted security since the last time we were here. Take a look."
    show mscmc jacket_hairdown basic
    show lexi casual angry
    "She reaches up to fix her hat, and points with her pinky toward the ceiling."
    show mscmc jacket_hairdown surprised
    "When I look, I see the bottom of a metal gate lifted into the ceiling between two of the exhibit rooms."
    show lexi casual smile
    lx "Looks like those door-gate things have been added all over, and probably drop when the alarms get tripped."

    lx "If they'd been set up last time, we'd be sitting in a cell somewhere."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Cool, cool, cool, cool. No pressure.)"
    show mscmc jacket_hairdown surprised at left2:
        xoffset +125
    show lexi casual smile hat sunglasses at right2:
        xoffset -100
    mclexi "So what do we do about them?"
    show mscmc jacket_hairdown embarrassed
    show lexi casual bigsmile
    "Lexi grins at me, that bright and excitable kind that tells me she likes the challenge of it all."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Her confidence is infectious and intoxicating at the same time.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2:
        xoffset +125
    show lexi casual smile hat sunglasses at right2:
        xoffset -100
    lx "Well, we just won't trip the alarms, obviously."
    hide mscmc
    hide lexi
    show lexi casual_cu smile_cu hat_cu sunglasses_cu at lexi_cu
    "She pulls down her shades enough to wink at me, then leisurely tugs me by the hand toward the other side of the room."
    hide lexi
    "Keeping up our charade, I put my arm around Lexi's shoulders, and she wraps hers around my waist."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I need to stop blushing, we're freaking casing out a place!)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at left2:
        xoffset +125
    show lexi casual smile hat sunglasses at right2:
        xoffset -100
    lx "See that dark room over there? I have a theory."
    show mscmc jacket_hairdown surprised
    show lexi casual bigsmile
    mclexi "What?"
    show lexi casual smile
    lx "Only one way for you to find out. C'mon, we just need a blindspot."
    show mscmc jacket_hairdown grin
    stop music fadeout 1.0
    play music mscromance
    "We giggle and sway through the crowd. Lexi is a natural, casting sultry looks my way as our hips move in time."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(We're bordering on PDA, but the way people look away in embarrassment means it's working.)"
    hide mscmc
    show lexi casual_cu smile_cu hat_cu sunglasses_cu at lexi_cu
    "Lexi leans close enough for me to feel her hot breath across my neck."

    "Her hand slips into my back pocket, where she tugs slightly, signaling me to stop."

    lx "Wait here."

    "We're standing so close, I swear I can hear her heartbeat. The fingertips of her free hand dance across my collarbone."
    show lexi casual_cu bigsmile_cu
    lx "You know, you'd look beautiful naked and perched like one of these sculptures."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I see what she's doing.)"

    "I laugh loudly and shyly—it's not completely fake either."
    hide mscmc
    show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu at lexi_cu
    "The immediate bystanders around us hear. There are a few coughs as they flusteredly move away."
    show lexi casual_cu smile_cu
    "Lexi watches until everyone's too embarrassed to look at us, then hooks her finger into the collar of my shirt and whispers."

    lx "Let's go."
    scene bg msc_museum_displays_night at bg with wiperight
    "We manage to duck into the dark exhibit room without anyone spotting us. The cover of an unlit room is definitely welcome."
    show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu at lexi_cu
    "Lexi props up her sunglasses, and I see an excited, proud look on her beaming face."

    lx "Check it out, none of the security cameras are on in here."

    lx "They must be doing the upgrades room by room."
    hide lexi
    show mscmc jacket_hairdown smile at left2:
        xoffset +125
    show lexi casual smile hat sunglasses at right2:
        xoffset -100
    mclexi "Okay, what's next?"

    lx "Check the walls for stuff like false panels or electrical compartments."

    lx "Anything that can tell us more about how this place keeps its treasures safe."
    hide lexi
    hide mscmc
    "We split up and each take one side of the room, and in the darkness..."
    show mscmc jacket_hairdown basic at centre
    "It's more productive to feel around the walls than try to rely on my eyes alone."
    show mscmc jacket_hairdown embarrassed
    "I can hear the careful but authoritative tap of Lexi's heeled booties. Everything about her movements are intentional and controlled."
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I can't help but feel safe with her here.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at centre
    stop music fadeout 1.0
    play music mscsuspense
    "But then I hear more footfalls. It takes me a second to register the sound, and I look frantically for a different room to dive into."
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Crap, there's nowhere to hide fast!)"
    hide mscmc
    show mscmc jacket_hairdown surprised at centre
    mclexi "Someone's coming."
    hide mscmc
    show lexi casual_cu embarrassed_cu hat_cu sunglasses_cu at lexi_cu
    "Lexi is closer than I expect, and grabs my arm, pulling my body flush to hers. I gasp, any questions stuck in my throat."

    lx "Kiss me."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is now really the time?!)"
    hide mscmc
    show lexi casual_cu smile_cu hat_cu sunglasses_cu at lexi_cu
    "Lexi smirks at my confused expression."

    lx "Trust me."
    show lexi casual_cu embarrassed_cu
    "I can hear the footsteps entering the exhibit room we're in—we're out of time!"
    show lexi casual_cu sleep_cu
    stop music fadeout 1.0
    play music mscpassionateromance
    "Lexi pulls my face close and kisses me, so sudden it's electric."
    hide lexi
    "The immediacy of her scent and taste overwhelms my senses, and I'm quick to forget about the museum all together."

    "I kiss her back, eager to drink in the feeling of being with her in this dark room."

    "How her fingernails grip slightly against my skin, commanding me to right where she wants me."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Can we just keep doing this?)"
    hide mscmc
    "But alas, There comes a pointed cough from behind us."
    show mscmc jacket_hairdown surprised at left1 behind lexi
    show lexi casual surprised hat sunglasses at right1
    "Lexi and I break apart, each turning and squinting against the bright beam of a flashlight."

    "The security guard pointing it at us looks unamused."
    show mscmc jacket_hairdown embarrassed
    show lexi casual embarrassed
    "I feel my cheeks burning bright. Lexi doesn't miss a beat, blurting out a brittle laugh of embarrassment."

    lx "O-oh! Um, we were just... The moment just came over us, and..."
    show lexi casual bigsmile
    lx "It's just, we're long-distance, and I haven't seen my girlfriend in months. I just missed her so much..."

    "As Lexi pretends to stumble through an explanation, I watch as the security guard's face remains flat."
    show mscmc jacket_hairdown smile
    "She's unmoved by our tragic love story."

    "Then she sighs, long and so, so tired."

    $sidecharone = "Security Lady"

    sid1 "Look... I get it, long-distance sucks."
    show mscmc jacket_hairdown embarrassed
    sid1 "I'll give you five minutes, and then you gotta scram."

    "Lexi claps her hands together and mouths the words 'thank you'."

    "The security guard remains unimpressed, but leaves to give us some privacy."
    hide mscmc
    hide lexi
    show lexi casual_cu angry_cu hat_cu sunglasses_cu at lexi_cu
    "Lexi drapes her arms around my shoulders, a frustrated furrow to her brow."
    show lexi casual_cu smile_cu
    lx "Five minutes isn't really enough time to case the rest of the place."

    "Then, a mischievous little smile curls at the corners of her lips."
    show lexi casual_cu embarrassed_cu
    lx "Buuut... we could take advantage of the time in other ways."
    show lexi casual_cu smile_cu
    "She meets my eye, a daring look on her face as I feel her hands once again settle around my hips like a promise."
    hide lexi
    $menuhideborder = True
    menu lexis1e10c2:
        "A. Keep kissing Lexi in the dark!"(paidchoice = "paidchoice"):
            $menuhideborder = False

            "I don’t even have to think about it. I pill Lexi in by the waist, and we crash together needily."

            "Lexi loses the grin for a moment, concentrating fully on the way our tongues dance and our bodies press together."

            "My heart is beating fast from the close call, but when I drown myself in Lexi like this, I can't remember being scared at all."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "We only part when we need the air, breathing hotly in the small space we’ve made between our bodies."

            mclexi "So... Long-distance girlfriends, huh?"
            hide mscmc
            show lexi casual_cu smile_cu hat_cu sunglasses_cu at lexi_cu
            "Lexi smiles at me."

            lx "Oh yes, it’s all very complicated, you see—what with my business trips taking me all over the world and her career as an athlete."

            lx "You know, just life things."
            show lexi casual_cu embarrassed_cu
            "I snort out a little laugh, but Lexi keeps a straight face as she continues to weave a fake life."
            show lexi casual_cu smile_cu
            lx "I live most of my life on planes, traveling in the skies, and you…?"

            "She raises an eyebrow at me, egging me on. I play along."
            hide lexi
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mclexi "I’m a marine biologist, always deep under the sea."
            hide mscmc
            show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu at lexi_cu
            "Lexi’s bright laugh is like music to my ears."
            show lexi casual_cu smile_cu
            lx "So you’re my mer girlfriend then? Luring me out of the clouds with your siren song."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "We met when... when your plane emergency landed on a deserted island? And I saved you from drowning."
            hide mscmc
            show lexi casual_cu embarrassed_cu hat_cu sunglasses_cu at lexi_cu
            lx "Dramatic! I awoke under tropical trees I didn’t recognize, and heard the most beautiful voice singing to me."
            hide lexi
            "My cool fractures with a blush, and Lexi kisses it right off my face."

            "My imagination runs wild; I can almost feel the warm sand and sea breeze. I run my hands over her perfect body."
            show lexi casual_cu embarrassed_cu hat_cu sunglasses_cu at lexi_cu
            lx "Alas, the sky had to call me away sooner or later—but not before we fell for each other."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I wait for you from the ground, wondering if each plane I see might be you."
            hide mscmc
            show lexi casual_cu embarrassed_cu hat_cu sunglasses_cu at lexi_cu
            "Lexi laughs, clearly charmed, but I belatedly feel a small pang in my chest."
            hide lexi
            show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
            "(It’s just a story, but… did she say ‘fell for each other’???)"
            hide mscmc
            "I’m distracted by another heated kiss, one that washes away my momentary somberness."

            "As we part again, I kiss along her jaw and neck."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mclexi "When oh when might my high flying business woman come down to earth and stay a while?"
            hide mscmc
            show lexi casual_cu bigsmile_cu hat_cu sunglasses_cu at lexi_cu
            lx "You’re irresistible enough to make me think about it, but the ocean can be so suffocating, and I like to be free."
            show lexi casual_cu basic_cu
            "The answer surprises me. I draw back, dropping our little game as I meet Lexi’s eye."
            hide lexi
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            mclexi "Is that really how you feel about the sea?"
            hide mscmc
            show lexi casual_cu sad_cu hat_cu sunglasses_cu at lexi_cu
            "Lexi glances sidelong, keeping an air of nonchalance to her. She shrugs."
            show lexi casual_cu smile_cu
            lx "I don’t like when it’s the only option."

            lx "I feel like my path will lead me to many places. My life is mine, to do whatever I like and go wherever I want."
            show lexi casual_cu embarrassed_cu
            lx "But... I don’t know, maybe you can come with me or something sometime."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "A soft happiness swells in my heart. I smile."

            mclexi "That works for me."

            mclexi "Besides, I like your legs too. I mean, your tail is incredible, breathtaking, magnificent, but your thighs too though."
            hide mscmc
            show lexi casual_cu smile_cu hat_cu sunglasses_cu at lexi_cu
            lx "Glad you think so."
            show lexi casual_cu embarrassed_cu
            "We share a laugh, sweeter than I’m used to from Lexi, but wonderful nonetheless."
            hide lexi
            "She kisses me again, reigniting that warmth between us as we cling to one another."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I could get lost like this, and never want to find my way out.)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left1 behind lexi
            show lexi casual angry hat sunglasses at right1
            "Just as our hands start wandering—Lexi’s into my hair, and mine into her back pockets—I hear another stern cough from across the room."
            show lexi casual basic
            "The security guard is back. She doesn’t speak to us, but her deadpan expression says enough."
            show mscmc jacket_hairdown embarrassed
            show lexi casual bigsmile
            "Lexi and I leave giggling and holding hands."

        "B. Let's just go.":
            $menuhideborder = False
            show lexi casual_cu embarrassed_cu sunglasses_cu hat_cu at lexi_cu
            "I bite my lip, glancing a little too obviously at Lexi's lips, then quickly away."
            hide lexi
            show mscmc jacket_hairdown basic at left1 behind lexi
            show lexi casual surprised hat sunglasses at right1
            mclexi "We're already in enough trouble as it is, right? I don't really want that guard to come back and find us still here."
            show lexi casual basic
            "Lexi withdraws her arms from around me and stretches them over her head."
            show lexi casual smile
            lx "You've got a point. I don't think we'll find much more in here anyway, but it should be enough to make a plan."
            show mscmc jacket_hairdown smile
            lx "Now all there's left to do is kill some time until the job tonight."

    scene bg msc_museum_displays_day at bg with wiperight
    stop music fadeout 1.0
    play music mscmctheme
    "We mutter out our thank-yous and scurry past the guard, back into the open to the public area of the mueseum."

    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu

    "(My face is flushed all the way to my ears! That was exhilarating.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left1 behind lexi
    show lexi casual basic hat sunglasses at right1
    mclexi "Shoot, but we didn't learn much about how to get around the security..."
    show mscmc jacket_hairdown surprised
    show lexi casual smile
    lx "That makes it fun, right? There's no challenge if we figure it all out on the recon mission."
    show mscmc jacket_hairdown sad
    mclexi "Umm, but I'd rather not wind up caught later on either."
    hide mscmc
    hide lexi
    show lexi casual_cu smile_cu hat_cu sunglasses_cu at lexi_cu
    "Lexi pulls down her sunglasses and winks at me."

    lx "Don't owrry, we've got this. I've got you. Let's kill some time before the job tonight. Let's help you relax."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Kill some time, huh... I have a few ideas.)"
    hide mscmc
    show lexi casual_cu embarrassed_cu hat_cu sunglasses_cu at lexi_cu
    "I loop my arm into Lexi's, as we makefor the exit. Lexi leans into me, smirking deviously as she nuzzles her face into my neck."
    lx "Great work back there, Miss Marine Biologist."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mclexi "You toom Miss Jet Setter."
    scene bg msc_boardwalk_sunset_people at bg with wiperight
    stop music fadeout 1.0
    play music mschappytimes
    "I'm still giddy from our perilous museum kiss even as Lexi and I head down the boardwalk to burn the last rays of daylight."
    show mscmc jacket_hairdown smile at left2
    show lexi casual smile at right2
    "We bought some treats—frozen cherry lemonade for Lexi, and spicy mango on a stick for me..."

    "But even the heat of the hot sauce can't wash out the memory of the taste of Lexi's lips."
    show lexi casual surprised
    "Lexi is going over the break-in plan for tonight, and I catch her giving me a mock incredulous look as she finishes."
    show lexi casual smile
    lx "You got all that, right?"
    show mscmc jacket_hairdown grin
    mclexi "Yeah, yeah, I hear you."
    show mscmc jacket_hairdown embarrassed
    show lexi casual bigsmile
    lx "Good, I thought that mango might've been dividing your attention."
    show lexi casual basic
    "I laugh at her teasing, and the way she takes a big sip from her lemonade, continuing to pretend she's offended."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Her fake pout is really cute. Aaaand now I'm thinking about kissing her again.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2
    show lexi casual sad at right2
    lx "Seriously though, you're not having second thoughts or anything about doing this job with me?"
    show mscmc jacket_hairdown basic
    show lexi casual basic
    mclexi "Weirdly enough, I'm not. I feel nervous, but it's like how I feel before a competition."
    show mscmc jacket_hairdown smile
    show lexi casual bigsmile
    "Lexi smiles brightly at me."

    lx "I think that's exactly how I feel."
    hide lexi
    hide mscmc

    $menuhideborder = True
    menu lexis1e10c3:
        "A. I didn't think you got nervous.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show lexi casual smile at right2
            "I shoot Lexi a teasing grin in turn."

            mclexi "I didn’t think you could get nervous. Even the anticipating kind."

            lx "Why not? I live on the edge, moment to moment. It’s bound to get a little nerve-wracking once in a while."
            show lexi casual bigsmile
            lx "Still, maybe you’re right. I guess the word I’m looking for is excited."

        "B. We just can't let the pressure get to us.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left2
            show lexi casual smile at right2
            mclexi "As long as we don’t let the pressure get to us, it’ll be just like any other challenge put in front of us."
            show mscmc jacket_hairdown grin
            mclexi "We just have to face it head on. No hesitation."
            show lexi casual bigsmile
            lx "I like the gusto. Making sure you don’t psych yourself out definitely makes the difference."

        "C. Is treasure hunting competitive?":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show lexi casual smile at right2
            mclexi "Does treasure hunting get competitive? Do you win gold for coming in first place?"

            lx "Of course it's competitive."

            lx "If it's valuable enough for one treasure hunter to hear about, it's valuable enough for the rest to hear about it."
            show lexi casual bigsmile
            lx "And unlike surfing, if you come in any place other than first, you don't get shit."
    show mscmc jacket_hairdown surprised at left2
    show lexi casual surprised at right2:
        easein 0.4 xoffset -100

    "Lexi suddenly stops, patting my arm rapidly."
    show lexi casual bigsmile
    lx "Ooh, is that a mirror maze? Let's go!"
    show mscmc jacket_hairdown grin

    "I can't help but laugh."

    mclexi "Really?"
    show lexi casual smile
    lx "Yes, really! Come on!"
    show mscmc jacket_hairdown grin at out_left
    show lexi casual bigsmile at out_left
    "Before I know it, Lexi is rushing for the pop-up maze, and I'm playing catch up as I follow her inside."
    scene bg msc_mirror_maze_lightson at bg
    stop music fadeout 1.0
    play music mscreggae
    "She both disappears and multiplies, as is the way of mirror mazes, as I try to reach for her."

    "I'm disoriented for a second, watching Lexi's many reflections, but quickly put on my game face."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(You can't rely on your eyes in here. You gotta use your other senses.)"
    hide mscmc
    show mscmc jacket_hairdown sleep at centre
    "I take a moment to listen and trace the sound of Lexi's footsteps and snickering."
    hide mscmc
    show lexi casual bigsmile at centre
    "I open my eyes to see her with a delighted look, watching me through the mirror, that puts kissing back in my mind."
    show lexi casual embarrassed at out_left
    lx "Too slow!"
    hide lexi
    "I gasp as she gives me a little whap on the arm, but she's gone again before I can touch her."
    show mscmc jacket_hairdown grin at centre
    mclexi "Sneaky-!"

    "Following her laughter, I throw out my arm at Lexi—but my hand only meets cold glass."
    show mscmc jacket_hairdown sad
    "I don't expect the cold to shoot through me like it does, but suddenly I just feel lonely."
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    stop music fadeout 1.0
    play music mscsadtimes
    "(All around me are reflections of Lexi, yet I can't reach out and hold her.)"

    "(I don't want to feel like this...)"
    hide mscmc
    show mscmc jacket_hairdown sad at left2
    show lexi casual sad at right3
    "Lexi must notice the way I deflate from our game. Her laughter stops, and soon she's right next to me, the real her."

    lx "[genericfn]? Is everything okay?"

    mclexi "Why did you leave?"
    show mscmc jacket_hairdown surprised
    show lexi casual surprised
    "I just blurt it out before I can think better of it. The air seems thicker for it, but now that it's out there, I just keep going."
    show mscmc jacket_hairdown sad
    show lexi casual basic
    mclexi "That night at the beach—why did you just disappear like that?"
    show mscmc jacket_hairdown basic
    mclexi "We're so good together, and we have so much fun. Why just leave me?"
    show lexi casual sad
    "I can see the confusion and defensiveness in Lexi's reflections, as she fumbles for an answer."
    show lexi casual sleep
    lx "I didn't just leave--"
    show lexi casual basic
    mclexi "You did. You made me feel like there was something special between us, and then you just vanished."
    show mscmc jacket_hairdown sad
    show lexi casual sad
    mclexi "What if the tide had washed away your message in the sand before I woke up? I wouldn't have even seen it."

    "I clench my fists closed. I'm just sad and confused and I guess it's all coming out now."
    show lexi casual sad:
        easein 0.4 xoffset -200
    "A warmth touches my hand. Lexi weaves her fingers into mine, and I feel all the tension just melt out of me."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    stop music fadeout 1.0
    play music mscromance
    "(There she is. The real Lexi. I can feel her warmth as she provides her shoulder for me to rest my head.)"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    "I look to find her staring at our interlaced hands."
    show lexi casual_cu sleep_cu
    lx "There was a moment, that night in the sand, when I felt like I could do this forever."

    lx "That I could give up the world and stay in just one place, on that beach every night. Because that's where you were."

    lx "No one's ever made me feel that way before... it scared me."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She was scared of how I make her feel?)"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "It felt good to imagine... us, so good, but also it feel too good to be true, like I was being naive or something."
    show lexi casual_cu sleep_cu
    lx "I thought about people I've watched settle down and do nothing with their lives, and I panicked a little."
    show lexi casual_cu embarrassed_cu
    "I squeeze Lexi's hand."
    hide lexi
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mclexi "I don't want to make you feel trapped, Lexi. I just... I don't want to be left behind."
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi smiles, a small and sad kind of smile that I'm not used to seeing from her."
    show lexi casual_cu embarrassed_cu
    lx "This thing, with you, is all new to me. For all the danger I've gotten into, and the scars I have to prove it... you scare me sometimes."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Me? Scare you?"
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "She laughs, like even she didn't expect to say what she just did. She brings one of her hands up to meet the other, clasping mine."

    lx "I don't know if I'll always want to stay, or when the need to run will come over me. But..."

    lx "I'll never leave you behind like that again. Because you're right, we have so much fun together."
    hide lexi
    "I laugh too, just as shy, but the nerves melt away as Lexi presses her lips to mine for a deep kiss as she holds me against her."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(You can't hit every wave on your first try. Sometimes it takes a little practice to figure it out. I want Lexi and I to figure it out.)"

    "(I'm so glad she opened up to me and told me.)"
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    "A sudden beeping sound causes us to break apart. Lexi looks down at her watch; her alarm is going off."
    show lexi casual_cu smile_cu
    lx "It's showtime. Let's go steal a magic mer orb."

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
