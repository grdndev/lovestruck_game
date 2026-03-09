label lexip_season1_episode5:

    $tbc = False
    scene bg msc_boardwalk_night_lights at bg
    play music mscloveinterest

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show lexi casual_cu bigsmile_cu at lexi_cu
    "I prepare myself for a kiss but instead feel her arms squeeze tightly around my torso."

    "I hug Lexi back, squeezing her as tightly as she's squeezing me before letting go."
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mclexi "You're a really good hugger."
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "That's not all I'm good at."

    "Lexi grins as she raises an eyebrow suggestively at me."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She probably would be a good kisser... Ah! Why is that the first thing I think of?)"
    stop music fadeout 1.0
    play music msctense
    hide mscmc
    show diver suit basic snorkel:
        easein 0.6 xpos 500
    pause
    show diver suit basic snorkel:
        xpos 500
        easein 0.6 xpos 1950
    "Suddenly, I see one of the divers that was with Ned walking down the boardwalk."
    hide diver
    show mscmc jacket_hairdown surprised at left3
    show lexi casual surprised at right3
    mclexi "Crap! Come here!"
    show mscmc jacket_hairdown surprised:
        easein 0.4 xpos 600
    pause
    show mscmc jacket_hairdown surprised:
        easein 0.4 xpos 400
    show lexi casual surprised:
        easein 0.4 xpos 600
    "I pull Lexi to me as one of Ned's diver lackeys walks by."
    show mscmc jacket_hairdown angry
    mclexi "One of Ned's divers is over there."

    mclexi "It looks like he's headed to the marina..."
    show mscmc jacket_hairdown basic
    show lexi casual basic
    lx "That's where Ned parks the yacht at night."
    show mscmc jacket_hairdown surprised
    show lexi casual basic:
        easein 0.4 xpos 550
    "As we stand there, Lexi casually leans into me."

    lx "It's fine. That diver didn't see us."
    show mscmc jacket_hairdown smile
    mclexi "Yeah. We should be careful, though."

    lx "Wanna head back to the shop?"

    "I nod"
    scene bg msc_mc_bedroom_night_lights at bg with wipeleft
    stop music fadeout 1.0
    play music mscromance
    pause
    show lexi casual bigsmile at centre
    lx "Oof."

    "Lexi falls face-first onto my bed."

    lx "Land beds feel so different from underwater ones! I love this!"

    lx "Do you mind if I sleep over again?"
    show mscmc casual_hairdown smile at left3
    show lexi casual surprised at right3
    mclexi "That's fine. I'll take the floor."
    show lexi casual sad
    lx "What?! No! I don't want to make you sleep on the floor. Maybe we could..."
    show lexi casual embarrassed
    "Lexi looks away like she's embarrassed."
    show mscmc casual_hairdown surprised
    lx "We could sleep together if you're okay with that."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Sleep together?!)"
    hide mscmc
    show mscmc casual_hairdown embarrassed at left3
    show lexi casual embarrassed at right3
    "My brain feels like it's about to explode as I imagine sleeping with Lexi next to me."

    mclexi "I... yea, that's fine. If you're okay with it."
    hide lexi
    hide mscmc
    show lexi casual bigsmile at centre
    "Lexi nods and rolls onto her back, looking up through the skylight."
    show mscmc casual_hairdown smile at left3
    show lexi casual bigsmile at right3
    lx "This will be awesome! Do you have any cards?"

    mclexi "Yeah, do you know any games?"
    show lexi casual smile
    lx "I know a few human games, but would you want to learn a mer game?"
    show mscmc casual_hairdown grin
    mclexi "Heck yea I do! That'd be so cool!"

    "The next few hours pass with Lexi and I playing and teaching each other card games while listening to music."
    hide lexi
    hide mscmc
    "As it starts to get late, we eventually decide to call it a night and both get under the covers."
    show bg msc_mc_bedroom_night at bg with dissolve
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(We're in the same bed. But we're just friends. Friends who are pretending to be dating.)"
    show mscmc casual_hairdown_cu surprised_cu
    "(Why am I freaking out! This is just the adrenaline of everything that's happened over the last few days.)"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "Are you asleep?"
    hide lexi
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mclexi "No... I'm too amped up about finding the treasure tomorrow."
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "I'm pretty excited, too. The sky is clear and the moon's out. We should do one of my favorite things, a midnight swim!"

    lx "What do you think?"
    hide lexi
    $menuhideborder = True
    menu lexis0e5c1:
        "A. Midnight swim with Lexi!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            stop music fadeout 1.0
            play music msclexi
            scene bg msc_labeach_night at bg with clockwise_wipe
            show mscmc bikini_hairdown surprised at left3
            show lexi swim bigsmile at right3
            lx "I’ll race you to the water!"
            show lexi swim bigsmile:
                easein 0.7 xpos -150
            "Before I can respond Lexi dashes past me."
            hide lexi
            show mscmc bikini_hairdown angry
            mclexi "That’s cheating!"
            show mscmc bikini_hairdown angry:
                easein 0.7 xpos -150
            "I race after her, the cool night breeze blowing in my face."
            hide mscmc
            show lexi swim bigsmile at centre
            lx "I win!"

            "I trot up behind Lexi as she steps into the water and marvel at how carefree she seems as she looks back and smiles at me."
            hide lexi
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(When she’s smiling at me my heart feels like it does when I’m surfing, like I’m in a whole different world.)"
            hide mscmc
            show lexi swim bigsmile at centre
            "As I stand lost in my thoughts, Lexi wades further out."
            #flashing animation
            show lexi mermaid bigsmile at centre with dissolve
            "A bright shine lights up the water and Lexi’s legs transform into her tail."

            lx "Are you coming in?"

            "Lexi beckons me with her hand as she lies on her back."
            hide lexi
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(Her scales are like crystals reflecting the light...)"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "I stare for several moments before I realize I’m holding my breath and Lexi is waiting for me."
            hide lexi
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(That’s so embarrassing! What if she saw me staring?)"
            hide mscmc
            show mscmc bikini_hairdown surprised at left3
            show lexi mermaid smile at right3:
                easein 0.9 ypos 1100
            "As I wade into the water after Lexi she disappears under the dark ocean waves."
            hide lexi
            mclexi "Where-?"
            show lexi mermaid bigsmile at right3:
                ypos 1100
                easein 0.9 ypos -25
            "Salty water splashes in my face and I see Lexi laughing hysterically."
            show mscmc bikini_hairdown grin
            mclexi "Why you!"
            hide mscmc
            hide lexi
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(If she wants a splash fight I’ll give her one!)"
            hide mscmc
            show mscmc bikini_hairdown grin at left3:
                easein 0.4 xpos 500
                easein 0.4 xpos 400
            show lexi mermaid bigsmile at right3
            "I splash Lexi back, while sputtering and laughing, trying my best to get as much as I can in her face as payback."
            show lexi mermaid smile
            lx "Pathetic!"
            show mscmc bikini_hairdown surprised
            show lexi mermaid smile:
                easein 0.4 ypos -30
                easein 0.4 ypos -25
            "As I wind back to launch another attack, Lexi sends a massive amount of water at me using the fin at the end of her tail."
            show mscmc bikini_hairdown angry
            show lexi mermaid bigsmile
            "Water fills my mouth as I try to retaliate, but in the end, all I can do is sputter in protest."
            show mscmc bikini_hairdown grin
            mclexi "That’s definitely not fair!"
            show mscmc bikini_hairdown surprised
            show lexi mermaid smile
            lx "Maybe not. But I still win."

            mclexi "You won’t next time."
            hide lexi
            hide mscmc
            "Relaxing my body, I float on my back and look at the sky."
            show mscmc bikini_hairdown smile at left2
            show lexi mermaid embarrassed at right2:
                easein 0.4
            "Barely making a sound in the water, Lexi joins me and we lie on top of the water next to one another."

            lx "It’s almost a full moon."
            show mscmc bikini_hairdown embarrassed behind lexi:
                easein 0.4 xpos 500
            show lexi mermaid embarrassed:
                easein 0.4 xpos 600
            "As we float the water slowly pushes us closer together until we’re barely touching."
            hide mscmc
            hide lexi
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(This feels so natural. Like this is how life should be every day. Having her here...)"
            show mscmc bikini_hairdown_cu surprised_cu
            mclexi "Is the moon special to mermaids at all?"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "Well, there are some superstitious sayings about romance, but it’s a bunch of fish poop. None of those sayings are ever true."
            show lexi mermaid_cu bigsmile_cu
            lx "To me, it doesn't really matter if it’s true or not though. Just knowing how powerful the moon is fills me with wonder."
            hide lexi
            "Our arms press together as the waves carry us and neither of us makes a move to put space between us."
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            mclexi "Powerful?"
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "The moon controls the tides which affect the weather and ocean currents."

            lx "It’s easy to think that something so far away makes that much of an impact on our lives."
            hide lexi
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mclexi "I had never thought of it that way, but you’re right. It’s almost as crazy as realizing mermaids exist."
            hide mscmc
            "We don’t say anything for a while and I start to feel sleepy as we bob together."
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            mclexi "This is so relaxing. I wish I could be out here in the water all the time. Like, never go back to land kind of all the time."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "Oh? That’s a pretty mer type feeling to have. Are you sure you’re not hiding a tail from me?"
            hide lexi
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "I chuckle at the idea."

            mclexi "I wish. That’d be amazing."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "Hmm... I don’t know. You’re a really good swimmer, you can hold your breath for a ridiculous amount of time for a human..."
            hide lexi
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mclexi "That’s just because I’ve practiced! I promise you I’m not a mermaid."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "Alright, alright. Keep your secrets, sea witch."
            hide lexi
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            mclexi "I'm not-!"
            hide mscmc
            show mscmc bikini_hairdown grin at left1 behind lexi
            show lexi mermaid surprised at right1
            "Instead of finishing my protest, I splash some water onto Lexi’s face."
            show lexi mermaid angry
            lx "Don’t make me splash you with my tail again!"
            show mscmc bikini_hairdown grin
            show lexi mermaid bigsmile
            mclexi "I’m sorry! I’m sorry! Please don’t!"
            hide lexi
            hide mscmc
            "We float silently for a while and as the waves rock me back and forth I feel myself falling asleep."
            show mscmc bikini_hairdown smile at left1 behind lexi
            show lexi mermaid bigsmile at right1
            mclexi "I’m about to fall asleep out here. Should we head back?"

            lx "Yeah, that sounds like a good idea. We’ve got a big day tomorrow."


        "B. We shouldn't, tomorrow's a big day.":
            $menuhideborder = False
            show mscmc casual_hairdown sad at left3
            show lexi casual smile at right3
            mclexi "As nice as that sounds, it'll be a pain in the butt to change into my swimsuit right now."
            show mscmc casual_hairdown basic
            lx "Are swimsuits required?"
            show mscmc casual_hairdown embarrassed
            "My face burns at the thought of Lexi and I skinny dipping and I'm forced to look away."
            show lexi casual bigsmile
            lx "I'm just messing with you. Is there something else you'd want to do to help fall asleep?"
            hide lexi
            hide mscmc
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(There is that new special that just came out by that comedian I like...)"
            hide mscmc
            show mscmc casual_hairdown grin at left3
            show lexi casual bigsmile at right3
            mclexi "Do you want to watch this stand-up comedy that everyone has been talking about lately? The comic is really funny."

            lx "Human comedy?! That sounds amazing!"

            mclexi "Let me grab my laptop."
            hide mscmc
            hide lexi
            "I pull out my laptop and put on the show."
            show lexi casual_cu sleep_cu at lexi_cu
            "After a while I can hear Lexi's soft breathing."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's asleep... She sounds so peaceful right now... And the sound of her breathing is putting me to sleep...)"
    stop music fadeout 1.0
    play music mscaction
    scene bg msc_ocean_wide_day at bg with clockwise_wipe
    #scene needs surfboard, but really having trouble getting it to work correctly
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid basic at right3
    mclexi "Do you think this is the right area?"

    "I paddle on my board through the cool water as Lexy swims next to me."

    "I find myself entranced as I watch her, staring at the small scales of her tail glittering in the morning sun."
    show lexi mermaid smile
    lx "From the picture and the journal, we should be right on top of it, more or less."
    show lexi mermaid smile:
        easein 0.4 ypos 900
    show mscmc surfer_hairup surprised:
        easein 0.4 xpos 600
        easein 0.4 ypos 900
    "She doesn't wait for me before she dives under the water and I quickly slip off my board and follow her."
    scene bg msc_underwater_day at bg with wipedown
    "We swim around the seafloor for a bit until I realize that I have no idea what I'm looking for."
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(What was I expecting? X marks the spot?)"
    hide mscmc
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid smile at right3:
        easein 0.4
    "As if sensing my confusion, Lexi swims over to me and points to various rock formations on the ocean floor."

    lx "Look for anything weird about the rocks around here."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Okay, anything weird...)"
    hide mscmc
    "I look over the closest formation, unsure of what would count as weird, when I notice a small glint in a crevice."
    show lexi mermaid surprised at centre with dissolve

    "I wave my hands to try to get Lexi's attention, and a moment later she's next to me."

    lx "Move back!"
    show lexi mermaid basic at centre:
        easein 0.4 ypos -100
        easein 0.4 ypos -25
    "Lexi sends water forcefully towards the rocks with her tail, causing several to collapse onto the seafloor."
    show lexi mermaid smile
    lx "Now let's see what we've got..."
    hide lexi
    "With the larger rocks displaced we both push the remaining rocks out of the way..."

    "And see a number of small rocks forming the shape of an X on the ocean floor!"
    show mscmc surfer_hairup_cu surprised_cu  at mscmc_cu
    "(Wow, X really did mark the spot.)"
    hide mscmc
    show mscmc surfer_hairup surprised at left2
    show lexi mermaid basic at right2
    "I swim toward the X to investigate it, but before I get close, Lexi holds her arm in front of me and shakes her head."
    show lexi mermaid smile
    lx "I got this."
    hide mscmc
    show lexi mermaid smile at centre:
        easein 0.4 ypos -100
        easein 0.4 ypos -25
    "Lexi begins to flap her tail, kicking up massive amounts of sand."
    hide lexi
    "It takes a minute for the sand to settle, but when it finally does, I can see the edge of a chest poking out of the seabed."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(This is... I wish I could talk down here like Lexi!)"
    scene bg msc_ocean_wide_day at bg
    #splash noise
    show mscmc surfer_hairup grin at left3:
        easein 0.4 ypos -25
    show lexi mermaid bigsmile at right3:
        easein 0.4 ypos -25
    "I tap Lexi on the shoulder and point towards the surface and we swim up together."

    mclexi "LEXI! WE FOUND IT!"

    lx "We did it!"
    show mscmc surfer_hairup grin behind lexi:
        easein 0.4 xpos 400
    show lexi mermaid bigsmile:
        easein 0.4 xpos 600
    "We grab one another's arms in excitement until we hear the familiar sound of a boat engine approaching."
    show mscmc surfer_hairup sad
    show lexi mermaid angry
    mclexi "Not now..."
    stop music fadeout 1.0
    play music mscantagonist
    hide lexi
    hide mscmc
    show bg msc_yacht_day at bg
    show ned vest basic at centre
    "A moment later Ned's yacht is next to us and we look up to find the arrogant documentarian looking down on us."

    dt "Good job finding the treasure. Too bad I found it first and was just using it as bait."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup surprised:
        xpos 400
    show lexi mermaid surprised:
        xpos 600
    "Lexi and I exchange puzzled looks."
    show lexi mermaid angry
    lx "Stop with the games, Ned. We found the chest and we're not letting you have it."
    hide mscmc
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest smile at centre
    "The air fills with Ned's obnoxious laughter."

    dt "That chest is worth a fraction of what I'll make now that I've got a mermaid."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup angry:
        xpos 400
    show lexi mermaid angry:
        xpos 600
    mclexi "Why do you keep going on about mermaids? Been in the sun too long?"
    hide mscmc
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest basic at centre
    dt "There's no use hiding it now. I caught you and your mermaid friend in 4K down there."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(He planted cameras around the treasure?!)"
    hide mscmc
    show lexi mermaid_cu surprised_cu
    lx "This can't be happening."

    "Lexi looks at me, her eyes wide."

    hide lexi
    show bg msc_yacht_day at bg
    show ned vest smile at centre
    dt "As far as how I knew where the treasure was and the fact that you are a mermaid... You can thank your friend Hannah for that."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Who's Hannah, Lexi?)"
    hide mscmc
    show lexi mermaid_cu angry_cu at lexi_cu
    lx "I don't know who you're talking about, Ned."
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest_cu smile_cu at ned_cu
    dt "Really? Because a certain Hannah Jones seems to know you quite well."

    dt "She even made a point to make sure that I let you know it was her that sold you out."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Is this the person Lexi mentioned yesterday? Why does this Hannah have it out for Lexi so bad?)"
    hide mscmc
    "While I'm lost in my thoughts, Ned picks up a laptop and pulls a USB drive out of it."

    $menuhideborder = True
    menu lexis0e5c2:
        "A. Reassure Lexi that it'll be okay.":
            $menuhideborder = False
            show mscmc surfer_hairup sad:
                xpos 400
            show lexi mermaid angry:
                xpos 600
            "I lean close to Lexi and whisper in her ear."

            mclexi "We’ll figure it out somehow. Don’t let him get to you."

            lx "How can I not? This is the worst thing that could ever happen!"
            hide mscmc
            hide lexi
            show bg msc_yacht_day at bg
            show ned vest angry at centre
            dt "Hey! Keep it quiet down there!"


        "B. Reason with Ned.":
            $menuhideborder = False
            show mscmc surfer_hairup angry at centre
            mclexi "Why is this so important to you? Can’t you see you’re ruining someone’s life?"
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest smile at centre
            "Ned chuckles."

            dt "All I care about is the money. I could care less about your fishy friend’s life."

        "C. Try and come up with a plan.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu angry_cu at mscmc_cu
            "(There has to be something we can do. Anything! I won't let him ruin Lexi's life like this.)"
            show mscmc surfer_hairup_cu surprised_cu
            "(What if I try to bargain for the USB? But we don't have anything to bargain with...)"
    scene bg msc_ocean_wide_day at bg
    show lexi mermaid_cu angry_cu at lexi_cu
    lx "What's your endgame?"
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest angry at centre
    dt "My endgame? I own you! If you don't do what I want, I'll make sure this footage goes all over the internet."
    hide ned
    show bg msc_ocean_wide_day at bg
    show lexi mermaid_cu angry_cu at lexi_cu
    "As I go to protest, I feel the water begin churn underneath me, and I look over at Lexi."

    "Her jaw is clenched tight and her tail is flicking back and forth under the water."
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest smile at centre
    dt "Ah, and there are my boys with the chest."
    hide ned
    show bg msc_ocean_wide_day at bg
    show diver suit basic snorkel at centre:
        ypos 1000
        easein 0.4 ypos -15
    "Behind us two divers surface, each one holding one side of the treasure chest."
    hide diver

    show bg msc_yacht_day at bg
    show ned vest smile at centre
    dt "Ah. Blackmail and treasure. Today is a good day."


    "He grins maliciously and a moment later the yacht engines kick back on."

    dt "You can expect to hear from me soon with orders for you, Lexi. And remember, you have to do whatever I want from now on."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup sad:
        xpos 400
    show lexi mermaid angry:
        xpos 600
    "Lexi and I bob in the wake the yacht makes as it drives off and I can't help but feel completely defeated."
    scene bg msc_mc_bedroom_day at bg with wiperight
    stop music fadeout 1.0
    play music msctense
    show lexi casual sad at centre
    lx "What am I going to do?!"
    hide lexi
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(She's been pacing like this since we got back...)"
    hide mscmc
    show lexi casual angry at centre
    lx "I just... Argh! I can't believe I let this happen! We need to go get that USD thing or whatever he was talking about."
    hide lexi
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(She's right, we need to get it somehow...)"
    hide mscmc
    show mscmc casual_hairdown angry at left3
    show lexi casual angry at right3
    mclexi "First off, it's called a USB. Secondly, you're right."

    lx "Cool, you're on board. Let's go, we know he anchors his yacht at the marina at the end of the boardwalk."
    show mscmc casual_hairdown surprised
    mclexi "Whoa! I'm totally down, but we need to keep this on the DL. We can't break into his yacht in broad daylight."
    hide mscmc
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(What if we were to trick Ned somehow to get the USB?)"
    show mscmc casual_hairdown smile at left3
    show lexi casual basic at right3
    mclexi "Hear me out. Ned is a huge narcissist."
    show mscmc casual_hairdown grin
    mclexi "We play into that to get him off the boat. Tell him we're a local historical society and we want to give him an award at an event or something."
    show lexi casual surprised
    lx "Right! We'll tell him a bunch of movie people are going to be there and hype it up!"

    mclexi "We'll say that an invitation was sent to one of his employees and make it their fault he never got it."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Alright, this is coming together. But we can't deliver an invitation ourselves... I'll ask Trina!)"
    scene bg msc_boardwalk_sunset_people at bg with clockwise_wipe
    stop music fadeout 1.0
    play music mscsuspense
    show mscmc jacket_hairdown smile at left3
    show trina casual basic at right3

    so "Explain why I'm doing this again?"
    hide mscmc
    hide trina

    menu lexis0e5c3:
        "A. Make up an elaborate lie.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show trina casual basic at right3
            mclexi "We’re actually going to be helping the historical society set up the event."
            hide mscmc
            hide trina
            show lexi casual sad at centre
            lx "Plus, I was really uncomfortable with how he was acting yesterday."
            hide lexi
            show trina casual basic at centre
            so "I can feel that. Alright, I guess I’ll go give it to that creep."
            show mscmc jacket_hairdown grin at left3
            show trina casual smile at right3
            mclexi "Thanks! I owe you one."

            so "I'll add it to your tab."


        "B. Tell a half truth.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show trina casual basic at right3
            mclexi "We're just trying to get back at him for being a creep yesterday."
            hide mscmc
            show lexi casual smile at left3
            lx "And we figured the best way to hurt him would be to hurt his ego. Imagine how mad he's going to be when there's no award!"
            show trina casual smile
            so "I would definitely pay money to see that. Alright, I guess I'll go give it to that creep."
            hide lexi
            show mscmc jacket_hairdown smile at left3
            mclexi "Thanks! I owe you one."

            so "I'll add it to your tab."


        "C. It's better if she doesn't know.":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left3
            show trina casual basic at right3
            mclexi "Honestly, it’s probably better if you didn’t know. I know we’re being sketchy, but just trust me."
            show mscmc jacket_hairdown basic
            "Trina eyes me suspiciously before shrugging."

            so "As long as this doesn’t cause trouble for me I guess it’s fine."
            hide mscmc
            show lexi casual bigsmile at left3
            lx "Thank you so much! We’ll pay you back somehow."
            show trina casual smile
            so "You don’t owe me anything, Lexi. [genericfn], on the other hand, owes me a lot."
            hide lexi
            show mscmc jacket_hairdown grin at left3
            so "Don’t think I’m not keeping track of these favors."

    scene bg msc_boardwalk_night_lights at bg with dissolve
    show trina casual basic at centre
    pause
    hide trina with dissolve
    "As night falls, Lexi and I watch from behind some crates as Trina heads to Ned's yacht."
    show mscmc jacket_hairdown sad at left3
    show lexi casual basic at right3
    mclexi "Keep your head down!"
    show lexi casual angry
    lx "I want to see her give it to him. What if he doesn't fall for it?"

    "I shift uncomfortably at the thought."
    show mscmc jacket_hairdown surprised
    show lexi casual surprised
    mclexi "Look, he's opening it now!"
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is he really going to fall for this?)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
