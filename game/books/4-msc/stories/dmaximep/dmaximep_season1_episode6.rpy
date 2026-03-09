label dmaximep_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_ocean_wide_day at bg
    play music mscsurfcompetition

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "The competition falls on a particularly warm morning, the sea dotted with colorful surfboards."
    "I'm in the thick of it, floating against my board among the swirl of foam and shouting competitiors."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Damn, I should have taken that wave!)"

    hide mscmc
    "I let the break of the wave lift me up and down, watching the surfer who just claimed it ride until they wipe out."
    "I glance back at the beach, where the judges are lined up at a table and watching us through binoculars."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(I made it to the final six—no way am I going to flop out because I can't find a good wave!)"

    hide mscmc
    "It's difficult to both notice the good waves and know when to bow out and let another surfer take them."

    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(And it's hard to 'breathe with the ocean' when you're trying to avoid getting clipped by someone else's board.)"

    show mscmc surfer_hairup_cu basic_cu
    "(Technically it doesn't matter who rides in first, since it's our tricks the judges are looking for.)"

    show mscmc surfer_hairup_cu sad_cu
    "(But waiting makes me antsy.)"

    hide mscmc
    "I look back nervously at the judges' table and hear a familiar shout."

    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Wait, that sounded like...?)"
    "(Maxime!!)"

    hide mscmc
    scene bg msc_labeach_day at bg with dissolve
    show maxime casual smile at centre
    "His tall figure stands out among the crowd as he cups his hands around his mouth, shouting my name."

    hide maxime
    show trina casual smile at left2
    show dawn jacket smile at right2
    "Beside him, Dawn and Trina are holding a glitter-caked sign with 'GO [genericfn]' scrawled across it, both of them whooping and hollering."

    hide dawn
    hide trina
    show maxime casual smile at centre
    "I stare at Maxime in astonishment, wondering if my eyes are deceiving me."

    hide maxime
    scene bg msc_ocean_wide_day at bg with dissolve
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(But...he said he didn't want to come! He said he hates competitions!)"
    show mscmc surfer_hairup_cu embarrassed_cu
    "(Did he really come just for me?)"

    hide mscmc
    "My heart swells just as the sea starts to rise beneath my board, and a sense of calm settles over me."
    "I remember how at-peace I felt last night, as if Maxime and I had joined the ocean as one, and the way my mind seemed to join with the waves."

    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(I can do this.)"

    hide mscmc
    $menuhideborder = True
    menu maximee6c1:
        "A: Reach out to the ocean.":
            $menuhideborder = False
            "I breathe deep and shut my eyes, remembering how it felt to form a connection with the ocean."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(Hello, Ocean. I know I'm not as good at this as Maxime, but I'm listening, if you want to talk to me.)"
            "(Or we can just Be. That's okay too.)"
            hide mscmc
        "B: Think of last night.":
            $menuhideborder = False
            "I press my eyes shut and block out the shouts of the crowd and my fellow surfers, transporting myself back to the previous night and our secret cove."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(It was just me, Maxime, and the ocean.)"
            "The peaceful memory soothes me, and soon my heart is beating in time with the lap of the waves."
            hide mscmc
        "C: Think of Maxime.":
            $menuhideborder = False
            "I couldn't feel the ocean breathe until Maxime opened up his work for me, so it's his face I picture in my mind."
            show maxime mermaid_cu basic_cu at maxime_cu:
                alpha .9
            "I remember the feeling of his heartbeat under the palm of my hand, and how perfectly in tune he was with the waves."
            hide maxime
            "I breathe deep, matching my own breathing to the lull of the water."


    "Deep in the calm waters of my mind, a voice, more like a sense, whispers {i}NOW{/i}."
    "I open my eyes, everything crystal clear as I see the beginnings of a wave forming."
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(Here we go!)"
    hide mscmc
    "I start to paddle away from it, my breathing steady and timed with the breath of the ocean."
    play sound splash02
    "The huge wave lifts my board, and I leap up in one fluid motion, as aware of the water beneath me as if it were a part of my own body."
    stop sound
    "I hear the crowd roaring as I ride the wave, but all I can see is the horizon ahead of me, and the vast stretch of blue that feels like home."
    "The wave begins to close, but I'm completely in control, fully anticipating it and shifting into a power turn."
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(And that's one for my 'best of' reel!)"
    hide mscmc
    play sound splash03 loop
    "When I dive off into the water, it muffles the roar of the crowd, though I know I've done well—I can sense it."

    stop sound
    scene bg msc_labeach_day at bg with dissolve
    "I finally paddle back to shore and start scaling the sand, drenched and tugging my board behind me."
    "Trina and Dawn rush me in excitement, enveloping me in a sandwich hug."

    show trina casual_cu smile_cu at trina_cu2
    so "You were so good! They're just announcing the results now."
    hide trina
    "We look at the judges table, waiting breathlessly as the judges call the third place winner."
    show trina casual_cu smile_cu at trina_cu2
    "Trina squeezes my hand tight."
    hide trina
    $sidecharone = "Judge"
    sid1 "And in second place, [genericfn] [genericln]!"
    show trina casual smile at left2
    show dawn jacket grin at right2
    so "[genericfn]! [genericfn], you got second! You're a champ!"

    hide trina
    hide dawn
    show maxime casual smile at centre
    "I join them in delighted squealing, all of us bouncing up and down, until I look up and see Maxime standing before me, beaming from ear to ear."

    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    mcmaxime "Maxime, you came!"

    hide mscmc
    show maxime casual smile at centre
    mx "Hey, [genericfn]. I knew you were something special. How could I miss it?"

    hide maxime
    show trina casual smile at left2
    show dawn jacket smile at right2
    "Trina claps her hands, looking around at us."
    so "C'mon everyone, this calls for a celebration back at the shop!"
    show dawn jacket grin
    dw "Ooh, I'm into that."
    hide dawn
    show maxime casual basic at right2
    so "Maxime, you're coming too!"

    hide trina
    hide maxime
    "Dawn grabs Maxime's arm, tugging him along in our excited party."
    show maxime casual_cu smile_cu at maxime_cu
    "I catch his eye and wink, and he grins back."

    scene bg msc_surf_shop_sunset at bg with wiperightdissolve
    play music mscsurfshop
    "Once we're inside the surf shop, Trina dives behind the counter and produces a bottle of pink chanpagne and a stack of party poppers."
    show trina casual smile at left2
    show dawn jacket smile at right2
    so "Surprise! I got us some bubbly."
    show dawn jacket grin
    dw "Woah, we're getting fancy."

    hide trina
    hide dawn
    show mscmc casual_hairdown grin at centre
    mcmaxime "Aw Trina! You didn't even know if I'd place."
    hide mscmc
    show trina casual smile at right1
    so "Oh, I knew you'd win. That's why I bought 'em."

    show mscmc casual_hairdown grin behind trina with dissolve:
        xpos stagepos[1]-180
        ease 0.35 xpos stagepos[1]-50
        ease 0.35 xpos stagepos[1]-65
    "She smirks, pleased with herself, and I run over to grab her in a hug."

    hide trina
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcmaxime "Thanks, bestie."

    hide mscmc
    show trina casual_cu smile_cu at trina_cu2
    so "You're welcome, bestie."

    hide trina
    show maxime casual basic at left2
    show dawn jacket grin at right2
    dw "I'm going to pop this cork unless anyone wants to stop me."

    show maxime casual smirk
    "Maxime folds his arms, watching Dawn with amusement."
    mx "Go on, do your worst."

    hide dawn
    hide maxime
    "Trina and I instinctively duck as the pop of the champagne rings out, but the cork merely hits the ceiling."

    show maxime casual basic at left2
    show dawn jacket surprised at right2
    dw "Aaand it's bubbling over."

    show maxime casual smile
    show dawn jacket smile
    mx "Don't worry, I've got it."

    show dawn jacket grin
    "Maxime darts in smoothly, catching the bottle in the ice bucket."

    hide maxime
    hide dawn
    show trina casual smile at centre
    so "I don't have real champagne glasses, but that's what novelty pineapple mugs are for. Everyone take one!"

    hide trina
    "Dawn pours us each a drink in the pineapple-shaped mugs Trina's been trying to hawk to customers."
    "I take a long sip, savoring the champagne on my tongue."

    show maxime casual basic at left2
    show dawn jacket grin at right2
    dw "C'mon Maxime, say something nice to your protege."
    "I turn to Dawn who is playfully poking Maxime's arm and wagging their eyebrows in my direction."
    show maxime casual smile
    "Maxime shares a long-suffering look with me, then breaks into a genuine smile."

    hide dawn
    show maxime casual_cu smile_cu at maxime_cu
    mx "You've really grown, [genericfn]—and in such a short time!"
    mx "You're special."

    hide maxime
    show trina casual_cu smile_cu at trina_cu2
    so "Hell yeah she is!"

    show mscmc casual_hairdown smile at left1
    show trina casual smile behind mscmc at right1
    "Trina throws an arm over my shoulders, raising her pineapple cup."
    so "A toast to [genericfn] and her ascent to surf fame and fortune!"
    show mscmc casual_hairdown embarrassed
    "Everyone raises their glasses to me, making me feel even warmer and fuzzier than the champagne has."
    so "What should we do now? Ooh, sea shanties! Sea shanties are hot right now. All the kids are singing them."

    hide trina
    hide mscmc
    show dawn jacket grin at centre
    dw "Oh, far out. I saw a good one on YouPlayer, lemme find it."
    dw "Here we go: 'How Many Pirates in a One-Man Bath?'"

    hide dawn
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(I think that's my cue to find something else to do.)"
    hide mscmc
    "I snicker, glancing around the shop, and realize that Maxime's already slipped away from the incoming sea shanty harmonizing."

    scene bg msc_labeach_sunset at bg with dissolve
    play music mscmctheme
    "I peer out the window and see him sitting on the shore, silhouetted by the last of the sunset."
    show mscmc jacket_hairdown grin at centre
    mcmaxime "Hey, mind if I join you?"

    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    "Maxime looks up, smiling in pleasure, though his cheeks have colored a little."
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Ah, he has his sketchbook!)"
    show mscmc jacket_hairdown smile at left2
    show maxime casual smile at right2
    mx "Please."
    "He shifts over, making space for me to settle down beside him."
    "He hesistates for a moment, a piece of charcoal still clasped in his hand, then glances at me shyly."
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    mx "Would you like to see?"

    hide maxime
    $menuhideborder = True
    menu maximee6c2:
        "A. Look at Maxime's sketches!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmaxime "I sure would!"
            hide mscmc
            "I settle down beside him, enjoying the way his shoulders relax at my enthusiasm."
            "I lean over his shoulder and admire the charcoal sketch he's been working on, of a wave breaking against the shore."
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "Wow, you added so much detail in just a few minutes!"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "I like capturing the waves—the ocean is one of my favorite things to draw."
            show maxime casual embarrassed
            "He rubs at his cheek bashfully, and accidentally leaves a smudge of charcoal that I'm very tempted to wipe off."
            show mscmc jacket_hairdown grin
            mcmaxime "Aw, are you being shy again?"
            show mscmc jacket_hairdown smile
            mx "Maybe a little."
            show mscmc jacket_hairdown grin
            mcmaxime "You shouldn't be. You've got a real gift!"
            show maxime casual smile
            mx "Well, I did want to show you what I was sketching. I thought you might like it."
            hide mscmc
            hide maxime
            "He holds up the page he's been working on so I can lean in and admire all the details."
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "I do like it. I remember some of your abstract paintings back at the studio. I like the way you capture the foam in the water."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Yeah, the texture's fun. You can use the paint or chalk to make it look natural."
            hide mscmc
            hide maxime
            "As he speaks, he rubs at the edge of the water he's drawn, smoothing the shading out to create a natural effect."
            show mscmc jacket_hairdown surprised at left2
            show maxime casual basic at right2
            mcmaxime "Is this a charcoal piece, or are you going to add paint?"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Not to this sketch page, but this is what you call a rough draft."
            mx "I figure I'll do a few studies at different times of day, then choose the one I like best to paint."
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmaxime "Is your sketchbook full of studies?"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Studies and practice, mostly."
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmaxime "Can I see?"
            hide mscmc
            hide maxime
            "I sit cross legged, and give him my most winning smile."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmaxime "Pretty please?"
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            "Maxime flushes again, momentarily fumbling for words, but quickly passes his sketchbook over."
            mx "Sure...But, uh, remember they're just sketches, so they're not very polished..."
            hide maxime
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmaxime "Don't worry, I get you."
            hide mscmc
            "I reach out, taking advantage of our close proximity to pat his shoulder."
            "I gingerly lift the first page and flip it over, admiring a spread of pages that's covered with many small sketches."
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "Hey, it's like a little slice-of-life of the pier!"
            mcmaxime "There's a seagull, and a crab, and a windsurfer..."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "That was Dawn, though you can't really tell since it's just a gesture sketch."
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmaxime "And some cute little kids building a sandcastle..."
            hide mscmc
            hide maxime
            "Even Maxime's 'gesture sketches', as he calls them..."
            "Seem to perfectly capture the movement and life of whatever he's drawing, with fluid strokes like water."
            "I keep happily flipping through his book and admiring each page..."
            "Until I come across a more detailed charcoal drawing, with a heavy use of light and dark."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmaxime "Ooh, this one looks like a full art piece..."
            hide mscmc
            "I pause as I take a second look at the portrait of a woman, and my jaw drops."
            scene bg msc_maxime_s0_mini4 at bg with dissolve
            "(That's...me?)"
            "It must be—of course I recognize myself—but Maxime's portrayed me beautifully, delicate shading shimmering over my skin like moonlight."
            "(Is this how he sees me?)"
            "The most arresting part of the drawing is my expression, which is soft and intelligent, yet filled with determination."
            "(I had no idea anyone could see me so beautifully.)"
            scene bg msc_labeach_sunset at bg with dissolve
            show maxime casual_cu embarrassed_cu at maxime_cu
            "Maxime clears his throat, looking out across the water clearly embarrassed."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I try to cover my own blushes, laughing lightly."
            show mscmc jacket_hairdown_cu grin_cu
            mcmaxime "This must be based on a beautiful lady."
            show mscmc jacket_hairdown embarrassed at left2
            show maxime casual smirk at right2
            "Maxime scoffs, his lips quirking in a smile."
            mx "You know it's you."
            show mscmc jacket_hairdown grin
            show maxime casual embarrassed
            mcmaxime "Yeah...Yeah, I do."
            hide mscmc
            hide maxime
            "I reach out and lay a hand on his shoulder."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmaxime "Thank you, Maxime—that drawing made me very happy."
            mcmaxime "And thank you for trusting me and showing me your art. It's a privilege."
            hide mscmc
            "I close the book and hand it back to him reverently, and he accepts it, swelling with pride."
            "We fall into silence, but it's not strained, just peaceful."
            show maxime casual_cu smile_cu at maxime_cu
            "When our eyes meet again we hold each other's gazes, the sound of the waves as a backdrop."
            "An unspoken communication passes between us, and for a moment I feel perfectly entwined with him..."
            "Just like I did when he taught me to listen to the ocean."
            hide maxime
        "B. Decline.":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left2
            show maxime casual basic at right2
            "I shift awkwardly on the sand, clearing my throat."
            mcmaxime "Actually, I had something important I wanted to ask you."
            show maxime casual sad
            "Maxime instantly sobers, nodding."
            show maxime casual surprised
            mx "I see. And what's that?"
            hide mscmc
            hide maxime

    "I lean forward so we're closer together, our shoulders almost brushing, and look up at him hopefully."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcmaxime "Will you teach me more of your ocean secrets, even now that the competition is over?"
    mcmaxime "Please say yes."
    hide mscmc

    scene bg msc_labeach_night at bg with dissolve
    play music mscmaxime
    "As the sun dips below the horizon, Maxime bites his lips at my hopeful expression."
    "He seems to war within himself for a moment, then sighs."
    show maxime casual_cu sad_cu at maxime_cu
    mx "I'm sorry [genericfn]. But I can't do...this any more. Any of this."
    hide maxime
    "I straighten up, sputtering in protest."
    show mscmc jacket_hairdown sad at left2
    show maxime casual sad at right2
    mcmaxime "What? What does that mean? Why not?"
    "Maxime raises his hands, his expression pleading as he tries to calm me."
    mx "Please understand—I like you, I want to spend more time with you, but it's not about what I want."
    mx "That was a closer call with Camilla than you realize. I'm a spy—my job is to spy on humans. You don't want to be mixed up in that!"
    mx "And I don't want to have to spy on you. I couldn't bear it."
    mx "I need to go somewhere where I can do my work without hurting the people around me."

    show mscmc jacket_hairdown surprised
    mcmaxime "Hold on, that doesn't mean we can never see each other again! I still want you in my life."
    show mscmc jacket_hairdown sad
    mcmaxime "And more importantly, I think you want me to be there for you."
    show mscmc jacket_hairdown basic
    mcmaxime "I'm the only person who knows both your secrets. You shouldn't have to carry that burden alone."
    "I reach out on impulse, catching his wrist."

    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcmaxime "Let me be there for you when you need a sympathic ear. It's the least I can do after all you've done for me."
    hide mscmc
    show maxime casual_cu sad_cu at maxime_cu
    "Maxime's eyes glisten, and for a moment I can tell he's genuinely considering it, imagining what it would be like for us to stay friends."
    show maxime casual_cu angry_cu
    "Then his expression clouds over and he shakes his head."
    show maxime casual_cu sad_cu
    mx "I can't make that choice, [genericfn]. That would be selfish."
    mx "I can't pick and choose in my line of work, and I'm not going to risk your safety—or your trust."
    mx "I knew what I was getting into when I took the position. Spying isn't a line of work where you can get close to people."
    mx "I've made this bed, so now I've got to sleep in it."
    mx "I'm just sorry you're stuck in the middle."
    "He has such an expression of hurt that my protests die, and all I want to do is wrap him in a hug."

    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I bet he gives great hugs, with his strong arms...)"
    "(Ugh, why am I still thinking this way? WHy am I making things more painful for myself?)"
    hide mscmc
    "I rest my hands on the sand between us."

    show mscmc jacket_hairdown basic at left2
    show maxime casual sad at right2
    mcmaxime "You shouldn't be sorry, Maxime. You've helped me so much, and even now, you're still looking out for me."
    show mscmc jacket_hairdown sad
    mcmaxime "I hope I've helped you too, even if I was your confidant for only a few days."
    show maxime casual smile
    "Maxime smiles regretfully, watching my hands as I trace circles in the sand."
    show mscmc jacket_hairdown smile
    mx "It's been a wonderful few days. It's been nice to have someone who makes talking easy."
    show mscmc jacket_hairdown sad
    mx "I'll never forget it."

    hide mscmc
    hide maxime
    scene bg msc_maxime_s0_mini5 at bg with dissolve
    "He raises his hand, hesitates, and then, to my surprise, cups my cheek, his palm rough and warm."
    "I gasp, flushing, and our eyes lock, his deep and dark with moonlight reflected like stars."

    scene bg msc_labeach_night at bg with dissolve
    show maxime casual_cu sad_cu at maxime_cu
    mx "I've never felt a bond like this [genericfn], not with anyone else."
    mx "I wish things didn't have to end this way. It feels wrong to leave you, even if it's the right thing to do."

    hide maxime
    $menuhideborder = True
    menu maximee6c3:
        "A. It isn't fair.":
            $menuhideborder = False
            "My lip trembles despite my best efforts to stay calm."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcmaxime "You're right—it isn't fair. It feels all kinds of wrong to have to say goodbye to you."
            hide mscmc
        "B. I'm glad I met you.":
            $menuhideborder = False
            "I force a smile, even as my heart is quietly breaking."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            mcmaxime "I'm glad I met you, Maxime. I'm glad we got some time together, even if it wasn't nearly long enough."
            hide mscmc
        "C: I won't make this harder for you.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcmaxime "I'm not sure it is the 'right' thing...It definitely doesn't feel that way."
            mcmaxime "But I promise I won't make things harder for you. I can see how difficult it is."
            hide mscmc

    show maxime casual_cu basic_cu at maxime_cu
    mx "Here."
    hide maxime
    "He shifts so he's now cupping my hands in his."
    show maxime casual_cu smile_cu at maxime_cu
    mx "Close your eyes. I've got something for you."
    hide maxime
    "I dutifully shut my eyes, trying to memorize the feeling of his hands against mine, when I feel something cool and smooth in my palm."
    "I open my eyes to find I'm now cradling the piece of red sea glass I saw in his studio."
    "Maxime smiles, closing my fingers around it."

    show maxime casual_cu smile_cu at maxime_cu
    mx "For good luck."

    hide maxime
    "He lingers, still clasping my hands, then sighs and pulls away."
    "As he stands up and starts to walk away along the beach, I grip the piece of sea glass hard, turning it over in my fingers."

    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcmaxime "Maxime!"

    hide mscmc
    show maxime casual basic at centre
    "I can't stop myself from crying out, and he pauses for me."
    show maxime casual smile
    pause 0.5
    show maxime casual smile:
        parallel:
            easein 1 xoffset 50
        parallel:
            linear 0.4 alpha 0.0

    "He looks over his shoulder, offering me a last, comforting smile, then when words fail me he turns away."
    "I grip the sea glass in my palm, more determined than ever."

    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I won't let this be the last time we meet!)"
    hide mscmc

    $tobecontinued()

    scene bg msc_end at bg with fade
    pause
    $ resets()
