label dmaximep_season1_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_maxime_studio_day at bg
    play music mscsuspense

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show camilla casual angry at centre
    "The stylish—and intimidating—woman eyes Maxime coldly, then thrusts out her hand."
    $sidecharone = "Party Crasher"
    sid1 "My report? Unless you'd like me to 'wait' for that too."

    hide camilla
    "She sneers while Maxime quickly reaches for a folder on his painting table."
    "He holds it out to her, and she snatches it from him."

    show maxime casual basic at left2
    show camilla casual basic at right2
    mx "Everything's in order."

    show camilla casual angry
    sid1 "Good. I hope you'll be more prompt for our next appointment."

    show camilla casual angry at out_right with dissolve
    "She turns on her heels and marches out officiously."
    "I hold my breath from my hiding spot in the closet, and Maxime watches warily as she makes her way down the beach."

    hide maxime
    play music mschappytimes
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    mcmaxime "Uh, can I come out now?"

    hide mscmc
    "I tentatively open the closet doors a crack, and Maxime nods wearily, waving me forward."

    show mscmc surfer_hairup basic at left2
    show maxime casual sad at right2
    mx "Yes. I'm really sorry about that."

    show mscmc surfer_hairup smile
    mcmaxime "Yeesh, you don't have to apologize. I could tell that lady didn't invite herself over for a friendly chat."

    show mscmc surfer_hairup basic
    "I look up at him expectantly, waiting for an explanation, but continues to stand in the middle of studio, shoulders slumped."

    hide maxime
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Poor guy, something's clearly going on...I bet he'd like someone to talk to.)"

    show mscmc surfer_hairup_cu basic_cu
    "(I know it's not in his nature, but surely there's a way I can get him to open up?)"

    show mscmc surfer_hairup basic at left2
    show maxime casual sad at right2
    "I glance around his painting studio, which is so full of art and trinkets that there's always something new to discover."

    show mscmc surfer_hairup grin
    mcmaxime "Ooh, sea glass! How pretty."

    hide mscmc
    hide maxime
    "I smile, making my way to the window sill, where he's collected a pile of sea glass smoothed by the waves."
    "A single bright red piece, like a sliver of sunset, particularly catches my eye, and I lift it gently, to the light."

    show mscmc surfer_hairup grin at left2
    show maxime casual basic at right2
    mcmaxime "Are you going to use these in an art project?"

    show maxime casual embarrassed
    "Maxime rubs the back of this neck bashfully, but does seem to relax."

    show mscmc surfer_hairup smile
    show maxime casual smile
    mx "I'm not sure. I've been collecting them for a while—just waiting for inspiration to strike, I guess."

    show mscmc surfer_hairup basic
    show maxime casual sad
    mx "...Listen, I am really sorry about shoving you in a closet. I should have kept an eye on the time."

    show mscmc surfer_hairup smile
    "I smile encouragingly, setting the glass back on the window sill."

    show mscmc surfer_hairup grin
    mcmaxime "Hey, do I look mad? It's alright."

    show mscmc surfer_hairup surprised
    mcmaxime "Who was that woman, though? She seemed to have it in for you."

    show mscmc surfer_hairup basic
    "He just sighs, shaking his head."
    mx "Listen, [genericfn]. There's things I'd like to tell you, but I can't—it's out of my control."

    show maxime casual basic
    mx "I {i}want{/i} to tell you everything. Funny how you have that effect on me."

    show maxime casual smile
    mx "How about this: I'll explain everything you need to know to stay safe."

    show mscmc surfer_hairup surprised
    show maxime casual basic
    mcmaxime "Seems fair. Can I ask who that lady was, and what was in the report?"

    show maxime casual sad
    "He grimaces, but nods."
    mx "She's a government representative of the nearest mer city."
    mx "I've been stationed at the pier, and until I'm activated my job is to write reports on human acivity near the mer city."
    mx "Camilla, who you just saw, is my boss, and I give her weekly reports."
    mx "...So basically, I'm a spy."
    "He shakes his head, disgusted with himself, but this has only opened up more questions for me."

    show mscmc surfer_hairup sad
    show maxime casual basic
    mcmaxime "Wait, Camilla's your boss? Why is she so hostile?"

    show maxime casual sad
    mx "You should stay away from her. If she knew a human was in on our secret...Well, it's better to keep her in the dark on that."

    show mscmc surfer_hairup surprised
    mcmaxime "Is she half-mer though, like you?"

    show maxime casual basic
    mx "No, she's a full mer—the city's allowed her some sort of spell to let her walk on land. It's what they do for full-mer agents."
    mcmaxime "Wait, just how many mermaids are walking around the pier?"

    show maxime casual smile
    "His mouth quirks up in a smile for the first time, and he beckons me towards the door."

    show mscmc surfer_hairup smile
    mx "Come on. That's something I {i}can{/i} show you."

    scene bg msc_boardwalk_day_people at bg with wiperightdissolve
    "Out on the boardwalk, Maxime looks around until he spots Dawn's fluffy purple jacket."

    show maxime casual smile at centre
    mx "Hey Dawn!"

    hide maxime
    show dawn jacket grin at centre
    dw 'Maxime, my guy!'

    show maxime casual smile at left2
    show dawn jacket smile at right2
    "Dawn hops up from where they were lounging on a bench watching the watre, and hurries towards us."
    "When they meet, Maxime and Dawn pound their fists together..."
    "And commence a complicated handshake that must have taken at least a week to learn."

    hide maxime
    hide dawn
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Wait a minute...No way...)"

    hide mscmc
    show maxime casual smile at left2
    show dawn jacket smile at right2
    mx "Good news, Dawn—[genericfn] here is 'in the know'."

    hide maxime
    hide dawn
    "Before I can squeal in excitement, Dawn beats me to it with a gasp of delight, sweeping me up in a hug."

    show dawn jacket_cu grin_cu at dawn_cu
    dw "Heyy, [genericfn]'s in the secret club!"

    hide dawn
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "I lower my voice to excited whisper."
    mcmaxime "I can't believe you're a mer too, that's so {i}cool!{/i}"

    hide mscmc
    "Maxime rolls his eyes fondly as we dance around on the boardwalk, making fools of ourselves."

    show maxime casual basic at left2
    show dawn jacket grin at right2
    dw "Okay, this is cool as shit, but unfortunately I've got a windsurfing lesson in five. Pinky-promise we'll talk more later."
    dw "Good work, Maxime. Love our new club member. Love to se you with a {i}friend{/i}."

    show dawn jacket grin at out_right with dissolve
    "They wink, saluting cheekily, before hurrying down the stairs to the beach."

    show maxime casual embarrassed
    "Maxime sputters, clearly embarrassed, and I giggle, looking for a way to relieve him."

    hide dawn
    hide maxime
    $menuhideborder = True
    menu maximee4c1:
        "A. Y'all are cute.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left2
            show maxime casual basic at right2
            mcmaxime "Aw, y'all are cute. You remind me of me and Trina."
            mcmaxime "Only taller. And secret-mermaids."
        "B. Let's form a real club.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left2
            show maxime casual basic at right2
            mcmaxime "We should form a real secret club, just the three of us."
            mcmaxime "We can make a fort and everything. Password is 'baby beluga'."
        "C. Teach me your secret handshake.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left2
            show maxime casual basic at right2
            mcmaxime "So, are you going to teach me that secret handshake? That was cool."

    show maxime casual smile
    "Maxime chuckles despite himself, before beckoning me back in the direction of his studio."

    scene bg msc_maxime_studio_sunset at bg with clockwise_wipe
    play music mscmctheme
    show mscmc surfer_hairup smile at left2
    show maxime casual smirk at right2
    mx "So, about that closet thing..."

    show mscmc surfer_hairup grin
    mcmaxime "I told you, don't worry about it! No closet could contain me, after all."

    show maxime casual basic
    "I poke his arm teasingly, and he just rolls his eyes."

    show mscmc surfer_hairup basic
    show maxime casual sad
    mx "I still feel like I should apologize for shoving you in with the broken boards and paddles."

    show maxime casual smile
    mx "Can I treat you to dinner? There's a great little poke place near my studio."

    show mscmc surfer_hairup grin
    "I perk up, a mixture of excitement and hope."

    hide maxime
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    "(He wants to pay for dinner? Whoa, gallant!)"

    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime notices me deliberating and gives me a winning smile, calculated to make a girl weak in the knees."
    mx "Pretty please?"

    hide maxime
    $menuhideborder = True
    menu maximee4c2:
        "A. Dinner date with Maxime." (paidchoice = "paidchoice"):
            $menuhideborder = True
            show mscmc surfer_hairup grin at left2
            show maxime casual smile at right2
            mcmaxime "Well, how can I refuse an offer like that? Lead the way, sailor."
            hide mscmc
            hide maxime
            scene bg msc_boardwalk_sunset_people at bg with wiperightdissolve
            "He just smiles and beckons me down a side street off the pier."
            "A poke food cart hides between two buildings, filling the alley with the delicious smell of fried rice."
            $sidecharone = "Poke Chef"
            sid1 "Maxime! What can I get you today?"
            show mscmc surfer_hairup smile at left2
            show maxime casual basic at right2
            "Maxime turns to me."
            show maxime casual smile
            mx "What would you like?"
            show mscmc surfer_hairup grin
            mcmaxime "You order for me, you're clearly a regular."
            hide mscmc
            hide maxime
            "He raises his hand in a simple gesture to the chef."
            show mscmc surfer_hairup smile at left2
            show maxime casual smile at right2
            mx "Two miso salmon bowls, and whatever the craft beer special is for the lady."
            show maxime casual basic
            "As the chef prepares our order, I turn to Maxime quizzically."
            show mscmc surfer_hairup surprised
            mcmaxime "So mermaids eat fish?"
            show maxime casual smirk
            "He snickers."
            mx "Hey, we're the top of the ocean food chain, just like you humans on land."
            show maxime casual smile
            mx "Not to say there aren't any vegan mermaids out there, though."
            show mscmc surfer_hairup grin
            mcmaxime "Sounds reasonable."
            hide mscmc
            hide maxime
            scene bg msc_maxime_studio_sunset at bg with wiperightdissolve
            "We return to the paint studio with bowls overflowing with rice, fish and fresh vegetables."
            "Maxime passes me a pair of chopsticks, and I briefly close my eyes..."
            "Reflecting on the smell of paint and the sound of waves just past the beach."
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(This is so cozy and peaceful...I can see why he chose this cottage.)"
            show mscmc surfer_hairup sleep at left2
            show maxime casual smile at right2
            mx "What're you thinking?"
            show mscmc surfer_hairup smile
            show maxime casual basic
            "I open my eyes to find Maxime cocking his head at me."
            show mscmc surfer_hairup grin
            mcmaxime "Just listening to the ocean."
            mcmaxime "...We are going to go out on the ocean for our next lesson, right?"
            show mscmc surfer_hairup smile
            show maxime casual smile
            "He chuckles, settling down beside me."
            mx "Yeah, don't worry. I want to see you on the water up close, you're pretty impressive from a distance."
            mx "You've got an uncommon skill."
            show mscmc surfer_hairup embarrassed
            show maxime casual basic
            "I blush just to hear him say it."
            show mscmc surfer_hairup grin
            mcmaxime "Well yeah, I do know that. But it means a lot, coming from a surfer like you."
            show maxime casual embarrassed
            "He smiles, also blushing, and quickly distracts himself with the beer bottle I'm holding."
            show mscmc surfer_hairup smile
            show maxime casual smile
            mx "So, what novelty IPA are they dishing up today?"
            show mscmc surfer_hairup surprised
            show maxime casual basic
            mcmaxime "Well, I'm not expert, but it's called 'Hangry Elk', and it's pretty good."
            show mscmc surfer_hairup smile
            show maxime casual smile
            mx "Huh, I haven't heard of that one. Can I try a taste?"
            show mscmc surfer_hairup embarrassed
            "My heart somersaults in my chest, even as i try to play it cool."
            hide maxime
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(In my neck of the woods, we call that an indirect kiss!)"
            show mscmc surfer_hairup grin at left2
            show maxime casual smile at right2
            "I dangle the bottle towards him teasingly."
            mcmaxime "You should have gotten yourself a hipster beer. But fortunately, I'm super nice, so help yourself."
            mx "Much obliged."
            hide mscmc
            hide maxime
            "As he takes the bottle, his hand briefly lays over mine, and now my stomach has joined my heart in doing flip-flops."
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "(His hands are so big...and warm...)"
            hide mscmc
            "Maxime brings the bottle to his lips for a brief sip, letting the beer linger on his tongue reflexively."
            show mscmc surfer_hairup smile at left2
            show maxime casual smile at right2
            mx "Yeah, not bad."
            show maxime casual basic
            "He sets the bottle down neatly, then pauses, his gaze still on me."
            show mscmc surfer_hairup surprised
            mcmaxime "W-what?"
            show mscmc surfer_hairup basic
            show maxime casual surprised
            mx "I was just thinking that I like how you speak your mind. When you didn't like my lesson plan, you let me know."
            show maxime casual smile
            mx "It's a rare virtue."
            show mscmc surfer_hairup surprised
            mcmaxime "Really? I feel like it annoys most people."
            show mscmc surfer_hairup grin
            mcmaxime "I like that you like it."
            "We smile at each other in the fading sunset."
            show mscmc surfer_hairup smile
            mx "Well, those people don't deserve you. It's always better to face the truth head-on."
            show mscmc surfer_hairup grin
            show maxime casual basic
            mcmaxime "That's what I think! Cheers."
            hide mscmc
            hide maxime
            "I raise my beer bottle, and he grabs his nearest paint pot jokingly to clink together."
            "Despite my fooling around, I can feel all my blood running to my cheeks, and that familiar sensation of butterflies in the stomach."
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "(What are you doing, [genericfn]? This isn't the time for crushes!)"
            show mscmc surfer_hairup_cu angry_cu
            "(You're a grown-up with a career plan!)"
            hide mscmc
            "I hastily shovel rice and salmon into my mouth, trying to distract myself."
            "All the while I'm fully aware that so long as Maxime is sitting across form me and watching me with those warm brown eyes..."
            "The butterflies aren't going anywhere."
        "B. No, I should head home":
            $menuhideborder = False
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mcmaxime "Hello there reader, it's me [genericfn]. We do not have this choice on file, so just pretend I turn Maxime down here."
            mcmaxime "We apologize for the inconvenience. Ok, back to your reguarly scheduled Lovestruck."
            hide mscmc

    show mscmc surfer_hairup smile at left2
    show maxime casual smile at right2
    mx "Can I walk you back to the surf shop? It's getting late."

    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(He knows the surf shop is only a block away...But he wants me to feel safe.)"
    "(He's so nice. How can I not catch feelings?)"

    show mscmc surfer_hairup grin at left2
    show maxime casual basic at right2
    mcmaxime "Aw, that's sweet of you. I'd love a walk down the pier."

    hide maxime
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(With you. Beacuse I don't want to say goodbye yet.)"

    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime smiles, illuminated by the setting sun, and I get the sense that he also wants to prolong our evening."

    hide maxime
    scene bg msc_boardwalk_night_lights_people at bg with fade
    play music mscmaxime
    "As we walk back along the pier, I study Maxime closely."

    show mscmc surfer_hairup basic at left2
    show maxime casual basic at right2
    "He's as tall and proud as ever, though I notice that he's started favoring his left foot very slightly whenever he takes a step."

    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Is that the injury Dawn mentioned? It seems like it affects him more on land than in the water, and only in his human form.)"

    show mscmc surfer_hairup surprised at left2
    show maxime casual basic at right2
    mcmaxime "Maxime, why did you give up surfing?"

    show maxime casual angry
    "I blurt my question out, hopeing to catch him unawares, but he instantly closes up, keeping his eyes on the horizon."
    mx "Let's not talk about that."

    hide maxime
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(So you'll tell me all about being a spy, but you don't want to talk about a surf injury? Priorities, dude.)"

    show mscmc surfer_hairup sad at left2
    show maxime casual angry at right2
    mcmaxime "It just seems like a shame to me that you've completely taken youself out of any competitions."
    mcmaxime "You're clearly still at the top of your game..."
    mx "I said I'm not going to talk about it."
    "He's as good as his word, pressing his lips shut."

    hide mscmc
    hide maxime
    "We've reached the back door of the surf shop, and he steps aside, gesturing with his arm."

    show mscmc surfer_hairup sad at left2
    show maxime casual basic at right2
    mcmaxime "Okay..."
    mx "Training's at eight tomorrow."
    mcmaxime "I know."

    show mscmc surfer_hairup basic
    mx "Good. I'll see you then."

    hide mscmc
    hide maxime
    "He turns abruptly and walks back across the pier, trying to hide his limp."

    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(So much for opening up to me.)"

    hide mscmc
    scene bg msc_labeach_sunset at bg with fade
    play music mscbeach
    show maxime shorts basic at centre
    "When I show up for training the next morning, Maxime nods curtly in greeting, his walls still up from last night."

    hide maxime
    show mscmc surfer_hairup_cu basic_cu at mscmc_cu
    "(Yeah yeah, I get it, you want to be a man of surf mystery. That's not going to keep me from practicing, though.)"

    hide mscmc
    scene bg msc_ocean_wide_sunset at bg with dissolve
    "This time, we paddle out into the water."

    play sound "audio/sfx/splash03.mp3"
    "Maxime floats a little ways away as I catch my first wave."
    "I keep my eyes on the horizon, determined and focused, and mount my board swiftly, my cares melting away as I tame my first wave."
    stop sound

    "I keep an unbroken streak, and by the time I paddle back after my third wave..."
    "I shake the water from my eyes to find Maxime breaking into a smile."

    show mscmc surfer_hairup smile surfboard at left2
    show maxime shorts smile surfboard at right3
    mx "You're on a roll today!"

    show mscmc surfer_hairup grin surfboard
    show maxime shorts basic surfboard
    mcmaxime "Anything I should work on?"
    "I kick my legs underwater, feeling quietly smug that I got him to lighten up."

    show mscmc surfer_hairup basic surfboard
    show maxime shorts surprised surfboard
    mx "Technically, you've got it all, but not everything is about the right technique."
    mx "If I were to give you any piece of advice, it would be to listen to the ocean more."

    show mscmc surfer_hairup sad surfboard
    show maxime shorts basic surfboard
    "I rest my arms on my board, frowning up at him."
    mcmaxime "'Listen to the ocean'?"

    show maxime shorts smile surfboard
    mx "I'm saying this as a merman, not some new age guru."

    show mscmc surfer_hairup basic surfboard
    show maxime shorts basic surfboard
    "He bends down so his palm is just touching the water."

    show maxime shorts smile surfboard
    mx "The ocean breathes just like any living thing—you can feel it in the rise and fall of the waves, and the way the moon tugs at the tides."
    mx "When you understand that rhythm and breathe in sync with it, you can clear your mind and move {i}with{/i} the ocean, not just over it."

    show mscmc surfer_hairup sad surfboard
    show maxime shorts basic surfboard
    mcmaxime "That sounds a little new age hippy-dippy, I have to be honest with you."

    show mscmc surfer_hairup smile surfboard
    show maxime shorts smile surfboard
    "He just laughs, soft and charming, which sets my heart fluttering."
    mx "Give it a try anyways. What could it hurt?"
    mx "Close your eyes and focus on your breathing. Feel the waves underneath you."

    show mscmc surfer_hairup sleep surfboard
    show maxime shorts basic surfboard
    "I do as he says, slowing my breathing and noticing the way the ocean gently lifts and releases my board with each wave."

    hide maxime
    hide mscmc
    show mscmc surfer_hairup_cu sleep_cu at mscmc_cu
    "(This is very relaxing, but...Am I one with the ocean yet?)"

    show mscmc surfer_hairup_cu sad_cu
    "(I don't think so. Not the way Maxime is.)"

    show mscmc surfer_hairup sad surfboard at left2
    show maxime shorts basic surfboard at right3
    "I sigh, blinking my eyes open."
    mcmaxime "I don't know, Maxime. Maybe only mer can 'breathe with the ocean'."

    show mscmc surfer_hairup basic surfboard
    show maxime shorts smile surfboard
    mx "I don't think that's true. I'm certain you can, there's something about you...It might take a little work, but you'll get there."

    show mscmc surfer_hairup embarrassed surfboard
    "I'm stunned by his belief in me and open smile, and feel something dangerously like feelings welling up in my chest."
    "I'm able to distract myself when we go back to practicing, and manage to keep up a winning streak."

    hide maxime
    hide mscmc

    scene bg msc_labeach_day at bg with dissolve
    play music mscsuspense
    "When we finally return to shore, there's a long figure waiting for us, her expensive shoes conspicuous against the sand."

    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Oh no, her again?)"

    show mscmc surfer_hairup basic at left2
    show maxime shorts angry at right2
    "I look to Maxime, who's stiffened, but still approaches Camilla gamely."

    hide mscmc
    hide maxime
    show camilla casual angry at centre
    cm "Again, Maxime? You decided that a little morning surf was more important than our meeting?"
    "Her daze shifts disdainfully to me."

    hide camilla
    show mscmc surfer_hairup basic at left2
    show maxime shorts basic at right2
    mx "I'm sorry, Camilla—I had a lesson to teach."

    hide maxime
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Did he just admit to his mer-boss that he chose me over her?)"

    hide mscmc
    show camilla casual smirk at centre
    cm "And this young lady is one of your coworkers, I presume? Aren't you going to introduce me?"

    hide camilla
    $menuhideborder = True
    menu maximec4c3:
        "A. Yup, I'm his coworker.":
            $menuhideborder = False
            show mscmc surfer_hairup basic at left2
            show maxime shorts sad at right2
            "I keep my voice casual, since poor Maxime seems to be treading thin ice."
            show mscmc surfer_hairup smile
            mcmaxime "My name's [genericfn]. I teach the peewee surf classes for Trina."
            hide mscmc
            hide maxime
        "B. He's my instructor.":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left2
            show maxime shorts sad at right2
            mcmaxime "Hi, I'm [genericfn]. Maxime's been giving me some pointers for the upcoming surf competition. He's just trying to help out."
            hide mscmc
            hide maxime
        "C. Who are you again?":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left2
            show maxime shorts sad at right2
            mcmaxime "Hi, I'm [genericfn]. Are you a friend of Maxime's?"
            hide mscmc
            hide maxime
            show camilla casual basic at centre
            "I offer my hand, waiting to see if she'll give me any further information."
            show camilla casual smirk
            "She just smiles and nods, eyes icy cool."

    show camilla casual smile at centre
    cm "It's nice to meet you, [genericfn]."

    show camilla casual smirk
    "Camilla sets her hand on her hip, eyeing me up and down in a manner that feels anything but friendly."

    show camilla casual smile
    cm "You're quite impressive on the water—so effortless. Seems like you can hold your breath for longer than usual too."
    cm "Perhaps I'll stop by the surf shop sometime when you're working."

    hide camilla
    show mscmc surfer_hairup surprised at left2
    show maxime shorts angry at right2
    "Maxime narrows his eyes, but he keeps his lips locked in a grim line."
    mcmaxime "Uh, thank you..."

    hide mscmc
    hide maxime
    show camilla casual surprised at centre
    cm "You know, it's funny. I could have sworn I've seen your face before..."

    show camilla casual sad
    "She taps her fingers to her lips, squinting at me, when her eyes widen."

    show camilla casual smirk
    "Then she just shrugs."

    show camilla casual smile
    cm "Well, I'll leave you to your very important surf lesson."

    show camilla casual smirk at out_right_slow
    "She turns with a little flounce, marching up the bank while Maxime glares after her."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(The nerve of this lady!)"

    show mscmc surfer_hairup_cu sad_cu
    "(And also, how the hell does she know so much about my swimming? Has she been watching me?)"

    $tobecontinued()

    show msc_tbc at bg with fade
    pause
    $ resets()
