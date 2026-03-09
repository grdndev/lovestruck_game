label maxime_season1_episode12:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_night at bg
    play music mscsuspense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show maxime casual angry at left3
    show wikus casual smile at right3
    "Maxime continues watching Wikus, still cool and collected even as Wikus laughs."
    "I cross my arm, on-edge, and irritated that he's gotten under my skin."
    hide wikus
    hide maxime
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Which just makes me want to try and get under his.)"
    show mscmc jacket_hairdown angry at left3
    show wikus casual smile at right3
    mcmax "Whenever you're done making yourself feel big with supervillain cackling, we'll be waiting."
    "Wikus breaks off with a sneer, seeing through my bluster."
    ws "Come off it, [genericfn], don't bother playing the hardened spy—the role doesn't suit you."
    ws "How did you wind up with a government pawn like him, anyway? Do dull, bureaucratic tools appeal to you?"
    hide mscmc
    show maxime casual angry behind wikus at left3
    show wikus casual smile:
        ease 0.4 xpos stagepos[1]
    "He jabs a finger at Maxime, so dismissive that it makes my blood boil, even though Maxime is immovable."
    ws "Since you 'know everything' about my research, then you know how ocean-shattering it is!"
    hide maxime
    show wikus casual_cu angry_cu at wikus_cu
    ws "My patron is a true visionary—I'll never give them up as long as I live, not when there's so much at stake."
    ws "For my part, I've found a way to change both our worlds. Stiffs like your boyfriend couldn't begin to comprehend my work."

    hide wikus
    $menuhideborder = True
    menu maximee12c1:
        "A. You're nothing compared to Maxime.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show wikus casual angry at right3
            mcmax "From where I stand, you're just a freak with an over-inflated sense of self-importance."
            mcmax "Your ideas are disgusting, and that's all there is to it. Maxime's the noble one for taking you down."
        "B. You're one to talk.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show wikus casual angry at right3
            mcmax "Funny, it sounds to me like {i}you're{/i} just a tool for your master, whoever they are."
            "Wikus rolls his eyes."
            ws "I know my place—and I know a true genius when I see one. I wouldn't sacrifice my patron's work for any price."
        "C. You're deluding yourself.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show wikus casual angry at right3
            "I set my hand on my hip, glaring straight back at him."
            mcmax "Oh really? Are you sure this isn't all one big vanity project so you can get your sadistic ya-yas out?"
            "Wikus sighs, seemingly disgusted."
            ws "I admire your prowess on the water, [genericfn]—but I wouldn't expect you to understand."

    hide mscmc
    hide wikus
    show maxime casual_cu basic_cu at maxime_cu
    "Maxime lays a hand on my arm, the coolness of his palm reigning my anger back."
    show maxime casual basic at left3
    show wikus casual angry at right3
    "H ekeeps his gaze on Wikus, watching for any sudden movements, even as he speaks softly to me."
    hide wikus
    show maxime casual_cu basic_cu at maxime_cu
    mx "It's alright, [genericfn]. You're not going to get through to him."
    mx "He's been drinking his own poison for too long."
    show maxime casual angry at left3
    show wikus casual angry at right3
    "Wikus glares at Maxime, clearly annoyed that he hasn't been able to rattle him."
    hide maxime
    show mscmc jacket_hairdown angry at left3
    "He quickly turns his attention back to me, practically purring."
    show wikus casual smile
    ws "I suppose you've figured out that you were next on my list?"
    show mscmc jacket_hairdown surprised
    show wikus casual basic
    ws "It's a pity I wasn't able to take you. I haven't had a test subject last longer than a week once I've given them the serum, but you..."
    show wikus casual smile
    ws "Well, I can't tell you're something special. I bet you could survive the serum, [genericfn]."
    hide mscmc
    show maxime casual angry at left3:
        pause 0.2
        ease 0.4 xpos stagepos[1]-60
    "I shudder as he stares at me, and Maxime rears up, looming over Wikus at his full height."
    "He doesn't strike him, but his fists are clenched in fury."
    show maxime casual_cu angry_cu behind wikus at maxime_cu:
        xoffset -230
    show wikus casual_cu angry_cu at wikus_cu:
        xoffset 230
    mx "Wikus Sapor, I'm arresting you on behalf of the Maritas government for crimes against mer and humankind."
    mx "You can tell us about your big bad boss from a holding cell."
    show wikus casual_cu smile_cu
    ws "Oh, I don't think so!"
    hide maxime
    hide wikus
    show maxime casual angry at left1:
        xoffset 40
    show wikus casual angry behind maxime at right3
    "Wikus hisses, then laughs again, raising his hand above his head."
    ws "You may have banished me from the ocean, but I'm still mer, and I've still got tricks up my sleeve!"

    # hoo-boy, here we go
    hide maxime
    hide wikus
    scene white at bg
    pause 0.6
    scene bg msc_labeach_night at bg
    show black_smoke_particles
    show wikus casual angry at centre:
        alpha 0.0
        pause 0.2
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0.0
    pause 1.0
    "He makes a sharp movement with his hand, and a cloud of smoke bursts around him, spreading out like squid's ink."
    hide wikus
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(He did not just drop a magical disappearing bomb!)"
    hide mscmc
    show maxime casual angry at centre
    "Maxime curses under his breath, grasping in the black ink, but Wikus has vanished without a trace."
    hide maxime
    show mscmc jacket_hairdown surprised at centre
    "I stare open-mouthed at the spot where Wikus was standing, trying to make sense of what just happened."
    hide mscmc
    show maxime casual angry at centre
    "Maxime swears darkly under his breath."
    mx "He must've had a magic item."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(A perfectly normal statement.)"

    hide mscmc
    hide black_smoke_particles
    play music msctense
    show camilla casual surprised at centre, step_in
    cm "Maxime!"
    show camilla casual angry:
        xanchor 0.5
        ease 0.4 rotate 5 rotate_pad True
        ease 0.3 yoffset 20
    "Camilla hurries towards us from the boardwalk, tripping over the sand in her heels."
    hide camilla
    show maxime casual angry at left3
    show camilla casual sleep at right3
    mx "He got away. Apparently he's not all science."
    show camilla casual smirk
    cm "It's alright. Headquarters is tracking him, magic or no."
    hide maxime
    show mscmc jacket_hairdown surprised at left3
    show camilla casual smile
    "She notices me, and quickly smooths her hair, trying to set me at ease with a smile."
    show mscmc jacket_hairdown basic
    cm "Oh, hello [genericfn]. Some criminals... go off the grid like magic, you know?"
    show camilla casual sad
    "She softens her voice sympathetically."
    cm "You're probably wondering what's going on. I'm a police detective."
    show camilla casual smile
    cm "Maxime, a civilian, has been cooperating with me by keeping an eye on Wikus Sapor."
    show mscmc jacket_hairdown surprised
    "I'm unimpressed by her attempts to cover up the magic and wizardry, but I nod, wide-eyed, and act as though I know nothing of mers."

    hide mscmc
    hide camilla
    $menuhideborder = True
    menu maximee12c2:
        "A. So he was a whitecollar criminal?":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left3
            show camilla casual sad at right3
            mcmax "Oh, was Wikus a bad guy? He always did give me the creeps."
            show camilla casual smirk
            mcmax "Did he commit whitecollar crimes, or something?"
        "B. So that was a smoke bomb?":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left3
            show camilla casual smirk at right3
            mcmax "Was that a real smoke bomb Wikus set off?"
            show mscmc jacket_hairdown sad
            "I make a show of shuddering, hugging my arms."
        "C. I know absolutely nothing.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left3
            show camilla casual basic at right3
            "I raise my hands palms-up."
            show mscmc jacket_hairdown smile
            show camilla casual smile
            mcmax "Don't worry, you don't have to tell me anything. If Wikus was involved in something shady, the less I know the better."

    show mscmc jacket_hairdown smile at left3
    show camilla casual basic at right3
    "Camilla searches my face in the dark while her's stays carefully neutral."
    show camilla casual sleep
    cm "It's nothing you or the other contestants need to worry about. Just a matter of embezzled funds from the competition."
    show camilla casual smirk
    cm "I hope his poor judgement won't detract from your victory."
    show camilla casual smile
    "She smiles, but still seems to eye me up and down."
    hide mscmc
    show maxime casual basic at left3
    "An awkward moment passes between us until Maxime clears his throat, interjecting calmly."
    mx "You'll call me later to take my statement, Camilla?"
    show camilla casual basic
    "Camilla reluctantly pulls her gaze from me, nodding."
    show camilla casual smirk
    cm "Yes. you'll hear from me soon. Thank you for your assistance, Mr. Okun."

    play music mscsadtimes
    show camilla casual smirk at step_out
    "When she's finally left us, stalking back across the beach, I sigh, inching nearer to Maxime."
    hide camilla
    show maxime casual_cu sad_cu at maxime_cu
    mx "You okay?"
    "His voice is gentle, and he places an arm around my shoulders, bringing me close to his side."
    "I nod, cuddling up against his solid chest."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcmax "{i}I'm{/i} okay, but I'm worried about Raymond and the other surfer."
    hide mscmc
    show maxime casual_cu sad_cu at maxime_cu
    "Maxime shifts his hand so he's rubbing my back soothingly."
    show maxime casual_cu basic_cu
    mx "Don't worry, this is the sort of thing Camilla and the government are good at."
    mx "They'll follow Wikus without letting him know he's under surveillance. Then he'll lead them straight to the missing surfers."
    mx "The bureau has more resources. Now that they aren't trying to blow our cover, they'll nab him quick."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    mcmax "Okay."

    hide mscmc
    play music mscromance
    show maxime casual_cu basic_cu at maxime_cu
    "I lean my head against his chest, savorign his warmth."
    show maxime casual_cu embarrassed_cu
    "He doesn't move, cradling me gently, and we stay like that, the ocean breeze ruffling our hair."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    mcmax "Soooo... are we going to talk about that kiss?"
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    "Maxime chuckles nervously, his laugh is deep, pleasant rumble his chest."
    mx "Yes, I definitely want to talk about it. It was a great kiss."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I smile from where I'm snuggled against him, inwardly cheering."
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    mx "Is it alright if we had the-kiss-talk tomorrow? I {i}do{/i} want to talk about 'us', I just..."
    show maxime casual_cu sad_cu
    mx "I don't want my words to get muddled, not when I've got so much I want to say. And right now, I may not say things right."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "He hesitates, and I look up at him, smiling gently."
    mcmax "That's fine. Tomorrow then, it's a date."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "Maxime grins back, his face reflecting the moonlight."
    mx "Thanks, superstar."
    mx "I can walk you home? It's been quite a day, between you winning a tournament and then confronting a 'mad scientist'."
    hide maxime
    "He offers his hand, and I gladly entwine my fingers with his."

    scene bg msc_boardwalk_night_lights_people at bg with wiperightdissolve
    show mscmc jacket_hairdown smile at left1
    show maxime casual embarrassed behind mscmc at right1plus
    "As we make our way back to the boardwalk, we keep our hands clasped, gently swinging our arms."
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(This is wonderful! This feels like we're a couple?!!)"
    show mscmc jacket_hairdown smile at left1
    show maxime casual smirk behind mscmc at right1plus
    mx "You know, my dad used to buy me ice cream when I won surfing competitions."
    mx "You want something?"
    show mscmc jacket_hairdown grin
    "I turn to Maxime eagerly, this is the first time he's ever mentioned his family."
    show maxime casual smile
    mcmax "How about you tell me about your dad? He sounds like a cool guy!"
    mcmax "I didn't realize he encouraged your surfing."
    show maxime casual surprised
    "Maxime raises his eyebrows, feigning surprise."
    mx "What, you're turning down my offer of free food?"
    show mscmc jacket_hairdown smile
    show maxime casual smile
    mcmax "I didn't say that. You can buy me a big ol' cheeseburger, {i}and{/i} tell me about surfing with your dad."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "He grins, musing on it."
    mx "Alright, that sounds like a deal. So, for a job well done, you want a cheeseburger and tales of my childhood?"

    hide maxime
    $menuhideborder = True
    menu maximee12c3:
        "A. Cheeseburgers and anecdotes!" (paidchoice="paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left1
            show maxime casual smile behind mscmc at right1plus
            mcmax "Yep, cheeseburgers and anecdotes, let's go!"
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime chuckles and goes to the boardwalk diner, buying us each a cheeseburger with all the fixings."
            hide maxime
            "We find a bench facing the ocean and settile down, carefully unwrapping our deliciously gooey burgers."
            show mscmc jacket_hairdown grin at left1plus
            show maxime casual smile behind mscmc at right1plus
            mx "It's hard to find a perfect burger, butr these come pretty damn close."
            show mscmc jacket_hairdown smile
            show maxime casual basic
            "I giggle and glance over to find him studying his burger with the eye of a chef—while seeming to stall for time."
            hide maxime
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Aw, that's right. He's always shy when talking about himself.)"
            show mscmc jacket_hairdown smile at left1plus
            show maxime casual embarrassed behind mscmc at right1plus
            "I nudge his foot gently under the bench."
            show maxime casual basic
            mcmax "So, your dad...he's a surfer?"
            show maxime casual smile
            "Maxime smiles fondly, his gaze drifting away into a memory."
            show mscmc jacket_hairdown grin
            mx "Yeah, he was a force to be reckoned with back in the day."
            show mscmc jacket_hairdown smile
            mx "Next time we're at the studio, I'll see if I have any old pictures of him. He had a big 80s surfing energy—the hair, the shorts..."
            show mscmc jacket_hairdown grin
            mcmax "Oh, I love that."
            "He grins, chewing a bite of his burger."
            show maxime casual basic
            show mscmc jacket_hairdown smile
            mx "He's human, to be clear—just a really good waterman. My mother's the mer of the family."
            "I nod, contemplating this."
            mcmax "When you were growing up, was your house in the ocean or on land?"
            mx "Both, I lived on-land with my dad for the most part. Mom was pretty busy with work in Maritas."
            mx "I'd visit her in the bay for the summer and go to mer camps and things like that."
            "I sense a certain hesitance surrounding his mom, and develop an image of a high-powered career woman."
            hide maxime
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(Which doesn't exactly jive with his dad, the laid-back 80s surfer...)"
            show mscmc jacket_hairdown surprised at left1plus
            show maxime casual basic behind mscmc at right1plus
            mx "They divorced when I was still a baby, so... We didn't all live together."
            show mscmc jacket_hairdown sad
            mcmax "Oh, I'm sorry."
            show maxime casual sad
            "Maxime just shrugs."
            show mscmc jacket_hairdown smile
            show maxime casual basic
            mx "It's okay, I was still a happy little kid. My dad and I get along well."
            show mscmc jacket_hairdown grin
            show maxime casual smile
            mx "He was so proud when I picked up surfing, and he always took me to competitions and camps, and stuff."
            show mscmc jacket_hairdown smile
            mx "He's a high school gym teacher."
            show mscmc jacket_hairdown grin
            mcmax "From one athlete to another, that is awesome."
            "I grin, setting Maxime further at ease."
            "He seems to be slowly relaxing, almost relieved to finally be mulling over things left unsaid."
            show mscmc jacket_hairdown smile
            mx "My mom works for a big company in Maritas, she doesn't really get why we're so passionate about sports."
            show maxime casual basic
            mx "I think she was hoping I'd do something more academic, though she was happy when I joined the bureau."
            show mscmc jacket_hairdown basic
            show maxime casual angry
            "He grimaces, and I'm reminded of his own distate whenever he mentions his spywork."
            hide maxime
            show mscmc jacket_hairdown_cu sad_cu at maxime_cu
            "(That's got to be hard. He wants to make his mom happy, but he doesn't like what he's doing, even if she does.)"
            show mscmc jacket_hairdown smile at left1plus:
                xpos stagepos[1]-140
                ease 0.4 xpos stagepos[1]-100
            show maxime casual basic behind mscmc at right1plus
            pause 0.4
            "I lean against him, our shoulders brushing, and speak softly."
            mcmax "How did your parents meet?"
            show mscmc jacket_hairdown grin
            show maxime casual embarrassed
            mcmax "I have no idea how a human and mer would meet, except to accidentally stumble on each other in a secret cove."
            show maxime casual smile
            "I wink, and Maxime breaks out in a laugh, laying his arm on the bench so it's draped over my shoulder."
            mx "My parents never told me a dramatic story like that. We might be two of a kind, you and I."
            show mscmc jacket_hairdown smile
            show maxime casual basic
            mx "They met when my mom was going through a rebellious phase. She wanted to spend more time on land, but it didn't last."
            hide mscmc
            show maxime casual_cu basic_cu at maxime_cu
            mx "I guess she was curious about the surface-world, and a good-looking human caught her eye."
            show maxime casual_cu smirk_cu
            "He looks at me, arching his eyebrow roguishly, and I dissolve into giggles."
            show maxime casual_cu smile_cu
            "Maxime laughs with me, then reaches out, briefly stroking my cheek with his finger."
            mx "In all seriousness, it's nice to have people who understand what it's like to have one foot in the ocean and the other on land."
            show maxime casual_cu basic_cu
            mx "My mother doesn't realize how strange it was for me, growing up."
            mx "That might be why we've never been as close—she doesn't really know how to talk to me."
            mx "I know you're not half-mer the way Dawn and I are, but..."
            show maxime casual_cu embarrassed_cu
            mx "You're such a talented waterwoman, and you've been so accepting of my life."
            mx "{i}You{/i} get me."
            "I'm tempted to kiss him again, but restrain myself, settling for leaning on his shoulder and meeting his eyes."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(We still haven't talked about our kiss. What did it mean?)"
            mcmax "You know you can always talk to me."
            hide mscmc
            show maxime casual_cu embarrassed_cu at maxime_cu
            mx "I do know that."
            show maxime casual_cu basic_cu
            "We hold each other's gazes for a moment, then Maixme sighs, reluctantly clearing up our burger wrappers."
            mx "I'll walk you home."
            hide maxime
        "B. Actually, I have food at home.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            mcmax "Got pasta in the fridge."
            hide mscmc

    play music mscmaxime
    show mscmc jacket_hairdown embarrassed at left1
    show maxime casual embarrassed behind mscmc at right1plus
    "When we reach the alley behind the shop that has the door to my room, our hands are still clasped."
    show mscmc jacket_hairdown smile:
        ease 0.4 xpos stagepos[1]-180
    show maxime casual smirk:
        ease 0.4 xpos stagepos[1]+180
    "We're both reluctant to separate."
    mx "So..."
    show maxime casual embarrassed
    mcmax "So..."
    show mscmc jacket_hairdown embarrassed
    show maxime casual smile
    "I giggle, and Maxime smiles shyly at the ground before looking back up into my eyes."
    show mscmc jacket_hairdown grin
    show maxime casual embarrassed
    mcmax "I don't want to say goodbye! Is that cheesy?"
    show mscmc jacket_hairdown embarrassed
    mx "If it is, then I'm just as cheesy."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I, for one, wouldn't mind if he came in with me and stayed the night.)"

    hide mscmc
    play music mscromance
    scene bg msc_maxime_s1_ei4 at bg with fade:
        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    mcmax "So, I guess that means I'll see you tomorrow?"
    "I raise my hand, threading my fingers through his and taking a hopeful step towards him, like the first move of a dance."
    "(And if he wants to close the gap and start kissing me, well...!)"
    "Maxime pulls me nearer, playing with my fingers in his."
    mx "Bright and early—though I'll try not to wake you up at the crack of dawn. But let's get breakfast together."
    mcmax "You'd better wake me up as soon as you're awake! Hell, you can come pull me out of bed."

    scene bg msc_boardwalk_night_lights_people at bg with fade
    show maxime casual_cu embarrassed_cu at maxime_cu
    "Maxime flushes at this, then seems to steal his courage."
    show maxime casual_cu smile_cu
    "He bends down, taking my jaw gently in his hands, and kisses my forehead."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(He's so sweet—so many butterflies flying around my stomach and in my heart!)"
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    mx "Tomorrow, then."
    show mscmc jacket_hairdown smile at left1:
        xpos stagepos[1]-100
        ease 0.4 xpos stagepos[1]-180
    show maxime casual basic behind mscmc at right1plus:
        xpos stagepos[1]+140
        ease 0.4 xpos stagepos[1]+220
    "We finally pull apart with great reluctance, and I put my key in the door as Maxime walks down the steps."
    show mscmc jacket_hairdown embarrassed
    show maxime casual embarrassed
    "I glance over my shoulder just as he pauses in the street to look back at me, and we meet each other's eyes."
    show mscmc jacket_hairdown grin
    mcmax "Goodnight, Maxime."
    show maxime casual smile
    mx "Goodnight, [genericfn]."

    hide mscmc
    hide maxime
    scene bg msc_mchomeentryway_lightsoff at bg with wiperightdissolve
    # This should really be a door closing sound but eh
    play sound "audio/sfx/79_door open.mp3"
    show mscmc jacket_hairdown embarrassed at centre
    "As soon as I've closed the door behind me, I lean against it, letting myself dissolve into blushes and happy giggles."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(It's really happening! Maxime likes me and I like him!)"
    show mscmc jacket_hairdown_cu grin_cu
    "(Not to mention winning the tournament—everything is coming up [genericfn]!)"
    show mscmc jacket_hairdown grin at centre:
        ease 0.4 xoffset 60
    "I catch my breath, then fumble for the light switch so I'm not standing in the dark."

    hide mscmc
    play music mscantagonist
    show bg msc_mchomeentryway_lightsoff at bg:
        ease 0.2 xoffset -10
        ease 0.2 xoffset 0
        repeat
    "Just as my hand touches the wall, something grabs me from behind, yanking my head back."
    show bg msc_mchomeentryway_lightsoff at bg
    "Before I can scream, I feel a cloth smothered in chemicals forced my mouth, muffling me."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Oh hell no!)"
    hide mscmc
    "I struggle against the strong arms that are pinning me, using all my strength to lash out..."
    "But the chloroform is fast-acting, and my limbs start to grow heavy."
    show smoke_effect
    "My mind slides into a fog as my body slumps to the floor and my eyes close."
    scene black at bg with eye_shut

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
