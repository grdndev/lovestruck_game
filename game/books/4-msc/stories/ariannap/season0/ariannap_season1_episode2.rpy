label ariannap_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_tide_pools_sunset at bg
    play music mscarianna
    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show arianna siren smile at centre
    "Arianna leans back on her hands and presents her tail, water gliding down the sides."

    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Mermaids are real!)"

    show mscmc jacket_hairdown surprised at left2
    show arianna siren grin at right3
    "When I glance up, Arianna is watching me with a toothy grin."

    show mscmc embarrassed
    "Embarrassed heat rushes over me and I straighten my back."

    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What am I even thinking?)"
    "(I wish mermaids were real, but they're not.)"

    hide mscmc
    show arianna siren grin at centre
    ai "Well? What do you think?"

    show arianna smile
    "Arianna puts her hands together and presses her lips against them."
    ai "You're the first person I've ever shown."

    show arianna grin
    "She laughs, shaky but delighted."

    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna has to be messing with me.)"

    show mscmc jacket_hairdown surprised at left3
    show arianna siren basic at right3
    mcariannaprev "I don't really understand what's going on."

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna sad
    "Arianna drops her hands, knitting her brows with confusion."
    ai "[genericfn], I'm trying to tell you that I'm a mermaid!"

    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(It must be some expensive fake tail. There's no way this is real.)"


    show mscmc jacket_hairdown surprised at left3
    show arianna siren basic at right3
    mcariannaprev "But I saw you on the beach earlier, walking."
    mcariannaprev "With legs."

    show arianna sleep
    show mscmc basic
    "Arianna makes an exasperated sign and shakes her head."

    ai basic "I {i}did{/i} have legs. It's magic."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Magic...of course.)"

    hide mscmc
    show arianna siren_cu sad_cu at arianna_cu
    "She flashes me puppy dog eyes filled with pleading."

    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is there a possibility that she's telling the truth?)"
    "(If mermaids are real, that would be a dream come true.)"

    show mscmc jacket_hairdown basic at left3
    show arianna siren sad at right3
    ai "Look, I took a chance with you because I think you can help me."

    show arianna basic behind mscmc:
        easein 0.5 right1
    "The tip of Arianna's tail dips back into the water as she shifts closer."
    ai sad "I'm an artist and a human's been stealing my sculptures."
    ai "I have no idea how to get them back, so I need you."
    show mscmc sad
    "The sudden intensity in her gaze makes it hard to look away."
    ai "I swear to you, I'm not lying."

    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(A mermaid artist who's the victim of art fraud. Got it.)"

    hide mscmc
    $ menuhideborder = True
    menu ariannas0e2c1:
        "A. Play along.":
            $ menuhideborder = False
            show arianna siren sad at right1plus
            show mscmc jacket_hairdown surprised at left2
            mcariannaprev "Right. Okay."
            mcariannaprev "And how is this {i}human{/i} getting your art?"
        "B. Try to understand.":
            $ menuhideborder = False
            show arianna siren basic at right1plus
            show mscmc jacket_hairdown surprised at left2
            mcariannaprev "So, a human is stealing your stuff?"
            mcariannaprev sad "Sorry, I'm just trying to wrap my head around this."
        "C. Level with her.":
            $ menuhideborder = False
            show arianna siren sad at right1plus
            show mscmc jacket_hairdown sleep at left2
            "I pinch the bridge of my nose and sigh."
            mcariannaprev surprised "Do you realize how insane that sounds?"

    show arianna basic
    show mscmc basic
    "Arianna clicks her tongue and then sets her jaw."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I want to believe her more than anything, but I used to get bullied for this kind of stuff.)"

    show arianna siren smile behind mscmc at right1plus
    show mscmc jacket_hairdown basic at left2
    ai "We're in the same boat here. I'm your first mermaid and you're my first human."
    ai embarrassed "You have these toned legs and cute little ears."
    show mscmc surprised
    "I raise a hand and touch my earlobe."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She thinks my ears are cute?)"
    hide mscmc
    show arianna siren smile at centre
    "Arianna slides herself back into the water and smirks up at me with bright eyes."
    ai "Allow me to show you something a human {i}can't{/i} do."

    show arianna siren smile at centre:
        transform_anchor True anchor (0.5, 0.75) yoffset 947 xoffset 67
        pause 0.2
        linear 0.6 alpha 0.0 zoom 0.9
    "After swimming out beyond the tidepools, Arianna disappears under the water."

    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Definitely the weirdest date I've ever been on.)"

    hide mscmc
    "Suddenly, Arianna launches herself out of the water and into the air."
    "She twirls - the setting sun reflecting off her tail to make her scales look like jewels."

    show mscmc jacket_hairdown surprised at centre
    "I feel frozen in a trance, my heart pounding in my chest."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I always believed in magic, I guess I still want it to be true.)"
    "(But I was the last one of my friends to outgrow make believe and they made fun of me.)"

    show mscmc jacket_hairdown sleep at centre
    "As Arianna resurfaces and starts swimming back to me, I shake away the possibility."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(No. No way. She has to be a synchronized swimmer or something.)"

    show mscmc jacket_hairdown surprised at left2
    show arianna siren smile behind mscmc at right7:
        pause 0.1
        easein 0.8 right1plus
    "Arianna is back on the edge of the tidepools now, a brow quirked at me."
    mcariannaprev sad "It was cool, but..."

    show arianna basic
    mcariannaprev "Not enough to convince me you're literally a mermaid."

    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    "Arianna rolls her eyes after a scoff."

    show mscmc jacket_hairdown sad at left2
    show arianna siren angry at right2:
        xoffset -20
    ai "Whatever. I'll handle my problem myself."

    hide mscmc
    show arianna siren basic at centre:
        xoffset 0
    "From under the water, she procures a conch shell that she sets beside me."

    show arianna sleep
    "She taps it with a finger."

    show mscmc jacket_hairdown basic at left2
    show arianna siren basic at right2
    ai "If you decide to stop being annoying, give me a call."
    ai "You just say my name and put your ear to it."
    mcariannaprev surprised "Can't you just say sike and we move on?"
    show mscmc basic
    "Arianna's silent. With one hand, she reaches towards my face."
    "Then she seems to think differently."

    show arianna siren basic at right2:
        transform_anchor True anchor (0.5, 0.75) yoffset 947 xoffset 67
        pause 0.5
        linear 0.6 alpha 0.0 zoom 0.9
    "She dives off the tide pools without another word."
    hide arianna
    show mscmc surprised
    "My hand moves to rub at my temples."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I must be losing my mind.)"

    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    scene bg msc_surf_shop_day at bg
    show trina casual smile at centre
    with fade
    so "Better luck next time, kid."
    "Trina triumphantly displays the matcha tea that I bought her after yesterday's wipeout."

    show mscmc casual_hairdown grin at left2
    show trina at right2
    mcariannaprev "Don't get used to it."
    mcariannaprev smile "The surfing tournament is coming up and once I hit that barrel, it's over for you."

    hide trina
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I know I'll do well, I just can't lose focus.)"
    show mscmc sad_cu
    "(There's no time to think about how Arianna looked with the sun behind her.)"

    show mscmc casual_hairdown basic at left2
    show trina casual smile at right2
    "Trina leans on the counter, wiggling her eyebrows at me."
    so "Soooo, how was your date? You haven't said a word about it."
    hide trina
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(It's not like I can tell Trina about what happened. I'm not even sure what happened!)"

    hide mscmc
    $ menuhideborder = True
    menu ariannas0e2c2:
        "A. Be short about it.":
            $ menuhideborder = False
            show mscmc casual_hairdown sad at left2
            show trina casual basic at right2
            "I rub my collarbone."
            mcariannaprev "It was fine, I guess."
        "B. Dodge the quesiton.":
            $ menuhideborder = False
            show mscmc casual_hairdown surprised at left2
            show trina casual basic at right2
            mcariannaprev "You kept pestering me about buying your drink."
            mcariannaprev basic "I didn't even have time to talk about it."
        "C. Don't talk about it.":
            $ menuhideborder = False
            show mscmc casual_hairdown sleep at left2
            show trina casual basic at right2
            "A deep sigh leaves me."
            mcariannaprev sad "Honestly, I don't really know."

    show mscmc sad
    show trina sad
    "Taking a long-winded slurp from her drink, Trina narrows her eyes at me."

    hide trina
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Why did Arianna do that? We had just met too.)"
    "(I have no idea what to think.)"

    show mscmc casual_hairdown sad at left2
    show trina casual sad at right2
    so "You don't sound very excited. Did something-?"

    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    hide mscmc
    hide trina
    show hamish casual basic at left7:
        xoffset -20
        pause 0.2
        easein 0.7 centre
    "The shop's door swings open and Hamish saunters in."

    show hamish sleep
    "He dips his head towards us."
    rm basic "Ladies."

    hide hamish
    show mscmc casual_hairdown angry at left2
    show trina casual angry at right2
    "Trina and I groan in unison."

    hide trina
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Hamish can't even go one day without boasting to us about buying the shop.)"

    show mscmc basic_cu
    "(Though for once I'm grateful he interrupted our conversation.)"

    hide mscmc
    show trina casual angry at centre
    so "Why are you here {i}again{/i}? It's too early for this."

    hide trina
    show hamish casual sleep at centre
    "Hamish adjusts his suit jacket and pushes his shoulders back."
    rm angry "Always with the attitude. I'm helping you out, aren't I?"
    rm "You can no longer afford keeping this place and I'm taking it off your hands."

    show hamish casual_cu smile_cu at hamish_cu
    "He flashes a smile."

    show hamish casual smile at centre
    rm "You might even like me if you give me a chance."
    rm "I can teach you how to run a real business."

    hide hamish
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(As if. He has no respect for what this place means to Trina or to the kids I teach, or me.)"
    show mscmc sad_cu
    "(Trina's dad loved this place...he ran it until he died. He would hate this.)"
    show mscmc casual_hairdown angry at centre
    mcariannaprev "It's more than just a mortgage. This place means something to people."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I was lost when I came to LA, but this shop gave me a home.)"
    show mscmc casual_hairdown angry at centre
    mcariannaprev "Not that you could appreciate something like that."

    show mscmc casual_hairdown angry at left2
    show hamish casual angry at right3
    "Hamish steps closer to me, a sneer on his face."
    rm "I'll have you know that I appreciate many things."

    hide hamish
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Things like money and showboating.)"

    hide mscmc
    show trina casual basic at centre
    "Trina casts me a disbelieving look."

    hide trina
    show hamish casual smile at centre
    rm "For instance, fine art."

    rm "Pretty soon, I'll be known across the art world."

    hide hamish
    show trina casual angry at centre
    so "And how exactly is that? You don't strike me as the artistically inclined type."

    hide trina
    show hamish casual smile at centre
    "Clearing his throat, he raises his chin higher."

    hide hamish
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(This'll be good.)"

    hide mscmc
    show hamish casual smile at centre
    rm "My diving team found a stash of divine sculptures at the bottom of the sea."
    rm "No artist means no owner. In fact, I've already sold one to Jerry's Beach Bar."

    hide hamish
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Wait, sculptures at the bottom of the ocean?)"
    "(Isn't that what Arianna was talking about?)"

    hide mscmc
    show trina casual angry at centre
    so "You don't like art, Hamish. You like the money it gives you."

    hide trina
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna said that a human was stealing her sculptures. Is that human Hamish?)"
    "(Does this mean she was telling the truth? This can't be a coincidence.)"

    show mscmc casual_hairdown surprised at centre
    "I put a hand to my mouth, a wave of excitement washing over me."

    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(What if Arianna's actually a mermaid?)"

    hide mscmc
    show hamish casual basic at centre
    rm "I care about the art, Trina. I'm a businessman, I shouldn't be punished for that."

    show hamish casual basic at left4
    show trina casual angry at right4
    so "A businessman who pawns found art off as his own."

    show hamish surprised
    show trina basic
    "My abrupt movement behind the counter makes Trina and Hamish pause for a moment."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    hide hamish
    hide trina
    show mscmc casual_hairdown surprised at centre
    mcariannaprev "I forgot something in my room. Be right back!"
    hide mscmc
    "They barely acknowledge me as they return to bickering."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(The shell phone - Arianna said I can use it to call her.)"
    hide mscmc
    "I sneak out the back to race to my room."

    scene bg msc_mc_bedroom_day at bg with fade
    "The conch is sitting on my dresser -- if nothing else it's a nice decoration."

    show mscmc casual_hairdown embarrassed at centre
    "I suck in a deep breath and put the shell to my ear, a bit embarrassed."

    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(This feels silly. What if I'm just falling for her joke?)"

    show mscmc casual_hairdown basic at centre
    mcariannaprev "Arianna."

    play sound "<to 3>audio/sfx/bubbles_003_6397.mp3" fadeout 0.5

    "There's a bubbling sound. It bubbles twice and then stops."
    show mscmc surprised
    ai "I see you're coming around."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(I can't believe it actually works!)"
    show mscmc casual_hairdown sad at centre
    mcariannaprev "I'm sorry I didn't believe you...but I do now."
    show mscmc basic
    "Arianna makes a hum, the smile clear in her voice."
    ai "Go to the beach and swim out. I'll meet you there."
    "There's a click. Nothing but the sound of the ocean."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(She hung up on me!)"
    show mscmc basic_cu
    "(Maybe merpeople don't say goodbye?)"

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    scene bg msc_labeach_day at bg with fade

    "Getting to the beach doesn't take long."
    "I walk into the water and, with my surfboard, paddle out."

    scene bg msc_ocean_wide_day at bg with dissolve
    pause 0.4
    show arianna siren smile at centre:
        transform_anchor True rotate 0 yoffset 400 xoffset 70
        rotate 8
        pause 0.1
        parallel:
            easein 0.5 xoffset 0
        parallel:
            linear 0.4 rotate 0
        parallel:
            easein 0.5 yoffset -20
            easein 0.2 yoffset 60


    "Arianna's head appears from out of the water with an awfully smug look."
    ai "Well?"
    hide arianna
    show surfboard back_cu at centre
    show mscmc bikini_hairup_cu basic_cu at mscmc_cu
    "(She looks annoyingly proud of herself.)"

    show surfboard back at left3:
        zoom 0.9 xoffset -20
    show mscmc bikini_hairup basic at left3:
        yoffset 60
    show arianna siren basic at right3:
        yoffset 60
    "Slipping off my board, I get into the water with Arianna."

    hide surfboard
    show mscmc sad:
        easein_back 0.4 yoffset 80

    mcariannaprev "Look, I'm sorry. I believe you, okay?"
    mcariannaprev surprised "Mermaids. Art. All of it."
    hide mscmc
    show arianna siren_cu sad_cu at arianna_cu:
        yoffset 0
    "Arianna pouts out her bottom lip as she turns away from me."

    show arianna siren sad at right3:
        yoffset 70
    show mscmc bikini_hairup basic at left3:
        yoffset 90
    ai "You're lucky I even picked up your call."

    hide arianna
    show mscmc bikini_hairup_cu sad_cu at mscmc_cu:
        yoffset 0
    "(I might deserve this just a teeny bit.)"

    hide mscmc
    show arianna siren smile at centre:
        yoffset 70
    "Arianna glances back, something of a smile on her face."
    ai grin "Honestly, I kind of expected you to not believe it."

    show arianna siren smile at right3:
        yoffset 90
    show mscmc bikini_hairup smile at left3:
        yoffset 100
    mcariannaprev "I think I can make it up to you."

    show arianna basic
    mcariannaprev basic "The guy who's stealing your art is named Hamish."

    show arianna sad
    "Arianna sucks in a breath, shock melting her stubborn posture."
    show arianna:
        easein 0.3 yoffset 85
    mcariannaprev angry "And he's more than just an art thief."
    mcariannaprev "He's buying my friend's surf shop and that place means a lot to her and me."
    mcariannaprev "Hamish is the {i}worst{/i}."
    ai basic "He certainly sounds like it."

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    hide mscmc
    show arianna siren_cu basic_cu at centre:
        transform_anchor True align (0.5, 0.5) yoffset 60 zoom 0.9 alpha 0.0
        linear 0.6 zoom 1.0 alpha 1.0
    "Arianna leans in, her eyes holding mine."

    hide arianna
    show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu
    "(She's like a magnet...I don't think I could look away if I wanted to.)"

    show arianna siren basic at right3:
        yoffset 95
    show mscmc bikini_hairup basic at left2:
        yoffset 95
    ai "Look, I don't want to owe anyone anything."
    ai smile "If you can help me with my problem, I'll help you with the shop."

    hide arianna
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(I'm not exactly sure how Arianna can help with the surf shop.)"
    show mscmc grin_cu
    "(But she's a real mermaid! I wouldn't mind spending more time with her.)"

    show arianna siren smile at right3:
        yoffset 95
    show mscmc bikini_hairup grin at left1plus:
        yoffset 95
    ai "Deal?"
    show mscmc sleep
    "I brush my knuckles under my chin as I manage to drop Arianna's gaze."

    hide arianna
    show mscmc bikini_hairup_cu basic_cu at mscmc_cu:
        yoffset 0
    "(Life has finally started to go my way.)"
    "(I've put so much into surfing to be where I am.)"
    show mscmc surprised_cu
    "(What if this jeopardizes that?)"

    show surfboard back behind mscmc at centre:
        zoom 0.9 xoffset -10
    show arianna siren smile at right3:
        yoffset 95
    show mscmc bikini_hairup basic at left2:
        yoffset 95

    "Hands on my board, Arianna begins playing with one of her rings."
    ai basic "I've never met a human before. My people...we're not allowed to interact with you."
    show mscmc:
        easein 0.4 yoffset 90
    ai smile "When I saw you, I just felt this feeling. Like I can trust you."
    show arianna embarrassed
    show mscmc embarrassed:
        easein 0.4 yoffset 95
    "A feeling of pride swells in my chest and when I look at Arianna, she's chewing on her lip."
    ai "If asking questions would make you feel better, ask me anything."

    hide arianna
    hide surfboard
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(She's trying to open up to me.)"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show mscmc grin_cu
    "(This might be the best chance to get to know her better.)"

    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    ai "[genericfn], do you want to know about mermaids?"

    hide arianna
    $ menuhideborder = True
    menu ariannas0e2c3:
        "A. Ask Arianna about mermaids!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show arianna siren smile at right3:
                yoffset 95
            show mscmc bikini_hairup surprised at left2:
                yoffset 95
            mcariannaprev "So, I'm the first human you've ever talked to?"

            show arianna sleep
            show mscmc basic
            "Arianna nods, her thumb and forefinger stuck to her necklace."
            show arianna basic:
                ease 0.4 yoffset 100
            "She grips it tighter."
            ai smile "Yes. Congratulations."

            show arianna grin
            show mscmc smile
            "Some of the awkward tension fizzles away as Arianna giggles at that."

            hide arianna
            show mscmc bikini_hairup_cu smile_cu at mscmc_cu:
                yoffset 0

            "(It does actually feel like some kind of honor.)"
            "(Arianna said that merpeople aren't allowed to talk with humans, but she trusts me.)"

            show arianna siren smile at right3:
                yoffset 95
            show mscmc bikini_hairup smile at left2:
                yoffset 95
            mcariannaprev "Obviously you can see there's loads of us humans."
            mcariannaprev surprised "Are there many other merpeople?"
            show mscmc basic:
                easein 0.4 yoffset 90
            ai grin "{i}Tons{/i}. There's a whole city just a bit out."
            show mscmc surprised:
                easein 0.4 yoffset 95
            ai "I was born there."

            hide mscmc
            show arianna grin at centre:
                xoffset -50
            "She drops her necklace so that she can make a grand sweeping gesture with her arms."

            hide arianna
            show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
            "(A whole city full of merpeople?)"
            show mscmc smile_cu

            "(I wonder if the city is overrun with fish and sea creatures. That would be their wildlife, I guess.)"

            show mscmc bikini_hairup smile at left2:
                yoffset 100
            show arianna siren grin at right3:
                yoffset 90
            mcariannaprev "I can't believe there are mermaid cities right under our noses."
            show arianna basic
            mcariannaprev grin "What's the city like?"
            show arianna sleep
            "Arianna takes in a sharp breath and then shrugs."
            show mscmc surprised:
                easein 0.4 yoffset 105
            show arianna smile:
                easein 0.4 yoffset 85
            ai "Skyscrapers. The local Kraken. Public transport. You name it."
            show mscmc:
                easein 0.4 yoffset 100
            show arianna:
                easein 0.4 yoffset 90
            mcariannaprev "How does your society stay hidden?"
            mcariannaprev grin "I would think underwater skyscrapers would be a giveaway."

            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu:
                yoffset 0
            "Arianna raises her brows and sprouts a grin."

            show mscmc bikini_hairup grin at left2:
                yoffset 100
            show arianna siren grin at right3:
                yoffset 90
            ai "With magic!"

            hide mscmc
            show arianna siren_cu sad_cu at arianna_cu:
                yoffset 0
            "Then her face falls as she looks over the water."

            show mscmc bikini_hairup basic at left2:
                yoffset 100
            show arianna siren sad at right3:
                yoffset 90
            ai "We can't all use magic - only the government is allowed to."
            ai basic "They use it to keep us safe."

            hide arianna
            show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
                yoffset 0
            "(Maybe they aren't so different from us. That sounds like human rhetoric.)"

            show mscmc bikini_hairup surprised at centre:
                yoffset 60
            "I follow Arianna's gaze over the water, a story popping into my mind."

            show mscmc sad
            "There are a lot of old tales of mermaids luring humans in and singing them to their deaths."

            show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
                yoffset 0
            "(Is this some kind of elaborate scheme to trap me?)"
            "(Arianna doesn't seem the type, but are those myths based on truth?)"

            show mscmc bikini_hairup basic at centre:
                yoffset 60
            "I can't help but stiffen at the thought. My fingers curl into my hand."
            show mscmc bikini_hairup basic at left2:
                yoffset 100
            show arianna siren surprised at right3:
                yoffset 90
            ai "What's wrong?"

            show arianna basic
            mcariannaprev sad "When I was a kid, people told me some nasty legends about mermaids."

            stop music fadeout 0.5
            play music mschappytimes fadein 1.0

            hide arianna
            show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu:
                yoffset 0
            "Embarrassment at my thoughts makes my ears burn, but I muster a breathy chuckle."

            show mscmc bikini_hairup smile at left2:
                yoffset 100
            show arianna siren basic at right3:
                yoffset 90
            mcariannaprev "Um, you're not going to sing me to my death, are you?"

            show arianna grin
            "Arianna laughs loudly and brings a hand to her mouth."
            ai "My voice is pretty killer, but not literally."

            hide arianna
            show mscmc bikini_hairup_cu smile_cu at mscmc_cu:
                yoffset 0
            "(Not that I feel endangered by Arianna, but it is good to know.)"
            show mscmc bikini_hairup smile at left2:
                yoffset 100
            show arianna siren grin at right3:
                yoffset 90
            "She shakes her head, an amused grin on her face as she wipes a tear of laughter away."
            ai "The mermaids from the deep have more hostile tendencies."
            ai "But killing is frowned upon, especially concerning humans."
            ai smile "Even deep mermaids aren't ruthless killers."

            hide arianna
            show mscmc bikini_hairup_cu basic_cu at mscmc_cu:
                yoffset 0
            "(I guess the same could be said for humans, but murder is more than just frowned upon.)"

            show mscmc bikini_hairup surprised at left2:
                yoffset 100
            show arianna siren smile at right3:
                yoffset 90
            mcariannaprev "Mermaids from the deep? They're different from other mermaids?"
            show mscmc basic
            show arianna:
                easein 0.4 yoffset 95
            ai "There are a few different types of mermaids. We're not all from the same place."
            show arianna:
                easein 0.4 yoffset 90
            ai "For example, I'm a mermaid who lives close to the surface."
            ai grin "My last name means 'bright'. Nitida."

            hide arianna
            show mscmc bikini_hairup_cu smile_cu at mscmc_cu:
                yoffset 0
            "(A bright mermaid. That seems...very fitting.)"
            show mscmc bikini_hairup smile at left2:
                yoffset 100
            show arianna siren grin at right3:
                yoffset 90
            mcariannaprev "Nitida."
            show mscmc:
                easein 0.4 yoffset 105
            show arianna:
                easein 0.4 yoffset 85
            mcariannaprev "I like it. Arianna Nitida."
            show mscmc grin:
                easein 0.4 yoffset 100
            show arianna:
                easein 0.4 yoffset 90
            "A warm smile grows on Arianna's face and I find myself mirroring it."
            ai "And what's your full name?"
            mcariannaprev "[genericfn] [genericln]."
            ai smile "I like it."
            hide arianna
            show mscmc smile at centre

            "I draw my finger through the surface of the water, making idle shapes."

            show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
                yoffset 0
            "(There's so much out there I didn't know about.)"
            "(An entire underwater society.)"
            show mscmc bikini_hairup grin at left2:
                yoffset 100
            show arianna siren smile at right3:
                yoffset 90
            mcariannaprev "Thank you for telling me all this."
            show mscmc:
                easein 0.4 xoffset -5
            mcariannaprev "It's really amazing."
            show mscmc:
                easein 0.4 xoffset 0
            "Arianna brushes a strand of hair from her face, a rather bashful expression on her face."
            show mscmc smile
            ai "Thank you for listening."

            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu:
                yoffset 0
            "Her silver eyes shimmer as I catch her watching me."
            hide arianna
            show mscmc bikini_hairup_cu smile_cu at mscmc_cu
            "(She's given me her complete trust. I don't want to let her down.)"
            "(What I believed when I was little is real. Maybe I can start to let that pain go.)"
            show mscmc bikini_hairup smile at left2:
                yoffset 100
            show arianna siren grin at right3:
                yoffset 90
            "Arianna breaks the silence with an amused breath."
            stop music fadeout 0.5
            play music mscarianna fadein 1.0
            ai "It wouldn't be easy, but maybe someday I can try to sneak you into the city."
            show arianna:
                easein 0.4 yoffset 85
            ai "I think you'd like it."
            mcariannaprev grin "Yeah? I think I would too."
        "B. Tell her you need a minute.":
            $ menuhideborder = False
            show mscmc bikini_hairup surprised at left2:
                yoffset 100
            show arianna siren smile at right2:
                yoffset 100
            mcariannaprev "Could you give me a minute?"
            mcariannaprev "It's just...there's so much to think about."
            "Arianna offers me a gentle smile and a nod."
            hide arianna
            show mscmc sleep at centre:
                pause 0.1
                easein 0.4 yoffset 95
            "Breathing in, I close my eyes."
            show mscmc:
                easein 0.4 yoffset 100
            "The water moves around me - a slow up and down."

            show mscmc bikini_hairup_cu sleep_cu at mscmc_cu:
                yoffset 0
            "(There's a real-life mermaid right in front of me and she's asking for my help.)"
            "(Arianna said she'd help with Trina's shop.)"
            show mscmc at mscmc_cu:
                easein 0.4 yoffset 10
            "(I'll do anything so that Trina can keep that place.)"
            show mscmc at mscmc_cu:
                easein 0.4 yoffset 0
            "(On top of that, I can get to know Arianna more.)"

            scene black
            pause 0.1
            scene bg msc_ocean_wide_day at bg
            show arianna siren_cu basic_cu at arianna_cu
            with eye_open_1s
            "When I open my eyes, Arianna is watching me carefully."

    hide arianna
    show mscmc bikini_hairup basic at centre:
        yoffset 100
    "I blow out a long breath."
    mcariannaprev smile "Alright, I'm in. Let's work together."

    show mscmc at left2
    show arianna siren smile at right2:
        yoffset 50
    "Arianna's mouth twists up into a smirk and she puts her hand up as if going for a high-five."

    scene arianna_s0_mini4 at bg with fade
    ai "Put your palm to mine. That's how we seal deals."
    "I put my hand against hers."
    "Her hand is bigger than mine and rough with callouses, they must be from her sculpting."
    "A tingle travels up my arm and filly my chest."
    "That warmth blossoms inside of me."
    "(I don't know what this is, but it feels good.)"

    scene msc_tbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
