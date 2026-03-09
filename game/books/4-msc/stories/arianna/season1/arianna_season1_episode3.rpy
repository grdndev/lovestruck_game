label arianna_season1_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mansion_exterior_day at bg
    play music mschappytimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "The next day comes and Arianna and I follow the directions to Emporia's home."
    "It's nothing short of extravagant."
    show arianna dress surprised at right2
    show mscmc jacket_hairdown surprised at left1plus
    mcarianna "Wow, this is, uh..."
    ai "Freakin' huge."
    mcarianna grin "Did you say freakin'?"
    ai "Did I use it right?"
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(There are a few words I'd like to teach Arianna.)"
    show arianna dress basic behind mscmc at right2
    show mscmc jacket_hairdown grin at left1plus
    mcarianna "Perfectly. Now then, are you ready?"
    "Arianna nods, but her hand moves up to grip her necklace."
    hide arianna
    hide mscmc

    $ menuhideborder = True
    menu ariannas1e3c1:
        "A. Don't worry.":
            $ menuhideborder = False
            show arianna dress basic behind mscmc at right2
            show mscmc jacket_hairdown grin at left1plus
            mcarianna "Hey, don't worry too much about it."
            mcarianna "I'm sure everything's going to go well and I'll be right here."
            ai grin "Yeah, you're right. I got this."
        "B. We can always leave.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(I know she's nervous--this is her first real commission.)"
            show arianna dress basic behind mscmc at right2
            show mscmc jacket_hairdown grin at left1plus
            mcarianna "If you decide you don't like what's going on, we can leave."
            mcarianna "You're the artist here, not Emporia."
        "C. This is what you wanted.":
            $ menuhideborder = False
            show arianna dress basic behind mscmc at right2
            show mscmc jacket_hairdown grin at left1plus
            mcarianna "This could be the big break you want--don't work yourself up."
            mcarianna "Think about the future Arianna."
            ai grin "She has a lot of human money and is a revered artist."
            mcarianna "Exactly."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    hide arianna
    hide mscmc
    "I take the lead and knock a few times on the door. Almost instantly it opens to a man in a suit."
    show arianna dress grin at right2
    show mscmc jacket_hairdown grin at left1plus
    mcarianna "Hello, we're here to meet Emporia. This is Arianna Nitida and I'm-"
    hide arianna
    hide mscmc
    "Butler" "Right this way."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(A bit rude.)"

    scene bg msc_mansion_interior_day at bg with dissolve
    "He throws his arm out to usher us in and then leads us down the hall with his hands behind his back."
    "The butler leads us to a large and extravagant living room."
    "Butler" "Ms. Lid will be with you shortly. Please wait a moment while I fetch her."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(This couch is about as stiff as a plank.)"
    hide mscmc
    show emporia casual basic mask at centre:
        alpha 0.0 xoffset -100
        linear 0.5 alpha 1.0 xoffset 0
    "A few minutes pass, then a woman in a dress and a fancy mask over her face walks in and goes straight to Arianna."
    bn smile "Arianna Nitida, what an honor it is to meet you in the flesh."
    bn "I am, of course {i}the{/i} Emporia Lid."
    hide emporia
    show arianna dress grin at right2
    show mscmc jacket_hairdown grin at left1plus
    ai "Hi, I'm Arianna and this is my manager, [genericfn]."
    mcarianna "We spoke on the phone."
    hide arianna
    hide mscmc
    show emporia casual basic mask at centre:
        pause 0.2
        linear 0.4 xoffset 40
    "She regards me with cold eyes as she rests her arm atop a shelf."
    show emporia angry:
        pause 0.2
        easein_back 0.4 xoffset -20
    "Emporia gasps, flinching away from the shelf."
    bn "Ugh, honestly my people don't know how to do their jobs. It's covered in dust!"
    bn sad "What do I pay them for? It's pathetic."
    show emporia smile
    "Emporia, arms close to her body now, suddenly shrugs and smiles at Arianna."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(The sudden mood shifts are intense. And what's with the mask over her face?)"
    hide mscmc
    show emporia casual smile mask at left2
    show arianna dress basic at right3
    bn "Arianna, your art is {i}exquisite{/i}."
    bn "It would please me very much to have an original of yours. Multiple if you are able."
    ai grin "Did you have anything in mind?"
    show arianna smile
    bn "I have but an essense in mind and the rest I shall leave for you to determine."
    "Emporia sits across from Arianna."
    bn "I want you to capture the beauty of the ocean. The waves. The shore."
    bn "The {i}sealife{/i}."
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "The overennunciation of 'sealife' sets me on edge."
    "(I can't keep getting anxious thinking people know about Arianna.)"
    show mscmc angry_cu
    "(But regardless, I don't like Emporia's demeanor.)"
    hide mscmc
    show emporia casual smile mask at left2
    show arianna dress grin at right3
    "Arianna doesn't seem to be bothered at all. In fact, she looks very interested."
    bn "I want you to create what you think defines the ocean's beauty."
    show emporia basic
    show arianna smile
    "Emporia's eyes flick down as she drags a finger over the table, inspecting it for dust after."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(There isn't a speck of dust anywhere in this place.)"
    hide mscmc
    show emporia casual smile mask at left2
    show arianna dress smile at right3
    bn "I fully intend to match whatever price you desire."
    ai surprised "Um, well, since you don't have anything specific in mind, it's a little hard to gauge."
    ai "Could we do an hourly rate and go by how many hours I work on the project?"
    bn "Whatever you desire, Arianna. No price is too high for one such as myself."
    hide arianna
    show mscmc jacket_hairdown basic at right3
    mcarianna "Is that so?"
    bn sad "Oh, silly me, I'd nearly forgotten you were even here."
    bn "What a quiet {i}manager{/i} you are."
    mcarianna angry "Just doing my job."
    show mscmc basic
    bn "I think Arianna and I are settled here if you'd like to take your leave."
    hide emporia
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(God, why does she want Arianna alone so badly?)"
    show emporia casual sad mask at left2
    show mscmc jacket_hairdown basic at right3
    mcarianna "I'm good."
    hide mscmc
    show emporia basic
    show arianna dress grin at right3
    ai "I don't think we have that much more to talk about anyways at this point."
    ai "Do you need these pieces by a specific date?"
    bn smile "I can't rush perfection, now can I? Please, take your dear time with them."
    ai "Then, I'll get started and have my manager contact you when I'm ready to show you the first of the three pieces."
    ai "I should be able to offer a timeframe once I know what kind of work I'll be doing."
    bn "Sounds delightful--I can't wait."
    hide arianna
    hide emporia
    "They go quiet and there's nothing but the distant sound of a grandfather clock ticking."
    show emporia casual basic mask at left2
    show mscmc jacket_hairdown basic at right3
    mcarianna "Well, if that's all, then we should get going. Arianna should get started."
    bn smile "Yes, of course. I'll see you out."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    scene bg msc_mansion_exterior_day at bg with fade
    "As soon as the butler shuts the door behind us, Arianna bumps against me with an elated laugh."
    show arianna dress grin at right1:
        xoffset 30
        pause 0.2
        easein_back 0.4 xoffset 0
    show mscmc jacket_hairdown smile at left1
    ai "I can't believe it! I'm actually going to get paid for my work."
    "Arianna claps her hands together with a squeal of delight."
    ai "I've worked so hard and gone unnoticed for so long. It feels amazing!"
    ai "And especially for it to be some rich elite? I could make it really expensive."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I'm happy for Arianna, but I can't shake the weirdness around Emporia."
    show mscmc sad_cu
    "(Something's up with her.)"
    show arianna dress grin behind mscmc at right1
    show mscmc jacket_hairdown surprised at left1
    mcarianna "Emporia was kinda weird though, wasn't she?"
    show arianna smile
    "Arianna shrugs."
    ai grin "Art people are always weird."
    show arianna basic
    mcarianna sad "And what was up with her talking down about her staff?"
    mcarianna basic "Every surface in there looked clean enough to eat off of."
    ai smile "Look, she might be some rich snob, but she's still giving me a big break."

    scene bg msc_boardwalk_day_people at bg
    show arianna dress smile at right1
    show mscmc jacket_hairdown sad at left1
    with dissolve
    show arianna:
        linear 0.5 right1plus
    "As we get back to the boardwalk, Arianna steps in front of me and puts a hand on my shoulder."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    ai "We don't need to like her. She's just a client."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Even when I talked on the phone with Emporia, she had that burst of irritation.)"
    "(Maybe it's just me? I've never been able to get along with people like Emporia.)"
    mcarianna basic_cu "I know, I know."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Don't be so serious! I just got a job, [genericfn]!"
    "Arianna drops her hand from my shoulder and grins at me."
    ai embarrassed_cu "Want to go for a celebratory swim?"
    ai "I'm happy and nervous and you helped me and all I want is to spend time with you."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Is this a tails out swim?"

    scene arianna_s1_mini1 at bg with dissolve
    "Arianna offers her hand to me with a few nods."
    ai "Why would I be swimming with these fake legs of mine?"
    ai "I know this kind of secret cove pretty close by. No one else will see us."
    "(I don't usually take a lot of time to just relax and do whatever I want.)"
    "(But all I can think about is spending time with Arianna.)"

    $ menuhideborder = True
    menu ariannas1e3c2:
        "A. Yes! Secret cove swim with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            scene bg msc_boardwalk_day_people at bg
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            with dissolve
            "(If Arianna wants to celebrate with a swim, that's what we'll do.)"
            "(While I might not like Emporia, I am proud of Arianna.)"
            show arianna dress grin at right1
            show mscmc jacket_hairdown grin at left1plus:
                pause 0.2
                easein_back 0.4 left1
            "I place my hand in hers."
            mcarianna "Then let's go swimming! You know I love the water."
            ai "Which is why we're perfect for each other."
            show mscmc embarrassed
            "The back of my neck heats up as she catches my gaze."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Does she mean more when she says that?)"
            "(Not that I need more, but...ugh, don't overthink!)"
            show mscmc jacket_hairdown grin at left1
            show arianna dress smile at right1
            mcarianna "So, where are we going?"
            ai grin "Come with me."
            "With a sing-songy voice and a dramatic wave of her hand, Arianna starts walking backwards."
            mcarianna "How mysterious."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Makes me think of how weird I though she was when she told me she was a mermaid.)"
            show mscmc embarrassed_cu
            "(To think I'd be here with her now.)"

            stop music fadeout 0.5
            play music mscbeach fadein 1.0
            scene bg msc_tide_pools_day at bg with dissolve
            "Arianna takes me to a more secluded part of the beach hidden by a rock wall."
            show arianna dress grin at centre
            ai "Race you to the water?"
            show arianna:
                easeout 0.5 xoffset 100 alpha 0.0
            "She's already running."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Hey!"
            hide mscmc
            "Arianna might have longer legs, but I've had legs my whole life."
            play sound big_splash
            "I reach the water first and watch as Arianna runs past me and dives under a wave."
            show arianna siren smile at left1:
                yoffset 480 alpha 0.0 xoffset 40
                parallel:
                    linear 0.4 alpha 1.0
                parallel:
                    easein 0.4 yoffset 0
            "When she surfaces, she's floating on her back with the tip of her tail poking out."
            ai grin "Ah, it feels so nice to have my tail."
            "The water glistens and shines along it and I feel like my breath is gone."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Seeing her tail will never get old. It's incredible and stunning and just straight up cool.)"
            show arianna siren smile at right3
            show mscmc bikini_hairdown smile at left2:
                alpha 0.0 xoffset -100
                linear 0.5 alpha 1.0 xoffset 0
            "As I wade over to her, I can see the tips of her ears poking through her wet hair."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(It's still hard to believe that she's a mermaid. I know a mermaid. How wild is that?)"
            show mscmc bikini_hairdown embarrassed at left2
            show arianna siren embarrassed at right3
            ai "See something you like?"
            "Arianna tilts her head at me with a smirk, flicking the tip of her tail down."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Oh, I see {i}a lot{/i} that I like.)"
            show mscmc bikini_hairdown grin at left2
            show arianna siren embarrassed at right3
            mcarianna "Yeah, a really big fish."
            play sound big_splash
            show arianna:
                easein_back 0.5 xoffset -50
            show mscmc:
                pause 0.2
                easein_back 0.5 xoffset -50
            "Her tail smacks down and sends a wave of water over me."
            ai grin "Wanna try that again?"
            "I wipe the water from my eyes and laugh."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu:
                xoffset 0
            mcarianna "Sorry."
            hide mscmc
            show arianna siren_cu grin_cu at arianna_cu
            ai "You're forgiven."
            show mscmc bikini_hairdown smile at left1plus
            show arianna siren smile at right6:
                parallel:
                    linear 1.0 xoffset -300 knot -30 knot -20 knot -200 knot -320
                parallel:
                    linear 1.0 yoffset 50 knot 80 knot 150 knot 150 knot 80
            "Arianna's tail dips underwater as she swims around me, doing a small twirl in the water."
            ai surprised "All of this Emporia business has me thinking I should get back into meditating."
            show arianna smile
            mcarianna surprised "You meditate?"
            hide arianna
            show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
            "(She's so...carefree that meditating doesn't seem like her speed at all.)"
            hide mscmc
            "We swim out to deeper water, Arianna slowing her swim speed for me."
            show arianna siren surprised at right1plus
            show mscmc bikini_hairdown smile at left1
            ai "Sometimes. It helps to, I don't know, calm my thoughts?"
            ai sad "If I'm particularly stressed or anxious, it helps me feel more relaxed and grounded."
            show arianna smile
            mcarianna grin "I would love to shut my brain up."
            ai "We should do it together sometime! I'm not the best at it, but I could help you out."
            mcarianna "Might be nice."
            show arianna:
                parallel:
                    linear 0.4 yoffset 130
                    linear 0.4 yoffset 30
                parallel:
                    easein 0.2 xoffset 150
                    linear 0.2 xoffset 0
                    linear 0.2 xoffset -80
                    linear 0.2 xoffset 0
            "Arianna swims a tight circle around."
            hide arianna
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(Speaking of being relaxed, I actually feel good right now.)"
            "(This is nice.)"
            hide mscmc
            "I'm ready to close my eyes and float on my back when Arianna gasps."
            show arianna siren_cu grin_cu at arianna_cu
            ai "Look, a turtle!"
            hide arianna
            show vfx_msc_acc_sea_turtle as turtle:
                align (0.5, 0.5) transform_anchor True zoom 1.3
            "Arianna stops swimming beside me as a large sea turtle swims up to us."
            hide turtle
            show arianna siren grin at centre:
                xoffset -50
            ai "Hello there, I hope you're doing well today."
            hide arianna
            show vfx_msc_acc_sea_turtle as turtle:
                align (0.5, 0.5) transform_anchor True zoom 1.3
            "The turtle goes up to Arianna, looking at her."
            hide turtle
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(Wait...is she talking to it?)"
            hide mscmc
            show arianna siren grin at centre:
                xoffset -50
            ai "The water's nice and peaceful over here, isn't it?"
            hide arianna
            show vfx_msc_acc_sea_turtle as turtle:
                align (0.5, 0.5) transform_anchor True zoom 1.3
            "Arianna moves over so that the turtle can swim past us."
            hide turtle
            show arianna siren smile at right2
            show mscmc bikini_hairdown surprised at left1plus
            mcarianna "Can you talk to sea creatures?"
            show arianna grin
            "Arianna laughs and shakes her head."
            show mscmc smile
            ai "No, turtles are just very respected amongst mers."
            ai "They live for so long and we usually think they're good omens."
            mcarianna grin "I always like it when I see a turtle head pop up in the water."
            mcarianna "Makes me feel like I have a surfing buddy."
            ai "I'm sure they like watching you."
            "With the water behind her and a soft smile on her face, Arianna looks radiant."
            hide arianna
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I hope we can keep being together like this.)"
            show arianna siren embarrassed behind mscmc at right2
            show mscmc bikini_hairdown smile at left1plus
            ai "Soo...can you talk to land animals?"
            mcarianna grin "All humans can."
            show arianna sad
            "The sly smirk on her face is replaced with a confused frown."
            ai "You're kidding, right?"
            mcarianna "I'm not kidding."
            show arianna grin:
                easein_back 0.5 xoffset -50
            show mscmc:
                pause 0.2
                easein_back 0.5 xoffset -50
            "When I start grinning, Arianna pushes me away with a laugh."
            ai embarrassed "As if I'd ever fall for that."

        "B. Gotta get to work.":
            $ menuhideborder = False
            scene bg msc_boarwalk_day_people at bg
            show mscmc jacket_hairdown sad at left1
            show arianna dress basic at right1
            with dissolve
            mcarianna "I can't--I'm sorry. Trina asked me to come in early to work today."
            mcarianna smile "But I promise we'll find some way to celebrate soon."
            show mscmc basic
            ai smile "Really?"
            show arianna surprised
            mcarianna grin "Of course, this is huge for you."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I would've loved to have seen her tail again after all this time, but I can't right now.)"
            show mscmc sleep_cu
            "(Duty calls.)"

    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    scene bg msc_surf_shop_day at bg with fade
    "Arianna goes back to her studio to start working and I'm back at the shop with Trina."
    show mscmc jacket_hairdown basic at left1plus
    show trina casual sad at right1plus
    so "Do you think I could rock a mullet?"
    mcarianna grin "Hell yeah."
    play sound phone_ringing
    hide mscmc
    hide trina
    stop music fadeout 0.5
    play music mscromance fadein 1.0
    "I'm about to search for good mullet pictures on my phone when it rings."
    show mscmc jacket_hairdown grin at centre
    mcarianna "Hello?"
    hide mscmc
    "???" "Hi, [genericfn] [genericln]? This is Phil with High Tide Sports."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(They must be calling about the sponsorship!)"
    show mscmc jacket_hairdown grin at centre
    mcarianna "Oh, hi! Yeah this is she."
    hide mscmc
    show trina casual smile at centre
    "Trina looks over at me with a questioning brow."
    hide trina
    "Phil" "You're close with Trina's Surf Shop, correct? It's tagged in most of your online profiles."
    show mscmc jacket_hairdown grin at centre
    mcarianna "I am, yes. It's very close to my heart."
    hide mscmc
    "Phil" "We couldn't help but notice all of the negative attention that it's been getting lately."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Uh oh.)"
    hide mscmc
    "Phil" "Nearly 60\% of the reviews are rather terrible. Which has caused some pause in bringing you on as an ambassador for the brand."
    show mscmc jacket_hairdown surprised at centre
    mcarianna "Well, we're almost positive it's just the same person over and over again."
    mcarianna sad "Trina's Surf Shop is great, I promise."
    hide mscmc
    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    "Phil" "While that may be the case, we can't take a risk in being associated with such a place."
    "Phil" "Bad attention is still bad attention."
    "Phil" "Please try to get this surf shop troll situation sorted or else we may need to look for someone else to work with."
    "Phil" "Thank you--have a good afternoon."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I could lose my sponsorship over this?)"
    show mscmc jacket_hairdown sad at left1
    show trina casual basic at right2
    so "Was that about my shop?"
    mcarianna surprised "It was {i}Phil{/i} with High Tide Sports."
    mcarianna sad "He said your shop is getting bad rep and they don't want to sponsor someone associated with this store."
    show trina angry
    "Trina throws her hands up with a groan."
    so "Oh my god, it's Hamish. His dumbass manages to get in the way of everything."
    mcarianna "Well we need to fix it, Trina!"
    so "I'll fix it alright. The next time I see him-!"
    hide mscmc
    hide trina
    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    show hamish casual basic at centre with dissolve
    "The shop door opens."
    hide hamish
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Speak of the devil.)"
    hide mscmc
    show hamish casual smile at centre
    rm "The owner is rude and vulgar. The shop sells overpriced cheap imitations."
    "Hamish is holding his phone up high, typing with one finger."
    hide hamish
    show trina casual angry at centre
    so "You've got to be kidding me."
    hide trina
    show hamish casual smile at centre
    rm "I believe the surfing classes are a front for a laundering business."
    show hamish basic
    "He jams his finger onto the screen one last time."
    rm smile "Post."
    hide hamish
    show mscmc jacket_hairdown angry at left1plus
    show trina casual angry at right1plus
    so "You better delete that before I shove your phone up your ass."
    mcarianna "And if Trina doesn't do it, I will."
    hide mscmc
    hide trina
    show hamish casual smile at centre
    rm "This is America. Free speech."
    hide hamish
    show mscmc jacket_hairdown angry at left1plus
    show trina casual angry at right1plus
    mcarianna "It's not free speech, it's libel, you rat."
    hide mscmc
    hide trina
    show hamish casual basic at centre
    "He folds his hands together"
    show hamish smile at left3
    show mscmc jacket_hairdown basic at right4
    rm "[genericfn], I heard you're in the middle of a deal with High Tide."
    hide hamish
    hide mscmc
    show trina casual angry at centre
    so "Here we go."
    hide trina
    show hamish casual angry at left3
    show mscmc jacket_hairdown basic at right3
    rm "You know they're my water gear brand's biggest competition."
    mcarianna angry "Your gear sucks so bad that it's in competition with itself."
    show mscmc basic
    rm smile "I have a brand and you have a large following."
    show mscmc surprised
    rm "Be an ambassador for my company instead of High Tide or I'll keep posting bad reviews."
    mcarianna angry "Ew."
    hide mscmc
    show hamish angry
    show trina casual angry at right3
    so "Gross."
    hide trina
    show mscmc jacket_hairdown angry at right3
    mcarianna "I wouldn't be caught dead in one of your wetsuits."
    "Hamish crosses his arms with a 'hmph'."
    rm smile "Do you want me to stop posting reviews or not?"
    mcarianna "What would be the point if I worked for you instead?"
    rm angry "Then I will crush this shop under my boots!"
    hide hamish
    hide mscmc
    show trina casual angry at centre
    "Trina comes around the corner and grabs a broom."
    so "Alright, I've had enough. Get off my lawn, Hamish."
    "Trina sticks the broom out like a lance, poking it towards Hamish as she moves towards him."
    hide trina
    show hamish casual angry at centre
    "He bats it away at first."
    rm "This is assault! I could have you arrested for this."
    hide hamish
    show trina casual smile at centre
    so "It's not assault until I hit you, so I recommend you get out."

    hide trina
    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show hamish casual angry at centre:
        pause 0.3
        linear 0.4 alpha 0.0 xoffset 100
    "Hamish leaves with a growl under his breath."
    hide hamish

    $ menuhideborder = True
    menu ariannas1e3c3:
        "A. What's wrong with him?":
            $ menuhideborder = False
            show mscmc jacket_hairdown sad at left1plus
            show trina casual angry at right1plus
            mcarianna "Is it really possible for someone to be this annoying?"
            mcarianna "Seriously, what's the matter with him?"
            so "A long list of things that I could write a trilogy about."
        "B. I'm screwed.":
            $ menuhideborder = False
            show mscmc jacket_hairdown sad at left1plus
            show trina casual angry at right1plus
            "I cover my face with my hands."
            hide trina
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Hamish is impossible.)"
            show mscmc jacket_hairdown sad at left1plus
            show trina casual sad at right1plus
            mcarianna "It's over. He's ruined everything."
            so "No, don't say that. We have time."
        "C. What do we do?":
            $ menuhideborder = False
            show mscmc jacket_hairdown sad at left1plus
            show trina casual angry at right1plus
            mcarianna "Great. What a shit day."
            mcarianna "What're we gonna do?"
            so "Throw rocks through his windows?"
            mcarianna "That'll be Plan B."

    so sad "We're gonna get this sorted. Hamish isn't that smart."
    mcarianna "No, but he knows how to be annoying."
    so angry "And so do we. We'll fix this."
    hide mscmc
    hide trina
    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    "The door opens again and Trina lunges for her broom once more."
    show trina casual sad at left2
    show maxime casual basic at right2
    so "Oh, it's just you. Sorry."
    hide trina
    show mscmc jacket_hairdown basic at left2
    "Maxime doesn't even flinch in the face of Trina's broom and instead walks towards me."
    mx "I need to ask you something."
    mcarianna surprised "What's up?"
    mx sad "Have you seen anyone strange hanging around lately?"
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I thought his question was going to be about surfing.)"
    show mscmc jacket_hairdown surprised at left2
    show maxime casual sad at right2
    mx "A woman who may seem a little off or eccentric. Like she isn't from around here."
    mcarianna "Uhhh, I don't think so."
    "He nods, looking a bit disappointed."
    mx "Well, let me know if you run into anyone."
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(A strange woman like Emporia? I mean, there's no way it'd be about her.)"
    show mscmc sad_cu
    "(Or maybe...is he talking about Arianna? Why would he be asking about her?)"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
