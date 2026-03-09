label maxime_season1_episode8:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_maxime_studio_day at bg
    play music msctense

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "I lean forward, listening to Maxime and Camilla's conversation with bated breath while trying not to rustle anything in the closet."
    "(And what does Camilla want me to do—supposedly without my knowledge—now?)"
    "(Funny, she went from not liking me to finding me pretty useful.)"
    hide mscmc
    show maxime casual angry behind camilla at left3:
        xoffset 130
    show camilla casual angry at right3:
        xoffset -120
    cm "Encourage her, as her trainer, to get closer to Wikus. No one will see anything suspicious—after all, it's good networking."
    mx "But—!"
    "Camilla cuts into Maxime's outrage."
    show camilla casual smirk
    cm "I've got a tracker you can plant on her. That way, she'll never really be out of your sight, and we can keep tabs on Wikus."
    hide maxime
    hide camilla
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(That's...actually not a bad idea, as much as I hate to admit it.)"
    hide mscmc
    show maxime casual angry behind camilla at left3:
        xoffset 130
    show camilla casual smirk at right3:
        xoffset -120
    mx "You want to use [genericfn] as bait."
    show camilla casual smile
    "Maxime's voice is cutting, but Camilla rolls her eyes."
    show camilla casual smirk
    cm "What does it matter if we've got the tracker in place? Hell, she's probably safer with it on."
    "Maxime sputters indignantly."
    mx "What does it matter? Why don't {i}you{/i} take Wikus into custody?"
    mx "You've got the bloody shirt and the security cam footage, that's plenty of evidence!"
    mx "Why let Raymond languish in captivity? Why leave the other humans at risk?"
    "Camilla scoffs, crossing her arms."
    show camilla casual smile
    cm "You haven't been listening. There's no way Sapor is working alone, so no, the smoking gun you found in his office isn't enough."
    cm "Once I take him in the jig's up and he can play dumb in interrogation, which I know he's fully capable of."
    show camilla casual smirk
    cm "If you're worried about the humans, then worry about the bigger picture."
    show camilla casual sad:
        ease 0.4 xoffset -185
    "She steps nearer to Maxime, frowning perceptively at him."
    cm "What's gotten into you? You didn't have any problems with the plan when you started the mission."
    show maxime casual sad
    cm "What's different—your little surf protegee?"
    show maxime casual angry
    cm "You wouldn't happen to have any special feelings for her, would you?"
    hide maxime
    hide camilla
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Oof. Speaking of interrogation rooms, I would really hate to be in one with Camilla.)"
    "(I wonder how Maxime will respond to that.)"
    hide mscmc
    show maxime casual basic behind camilla at left3:
        xoffset 130
    show camilla casual angry at right3:
        xoffset -185
    "There's a long, loaded silence—probably a little too long, as Camilla's frown gets deeper by the second."
    show camilla casual basic
    "Finally, Maxime speaks, his voice clipped."
    show maxime casual angry
    mx "I'll do what needs to be done to keep people safe."
    mx "I'll see you tomorrow Camilla."
    show camilla casual smile
    "His words are final, and he lifts his hand, gesturing her firmly towards the door."
    show camilla casual smirk at out_right_slow
    pause 1.0
    "Camilla turns on her heels, flipping her hair over her shoulder smugly, and stalks out."
    hide camilla
    hide maxime

    show maxime casual_cu sad_cu at maxime_cu
    play sound "audio/sfx/79_door open.mp3"
    play music mscsadtimes
    "When her footsteps have faded, Maxime walks over to the closet, pulling the door open."
    "He leans in the doorway, shoulders drooping, and I'm tempted to give him a hug."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I wish he didn't have to worry so much. I wish I could protect him instead of it always being the other way around.)"

    hide mscmc
    $menuhideborder = True
    menu maximee08c1:
        "A. Commiserate.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left2minus
            show maxime casual sad behind mscmc at right2minus
            "I throw my hands up, exasperated on his behalf."
            mcmax "She should have listened to you! Saving Raymond and putting Wikus behind bars is clearly the top priority."
            mcmax "Is she always like that?"
            hide mscmc
            show maxime casual_cu sad_cu at maxime_cu
            "Maxime nods wearily."
            mx "It's pretty standard."
            hide maxime
        "B. Squeeze his hand.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Maybe I can't hug him, but I have to do something.)"
            hide mscmc
            show maxime casual_cu sad_cu at maxime_cu
            "I reach out, clasping his hand in a gentle squeeze and offering him a reassuring smile."
            hide maxime
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            mcmax "Hey, it's gonna be okay."
            hide mscmc
            show maxime casual_cu basic_cu at maxime_cu
            "Maxime hesistates, then briefly squeezes my hand back, thankful."
            hide maxime
        "C. Hand him his missing file.":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left1plus
            show maxime casual sad behind mscmc at right2minus
            mcmax "Um."
            show maxime casual basic
            show mscmc jacket_hairdown basic:
                ease 0.5 xoffset -30
            "I'm not quite sure what to do, so I reach for his file cabinet awkwardly."
            mcmax "Here's that file she wanted, I think...?"
            mcmax "Just, you know, so you don't have to go looking for it."
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime takes the file, a smile playing on his lips."
            mx "Thanks, I appreciate that."
            hide maxime

    show mscmc jacket_hairdown smile at left2minus
    show maxime casual smile behind mscmc at right2minus
    "I nod towards the beach outside his window."
    mcmax "Want to grab some fresh air?"
    mx "I think that sounds like a great idea."

    scene bg msc_labeach_day at bg with wiperightdissolve
    play music mscbeach
    show mscmc jacket_hairdown basic at left2minus
    show maxime casual basic behind mscmc at right2minus
    "Maxime locks up the studio, and we take a leisurely stroll down the beach, letting the briny air clear our heads."
    show mscmc jacket_hairdown sad
    "Maxime is quiet, but I'm desperate to unpack everything we've just heard, and I can feel his tense energy radiating beside me."

    hide mscmc
    hide maxime
    $menuhideborder = True
    menu maximee08c2:
        "A. Here's what I'm feeling.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left2minus
            show maxime casual basic behind mscmc at right2minus
            "I start speaking gently."
            mcmax "I know you're worried about me, but here's what I'm thinking."
            show mscmc jacket_hairdown basic
            mcmax "I agree with you that Camilla's priorities are skewed, but I don't hate her idea about a tracker."
            show mscmc jacket_hairdown grin
            show maxime casual angry
            mcmax "It wouldn't hurt me, and Wikus 'showing an interest' already gave us one lead."
            show mscmc jacket_hairdown basic
            mx "Yes, but at what cost? The man's dangerous. He didn't hold back with Raymond."
        "B. How are you feeling?":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left2minus
            show maxime casual sad behind mscmc at right2minus
            "I glance at Maxime, trying to read his frown."
            show mscmc jacket_hairdown surprised
            mcmax "What are you thinking?"
            show maxime casual angry
            mx "I'm thinking I'd feel much better if you were as far away as possible from Wikus and his tournament."
            show mscmc jacket_hairdown surprised
            show maxime casual sad
            mx "I hate the idea of using you as bait, and I hate the thought of what Wikus might be planning even more."
        "C. Let's go over what we know.":
            $menuhideborder = False
            show mscmc jacket_hairdown sleep at left2minus
            show maxime casual sad behind mscmc at right2minus
            "I take a deep breath, sorting through the muddle of conflicting feelings in my head."
            show mscmc jacket_hairdown basic
            show maxime casual basic
            mcmax "Okay, I'm going to talk this out so I know where we stand. Wikus kidnapped Raymond, we know that for sure."
            mcmax "Camilla thinks Wikus is working for someone else, but we don't know that for sure."
            show maxime casual sad
            mcmax "We have enough evidence to haul Wikus in, but he could refuse to say who he's working for."
            show maxime casual angry
            "Maxime mutters darkly."
            mx "And Camilla wants to dangle you in front of him as bait."
            show mscmc jacket_hairdown surprised
            show maxime casual basic
            mcmax "Well, is ther anything that would put you more at ease as we go through with this?"
            show mscmc jacket_hairdown basic
            show maxime casual sad
            mx "Frankly, I'd feel better if there was an entire ocean between you and Wikus Sapor."

    show mscmc jacket_hairdown surprised at left2minus
    show maxime casual sad behind mscmc at right2minus
    mcmax "So you want me to drop out of the competition?"
    show mscmc jacket_hairdown basic
    show maxime casual basic
    "Maxime purses his lips grimly, which I take as a 'yes'."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(And yet, he's not fighting me about staying. Maybe this time I can reason with him.)"
    show mscmc jacket_hairdown surprised at left2minus
    show maxime casual sad behind mscmc at right2minus
    mcmax "I don't want to do that. I've still got my career to think about."
    show mscmc jacket_hairdown basic
    show maxime casual angry
    mcmax "Yes, Wikus is a freak, but I can't deny that this tournament has helped me."
    show maxime casual basic
    mcmax "I got a lot of networking done at the gala, and the tournament's a great showcase of what I can do."
    show mscmc jacket_hairdown angry
    show maxime casual sad
    mcmax "And I want to help you catch the bad guy! You know that."
    show mscmc jacket_hairdown basic
    show maxime casual angry
    "I pause, waiting for a protest, but Maxime only glares discontently out at the ocean."
    show maxime casual basic
    mcmax "...Does that stony silence mean you're not going to try and stop me?"
    show mscmc jacket_hairdown sad
    show maxime casual sad
    "Maxime hesitates, and when he turns back to me his eyes are clouded with worry."
    mx "I can't make that choice for you. If you decide to stay, it goes without saying that I'm not letting you out of my sight."
    show mscmc jacket_hairdown smile
    mcmax "Thanks, Maxime. I appreciate knowing that you've got my back."
    hide mscmc
    show maxime casual_cu sleep_cu at maxime_cu
    "I manage a small smile, but Maxime shakes his head, distracted."
    show maxime casual_cu sad_cu
    mx "[genericfn], if something happened to you, I'd..."
    "He hesitates, then adds softly."
    mx "I'd never be able to forgive myself."
    show mscmc jacket_hairdown grin at left2minus
    show maxime casual sad behind mscmc at right2minus
    mcmax "Hey, nothing's going to happen to me!"
    show mscmc jacket_hairdown grin:
        ease 0.4 xoffset 60
    "I grip his arm to try and ground him."
    show mscmc jacket_hairdown smile
    mcmax "You know I've got a good head on my shoulders, and I know I've got you looking after me."
    mcmax "And we both know I can win this tournament, which will get us closer to Wikus and wherever he's hiding Raymond."
    hide mscmc
    show maxime casual_cu basic_cu at maxime_cu
    "Maxime smiles ruefully, giving me a proud, appraising glance."
    show maxime casual_cu smile_cu
    mx "I do know you're a winner. That was never in doubt."
    mx "Listen, [genericfn], I wouldn't dream of forcing you out of the tournament because you deserve to be here."
    mx "You've got real talent, and you've worked so hard."
    mx "So, if I can help by keeping you close and monitoring Wikus, then that's what I'll do."
    show maxime casual_cu embarrassed_cu
    "It's a surprisingly long and impassioned speech coming from him, and he flushes as soon as he's done."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I just smile, watching him fondly as he stares out at the waves."
    mcmax "Thank you. That means the world to me."

    hide mscmc
    scene bg msc_maxime_studio_sunset at bg with clockwise_wipe
    play music mschappytimes
    "We return to the studio as the sun sets, with Maxime still deep in thought."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It's like he's still carrying a little grey thundercloud over his head.)"
    show mscmc jacket_hairdown surprised at left3
    show maxime casual basic at right4
    mcmax "Hey."
    show maxime casual sad
    show mscmc jacket_hairdown surprised:
        ease 0.7 xoffset 190
    pause 0.7
    "I tap his shoulder, to get his attention."
    show mscmc jacket_hairdown smile
    show maxime casual basic
    mx "What's up?"
    show mscmc jacket_hairdown surprised
    "He blinks, shaking his head, then chuckles at my puzzled look."
    show maxime casual smile
    mx "Had my head in the clouds for a moment."
    show mscmc jacket_hairdown surprised
    show maxime casual angry
    mx "I keep wondering if there's a solution I haven't seen yet, but I've run through everything again and again..."
    show mscmc jacket_hairdown smile
    show maxime casual smile
    mcmax "It sounds like you could actually use a break from work."
    show maxime casual sad
    "I glance around the studio, smiling as me eyes light on his easel."
    show mscmc jacket_hairdown grin
    show maxime casual basic
    mcmax "Why not do some painting or something? I know you haven't had much time to paint lately."
    show maxime casual surprised
    mcmax "I bet it would make you feel better."
    show maxime casual smile
    "Maxime looks surprised, then touched, breaking into a smile."
    mx "You're right."
    show maxime casual basic
    mx "Actually, yoiu're right about a lot of things—'unplugging' from work would probably be good for me."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "He suddenly lights up, catching my hand eagerly."
    show maxime casual_cu embarrassed_cu
    mx "Want to do it with me? You deserve a break too."
    mx "We could paint something together."
    "He gently takes my hand in his as he looks into my eyes, which evokes images in my mind of him guiding my hand in brush strokes."

    hide maxime
    $menuhideborder = True
    menu maximee08c3:
        "A. Paint with Maxime as the sun sets!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "I clap my hands together eagerly."
            mcmax "I would love to."
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime looks positively delighted, pulling his easel closer to the center of the floor."
            show maxime casual_cu smirk_cu
            mx "Great, you won't regret it!"
            show maxime casual_cu smile_cu
            mx "I've got some smocks and aprons on the coat rack, see if you can find one that fits."
            show mscmc jacket_hairdown smile at left2
            show maxime casual basic at right2
            "I go for an apron, since his shirts would probably dwarf me, and join him at the easel, where he's neatly laying out tubes of paint."
            hide maxime
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(The apron smells like him.)"
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmax "Fair warning, I know absolutely nothing about painting, or drawing."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "That's no problem. We'll do something abstract."
            "He nods towards his paintings, gentle swirling images that always make me think of the many faces of the sea."
            mx "My favorite thing about abstract is that you can start by just experimenting and there are no wrong answers."
            show mscmc jacket_hairdown embarrassed
            "I look around at his paintings on the walls, admiring the mixture of colors and textures."
            hide maxime
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(His art is so full of emotion.)"
            show mscmc jacket_hairdown surprised at left2
            show maxime casual smirk behind mscmc at right2:
                ease 0.4 xoffset -130
            pause 0.4
            mx "Hey."
            show mscmc jacket_hairdown embarrassed
            show maxime casual smile
            "Maxime lays his big, strong hands on my shoulders, smiling encouragingly."
            mx "We're doing this to relax and free our minds, there's no one I'd rather be here with."
            show maxime casual embarrassed
            mcmax "Me too."
            show maxime casual smile
            "Maxime chuckles, pointing me towards the table."
            show mscmc jacket_hairdown smile
            mx "Why don't you choose our colors?"
            show mscmc jacket_hairdown surprised
            "I peer thoughtfully at the tubes of paint, wracking my brain for inspiration."
            mcmax "Your abstract pieces are inspired by real things, right? Like the ocean."
            mx "They are. You can find a lot of inspiration in nature."
            show mscmc jacket_hairdown grin
            mcmax "I want to try that too. Remember that piece of red sea glass you gave me?"
            show maxime casual embarrassed
            "Maxime flushes a little at the mention of his gift, but prepares shades of orange, brown, and a deep red."
            hide maxime
            hide mscmc
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset -200
            show maxime casual_cu basic_cu behind mscmc at maxime_cu:
                xoffset 200
            "As we're mixing shades, he shows me how to hold the palette knife, and his fingers close gently over mine."
            show maxime casual_cu embarrassed_cu
            mx "Like that, spread them into each other...And if you want it a little lighter, we can add some white."
            show mscmc jacket_hairdown_cu basic_cu
            show maxime casual_cu smile_cu
            "He has to lean over me to see the palette, practically resting his chin on top of my head."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(I feel so safe with him all around me like this, I never want this to end.)"
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset -200
            show maxime casual_cu smile_cu behind mscmc at maxime_cu:
                xoffset 200
            mx "Hey, that's a nice coral! You've got a good eye for color."
            mcmax "Really?"
            show mscmc jacket_hairdown_cu smile_cu
            show maxime casual_cu smirk_cu
            mx "Really. Maybe you've got a hidden talent for painting that you never knew about."
            show maxime casual_cu embarrassed_cu
            mx "Now, grab a brush and just follow your heart."
            show mscmc jacket_hairdown_cu embarrassed_cu
            show maxime casual_cu smirk_cu
            "I hold my brush in one hand, staring at the empty canvas."
            show mscmc jacket_hairdown_cu surprised_cu
            show maxime casual_cu smile_cu
            mcmax "...I'm not sure where to start."
            mx "Here."
            show mscmc jacket_hairdown_cu grin_cu
            mcmax "Show me how it's done."
            show mscmc jacket_hairdown_cu embarrassed_cu
            show maxime casual_cu embarrassed_cu
            "Just as I'd hoped, Maxime presses closer to my back, reaching around and cupping my hand, guiding our first light strokes."
            show mscmc jacket_hairdown_cu grin_cu
            show maxime casual_cu smile_cu
            "(His movements are sure of themselves but also light in a way that makes it feel like he's letting the brush decides what to do.)"
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu:
                xoffset 0
            "Maxime leans down, to whisper in my ear."
            show maxime casual_cu embarrassed_cu
            mx "You're getting it."
            hide maxime
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            mcmax "Yeah, I think I am."
            show mscmc jacket_hairdown_cu embarrassed_cu
            "(The warmth from his body and his closeness makes me feel like I'm floating. Oh Maxime, I want all of you all the time.)"
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "I take the lead and guide his hand in mine now."
            show maxime casual_cu smile_cu
            mx "We could do a wash of light pink as a background. Want me to take care of that while you get the pattern down?"
            hide maxime
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmax "Sure!"
            show mscmc jacket_hairdown smile at left1
            show maxime casual smile behind mscmc at right1
            "Maxime starts to fill in the canvas with broad strokes of a watered-down pink."
            "I experiment with yellows, whites and oranges, adding depth to the shapes I've created. It feels exhilarating in a way."
            show mscmc jacket_hairdown surprised
            "Maxime reaches up, painting a streak along the top, and I feel something wet drip on to my arm."
            show mscmc jacket_hairdown grin
            mcmax "Hey, you got me!"
            show mscmc jacket_hairdown smile
            show maxime casual smirk
            "Even as he towers above me, I can sense his faint smirk."
            show maxime casual smile
            mx "Whoops. Hazard of the job, I guess."
            show mscmc jacket_hairdown grin
            show maxime casual smirk
            mcmax "Yes, very hazardous."
            show maxime casual surprised
            show mscmc jacket_hairdown grin:
                ease 0.7 xoffset 40
            pause 0.7
            "I dap my finger in yellow, then turn towards him and hop up to briefly poke his cheek and leave a spot of paint."
            show maxime casual embarrassed
            mx "Hey now!"
            show maxime casual surprised
            mcmax "Don't rub it off, you look cute."
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "He flushes under my dab of paint and mutters, suddenly seeming very interested in coating the edges of the canvas."
            mx "I'll take your word for it—you've got a good eye, after all."
            hide maxime
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "I beam, holding my brush aloft."
            mcmax "Thank you. And, I've got a good teacher."
            show mscmc jacket_hairdown smile at left1:
                xoffset 40
            show maxime casual embarrassed behind mscmc at right1
            "We finally step back from the canvas, wiping our hands and admiring the swirl of colors."
            show mscmc jacket_hairdown grin
            show maxime casual smile
            mcmax "That was way more cathartic than I thought it would be! Maybe I {i}should{/i} take up painting."
            hide maxime
            hide mscmc
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Especially if I get to spend more time like this with Maxime.)"
            show mscmc jacket_hairdown grin at left1:
                xoffset 40
            show maxime casual smile behind mscmc at right1
            mx "You know, I got into painting fairly late in life. I was already an adult, a young adult, but still."
            show mscmc jacket_hairdown surprised
            mcmax "Wait, really? How long did it take you to learn?"
            "Maxime laughs."
            show maxime casual smirk
            mx "Honestly, it feels like I'm still learning. That's part of what I love about it."
            show maxime casual smile
            mx "I've found it actually helps my surfing too."
            show mscmc jacket_hairdown surprised:
                ease 0.7 xoffset 0
            pause 0.7
            "I lean back against his paint-stained table, fascinated."
            show mscmc jacket_hairdown smile
            mcmax "Really? How so?"
            show maxime casual basic
            mx "It's a little hard to put into words, but it taught me to get out of my head."
            mx "Art's not a sport—you're only competiung against yourself, and there are no wrong moves. It's a good headspace to be in."
            "As we leave the studio, I mull his words over."
            hide maxime
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Maxime's always saying to 'get out of my head' and 'let it flow' when surfing. Is that all it is? Calming my mind down? Not fearing failure?)"
            hide mscmc
        "B. Get shy.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            mcmax "I am shy."
            hide mscmc

    scene bg msc_boardwalk_night_lights_people at bg with wiperightdissolve
    play music mscdanger
    show mscmc jacket_hairdown surprised at left1
    show maxime casual basic behind mscmc at right1
    "As Maxime locks the door to his beach cottage, we hear a shout from across the boardwalk."
    hide mscmc
    hide maxime
    show trina casual sad at centre
    so "[genericfn]? [genericfn]!"
    show trina casual sad:
        parallel:
            ease 0.8 zoom 1.1 xoffset -20
        parallel:
            linear 0.3
            linear 0.4 yoffset 30
    "Trina runs towards us, her sneakers pounding the wooden planks."
    hide trina
    show mscmc jacket_hairdown surprised at left3
    show trina casual sad at right3
    mcmax "Trina, what's wrong? Are you ok?"
    so "Thank god, you're here!"
    show mscmc jacket_hairdown surprised:
        ease 0.4 xpos stagepos[1]-80
    show trina casual sad behind mscmc:
        ease 0.4 xpos stagepos[1]+80
    "Trina grabs me in a tight hug, leaving me confused and a little squished."
    hide mscmc
    hide trina
    show maxime casual_cu surprised_cu at maxime_cu
    "I exchange a perplexed look with Maxime as I pat her shoulder, trying to console her."
    hide maxime
    show mscmc jacket_hairdown surprised at left1:
        xoffset 20
    show trina casual sad behind mscmc at right1:
        xoffset -20
    mcmax "What are you talking about? Why wouldn't I be?"
    hide trina
    hide mscmc
    show trina casual_cu angry_cu at trina_cu:
        xoffset 60
    "Trina pulls back, gripping my shoulders."
    show trina casual_cu sad_cu
    so "Didn't you hear? THe tournament people made an announcement—another surfer's gone missing!"

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    hide trina
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
