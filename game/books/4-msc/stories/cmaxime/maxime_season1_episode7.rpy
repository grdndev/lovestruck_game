label maxime_season1_episode7:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_boardwalk_sunset_people at bg
    play music mscromance

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime cradles me in his arms after dipping me, our noses practically touching."
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Please kiss me, Maxime! Please go for it!)"
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu:
        ease 1 zoom 1.1 xoffset -60 yoffset -30
    pause 1
    "Maxime leans in, and I instinctively close my eyes, tilting my lips up expectantly."
    
    play music mschappytimes
    show maxime casual_cu surprised_cu
    $sidecharone = "Seagull"
    sid1 "WAWK!"
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcmax "Ahh!"
    show mscmc jacket_hairdown embarrassed at left1plus
    show maxime casual embarrassed behind mscmc at right1plus
    "Maxime sets me gently on my feet, visibly flustered."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(And just like that, our magic moment's broken.)"

    hide mscmc
    $menuhideborder = True
    menu maximee07c1:
        "A. Get embarrassed.":
            $menuhideborder = False
            show mscmc jacket_hairdown embarrassed at left1plus
            show maxime casual embarrassed behind mscmc at right1plus
            "I desperately want to say something to Maxime, but it takes me a moment to cool my burning face."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Seriously, I feel like my cheeks are on fire!)"
            show mscmc jacket_hairdown embarrassed at left1plus
            show maxime casual embarrassed behind mscmc at right1plus
            "Maxime clears his throat."
        "B. Look hopeful.":
            $menuhideborder = False
            show mscmc jacket_hairdown embarrassed at left1plus
            show maxime casual embarrassed behind mscmc at right1plus
            "I look to Maxime hopefully, but he's retreated, flushing and rubbing the back of his neck."
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "He meets my eye and gives me a rueful smile."
        "C. Blame the seagull.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left1plus
            show maxime casual embarrassed behind mscmc at right1plus
            "The seagull's hopped over to rummage in a nearby trash can."
            show mscmc jacket_hairdown angry
            show maxime casual smile
            mcmax "Shoo! Why don't you go catch some fish?"
            "Maxime chuckles beside me."

    show mscmc jacket_hairdown surprised at left1plus
    show maxime casual smile behind mscmc at right1plus
    mx "I got a little carried away, sorry about that."
    show maxime casual sleep
    "He takes a deep breath, grounding himself."
    show maxime casual smile
    mx "I can only promise it won't happen again."
    mcmax "It's good to get carried away sometimes."
    
    play music mscsadtimes
    show maxime casual sad
    "Maxime looks out at the sea."
    show mscmc jacket_hairdown sad
    mx "Not for someone in my line of work."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Right...he's a spy.)"
    show mscmc jacket_hairdown sad at left1plus
    show maxime casual sad behind mscmc at right1plus
    "I hug my arms, trying to hide my disappointment."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Just don't run away from me again, Maxime.)"
    show mscmc jacket_hairdown smile at left1plus
    show maxime casual sad behind mscmc at right1plus
    "I clear my throat, trying to dispel the awkwardness with a force smile."
    mcmax "So, are we still on for some more sleuthing tomorrow?"
    show maxime casual basic
    mx "Right, the bar. We'll meet at Jerry's Beach Bar—that's where Raymond's search party seems to be gathering."
    show maxime casual smile
    mx "Does nine o'clock work?"
    "I keep my voice forcibly cheerful."
    show mscmc jacket_hairdown grin
    mcmax "That's perfect."
    mx "Good."
    "Maxime's smile is also pained, and he hesitates, as if about to say something more."
    show maxime casual sleep
    "Then he shakes his head, merely raising a hand in farewell."
    show maxime casual smile
    mx "Goodnight, [genericfn]."
    show mscmc jacket_hairdown sad
    show maxime casual smile at out_right
    "I wave back, and when he's turned away I finally let my shoulders sag."
    hide mscmc

    scene bg msc_beach_bar_day at bg with clockwise_wipe
    play music mscbeach
    show jerry casual smile at centre
    "Jerry's bar is always slow in the mornings, and Jerry gives us a lazy nod as we walk up."
    "A gaggle of people are passing out 'missing' posters next to the bar."
    hide jerry
    show mscmc jacket_hairdown smile at left3
    show maxime casual basic at right3
    mcmax "How do you want to play this?"
    "To my relief, nothing feels awkward between Maxime and me—though he was stiflingly professional when greeting me."
    "Maxime purses his lips, assessing the group of searchers."
    mx "Let me handle the talking at first, then follow my lead."
    "I willingly fall into step behind him, though I have to wonder how he fairs with intel-gathering."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Since he's not exactly Mr. Chatty with new people.)"
    hide mscmc
    show maxime casual basic at right1
    "A woman who I recognize as Raymond's trainer is struggling to keep her stack of flyers from blowing away in the sea breeze."
    show maxime casual smile
    mx "Let me give you a hand."
    "Maxime smiles warmly, transforming from teh shy man I know into an easy-going extrovert."
    show maxime casual smile:
        ease 0.4 yoffset 30
        ease 0.4 xoffset 50 yoffset 0
    pause 0.8
    "He catches her flyers before she drops them."
    $sidecharone = "Trainer"
    sid1 "Oh, thank you so much. I wanted to leave a stack on the bar."
    mx "I think we can manage that."
    show maxime casual smile:
        ease 0.4 xpos stagepos[1]
    pause 0.4
    "Maxime shuffles the flyers neatly and sets them under one of Jerry's decorative succulents."
    show maxime casual basic
    "The trainer relaxes, clearly eager to open up to someone."
    sid1 "It's all so awful. It's as though Raymond's disappeared into thin air."
    show maxime casual sad
    sid1 "I'm afraid the police think he's off on some bender, but that's not like Raymond."
    mx "He wasn't at any opening night parties?"
    show maxime casual basic
    "Maxime keeps his voice casual, one trainer to another."
    sid1 "No, he stays away from that sort of thing—he doesn't like to drink while a tournament's going."
    sid1 "Even when he went to dinner with Mr. Sapor, he promised me he'd only have a soda. He's so dedicated."
    "Maxime doesn't react, and I press my fingers to my lips to keep from displaying any emotion."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Wikus was showing an interest in Raymond and taking him out to dinner...That's eerily familiar.)"
    hide mscmc

    scene bg msc_labeach_day at bg with clockwise_wipe
    play music mscsurftraining
    show mscmc surfer_hairup basic at left1
    show maxime shorts basic behind mscmc at right1plus
    show surfboard_acc_back behind mscmc:
        zoom 0.7
        xpos -45
        ypos 390    
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.6
        xpos 595
        ypos 358
    "After our morning sleuthing, Maxime and I head out to the water for more training."
    hide maxime
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Got to keep up appearances so everyone thinks we're an ordinary surfer and her trainer.)"
    "(Plus, I still need to train.)"
    show mscmc surfer_hairup basic at left1
    show maxime shorts basic behind mscmc at right1plus
    show surfboard_acc_back behind mscmc:
        zoom 0.7
        xpos -45
        ypos 390    
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.6
        xpos 595
        ypos 358
    "I glance at Maxime, who's looking far more relaxed beside me as he carries his board to the surf, taking in a deep breath of salty air."
    show mscmc surfer_hairup surprised
    mcmax "I can't believe the beach is so empty!"
    show mscmc surfer_hairup smile
    show maxime shorts smile
    "Maxime grins, winking knowingly."
    show mscmc surfer_hairup grin
    mx "I can. I timed our training session with Jerry's happy hour so we'd have the place to ourselves."
    show maxime shorts embarrassed
    mcmax "Aw, best trainer ever!"
    show mscmc surfer_hairup grin:
        ease 0.5 xpos stagepos[1]-180
    show surfboard_acc_back:
        ease 0.5 xpos 33
    "He flushes and mutters something, and I just laugh, hopping onto my board to paddle out."
    hide maxime
    hide surfboard_acc_back
    hide surfboard_maxime_acc_back
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(I can't help but notice the way we're keeping everything carefully casual, dancing around what happened last night.)"
    
    scene bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Ugh, no time for that, [genericfn]—time to TRAIN.)"
    show mscmc surfer_hairup grin surfboard at left2
    show maxime shorts basic at right1plus
    show surfboard_maxime_acc_back behind maxime:
        zoom 0.8
        xpos 555
        ypos 308
    pause 0.2
    show maxime shorts basic:
        ease 0.4 xpos stagepos[1]+180
    show surfboard_maxime_acc_back:
        ease 0.4 xpos 375
    pause 0.4
    "Maxime joins me, straddling his board."
    mx "Alright, show me a little {i}oomph{/i}. The first wave you catch, I want to see some fire."
    show mscmc surfer_hairup basic surfboard
    "I roll my eyes, but obediently scan the horizon, searching for the ideal wave."
    mcmax "Surfing's not dancing, though. What even counts as 'flare'?"
    show mscmc surfer_hairup smile surfboard
    show maxime shorts embarrassed
    "Maxime startles at 'dancing', and now I'm also thinking of our dip on the pier."
    hide maxime
    hide surfboard_maxime_acc_back
    show mscmc surfer_hairup_cu sleep_cu -surfboard at mscmc_cu
    "(He says we can't be anything more than friends, but that was so romantic!)"
    show mscmc surfer_hairup smile surfboard at left2
    show maxime shorts basic surfboard at right2
    "He quickly gestures broadly at the water around us."
    mx "Loosening up, for starters. Stop tryuing to be a paragon of surfing all the time—it's impossible."
    show mscmc surfer_hairup basic surfboard
    show maxime shorts smile surfboard
    mx "You don't have to distance yourself from the performance to get a perfect ten."
    mx "The judges want to see {i}you{/i}, [genericfn], in your element."
    show mscmc surfer_hairup surprised surfboard
    mcmax "I suppose..."
    hide maxime
    show mscmc surfer_hairup smile surfboard at centre
    pause 0.3
    show mscmc surfer_hairup smile surfboard at centre, step_out
    "When I finally catch a wave, I manage a snap across its face, the deep blue water arcing over me until I neatly take the plunge."
    hide mscmc
    show mscmc surfer_hairup grin surfboard at left3:
        yoffset 100
        pause 0.3
        ease 0.5 yoffset 0
    show maxime shorts basic surfboard at right3
    pause 0.8       
    "I paddle back to Maxime and shake my hair out, looking up at him expectantly."
    mcmax "Well? How was that for flare?"
    show maxime shorts smile surfboard
    "Maxime first gives me a thumbs up, then tilts his palm from side to side."
    show mscmc surfer_hairup basic surfboard
    mx "A beautiful, gracefully executed maneuver worth lots of points! Though I didn't see much [genericfn]-ness specific flair."
    show mscmc surfer_hairup angry surfboard
    mx "Be free! Give yourself a break!"
    show mscmc surfer_hairup angry surfboard:
        ease 0.6 yoffset 50
    pause 0.6
    "I grumble crossing my arms as I lean on my board."
    show mscmc surfer_hairup smile surfboard
    show maxime shorts surprised surfboard
    mcmax "I'm plenty free! I'd say I'm more easy-going than you."
    show mscmc surfer_hairup grin surfboard
    show maxime shorts smirk surfboard
    "I arch an eyebrow at him, but Maxime just smirks, ignoring the bait."
    show mscmc surfer_hairup basic surfboard
    mx "Not on a surfboard, apparently. The ocean's the one place I get to let loose."
    show mscmc surfer_hairup smile surfboard
    show maxime shorts basic surfboard
    mcmax "Compared to elsewhere, I suppose."
    hide mscmc
    show maxime shorts_cu smile_cu -surfboard at maxime_cu
    mx "Trust me. I'm more fun in the water."
    show maxime shorts_cu smirk_cu
    mx "What, you want me to show you how it's done?"
    "He gives me a cheeky grin, looking unusually gleeful."
    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(I am always trying to get him to loosen up.)"
    
    hide mscmc
    $menuhideborder = True
    menu maximee07c2:
        "A. Loosen up with Maxime!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc surfer_hairup grin surfboard at left3:
                yoffset 50
            show maxime shorts smile surfboard at right3
            mcmax "Yeah, I do want you to show me!"
            mcmax "I'll race ya to the next wave."
            play sound big_splash
            show mscmc surfer_hairup grin surfboard:
                ease 0.3 yoffset 0
            pause 0.3
            show mscmc surfer_hairup grin surfboard at step_out
            pause 0.4
            "I hop swiftly on my board, paddling out and taking advantage of my head start."
            show maxime shorts smirk surfboard
            mx "Tsk, cheating again!"
            show maxime shorts smirk surfboard at step_out
            pause 0.4
            hide mscmc
            hide maxime # to reset their alphas
            "Maxime shakes his head, quickly catching up with powerful strokes, his arms cutting through the water."
            "There's a cluster of three large waves, he snags the first one but I'm right behind him."
            show mscmc surfer_hairup surprised surfboard at centre
            "I catch my wave fine, but feel my board listing before I've ridden its entire length."
            show mscmc surfer_hairup_cu basic_cu -surfboard at mscmc_cu
            "(Damn, I guess this is my stop.)"
            show mscmc surfer_hairup surprised at centre
            show surfboard_acc_back behind mscmc:
                zoom 0.7
                xpos 240
                ypos 390
            play sound big_splash
            show mscmc surfer_hairup surprised:
                ease 0.6 yoffset 900
                pause 0.2
                ease 0.6 yoffset 120
            show surfboard_acc_back:
                ease 0.6 xoffset -250
            pause 1.4
            "I dive from my board before the wave breaks and pop back up to watch Maxime cutting a beautiful trail through the barrel of his."
            hide mscmc
            hide surfboard_acc_back
            show maxime shorts basic surfboard at centre:
                zoom 0.9
                yoffset 65
                xoffset 45
                ease 0.8 zoom 1.0 xoffset 0 yoffset 0
            pause 0.8
            "His arms are held loosely aloft, and his gaze is firmly on the horizon, calm and at-ease."
            show maxime shorts smile -surfboard
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.8
                xpos 145
                ypos 305
            pause 0.3
            play sound big_splash
            show maxime shorts smile:
                ease 0.6 xoffset 80 yoffset 600
            show surfboard_maxime_acc_back:
                ease 0.6 xoffset -100
            pause 0.6
            "It's like he's dancing with the wave, like I can see that his soul is joyful in this moment."
            hide maxime
            hide surfboard_maxime_acc_back
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Well, he's got a natural advantage in {i}some{/i} areas concerning the ocean.)"
            hide mscmc
            show maxime mermaid smile at centre:
                xoffset 650
                yoffset 600
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.8
                xpos 45
                ypos 305
            play sound big_splash
            show maxime mermaid smile:
                ease 0.4 yoffset 130
            pause 0.4
            "Maxime bursts through the surface after finishing his ride, water droplets rolling off his muscular shoulders and down his chest."
            hide surfboard_maxime_acc_back
            hide maxime
            show maxime mermaid_cu smirk_cu at maxime_cu
            mx "Looks like I held on for longer."
            hide maxime
            show mscmc surfer_hairup sad at left2:
                yoffset 120
            show surfboard_acc_back behind mscmc:
                zoom 0.7
                xpos -105
                ypos 390   
            show maxime mermaid smirk at right2:
                yoffset 130
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.8
                xpos 495
                ypos 288
            "I pretend to sulk, sticking my nose up in the air."
            show mscmc surfer_hairup embarrassed
            mcmax "Maybe your wave was better."
            show mscmc surfer_hairup smile
            show maxime mermaid smile
            mx "Waves aren't anything other than what we make them."
            show mscmc surfer_hairup embarrassed
            
            play music mscromance
            mx "You've got to stop worrying about technique and just... give in to what you want."
            show maxime mermaid smirk
            mcmax "And will that give me 'flare'?"
            show mscmc surfer_hairup smile
            show maxime mermaid smile
            mx "It's a start."
            mx "You're the only experiencing the wave and you have to channel that experience into your own self-expression."
            show mscmc surfer_hairup embarrassed
            "(He looks so beautiful out here with the sun beating down on us and the clear blue water lapping at our boards. What was he just saying?)"
            show mscmc surfer_hairup smile
            show maxime mermaid smirk
            mcmax "Well...I'll take that into consideration."
            play sound splash04
            show mscmc surfer_hairup grin:
                ease 0.6 xoffset -50 yoffset 0
            show surfboard_acc_back:
                ease 0.6 xoffset 90
            "I leap neatly on my board, managing to splash him as I do."
            mx "Oi!"
            show mscmc surfer_hairup smile
            "Maxime shakes the water from his face, looking up at me wryly."
            show mscmc surfer_hairup grin
            mcmax "{i}So{/i} sorry, I swear that was an accident..."
            show mscmc surfer_hairup surprised
            mx "Oh really? How's your dodge?"
            play sound splash04
            show maxime mermaid smirk:
                ease 0.3 xoffset -20
                ease 0.3 xoffset 0
            show mscmc surfer_hairup grin:
                pause 0.6
                ease 0.8 xoffset 65 yoffset 900
            show surfboard_acc_back:
                pause 0.6
                ease 0.3 xoffset -10
            "He splashes me back, and I manage to leap out of the way, diving back into the water and giggling."
            show mscmc surfer_hairup grin behind maxime:
                ease 0.3 yoffset 130
            pause 0.9
            "I pop back up and hug the edge of my board smugly. He reaches over and pulls my board and me closer to him."
            show mscmc surfer_hairup surprised
            mcmax "Pretty good, it looks like—oh!"
            show maxime mermaid smile
            "I gasp as something solid and warm brushes my leg."
            show mscmc surfer_hairup surprised:
                ease 0.3 xoffset -40
            pause 0.3
            "I instinctively scramble onto my board."
            show mscmc surfer_hairup smile
            show maxime mermaid basic
            mcmax "Was that...?"
            "(Maxime holds my gaze intensely as I figure out what touched my leg and slip back into the water beside him.)"
            show maxime mermaid smile
            mx "Did I scare you?"
            show mscmc surfer_hairup embarrassed
            "Maxime's smile tells me there's nothing to be afraid of."
            show mscmc surfer_hairup grin
            "He angles to the side, as his shimmering, vibrant tail breaks the water in a gentle arc."
            show mscmc surfer_hairup embarrassed
            "I stare at him, slack-jawed, in awe of his full beauty."
            show mscmc surfer_hairup grin
            mcmax "Were you trying to prank me?"
            show maxime mermaid embarrassed
            mcmax "Who are you and what have you done with Maxime?"
            show mscmc surfer_hairup embarrassed
            show maxime mermaid smirk
            mx "I told you, I can be fun. It's just easier out here."
            play sound splash04
            show maxime mermaid smile:
                ease 0.3 xoffset -20
                ease 0.3 xoffset 0
            "While I'm still staring, flabbergasted, he slaps the water playfully with the fin at the end of his tail and drenches me."
            show mscmc surfer_hairup surprised
            "I'm unable to dodge the water at all."
            show mscmc surfer_hairup grin
            show maxime mermaid smirk
            mcmax "Hey, not fair, some of us don't have a tail!"
            play sound splash03
            show mscmc surfer_hairup surprised
            show maxime mermaid smirk:
                ease 0.6 yoffset 900
            pause 0.6
            "He snickers, disappearing beneath the surface with another flick of his tail."
            hide maxime
            hide mscmc
            hide surfboard_acc_back
            hide surfboard_maxime_acc_back
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(But I {i}am{/i} also unusually good at maneuvering underwater, well, for a human.)"
            play sound splash03
            show surfboard_acc_back behind mscmc:
                zoom 0.7
                xpos -115
                ypos 390   
            show surfboard_maxime_acc_back:
                zoom 0.8
                xpos 495
                ypos 288
            show mscmc surfer_hairup smile at left2:
                xoffset -40
                yoffset 0
                ease 0.9 yoffset 900
            pause 0.9
            "I take a deep breath and dive down to meet him, quickly zeroing in on Maxime's brightly colored tail."
            play sound big_splash
            scene bg msc_underwater_ship_day at bg with wipediagTLBRdissolve
            show maxime mermaid smile at right3:
                yoffset 900
                ease 0.6 yoffset 130
            show mscmc surfer_hairup grin at left3:
                yoffset 900
                pause 0.6
                ease 0.6 yoffset 130
            "I give his tail fin a very gentle little tug, and he turns to look at me, with a spark in his eye, laughing. Then we head back for the surface."
            scene bg msc_ocean_wide_day at bg with wipediagTLBRdissolve
            show maxime mermaid smile at right3:
                yoffset 130
            show mscmc surfer_hairup grin at left3:
                yoffset 130
            show surfboard_acc_back behind mscmc:
                zoom 0.7
                xpos -115
                ypos 390   
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.8
                xpos 495
                ypos 288
            mcmax "Tag, you're it."
            show mscmc surfer_hairup surprised
            show maxime mermaid smirk:
                ease 0.3 xoffset -90
            pause 0.3
            "He brings his tail up to tap my shoulder lightly with the edge of his fin."
            show mscmc surfer_hairup grin
            mx "No, you're it."
            show mscmc surfer_hairup smile
            show maxime mermaid smile
            mcmax "We could be at this tag game forever if we're not careful."
            mx "You're probably right, I wouldn't mind."
            show mscmc surfer_hairup embarrassed
            show maxime mermaid smile:
                ease 0.6 xoffset 0
            pause 0.6
            "He chuckles, laying back on his board, and I get a good view of his shining abs and where his torso meets his tail."
            "I've never seen him so relaxed, he's laid out like the ocean is gently holding him."
            hide mscmc
            hide maxime
            hide surfboard_acc_back
            hide surfboard_maxime_acc_back
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(He's really just a big goof ball. A sexy goof ball.)"
            show maxime mermaid smile at right3:
                yoffset 130
                ease 0.5 xoffset -90
            show mscmc surfer_hairup embarrassed at left3:
                yoffset 130
                ease 0.5 yoffset 0
            show surfboard_acc_back behind mscmc:
                zoom 0.7
                xpos -115
                ypos 390
                ease 0.5 xoffset 110
            show surfboard_maxime_acc_back behind maxime:
                zoom 0.8
                xpos 495
                ypos 288
            "Maxime nudges my surfboard back to me with his tail, gently helping me back on."
            show mscmc surfer_hairup smile
            mx "Ready to try another wave?"
            show mscmc surfer_hairup grin
            "I smile, feeling invigorated from our little break."
            mcmax "Watch me."
            hide mscmc
            hide maxime
            hide surfboard_acc_back
            hide surfboard_maxime_acc_back
        "B. Forget it.":
            show mscmc surfer_hairup_cu basic_cu at mscmc_cu
            mcmax "Forget it."
            hide mscmc

    scene bg msc_labeach_day at bg with clockwise_wipe
    play music mscbeach
    show mscmc surfer_hairdown basic at left3
    show maxime shorts basic at right3
    "We keep up our 'debate' about flair throughout our session, even as we drag our boards up the sand."
    show mscmc surfer_hairdown smile
    mcmax "Maybe the '[genericfn] flair' is just about being really technically perfect."
    show maxime shorts smile
    "Maxime pretends to be stoic, even as his mouth twitches in a smile."
    show mscmc surfer_hairdown surprised
    mx "Being alive is to be imperfect."
    show mscmc surfer_hairdown basic
    show maxime shorts basic
    mcmax "I'd be a robot if it made me a better surfer."
    show mscmc surfer_hairdown surprised
    mx "But a robot couldn't love the ocean the way you do."
    hide mscmc
    hide maxime
    show dawn casual sleep at centre
    "The beach is still fairly empty, though we notice Dawn seated on the sand, legs crossed and silently meditating."
    show dawn casual smile
    "They open their eyes once we're within earshot as they probably recognized our voices."
    show dawn casual grin
    dw "Oh, hey! It's my faves."
    show mscmc surfer_hairdown smile at left3
    show dawn casual surprised at right3
    mcmax "Hiya, Dawn. Can you settle a matter of sports philosophy for us?"
    show mscmc surfer_hairdown grin
    show dawn casual grin
    "Dawn folds their hands, appearing very sage."
    dw "Hit me."
    hide dawn
    show maxime shorts smirk at right3
    mx "Yes, I'm curious to hear your take on our surfing quandry."
    show maxime shorts embarrassed
    "I stick my tongue out playfully at Maxime before turning back to Dawn."
    hide maxime
    show dawn casual smile at right3
    show mscmc surfer_hairdown smile
    mcmax "To what extent does an athlete have to embrace the 'self' to really excel? Or can everything just be all about technique?"
    hide dawn
    show maxime shorts smirk at right3
    "(I shoot a glance that he returns with a quirked eyebrow that sets my heart beating all over the place.)"
    hide maxime
    show mscmc surfer_hairdown surprised
    show dawn casual grin at right3
    dw "Dudes, dudes, I have an answer."
    show mscmc surfer_hairdown smile
    show dawn casual smile
    "Dawn raises their hands, motioning for silence."
    show dawn casual sleep
    dw "Remember, we're all on a quest for perfection and self-truth, that quest is life."
    show mscmc surfer_hairdown grin
    show dawn casual smile
    mcmax "Okay...?"
    show mscmc surfer_hairdown smile
    dw "I'm saying, maybe it's not an either-or. All struggles are one."
    show dawn casual grin
    "They link their hands together, then shrug."
    show dawn casual embarrassed
    dw "Or whatever. You gotta define your own truth."
    hide dawn
    show maxime shorts basic at right3
    show mscmc surfer_hairdown surprised
    "I'm still a little befuddled, but I raise my eyebrows at Maxime."
    show mscmc surfer_hairdown embarrassed
    show maxime shorts embarrassed
    mcmax "Maybe that means we should meet halfway?"
    hide mscmc
    show maxime shorts_cu smile_cu at maxime_cu
    "He smiles, with a fondness in his eyes that I can't quite read."
    mx "Yeah... maybe we should."

    hide maxime
    scene bg msc_maxime_studio_day at bg with clockwise_wipe
    play music mscmaxime
    show mscmc casual_hairdown smile at left3
    show maxime casual basic at right3
    "We say goodbye to Dawn and walk towards Maxime's studio."
    show mscmc casual_hairdown basic
    show maxime casual basic
    "He turns to me as we step through the doorway, growing serious once more."
    mx "I'm meeting Camilla here to brief her. She wants an update on the investigation."
    show mscmc casual_hairdown surprised
    show maxime casual angry
    mx "You deserve to hear what's discussed since you're a part of all this, but..."
    show mscmc casual_hairdown grin
    mcmax "Oh, that's no problem! I can hide in your closet again."
    show maxime casual surprised
    "I beam, enjoying Maxime's surprise."
    show maxime casual embarrassed
    mx "You...want to hide in the closet again?"
    show mscmc casual_hairdown smile
    show maxime casual smile
    mcmax "Hey, it worked last time. If it ain't broke, don't fix it."

    hide maxime
    hide mscmc
    $menuhideborder = True
    menu maximee07c3:
        "A. We'll make it cozier.":
            $menuhideborder = False
            show mscmc casual_hairdown smile at left3
            show maxime casual smile at right3
            mcmax "We can make it cozier. Have you gotten a pillow or something I can borrow?"
            show mscmc casual_hairdown grin
            mx "Uh...I do, actually."
            show maxime casual smile:
                ease 0.5 xoffset 60
                ease 0.5 xoffset -40
            pause 1.0
            "Maxime's thoroughly bemused, but helps me drag a small beanbag into the closet."
            hide mscmc
            hide maxime
        "B. I'll hide better":
            $menuhideborder = False
            show mscmc casual_hairdown smile at left3
            show maxime casual basic at right3
            mcmax "I'll hide better this time, so she won't try to peek through the slats."
            mcmax "You've got extra of the sheets you set down for painting in there. I'll just hide behind one."
            show maxime casual smile
            mx "Well, alright..."
            show mscmc casual_hairdown grin
            show maxime casual sleep
            "Maxime shakes his head, surrendering to my crazy idea."
            show mscmc casual_hairdown smile
            show maxime casual smile:
                ease 0.5 xoffset -40
            pause 0.5
            "We drape the sheet so it sits like a tent and I can hide inside."
            hide mscmc
            hide maxime
        "C. I'm starting to like it in there":
            $menuhideborder = False
            show mscmc casual_hairdown smile at left3
            show maxime casual embarrassed at right3
            mcmax "Your closet isn't actually a bad place to be. You're actually really well organized, and it's pretty spacious."
            show maxime casual smile
            mx "Well, I guess, but.."
            show mscmc casual_hairdown grin
            show maxime casual surprised
            mcmax "You know, when this is over we could do something with it."
            show maxime casual smile
            mcmax "Dawn told me they set up a little meditation space in theirs with an oil diffuser. Think about it!"
            show mscmc casual_hairdown grin:
                ease 0.5 xoffset 80
            "Maxime shakes his head with a despairing laugh as I slip into the closet."
            hide mscmc
            hide maxime

    show maxime casual_cu sad_cu at maxime_cu
    "He closes the closet door and gives the slats a questioning look. I throw him a thumbs-up, not totally sure he can see me."

    play music msctense
    play sound "audio/sfx/79_door open.mp3"
    show maxime casual basic at left3
    show camilla casual basic at right3, step_in
    "I'm completely hidden from view when Maxime opens the door to Camilla, who stalks in on her high-heeled sandals."
    show camilla casual angry
    cm "I got your message. You're certain it was Raymond Church in the live footage on Wikus' phone."
    show camilla casual smirk
    mx "Positive. [genericfn] and I got a good look at him during opening night."
    show camilla casual smile:
        ease 0.4 xoffset -50
    pause 0.4
    "Camilla starts to pace, excited despite the grim news."
    show camilla casual smile:
        ease 0.4 xoffset 0
    pause 0.4
    cm "I {i}knew{/i} Sapor was up to something. This vindicates me with the Bureau."
    show camilla casual smile:
        ease 0.4 xoffset -50
    pause 0.4
    cm "What else have you found?"
    show camilla casual smile:
        ease 0.4 xoffset 0
    pause 0.4
    show maxime casual sad
    "Maxime sighs, I can tell he's a little frustrated in the face of her excitement."
    show camilla casual smile:
        ease 0.4 xoffset -50
    pause 0.4
    show maxime casual basic
    mx "We still don't know the location where Wikus is holding Raymond."
    show camilla casual basic:
        ease 0.4 xoffset 0
    pause 0.4
    mx "Raymond's trainer says Wikus showed an interesting him—taking him out to dinner, that sort of thing."
    show camilla casual smirk
    "Through the slats in the door, I see Camilla stop abruptly, turning to Maxime."
    show camilla casual smile
    cm "Like he has with your girl? He took you two out for sushi, right?"
    hide maxime
    hide camilla
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(She called me 'his girl.' Ok, I've got to get it together, this is not the time for butterflies.)"
    hide mscmc
    show maxime casual angry at left3
    show camilla casual smirk at right3
    "I can feel Maxime's discomfort radiating through the door."
    show maxime casual sad
    mx "...Yes."
    show maxime casual sleep
    "Camilla hums, pleased."
    show maxime casual surprised
    cm "That's good. We can work with that."
    show maxime casual basic
    show camilla casual smile
    cm "Listen, I don't think Wikus Sapor is keeping Raymond Church hostage for his own sick curiosity."
    cm "Wikus likes his science, but he likes money and power more."
    mx "You think he's working for someone else?"
    show maxime casual angry
    show camilla casual smirk
    cm "Precisely, and I want you to find out who, with the help of surfer chick."
    show maxime casual surprised
    cm "Where's that file I gave you on Wikus' movement after he moved to the surface?"
    show camilla casual angry
    "Maxime's eyes dart to the closet I'm hiding in."
    hide maxime
    hide camilla
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(There is, indeed, a file cabinet in here.)"
    show mscmc jacket_hairdown_cu sad_cu
    "(Uh oh.)"
    hide mscmc
    show maxime casual smile behind camilla at left3:
        ease 0.4 xoffset 130
    show camilla casual basic at right3:
        ease 0.4 xoffset -50
    pause 0.4
    "Maxime clears his throat, subtly moving to stand between her and the closet."
    show maxime casual basic
    show camilla casual angry
    mx "I'll get it to you tomorrow."
    show maxime casual smile
    show camilla casual surprised
    mx "I want to double-check some things before I write up my report."
    show maxime casual basic
    show camilla casual sad
    "I peer through the slats, watching Camilla frown over Maxime's shoulder."
    show camilla casual basic
    cm "Alright. Anyway, we can make use of Wikus' new interest in [genericfn]."
    show maxime casual angry
    show camilla casual smile
    cm "She'll do anything you ask, right? She trusts you."
    show camilla casual basic
    "Maxime stiffens, his voice growing cold."
    mx "I don't want her to be involved in this any further. Serving as my cover story is one thing, but..."
    hide camilla
    hide maxime
    show maxime casual_cu angry_cu at maxime_cu:
        xoffset -270
    show camilla casual_cu angry_cu at camilla_cu:
        xoffset 270
    "Camilla cuts him off, jabbing a finger in his face."
    cm "Let me be clear: this is an order, not a request."
    show camilla casual_cu smile_cu
    cm "And I'll take that as a yes, she trusts you completely. So let me tell you how you're going to use her..."

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    hide camilla
    hide maxime
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.