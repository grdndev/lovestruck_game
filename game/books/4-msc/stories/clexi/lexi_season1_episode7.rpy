label lexi_season1_episode7:

    $tbc = False
    scene bg msc_boardwalk_night_lights at bg
    play music msctense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    #rain effect
    show hannah casual angry at centre
    "The rainfall is almost deafening, but I'm watching Hannah carefully for any sudden movements."

    "She sneers."
    show hannah casual angry at right2
    show lexi casual angry at left2
    hj "Mark my words, Lexi. Stay out of my way."
    show hannah casual basic
    lx "Or stay out of mine."
    hide hannah
    hide lexi
    show hannah casual_cu angry_cu at hannah_cu
    "Hannah's eyes narrow, sending a cold, sharp jolt through me."
    show hannah casual_cu sleep_cu
    "She composes herself well, but just beneath the surface, she's dangerous."
    hide hannah
    show hannah casual sleep at centre, step_out
    "She turns, the rain water whipping off her in the fast movement, and disappears into the night."
    hide hannah
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Hannah doesn't seem to be the type of person to make idle threats.)"
    hide mscmc
    show mscmc jacket_hairdown angry at left3
    show lexi casual smile at right3
    lx "That went well."
    show mscmc jacket_hairdown basic
    "She gives me a roguish grin."
    show mscmc jacket_hairdown sad
    mclexi "Do you think so? You're not worr...?"

    "A wave of lightheadedness washes over me; I stumble, touching my temple."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Am I getting sick from the rain?)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3
    show lexi casual sad at right3
    lx "[genericfn]? What's going on?"
    show lexi casual basic:
        easein 0.4 xoffset -300
    "Lexi grabs my arm to support me; my vision blurs as she steadies me."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She sounds so far away...)"
    scene bg msc_mcs_vision at bg with eye_open_slow
    stop music fadeout 1.0
    play music mscmcvisions
    "I shut my eyes, trying to refocus, but when I open them, Lexi and the alley are gone. All I see now is the ocean around me."

    "(Is this another vision?)"

    "I feel myself sigh, letting the current cradle me as I relax into its touch. Suddenly, I feel at ease."

    "I look up to the surface of the water, and see the now familiar silhouette of a mermaid swimming above."

    "(It's the same mermaid! It has to be.)"

    "I'm drawn to the distant form, as elegant as a ribbon in the wind. My hand reaches up without me telling it to."

    "But the mermaid is high up, and I can feel my lower back softly resting on the sea floor beneath me."

    "As I stare up at the mermaid circling above me, I hear a soft melodic voice singing an unfamiliar song."
    scene bg msc_mc_bedroom_night_lights at bg with eye_open_slow
    stop music fadeout 1.0
    play music msclexi
    show lexi casual_cu smile_cu at lexi_cu
    "I blink rapidly as my eyes adjust to the bright light of my room and the sight of Lexi smiling softly at me."

    "Her long hair creates a curtain around my face and my nose is filled with a soothing petrichor."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I'm in my bed. And in Lexi's lap...)"

    "(Was that her singing just now? It was beautiful...)"
    show mscmc jacket_hairdown_cu grin_cu

    mclexi "What was that song you were singing?"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi laughs off my question, carding her fingers through my hair."
    show lexi casual_cu bigsmile_cu
    lx "You heard that, huh? Maybe that's the trick to bringing you back from your visions."
    show lexi casual_cu smile_cu
    lx "It's a mer lullaby about a small lake fish. My dad used to sing it to me when I was little."
    hide lexi
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(That's pretty cool.)"

    $menuhideborder = True
    menu lexis1e7c1:
        "A. Ask more about Lexi's dad.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left1
            show lexi casual smile at right1 behind mscmc
            mclexi "Your dad used to sing you that lullaby?"

            "Lexi shrugs, but a small sentimental grin forms at the edge of her mouth."

            lx "He did stuff like that, yeah."

            lx "It’s usually supposed to put people to sleep though, not wake them up."

            "She gives me a teasing look. I smile back at her."

            mclexi "Hard to sleep through such a nice song."

        "B. Ask if Lexi carried you home.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left1
            show lexi casual basic at right1 behind mscmc
            mclexi "You took me all the way back to my room?"
            show lexi casual smile
            lx "No, obviously you strolled back all by yourself. Impressive sleepwalking, by the way."
            show mscmc jacket_hairdown grin
            "I laugh, my voice still heavy from unconsciousness."

            mclexi "Fine, okay, you got me there."

        "C. Ask abouter her lullabies.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left1
            show lexi casual basic at right1 behind mscmc
            mclexi "You said the song is about a lake fish, right?"
            show lexi casual smile
            lx "Yeah. I even still remember the words, though it’s been a while since I’ve sung it."
            show mscmc jacket_hairdown grin
            mclexi "Really? You sounded nice, so I figured you must sing a lot."

            lx "It’s not a habit I’ve really ever gotten the chance to indulge."
            show mscmc jacket_hairdown surprised
            mclexi "What, really?"
            show lexi casual bigsmile
            lx "Yup! Same as all that magical, whimsical kinda stuff, the gov is not about it. I’m glad you liked it though."
            show mscmc jacket_hairdown embarrassed
            show lexi casual smile
            "She winks, sending a blush to my cheeks that I have to gently shake away."
    show mscmc jacket_hairdown surprised at left1
    show lexi casual smile at right1 behind mscmc
    mclexi "What happened? We were dealing with Hannah, and then..."
    show lexi casual sad
    lx "You fainted. It was pretty sudden, and you were mumbling stuff at points."

    "The memory of the mermaid in the ocean jumps back to mind."
    show mscmc jacket_hairdown sad
    show lexi casual surprised
    mclexi "I had another vision. I saw that mermaid again."

    lx "The one circling above you? It almost sounded like you were trying to call to someone, but I couldn't make it out."
    show mscmc jacket_hairdown sleep
    mclexi "I don't remember what I said..."
    show lexi casual basic:
        easein 0.5 xoffset 10
        easein 0.5 xoffset -20
    "Lexi stares off into the air for a moment before reaching back to my nightstand and grabbing a piece of scrap paper."
    show lexi casual angry
    "She twirls a black gel tip pen that she pulls from her cleavage and starts to scribble down notes."
    show mscmc jacket_hairdown embarrassed
    "She's fully focused on her writing, giving me a moment to recover from watching her stunt with the pen just now."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She even makes taking notes look hot. That concentrating face is so cute.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left1
    show lexi casual angry at right1 behind mscmc
    lx "Okay, let's try and piece together everything we know so far."
    show mscmc jacket_hairdown sleep
    "I take a moment to collect my thoughts, bringing as many details about the vision as I can to the front of my mind."
    show mscmc jacket_hairdown basic
    mclexi "I remember feeling drawn to the mermaid... like they wanted to say something to me, and I wanted to answer."
    show lexi casual surprised
    lx "Say something to you? What did they say?"
    show mscmc jacket_hairdown sad
    mclexi "I didn't hear them actually say anything, it was just this...instinct. Like somehow, I just knew they wanted to tell me something."
    show mscmc jacket_hairdown embarrassed
    show lexi casual angry
    "Lexi taps the clicky end of the pen against her lip. I bite my own, trying not to stare at her mouth too long."
    show mscmc jacket_hairdown surprised
    lx "The way you describe these visions... I think that the orb might be trying to bring them out of you."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(So the visions are... inside of me? Like a forgotten dream or a memory?)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left1
    show lexi casual angry at right1 behind mscmc
    mclexi "Bringing the visions out of me... is that anything you've ever heard of before?"
    show lexi casual sleep
    "Lexi shakes her head vigorously."
    show lexi casual bigsmile
    lx "No, but that's what makes this so exciting!"
    hide mscmc
    hide lexi
    show lexi casual_cu bigsmile_cu at lexi_cu
    "I catch the familiar sparkle in Lexi's eyes, the sparkle that tells me she's concocting a plan."
    show lexi casual_cu smile_cu
    lx "Now I really want to get my hands on that orb just to get to the bottom of this!"
    scene bg msc_day_lightson_uv at bg with wiperight
    show lexi casual smile at centre
    stop music fadeout 1.0
    play music msclexiuv
    "Several large towers of books surround Lexi as she lays on the floor of the UV reading a particularly thick tome."

    "Her silky green hair is splayed out as she lays on her back, holding the hefty book in the air above her as she reads."
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I'm doing my best to keep up, but she looks so serene when she's focused. It's difficult not to steal glances.)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3
    show lexi casual basic at right3
    "I look down at the book I've been combing through, then at Lexi's feet that are kicked up on the couch. I can't help a little laugh."
    show lexi casual smile
    mclexi "How are you comfortable like that?"
    show lexi casual surprised
    lx "Like what?"
    show mscmc jacket_hairdown embarrassed
    show lexi casual embarrassed
    mclexi "You look like you're purposely posing very alluringly."
    show lexi casual smile
    "Lexi winks at me."

    lx "Maybe I am. I do have a lot to show off."

    "Lexi lays the open book on her chest and playfully flexes her toned bicep before picking it back up."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Is she trying to fluster me? Who am I kidding, of course she is—and it's working.)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3
    show lexi casual smile at right3
    lx "Besides, I'm good at speed reading, doesn't require much focus from me."
    show mscmc jacket_hairdown smile
    mclexi "Oh yeah? How good?"
    show lexi casual bigsmile
    lx "Good enough to swim circles around—ah ha!"
    show mscmc jacket_hairdown grin
    "As she teases me, her eyes light up at the pages of her book."
    show mscmc jacket_hairdown surprised
    mclexi "Did you find something?"
    show lexi casual basic
    lx "Hell yeah I did! Well, sort of. There's a small passage here about mer artifacts bringing on visions..."

    lx "...and it's referencing this other research book I've got over here."
    show lexi casual surprised:
        easein 0.4 xoffset 40
    "Without looking, she grabs a book from the middle of one of the stacks around her, causing many books to tumble down on her."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Oof! That must've knocked the wind out of her. It's kinda endearing though how she's so motivated.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show lexi casual bigsmile at right3
    "Lexi pushes the fallen books off of her without hesitation and starts to flip through pages, sitting up energetically as she stops."
    show mscmc jacket_hairdown surprised
    lx "Here it is! 'Some artifacts have been reported to bring on visions, and..."
    show lexi casual sad
    "Lexi's face sours. She huffs as she slams the book shut and gets up off the floor."

    mclexi "What's wrong? I'm not cursed or something, right?"
    show lexi casual angry
    lx "No, it's just that these books all say the same vague things. This won't get us anywhere."
    show mscmc jacket_hairdown basic
    "Lexi crosses her arms, scowling at the two books."
    show lexi casual bigsmile
    lx "It's because the magic involved is so rare. I've nabbed my fair share of low-key magic antiques, but this is on a whole other level."
    show mscmc jacket_hairdown smile
    show lexi casual angry:
        easein 0.4 xoffset -100
        easein 0.4 xoffset +100
    "Lexi paces rapidly back and forth, biting her thumb."

    "I watch as she starts talking to herself, puzzling through the conundrum on our hands."

    lx "Mer magic is touchy with who you can sell it to, though 'sell' isn't really accurate."

    lx "There's the mer resistance that is against the government, but they're broke as hell."

    lx "Then there's the black market, but that's like rolling dice, always a gamble."

    lx "The buyer might decide it's easier to kill you and take your wares and then you've got to fight your way out."
    show mscmc jacket_hairdown surprised
    lx"The mer government wants the artifacts, obviously, but you won't convince them to pay you—they'll just arrest you and confiscate it."

    mclexi "So magic artifacts are rare, but not exactly profitable?"
    show lexi casual smile
    lx "Only unless you sell it to the right person, in the right place, at the right time. The stars need to align perfectly."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It sounds really high risk, even for her.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show lexi casual angry at right3
    lx "I just don't understand how a {i}human{/i} museum got their hands on this orb."
    show mscmc jacket_hairdown basic
    mclexi "Maybe it's somehow been in circulation on land for a long time?"
    show lexi casual surprised
    lx "It's possible, but..."
    show mscmc jacket_hairdown surprised
    "She trails off, eyes widening at nothing. I lean a little into her line of sight."

    mclexi "Lexi?"
    show lexi casual bigsmile
    lx "That's it! We're looking in the wrong kind of library!"
    show lexi casual smile
    lx"We don't need mer books, we need {i}human{/i} books! I know just the bookstore for the job too."
    show mscmc jacket_hairdown grin
    "I beam up at her, and then wrinkle my nose."

    mclexi "Why do you keep saying {i}'human'{/i} like that?"

    "She grins devilishly at me, her green eyes sparkling in the light."

    lx "Like what?"

    lx "Should I say it like this? Hoo-man."
    show mscmc jacket_hairdown sleep
    "I roll my eyes and try to fight back an amused smile. Lexi winks again, then her eyes shift just a tad lower."
    show mscmc jacket_hairdown smile
    "I cock an eyebrow at her, half-teasing and half-confused."
    show lexi casual embarrassed
    mclexi "Looking for something?"
    show mscmc jacket_hairdown embarrassed
    show lexi casual smile
    lx "Just thinking. Are you still feeling faint?"
    show mscmc jacket_hairdown smile
    mclexi "I'm fine now."
    show lexi casual smile:
        easein 0.5 xoffset -100
    "Lexi doesn't answer, and instead sits next to me on the couch, leaning in real close."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I can feel the warmth of her...!)"
    show mscmc jacket_hairdown embarrassed at left3
    show lexi casual smile at right3:
        xoffset -100
    lx "We were kind of in the middle of a good time, before."

    "I smirk back at her."

    mclexi "That we were. I am a little disappointed about that..."
    hide mscmc
    hide lexi
    show lexi casual_cu smile_cu at lexi_cu
    stop music fadeout 1.0
    play music mscromance
    "Lexi's lip curls into a grin and she brings her face to mine until our noses are almost touching."

    lx "I'll just have to make it up to you then."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "I can feel my cheeks getting hot, but I stay cool even as her bright eyes look into mine."

    "(Like looking into the ocean... inviting but mysterious.)"
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mclexi "How are you going to do that?"
    show mscmc jacket_hairdown_cu smile_cu
    "I can't help but bite my bottom lip as my mind starts to imagine where our touching had been previously headed."
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    lx "Maybe a kiss? A kiss to make it up to you..."

    "Lexi's cheeks are flushed red as she touches the tips of our noses together."

    "Her breath on my lips makes my body tremble slightly as she takes my hands in hers."
    hide lexi
    $menuhideborder = True
    menu lexis1e7c2:
        "A. Let Lexi kiss you better."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I smile and nod coyly as I feel my heart rate begin to speed up in anticipation of her touch."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi grins and places her free hand on the wall behind my head."

            "She brings her face even closer, to the point any  movement from me will bring our lips together."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(When she looks at me like that it’s all I can do to hold back from kissing her! But I know she wants me to wait.)"
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "Lexi’s green eyes peer through her long lashes. Each breath we take can be felt between us, as she brings her chest against mine."

            "Then she presses our lips together, but instead of a passionate energy-packed kiss, it’s soft and sweet. I’m pleasantly surprised."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(This feels different… like a new side of Lexi I’m getting to see.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi leans back, looking at me again from under those pretty lashes."
            show lexi casual_cu embarrassed_cu
            lx "So, feeling a little less disappointed?"

            "My head is swirling from the scent of Lexi’s hair mixed with the longing coursing through my body."
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(I want more... I need her to kiss me more.)"
            show mscmc jacket_hairdown_cu sad_cu
            mclexi "Not quite yet…"
            show mscmc jacket_hairdown_cu embarrassed_cu
            "I barely manage to whisper my response; my mouth feels so dry."
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            lx "Oh?"
            show lexi casual_cu smile_cu
            "She brushes my hair behind my ear and looks deeply into me. I shudder, and nod my head."

            lx "I guess I’ll just have to keep going until you’re all better."
            hide lexi
            "She kisses me again, this time harder, fiercer. I relish the taste of her, it’s like sparks are dancing between our lips."
            stop music fadeout 1.0
            play music mscpassionateromance
            "She slides her hand into my hair and pulls my body into hers."

            "A soft moan escapes my lips as I run my hands down her back and slip them into her back pockets."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I want to keep her close to me, against me, forever.)"
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "I squeeze my hands a little in Lexi’s pockets and she jumps."
            hide lexi
            "Her face is flushed and she kisses me again, hotter than the last, but I can feel the smallest hint of a grin against my lips."
            show lexi casual_cu smile_cu at lexi_cu
            "She releases me, a colder air dancing between us and I mourn the loss of her warmth."

            lx "How about now?"
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I guess after a kiss like that I could let you off the hook... but I’m not really convinced."
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            lx "You're a needy girl, aren't you?"
            show lexi casual_cu smile_cu
            "She puts on a tone like she’s incredulous, but that burning want in her eyes is impossible to miss. I shrug nonchalantly."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "When it comes to you, maybe I am."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "She smirks shyly as she lets go of my hand and places hers firmly on my hip."
            hide lexi
            "She holds me firmly in her hands as she kisses me again, this time pulling me into her lap as we move down onto the couch."

            "The feeling of her soft lips pressed against mine and her hands so low and hungrily on my body makes my insides tingle."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I feel like a moth to her flame. I’m enraptured by her.)"
            hide mscmc
            "Lexi and I both lean into one another, it’s like we’re in tune, but still keeping the other on their toes with our longing."

            "I feel her tongue brush against my lips and I part them willingly for her."

            "The floral scent of her hair mixed with the taste of her tongue takes my breath away."

            "My head feels light, but I don’t come up for air until I have to."

            "Neither does she. Every breath we do take is short before we’re crashing together again."

            "One of Lexi’s hands moves up from my hip and slips under my shirt and my knees shake as she runs her fingers up my body."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(This is it. She’s not playing games anymore.)"
            hide mscmc
            "Her finger hooks the top of my bra and she pulls it ever so slightly."
            show lexi casual_cu embarrassed_cu at lexi_cu
            lx "We should probably head out to the bookstore."
            show lexi casual_cu smile_cu
            "She pulls her hand out from under my shirt and kisses me long and soft."
            hide lexi
            show mscmc jacket_hairdown_cu grin_cu
            "(Really?! She’s the ultimate tease.)"
            show mscmc jacket_hairdown_cu sad_cu
            "I give Lexi a playful pouty frown as I try to slow my pounding heart."
            show mscmc jacket_hairdown_cu smile_cu
            mclexi "I hate that you’re right. Let’s go."

        "B. But the bookstore...":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show lexi casual basic at right2
            mclexi "I... We need to head to the bookstore, don't we?"
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(God, that was lame. The way she looks at me just gets me so flustered—I can't think straight.)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left2
            show lexi casual basic at right2
            "Lexi eyes me with an expression I can't quite decipher and gets back to her feet."
            show lexi casual smile
            lx "You're not wrong. We do need more information on the orb before Hannah gets her hands on it."
            hide mscmc
            hide lexi
            show lexi casual_cu smile_cu at lexi_cu
            "She gives me a mild smirk and pulls me off the couch by the hand."
            show lexi casual_cu bigsmile_cu
            lx "To the bookstore!"
    scene bg msc_bookstore_day at bg with clockwise_wipe
    stop music fadeout 1.0
    play music mscmctheme
    "Lexi takes me to a bookstore that, without her, I would've missed on my own. Inside it feels like its own little world."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Feels like there should be a portal or secret passage hidden in one of the shelves...)"
    show mscmc jacket_hairdown smile at left2
    show lexi casual smile at right2
    mclexi "It's so... different from anything I'm used to around here."

    lx "Different is usually what you're looking for when it comes to magical artifacts."
    show lexi casual bigsmile
    lx "Don't let the storekeeper hear you sounding like a tourist though."

    "I immediately lower my voice as I walk through the softly lit and cramped bookstore, marveling at the sheer number of tomes."

    "The aisles between bookshelves are almost nonexistent and there are several dozen stacks of books leaning at the ends of each row."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I've only ever been in commercial bookstores before, but this is totally different. All the books look really old.)"

    $sidecharone = "Witchy Old Lady"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2
    show lexi casual smile at right2
    sid1 "Close the door before Miss Nocturne gets out."
    hide lexi
    hide mscmc
    "Lexi and I spin around to see an elderly woman in a paisley dress with a black knitted shawl draped over her shoulders."

    "She's sitting on an old victorian style armchair and at her feet is a fluffy black cat rubbing against her stockinged legs."
    show mscmc jacket_hairdown surprised at left2
    show lexi casual bigsmile at right2
    "Lexi quickly shuts the door behind her as the cat, Miss Nocturne, walks towards us and meows softly."
    hide mscmc
    hide lexi
    $menuhideborder = True
    menu lexis1e7c3:
        "A. Pet Miss Nocturne.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show lexi casual smile at right2
            mclexi "Hey there, kitty kitty."
            show mscmc jacket_hairdown surprised:
                easein 0.4 yoffset +25
                easein 0.4 yoffset -15
            "I crouch down to pet the cat, but as my hand gets closer to her head, she spins around and walks back to the old lady."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(She teased me. Just like Lexi does...)"
            hide mscmc
            show mscmc jacket_hairdown smile   at left2
            show lexi casual smile at right2
            lx "Don't be too upset. Miss Nocturne is just like that."

            mclexi "You've been here before?"
            show lexi casual bigsmile
            lx "Lots of times. It's a trove of knowledge."

        "B. Ask about the store.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show lexi casual bigsmile at right2
            mclexi "This store is crazy… Have you been here before?"
            show mscmc jacket_hairdown smile
            "Lexi nods with a grin."

            lx "Lots of times. It's a trove of knowledge for a treasure hunter."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(That makes sense. There are at least ten times as many books here as in the UV.)"

        "C. Look around.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show lexi casual smile at right2
            "I smile at the cat and take in the book store around me. I touch the spines of tomes on one shelf; they feel old and storied."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(The smell of the pages mixed with incense… I’ve never been in a store like this before.)"
            hide mscmc
            show mscmc jacket_hairdown grin at left2
            show lexi casual smile at right2
            mclexi "This place is crazy. It doesn’t even feel real."

            lx "It is pretty amazing. I’ve come here a lot over the years."

    hide mscmc
    hide lexi
    show mscmc jacket_hairdown grin at left2
    show lexi casual smile at right2
    mclexi "Do you know the old lady?"

    "Lexi nods and leans her head in closer to whisper in my ear."
    hide lexi
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "I've done several jobs for her over the years. She's nice, but really private, doesn't like being bothered."
    hide lexi
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I can tell. She's been a little standoffish since we entered, purveying her domain from her armchair.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left2
    show lexi casual bigsmile at right1 behind mscmc
    sid1 "Make sure your friend there doesn't knock anything over, Lexi."

    lx "She'll be fine, Minerva. You know you can trust me!"

    "Minerva scoffs but shoots me a kind look and picks a scuffed-up tome from the armrest next to her, starting to read to herself."
    show lexi casual smile
    lx "Okay, so we'll split up. You go look in the 'Missing Objects of Interest' section over there."

    lx "I'll look over here in the 'Objects Made for Royalty' section."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Royalty? Does she think the orb was made for royalty?)"
    hide mscmc
    show mscmc jacket_hairdown basic at centre
    "Lexi points me down an unmarked aisle and I gently run my fingers along the leather spines of the books as I stroll down it."
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(They're all so old... and not one of them seems to be fictional. Wait, is this...?)"
    hide mscmc
    show mscmc jacket_hairdown surprised at centre
    "I pick up a book titled 'Ley Lines and Their Uses in Alchemy' and absently flip through it."

    "As I put it back on the shelf I realize all the books on the shelves are about similar topics."
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(This can't be real. I'm in an actual magic bookstore. With real magical books.)"
    hide mscmc
    show mscmc jacket_hairdown sleep at centre
    "I rub the bridge of my nose with my fingers as my mind tries to process my revelation."
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I guess I'll just look for something on... vision-granting orbs... That's specific enough, right?)"
    hide mscmc
    "At least half an hour passes as I skim through several books mentioning anything close to what I'm looking for."

    "As it turns out, inventors of powerful items can come up with a whole lot of words for orbs."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Ball, sphere, egg, eye... My mind's starting to look like a thesaurus.)"
    show mscmc jacket_hairdown_cu surprised_cu
    "As I flip through a book, I feel Lexi come up behind me and press her back against mine."
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "I glance back and see her absently looking at the books on the shelf."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(These aisles really are cramped.)"
    hide mscmc

    "Lexi pushes her back into me a little harder, and delicately brushes her lips against my neck."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(No one can see us back here among the books, god, she's bad.)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "You smell a lot nicer than these dusty old books."

    "I shiver from her breath against my ear; her purring praise brings a laugh out of me."

    $sidecharone = "Minerva"
    hide lexi
    show mscmc jacket_hairdown surprised at left3
    show lexi casual surprised at left1 behind mscmc
    sid1 "What exactly are you two looking for?"
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Son of a-! When did she get there?!)"
    show mscmc jacket_hairdown surprised at left3
    show lexi casual smile at left1 behind mscmc
    "I almost drop the book I'm holding, as Lexi casually backs off of me with a smug look on her face."
    show mscmc jacket_hairdown embarrassed
    "Minerva's gaze has a slight mischievousness to it as she eyes us and the book I was looking at."
    show mscmc jacket_hairdown surprised
    lx "We need a book about objects that elicit visions. Specifically mer related."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Does this old lady know Lexi is a mermaid? Actually, I guess that wouldn't be the weirdest thing in a place like this.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show lexi casual basic at centre behind mscmc
    sid1 "Hmm. I believe I sold such a book to a private collector."
    show lexi casual smile
    lx "Do you happen to know their name?"

    "Without answering, Minerva walks out of the aisle, waving for us to follow."
    show mscmc jacket_hairdown surprised
    show lexi casual basic
    "She walks behind the checkout counter and pulls out a thick ledger that she sets down with a heavy thud."
    show mscmc jacket_hairdown basic
    "After flipping through several pages, she scribbles a name down on a piece of paper."
    show lexi casual smile
    "She folds it before holding it out to Lexi, but as Lexi goes to grab it, Minerva pulls it back slightly."
    show mscmc jacket_hairdown surprised
    sid1 "You know the deal, right?"
    show lexi casual basic
    "Lexi nods solemnly."

    lx "I'll make sure to look for those books you want on my next run, I haven't forgotten."
    show mscmc jacket_hairdown smile
    "Minerva nods curtly. As Lexi takes the slip of paper from her."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Lexi seems to have a talent at communicating with people who have a lot of walls up.)"
    scene bg msc_boardwalk_sunset_people at bg with clockwise_wipe
    stop music fadeout 1.0
    play music mschappytimes
    show mscmc jacket_hairdown smile at left3
    show lexi casual smile at right3
    "The sky is bright orange from the setting sun as we return to the boardwalk."

    "Lexi unfolds the paper with the name of the collector with the book we need."
    show mscmc jacket_hairdown surprised
    show lexi casual angry
    "Her jaw clenches and she sucks her teeth as she reads what's been written on the paper."

    mclexi "What's wrong?"

    "Lexi's shoulders are tense and her default cheeky expression is nowhere to be found."
    show mscmc jacket_hairdown basic
    lx "The person who bought the book is an exiled mer named Emporia. Most people call her Mia, but..."
    show mscmc jacket_hairdown surprised
    stop music fadeout 1.0
    play music msctense
    lx "She's bad news. Like, dangerous. I've heard she's into torturing people."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Jesus, torture!?)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3
    show lexi casual angry at right3
    mclexi "I didn't think anyone could scare you, but torture definitely sounds...yeah."
    show lexi casual basic
    "Lexi chuckles ruefully and runs her fingers through her hair."
    show mscmc jacket_hairdown basic
    show lexi casual smile
    lx "I'm not scared, I'm just smart enough not to mess with Mia for no good reason."
    show lexi casual embarrassed
    show mscmc jacket_hairdown smile
    lx "But this is definitely a good reason because I'm doing it for you. We need this book."
    hide mscmc
    hide lexi
    show lexi casual_cu smile_cu at lexi_cu
    "She looks sidelong at me, smirking daringly."

    lx "So, ready to be bad with me and break into a very dangerous woman's home? I promise to protect you."


    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
