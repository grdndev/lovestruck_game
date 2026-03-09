label lexip_season1_episode3:

    $tbc = False
    scene bg msc_mc_bathroom_lights_on at bg
    play music msctense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False


    show mscmc casual_hairdown surprised at left3
    show lexi mermaid surprised at right3:
        yoffset 100
    "I can hear the door knob turn as Lexi and I stare in horror at one another."

    mclexi "Hold on! I'm changing!"
    hide lexi
    hide mscmc
    so "It's not like I've never seen you change before."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(What do I do?!)"
    hide mscmc
    show mscmc casual_hairdown surprised at centre
    mclexi "Um, someone else is here, too!"
    show mscmc casual_hairdown smile
    "I strain my ears and to my relief, I hear the doorknob return to its original position."
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Now what? I have a mermaid in my bathtub and I just told Trina I was with someone. Think!)"
    show mscmc casual_hairdown surprised at left3
    show lexi mermaid surprised at right3:
        yoffset 100
    lx "Why would you say that?! She can't see me!"
    show mscmc casual_hairdown sad
    mclexi "I know! Just let me think. Okay, I got it. Let's get you to my bed."
    #animation of MC dragging Lexi to bed before falling
    hide mscmc
    hide lexi
    "Lexi wraps her arms around me as I help her out of the tub, but as her tail comes out her weight shifts causing us to tumble to the floor."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu

    "(Ow... That didn't feel great.)"
    hide mscmc
    show lexi mermaid_cu surprised_cu at lexi_cu
    "As I move to get up, I find Lexi's face inches from mine, her hair hanging down around me."
    hide lexi
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu

    "(Her hair smells like ocean salt...)"
    hide mscmc
    show lexi mermaid_cu embarrassed_cu at lexi_cu
    "Neither of us move, and as I stare into her bright green eyes, I feel like waves are crashing in my stomach."
    hide lexi
    so "Are you okay in there?"
    scene bg msc_mc_bedroom_night_lights at bg with wipeleft
    stop music fadeout 1.0
    play music mscmctheme
    "Trina's voice snaps Lexi and me back to our current dilemma and I hastily drag her to my bed and throw a blanket over her legs."
    show mscmc casual_hairdown grin at centre

    mclexi "Sorry, I just knocked something over. You can come in now!"
    hide mscmc
    show trina casual basic at centre with dissolve
    "The door knob turns again, and a moment later Trina is in the room."
    hide trina
    show mscmc casual_hairdown embarrassed at left2
    show lexi mermaid embarrassed at right2
    "She immediately eyes the two of us in bed and I realize that Lexi and I are both breathing heavily."
    hide mscmc
    hide lexi
    show trina casual sad at centre
    so "Ooooh! I didn't realize it was... I'm so sorry to interrupt."
    show trina casual smile
    so "Hi there! I'm Trina. I own the surf shop."
    hide trina
    show lexi mermaid bigsmile at centre
    lx "Hi Trina, I'm Lexi. It's nice to meet you."
    hide lexi
    show mscmc casual_hairdown embarrassed at left2
    show lexi mermaid bigsmile at right2:
        easein 04 xoffset 40
    "As she finishes her introduction, Lexi casually throws her arm over my shoulder."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(This is kind of nice... It's too bad that we're just... Wait! What am I saying?!)"
    hide mscmc
    show trina casual smile at centre
    so "I was going to ask my bestie here if she wanted to grab some food, but I think I'll give you two some space. Sorry for interrupting you."
    show trina casual smile at right3
    show mscmc casual_hairdown embarrassed at left3
    "Trina gives me a look that says she's cheering me on which only causes me to want to hide under the covers in embarrassment."
    hide mscmc
    show lexi mermaid bigsmile at left3
    so "It was nice meeting you, Lexi!"
    hide trina with dissolve
    "They exchange polite smiles and then Trina makes her exit."
    show lexi mermaid smile at left2
    show mscmc casual_hairdown sad at right2
    mclexi "That was mortifying."

    "Lexi smirks."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu

    "(Was this fun for her?)"
    hide mscmc
    show lexi mermaid smile at left2
    show mscmc casual_hairdown surprised at right2
    lx "I'm sorry that you had to lie to her, but I really appreciate it. Also, good thinking with the blanket."
    show mscmc casual_hairdown sad
    mclexi "That's all I could think of!"
    show mscmc casual_hairdown surprised
    show lexi mermaid smile
    lx "It just shows you can think quickly on your feet. Which is why I would really appreciate your help looking for the treasure."

    lx "A quick wit like that will be super helpful in keeping that lamprey Ned off my back, and like I said before, I'm more than happy to share the loot."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(It's kind of sexy how even after stressful situations Lexi can still think about business... She's so free spirited and driven.)"
    hide mscmc
    show mscmc casual_hairdown surprised at centre
    mclexi "I..."

    "I pause, thinking of the implications of saying yes. As crazy as it all was, this was the most exciting day I've had in a long time."
    hide mscmc
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Do I really want to give up this once-in-a-lifetime opportunity?)"
    hide mscmc

    $menuhideborder = True
    menu lexis0e3c1:
        "A. I'm in.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu

            mclexi "I'm definitely in. This is the most exciting experience of my life, and I'm not about to turn down an adventure like this."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "I'm glad to hear it! It'll make everything so much easier knowing you have my back."
            hide lexi


        "B. As long as you keep your promise.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu angry_cu at mscmc_cu
            "(I don’t really care about the treasure, but I don’t want to seem easy to take advantage of.)"
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            mclexi "I’m in, but only if you keep your promise about giving me half the loot."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "Of course! I’m a mermaid of my word. Kraken eat me if I’m lying."
            hide lexi

        "C. I'm not going to abandon you now!":
            $menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "After all this, there’s no way I’m just going to bail on you. I mean, I just lied to my best friend to cover for you!"
            hide mscmc
            show lexi mermaid_cu sad_cu at lexi_cu
            lx "I’m sorry about that, but like I said, I really, really appreciate it."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Don’t be! This has been a life changing experience."
            hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Business aside, let's talk sleeping arrangements. I was thinking that you could have the bed and I'll camp out on the floor."
    hide mscmc
    show lexi mermaid_cu surprised_cu at lexi_cu
    lx "What?! No! I'm not going to push you out of your bed. I can just chill back in the tub. The water will be better for my tail anyway."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Are you sure?"
    hide mscmc
    show lexi mermaid_cu bigsmile_cu at lexi_cu
    lx "Positive."
    scene bg msc_mc_bedroom_night at bg
    "True to her word, Lexi ends up sleeping in the bathtub, leaving me to lie awake staring at the ceiling."
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(There's seriously a mermaid sleeping in the other room. This is just... I can't believe it's all real! What else don't I know about the world?)"
    hide mscmc
    "I struggle to fall asleep, but as I finally drift off, I can feel myself grinning. This is going to be amazing."
    scene bg msc_ocean_wide_night at bg with wipeleft
    stop music fadeout 1.0
    play music mscbeach
    show mscmc bikini_hairdown surprised at centre

    mclexi "Are you sure he's gone?"
    hide mscmc
    "It's the next night and Lexi and I are out in the water where Ned had been treasure hunting the previous day."
    show lexi mermaid smile at centre
    lx "I mean, it's kind of hard to miss that yacht of his."

    lx "Plus, it's pretty standard for treasure hunters to move on after a day of not finding anything."

    lx "And I already made sure there was no loot around where I parked."
    show lexi mermaid bigsmile at centre
    lx "Now come on! I want to show you my UV. I think you'll find it pretty awesome."
    show lexi mermaid bigsmile at centre:
        easein 0.4 yoffset -40
        easein 0.4 yoffset 600
    "Without waiting for a response, Lexi disappears, diving down into the dark ocean water."
    scene bg msc_underwater_night at bg with wipeup
    show uv_exterior-color at bg
    stop music fadeout 1.0
    play music msclexiuv
    "I dive under to follow her, and as we get near the ocean floor, I see what looks to be a hybrid between a spaceship and a submarine."
    show mscmc bikini_hairdown surprised at left3 with dissolve
    show lexi mermaid bigsmile at right3 with dissolve
    "As we get to the vehicle, Lexi opens a panel on the side and goes into a small entryway, waving for me to follow."
    hide lexi
    hide mscmc
    "I follow her and when I begin to swim in, I find that my head is suddenly out of the water."
    show mscmc bikini_hairdown surprised at left3
    show lexi mermaid surprised at right3
    mclexi "What the-!"

    lx "Careful! Bring your legs down so you don't face plant onto the floor."
    show lexi mermaid bigsmile
    "I follow Lexi's advice and find myself in the entrance way of the vehicle."
    hide lexi
    hide mscmc
    "Looking behind me, there's a faint shimmer and I wonder if the water is being held back by a magic force field."
    show lexi mermaid bigsmile at centre
    lx "Welcome to my humble home!"
    show lexi mermaid smile
    lx "I don't normally have visitors, especially not humans, so I hope you feel honored. Give me a second and I'll show you around."
    show lexi mermaid bigsmile
    "She laughs at her own cheesy introduction before grabbing a necklace off of a hook on the wall."
    #animation of white flash of light
    show lexi swim bigsmile at centre
    "As she puts it on her neck, I'm forced to shield my eyes from a bright light and when it finally fades, I'm shocked to see Lexi standing in front of me."
    hide lexi
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(She really does have a magic item to give her legs!)"
    hide mscmc
    show mscmc bikini_hairdown surprised at left3
    show lexi swim bigsmile at right3
    lx "Oh, don't make a big deal about it."

    "Her words contradict her expression. I can tell she's trying to play it cool, but my slack jawed amazement seems to make her happy."
    show mscmc bikini_hairdown sad
    mclexi "So, um, since you normally have your tail, how come there's no water in here?"
    hide mscmc
    hide lexi
    show lexi swim_cu bigsmile_cu at lexi_cu
    "Lexi laughs, as if the answer should be obvious."

    lx "The salt water degrades human antiques, especially books."

    lx "Speaking of antiques, come into the main room! There are some super awesome items in my collection that I want to show you!"

    "She holds out her hand, her face beaming with excited anticipation."
    hide lexi
    $menuhideborder = True
    menu lexis0e3c2:
        "A. Take Lexi's hand and check out her collection."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc bikini_hairdown grin at left3:
                easein 0.4 xoffset 40
            show lexi swim bigsmile at right3:
                easein 0.4 xoffset -40
            hide mscmc with dissolve
            hide lexi with dissolve
            "I take Lexi’s outstretched hand and am immediately pulled further into the UV."

            "(This is going to be amazing!)"
            scene bg msc_night_lightson_uv at bg
            show lexi swim bigsmile at centre
            lx "So, this is me..."

            "She holds her arms out and does a playful spin in the middle of the room and I take in all the amazing antiques she’s collected."
            hide lexi
            "The whole room is full of various treasures."

            "Some hang on the walls while others are piled on every available surface."
            show mscmc bikini_hairdown surprised at centre
            mclexi "This is... Just wow. I’ve never seen anything like this. And look at all the books!"
            hide mscmc
            "I look closer at the crammed bookshelf."
            show mscmc bikini_hairdown surprised at left3
            show lexi swim bigsmile at right3
            "It’s messy, but somehow adds to the magical aesthetic of the room."

            mclexi "Are all UVs this breathtaking?"

            lx "Well, not really. This is actually a super cheap basic one, but I’ve made a lot of modifications to it over the years."
            show mscmc bikini_hairdown grin
            show lexi swim embarrassed
            mclexi "It suits you."
            show lexi swim bigsmile
            "Lexi looks pleased by my statement but doesn’t say anything, letting me take everything in more."
            show mscmc bikini_hairdown surprised
            mclexi "Wow, this ship’s wheel is super fancy."
            hide lexi
            hide mscmc
            "In front of me is a huge ship’s steering wheel, it’s intricately carved and inlaid with what appears to be gold."
            show mscmc bikini_hairdown surprised at left3
            show lexi swim smile at right3
            lx "That, my dear [genericfn], is a wheel from the ship of an old sultan of Zanzibar."

            mclexi "It’s seriously amazing. It must be worth a fortune!"
            show lexi swim bigsmile
            "Lexi grins."

            lx "It is, but I like to keep the antiques that have the best stories behind them."

            lx "All the antiques here are reminders of the past, and a lot of the stories surrounding them are often completely unbelievable."
            hide mscmc
            hide lexi
            show lexi swim_cu bigsmile_cu at lexi_cu
            "As Lexi talks, I can see a passion in her eyes that adds to her natural beauty."
            hide lexi
            show mscmc bikini_hairdown_cu angry_cu at mscmc_cu
            "(Ah! Don’t think about that! You’re only pretending to be dating! Don’t catch feels! Say something, anything!)"
            show mscmc bikini_hairdown_cu embarrassed_cu
            mclexi "Um, are all UVs this size?"
            hide mscmc
            show lexi swim_cu smile_cu at lexi_cu
            "A mischievous look spreads across Lexi’s face."

            lx "Actually, most are a lot smaller, but thanks to Ned’s incompetence at finding treasure and my skill at it, I was able to expand this one."
            hide lexi
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            mclexi "What?! How so?"
            hide mscmc
            show lexi swim_cu bigsmile_cu at lexi_cu
            lx "I first met Ned last year. We were both looking for the Zanzibari shipwreck I got that wheel from."

            lx "Eventually there was only one spot left, and just before Ned and his henchmen could get to it, I swooped in and grabbed it for myself."
            show lexi swim_cu smile_cu
            "A devious smile spreads across Lexi’s face."

            lx "I may or may not have flaunted it in his face, too. And the rest of the stuff from that ship paid for work on the UV."
            hide lexi
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mclexi "That is diabolical. I can’t believe you did that!"

            "(She really is the real deal. All of these finds, buying this amazing UV by herself...)"
            hide mscmc
            show lexi swim_cu smile_cu at lexi_cu
            lx "If everything goes well, I’ll take this treasure out from under him, too. It’s getting cluttered in here and I need to make some additions."

            "As she grins, I can’t help but admire her roguish charm."
            hide lexi
            show lexi swim surprised at centre
            lx "Anywho, we should probably head out. Let me just..."
            show lexi swim bigsmile
            "She grabs a book off of the shelf and puts it into a waterproof bag."
            show mscmc bikini_hairdown smile at left3
            show lexi swim bigsmile at right3
            mclexi "What’s the book?"

            lx "Just another advantage over Ned. It’ll help us find the treasure."


        "B. Get nervous and decline her offer.":
            $menuhideborder = False
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(Go into the main room? I get nervous entering a human girl's house, let alone a gorgeous mermaid's!)"
            hide mscmc
            show mscmc bikini_hairdown embarrassed at left3
            show lexi swim surprised at right3
            mclexi "I... I'm sorry, maybe some other time."

            lx "Are you sure?"
            show mscmc bikini_hairdown smile
            show lexi swim basic
            "I nod and Lexi shrugs, thankfully not looking offended."
            show lexi swim bigsmile
            lx "Alright, let me just grab something real quick from inside and we can go."
            hide lexi with dissolve
            "She disappears into the UV for a moment."
            show lexi swim bigsmile at right3 with dissolve
            "Before coming back to the entrance with a sling bag strapped over her shoulder that she hurriedly stuffs an old book into."

            lx "Kay, let's go."

    scene bg msc_underwater_night at bg with dissolve
    show uv_exterior-color at bg
    pause
    show mscmc bikini_hairdown smile at left3
    show lexi mermaid bigsmile at right3
    stop music fadeout 1.0
    play music mscromance
    "Lexi switches back to her tail as we exit her UV and I swim behind her until she turns to face me."
    hide lexi
    hide mscmc
    show lexi mermaid_cu bigsmile_cu at lexi_cu
    lx "So I have a surprise for you. Think of it as a thank you for all your help."
    hide lexi
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(How can I hear her talking underwater? And it sounds so normal. Is this more magic?)"

    scene bg msc_underwater_kelp_night at bg
    show lexi mermaid_cu smile_cu at lexi_cu
    "Unable to answer her, I simply nod and Lexi begins to swim a bit further until we reach a small kelp forest."

    "We make our way through the tall, waving kelp until Lexi abruptly stops."
    show lexi mermaid_cu bigsmile_cu
    "She takes a moment and peaks through the dense wall of seaweed before waving me to her."
    hide lexi
    "As I swim up to her, Lexi spreads the kelp wider, then holds her hands up like she's showcasing something for me."
    show bg msc_lexi_short_mini2 at bg
    "It takes me a minute to process what she is showing me."

    "But as I continue to stare out into the darkness I realize I can see a mass of shining lights in the distance."

    "(Is that a city?!)"

    lx "Pretty cool, right?"

    "I nod excitedly, my eyes wide with wonder. Even though I can't make out the details of buildings, I'm looking at a real mermaid city."

    lx "Alright, let's head back up."
    scene bg msc_ocean_wide_night at bg
    pause
    #animation of gals coming back up
    show mscmc bikini_hairdown surprised at left3:
        yoffset 500
        easein 0.4 yoffset -10
    show lexi mermaid bigsmile at right3:
        yoffset 500
        easein 0.4 yoffset -10

    "It doesn't take us long to surface and I immediately start freaking out as soon as my mouth breaks the water."
    show mscmc bikini_hairdown grin
    mclexi "That was incredible! Thank you so much for showing me that. I genuinely feel like I'm the luckiest person alive right now!"
    show lexi mermaid embarrassed
    "As I continue to freak out, I notice that Lexi is blushing."

    lx "It was nothing. Just a small thanks for everything you've done so far."
    show lexi mermaid smile
    lx "Now then..."
    show mscmc bikini_hairdown smile
    "Calming myself down, I watch as Lexi pulls the book she had taken from the UV out of her bag."

    lx "With this, together we can..."
    show mscmc bikini_hairdown embarrassed
    "I can barely pay attention to the end of Lexi's sentence as my mind begins to echo the word 'together.'"
    hide lexi
    hide mscmc
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Together... We're doing this together! Lexi and I...)"
    show mscmc bikini_hairdown embarrassed at left3
    show lexi mermaid surprised at right3
    lx "Are you okay?"
    show mscmc bikini_hairdown surprised
    "I snap out of my thoughts and nod."
    show mscmc bikini_hairdown grin
    show lexi mermaid smile
    mclexi "Yeah! We're going to use that book and find the treasure before Ned. Together."
    scene bg msc_surf_shop_day at bg with clockwise_wipe
    stop music fadeout 1.0
    play music mscsurfshop
    "Lexi stretches her arms out and yawns as we both sit behind the checkout counter of the surf shop."
    show mscmc casual_hairdown sad at left3
    show lexi casual angry at right3
    lx "I'll never understand how merchants can do it. Sitting here like this is so boring!"

    mclexi "I know, I'm sorry! Trina really needed me to cover. I know you'd rather be out looking for the treasure."
    show lexi casual basic
    "Lexi waves off my apology with her hand."
    show mscmc casual_hairdown smile
    show lexi casual smile
    lx "I told you we're going to find it together."
    show mscmc casual_hairdown surprised
    mclexi "What's so special about this find anyways? Wouldn't it be easier to just look somewhere else since Ned is harassing you?"
    show lexi casual angry
    lx "Well, of course it would be. But I'm not about to lose to Ned and let him take the treasure."

    lx "Not to mention he is so disrespectful to the sites he searches."

    mclexi "How?"

    lx "He only cares about fame and fortune."
    show mscmc casual_hairdown angry
    lx "He trashes everything around what he's looking for and doesn't care if he messes up the local ecosystems."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(That doesn't surprise me.)"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "Ugh! He just boils my blood!"

    "Lexi's face flushes as she clenches her fists."
    hide lexi
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I should change the subject...)"
    hide mscmc
    $menuhideborder = True
    menu lexis0e3c3:
        "A. Ask about Lexi's approach to treasure hunting.":
            $menuhideborder = False
            show mscmc casual_hairdown surprised at left3
            show lexi casual basic at right3
            mclexi "Does treasure hunting often affect the ecosystem?"
            show lexi casual angry
            lx "Sometimes, but a responsible hunter is mindful of the ocean life around their finds, unlike Ned."
            show lexi casual basic
            lx "Taking your time excavating and leaving the wreck intact and other objects that sea life can live in is just as important as getting loot."

            mclexi "Have you ever had to give up on a find because of the environment?"
            show lexi casual basic
            lx "More than once, but it was worth it."



        "B. Talk about the ocean.":
            $menuhideborder = False
            show mscmc casual_hairdown angry at left3
            show lexi casual angry at right3
            mclexi "Someone should say something. If what you’re saying is true, he’s ruining the ocean for everyone."
            show mscmc casual_hairdown surprised
            lx "He really is. But maybe that’s just how humans are? It seems like they’re always causing trouble."

            mclexi "All humans?"
            show lexi casual smile
            "Lexi smiles at me, realizing she might have offended me."
            show mscmc casual_hairdown smile
            lx "Present company excluded."


        "C. Let her vent.":
            $menuhideborder = False
            show mscmc casual_hairdown surprised at left3
            show lexi casual angry at right3
            lx "He just doesn't understand what he's doing!"
            show lexi casual surprised
            lx "Did you know that the last time he destroyed an entire sunken ship with new coral on it to get to the find?"
            show lexi casual angry
            mclexi "But why?"
            show mscmc casual_hairdown sad
            lx "Because it was faster than diving down and slowly digging out the artifact."

            lx "He destroyed a newly grown coral reef just for money."

    show mscmc casual_hairdown sad at left3
    show lexi casual sad at right3
    stop music fadeout 1.0
    play music msclexi
    "Lexi sighs and I can tell that talking about Ned stresses her out."

    lx "Don't get me wrong, I'm all for the money, but the history and stories of the locations are just as important to me."
    show mscmc casual_hairdown surprised
    show lexi casual basic
    mclexi "Do you only go after human treasures?"
    show lexi casual smile
    "A roguish grin creeps across Lexi's face."

    lx "Not at all. Mer treasure is always on my radar. A lot of it ends up being magical and I sell it on the deep market."

    mclexi "Deep market?"
    show lexi casual surprised
    lx "Oh! Sorry, that's what we merfolk call... I think the human term is black market?"
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(The black market?! I know she said she'd had issues with the Mer police before, but is Lexi an actual criminal?)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "Calm down, I know that look."

    "She chuckles."
    show lexi casual_cu angry_cu
    lx "I'm not some shady criminal. I just think that everyone should have access to magical items, not just the Mer government."

    lx "They hoard all of it and then are surprised when the deep market meets demand."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Is the treasure we're looking for magical?"
    hide mscmc
    show lexi casual_cu basic_cu at lexi_cu
    lx "It's definitely possible, which is why I brought this captain's journal."
    hide lexi
    "She thrums her fingers on the worn cover of the book she had brought with her from her UV."
    show lexi casual_cu angry_cu at lexi_cu
    lx "It's another reason I want to get this treasure before Ned."

    lx "The last thing the world needs is for an addle-brained jerk to get his hands on mer magic."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "You're really passionate about your work."
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi smiles, seeming to take my statement as a compliment."

    lx "I am. I grew up in a small lake with a dad that was too agoraphobic to explore the world beyond books."

    lx "So now I just try to make everything an adventure."
    hide lexi
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mclexi "I can definitely understand that. I don't think I could live without surfing."
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    lx "Right?! The ocean is amazing and has so many opportunities, even for humans! It's why I hated living in that tiny lake growing up."

    "I find myself staring at Lexi as she gazes out the window, dreamy eyed."
    hide lexi
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's so gorgeous and driven. I wish I could have met her under different circumstances.)"
    hide mscmc
    "I scrunch my face up and slap myself lightly on the cheeks to push the thought out of my head."
    show ned vest basic at centre with dissolve
    stop music fadeout 1.0
    play music mscsuspense2
    dt "Well, I'll be... You really do work here."
    hide ned
    show mscmc casual_hairdown surprised at left3
    show lexi casual surprised at right3
    "Lexi and I both snap to attention as Ned walks up to the counter."
    hide mscmc
    hide lexi
    show ned vest basic at centre
    dt "I've been looking for you."
    hide ned
    show mscmc casual_hairdown sad at left3
    show lexi casual sad at right3:
        easein 0.4 xoffset -250
    "He eyes Lexi and suddenly I feel Lexi grab my hand."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Don't worry, Lexi. I've got your back.)"
    hide mscmc
    show mscmc casual_hairdown angry at left3:
        easein 0.4 xoffset 20
    show lexi casual sad at right3:
        xoffset -250
    "I squeeze her hand to reassure her and we both stare Ned down."

    lx "What do you want? We were having a nice day."
    hide lexi
    hide mscmc
    show ned vest basic at centre
    dt "I don't doubt it. I just wanted some advice."
    hide ned
    show lexi casual surprised at centre
    "I eye Lexi and I can tell that she has no idea what Ned is hinting at either."
    hide lexi
    show mscmc casual_hairdown angry at left3
    show ned vest basic at right3
    mclexi "Okay... Advice on what?"
    show ned vest smile
    dt "On how I can meet a cute girl like you! How'd you two meet?"
    hide ned
    hide mscmc
    show lexi casual angry at centre
    lx "We met on land."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(On land?! What does that even mean, Lexi?)"
    hide mscmc
    show mscmc casual_hairdown angry at left3
    show ned vest basic at right3
    mclexi "What she means to say is we met on the boardwalk a few weeks ago."

    dt "Is that so?"
    hide mscmc
    show ned vest basic at centre
    "He turns his attention away from us and starts to absently look around the shop."

    dt "Well, it doesn't matter."

    dt "I just dropped by to let you know that I will be leaving in the next few days after I find the treasure you thought you could steal from me."
    hide ned
    show lexi casual_cu angry_cu at lexi_cu
    "I try to shoot a questioning look at Lexi, but she doesn't notice, her attention focused on Ned."
    hide lexi
    show ned vest_cu basic_cu at ned_cu
    dt "Then again, plans change. I may have found something even more valuable than old pieces of collector's junk."

    "He picks up a snorkel mask and briefly looks at it before tossing it on a different shelf and looking at me."

    dt "Do you believe in mermaids?"
    hide ned
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "My eyes widen at the question and I immediately feel myself begin to panic."

    "(He'll throw Lexi in a cage and sell her to the highest bidder if he knows the truth!)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
