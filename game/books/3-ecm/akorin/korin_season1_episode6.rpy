label korin_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_stairway_on at bg
    play music ecmsuspense1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "Korin gestures for me to go, and I leave her in Connie's clutches."

    show ecmc jacket_v2 pin sad at centre
    "I head straight to the lab, eager to get away from Connie... but reluctant to leave Korin behind."

    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(It's fine. She can handle herself.)"
    "(...What am I headed into with Gael, though?)"
    hide ecmc

    $menuhideborder = True
    menu korins1e6c1:
        "A. SHE KNOWS!":
            $menuhideborder = False
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(Is that what this is? Gael knows Korin is helping me, and she and Connie are separating us to see if our stories match up?!)"
            "I feel myself grow clammy with fear."
        "B. It's a status report.":
            $menuhideborder = False
            show ecmc jacket_v2_cu determined_cu at ecmc_cu
            "(It's probably a status report. Nothing to report. Nothing to worry about.)"
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(Wait, no, I do have progress to report on. Yikes!)"
        "C. I'm about to get bullied.":
            $menuhideborder = False
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(Gael's probably freed up time in her schedule, and now she wants to grill me.)"
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "I drag my feet, not eager for Gael's undivided attention that I'm sure is coming my way."

    stop music
    play music ecmplottwist2

    scene bg ecm_office_lab_on at bg
    show anton casual basic at left1plus:
        xoffset -10
    show gael uniform basic glasses at right3:
        xoffset 20
    with doors_open

    "When I enter the lab, I look around for Eko, but am met with only Gael and..."

    hide anton
    hide gael
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Great. Anton's here.)"

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Wait. Why is Anton here?)"
    hide ecmc

    show ecmc jacket_v2 pin basic at left3
    show gael uniform basic glasses at right3:
        xoffset 20
    ga "[genericfn], finally. Is there anything you'd like to tell us?"

    show ecmc jacket_v2 pin surprised at left3
    "My mouth goes dry."

    hide gael
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Does she know I went to visit Skye without her?)"
    hide ecmc

    show ecmc jacket_v2 pin surprised at left3
    show gael uniform basic glasses at right3:
        xoffset 20
    "I look between her and Anton, hoping I can sell my confusion."
    mckorin "Um... no?"

    show gael uniform sad glasses at right3:
        xoffset 20
    "Anton and Gael share a look."

    show gael uniform angry glasses at right3:
        xoffset 20
    ga "If there's {i}anything{/i} you'd like to admit to, now would be the time."

    hide gael
    hide ecmc
    show anton casual_cu angry_cu at anton_cu
    "Anton keeps his steely gaze on me, making Gael seem comparatively reasonable."
    hide anton

    show ecmc jacket_v2 pin sleep at left3
    show gael uniform angry glasses at right3:
        xoffset 20
    "I take a breath, thinking."

    hide gael
    hide ecmc
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(They don't know anything. What would Anton have to do with my interview with Skye?)"
    "(And if someone knew about me and Korin, we'd be answering to Dom, not Gael.)"
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show gael uniform angry glasses at right3:
        xoffset 20
    mckorin "...Look, I really don't know what this is about. How about we just all get on the same page?"

    show gael uniform sad glasses at right3:
        xoffset 20
    "Gael sighs."
    ga "The hard drive is missing."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "I... what?"

    show gael uniform angry glasses at right3:
        xoffset 20
    ga "The drive is missing, and our logs show that you were the last person to touch it."
    "I'm hit with relief that this isn't about Korin--but stunned about the actual issue."

    show ecmc jacket_v2 pin embarrassed at left3
    mckorin "Wait, that can't..."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "The logs have to show that I checked it back in, right? I'm sure I did!"

    show gael uniform sad glasses at right3:
        xoffset 20
    ga "They do, but..."

    hide gael
    show anton casual angry at right3:
        xoffset 20
    an "Look, rookie. If you logged the drive back but secretly took it to do work with your black market friends, you need to tell us."

    hide anton
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Jeez, what is this, Bad Cap and Worse Cop?)"
    hide ecmc

    show ecmc jacket_v2 pin angry at left3
    show anton casual angry at right3:
        xoffset 20
    mckorin "I didn't. I wouldn't!"

    show ecmc jacket_v2 pin surprised at left3
    hide anton
    show gael uniform angry glasses at right3:
        xoffset 20
    ga "Then... maybe you thought you logged it back in but packed it away by mistake?"

    show ecmc jacket_v2 pin determined at left3
    "I throw my bag on the nearby table and start unloading my belongings."
    mckorin "Search me, if that's what you want. I don't have it. I logged it out, then logged it back in when I was done."
    mckorin "Is someone else working on this case that I don't know about? Who noticed it was missing?"
    ga "I requisitioned the drive to catalogue my progress brief to the F.D.I."
    ga "Anton here was sent to pick it up."

    hide ecmc
    show anton casual angry at left1plus:
        xoffset -10
    "Anton speaks directly to Gael."
    an "This is precisely the problem with D.I.V.A.A. giving a rookie a second chance like this."
    ga "You say this as if it was my decision. It wasn't."

    hide anton
    hide gael
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(I'm standing right here, you know.)"
    hide ecmc

    show anton casual angry at left1plus:
        xoffset -10
    show gael uniform angry glasses at right3:
        xoffset 20
    an "You should requisition badge access logs for her. See if she was sneaking around somewhere she shouldn't have been."
    "Gael stares hard at him."
    ga "Thanks for your input."

    hide gael
    hide anton
    show anton casual_cu angry_cu at anton_cu
    "Anton looks at me."
    an "After all, everyone here knows your chances of recovering anything from that drive are slim to none..."
    hide anton

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(What is he saying?)"
    hide ecmc

    show ecmc jacket_v2 pin determined at left3
    show gael uniform angry glasses at right3:
        xoffset 20
    "Gael picks up on it first."

    show ecmc jacket_v2 pin surprised at left3
    ga "Look, if you did this thinking it'd buy you more time to think of a solution, or absolve you of having to prove yourself..."

    show ecmc jacket_v2 pin surprised at left3
    "I stamp my foot down, frustrated to my boiling point."

    show ecmc jacket_v2 pin angry at left3
    mckorin "I didn't!"

    hide ecmc
    show anton casual angry at left1plus:
        xoffset -10
    "Gael and Anton look at someone over my shoulder who's just entered the lab."

    hide anton
    hide gael
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Maybe it's Eko. Maybe she'll listen to me...)"
    hide ecmc

    stop music
    play music ecmaction1

    show korin nojacket pin basic at centre
    "I turn around and feel like I could collapse with relief."
    ko "...I came to collect [genericfn] to catch her up on what she missed in training today."

    show korin nojacket pin surprised at centre
    ko "Is this a bad time?"

    hide korin
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(No! It's a very good time! The best time!!)"
    hide ecmc

    show korin nojacket pin surprised at left3
    show anton casual angry at right3:
        xoffset 32
    ga "We need her a little longer, Reyes."
    ko "What's going on?"

    hide anton
    show gael uniform angry glasses at right3:
        xoffset 20
    ga "That's classif--"

    hide korin
    show ecmc jacket_v2 pin angry at left3
    "I take my chances and interrupt Gael."

    hide gael
    hide ecmc

    $menuhideborder = True
    menu korins1e6c2:
        "A. I didn't do it!":
            $menuhideborder = False
            show ecmc jacket_v2 pin angry at left3
            show korin nojacket pin surprised at right3
            mckorin "I didn't do it, I swear!"
            ko "Whoa, slow down. I thought we already established that the drive wiped itself?"
            "Korin takes stock of our blank expressions."

            show korin nojacket pin angry at right3
            ko "...Or is this about something else?"

        "B. I might have screwed up.":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad at left3
            show korin nojacket pin surprised at right3
            mckorin "I'm really worried I screwed something up."
            an "Good! You should be!"

            show korin nojacket pin angry at right3
            ko "Anton, please. That's not helpful. What's happened?"

        "C. These two seem to be confused.":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad at left3
            show korin nojacket pin angry at right3
            mckorin "These two seem to be confused that I'm responsible for some sort of mistake in the lab."

    hide korin
    show gael uniform angry glasses at right3:
        xoffset 20
    ga "We're just asking you some clarifying questions. This isn't helping your case, you know."

    hide ecmc
    show korin nojacket pin surprised at left3
    ko "Excuse me? What case?"

    hide korin
    hide gael
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    mckorin "The hard drive is gone, and Gael and Anton here think that I took it."
    hide ecmc

    show ecmc jacket_v2 pin sad at left3
    show korin nojacket pin surprised at right3
    "Korin raises her eyebrows and looks back at the two of them."

    show korin nojacket pin smirk at right3
    ko "Interesting. Why do you think that?"

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(She's taking me at my word! I could kiss her.)"

    show ecmc jacket_v2_cu blush_cu surprised_cu at ecmc_cu
    "(I mean... figuratively.)"
    hide ecmc

    show korin nojacket pin smirk at left3
    show gael uniform angry glasses at right3:
        xoffset 20
    ga "The logs show that she was the last one to touch the hard drive."

    show korin nojacket pin surprised at left3
    ko "Huh. Did she not check it back in, or something?"

    hide gael
    show anton casual angry at right3:
        xoffset 32
    an "She's the one who destroyed the evidence. Who would stand to benefit from it being gone more than her?"

    hide anton
    hide korin
    show korin nojacket_cu surprised_cu at korin_cu
    "Korin points at me."
    hide korin

    show korin nojacket pin surprised at left3
    show anton casual angry at right3:
        xoffset 32
    ko "Her?"
    ko "The rookie who's losing sleep because her entire future at D.I.V.A.A. is predicated on recovering something from that drive?"
    ko "{i}That{/i} rookie?"

    show korin nojacket pin sad at left3
    "Korin folds her arms, looking unimpressed."

    show anton casual sad at right3:
        xoffset 32
    "Anton and Gael are silent."
    ko "Just want to make sure we're talking about the same person, here."

    show anton casual angry at right3:
        xoffset 32
    an "I'm just saying, she's new."

    hide anton
    show gael uniform sad glasses at right3:
        xoffset 20
    ga "Exactly. I'm willing to forgive a mistake."

    show korin nojacket pin smile at left3
    ko "Oh! That's good to hear."
    ko "Because I know you two are skilled agents, and surely you wouldn't try and pin motive to a suspect with zero evidence."
    ko "Right?"

    hide korin
    hide gael
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(Get 'em, Korin!)"
    hide ecmc

    show korin nojacket pin smile at left3
    show anton casual angry at right3:
        xoffset 32
    an "Maybe we should just search her belongings--"

    show anton casual angry behind korin at right3:
        xoffset 32
        linear 0.4 xoffset -30
    pause 0.1
    show korin nojacket pin angry at left3:
        ease 0.4 xoffset 75
        easein 0.2 xoffset 70
    "Anton makes a move for my bag, but Korin cuts him off, both physically and verbally."
    ko "No, I think that's unnecessary."

    hide anton
    show gael uniform angry glasses at right3:
        xoffset 20
    show korin nojacket pin angry at left2:
        xoffset 0
    "She looks directly at Gael."
    ko "You should take this up with the head of the lab. And you should also probably tell F.D.I. that this happened on your watch."

    show korin nojacket pin smirk at left2
    ko "Or, you could both take a breather and wait a day for the drive to turn up. Like things often do."

    show gael uniform sad glasses at right3:
        xoffset 20
    "Gael winces and rubs her temples."
    ko "I mean, what's more plausible..."
    ko "That our inter-office collection system temporarily misplaced a piece of evidence?"
    ko "Or that someone with ill intent managed to break into one of the most secure buildings in the city just to tamper with a single bricked hard drive?"
    ga "For the record, that was never my theory."

    hide korin
    hide gael
    show anton casual_cu angry_cu at anton_cu
    "Anton points at me."
    hide anton

    show korin nojacket pin basic at left3
    show anton casual angry at right4
    an "But she was the last one to lay her hands on it!"
    ko "I can vouch for the whereabouts of [genericfn] for most of the day."

    hide anton
    show gael uniform sad glasses at right3:
        xoffset 20
        easein 0.4 xoffset 55
    "Gael throws up her hands and takes a step back, defeated."

    show gael uniform angry glasses at right3
    ga "You better be thankful I've got such a soft spot for this place."
    ga "If it doesn't turn up, though, I'm going to have to run it up the chain at the F.D.I."

    hide korin
    hide gael
    show gael uniform_cu angry_cu glasses_cu at gael_cu
    "She points at me."
    ga "And seriously. {i}Be more careful.{/i}"
    hide gael

    show anton casual angry at centre
    "Anton turns away with a scowl."

    hide anton
    show anton casual_cu angry_cu at anton_cu
    an "Waste of time..."
    hide anton

    stop music
    play music ecmemotional2

    show ecmc jacket_v2 pin sad at left3
    show korin nojacket pin basic at right3
    "Korin stays by my side as they both leave the lab. I'm thankful she came to my rescue, but..."
    mckorin "So. This went from being only kind of impossible to being completely impossible."
    "Korin doesn't respond right away. My breathing grows rapid."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "Korin... how am I supposed to extract evidence from the drive if it's gone?!"

    show korin nojacket pin smirk at right3
    ko "D.I.V.A.A. is a very secure building. We have a ping system in place for evidence going offsite."
    ko "If you had accidentally slipped it in your bag before leaving today, we'd know all about it."

    show ecmc jacket_v2 pin sad at left3
    mckorin "So it's somewhere here for sure, then?"
    mckorin "We gotta find it. I bet if we start searching right now, turn this place inside out..."

    show korin nojacket pin surprised at right3
    ko "...You'll end up pissing off every other detective trying to do their job today?"
    mckorin "I mean, what am I supposed to do? Just go home and wait for it to turn up?"

    show korin nojacket pin basic at right3
    ko "Maybe... take a step back? Clear your head and ground yourself?"
    "She tilts her head as she looks at me."

    show korin nojacket pin sad at right3
    ko "It's been a hard few days, hasn't it?"

    show ecmc jacket_v2 pin sleep at left3
    "I nod and close my eyes, trying not to completely break down."
    ko "Here. Come with me."

    show ecmc jacket_v2 pin sad at left3
    mckorin "Where?"
    ko "Somewhere I go when I need to clear my head."

    hide ecmc
    hide korin
    "I'm lost in my own thoughts as Korin leads me out of HQ..."

    scene bg ecm_elysian_park_day at bg with wiperightdissolve

    "...To Elysian Park, just a stone's throw away."

    show ecmc jacket_v2 pin sad at left3
    show korin jacket pin sad at right3
    "We walk on the path overlooking the city. Korin keeps looking over at me with concern, but stays silent for the moment."
    "I look around the park, trying to take in my new surroundings."

    show ecmc jacket_v2 pin basic at left3
    mckorin "I can't remember the last time I was here."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "You said you come here to relax?"

    show korin jacket pin basic at right3
    "Korin nods slowly."
    ko "The view of the city is something else, but mostly I come to people-watch."
    ko "When you spend all your time around people who are either victims, perpetrators, or investigators of some kind of crime..."

    show ecmc jacket_v2 pin basic at left3
    show korin jacket pin smirk at right3
    ko "It's nice to be reminded that there's other components of life. People whose lives are unaffected by all that misery."
    ko "People walking their pets, going to work, walking hand in hand with someone they love..."
    "I watch her wistful expression as she watches one such couple walk by, talking happily as their latched hands swing between them."
    ko "I find it grounding."

    show korin jacket pin smile at right3
    ko "Reminding yourself why you're doing what you're doing... and that there's a whole world outside of it."

    show korin jacket pin sad at right3
    "She looks over at me again, tilting her head."
    ko "How you holding up, Scraps?"

    show ecmc jacket_v2 pin embarrassed at left3
    mckorin "I'm in way over my head."
    mckorin "Like you said, I'm trying to do everything by the book, triple-check my methods, only take risks when it's absolutely necessary..."
    mckorin "And it's just one bad thing after another. And I'm powerless to do anything to fix it."

    show korin jacket pin surprised at right3
    ko "Well, come on. That's not true."

    show ecmc jacket_v2 pin determined at left3
    mckorin "Really? I mean, what can I do to get that hard drive back?"
    ko "That's not what I'm talking about. You just said you were powerless... and I said you aren't."

    show korin jacket pin smile at right3
    ko "You have the power to give yourself a break. Frame this moment differently."
    ko "Yes, it's troubling that this hard drive is gone. But it hasn't left D.I.V.A.A., and it's a matter of waiting for it to turn up again."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    ko "So I'd say you could use this time to give yourself a break, but... you're a go-getter, aren't you? That's hard for you to do."
    hide korin

    show ecmc jacket_v2 pin blush embarrassed at left3
    show korin jacket pin smile at right3
    "I flush, and it's nothing to do with being around Korin, and everything to do with how naked I feel with her."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(Like she can read everything about me just by looking at me.)"
    "(...I really hope she can't read {i}everything{/i} about me.)"
    hide ecmc

    show ecmc jacket_v2 pin blush embarrassed at left3
    show korin jacket pin sad at right3
    ko "Well, we've talked about how crucial it is not to focus on work every single minute, right? That leads to burnout."

    hide ecmc
    show ecmc jacket_v2 pin sad at left3
    mckorin "Easier said than done."
    ko "Yeah, but when I say it's crucial, I don't just mean in theory."

    show korin jacket pin basic at right3
    ko "When you become a detective, you owe it to your clients to give your best to a case. The stakes couldn't be higher."
    ko "So how can you give everything if you're already spreading yourself thin by hauling these things with you?"

    show ecmc jacket_v2 pin sad at left3:
        easein 0.4 left1
    "I slump forward, lacing my hands and hanging them on the back of my neck."

    show korin jacket pin basic behind ecmc at right3:
        easein 0.4 right1
    "Goosebumps rise on my skin as I feel Korin's hand on my back, tentative but comforting."

    stop music
    play music ecmkorintheme

    hide ecmc
    hide korin
    show korin jacket_cu smirk_cu at korin_cu
    ko "I'm not saying it's easy, Scraps. Nothing worthwhile ever is. But it's necessary."
    hide korin

    show ecmc jacket_v2 pin embarrassed at left1
    show korin jacket pin smirk behind ecmc at right1
    mckorin "It's an adjustment for me. Problems, even complex ones, don't get solved by hitting the brakes."
    "Korin chuckles."

    show korin jacket pin smile at right1
    ko "They do if you're about to crash!"

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(...Okay, she may have a point there.)"
    hide ecmc

    show korin jacket pin smile behind ecmc at right1
    show ecmc jacket_v2 pin embarrassed at left1
    "I stand upright again and look Korin in the eyes."
    mckorin "Until you came in, I thought Gael and Anton were going to eat me alive."

    show korin jacket pin basic at right1
    "Korin nods knowingly."

    show korin jacket pin sad at right1
    ko "It's very normal to feel overwhelmed, especially when you're being accused."

    show ecmc jacket_v2 pin smile at left1
    mckorin "I just wish I could handle them like you did. You just... made them shut right up."
    ko "Yeah, but I've had practice in that. Believe it or not, I've been in your shoes before."

    show ecmc jacket_v2 pin surprised at left1
    ko "I know what it's like to be inundated by your feelings. Talking about it can help, sometimes."
    "Korin stops as we reach a bench off the path."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    ko "Want to stop for a second? We can talk about it a bit more, if you'd like."
    hide korin

    $menuhideborder = True
    menu korins1e6c3:
        "A. Stay and take a breather with Korin!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin jacket_cu smile_cu at korin_cu
            "I nod, and seeing Korin's smile floods me with relief."
            hide korin

            show korin jacket pin basic behind ecmc at right1plus
            show ecmc jacket_v2 pin basic at left2
            "I throw myself down on the bench. Korin lets me get comfortable before settling beside me."

            show korin jacket pin sad at right1plus
            "I slouch forward, and Korin tucks one leg underneath her as she twists to face me, one arm slung over the backrest."
            ko "Take a second and ground yourself, okay?"

            show ecmc jacket_v2 pin sad at left2
            "I nod but frown, not really sure what she means."
            "Lucky for me, she explains..."
            ko "Just kind of take stock of where you are, physically. What you're feeling."
            ko "You feel the ground under your feet. The bench beneath you. The wind on your face."
            "I feel it, taking note of each sensation in turn."

            show korin jacket pin surprised at right1plus
            ko "What else?"

            show ecmc jacket_v2 pin embarrassed at left2
            mckorin "My whole body just feels {i}heavy{/i}. My gut feels cold, almost painful."

            show korin jacket pin basic at right1plus
            "Korin nods, like this is normal."
            ko "Good."

            show ecmc jacket_v2 pin surprised at left2
            mckorin "Good??"

            show korin jacket pin smile at right1plus
            ko "That you're acknowledging it. That it feels bad, and you're recognizing that, and not trying to tune it out or push it down."
            ko "Now, work on your other senses. Sound, smell, sight..."

            show ecmc jacket_v2 pin sleep at left2
            "I close my eyes and listen. People pass us, and I catch snippets of conversation here and there."

            hide ecmc
            hide korin
            infl "...Like, hello?? I came up with the idea with telling my followers to stay hydrated..."
            infl "And in her next video, what advice does she give? That's right..."
            techbro "...I'm like, of course I'm selling your data! What are you going to do, peddle it on the street yourself?"
            blew_interview "...Turns out they wanted {i}cache{/i} handling experience, not c-a-s-h handling..."

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "I stifle a snort of laughter."
            hide ecmc

            show korin jacket pin sad behind ecmc at right1plus
            show ecmc jacket_v2 pin smile at left2
            "I drag my head up and see Korin pressing her lips together, shaking her head in sympathy."
            "I look beyond the path. The city sprawls before us, glistening and silver in the afternoon sun."

            show ecmc jacket_v2 pin surprised at left2
            "My eyes are drawn to a holosculpture with pink tendrils crawling hypnotically skyward."

            show korin jacket pin surprised at right1plus
            "Korin follows my eyes."

            show korin jacket pin smirk at right1plus
            ko "It's even better at night."

            show ecmc jacket_v2 pin smile at left2
            mckorin "We should come back and see it sometime."
            "I breathe deep and smell... nature. Freshly cut grass, water from the pond..."
            "A breeze whispers by, and for a second I catch the faintest scent of Korin, almost blending in with the smell of flowers."
            "And there's something else. Nudging slightly against my leg is Korin's knee."
            "Normally, my heart would be racing at the thought, but right now with her, it just makes me feel at peace."

            show korin jacket pin smile at right1plus
            ko "What are you feeling now?"
            "I really think about it. My anxiety is still there, still real, but it's... not taking up all the space in my mind."

            hide korin
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(How could it... when Korin's here, sitting this close to me, making sure that I'm okay?)"
            hide ecmc

            show ecmc jacket_v2 pin sad at left2
            show korin jacket pin smile behind ecmc at right1plus
            mckorin "I just wish none of this was happening."

            show korin jacket pin smile at right1plus:
                ease 0.4 right1 xoffset -30
            "She pats my back."

            show korin jacket pin smirk at right1
            ko "Totally normal."
            ko "Now, can you accept that it {i}is{/i} happening?"
            "I think about what she's really saying to me."
            mckorin "Ever since my first day, it's all just felt like this weird nightmare."
            mckorin "The kind where you're supposed to take a test for a class you didn't know you were in."
            ko "Ground yourself, [genericfn]. This is nightmarish, yeah, but it's actually happening."

            show ecmc jacket_v2 pin determined at left2
            mckorin "I just don't want to get stuck thinking about it, you know? I don't want to get trapped in those thoughts."

            show korin jacket pin surprised at right1
            ko "Do you think about breathing?"

            show ecmc jacket_v2 pin surprised at left2
            mckorin "No..."

            hide ecmc
            hide korin
            show korin jacket_cu smile_cu at korin_cu
            ko "Not until you start thinking about it. Otherwise, it just happens."
            ko "When that feeling comes on again, try grounding yourself in real life. If coming to this park helps, then... I'm happy to come back with you."
            ko "Once you accept the reality of your situation and see, yeah, it is happening--it's going to be easier to take steps forward."
            ko "You're going to get out okay, Scraps. No matter what."

            show ecmc jacket_v2 pin basic at left2
            show korin jacket pin smile behind ecmc at right1:
                xoffset -30
            "I look over at her."

            show ecmc jacket_v2 pin surprised at left2
            mckorin "How are you so put together, Korin? How did you learn that all this is helpful?"

            show korin jacket pin smirk at right1:
                ease 0.4 right1plus xoffset 0
            "Korin fondly scratches my back before getting to her feet."
            ko "Experience is the best teacher."

            show ecmc jacket_v2 pin basic at left2
            "She looks out at the city, gesturing for me to follow."

            show korin jacket pin smile at right1plus
            ko "Come on, Scraps. One foot in front of the other, like we just learned."

            show ecmc jacket_v2 pin smile at left2:
                ease 0.4 left1
            "I stand... and follow her."
        "B. Walk away.":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad behind ecmc at left1plus
            show korin jacket pin sad at right1plus
            mckorin "I appreciate it, but we should get back. I want to know the second that drive turns up."
            "Korin nods, looking disappointed."
            ko "Well, if you ever want to come back or even just talk... let me know."

    hide ecmc
    hide korin
    "We head down the path back the way we came."

    show ecmc jacket_v2 pin smile at left3
    show korin jacket pin basic behind ecmc at right3
    mckorin "Thanks for that, Korin. I'm feeling a lot better, really."

    show korin jacket pin smirk at right3
    ko "Well, hopefully not {i}all{/i} the way better."
    ko "This was just a side-stop. The {i}real{/i} de-stressing is later tonight."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "...Huh?"

    show korin jacket pin surprised at right3
    "Korin raises an eyebrow, then widens her eyes."
    ko "Shoot, that's right. You weren't there!"

    show korin jacket pin smile at right3
    ko "Special outing with the trainees tonight. I announced it while you were off working on the drive."
    mckorin "...What kind of outing?"

    hide ecmc
    hide korin
    show korin jacket_cu smirk_cu at korin_cu
    "Korin smirks."
    ko "The secret kind."

    show korin jacket_cu smile_cu at korin_cu
    ko "Let's get back, Scraps. Hope you're ready for this!"

    scene bg ecm_tbc at bg with fade


    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

