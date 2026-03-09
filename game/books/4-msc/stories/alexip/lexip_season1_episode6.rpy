label lexip_season1_episode6:

    $tbc = False
    scene bg msc_boardwalk_night_lights at bg
    play music msctense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show mscmc jacket_hairdown surprised at left3
    show lexi casual surprised at right3
    lx "He took the invite!"
    hide lexi
    hide mscmc
    show bg msc_yacht_night_lights_on at bg
    show ned vest basic at centre
    hide ned with dissolve
    "We watch in anticipation as Ned disappears into the yacht before leaving with a group of his lackeys."
    show mscmc jacket_hairdown basic at left3 with dissolve
    show lexi casual basic at right3 with dissolve
    "We sneak out from our hiding spot behind the crates and slip onto the yacht, staying cautious in case anyone is still onboard."
    show mscmc jacket_hairdown smile
    mclexi "Looks clear."
    show lexi casual surprised
    lx "Alright, now where can we find that drive thing he had?"

    mclexi "We should check the cockpit. They probably have their computers in there."
    show mscmc jacket_hairdown sad
    mclexi "Now let's just hope that it's not locked."
    hide lexi
    hide mscmc
    "I turn the doorknob to the cockpit and to my relief it opens without any resistance."
    show mscmc jacket_hairdown grin at left3
    show lexi casual smile at right3
    lx "Score!"
    hide mscmc
    hide lexi
    "The cockpit is fairly standard, except for the mass of computer monitors at a desk on the left side..."

    "And the massive treasure chest in the middle of the floor."
    show mscmc jacket_hairdown smile at centre
    mclexi "Over here."
    show mscmc jacket_hairdown smile at left3
    show lexi casual surprised at right3
    "Lexi follows me to the computer set up and stares blankly at it."

    lx "So we just destroy this?"
    show mscmc jacket_hairdown sad
    mclexi "That's a start, but it won't do any good if we don't find the drive."

    lx "Is this it?"
    show mscmc jacket_hairdown surprised
    "I look to the PC tower Lexi points at and to my relief the drive is sticking out of a USB port."

    mclexi "Is that a sticky note?"

    $sidecharone = "Note"

    sid1 "PUT USBs IN THE LOCKBOX WHEN DONE. -NED."
    show mscmc jacket_hairdown grin
    show lexi casual smile
    lx "I guess his crew is as incompetent as he makes them out to be."
    hide mscmc
    hide lexi
    $menuhideborder = True
    menu lexis0e6c2:
        "A. Make fun of the incompetency.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi casual smile at right3
            mclexi "Where did he find these guys?"

            lx "Right?! I definitely didn’t think it would be THIS easy."

            mclexi "His loss is our gain, I guess. Grab it and we can get out of here."




        "B. Joke about how lucky we are.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi casual smile at right3
            mclexi "Is this mermaid magic? How are we getting this lucky?"
            show lexi casual bigsmile
            "Lexi laughs."

            lx "If I had magic like that my life would be so much easier."

            mclexi "True. That’d be an amazing power for a treasure hunter. Anyways, grab the drive and we can get out of here."


        "C. Hurry up.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(We need to hurry up and get out of here.)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left3
            show lexi casual smile at right3
            mclexi "We don't have much time until Ned realizes he was tricked. Grab the drive and let's get out of here."
    show mscmc jacket_hairdown smile at left3
    show lexi casual smile at right3
    stop music fadeout 1.0
    play music mscaction
    lx "Got it. Now..."
    show mscmc jacket_hairdown surprised
    "Lexi drops the drive on the ground and stomps on it with her heel, smashing it to pieces."

    lx "That'll take care of it, right?"
    show mscmc jacket_hairdown grin
    mclexi "Yep! Now let's just..."

    "I unplug the PC tower and bring it with us as we leave the cockpit."
    show lexi casual surprised
    lx "One second..."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What are you doing Lexi?! We need to leave!)"
    hide mscmc
    show lexi casual bigsmile at centre
    lx "Found it!"

    "A moment later I see Lexi dragging the massive treasure chest out of the cockpit."
    hide lexi
    "Suddenly, a booming angry voice comes from the dock."
    show bg msc_boardwalk_night_lights at bg
    show ned vest angry at centre
    dt "Find out who set up this fake award ceremony! I am being trolled!!"
    hide ned
    $sidecharone = "Lackey"

    sid1 "I told you we never got an invitation before tonight, boss."
    show ned vest angry at centre
    dt "Shut up! Something is going on. Go and check on the treasure."
    hide ned
    show bg msc_yacht_night_lights_on at bg
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What do we do?!)"
    hide mscmc
    show lexi casual smile at centre
    lx "I'll be right back."
    hide lexi with dissolve
    "Lexi disappears back into the cockpit and a few moments later I hear the yacht's engines kick on and we start moving."
    show bg msc_boardwalk_night_lights at bg
    show ned vest angry at centre
    dt "WHAT THE HELL! WHO'S DRIVING AWAY WITH MY YACHT?!"
    hide ned
    show bg msc_yacht_night_lights_on at bg
    show mscmc jacket_hairdown surprised at left3
    show lexi casual bigsmile at right3 with dissolve
    "Lexi reappears and grins at me as we begin to accelerate out of the marina."

    mclexi "How...?"

    lx "I hotwired the starter. This'll make it easier to escape!"

    lx "Now we throw the treasure chest and computer over the side. We can get the treasure later and that should destroy that computer, right?"
    show mscmc jacket_hairdown grin
    mclexi "Definitely."
    show mscmc jacket_hairdown grin:
        easein 0.4 ypos 800

    show lexi casual bigsmile:
        easein 0.4 ypos 800

    "We toss the PC and treasure chest over the side of the boat as the yacht starts to pick up speed before diving into the water."
    hide lexi
    hide mscmc
    "In the distance, we hear Ned screaming."
    scene bg msc_ocean_wide_night at bg with wipeup
    show mscmc jacket_hairdown grin at left3
    show lexi casual bigsmile at right3
    lx "We did it! Now let's get back to shore and celebrate!"
    hide lexi with dissolve
    hide mscmc with dissolve
    "We laugh as we swim away, heading towards the lit-up shoreline in the distance."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(We really got away with it!)"

    scene bg msc_surf_shop_night at bg with wipeleft
    show trina casual angry at centre
    stop music fadeout 1.0
    play music mscsurfshop

    so "What the hell! You two are soaked!"
    hide trina
    show mscmc casual_hairdown grin at left3
    show lexi casual bigsmile at right3
    "Lexi and I are rolling with laughter as we stumble into the surf shop."
    show mscmc casual_hairdown surprised
    show lexi casual surprised
    mclexi "Hey Trina! I didn't realize you were still closing up. We, uh..."
    hide lexi
    hide mscmc
    show trina casual smile at centre
    "Trina grins suggestively and gives me a less than subtle thumbs up."

    so "Night swims are pretty fun, aren't they? But you two are mopping up all that water."
    hide trina
    show mscmc casual_hairdown surprised at left3
    show lexi casual sad at right3:
        xpos 600
        easein 0.4 xpos 500
    "As I fill the mop bucket, I feel Lexi tap on my shoulder."
    show mscmc casual_hairdown smile
    mclexi "This will only take a minute, don't worry."

    lx "No, it's fine. I was just thinking... Now that we got the treasure from Ned, I'm going to have to head out soon."
    show mscmc casual_hairdown surprised
    "My heart sinks at her words and I momentarily forget what I'm doing, causing the mop bucket to overflow in the sink."

    mclexi "I mean... Yeah, I guess that makes sense. I just hadn't thought that far ahead."
    show lexi casual embarrassed
    lx "Well... I was thinking about it. Even though I'm going to have to head out, it doesn't have to be tonight. Would you want to go out?"
    show mscmc casual_hairdown grin
    mclexi "I thought we were already going out."
    show lexi casual smile
    "Lexi smirks at my joke and grabs the mop from the wall as I pull the full bucket from the sink."

    lx "Like out dancing or something, dummy!"
    hide lexi
    hide mscmc
    show trina casual smile at centre
    so "That sounds like a great idea!"
    hide trina
    show mscmc casual_hairdown surprised at left3
    show lexi casual surprised at right3
    "Lexi and I both jump at the sound of Trina's voice, and I see her standing in the doorway behind Lexi."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(I'm not normally into clubs, but ever since meeting Lexi she's been forcing me out of my comfort zone. This could be fun!)"
    hide mscmc
    show mscmc casual_hairdown grin at left3
    show lexi casual bigsmile at right3:
        xpos 500
    mclexi "Alright! I'm down! Let's hurry this up!"
    hide mscmc
    hide lexi
    "It takes us around half an hour before we all get ready and make it to the popular nightclub on the boardwalk."
    scene bg msc_nightclub_people at bg with clockwise_wipe
    stop music fadeout 1.0
    play music msclexiclub
    "When we get in the music is blasting and there are colorful lights flashing on the dark dance floor that is crowded with people."
    show trina casual smile at centre
    so "Do you guys wanna grab some drinks?"
    hide trina
    show mscmc casual_hairdown surprised at left3
    show lexi casual bigsmile at right3
    lx "Hell yeah! Let's go, [genericfn]!"
    show lexi casual bigsmile:
        easein 0.4 xpos 500
    "She grabs my hand and pulls me as she follows behind Trina."
    hide lexi
    hide mscmc
    show trina casual smile at centre
    so "Shots!"
    show trina casual smile at right4
    show lexi casual bigsmile at centre
    show mscmc casual_hairdown grin at left4
    "We all count to three and cheer as we down our drinks."

    mclexi "Phew! It's been a minute! Do you guys want to dance?!"

    "The girls perk up at the idea and in no time the three of us are dancing in the middle of the dancefloor."

    so "HEY, [genericfn]. LET'S GET SOME MORE DRINKS!"

    "I can barely hear Trina over the pounding bass of the music but nod and follow her to the bar."
    hide lexi
    show trina casual smile at right3
    show mscmc casual_hairdown grin at left3
    "Trina orders the drinks, and as we wait for the bartender we both look back at the dancefloor where Lexi is dancing."
    hide mscmc
    hide trina
    show lexi casual bigsmile at centre
    "All around her people are trying to steal glances at her as she gracefully moves her body to the music..."

    "and to my surprise, a wave of jealousy washes over me."
    hide lexi
    show trina casual smile at right3
    show mscmc casual_hairdown surprised at left3
    so "She's the center of attention right now. I'll wait for the drinks, why don't you go dance with her?"
    hide trina
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "As if on queue, Lexi looks at me through the crowd of people and beckons to me with her finger."
    hide lexi
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Why does my face suddenly feel so hot?)"
    hide mscmc
    show trina casual smile at right3
    show mscmc casual_hairdown embarrassed at left3
    so "Look! She's even calling you over to her!"
    show mscmc casual_hairdown surprised behind trina
    mclexi "No way! She's calling us both over!"
    show trina casual angry:
        easein 0.3 xpos 450
    "Trina nudges me roughly with her arm and gives me a look that tells me I'm being stupid."
    hide trina
    hide mscmc
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Lexi really wants to dance with just me? The way she's moving her hands over her body, that's...)"
    hide mscmc
    show mscmc casual_hairdown surprised at left3
    show trina casual angry at right3:
        xpos 450
    so "If you don't make a move, someone else is going to! Get out there!"
    hide mscmc
    hide trina
    show lexi casual_cu embarrassed_cu at lexi_cu
    "(Should I dance with Lexi?)"
    hide lexi
    $menuhideborder = True
    menu lexis0e56c2:
        "A. Show the club what 'sensuous' means with Lexi"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc casual_hairdown_cu angry_cu at mscmc_cu
            "(Enough messing around.)"
            hide mscmc
            show lexi casual smile at right3
            show mscmc casual_hairdown embarrassed at left3
            "I saunter towards Lexi, locking eyes with her, ignoring everyone else around me."
            show lexi casual smile at right3:
                easein 0.4 xpos 600
            show mscmc casual_hairdown embarrassed at left3:
                easein 0.4 xpos 500
            "Lexi’s eyes never leave mine and as I get close to her, Lexi grabs my lower back and pulls me to her."

            "We don’t say anything, instead, moving our bodies to the music and I can feel her soft, tan skin rubbing against me with every beat."
            hide lexi
            hide mscmc
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(This is…)"
            hide mscmc
            stop music fadeout 1.0
            play music mscloveinterest
            "The song changes to a slower remixed version of a popular dance song."
            show mscmc casual_hairdown smile at left3 behind lexi:
                xpos 450
            show lexi casual embarrassed at right3:
                xpos 600
            "Without thinking I turn Lexi around and dance behind her, wrapping my hands around her hips and holding her close to me."

            "Her hair brushes against my cheek as we move to the music and with each breath I take I can smell its sweet ocean scent."

            "She grinds against me, leaning into me and reaching her hands behind her, and pulling my head to her neck."
            hide mscmc
            hide lexi
            show lexi casual_cu embarrassed_cu at lexi_cu
            "My lips brush against her skin for a moment before Lexi turns and faces me, her hands gracefully transitioning onto my shoulders."

            "I stare into her heep green eyes, my hands wrapped around her curvy hips and soon we’re so close our foreheads are pressed together."

            "Her breath is warm on my face and my body is tingling with excitement."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(If I kissed her right now, what could she do?)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "I grin at the thought and Lexi grins back at me."

            "She leans her head closer to mine, grazing her lips against my cheek and whispers in my ear."

            lx "This is a side of you I didn’t expect…"
            hide lexi
            "Her voice tickles as she whispers, each syllable sending tremors through my body."
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "You know me. I’m full of surprises."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "I feel Lexi chuckle softly in my ear and I instinctively bite my lower lip."
            hide lexi
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            "(If we were really dating, would it always be like this? This feeling coursing through me...)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "You really are full of surprises..."
            hide lexi
            show mscmc casual_hairdown embarrassed at left3 behind lexi:
                xpos 450
            show lexi casual smile at right3:
                xpos 600
            "As she whispers, her hands run down my back and back up sending shivers through my body."

            "Goosebumps form on my arms as Lexi steps back from me, her hands running down my arms to my hands."
            show mscmc casual_hairdown surprised
            "Her fingers wrap around mine and she spins me before pulling me back into her."

            "My arms are crossed over my chest as our hands stay linked together."
            hide mscmc
            hide lexi
            show lexi casual_cu smile_cu at lexi_cu
            lx "Bet you didn’t see that coming."
            hide lexi
            "I shake my head, tilting my head to the side as Lexi brushes her lips against my neck."
            show lexi casual_cu smile_cu at lexi_cu
            lx "You’re adorable, you know that?"
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(She thinks I’m adorable? Does she like me?)"
            hide mscmc
            "I turn my head back to look at Lexi, her hair covering my face a little, and grin."
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Just adorable? Not sexy?"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Sexy, too. I really wish I didn’t have to leave."
            hide lexi
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(Me, too.)"
            show mscmc casual_hairdown_cu embarrassed_cu
            mclexi "Let’s not worry about that right now. I just want to be here with you."
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "Lexi nods and pulls me closer to her before letting me go og my hands and running them down the curves of my body to my waist."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "How about we make a wager?"
            hide mscmc
            "I spin around to face Lexi, grabbing her hands and falling back a little before pulling myself back to her."
            show lexi casual_cu surprised_cu at lexi_cu
            lx "A wager?"
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Yeah. For the coin."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi bites her lip and smiles coyly."

            lx "Go on."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "We keep dancing until someone gives up. The person who lasts longer gets to keep the coin."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "I’ll make you regret it."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "I grin."

            "(Even if I get tired first and don’t get the coin, I still win. Spending the rest of the night like this is better than any coin.)"

            mclexi "Then we’re on!"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "As I declare the start of the challenge, the music picks up and Lexi lets go of me, changing her dancing, but never taking her eyes off of mine."


        "B. No way! Everyone is looking!":
            $menuhideborder = False
            show mscmc casual_hairdown embarrassed at left3
            show trina casual angry at right3:
                xpos 450
            "My face flushes red and I look at the floor as I think about Lexi and I dancing together. I shake my head at Trina."
            hide mscmc
            hide trina
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(There's no way. Nope.)"
            hide mscmc
            show mscmc casual_hairdown surprised at left3
            show trina casual sad at right3:
                xpos 450
            so "Looks like you missed your chance. She's coming over."
            hide trina
            hide mscmc
            show lexi casual bigsmile at centre with dissolve
            "I turn my attention back towards Lexi and see her walking towards us, her face beaming and sweat sticking to her skin."

            lx "This music is amazing!"
            show lexi casual sad
            "Lexi leans against the bar and looks at me, giving me a playful frown."
            show lexi casual smile
            lx "You should have danced with me! It would have been fun."

    scene bg msc_hidden_cove_night at bg with wipeleft
    stop music fadeout 1.0
    play music msclexi
    "The moon illuminates the beach as Lexi and I walk along the shore, hand in hand."
    show mscmc casual_hairdown smile at left2
    show lexi casual bigsmile at right2
    lx "I haven't had a night this fun in forever!"
    show mscmc casual_hairdown grin
    mclexi "Same. I'm still a little faded from all those drinks."
    show lexi casual smile
    lx "Right?! That girl knows the good stuff."
    hide lexi
    hide mscmc
    "We keep walking, talking about the night's escapades until we eventually find ourselves in my hidden cove."
    show mscmc casual_hairdown grin at left2
    show lexi casual smile at right2
    mclexi "So, how did I do as your fake girlfriend?"

    "Lexi grins mischievously."

    lx "Okay, I guess. I've had better."
    show mscmc casual_hairdown angry
    mclexi "What?!"
    show mscmc casual_hairdown grin at left2:
        easein 0.4 xpos 500
    show lexi casual smile at right2:
        easein 0.4 xpos 600
    pause
    show mscmc casual_hairdown grin at left2:
        xpos 500
        easein 0.4 ypos 800
    show lexi casual smile at right2:
        xpos 600
        easein 0.4 ypos 800
    "I playfully tackle Lexi into the sand on the edge of the water, and without realizing it I'm on top of her looking down."
    hide lexi
    hide mscmc
    show lexi casual bigsmile at centre
    "Her hair is splayed out across the sand, the water barely touching the ends of it."
    #flash
    show lexi mermaid bigsmile with dissolve
    "Lexi's legs transform into her beautiful tail."
    hide lexi
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(She's so beautiful. She's so... everything. Why did this have to be a fake relationship?)"
    hide mscmc
    show lexi mermaid_cu embarrassed_cu at lexi_cu
    lx "I don't understand how someone like you could be single. You're smart, beautiful, talented..."

    "Lexi's hands wrap around my waist as she stares up at me."

    lx "What is it?"
    hide lexi
    "I shake my head, trying to come up with a good reason."
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    mclexi "I... I don't know. I haven't really thought about it. I just focus on surfing mostly."
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Hmm... are you a bad kisser? Is that why?"
    hide lexi
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    mclexi "Bad kisser?! First, you say I'm just an okay girlfriend and now you think I'm a bad kisser?!"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    "Lexi grins up at me, never breaking her gaze."

    lx "Prove me wrong."
    hide lexi
    stop music fadeout 1.0
    play music mscromance
    "Without another word I lean down to Lexi, pressing my forehead to hers, pausing briefly to build the tension."
    show lexi mermaid_cu embarrassed_cu at lexi_cu
    "I can feel her breath quicken slightly as I look down on her, and after I'm satisfied, I press my lips to hers. "
    hide lexi
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Her lips are soft with a slightly sweet and salty taste.)"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "You know it's a full moon, right?"
    hide lexi
    "Her voice is a whisper, barely audible over the melodic sound of the waves breaking on the shore."
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Merfolk say if you kiss someone under a full moon you're linked forever."
    hide lexi

    $menuhideborder = True
    menu lexis0e6c3:
        "A. Kiss her again.":
            $menuhideborder = False

            "I don't say anything, instead, leaning in to kiss Lexi again."

            "She meets me halfway and as I go to pull away, she gently bites my lip before letting me go."
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "You're really something else, ya know that?"
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Well if what you said about the moon is true, you're stuck with me."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "I can live with that."



        "B. Make a joke.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "I don’t see how that’s a problem."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "I don’t know, you are a handful. Having you in my life forever might be too much excitement for me."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Too much excitement for you? I don’t think that’s possible."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "Lexi chuckles."

            lx "We’ll have to see, won’t we?"


        "C. Ask her to not leave.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            mclexi "I wish you didn’t have to leave. We could stay like this, ya know?"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "Lexi chuckles."

            lx "We could. But with Ned still around, there’s no way I could. At least, not right now."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(Not right now? So then maybe someday...)"
    # zooming shenanigans I don't feel comfortable fucking with
    scene bg msc_mysirencrush_lexi_ei2 at bg with fade:
        zoom 0.5
    "We lie on the edge of the water, the water lapping against our bodies as we stare at one another."

    "The full moon shines down on us and neither of us say anything."

    "(I don't want this to ever end.)"

    lx "I stand corrected. Bad Kissing is definitely not the reason you are single."

    "She leans towards me, brushing a loc out of my face, caressing my cheek, and then kisses me tenderly."

    mclexi "I know. I just had to make sure you knew."
    scene bg msc_hidden_cove_night at bg
    show mscmc casual_hairdown embarrassed at left2 behind lexi
    show lexi mermaid embarrassed at right2
    "She sits herself up, taking my hand in hers as she does and I pull myself up next to her."

    "I lean into her shoulder and we both gaze up at the shimmering night sky as I get lost in the rise and fall of her breathing."
    scene bg msc_hidden_cove_sunset at bg with clockwise_wipe
    show mscmc casual_hairdown surprised at centre
    stop music fadeout 1.0
    play music mscmctheme
    mclexi "Where..."
    #blink thing with sides
    "I blink my eyes open and look up at the pink and orange sky. Sitting up, I realize it's morning and the sun is starting to come up."
    hide mscmc
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Last night, Lexi and I were making out!)"
    hide mscmc
    "My face flushes and I bury it in my hands. I look at the sand next to me and I realize Lexi isn't lying there."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Where?!)"
    hide mscmc
    show bg msc_lexi_short_mini3 at bg with dissolve
    "I jump to my feet and look around the beach, and my eyes fall on letters carved into the sand."
    stop music fadeout 1.0
    play music msclexi

    $sidecharone = "Message in the sand"

    sid1 "Had to run! Don't forget me!"
    show bg msc_lexi_short_mini4 at bg with dissolve
    "At the end of the message is a winking smiling face and as the morning tide comes in, it begins to wash the message away."

    "I absent-mindedly reach into my pocket and feel the gold coin that started everything."
    show bg msc_hidden_cove_sunset at bg with dissolve
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(This was all so crazy. Hunting for treasure, dancing, kissing under the full moon. Being with Lexi was a whirlwind of excitement.)"

    "(I wish she had stayed, but I have a feeling we'll meet again.)"

    $tobecontinued()

    scene bg msc_end at bg with fade
    pause
    $ resets()
