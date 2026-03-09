label lexi_season1_episode1:

    $tbc = False
    scene bg msc_museum_displays_day at bg with dissolve
    play music mscmctheme

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I've been coming to the museum a lot lately... I guess Lexi rubbed off on me.)"

    "I think back to the whirlwind adventure that I was in six months ago with her, Lexi, an actual mermaid treasure hunter."

    "A grin creeps onto my face as I think about the last night I saw her, six months ago."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "With a sigh, I pull myself out of my thoughts and gaze at the ornate egg-shaped artifact in the glass display I came to see."
    hide mscmc
    show magi_tech_egg:
        xpos 360
        ypos 100
    "I came to the museum for the first time on a whim shortly after Lexi disappeared."
    hide magi_tech_egg
    show mscmc jacket_hairdown basic at centre
    "That was the first time I had been drawn to this antique orb."
    show mscmc jacket_hairdown smile
    "Of all the exhibits, it's the only one I visit regularly. Something about it draws me in, and I often lose track of time staring at it."
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What would Lexi think of it? I bet she would be able to rattle off something about its history and origin.)"


    $sidecharone = "???"
    hide mscmc
    show mscmc jacket_hairdown surprised at centre
    sid1 "It's quite lovely, isn't it?"
    hide mscmc
    show hannah casual basic at centre
    "I blink in shock and regard the woman next to me, immediately noting her platinum and brown hair and chic clothing."
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Something about her seems off somehow. Is it the way her smile doesn't reach her eyes?)"

    "(Well, I should respond.)"
    hide mscmc
    $sidecharone = "Real Housewives Looking Woman"
    $menuhideborder = True
    menu lexis1e1c1:
        "A. Yeah it's great.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left3
            show hannah casual basic at right3
            mclexi "Um, yeah. I really like it. Something about it just speaks to me."
            show hannah casual smile
            sid1 "It’s always nice when an artifact does that, isn’t it? It’s like a part of the past speaking to us in the present."
            hide mscmc
            hide hannah

        "B. It's nothing special.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left3
            show hannah casual basic at right3
            mclexi "It’s nothing special. I just like how it looks."
            show hannah casual smile
            sid1 "Is that all? There’s a lot of history behind old artifacts like this. Haven’t you ever wanted to hear their story?"
            hide hannah
            hide mscmc
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(That sounds like something Lexi would say...)"
            hide mscmc
        "C. Shrug.":
            $menuhideborder = False
            show mscmc jacket_hairdown basic at left3
            show hannah casual basic at right3
            "I shrug off the question."

            mclexi "Something about it is different from the other exhibits."

            sid1 "It is different, isn't it? There are probably only a handful of people left in the world who can make something so exquisite."

    show mscmc jacket_hairdown smile at left3
    show hannah casual smile at right3
    sid1 "Are you a fan of historical artifacts?"

    mclexi "Not particularly... Coming here just reminds me of a friend I haven't seen in a while."

    $sidecharone = "Exhibit Aficionado"

    sid1 "I'm sure whoever made this piece would be happy to hear that."

    sid1 "Having your work admired by others is quite validating."

    mclexi "Are you an artist?"

    $sidecharone = "Who is she?"

    sid1 "In a way... Allow me to introduce myself. Hannah, Hannah Jones."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "Alarms instantly go off in my mind as Hannah introduces herself and my thoughts jerk back to six months ago."
    stop music fadeout 1.0
    play music msclexi
    #scene should be black and white to indicated flashback to preview special
    hide mscmc
    show bg msc_yacht_day at bg with fade
    show ned vest basic at centre
    dt "As far as how I knew where the treasure was and the fact that you are a mermaid.... You can thank your friend Hannah for that."
    hide ned
    show bg msc_ocean_wide_day at bg
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Who's Hannah, Lexi?)"
    hide mscmc
    show lexi mermaid_cu angry_cu at lexi_cu
    lx "I don't know who you're talking about, Ned."
    hide lexi
    show bg msc_yacht_day
    show ned vest_cu smile_cu at ned_cu
    dt "Really? Because a certain Hannah Jones seems to know you quite well."

    dt "She even wanted me to tell you that she was the one who sold you out."
    hide ned
    #Flash back ends, return to color
    show bg msc_museum_displays_day at bg with fade
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    stop music fadeout 1.0
    play music mscsuspense2
    "(Is this the same Hannah Jones?)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show hannah casual smile at right3
    hj "And your name?"
    show mscmc jacket_hairdown basic
    mclexi "Oh! It's [genericfn]."
    show hannah casual basic
    "She reaches into her designer purse and pulls out a gaudy but stylish gold colored leather wallet."

    "She opens the wallet and goes to pull out a business card, but as she does a polaroid falls out onto the ground."
    show mscmc jacket_hairdown surprised:
        easein 0.3 ypos 200
    "I instinctively reach down to pick up the picture but freeze as I look at it."

    "Staring back at me is Lexi, with Hannah's arm around her shoulders, on a speedboat, both of them beaming."
    show hannah casual angry
    hj "Oh, oops. I didn't realize I still had that picture on me. I thought I threw it away."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(You {i}accidentally{/i} dropped a photo of Lexi you thought you threw away? I find that hard to believe...)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show hannah casual sad at right3
    mclexi "Is she a friend of yours?"
    show hannah casual smile
    "Hannah chuckles half-heartedly as if she's just heard a sad joke."
    show hannah casual angry
    show mscmc jacket_hairdown surprised
    hj "A friend? Maybe that was true at one point. But in the end, she's a narcissist who uses people before tossing them away."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What the hell?)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show hannah casual basic at right3
    "I move to hand the picture back to Hannah but she puts up her hand to stop me."

    hj "I don't want it. And keep an eye out. Someone told me she'd been seen around here. That woman is bad news."
    show hannah casual angry
    hj "My advice? If you ever meet her, run in the opposite direction."
    hide mscmc
    hide hannah
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(What is going on?)"
    hide mscmc

    show mscmc jacket_hairdown surprised at left3
    show hannah casual smile at right3
    hj "Well look at the time. I need to be going, nice meeting you!"
    stop music fadeout 1.0
    play music mscsadtimes
    scene bg msc_tide_pools_sunset at bg with wipeleft
    "I stare at the sun setting on the horizon past the tide pools and I can't help but think about the past, my last night with Lexi."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She was so much fun. Dancing, drinking... kissing.)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at centre
    "My cheeks flush at the memory and I bury my face into my hands."
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I want to be mad at her, but I also wish she would just show up and be with me.)"
    show mscmc jacket_hairdown_cu surprised_cu
    "(And what about Hannah? It has to be the same woman who tipped off Ned. She seems jaded for sure.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at centre
    "Suddenly, I feel a light flick of water land on the side of my face."

    "Confused, I look to the side only to get lightly splashed on my other cheek from the opposite direction!"

    $sidechartwo = "Sassy Voice"
    show mscmc jacket_hairdown grin
    sid2 "Looking for someone, cutie?"
    stop music fadeout 1.0
    play music msclexi
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    "My head snaps forward at the sound of the familiar voice and I see Lexi staring up at me from the water."
    hide lexi
    show mscmc jacket_hairdown surprised at left2:
        easein 0.3 xpos 800
    "I lean over the edge of the rock I'm sitting on and look down to search the water for my prankster..."

    "...only to catch a glimpse of her speckled green and pink tail as it disappears under the water."
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Over here, hot stuff."
    show lexi mermaid_cu embarrassed_cu
    "She pops her head out of the water a bit farther away from the shore and shoots me a sly wink."
    hide lexi
    show mscmc jacket_hairdown grin at centre
    mclexi "Stop teasing. Get over here!"
    #sparkle effect on the entire screen, reference is 3:40 on the S1E1 video
    hide mscmc
    show lexi mermaid bigsmile at centre:
        ypos 1000
        easein 0.4 ypos -100
    "Without answering, Lexi propels herself into the air, her tail glistening in the setting sun as she gracefully dives back under."
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Showoff. She's here!)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at left3
    show lexi mermaid smile at right3
        #effect of her swimming up from the bottom right on a diagonal
    "Lexi casually back strokes towards me, rolling in the water every once in a while for fun."
    hide mscmc
    hide lexi
    show lexi mermaid_cu smile_cu at lexi_cu
    "When she finally gets back over to me, she slowly rises out of the water until her face is inches from mine."
    scene bg msc_lexi_s1_ei1 at bg with fade:
        yanchor 0.6
        linear 8 yanchor 0.2
    "Strands of her dark green hair frame her face and cover her tan shoulders as she looks up at me smiling."

    "Her irises are the green of sea glass, and her eyes are surrounded by dark, long lashes that accentuate her eye shape."

    lx "Miss me?"

    "She playfully hooks her finger under my chin and pulls me closer to her until our noses are almost touching."

    "I nod, unable to think."

    lx "What, sea witch got your tongue?"

    "Her eyes glimmer saucily as she stares deep into mine and my heart beat pounds fast and loud."
    scene bg msc_tide_pools_sunset at bg with fade
    show mscmc jacket_hairdown smile at left3
    show lexi mermaid bigsmile at right3
    "With a grin, Lexi pulls herself up onto the tide pools and sits next to me, her tail moving languidly in the water."
    show mscmc jacket_hairdown embarrassed
    show lexi mermaid smile
    "I try to gather my thoughts as she looks out at the horizon to give me time to respond."
    hide mscmc
    hide lexi
    $menuhideborder = True
    menu lexis1e1c2:
        "A. Am I dreaming?":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Is she really here? Maybe I’m dreaming.)"
            hide mscmc
            show lexi mermaid bigsmile at centre
            "I don’t say anything as Lexi stretches her arms up nest to me, and casually cracks her neck."
            hide lexi
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(It really is her! Jeez. Of course, she’d just show up and act as if nothing happened.)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left3
            show lexi mermaid basic at right3
            lx "You’re being quiet. Maybe you didn’t miss me after all."
            show mscmc jacket_hairdown smile
            show lexi mermaid smile
            mclexi "Of course I did! Where have you been?"

        "B. Of course, I've missed you!":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi mermaid bigsmile at right3
            mclexi "I’ve missed you. It’s been so long I’m just in shock!"
            show lexi mermaid embarrassed
            lx "Glad to hear it! I’ve missed you too."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(Did you really, though?)"
            hide mscmc
            show mscmc jacket_hairdown sad at left3
            show lexi mermaid surprised at right3
            lx "Don’t look at me like that! Honest! I really did miss you."
            show mscmc jacket_hairdown surprised
            show lexi mermaid sad
            mclexi "Then where did you go that night? You left and then I never heard from you."


        "C. Pretend I haven't missed her.":
            $menuhideborder = False
            show mscmc jacket_hairdown basic at left3
            show lexi mermaid bigsmile at right3
            mclexi "Miss you? I didn't even notice you were gone."
            show lexi mermaid smile
            "I try to keep a straight face, but I see feel Lexi grin and it gradually becomes harder and harder."
            show mscmc jacket_hairdown smile
            show lexi mermaid bigsmile
            mclexi "Fine! Yes, I missed you! Now tell me where you disappeared to!"
    show mscmc jacket_hairdown basic at left3
    show lexi mermaid bigsmile at right3
    "Lexi shrugs, maintaining her characteristically carefree attitude."
    show lexi mermaid basic
    lx "That night... Something came up and I had to go. Life as a treasure hunter, ya know?"
    show mscmc jacket_hairdown sleep
    "I take a deep breath and try to match Lexi's casual air."
    show mscmc jacket_hairdown smile
    show lexi mermaid smile
    mclexi "Busy, huh?"

    lx "Something like that. You know how it goes. New places to visit, new people to meet."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's being vague. Why?)"
    hide mscmc
    show mscmc jacket_hairdown smile at left3
    show lexi mermaid bigsmile at right3
    lx "What about you? Any surfing competitions?"

    mclexi "Hmm... I've done a few tournaments since you've been gone."
    show lexi mermaid smile
    lx "I'd ask if you won, but I already know you did."
    show mscmc jacket_hairdown embarrassed
    "She grins at me, I can feel the butterflies fluttering in my stomach just like when we first met."

    lx "What else? Meet any interesting people? Maybe other mers?"
    show mscmc jacket_hairdown sleep
    "I shake my head and roll my eyes at her."
    show mscmc jacket_hairdown embarrassed
    mclexi "Nope, you're the only mermaid in my life."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Even if I do ever meet other mers, Lexi's in a league of her own.)"
    hide mscmc
    show mscmc jacket_hairdown basic at left3
    show lexi mermaid surprised at right3
    mclexi "There is this, though..."
    stop music fadeout 1.0
    play music msctense
    "I reach into my jacket pocket and hold up the picture that Hannah dropped earlier. This time it's Lexi who's shocked."
    show lexi mermaid angry at right3:
        xpos 700
        easein 0.4 xpos 450
    "Lexi's face is full of confusion and then maybe anger as she takes the photo from me and looks it over."
    show lexi mermaid basic
    lx "Where'd you get this?"
    show mscmc jacket_hairdown surprised
    show lexi mermaid angry
    mclexi "Hannah. She introduced herself to me at the museum. Who is she to you?"
    scene bg msc_tide_pools_night at bg with dissolve
    "Lexi's sigh fills the evening air as she lays back and looks up at the now dark sky."
    show mscmc jacket_hairdown sad at left3
    show lexi mermaid angry at centre
    lx "We partnered on a job {i}once{/i}."
    show mscmc jacket_hairdown surprised
    mclexi "Like how we did?"
    show mscmc jacket_hairdown embarrassed
    show lexi mermaid smile
    lx "Ha! As if. It was nothing like it was with us. And in the end, with Hannah, the job blew up in our faces."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Nothing like it was with us. Why does that make me feel so warm inside? Was what we had special?)"
    show mscmc jacket_hairdown surprised at left3
    show lexi mermaid angry at centre
    lx "But if she's around... Just be careful. She's bad news."
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Funny, Hannah said the same thing about you...)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show lexi mermaid surprised at centre
    mclexi "Is she why you're back?"
    show mscmc jacket_hairdown basic
    lx "Of course not! I knew she got released from prison, but if we're being honest..."
    stop music fadeout 1.0
    play music mscmctheme
    show mscmc jacket_hairdown embarrassed
    show lexi mermaid bigsmile
    lx "I wanted to stock up on those plush monsters you showed me last time!"
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Right. I'm {i}sure{/i} you came back after six months for some plushies.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left3
    show lexi mermaid bigsmile at centre
    mclexi "Plushies, huh? Is that going to be the new treasure you hunt?"
    show lexi mermaid embarrassed
    "Lexi winks at me with a slightly embarrassed look on her face."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She's cute when she's embarrassed!)"
    hide mscmc
    show mscmc jacket_hairdown smile at left3
    show lexi mermaid bigsmile at centre
    lx "I mean apparently they get valuable eventually... But enough about that!"
    show lexi mermaid embarrassed
    show mscmc jacket_hairdown surprised
    lx "I'm back and I think we should do something special!"
    show lexi mermaid bigsmile
    show mscmc jacket_hairdown grin
    mclexi "What were you thinking?"
    show lexi mermaid embarrassed
    lx "I've never done it, but mers have this thing they can do with humans where it lets people breathe underwater, for a bit at least."
    show mscmc jacket_hairdown surprised
    mclexi "That..."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Sounds amazing!)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3
    show lexi mermaid bigsmile at right3
    mclexi "Sounds cool. How does that work?"
    show mscmc jacket_hairdown embarrassed
    show lexi mermaid smile
    lx "Sailors used to call it the 'Kiss of Life."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Does she want to breath into my mouth? Mermaid mouth-to-mouth?)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at left3
    show lexi mermaid smile at centre
    mclexi "How do you do it?"
    stop music fadeout 1.0
    play music mscromance
    lx "Well, first we get in the water, and get really close..."
    show lexi mermaid smile at left1:
        xpos 450
        easein 0.4 xpos 425
    "Lexi scoots closer to me, taking my hands in hers."
    hide mscmc
    hide lexi
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Then I lean in like this..."

    "She leans in close to me until our lips are barely half an inch apart."

    "My eyes flick to her full red lips that are so close it seems a gentle breeze could push them to mine."

    "Time seems to stand still and her gentle breath tickles my lips, it tastes like roses, roses with a bit of a salty edge."
    show lexi mermaid_cu bigsmile_cu at lexi_cu
    "As I lose myself in the moment, Lexi pulls me back by puckering her lips and raising her eyebrows up and down comedically."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(God, she's cute, and funny, and so freaking hot.)"
    hide mscmc
    show lexi mermaid_cu embarrassed_cu at lexi_cu
    lx "Then I breathe... into you."
    show lexi mermaid_cu smile_cu
    "She leans in even further, giggling softly and staring up at me from under her thick lashes."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I'm going to need a kiss of life because she's killing me right now. God, I'm flustered, keep it cool, keep it cool.)"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "I've never done it with anyone before... I want to do this with you."

    "Her eyes twinkle with the promise of rogueish fun."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mclexi "I..."
    hide mscmc
    show lexi mermaid smile at centre
    "Before I can answer, Lexi slips into the water and looks back up at me, her heavy-lidded eyes searching mine."
    hide lexi
    show lexi mermaid_cu smile_cu at lexi_cu
    "She holds her hand out to me."

    lx "Do you want my kiss of life?"
    hide lexi
    $menuhideborder = True
    menu lexis1e1c3:
        "A. Accept Lexi's kiss of life!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I definitely can’t pass this up!"
            hide mscmc
            show mscmc casual_hairdown grin at left3
            show lexi mermaid smile at right3
            "I throw my jacket and shoes to the side and drop into the water next to Lexi."
            hide mscmc
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(I missed this. The promise of adventure and allure Lexi brings with her.)"

            "(I missed {i}her{/i}. Her confidence, her boldness, the fun I have when she’s around.)"
            hide mscmc
            show mscmc casual_hairdown embarrassed at left3:
                easein 0.4 ypos 800
            show lexi mermaid smile at right3
            "My face starts to feel warm and I submerge myself underwater in an attempt to cool down."
            stop music fadeout 1.0
            play music mscunderwaterromance
            scene bg msc_underwater_night at bg with wiperight
            "Lexi follows me under and holds my hand, taking me deeper until we’re about halfway to the nearby ocean floor."
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(Her hands are soft, and surprisingly small, but her grip is self-assured and strong.)"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "She puts her hands on my waist and pulls me closer to her, our bodies like two parallel lines."
            show lexi mermaid_cu embarrassed_cu
            "Lexi tilts her head as she leans in towards me, lining up her lips with mine, as her eyes flick to mine and back to my lips."
            show lexi mermaid_cu sleep_cu
            "She brushes her nose against mine tenderly before closing the space between us and I feel the whisper of her lips against my own."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(Her lips are like velvety flower petals, pressed gently against mine.)"
            hide mscmc
            show lexi mermaid_cu sleep_cu at lexi_cu
            "Lexi presses her body to mine, and I feel sweet air push itself between the parting of my lips from her into me."
            hide lexi
            show mscmc casual_hairdown_cu sleep_cu at mscmc_cu
            "(Can she feel my heart about to beat out of my chest?)"
            hide mscmc
            show lexi mermaid_cu embarrassed_cu at lexi_cu
            "I close my eyes and give into the moment as my lungs fill, and then Lexi’s plump lips pull away."
            show lexi mermaid_cu smile_cu
            lx "Now breathe like you would on land."
            show lexi mermaid_cu bigsmile_cu
            "I follow Lexi’s instructions and nervously take a deep breath in and hold it for a moment."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(Right, breathing underwater. I honestly forgot that was the point of all this for a second there.)"
            hide mscmc
            "The light headedness that I felt before is replaced by a refreshing sensation as I am able to breathe in and out."
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(This feels incredible! I’m breathing underwater!!!)"
            hide mscmc
            "I exhale heavily and then eagerly breathe in, testing my new power and marveling at the bubbles escaping my lips every now and then."
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "Ha! You’re a natural!"
            show lexi mermaid_cu smile_cu
            "Lexi winks as she plays with my fingers."

            lx "You haven’t done this with another mermaid, have you?"

            "I shake my head, still stunned by my new ability."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(Lexi really knows how to blow my mind, and I want to tell her that.)"
            show mscmc casual_hairdown_cu surprised_cu
            mclexi "Nagh!"
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "Lexi chuckles at my attempt to speak and gracefully swims around me."


            lx "You still can’t talk, silly!"
            hide lexi
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            "(One day, I want to be able to do all the things underwater, just like a mermaid.)"
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "I playfully stick my tongue out at Lexi as she circles me laughing and I swim to try and catch up to her."

            "The bright moonbeams piercing the water’s surface make it relatively easy to see, but somehow I lose track of Lexi."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(Where did she go? I know I have exceptional underwater eyesight for a human. How did I lose track of her?)"

            "I peer around for her but she’s nowhere to be found..."
            hide msmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "Then, I jump as I feel a finger playfully poke my side."
            show lexi mermaid_cu bigsmile_cu
            lx "Gotcha! Are you ticklish?"
            hide lexi
            show mscmc casual_hairdown grin at left3
            show lexi mermaid bigsmile at right3:
                xpos 700
                easein 0.4 xpos 1500
            "I send a poke towards Lexi’s side but she shoots away from me laughing."
            hide lexi
            hide mscmc
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(Oh yeah?!)"
            show mscmc casual_hairdown smile at left3:
                xpos 300
                easein 0.4 xpos 500
            show lexi mermaid surprised at right3:
                xpos 1500
                easein 0.4 xpos 700
            "I relax my body and wait, anticipating Lexi, and as I feel the water move behind me I spin around and boop her on the nose."
            show lexi mermaid bigsmile
            lx "Hey! No fair! How’d you know I was there?"
            show mscmc casual_hairdown grin:
                xpos 500
                easein 0.4 xpos 575
            "I grin at Lexi and raise my chin confidently as I dart around her and attack her sides with tickles."
            show lexi mermaid surprised
            lx "Ah!"
            show mscmc casual_hairdown grin:
                xpos 575
                easein 0.4 xpos 475
            show lexi mermaid bigsmile:
                xpos 700
                easein 0.4 xpos 750
            "She screams out playfully and uses her tail to push water at me, knocking me back a little."
            hide mscmc
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(She was right, this is the most fun I’ve had in ages! And she’s definitely ticklish, good to know.)"
            hide mscmc
            show mscmc casual_hairdown grin at left3:
                xpos 575
            show lexi mermaid bigsmile at right3:
                xpos 750
            "I laugh at the thought."

            lx "Above you!"

            "I look up and see Lexi floating above me, she reaches down and gives me a gently whack on the forehead as I’m looking up."
            hide lexi
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "As she goes to dark away, I manage to grab her hand and pull her down to me, preventing her escape."

            "Our faces are suddenly very close and she’s holding tightly to my hand."
            hide lexi
            show mscmc casual_hairdown_cu smile_cu at mscmc_cu
            "(I missed feeling like this.)"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "Lexi twirls around under my hand as if we’re dancing."

            lx "Look at you, I bet you know how to lead a lady around the dancefloor."
            show lexi mermaid_cu bigsmile_cu
            "Lexi shoots me an absolutely wicked grin."


            lx "But I’m no lady."

            "It feels just like yesterday we were flirting like this together on the beach under the same moon."

            "Our eyes lock and for a moment I wonder if we’ll actually kiss this time..."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "...but before the moment can play out, my lungs suddenly feel like I’ve sprinted a mile."

            "(I need to inhale! But not down here.)"
            hide mscmc
            "Seeing my confusion, Lexi takes my hand and starts swimming with me to the surface."
            show bg msc_tide_pools_night at bg with wiperight
            show mscmc casual_hairdown surprised at left1
            show lexi mermaid basic at right2
            "As we breach the surface of the water, I take a deep breath in."
            show mscmc casual_hairdown grin at left1
            show lexi mermaid smile at right2
            lx "Looks like time’s up! How was it?"
            show mscmc casual_hairdown smile
            "I nod as I take a few more deep breaths and smile at her."

            mclexi "Do you even have to ask? That was the most incredible thing that’s happened to me in I don’t know how long!"
            hide mscmc
            hide lexi
            "We start swimming towards the edge of the tidepools, Lexi cutting through the water like a beautiful, sharp knife."

            "I pull myself out onto the rocks and as I do, Lexi follows suit and switches her tail for her legs."

        "B. It's just so sudden...":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mclexi "I... my stomach hurts a little, maybe another time."
            show mscmc jacket_hairdown_cu angry_cu
            "(My stomach hurts? Why didn't I say yes?!)"
            show mscmc jacket_hairdown_cu sleep_cu
            "(Damn my inability to be cool around very good-looking, flirty women.)"
            hide mscmc
            show lexi swim sad at centre
            "Lexi frowns, clearly put out before she switches to her legs using a magic item."

            lx "I really wanted my first time doing it to be with you... but whatever."
    show lexi swim smile at centre
    "Lexi lounges on the tidepools with me, stretching and observing her long legs after just switching from her tail."
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I forgot how incredible it is to see magic at work! I wonder if mer magic could turn my legs into a tail...)"
    hide mscmc
    show mscmc jacket_hairdown smile at left3
    show lexi swim bigsmile at right3
    lx "So how close are you to your dream of being in the World Surf League now?"
    show mscmc jacket_hairdown grin
    show lexi swim smile
    "I grin proudly, happy that she wants to know about me."
    show lexi swim bigsmile
    mclexi "Really close. I've got a seat in the Qualifier Series!"
    stop music fadeout 1.0
    play music mscmctheme

    "Lexi listens intently to me as I get lost in my explanation of how the World Surf League works and the point system."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Ah! I'm rambling! Trina always makes fun of me when I do this...)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3
    show lexi swim bigsmile at right3
    mclexi "But yeah, I'm almost there!"
    show lexi swim smile
    lx "Well I have no doubt you'll be number one in the Championship Tour. But... all work and no play is never good."
    show mscmc jacket_hairdown embarrassed
    lx "And you look like you've been working too much, and not playing enough."
    hide mscmc
    hide lexi
    show lexi swim_cu smile_cu at lexi_cu
    "Lexi shoots me a flirty glance and I can feel goosebumps rise up on my arms."

    lx "Wanna paint the town red tonight together?"

    $tobecontinued()

    scene bg msc_msctbc at bg with fade
    pause
    $ resets()
