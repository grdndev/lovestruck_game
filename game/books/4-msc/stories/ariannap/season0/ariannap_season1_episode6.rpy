label ariannap_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg
    play music mscsurfshop

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "It's the day of the party!"
    "The surf shop is bustling with people and music."
    "Arianna has brought up more of her amazing sculptures and they're scattered about"
    show trina casual smile at centre
    "Trina is busy going up to people and talking, getting them more involved with the activities."
    hide trina
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(It's good to see her hopeful. The turnout is better than any of us thought.)"
    show mscmc jacket_hairdown smile at left2
    show arianna siren smile at right2
    "Arianna and I are on a makeshift stage, Arianna stationed inside of a kiddy pool."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(It's so bizarre seeing her in public with her tail...but so far everything's been fine.)"
    show mscmc jacket_hairdown smile at left2
    show arianna siren smile at right2
    "I bring kids up to her, some of them from my classes, and take their pictures."
    "Arianna chats with them about being a mermaid and laughs as they ask to touch her tail."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I think she's having fun and, on top of that, she must feel good to have her art out.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas0e6c1:
        "A. Usher over more kids.":
            $ menuhideborder = False
            show mscmc jacket_hairdown smile at centre
            "Spotting one of the girls from my surfing class, I wave to her."
            mcariannaprev grin "Do you want a picture with Arianna?"
            "She nods in excitement, coming over to pose next to Arianna and I take the picture."
        "B. Ask Arianna how she's doing.":
            $ menuhideborder = False
            show mscmc jacket_hairdown smile at left2
            show arianna siren smile at right2
            mcariannaprev "You doing alright?"
            "There's a break in kids and I bend down to Arianna."
            ai grin "Better than alright! I'm having a really great time."
        "C. Think about how good Arianna looks.":
            $ menuhideborder = False
            show arianna siren smile at centre
            "Arianna combs her hair to the side, shaking out a little bit of water."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Even in a kiddy pool, Arianna looks like she's out of some renaissance painting.)"
            hide mscmc
            show arianna siren smile at centre
            "Arianna's lips quirk up as she catches me staring."

    hide mscmc
    hide arianna
    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    show hamish casual basic at left7:
        pause 0.1
        easein 0.8 centre
    "The door swings open and I'm expecting to see Jerry with the drinks he promised."
    rm angry "You know this won't work."
    "Hamish moves into the shop to stand over Trina with a scowl."
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(I'm not surprised he showed up, but it's still annoying.)"
    hide mscmc
    show hamish casual angry at left2
    show trina casual angry at right3
    rm "I don't know what you're trying to pull here."
    "Trina glares at him while she scoffs and crosses her arms."
    so "Get out of my shop, Hamish. You're not invited to the party."
    rm basic "Soon this will be {i}my{/i} shop, Trina."
    "His eyes leave Trina and look around."
    hide trina
    show hamish casual_cu surprised_cu at hamish_cu
    "When he sees Arianna, his eyes grow wide."
    show hamish casual angry at centre
    rm "Of course. It all makes sense."
    hide hamish
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Oh no. This isn't good.)"
    hide mscmc
    show hamish casual angry at centre
    rm "That woman's a real mermaid. She has to be! There's no other way."
    hide hamish
    show mscmc jacket_hairdown surprised at left2
    show arianna siren angry at right2
    "My stomach drops at his words and I can see Arianna's body tense, though her gaze is level."
    hide mscmc
    hide arianna
    show hamish casual surprised at left2
    show trina casual basic at right1plus
    "Trina puts a hand on Hamish's shoulder to direct him to the door."
    show hamish angry
    so angry "Are you drunk or something? Get out."
    "Hamish shakes Trina off, his voice raising."
    rm "She's a mermaid! How else would her art be at the bottom of the ocean?"
    hide hamish
    hide trina
    show arianna siren_cu basic_cu at arianna_cu
    "I catch Arianna's eye, my heart stopped, but she gives me a barely visible shake of the head."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Right. We shouldn't engage with this. Just ignore it.)"
    hide mscmc
    show hamish casual angry at left2
    show trina casual angry at right2
    so "Hamish, you need to go. {i}Now{/i}. You're embarrassing yourself."
    "Hamish throws his hands up and heads towards the door."
    show hamish:
        linear 0.6 left7 xoffset -20
    "He grumbles to himself and pushes past Jerry coming in with a drink cooler."
    hide hamish
    hide trina
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(Glad that's over with.)"
    show mscmc jacket_hairdown basic at left2
    show arianna siren basic behind mscmc at right2
    "Arianna and I share another quiet look before Arianna waves to a little boy to get his attention."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show mscmc casual_hairdown smile at left2
    show arianna smile
    "The party eventually dies down a bit and I end up sitting in the kiddy pool with Arianna."
    hide mscmc
    hide arianna
    show trina casual basic at centre
    "Trina is kneeling beside it, her hands playing in the water."
    show mscmc casual_hairdown grin at left2
    show trina smile at right2
    mcariannaprev "How'd we do? A lot of people showed up."
    "Trina takes a breath and idly plunges a hand in and out of the water."
    show mscmc basic
    so sad "You guys were great. Everything was, but..."
    so "It just wasn't enough."
    hide trina
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(We're out of time and ideas.)"
    "(This was it. The shop has been my home and now I'm losing it.)"
    hide mscmc
    show arianna siren sad at centre
    "Arianna gently splashes her tail down, her hand worrying over her necklace."
    hide arianna
    play sound phone_ringing
    stop music fadeout 0.5
    play music msctense fadein 1.0
    "The store phone rings."
    show trina casual basic at centre
    "Trina begrudgingly gets to her feet, wiping her hands off on her shorts."
    hide trina
    show mscmc casual_hairdown sad at left2
    show arianna siren sad behind mscmc at right1plus
    "Arianna and I exchange defeated frowns as Trina picks up the phone."
    hide mscmc
    hide arianna
    show trina casual basic at centre
    so "Hello?"
    "Trina stands up straighter, a crease forming between her brows."
    so angry "Okay...who is this?"
    show mscmc casual_hairdown sad at left2
    show trina at right2
    "Arianna raises her eyebrows in question at me and I shrug."
    hide trina
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Maybe a parent calling to say their kid left behind a stuffed animal or something?)"
    hide mscmc
    show trina casual basic at centre
    so "Wait, what?"
    "Trina looks over at us, her mouth opening as she listens on the phone."
    so "{i}All{/i} of them?"
    show trina sleep
    "She pushes her fingers through her hair and nods her head."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    so basic "Uh, yeah. Totally. Oh my god."
    show trina smile
    "Trina lets out a quiet laugh."
    so "No, thank {i}you{/i}. This is probably the best thing I've ever heard."
    "She mutters a quick goodbye before hanging up the phone."
    so "Someone just bought {i}all{/i} of Arianna's pieces!"
    show mscmc casual_hairdown surprised at left3
    show trina at right2
    mcariannaprev "What? Who?"
    show trina sleep
    "Trina shakes her head, a laugh of disbelief to follow."
    show mscmc basic
    so smile "I don't know. They wanted to remain anonymous."
    show mscmc grin
    so "But it's enough money to keep us afloat. I'm not gonna lose the shop!"
    hide trina
    show arianna siren grin at right1plus
    "Arianna opens her mouth in shock and I nudge her with my elbow."
    mcariannaprev "We did it!"
    show trina casual smile behind mscmc at centre:
        transform_anchor True zoom 0.95 xoffset -50 alpha 0.5
        linear 0.6 zoom 1.0 alpha 1.0
    "Trina comes from behind and leans down, wrapping her arms around Arianna and me."
    so "It's all thanks to you guys! You two did it!"

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    scene bg msc_labeach_day at bg with fade
    "After the party is done, Arianna and I walk to the beach to get some air."
    show arianna dress smile at right2
    show mscmc jacket_hairdown smile at left2
    "The sand feels nice on my feet and as I take a deep breath."
    show arianna grin
    "Arianna hums to herself, a smile still fixed on her face since the news of her art being bought."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Arianna was so sad about her art and now look at her.)"
    "(We made a deal that we'd help each other and I guess we did that.)"
    "(Is there anything more for us? I want there to be, I really do.)"
    show mscmc jacket_hairdown surprised at centre
    "Arianna taps a knuckle against my arm to make me look at her."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "She smirks."
    show mscmc jacket_hairdown basic at left1plus
    show arianna dress smile at right2
    ai "How about going for a swim?"
    show mscmc smile
    "Her voice sounds mischievous, though nothing I'm not used to by now with her."
    mcariannaprev "Sure, but why?"
    show arianna grin
    "Arianna shrugs with a laugh."
    ai "Just follow me."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I wonder if she's thinking about the same things I am.)"
    show mscmc grin_cu
    "(What's Arianna's plan now?)"
    hide mscmc
    show arianna siren basic at centre
    "We wade out into the crashing waves, Arianna eventually switching back to her tail."
    show arianna smile
    "The tips of her ears poke through her hair."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Is every mermaid as beautiful as Arianna?)"
    hide mscmc
    show arianna siren grin at centre
    ai "Let's go!"
    show arianna:
        transform_anchor True yalign 0.9 yoffset 592
        easein 0.6 zoom 0.97 alpha 0.0
    "She dives underneath, making me duck out of the way of her tail."

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    $ wavy_transition("bg msc_labeach_day", "bg msc_underwater_day")
    scene bg msc_underwater_day at bg with dissolve
    "I follow her under the water and watch her twist and twirl effortlessly."
    show mscmc bikini_hairdown basic at left3
    show arianna siren smile at right2
    "She swims over me and then in front, nodding at me to join her."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(My swimming is nothing compared to hers.)"
    show mscmc surprised_cu
    "(Arianna literally lives in the water and has a tail!)"
    hide mscmc
    "Feeling a bit awkward, I swim around her, but that seems to please her."
    show bg msc_underwater_sunset with dissolve
    "The sun has begun to set, casting its orange glow through the water."
    show arianna siren_cu smile_cu at arianna_cu
    "Arianna swims through and around the rays, beckoning me with the most inviting face."
    hide arianna
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(I might not be able to compete with Arianna's swimming, but I wouldn't trade this for the world.)"
    show mscmc bikini_hairdown basic at left3
    show arianna siren basic at right2
    "Pointing to the top, I let Arianna know that I'm going up for air."
    show mscmc surprised
    show arianna behind mscmc:
        easein 0.5 right1 xoffset -30
    "Arianna is quick to swim over to me and takes my wrist with a delicate grab."
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Oh?)"

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show mscmc bikini_hairdown surprised at left3:
        pause 0.2
        easein_back 0.4 left1 xoffset -50
    show arianna siren basic behind mscmc at right1:
        xoffset -30
    "She pulls me closer and I let it happen, my heart pounding."
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu:
        xoffset 0
    "(Is she going to kiss me?!)"
    hide mscmc

    show arianna siren_cu smile_cu at arianna_cu:
        transform_anchor True align (0.5, 0.5) yoffset 50
        linear 0.6 zoom 1.2 alpha 0.0
    "Arianna leans in and when her lips are almost to mine, she breathes out air."
    hide arianna
    "It flows across the small space between us and between my own lips."
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(That definitely beats going up for a breath.)"
    show mscmc bikini_hairdown smile at centre
    "The air fills me and it feels like taking a deep breath on a winter morning."

    scene arianna_00_e6 with fade:
        align(0.0, 1.0) zoom 1.3
        pause 0.4
        linear 4.5 align(1.0, 0.0) yoffset -115 xoffset 300
    pause 5.0
    "Arianna pulls back just a little."
    "Her eyes flick down to my lips."
    window hide
    show arianna_00_e6:
        transform_anchor True
        linear 4.0 yoffset 0 xoffset 0 zoom 0.65
    pause 4.0
    "(Should I kiss her? Does she want me to?)"
    "Her fingers travel down to my hand and she pulls me flush against her in a spin."
    "She puts her lips to my ear, her voice sounds clear as it is above water."
    ai "Will you dance with me, [genericfn]?"

    $ menuhideborder = True
    menu ariannas0e6c2:
        "A. Dance with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            scene bg msc_underwater_sunset at bg
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            with fade
            "(How could anyone say no to her?)"
            show mscmc bikini_hairdown smile at left1plus
            show arianna siren smile behind mscmc at right1
            "Arianna pulls back so that she can look at me, her eyes shining and I nod."
            hide arianna
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(I'm not exactly sure how underwater dancing works, but who cares?)"
            show mscmc grin_cu
            "(Nothing could beat this moment.)"
            hide mscmc
            "Arianna's hand is now travelling back up my arm and over my bicep as she swims around me."
            "Her fingers ghost over my shoulders, dipping into my neck and her tail wraps around my legs."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I'm sure she can feel my heart beating.)"
            hide mscmc
            "Each touch from her leaves a trail of electric heat that makes my skin tingle."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(She has this power over me that I can't explain.)"
            "(If she weren't holding onto me right now, I might just float away.)"
            show mscmc bikini_hairdown smile at left1plus
            show arianna siren smile behind mscmc at right1plus
            "Arianna spins me to face her, her tail still around my waist."
            "It's strong and muscular around me."
            show arianna grin:
                pause 0.3
                easeout 0.9 right7 xoffset 65
            pause 1.0
            "The fan of her tail brushes across my cheek as Arianna swims back with a laugh."
            hide mscmc
            show arianna siren smile at centre:
                xoffset 0
            ai "Let the water lead you. Just listen to it."
            hide arianna
            show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
            "(It's not like we're dancing to real music down here, but there is something.)"
            show mscmc surprised_cu
            "(Like the ocean is a song itself.)"
            hide mscmc
            "The gentle current of the ocean encourages me towards Arianna and I allow it."
            show mscmc bikini_hairdown sleep at centre
            "It feels as though I'm part of the water, like I've given it control over me."
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(I'm dancing with a mermaid under the ocean.)"
            show mscmc bikini_hairdown smile at left3
            show arianna siren basic at right4
            "The thought makes me laugh in disbelief, Arianna cocking her head in question."
            hide arianna
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(I wonder how Arianna's land legs would fare with dancing on solid ground.)"
            "(Maybe I'll get to see that someday.)"
            hide mscmc
            "I swim down and then back up to Arianna, my hand trailing up her tail."
            show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
            "(It's smooth like very soft leather.)"
            show mscmc bikini_hairdown smile at left2
            show arianna siren grin at right2
            "At eye level now, Arianna puts her hand up much like she did when we made our deal."
            hide arianna
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(This is like a different kind of deal, isn't it? Like a deal to never forget this.)"
            show mscmc bikini_hairdown smile at left2
            show arianna siren smile at right2
            "I press my palm to hers and she closes her fingers over mine."
            ai "Your hand is so small it fits in mine."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(Like a missing puzzle piece.)"
            show mscmc bikini_hairdown smile at left2
            show arianna siren grin at right2
            "Arianna giggles and I roll my eyes, though I can't help but grin."
            hide mscmc
            hide arianna
            "Moving around with her, I keep hold of her hand so that I can turn her with me."
            "The water flows all around us, each delicate sway nudging us."
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(I would stay down here with her forever if I could.)"
            show mscmc bikini_hairdown smile at left1plus
            show arianna siren smile behind mscmc at right1
            "Arianna's hand moves to my back and presses our bodies against one another."
            hide mscmc
            hide arianna
            "The colors of the water change as the sun continues to go down."
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(As cliché as it sounds, this moment feels magical.)"
            show mscmc grin_cu
            "(In a sense, I guess it actually is.)"
            show mscmc bikini_hairdown grin at left1plus
            show arianna siren smile behind mscmc at right1plus
            "I put my hands on Arianna's shoulders, wishing it possible for us to be even closer."
            show mscmc smile
            "It's like time freezes."
            "At this moment, it's just Arianna and me in the whole world."
            "Together, we're suspended beneath the waves looking into each other's eyes."
            hide arianna
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(We've both changed, haven't we?)"
            "(In such little time, we've both helped each other be more comfortable with ourselves.)"
            show mscmc bikini_hairdown embarrassed at left1
            show arianna siren smile behind mscmc at right1
            "I feel a heartbeat against my chest, but I'm not sure if it's mine or hers. We're so close."
            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu
            "My eyes drop to Arianna's lips."
            ai "[genericfn]."
            hide arianna
            show mscmc bikini_hairdown embarrassed at centre
            "As she says my name, a shiver runs down me."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Right now, I feel like one of the luckiest people alive.)"
            show mscmc bikini_hairdown embarrassed at left1
            show arianna siren smile behind mscmc at right1
            ai "Thank you for dancing with me."
            show arianna surprised
            "A realization seems to dawn on Arianna's face, like she too is aware of our position."
            show arianna embarrassed:
                easein 0.5 right1plus xoffset 20
            "Then Arianna lets me go and swims back with a smile. Her warmth leaves me."
            hide arianna
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(I wish we could've stayed like that for longer.)"

        "B. Refuse":
            $ menuhideborder = False
            scene bg msc_underwater_sunset at bg
            show mscmc bikini_hairdown embarrassed at centre
            with fade
            "Even in the cool water, I feel hot."
            "My heart is pounding fast enough I think it might burst."
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(We almost kissed, right?)"
            "(And now she wants me to dance with her. This is just...)"
            show mscmc bikini_hairdown embarrassed at centre
            "I shake my head, with an apologetic and embarrassed smile."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Arianna's all I've been thinking about.)"
            show mscmc sleep_cu
            "(I don't want to fall for her.)"
            hide mscmc
            show arianna siren basic at centre
            "Arianna pulls back from me with a carefree shrug."
            show arianna smile
            "She does a small spin before swimming off."
            hide arianna
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(Wait, is she leaving? Is she upset that I didn't say yes?)"
            hide mscmc
            show arianna siren smile at centre:
                transform_anchor True zoom 0.8 alpha 0.0
                pause 0.1
                linear 0.8 zoom 1.0 alpha 1.0
            "My worry doesn't control me for long, as Arianna is already coming back."
            show mscmc bikini_hairdown grin at left1plus
            show arianna at right1plus
            "With her palm out, she shows me a tiny yellow fish swimming over her palm."
            show arianna grin
            "Arianna grins at me and I return it."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(We might not be dancing, but this is still nice.)"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    scene bg msc_tide_pools_sunset at bg with fade
    "Tuckered out from our swim and the last few days, Arianna and I sit on the tidepools."
    show arianna siren smile at right1plus
    show mscmc jacket_hairdown grin at left1plus
    "I'd found my headphones in my stuff and wanted to show Arianna some human music."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She's so adorably curious about human things.)"
    hide mscmc
    "With my headphones shared between us, we watch as the sun goes down."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(And just like that, another day is ending.)"
    "(I wouldn't mind if we had more time togther.)"
    hide mscmc
    show arianna siren sleep at centre
    "Arianna has her eyes closed as she listens, her head nodding along ever so slightly."
    show arianna siren_cu sleep_cu at arianna_cu
    "I look at her eyelashes, long and upturned."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She's probably love a concert.)"
    show mscmc smile_cu
    "(I could show her so many different things, and I can't even imagine what she could show me.)"
    show mscmc jacket_hairdown smile at left2
    show arianna siren smile behind mscmc at right1plus
    "Arianna opens her eyes, catches me staring, and smiles at me like she can't help herself."
    ai surprised "This is pretty good. What're they called again?"
    show arianna basic
    mcariannaprev "Girl in blue."
    show arianna smile
    "The water from our swim is still drying on my skin and Arianna's tail is pressed against my thigh."
    "A breeze blows a few pieces of Arianna's hair onto my shoulder."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Since when did physical contact become so natural between us?)"
    show mscmc embarrassed_cu
    "(So many gentle touches here and there...)"
    show mscmc jacket_hairdown basic at left2
    show arianna siren basic behind mscmc at right1plus
    "As the song ends, Arianna takes out the earbud and examines it."
    ai smile "We use song pearls to listen to music."
    mcariannaprev surprised "Song pearls?"
    show arianna sleep
    "She nods and imitates putting something to her ear."
    show mscmc smile
    ai grin "They're not real pearls, but they're made to look like them."
    ai smile "You just kind of stick it to your ear and it plays songs you save to this other pearl."
    ai "It's a whole thing."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(The wireless headphones of the sea.)"
    show mscmc jacket_hairdown smile at left2
    show arianna siren smile behind mscmc at right1plus
    "Arianna hands me back my earbud, our fingers brushing as I take it."
    show mscmc grin
    "I laugh in an attempt to distract from my red face as I wrap the earbuds around my phone."
    show arianna basic
    "My laugh fades as Arianna's face falls."
    mcariannaprev surprised "Hey, what's wrong?"
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    "The smile is back, but this one seems forced."
    show mscmc jacket_hairdown basic at left2
    show arianna siren smile behind mscmc at right1plus
    ai "You know, I've had a really amazing time...with you."
    ai "It's been so much fun and you really did help me."
    hide arianna

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show mscmc jacket_hairdown sad at centre
    "My stomach drops a bit."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She's going to leave isn't she?)"
    hide mscmc
    show arianna siren basic at centre
    "Arianna puts a hand to her necklace and twirls it around her fingers."
    ai "But, I should really get going. I've been here long enough."
    show arianna siren_cu sad_cu at arianna_cu
    "In her eyes I see her vulnerable side again."
    "She's sad she has to go."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I knew this was coming - it was inevitable. This isn't her world.)"
    "(And her world isn't mine.)"
    hide mscmc
    show arianna siren basic at centre
    ai "I never meant to talk to a human or reveal myself."
    ai smile "When I saw you that first day helping that porpoise, and the way you love the water..."
    ai "Something just clicked."
    hide arianna

    $ menuhideborder = True
    menu ariannas0e6c3:
        "A. Say that you felt the same way.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(I can still remember clearly how she looked when we first met.)"
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Me too."
            hide mscmc
            show arianna siren_cu smile_cu at arianna_cu
            "Arianna smiles at me, warm and tender."
        "B. Thank her for everything.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Arianna's shown me so much. No matter what happens, I'll always remember this.)"
            show arianna siren basic behind mscmc at right1plus
            show mscmc jacket_hairdown smile at left2
            mcariannaprev "Thank you, Arianna. Seriously, these past few days have been incredible."
            ai smile "They really have been."
        "C. Stay quiet.":
            $ menuhideborder = False
            show mscmc jacket_hairdown sad at centre
            "I take her words in with a heavy, but happy heart."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Of course I don't want her to leave, but I know she has to.)"
            "(I'm just glad for what we experienced together.)"

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show arianna siren smile behind mscmc at right1plus
    show mscmc jacket_hairdown basic at left2
    ai "I broke a lot of rules."
    show mscmc smile
    ai "Like, {i}a lot{/i}."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I'm glad that she did. I can't imagine never having met her.)"
    show mscmc jacket_hairdown grin at left2
    show arianna siren smile behind mscmc at right1plus
    mcariannaprev "Good thing you're not the type to let rules stop you."
    mcariannaprev "You've completely changed my world."
    show arianna grin
    "She laughs a bit, her grip tightening on her necklace."
    ai "And you've changed mine."
    show mscmc smile
    "My eyes fall to her pink lips. I watch how they move."
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu
    "She licks at her bottom lip."
    show mscmc jacket_hairdown basic at left2
    show arianna siren basic behind mscmc at right1plus
    ai "I know no one believed Hamish earlier when he called me a mermaid, but still."
    ai "I need to lay low for a while."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Just when I thought Hamish couldn't mess with anything anymore.)"
    show mscmc jacket_hairdown sad at left2
    show arianna siren basic behind mscmc at right1plus
    mcariannaprev "Yeah, it's not a bad idea, but..."
    mcariannaprev "I'll miss you"
    show arianna surprised
    "Arianna raises her eyebrows at me and tilts her head with a smirk."
    show mscmc basic
    ai smile "Oh, how come?"
    show mscmc surprised
    "I scratch the back of my head, trying to play it off."
    mcariannaprev smile "You're a lot of fun."
    "My hand falls back down and Arianna touches the tips of her fingers to mine."
    ai grin "Is that it?"
    show mscmc embarrassed
    "Her voice grows soft as I lock my fingers with hers."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(How could that be it?)"
    show mscmc jacket_hairdown sleep at left2
    show arianna siren basic behind mscmc at right1plus
    mcariannaprev "Of course not."
    show mscmc basic
    show arianna sleep
    "Arianna drops my gaze after a moment and shrugs"
    ai "Well, at least I won't keep your from surfing anymore."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(There has to be a way to see her again.)"
    show mscmc jacket_hairdown basic at left2
    show arianna siren smile behind mscmc at right1plus
    ai "If you ever need any help, call me."
    show arianna:
        easein 0.5 right1
    "Arianna puts her other hand on my opposite cheek, pulling my face closer."
    scene arianna_s0_mini3 at bg with fade
    "She presses a soft, but searing kiss on my cheek."
    "My body is torn between leaning into her comforting hand or into her lips."
    "(She kissed me!)"
    scene bg msc_tide_pools_sunset at bg with dissolve
    pause 0.1
    show arianna siren_cu smile_cu at centre:
        transform_anchor True align (0.5, 0.5) yoffset 50 zoom 1.05 alpha 0.0
        linear 0.5 alpha 1.0 zoom 1.0
    "Arianna slowly pulls back, her hand sliding away from mine as she meets my eyes."
    ai "Bye [genericfn]."
    play sound big_splash
    show arianna siren smile at centre:
        yoffset -300
        pause 0.1
        linear 0.8 zoom 0.95 alpha 0.0 yoffset -250
    pause 0.5
    "She slips into the ocean, her tail splashing a faceful of water at me."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I know this isn't goodbye forever.)"

    scene bg msc_end at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
