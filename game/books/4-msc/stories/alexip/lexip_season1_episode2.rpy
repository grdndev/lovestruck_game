label lexip_season1_episode2:

    $tbc = False
    scene bg msc_ocean_wide_day at bg
    play music mscsuspense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False


    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Did she just call me her girlfriend?!)"
    hide mscmc
    "My heart races as I think about what it would be like to date a mermaid until I remember that I need to back Lexi up."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(If we can convince him that we're on a date...)"
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Maybe he'll just leave without causing any more trouble because he won't think Lexi's looking for treasure in this spot.)"
    hide mscmc
    show mscmc surfer_hairup angry at centre
    mclexi "Yea! We came out here to spend time together, ALONE, and now you're here bothering us with your obnoxious yacht."
    hide mscmc
    show lexi mermaid bigsmile at centre
    "Lexi smiles appreciatively at me as Ned scoffs at us."
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest basic at centre
    dt "Dating, huh? Wouldn't you rather date the famous treasure hunter and documentarian, Ned Lewis?"
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup angry at centre
    "I roll my eyes."

    mclexi "Maybe you should have tried that before you acted like a pompous jerk at my friend's surf shop."
    hide mscmc
    show bg msc_yacht_day at bg
    show ned vest basic at centre
    dt "Surf shop?"

    "There's visible confusion on his face as he tries to recall whether or not we've already met."
    hide bg msc_yacht_day
    hide ned
    show bg msc_ocean_wide_day at bg
    $menuhideborder = True
    menu lexis0e2c1:
        "A. Tell him I work at the surf shop.":
            $menuhideborder = False
            show mscmc surfer_hairup surprised at centre
            mclexi "Are you serious right now? I work at the surf shop you and your croney up there bought all your diving gear from."
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest basic at centre
            dt "Nope, doesn’t ring a bell."
            hide bg msc_yacht_day
            hide ned
            show bg msc_ocean_wide_day at bg
            show mscmc surfer_hairup angry at centre
            "I grit my teeth in annoyance, fighting back the urge to scream at Ned."

            mclexi "Are you for real? There were only two of us at the shop and I’m the one that rang you up."


        "B. Be sarcastic":
            $menuhideborder = False
            show mscmc surfer_hairup angry at centre
            mclexi "Do you really not remember? What, you think your gear just magically appeared on your boat?"
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest basic at centre
            "Ned scowls at the remark, but it’s clear he still doesn’t remember me at all."
            hide bg msc_yacht_day
            hide ned
            show bg msc_ocean_wide_day at bg
            show mscmc surfer_hairup_cu angry_cu at mscmc_cu
            "(Why am I even trying? This guy is unreal.)"
            hide mscmc

        "C. Spell it out for him.":
            $menuhideborder = False
            show mscmc surfer_hairup angry at centre
            mclexi "You. Bought. Your. Gear. From. Me. What part are you not getting about that?"
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest basic at centre
            "Ned squints his eyes as he tries to remember, until he finally shrugs and gives up."
            hide bg msc_yacht_day
            hide ned
            show bg msc_ocean_wide_day at bg
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(He really doesn't remember. This is insane.)"
            hide mscmc
    show bg msc_yacht_day at bg
    show ned vest basic at centre
    dt "Seems strange that I wouldn't remember a looker like you, but all I remember was how crummy that shop was."
    hide bg msc_yacht_day
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup angry at centre
    "A fiery rage burns in my chest at Ned's insult of Trina's shop."
    hide mscmc
    show mscmc surfer_hairup_cu sleep_cu at mscmc_cu
    "(Deep breaths. Don't lash out. He's not worth it.)"
    hide mscmc
    show mscmc surfer_hairup angry at centre
    mclexi "Whatever. Can you leave now so we can get back to our date? Your dumb boat is blocking the waves."
    hide mscmc
    show lexi mermaid smile at centre
    lx "Right? I was quite enjoying myself until Mr. Famous came over and ruined the mood."

    $sidecharone = "Dingus"
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest basic at left3
    show diver suit basic snorkel at right3
    sid1 "Boss, some of the boys said they picked something up on the sonar a little down the coast."
    show ned vest angry
    dt "Why am I just hearing about this now?! Get the boat started and let's go. As for you..."
    hide diver
    show ned vest angry at centre
    "He purses his lips and points his finger aggressively at Lexi."

    dt "If I see you anywhere near my diving spot trying to steal my treasure, I'll make sure you regret it."
    hide ned with dissolve
    "He disappears towards the back of the yacht and a few moments later the engines kick on."
    hide bg msc_yacht_day
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Finally!)"
    show mscmc surfer_hairup smile at left3
    show lexi mermaid smile at right3
    stop music fadeout 1.0
    play music mscmctheme

    "I look over to Lexi, who is visibly as relieved as I am."

    "We watch together as Ned and his crew drive off."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Phew, he's gone.)"
    hide mscmc
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid angry at right3
    lx "Barnacle sucker!"

    "I look at Lexi, surprised at how vexed she seems now that we've gotten rid of Ned."

    mclexi "What's wrong? Isn't it a good thing that he left?"

    lx "Yes, but he just happened to move to and anchor right on top of where my UV is parked."

    mclexi "UV? What's that?"
    show lexi mermaid sleep
    "Lexi sighs."
    show lexi mermaid basic
    lx "It's my underwater vehicle that I live in to treasure hunt."

    mclexi "Wait, so it's like an underwater RV?"
    show lexi mermaid surprised
    "Lexi's brow furrows and I realize that she probably doesn't know what an RV is."
    show mscmc surfer_hairup grin
    mclexi "It's like a big vehicle with a living area in the back."
    show mscmc surfer_hairup surprised
    show lexi mermaid bigsmile
    lx "Yes! Exactly that! I move around a lot as a treasure hunter so it's pretty much my home."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(She really lives a life of adventure. I wonder if it ever gets lonely.)"
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Ah! Why am I even thinking about that?!)"

    "(Wait, so if they're anchored above it...)"
    hide mscmc
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid angry at right3
    mclexi "What if they find it?!"

    "Lexi shakes her head, her expression showing more annoyance than concern."

    lx "It has a magical camouflage that makes it so anyone who isn't me, or with me, can't see it."

    lx "It's just that if he's searching that area he'll be there at least until tomorrow."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Magic camouflage? That's amazing! That means magic is real!)"
    hide mscmc
    "I feel giddy at the idea of magic being real, but I do my best to refrain from showing it given the situation."
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(I wish there was something I could do to help... Wait!)"
    hide mscmc
    show mscmc surfer_hairup smile at left3
    show lexi mermaid surprised at right3
    mclexi "You could stay with me if you wanted."

    lx "Really? Are you sure?"
    show mscmc surfer_hairup grin
    show lexi mermaid basic
    mclexi "It's the least I can do to thank you for opening up a whole new world to me."

    mclexi "You're literally validating all the dreams I had when I was younger."
    hide mscmc
    hide lexi
    show lexi mermaid_cu basic_cu at lexi_cu
    "Lexi eyes me and I can tell she's debating internally on whether or not she should fully trust me."
    hide lexi
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Say yes! How cool would it be to have a sleepover with a mermaid!)"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "You know what? You've been fun to hang out with and I've always wanted to see what a human house looks like. Let's do it!"

    scene bg msc_hidden_cove_sunset at bg with clockwise_wipe
    stop music fadeout 1.0
    play music mscbeach
    pause
    show lexi mermaid bigsmile at centre
    lx "You seem really at home on your board."
    show lexi mermaid bigsmile at right3
    show mscmc surfer_hairup surprised at left3
    "The comment catches me off guard as I paddle on my surfboard on our way to a secluded part of the beach."
    show mscmc surfer_hairup smile
    mclexi "Yeah, I spend a lot of time on it. I'm trying to become a pro-surfer and get into the World Surf League."
    show lexi mermaid smile
    "Lexi cocks her eyebrow."

    lx "Pro-surfer, huh? That's pretty cool. How do you become a pro?"

    mclexi "They have competitions throughout the year to qualify, though there aren't any coming up."
    #animation of MC jumping off board
    show lexi mermaid bigsmile
    "As the sun sets, we get to the shore of the lagoon and I roll off of my board into the water next to Lexi."
    show lexi mermaid surprised
    lx "Are you sure no one will see us here?"

    "I nod."

    mclexi "The boardwalk is way down the beach on the other side of these big rocks and there's really nothing down the other end of the beach."
    show lexi mermaid sad
    show mscmc surfer_hairup surprised
    lx "Ugh! I wish I had brought my charm with me."
    show mscmc surfer_hairup embarrassed
    mclexi "I mean, you've been pretty charming since we've met."
    show lexi mermaid bigsmile
    "Lexi grins."
    show mscmc surfer_hairup grin
    lx "It's a magic charm that lets me turn my tail into legs. I got it from an old sea witch I met a few years ago."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(A sea witch? That sounds just like that movie I used to watch as a kid. Oh god, this really is all just a bad smoothie hallucination!)"
    hide mscmc
    "As I begin to question my reality again, I suddenly feel Lexi's soft tail brush against my leg."
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Nope. Definitely real. It's definitely real!)"
    show lexi mermaid surprised at right3
    show mscmc surfer_hairup grin at left3
    "The feeling of giddy excitement I felt when I first realized Lexi was a mermaid comes back to me and I can feel my heart begin to race."
    show mscmc surfer_hairup surprised
    lx "Are you okay?"
    show mscmc surfer_hairup grin
    "I nod to Lexi, failing miserably to hold back my gleeful grin."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Calm down! She's going to think you're a creep if you smile at her like that!)"
    hide mscmc
    show lexi mermaid surprised at right3
    show mscmc surfer_hairup grin at left3
    mclexi "Yea! I'm fine, I just thought of something funny."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Smooth...)"
    hide mscmc
    show lexi mermaid smile at right3
    show mscmc surfer_hairup surprised at left3
    lx "So what's the plan?"
    show mscmc surfer_hairup smile
    mclexi "I guess the first thing we need to do is just wait until it gets dark. Then I'll have to somehow get you from here to Trina's surf shop."
    show lexi mermaid surprised
    lx "Is this the one you were talking about earlier?"

    mclexi "Yea, I live in a room above the shop. It's not too far from here."
    hide mscmc
    hide lexi
    show lexi mermaid_cu surprised_cu at lexi_cu
    "Lexi nods and I can see the gears turning in her head as she considers the situation."

    lx "The biggest problem is how you'll get me there. I'm definitely too heavy for you to carry."
    show lexi mermaid_cu smile_cu
    "She slaps her tail on the water, splashing water."

    lx "This baby is pure muscle."
    hide lexi
    "I stare at her tail for a moment, admiring its coloring and how unreal it feels."
    show lexi mermaid basic at right3
    show mscmc surfer_hairup surprised at left3
    "The image of carrying Lexi in my arms like a princess pops into my mind."
    show mscmc surfer_hairup embarrassed
    "The thought immediately makes me blush for the millionth time and I'm thankful that it's getting dark so Lexi can't see my embarrassment."
    show mscmc surfer_hairup surprised
    mclexi "I could get a wheelbarrow?"

    "Lexi shrugs."
    show lexi mermaid smile

    lx "Whatever works. I've been in more embarrassing situations."
    show mscmc surfer_hairup embarrassed
    "I consider asking Lexi about the situations, but decide better of it."
    hide lexi
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(I should change the subject. Even if she's okay with it, this is still going to be embarrassing for her.)"
    hide mscmc
    show lexi mermaid smile at right3
    show mscmc surfer_hairup grin at left3
    stop music fadeout 1.0
    play music mschappytimes
    mclexi "So are we going to 'break up' after we sort all this out?"

    lx "Ha! I guess we'll have to see. My plan was to get the treasure here and take the portal to the city and sell it."
    show mscmc surfer_hairup surprised
    mclexi "Wait, what? Portal?!"
    show lexi mermaid surprised
    lx "Yeah, the portal to the city. Don't you humans have portals to your cities?"
    hide lexi
    hide mscmc
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(I wish!)"
    hide mscmc
    show lexi mermaid surprised at right3
    show mscmc surfer_hairup sad at left3
    mclexi "No, we have roads and it takes hours to travel between cities."

    lx "Hours?! I can't even imagine. I guess the portals aren't close to one another, but I don't really go to the cities unless I'm selling treasure."
    show mscmc surfer_hairup smile
    mclexi "Like this?"

    "I pull out the gold coin that had brought Lexi and me together and hold it out to her."
    show lexi mermaid smile
    lx "You can keep that one."
    show mscmc surfer_hairup grin
    mclexi "Keep it? Isn't it finders keepers? I thought it was already mine."
    show lexi mermaid bigsmile
    lx "Normally, but you stole that one from me! I'm just being nice and letting you have it. Besides, you're my girlfriend, I have to spoil you somehow."
    show lexi mermaid smile
    "She places her hands on her hips and turns her nose up with a sarcastic look of superiority on her face."
    hide mscmc
    hide lexi
    $menuhideborder = True
    menu lexis0e2c2:
        "A. Try to act even more superior.":
            $menuhideborder = False
            show lexi mermaid smile at right3
            show mscmc surfer_hairup angry at left3
            "I stand up and match Lexi's pose adding a harumph for effect."

            mclexi "I've never stolen anything in my life. For a peasant like you to even..."
            show lexi mermaid bigsmile
            show mscmc surfer_hairup grin
            "We both crack up at the same time, neither of us able to take the conversation seriously."



        "B. Pretend to be Ned.":
            $menuhideborder = False
            show lexi mermaid smile at right3
            show mscmc surfer_hairup angry at left3
            mclexi "Of course you’re giving it to me. Don’t you know I’m the famous treasure hunter and documentarian, [genericfn]?"
            show lexi mermaid bigsmile:
                easein 0.4 yoffset 40
                easein 0.4 yoffset -40
            "Lexi chuckles and begins to bow before me."
            show mscmc surfer_hairup grin
            lx "Of course! How could I ever compete with a great treasure hunter like you. Teach me your ways."


        "C. Joke about taking all the treasure.":
            $menuhideborder = False
            show lexi mermaid smile at right3
            show mscmc surfer_hairup grin at left3
            mclexi "Maybe I just need to find all the treasure before you and Ned and keep it all to myself."
            show mscmc surfer_hairup smile
            "I eye Lexi tauntingly."
            show lexi mermaid bigsmile
            lx "As if you could! It takes skill to be as awesome as me!"

    scene bg msc_hidden_cove_night at bg with dissolve
    show mscmc surfer_hairup grin at left3
    show lexi mermaid bigsmile at right3
    "We continue to joke about the coin for a while until the sun finally sets."

    mclexi "Alright! Let's do this!"
    scene bg msc_labeach_night at bg with wipeleft
    show mscmc surfer_hairup surprised at centre
    stop music fadeout 1.0
    play music mscsuspense
    mclexi "Okay, are you ready?"
    #animation of Lexi going diagonal to be in wheelbarrow
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid basic at right3
    "Lexi nods and I hold the wheelbarrow I had borrowed from the surf shop steady as she pulls herself into it."
    show lexi mermaid smile
    lx "Alright, let's go."
    hide lexi
    hide mscmc
    "The wheelbarrow is difficult to maneuver in the sand with Lexi in it."

    "But after a while we finally manage to make it to the back door of the surf shop that leads to my room."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    mclexi "Next challenge. Stairs."
    #animation for Lexi
    hide mscmc
    show mscmc surfer_hairup surprised at left2
    show lexi mermaid smile at centre
    "Lexi wraps her arm around my neck and pulls herself out of the wheelbarrow and supports herself on me."
    show mscmc surfer_hairup embarrassed
    "Her skin is soft and warm as it presses against my neck and I can feel goosebumps forming on my arms from her touch."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(Keep it together, don't freak out. I'm just helping a mermaid up some stairs.)"

    "(An attractive mermaid with super soft skin, who smells like sweet ocean mist.)"
    hide mscmc
    "We struggle for a little bit until we finally give up on me pulling Lexi up the stairs."
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "New plan. You help hold my tail up and I'll climb up the stairs."
    hide lexi
    "I agree and wrap my hands around her tail and to my surprise her scales feel nothing like I expected."

    "Instead of being hard and fishy, her tail is as soft as her skin is and silky smooth."
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(I'm essentially holding Lexi's legs...)"
    hide mscmc
    "My brain feels like it's going to explode at the realization and I almost let Lexi's tail slip out of my grasp. Thankfully, I manage to keep my grip."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(That was close! It'll be a disaster if Trina sees us!)"

    scene bg msc_mc_bathroom_lights_on at bg
    stop music fadeout 1.0
    play music msclexi

    "We eventually get Lexi into my bathroom, and as she lays down in the bathtub, the reality of the situation sets in."
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(I have a mermaid in my bathtub! A super attractive, super cool treasure hunting mermaid. Trina would never believe this!)"
    #need zooming animation that pans from her tail to her face
    scene bg msc_mysirencrush_lexi_ei1 at bg
    "Lexi grins up at me and I realize I've been staring at her."

    mclexi "Sorry! I didn't mean to stare!"

    lx "Not really. And it's the first time I've ever been in a human house. It's really interesting."

    lx "Besides, why would I be uncomfortable with my girlfriend staring at me?"

    "I can feel my face start to burn up at her jest as her smoldering green eyes stare up at me."

    "And, for a moment, I forget about the absurdity of the situation."

    lx "This is all so surreal."
    scene bg msc_mc_bathroom_lights_on at bg
    show mscmc casual_hairdown surprised at centre
    "I sit down on the bathroom floor, leaning my back against the tub and nod."
    show mscmc casual_hairdown grin
    mclexi "It really is. If you had told me this morning I'd be spending my day with a mermaid, I would've told you that you were crazy."
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    "Lexi looks at me, and from her expression I can tell that she wants to ask something."
    hide lexi
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    mclexi "What's on your mind?"
    hide mscmc
    show lexi mermaid_cu bigsmile_cu at lexi_cu
    lx "I was just thinking about how much you've helped me and I don't know anything about you. Will you tell me more about yourself?"
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "I'll trade you info about me for info about you."
    hide lexi
    $menuhideborder = True
    menu lexis0e2c3:
        "A. Learn about Lexi."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "Me? Well, I’m from Jamaica but I grew up in a small town in the midwest."
            hide mscmc
            show lexi mermaid_cu surprised_cu at lexi_cu
            lx "The midwest? Isn’t that super far from the ocean? I figured as a surfer you would have grown up on the coast."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Well when I was younger my parents frequently took me on trips to the ocean to visit my family."

            mclexi "My family is Jamaican and it’s always been super important to my parents that I keep in touch with my heritage."
            hide mscmc
            show lexi mermaid_cu sad_cu at lexi_cu
            lx "I never got to go to the ocean as a kid."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "What?"
            hide mscmc
            show lexi mermaid_cu basic_cu at lexi_cu
            lx "I grew up in a small lake, so all I ever knew about the ocean were the stories my dad told me."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "Wait, you grew up in a lake? Mermaids can live in freshwater? Are there a lot of merfolk in the freshwater lakes?"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "I can live in any type of water. As far as freshwater merfolk, there’s a good number of us, but there are definitely way more in the oceans."

            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "That’s why I decided to leave home and go to an ocean city college to study Merstory."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "Whaaaat? There’s mer college? That’s so cool. I went to college near home and majored in marine biology."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "What about surfing?"
            hide lexi
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            mclexi "Well, I learned to surf from my cousins when I was a kid."

            mclexi "And even though I was a professional skateboarder in college, I always thought surfing would be more enjoyable."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "Plus you never know when you’ll run into a sexy treasure hunting mermaid, right?"
            hide lexi
            "I blush at Lexi’s jest. It’s not like I ever thought mermaids could be real, but admittedly a part of me had always hoped."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I’ll have you know that had nothing to do with my life choices!"
            hide mscmc
            "We both stifle laughs and as we sit there, I feel as if Lexi and I have always been friends."
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(How do I feel so comfortable around her? Now that I’m over the initial mermaid shock, it’s like talking to a friend I’ve known my whole life.)"
            show mscmc casual_hairdown surprised at left3
            show lexi mermaid basic at right3:
                yoffset 100
            mclexi "What about you? You said you majored in history, but why become a treasure hunter?"
            show lexi mermaid bigsmile
            lx "So I could experience that history for myself!"

            lx "There’s literally nothing better than reading about some ancient treasure and going on an adventure to find it."

            mclexi "Is it ever dangerous?"
            show lexi mermaid angry
            lx "Sometimes. I’ve had a few run-ins with less savory treasure hunters like Ned, and I’ve had rocks almost crush me."
            hide lexi
            hide mscmc
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(That sounds just like that treasure hunter from that old famous movie!)"
            show mscmc casual_hairdown surprised at left3
            show lexi mermaid smile at right3:
                yoffset 100
            lx "I can tell from your face that you’re realizing just how cool I am."
            show mscmc casual_hairdown embarrassed
            "She puts her fists on her hips and pretends to flex, grinning from ear to ear."
            show mscmc casual_hairdown grin
            mclexi "Don’t get too full of yourself. You’re not that cool."
            show lexi mermaid bigsmile
            "We briefly stare at one another, both trying to keep a straight face until we burst out laughing at the same time."
            hide lexi
            hide mscmc
        "B. Get nervous.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            mclexi "There really isn't much to say. I'm not anyone special."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "I'd say you'd have to be pretty special to want to become a professional surfer, but I understand."
            hide lexi
    show lexi mermaid_cu smile_cu at lexi_cu
    stop music fadeout 1.0
    play music mscromance
    lx "You've really helped me out a lot. If you helped me a little more, I'd be willing to split the treasure I'm looking for with you."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Help out how?"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Well you know the area pretty well and with that jerk Ned focused on me, it'd be really helpful if you'd keep up the girlfriend cover."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(That's not a bad deal at all.)"
    hide mscmc
    show mscmc casual_hairdown smile at left3
    show lexi mermaid smile at right3:
        yoffset 100
    mclexi "Yea, I think that..."
    #sound for knocking
    stop music fadeout 1.0
    play music msctense
    show mscmc casual_hairdown surprised
    show lexi mermaid surprised
    "Suddenly, there is a loud knock on my bedroom door which I can see from the bathroom and Lexi and I stare at one another in panic."
    hide lexi
    hide mscmc
    so "Hey, [genericfn], I'm coming in."


    $tobecontinued()

    show msc_tbc at bg with fade
    pause
    $ resets()
