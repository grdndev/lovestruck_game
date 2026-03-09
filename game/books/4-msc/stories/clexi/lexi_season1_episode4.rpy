label lexi_season1_episode4:

    $tbc = False
    scene bg msc_mcs_vision at bg with dissolve
    play music mscmcvisions

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show lexi casual_cu surprised_cu at lexi_cu:
        alpha 0.5
    lx "Come back to me!"

    lx "[genericfn]!"
    hide lexi
    "Bubbles float up in the water around me as I float weightlessly."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Don't worry, Lexi. Everything is fine, I'm floating and relaxing. It's really warm, you should join me.)"
    hide mscmc
    "I move, but just then I feel a weight in my hand that was absent before..."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Hmm? What's this?)"
    hide mscmc
    show magi_tech_egg at bg
    "(The mer orb from the museum?)"
    hide magi_tech_egg
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Why am I holding this?)"
    hide mscmc
    show magi_tech_egg at bg
    "I hold the orb up in front of me, following the intricate red, blue, and yellow patterns upon its surface."

    "I'm enthralled, I'm getting lost in these patterns and a strange sense of nostalgia tickles the back of my mind."
    hide magi_tech_egg
    show lexi casual_cu angry_cu at lexi_cu
    lx "Hey! I need you to open your eyes and let me know you're okay!"
    scene bg msc_bg_001 at bg with eye_open_slow
    stop music fadeout 1.0
    play music mscsadtimes
    "I blink rapidly as light floods my vision and blinds me."
    scene bg msc_mc_bedroom_night_lights at bg with eye_open
    "The first thing I notice is that I am back in my room, and my hands are warm. I look down and realize Lexi is holding my hands in hers."
    show lexi casual_cu surprised_cu at lexi_cu
    lx "Are you okay? What happened?"
    show lexi casual_cu sad_cu
    "Lexi's hands are kind of small but her fingers feel very strong and sure around mine, like an anchor."
    show lexi casual_cu basic_cu
    "I try to smile reassuringly at Lexi as I find my voice, but her brow remains furrowed as she regards me intensely."
    show lexi casual_cu sad_cu
    lx "Thank god you came back."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(If I wasn't just magically transported underwater, and was actually still here just now, what did Lexi see?)"
    hide mscmc
    show mscmc jacket_hairdown smile at left2
    show lexi casual smile at centre:
        easein 0.4 xoffset +150
    "She lets my hands go and sits back on my bed, covering her concern with a small smile."
    show lexi casual basic
    lx "What happened?"
    show mscmc jacket_hairdown surprised
    show lexi casual surprised
    mclexi "I'm not sure. I've never experienced, nothing like that has ever-"
    show mscmc jacket_hairdown sleep
    show lexi casual basic
    "I take a deep breath and try to collect my thoughts."
    show mscmc jacket_hairdown basic
    mclexi "That's never happened to me before."
    hide lexi
    hide mscmc
    $menuhideborder = True
    menu lexis1e4c1:
        "A. I thought I was underwater.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show lexi casual surprised at right1
            mclexi "I was underwater all of a sudden... and very calm. I didn’t have a care in the world."
            show mscmc jacket_hairdown sad
            "Lexi definitely seems surprised. It’s surprising, what the hell does it mean?"
            show mscmc jacket_hairdown basic
            show lexi casual sad
            lx "You seemed calm, you kind of fainted all of a sudden. Can you describe it more?"

        "B. Could I have just zoned out really hard?":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left2
            show lexi casual surprised at right1
            mclexi "I zoned out, but there was more to it than that. It was like I was transported somewhere else entirely."
            show lexi casual basic
            "Lexi cocks her eyebrow and it’s like I can practically see the wheel’s turning in her brain."
            show mscmc jacket_hairdown basic
            lx "Transported? Like where?"


        "C. What did I looked like during... that?":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show lexi casual surprised at right1
            mclexi "That's never happened to me before."

            mclexi "Did I look weird while I was... away?"
            show mscmc jacket_hairdown embarrassed
            show lexi casual smile
            "Lexi chuckles."
            show mscmc jacket_hairdown surprised
            show lexi casual basic
            lx "You looked like you just randomly fell asleep."
            show lexi casual sad
            lx "Your eyes drifted closed and your breathing slowed... It was kind of scary."

    show mscmc jacket_hairdown basic
    show lexi casual basic
    mclexi "One minute we were talking about the orb, and the next minute I was at the bottom of the ocean."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(It was just so random.)"
    show mscmc jacket_hairdown_cu sad_cu
    "(It felt real, like I was actually underwater, actually breathing underwater.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2
    show lexi casual smile at right1
    lx "So a full-on vision. That's..."
    show mscmc jacket_hairdown sad
    show lexi casual basic
    "Lexi bites her bottom lip, a worried look briefly flashing across her eyes, before she stands."
    show mscmc jacket_hairdown surprised
    show lexi casual smile
    "She grabs my half-full water bottle from the bedside table."
    show lexi casual sleep:
        easein 0.4 xoffset -30
    lx "Drink water. Maybe this is a weird part of your hangover?"
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(I've never had a hangover that made me hallucinate.)"
    hide mscmc
    show mscmc jacket_hairdown sleep at left2
    show lexi casual basic at right1:
        xoffset -30
    "I take a sip of water, but I can tell Lexi is still running through and vetting possible explanations in her mind."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Maybe there is no meaning and it was just a weird fluke?)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2
    show lexi casual surprised at right1:
        xoffset -30
    mclexi "Oh! I had the mer orb in my hand! In my vision!"
    stop music fadeout 1.0
    play music mscmctheme
    show lexi casual bigsmile
    "Lexi's green eyes widen with surprise, shining with excitement."

    lx "Wait, what, really?!"

    mclexi "Yeah! I was underwater, looking up at the surface. I could breathe fine and I was holding that freaking egg thing."
    show mscmc jacket_hairdown sad
    mclexi "Is the orb magic? Is it doing this to me?"
    show mscmc jacket_hairdown grin
    lx "I've heard of magic giving people visions before, but I just don't know enough! Gah!"

    "She cries out in excited frustration and tussles her hair with her hands. Her energy is infectious and my heart pounds in my chest."
    show mscmc jacket_hairdown embarrassed
    mclexi "Any of the books on your UV we could check?"
    show mscmc jacket_hairdown grin
    lx "Maybe. That's not a bad idea..."
    show mscmc jacket_hairdown embarrassed
    show lexi casual basic:
        easein 0.4 xoffset +40
    "Lexi lets herself fall back from standing and flops onto the pillows at the head of my bed."
    show lexi casual smile
    "Her dark green hair spreads out over them in soft curls and she stares pensively at the ceiling."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I know her thoughts are running a mile a minute, if anyone can figure this out it's her.)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at left2
    show lexi casual sleep at right1
    "Lexi closes her eyes and lets out a long sigh."
    show mscmc jacket_hairdown smile
    show lexi casual bigsmile
    lx "I just can't think of anything that would explain it. Maybe if I..."
    show mscmc jacket_hairdown basic
    "She rolls off the bed and stretches her arms above her head."
    show mscmc jacket_hairdown embarrassed
    show lexi casual angry
    "As she leans back into the stretch, her long green hair curtains behind her and I can see her toned muscles flexing under her tanned skin."
    show mscmc jacket_hairdown surprised
    show lexi
    lx "Let me go see if I can't dig up some more information. Meet me tomorrow?"
    show mscmc jacket_hairdown basic
    show lexi casual bigsmile
    "I playfully salute Lexi, while putting on an exaggeratedly serious expression. I don't want her to go though."
    show mscmc jacket_hairdown grin
    show lexi casual embarrassed
    mclexi "Aye aye captain!"
    scene bg msc_museum_displays_day at bg with fade
    stop music fadeout 1.0
    play music suspense
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Hannah's bound to be here somewhere. I need to talk to her and tell her that Lexi isn't who Hannah thinks she is.)"
    hide mscmc
    show mscmc jacket_hairdown basic at centre
    "I wander the halls of the museum, making my way through familiar exhibits."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Lexi is helping me and I want to help Lexi. I think I can make Hannah see that she's wrong about Lexi.)"
    show mscmc jacket_hairdown_cu basic_cu
    "(I need to try. I want Hannah to leave Lexi alone.)"
    show mscmc jacket_hairdown_cu sleep_cu
    "(I'll explain Lexi doesn't want the orb...)"
    hide mscmc
    show mscmc jacket_hairdown basic at centre
    "I shake my head."
    stop music fadeout 1.0
    play music mscantagonist
    hide mscmc
    show hannah casual basic at centre
    "I round a corner into the orb's exhibit room and see Hannah gazing pensively at a large hung portrait on the far wall. "
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I've found Hannah but my attention is pulled to the orb, it looks just like it did in my vision...)"
    hide mscmc
    show mscmc jacket_hairdown smile at centre
    "I laugh internally as I imagine how museum staff would react if I just casually asked if I could hold this precious artifact."
    hide mscmc
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Wait, I need to focus on getting Hannah off Lexi's back.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left2
    show hannah casual sad at right3
    mclexi "Ahem."
    show hannah casual angry
    "I clear my throat loudly and approach Hannah slowly, trying not to startle her."
    show hannah casual basic
    mclexi "Can we talk?"
    show hannah casual smile
    "Hannah tenses briefly when I address her but composes herself quickly and flashes me a smile."
    show hannah casual basic
    hj "About what?"
    show hannah casual angry
    "Her smile drops from her face, challenging me to address the elephant in the exhibit room."
    show hannah casual sleep
    mclexi "I want to talk to you about Lexi."

    hj "Is there anything else to say? I've warned you, you won't listen. We all have to live with the consequences of our actions."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(That could totally, maybe, have just been a threat. Oh boy.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left2
    show hannah casual angry at right2
    hj "Let me guess, you're here to defend her. You're going to tell me this is all a misunderstanding?"
    hide mscmc
    hide hannah
    $menuhideborder = True
    menu lexis1e4c2:
        "A. It is a misunderstanding.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left2
            show hannah casual basic at right2
            mclexi "Lexi isn’t here to stir up trouble."
            show mscmc jacket_hairdown basic
            show hannah casual sad
            "Hannah purses her lips and there’s a vexed look in her eyes."
            show mscmc jacket_hairdown angry
            show hannah casual smile
            hj "Do you really believe that?! There must be no limit to your naivete."

            mclexi "Please, just listen."


        "B. Can't you leave her alone?":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left2
            show hannah casual angry at right2
            mclexi "I get where you're coming from. The job you two did together, it ended badly for you. But that's the past."
            show mscmc jacket_hairdown basic
            "Hannah's lips contort into a sneer."
            show mscmc jacket_hairdown surprised
            hj "Why don't you have five years of your life stolen, and then come tell me if you forgive the person who stole those years."

            "She clenches her fists at her sides and her knuckles go white."



        "C. Maybe this was pointless.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(She already seems upset. I don’t think she’ll listen to me.)"
            show mscmc jacket_hairdown basic at left2
            show hannah casual basic at right2
            mclexi "I just want to talk."
            show hannah casual angry
            "Hannah crosses her arms as she aggressively stares down a painting on the wall."
            show hannah casual smile
            hj "You keep defending this fish-girl, but you don’t even know who she really is."
    show mscmc jacket_hairdown angry at left2
    show hannah casual basic at right2
    mclexi "Lexi doesn't want the orb. So she isn't trying to set me up and ditch me."
    show hannah casual smile
    hj "You actually believe that, don't you?"
    hide hannah
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What happened between them that she's this convinced of Lexi's shittiness? Is it really just the jail time?)"
    hide mscmc
    show mscmc jacket_hairdown basic at left2
    show hannah casual sad at right2
    "Hannah shakes her head and looks at me, her eyes gleaming with disingenuous sympathy."
    show mscmc jacket_hairdown surprised
    hj "I feel sorry for you. I've tried my best to save you from a bad person."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Well, I definitely shouldn't listen to Hannah... But that still doesn't mean that I can trust Lexi...)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left2
    show hannah casual sad at right2, out_right
    "Hannah turns on her heel and leaves."
    stop music fadeout 1.0
    play music mscmagicartifact
    show mscmc jacket_hairdown basic:
        easein 0.4 xoffset +200
    "I walk over to the orb that seems to be somehow at the center of all this, as I ponder what just went down."
    hide mscmc
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(The answers to everything lie with this ornamentary looking antique.)"
    show mscmc jacket_hairdown_cu sad_cu
    "(Well, maybe not the answer to what Lexi and I are doing in terms of each other's affections, but still, a lot of answers.)"
    hide mscmc
    show mscmc jacket_hairdown sleep at centre
    "My thoughts seem to taper out as a sense of calm washes over me, and the museum begins to blur around me."
    show mscmc jacket_hairdown surprised
    "The feeling only lasts for a few seconds, but it leaves goosebumps on my arms even as my surroundings come back into focus."
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Did the orb just do that to me?! I need to get out of here before I faint or have a vision.)"

    "(I hope Lexi found some kind of explanation in her research.)"
    hide mscmc
    show mscmc jacket_hairdown smile at centre
    "I head out, but I can't help looking back at the orb one last time before I leave the room."
    scene bg msc_beach_bar_day at bg with wiperight
    stop music fadeout 1.0
    play music mscbeach
    show mscmc jacket_hairdown grin at left2
    show lexi casual smile at right2
    lx "I love breakfast. It's literally the best meal."

    mclexi "Lexi... It's almost three in the afternoon. It's definitely way past breakfast."
    stop music fadeout 1.0
    play music mscromance
    show mscmc jacket_hairdown embarrassed
    show lexi casual smile:
        easein 0.4 xoffset -150
    "Lexi shrugs nonchalantly, but suddenly leans in close and puts her hand on the back of my barstool."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Her hand positioning means that her arm is blocking me in close to her, as if she's signaling that I'm hers...)"
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "The side of her mouth raises in an amused smirk and without a word she brings her other hand to my cheek."

    "The palm of her hand against my cheek is soft like silk."

    "She gently brushes the side of my mouth with her thumb as I hold my breath in awe of her."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "My chest tightens in anticipation of whatever her next move will be as she pins me in place with her eyes..."
    hide mscmc
    show mscmc jacket_hairdown surprised at left1 behind lexi
    show lexi casual smile at right1
    "...but the feeling quickly fades as she sits back and grins, showing me the smidge of ketchup on her thumb."
    show mscmc jacket_hairdown embarrassed
    lx "You had something on your face."

    "My cheeks flush with embarrassment as I try to force my heart rate to slow."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Ketchup?! Here I am getting excited because I think she's going to kiss me and she's just wiping my face!?)"
    hide mscmc
    show mscmc jacket_hairdown angry at left1 behind lexi
    show lexi casual bigsmile at right1
    "I look down at the plate of fries and ketchup in front of me."
    show mscmc jacket_hairdown smile
    show lexi casual smile
    mclexi "Thanks. I didn't even notice it."
    show mscmc jacket_hairdown embarrassed
    lx "Don't be embarrassed. It was a cute look on you."

    "My cheeks grow hot as I nod stiffly and rack my brain for something to change the subject to."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She said I looked cute! Oh, But I do still have to tell her about...)"
    show mscmc jacket_hairdown basic at left1 behind lexi
    show lexi casual smile at right1
    mclexi "So, I went to the museum this morning, and checked out the orb."
    show mscmc jacket_hairdown sleep
    show lexi casual basic
    mclexi "While I was there, the strangest thing happened..."
    hide mscmc
    hide lexi
    "I recount the feeling that came over me when I was near the orb that morning..."

    "...but omit the part about talking to Hannah. That conversation did not go well."
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Besides, Lexi still hasn't told me why she's back in town. If she's keeping things to herself, I can too.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left1 behind lexi
    show lexi casual sad at right1
    lx "I still don't know why a mer artifact would have such an effect on a human."
    show lexi casual smile
    "She looks me up and down, squinting her eyes and furrowing her brow, as if she's looking for something she may have missed before."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's undressing me with her eyes!)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at left1 behind lexi
    show lexi casual smile at right1
    lx "The whole situation is weird. But don't worry, we'll figure it out. Together."
    show mscmc jacket_hairdown grin
    "My heart jumps a little at the way she says 'together.'"
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She makes it sound so natural. Like the two of us can do anything.)"
    hide mscmc
    show mscmc jacket_hairdown grin at left1 behind lexi
    show lexi casual embarrassed at right1
    lx "Oh! I love this song!"
    stop music fadeout 1.0
    play music mscpassionateromance
    show mscmc jacket_hairdown smile
    "A slow and sultry song has started to play on the radio. Lexi sways on her barstool in time with the music."
    show mscmc jacket_hairdown smile
    mclexi "You know this song?"
    show mscmc jacket_hairdown embarrassed
    show lexi casual sleep
    "Lexi doesn't say anything but closes her eyes, feeling the rhythm..."
    show lexi casual sleep:
        easein 0.4 xoffset +60
        easein 0.4 xoffset -60
    "...and starts to lose herself in the music as she sways her body and moves her hands in fluid motions."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(This song's passionate vibe suits her devil may care attitude.)"

    "(We're the only one's at the bar, no one's walked by in ages. It feels like we're in our own world.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left1 behind lexi
    show lexi casual sleep at right1
    "I glance around to see if anyone is walking over the horizon or headed this way..."
    hide lexi
    hide mscmc
    "But the beach is deserted and Jerry is busy in the back grilling, not minding us at all."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(It's just us right now. Us, in this moment together.)"
    show mscmc jacket_hairdown surprised at left1 behind lexi
    show lexi casual smile at right1
    "Lexi smiles gleefully as she slips off her bar stool and rolls her hips while the rich melody fills the air."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's letting her body really feel the music, while still being in control and intentionally charming the hell out of me.)"

    "(It's like she's an enchantress and I am enchanted.)"
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "Lexi peeks up at me through a curtain of hair that has fallen over her face as she slinks over to me."

    lx "Want to see more?"

    "She leans down until her lips are almost touching my ear and a tingle shoots through my body as she opens her mouth to whisper."
    show lexi casual_cu smile_cu
    lx "Should I keep dancing for you? No one else is here... It'll be for your eyes only..."
    hide lexi
    $menuhideborder = True
    menu lexis1e4c3:
        "A. Yes, Lexi, keep dancing for me!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown embarrassed at left2
            show lexi casual embarrassed at right2
            mclexi "Keep going..."
            show lexi casual embarrassed:
                easein 0.6 xoffset +100
            "Lexi steps around the back of my barstool, and runs her hands over my shoulder as she continues to dance."

            "She tilts her head slightly as she looks at me and runs her hands through her hair."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I don’t think I’ve ever seen anyone so picturesque. She looks like she should be the cover art for whatever song is playing.)"
            show mscmc jacket_hairdown_cu embarrassed_cu
            "(The way her hair is so silky and shines in the sunlight, the way her hips slope and become her thighs...)"
            hide mscmc
            show mscmc jacket_hairdown embarrassed at left2
            show lexi casual smile at right2:
                xoffset +100
                easein 0.6 xoffset -100
            "Lexi gives me a sly grin and starts to move her hips to the beat of the music while slowly inching even closer."
            hide lexi
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "She presses her body gently against me as she continues to dance and raises her slender arms above her head."

            "Her eyes are slightly closed, but there’s an intensity to them that takes my breath away, and I feel a rush of excitement."
            show lexi casual_cu embarrassed_cu
            "A yearning tension fills the air, neither one of us breaking eye contact as Lexi brings her arms down and runs her hands over her body."

            "She leans against me as her body moves to the song and my hands find their way to her hips."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(It’s like we’re the only two people in the world.)"

            "(She never seems to care what other people think. She just does whatever she wants, whatever feels good...)"
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "My eyes follow Lexi’s fingers as they trail across her collarbone, down to her chest, then she bites her bottom lip."
            show lexi casual_cu smile_cu
            "She arches her back and throws back her head as the music softens and her slightly sweaty skin glistens in the hot sunlight."
            show lexi casual_cu embarrassed_cu
            "But my eyes don’t leave her fingers."

            "Fingers that she drags down further on a path through the middle of her torso, tracing a path to her lower abdomen."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her elegance as she transitions between moves devastates me with every passing second...)"

            "(I am such a goner. Oh Lexi, what are you doing to my heart?)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "She leans her face close to mine, looking at me with hooded eyes that make my heart pound loudly in my ears..."
            show lexi casual_cu embarrassed_cu
            "There’s a tingling sensation all over my body as I watch her and feel her against me."

            "She runs her fingers across my forearm as she dances and my skin becomes covered in goosebumps."
            show lexi casual_cu bigsmile_cu
            "I catch her hand in mine and pull her close."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I never want to let her go. I never want her to let me go.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "She snaps her hand away and looks coquettishly at me."

            "Then, runs her hands slowly down my thighs as she shakes her hips slowly and intentionally."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Oh my god, she... she is a magical creature!)"
            show mscmc jacket_hairdown_cu sleep_cu
            "(A mermaid is moving slowly and sensually for me in a beach bar during broad daylight! I don’t even know who I am anymore.)"
            hide mscmc
            "As the music continues its rhythmic melody, Lexi winds her way behind me and places her arms over my shoulders."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(I want to do something smooth right now but I am paralyzed, why is she so hot?)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi leans forward and places her lips next to my ear, I can feel her hot breath on my neck as she tilts her head."

            "I reach my arm back and place my hand on her soft cheek as she whispers into my neck and a sea of green curls cloud my vision."
            show lexi casual_cu embarrassed_cu
            lx "I like the way you look at me when you’re thinking dirty thoughts about me."
            show lexi casual_cu smile_cu
            "I stop breathing for a second as she laughs, arching her back and pressing the length of her torso and hips against my back."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her boldness makes me want to be bold.)"
            hide mscmc
            show mscmc jacket_hairdown grin at left1 behind lexi
            show lexi casual embarrassed at right1
            "I grab her wrist lightly and stand up from my stool."
            show mscmc jacket_hairdown embarrassed
            "I stand against the bar and pull her to me, resting my hands on her hips. She inhales sharply and looks up at me, impressed."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(This is heaven.)"
            hide mscmc
            "Lexi grins in delight at my response and squirms closer to me so I can clasp my hands behind her back and hold her against me."
            show lexi casual_cu smile_cu at lexi_cu
            lx "I love dancing like this..."
            show lexi casual_cu embarrassed_cu
            "I stare down at her, we’re so close, I can see every darkened, upturned lash and the different shades of pink swirling across her cheeks."
            show lexi casual_cu smile_cu
            lx "I love the way certain humans treat music and dance as an expression of their sensuality… and a way to express their desire."
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "I open my mouth, no idea what I’m about to say because I’m too awestruck by her, but..."
            hide mscmc
            "Before I can even start to say something, Lexi puts a finger to my lips and I immediately lose any intention of speaking."
            show lexi casual_cu embarrassed_cu at lexi_cu
            lx "I think you’re the best."
            show lexi casual_cu smile_cu
            "She moves her finger and nods at me."

            "And I understand she means that I can speak now as she grins saucily, seeing if I’ll play her game."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "You’re pretty great too."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi tries to keep her face serious but she very obviously is pleased and wants to smile."

            "Her eyes narrow mischievously at me and she brings her lips mere inches from mine before stopping."
            show lexi casual_cu embarrassed_cu at lexi_cu
            "She brushes the tip of her nose against mine, and looks up at me as her eyes sparkle."
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I would sell my soul in a second if she asked me to.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "I hope you liked your dance."
            hide lexi
        "B. Brain overload.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(It's the middle of the day! She's obviously about to turn the heat up in here, and not in a temperature way.)"

            "(Of course I want to see that, but what if someone walked by?! What if Jerry came back out to the front?)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left1 behind lexi
            show lexi casual smile at right1
            mclexi "I, um, just for me, yes, er, I mean no, there's..."
            show lexi casual embarrassed
            "I stumble to get an answer out until Lexi giggles, and then looks sheepish."
            show mscmc jacket_hairdown embarrassed
            lx "I think I broke you."
            show lexi casual smile
            "I turn my eyes away in embarrassment..."
            hide lexi
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "But Lexi's finger comes out of nowhere and softly boops the tip of my nose."
            hide lexi
    stop music fadeout 1.0
    play music mscbeach
    show jerry casual smile at centre, step_in
    "Lexi jumps into her seat, just as Jerry makes his way back from the grill on the other side of the beach bar."

    jr "What'd I miss?"
    show lexi casual bigsmile at left3
    show jerry casual smile at right3
    "Lexi beams at Jerry with a mischievous glint in her eye, while I experience too many emotions to compute all at once."

    lx "Nothing much, standard breakfast stuff."
    hide lexi
    hide jerry
    show lexi casual_cu smile_cu at lexi_cu
    "She winks at me as she picks up her coffee and takes a sip."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I should say something, I can't just sit here blushing forever.)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3
    show jerry casual smile at right3
    mclexi "Yep, just finishing up lunch!"
    hide mscmc
    show lexi casual basic at left3
    "Lexi clears her throat."
    show lexi casual smile
    lx "Breakfast."
    stop music fadeout 1.0
    play music msctense
    hide lexi
    hide jerry
    show lexi casual surprised at centre
    $sidecharone = "Wher do I know that voice? Oh, right"

    sid1 "I knew I'd run into you eventually."

    "Suddenly, everything about the mood at the bar changes as the sound of clipped angry words fly through the air at Lexi."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Oh. Hannah and Lexi in the same place, at the same time. Oh no.)"
    hide mscmc
    show hannah casual angry at centre
    "Hannah must've seen us from the beach path, but she is now definitely storming right at us."
    hide hannah
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(Jerry, I am so sorry if I am about to be in a bar fight at your bar.)"
    hide mscmc
    show lexi casual angry at centre
    "I look over at Lexi, and her top lip is lifted ever so slightly at one corner in a, surprisingly delicate, sneer of annoyance."
    show lexi casual angry at left3
    show hannah casual angry at right3
    "An aura of seething rage radiates off Hannah as she halts sharply and straightens herself to her full height."
    hide lexi
    hide hannah
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(I don't even know how to try to de-escalate this situation right now, so I guess I'll wait and see how things play out for now.)"
    hide mscmc
    show lexi casual basic at left3
    show hannah casual angry at right3
    "Lexi leans back on her bar stool and sighs, before acknowledging the tense woman glaring at her from the end of the bar."

    lx "Hannah."
    show hannah casual sleep
    "Hannah's eye twitches, but then she takes a deep breath and speaks in a voice ringing with conviction and grounded confidence."
    hide lexi
    hide hannah
    show hannah casual_cu basic_cu at hannah_cu
    hj "Lexi Sweetwater, it's been a long time, but mark my words, I'm going to end you."
    $tobecontinued()
    scene msc_tbc at bg with fade
    pause
    $ resets()
