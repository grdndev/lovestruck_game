label arianna_season1_episode7:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg as background
    play music mscantagonist

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Emporia Lid is an anagram for Mia Diplore...)"
    "(Oh my god.)"
    show mscmc sad_cu
    mcarianna "{i}Oh my god{/i}."
    show mscmc surprised_cu
    "(And Maxime's a merman! Holy shit! What is going on?!)"

    show mscmc surfer_hairup surprised at centre
    "Hand to my forehead, I blow out a long breath."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(I need to talk to Arianna.)"

    scene bg msc_mc_bedroom_day at bg with fade
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    "I head to my room and open the door."
    show arianna dress basic at centre
    "Arianna is sitting cross-legged on my bed with my laptop in front of her as movie credits scroll on the screen."
    show arianna angry at right2
    show mscmc surfer_hairup basic at left2
    ai "So, he doesn't turn her into a vampire?"
    hide arianna
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Oh, yeah I left her with a movie playing.)"
    hide mscmc

    $menuhideborder = True
    menu ariannas1e7c1:
        "A. Spill it!":
            $menuhideborder = False
            show mscmc surfer_hairup surprised at left2
            show arianna dress surprised at right2
            mcarianna "No time! Arianna!"
            ai "What? What happened?"
            show arianna surprised
            mcarianna sad "You're never gonna believe this!"
        "B. Take a breath.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "I need to chill for just a second."
            show mscmc sleep_cu
            "I take a deep breath, hold it in for ten seconds, and blow it out."
            show mscmc surfer_hairup sleep at left2
            show arianna dress surprised at right2
            ai "Are you okay?"

        "C. Get distracted by the movie Midnight for just one second.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left2
            show arianna dress surprised at right2
            mcarianna "No, but there are four movies."
            show arianna grin
            ai "Can we watch them?"
            show mscmc sad
            mcarianna "Another time."

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show mscmc sad
    show arianna basic
    mcarianna "I just figured out some shit, Arianna."
    show arianna surprised
    ai "Like...?"
    mcarianna "I was walking home on the boardwalk and I saw Maxime below on the beach."
    show arianna basic
    "I sit on the edge of the bed and Arianna scoots my laptop away from her to turn towards me."
    mcarianna "He was talking to a woman and I was...eavesdropping but not eavesdropping."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(If I hadn't dropped my keys, I never would've even seen him.)"
    hide mscmc
    show mscmc surfer_hairup basic at left2
    show arianna dress basic at right2
    mcarianna "They said they're in the mer government and were talking about an exiled mermaid."
    show arianna surprised
    ai "{i}What{/i}?! Maxime, that other surfing instructor?"
    show arianna basic
    show mscmc surprised
    mcarianna "Yes, but that's not all!"
    mcarianna "The exiled mermaid's name is Mia Diplore."
    show arianna surprised
    "Arianna's eyes widen."
    show mscmc sad
    mcarianna "They're looking for her, and said she's dangerous, and all this stuff."
    mcarianna "And then I got a notification from the word scramble game and..."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    mcarianna "I think Emporia Lid is Mia Diplore. The names are anagrams for each other."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "Arianna's shoulders sink."
    hide arianna
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Does she think this is too outside the realm of possibility?)"
    hide mscmc
    show mscmc surfer_hairup sad at left2
    show arianna dress sad at right2
    ai "What?"
    show mscmc basic
    show arianna surprised
    mcarianna "There's virtually nothing about Emporia anywhere on the internet."
    show mscmc sad
    show arianna sad
    mcarianna "Maybe it's because she's a mermaid in hiding."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(It would make a lot of sense! And maybe she somehow knows Arianna is also a mermaid.)"
    hide mscmc
    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show mscmc surfer_hairup basic at left2
    show arianna dress sad at right2
    ai "I don't think Emporia is Mia. I know Mia Diplore...or I used to, a long time ago."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(No way! What're the odds of that?)"
    hide mscmc
    show mscmc surfer_hairup surprised at left2
    show arianna dress basic at right2
    mcarianna "You did?!"
    show mscmc basic
    show arianna surprised
    ai "Well, not {i}know her{/i} know her, but we went to school together for a bit, like, elementary."
    ai "Her family moved away and then like 15 years later I heard she got exiled for running some ponzi scheme or something."
    show mscmc surprised
    show arianna sad
    ai "But, if she was Mia...I feel like I would've recognized her..."
    show mscmc basic
    show arianna basic
    mcarianna "She wears a mask."
    "Arianna nods as she leans against the pillows."
    ai sleep "Yeahhh, but still."
    ai smile "I mean, she {i}could{/i} but, but I don't really think so."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(I thought I was really on to something.)"
    hide mscmc
    show mscmc surfer_hairup basic at left2
    show arianna dress sad at right2
    mcarianna "They said Mia is dangerous."
    show mscmc sad
    ai basic "You have to take what the government says with a grain of salt."
    show mscmc basic
    ai surprised "Growing up, I always found art to be the best way to express myself"
    show mscmc smile
    ai grin "It's comfortable and real and also not real, which is why it's so great."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(I can tell how important art is to her. Surfing is my way of self-expression.)"
    hide mscmc
    show mscmc surfer_hairup basic at left2
    show arianna dress angry at right2
    ai "But our government condemns the arts."
    ai sad "In my world, government doesn't necessarily mean good and going against them isn't necessarily bad."
    show mscmc sad
    mcarianna "I get that."
    ai "They think the self-expression of art is too closely linked to magic."
    show mscmc basic
    show arianna angry
    ai "Which is also a no-no."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(I remember Arianna mentioning that when she told me about her magic ring.)"
    hide mscmc
    show mscmc surfer_hairup sad at left2
    show arianna dress sad at right2
    mcarianna "Is it really that bad? I mean, you're a mer artist."
    ai angry "It's pretty bad. Like, bad enough for me to be in a semi-illegal resistance group."
    show mscmc surprised
    show arianna basic
    mcarianna "You're in a resistance?"
    ai angry "We work against the draconian stance towards art and magic, the government is just trying to hoard power."
    show arianna smile
    mcarianna "That's actually...really awesome"
    "Arianna hums in thought and fiddles with her necklace."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(It must be hard to be an outcast for doing something she loves.)"
    hide mscmc
    show mscmc surfer_hairup basic at left2
    show arianna dress grin at right2
    ai "The situation sucks, but I've met a lot of really great people through the movement."
    show mscmc smile
    ai sad "Just because someone is exiled doesn't mean they're actually bad or dangerous."
    show mscmc sad
    show arianna basic
    mcarianna "Maybe I was jumping the gun."
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu basic_cu at mscmc_cu
    "(I don't have enough evidence to really back up the conclusion I came to.)"
    hide mscmc

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show mscmc surfer_hairup basic at left2
    show arianna dress grin at right2
    "Arianna sits up, looking at a surfing poster on my wall."
    ai "Hey, we still need to film your surfing for High Tide."
    show mscmc smile
    ai "Enough about Mia. I get where you're coming from, I just don't think it's her."

    scene bg msc_ocean_wide_day at bg with fade
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    "We go to the secret cove I like to surf at so that Arianna can be in her mer form."
    window hide
    show surfboard back at centre:
        yoffset 130
    show mscmc surfer_hairup smile at centre:
        xoffset -50
    show arianna siren grin at right2:
        yoffset 150
        pause 0.2
        parallel:
            linear 1.5 xoffset -450 knot 0 knot 10 knot -460 knot -450
        parallel:
            linear 1.5 yoffset 150 knot 150 knot 180 knot 150

    pause 2.0
    "As I sit on my board, waiting for a good wave, Arianna swims around, snapping photos."

    hide arianna
    hide mscmc
    hide surfboard
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(It's a good thing no one comes to this part of the beach. This would be...quite the sigt to see.)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "You look good with the water on your skin. Give me a distant look over the ocean."
    ai "Wonderful."
    ai embarrassed_cu "Now, put your hand in your hair. Mysterious surfer babe vibes."
    hide arianna
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "Though it feels a bit funny, I put my hand in my hair and Arianna is more than pleased."
    hide mscmc
    show surfboard back at left1plus:
        yoffset 100
    show mscmc surfer_hairup grin at left1
    show arianna siren smile at right3:
        yoffset 150
    mcarianna "There's a big one coming in."

    hide mscmc
    hide arianna
    hide surfboard
    "I point towards the wave and then start paddling, Arianna following behind ready to film."
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(It's kinda embarrassing having Arianna watching me so closely, but I can't think about that.)"
    hide mscmc
    "I wait for the right moment and as I catch the wave, I push myself to my feet."
    "There's a flash of pink through the wave and then Arianna jumps out beside me with the camera."
    "Cool flecks of water spray my face and I feel the tension melt away from my mind and body as the wave rears under me and I do a cut back."
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(This is where it feels like home. Here on the water.)"
    hide mscmc
    "After that wave, I catch every other one that I can, Arianna leaping above and around me."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "On the next wave, I shift slightly, but I can tell it was the wrong decision the second I do it."
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        alignaround(0.5, 0.5) rotate 0
        transform_anchor True
        parallel:
            linear 0.4 rotate 3
        parallel:
            linear 0.5 alpha 0.0
        parallel:
            pause 0.2
            linear 0.5 ypos 400
    "I wipe out, anticipating falling into the wave below."
    scene arianna_03_s1e7 with fade:
        align(0.5, 1.0) transform_anchor True zoom 1.3
        pause 0.5
        linear 5.0 yoffset 1210
    pause 5.0
    "But I never hit the water."
    "Arianna leaps into the air, catching me."
    "She pulls me to her chest, so we're pressed together."
    "Time stops."
    "I can't tell if that's her heart beating or my own."
    "(She's ethereal.)"
    scene bg msc_ocean_wide_day at bg with fade
    "We land back in the water and I can't help but laugh at the absurdity of her actually catching me."
    show arianna siren embarrassed at right1
    show mscmc surfer_hairup grin at centre:
        yoffset 50 xoffset -30
    mcarianna "You didn't need to catch me!"
    ai grin "I wasn't going to let you fall!"
    mcarianna "Falling is part of surfing."
    hide arianna
    hide mscmc
    "I pull my board over, throwing my hair out of my face."
    show surfboard back at left3:
        yoffset 80 xoffset -20
    show mscmc surfer_hairup smile at left1plus
    show arianna siren surprised at right2:
        yoffset 150
    ai "You don't care?"
    mcarianna grin "Why would I? I fall all the time. Shit happens."
    hide surfboard
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Even professional surfers have wipeouts.)"
    hide mscmc
    show surfboard back at left2:
        yoffset 80
    show mscmc surfer_hairup grin at left1plus
    show arianna siren surprised at right2:
        yoffset 150
    mcarianna "I know I'm good at surfing--I can't let a fall make me doubt."
    show mscmc basic
    ai sad "I guess that's true...I've never been able to think that way about my art."
    "Arianna looks down at her hands and fidgets with her ring."
    show mscmc sad
    ai basic "It needs to be perfect. All the time."
    ai "I get disappointed in myself when it doesn't meet my own standards."
    hide surfboard
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Arianna's so hard on herself about work. I get it.)"
    hide mscmc
    show surfboard back at left2:
        yoffset 80
    show mscmc surfer_hairup grin at left1plus
    show arianna siren sad at right3:
        yoffset 150
    mcarianna "It's okay to have standards for yourself too, you know."
    show arianna grin
    mcarianna "Just don't dwell on your mistakes 'cause ultimately they're helping you be better for next time."
    show mscmc smile
    show arianna smile
    "Arianna glances to the side in thought, lips pursed, before it's gone in a flash."
    ai grin "I love watching you surf--you look so alive. So passionate."
    show mscmc grin
    "I duck my head with a flustered laugh."
    mcarianna "Thanks. Surfing is my everything."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show arianna smile behind surfboard:
        easein_back 0.4 right1plus
    show mscmc smile
    "Arianna puts her arms on my board, testing her weight on it."
    ai grin "I want to know what it feels like."
    hide surfboard
    hide arianna
    hide mscmc
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Arianna really wants to try surfing?)"
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "Wind in my hair and not a care in the world."
    ai "Would you show me how to ride a wave?"
    hide arianna

    $menuhideborder = True
    menu ariannas1e7c2:
        "A. Show Arianna the joys of surfing!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show arianna siren grin at right1plus:
                yoffset 150
            show surfboard back at left2:
                yoffset 80
            show mscmc surfer_hairup grin at left1plus
            mcarianna "I'd love to show you!"
            hide surfboard
            hide arianna
            hide mscmc
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(She won't be able to stand on teh board with her tail, but we'll make this work.)"
            "(I'd still love to see it.)"
            hide mscmc
            show arianna siren grin at right3:
                yoffset 150 xoffset 20
            show surfboard back at centre:
                yoffset 80
            show mscmc surfer_hairup grin at left1:
            # animation: jump off surfboard
                parallel:
                    linear 0.2 xoffset -150
                parallel:
                    easeout_circ 0.2 yoffset 165
                easein 0.2 yoffset 150
            play sound big_splash
            "I slip off into water beside Arianna and pat my board."
            "Get on."
            hide surfboard
            hide mscmc
            hide arianna
            show arianna siren_cu grin_cu at arianna_cu
            ai "This is so exciting!"
            hide arianna
            show surfboard back at centre:
                transform_anchor True zoom 1.3 yoffset 100
                rotate 25
                pause 0.2
                linear 0.4 right1plus
            show arianna siren grin at right3:
                yoffset 150
                pause 0.1
                parallel:
                    linear 0.5 centre
                parallel:
                    easein_circ 0.5 yoffset 0
            show mscmc surfer_hairup smile at left4:
                yoffset 150
            "Arianna hoists herself up, the end of her tail hanging off the back."
            ai surprised "It's kind of slippery."
            show arianna smile
            "She moves her tail around, the board squeaking beneath her."
            hide surfboard
            hide arianna
            hide mscmc
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(It might not be the most stable thing for her, but it'll work well enough for a tiny wave.)"
            hide mscmc
            show surfboard back at right1plus:
                transform_anchor True zoom 1.3 yoffset 100 rotate 25
            show arianna siren smile at centre
            show mscmc surfer_hairup grin at left4:
                yoffset 150
            mcarianna "It's not built for fish scales."
            show mscmc smile
            ai grin "Once you get your sponsorship, have them make a mermaid board"
            mcarianna grin "That'll be number one on the priority list."
            hide surfboard
            hide arianna
            hide mscmc
            "Arianna lays against the board and begins paddling away, giggling to herself."
            show arianna siren_cu grin_cu at arianna_cu
            ai "I already feel like a surfer."
            hide arianna
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcarianna "You look like one. Now get back here."
            show mscmc embarrassed_cu
            "(And she's so adorable too.)"
            hide mscmc
            show surfboard back at right3:
                transform_anchor True zoom 1.3 yoffset 100 rotate 25
            show arianna siren smile at right1
            show mscmc surfer_hairup grin at left2:
                yoffset 150
            mcarianna "We'll catch one of the baby waves."
            mcarianna "I'll give you a push at the right time so you can catch the wave and then use your arms to push yourself up."
            show arianna basic
            "Arianna nods intensely like she's engraining my words into her brain."
            ai surprised "Alright, I think I can do that."
            show arianna smile
            show mscmc smile
            "I wade around beside her, watching until I see a nice little wave on the rise."
            hide arianna
            hide surfboard
            hide mscmc
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(This one's perfect for her.)"
            hide mscmc
            show surfboard back at right3:
                transform_anchor True zoom 1.3 yoffset 100 rotate 25
            show arianna siren smile at right1
            show mscmc surfer_hairup grin at left2:
                yoffset 150
            mcarianna "Okay, let's catch this one."
            mcarianna "Alright, surf's up. You ready?"
            ai grin "Yes!"
            hide surfboard
            hide arianna
            hide mscmc
            "I push Arianna off as the wave comes in and she's off!"
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Look at her go!)"
            "I cup my hands over my mouth."
            mcarianna "Woooooo! Go Arianna!"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "AHHHH!"
            "Arianna's long hair billows out behind her."
            hide arianna
            "She curls the end of her tail up and over her back as the wave carriws her towards the shore."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(I would love to see a surfing competition between mermaids.)"
            "(The Olympics could be insane.)"
            hide mscmc
            show mscmc surfer_hairup smile at left2:
                yoffset 150
            show surfboard back behind mscmc at centre with dissolve:
                yoffset 50
            show arianna siren grin behind surfboard at right4, right_in:
                yoffset 150
            "As the wave pitters out, Arianna flops back into the water and swims my board back to me."
            mcarianna grin "Good job!"
            "I hold my hand up and Arianna high-fives me."
            ai "That was so fun and awesome! I felt like I was flying!"
            mcarianna "Yeah, it's cool, right? That's what hooked me."
            hide surfboard
            hide arianna
            hide mscmc
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(There's no other feeling in the world like surfing. I don't think it can be beat.)"
            hide mscmc
            show arianna siren grin at right4:
                yoffset 150
            show surfboard back at centre:
                yoffset 50
            show mscmc surfer_hairup grin at left2:
                yoffset 150
            mcarianna "It's so freeing."
            show mscmc smile
            "Arianna passes my board to me and I rest an arm on it."
            ai surprised "One day I'll switch to legs. I can't imagine what it would be like to stand and balance."
            show arianna grin
            "Arianna puts two fingers on the board, pretending like it's a little person surfing."
            mcarianna grin "Keep practicing, you'll get there."
            mcarianna "I wouldn't mind teaching you."
            hide surfboard
            hide arianna
            hide mscmc
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(It took me a shile to get used ot it and I was {i}born{/i} with legs.)"
            hide mscmc
            show arianna siren sad at right4:
                yoffset 150
            show surfboard back at centre:
                yoffset 50
            show mscmc surfer_hairup smile at left2:
                yoffset 150
            ai "I feel like you have to be fearless to really do this. I'm scared of falling."
            show arianna basic
            mcarianna grin "I used to get scared, sometimes I still do, but I don't let it hold me back."
            mcarianna "This is what I love to do and I won't let anything get in the way of that."
            mcarianna "There's nothing worse than holding yourself back out of fear."
            hide surfboard
            hide mscmc
            hide arianna
            show arianna siren_cu smile_cu at arianna_cu
            "Leaning against the board, Arianna fixes me with a soft smile, her eyes completely penetrating."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(Whenever she looks at me like that, I feel like my whole body is burning up.)"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "You are so cool."
            hide arianna
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcarianna "I'm not {i}that{/i} cool."
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            "Arianna pushes my shoulder with a laugh."
            ai "So humble and fearless, my human."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(I like hearing her call me that. Like I'm hers.)"
            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu
            "Arianna reachesr her hand out, her thumb wiping the water from my cheek."
            hide arianna
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcarianna "Should I call you, my mermaid?"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "You can call me whatever you want."
            hide arianna
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(She's giving me too much brain overload to think of a good nickname right now.)"
            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu
            "Arianna's thumb drags down my cheek and along my jawline."
            hide arianna
            show arianna siren smile at right4:
                yoffset 150
            show surfboard back at centre:
                yoffset 50
            show mscmc surfer_hairup smile at left2:
                yoffset 150
            "She drops her hand back into the water."
            ai grin "I think we got enough footage for the submission."
            ai "I'll show you everything I got later."
            show arianna embarrassed
            "She wiggles the camera at me "
            hide surfboard
            hide arianna
            hide mscmc
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(I actually am pretty excited for what she captured today.)"
            hide mscmc
            show arianna siren smile at right4:
                yoffset 150
            show surfboard back at centre:
                yoffset 50
            show mscmc surfer_hairup grin at left2:
                yoffset 150
            mcarianna "Thank you for that, by the way."
            mcarianna "You're really helping me out."
            ai grin "That's what friends do."
            hide surfboard
            hide arianna
            hide mscmc
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Friends. Yeah. I like that...)"

        "B. Head back to the shore.":
            $menuhideborder = False
            show arianna siren basic at right1plus:
                yoffset 150
            show surfboard back at left2:
                yoffset 80
            show mscmc surfer_hairup basic at left1plus
            mcarianna "As much as I'd love to see you on a surfboard, I'm exhausted."
            mcarianna sad "Can we head back for now?"
            ai smile "Boo. As long as you promise to teach me one day."
            mcarianna smile "I promise"
            ai grin "Alright, let's go."

    scene bg msc_beach_bar_sunset at bg
    show arianna dress smile at right1plus
    show mscmc jacket_hairdown smile at left1
    with fade
    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    "Arianna clinks her beer against mine as we sit at Jerry's"
    ai grin "Cheer's to surfing!"
    mcarianna grin "Cheers."
    hide arianna
    hide mscmc
    "I set my phone on the table in case I get any calls from High Tide."
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown grin at left1
    ai "How are you feeling about what we filmed? I think I got some great footage."
    mcarianna "You were like flying out of the water and filming! If that's not good enough for High Tide then they're stupid."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(There's probably very little surf cinematography that can compete with a mermaid behind the camera.)"
    hide mscmc
    show arianna dress smile at right1plus
    show mscmc jacket_hairdown grin at left1
    mcarianna "It's out of my hands now. What happens happens."
    ai grin "You want it though."
    show mscmc sad
    "I put my head down on the table."
    mcarianna "So badly."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I won't let it get me too down if I don't get it, but damn that would suck.)"
    hide mscmc
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown embarrassed at left1
    "I feel Arianna's hand on my arm and she rubs my arm a few times."
    show mscmc smile
    ai "What did you say earlier? Shit happens."
    ai "You're always telling me I'm a real artist regardless of what happens."
    "With my head still down, Arianna's soothing voice is all I can focus on."
    ai "There are other companies out there."
    "Arianna draws a little circle on my arm with her nail."
    ai surprised "That being said, I do believe in bad vibes, so we need to believe you're going to get it."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I do have to agree with her on that. I can't think about not getting it.)"
    hide mscmc
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "Come on. Let me see that face of yours."
    show mscmc sad
    "Chin on the table, I move my arms out of the way so I can look at her."
    ai "Awww, give me a smile?"

    hide arianna
    hide mscmc
    $menuhideborder = True
    menu ariannas1e7c3:
        "A. Smile!":
            $menuhideborder = False
            show arianna dress grin at right1plus
            show mscmc jacket_hairdown grin at left1
            "I give her the cheesiest stupid grin I can muster."
            mcarianna "Better?"
            ai "Much!"
        "B. No.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "Face as straight as can be, I stare into Arianna's eyes."
            mcarianna sad_cu "I don't wanna."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "You're still cute, so it's fine."
        "C. Hide your face again.":
            $menuhideborder = False
            "Instead, I bury my face back into my arms."
            show arianna dress_cu surprised_cu at arianna_cu
            ai "No, come back!"
            hide arianna
            show arianna dress grin at right1plus
            show mscmc jacket_hairdown sad at left1
            "I peek out and Arianna laughs."
            ai "Fine, you don't have to!"


    hide arianna
    hide mscmc
    play sound phone_vibrating
    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    "She pats my head and as she does, my phone vibrates."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "Emporia's calling."
    "Arianna pushes my phone towards me and I put it on speaker."
    show arianna basic
    mcarianna surprised "Hello, Emporia."
    hide arianna
    hide mscmc
    bn "I need to speak to the artist."
    show arianna dress basic at right1plus
    show mscmc jacket_hairdown surprised at left1
    mcarianna "Uh huh."
    show arianna sad
    show mscmc sad
    "Arianna and I both roll our eyes."
    ai surprised "Hey, what's up?"
    hide arianna
    hide mscmc
    bn "Well, we're almost finished with our business, aren't we?"
    show arianna dress surprised at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "Two days. Yep."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Can't come soon enough in my opinion.)"
    hide mscmc
    bn "And how is your work coming? Have you been eating well?"
    bn "Following the regiment?"
    show arianna dress surprised at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "Yeah, of course. Doing my best."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(We deleted the email with the weird lifestyle regiment the second I got it.)"
    hide mscmc
    bn "Good, good. I knew you were the right one for the job."
    bn "I wanted to invite you over for dinner to celebrate the commissions."
    bn "I was thinking the night you turn the final piece in."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown basic at left1
    "Arianna cringes and shakes her head at me."
    ai sad "Oh, no that's alright."
    hide arianna
    hide mscmc
    bn "There is someone that I want you to meet."
    bn "They're big in the art world, could really do things for your career."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown basic at left1
    "Arianna looks at me and I shake my head 'no.'"
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(It doesn't matter if Emporia isn't Mia--I still don't trust her.)"
    hide mscmc
    show arianna dress surprised at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "I have to check what I'm doing that evening so I'll get back to you on that."
    hide arianna
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Good answer.)"
    hide mscmc
    bn "Of course, I understand that you're a very busy woman."
    bn "Right, well I look forward to your answer."
    bn "If you decide to come for dinner, don't bring your assistant. Just yourself."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(She's trying to get Arianna alone, why?)"

    scene bg msc_msctbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
