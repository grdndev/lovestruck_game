label arianna_season1_episode4:
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

    show surfboard back at left2:
        xoffset -40
    show mscmc surfer_hairup basic at left2
    show arianna siren grin at right3:
        yoffset 130
    ai "And that's when I was like, why is there a fish skeleton in your hair?"
    show mscmc smile
    "Arianna throws her hands up, flecks of water meeting my skin as I paddle beside her."
    ai "And he was like 'Oh well, it's he latest fashion'. It {i}was{/i} cool."
    show arianna surprised
    "Arianna pauses to hesitantly look up at me."
    ai embarrassed "Do you like my style?"
    hide surfboard
    hide arianna
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Maxime was asking if I'd seen any weird women around. Could it really be her?)"
    "(She can seem a bit out of place at times.)"
    show surfboard back behind mscmc at left2:
        xoffset -40
    show mscmc surfer_hairup basic at left2
    show arianna siren sad at right3:
        yoffset 130
    ai "Why aren't you saying yes?"
    mcarianna surprised "Sorry, sorry. I think you're very fashionable."
    hide surfboard
    hide arianna
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(There's no way he could know about her being a mermaid.)"
    show surfboard back behind mscmc at left2:
        xoffset -40
    show mscmc surfer_hairup smile at left2
    show arianna siren grin at right3:
        yoffset 130
    "Arianna grins and tosses her hair over her shoulders."
    ai "Thank you."
    mcarianna grin "Didn't we come out here so you could work on your commissions?"
    ai "Oh, yeah! We're here!"
    show surfboard:
        linear 0.5 xoffset -200
    show mscmc:
        parallel:
            linear 0.3 yoffset 130
        parallel:
            easeout 0.5 xoffset 50
    "I slide off my board into the water next to Arianna and she puts a hand to my shoulder."
    show mscmc smile
    show arianna behind mscmc:
        easein 0.5 right1
    ai "Hold on, air-breather. I'm not letting you in my studio, remember?"
    ai "It's not a safe place for humans."
    show arianna smile
    mcarianna sad "I'll just take a little peek inside, okay?"
    hide surfboard
    hide arianna
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu:
        yoffset 0 xoffset 0
    "(I will get in there one day. Maybe I should look into scuba gear?)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "Don't breathe in any water or I might have to give you mouth to mouth."
    show arianna smile_cu
    "Arianna tilts her head at me with a sly smile, her eyes flicking down to my lips."
    hide arianna
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    mcarianna "Yeah, that would be, uh...not good! Right? Yeah, not good. Won't breathe in water."
    mcarianna "Got lungs of steel. Can hold my breath forever."
    "(Nailed it.)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "You are such a cutie. Come on."
    hide arianna
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Arianna, you are going to be the death of me.)"
    play sound "<to 4>audio/sfx/MSC_Sound_Effects/splash02.mp3"
    show surfboard back behind mscmc at left2:
        xoffset -200
    show mscmc surfer_hairup smile at left2:
        yoffset 130 xoffset 50
        pause 0.2
        parallel:
            easein_circ 0.5 xoffset 130
        parallel:
            easein 0.5 yoffset 180 knot 80 knot 180
        parallel:
            linear 0.5 alpha 0.0
    show arianna siren grin behind mscmc at right1:
        yoffset 130
        pause 0.1
        parallel:
            easein_circ 0.5 xoffset 80
        parallel:
            easein 0.5 yoffset 180 knot 80 knot 180
        parallel:
            linear 0.5 alpha 0.0
    "Arianna goes under the water, and I'm right behind her as we dive down."

    hide surfboard
    stop music fadeout 0.5
    play music mscromance fadein 1.0
    $ wavy_transition("bg msc_ocean_wide_day", "bg msc_underwater_ship_day")
    scene bg msc_underwater_ship_day at bg with dissolve
    "Seeing the outside of the sunken ship that's her studio is as mesmerizing as it was the first time"
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(I don't think any of this mermaid stuff will ever get old.)"
    show mscmc surfer_hairup smile at left1:
        xoffset -30 yoffset 50 alpha 0.0
        pause 0.2
        linear 0.5 xoffset 0 yoffset 10 alpha 1.0
    show arianna siren grin at right1:
        xoffset 30 yoffset 50 alpha 0.0
        pause 0.1
        linear 0.5 xoffset 0 yoffset 10 alpha 1.0
    "Arianna looks over her shoulder to make sure I'm behind her and she grins."
    ai "Stay out here, my human."
    hide arianna
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(All I want is to see everything Arianna can show me.)"
    hide mscmc
    "Arianna swims through an opening on the side of the shipwreck and I make my way to one of the portholes to look in."
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(I'm sure I could find a good deal on a scuba rental somewhere.)"

    scene arianna_s1_mini2 at bg with dissolve
    "Arianna pops up on the other side of the porthole."
    "She winks at me!"
    "(God, she's so damn cute!)"

    scene bg msc_underwater_ship_day at bg
    show arianna siren grin at centre
    with dissolve
    "Arianna puts her hand up to the glass and I put mine there too."
    hide arianna with dissolve
    "She turns and looks over her shoulder before swimming away."
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Should I leave her to it? I won't be able to stay here and watch her work.)"
    hide mscmc
    show arianna siren grin at left1:
        pause 0.3
        parallel:
            easein_circ 0.4 xoffset 120
            linear 0.4 xoffset 80
        parallel:
            easein 0.8 yoffset -400
        parallel:
            linear 0.8 alpha 0.0
    pause 1.0
    "But, Arianna swims back out and, as I point up, she follows me to the surface."

    $ wavy_transition("bg msc_underwater_ship_day", "bg msc_ocean_wide_day")
    scene bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup grin at left2:
        yoffset 140
    show arianna siren grin at right2:
        yoffset 140
    with dissolve
    mcarianna "Be cooler if I could get inside."
    ai "We'll figure something out."
    show arianna smile
    mcarianna "Well, I'll let you get to work then. Don't want to keep Emporia waiting."
    show mscmc smile
    "Arianna purses her lips in thought."
    ai grin "Wait. Not juuuuust yet."
    play sound big_splash
    show arianna smile:
        alignaround(0.5, 0.2) transform_anchor True rotate 0 yoffset 140
        pause 0.3
        parallel:
            linear 0.3 yoffset 120
            linear 0.5 yoffset 500
        parallel:
            pause 0.2
            linear 0.3 rotate 3 xoffset 20
        parallel:
            linear 1.0 alpha 0.0
    "She smirks and dives back down."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(There's more to show me?)"

    hide mscmc with dissolve
    $ wavy_transition("bg msc_ocean_wide_day", "bg msc_underwater_kelp_day")
    scene bg msc_underwater_kelp_day at bg with dissolve
    "After a deep breath of air, I swim down to see her hovering beside the kelp forest."
    show arianna siren_cu grin_cu at arianna_cu
    ai "Hurry up, slowpoke!"
    show arianna siren grin at centre:
        xoffset 76
        pause 0.1
        easein_back 0.4 xoffset 60
    show mscmc surfer_hairup smile at left1plus:
        pause 0.2
        easein 0.4 xoffset 0 knot -10 knot 0
    "She grabs my wrist with a laugh sending a jolt of electricity through me with her touch."
    ai sad "I know we both have things to do, but...I'm not ready to say goodbye yet."
    hide arianna
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Honestly, neither am I. I love spending time with her.)"
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    "Arianna then taps my arm with a smirk, pausing momentarily to wait for my questioning brow."
    show arianna siren_cu grin_cu at arianna_cu:
        pause 0.3
        linear 0.4 alpha 0.0
    pause 0.7
    ai "Tag, you're it!"
    show arianna siren grin at centre:
        alignaround(0.5, 0.5) transform_anchor True yoffset 600 rotate 0 xoffset 30 alpha 0.0
        rotate 3
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            easein 0.4 yoffset -10
            easein 0.3 yoffset 0
        parallel:
            pause 0.3
            linear 0.2 rotate 0 xoffset 0
    "She swims off into the kelp before popping her head back out, waiting for me with a silly smile."
    hide arianna

    $ menuhideborder = True
    menu ariannas1e4c1:
        "A. Play Arianna's game!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Work can wait...for just a bit.)"
            hide mscmc
            show arianna siren grin at centre:
                alignaround (0.5, 0.5) transform_anchor True rotate 0
                pause 0.4
                parallel:
                    linear 1.0 alpha 0.0
                parallel:
                    easein 0.3 yoffset -10
                    easein 0.4 yoffset 500
                parallel:
                    pause 0.1
                    linear 0.3 rotate 1 xoffset 10
                    linear 0.2 rotate 0
            pause 1.5
            hide arianna
            "As I start to swim after Arianna, her face lights up before she disappears into the kelp."
            "I glide through the kelp with the gentle ocean, looking for the glint of Arianna's tail."
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(She'll definitely be able to outswim me, but I should be able to use the element of surprise.)"
            show mscmc grin_cu
            "The thought of playing underwater tag with a mermaid makes me feel light with excitement."
            "(If only childhood-me could know that this is where we'd end up.)"
            show mscmc embarrassed_cu
            "(Not even just knowing mermaids are real though...it's Arianna. She's what's so special.)"
            hide mscmc
            "A rustle to my left catches my eye and I dive down lower as I approach."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Got her right where I want her.)"
            hide mscmc
            show arianna siren:
                align (0.5, 0.5) rotate 0 yoffset 500
                rotate -90
                block:
                    linear 0.8 rotate -93
                    linear 0.8 rotate -87
                    repeat
            "I can see the tip of one of her fins drifing against the swaying kelp."
            show arianna siren:
                align (0.5, 0.5) rotate 0 yoffset 500
                rotate -90
                pause 0.1
                parallel:
                    linear 0.2 yoffset 480
                    linear 0.4 yoffset 600
                parallel:
                    linear 0.6 alpha 0.0
            pause 0.6
            hide arianna
            "As I propel myself up, ready to tag her, her tail moves out of the way."
            show arianna siren_cu grin_cu at arianna_cu
            ai "Don't think I'm an easy target!"
            show arianna siren smile at left1:
                alpha 0.5 yoffset 0
                pause 0.1
                parallel:
                    linear 0.8 alpha 1.0 right1
                parallel:
                    linear 0.8 yoffset 0 knot 0 knot 30 knot -30 knot 0
            "She swims backwards, albeit seeming purposefully slower than usual."
            ai grin "Come and get me."
            show arianna siren grin at right4:
                pause 0.3
                parallel:
                    linear 0.4 alpha 0.5
                parallel:
                    easein 0.4 xoffset 30 yoffset 40
                easein 0.4 xoffset -30 left3
                parallel:
                    linear 0.4 alpha 1.0
                parallel:
                    easein 0.4 xoffset 0 yoffset 0
            show mscmc surfer_hairup smile at right1:
                xoffset -100 alpha 0.0
                pause 0.2
                parallel:
                    linear 0.4 alpha 1.0
                parallel:
                    easein 0.4 xoffset 0
                easein 0.4 xoffset -50
            "I lunge for her again and she circle sback around me with a laugh."
            ai smile "Feeling a little out of your element?"
            hide arianna
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu:
                xoffset 0
            "(When in doubt, fake 'em out.)"
            show arianna siren smile behind mscmc at left1plus
            show mscmc surfer_hairup surprised at right2
            "Putting on my best surprised face, I point to the left."
            show arianna sad
            "Arianna frowns and looks to where my finger is pointing."
            ai "What?"
            hide arianna
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(Easy target.)"
            show arianna siren surprised behind mscmc at left1plus:
                pause 0.1
                easein_back 0.3 xoffset -40
            show mscmc surfer_hairup grin at right2:
                easein 0.3 xoffset -50
                parallel:
                    linear 0.3 alpha 0.0
                parallel:
                    easein 0.3 xoffset 250
            "I hit my knuckles against her tail and dive off in the other direction."
            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu:
                xoffset 0
            ai "You tricked me!"
            hide arianna
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(We never made any rules about that!)"
            hide mscmc
            "I swim down and then stop, hiding amongst a particularly thick patch of kelp."
            show arianna siren grin at centre:
                xoffset -150 alpha 0.5
                parallel:
                    linear 0.5 alpha 1.0 xoffset 0
                parallel:
                    easein 0.5 yoffset 0 knot 0 knot -30 knot 0
            ai "Come out, come out, wherever you are."
            ai smile "You're in my turf, don't forget."
            hide arianna
            "Arianna's voice draws closer and as the kelp sways, I see the ends of her hair poke around."
            "I sink down just a little bit and then stay still."
            "Arianna is quiet now, but it seems like she swam away."
            show arianna siren_cu grin_cu at arianna_cu
            ai "Surprise attack!"
            show mscmc surfer_hairup grin at centre:
                xoffset -30
                pause 0.2
                easein 0.2 xoffset -70
                easein 0.3 xoffset -60
            show arianna siren grin at centre:
                xoffset 80
                pause 0.1
                easein 0.3 xoffset 40
                easein 0.3 xoffset 60
            "Arianna's arms wrap around me from behind, her chest presses to my back."
            show mscmc embarrassed
            ai smile "Looks like there's a cute human swimming around in my water."
            "Her arms around me are loose, but I don't bother trying to swim away."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(The only game of tag where I don't mind getting caught.)"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            "Arianna laughs in my ear and hugs me tighter."
            ai "I think this is when you're supposed to tag me again."
            show arianna siren smile at right1plus
            show mscmc surfer_hairup smile at left1plus:
                xoffset 80
                pause 0.3
                easein 0.5 xoffset 20
            "I do slip down out of her arms, but Arianna doesn't swim away."
            show mscmc:
                pause 0.1
                linear 0.4 xoffset 0 left1
            "I touch her shoulder."
            show arianna:
                pause 0.1
                easein_back 0.4 xoffset -30
            show mscmc:
                pause 0.2
                easein_back 0.4 xoffset -30
            "She taps me back."
            show mscmc:
                linear 0.4 xoffset 0
            show arianna:
                pause 0.2
                easein 0.2 xoffset -60
            "When I go to tag her again, she catches my wrist."
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu:
                xoffset 0
            ai "No tag-backs."
            show arianna siren grin at right1
            show mscmc surfer_hairup embarrassed at left1
            "She lets go of my wrist so that she can put her palm to mine."
            "Her long hair drifts gently around her."
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "You really are my favorite human, you know."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "Staying in this moment is the only thing I want."
            show mscmc sad_cu
            "(Damn these lungs of mine.)"
            hide mscmc
            play sound big_splash
            pause 2.0
            show arianna siren_cu grin_cu at arianna_cu
            "I break away from the magnetism of her eyes and swim towards the surface."
            hide arianna

            $ wavy_transition("bg msc_underwater_kelp_day", "bg msc_ocean_wide_day")
            scene bg msc_ocean_wide_day at bg
            show arianna siren grin at right3:
                yoffset 140

            show mscmc surfer_hairup smile at left1plus:
                around(0.3, 0.5) transform_anchor True yoffset 490 rotate 0 xoffset 40 alpha 0.0
                rotate 2
                pause 0.3
                parallel:
                    linear 0.8 alpha 1.0
                parallel:
                    easein 0.4 yoffset 100
                    easein 0.3 yoffset 120
                parallel:
                    pause 0.3
                    linear 0.2 rotate 0 xoffset 20
            "As I break the water and take a breath, she comes up beside me laughing."
            ai "So, I won."
            mcarianna grin "How did you win? You were cheating."
            ai surprised "What did I do that was cheating?"
            mcarianna "You grappled me and then said no tag-backs when it was convenient."
            mcarianna "That was cheap."
            show mscmc smile
            ai grin "I did tag you more though. Therefore, I'm the winner. You were also the last one 'it'."
            mcarianna grin "It's about quality over quantity."
            play sound splash01
            ai smile "And {i}you{/i} didn't cheat? You faked me out."
            mcarianna "It's your fault for falling for it."
            show mscmc:
                easein_back 0.4 centre xoffset -36
            "I try to tag Arianna's shoulder, but she dodges it."
            show mscmc smile
            ai grin "Just accept your defeat! I have to get to work!"
            mcarianna grin "I guess we both do."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu:
                xoffset 0 yoffset 0
            "(Even though I really don't want to leave.)"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "Arianna smirks at me."
            ai grin_cu "Well, it was fun playing with you."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(She can play with me however she wants.)"
            show mscmc surprised_cu
            "(God, I need to shut my thoughts up.)"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu:
                anchor (0.5, 0.5) yoffset 360
                pause 0.1
                linear 0.4 zoom 1.15
            "Neither of us makes a move to leave. In fact, Arianna swims a tiny bit closer."
            show arianna smile_cu
            "The smirk falls from her face, an intensity in her eyes replacing the playfulness."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(I should get back.)"
            "Everything in my body fights my mind."
            "(What is she thinking?)"
            "Another silent moment passes before I regain control of myself and clear my throat."
            stop music fadeout 0.5
            play music mschappytimes fadein 1.0
            mcarianna grin_cu "I had a good time too."
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "I'm glad."
            hide arianna
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcarianna "Come find me when you're finished up?"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "Of course. I'll see you later."
            show arianna siren_cu grin_cu at arianna_cu, step_out
            "Arianna blows me a kiss and goes back under the water."

        "B. You need to get to the Surf Shop.":
            $ menuhideborder = False
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(She wants to play tag right now?)"
            show mscmc sad_cu
            "(I have to get to Trina's for work...)"
            hide mscmc
            show arianna siren surprised at centre:
                alpha 0.5 yoffset 200
                easein 0.5 alpha 1.0 yoffset 0
            "When I don't follow after her, Arianna eventually pops her head back out of the kelp."
            show arianna:
                easeout 1.0 yoffset -600 alpha 0.0
            "I point to the top and swim to the surface, Arinna right behind me."

            $ wavy_transition("bg msc_underwater_kelp_day", "bg msc_ocean_wide_day")
            scene bg msc_ocean_wide_day at bg
            show arianna siren_cu grin_cu at arianna_cu
            with dissolve
            ai "What? Worried I'd beat you too bad?"
            hide arianna
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            mcarianna "I gotta work--Trina really wanted me to help her set up some boards."
            hide mscmc
            show arianna siren_cu basic_cu at arianna_cu
            ai "Alriiiiiight. I guess I should probably work too."
            hide arianna
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcarianna "Come find me when you're finished up?"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "Of course. I'll see you later."
            show arianna siren_cu grin_cu at arianna_cu:
                pause 0.1
                parallel:
                    ease 0.8 yoffset 400 knot -80 knot 400
                parallel:
                    linear 0.8 alpha 0.0
            "Arianna blows me a kiss and goes back under the water."

    scene bg msc_labeach_day at bg with clockwise_wipe
    "After a few hours, Arianna and I meet back up at the beach, we're sitting on the sand next to each other watching the waves."
    show mscmc jacket_hairdown smile at left1
    show arianna dress basic behind mscmc at right3:
        pause 0.1
        easein 0.5 right2
    "I go to put my phone away after responding to a text from Trina, but Arianna stops my hand."
    ai grin "What kind of stuff does your phone do?"
    mcarianna grin "A lot of stuff. Take pictures, videos, text, call. It's pretty much a handheld computer."
    show arianna surprised
    "I hand my phone over to Arianna and she takes it with a delicate hold."
    ai "It's asking for your passcode."
    mcarianna "Four 7's."
    ai smile "How secure."
    show mscmc smile
    "Arianna types in the passcode and starts swiping on the screen."
    ai surprised "My phone can't take pictures, but I can text and call."
    show arianna smile
    mcarianna surprised "You can text on that thing?"
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(The shellphone is already a wonder on its own.)"
    hide mscmc
    "Arianna sets my phone onto her lap and pulls her shell out."
    "She presses a tiny button on the side and I watch as a compartment opens for a keyboard."
    show arianna dress grin at right1plus:
        xoffset 30
    show mscmc jacket_hairdown smile at left1
    ai "Nothing as fancy as yours."
    show arianna smile
    mcarianna grin "Somewhat surprising considering you guys have magic."
    show mscmc smile
    ai grin "Eh, I'm not really a phone person anyways, I like a nice off-the-grid lifestyle."
    mcarianna grin "You got games on your phone?"
    ai surprised "Games? Like what?"
    mcarianna surprised "Ah, nothing. It's just a meme."
    ai "Meme?"
    mcarianna grin "It's like an internet joke. Kinda."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I'm going to make it my mission to teach Arianna every part of stupid human culture.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress surprised behind mscmc at right1plus:
        xoffset 30
    ai "Oh...do you have games on your phone?"
    show arianna smile:
        easein 0.4 right1 xoffset 0
    "I take my phone from Arianna's lap and she leans into me so she can watch."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Don't think about how good she smells...)"
    show mscmc jacket_hairdown grin at left1
    show arianna dress smile behind mscmc at right1
    mcarianna "Not a lot, but when I'm really bored I mess around with this one."
    mcarianna "It's a word scramble thing. Make as many words as you can out of the letters here and everyday you get different letters."
    mcarianna "You can re-scramble them if you get stuck."
    show mscmc smile
    show arianna:
        easein 0.4 xoffset 30
    "I offer the phone to Arianna and she takes it, hunching over to block the screen from the sun."
    ai grin "Oh, this is pretty fun actually."

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    hide arianna
    hide mscmc
    "I lean back on my hands, looking out over the water and watching a surfer catch a wave."
    show hamish casual basic at centre:
        transform_anchor True zoom 0.55 yoffset 130
    "A disgustingly familiar suit down the beach catches my eye."
    hide hamish
    show arianna dress basic at right1
    show mscmc jacket_hairdown angry at left1
    mcarianna "Hamish is here."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(There's still the issue of Hamish and my sponsorship.)"
    show arianna dress angry behind mscmc at right1
    show mscmc jacket_hairdown sad at left1
    "Arianna glances up with a grimace."
    mcarianna "What am I gonna do about him? He's, clasically, ruining everything."
    ai sad "We just need a way to make him back off."
    mcarianna "He doesn't back off easily. He's like a mosquito."
    hide arianna
    hide mscmc
    show hamish casual basic at centre:
        transform_anchor True zoom 0.55 yoffset 130
    "Hamish passes a boy digging out a hole in the sand beside a huge sandcastle."
    show hamish angry
    "Not even looking, the kid throws a handful of sand over his back, dusting Hamish."
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(I'd like to throw sand at Hamish.)"
    hide mscmc
    show hamish casual angry at centre:
        transform_anchor True zoom 0.55 yoffset 130
    "Hamish stops in his tracks, shaking a fist at the kid."
    hide hamish
    show arianna dress basic at right1
    show mscmc jacket_hairdown sad at left1
    mcarianna "And now he's getting into a fight with a child."
    show arianna surprised
    "Arianna watches the scene with Hamish yelling at a kid unfold."
    hide arianna
    hide mscmc
    show hamish casual angry at centre:
        transform_anchor True zoom 0.55 yoffset 130
    "In some kind of fit, Hamish begins stomping on the sandcastle, kicking sand every which way."
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(He really is {i}that{/i} guy, huh?)"
    show arianna dress sad behind mscmc at right1
    show mscmc jacket_hairdown angry at left1
    mcarianna "He's a douche."
    show mscmc basic
    show arianna basic
    "Arianan taps her hand against me and holds my phone out."
    ai surprised "Hey, take a video with your phone!"
    mcarianna surprised "What, why?"
    ai "Because he sucks! Isn't this kind of the perfect thing to show that?"
    ai "Isn't that the kind of stuff people post on the internet? 'Grown man makes a kid cry'."
    hide arianna
    hide mscmc
    show hamish casual angry at centre:
        transform_anchor True zoom 0.55 yoffset 130
    "I pull up my camera and zoom in, recording Hamish in his rage along with the crying kid."
    hide hamish
    show arianna dress surprised at right1
    show mscmc jacket_hairdown surprised at left1
    ai "What if we show him the video and threaten to post it?"
    ai smile "We don't ruin his reputation in exchange for him backing off of Trina's Shop."
    ai grin "This guy is obsessed with his image. It might work, right?"
    show arianna angry
    mcarianna smile "Actually, it just might."
    hide arianna
    hide mscmc
    "As Hamish finishes stomping out the castle, Arianna and I approach him."

    $ menuhideborder = True
    menu ariannas1e4c2:
        "A. You really are an ass.":
            $ menuhideborder = False
            show arianna dress angry at right1plus
            show mscmc jacket_hairdown angry at left1
            mcarianna "You really are an ass, aren't you?"
            hide arianna
            hide mscmc
            show hamish casual angry at centre
            rm "Oh great, my least favorite person to ever exist."
            hide hamish
            show arianna dress angry at right1plus
            show mscmc jacket_hairdown angry at left1
            mcarianna "Back at you."
            hide arianna
            hide mscmc
        "B. That was pathetic":
            $ menuhideborder = False
            show arianna dress angry at right1plus
            show mscmc jacket_hairdown smile at left1
            mcarianna "Wow, you really showed that 6-year-old."
            mcarianna "That was pathetic, Hamish. Low, even for you."
            hide arianna
            hide mscmc
            show hamish casual angry at centre
            rm "That little twerp was-!"
        "C. Got something to show you.":
            $ menuhideborder = False
            show arianna dress smile at right1plus
            show mscmc jacket_hairdown grin at left1
            mcarianna "Hey Hamish, got something to show you."
            hide arianna
            hide mscmc
            show hamish casual angry at centre
            rm "Run back to your precious shop and get out of my face."
            hide hamish
            show arianna dress smile at right1plus
            show mscmc jacket_hairdown grin at left1
            mcarianna "I think you're gonna want to see this."
            hide arianna
            hide mscmc

    show hamish casual_cu angry_cu at hamish_cu
    "Hamish's eyes widen as he sees Arianna, but his face quickly drops into a scowl."
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(He probably thought she'd never come back, but Arianna's not scared of him.)"
    show arianna dress angry behind mscmc at right1plus
    show mscmc jacket_hairdown angry at left1
    mcarianna "I've got a proposition for you. Stop saying shit about Trina's shop and I won't post this."
    hide arianna
    hide mscmc
    show hamish casual angry at centre
    "I hold my phone up for him to see the video play and his shoulders tense with each second."
    show hamish at left4:
        pause 0.1
        easein_back 0.4 left1plus
    show mscmc jacket_hairdown angry at right2:
        pause 0.2
        easein_back 0.4 right5
    "He makes a grab for it, but I pull my phone back."
    hide hamish
    hide mscmc
    show arianna dress angry at centre
    ai "Sure would be a shame if everyone saw what a jerk you are."
    ai smile "Could even ruin some of your business."
    hide arianna
    show hamish casual angry at centre:
        pause 0.2
        linear 0.4 alpha 0.0
    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    "Hamish makes some kind of grumble and growl, turning away and stalking down the beach."
    hide hamish
    show mscmc jacket_hairdown surprised at left1
    show arianna dress smile at right1plus
    mcarianna "Was that...a good sign? Think it worked?"
    ai grin "I'm sure. If it hadn't, he would've had something annoying to say."
    mcarianna smile "Let's hope."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(If Hamish backs off, I can finally get this sponsorship deal.)"

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    scene bg msc_mansion_interior_day at bg with fade
    "With Hamish, hopefully, out of our hair, Arianna and I have more room to think about her comissions for Emporia."
    "Once she finishes the first piece, we head to Emporia's house to show it to her."
    "A different butler from before takes us to the living room where Arianna sets the piece down."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna's sculptures are so fascinating and unique. It's not hard to see how talented she is.)"
    show mscmc sad_cu
    "(But I want Arianna to get this job done and get paid so we don't have to talk to Emporia anymore.)"
    hide mscmc
    show emporia casual smile mask at centre:
        xoffset -100 alpha 0.0
        pause 0.1
        linear 0.4 xoffset 0 alpha 1.0
    bn "Ah, what a delight it is to see you have the first piece done."
    "Emporia waltzes into the room, her arms crossed."
    hide emporia
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown smile at left1
    ai "The other two are coming along nicely too."
    hide arianna
    hide mscmc
    show emporia casual basic mask at centre
    "Emporia walks around the sculpture, eyeing every inch of it."
    bn smile "You got it done rather quickly, didn't you?"
    stop music fadeout 0.5
    play music msctense fadein 1.0
    bn basic "I just think that it looks a little rushed. This side here is far too uneven."
    bn sad "It needs to be different."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Great, here we go.)"
    hide mscmc
    show emporia casual basic mask at left2
    show arianna dress surprised at right3
    ai "Well, I can go ahead and adjust that."
    bn angry "It's not just that."
    bn "There's not enough of an ocean flowing feel to it, not dynamic. It's far too solid."
    hide arianna
    hide emporia

    $ menuhideborder = True
    menu ariannas1e4c3:
        "A. Defend the piece.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            mcarianna "I think it captures exactly what you asked for."
            mcarianna "It's incredibly dynamic."
            hide mscmc
            show emporia casual angry mask at left2
            show arianna dress sad at right3
            bn "I'm talking to the artist, not you, dear."
        "B. Don't say anything.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I can hold my tongue. I won't start something with Emporia.)"
            hide mscmc
            show emporia casual sad mask at left2
            show arianna dress sad at right3
            "But Arianna's dejected face makes my leg bounce."
        "C. Call Emporia out.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            mcarianna "How can you say it wasn't what you wanted?"
            mcarianna "You hardly gave any instructions."
            hide mscmc
            show emporia casual angry mask at left2
            show arianna dress sad at right3
            bn "And now I'm giving them."

    show emporia sad
    ai basic "You told me to do what I wanted, but if you have something more specific-"
    show arianna surprised
    bn angry "I'd like to come with you to your studio--see the process."
    bn "Then I can perhaps help to understand why it turned out this way."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Well, there's no way Emporia can see her studio. It's underwater!)"
    hide mscmc
    show emporia casual sad mask at left2
    show arianna dress sad at right3
    ai "I understand that, but my studio really isn't a place for visitors."
    show emporia angry
    "Emporia clicks her tongue and stands taller with a sharp glare at Arianna."
    bn "What kind of business is that? I'm paying you a large sum of money for this work."
    bn "How do you expect to get more clients when you're so closed off?"
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(What is with her?! She's lighting Arianna up for no reason!)"
    hide mscmc
    show emporia casual smile mask at left2
    show arianna dress sad at right3
    "I start to open my mouth, but Emporia laughs to herself."
    "She smiles softly, her tense posture suddenly very relaxed."
    bn "Well, of course. It is your workspace afterall. It can't be helped."
    bn "I have full faith in your artistic abilities, Arianna."
    "Arianna nods slowly an catches my eye."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I don't know whether to be pissed at Emporia or just confused.)"
    hide mscmc
    show emporia casual smile mask at left2
    show arianna dress smile at right3
    ai "I promise the other ones will...meet your expectations."
    bn "I'm sure they will."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Alright. Enough of this meeting.)"
    show arianna dress basic behind mscmc at right1plus
    show mscmc jacket_hairdown basic at left1
    "I clear my throat and stand."
    mcarianna surprised "If that's all for today, it's time we get going. Arianna needs to get back to work."
    show emporia casual angry mask at left4
    show arianna at right5
    show mscmc basic at right1plus
    "Emporia eyes me with a harsh glare."
    bn "Does your manager decide everything that you do in your life?"
    mcarianna angry "As her manager, I need to manage her work time."
    show mscmc basic
    "Arianna puts a hand on my shoulder."
    show emporia basic
    ai grin "It would be best for me to get back to my studio. I have a lot more to do."
    bn smile "Of course, of course. I do very much so look forward to the rest of your work."
    hide arianna
    hide emporia
    hide mscmc
    "As the butler returns to lead us out, I can feel Emporia's eyes burning into my back."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(I don't like anything about this. I'm going to get to the bottom of what throws me off about you, Emporia. Time to do some research.)"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
