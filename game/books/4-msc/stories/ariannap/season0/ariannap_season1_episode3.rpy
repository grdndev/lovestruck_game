label ariannap_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_ocean_wide_day at bg
    play music mscarianna

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show surfboard back at centre:
        transform_anchor True zoom 0.8
    show mscmc bikini_hairup basic at left2:
        yoffset 100
    "I pull myself back onto my board so I can at least feel like I practied today."
    show mscmc:
        parallel:
            easeout_circ 0.4 centre
            easein 0.3 xoffset 30
        parallel:
            easein 0.4 yoffset 50
    mcariannaprev "How do you want to go about this? It's your art."
    show mscmc at left3
    show surfboard at left3
    show arianna siren sleep at right2:
        yoffset 100
    "Arianna shrugs and leans over my board, her chin resting on her hand."
    ai basic "I'm fine with winging it."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0 xoffset 0
    "(There's too much at stake for that!)"
    show surfboard back at left3:
        zoom 0.8
    show mscmc bikini_hairup sad at left3:
        yoffset 50
    show arianna siren basic at right2:
        yoffset 100
    mcariannaprev "Arianna, we need a plan."
    show mscmc basic
    show arianna grin
    "Arianna goes quiet and just when I feel like she's thinking about it, she grins."
    hide arianna
    show surfboard back_cu at centre:
        zoom 1.0
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
        yoffset 0 xoffset 0
    "(That is definitely not the look of someone who's planning...)"
    show surfboard back at left3:
        zoom 0.8 xoffset -20
    show mscmc bikini_hairup basic at left3:
        yoffset 50
    show arianna siren grin at right2:
        yoffset 100
    ai "Sure, but I really want to show you something first."
    hide surfboard
    hide mscmc
    show arianna siren grin at left7:
        transform_anchor True rotate 0 xoffset 10
        rotate 5
        pause 0.1
        parallel:
            easein 0.6 centre
        parallel:
            pause 0.4
            linear 0.2 rotate 3 xoffset 5
    "Now swimming towards shore, Arianna beckons me with a hand over her shoulder."
    show arianna at centre:
        linear 0.3 rotate 0 xoffset 0
    ai "Come here!"
    show arianna siren_cu smile_cu at arianna_cu:
        yoffset 0
    "She flips over to do a slow backstroke, her eyes trained on me."
    hide arianna
    show surfboard back_cu at centre
    show mscmc bikini_hairup_cu sad_cu at mscmc_cu
    "(Shouldn't she be taking this more seriously?)"
    hide surfboard
    hide mscmc
    show arianna siren smile at centre:
        yoffset 100
    "I paddle after her and laugh as Arianna raises her brows at me."
    hide arianna
    show surfboard back_cu at centre
    show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu
    "(But, I won't deny how enticing it is to watch her swim away.)"

    scene bg msc_labeach_day at bg with dissolve

    "When the water is shallow, I stand up with Arianna swimming a circle around me."
    show arianna siren smile at centre:
        transform_anchor True zoom 0.46 yoffset 50
    "Then she lays on the shore with a wink, an arm draped over her tail."
    show arianna at right3
    show mscmc bikini_hairup grin at centre:
        transform_anchor True zoom 0.43 yoffset 80
    mcariannaprev "Was that it?"
    show mscmc surprised
    ai "Not quite."
    show mscmc basic
    show sparkle_focused behind arianna:
        xoffset 220
    "A hand up, Arianan rubs a finger over her thumb ring."
    show arianna dress smile with dissolve
    "There's suddenly a pair of very human legs where Arianna's tail had been"
    hide arianna
    hide sparkle_focused
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu:
        zoom 1.0 yoffset 0
    "{i}(No way!){/i}"
    show mscmc bikini_hairup surprised at left2
    show arianna dress smile at right3
    "I kneel in the sand next to her, my eyes roving over her slender legs."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "I glance up to see Arianna regarding me, a hint of a smile there."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show mscmc bikini_hairup embarrassed at left2
    show arianna dress smile at right3
    "Heat creeps up my face and I avert my eyes."
    mcariannaprev grin "How'd you do that?"
    show mscmc smile
    show arianna sleep
    "Arianna dramatically puts her hand out."
    ai grin "{i}Magic{/i}."
    ai "It's my thumb ring."
    show mscmc surprised
    "I take her hand and again it's like a wave of static electricity that travels through me."
    hide arianna
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(Her fingers are so long...)"
    show mscmc embarrassed_cu
    "(This is the second time I've touched her hand and I don't want to let it go.)"
    show mscmc bikini_hairup basic at left2
    show arianna dress smile at right3
    "Turning Arianna's hand over, I try to look at the ring from all sides."
    "It looks like a normal ring."
    ai "My grandmother's an old sea witch - she made this for me."
    hide arianna
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(I don't know why I'm surprised.)"
    "(I'm talking to a mermaid for god's sake.)"
    show mscmc bikini_hairup surprised at left2
    show arianna dress smile at right3
    mcariannaprev "A sea witch?"
    show arianna sleep
    "She nods, a fond sigh leaving her lips."
    show mscmc basic
    ai basic "Magic isn't something that's really allowed."
    ai surprised "It's not illegal per se, but I've seen some hefty fines dished out."
    hide arianna
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(I can't believe sea magic is something that's not allowed.)"
    "(This whole scenario is magical on its own.)"
    show mscmc bikini_hairup basic at left2
    show arianna dress basic at right3
    ai "I sadly don't have the gift, but even if they found out about the ring, it'd be destroyed."
    hide arianna
    show mscmc bikini_hairup_cu basic_cu at mscmc_cu
    "(Their legal system doesn't sound too different from ours.)"
    show mscmc bikini_hairup basic at left2
    show arianna dress smile at right3
    ai "And here I am telling a human everything. Guess I'm bad to the bone."
    hide arianna
    hide mscmc

    $ menuhideborder = True
    menu ariannas0e3c1:
        "A. Muse about having a ring.":
            $ menuhideborder = False
            show mscmc bikini_hairup surprised at left2
            show arianna dress smile at right3
            mcariannaprev "Maybe I should get a ring..."
            ai grin "You'd love a tail, huh?"
            "Before I can think of a response, Arianna is moving on."
        "B. Tease her about being bad.":
            $ menuhideborder = False
            show mscmc bikini_hairup smile at left2
            show arianna dress smile at right3
            "I snort, she's anything but."
            mcariannaprev "You're a bonafide criminal."
        "C. Steer her back to planning.":
            $ menuhideborder = False
            show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
            "(Learning about her culture is more than amazing, but...)"
            show mscmc bikini_hairup sad at left2
            show arianna dress smile at right3
            mcariannaprev "Arianna, we need to think about what to do with Hamish."

    show mscmc basic
    ai smile "Right, how should we get my art back? It'll be hard to steal something so big."
    hide arianna
    show mscmc bikini_hairup_cu surprised_cu at mscmc_cu
    "(Steal it? Is that what she's thinking?)"
    show mscmc bikini_hairup surprised at left2
    show arianna dress basic at right3
    mcariannaprev "Wouldn't it be better if you just came forward as the artist?"
    mcariannaprev basic "Discredit Hamish right then and there."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "Arianna pulls her hand back and examines her nails, a distant look in her eyes."
    show mscmc bikini_hairup basic at left2
    show arianna dress sad at right3
    ai "What are we gonna do about your friend's shop?"
    show mscmc sleep
    show arianna basic
    "I blow out a long puff of breath."
    show mscmc basic
    "Hamish is a tiring thought."
    mcariannaprev "I have no idea what to do and we're out of time."
    hide arianna
    show mscmc bikini_hairup_cu basic_cu at mscmc_cu
    "(I don't want Trina to lose the shop, but there's not much we can do.)"
    show mscmc bikini_hairup surprised at left2
    show arianna dress basic at right3
    mcariannaprev "Unless you have a super secret mermaid fund?"
    show mscmc smile
    show arianna smile
    "Arianna laughs, but shakes her head with an apologetic frown."
    ai "That's a negative."
    show mscmc surprised:
        easein 0.4 left1plus
    show arianna surprised behind mscmc:
        easein_back 0.4 right1plus
    "Arianna pushes herself to her feet and puts her arms out to balance her wobbly stance."
    show mscmc basic
    ai smile "Wanna take me to the shop? I've never been to a human store before!"
    hide arianna
    show mscmc bikini_hairup_cu grin_cu at mscmc_cu
    "(It'd be awesome to show Arianna around!)"
    "(Afterall, we're partners in crime now.)"
    show mscmc bikini_hairup grin at left1plus
    show arianna dress smile behind mscmc at right1plus
    mcariannaprev "Yeah, sure thing."
    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    scene bg msc_surf_shop_day at bg with fade
    play sound ["<to 1>audio/sfx/MSC_Sound_Effects/79_door open.mp3","audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"]
    "The doorbell goes off as I step into the shop, Arianna behind me with wide eyes."
    show trina casual smile at centre
    "Trina looks up from a magazine she's reading on the counter and slaps it closed with a gasp."
    hide trina
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Please Trina don't do this...)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress smile at right2
    "I ignore Trina's raised brows and motion to Arianna."
    mcariannaprev smile "Arianna, this is Trina. Trina, Arianna."
    hide mscmc
    show trina casual smile at left3
    ai "It's so nice to meet you-I've heard a lot about you."
    so "I'd say the same, but sometimes this one has a hard time opening up."
    "Trina jabs a thumb in my direction."
    hide trina
    hide arianna

    $ menuhideborder = True
    menu ariannas0e3c2:
        "A. Get embarrassed.":
            $ menuhideborder = False
            show mscmc jacket_hairdown embarrassed at centre
            "I shake my head in an attempt to hide my blush of embarrassment."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(I swear, sometimes Trina is worse than a parent.)"
            hide mscmc
        "B. Be defensive.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I don't want Arianna to feel uncomfortable with Trina's implications.)"
            show mscmc jacket_hairdown basic at centre
            mcariannaprev "There's nothing to open up about. She's just a friend."
            hide mscmc
            show trina casual basic at centre
            "Trina brushes me off with pursed lips."
        "C. Don't deny it.":
            $ menuhideborder = False
            show mscmc jacket_hairdown surprised at centre
            mcariannaprev "I'm right here, you know."
            hide mscmc
            show trina casual smile at centre
            so "That's the point."
    show trina casual smile at left3
    show arianna dress basic at right3
    so "So, are you from around here, Arianna?"
    hide trina
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna's never spoken to another human aside from me and she told me everything.)"
    show mscmc jacket_hairdown surprised at left3
    show arianna dress sad at right3
    "My shoulders tense as I catch Arianna's eye and shift my weight onto one leg."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(If Trina finds out, Arianna could get in huge trouble.)"
    hide mscmc
    show trina casual basic at left3
    show arianna dress smile at right3
    ai "Here and there. I've lived all over, honestly."
    so smile "A woman of mystery. I dig it."
    hide trina
    hide arianna
    show mscmc jacket_hairdown sleep at centre
    "I let out a breath of relief, my shoulders relaxing."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Thank god.)"
    hide mscmc
    "In an effort to steer the conversation away, Arianna points to a poster of dolphins on surfboards."
    show arianna dress grin at centre
    ai "I love dolphins! I could listen to them talk all day."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Can Arianna {i}actually{/i} talk to dolphins?)"
    hide mscmc
    show trina casual smile at centre
    so "Some guy was selling posters by the beach bar and I couldn't resist."
    hide trina
    show arianna dress surprised at centre
    ai "Beach bar?"
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is there an underwater equivalent to that?)"
    hide mscmc
    show trina casual smile at centre
    so "You've never been, Arianna?"
    show mscmc jacket_hairdown surprised at left2
    show trina at right1plus
    "Trina pats me on the back."
    so "Dude, you have to take her out!"
    hide mscmc
    hide trina
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna lights up with an excited nod towards me."
    hide arianna
    show mscmc jacket_hairdown embarrassed at centre
    "Seeing Arianna's excitement makes my heart warm."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I'll have to thank Trina later for being the ultimate wingman.)"

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    scene bg msc_beach_bar_sunset at bg with fade
    "I take Arianna to Jerry's Beach Bar, the sun setting over the water."
    show mscmc jacket_hairdown smile at left2
    show arianna dress basic at right3
    "Sitting at the counter, I order us both beers and push one over to Arianna as she takes it in."
    ai smile "We don't call them bars, but this reminds me of a place I go to back at home."
    show mscmc surprised
    show arianna basic
    "Still looking around, Arianna is about to try her beer when she grabs my wrist."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is she making a move?)"
    show mscmc jacket_hairdown surprised at left2
    show arianna dress angry at right3
    ai "Look."
    hide mscmc
    hide arianna
    "Behind the counter is a metal sculpture of a mermaid - elegant and fluid like it's moving."
    show arianna dress basic at right1plus
    show mscmc jacket_hairdown surprised at left1plus
    ai "That's my sculpture."
    show mscmc embarrassed
    "She's leaned in, her hot breath on my ear sending a shiver down my spine."
    mcariannaprev "It's beautiful."
    show arianna:
        pause 0.1
        easein 0.6 right2
    "Arianna mumbles in thanks before pulling back and taking a sip of her beer."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(She should be proud of herself - she's talented.)"
    hide mscmc
    show arianna dress_cu surprised_cu at arianna_cu
    "A thoughtful look crosses Arianna's face as she examines her beer."
    show arianna dress surprised at centre
    ai "We don't have beer. We have drinks that get you drunk, but nothing like this."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She told me to order her whatever, but maybe I should've gotten something different.)"
    show mscmc jacket_hairdown surprised at left2
    show arianna dress basic at right3
    mcariannaprev "You don't like it?"
    show mscmc smile
    ai grin "I love it! It's so bubbly!"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Her eyes meet mine and her grin turns into the most heart melting smile."
    show mscmc jacket_hairdown smile at left2
    show arianna dress grin at right3
    mcariannaprev "Where exactly in the ocean do you live?"
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I need to start talking about something to get my mind off of how much I like looking at her.)"
    show mscmc jacket_hairdown smile at left2
    show arianna dress smile at right3
    ai "The capital is south east from here. There's a portal to it not too far from the coast."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Portals? Is that the kind of public transportation they have?)"
    show mscmc jacket_hairdown smile at left2
    show arianna dress smile at right3
    mcariannaprev "I'm Jamaican, but I was raised in the midwest."
    mcariannaprev grin "I want to go to Jamaica. Sure would be nice to walk through a portal and be there."
    mcariannaprev "But, I know I'll get there. Surfing's gonna take me all over the world."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna silently watches me with her head cocked."
    show arianna dress smile at centre
    "She hums in thought before taking a drink."

    show bg msc_beach_bar_night_lights with dissolve
    "By the time the sun has gone down, Arianna has finished two beers."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I only had one drink so I could watch her, but other than being a bit tipsy, she seems fine.)"
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress grin behind mscmc at right1plus
    "Arianna tugs on my sleeve as she sees a bonfire and pulls me onto the beach towards it with a giddy laugh."
    show bg msc_labeach_night with dissolve
    "We stand next to the fire, the flames casting shadows on us and the heat on our skin."
    show mscmc embarrassed
    "There's only about an inch of space between us and I think of how her hand felt."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I wouldn't mind feeling that again.)"
    hide mscmc
    "Arianna and I move a little ways from the fire and sit in the sand together."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(It's been so long since I've thought about anything other than surfing and the shop.)"
    "(I feel...peaceful.)"
    show mscmc jacket_hairdown smile at left2
    show arianna dress smile behind mscmc at right2
    ai "I really liked that beer."
    ai grin "It makes me feel different from the drinks I'm used to, but it's nice. And I'm not too tipsy or anything."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "She grins at me, one of her fingers twirling her hair."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I'm glad she liked it, but I don't want her to leave.)"
    show mscmc sad_cu
    "(It's dark now and the thought of her swimming alone makes me feel uneasy.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress basic behind mscmc at right2
    mcariannaprev "Do you want to crash at my place tonight? It's pretty late."
    show arianna smile:
        easein 0.4 right1plus
    "Arianna lets out a gasp of delight and she shifts closer."
    show mscmc embarrassed
    ai "Really? I can stay at your place?"
    "I'm hoping the night will hide the blush on my face."
    mcariannaprev "If you want. Don't drink and swim, am I right?"
    show arianna grin
    "Arianna laughs and gives a slow nod."
    ai "Exactly."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with wiperightdissolve
    "We make our way back to the surf shop and I take her to my room."
    show arianna dress smile at centre
    "I watch as Arianna checks it out. She looks delighted."
    ai "It feels like you."
    ai "It's cute."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(That was the same as her calling me cute, right?)"
    hide mscmc
    show arianna dress basic at centre
    "Arianna moves to sit on the edge of my bed and runs her hands over the covers."
    ai smile "This is what you sleep on? I sleep in a biiiig shell."
    "She shuffles back and forth, rubbing her thighs against the covers."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Seeing Arianna on my bed is something else.)"
    "(I know she's just testing it out, but does she have to look so hot?)"
    hide mscmc
    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna dress sad at centre
    ai "When Hamish buys the shop, won't you lose your home?"
    show arianna dress_cu sad_cu at arianna_cu
    "She looks at me with a frown."
    hide arianna
    show mscmc jacket_hairdown sad at centre
    "Unsure if I should sit next to her or not, I end up standing in the middle of the room."
    mcariannaprev basic "I'll figure something out."
    hide mscmc
    show arianna dress_cu basic_cu at arianna_cu
    "She meets my gaze."
    show arianna dress basic at centre
    ai "You really care about Trina and this place."
    ai smile "I really like that about you."
    "Arianna scoots herself further up the bed and starts looking at her stretched out legs curiously."
    hide arianna
    show mscmc jacket_hairdown embarrassed at centre
    "I move my eyes to the wall. It's hard not to feel flustered while she seems so unfazed."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Maybe I'm reading into things, but she makes me feel like romance isn't such a bad thing.)"
    hide mscmc
    show arianna dress sleep at centre
    "Moving her hand to her mouth, Arianna yawns."
    show mscmc jacket_hairdown smile at left2
    show arianna dress basic behind mscmc at right2
    mcariannaprev "You sleep on the bed tonight. I'll set up on the floor."

    scene arianna_s0_mini1 at bg with fade
    "Arianna opens her mouth and quickly closes it."
    "She brings her hand up to her necklace and starts fidgeting with it."
    ai "I've never slept on land before and I feel a bit...anxious."
    ai "I think I'd feel better if you were next to me."

    scene bg msc_mc_bedroom_night_lights at bg
    show arianna dress_cu sad_cu at arianna_cu
    with dissolve
    "She stares down at her hands, her face red."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna usually seems in control and casual, but right now she looks so vulnerable.)"
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "Would you sleep in the bed with me, [genericfn]?"
    hide arianna

    $ menuhideborder = True
    menu ariannas0e3c3:
        "A. Share the bed with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mscmctheme fadein 1.0
            show mscmc jacket_hairdown embarrassed at centre
            "I hope mermaids don't have super hearing because the only thing I can hear is my own heart."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(It's no big deal. It's just sleeping.)"
            "(In the same bed. With a mermaid. Who's also extremely gorgeous.)"
            "(And who has maybe been flirting with me.)"
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Uh, yeah. Yeah, that's cool with me. I don't mind."
            show mscmc surprised
            "In my attempt at being the most casual person in the world, I bump my elbow into my lamp."
            hide mscmc
            "It wobbles and knocks over an old water bottle missing its cap."
            "There's not much water in it, but it seeps into the floor."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Not being cool!)"
            show mscmc jacket_hairdown surprised at left7:
                pause 0.1
                easein_back 0.5 centre
                pause 0.1
                easein 0.4 yoffset 100
            "I make a hasty grab for my beach towel and drop to my knees, soaking up the water."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
                yoffset 0
            "(I'm a complete mess because there's a beautiful girl on my bed watching me.)"
            show mscmc jacket_hairdown surprised at centre
            mcariannaprev "I was in a rush earlier and I forgot about it and I don't know why the cap is gone and-!"
            hide mscmc
            show arianna dress grin at centre
            "Arianna's laughing cuts me off and my iron grip on the towel loosens."
            hide arianna
            show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
            "(Relax.)"
            show mscmc basic_cu
            "(Don't start panicking.)"
            show mscmc jacket_hairdown basic at centre
            "After I finish cleaning the water, I walk past the bed to toss the towel in my hamper."

            stop music fadeout 0.5
            play music mscromance fadein 1.0
            show mscmc at left1plus
            show arianna dress basic behind mscmc at right1plus
            "Arianna leans over to catch my hand."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Every time she touches me, it's like nothing matters but the way her hand feels.)"
            show mscmc jacket_hairdown embarrassed at left1plus
            show arianna dress basic behind mscmc at right1plus
            "That electric feeling is there again - from her to me. Then she's letting go."
            show mscmc smile
            ai smile "Thank you, [genericfn]. For tonight."
            hide mscmc
            show arianna at centre
            "She moves herself to the top of the bed and lifts the covers so that she can slip under."
            hide arianna
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Of course."
            "There's a softness in my voice that I haven't heard in ages."

            scene bg msc_mc_bedroom_night at bg
            show mscmc casual_hairdown smile at centre
            with dissolve
            "I can't help but smile to myself as I turn the lights off."
            hide mscmc
            show arianna dress smile at centre
            "Arianna makes a pleased noise as she situates herself, her long hair sprawled on the pillow."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her hair looks soft and sleek. I bet it'd feel nice to run my fingers through.)"
            show mscmc casual_hairdown embarrassed at centre
            "I get on the bed as carefully as I can, but I'm shaking. It's more than just nerves."
            "My whole body is tingling from when she touched my hand."
            hide mscmc
            show arianna dress sleep at centre
            "Arianna's chest steadily rises and falls with each breath."
            hide arianna
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(I've never met someone like her before...and I've never felt this way before.)"
            show mscmc sad_cu
            "(Surfing has been number one in my mind for so long and I'm scared of losing focus.)"
            show mscmc casual_hairdown sad at left1plus
            show arianna dress sleep behind mscmc at right2
            "The heat from Arianna's body is making my head swim."
            show mscmc sleep
            "I take a deep but quiet breath and stop fidgeting with the covers."
            hide arianna
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(I have to calm down. She's gonna think I'm some kind of weirdo.)"
            show mscmc sleep_cu
            "(Don't think about how close she is or how she feels. Just chill.)"
            show mscmc casual_hairdown surprised at left1plus
            show arianna dress basic behind mscmc at right1plus
            "Chilling is far from my mind as Arianna rolls to her side, facing me."
            show mscmc basic
            "Flat on my back and eyes to the ceiling, I try not to look at her."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(I'm scared that I won't be able to look away.)"
            "(Arianna's trusted me with so much. I'm glad I make her feel comfortable.)"
            show mscmc casual_hairdown basic at left1plus
            show arianna dress sad behind mscmc at right1plus
            ai "Are you awake?"
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "She's speaking quietly, but she's so close to my ear that my breath hitches."
            "If I just moved in a little more, she'd be against my arm."
            show mscmc casual_hairdown surprised at left1plus
            show arianna dress sad behind mscmc at right1plus
            mcariannaprev "Yeah."
            show arianna basic
            "Arianna snuggles into the pillow with a hum."
            ai smile "I'm really glad I met you."
            "Tiredness makes her words melt into one another."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(God, she sounds adorable. How can someone be this cute?)"
            "(If I don't settle down, I'm gonna have a heart attack.)"
            show mscmc casual_hairdown sleep at left1plus
            show arianna dress smile behind mscmc at right1plus
            "I take another deep breath and relax against the mattress."
            mcariannaprev smile "I'm really glad too."
            show arianna sleep
            "Arianna is silent and when I dare to peek at her, I see that she's fallen asleep."
            "I put a hand to my mouth and smile against my fingers."
            hide arianna
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            "(Even when she's sleeping, she's beautiful.)"
            hide mscmc
            show arianna dress_cu sleep_cu at arianna_cu
            "Her face looks so much softer - she's completely relaxed."
            hide arianna
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            "(She makes me feel comfortable and confused and every good emotion at the same time.)"
            "(Arianna feels {i}familiar{/i}. It's like we've known each other forever.)"
            hide mscmc
            show arianna dress_cu sleep_cu at arianna_cu
            "Her quiet breathing mixes with the sound of waves breaking outside."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(I don't want to lose this.)"
            hide mscmc
            show arianna dress_cu sleep_cu at arianna_cu
            "For a moment, I feel peaceful and then Arianna moves her hand, nearly brushing mine."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(There's no way I'm ever going to fall asleep!)"


        "B. Sleep on the floor.":
            $ menuhideborder = False
            show mscmc jacket_hairdown embarrassed at centre
            "I look at Arianna blushing and I want nothing more than to say yes."
            mcariannaprev "It'll be fine, I promise."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Sleeping in the same bed would've been the perfect excuse to be closer to her!)"
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "You're completely save and if you need anything, I'll be right here."
            hide mscmc
            "Grabbing a pillow and a blanket, I toss them to the floor."
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(She's being vulnerable and trusting me, but I haven't felt this way in forever.)"
            show mscmc sad_cu
            "(I'm scared of how I'm starting to feel towards her.)"
            hide mscmc
            show arianna dress sad at centre
            ai "Yeah, you're right."
            hide arianna
            "She starts to get under the covers, her eyes not meeting mine."
            scene bg msc_mc_bedroom_night at bg
            show mscmc casual_hairdown sad at centre
            with dissolve
            "Arianna's quick change in demeanor has me confused as I turn off the lights."
            show mscmc at left4
            show arianna dress basic at right4
            ai "Goodnight."
            mcariannaprev "Night."
            hide arianna
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(Is she actually fine with this?)"
            show mscmc casual_hairdown basic at centre
            "I arrange the pillow and blanket into my makeshift bed. It's definitely not luxury comfort."
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            "(Oh well. It's better this way.)"
            show mscmc sad_cu
            "(I can't lose sight of what's important because of romance.)"
            show mscmc casual_hairdown sleep at centre
            "I close my eyes listening to the lull of the waves and Arianna's breathing."
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    scene black
    scene bg msc_mc_bedroom_night at bg with eye_open
    "I wake up and it's still dark out."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(I don't even remember falling asleep.)"
    show mscmc casual_hairdown smile at centre
    "The sound of Arianna breathing instantly reminds me of everything."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(We need some kind of plan.)"
    show arianna dress sleep behind mscmc at right2
    show mscmc casual_hairdown basic at left1plus
    "I look over at Arianna."
    "She's comfortably nestled in the blanket."
    hide mscmc
    show arianna dress_cu sleep_cu at arianna_cu
    "A stray piece of hair is draped over her face, lining her cheekbone and resting on plump lips."
    show arianna dress sleep behind mscmc at right2
    show mscmc casual_hairdown embarrassed at left1plus
    "My breath catches as I take her in."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(I could look at her forever.)"
    show arianna dress sleep behind mscmc at right2
    show mscmc casual_hairdown surprised at left1plus
    "Arianna rolls onto her back and stretches out the arm she'd been sleeping on."
    show arianna smile
    "She blinks open her eyes and looks at me with a tired smile."
    ai "What're you doing?"
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Crap, I've been caught!)"
    show arianna dress smile behind mscmc at right2
    show mscmc casual_hairdown surprised at left1plus
    "I try to fumble for a reply, but she cuts me off."
    ai grin "I'll make you tell me later. I think I have an idea to fix everything!"

    scene msc_tbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
