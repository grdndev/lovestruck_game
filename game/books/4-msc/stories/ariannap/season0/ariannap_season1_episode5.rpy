label ariannap_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_ocean_wide_day at bg
    play music mscmctheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Arianna swims pretty far out as I follow on my surfboard."
    show surfboard back_cu at centre
    show mscmc bikini_hairup_cu smile_cu at mscmc_cu
    "(I'm thankful that I keep in shape.)"
    "(I don't even think I'd be able to keep up with her otherwise.)"
    hide surfboard
    hide mscmc
    play sound "audio/sfx/MSC_Sound_Effects/big_splash.mp3"
    show arianna siren grin at centre:
        transform_anchor True rotate 0 yoffset 480 xoffset 70
        rotate 8
        pause 0.1
        parallel:
            easein 0.5 xoffset 0
        parallel:
            linear 0.4 rotate 0
        parallel:
            easein 0.5 yoffset 40
            easein 0.2 yoffset 90
    "She keeps dipping under and out like a dolphin to entertain me."
    show arianna smile
    "Arianna does a tight lap around me before stopping."
    ai grin "We're here!"
    hide arianna
    show surfboard back at centre
    show mscmc bikini_hairup surprised at centre:
        yoffset 50
    mcariannaprev "Uh, I don't see anything."
    show surfboard back_cu
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(Is this her favorite part of the water or something?)"
    hide surfboard
    hide mscmc
    show arianna siren grin at centre:
        yoffset 90
    "Arianna laughs, shaking her head."
    show arianna siren_cu grin_cu at arianna_cu:
        transform_anchor True zoom 1.4 yoffset -145 xoffset 50
        pause 0.1
        easein 0.4 yoffset -140
    ai "Not up here, silly! It's {i}under{/i} the water."
    show arianna siren grin at centre:
        zoom 1.0 yoffset 100 xoffset 0
        pause 0.1
        easein 0.4 yoffset 95
    ai "This is where my art studio is."
    hide arianna
    show surfboard back_cu at centre
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(No way! She's taking me to a cool underwater mermaid art studio!)"
    show surfboard back at left3:
        xoffset -50
    show mscmc bikini_hairup surprised at left3:
        yoffset 50
    show arianna siren smile at right4:
        yoffset 95
    "I lean over the side of my board and put my face into the water, but she taps me on the head."
    ai "Hold your seahorses."
    show surfboard:
        easein 0.4 yoffset 5
    show mscmc basic:
        easein 0.4 yoffset 55
    show arianna basic:
        easein 0.4 yoffset 100
    ai "I can't just take an air breathing human inside an underwater structure."
    show surfboard:
        easein 0.4 yoffset 0
    show mscmc:
        easein 0.4 yoffset 50
    show arianna sad:
        easein 0.4 yoffset 95
    ai "If something goes wrong, I cannot have a dead human on my hands."
    show mscmc smile
    "I roll my eyes."
    ai basic "My studio is inside an old shipwreck. I wanted to show it to you as thanks..."
    hide surfboard
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu:
        yoffset 0
    "A sheepish look crosses her face as she brushes a piece of hair behind her ear."
    show surfboard back at left3:
        xoffset -50
    show mscmc bikini_hairup smile at left3:
        yoffset 50
    show arianna siren embarrassed at right4:
        yoffset 95
    ai "For what you said about me being a real artist and the things you give your life to."
    hide arianna
    show surfboard back_cu at centre:
        xoffset 0
    show mscmc bikini_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(I'm glad that I could make Arianna feel better, but I feel more thankful to her.)"
    show mscmc grin_cu
    "(She's shown me so much.)"
    show surfboard back at left3:
        xoffset -50
    show mscmc bikini_hairup grin at left3:
        yoffset 50
    show arianna siren smile at right4:
        yoffset 95
    mcariannaprev "You don't have to thank me for that, but this is going to be super awesome."
    hide surfboard
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu:
        yoffset 0
    "She grins at me, nodding."
    ai "Stick close, okay?"
    hide arianna

    play sound "audio/sfx/MSC_Sound_Effects/big_splash.mp3"
    $ wavy_transition("bg msc_ocean_wide_day", "bg msc_underwater_kelp_day")
    scene bg msc_underwater_kelp_day at bg with dissolve
    "Arianna dives under and I quickly follow into the cool water."
    show mscmc bikini_hairup_cu smile_cu at mscmc_cu
    "(I'm so glad I can see so well underwater because I would hate to miss this.)"

    scene bg msc_underwater_ship_day at bg with dissolve
    "Below is a coral reef of pinks and light blues - just behind is the shipwreck."
    show mscmc bikini_hairup surprised at centre
    "(To think that this is where Arianna spends so much of her time!)"
    show mscmc smile at left2
    show arianna siren grin at right2
    "Arianna takes my hand with a brilliant smile and tugs me towards the ship."
    hide arianna
    show mscmc bikini_hairup_cu smile_cu at mscmc_cu
    "(Even underwater, her hand feels so warm.)"
    hide mscmc
    "We move closer to the wreck, a school of tiny fish swimming out of the way."
    "I look into one of the windows, seeing piles of human junk and half-finished projects."
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(I've never wanted to have gills more than in this moment because I need to go up for air soon.)"
    show mscmc bikini_hairup basic at left2:
        pause 0.2
        easeout 1.0 yoffset -1250
    show arianna siren basic at right2
    "Letting go of Arianna's hand, I motion to the top and start to swim up as she follows me."

    play sound "audio/sfx/MSC_Sound_Effects/big_splash.mp3"
    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_ocean_wide_day at bg with dissolve
    show mscmc bikini_hairup surprised at left2:
        yoffset 300
        easein_back 0.5 yoffset 105
    show arianna siren smile at right1plus:
        yoffset 500
        pause 0.2
        easein 0.5 yoffset 90
    "My head breaks through the water and I take in a breath."
    mcariannaprev grin "That was so cool!"
    show arianna grin
    show mscmc surprised:
        easein 0.4 yoffset 100
    "Arianna laughs as I gasp out my words between breaths."
    show mscmc smile:
        easein 0.4 yoffset 105
    mcariannaprev "I might be able to get my hands on some diving gear next time."
    "Arianna swims closer, tilting her head at me and twirling a piece of her hair."
    ai smile "Next time? You're already asking me on a second date?"


    show mscmc grin
    show arianna grin
    "She laughs a bit so I know that she's just messing around."
    hide arianna
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu:
        yoffset 0
    "(I wouldn't mind if she thought of this as a date.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas0e5c1:
        "A. Of course!":
            $ menuhideborder = False
            show mscmc bikini_hairup grin at left2:
                yoffset 105
            show arianna siren grin behind mscmc at right1plus:
                yoffset 90
            mcariannaprev "If every date is this special, sign me up!"
            show arianna smile
            mcariannaprev "I'm not sure much could top this."

        "B. Say you'd like to show her human stuff.":
            $ menuhideborder = False
            show mscmc bikini_hairup smile at left2:
                yoffset 105
            show arianna siren smile behind mscmc at right1plus:
                yoffset 90
            mcariannaprev "Y'know, there's up here for you to see too."
            mcariannaprev "Maybe next time we can do something human."
        "C. Start feeling shy.":
            $ menuhideborder = False
            show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu
            "I suddenly feel extremely self-conscious with her eyes trained on me."
            show mscmc bikini_hairup grin at left2:
                yoffset 105
            show arianna siren grin behind mscmc at right1plus:
                yoffset 90
            mcariannaprev "If you want...yeah."


    show mscmc bikini_hairup smile at left2:
        yoffset 105
    show arianna siren grin behind mscmc at right1plus:
        yoffset 90
    ai grin "Well, it's not done yet. There's one last thing I want to show you."

    play sound "audio/sfx/MSC_Sound_Effects/big_splash.mp3"
    show arianna:
        transform_anchor True yalign(1.0) yoffset 739 xoffset 1 rotate 0
        pause 0.3
        linear 1.0 rotate 90 yoffset 850 xoffset -800
    "She beckons me with her finger before diving back down, her tail splashing water at me."
    hide arianna
    show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu:
        yoffset 0
    "(I feel like I'd follow her anywhere.)"

    scene bg msc_underwater_ship_day at bg with fade
    "Excitement bubbles inside of me and I swim down."
    "We go past her studio and towards what looks like a kelp forest."
    show bg msc_underwater_kelp_day with dissolve
    "Staying close together, we move through it until Arianna puts an arm out to stop me."
    show arianna siren basic at centre
    "She parts the last few pieces of kelp with a hand and points out into the distance."
    hide arianna
    show mscmc bikini_hairup surprised at centre
    "I can see some kind of large sparkling dome."
    "Within it, looks to be spiraling skyscrapers reaching up from the ocean floor."
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(It's a city!)"
    show mscmc grin_cu
    "(This must be the mermaid city!)"

    play sound "audio/sfx/MSC_Sound_Effects/big_splash.mp3"
    scene bg msc_ocean_wide_day at bg with fade
    "We swim back to the top, my mind buzzing."
    show surfboard back at left3
    show mscmc bikini_hairup surprised at left2:
        yoffset 100
    show arianna siren smile at right3:
        yoffset 90
    mcariannaprev "That was the city? I thought that you had to go through portals."
    show mscmc smile
    "Arianna laughs as she leads the way back to shore while I paddle next to her on my board."
    ai "Outside it, you're in California or whatever you told me this place is called."
    ai grin "But if you swim into the dome, you're in the tropics!"
    hide arianna
    show surfboard back_cu at centre
    show mscmc bikini_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(That is way too awesome.)"
    hide surfboard
    hide mscmc
    show arianna siren smile at centre:
        yoffset 95
        pause 0.1
        easein 0.4 yoffset 90
    ai "My friends and I could show you such a great night in the city."
    show arianna:
        easein 0.4 yoffset 95
    ai "us underground artists and rejects know all the right spots."
    hide arianna
    "As we near the shore, I find myself wishing we could stay out here forever."

    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    scene bg msc_surf_shop_day at bg
    show trina casual basic at left2
    show arianna dress basic at right2
    with fade
    "That night, Trina and Arianna stand around the counter in the surf shop."
    hide trina
    hide arianna
    show mscmc casual_hairdown smile at centre
    mcariannaprev "I've gathered you all here because Arianna gave me an idea of how to save the shop."
    hide mscmc
    show trina casual basic at centre
    "Trina looks to Arianna with her eyebrows raised and Arianna looks at me just as surprised."
    so smile "I'm desperate enough for anything, so take it away."
    hide trina
    show mscmc casual_hairdown grin at centre
    mcariannaprev "We throw a party!"
    hide mscmc
    show trina casual basic at left2
    show arianna dress grin at right2
    "Arianna's face lights up with an excited breath, but Trina looks less enthused."
    show arianna smile
    so sad "Love the confidence, but I don't think a party is gonna do much."
    ai surprised "Wait, let's hear her out."
    hide trina
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna nods to me with a knowing sparkle in her eye."
    hide arianna
    show mscmc casual_hairdown smile at centre
    mcariannaprev "It'll be a fundraising party and we'll invite the community and kids."
    mcariannaprev "But we'll have something special..."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "I make eye contact with Arianna and a smile grows on her face."
    show arianna dress grin at centre
    ai "A fundraising party with a mermaid."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(She knew exactly what I was thinking!)"
    show mscmc casual_hairdown embarrassed at centre
    "My heart flutters as I smile back at her."
    hide mscmc
    show trina casual basic at centre
    "Trina raises her hands in confusion."
    so sad "A mermaid?"
    show trina at left2
    show arianna dress smile at right2
    ai "A fake one."
    show trina basic
    "Arianna looks down at her hands and twiddles her thumbs."
    hide trina
    hide arianna
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(Time to sell it. I've been thinking this over for a bit.)"
    show mscmc casual_hairdown smile at centre
    mcariannaprev "Arianna is a professional mermaid."
    mcariannaprev "She acts in parties and events and stuff all over."
    mcariannaprev "She even has her own tail."
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(And a really beautiful strong looking one at that.)"
    hide mscmc
    show arianna dress smile at centre
    "Arianna covers an amused grin behind her hand."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Trina has no idea there's a literal mermaid next to her.)"
    show mscmc smile_cu
    "(I'm not sure she'd even believe it. I almost didn't.)"
    hide mscmc
    show trina casual basic at centre
    "Trina looks between Arianna and me."
    so "Alright, this plan is sounding a little better."
    show mscmc casual_hairdown grin at left2
    show trina at right2
    mcariannaprev "My students would flip out over the chance to talk to a mermaid."
    mcariannaprev "They can bring their rich parents and we'll charge for pictures and like time with her."
    mcariannaprev "Like an amusement park princess."
    hide mscmc
    hide trina
    show trina casual_cu sad_cu at trina_cu
    "Trina gives a skeptical look to Arianna."
    show trina casual sad at centre
    so "And you think this will work?"
    hide trina
    show arianna dress smile at centre
    "Arianna throws her hair over her shoulders with a laugh."
    ai "I'm very photogenic, you know."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Does she even try to be so charming?)"
    hide mscmc
    show trina casual basic at centre
    so "We might as well give it a shot. There's that nice old camera in the back."
    hide trina
    show mscmc casual_hairdown grin at centre
    mcariannaprev "I'll take the pictures at the party and we can do a raffle and other stuff."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna lifts her chin at me in mock superiority."
    show arianna dress smile at centre
    ai "Make sure you know my angles."
    show arianna dress_cu smile_cu at arianna_cu
    "A thought seems to cross her mind and Arianna smirks, her eyes looking over me."
    show arianna dress smile at centre
    ai "Why don't you take some photos now?"
    ai "To promote the event."
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(She wants to take photos right {i}now{/i}?)"
    hide mscmc
    show trina casual smile at centre
    so "That's not a bad idea. We can make a poster or flyer."
    hide trina
    show arianna dress embarrassed at centre
    "Arianna licks at her bottom lip with a half-lidded gaze."
    ai "Come on. Don't you want an excuse to stare at me all afternoon?"
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Um, absolutely!)"
    hide mscmc

    show trina casual smile at centre
    "I can feel Trina's excited energy without even looking at her and my heart is in my throat."
    hide trina
    show arianna dress_cu grin_cu at arianna_cu
    ai "Should we do a photoshoot, [genericfn]?"
    hide arianna

    $ menuhideborder = True
    menu ariannas0e5c2:
        "A. Sexy photoshoot with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mscbeach fadein 1.0
            scene bg msc_labeach_sunset at bg with fade
            "Camera in tow, I follow Arianna down to the beach."
            show arianna dress basic at centre
            "She sits on the shore, the tide lapping at her."
            show sparkle_column behind arianna
            show arianna sleep
            "She rubs her ring and her legs are replaced by her glistening tail."
            show arianna siren smile with dissolve
            "Arianna lays on her back, her tail curling up and an arm behind her head."
            hide sparkle_column
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Oh, wow. Okay.)"
            show mscmc jacket_hairdown embarrassed at centre
            "I stand there staring, completely enchanted by every inch of her."
            hide mscmc
            show arianna siren smile at centre
            ai "How do you want me?"
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Right. We're here for pictures.)"
            show mscmc jacket_hairdown smile at centre
            "My hands feel sweaty around the camera and I swallow down my excitement."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(We're doing this for the good of the shop, not just for some fun.)"
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Do whatever you want. Whatever feels natural."
            "I raise the camera and look through it at her."
            hide mscmc
            show arianna siren smile at centre
            "Arianna sits up and leans back on her hands."
            "A classic pose to start."
            show mscmc jacket_hairdown smile at left3
            show arianna siren smile at right3
            "My finger hesitates over the capture button."
            "Her arched back accentuates the curve of her chest."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(This really is the perfect excuse to stare at her.)"
            "(And wow, do I feel like I could stare at her forever.)"

            play sound camera_shutter_6305
            scene bg msc_labeach_sunset at bg
            show mscmc jacket_hairdown smile at left3
            show arianna siren smile at right3
            pause 0.05
            show white
            pause 0.05
            hide white with Dissolve(0.05)
            "I snap the first picture, the flash going off."
            hide mscmc
            hide arianna
            "Arianna changes the pose by lifting one hand and mussing up her hair."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(One photo is really all we need, but I'm not ready to give this moment up.)"
            show mscmc jacket_hairdown grin at centre
            mcariannaprev "Lookin' good! Are you sure you're not some undersea model?"
            hide mscmc
            show arianna siren grin at centre
            "I snap the photo and Arianna laughs, dropping the pose."
            ai "What did I say? I'm very photogenic."
            "She rolls onto her stomach and frames her chin with her hands, grinning."
            ai smile "How's this?"
            hide arianna
            show mscmc jacket_hairdown smile at centre
            "Moving around to the side to act as a real photographer, I crouch."
            mcariannaprev grin "Ten outta ten."
            hide mscmc
            show arianna siren grin at centre
            "She raises her tail over her back, the end fin hanging just over her head."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Her tail looks so graceful. She has such solid control over it.)"
            hide mscmc
            show arianna siren basic at centre
            "After the next photo, Arianna goes limp on her side."
            ai smile "I call this one, 'Beached Whale'."
            show arianna sleep
            "She closes her eyes and hangs her tongue out."
            show mscmc jacket_hairdown grin at left3
            show arianna siren sleep at right3
            mcariannaprev "Pure genius."

            play sound camera_shutter_6305
            show white
            pause 0.05
            hide white with Dissolve(0.05)
            "The flash goes off and we both laugh as Arianna sits up."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Arianna can be such a goofball.)"
            "(Seeing her having fun like this is worth everything.)"
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Wanna see?"
            show mscmc at left1plus
            show arianna siren smile behind mscmc at right1
            "I bend down next to Arianna and bring the photo roll up on the little screen."

            stop music fadeout 0.5
            play music mscromance fadein 1.0
            "She leans in, her cheek nearly to mine."
            hide arianna
            show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
            "(Arianna smells like the ocean, but sweeter.)"
            show mscmc embarrassed_cu
            "(Like some flower of the sea.)"
            show mscmc jacket_hairdown surprised at left1plus
            show arianna siren sad behind mscmc at right1
            "Arianna is silent as I show her the photos, her eyebrows knit."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Does she not like them? She looks absolutely amazing in them.)"
            show mscmc jacket_hairdown basic at left1plus
            show arianna siren basic behind mscmc at right1
            "She brings a finger up and delicately touches the button to move to another photo."
            ai surprised "We have the technology to take photos underwater, but not like this."
            ai basic "It's very different."
            mcariannaprev smile "Yeah, most of our tech wouldn't do too well at the bottom of the sea."
            hide mscmc
            show arianna siren_cu basic_cu at arianna_cu
            "Arianna turns to look at me, her breath now on my cheek."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(She's so close to me that if I turn too...)"
            show mscmc jacket_hairdown embarrassed at left1plus
            show arianna siren embarrassed behind mscmc at right1
            "My face heats up. I turn to her and we're nearly nose to nose."
            ai smile "Let me take your picture."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Arianna wants to take {i}my{/i} picture?)"
            show mscmc jacket_hairdown surprised at left1plus
            show arianna siren smile behind mscmc at right1
            mcariannaprev "Uh, why?"
            "Arianna's already taken the camera from my hands."
            show mscmc basic
            show arianna:
                easein 0.4 right2
            "Fingers under my chin, she tilts my head up and backs away just a little bit."
            ai grin "Perfect."
            show mscmc smile
            "Her low voice makes my breath hitch and she takes the picture."
            ai smile "See? Perfect."
            "Proudly, she shows me the picture."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(I'm surprised at how good it actually looks.)"
            "(It's almost like a professional photo.)"
            show mscmc jacket_hairdown smile at left2
            show arianna siren smile behind mscmc at right1plus
            mcariannaprev "You were worried about me knowing your angles, but you certainly know mine."

            stop music fadeout 0.5
            play music mscarianna fadein 1.0
            ai "I did take a photography class in college."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Mermaids have college too?)"
            show mscmc jacket_hairdown surprised at left2
            show arianna siren smile behind mscmc at right1plus
            mcariannaprev "You went to college?"
            show arianna sleep
            "Arianna nods absently, her eyes on the picture of me."
            show mscmc basic
            ai basic "Yep, for fine art. I dropped out though. Not really my thing."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(That doesn't come as a surprise. She's so freespirited.)"
            show mscmc jacket_hairdown basic at left2
            show arianna siren surprised behind mscmc at right1plus
            ai "What about you?"
            show arianna basic
            mcariannaprev smile "Yeah. I have a degree in marine biology."
            hide arianna
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(Even if that degree was only so I could get my parents off my back and focus on surfing.)"
            show mscmc jacket_hairdown basic at left2
            show arianna siren smile behind mscmc at right1plus
            "Arianna giggles and raises the camera again."
            ai "Well show me how a marine biologist works it for the camera."
            show mscmc smile
            "I give my hair a flip and imitate the most classic model face."
            show arianna surprised
            "Arianna takes the picture and when she looks down at it, her eyes widen a bit."
            ai "You look amazing!"
            show arianna embarrassed
            "She catches her bottom lip between her teeth, her eyes flicking up to me."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "({i}Oh{/i}.)"
            "(Does she think I'm pretty?)"
            show mscmc jacket_hairdown smile at left2
            show arianna siren embarrassed behind mscmc at right1plus
            "I reach over to take the camera from her hands, my eyes dropping."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(It's getting late...)"
            scene bg msc_labeach_night at bg
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            with dissolve
            "(I should probably get the camera back to Trina.)"
            show mscmc jacket_hairdown basic at centre
            mcariannaprev "We should get back."
            hide mscmc
            show sparkle_column behind arianna
            show arianna siren basic at centre
            "Arianna nods a little too quickly as she rubs her ring, her legs reappearing."
            show arianna dress grin at centre with dissolve
            ai "Yeah."
            hide sparkle_column
            hide arianna
            "I help her to her feet feeling giddier than usual."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(When was the last time I had fun like this?)"

        "B. Offer to set-up for the party.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(Of course I want an excuse to stare at Arianna!)"
            show mscmc smile_cu
            "(Like how Arianna would definitely put on the most picture perfect smile)"
            "(And how her plump lips would curl up or how her tail flexes when it moves.)"
            show mscmc casual_hairdown surprised at centre
            mcariannaprev "Actually, I can just help setup for the party."
            mcariannaprev basic "We don't need promotional pictures."
            mcariannaprev smile "Let's just find a photo online or something."
            show mscmc embarrassed
            "I drop Arianna's gaze, my ears burning."
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(What is wrong with me? She was totally flirting and I just blew it!)"
            hide mscmc
            show arianna dress sad at centre
            "Arianna pulls back from the counter with a small pout."
            ai "Aw, okay."
            hide arianna
            show mscmc casual_hairdown sad at left2
            show trina casual basic at right2
            "Trina snaps me a bewildered look and I give her a tiny shake of the head."
            show trina smile
            "A smirk growns on her face as she realizes my dilemma."
            hide trina
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(Oh Trina, please let this go. I'm beating myself up enough just fine.)"
            hide mscmc
            show trina casual smile at centre
            so "Don't worry about setting up."
            so "You guys can just go to the bar and tell Jerry about it."
            so "That guy loves to talk. He'll spread the word."
            hide trina
            show mscmc casual_hairdown smile at centre
            "I nod, thankful for her input."
            mcariannaprev "Sounds good."

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    scene bg msc_beach_bar_day at bg with fade
    "The beach bar is moderately packed as Arianna and I sit at the counter."
    "We tell Jerry about the fundraising party and he nods with a big grin."
    jr "I will certainly let the people know. Anything for you and Trina."
    jr "People want to give back to that place."
    "He slides us two beers with a wink."
    jr "Those are on the house!"
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown smile at left2
    "Arianna takes the beer excitedly and I look around, feeling at ease."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(It'll work out. It has to.)"
    show mscmc jacket_hairdown angry at centre
    "The ease I feel turns to unease as I see none other than Hamish sitting in the corner by himself."
    hide mscmc
    show hamish casual angry at centre
    "His phone is to his ear and he seems pretty annoyed at whoever's on the other line."
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Leave it to Hamish to ruin every peaceful moment.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress basic behind mscmc at right1plus
    "I nudge Arianna's foot with my own and nod over at the corner."
    ai surprised "Is that Hamish?"
    show arianna basic
    mcariannaprev sad "Unfortunately."
    hide mscmc
    hide arianna
    show hamish casual basic at centre
    "He looks up with a heavy breath, his eyes going our way."
    hide hamish
    show mscmc jacket_hairdown basic at left2
    show arianna dress basic behind mscmc at right1plus
    "Arianna and I are quick to avert our eyes."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show arianna smile
    "Tapping on the rim of her glass, Arianna gives a soft smile."
    ai "I like this."
    mcariannaprev smile "Yeah? I'll remember that if I ever come to visit you at your studio."
    "Arianna raises an eyebrow at that, but says nothing as she takes a sip."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Am I actually flirting with her? Trina would be proud of me.)"
    show mscmc jacket_hairdown surprised at left2
    show arianna dress basic behind mscmc at right1plus
    "I'm feeling bold enough to keep going, but I find that Arianna's attention is elsewhere."
    "She's looking at her sculpture behind the bar, a tightly closed fist on her lap."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(If we can get her art back, it would mean the world to her.)"
    show mscmc jacket_hairdown embarrassed at centre
    "A memory of her bright smile makes my stomach flip with butterflies."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Anything to see her smile like that.)"
    hide mscmc
    show arianna dress_cu basic_cu at arianna_cu
    "My eyes drop to watch the curve of Arianna's lips as she takes a drink."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(So much for not catching feelings.)"
    show mscmc surprised_cu
    "(What am I thinking? I haven't caught anything.)"
    show mscmc smile_cu
    "(She's just...really pleasant to be around.)"
    show mscmc basic_cu
    "(I have to focus.)"
    hide mscmc
    "Jerry passes behind the counter, drying out a glass with a cloth."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Screw it! We're getting Arianna's art back.)"
    show mscmc basic_cu
    "(I want her to be proud of herself.)"
    show mscmc jacket_hairdown smile at centre
    mcariannaprev "Hey Jerry, that sculpture is really something. Who's the artist?"
    hide mscmc
    show arianna dress_cu surprised_cu at arianna_cu
    "Arianna snaps her head toward me with her mouth agape."
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress surprised at right1plus
    "I give her an encouraging nod with a grin."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Come on, Arianna. Own it.)"
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress sleep behind mscmc at right1plus
    "Arianna puts her shoulders back and clears her throat."
    show arianna basic
    jr "Oh? Actually, I'm not sure-!"
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    ai "I'm the artist of that piece..."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "She sneaks another look at me and takes a breath."
    show arianna dress basic at centre
    ai "A few weeks ago, someone stole that piece from my studio."
    hide arianna
    "The chatter of the small bar dies down, attention drawing to us."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She did it!)"
    hide mscmc
    show hamish casual angry at centre
    rm "And how can you be the artist of this piece?"
    hide hamish
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Arianna being the artist means that Hamish can no longer sell her art as his own.)"
    hide mscmc
    show hamish casual basic at centre
    "Hamish is stepping up beside the counter."
    show hamish sad
    "His eyes look nervous, but he's trying to look stern."
    rm angry "What proof do you have?"
    hide hamish
    show arianna dress basic at centre
    ai "I mark every piece with my ring. It's my signature."
    "Arianna sticks her thumb up, showcasing the ring."
    ai "The mark should be on the bottom."
    hide arianna
    "Jerry examines Arianna's ring and bends down to check the sculpture."
    jr "Sure as daylight, it's there!"
    show hamish casual_cu surprised_cu at hamish_cu
    "Hamish's face falls and he takes a step back from the counter."
    hide hamish
    show arianna dress smile at centre
    jr "You're awfully talented, miss. Any other pieces you're selling?"
    ai "I'll be selling pieces at Trina's Surf Shop fundraiser. All proceeds go to the shop."
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna winks at me and I feel completely awestruck."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's really going to sell her art at the party?)"
    "(That's...)"
    show mscmc jacket_hairdown grin at centre
    "I find it hard to catch my breath and a smile grows on my face."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She's such a sweetheart.)"
    hide mscmc
    "Jerry is more than happy to give Arianna another free round of beer."

    show arianna dress grin at right1plus
    show mscmc jacket_hairdown smile at left2
    "We clink our glasses together, ready to cheers when Hamish approaches."
    hide mscmc
    hide arianna

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    show hamish casual angry at centre
    rm "There's no way you're the artist. You can't be."
    hide hamish

    $ menuhideborder = True
    menu ariannas0e5c3:
        "A. Tell Hamish to back off.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
            "I frown, a feeling of protectiveness surging through me."
            show mscmc jacket_hairdown angry at centre
            mcariannaprev "Step off, Hamish."
        "B. Ignore him.":
            $ menuhideborder = False
            show mscmc jacket_hairdown angry at centre
            "I roll my eyes."
            show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
            "(He's like a bug. Ignore it and it goes away.)"
        "C. Laugh at him.":
            $ menuhideborder = False
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Why not? Because {i}you're{/i} the real artist?"
            show mscmc grin
            "I laugh to myself and shake my head."

    hide mscmc
    show hamish casual basic at centre
    "He points an accusing finger at Arianna."
    rm angry "There's something fishy about you and I'm going to find out what."
    show hamish casual_cu angry_cu at hamish_cu
    rm "Mark my words."

    scene msc_tbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
