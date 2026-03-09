label arianna_season2_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_night at bg
    play music mschappytimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna's asking me to join the mer resistance with her...I can do this!)"
    mcarianna grin_cu "Hell yeah, I'm in!"
    hide mscmc
    show arianna dress grin at left2
    show neptria casual basic at right3
    "Arianna beams at me and Neptria nods her head."
    ai "I knew you would be!"
    nt smile "I gotta get going. I'll see you two later."
    show neptria basic:
        linear 0.5 xoffset 100 alpha 0.0
    pause 0.6

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show arianna dress_cu grin_cu at arianna_cu:
        transform_anchor True
        zoom 0.95 alpha 0.5
        pause 0.1
        linear 0.4 zoom 1.0 alpha 1.0
    pause 0.5
    "As Neptria walks out the door, Arianna engulfs me in a hug."
    ai embarrassed_cu "I wouldn't want to do this with anyone else."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "Her arms tighten around me and I let myself bury my face into her shoulder."
    "(I love how I fit into her arms.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "When she pulls back, she's grinning even harder."
    ai "You know, if you're going to be working with me, we're gonna be working underwater."
    ai embarrassed_cu "Want to try out the magic shell that lets you talk and breathe under the surface?"
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "More than anything."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "We can do so much now that you have that!"
    ai embarrassed_cu "Oh! You can finally come inside my studio!"

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    scene bg msc_labeach_night at bg with clockwise_wipe
    "Arianna and I go to the beach and she leads me into the water by the hand."
    show arianna bikini smile at right1
    show mscmc bikini_hairdown embarrassed at left1plus
    mcarianna "How does this work exactly?"
    show mscmc surprised
    "I hold the shell up, flipping it over in my hands."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(Doesn't look like it has an on/off button.)"
    show arianna bikini grin behind mscmc at right1
    show mscmc bikini_hairdown basic at left1plus
    ai "Just keep it on you and it just does its thing when you need it."
    mcarianna surprised "I just...breathe in underwater?"
    show mscmc smile
    ai "Yep!"
    show mscmc grin
    "Arianna nods encouragingly."
    show arianna surprised
    mcarianna sad "It'll work right? I better not breathe in a bunch of water and choke."
    ai grin "It'll be okay. I'm right here. You {i}are{/i} going to breathe in water, but you won't choke."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Arianna's got me, I know she wouldn't let anything happen to me.)"
    show arianna bikini surprised at right1 behind mscmc
    show mscmc bikini_hairdown surprised at left1plus
    ai "It'll probably feel a little uncomfortable at first. You won't be used to breathing water."
    show mscmc smile
    ai smile "It's different."

    stop music fadeout 0.5
    play music mscunderwaterromance fadein 1.0
    scene bg msc_ocean_wide_night at bg with dissolve
    "Arianna dives into and under the water, then waits for me."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Let's do this.)"
    hide mscmc
    $ wavy_transition("bg msc_ocean_wide_night", "bg msc_underwater_night")
    scene bg msc_underwater_night at bg with dissolve
    show arianna siren grin at centre:
        zoom 0.75 alpha 0.75 xoffset 200 yoffset 80
        parallel:
            easein_back 0.4 yoffset 20
        parallel:
            easeout_circ 0.4 xoffset 100
        parallel:
            linear 0.4 alpha 1.0
    pause 0.2
    "I dip my head under the water and find Arianna in full mer glory, lounging on the sand at the bottom, smiling up at me."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Just like breathing. Except, it's water.)"
    hide mscmc
    "I have to fight against every instinct I have to suck in a breath of water."

    scene bg msc_ocean_wide_night at bg with wipedowndissolve
    show mscmc bikini_hairdown angry at left1:
        xoffset -200 yoffset 220 xoffset -80
        pause 0.1
        parallel:
            easein_back 0.4 yoffset 140
        parallel:
            easeout_circ 0.4 xoffset 0
    "I surge back up, coughing."
    show mscmc sad
    show arianna siren sad at right1plus behind mscmc:
        xoffset 100 yoffset 250 alpha 0.4
        pause 0.1
        parallel:
            easein_back 0.4 yoffset 180
        parallel:
            easeout_circ 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    ai "Hey, it's okay! It's okay!"
    "Arianna rests a hand on my shoulder."
    show mscmc sleep
    ai smile "Don't overthink it. It's just breathing. You're doing it right now."
    show mscmc sad
    ai grin "Just breathe. The magic will work. I promise."
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu:
        yoffset 0
    "(I didn't drown just now, so I guess it {i}did{/i} work.)"
    show arianna siren smile at right1plus behind mscmc:
        yoffset 180
    show mscmc bikini_hairdown smile at left1:
        yoffset 140
    mcarianna "Okay."
    ai grin "Ready?"
    hide mscmc
    hide arianna

    $ wavy_transition("bg msc_ocean_wide_night", "bg msc_underwater_night")
    scene bg msc_underwater_night at bg with dissolve
    "I nod as the both of us go back under."
    "I quickly and sharply breathe through my nose, inhaling the water."
    show mscmc bikini_hairdown_cu sleep_cu at mscmc_cu
    "(Breathe.)"
    "The sensation of the water is somewhat uncomfortable at first, but I let it in."
    show mscmc smile_cu
    "(Stay calm. Arianna's right here. She won't let anything hurt me.)"
    hide mscmc
    "I find my peace and breathe out."
    show arianna siren_cu grin_cu at arianna_cu
    ai "You're doing great."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I can talk underwater with this shell too!)"
    show arianna siren smile behind mscmc at right1plus
    show mscmc bikini_hairdown surprised at left1plus
    mcarianna "It feels...weird."
    show mscmc grin
    ai sad "Do you feel okay?"
    show arianna grin
    mcarianna "I think so."
    show mscmc surprised
    ai "Feeling up for an art studio tour?"
    show arianna embarrassed
    mcarianna grin "Yes!"

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    scene bg msc_underwater_ship_night at bg with dissolve
    "Arianna takes me to her studio and I feel invigorated."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I don't have to go up for air ever! How awesome is that?!)"
    hide mscmc
    show arianna siren grin at centre
    "Arianna swims through the hole in the side of the ship and beckons to me."
    ai embarrassed "Welcome, welcome to where the art happens!"
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    mcarianna "I can't believe I'm finally here!"
    hide mscmc

    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    $ wavy_transition("bg msc_underwater_ship_night", "bg msc_arianna_studio_night_lightson")
    scene bg msc_arianna_studio_night_lightson at bg with dissolve
    "Arianna waits for me to swim in and then she sweeps her arm over the studio."
    "Now that I'm inside, I can really see all of the sculptures and art she does. The space is incredible."
    "It's a little cluttered, but in a wonderful, artsy, Arianna way."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Looks like she's working on a lot of stuff.)"
    show arianna siren embarrassed behind mscmc at right2
    show mscmc bikini_hairdown smile at left1
    ai "What do you think?"
    mcarianna grin "It feels like you."
    "Arianna looks down at her nails and picks at her thumb."
    show mscmc embarrassed
    ai "It feels special to have you here."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "Arianna reaches out and laces her fingers through mine."
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    ai "I can give you a {i}personal{/i} tour if you'd like?"
    hide arianna

    $ menuhideborder = True
    menu ariannas2e2c1:
        "A. Personal studio tour with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show arianna siren embarrassed behind mscmc at right2
            show mscmc bikini_hairdown grin at left1
            mcarianna "I didn't come all this way not to get a personal tour!"
            show mscmc embarrassed
            show arianna grin
            "Arianna claps her hands together with a grin."
            ai embarrassed "No better way to test out your cool new shell."
            show mscmc grin
            ai grin "Welcome to the magic item club."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(A mermaid and a magic shell. How is this my life?)"
            show arianna siren grin behind mscmc at right2:
                pause 0.1
                easein 0.3 right1 xoffset -50
                easein_back 0.4 right1plus xoffset 10
            show mscmc bikini_hairdown smile at left1:
                xoffset -20
                pause 0.4
                easein_back 0.4 xoffset 30
            "Arianna winks at me and then pulls me to the centre of the studio."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(I love how she casually holds my hand all the time.)"
            "(Of course, I wouldn't mind if something {i}more{/i} happened...)"
            show arianna siren embarrassed behind mscmc at right2
            show mscmc bikini_hairdown embarrassed at left1
            ai "So, obviously, this is where I do all my work. It's a little messy."
            mcarianna grin "I don't mind. It feels real."
            show mscmc surprised
            ai grin "This place is outside the city limits, so I can escape detection."
            show mscmc smile
            ai sleep "You know, from the government that hates magic and art."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(A place where she can be herself.)"
            show arianna siren smile behind mscmc at right2
            show mscmc bikini_hairdown smile at left1
            "Arianna moves a few stray pieces of metal into a more condensed pile on one of the tables."
            show mscmc embarrassed
            "She's delicate with the pieces and I can't help but focus on the beauty of her long fingers."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I wouldn't mind if she laid me down on this table right now and...)"
            show mscmc sad_cu
            "(Keep the thoughs PG, [genericfn]!)"
            show arianna siren smile behind mscmc at right2
            show mscmc bikini_hairdown embarrassed at left1
            "Arianna leans bak on the table."
            ai grin "Since I'm off the radar here, I can be free to make whatever I want."
            show arianna smile
            mcarianna grin "How did you find this place? It's kind of perfect."
            show mscmc smile
            ai grin "It is, isn't it?"
            "There's a fond look in her eyes."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(She really loves this place. I can tell it means a lot to her.)"
            show arianna siren grin behind mscmc at right2
            show mscmc bikini_hairdown smile at left1
            ai "I knew I needed some kind of secret place to make my art."
            show mscmc basic
            ai sad "It's just too dicey in the city with how the government is cracking down."
            show mscmc surprised
            show arianna grin
            "Arianna puts a hand over her mouth and laughs."
            show mscmc smile
            ai grin "It's actually kind of a funny story how I found it."
            ai "I was out looking for anything I could use for a new sculpture."
            show mscmc grin
            ai embarrassed "And then I realized I'd lost my bracelet."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(I need to get her one of those beep-y things you can put on your keys.)"
            show arianna siren embarrassed behind mscmc at right2
            show mscmc bikini_hairdown grin at left1
            mcarianna "Now I know why your grandma was giving you a hard time about losing stuff."
            show mscmc surprised
            ai grin "A fish swam by and it had my bracelet in its mouth!"
            show mscmc grin
            ai "So I tried to catch it! I followed it for, like, two hours."
            show arianna surprised
            "Arianna uses her hands to act out the fish swimming."
            show mscmc smile
            ai sad "I mean, I didn't want the fish to choke, but I also needed my bracelet back."
            show mscmc grin
            ai grin "And then it swam here. It felt like destiny when I saw this place."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(Maybe it really was.)"
            show arianna siren basic behind mscmc at right2
            show mscmc bikini_hairdown grin at left1
            mcarianna "Did you get your bracelet back?"
            ai grin "No, {i}but{/i} I didn't care!"
            show mscmc smile
            "Arianna throws her arms up, barely missing the table with her elbows."
            ai "I put so much time into fixing this place up and it felt so great."
            ai "It felt like I finally found a piece of myself that I was missing."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I love seeing her like this, totally comfortable, in her element, truly at home. I want to be part of home for her.)"
            show arianna siren grin behind mscmc at right2
            show mscmc bikini_hairdown embarrassed at left1
            ai "This is where I belong."
            "My heart swells as I watch her smile."
            mcarianna grin "You know, I felt the same about moving to the sea, I mean Los Angeles--a place of belonging."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(Moving from the midwest to a place like this was hard, but I loved it.)"
            show arianna siren basic behind mscmc at right2
            show mscmc bikini_hairdown grin at left1
            mcarianna "I knew I wanted to pursue surfing and that was all that mattered."
            show arianna grin
            mcarianna "Like, I just knew that this is where I'm supposed to be."
            show arianna smile
            "I run my fingers along the table."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(And now I couldn't be happier because now I'm here, with her.)"
            show arianna siren grin behind mscmc at right2
            show mscmc bikini_hairdown embarrassed at left1
            "Arianna puts her hand over mine on the table."
            show mscmc smile
            ai "We've found our places."
            mcarianna grin "Yeah."
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            "She holds my gaze, her smile growing."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Uggggghhh. I want to kiss her. Like, {i}so badly{/i}.)"
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "Can I show you some of my projects?"
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcarianna "It's a tour after all."
            show mscmc embarrassed_cu
            "(And another moment passes where I don't have the guts to make an actual move.)"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            "With my hand in hers, Arianna swims us over to the side of the studio."
            show arianna siren grin behind mscmc at right1
            show mscmc bikini_hairdown smile at left1
            ai "I made this for my grandma, it's her birthday soon."
            "Arianna points to a piece of a mermaid that almost looks like it's sparkling."
            "Then she gestures to a human looking statue."
            ai "I used to love people-watching humans on beaches."
            ai "Thinking of the stories of their lives."
            mcarianna embarrassed "These are amazing pieces."
            show arianna embarrassed:
                ease 0.4 xoffset 0 knot 5 knot -10 knot 0
            show mscmc grin:
                pause 0.1
                easein_back 0.3 xoffset -20
            "Arianna bumps herself into my side."
            show mscmc embarrassed
            ai "There is one particular human I would love to make a sculpture of."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Would she really make a sculpture of me? I would love to see how I look to Arianna.)"
            mcarianna "Am I that human?"
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu
            ai "Maybe."

        "B. I'd rather go back to the surface.":
            $ menuhideborder = False
            show arianna siren basic at right1
            show mscmc bikini_hairdown sad at left2
            mcarianna "I really want to, but honestly...I'm so tired."
            show arianna sad
            "Arianna frowns slightly, but then she chuckles."
            show mscmc smile
            ai smile "Breathing water can be a lot. It took me a bit to get used to air when I first tried it."

    window hide
    scene arianna_05_s2e2 at bg:
        align (1.0, 1.0) yoffset 130
    with fade
    pause 0.3
    show arianna_05_s2e2 at bg:
        transform_anchor True
        linear 5.0 xalign 0.0 yalign 0.0 yoffset -150
    pause 5.5
    mcarianna "Thank you for bringing me here."
    "Arianna brushes my hair away from my face, a smile resting on her lips, her face suddenly very close to mine."
    ai "Of course. I really wanted you to see it."
    "(I feel like this is a big step for us. I can be a part of her life down here now too.)"
    "Her hair drifts gently behind her in the current as we stare into each other's eyes. Her fingers gently resting against my jaw."
    "(She looks beautiful in the water. In her element. I want to be down here with her always. It feels right.)"

    scene bg msc_arianna_studio_night_lightson at bg
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    with fade
    "(I can't stay down here forever, though.)"
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    ai "I know I have my tail back but would it be okay if I kept staying with you at your place?"
    ai sad_cu "It would be safer for me to stay on land since I'm working on the resistance project."
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(I don't mind having her near me.)"
    hide mscmc
    show arianna siren_cu embarrassed_cu at arianna_cu
    "Arianna puts her hand to her necklace as her cheeks redden."
    ai "I also just...like spending time with you."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Maybe she feels the same way about me as I do about her.)"
    mcarianna grin_cu "You can stay as long as you need or want."

    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    scene bg msc_surf_shop_day at bg with clockwise_wipe
    "The next day, Trina and I are both at the shop as Trina counts the money in the register."
    show mscmc casual_hairup grin at left1
    show trina casual basic at right2
    mcarianna "How were the bars last night? You were practically running out the door."
    hide trina
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(Which was actually a good thing considering Neptria showed up like five minutes later.)"
    show mscmc casual_hairup smile at left1
    show trina casual smile at right2
    so "Ah, I ended up just going to Jerry's. Nothing beats his mojitos."
    mcarianna grin "True."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    show mscmc basic
    so basic "So."
    mcarianna surprised "What?"
    show mscmc basic
    "Trina shrugs and glances up at me."
    so smile "How're you and Arianna?"
    hide trina
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(How {i}are{/i} we? We're the same, but also different after Mia's?)"
    show mscmc embarrassed_cu
    "(But nothing's really happening outside of hugging and holding hands!)"
    show mscmc casual_hairup grin at left1
    show trina casual basic at right2
    mcarianna "We're good."
    so "Yeah?"
    mcarianna smile "Mhm."
    "Trina fixes me with a look that tells me she's not saying something."
    mcarianna grin "Arianna's actually gonna be staying for a while."
    show mscmc basic
    "Trina pauses with the cash in her hands and raises a questioning eyebrow at me."
    show mscmc embarrassed
    so smile "So, you're dating?"
    show trina basic
    mcarianna surprised "No! I'm just...helping her out."
    hide trina
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(Not that I could tell Trina that I'm helping Arianna out with a mermaid resistance.)"
    show mscmc casual_hairup embarrassed at left1
    show trina casual smile at right2
    so "Riiiiight, by letting her sleep in your bed."
    hide trina
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(It does sound pretty intimate when she puts it that way.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e2c2:
        "A. It's not what you think.":
            $ menuhideborder = False
            show mscmc casual_hairup surprised at left1
            show trina casual basic at right2
            mcarianna "Look, it's not what you think, okay?"
            show mscmc embarrassed
            so smile "It's exactly what I think. Don't try to weasel out of this one."
            mcarianna grin "I'm not weaseling."

        "B. Because we're friends!":
            $ menuhideborder = False
            show mscmc casual_hairup grin at left1
            show trina casual basic at right2
            mcarianna "Well, yeah, but we're friends. That's normal."
            show trina sleep
            mcarianna "Friends share beds all the time."
            show mscmc basic
            so basic "We've slept in the same bed before, but it's different."
            show mscmc embarrassed
            so "You like her."
            hide trina
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Got me there, Trina.)"

        "C. Uh...yeah.":
            $ menuhideborder = False
            show mscmc casual_hairup grin at left1
            show trina casual smile at right2
            mcarianna "Yeah..."
            show mscmc smile
            so "Mhm."
            show trina basic
            mcarianna grin "I know what it looks like."
            show mscmc embarrassed
            so "Mhmmmm."

    show mscmc casual_hairup smile at left1
    show trina casual basic at right2
    "Trina shuffles the money in her hands and sets it down."
    show mscmc surprised
    so "Is she splitting rent with you?"
    mcarianna basic "No, I'm not asking her."
    show mscmc surprised
    so "I don't want her to mooch off of you."
    mcarianna sad "Arianna isn't a mooch."
    show mscmc basic
    "Trina clicks her tongue."
    show mscmc sleep
    so smile "She at least needs to pitch in for utilities."
    hide trina
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(Trina's looking out for me, I get why she's pushing this.)"
    show mscmc casual_hairup smile at left1
    show trina casual smile at right2
    mcarianna "Fine. I'll ask her."
    hide mscmc
    hide trina

    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show arianna dress grin:
        xanchor 0.5 yanchor 0.44 xpos 0.6 ypos 1.0 transform_anchor True zoom 0.95 alpha 0.0
        linear 0.4 zoom 1.0 alpha 1.0
    "The shop bell rings and Arianna walks in with a smoothie and a grin."
    hide arianna
    show arianna dress_cu grin_cu at arianna_cu
    ai "Hey!"
    hide arianna
    show mscmc casual_hairup smile at left1
    show trina casual basic at right2
    "Trina eyes me."
    hide trina
    show mscmc casual_hairup_cu basic_cu at mscmc_cu
    "(I'm gonna have to ask Arianna right now, aren't I?)"
    show arianna dress grin at right2 behind mscmc
    show mscmc casual_hairup grin at left1plus
    mcarianna "How was yoga?"
    ai "Fantastic and I tried that new smoothie place on the boardwalk."
    show mscmc smile
    "Arianna presents the smoothie like it's a prize she just won."
    show arianna smile
    mcarianna surprised "Uh, Arianna, so rent's coming up soon...which I totally have!"
    hide mscmc
    hide arianna
    show trina casual basic at centre
    "I can see Trina nodding out of the corner of my eye as she looks back to her money."
    hide trina
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(This is for you, Trina.)"
    show arianna dress smile at right2 behind mscmc
    show mscmc casual_hairup smile at left1plus
    mcarianna "But, uh, would you mind helping to pay for utilities? You know, since you're staying."
    ai grin "Of course I don't mind!"
    ai "I'm actually going to sell pieces at some farmers' markets."
    hide mscmc
    hide arianna
    show trina casual basic at centre
    "Trina nods in contentment."
    so smile "I think that's a great idea!"
    hide trina
    show arianna dress grin at centre
    ai "I actually got a spot in one today."
    hide arianna
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(That's awesome!)"
    show arianna dress grin at right2 behind mscmc
    show mscmc casual_hairup embarrassed at left1plus
    ai "Want to come with, [genericfn]?"
    show arianna embarrassed
    "Arianna bats her lashes at me with an alluring smirk."
    mcarianna sad "It's my shift. I have to work."
    show mscmc surprised
    hide arianna
    show trina casual smile at right2
    so "No you don't."
    show mscmc grin
    "Trina closes the cash box and pats me on the shoulder."
    so basic "I'll watch the shop. Go have fun!"
    hide trina
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(Trina, I love you!)"
    show mscmc casual_hairup grin at left1
    show trina casual smile at right2
    mcarianna "You don't mind?"
    so "I was gonna be here anyways."
    hide mscmc
    hide trina
    show arianna dress_cu grin_cu at arianna_cu
    ai "Trina, you're the best!"
    hide arianna
    show trina casual_cu smile_cu at trina_cu
    so "I know I am."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_siren_park_day at bg with fade
    "Arianna and I go to the market and set up a table I borrowed from Trina."
    show arianna dress smile at right1plus
    show mscmc jacket_hairup grin at left1plus
    mcarianna "I think this is a really cool idea. I'm proud of you."
    ai embarrassed "Really?"
    show arianna grin
    "Arianna puts her hands to her mouth, a smile creeping out behind."
    hide arianna
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(She is so damn cute.)"
    show arianna dress grin at right1plus behind mscmc
    show mscmc jacket_hairup grin at left1plus
    mcarianna "Totally."
    show mscmc smile
    show arianna smile
    "Arianna adjusts one of the smaller sculptures on the table, facing it forward."
    mcarianna grin "Have you ever sold your stuff like this before?"
    ai grin "There's a first time for everything."
    hide mscmc
    hide arianna
    "Arianna ushers me towards one of the chairs behind the table and I take the seat."
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(This is actually a really good idea. It's also a graet way for Arianna to get her stuff out there.)"
    show arianna dress grin at right1plus behind mscmc
    show mscmc jacket_hairup grin at left1plus
    mcarianna "Excited?"
    ai "I feel like a real working woman."
    mcarianna "Self-employment at its finest."
    hide mscmc
    hide arianna
    "An older couple of two women pause at the table, both of them with short cropped hair."
    show arianna dress grin at right1plus
    show mscmc jacket_hairup smile at left1plus
    ai "Hi! How are you guys doing today?"
    hide arianna
    hide mscmc
    "Shorter Woman" "It's a lovely day for the market, isn't it?"
    show arianna dress grin at right1plus
    show mscmc jacket_hairup smile at left1plus
    ai "It is!"
    hide arianna
    hide mscmc
    "The couple lets go of each other's hands as they examine Arianna's art."
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(Could that be Arianna and me one day?)"
    hide mscmc
    "Taller Woman" "These pieces are wonderful. You two make these?"
    show arianna dress embarrassed at right1plus
    show mscmc jacket_hairup grin at left1plus
    mcarianna "It's all her. I'm just moral support today."
    show mscmc embarrassed
    "Arianna pinches my cheek."
    hide arianna
    hide mscmc
    "Shorter Woman" "Aren't you two just adorable?"
    "The woman pats her partner on the back and smiles."
    "Shorter Woman" "Reminds me of us when we were younger."
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(They think we're a couple?)"
    show arianna dress embarrassed at right1plus behind mscmc
    show mscmc jacket_hairup embarrassed at left1plus
    "Arianna and I both share the same quiet embarrassed laugh."
    hide arianna
    hide mscmc
    "Taller Woman" "We're going to check out the other booths, but we'll be back around."
    show arianna dress grin at right1plus
    show mscmc jacket_hairup smile at left1plus
    ai "I look forward to it."
    hide arianna
    hide mscmc
    "The couple leaves hand-in-hand."
    show arianna dress smile at right1plus
    show mscmc jacket_hairup smile at left1plus
    "Arianna leans back in her chair and looks behind me at the soap booth next to us."
    ai grin "Those smell so good."
    ai "Are you a soap person?"
    mcarianna grin "I mean, I use it."
    ai "I really love smells and artisanal soap."
    ai "They're so fancy."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna leans into my ear, her breath hot on my skin."
    ai "Mermaids have special bathing rituals, you know."
    hide arianna
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "The tone of her voice alone is enough to short circuit my brain."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Will you pick a soap out for me?"
    show arianna embarrassed_cu
    "Arianna leans her face into my neck and breathes in deeply with a giggle."
    ai grin_cu "And I want to pick one out for you."
    ai "I want us to pick out soaps that remind us of each other."
    hide arianna

    $ menuhideborder = True
    menu ariannas2e2c3:
        "A. Yes, pick a scent for Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show arianna dress_cu grin_cu:
                align(0.5, 0.5) yoffset 50 transform_anchor True
                linear 0.5 zoom 0.95 alpha 0.0
            pause 0.5
            "Arianna slides out behind me, her hand brushing along my back."
            hide arianna
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(Definitely don't think about taking a bath with Arianna.)"
            "(But wow! Would that be something!)"
            hide mscmc
            show arianna dress grin at centre
            "Arianna waves lightly to the burly man running the soap booth."
            ai "I told you I would come for your soaps."
            hide arianna
            "Soap Guy" "I have many to choose from."
            "The man welcomes us over with beckoning hands."
            "Soap Guy" "What are you ladies thinking about? A gentler scent? Or something spicier?"
            show arianna dress smile at right1plus
            show mscmc jacket_hairup smile at left1plus
            "Arianna looks at me with a raised brow."
            ai grin "We don't know yet. We're picking them out for each other."
            show arianna smile
            mcarianna grin "What kind of soap do you like, Arianna?"
            show mscmc smile
            ai grin "What makes you think of me? I want you to choose one."
            show arianna embarrassed
            "Arianna flips her hair over her shoulder, presenting herself to me."
            hide arianna
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(A lot of things make me think of her.)"
            hide mscmc
            "I lean over the table to get a better look at the different colored soap blocks."
            "They all have little scent tags on them."
            "Soap Guy" "There are a few that are very popular amongst couples."
            "Soap Guy" "Lavender and rose creates a very soothing atmosphere."
            show arianna dress smile at right1plus
            show mscmc jacket_hairup surprised at left1plus
            mcarianna "Oh, we're not-!"
            ai grin "Lavender and rose?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna loops her arm through mine and winks at me."
            hide arianna
            "The man hands the soap to Arianna and she holds it up to her nose."
            show arianna dress smile at right1plus
            show mscmc jacket_hairup smile at left1plus
            ai "Mmmm. It does smell really good."
            "She holds it out for me."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "What do you think, {i}honey{/i}?"
            hide arianna
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "My mouth goes dry at the way that word slips out of her lips."
            show mscmc embarrassed_cu
            "(Oh, is she...? Are we pretending to be...a couple?)"
            show mscmc grin_cu
            "(Cool. Yeah. This is fine.)"
            show arianna dress grin at right1plus behind mscmc
            show mscmc jacket_hairup smile at left1plus
            "I try to focus on the scent and not the way my heart is beating in my throat."
            mcarianna grin "I like it."
            ai "Hmm, what about this?"
            show mscmc smile
            show arianna smile
            "Arianna sets that soap down as she picks up a lemongrass scented one."
            ai grin "Oh, I like this one for you."
            hide mscmc
            hide arianna
            "Soap Guy" "Lemongrass is a popular one."
            "Soap Guy" "We also have lemongrass and lavender."
            show arianna dress smile at right1plus
            show mscmc jacket_hairup smile at left1plus
            "He hands the soap to Arianna and she nods as she smells it."
            ai grin "I think this might be it."
            mcarianna grin "For me?"
            ai "It reminds me of you. It makes me feel all warm inside."
            hide arianna
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(I need to get home and wash myself with this soap.)"
            show arianna dress smile at right1plus
            show mscmc jacket_hairup surprised at left1plus
            mcarianna "I still need one for you."
            show mscmc smile
            ai embarrassed "I can be hard to pin down."
            mcarianna grin "We'll see."
            hide mscmc
            hide arianna
            "I rove my eyes over all of the choices."
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Black raspberry vanilla?)"
            "(Or maybe almond?)"
            show mscmc embarrassed_cu
            "Deciding what soap makes me think of Arianna is a little harder than I thought it would be."
            show mscmc surprised_cu
            "(There's so many choices!)"
            show arianna dress embarrassed at right1plus
            show mscmc jacket_hairup basic at left1plus
            ai "You look like you're having a hard time."
            mcarianna grin "Don't rush perfection."
            hide mscmc
            hide arianna
            "Soap Guy" "Picking the right scent can be difficult, but you'll know when you find it."
            "Soap Guy" "They choose us."
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna nods, eating up every one of his words."
            hide arianna
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(I didn't realize the soap business was so hardcore.)"
            hide mscmc
            "I pick up a light green bar of soap and take a deep whiff."
            show mscmc jacket_hairup_cu smile_cu at mscmc_cu
            "(Cucumber melon. It makes me think of summer.)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna watches me closely like she's trying to read my expression."
            hide arianna
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(A breath of fresh air.)"
            show arianna dress smile at right1plus
            show mscmc jacket_hairup grin at left1plus
            mcarianna "I think this one would suit you."
            ai grin "Really?"
            show arianna smile
            mcarianna "Really."
            show mscmc smile
            "I set the soap down so that I can dig my wallet out."
            mcarianna grin "We'll take these two."
            hide mscmc
            hide arianna
            "Soap Guy" "Very good choices."
            show arianna dress sad at right1plus
            show mscmc jacket_hairup smile at left1plus
            ai "I was gonna buy them."
            mcarianna grin "Beat you to it."
            show arianna embarrassed
            "I grin at Arianna and I see a red tint forming on her cheeks."
            hide arianna
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(I'll buy her all the soap she wants.)"
            show arianna dress grin at right1plus
            show mscmc jacket_hairup grin at left1plus
            ai "Thank you."

        "B. Thinking about bathing with her is too much.":
            $ menuhideborder = False
            show mscmc jacket_hairup_cu sad_cu at mscmc_cu
            "I'm far too frazzled from her implication to be able to pick soaps out with her."
            show arianna dress basic at right1plus behind mscmc
            show mscmc jacket_hairup sad at left1plus
            mcarianna "Uh, I've got a lot of soap at home we can pick from."
            show arianna sad
            "Arianna huffs."
            ai "You use generic brand body wash."
            mcarianna "It gets the job done."
            show mscmc smile
            ai smile "I guess. I do still love the way you smell."

    hide mscmc
    hide arianna

    play sound "audio/sfx/bubbles_003_6397.mp3" loop
    stop music fadeout 0.5
    play music msctense fadein 1.0
    "Arianna jumps as her shellphone starts making bubbling noises."
    stop sound fadeout 0.5
    show arianna dress basic at right1plus
    show mscmc jacket_hairup basic at left1plus
    "She picks it up with a finger held up to me to hold on."
    ai surprised "Hello?"
    show arianna sad
    "As the phone call continues, Arianna's face turns down into a frown."
    hide arianna
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(It doesn't seem like good news.)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairup basic at left1plus
    ai "Yeah...okay."
    "She puts her phone down as the call ends and runs a hand through her hair."
    ai "Remember that guy Casper in the video Neptria showed us?"
    hide arianna
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(He wwas that extremist destroying the sculptures.)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairup basic at left1plus
    ai "Well, the resistance got a tip as to where he is. They want to set up a meeting with him."
    "Arianna stands and begins to pack her things up."
    hide arianna
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Right now?!)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairup surprised at left1plus
    mcarianna "Wait, hold on, you're going to meet him alone?"
    ai "My grandma will be there."
    mcarianna sad "He sounds...I don't know. What if he's dangerous?"
    "I put a hand on Arianna's arm, stopping her."
    ai smile "I'll be fine."
    show arianna basic
    mcarianna "You said that about Mia."
    hide arianna
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(I'm not going to lose her again.)"
    show arianna dress basic at right1plus behind mscmc
    show mscmc jacket_hairup sad at left1plus
    "Arianna puts her hand over mine."
    ai sad "I'll come back to you, I promise."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
