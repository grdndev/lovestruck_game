label arianna_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mc_bedroom_day at bg
    play music mscmctheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "As a new day dawns, for once it's Arianna that wakes up before me."
    show arianna dress_cu grin_cu at arianna_cu:
        transform_anchor True zoom 0.85 alpha 0.0
        linear 0.8 zoom 1.0 alpha 1.0
    "She taps me on the nose and I open my eyes to her leaning over me."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Waking up like this...it almost feels like we're a couple.)"
    "(Can't I just stay in bed all day looking at her?)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Morning, sleepyhead."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Morning."
    show mscmc embarrassed_cu
    "(I wonder if she's been thinking the same things.)"
    show mscmc casual_hairdown smile at left1
    show arianna dress grin behind mscmc at right1plus
    ai "You said something in your sleep last night."
    mcarianna surprised "I did?"
    ai embarrassed "Something about how everyday you spend with me is better than the last."
    mcarianna grin "I did not say that."
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(At least I hope not! I would die from embarrassment.)"
    show mscmc casual_hairdown grin at left1
    show arianna dress grin behind mscmc at right1plus
    "Arianna laughs quietly."
    ai "You didn't."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Arianna's eventually going to notice that my heart hasn't slowed down since she's been back.)"
    show mscmc grin_cu
    "A favorite tactic of mine: change the subject."
    show mscmc casual_hairdown grin at left1
    show arianna dress basic behind mscmc at right1plus
    mcarianna "What do you want to do today?"
    show mscmc smile
    show arianna smile
    "Arianna rolls onto her back."
    ai grin "Well, I signed up for a yoga class early in the afternoon."
    mcarianna grin "Yoga? Really?"
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(She does give me yoga smoothie girl vibes.)"
    show mscmc casual_hairdown smile at left1
    show arianna dress grin behind mscmc at right1plus
    ai "Yeah, I thought it'd be fun. Stretch these new legs of mine and see more human stuff."
    mcarianna grin "I can probably try to come with you, I'll just need to tell Trina."
    show arianna smile
    mcarianna "We were planning on getting some surfing videos of me to send to the water sport company."
    show mscmc smile
    ai grin "You don't need to come with me. I'm kind of excited to go off on my own."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(I guess if Arianna wants to acclimate, she'll have to be able to do things on her own.)"
    "(She's perfectly capable of taking care of herself.)"
    show mscmc casual_hairdown grin at left1
    show arianna dress smile behind mscmc at right1plus
    mcarianna "Alright, but call me if you need anything?"
    show mscmc smile
    show arianna grin
    "Arianna looks over at me and sticks her pinky out."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Pinky promise."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "I lock my pinky with hers."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Shoot some gnarly videos, dude. Cowabunga."
    hide arianna
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "I can't help the snort that I left out."
    show mscmc grin_cu
    mcarianna "You sound like a surfer bro."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "All part of the plan of blending into human society."
    hide arianna
    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    "We take our time in getting up and ready and then walk out of the shop together."

    scene bg msc_ocean_wide_day at bg
    show surfboard front at centre as trina_board:
        transform_anchor True zoom 0.7 yoffset 20 xoffset 10
    show trina casual basic at centre
    with clockwise_wipe
    "Trina is already waiting at the beach for me, sitting out on her board in the water."
    show surfboard front at right3 as trina_board:
        transform_anchor True zoom 0.7 yoffset 20 xoffset 10
    show surfboard back behind mscmc at left2:
        yoffset 60 xoffset -30
    show mscmc surfer_hairup basic at left2
    show trina casual sad at right3
    so "God, it's about time you woke up!"
    show trina smile
    mcarianna surprised "You could've knocked on my door."
    so "And interrupt you two? No thanks."
    mcarianna grin "There was nothing to interrupt."
    so "That makes me sad for you."
    mcarianna embarrassed "Shut up."

    scene bg msc_ocean_wide_day at bg
    "Trina tries to get shots as I surf around her."
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "Surfing is surfing, but something about being filmed makes it feel different."
    show mscmc sad_cu
    "(I need to look good in everything that I post now. Talk about pressure.)"
    hide mscmc
    "But, I manage to ignore the camera, mostly, and film what we need."
    show surfboard back behind mscmc at left2:
        yoffset 60 xoffset -30
    show surfboard front behind mscmc at right3 as trina_board:
        transform_anchor True zoom 0.7 yoffset 20 xoffset 10
    show mscmc surfer_hairup basic at left2
    show trina casual smile at right3
    so "So, how {i}is{/i} Arianna?"
    mcarianna embarrassed "Good."
    so "That's it? Give me more than that."
    mcarianna grin "I mean, I dunno! She's awesome and pretty and fun."
    hide surfboard
    hide trina_board
    hide trina
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(And she's all that I think about.)"
    show surfboard back behind mscmc at left2:
        yoffset 60 xoffset -30
    show surfboard front behind mscmc at right3 as trina_board:
        transform_anchor True zoom 0.7 yoffset 20 xoffset 20
    show mscmc surfer_hairup smile at left2
    show trina casual smile at right3
    so "Okay, okay, now we're getting into it."
    "Trina stops her fiddling with the camera as she looks at me with a suggestive smirk."
    so "How does she make you feel?"
    hide surfboard
    hide trina_board
    hide trina
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Trina's pulling out her friend-therapist mode.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas1e5c1:
        "A. Do we have to do this?":
            $ menuhideborder = False
            show surfboard back behind mscmc at left2:
                yoffset 60 xoffset -30
            show surfboard front behind mscmc at right2 as trina_board:
                transform_anchor True zoom 0.7 yoffset 20 xoffset 20
            show mscmc surfer_hairup sad at left2
            show trina casual basic at right3
            "I can't help but groan a little."
            mcarianna "Trina, do we have to do this right now?"
            so smile "You are not running from me."
            show mscmc sleep
            so "Mama Trina's here. Tell me how you feel."
        "B. There aren't words for it.":
            $ menuhideborder = False
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(She makes me feel everything.)"
            show surfboard back behind mscmc at left2:
                yoffset 60 xoffset -30
            show surfboard front behind mscmc at right3 as trina_board:
                transform_anchor True zoom 0.7 yoffset 20 xoffset 10
            show mscmc surfer_hairup grin at left2
            show trina casual basic at right3
            mcarianna "I don't know. It's like there aren't really any words for it."
            mcarianna embarrassed "Like the feeling you get when you can't breathe at the sight of them."
            so smile "That's when you know you'fe fallen."
        "C. I want to be with her all the time.":
            $ menuhideborder = False
            show surfboard back behind mscmc at left2:
                yoffset 60 xoffset -30
            show surfboard front behind mscmc at right3 as trina_board:
                transform_anchor True zoom 0.7 yoffset 20 xoffset 10
            show mscmc surfer_hairup sad at left2
            show trina casual smile at right3
            mcarianna "I want to be with her all the time."
            show mscmc basic
            so "Should I pretend to be Arianna to make you feel better?"
            show mscmc grin
            show trina sad
            "Trina throws her hair over her shoulders and pouts her lips."
            show mscmc smile
            so "I'm so cool and tall."
            show trina smile
            mcarianna grin "That goes in the books as one of the worst impressions I've ever seen."

    show trina basic
    mcarianna sad "I think I...like her. {i}Like{/i} like."
    so smile "Awwwwww. We're gonna get you this girl."
    mcarianna surprised "I thought she wasn't your favorite?"
    show mscmc embarrassed
    so "I want you to be happy and I can tell that you are when you're with her."
    so "I'll be the ultimate wingwoman."
    mcarianna grin "Thanks. Just don't embarrass me...please."
    so "It's a part of the process, babe."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    scene bg msc_surf_shop_day at bg with fade
    "With the shop slow and Arianna still out, I decide it's time to look into Emporia."
    "Slouched at the store computer, I type Emporia's full name into the search bar."
    "All the internet gives me is links to a thousand things that have nothing to do with her."
    "Even the search image are random things, none of her."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(For someone as rich as her, there has to be information out there. Even just like stuff to make her look good.)"
    show mscmc basic_cu
    "(Everyone knows who rich people are.)"
    show mscmc sad_cu
    "(It's like she just randomly appeared one day and started buying Arianna's art.)"
    hide mscmc
    "I try putting \"the\" in front of her name, but all that gives me is shops with the word \"Emporium\"."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Finding people is supposed to be easy and it's not like she's some nobody.)"
    hide mscmc
    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    show maxime casual basic at centre with dissolve
    "The shop bell dings as Maxime walks in, a towel thrown over his shoulder."
    hide maxime
    show mscmc casual_hairdown surprised at centre
    mcarianna "'Sup?"
    hide mscmc
    show maxime casual smile at centre
    mx "Hey."
    "He walks up to the class scedule, crossing out a time on the board."
    hide maxime
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Maybe a second mind would be able to help with this--I'm coming up with nothing on my own.)"
    show mscmc casual_hairdown surprised at left1plus
    show maxime casual basic at right3
    mcarianna "Do you have a minute?"
    mx "What do you need?"
    mcarianna sad "Have you ever tried to find someone on the internet?"
    mcarianna "I literally can't find anything about this person. No photos or links or anything."
    hide mscmc
    hide maxime

    $ menuhideborder = True
    menu ariannas1e5c2:
        "A. It's like she isn't real.":
            $ menuhideborder = False
            show mscmc casual_hairdown sad at left1plus
            show maxime casual basic at right3
            mcarianna "It feels bizarre. It's like she's not a real person."
            mx smile "Are you sure she is?"
            show maxime basic
            mcarianna "I've met her and been to her house."
        "B. Is that normal?":
            $ menuhideborder = False
            show mscmc casual_hairdown sad at left1plus
            show maxime casual basic at right3
            mcarianna "Is that normal? I've never really tried to find anyone before."
            mx surprised "How long have you been looking?"
            mcarianna "A hot minute."
        "C. Any tips?":
            $ menuhideborder = False
            show mscmc casual_hairdown sad at left1plus
            show maxime casual basic at right3
            mcarianna "Got any tips for me? I feel like an old person who can't use technology."
            mx smile "I guess I could spare some time."

    hide maxime
    hide mscmc
    "He pauses at the board and slowly caps the marker he's holding."
    show maxime casual surprised at centre
    mx "Who are you looking for?"
    hide maxime
    show mscmc casual_hairdown surprised at centre
    mcarianna "Emporia Lid. Ever heard of her?"
    show mscmc casual_hairdown basic at left1plus
    show maxime casual basic at right2:
        alpha 0.0 xoffset 150
        pause 0.1
        linear 0.6 alpha 1.0 xoffset 20
    "Maxime shakes his head as he comes to look at the computer screen."
    mx smile "Interesting name."
    show maxime basic
    mcarianna surprised "She's some big rich person. She has a huge mansion pretty close by."
    show mscmc basic
    mx "What do you want to know about her?"
    show maxime surprised
    mcarianna sad "Anything."
    show maxime sad
    "He raises an eyebrow at me, but doesn't pry any further."
    mx surprised "Do you know her address?"
    hide mscmc
    hide maxime
    "I type the address into the search bar and it pulls a few distant photos of her house."
    show mscmc casual_hairdown basic at left1plus
    show maxime casual smile at right2:
        xoffset 20
    mx "I would click on each picture--if it's from a website or article, it should link you."
    mx "You can also paste the images into image search. That might get something."
    hide mscmc
    hide maxime
    "Maxime stands beside me as I click on each picture of her house, no matter how blurry."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(This shouldn't be this hard.)"
    hide mscmc
    "Luck finally comes to me after one search image actually takes me to a company's website."
    show mscmc casual_hairdown surprised at left1plus
    show maxime casual basic at right2:
        xoffset 20
    mcarianna "Art of the Ocean? What is this?"
    mcarianna sad "The interface looks like it was made in the 90's."
    mx sad "I've never heard of this company before."
    mcarianna "Neither have I."
    hide mscmc
    hide maxime
    "I pause over a few tabs and go to a tab for the board of directors."
    "There's only five names listed, but one of them is exactly what I'm looking for."
    show mscmc casual_hairdown surprised at left1plus
    show maxime casual basic at right2:
        xoffset 20
    mcarianna "That's her!"
    hide mscmc
    hide maxime
    "Listed at the top is Emporia's name."
    show mscmc casual_hairdown surprised at left1plus
    show maxime casual basic at right2:
        xoffset 20
    mcarianna "She's on a board for this company? Is this where her money comes from?"
    mx sad "I don't know who this person is, but this website looks fake."
    mx "If it were really a company, Emporia's name would've come up a lot quicker in the search."
    show maxime basic:
        linear 0.6 alpha 0.0 xoffset 150
    "Maxime shrugs, stepping away from the computer."
    hide mscmc
    show maxime casual surprised at centre:
        alpha 1.0 xoffset 0
    mx "Be careful and I wouldn't trust a word on the website."
    mx sad "I have to run, though. I've got a class."
    hide maxime
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Thanks for the help."
    hide mscmc
    show maxime casual smile at centre
    mx "Sure. Good luck finding whatever it is you're looking for."
    show maxime:
        linear 0.6 alpha 0.0 xoffset 150
    "Maxime leaves with a wave over his shoulder."
    hide maxime
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Who the hell is Emporia?)"
    hide mscmc
    "I search up the company name and see only the same sketchy site."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    scene bg msc_mc_bedroom_sunset_lights at bg with fade
    "Burned out from Emporia hunting and mermaid conspiracies that I got lost in after that, I idly look through a surf magazine."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(What even was that dumb website?)"
    hide mscmc
    play sound knocking
    pause 0.5
    play sound "audio/sfx/MSC_Sound_Effects/79_door open.mp3"
    show arianna dress grin at centre with dissolve
    "There's a light knock on my door before Arianna opens it."
    "She has a shopping bag hanging off her arm and a huge grin on her face."
    ai "Honey, I'm home!"
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "I can't help the excitement that flutters in my chest and warms my cheeks."
    show arianna dress smile behind mscmc at right1plus
    show mscmc casual_hairdown grin at left1
    mcarianna "How was yoga?"
    ai grin "It felt sooo good and I did some shopping and got coffee and was a total human!"
    hide mscmc
    hide arianna
    "Arianna sets her bag on the ground and kicks her shoes off."
    show arianna dress smile at right1plus
    show mscmc casual_hairdown grin at left1
    mcarianna "What'd you buy?"
    show mscmc smile
    ai grin "Well..."
    ai "I stopped by an art store and though we could have some fun."
    mcarianna grin "Like?"
    hide mscmc
    hide arianna
    "Arianna digs around in the bag and pulls out a tarp that she unfolds and sets on the ground."
    show arianna dress_cu grin_cu at arianna_cu
    ai "I got a bunch of clay!"
    ai "You've got to relax and get out of your head."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "I {i}am{/i} relaxed."
    show arianna dress smile behind mscmc at right1plus
    show mscmc casual_hairdown grin at left1plus
    "I shake the magazine at Arianna for emphasis."
    show mscmc smile
    ai grin "You have this tiny little crease in between your eyebrows."
    mcarianna sad "That's just my face."
    show mscmc smile
    ai embarrassed "Because you're always thinking about stuff!"
    show arianna smile
    mcarianna grin "Are you saying you don't think about things?"
    ai grin "The fact that you're fighting me on it, means you know it's true."
    ai "Find your zen."
    mcarianna "And that zen will be in clay?"
    ai smile "Yes."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna sits down on the tarp and beckons at me to join her."
    ai grin_cu "Don't you want to get dirty with me?"
    hide arianna

    $ menuhideborder = True
    menu ariannas1e5c3:
        "A. You absolutely want to get dirty with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Well, when you put it that way..."
            mcarianna "I guess I could give it a shot."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Yay! I'm going to make an artist out of you."
            "Arianna claps with joy."
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Don't get ahead of yourself."
            show mscmc casual_hairdown smile at left1:
                xoffset 16
            show arianna dress grin behind mscmc at right1plus
            ai "Put your hands out, please."
            show arianna smile
            "She plops a glob of clay into my hands and then closes my fingers around it."
            "The clay is cold and hard, but softens as I roll it around in my hands."
            mcarianna surprised "I think the last time I used clay, I was in grade school."
            ai grin "Did you like art classes?"
            show arianna smile
            mcarianna grin "It was fun because I wasn't getting graded through tests."
            mcarianna sad "But, in some ways, art is harder because there's not one way to do things."
            ai grin "That's what's so great about it. You can make whatever you want."
            hide mscmc
            hide arianna
            "Arianna pulls out her own ball of clay and starts tearing off pieces from it that she rolls out."
            show arianna dress_cu grin_cu at arianna_cu
            ai "I would like to commission a piece. I'm willing to pay a hefty price."
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "I don't make pieces for just anyone. My art is one of a kind."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Then I'll have to think of a one of a kind payment."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "Either my face is red or Arianna just knows what she's doing because she laughs."
            "(If the payment is what I think it would be, I would make a thousand clay sculptures.)"
            mcarianna grin_cu "What should I make?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Whatever."
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "That doesn't help."
            hide mscmc
            "Arianna is busy making a clay turtle. She uses her nail to define the shell."
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(What is the most basic thing to sculpt I can think of?)"
            show mscmc smile_cu
            "A vase seems like an easy enough thing to mould."
            hide mscmc
            "As Arianna hums to herself beside me, I find that the clay is not doing what I want it to."
            "I jam my fingers inside of the vase to fix the opening, but it gets thin enough to tear on the side."
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(Arianna makes it look so easy. I guess this is what she does for a living.)"
            show mscmc grin_cu
            "(But I did want to impress her just a little bit.)"
            hide mscmc
            "I huff out a breath and crush the clay back into a ball."
            show mscmc casual_hairdown basic at left1:
                xoffset 16
            show arianna dress surprised behind mscmc at right1plus
            ai "Why'd you ruin it?"
            mcarianna sad "I ripped it."
            ai smile "I know you're used to being good at things, but this takes time."
            mcarianna "I'm not frustrated."
            ai grin "You have that eyebrow crease."
            show mscmc:
                transform_anchor True ycenter 651 rotate 0
                easein 0.4 rotate 2 xoffset 6 yoffset 6
            "I push Arianna's hand away as she points between my eyebrows."
            show mscmc embarrassed:
                transform_anchor True ycenter 651 rotate 2
                easein 0.3 rotate 0 xoffset 0 yoffset 4
            show arianna:
                easein 0.3 xoffset -100
            "Arianna scoots up against my back and her arms come around either side of me."

            scene arianna_02_s1e5:
                align(0.5, 1.0) transform_anchor True zoom 1.3 xoffset 30
            with fade
            pause 0.3
            show arianna_02_s1e5:
                linear 5.0 yoffset 1200
            pause
            "She leans her head on my shoulder as her hands cover mine."
            ai "Don't be so tense."
            "She guides my thumbs to press into the clay, starting to shape it out."
            "I lean back into her, a sense of security falling over me."
            "(She might just be able to get me into pottery.)"
            window hide
            show arianna_02_s1e5:
                linear 4.0 yoffset 300
            pause
            "With Arianna, I do manage to make a dinky misshapen vase."
            ai "It's perfect."

            scene bg msc_mc_bedroom_sunset_lights at bg
            show arianna dress_cu grin_cu at arianna_cu
            with fade
            ai "Art was always appealing to me because I could make whatever I wanted."
            ai "I turn my thoughts and ideas into real things."
            show arianna dress grin at centre:
                xoffset 30
            show mscmc casual_hairdown embarrassed at left1:
                xoffset 30
            "Arianna's hands are still around mine, her cheek so close to mine."
            "I'm sure she can feel the way my heart is pounding."
            show arianna smile
            mcarianna grin "It's fun. Thanks for buying all this."
            ai grin "We'll have another clay date soon."
            hide arianna
            hide mscmc
            "Arianna does finally pull away from me, taking her warmth with her as she sets my vase on the nightstand to dry."
            show arianna dress_cu grin_cu at arianna_cu
            ai "Ready to clean up?"
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Yep."

        "B. Art is...hard.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            "(Any kind of art has never been my forté.)"
            show arianna dress smile behind mscmc at right1plus
            show mscmc casual_hairdown grin at left1plus
            mcarianna "I think I'll just watch the master work."
            ai sad "You don't want to try it?"
            show arianna smile
            mcarianna smile "Nah, I'm fine just watching."
            ai grin "Alright, but one of these days I am going to get you to make something."
            show arianna smile
            mcarianna grin "Sure."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with dissolve
    play sound phone_ringing
    "With the clay and tarp finally put away, we're getting ready to settle in for the night when my phone rings."
    "Phil" "Hi, [genericfn], it's Phil again calling about your potential sponsorship with our company."
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Hey, I got all of that bad rep stuff sorted, so that won't be a problem anymore."
    hide mscmc
    "Phil" "We appreciate you getting on that so quickly, but I'm calling about your recent videos."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Oh, okay."
    hide mscmc
    "Phil" """
    We think you've got the right idea, but your content doesn't stand out enough.

    We need to see why you're different.

    From here on out, we're going to need to see something that makes you stand out or we won't be able to move forward with you.
    """
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Sure, yeah. Of course. I understand."
    hide mscmc
    "Phil" "Thank you and we look forward to seeing what you have to offer. Have a good night."
    show arianna dress basic at right1plus
    show mscmc casual_hairdown sad at left1
    ai "You okay?"
    show arianna surprised
    mcarianna "I feel like I'm not gonna get this sponsorship."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
