label ariannap_season1_episode1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_day at bg
    play music mscbeach

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "The beach is nothing but peaceful wanderers and the tide lapping against the shore."
    show mscmc bikini_hairup sleep at centre
    "I breathe in the salty air."
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(Nothing like surfing to get the day started!)"
    hide mscmc
    show arianna dress basic at right4:
        transform_anchor True zoom 0.3 yoffset 150
    "A little ways off, I see a woman walking beside the water."
    "The breeze makes the curled ends of her long hair and dress billow back."
    hide arianna
    show mscmc bikini_hairup embarrassed at centre
    "As she stills to look over the water, I catch my bottom lip between my teeth."
    show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu
    "(I've never seen her around.)"
    hide mscmc
    show trina casual smile at centre
    so "Hey beach bug."
    show mscmc bikini_hairup surprised at left1plus
    show trina at right2
    "Turning, I find my best friend Trina standing beside me."
    mcariannaprev smile "Hey yourself. Ready to get surfing?"
    show mscmc basic
    show trina sad
    "Trina puffs out a sign, her face falling."
    hide trina
    show mscmc bikini_hairup_cu sad_cu at mscmc_cu
    "(She must be thinking about how she's going to lose her shop...)"
    show mscmc bikini_hairup surprised at left1plus
    show trina casual sad at right2
    mcariannaprev "C'mon. Don't think about {i}that{/i}."
    mcariannaprev grin "It's just you, me, and the waves."
    show trina basic
    "Nudging Trina with my elbow, I offer a smile."
    so smile "Yeah, you're right."
    so "My board was singing for me allll night."
    hide trina
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(There we go! It's good to hear her cheer up.)"
    show mscmc bikini_hairup grin at left1plus
    show trina casual smile at right2
    so "Last one to catch a wave has to buy coffee!"
    mcariannaprev smile "Good thing you know my order."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_ocean_wide_day at bg with fade
    "As we paddle out and over the breaking waves, I glance back towards the beach."
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(I wonder where that woman went. She was...breathtaking.) "
    hide mscmc
    "A wave crashes into me, forcing me to cling to my board."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(I don't have time to think about crushes or love. I have to focus on surfing.)"
    hide mscmc
    hide surfboard
    "Another wave comes in and I push against my board, diving underneath it."
    show surfboard front at centre as trina_board:
        transform_anchor True zoom 0.65
    show trina casual smile
    so "Jeez, you look serious. Did that wave hurt your head?"
    show surfboard back behind mscmc at left2:
        transform_anchor True zoom 0.95 xoffset -40
    show surfboard front behind mscmc at right2 as trina_board:
        transform_anchor True zoom 0.65 yoffset 20 xoffset 20
    show mscmc surfer_hairup smile at left1plus
    show trina casual smile at right2
    "Trina, in her cut-offs she never takes off, knocks on the top of my head as I paddle next to her."
    mcariannaprev grin "No, it didn't. I'm just enjoying the water."
    so "You can't marry the water, [genericfn]."
    show mscmc smile
    so "You need to get out more. Meet people. Go on dates."
    hide surfboard
    hide trina_board
    hide mscmc
    hide trina

    $ menuhideborder = True
    menu ariannas0e1c1:
        "A. Think about surfing.":
            $ menuhideborder = False
            show surfboard back behind mscmc at left1plus:
                transform_anchor True zoom 0.95 xoffset -40
            show surfboard front behind mscmc at right2 as trina_board:
                transform_anchor True zoom 0.65 yoffset 20 xoffset 20
            show mscmc surfer_hairup smile at left1plus
            show trina casual smile at right2
            mcariannaprev "There's more important stuff to focus on right now."
            mcariannaprev "Like surfing."

        "B. Tell her you're fine.":
            $ menuhideborder = False
            show surfboard back behind mscmc at left1plus:
                transform_anchor True zoom 0.95 xoffset -40
            show surfboard front behind mscmc at right2 as trina_board:
                transform_anchor True zoom 0.65 yoffset 20 xoffset 20
            show mscmc surfer_hairup smile at left1plus
            show trina casual smile at right2
            mcariannaprev "This has nothing to do with getting out or not."
            mcariannaprev surprised "And I know tons of people!"

        "C. Marry the water.":
            $ menuhideborder = False
            show surfboard back behind mscmc at left1plus:
                transform_anchor True zoom 0.95 xoffset -40
            show surfboard front behind mscmc at right2 as trina_board:
                transform_anchor True zoom 0.65 yoffset 20 xoffset 20
            show mscmc surfer_hairup grin at left1plus
            show trina casual smile at right2
            mcariannaprev "The water and I are very happy together, thank you very much."

    so "Uh huh. Whatever you say."
    play sound big_splash
    show surfboard:
        pause 0.1 transform_anchor True rotate 0
        linear 0.6 xoffset -100 alpha 0.0 rotate -2
    show mscmc surprised:
        pause 0.1
        transform_anchor True anchor (0.5, 1.0) yoffset 1215 xoffset -82 rotate 0
        parallel:
            easein 0.4 yoffset 1350
            easein 0.2 yoffset 1470
        parallel:
            linear 0.3 rotate -4
        parallel:
            pause 0.2
            easeout 0.4 xoffset -350
            linear 0.2 xoffset -510
    "Trina pushes me off my board with a surprisingly strong shove."

    hide trina
    hide trina_board
    with dissolve
    $ wavy_transition("bg msc_ocean_wide_day", "bg msc_underwater_day")
    scene bg msc_underwater_day at bg
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    with dissolve
    "(Alright Trina, I see how it is!)"
    hide mscmc
    "As I swim under Trina's board, ready to tip it, I notice a bunch of sand being kicked up below."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(What is that?)"
    scene bg msc_ocean_wide_day at bg with dissolve
    show mscmc surfer_hairup basic at centre:
        transform_anchor True rotate 0 yoffset 200
        rotate 10
        easein 0.3 yoffset 50 rotate 0
        easein 0.2 yoffset 100
    "I pop my head back out of the water."
    mcariannaprev surprised "Something's moving around on the seafloor. I'm gonna check it out."
    show mscmc smile at left2
    show surfboard front behind mscmc at right2 as trina_board:
        transform_anchor True zoom 0.65 yoffset 20 xoffset 20
    show trina casual smile at right2:
        yoffset 50
    so "You and your water vision."
    show mscmc:
        easein 0.4 yoffset 95
    mcariannaprev "Feeling jealous?"
    show mscmc:
        easein 0.4 yoffset 100
    "Trina splashes water at me as I take a deep breath and dive down, slipping from my ankle strap."
    hide mscmc
    hide trina_board
    hide trina

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    $ wavy_transition("bg msc_ocean_wide_day", "bg msc_underwater_day")
    scene bg msc_underwater_day at bg with dissolve
    "Getting closer, I see a creature flailing around while caught in something."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(It's a porpoise!)"
    "(Woah. This is the first time I've ever had to deal with this.)"
    show mscmc surfer_hairup basic at centre
    "Filled with determination and passion to free it, I swim down next to it."
    show mscmc sad
    "There's a tangled up plastic bag snagged on its tail."
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Can't people keep their trash to themselves? This is awful.)"
    show mscmc surfer_hairup basic at centre
    "I start working to free it, but the thrashing creature and flying sand don't make it easy."
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(I need to go up for air soon, but it looks scared. It doesn't know why it's stuck here.)"
    show mscmc surfer_hairup surprised at centre
    "Suddenly, an extra set of hands are next to mine and I look up into a pair of eyes."

    scene arianna_s0_mini2 at bg with dissolve
    "(The woman from the beach!)"
    "It's difficult to see with all the sand and silt flying around, but it's definitely her."

    scene bg msc_underwater_day at bg
    "We tug together and the moment the plastic is loose, the porpoise speeds away."

    scene bg msc_ocean_wide_day at bg with dissolve
    show mscmc surfer_hairup surprised at centre:
        transform_anchor True rotate 0 yoffset 200
        rotate 10
        easein 0.3 yoffset 50 rotate 0
        easein 0.2 yoffset 100
    "I propel myself back to the top and suck in a deep gasp of air."
    mcariannaprev "There was a porpoise stuck and I was trying to get it out!"

    show arianna_s0_mini2 at bg as event_image
    with dissolve
    mcariannaprev "Then there was this woman and..."
    "(Her eyes were like shimmering pools of silver.)"
    "My heart pounds against my chest, the image of her burned into my mind."
    hide event_image with dissolve
    mcariannaprev "She helped me free it."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show mscmc at left2:
        easein 0.4 yoffset 95
    show surfboard front behind mscmc at right2:
        transform_anchor True zoom 0.65 yoffset 20 xoffset 20
    show trina casual sad at right2:
        yoffset 50
    so "All that lack of oxygen was messing with you. No one else has been over here."
    show mscmc:
        easein 0.4 yoffset 100
    mcariannaprev "I wasn't hallucinating a person. I swear—!"
    show mscmc basic
    show surfboard:
        pause 0.3
        easein 1.0 xoffset 560
    show trina basic:
        pause 0.2
        easein 1.0 xoffset 540
    "Trina begins to paddle off towards a wave and shouts over her shoulder."
    hide mscmc
    show trina casual smile at centre:
        xoffset 0
    show surfboard front at centre:
        xoffset 0
    so "Hold that thought!"
    hide trina
    hide surfboard
    "Trina catches the wave with a holler."
    show surfboard front at centre:
        transform_anchor True zoom 0.65 yoffset 20
    show trina casual smile at centre:
        yoffset 50
    so "Coffee's on you!"
    hide trina
    hide surfboard
    show surfboard back at centre:
        transform_anchor True zoom 0.95 xoffset -20
        easein 0.3 xoffset -40
        easein 0.3 xoffset 0
        easein_back 0.2 xoffset -20
    show mscmc surfer_hairup smile at centre:
        yoffset 100
        easein_back 0.5 yoffset 50
    "I roll my eyes but begin surveying the water as I pull myself onto my board."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    show surfboard back_cu:
        zoom 1.0 xoffset 0
    "(Where did that woman go?)"
    "(I know I wasn't making her up.)"
    show mscmc surfer_hairup basic at centre:
        yoffset 50
    show surfboard back:
        xoffset -20
    "Not too deep in the water, something shimmering swims by."
    hide mscmc
    hide surfboard
    show arianna siren_cu smile_cu at arianna_cu
    "Gorgeous Woman" "Hey."
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show arianna siren smile at centre:
        yoffset 100
    "Hanging onto the tail of my board is the woman! She has a voice like honey."
    hide arianna
    show surfboard back_cu at centre:
        xoffset 20
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(When did she get over here?! Wait...is she wearing prosthetic ears?)"
    show surfboard back:
        transform_anchor True zoom 0.8 xoffset -30
    show mscmc surfer_hairup surprised at centre:
        yoffset 50
    mcariannaprev "H-hey."
    "Once again, I'm transfixed by swirling silver eyes. Her pink lips curl into a smile."
    show surfboard back_cu:
        xoffset 0 zoom 1.0
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(She looks like she's straight out of a movie...or maybe a fairytale.)"
    show surfboard back:
        zoom 0.8 xoffset -40
    show mscmc surfer_hairup embarrassed at centre:
        yoffset 50
    "My face flushes, but I attempt to hide it with a smile of my own."
    show mscmc at left3
    show surfboard at left3:
        xoffset -20
    show arianna siren smile at right3:
        yoffset 100
    mcariannaprev "Thanks for earlier. I mean, helping me save that porpoise."
    "She lets go of my board and gives a half-bow, her one arm dipping under the water."
    "Gorgeous Woman" "Glad to be of assistance."
    hide surfboard
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu:
        yoffset 0
    "She swims around to the front of my board, tilting her head up at me."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(And now she's closer to me...)"
    show mscmc surfer_hairup smile at left2:
        yoffset 50
    show surfboard back at left2:
        zoom 0.8 xoffset -20
    show arianna siren smile at right2:
        yoffset 100
    "Gorgeous Woman" "You can see really well under water, can't you?"
    show arianna grin
    "Gorgeous Woman" "I'm impressed you even spotted it."
    show mscmc embarrassed
    "I lean back and rub at my neck to act like her compliment hasn't affected me."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 0
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(Underwater eyesight actually runs in my family.)"
    show mscmc surfer_hairup smile at left2:
        yoffset 50
    show surfboard back at left2:
        zoom 0.8 xoffset -20
    show arianna siren smile at right2:
        yoffset 100
    mcariannaprev "Yeah, it's just kinda something I've always been good at."
    show arianna sleep
    "She nods slightly, following it with a long silence as she stares at me."
    show arianna basic
    mcariannaprev grin "I should probably ask what your name is."
    ai grin "You can call me Arianna."
    mcariannaprev smile "I'm [genericfn]."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 0
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu:
        yoffset 0
    "(Arianna? Somehow that's a perfect name for her.)"
    show mscmc surfer_hairup smile at left2:
        yoffset 50
    show surfboard back at left2:
        zoom 0.8 xoffset -20
    show arianna siren smile at right2:
        yoffset 100
    mcariannaprev "Well, Arianna, do you save imperilled sea creatures every day?"
    ai grin "I just might."
    "Arianna laughs."
    ai smile "And what about you?"
    ai "You seem like you spend a good deal of time out here."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 0
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(I do, but sometimes it still doesn't feel like enough.)"
    show mscmc surfer_hairup smile at left1plus:
        yoffset 50
    show surfboard back at left1plus:
        zoom 0.8 xoffset -10
    show arianna siren basic at right2:
        yoffset 100
    mcariannaprev "Honestly, I'd live out here if I could."
    mcariannaprev grin "When I'm out here, I feel like myself."
    show arianna sad
    show mscmc basic
    "Floating beneath me, Arianna's eyebrows knit together."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 0
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(Her gaze is so intense, like burning into my soul intense.)"
    hide mscmc
    hide surfboard
    show arianna siren_cu smile_cu at arianna_cu
    "She looks me up and down."
    ai embarrassed_cu "I knew I liked you."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(Is she flirting or just being really friendly?)"
    show surfboard back at left2:
        zoom 0.8 xoffset -10
    show mscmc surfer_hairup embarrassed at left2:
        yoffset 50
    show arianna siren smile at right2:
        yoffset 100 xoffset 40
    "I slide my clammy palms together, needing a new topic."
    mcariannaprev surprised "You swim pretty far out. Are you some kind of pro swimmer or something?"
    show mscmc smile
    ai "Or something."
    show arianna grin:
        parallel:
            linear 0.4 xoffset 120
        parallel:
            easein_circ 0.4 yoffset 130
    "Pulling back from my board, Arianna grins."
    ai "What're you doing later?"

    hide arianna
    hide surfboard
    hide mscmc

    $ menuhideborder = True
    menu ariannas0e1c2:
        "A. Fumble for a reply.":
            $ menuhideborder = False
            show surfboard back at centre:
                zoom 0.8
            show mscmc surfer_hairup surprised at centre:
                yoffset 50
            mcariannaprev "Uh, nothing much..."
            show surfboard back_cu at centre:
                zoom 1.0 xoffset 10
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu:
                yoffset 0
            "(Hopefully doing something with Arianna.)"
        "B. Be nonchalant.":
            $ menuhideborder = False
            show surfboard back at left2:
                zoom 0.8 xoffset -10
            show mscmc surfer_hairup sleep at left2:
                yoffset 50
            show arianna siren grin at right2:
                yoffset 100 xoffset 40
            "I shrug."
            mcariannaprev smile "Not sure yet."
        "C. Tell her your plans.":
            $ menuhideborder = False
            show surfboard back at left2:
                zoom 0.8 xoffset -10
            show mscmc surfer_hairup smile at left2:
                yoffset 50
            show arianna siren grin at right2:
                yoffset 100 xoffset 40
            mcariannaprev "I teach a surfing class in a bit, but that's it."
            hide arianna
            show surfboard back_cu at centre:
                zoom 1.0 xoffset 10
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu:
                yoffset 0
            "(But I wouldn't mind if she asked me out.)"

    hide surfboard
    hide mscmc
    show arianna siren embarrassed at centre:
        yoffset 100
    "She twirls a strand of hair between her fingers, chewing on her bottom lip."
    show arianna siren_cu grin_cu at arianna_cu:
        transform_anchor True zoom 1.5 yoffset -160 xoffset 50
    ai "How about meeting me at sunset?"
    show arianna siren_cu smile_cu at arianna_cu:
        easein 0.3 yoffset -150
    ai "By the tidepools."
    hide arianna
    show surfboard back_cu at centre:
        xoffset 10
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(I don't know if I should read into this...)"
    show surfboard back at left3:
        zoom 0.8 xoffset -10
    show mscmc surfer_hairup surprised at left3:
        yoffset 50
    show arianna siren basic at right2:
        yoffset 100 xoffset 40
        pause 0.1
        easein 0.6 right4
    "Arianna starts slowly moving backwards, waiting for my answer."
    mcariannaprev embarrassed "Yeah, um, I'll see if that works."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 10
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu:
        yoffset 0
    "(Very smooth, [genericfn].)"
    hide mscmc
    hide surfboard
    show arianna siren embarrassed at centre:
        yoffset 100
    ai "I certainly hope so."
    show arianna smile:
        transform_anchor True anchor(0.5, 0.5) ypos 1.0 yoffset 177 xoffset 67
        pause 0.2
        linear 0.6 alpha 0.0 zoom 0.95
    "She raises a hand in a wave before swimming off."
    hide arianna
    show surfboard back_cu at centre:
        xoffset 10
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(And I certainly hope this is a date.)"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    hide mscmc
    show surfboard front at centre:
        zoom 0.6 yoffset 0
    show trina casual smile at centre:
        yoffset 50
    so "I'll take a large matcha tea, please."
    show surfboard at right7:
        pause 0.1
        easein 0.7 centre
    show trina at right7:
        pause 0.1
        easein 0.7 centre
    "Trina is paddling over now with a giant grin, a content sigh to follow."
    hide trina
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 10
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(Arianna, huh? Her voice and features were so gentle...but she seems awfully fiery.)"
    show mscmc smile_cu
    "(I wonder if she's out here often.)"
    hide mscmc
    show surfboard front at centre:
        zoom 0.6 yoffset 0
    show trina casual basic at centre:
        yoffset 50
    so "Earth to [genericfn]. You doing alright?"
    "A large wave starts coming in, Trina has her back to it."
    hide trina
    show surfboard back at centre:
        zoom 0.8 xoffset -20
    show mscmc surfer_hairup smile at centre:
        yoffset 50
    "Seeing as it's the perfect moment to beat Trina to the wave, I turn and start paddling."
    mcariannaprev "I'll tell you after!"
    "I position myself and paddle and as the wave breaks I push myself to my feet."
    show mscmc grin
    "The familiar rush of surfing consumes me. It's like I'm floating."
    show surfboard back_cu at centre:
        zoom 1.0 xoffset 10
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu:
        yoffset 0
    "(And at sunset, maybe I'll get to see Arianna again.)"
    show surfboard back at centre:
        zoom 0.8 xoffset -20
    show mscmc surfer_hairup embarrassed at centre
    "My heart pounds, but at this point I can't tell if it's from surfing or from her."

    scene bg msc_surf_shop_day at bg with dissolve
    "Typically I'm exhausted after teaching the kids surfing, but today I feel light on my feet."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I haven't had butterflies like this in a while and it's all because of Arianna.)"
    hide mscmc
    show trina casual angry at centre
    "Trina grumbles to herself as she puts surf suits back on hangers."

    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    show mscmc jacket_hairdown basic at left2
    show trina casual basic at right2
    "The sound of the doorbell makes us look up."

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    hide mscmc
    hide trina
    show hamish casual smile at centre
    rm "Good afternoon, ladies."
    hide hamish
    show trina casual angry at centre
    "Catching Trina's eye from across the shop, she makes an exaggerated eye roll."
    hide trina
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Must he ruin everything?)"
    hide mscmc
    show hamish casual smile at centre
    rm "I'm thinking booths on the right side."
    rm "That crummy counter will be replaced with something trendier."
    hide hamish
    show trina casual angry at centre
    so "Greeatt. Another {i}trendy{/i}, expensive beach bar."
    hide trina
    show mscmc jacket_hairdown angry at centre
    mcariannaprev "Nothing trendier than destroying a place with history."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(The surf shop means the world to Trina...I can't believe she's losing it to someone like Hamish.)"
    hide mscmc
    show hamish casual smile at centre
    rm "You're not planning on doing anything crazy before I own this place, right?"
    rm "You're not going to burn it all down and make off with the insurance?"
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(The guy is here constantly just so he can rub it in our faces.)"
    hide mscmc
    show trina casual angry at centre
    so "Believe it or not, not everyone is as big of a slimeball as you."
    hide trina
    show hamish casual angry at centre
    "The smirk that had formed on Hamish's face disappears."
    rm basic "I was just stopping by."
    show hamish:
        easeout 0.8 right7 xoffset 50
    "Dipping his head he makes a hasty exit."
    hide hamish
    show mscmc jacket_hairdown angry at centre
    mcariannaprev "Could he be any more stereotypical villain?"
    show mscmc jacket_hairdown angry at left2
    show trina casual angry at right2
    so "I bet he counts all of his gold before going to bed."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show mscmc grin
    show trina smile
    "As Trina and I laugh, Trina looks out the window."
    show bg msc_surf_shop_sunset with dissolve
    so "Seeing the sunset on the beach never gets old."
    hide trina
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is it sunset already?)"
    "(That means Arianna's waiting for me.)"
    show mscmc jacket_hairdown basic at left2
    show trina casual smile at right2
    so "You gonna go meet that girl you told me about?"
    so "Or are you too busy trying to be a pro-surfer?"
    hide trina
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I want to go, I want it to be a date. What if Arianna isn't thinking that?)"
    show mscmc jacket_hairdown smile at left2
    show trina casual smile at right2
    mcariannaprev "I don't know, okay? I might."
    so "Uh uh."
    so "Besides, I'm getting ready to kick you out. I need a break."
    "Standing, I wave dismissively at her."
    mcariannaprev grin "Yeah, yeah. Whatever. I get it."
    so "See that's what I'm talking about."
    hide trina
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Trina cares more about my love life than I do, but maybe that's what I need.) "
    stop music fadeout 0.5
    play music mscromance fadein 1.0
    scene bg msc_tide_pools_sunset at bg with dissolve
    "The sun is going down over the tidepools when I spot Arianna."
    "Just past the lip of the last tidepool, Arianna is swimming in the deeper water."
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(You got this. Be cool.)"
    show mscmc jacket_hairdown basic at centre
    "I take a steady breath and kick my shoes off, beginning to walk towards her."
    mcariannaprev smile "Hey."
    hide mscmc
    show arianna siren sad at centre:
        yoffset 100
    "Arianna had been fiddling with her necklace with a concerned look, but it melts away."
    ai grin "You came."
    show arianna at right3
    show mscmc jacket_hairdown grin at left2
    mcariannaprev "I wasn't gonna leave you hanging."
    ai smile "Have you ever believed in something that no one else does?"
    "I can't help but laugh a bit."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(That's an awfully loaded question to start the night.)"
    show arianna siren smile at right3:
        yoffset 100
    show mscmc jacket_hairdown grin at left2
    mcariannaprev "Working to be a professional surfer feels like that sometimes."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Something about Arianna makes me feel at ease...like I can talk about myself.)"
    show arianna siren smile at right3:
        yoffset 100
    show mscmc jacket_hairdown surprised at left2
    mcariannaprev "Why do you ask?"
    show arianna sleep
    show mscmc basic
    "Arianna shrugs."
    ai smile "You want to be a professional surfer?"
    mcariannaprev smile "I do, yeah. You didn't answer my question."
    ai basic "It's nothing."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Why is she deflecting?)"
    show arianna siren basic at right3:
        yoffset 100
    show mscmc jacket_hairdown basic at left2
    "Looking over the beach, nothing looks like it belongs to Arianna."
    mcariannaprev surprised "Where's all your stuff?"
    mcariannaprev "Are you planning on sleeping in the ocean?"
    show mscmc basic
    show arianna smile
    "Arianna hides a laugh behind her hand as she swims to the edge of the tidepools."
    ai "[genericfn], can you keep a secret?"

    hide arianna
    hide mscmc
    $ menuhideborder = True
    menu ariannas0e1c3:
        "A. Be flirty.":
            $ menuhideborder = False
            show arianna siren smile at right3:
                yoffset 100
            show mscmc jacket_hairdown smile at left2
            mcariannaprev "Guess it depends on the secret."
            "I cast her a wink."
        "B. Joke about it.":
            $ menuhideborder = False
            show arianna siren smile at right3:
                yoffset 100
            show mscmc jacket_hairdown grin at left2
            mcariannaprev "A kid told me a secret back in fifth grade and I still haven't told anyone."
        "C. Be cautious of her.":
            $ menuhideborder = False
            show arianna siren smile at right3:
                yoffset 100
            show mscmc jacket_hairdown basic at left2
            mcariannaprev "Look, I'm not interested in playing games."
            ai "I promise I'm not playing anything."

    hide mscmc
    show arianna basic at centre
    "Arianna stills for a moment, like she's mulling something over."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's gotten pretty serious...)"
    show mscmc jacket_hairdown basic at centre
    "Looking over my shoulder, I see if anyone else is around. The beach is dead."
    show arianna siren basic at right2:
        yoffset 100
    show mscmc jacket_hairdown surprised at left2
    mcariannaprev "Um, what's going on here?"
    ai smile "I'll show you."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Show me what?)"
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    "A devilish grin spreads on Arianna's face as she grabs onto the edge."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(A severed head on a chain under the water?)"
    show mscmc jacket_hairdown basic at centre
    "I take a step back."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Maybe it's just a nice shell she found?)"
    show mscmc surprised_cu
    "(Or maybe she's some kind of criminal!)"
    hide mscmc
    "In a very methodical way, Arianna pulls herself onto the edge of the tidepool."

    scene arianna_00_e1 with fade:
        zoom 1.3 align(0.0, 0.0) xoffset -200
        pause 0.5
        linear 5.0 align(1.0, 1.0) xoffset 0
    pause 5.0
    "Her tight abdomen travels down into a long, muscular tail."
    "Water glistens over the scales."
    "It ends in a huge fan that's reminiscent of a flower petal."
    window hide
    show arianna_00_e1:
        transform_anchor True
        linear 5.0 zoom 0.65
    pause 5.0
    "With the glow of the setting sun behind her, I feel like I'm in the presence of a divine being."
    "Arianna flips her hair over her shoulders, her eyes shining."
    "{i}(Is this real?!){/i}"

    scene msc_tbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
