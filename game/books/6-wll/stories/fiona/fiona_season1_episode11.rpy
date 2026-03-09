label fiona_season1_episode11:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_mc_room_lights_on at bg
    play music wllromancelight2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Fiona's lips are on mine the moment I say yes, and it feels like a dam breaking, a torrent of desire washing me away."
    "But at last Fiona breaks the kiss long enough to whisper in my ear."
    show fiona cloak_cu basic_cu at fiona_cu
    mb "You know, before my family got involved with the occult, we had another occupation."
    "My hands stop trying to work their way under her shirt long enough for me to give her a look."
    hide fiona
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(This feels like a set up.)"
    show wllmc skirt_cu basic_cu
    mcfiona "Oh yeah? What was that?"
    hide wllmc
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "We were pearl divers."
    hide fiona
    show wllmc skirt_cu embarrassed_cu at wllmc_cu
    "My entire face flushes as the double entendre hits me."
    show wllmc skirt_cu smirk_cu
    mcfiona "Fiona Eichen, how long have you been planning that?"
    hide wllmc
    show fiona cloak_cu grin_cu at fiona_cu
    "She giggles and presses her hands to my shoulders, beaming at me."
    mb "Since I first came up with the nickname. Holding it in has been absolute torture."
    show fiona cloak_cu smirk_cu
    mb "But it's worth it now that I get to see you turn such a wonderful color."
    show fiona cloak_cu grin_cu
    mb "Pink pearls are worth even more, you know."
    hide fiona
    show wllmc skirt_cu grin_cu at wllmc_cu
    mcfiona "You're outrageous. I don't know what I'm going to do with you."
    hide wllmc
    "I kiss her neck, slow and teasing, and she almost purrs with satisfaction."
    show fiona cloak_cu smile_cu at fiona_cu
    mb "Will you let me dive for you? I want to show you what a spectacular treasure you really are."
    "My mouth goes a little dry."
    hide fiona
    show wllmc skirt_cu embarrassed_cu at wllmc_cu
    "(Just like before, there's only one thing I can say to her.)"
    show wllmc skirt_cu smallsmile_cu
    mcfiona "Yes."
    hide wllmc
    "Fiona strips me reverently, a reenactment of the ritual in the hot springs, kissing my body as she bares it."
    show wllmc under_cu embarrassed_cu at wllmc_cu
    "(I'm used to thinking of my body as a functional tool, but the way Fiona touches it makes it feel like a work of art.)"
    hide wllmc
    "She murmurs to herself as she moves over me, finding every tender spot, from the curve of my ear to the back of my knees."
    show fiona cloak_cu smile_cu at fiona_cu
    mb "Oh my pearl, my treasure, oh you beauty."
    hide fiona
    "Her sweet lips brush my skin again and again, leaving me heated and aching and desperate for movement of her long dexterous fingers."
    show wllmc under_cu embarrassed_cu at wllmc_cu
    mcfiona "Fiona, please, I need you."
    "(What am I even saying? But I can't remember ever feeling this good before.)"
    hide wllmc
    show wllmc under embarrassed at left2
    show fiona cloak smile at right2
    "My entire body shakes with rapture, and when I come back to myself Fiona is at my side, still fully clothed, watching me with soft eyes."
    mb "That was just as good as I imagined it would be."
    show fiona cloak smirk
    mb "No, what am I saying? It was even better."
    hide wllmc
    hide fiona
    "I pull her down against me, pressing myself to her as my hands work their way through layers of cloth."
    show wllmc under_cu smirk_cu at wllmc_cu
    mcfiona "Do you think we're done? You've been leading this dance. Now I want a turn."
    mcfiona "I want to give you so much pleasure that every muscle in your body groans my name tomorrow."
    "Fiona shivers, a delicious full-body ripple that makes me feel like a maestro violinist playing a Stradivarius."
    hide wllmc
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "Well in that case, you can have me however you like."
    hide fiona
    "She sinks back against me, soft and boneless, and I take her."
    "I take her and take her, strip her down and bend her over the bed so I can plunder every inch of her."
    show wllmc under_cu smirk_cu at wllmc_cu
    mcfiona "Make noise for me, Fiona. Let yourself go for me."
    hide wllmc
    "The mewl that comes from the back of her throat as I finally push her over the edge is the most satisfying sound I've ever heard."
    "I lie down on the bed beside her as she relaxes."
    show wllmc under smile at left2
    show fiona under smile at right1plus
    mcfiona "How are you?"
    show fiona under grin
    mb "Just wonderful. I feel thoroughly ravished."
    show fiona behind wllmc:
        easein 0.5 centre
    "She leans in and kisses me."
    show fiona under smirk
    mb "It turns out that this is another way you're unique."
    show wllmc under smirk
    mcfiona "What, uniquely good at bedding women?"
    show fiona under pout
    mb "You must be! I've never..."
    "She doesn't finish her sentence, but I don't think much of it, still half-dazed from bliss myself."
    show fiona under sleep:
        easein 0.3 xoffset 40
    "Then Fiona sits up and stretches."
    hide fiona
    hide wllmc
    show wllmc under_cu smirk_cu at wllmc_cu
    "(That stretch does the most marvelous things to her body.)"
    hide wllmc
    show fiona under surprised at centre:
        xoffset 40
    show wllmc under smallsmile at left2
    mb "Oh, I should get back to work. Lots to do if we're going to be ready for this ghost."
    show fiona:
        easein 0.4 right2 xoffset 0
    show wllmc under sad:
        pause 0.2
        easein 0.4 left1
    "She swings her legs off the bed and stands up, but I reach out and wrap my hand around her wrist."
    mcfiona "Wait."
    "Fiona looks down at me."
    hide fiona
    hide wllmc
    show wllmc under_cu sad_cu at wllmc_cu
    "(I'm not ready for her to go yet. But how do I ask her to stay?)"
    hide wllmc
    show fiona under basic at right2
    show wllmc under sad at left1
    "Something in my chest is strangely tight."
    mcfiona "Stay."
    show fiona under smirk
    "Fiona's eyes gleam, and her mouth pulls up into a smirk."
    show wllmc under surprised
    mb "What, ready for round two already?"
    show wllmc under embarrassed
    "A dull flush creeps over my cheeks."
    mcfiona "Actually, I just wanted to, I dunno, talk, or something."
    "I feel stupid as soon as I say it, but it's true."
    hide fiona
    hide wllmc
    show wllmc under_cu smile_cu at wllmc_cu
    "(I want a bit more time with her before it all becomes work again.)"
    hide wllmc
    show fiona under sad at right2
    show wllmc under embarrassed at left1
    mb "I don't know... There's a lot to do."
    hide fiona
    hide wllmc
    show wllmc under_cu grin_cu at wllmc_cu
    "(I can tell she wants to, though. One more push, and she'll say yes.)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e11c1:
        '"Stay with me. Just for a while."' (paidchoice = "paidchoice"):
            $menuhideborder = False
            show fiona under sad at right2
            show wllmc under sad at left1
            mcfiona "Stay with me. Just for a while."
            show fiona under smile
            "Fiona's eyes soften."
            mb "How can I say no when you look so adorable?"
            hide wllmc
            hide fiona
            "She lies down beside me and rests her head on the curve of her arm."
            show fiona under_cu smile_cu at fiona_cu
            "The moonlight falling through the window turns the gold in her eyes to steel."
            mb "Did you want to talk about anything in particular?"
            hide fiona
            show fiona under smile at right1
            show wllmc under sad at left1
            mcfiona "Not really. Tell me, oh, I don't know. Anything. Something I don't know."
            show fiona under smirk
            mb "Hmmm... The worst thing about living in Wisp Willow is that the food isn't spicy enough."
            show wllmc under surprised
            mcfiona "Really? I think Ada's chili is pretty good."
            show fiona under smile
            "Fiona snorts."
            mb "Barely a spark to it. I miss my mother's jjamppong so much."
            show wllmc under smirk
            mcfiona "Have you ever had Triple Alliance food? Their tlahcos are ferocious."
            show fiona under grin
            mb "Oh, I love tlahcos! I used to get them from this incredible food stall when I lived out west."
            show wllmc under surprised
            mcfiona "You lived out west? Where?"
            hide fiona
            hide wllmc
            show wllmc under_cu surprised_cu at wllmc_cu
            "(Strange to think she's been to the place I was going, before all this started.)"
            hide wllmc
            show fiona under smile at right1
            show wllmc under surprised at left1
            mb "Cuyaca. I spent a couple of years there learning from a card sharp I'd seen in my visions."
            show wllmc under basic
            "Her eyes soften as she talks, and I feel a sudden surge of jealousy."
            hide fiona
            hide wllmc
            show wllmc under_cu sad_cu at wllmc_cu
            "(We're about the same age, but it feels like she's done so much more with her life than me.)"
            hide wllmc
            show fiona under smile at right1
            show wllmc under smile at left1
            mcfiona "I'd like to see Cuyaca. Maybe I'll go there, when the job is done."
            show fiona under surprised
            mb "I thought you were going to Serpent River territory."
            show wllmc under smirk
            mcfiona "Really, I was going anywhere. The important thing is that I was leaving."
            show fiona under pout
            mb "You never told me what you were running from. And I can't read it in you."
            "She reaches out with one finger and traces the lines of my palm."
            show fiona under sad
            show wllmc under surprised
            mb "I only see a shadow."
            show wllmc under sad
            "I close my hand around hers, holding her close."
            mcfiona "It wasn't any one thing. My luck just ran dry."
            mcfiona "Too many people knew my face, the jobs I was taking got riskier and riskier, and my magic kept acting up..."
            show wllmc under basic
            mcfiona "I wanted a clean start."
            show fiona under surprised
            mb "And you had nothing to stay for? No one to stay for?"
            show fiona under smirk
            "She arches one eyebrow salaciously."
            show wllmc under surprised
            mcfiona "No. Not like that. I've always been alone."
            show wllmc under sad
            "I bite my lip."
            show fiona under basic
            mcfiona "I don't normally talk about this kind of stuff."
            hide fiona
            hide wllmc
            show wllmc under_cu sad_cu at wllmc_cu
            "(Never get too deep, that's the rule.)"
            hide wllmc
            show fiona under sad at right1
            show wllmc under sad at left1
            mb "I know what you mean."
            mb "This is strange for me, too. I never really stick around, you know?"
            mcfiona "Yeah. Too dangerous."
            hide fiona
            hide wllmc
            show wllmc under_cu angry_cu at wllmc_cu
            "(The last thing I need is a weakness.)"
            hide wllmc
            show fiona under pout at right1
            show wllmc under sad at left1
            mb "Too complicated."
            mb "Even if I couldn't see the end of the relationship right from the start, my powers make it hard to stay."
            show wllmc under smirk
            mcfiona "Right. I guess it would be kind of awkward if your patron visited at the wrong moment."
            show fiona under angry
            show wllmc under grin
            "I grin, imagining how that might look, and Fiona rolls her eyes."
            mb "I'm usually pretty good at covering up for myself. It's the lying that makes things hard."
            show fiona under sad
            mb "No wonder all my relationships are bound to end."
            show wllmc under smallsmile
            mcfiona "I understand."
            mcfiona "Even though I didn't know what my power was, it was always there in the background, ready to emerge at the worst possible time."
            show fiona under smile
            mb "So this is something new for both of us."
            "Her words seem strangely loud in my ears, though her voice is barely more than a whisper."
            show wllmc under smile
            mcfiona "Yeah. Something special."
            show wllmc under surprised
            "As soon as the words leave my mouth, I know they're a step too far."
            hide fiona
            hide wllmc
            show wllmc under_cu smallsmile_cu at wllmc_cu
            "(Like the drawing on the card Fiona showed me when we met, the young woman about to walk off the cliff.)"
            hide wllmc
            show fiona under smile at right1
            show wllmc under smirk at left1
            "I twist my mouth into a smirk and stretch my arms."
            mcfiona "Goddess, I say the stupidest things after midnight."
            show fiona under smirk
            mb "Don't we all?"
            hide wllmc
            hide fiona
            show fiona under_cu sleep_cu at fiona_cu
            "She leans forward and gives me a quick kiss."
            show fiona under_cu smile_cu
            mb "Go to sleep, my pearl. When you wake up in the morning, all nonsense will be forgotten. I promise."
            hide fiona
            "Feeling like my mouth has got me in enough trouble for one night, I take her advice."
        "Let her get back to work.":
            $menuhideborder = False
            show wllmc under_cu angry_cu at wllmc_cu
            "(I can't. It's too much. I shouldn't want this.)"
            hide wllmc
            show fiona under sad at right2
            show wllmc under sad at left1:
                pause 0.1
                easein 0.4 left1plus
            "I let my hand fall away."
            show fiona under surprised
            mcfiona "It's nothing."
            show fiona under basic
            "Fiona's eyes search mine for a moment, and then she nods."
            mb "Okay then."
            show fiona:
                easein 0.4 right3
            "She settles herself at the desk and begins reading, and I watch her until my eyes close."

    scene black at bg
    scene bg_wll_mc_room_day at bg with eye_open
    stop music fadeout 1.0
    play music wlleverydaycalm1 fadein 1.0
    "I wake up with the strange sense that something is missing."
    show wllmc under_cu sad_cu at wllmc_cu
    "(Fiona.)"
    hide wllmc
    "The other side of the bed is smooth and unruffled, and my room is empty."
    show wllmc under_cu sad_cu at wllmc_cu
    "(So she left.)"

    scene bg_wll_common_room_day at bg with wiperightdissolve
    "I ignore the bitter taste that leaves in my mouth and head downstairs, but as I get close to the common room, I hear two familiar voices."
    show fiona cloak basic at left3
    show donna casual basic at right3
    bo "So that's your excuse for being here so bright and early?"
    show fiona cloak angry
    mb "And isn't it a good one!"
    show donna casual smile
    bo "Some day that silver tongue of yours is gonna get you in trouble, Ms. Eichen."
    hide fiona
    show wllmc coat smile at left3
    mcfiona "Good morning Donna. Good morning Fiona."
    hide donna
    show fiona cloak surprised at right3
    "Fiona's eyes widen slightly when she sees me, and at her side, her hand half-curls unconsciously."
    hide fiona
    hide wllmc
    show wllmc coat_cu basic_cu at wllmc_cu
    "(That's a tell, one of the only ones I've ever seen from her. But of what, I don't know.)"
    hide wllmc
    show wllmc coat basic at left3
    show fiona cloak surprised at right3
    mb "Good morning, [genericfn]! Donna and I were just talking about romance novels. Would you like some coffee?"
    "Her words tumble out of her, all in one long rush of breath."
    show wllmc coat surprised
    mcfiona "Coffee sounds good."
    "I can feel myself clamming up around her, not sure where precisely the new boundaries between us lie."
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(Last night doesn't mean anything. It never did. But in my imagination, I always skipped town the next day.)"
    hide wllmc
    show fiona cloak surprised at right3:
        pause 0.3
        easein 0.4 right1
        pause 0.3
        easeout 0.4 right3
    show wllmc coat surprised at left3
    "Fiona hands me a mug, but as I take it, our hands brush, and she jerks her fingers back fast enough to slop coffee on the boards."
    show fiona cloak sad
    mb "Oh damn, I'm sorry Donna. I'll clean that up now."
    hide wllmc
    hide fiona
    show donna casual angry at centre
    bo "See that you do."
    "She tosses Fiona a rag and leaves the room, muttering something dark under her breath."
    hide donna
    show fiona cloak sad at right3
    show wllmc coat sad at left3
    mcfiona "She wasn't cursing us or anything, was she?"
    show fiona cloak smile
    mb "No. Thankfully for the world, Donna has no gift for magic."
    show wllmc coat smile
    "I laugh at her joke, and for a moment, everything feels easy. But as Fiona's gaze lingers on me, it gets awkward again."
    show wllmc coat sad
    mcfiona "Look, do we need to talk? I know last night wasn't what we planned..."
    show fiona cloak surprised
    mb "No, it's fine. I mean, last night was good! Right?"
    show wllmc coat smallsmile
    mcfiona "It was good."
    hide fiona
    hide wllmc
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(It was too good. All I want to do is drag Fiona back upstairs for round two.)"
    hide wllmc
    show fiona cloak surprised at right3:
        pause 0.1
        easein 0.5 right1
    show wllmc coat surprised at left3
    "Fiona reaches out and takes my hand, and in one swift movement, sucks a scrap of butter from my thumb."
    mb "You were about to get it on the tablecloth."
    show wllmc coat smile
    mcfiona "You say that, but I see the butter melting in your mouth."
    show wllmc coat surprised
    "We both open our mouths to say something, stop, and hesitate."
    show wllmc coat smallsmile
    mcfiona "You first."
    show fiona cloak smile
    mb "You know, last night doesn't have to be one and done. We did promise ourselves a reward when the job is done."
    show wllmc coat grin
    "I hate how my heart leaps at those words."
    hide fiona
    hide wllmc
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(It was just good, and I've been having a bit of a dry spell. That's all.)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e11c2:
        "Why not? We can make it special.":
            $menuhideborder = False
            show fiona cloak smile at right1
            show wllmc coat grin at left3
            mcfiona "Why not? Once this job is done, we can take our time with it. Hole up for a week with enough food to last us."
            show fiona cloak grin
            mb "Oh, I like the sound of that."
        "You just can't get enough of me.":
            $menuhideborder = False
            show fiona cloak smile at right1
            show wllmc coat smirk at left3
            mcfiona "You just can't get enough of me, can you?"
            show fiona grin
            mb "Let's say that I don't think I've quite reached the last page of this story yet."
        "It'll be a good way to say goodbye.":
            $menuhideborder = False
            show fiona cloak smile at right1
            show wllmc coat smirk at left3
            mcfiona "It'll be a good way to say goodbye. We can go out with a bang."
            show fiona cloak smirk
            mb "Make another joke as bad as that, and I might just have to tear your clothes off right here and now."

    show wllmc coat surprised
    show fiona cloak surprised
    show enzo familiar basic at right5:
        xoffset 300
        easein 0.5 xoffset 0
    "She leans towards me, fingers curled on the inside of my wrist... and Enzo zooms through the window."
    show enzo familiar smile
    enz "Good morning Mistress! You're in a good mood today, I can tell. I don't think I've ever felt you this happy."
    show wllmc coat angry
    show fiona cloak smile
    mcfiona "Enzo, don't look at my feelings!"
    enz "I can't exactly help it. Empathic bond and all that. Anyway, there's a letter for you."
    show wllmc coat surprised
    show fiona cloak surprised
    "He tosses it on the table, addressed to me and Fiona."
    mcfiona "It's from Diana."
    "Fiona is already ripping it open."
    show fiona cloak grin
    mb "Hah, I was right!"
    show wllmc coat basic
    "She tosses me the letter, and I read it."
    hide enzo
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(She's going to give us her wedding ring if we help out with the festival.)"
    hide wllmc
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "Well, now it's definitely time to get this show on the road."

    scene bg_wll_ward_hq_lights_off at bg with fade
    stop music fadeout 1.0
    play music wlleverydayupbeat2 fadein 1.0
    "We give the Ward another demonstration of our improved performance."
    show wllmc coat_hat_cu smile_cu at wllmc_cu
    "(Now that my magic isn't going haywire every time Fiona touches me, it's a lot easier.)"
    hide wllmc
    show sascha vest smile at left3
    show cecelia dunevest smile at right3
    "Cecelia and Sascha certainly look happier."
    sasch "I mean, I'm not telling you two to head back east and try and get a spot on Broadway..."
    vr "But for our purposes, it will more than suffice."
    hide sascha
    hide cecelia
    show fiona cloak grin at right2
    show wllmc coat grin at left3
    "Fiona laughs, and holds up her hands for a high five."
    mb "I think this calls for a celebration."
    mcfiona "You think everything calls for a celebration."
    show fiona cloak smirk
    mb "That's one of my many wonderful characteristics, yes."
    hide fiona
    hide wllmc
    show cecelia dunevest basic at centre
    "Cecelia digs out a bottle of wine, turning it around to look at the yellowing label."
    show cecelia dunevest smile
    vr "This was given to me a long time ago. A very rare vintage. I never found a use for it."
    show wllmc coat surprised at left3
    show cecelia dunevest smile at right3
    mcfiona "It doesn't have magical powers or anything, does it?"
    show cecelia dunevest smirk
    vr "Not that I know of."
    show wllmc coat smile
    mcfiona "Then it's just plonk."
    "I take it and pour out glasses for everyone who wants them."
    hide cecelia
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Cecelia herself only drinks from that silver flask, as usual.)"
    hide wllmc
    show nathan redcasual_bandana smile at centre
    wc "Well, here's a toast to Fiona and [genericfn]! For getting over their problems and putting on a show."
    show sascha vest smirk at left3
    show nathan at right3
    sasch "I think you mean getting into their problems."
    hide nathan
    show sascha at centre
    "He gives us a look, and Fiona rolls her eyes at him."
    hide sascha
    show fiona cloak grin at centre
    mb "I want to propose a toast too."
    mb "Here's to [genericfn], who came into a difficult job and has been nothing but helpful and resilient."
    mb "I'm grateful that I got to meet the first witch in a century..."
    mb "And see all the wonderful magic she can do, but I'm even more grateful I got to meet you."
    hide fiona
    show wllmc coat_cu grin_cu at wllmc_cu
    "(She really means that.)"
    hide wllmc
    show wllmc coat grin at centre
    mcfiona "Well then I also have a toast."
    show wllmc coat smile at left3
    show fiona cloak smile at right2
    "I stand up beside Fiona and look at her."
    mcfiona "Fiona, I've learned a lot about myself from you. You've shown me again and again that I can trust you."
    show wllmc coat grin
    mcfiona "I couldn't have asked for a better teacher, or a better friend."
    hide wllmc
    hide fiona
    show fiona cloak_cu surprised_cu at fiona_cu
    "Fiona stares at me for a moment, wide-eyed."
    hide fiona
    show wllmc coat grin at left3
    show fiona cloak smirk at right2
    mb "There you go again, surprising me. You're still the most unexpected person I've ever met."
    hide wllmc
    hide fiona
    show sascha vest smirk at centre
    sasch "Okay, let's drink before this gets sappier than the penny dreadful."
    hide sascha
    show wllmc coat grin at centre
    mcfiona "Hear hear. Bottoms up."
    "The wine hits my tongue, powerful and delicious, and I join Fiona in defending the book we're performing."
    hide wllmc
    show fiona cloak basic at centre
    "When the party ends, hours later, I stay behind to clean up. As I return from putting the glasses back in their cabinet I spot Fiona."
    show wllmc coat smile at left3
    show fiona at right2
    mcfiona "What are you doing, all hunched over the table?"
    mb "Just looking at my cards."
    hide fiona
    hide wllmc
    show wllmc coat_cu smile_cu at wllmc_cu
    "(I like how she studies them so intently. She really is pretty cool when she's working.)"
    hide wllmc
    show wllmc coat smile at left1
    show fiona cloak sleep at right1
    "I give her shoulders a rub, easing the tension out of them, and look at what she's drawn."
    mcfiona "The Empress, the Queen of Wands, the two of cups - oh hey, that's the one from the play, right?"
    show fiona cloak smile
    mb "Very good, my pearl."
    show wllmc coat smallsmile
    mb "I think the Empress is Diana. The Queen of Wands might be you, although it's a little early for that."
    mb "The nine of wands is promising though. It seems like things will work out."
    show wllmc coat smirk
    mcfiona "If I don't mess them up."
    show fiona cloak angry
    "I mean it as a joke, but Fiona frowns."
    show wllmc coat surprised
    mb "I won't let that happen. No matter what."
    show fiona cloak sad
    "She sighs, and rubs her temples."
    mcfiona "Are you sure everything is okay?"
    hide wllmc
    hide fiona
    show fiona cloak_cu sad_cu at fiona_cu
    "She looks up at me, and there's an edge of vulnerability in her eyes that I've never seen before."
    mb "I really want to ask you something stupid, but I'm afraid."
    hide fiona

    $menuhideborder = True
    menu fionas1e11c3:
        "I won't laugh at you.":
            $menuhideborder = False
            show wllmc coat smallsmile at left1
            show fiona cloak sad at right1
            mcfiona "It's okay. I won't laugh at you, I promise."
        "Now I have to know.":
            $menuhideborder = False
            show wllmc coat smile at left1
            show fiona cloak sad at right1
            mcfiona "Oh come on, you can't tease me like that. Now I have to know!"
        "How is that different from normal?":
            $menuhideborder = False
            show wllmc coat smirk at left1
            show fiona cloak sad at right1
            mcfiona "Something stupid, huh? And how is that different from normal?"
            show fiona cloak surprised
            "Fiona pretends to be shocked, but I see her smile."

    show wllmc coat surprised
    show fiona cloak smile
    mb "Will you do something for me?"
    "She takes my hands in hers."
    hide wllmc
    hide fiona
    show fiona cloak_cu sad_cu at fiona_cu
    mb "Will you hold me, and tell me everything's going to be alright?"
    hide fiona

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
