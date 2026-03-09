label arianna_season2_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_night at bg
    play music mscsuspense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    play sound ["<to 1.5>audio/sfx/honk_alarm_repeat_loop_101015.mp3",running]
    "Arianna quiets her phone's security alarm as we quickly run to the beach."
    show arianna dress_cu basic_cu at arianna_cu
    ai "We need to hurry. There could be nothing left by the time we get there."
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Oh shit.)"

    scene bg msc_ocean_wide_night at bg
    with dissolve
    show mscmc bikini_hairdown sad at left1plus:
        xoffset -100 alpha 0.0
        pause 0.1
        linear 0.5 xoffset 0 alpha 1.0
    show arianna siren basic at right3:
        xoffset -150 alpha 0.0 yoffset 300
        parallel:
            easein_back 0.5 yoffset 150
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset 0
    play sound "<to 4.0>audio/sfx/MSC_Sound_Effects/splash02.mp3"
    "Arianna dives into the water and I follow behind, paddling on my surfboard since I can't swim as fast as her."
    show arianna sad
    "We're silent as we make our way out into the dark waters and Arianna swims just under the surface next to my board."
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(What are we going to find at her studio? A merperson SWAT team?)"
    hide mscmc

    $ wavy_transition("bg msc_ocean_wide_night", "bg msc_underwater_ship_night")
    scene bg msc_underwater_ship_night at bg with dissolve
    "When we get there I ditch my board and dive down. As we approach the outside of the shipwreck, Arianna glances at me."
    show mscmc bikini_hairdown surprised at left2
    show arianna siren basic at right3
    ai "Stay back, okay? I don't know who's in there."
    mcarianna basic "Okay..."
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(But I will protect her too if it comes to that.)"
    show mscmc bikini_hairdown surprised at left2
    show arianna siren basic at right3:
        transform_anchor True
        linear 0.5 zoom 1.05 alpha 0.0
    "Arianna swims in ahead of me and then stops dead in her tracks."
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu:
        zoom 1.0 alpha 1.0
    ai "What are {i}you{/i} doing here?"
    show arianna siren angry at right1
    show mscmc bikini_hairdown surprised at left1plus behind arianna:
        xoffset -80 yoffset 150 alpha 0.0
        pause 0.1
        parallel:
            easein 0.4 xoffset 0
        parallel:
            easein_back 0.4 yoffset 0
        parallel:
            linear 0.4 alpha 1.0
    "I come up and peer around her to see Casper in the middle of her studio."
    hide mscmc
    hide arianna

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    show casper casual_cu confused_cu at casper_cu
    cs "Sorry!"
    hide casper
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Why {i}is{/i} he here late at night?)"
    show mscmc bikini_hairdown basic at right5
    show arianna siren angry at right2
    show casper casual confused at left3
    cs "I was just trying to find you, Arianna, but then the alarms started going off."
    cs angry "I tried to make it stop, but I couldn't figure it out..."
    show casper sleep
    "He hangs his head as though overcome with defeat."
    cs smile "But, I also figured that the alarms would at least get you here."
    show mscmc smile
    "I let out a breath of relief, the studio hasn't been compromised."

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(It's only Casper. I was scared it'd be bad.)"
    show arianna siren basic at right2
    show mscmc bikini_hairdown smile at right5 behind arianna
    show casper casual basic at left3
    "Arianna makes a low grumble as she punches some numbers into a panel on the wall."
    ai "You didn't have to break in..."
    show mscmc basic
    cs "I'm sorry. I didn't know about the alarm."
    show casper smile
    show mscmc smile
    "Casper raises his head and gives me a little wave."
    show mscmc basic
    cs "I didn't mean for it to look like this."
    hide mscmc
    hide arianna
    hide casper

    $ menuhideborder = True
    menu ariannas2e6c1:
        "A. You could've called.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
            "(I guess his intentions weren't bad.)"
            show casper casual basic at left2
            show mscmc bikini_hairdown basic at right3
            mcarianna "You could've called, you know."
            show mscmc smile
            cs smile "I...yeah. Next time."
            hide mscmc
        "B. Well, we're here now.":
            $ menuhideborder = False
            show casper casual basic at left2
            show mscmc bikini_hairdown smile at right3
            mcarianna "Well, at least it wasn't a crisis like Arianna and I thought."
            show casper smile
            mcarianna "We're here now."
            show casper basic
            hide mscmc
            show arianna siren basic at right3
            ai "We {i}are{/i} here now."
            hide arianna
        "C. Did you need something, Casper?":
            $ menuhideborder = False
            show casper casual basic at left2
            show mscmc bikini_hairdown basic at right3
            mcarianna "Why did you come here?"
            cs confused "I just wanted to talk to you guys."
            hide mscmc

    show casper casual_cu basic_cu at casper_cu
    cs "Really, Arianna, I am so-"
    hide casper

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna siren_cu basic_cu at arianna_cu
    ai "Casper. It's okay."
    show arianna sleep_cu
    "Arianna runs a hand over her face then holds her necklace."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(Is Arianna {i}okay{/i}, though? She looks worn out.)"
    hide mscmc
    show casper casual basic at left2
    show arianna siren basic at right3
    ai "I'm trying to believe you, Casper, but I still don't know you that well."
    ai "What if you're taking information about the resistance back to the government?"
    show arianna sleep
    cs angry "I would never do that. I'm on your side now!"
    hide casper
    hide arianna
    play sound electricbuzz
    show queenie casual basic at centre:
        xoffset 100 yoffset 50 alpha 0.0
        pause 0.1
        parallel:
            easein 0.4 xoffset 0
        parallel:
            easein_back 0.4 yoffset 0
        parallel:
            linear 0.4 alpha 1.0
    qn "What's going on here? Arianna?"
    show queenie angry
    "Queenie's head has popped through the side of the ship and she stares at us disapprovingly."
    qn "I got the security systen alert..."
    hide queenie
    show mscmc bikini_hairdown basic at right5
    show arianna siren basic at right2
    show casper casual basic at left3
    ai "Everything's fine."
    hide mscmc
    hide arianna
    hide casper
    show queenie casual basic at centre
    "Queenie pauses as she looks around."
    hide queenie
    show casper casual basic at centre
    cs "I didn't mean to set off the alarm."
    show casper confused at left2
    show queenie casual basic at right2
    "Queenie holds up a hand as she comes closer to the three of us."
    show casper basic
    qn "Casper, calm down. It's alright. We believe you."
    show casper smile
    "Casper's face lights up at her words of acceptance."
    cs "Yeah, cause I didn't mean to."
    qn "Really, dear. Don't worry."
    hide casper
    hide queenie
    show mscmc bikini_hairdown smile at right1plus
    show arianna siren basic at left1
    "Arianna meets my eyes and I give her a small smile, hoping to see her return it."
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Casper coming here at night on his own wasn't the best plan, but I think he needs this.)"
    show mscmc basic_cu
    "(If he were going to turn the resistance over to the government, he probably already would have.)"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show casper casual basic at left1plus
    show mscmc bikini_hairdown surprised at right4
    cs "Thank you...especially you, [genericfn]."
    cs confused "After our talk at the tidepools, I tried to find any proof of existence I could for my uncle."
    show mscmc sad
    cs angry "But I couldn't find anything."
    "His face falls."
    show mscmc basic
    cs "It's like he's disappeared from my family records."
    hide casper
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(I hope the resistance can help him.)"
    show casper casual angry at left1plus
    show mscmc bikini_hairdown basic at right4
    cs "How could they do that? Like he was nothing..."
    hide mscmc
    show queenie casual basic at right2 behind casper
    qn "Casper, come here."
    "Queenie, with a gentle smile, opens her arms as he moves towards her uncertainly."
    show casper:
        easein_back 0.4 xoffset 100
    "Then Casper goes limp as Queenie hugs him, he is still for a moment then rests his head on her shoulder and hugs her back."
    hide casper
    hide queenie

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Queenie is an incredible leader.)"
    hide mscmc
    show arianna siren_cu surprised_cu at arianna_cu
    "Arianna's eyes widen momentarily at the sight of Queenie and Casper hugging it out."
    ai basic_cu "Casper..."
    show arianna smile_cu
    "Then Arianna smiles softly."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I think Arianna is going to be a great leader too.)"
    hide mscmc
    show casper casual confused at left2
    show arianna siren basic at right2
    ai "Do you want to help make the sculpture's scales for the protest piece?"
    show casper smile
    "Casper lets out a little gasp and his lips quirk up in a smile."
    cs "Yes, I do want to do that."
    hide casper
    hide arianna

    $ wavy_transition("bg msc_underwater_ship_night", "bg msc_labeach_night")
    scene bg msc_labeach_night at bg with dissolve
    "Once our meeting with Casper is done, Arianna and I go back to the surface."
    show mscmc bikini_hairdown smile at left1
    show arianna bikini basic at right1
    "Arianna sits on the sand when we get back and looks out at the ocean as I sit beside her."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(She looks tired. I don't blame her. A lot happened today.)"
    show mscmc bikini_hairdown embarrassed at left1:
        transform_anchor True rotate 0
        rotate 2 xoffset 50 yoffset 40
    show arianna bikini sad at right1 behind mscmc:
        transform_anchor True rotate 0
        rotate -2 xoffset -50 yoffset 20
    "Arianna leans her head on my shoulder and I rest my cheek against her soft, silver-blue hair."
    show arianna basic
    mcarianna basic "How are you doing?"
    ai sad "Not great, actually. I don't know."

    play sound "<to 3>audio/sfx/MSC_Sound_Effects/splash02.mp3" fadeout 0.5
    "The soothing sound of the waves surrounds us as we sit against each other."
    ai "When the alarm went off, I thought it was the government."
    show mscmc sad
    ai sleep "Everything would've been over. The resistance. My art. My family would be torn apart."
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu:
        rotate 0 xoffset 0 yoffset 0
    "(I can't imagine what living with the possibility of losing everything all the time must feel like.)"
    show mscmc bikini_hairdown sad at left1:
        transform_anchor True rotate 0
        rotate 2 xoffset 50 yoffset 40
    show arianna bikini basic at right1 behind mscmc:
        transform_anchor True rotate 0
        rotate -2 xoffset -50 yoffset 20
    "Arianna finds my hand and brings it into her lap."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show mscmc surprised
    ai sad "Grandma and I would be charged and...I'd never see you again, that's the part that scared me most."
    show mscmc embarrassed
    "She plays with my fingers, her touch delicate as she looks away from me."
    hide mscmc
    show arianna bikini_cu embarrassed_cu at arianna_cu:
        rotate 0 xoffset 0 yoffset 0
    ai "I don't want to think about a future without you in it."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "The softness of her voice makes my heart ache."
    "(I don't want that kind of future either.)"
    show mscmc bikini_hairdown embarrassed at left1:
        transform_anchor True rotate 0
        rotate 2 xoffset 50 yoffset 40
    show arianna bikini embarrassed at right1:
        transform_anchor True rotate 0
        rotate -2 xoffset -50 yoffset 20
    "I slip my arm around her wasit, pulling her close to my side."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        rotate 0 xoffset 0 yoffset 0
    "She burrows her head gently into the space where my neck meets my shoulder and I blush as we tangle our arms around each other."
    "Being pressed together in nothing but our bikinis makes my breath come quicker, and I consciously try to breathe normally."
    show mscmc bikini_hairdown embarrassed at left1:
        transform_anchor True rotate 0
        rotate 2 xoffset 50 yoffset 40
    show arianna bikini embarrassed at right1:
        transform_anchor True rotate 0
        rotate -2 xoffset -50 yoffset 20
    "Arianna strokes a finger down the back of my hand as we rest against one another."
    hide mscmc
    hide arianna

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    "There's suddenly a small movement in the sand to the left of us and we both perk up to see what the small commotion is."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Is that?)"
    hide mscmc
    show vfx_msc_acc_baby_sea_turtle as baby_turtle:
        zoom 0.4 xalign 0.5 yanchor 0.5 ypos 0.8
    "A tiny fin pops out from the sand."
    hide baby_turtle
    show mscmc bikini_hairdown grin at left1:
        transform_anchor True rotate 0
        rotate 2 xoffset 50 yoffset 40
    show arianna bikini surprised at right1:
        transform_anchor True rotate 0
        rotate -2 xoffset -50 yoffset 20
    "I tap Arianna's side."
    mcarianna "Hey, look."
    hide mscmc
    hide arianna
    show vfx_msc_acc_baby_sea_turtle as baby_turtle:
        zoom 0.9 xanchor 0.5 xpos 0.55 yanchor 0.5 ypos 0.85
    "Out from the sand, a precious little baby turtle fully emerges, sand spilling off its face."
    hide baby_turtle
    show mscmc bikini_hairdown smile at left1:
        transform_anchor True rotate 0
        rotate 2 xoffset 50 yoffset 40
    show arianna bikini surprised at right1:
        transform_anchor True rotate 0
        rotate -2 xoffset -50 yoffset 20
    "Arianna sucks in a breath."
    show mscmc grin
    ai grin "It's soooooooo cute! Hi, baby turtle!"
    mcarianna surprised "There're more hatching! Oh wow."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        rotate 0 xoffset 0 yoffset 0
    "(Baby turtles hatching under the moonlight, with Arianna next to me, this feels really special and unique.)"
    hide mscmc
    show arianna bikini_cu grin_cu at arianna_cu
    "Arianna watches with awe and delight and I can't help but glance up from the sand to watch the way her eyes are sparkling."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(I want to make her happy, forever if possible. I love seeing that smile.)"
    show mscmc bikini_hairdown embarrassed at left1:
        xoffset 30
    show arianna bikini grin at right1:
        xoffset -20
    mcarianna "Off on their new journey. Bigger and bluer."
    hide mscmc
    hide arianna
    show vfx_msc_acc_baby_sea_turtle as baby_turtle:
        zoom 0.4 xalign 0.5 yanchor 0.5 ypos 0.75
    "The first baby turtle starts slowly pulling itself towards the adventure of the sea."
    hide baby_turtle
    show mscmc bikini_hairdown smile at left1:
        xoffset 30
    show arianna bikini surprised at right1:
        xoffset -20
    ai "I guess..."
    ai embarrassed "We're kind of like that right now, aren't we? A new journey, together."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        xoffset 0
    "(Can we make that journey last a lifetime? Oh wow, I like her way too much.)"
    hide mscmc
    "Another tiny turtle head surfaces near where the first one busted out, then another, as the first makes its intrepid way to the surf."
    show mscmc bikini_hairdown grin at left1:
        xoffset 30
    show arianna bikini embarrassed at right1:
        xoffset -20
    mcarianna "Wouldn't want to be starting a crazy new adventure with anyone else."
    mcarianna embarrassed "I want to do it with you."
    "Arianna takes both of my hands and holds them close to her chest as she looks into my eyes."
    ai grin "I know it's getting late, but turtles hatching doesn't happen every night! This means a lot to me, can we stay?"
    hide mscmc
    show arianna bikini_cu embarrassed_cu at arianna_cu:
        xoffset 0
    ai "Can we keep cuddling and watch the babies hatch?"
    hide arianna

    $ menuhideborder = True
    menu ariannas2e6c2:
        "A. See baby turtles and trade flirty touches!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(I want to stay out here with her indifinitely, I want this night to stretch out to infinity!)"
            "(Yeah, sleep can wait.)"
            show mscmc bikini_hairdown grin at left1:
                xoffset 30
            show arianna bikini grin at right1:
                xoffset -20
            mcarianna "Well, yeah, we can't leave now! We're their watchers so they all make it to the water."
            "Arianna slips her fingers through mine then puts her other hand to her chest and gasps dramatically."
            show mscmc embarrassed
            ai "Our beautiful adorable baby turtle children for this one night."
            hide mscmc
            hide arianna
            "More little, green scaly turtles start kicking up sand and unburying themselves."
            show mscmc bikini_hairdown grin at left1:
                xoffset 30
            show arianna bikini grin at right1:
                xoffset -20
            ai "Ah, look! More babies!"
            show mscmc embarrassed
            "Arianna squeezes my hand as we get down close to the sand together."

            stop music fadeout 0.5
            play music mscromance fadein 1.0
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(There must be something in the air tonight because I feel drunk off her touch. It makes me forget everything but her.)"
            show mscmc bikini_hairdown embarrassed at left1:
                xoffset 30
            show arianna bikini embarrassed at right1:
                xoffset -20
            "My hand fits perfectly in Arianna's and we smile to each other when she catches me looking at our fingers."
            show mscmc grin
            ai "They are so cute! Oh, and you are so cute, let me not forget to mention."
            show arianna grin
            mcarianna embarrassed "They're so small. It's crazy to think how big they can get."
            show arianna surprised
            mcarianna "A humongous sea turtle would be a pretty cool sculpture."
            show arianna grin
            "I raise my eyebrows at Arianna and she grins."
            ai "It would be though, wouldn't it?"
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu:
                xoffset 0
            "(I'll admit I'm biased cause I'm head over heels, but I think any sculpture by her would turn out amazing.)"
            show mscmc bikini_hairdown embarrassed at left1:
                xoffset 30
            show arianna bikini grin at right1:
                xoffset -20
            "Arianna squeals as a little group of baby turtles shuffle right in front of where we're kneeling in the sand."
            show mscmc grin
            ai sad "Awwww, look at that face, and those big eyes!"
            show arianna grin
            mcarianna "I remember you saying turtles are significant in mer culture."
            hide mscmc
            show arianna bikini_cu grin_cu at arianna_cu:
                xoffset 0
            "The smile that lights up Arianna's face has my heart beating a mile a minute while she stares at me, impressed."
            "Arianna tilts her head and a strand of hair falls across her cheek as she continues to study my face. We're leaning in towards each other..."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(God, she's pretty.)"
            hide mscmc

            play sound seagulls_short_6004 fadeout 0.5
            "A seagull squawks above us and we both jump."
            show mscmc bikini_hairdown surprised at left1:
                xoffset 30
            show arianna bikini angry at right1:
                xoffset -20
            stop sound
            "Arianna looks up frowning."
            show mscmc smile
            ai grin "We have to run off the birds to protect our turtle little ones."
            mcarianna grin "I don't think they'll come close as long as we're here."
            hide mscmc
            hide arianna
            "Arianna seems reassured and scoots closer to me on the sand, leaning forward so our faces are close together."
            show mscmc bikini_hairdown embarrassed at left1:
                xoffset 30
            show arianna bikini embarrassed at right1:
                xoffset -20
            ai "Nothing's going to get our turtles before they get a chance to feel the ocean."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Aw, {i}our{/i} turtles.)"
            show mscmc bikini_hairdown grin at left1:
                xoffset 30
            show arianna bikini grin at right1:
                xoffset -20
            mcarianna "The baby turtles are safe with us!"
            hide mscmc
            show arianna bikini_cu embarrassed_cu at arianna_cu:
                xoffset 0
            "Arianna meets my eyes and smirks as she pushes a loc behind my ear and lets her finger trail down the side of my jaw."
            ai "You're cute when you're amped up."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "As her hand leaves my face, she reaches out and places her other hand on my thigh with a questioning smile."
            "(I never want her to stop touching me.)"
            mcarianna grin_cu "I'm always cute."
            hide mscmc
            show arianna bikini_cu embarrassed_cu at arianna_cu
            "Arianna laughs and looks to the water as a group of baby turtles reach it and start swimming off."
            ai "I {i}guess{/i} you're as cute as the turtles."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "I'll take it. The turtles are pretty cute."
            hide mscmc
            "More baby turtles start to disappear into the lapping water."
            show arianna bikini_cu sad_cu at arianna_cu
            ai "I love babies. So much."
            ai "They're just so cute."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Arianna is so bright and warm and highly effected by cuteness, be still my heart.)"
            "(Her smile. Her heart. The way she's so excited about these turtles.)"
            hide mscmc
            show arianna bikini_cu embarrassed_cu at arianna_cu
            "Arianna smiles, a blush on her cheeks."
            hide arianna
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(Wait, what was she just thinking about?)"
            show mscmc embarrassed_cu
            "I feel my own cheeks turn hot as she spears me with her eyes."
            hide mscmc
            "We hold hands and watch as the rest of the turtles make their way into the lapping of soft waves."
            show mscmc bikini_hairdown smile at left1:
                xoffset 30
            show arianna bikini grin at right1:
                xoffset -20
            "As the last one disappears off the shore, Arianna waves."
            ai "Bye, little guys. Maybe we'll meet again one day."
            show arianna basic
            mcarianna sad "There is one problem though."
            show arianna sad
            "Arianna frowns, her hand squeezing mine as we stroll to the waters edge and stif at the waterline."
            ai surprised "What is it?"
            show arianna grin
            mcarianna grin "How are we gonna remember all their names? There were so many."

            window hide
            scene arianna_06_s2e6:
                align(0.5, 0.0) transform_anchor True zoom 1.3 yoffset -60
            with fade
            pause 0.3
            show arianna_06_s2e6:
                linear 5.0 zoom 0.65 yoffset 0
            pause 5.0
            "Arianna snorts and bumps her shoulder into mine."
            ai "Well, that's easy. We'll get them color-coded hats."
            ai "We name them after the color of their hat."
            "Arianna taps her finger to the side of her head."
            mcarianna "Where would I be without you? You're so smart."
            ai "I know. It's not easy being brilliant {i}and{/i} beautiful."
            "(She's right-she is brilliant and beautiful, and a great baby turtle co-parent for the evening.)"

            scene bg msc_labeach_night at bg
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcarianna "You must be exhausted from being so attractive and smart all the time!"
            show mscmc bikini_hairdown embarrassed at left1:
                xoffset 30
            show arianna bikini embarrassed at right1:
                transform_anchor True rotate 0
                rotate -2 xoffset -56 yoffset 56
            "Arianna puts her head on my shoulder, snuggling in close."
            ai "Can we stay here til the sun comes up?"
            mcarianna "We'll stay as long as you want."
            ai "Forever?"
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(I like the sound of that.)"

            scene bg msc_labeach_sunset at bg
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            with fade
            mcarianna "Forever it is, Arianna."

        "B. Call a conservation group.":
            $ menuhideborder = False
            show mscmc bikini_hairdown basic at left1:
                xoffset 20
            show arianna bikini basic at right1:
                xoffset -20
            mcarianna "I'll find a number for a local marine life conservation group to make sure they all get to the water."
            mcarianna smile "They'll handle it."
            show arianna sad
            "Arianna pouts a little as we walk up the beach."
            ai basic "Let's at least stay until they get here."
            show arianna smile
            mcarianna "Ok! And then I think we both could use some sleep."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_arianna_studio_day at bg with fade
    "The next day, Arianna and I wait in her studio for Casper to show for scale making."
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Today is his official first day of working on a resistance project.)"
    show mscmc bikini_hairdown basic at left1plus
    show arianna siren basic at right2 behind mscmc
    "Arianna drums her fingers on one of the tables as she looks over supplies that's been laid out."
    mcarianna smile "It'll be okay."
    ai smile "I know...I'm just a little tense."
    show arianna embarrassed
    show mscmc:
        easein 0.4 left1 xoffset 40
    "I take her hand, stopping her drumming and give her fingers a quick kiss."
    hide arianna
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e6c3:
        "A. Trust me.":
            $ menuhideborder = False
            show arianna siren basic at right1
            show mscmc bikini_hairdown grin at left1plus
            mcarianna "It'll be fine. Trust me."
            hide arianna
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(I will work my hardest to keep the peace today, but I'm hopeful it'll be smooth sailing.)"
            show arianna siren smile at right1 behind mscmc
            show mscmc bikini_hairdown smile at left1plus
            ai "I do trust you."
            show arianna grin
            "She squeezes my hand with a smile."
            mcarianna "Good."
        "B. We'll figure it out.":
            $ menuhideborder = False
            show arianna siren basic at right1
            show mscmc bikini_hairdown smile at left1plus
            mcarianna "Look, whatever happens, we'll figure it out."
            mcarianna grin "He's willing to work with us and for us."
            ai smile "I'm glad you're here with me."
            mcarianna "Me too."
        "C. I'll keep an eye on him.":
            $ menuhideborder = False
            show arianna siren basic at right1
            show mscmc bikini_hairdown grin at left1plus
            mcarianna "I'll keep an eye on him, okay?"
            show arianna surprised
            mcarianna angry "He tries anything funny and he's outta here."
            show mscmc embarrassed
            show arianna grin
            "Arianna giggles at my macho display."
            ai "Are you my personal bodyguard now?"
            show arianna embarrassed
            mcarianna grin "Always have been."

    hide arianna
    hide mscmc
    show casper casual basic at centre
    cs "Uh, hello?"
    "Casper appears in the entrance, his hands awkwardly folded in front of his chest."
    hide casper
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(He looks just as nervous as Arianna.)"
    show casper casual basic at left3
    show arianna siren smile at right4 behind mscmc
    show mscmc bikini_hairdown grin at right1plus
    mcarianna "Hey, Casper. Come on in."
    "Casper nods at me and swims in."
    cs smile "So, what's first on the agenda?"
    show mscmc smile
    ai grin "We need to finish these scales for the piece."
    ai "I'll show you how to make them, okay?"
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Okay, so far so good. Things are looking up!)"
    hide mscmc
    show casper casual basic at left1plus
    show arianna siren smile at right3
    "Arianna leads him over to the table and we all sit around it."
    ai "It's pretty easy. Don't stress about it too much."
    show casper smile
    "Casper watches her with eager eyes as she works the stamp machine."
    ai "This is the stamping press. Take the metal here and slide it in."
    ai "Then, pull the stamp down."
    "Casper takes the metal and does what Arianna says as she watches from a little ways away."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(They both seem comfortable enough. I'm relieved.)"
    hide mscmc
    show casper casual smile at left1plus
    show arianna siren smile at right3
    cs "So, how does this help the resistance?"
    ai grin "Well, it's going to be a giant art piece—a sea serpent."
    show casper basic
    ai "The scales will be detachable and imbued with magic."
    show arianna smile
    "Arianna picks up the stamped metal and hands it to Casper."
    show casper smile
    ai grin "People can take the scales and this will redistribute magic to the general population."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(It's pretty badass for an art installation, that's for sure.)"
    hide mscmc
    show casper casual basic at left1plus
    show arianna siren smile at right3
    "Casper tenderly holds the metal in his hands like he's scared of messing it up somehow."
    cs confused "What kind of magic will the scales have?"
    show casper basic
    ai grin "They will interfere with government surveillance magic."
    show casper smile
    ai "It'll cut them out."
    show casper basic
    "Casper purses his lips and then grins widely."
    cs smile "I love what you're doing here."
    ai surprised "Oh, thank you."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Look at them bonding! I knew this was going to go well.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    show casper casual smile at left1plus
    show arianna siren grin at right3
    cs "Would I be able to make a suggestion?"
    ai "Of course."
    "Casper sets the metal down and spreads his hands on the table."
    show arianna basic
    cs "What if we did {i}more{/i}?"
    hide arianna
    show mscmc bikini_hairdown smile at right3
    mcarianna "Like...?"

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show mscmc surprised
    cs confused "Shouldn't we hit back at the government as hard as they hit us?"
    cs angry "Imbue the scales with distructive magic. That would make a difference."
    show mscmc basic
    cs "We need to give people the means to fight back."
    hide casper
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Is he talking about handing out bombs to people?)"
    hide mscmc
    show casper casual basic at left1plus
    show arianna siren angry at right3
    ai "I like the enthusiasm, but this isn't the piece or the time for that kind of move on the resistance's part."
    show arianna smile
    "Arianna offers him an understanding smile but I see the alarm she's trying to hide in her eyes."
    ai "There will be direct disruption, but that will happen in different phases and serious planning and forethought goes into each escalation."
    show casper confused
    ai basic "If we do something too destructive, the resistance will be labeled outright as terrorists and hunted down."
    ai "And the government would try to destroy us instead of semi-tolerating us so long a swe appear to be laying low."
    show casper angry
    "Casper sighs as he picks his stamped metal up and frowns."
    cs "Fine..."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Handing out destructive devices like free candy to the public sounds like a bad idea at any point during a conflict.)"
    hide mscmc
    show casper casual confused at left1plus
    show arianna siren angry at right3
    cs "I just don't understand the point of doing this anonymously. Why hide ourselves?"
    ai "This fight we fight is not about notoriety."
    cs smile "Why not? Isn't it cowardly to not take credit for it?"
    show casper basic
    "Arianna's hands tighten around the scale she was working on and she looks sharply at Casper, causing his smile to falter."
    hide casper
    hide arianna
    show mscmc bikini_hairdown_cu angry_cu at mscmc_cu
    "(Does he even know what it means to be cowardly.)"
    hide mscmc

    play sound knocking
    stop music fadeout 0.5
    play music msctense fadein 1.0
    "A knock on the outside of the ship prevents any further arguing."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(That's not Queenie, is it? She never knocks.)"
    "(Who else could it be? The mer government?!)"
    show arianna siren angry at right1plus behind mscmc
    show mscmc bikini_hairdown basic at left1:
        xoffset 20
    "Arianna puts a hand on my shoulder."
    ai "You need to hide!"
    mcarianna surprised "Oh, god. Okay."
    hide arianna
    hide mscmc
    show casper casual smile at centre
    cs "I'll help. You know, since I saw you last time you tried to hide in here."
    show casper at left1plus
    show mscmc bikini_hairdown smile at right3
    mcarianna "Yeah...don't need to remind me."
    hide casper
    hide mscmc
    "Casper helps me behind one of the statues and he pulls another one closer for more cover."
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(I'll keep my mouth shut this time.)"
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    ai "Come in."
    hide arianna
    show maxime mermaid basic at centre:
        xoffset -100 alpha 0.0
        pause 0.1
        linear 0.5 xoffset 0 alpha 1.0
    "It's hard to keep my mouth shut when I see Maxime swim through the hull of the shipwreck, though."
    hide maxime
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(What's he doing here?)"
    show mscmc sad_cu
    "(What, shit. He's {i}in{/i} the mer government! He's an agent or something.)"
    hide mscmc
    show maxime mermaid basic at left2
    show arianna siren surprised at right3
    ai "Oh, Maxime. What's up?"
    show maxime sad
    show arianna basic
    "Maxime sighs and then straightens his shoulders."
    show arianna sleep
    mx "Arianna...I'm here as an agent of the government."
    hide maxime
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(No, no, no. Maxime, what're you doing?!)"
    hide mscmc
    show maxime mermaid basic at left2
    show arianna siren surprised at right3
    mx "There's a rumor that you, Arianna Nitida, built this place as an art studio."
    show arianna angry
    mx "And the resistance works out of here."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
