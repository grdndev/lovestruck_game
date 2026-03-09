label arianna_season2_episode7:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_arianna_studio_day at bg
    play music mscsuspense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show maxime mermaid_cu sad_cu at maxime_cu
    "Arianna doesn't stop looking at Maxime but Casper stiffens as Maxime's eyes run over the studio."
    hide maxime
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(He's here on government business because there's a rumor Arianna is with the resistance!)"
    "(And that this is an illegal {i}art{/i} studio, which I guess by mer law it is. Oh this is bad.)"
    hide mscmc
    show maxime mermaid sad at left3
    show arianna siren surprised at right3
    ai "Resistance?"
    show arianna grin
    "Arianna laughs lightly as though she doesn't know what Maxime is talking about."
    ai "Resistance for what?"
    hide maxime
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(She thinks well on her feet, thank god.)"
    hide mscmc
    show maxime mermaid basic at left3
    show arianna siren basic at right3
    mx "The artist resistance against the government and its bureau for the control of magic and art."
    hide maxime
    show casper casual confused at left2
    cs "Oh. I think I've heard of them on the news."
    show casper angry
    "Casper crosses his arms."
    ai "Same, but I don't know anything about them."
    ai grin "And this isn't an art studio."
    hide casper
    show arianna surprised
    show maxime mermaid basic at left3
    mx "I see...I guess it could look more like an engineering lab to me."
    hide maxime
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(No way this place looks like an engineering lab. Is he giving them an out?)"
    hide mscmc
    show maxime mermaid basic at left3
    show arianna siren basic at right3
    "Arianna sweeps her arms over the studio."
    ai "It's just a lot of weird engineering projects we're messing around with."
    hide maxime
    show casper casual angry at left2
    cs "We're collectors, more than anything. A lot of this is just stuff we've found."
    hide casper

    stop music fadeout 0.5
    play music mscmaxime fadein 1.0
    show maxime mermaid basic at left3
    "Maxime nods and a very small upward tilt appears at the corner of his mouth."
    hide maxime
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Maxime would go against the government he works for? There's more to him than I thought.)"
    hide mscmc
    show arianna siren smile at right3
    show casper casual angry at left2
    ai "We love...engineering. It's our hobby."
    hide arianna
    hide casper
    show maxime mermaid basic at centre
    "Maxime nods, taking one last fast look around the place."
    mx smile "I don't see any illegal activities happening here and met no resistance to my investigation."
    hide maxime
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Oh my god. Maxime, thank you.)"
    hide mscmc
    show maxime mermaid basic at left3
    show arianna siren basic at right3
    "Maxime pulls out a small shellphone and says some quick codewords into it."
    mx smile "I didn't think you'd know anything about the resistance, important to double check rumors though."
    show maxime basic
    ai grin "I barely know anything about it."
    hide maxime
    show casper casual basic at left2
    show arianna basic
    cs "Me too. I don't know what put this place on the government's radar."
    hide arianna
    hide casper
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(It's so obvious that everyone here is pretending, I wonder why Maxime is helping?)"
    show mscmc sad_cu
    "(If Maxime hadn't showed up and it was a different government agent instead, who knows what could've happened?)"
    hide mscmc
    show maxime mermaid basic at left3
    show arianna siren smile at right3
    mx "People talk and get suspicious, that's all. Not all tips are true."
    "Maxime shrugs as he starts swimming backwards towards the exit."
    show arianna basic
    mx sad "Sorry to have disturbed you. Please let me know if you ever hear anything about any resistance."
    show maxime basic
    ai grin "Glad we could clear our names."
    "Arianna closes her hand over the ring on her finger as she smiles nonchalantly."
    hide maxime
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Arianna's been so casual this whole time, I can't imagine how she's feeling on the inside.)"
    hide mscmc
    show maxime mermaid basic at centre
    "Maxime gives them a parting nod."
    mx "Have a good rest of your day."
    show maxime sad
    "He pauses and I hold my breath, unsure of what's going to happen next."
    mx basic "Even though I totally believe that this is all engineering stuff... You two should lay low for a bit."
    mx smirk "And same to whoever is hiding in there with us."
    hide maxime
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(How did he know? He must be scary good at his job.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show maxime mermaid basic at centre:
        pause 0.3
        linear 0.4 xoffset -100 alpha 0.0
    pause 0.7
    "Maxime leaves and for a moment, nobody moves."
    hide maxime
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Maxime is on our side?)"
    hide mscmc
    show arianna siren sad at right3
    show casper casual confused at left2
    "Arianna and Casper both sag like the life has been sucked out of them."
    hide arianna
    hide casper
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(If they had gotten arrested just now, I proably wouldn't have ever seen Arianna again. I don't want to think about that.)"

    show mscmc bikini_hairdown basic at centre:
        xoffset 200 yoffset 100 alpha 0.0
        pause 0.1
        parallel:
            easein 0.6 xoffset 0
        parallel:
            easein_circ 0.3 yoffset 150
            easein_circ 0.3 yoffset 0
        parallel:
            linear 0.6 alpha 1.0
    "I swim out from my hiding spot, still feeling unnerved and go to be with Arianna."
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e7c1:
        "A. Arianna, you okay?":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            mcarianna "Are you okay, Arianna?"
            hide mscmc
            show casper casual basic at left2
            show arianna siren basic at right2
            cs "I'm fine."
            show arianna sleep
            "Arianna only nods her head."
        "B. That was terrifying.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            mcarianna "Um, that was kind of terrifying."
            hide mscmc
            show casper casual confused at left2
            show arianna siren angry at right2
            cs "I would've taken him out if he tried to arrest us."
            cs "I'm glad it didn't come to that."
        "C. Crisis averted?":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcarianna "So, crisis averted?"
            show mscmc sad_cu
            "(Though, it's sort of an ongoing crisis seeing as they're always at risk of getting arrested.)"
            hide mscmc
            show casper casual confused at left2
            show arianna siren sleep at right2
            cs "At least for now, I guess."

    hide casper
    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    show mscmc bikini_hairdown surprised at left1
    show arianna siren sad at right2:
        easein 0.4 right1
    "Arianna swims the remaining distance to me and wraps her arms around me in a tight hug, pulling us together."
    hide mscmc
    show arianna siren_cu sleep_cu at arianna_cu
    "She buries her face into my neck and I feel her heavy sigh against my skin."
    hide arianna
    show mscmc bikini_hairdown_cu sleep_cu at mscmc_cu
    "I stroke Arianna's smooth long hair and close my arms around her in return as she holds onto me."
    hide mscmc
    show casper casual confused at centre
    cs "Um, I'm gonna get going for now."
    hide casper
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    mcarianna "Stay safe out there."
    hide mscmc
    show casper casual angry at centre
    cs "I will. That was a close call. See you guys later."
    show casper:
        linear 0.4 xoffset -150 alpha 0.0
    "As Casper leaves, Arianna gives a weak wave in his direction before bringing her arm back to wrap around my waist."
    hide casper
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "I can feel Arianna's heart pounding in her chest we're so close together, I never want to let her go."
    hide mscmc
    show arianna siren_cu sleep_cu at arianna_cu
    "She hugs me tighter as though I'm what's grounding her in the present."
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Arianna has been dealing with so much these past few days.)"
    mcarianna embarrassed_cu "Are you sure you're okay?"
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    ai "Me?"
    show arianna sad_cu
    "Arianna lifts her head and holds me out at arms length then brings me close again, her voice wavering."
    ai "I'm the one who dragged you into this mess. I should be asking if {i}you're{/i} okay."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(She doesn't need to worry about me right now.)"
    show arianna siren surprised at right1plus behind mscmc
    show mscmc bikini_hairdown smile at left1:
        xoffset 20
    mcarianna "I'm here by my own free will because I want to be. You didn't drag me into anything. I want to be here, even for the hard parts."
    hide mscmc
    show arianna siren_cu sad_cu at arianna_cu
    "Arianna cups my face in her hands, her eyes searching mine as though to confirm I'm telling the truth."
    ai embarrassed_cu "Has anyone ever told you that you're amazing?"
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    mcarianna "Once or twice."
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    "She laughs and puts her forehead on my shoulder, she's starting to get her usual energy back."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(I'm glad she's unwinding a little bit after what just happened with Maxime.)"
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    ai "I want to do something for you."
    show mscmc bikini_hairdown embarrassed at left1
    show arianna siren smile at right1:
        xoffset -10
        pause 0.1
        easein 0.3 xoffset 20
    "Arianna lifts her head and smiles at me as her tail fin gently waves back and forth beside her."
    mcarianna surprised "Why? You don't owe me anything for being here."
    ai grin "Do I need a reason to do something nice for you? Well, for us. I'm going to be there too."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(I'm not going to say no to that. It's sweet that she likes doing things for others.)"

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    scene black with fade
    "Once we get back to land and change, Arianna ties a blindfold around my head so I can't see our destination before we arrive."
    "Arianna guides me confidently down the boardwalk, her arm around my hips. We enter some type of building and I feel the air cool."
    ai "Okay! Time to take it off!"
    scene bg msc_siren_aquarium_lights_on at bg with eye_open
    "As Arianna's fingers delicately remove my blindfold, I realize she's taken me to the aquarium!"
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(I love this glass tunnel, I always imagine being underwater.)"
    show arianna dress embarrassed at right2 behind mscmc
    show mscmc jacket_hairup grin at left1plus
    mcarianna "Why'd you bring me here?"
    show mscmc surprised
    ai "Well, I remembered you majored in marine biology. I thought this would be your kind of thing."
    hide arianna
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(Aw. She remembered my college major. I think I just mentioned that in passing once.)"
    show mscmc jacket_hairup smile at left1plus:
        pause 0.2
        easein 0.4 left1
    show arianna dress grin at right2 behind mscmc:
        pause 0.1
        easein 0.4 right1plus
    "Arianna grins and puts her arm through mine, pulling me to her side."
    mcarianna embarrassed "I haven't been to the aquarium in a while. It's one of my favorites. Thanks."
    show arianna smile
    "Arianna's grin falls into a much softer smile as her gaze lingers on my face."
    ai embarrassed "I'm glad you liked it."
    hide arianna
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(I feel so happy. Even though there's stressful stuff going on, Arianna's over here remembering little details about me.)"
    hide mscmc
    "Arianna and I walk along the hallway, watching the array of colorful fish and organisms swim past."
    show arianna dress grin at right1plus
    show mscmc jacket_hairup surprised at left1
    ai "Do you have a favorite fish?"
    hide arianna
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e7c2:
        "A. Unicorn fish!":
            $ menuhideborder = False
            show arianna dress grin at right1plus
            show mscmc jacket_hairup grin at left1
            mcarianna "I really like unicorn fish. They have big noses."
            show mscmc smile
            ai surprised "That's why you like them?"
            show arianna grin
            mcarianna grin "They're fun to look at."
        "B. Are mermaids fish?":
            $ menuhideborder = False
            show arianna dress smile at right1plus
            show mscmc jacket_hairup grin at left1
            mcarianna "Hm...mermaids?"
            show arianna angry
            "Arianna laughs and pretends to act offended."
            ai grin "I am a mammal, thank you very much."
        "C. Not really.":
            $ menuhideborder = False
            show arianna dress smile at right1plus
            show mscmc jacket_hairup surprised at left1
            mcarianna "I dunno. There are so many cool fish."
            mcarianna grin "Colorful ones are cool."
            ai grin "Yeah, fish are beautiful."

    hide arianna
    hide mscmc
    "Arianna pauses at the glass as a few parrotfish zip by."
    show arianna dress grin at right1plus
    show mscmc jacket_hairup grin at left1
    ai "Aw, look at the parrotfish! I love their little faces."
    hide arianna
    hide mscmc
    "One of the parrotfish in question stops at the glass and seems to look at Arianna."
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(Can it sense that Arianna is of the ocean too?)"
    hide mscmc
    "As we keep walking, the fish follows alongside us and a few others join in."
    show arianna dress smile at right1plus
    show mscmc jacket_hairup surprised at left1
    mcarianna "Are they following us?"
    ai grin "Yeah, fish love hitching rides with mermaids."
    hide arianna
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(She's like a celebrity to these fish!)"
    show arianna dress embarrassed at right1plus behind mscmc
    show mscmc jacket_hairup grin at left1
    mcarianna "We paid to see the fish, but I think they should be paying us to see you."
    mcarianna embarrassed "Although, I do get where they're coming from, you're kind of enchanting."
    hide arianna
    hide mscmc
    "Arianna stops and puts one of her hands against my cheek as my heart speeds up and she steps closer."
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "You can look all you want."
    hide arianna
    "A big flounder swims over and seems to eye Arianna and we both end up laughing under its watchful look."
    show arianna dress grin at right1plus
    show mscmc jacket_hairup grin at left1
    mcarianna "Next on our adventures: touring you for meet and greets with aquarium fish."
    ai "Something tells me fish don't have a lot of money."
    show mscmc embarrassed
    "Arianna watches the fish with an enormous smile and my heart warms, she looks so happy."
    hide arianna
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(It's nice that we can finally escape all of the mer government stress for a bit.)"
    hide mscmc
    "We continue through the aquarium, pointing and 'ooing' at different fish and sea creatures as they pop up and pay extra attention to Arianna."
    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna dress basic at right1plus
    show mscmc jacket_hairup smile at left1
    ai "Hey, you ready to go?"
    show arianna:
        easein 0.3 xoffset -20
    show mscmc surprised:
        pause 0.1
        easein 0.3 xoffset 20
    "Suddenly, there's a flash of a grimace on Arianna's face and she inadvertently pulls me closer to her side."
    hide arianna
    show mscmc jacket_hairup_cu basic_cu at mscmc_cu:
        xoffset 0
    "(Maybe she's tired. It's been a long day.)"
    show arianna dress basic at right1 behind mscmc
    show mscmc jacket_hairup smile at left1:
        xoffset 20
    mcarianna "Sure, but is everything okay?"
    show mscmc basic
    show arianna smile
    "Arianna laughs lightly like she's trying to keep the mood up but then her expression falls somewhat."
    ai basic "I overhead some dolphins in the room over, they miss the ocean."
    hide arianna
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu:
        xoffset 0
    "(She can understand dolphins? And has like super hearing?)"
    show arianna dress basic at right1 behind mscmc
    show mscmc jacket_hairup surprised at left1:
        xoffset 20
    mcarianna "I thought you couldn't talk to fish?"
    ai smile "I can talk to sea mammals. It's different."
    hide arianna
    show mscmc jacket_hairup_cu smile_cu at mscmc_cu:
        xoffset 0
    "(Guess I missed that one in mermaid 101.)"
    show arianna dress basic at right1 behind mscmc
    show mscmc jacket_hairup basic at left1:
        xoffset 20
    mcarianna "Yeah, it's hard."
    show arianna smile
    "Arianna starts to walk us towards the exit as she smiles at me."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    ai "Maybe one day we'll just have to break them out."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with clockwise_wipe
    "After our day at the aquarium, Arianna sits on my bed cross legged, combing her fingers through her pale silver blue hair."
    show arianna dress grin at right2
    show mscmc casual_hairdown surprised at left1plus
    ai "We've made a lot of progress on the sculpture pieces—we should be able to finish all the scales needed tomorrow."
    show arianna smile
    mcarianna grin "Really?! I can't believe we're almost done."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(It feels like we only just started working on the piece, but also like forever.)"

    scene bg msc_mc_bedroom_night at bg with dissolve
    "I turn the light off and get into bed and Arianna gets under the covers with me. Her leg brushes mine gently."
    show arianna dress embarrassed at right2
    show mscmc casual_hairdown embarrassed at left1plus
    ai "Good night, my favorite human."
    show arianna sleep:
        easein 0.4 right1
    "Arianna weaves her fingers through mine and I hear her let out a happy sigh as she closes her eyes."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(She makes me feel so appreciated and seen.)"

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    scene bg msc_arianna_studio_day at bg with clockwise_wipe
    "The next day, we go back to Arianna's studio to make the final few scales for the sea serpent installation."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(We've made so many, I see these scales when I close my eyes, but we're finally almost done!)"
    show arianna siren grin at right1plus behind mscmc
    show mscmc bikini_hairdown smile at left1plus
    "As I go to pull the stamp down, Arianna gasps and starts counting scales on the table with her pointer finger."
    ai "We did it!"
    mcarianna surprised "We did?"
    ai "That's the last scale."
    mcarianna grin "How are the scales attached to the sea serpent's body?"
    show mscmc embarrassed
    "Arianna takes my hand off the stamp and squeezes it."
    ai "When the scales are imbued with magic, they'll also be attached to the body."
    ai "So we don't need to worry about that part."
    mcarianna surprised "Like, they'll fly on?"
    show mscmc grin
    ai smile "You'll see."
    "Arianna winks at me and then pulls out her shell phone."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Gotta love the air of mystery.)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "I'll let Grandma Q know that we're ready for the magic part to happen."
    show arianna smile_cu
    "Arianna touches some glowing symbols on her shell phone then puts it away."

    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    show arianna siren embarrassed at right1plus
    show mscmc bikini_hairdown smile at left1plus
    ai "Now...wanna celebrate?"
    show mscmc embarrassed
    "Arianna wiggles her eyebrows at me and then winks with an alluring laugh."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Whatever kind of celebration it is, I'm more than interested.)"
    hide mscmc
    "Arianna pulls a dark box with a ribbon wrapped around it from under one of the work tables."
    show arianna siren grin at right1plus
    show mscmc bikini_hairdown grin at left1plus
    mcarianna "What kind of celebration do you have in mind?"
    show mscmc embarrassed
    ai embarrassed "These are my favorite candies. They're kind of expensive and you have to go to a special store, and I'm willing to share them with you."
    show mscmc smile
    "Arianna opens the lid and I lean over her."
    hide arianna
    hide mscmc
    "The candies are small perfect squares. Almost cake-like with one golden layer and one darker."
    "In a perfect zigzag on top is a crimson drizzle and a dollop of something white and cream textured."
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(That doesn't look like anything up in the human world. But it does look really tasty!)"
    show arianna siren grin at right1plus behind mscmc
    show mscmc bikini_hairdown grin at left1plus
    ai "All you need to know before trying is that it's my favorite and super delicious."
    show mscmc embarrassed
    ai "This is something good from my world that I want to share with you."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I want to be a part of her world as much as she is a part of mine.)"
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    "Arianna picks up one of the squares in her long fingers and holdes it up towards my mouth, with a smirk, her eyes glinting at me."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Oh, she wants me to eat it from her fingers...)"
    "I can already feel my face heating up."
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    ai "I've spent a lot of time with you, I notice what you like and stuff, and I think you'll really like these."
    show arianna sad_cu
    "Arianna dazzles me with her puppy dog eyes look that she turns on with full force."
    ai embarrassed_cu "Please, try my favorite candy? I promise not to hate you if you don't like it."
    hide arianna

    $ menuhideborder = True
    menu ariannas2e7c3:
        "A. Eat mer candy from Arianna's fingers!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcarianna "You better hope I like this after selling it so well."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "I lean forward and Arianna excitedly holds it up for me and my heart pounds."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(This is a pretty intimate thing...)"
            hide mscmc
            "I'm praying my face isn't as red as I think it is when I carefully take a bite of the treat that Arianna is holding to my lips."
            "As soon as I begin to chew, it almost melts in my mouth in a swirl of flavors and textures."
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(It's delicious! Refreshing but also rich!)"
            "The candy turns airy as I swallow, leaving a sweet aftertaste."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "You like it?"
            show arianna grin_cu
            "Arianna raises her eyebrows at me in eager questioning."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "I do!"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "I knew you would like it! I told you!"
            "Arianna grins like she's proud of herself."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(She is adorable right now. Even if I hadn't liked it, I don't know if I would've said so.)"
            show arianna siren smile at right2 behind mscmc
            show mscmc bikini_hairdown grin at left1
            mcarianna "Is there spice in there? Like in Mexican chocolate?"
            show arianna embarrassed
            mcarianna "Reminds me of something like that, but then also like the texture of meringue?"
            show mscmc smile
            ai grin "I definitely need to try some Mexican chocolate, but it's not quite the same spicy you would get from human peppers."
            "Arianna picks up another square of candy as she leans towards me, pointing to the cream looking part."
            show mscmc grin
            ai "When the cream starts to melt in your mouth, it amplifies the other flavors."
            show arianna smile
            mcarianna "It's like a really really light chocolate."
            ai grin "Mhm mhm."
            show mscmc embarrassed
            "The grin on her face is joyful. I notice her tail is suspended in the water closer to my legs than before, she could wrap me up in it."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Oh my god, she is out of this world. My lips are still tingling from when they brushed against her fingertips.)"
            show arianna siren grin at right2 behind mscmc
            show mscmc bikini_hairdown grin at left1
            mcarianna "It melted so fast, but I can still taste it. It's got a nice after taste thing going on."
            ai surprised "Oh yeah, these things are dangerous!"
            ai embarrassed "You can eat like fifty of them and not even realize it."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "Arianna holds another piece up questioningly, her eyes flicking down to my lips and staying there as I nod."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(She already knows I like it, so this is more than just taste-testing, isn't it?)"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "Then please, have another one. I want to share my favorite things with you. It feels right somehow."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(My heart is hers. At this point, that's just a fact.)"
            hide mscmc
            "I take a bite and Arianna runs her fingers across my lips after she lets go of the candy, her eyes never leaving mine."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her fingers are so soft...did she do that on purpose? If she wants my mouth she can have it.)"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "A blush spreads over Arianna's face, she swishes her tail back and forth as she looks away, but when she looks back at me it's with intensity."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "You touched my lips just then."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "Did I?"
            "She smiles sweetly at me in an actof innocence but her cheeks blaze red."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I can see the blush on her face—Arianna knows exactly what I'm talking about.)"
            show arianna siren embarrassed at right2 behind mscmc
            show mscmc bikini_hairdown embarrassed at left1:
                xoffset 36
            ai "You know, if you didn't like the candy, well I don't know if we could've stayed...close."
            "Arianna tries to say it with a straight face, but she ends up hiding a laugh behind her hand."
            show arianna grin
            mcarianna grin "Shut up."
            show mscmc embarrassed
            ai embarrassed "I'm serious! These are my favorites!"
            show arianna:
                easein_back 0.4 right1plus
            show mscmc:
                pause 0.1
                easein_back 0.4 xoffset 0
            "Arianna pushes my shoulder playfully, but then her hand stays at the top of my arm as we look at each other, the air thick with longing."
            mcarianna "Well, lucky me that I have a very refined palate."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "Her fingers slide across my collarbone and her eyes rove over my body in my bikini."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I could get lost in her for the rest of eternity.)"
            mcarianna "Your turn. You did say they were your favorite."
            hide mscmc
            "I take one of the candies and hold it up towards her as her lips part slightly."
            show arianna siren_cu embarrassed_cu:
                xanchor 0.5 yanchor 0.42 xpos 0.5 ypos 0.5
            ai "Are you nervous?"
            show arianna:
                xanchor 0.5 yanchor 0.42 xpos 0.5 ypos 0.5
                linear 0.5  zoom 1.05
            "Arianna leans forward tantalizingly slowly and brushes one of my locs behind my ear."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "What would I be nervous about?"
            "(Nothing out of the norm. Just a super awesome beautiful woman eating candy from my fingers and definitely diving me eyes.)"
            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu
            "As she places her pouty pink lips delicately around the candy, she keeps her eyes on mine."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "I feel the hint of her lips on my fingers and fire burns through my hands."
            "(I want to grab her and kiss her.)"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "Mmmm...I think it tastes better when you're the one giving it to me."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "I need to remind myself to breathe."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "Last one?"
            "Arianna picks up the final candy and offers it to me with a smirk."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(At this point, we're using the candy as an excuse to brush each other's lips with our fingers, and I do not mind.)"
            mcarianna "Thanks."
            hide mscmc
            "But even as I take the candy into my mouth, her fingers don't move from my lips, as the candy quickly evaporates in my mouth."
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "Is it good?"
            "Arianna looks down to my mouth and her thumb drags across my lower lip."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I don't think we're talking about the candy anymore.)"
            mcarianna "I want more."
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "Arianna slowly lets her fingers trail over my jaw and down my neck."
            ai "You have beautiful lips."
            "Her eyes shoot up to meet mine again and I feel my heart stop."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I don't even know what to say. All I want is for her to kiss me.)"
            hide mscmc
            show arianna siren_cu embarrassed_cu:
                xanchor 0.5 yanchor 0.42 xpos 0.5 ypos 0.5
            "Arianna cups my cheek and tilts her head, slowly coming closer as her other hand encircles my waist and her eyes half-close."
            show arianna siren_cu embarrassed_cu:
                xanchor 0.5 yanchor 0.42 xpos 0.5 ypos 0.5
                linear 0.4 zoom 1.08 alpha 0.0
            "She pulls me into her and our lips are drawn to one another, closing the last remaining space..."
            hide arianna

            stop music fadeout 0.5
            play music mschappytimes fadein 1.0
            qn "Arlight girls, are we ready?"
            show arianna siren surprised at right1plus:
                xoffset -30
                pause 0.1
                easein_back 0.4 xoffset 0
            show mscmc bikini_hairdown surprised at left1plus:
                xoffset 30
                pause 0.1
                easein_back 0.4 xoffset 0
            "Queenie's voice sounds from just outside the studio entrance and Arianna and I jump apart in surprise."
            hide arianna
            show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
            "(Queenie, couldn't you have showed up just a few minutes later?)"
            hide mscmc
            show arianna siren_cu angry_cu at arianna_cu
            ai "Hi, grandma Queenie."
            hide arianna
            show queenie casual smile at left1plus:
                xoffset 150 alpha 0.0
                pause 0.1
                parallel:
                    easein 0.5 xoffset 0
                parallel:
                    linear 0.5 alpha 1.0
            "Arianna waves to Queenie while trying to hide her bright red face."

        "B. Hesitate.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
            "(It does look good, but what if I don't like it and hurt her feelings?)"
            show arianna siren grin at right1plus behind mscmc
            show mscmc bikini_hairdown basic at left1
            "Arianna sees my hesitation and laughs."
            show mscmc smile
            ai "Well, I won't force you."
            "She pops the candy into her mouth and a look of delight passes over her face."
            mcarianna "Promise I'll try out some of your world eventually."
            hide arianna
            hide mscmc

            show queenie casual smile at left1plus:
                xoffset 150 alpha 0.0
                pause 0.1
                parallel:
                    easein 0.5 xoffset 0
                parallel:
                    linear 0.5 alpha 1.0
            "Just then, Queenie swims through the entrance of the studio."
            hide queenie
            show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
            "(And now the moment to try the candy is definitely gone.)"
            hide mscmc
            show queenie casual smile at left1plus

    qn "It's time to cast the spell on the scales."
    show neptria siren basic at right3:
        xoffset 100 alpha 0.0
        parallel:
            easein 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    "Neptria swims in not long after Queenie with a bag over her shoulder and gives us an unenthused wave."
    hide queenie
    hide neptria
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I can't believe I get to witness a spell being cast!)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    "Arianna grins at me, she also seems amped up about the spell, this must not be and every day kind of thing."
    ai smile_cu "Ready to see some serious mer magic go down?"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
