label fiona_season1_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_saloon_night_lights at bg with fade
    play music wlleverydaycalm2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show fiona cloak_cu smile_cu at fiona_cu
    "I run my eyes thoughtfully up and down Fiona's body, then lean forward and tip her chin up with one finger."
    hide fiona
    show wllmc coat_cu smile_cu at wllmc_cu
    mcfiona "I say yes."
    mcfiona "A warm bed and an enthusiastic partner sounds a lot better than some cold boarding house."
    hide wllmc
    show fiona cloak_cu grin_cu at fiona_cu
    "Fiona's eyes get wide for a moment, then soften as she laughs and sets a hand on my cheek."
    mb "Wow, you never hide what you want. It might be my favorite thing about you."
    show fiona cloak_cu smirk_cu
    mb "But, uh, I was asking about the job. Though it's very good to know we're on the same page for when I have more free time."
    hide fiona
    show fiona cloak grin at right1
    show wllmc coat embarrassed at left1plus
    "I can't help flushing a little, but Fiona's simmering excitement stops me from feeling like a total fool."
    show wllmc coat smirk
    mcfiona "Did you doubt for a second where this was leading?"
    show fiona cloak smile
    "Fiona shrugs."
    mb "It's an area where my usual skills are lacking, since I've never had to guess before."
    show wllmc coat smallsmile
    mcfiona "That sounds dull. The uncertainty is half the thrill of the chase."
    show fiona cloak smirk
    mb "I'm certainly beginning to see that."
    hide wllmc
    hide fiona
    show cecelia coat basic at centre
    "Cecelia coughs dryly."
    show cecelia coat smirk
    vr "You've always had a habit of getting off topic, Fiona, but I didn't realize how terrifying that would be when doubled."
    show fiona cloak smile at left3
    show cecelia coat smirk at right3
    "Fiona turns her head to Cecelia and gives her a grin that isn't even slightly repentant."
    mb "Sorry, Cece darling."
    hide fiona
    hide cecelia
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(So I'm not the only one she gives ridiculous pet names to. That's... a little disappointing?)"
    hide wllmc
    show wllmc coat surprised at left3
    show fiona cloak smile at right3
    "Fiona looks back at me."
    mb "So how do you feel about working together?"
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Good question.)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e4c1:
        "I'm game.":
            $menuhideborder = False
            show wllmc coat smile at left3
            show fiona cloak smile at right3
            mcfiona "I'm game. I can't leave until I scrape together the money for a train ticket anyway."
            hide fiona
            hide wllmc
            show wllmc coat_cu smile_cu at wllmc_cu
            "(I'm pretty sure they'll have posters up with my face on them, so trying to hop another free trip would be a real bad idea.)"
            hide wllmc
            show wllmc coat smile at left3
            show fiona cloak grin at right3
            mb "Trust me, this job will more than cover a ticket to Serpent's River."
        "I have conditions.":
            $menuhideborder = False
            show wllmc coat basic at left3
            show fiona cloak smile at right3
            mcfiona "I have conditions?"
            show fiona cloak smirk
            mb "In addition to pay?"
            hide wllmc
            hide fiona
            show fiona cloak_cu smirk_cu at fiona_cu
            "Her smirk is very knowing."
            hide fiona
            show wllmc coat smile at left3
            show fiona cloak smirk at right3
            mcfiona "Obviously."
            mb "Well, whatever it is, I'm sure we can come to some... arrangement."
        "Is it paid?":
            $menuhideborder = False
            show wllmc coat smirk at left3
            show fiona cloak smile at right3
            mcfiona "Is it paid?"
            show fiona cloak smirk
            mb "Do you even have to ask?"
            mcfiona "Yes. I've seen too many people screwed over with jobs that use them up and don't offer fair compensation."
            show fiona cloak grin
            mb "Well, rest assured, this pays real silver."
    hide fiona
    hide wllmc
    show wllmc coat_cu smile_cu at wllmc_cu
    "(Alright. Time to push my luck.)"
    hide wllmc
    show wllmc coat smile at left3
    show fiona cloak smile at right3
    mcfiona "Also, I heard you guys have a bit of power."
    show fiona cloak smirk
    mb "Well. It seems a busy bee has been buzzing in your ear."
    show wllmc coat smirk
    mcfiona "Enough power to grant a pardon?"
    hide wllmc
    show cecelia coat angry at left3
    show fiona cloak surprised at right3
    "Fiona looks genuinely startled, and so does everyone else. Cecelia even narrows her eyes."
    hide cecelia
    hide fiona
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(They didn't think I was some kind of angel, did they?)"
    hide wllmc
    show fiona cloak_cu surprised_cu at fiona_cu
    mb "A pardon? Dear troublemaker, what on earth did you do?"
    hide fiona
    show wllmc coat smirk at left3
    show fiona cloak smirk at right3
    mb "You're not that warlock who raised a town of undead south of the border, are you?"
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Warlock? Town of undead?)"
    hide wllmc
    show wllmc coat smirk at left3
    show fiona cloak angry at right3
    mcfiona "I try not to truck with corpses unless it's absolutely necessary. In either direction."
    show fiona cloak grin
    "Fiona cackles."
    mb "Well that's a relief. Because high necromancy is the kind of thing even I couldn't let you get away with."
    hide fiona
    hide wllmc
    show wllmc coat_cu smile_cu at wllmc_cu
    "(She's such an odd creature, and yet so brazen and upfront with her oddities that it's impossible not to find them totally charming.)"
    hide wllmc
    show wllmc coat smile at left3
    show fiona cloak grin at right3
    mcfiona "If I assure you that my troubles are in the nature of misdemeanors, will you promise me that pardon?"
    show fiona cloak smirk
    mb "Since you're begging for it so cutely, I don't see how I can say no."
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "She holds out her hand to me."
    hide fiona
    show wllmc coat smile at left3
    show fiona cloak smile at right3
    mb "It's a deal, then? We're working together?"
    show wllmc coat surprised
    "I look at her hand."
    hide fiona
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Taking it means crossing a line of some kind. I feel like I can only see the consequences dimly, but I know they're there.)"
    hide wllmc
    show wllmc coat grin at left3:
        pause 0.1
        easein 0.5 left1
    show fiona cloak grin at right3
    mcfiona "It's a deal."
    "I close my hand over hers, and we shake firmly."
    hide fiona
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(And if this job gives me the opportunity to spend more time with Fiona herself, well then that's a nice side-effect.)"
    "(And nothing more.)"
    hide wllmc
    show wllmc coat grin at left3
    show nathan redcoat smile at right3
    wc "That took long enough."
    hide nathan
    show sascha belt smirk at right3
    sasch "It would have been shorter if Fiona weren't making such moon eyes at our new friend."
    hide wllmc
    show fiona cloak angry at left3
    mb "You two hold your tongues. Unless you want some of your secrets to start spilling."
    "She sticks her tongue out impishly at the two men."
    hide sascha
    show nathan redcoat surprised at right3
    wc "I think all our private matters can stay just so."
    hide fiona
    hide nathan
    show cecelia coat smirk at centre
    vr "Agreed."
    show fiona cloak angry at left3
    show cecelia coat basic at right3:
        pause 0.1
        easein 0.4 right2
    "She stands up and puts a hand on Fiona's shoulder."
    vr "I think asking for help is a good idea, Fiona, but don't let yourself get distracted."
    show fiona cloak basic
    show cecelia coat angry
    vr "I need your head in the game for this one."
    "Fiona reaches up, and closes her hand over Cecelia's."
    mb "Don't worry, Cece. I might get a bit giddy now and then, but you know how important this work is to me."
    hide fiona
    hide cecelia
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(It's a little jarring. I didn't realize she could be so serious.)"
    hide wllmc
    show wllmc coat surprised at centre
    "Something shifts in my stomach as the realization that I'm a brief, fun diversion to Fiona really hits me."
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(And what does that matter? Isn't she the same thing to me?)"
    hide wllmc
    show wllmc coat sad at centre
    "I don't find a satisfactory answer, so I just bury the thought deep and leave the bar with a wave to Ada."

    scene bg_wll_town_streets_night at bg
    show fog_effect:
        alpha 0.4
    with wiperightdissolve
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    "As soon as the five of us are outside Ada locks the door behind us, muttering about the paling sky in the east."
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(It's so misty out I don't know how she can tell.)"
    hide wllmc
    show fog_effect:
        alpha 0.4
    show nathan redcoat_hat smirk_hat at centre
    wc "That was the pleasantest night I've had in a while. Thank you for the company."
    show nathan redcoat_hat smirk_hat:
        pause 0.1
        linear 1.0 xoffset 800
    "He tips his hat to us and saunters off."
    hide nathan
    show sascha belt smirk_hat at left3
    show cecelia coat basic_hat at right3
    sasch "I need to grab something from the office. Walk me there, Cecelia?"
    show cecelia coat smirk_hat
    vr "Of course."
    hide sascha
    hide cecelia
    show wllmc coat_hat basic at left3
    show fiona hood basic_hood at right3
    "They leave too, and now it's just Fiona and I."
    show wllmc coat_hat surprised
    mcfiona "So... any idea where I'm sleeping tonight?"
    show wllmc coat_hat smirk
    "I raise an eyebrow at her."
    show fiona hood pout_hood
    mb "As much as I'd love it to be my bed, that bed is currently piled high with books, and they're not to be dislodged until the job is done."
    show wllmc coat_hat sad
    show fiona hood sad_hood
    mcfiona "So you're leaving me to suffer, then?"
    hide wllmc
    hide fiona
    show fiona hood_cu pout_hood_cu at fiona_cu
    mb "Oh I'll be suffering too, longing for a warm embrace as I pour over dusty tomes."
    hide fiona
    show fog_effect:
        alpha 0.4
    show wllmc coat_hat sad at left3
    show fiona hood pout_hood at right3
    "She tilts her head thoughtfully."
    show wllmc coat_hat surprised
    show fiona hood smirk_hood
    mb "You know, when I have a really difficult job, I like to order myself a bar of Xiconoc's premium chocolate."
    mb "The really good stuff with the chili flakes in it."
    show wllmc coat_hat smile
    mb "I buy it, but I don't open it, and the promise of it pushes me to finish more quickly."
    hide wllmc
    hide fiona

    $menuhideborder = True
    menu fionas1e4c2:
        "So you're saying I'm chocolate?":
            $menuhideborder = False
            show fog_effect:
                alpha 0.4
            show wllmc coat_hat smirk at left3
            show fiona hood smirk_hood at right3
            mcfiona "So you're saying I'm chocolate? Because if you think I'm sweet, you're sorely mistaken."
            mb "The chocolate I like isn't sweet. It's decadent and expensive and spicy and a little bitter."
            mcfiona "Oh, well in that case..."
            "I wink at her."
        "I'm an eat it all at once girl.":
            $menuhideborder = False
            show fog_effect:
                alpha 0.4
            show wllmc coat_hat smile at left3
            show fiona hood smirk_hood at right3
            mcfiona "When it comes to chocolate, I'm an eat it all at once kind of girl."
            mb "I'm sure you are."
            hide wllmc
            hide fiona

            show fiona hood_cu smirk_hood_cu at fiona_cu
            "The words are practically a purr."
            hide fiona
            show fog_effect:
                alpha 0.4
            show wllmc coat_hat smile at left3
            show fiona hood smirk_hood at right3
            mb "But can you linger in anticipation a little longer, just this once?"
            show wllmc coat_hat smirk
            mcfiona "Maybe. If you promise to appreciate my sacrifice."
        "I've done the same with good tequila.":
            $menuhideborder = False
            show fog_effect:
                alpha 0.4
            show wllmc coat_hat smile at left3
            show fiona hood smirk_hood at right3
            mcfiona "I've done the same with good tequila."
            mb "You know, maybe we should combine tactics. Have ourselves a little party when this is over."
            show wllmc coat_hat smirk
            mcfiona "Good food, strong drink, and just the two of us alone?"
            show fiona hood grin_hood
            mb "Exactly."
    show fiona hood grin_hood
    mb "The boarding house is down that way. You can't miss it. Tell Donna I sent you."
    show wllmc coat_hat surprised
    mcfiona "You're not going to walk me to my door?"
    show fiona hood sleep_hood:
        pause 0.2
        easein 0.5 right1
    "Fiona hesitates, then takes my hand in hers and kisses my knuckles."
    hide wllmc
    hide fiona
    show fiona hood_cu smile_hood_cu at fiona_cu
    mb "Willpower only gets me so far, sweet complication. So no, not tonight."
    hide fiona
    "She lets go and saunters off into the thickening fog."
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(It was clear and starry just a few hours ago. Where did all this come from?)"
    hide wllmc
    show wllmc coat_hat sad at centre
    "I start walking in the direction Fiona pointed me, but the fog is getting thicker and thicker, and my pace is slow."
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(If I don't take care I'm going to end up turned around and hopelessly lost.)"
    hide wllmc
    show wllmc coat_hat surprised at centre
    $sidecharone = "Distant Voice"
    sid1 "Ohhhh.... ohhhhhh...."
    "It's a sob so raw and anguished it rips right through me, though I can't tell where it's coming from."
    mcfiona "All well? You need help?"
    hide wllmc
    show fog_effect:
        alpha 0.6
    show sunmok ghost sad at centre:
        alpha 0.5 transform_anchor True zoom 0.9
        linear 1.0 zoom 1.0 alpha 1.0
    $sidecharone = "Voice"
    sid1 "Ohhhhhh..."
    "Out of the fog, someone lurches towards me."
    hide sunmok
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(Are they trying to pull a fast one?)"
    hide wllmc
    show wllmc coat_hat angry at left3
    show sunmok ghost sad at right3
    "I drop my hand to my pistol, and the cold weight of the metal comforts me."
    mcfiona "Hold it there, let me get a look at you."
    $sidecharone = "Strange Figure"
    sid1 "Ohhhhhh..."
    show wllmc coat_hat surprised
    "As it gets closer I see more of its form and face, but there's still something off."
    hide sunmok
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(Every instinct I have is screaming at me to run.)"
    hide wllmc
    show wllmc coat_hat sad at left3
    show sunmok ghost sad at right3
    "But I hold my ground, half from genuine concern and half from sheer bullheadedness."
    mcfiona "Ma'am, you look like you need a doctor."
    sid1 "Help..."
    hide wllmc
    show sunmok ghost sad at centre:
        transform_anchor True
        linear 0.6 zoom 1.05
    "She lurches closer again, the air gets a good fifteen degrees colder all at once, and my heart drops into my stomach."
    hide sunmok
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(That's not a person.)"
    hide wllmc
    show sunmok ghost sad at centre
    "From the waist up, sure she looks human, but her body trails into vapor where her legs should be."
    hide sunmok
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(A ghost?!)"
    hide wllmc
    show wllmc coat_hat sad at left3
    show sunmok ghost sad at right3
    $sidecharone = "Can't Be An Actual Ghost"
    sid1 "Missing... come closer..."
    "Its voice is horrible, raspy and distorted."
    hide sunmok
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(No.)"
    hide wllmc
    show wllmc coat_hat angry at left3
    show sunmok ghost sad at right3
    "It's the only word echoing through my mind, an abject refusal to accept the situation I'm in."
    hide wllmc
    hide sunmok
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(Bad luck and fancy card tricks are one thing, a ghost is quite another.)"
    hide wllmc
    show wllmc coat_hat angry at left3:
        pause 0.1
        linear 0.4 left4
    show sunmok ghost sad at right3
    "I take a step backwards, and a wind whips up around me."
    show wllmc coat_hat surprised
    $sidecharone = "Stupid Bullshit Phantom"
    sid1 "...the key... get home..."
    show sunmok ghost sad:
        easein 0.4 right1plus
    "It moves more quickly towards me, hands outstretched."
    hide wllmc
    hide sunmok
    show sunmok ghost_cu angry_cu at sunmok_cu
    $sidecharone = "Not Real, Go Away"
    sid1 "Give me... the key..."
    hide sunmok
    show mc_instinct at full_size:
        alpha 0.0
        linear 0.5 alpha 0.7
        linear 0.5 alpha 0.0
    show wllmc coat_hat_cu sad_cu at wllmc_cu
    "As its fingers touch me my whole body spasms, wracked with sudden agony."
    show wllmc coat_hat_cu angry_cu
    "(I need a way to fight it. No time to do anything else.)"
    hide wllmc
    $menuhideborder = True
    menu fionas1e4c3:
        "Shout at it.":
            $menuhideborder = False
            show wllmc coat_hat angry at left4
            show sunmok ghost angry at right1plus
            mcfiona "Don't come one step closer."
            hide sunmok
            hide wllmc
            show wllmc coat_hat_cu angry_cu at wllmc_cu
            show bg_wll_town_streets_night behind wllmc as pulse_effect:
                align(0.5, 0.5) transform_anchor True alpha 0.2
                linear 0.7 zoom 2.0 alpha 0.0
            pause 1.0
            hide wllmc
            hide pulse_effect
            show wllmc coat_hat surprised at centre
            "My voice echoes oddly, filled with a power beyond mere volume."
        "Push your hands out.":
            $menuhideborder = False
            show wllmc coat_hat angry at left4
            show sunmok ghost sad at right1plus
            "I fling my hands out in front of me, wishing I had a shield."
            hide sunmok
            hide wllmc
            show wllmc coat_hat_cu angry_cu at wllmc_cu
            "(Like one of those old knights in stories.)"
            show bg_wll_town_streets_night behind wllmc as pulse_effect:
                align(0.5, 0.5) transform_anchor True alpha 0.2
                linear 0.7 zoom 2.0 alpha 0.0
            pause 1.0
            hide wllmc
            hide pulse_effect
            show wllmc coat_hat surprised at left4
            show sunmok ghost angry at right1plus
            "The air ripples in front of me, seeming to somehow get thicker and heavier."
        "Throw something at it.":
            $menuhideborder = False
            show wllmc coat_hat angry at left4
            show sunmok ghost angry at right1plus
            "I glance around and spot a rock on the ground. I scoop it up at once and fling it forward."
            hide sunmok
            hide wllmc
            show wllmc coat_hat_cu angry_cu at wllmc_cu
            show bg_wll_town_streets_night behind wllmc as pulse_effect:
                align(0.5, 0.5) transform_anchor True alpha 0.2
                linear 0.7 zoom 2.0 alpha 0.0
            pause 1.0
            hide pulse_effect
            "(Take that, you stupid ghost.)"
            hide wllmc
            show wllmc coat_hat surprised at left4
            show sunmok ghost angry at right1plus
            "I expect it to pass through the ghost, and it does, but it has an effect all the same."
    hide wllmc
    hide sunmok
    show sunmok ghost angry at centre
    pause 0.1
    hide sunmok with dissolve
    "The ghost stops so suddenly it takes me by surprise, and its substance seems to dissipate."
    show sascha belt angry_hat at left3
    show fiona hood angry_hood at right3
    sasch "Away from here, lost soul! Return to the lonely ways from which you came."
    "I turn my head to see Sascha and Fiona running towards me. Sascha has some kind of talisman in his hand."
    show sascha belt smirk_hat
    sasch "Good thing you asked me to pick up that memoria necklace, Fiona. We wouldn't have found [genericfn] without it."
    show fiona hood surprised_hood
    mb "Or been able to dispel that ghost so quickly. Are you okay, [genericfn]?"
    hide sascha
    hide fiona
    show fiona hood_cu surprised_hood_cu at fiona_cu
    "There are no smiles or pet names as she rushes to my side, her hands gently touching my face."
    show fiona hood_cu sad_hood_cu
    mb "If only I'd seen something, this wouldn't have happened at all."
    hide fiona
    show fiona hood sad_hood at right1
    show wllmc coat_hat sad at left1plus
    "All the reserves I was calling on fade away under a tide of relief, and Fiona ends up supporting most of my weight as I slump against her."
    mcfiona "I'm fine. I just need a minute."
    show fiona hood basic_hood
    mb "Of course you do."
    hide wllmc
    show sascha belt basic_hat at left3
    show fiona hood angry_hood at right3
    "She cradles my head against her shoulder as she talks to Sascha."
    show fiona hood surprised_hood
    mb "I wasn't expecting the locket to start drawing specters to it this quickly."
    show sascha belt smirk_hat
    sasch "It certainly puts pressure on you time wise."
    "I straighten up, feeling more stable and also deeply embarrassed that I collapsed against Fiona like that."
    hide sascha
    hide fiona
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(I'm no fainting damsel, and I don't need her getting any kind of wrong impressions.)"
    hide wllmc
    show wllmc coat_hat angry at left1plus
    show fiona hood surprised_hood at right1plus
    mcfiona "Can we go back to the start for a second?"
    show wllmc coat_hat smirk
    show fiona hood smile_hood
    mb "Whatever you need. I was going to give you the details on the locket tomorrow, anyway."
    show wllmc coat_hat angry
    mcfiona "No, not the locket. The ghost. The actual, real-life ghost I just saw."
    show fiona hood surprised_hood
    "Sascha and Fiona exchange a glance."
    show fiona hood smirk_hood
    mb "Ghosts certainly can be a shock your first time seeing them."
    show wllmc coat_hat surprised
    mcfiona "You say that like you've seen them before. But it can't be so. Ghosts aren't real."
    show fiona hood surprised_hood
    "Another glance, this time with a lot more surprise in it."
    hide fiona
    show wllmc coat_hat surprised at left3
    show sascha belt smirk_hat at right3
    sasch "Whoever gave you your training, they sure left out a lot of the basics."
    show wllmc coat_hat angry
    "The implicit criticism in his words sends a wave of tension through me."
    hide sascha
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(This is going to be just like every other time.)"
    "(Time to get out before they run me out.)"
    hide wllmc
    show wllmc coat_hat sad at left3
    show sascha belt surprised_hat at right3
    mcfiona "Look, I've.... I'm sorry. This was a mistake."
    hide sascha
    hide wllmc
    show wllmc coat_hat_cu sad_cu at wllmc_cu
    "(I don't need psychic powers to know what happens next. My bad luck is as predictable as the sunrise.)"
    hide wllmc
    show wllmc coat_hat sad at left3
    show fiona hood surprised_hood at right3
    mcfiona "Sorry, Fiona. This job isn't for me after all."
    "My stomach churns at my own cowardice, but survivor's instinct overrules everything else, and I do what I've always done."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(I run.)"
    hide wllmc
    show fiona_s1_mini3 at bg
    with fade
    show cinema_fov at cinema_fov_in
    pause 1.0
    "But I've hardly taken ten steps when something closes over my wrist."
    show cinema_fov at cinema_fov_out
    hide fiona_s1_mini3
    hide cinema_fov
    show fiona hood_cu sad_hood_cu at fiona_cu
    with fade
    mb "Please, [genericfn]. Please don't go."
    hide fiona

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
