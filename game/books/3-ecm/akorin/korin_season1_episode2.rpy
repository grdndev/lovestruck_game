label korin_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_junkyard_day at bg
    play music ecmtense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show korin jacket pin basic at left3
    show connie casual angry at right3
    "Connie stomps her way back to the front of the group. "
    co "You just can't help looking out for her because of her father, can you?"

    show korin jacket pin angry at left3
    ko "Ms. Summers, if you're going to resort to {i}personal{/i} accusations, I'm going to have to ask you to leave."
    co "Leave? I'm the only one here who seems to be taking this seriously!"
    co "D.I.V.A.A. has a reputation to uphold. We can't put aside blunders like this for rookies no matter who their parents are!"
    "My chest grows tight as the full gravity of the situation hits me."

    hide korin
    hide connie
    show ecmc jacket_v2_cu headset_cu sad_cu at ecmc_cu
    "(This really could reflect badly on Korin, couldn't it?)"
    hide ecmc

    show korin jacket pin angry at left3
    show connie casual angry at right3
    ko "Connie, I'm well aware of the position that D.I.V.A.A. is in."
    ko "But this is my outing, and I get final say on how this is handled. So let me make two things perfectly clear."

    show korin jacket pin angry at left3:
        ease 0.4 left1plus
    ko "One: you're not the only person here who has to submit a report to Dom at the end of the day."

    show connie casual basic
    "Connie's face grows pale. Clearly, she hasn't thought about what Korin might say about her to her boss."

    show korin jacket pin angry at left1plus behind connie:
        ease 0.4 left1 xoffset 26
    ko "And two: we're given the best talent from the academy to train and serve under D.I.V.A.A.."
    ko "It's important that we {i}foster{/i} those trainees, not punish them as harshly as possible for following procedure."

    hide korin
    hide connie
    show ecmc jacket_v2 pin headset smile at centre
    "I look around at the other trainees and see the relief I feel reflected in their expressions."

    hide ecmc
    show ecmc jacket_v2_cu headset_cu smile_cu at ecmc_cu
    "(Korin's really going to bat for us Hatchlings.)"
    hide ecmc

    show korin jacket pin angry at left1 behind connie:
        xoffset 26
    show connie casual angry at right3
    "Connie, however, looks stung."
    "I expect Korin to briskly move on, but she lowers her voice to Connie."
    ko "I don't like pulling rank, Ms. Summers."
    co "I didn't mean...I just wanted to--"

    show korin jacket pin smile
    ko "I know you think you're doing what's best..."
    ko "But I think it would help everyone if you go back to HQ and cool off before finishing your report."
    ko "I can't afford any more time lost with my trainees today."
    ko "And let's all, including yourself, reflect on how we could have handled things better."
    ko "This can still turn into a positive situation for all involved."
    "Connie looks at her and finally nods in defeat."

    show connie casual angry at right3:
        parallel:
            linear 0.6 alpha 0.0
        parallel:
            easein 0.2 yoffset -10
            easein 0.4 yoffset 30
    "She slinks off to the exit, and Korin turns back to the rest of the group."
    ko "Back to work, cadets. I'll resume our one-on-ones shortly."

    hide connie
    show korin jacket pin basic at centre:
        xoffset 250 alpha 0.0
        parallel:
            easein 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    show ecmc jacket_v2 pin headset sad at left3
    "They drift away. Arms folded, Korin turns to me. I brace myself for a brisk talking-to like Connie just got."
    ko "How you doing, Scraps?"

    hide ecmc
    hide korin
    $menuhideborder = True
    menu korins1e2c1:
        "A. Oh, you know":
            $menuhideborder = False
            show korin jacet pin basic at center
            show ecmc jacket_v2 pin headset smile at left3
            mckorin "Oh, you know. Could be better!"
            show korin jacet pin sad at center
            "Korin gives my arm a reassuring squeeze."

        "B. Yeah, not great!":
            $menuhideborder = False
            show korin jacket pin basic at centre
            show ecmc jacket_v2 pin smile at left3
            mckorin "Yeah, not great!"
            show korin jacket pin sad at centre
            "Korin winces and nods like she understands exactly."
        "C. Fantastic! And you?":
            $menuhideborder = False
            show korin jacket pin basic at centre
            show ecmc jacket_v2 pin headset smile at left3
            mckorin "Fantastic! And you?"

            show korin jacket pin smile at centre
            "Korin smiles grimly in acknowledgement of my sarcasm."

    show korin jacket pin smirk
    ko "We'll figure out what else to do once we get back to HQ."

    show ecmc jacket_v2 pin headset determined
    mckorin "I pulled out my ARCware to log the drive as evidence, Korin. I really was just following procedure."

    show korin jacket pin basic
    ko "I completely understand."

    show korin jacket pin sad
    ko "But anything that leads to destruction of evidence is taken very seriously."

    show ecmc jacket_v2 pin headset sad
    mckorin "...How seriously?"
    "My stomach plunges as she dodges the question."
    ko "This all may feel unfair right now, but it's part of the burden of accountability for a case."
    ko "We're held to a higher standard at D.I.V.A.A.. Any weak links in the chain can reflect poorly on all of us."
    "Sadly, I nod."
    mckorin "I understand."
    "I look up at Korin, trying not to show her that I feel completely hopeless and afraid for my job."
    mckorin "What do I do?"
    show korin jacket pin basic
    ko "You're going to file an indecent report with Griffin Detective Dominick Vega as soon as we get back to HQ."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu headset_cu surprised_cu at ecmc_cu
    "(That's Dad's old boss. And Connie and Korin's current boss...) I must look pale, because Korin moves to reassure me."
    hide ecmc

    show korin jacket pin smile at centre
    show ecmc jacket_v2 pin headset sad at left3
    ko "Look, everything you've heard about what a hardcase he is..."

    show ecmc jacket_v2 pin headset surprised
    mckorin "...is all overblown? A complete exaggeration?"

    show korin jacket pin smirk
    ko "All true, I'm afraid."

    show ecmc jacket_v2 pin headset sad
    "Korin pats my slouching shoulders."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    ko "But! Since this happened under my watch, you're not alone. For better or worse, we're in it together."
    hide korin

    show ecmc jacket_v2_cu headset_cu sad_cu at ecmc_cu
    "(If it weren't for her reassurance, I might completely break down.)"
    hide ecmc

    show korin jacket pin smile at centre behind ecmc:
        parallel:
            easein 0.4 xoffset 250
        parallel:
            linear 0.4 alpha 0.0
    show ecmc jacket_v2 pin headset sad at left3
    "She leaves to attend to the other trainees."

    hide korin
    show ecmc jacket_v2 pin headset basic at left3:
        easein 0.4 centre
    "I do feel better."

    hide ecmc
    show ecmc jacket_v2_cu headset_cu sad_cu at ecmc_cu
    "(But she still didn't tell me that everything was going to be okay.)"
    hide ecmc

    show korin jacket pin sad at centre
    "I watch Korin carefully as she heads off, and I think I catch the shadow of the concern she's trying to hide."

    hide korin
    show ecmc jacket_v2_cu headset_cu sad_cu at ecmc_cu
    "(Just how serious is this going to be?)"
    hide ecmc

    stop music
    play music ecmcalmeveryday2
    scene bg ecm_office_hq_on at bg with wiperightdissolve
    "Back at HQ, I buckle down in a free workcube and start my incident report."

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Day one, and I'm filling out a form detailing what could be a fireable offense.)"
    "(Korin's probably busy, right?)"
    "(She has her own report to do...)"
    hide ecmc

    show ecmc jacket_v2 pin sad at centre:
        easein 0.4 yoffset 80
    "I sigh and let my head bump down on my desk."
    hide ecmc

    show enver casual basic at centre:
        yoffset 50 alpha 0.0
        parallel:
            linear 0.6 alpha 1.0
        parallel:
            easein 0.4 yoffset -10
            easein 0.2 yoffset 0
    "I'm about to cycle into a deep spiral of negative thoughts when suddenly the door to my cube whizzes open."

    show ecmc jacket_v2 pin sad at left3:
        yoffset 80
    show enver casual basic at right2
    mckorin "Hey, Enz."
    "It's Enver--a Crow-rank agent at D.I.V.A.A., and a close personal friend."

    show enver casual sad
    "He mirrors my slumped-over posture."
    en "So, great first day?"
    "I stare at him, face still pressed to my desk."

    show rion black pin basic at right:
        zoom 0.9 rotate 0 anchor(0.5, 1.0) transform_anchor True yoffset 640
        linear 0.4 rotate -5
    show ecmc jacket_v2 pin surprised
    "Before I can even answer him, someone else pokes his head through the door."
    ri "Sorry to interrupt. Enver, the next rail leaves in ten."

    show enver casual smile
    en "Yeah, just got to catch up with [genericfn] here real quick."

    show rion black pin surprised at right:
        zoom 0.9 rotate -5 anchor(0.5, 1.0) transform_anchor True yoffset 640
    ri "The rookie?"
    en "Yep."

    show rion black pin smirk at right:
        zoom 0.9 rotate -5 anchor(0.5, 1.0) transform_anchor True yoffset 640
    "Rion's eyes widen in recognition. He nods slowly, then claps Enver briskly on the arm."
    ri "Take your time, then. See you tomorrow."

    show rion black pin smirk at right:
        zoom 0.9 rotate -5 anchor(0.5, 1.0) transform_anchor True yoffset 640
        linear 0.4 xoffset 80 alpha 0.0
    "Enver waves him off, then closes the door to my cube."
    en "So, yeah...word travels fast!"

    hide rion
    show ecmc jacket_v2 pin sad
    mckorin "I mean, is this it? It's over for me, right?"

    show ecmc jacket_v2 pin angry:
        easein 0.4 yoffset 0
    show enver casual sad
    "Enver doesn't answer right away. I bolt upright."
    mckorin "Enz!!"
    en "Yeah, no. I'm just trying to think of what to say."

    show enver casual smile
    en "Look...nobody knows how this'll all turn out!"

    show ecmc jacket_v2 surprised
    mckorin "In all your time here, have you ever known anyone to keep their job after destruction of evidence?"

    show enver casual sad
    en "Well...no."

    show ecmc jacket_v2 pin sad
    "I bury my head in my hands."

    show enver casual smile
    en "But only because I've never seen it happen!"
    en "You're new! Maybe Dom'll go easy on you."

    show ecmc jacket_v2 angry
    "I look up at him, exasperated."

    show enver casual sad
    en "Yeah...that sounded more convincing in my head."
    en "But, look, I heard Korin pulled rank on Connie--"

    show ecmc jacket_v2 surprised
    mckorin "So what?"

    show enver casual smile
    en "Look, Korin just like, {i}gets{/i} people, y'know?"
    en "The way you understand tech and programming? That's how Korin understands other people."
    en "So when I had some trouble with Connie a while back, Korin told me to give her a wide berth. Make her feel like she's in charge."

    show ecmc jacket_v2 determined
    "I scoff."
    mckorin "...Did it work?"
    en "Kept the peace ever since. It's how Korin deals with Connie herself."
    en "So if Korin pulled rank on Connie in front of everyone? That's kinda huge."
    "I check his expression to make sure he's not just trying to fill me with false assurances."
    mckorin "Why would she do that?"

    show enver casual basic
    "He shrugs."

    show enver casual sad
    en "Maybe because of your dad?"

    show ecmc jacket_v2 sad
    "My heart drops a little."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Yeah, maybe it's just that.)"
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show enver casual smile at right2
    en "Or maybe she sees something else in you. Like I said, she's good at reading people."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Whatever the reason...I need to make sure I don't let her down.)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at left3
    show enver casual smile at right2
    mckorin "What about you? Are you done for the day?"
    en "Oh, yeah, I just wrapped my work up a few minutes ago."

    show ecmc jacket_v2 pin smile
    mckorin "So you'll be able to help me with this report, right?"

    show ecmc jacket_v2 pin sad
    "Enver just tips his head back, letting laughter booming around the tiny workcube."

    show enver casual sad
    en "...Oh. You were serious."
    en "Look, [genericfn]...if Dom gets wind that you were helped on this report by someone who wasn't even there..."

    show enver casual smile
    en "Why not ask Korin?"

    show ecmc jacket_v2 pin surprised
    mckorin "Yeah, no. I saw her orientation schedule today."
    en "She {i}is{/i} busy, maybe you can bribe her with dinner?"

    show ecmc jacket_v2 pin embarrassed
    "I tug on the ends of my hair."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(They didn't teach this kind of thing at the academy...)"
    hide ecmc

    show ecmc jacket_v2 pin embarrassed at left3
    show enver casual smile at right2
    en "C'mon. Worst she can do is say no, right?"

    play sound phone_vibrating

    show ecmc jacket_v2 pin surprised
    "I'm rattled by a sudden buzz from my ARCware."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(It's Korin!)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at left3
    show enver casual smile at right2
    "Enver takes this chance to escape."
    en "Good luck! See ya!"

    hide enver
    hide ecmc
    show korin nojacket pin sad at holo_mask, korin_holo, centre
    "I wave him away, then answer a call to a very flustered-looking Korin."
    hide korin

    show ecmc jacket_v2 pin basic at left3
    show korin nojacket pin sad at holo_mask, korin_holo, right3
    ko "Hey, Scraps, can you do me a favor?"

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(She's really married to that nickname, isn't she?)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at left3
    show korin nojacket pin sad at holo_mask, korin_holo, right3
    "But a warm feeling fills me as I realize {i}she{/i} came to {i}me{/i} for help."
    mckorin "What's up?"
    ko "The holo interface on my desk...this damn thing has always had it out for me. It's on the fritz again."

    show korin nojacket pin smirk at holo_mask, korin_holo, right3
    ko "Could you come up and take a look at it, maybe?"
    mckorin "The Information Technology department couldn't fix it?"

    show korin nojacket pin sad at holo_mask, korin_holo, right3
    "Korin grimaces."
    ko "They're a little slammed today, and... they hear enough from me. You were so good with BB earlier, I just kinda thought..."
    ko "But you're probably swamped with that report, right?"

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(More like just stuck, but I can't tell her that {i}now{/i}.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show korin nojacket pin sad at holo_mask, korin_holo, right3
    mckorin "Not completely!"

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(I could really use a break, though! And I bet I could really impress her by helping her out...)"
    hide ecmc

    show korin nojacket_cu smile_cu at holo_mask, korin_holo, korin_cu
    ko "If you feel like you need a break from that report or something, stopping by would really help me."
    hide korin

    $menuhideborder = True
    menu korins1e2c2:
        "A. I can fix that." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin sad at holo_mask, korin_holo, right3
            mckorin "Actually, I could really use a break. I'll be right up!"
            stop music
            play music ecmkorintheme
            scene bg ecm_generic_office_on at bg
            show korin nojacket pin sad at centre
            with wiperightdissolve

            "I arrive a few minutes later at Korin's office to find her in a fight with the holo interface."

            $renpy.sound.play("<to 3>audio/sfx/phone 01.mp3", channel="sfx1")
            $renpy.sound.play(["<silence 2>","audio/sfx/phone 02.mp3"], channel="sfx2")
            $renpy.sound.play(["<silence 1>","audio/sfx/phone 05.mp3"], channel="sfx3")
            "Notifications ring like klaxons. Messages and appointments zip around the room like a hurricane."
            "Korin's muttering to herself as she tries to pull up different settings and wrangle filters."

            show bird normal:
                pos(1100, 20)
                easein 0.8 pos(650, 30)
                easein 0.6 pos(850, 200)
                easein 0.4 pos (720,280)
            "Baby Bird zips around, pecking the air and trying its best to help wrangle the high-priority messages."

            show korin nojacket pin sad at centre:
                easein_back 0.6 left2
                easein_back 0.6 centre
            show bird normal:
                pos(720, 280)
                easein 0.4 pos(720, 120)
            "I watch Korin jump around, frantically trying to silence each one, but it's no use."
            show bird normal:
                pos(720, 120)
                easein 0.4 pos(850, 200)
            "I see everything--meetings, reminders, even fieldwork blocks on her calendar."
            "But it's not all business. She's tracked birthdays, anniversaries, private appointments..."

            hide korin
            hide bird
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(...Was that a date?)"
            hide ecmc

            show ecmc jacket_v2 pin basic at centre
            "Since Korin hasn't noticed me yet, I sneak a peek at one of the little heart-shaped notifications."
            hide ecmc

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(Yep. She puts dates in her calendar.)"

            show ecmc jacket_v2_cu surprised_cu
            "(I don't see a lot of names showing up more than once, though...)"

            hide ecmc
            show ecmc jacket_v2 pin sleep at centre
            "I shake my head and snap out of it."

            hide ecmc
            show ecmc jacket_v2_cu determined_cu at ecmc_cu
            "(Gotta focus. I came here to help Korin! Her personal life is none of my business.)"
            hide ecmc

            show ecmc jacket_v2 pin determined at centre
            "Still unnoticed, I use a hand-gesture to pull down the holo settings and mute the interface."

            hide ecmc
            show korin nojacket pin surprised at centre
            show bird normal at centre, birdbob:
                xoffset 200 ypos 200
            "Korin whirls around in surprise."
            ko "[genericfn]!"

            hide bird
            show korin nojacket pin surprised at right3
            show ecmc jacket_v2 pin determined at left3
            "The notifications keep popping up around us like a lights show, but at least now it's quiet."

            show korin nojacket pin smile at right3:
                easein_back 0.4 right1plus
            show ecmc jacket_v2 pin basic
            "Korin collapses on the edge of her desk in relief and lets out a laugh."
            ko "How much of my panic dance did you see?"

            show ecmc jacket_v2 pin smile
            mckorin "Oh, I saw enough."
            ko "Good thinking with the...silencing thing. I just got kind of overwhelmed."

            show ecmc jacket_v2 pin determined
            mckorin "I don't blame you. What happened?"

            show korin nojacket pin sad
            ko "Well, that's what I was hoping you could tell me..."

            show ecmc jacket_v2 pin headset determined
            "I put on my ARCware and connect to Korin's desk."
            ko "I know how this must look..."
            ko "Obviously, every D.I.V.A.A. agent has to have a solid background in tech, I'm just not great with troubleshooting."
            "I nod in understanding."

            show ecmc jacket_v2 pin headset smile
            mckorin "We all have our specialties."
            mckorin "I'd be interested to hear what yours is, though."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu headset_cu blush_cu embarrassed_cu at ecmc_cu
            "(...Did I just say that out loud?)"
            hide ecmc

            show ecmc jacket_v2 pin headset blush embarrassed at left3
            show korin nojacket pin smirk at right1plus
            "Korin gives me a coy look."
            ko "Oh, you'll learn soon enough..."
            "I hope my ARCware is hiding my sudden blush. Korin clears her throat."

            show korin nojacket pin surprised
            ko "In training, I mean. I'll do a whole unit on it."

            hide ecmc
            show ecmc jacket_v2 pin headset surprised at left3
            mckorin "Oh! Got it."

            show korin nojacket pin basic
            show ecmc jacket_v2 pin headset smile
            mckorin "I mean, I think I found your problem."

            show ecmc jacket_v2 pin headset determined
            "I scroll through the logs, then point out a specific item to Korin."
            mckorin "IT pushed through an update that futzed with your settings and loaded everything from an old backup."
            mckorin "So your desk is playing catch-up from the last...three months."

            show korin nojacket pin smile
            ko "So what I'm hearing is...it wasn't my fault?"

            show ecmc jacket_v2 pin headset sleep
            "I shake my head."

            show ecmc jacket_v2 pin headset determined
            mckorin "IT's fault, if you really want to get petty about it."

            show korin nojacket pin smile behind ecmc at left3:
                easein_back 0.4 left1 xoffset 40
            "Korin throws her hands over her head in victory, then clasps me by the shoulders."
            ko "I never thought I'd get to hear those simple, beautiful words."
            ko "Thank you, [genericfn]. You're a lifesaver."

            show bird normal at left1:
                xoffset 500 yoffset 90
                easein 0.4 xoffset 140
            "Korin drops her hands as Baby Bird flashes and sings a cheerful little tune."

            show korin nojacket pin surprised
            ko "What does that mean?"

            show ecmc jacket_v2 pin headset smile
            mckorin "It's programmed to sing that when you've managed all priority issues in your calendar and completely cleared your inbox."

            show korin nojacket pin smile
            "Korin laughs."
            ko "Well, no wonder I've never heard it."
            ko "Thank you again. You're much more help than Enver."

            show ecmc jacket_v2 pin headset surprised
            "I raise an eyebrow."

            show korin nojacket pin smirk
            ko "I mean, he helped, but..."

            show ecmc jacket_v2 pin headset smile
            mckorin "Oh, trust me. I know exactly what you mean."
            ko "He certainly knows how to turn a five-minute fix into two hours of chatting."

            show korin nojacket pin surprised
            "Korin rushes to explain herself."
            ko "Not that I'm saying you need to leave...feel free to stay as long as you'd like."
            mckorin "Well...what else can I help with?"

            hide korin
            hide bird
            hide ecmc
            show ecmc jacket_v2_cu headset_cu determined_cu at ecmc_cu
            "(Okay, relax. No need to get quite so eager with her...)"
            hide ecmc

            show korin nojacket pin basic at left1:
                xoffset 40
            show bird normal at left1:
                xoffset 140 yoffset 90
            show ecmc jacket_v2 pin headset smile at left3
            ko "How's that incident report coming along?"

            show ecmc jacket_v2 pin headset sad
            "My heart starts dropping frames."

            hide korin
            hide bird
            hide ecmc
            show ecmc jacket_v2_cu headset_cu sad_cu at ecmc_cu
            "(She's so impressed with me. I don't want to ruin it...)"
            hide ecmc

            show korin nojacket pin basic at left1
            show bird normal at left1:
                xoffset 100 yoffset 90
            show ecmc jacket_v2 pin headset surprised at left3
            mckorin "Um. Fine! It's fine."

            show korin nojacket pin surprised
            ko "You sure?"

            show ecmc jacket_v2 headset smile
            mckorin "Totally! Definitely. Just, you know how long it is..."
            "I jab a thumb over my shoulder."
            mckorin "Actually, I should probably...get back to work on it..."

            show korin nojacket pin angry
            "Korin narrows her eyes, scrutinizing me as I back toward the door."
            ko "Well, don't let me keep you, Scraps."

            hide ecmc
            hide bird
            hide korin
            show korin nojacket_cu smile_cu at korin_cu
            ko "But come back anytime."

        "B. I'm not the Information Technology department.":
            $menuhideborder = False
            show ecmc jacket_v2 pin basic at left3
            show korin nojacket pin sad at holo_mask, korin_holo, right3
            mckorin "Sorry, I really need to finish this report..."
            "Korin looks dejected, but gives me a thumbs-up."
            show korin nojacket pin smile at holo_mask, korin_holo, right3
            ko "Got it. Totally understand. Best of luck!"

    stop music
    play music ecmcalmeveryday4
    scene bg ecm_office_hq_on at bg with fade
    "More than an hour later, the office is practically empty and I'm still working on my report."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Didn't Korin tell me at orientation that she'd help me out with anything? Anything at all?)"
    hide ecmc

    show ecmc jacket_v2 pin sad at centre
    "A thrill runs through me at the simple thought of it."

    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(What is my problem? Why is this such a big deal?!)"
    "(Enver was right. I could just go. Right now. I could just stand up right now and do it. Nothing is stopping me.)"
    hide ecmc

    show ecmc jacket_v2 pin determined at centre
    "I take a deep breath, seize the rare burst of inspiration, and force myself up."

    scene bg ecm_records_room_on at bg
    show korin nojacket pin smirk at centre
    with wiperightdissolve
    "I pass by the D.I.V.A.A. server room and spot Korin through the open door."

    hide korin
    show eko jacket_cu glasses_cu surprised_cu at eko_cu
    "My view is blocked suddenly by a wide-eyed android on her way out."
    "She analyzes my jacket and badge, then smiles."
    hide eko

    show eko jacket pin glasses smile at right3
    show ecmc jacket_v2 pin surprised at left3
    ek "Hello, Hatchling. I'm Eko. Are you lost?"

    hide eko
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Right, the colors give away my rank.)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left3
    show eko jacket pin glasses smile at right3
    mckorin "Hi, Eko. I'm [genericfn]. And thanks, no, I'm just trying to talk to Korin..."
    ek "Oh! I was just assisting her. Well, let me get out of your way."

    show eko jacket pin glasses smile at right3:
        parallel:
            easein 0.8 xoffset 200
        parallel:
            linear 0.8 alpha 0.0
    "Eko steps aside, and I step into the records room."

    hide eko
    hide ecmc
    show korin nojacket pin basic at centre:
        yoffset 80
    show bird normal at centre:
        xoffset 180 yoffset 280
    "Inside, Korin is crouched down as BB interfaces with a unit closer to the floor."

    show korin nojacket pin basic at right1plus
    show bird normal at right1plus
    show ecmc jacket_v2 pin basic at left3
    "Korin spots me and settles back on her heels."

    show korin nojacket pin smile
    ko "Oh, hey! What are you doing here?"

    show ecmc jacket_v2 pin surprised
    mckorin "Um...I was looking for you. You busy?"
    "She aims a thumb at Baby Bird."

    show korin nojacket pin basic
    show ecmc jacket_v2 pin basic
    ko "Just pulling a filter for some old records with data I wanted to try and massage on my own."

    show korin nojacket pin sad
    ko "It's just a {i}lot{/i} of data. I'm a little worried about my desk acting up again..."
    ko "So I'm seeing if BB here can pull the files on a portable drive."

    show korin nojacket pin basic
    ko "But...you were looking for me?"

    show ecmc jacket_v2 surprised
    mckorin "Yeah, I um..."

    hide korin
    hide bird
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Just say it. Just spit it out!)"
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show korin nojacket pin basic at right1plus:
        yoffset 80
    show bird normal at right1plus:
        xoffset 180 yoffset 280
    mckorin "I need help."

    show ecmc jacket_v2 pin sad at left3:
        easein 0.6 left1
    pause 0.6
    show korin nojacket pin basic at right1plus:
        easein 0.6 yoffset 0
    "She reaches for me, and I reflexively reach back with a hand to help her up."
    show korin nojacket pin basic at right1plus:
        rotate 0 transform_anchor True anchor(0.5, 1.0) xpos stagepos[1]+140 ypos 1220
        linear 1.0 rotate -3
    "Her hand stays in mine a little longer as she teeters on her heels."

    show korin nojacket pin surprised at right1plus:
        anchor(0.5, 1.0) xpos stagepos[1]+140 ypos 1220 rotate -3
        linear 1.0 rotate 0
    ko "Oof, sorry. My legs are asleep."

    show korin nojacket pin basic
    "I look down to make sure she's steady. Korin smooths out her skirt."

    show ecmc jacket_v2 basic
    "I drag my eyes back up to her face as she brushes a lock of hair behind her ear."

    hide korin
    hide bird
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Has she always been this tall?)"
    hide ecmc

    show korin nojacket_cu smile_cu at korin_cu
    "I look up at her, caught in her warm gaze..."
    ko "Whatcha need help with, Scraps?"
    hide korin

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Um...)"
    "(...Why was I here again?)"
    hide ecmc

    $menuhideborder = True
    menu korins1e2c3:
        "A. Where's the bathroom?":
            $menuhideborder = False

            show ecmc jacket_v2 pin surprised at left1
            show korin nojacket pin basic at right1plus
            show bird normal at right1plus:
                xoffset 180 yoffset 280
            mckorin "Where's the bathroom?"

            show korin nojacket pin surprised
            ko "First left out of the office. You'd have passed it on your way here."
            ko "We covered it in our walkthrough during orientation."

            show ecmc jacket_v2 pin embarrassed
            mckorin "Oh. Yeah! Duh."

        "B. How late can I stay here?":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left1
            show korin nojacket pin basic at right1plus
            show bird normal at right1plus:
                xoffset 180 yoffset 280
            mckorin "How late am I allowed to stay here?"
            show korin nojacket pin surprised
            ko "What, at HQ?"
            "She shrugs."
            show korin nojacket pin smirk
            ko "It's a 24-hour operation...but I wouldn't recommend staying later than midnight during training."

        "C. Any more trouble with your desk?":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left1
            show korin nojacket pin basic at right1plus
            show bird normal at right1plus:
                xoffset 180 yoffset 280
            mckorin "Any more trouble with your desk?"
            show korin nojacket pin smile
            "Korin laughs bitterly and shakes her head."
            ko "Nothing yet. Enjoying the peace while I can."

    show ecmc jacket_v2 pin smile at left1
    show korin nojacket pin smile at right1plus
    show bird normal at right1plus:
        xoffset 180 yoffset 280
    mckorin "Thanks! Well. Back to my report!"

    show korin nojacket pin surprised
    ko "You're still working on it?"
    mckorin "Yup. See ya!"

    stop music
    play music ecmemotional2
    scene bg ecm_office_hq_off at bg
    show ecmc jacket_v2 pin sad at centre
    with wiperightdissolve

    "I watch the minutes tick down as the office grows dark."

    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Still no closer to finishing...)"
    hide ecmc

    show ecmc jacket_v2 pin angry at centre
    "I'm about to start tearing my hair out."
    hide ecmc

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Why can't I just get my head on straight and ask Korin what I should have asked her hours ago?)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at centre
    "I look at the clock."

    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Okay, seriously. It's now or never.)"

    scene bg ecm_dorm_hallway_on at bg with wiperightdissolve
    "I find my way to Korin's office and pace outside of it, psyching myself up to knock."

    show anton casual basic at centre:
        alpha 0.0 yoffset 50
        parallel:
            easein_back 0.8 yoffset 0
        parallel:
            linear 0.8 alpha 1.0
    "Someone rounds the corner."

    show anton casual angry
    "He freezes...and so do I. His brow furrows into a scowl."

    show ecmc jacket_v2 pin surprised at left3
    show anton casual angry at right4
    wasntexpecting "...Hello."

    show ecmc jacket_v2 pin smile
    mckorin "Um...nope! Thanks."
    judgymuch "Problem, Hatchling?"

    show ecmc jacket_v2 pin determined
    mckorin "...I need to talk to Korin."
    andhardcase "Phoenix Reyes, you mean."
    mckorin "Right. Phoenix Reyes."

    show anton casual smile
    hardcase "Well, a bit of advice, rookie..."
    show anton casual smile behind ecmc:
        easein_back 0.4 right3
    "He smiles and takes a step closer."
    hide ecmc
    hide anton

    show anton casual_cu angry_cu at anton_cu
    hardcase "If you want something, don't block up the halls. Get out of the way and go {i}ask.{/i}"
    hide anton

    show korin nojacket pin basic at centre:
        alpha 0.0 yoffset 50
        parallel:
            easein_back 0.8 yoffset 0
        parallel:
            linear 0.8 alpha 1.0
    "The door to Korin's office zips open."

    show korin nojacket pin surprised
    ko "Hey, Anton. Hey, [genericfn]. You guys are here late..."

    hide korin
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "I feel a blush flood my cheeks, and wonder whether it's from Anton being such a jerk or from the sudden appearance of Korin."
    hide ecmc

    show korin nojacket pin basic at left3
    show anton casual basic at right4
    an "Rookie here says she's staying late finishing a report. She also says she needs to ask you for something."

    hide anton
    hide korin
    show korin nojacket_cu surprised_cu at korin_cu
    "I feel Korin's eyes on me, heavy with curiosity, before I meet them with my own."
    ko "[genericfn], is that true?"
    hide korin

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Am I actually going to ask her this time?)"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

