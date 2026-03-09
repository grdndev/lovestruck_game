label korin_season1_episode9:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_mc_dorm_off at bg
    play music ecmtense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird. 
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show ecmc casual_v1 surprised at left3
    show korin jacket pin basic at right3
    mckorin "Hey! Any trouble finding the place?" 
    "Korin is in my doorway a short while later, still in her work clothes." 

    show korin jacket pin surprised at right3
    "Her eyes snap back up to mine, and I realize very acutely that I'm in my casual wear with my hair down." 

    hide korin
    hide ecmc
    show ecmc casual_v1_cu surprised_cu  at ecmc_cu
    "(And Korin is {i}literally at my apartment{/i}.)"
    hide ecmc

    show ecmc casual_v1 surprised at left3
    show korin jacket pin surprised at right3
    ko "Yeah! I mean...no! No trouble." 

    show ecmc casual_v1 basic at left3
    show korin jacket pin basic at right3
    "I step aside and hold my breath as she walks in." 
    "She takes a slow look around."
    hide korin
    hide ecmc

    $menuhideborder = True
    menu korins1e9c1:
        "A. Do you like it?":
            $menuhideborder = False
            show ecmc casual_v1 smile at left3
            show korin jacket pin basic at right3
            mckorin "Do you like it?" 
            show korin jacket pin smile at right3
            ko "Your place? I love it." 
            show korin jacket pin sad at right3
            ko "But...yeah. That's not why I'm here." 
        "B. Should we go somewhere else?":
            $menuhideborder = False
            show ecmc casual_v1 smile at left3
            show korin jacket pin basic at right3
            mckorin "Should we go somewhere else? We could get some coffee..." 
            ko "No. It's perfect here." 
            ko "I mean...it's better if we're somewhere private, anyway." 
        "C. Can I get you something to drink?":
            $menuhideborder = False 
            show ecmc casual_v1 smile at left3
            show korin jacket pin basic at right3
            mckorin "Can I get you something to drink?" 
            ko "Oh...you're so sweet. I'm fine, thank you." 

    "Korin shakes her head a little, like she's snapping herself out of something."

    show ecmc casual_v1 determined at left3
    mckorin "Here...come sit down. You said you think I'm being set up?" 
    "Korin folds a leg under herself and takes a seat on my couch like she's been here a million times before."

    show korin jacket pin basic at right3
    ko "I had a bad hunch about the security footage and the terminal, so I stayed late to investigate." 
    ko "With BB's help, Eko and I discovered that both the terminal and the security cameras had been tampered with." 

    show ecmc casual_v1 surprised at left3
    mckorin "What? Are you serious? But that means..." 

    show korin jacket pin sad at right3
    "She nods." 
    ko "It had to be someone onsite. Someone who used the lab." 

    hide korin
    hide ecmc
    show ecmc casual_v1_cu surprised_cu  at ecmc_cu
    "(Someone inside D.I.V.A.A.?)"
    hide ecmc

    show ecmc casual_v1 sad at left3
    show korin jacket pin sad at right3
    mckorin "But that could be anybody. Vendors, outside partners...agents..." 
    "Korin nods gravely." 
    ko "I thought I should let you know straight away, in case someone else tried to get to you first." 
    ko "I try not to let coincidences arrange themselves into patterns, but we need to consider every possibility." 

    show ecmc casual_v1 surprised at left3
    mckorin "How far back does this go? The terminal, the footage, the hard drive going missing..." 
    mckorin "The data got wiped, when it was initially just corrupted. You don't think...?" 

    show korin jacket pin angry at right3
    ko "Maybe I'm paranoid, but I wouldn't rule it out as a possibility. I think someone is targeting you." 

    show ecmc casual_v1 determined at left3
    mckorin "But...who? And why? The only person I would have known at D.I.V.A.A. would have been my dad." 

    show korin jacket pin sad at right3
    ko "Maybe it's just some senseless act. Maybe it has something to do with your dad." 
    ko "At worst, it could be linked to the original cold case that finding that hard drive reopened." 

    show ecmc casual_v1 sad at left3
    "My blood chills."
    mckorin "The serial killer case? But that would mean..." 
    "Neither of us says it, but the words hang silent between us."

    hide korin
    hide ecmc
    show ecmc casual_v1_cu sad_cu  at ecmc_cu
    "(That might mean the killer was an agent of D.I.V.A.A..)"
    hide ecmc

    show ecmc casual_v1 sad at left3
    show korin jacket pin sad at right3
    ko "Your building seems secure enough. Are you going to be okay here until morning?" 
    mckorin "I think so..." 

    hide korin
    hide ecmc
    show ecmc casual_v1_cu embarrassed_cu blush_cu  at ecmc_cu
    "(Unless you want to stay?)"
    hide ecmc

    show korin jacket pin basic at right3
    show ecmc casual_v1 sad at left3
    ko "I'm heading back to HQ. I need to investigate a few more things tonight." 
    "I nod. "
    ko "Don't leave in the morning. I'll pick you up, and then we'll meet up with Skye first thing." 
    ko "We'll get that drive recovered, and then report all our findings to Gael." 

    show ecmc casual_v1 surprised at left3
    mckorin "Gael? Are you sure we can trust her?" 

    show korin jacket pin smirk at right3
    ko "If the killer is a D.I.V.A.A. agent...Gael might be the only person we can trust." 

    show korin jacket pin smirk behind ecmc at right3:
        ease 0.4 centre
    "Korin puts a hand on my arm."

    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    ko "Scraps...we're gonna get through this, okay? I'm not gonna let anything happen to you." 
    hide korin

    "Korin leaves my place not long after that." 
    "I call it a night, and underneath my flood of worry is a soft current of warmth that Korin is so concerned about me." 

    scene bg ecm_office_hq_on at bg with wiperightdissolve
    stop music
    play music ecmupbeateveryday2
    "The next morning, Korin and I manage to grab the hard drive from Skye and make it back to HQ without incident." 

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(True to his word, he's got the process started.) "

    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Now, we just need to get that drive in Eko's hands and...)" 
    hide ecmc

    show connie casual smile at centre
    co "Good morning, ladies!" 
    "My stomach plummets. "
    hide connie

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Oh, no. Not Connie. Not now...)"
    hide ecmc

    show korin nojacket pin smile at left3
    show connie casual smile at right3
    ko "Hi Connie! I love your lipstick. Is that a new shade?" 
    "Connie sidesteps Korin's compliment." 
    co "You know, I see you two leaving HQ on errands {i}a lot{/i}." 

    show korin nojacket pin sad at left3
    "Korin makes an apologetic face." 
    ko "Sorry. I know how you like those caramel macchiatos...I keep forgetting to ask you if you want one when we go out to grab them!" 

    show connie casual angry at right3
    co "Yeah. Because {i}that's{/i} what this is about." 
    co "And now, you're showing up early together..." 
    "Korin sucks in a breath." 
    ko "Oh, yeah, well..." 
    "I can see she's trying to keep her cool." 

    hide korin
    hide connie
    $menuhideborder = True
    menu korins1e9c2:
        "A. We took the same train":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show connie casual angry at right3
            mckorin "We took the same train getting here. I guess we live kind of near each other, don't we, Korin?" 

        "B. I need to catch up":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show connie casual angry at right3
            mckorin "Korin's catching me up on what I've been missing in my normal trainee sessions." 
            mckorin "With this special assignment, I've fallen a bit behind." 

        "C. It's just a coincidence":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show connie casual angry at right3
            mckorin "I wanted to get started early today, and I guess Korin did, too."  
    hide ecmc
    show korin nojacket pin smile at left3
    "Korin nods, agreeing with my fabrication." 
    co "Yeah, well...I don't believe any of it." 
    co "I know you checked out the hard drive. I bet you have it with you now." 

    show korin nojacket pin surprised at left3
    "Korin pats herself down, looking confused." 
    ko "Hard drive?" 

    show korin nojacket pin smile at left3
    ko "Oh! You mean the one that [genericfn] is working on?" 
    ko "I only know what Enver passes on to me sometimes. You know what a gossip he can be..." 
    "Korin's right about Enver, but Connie isn't having any of it." 
    co "I'm going to call Dom. You're helping her, aren't you, Korin?" 

    show korin nojacket pin sad at left3
    "Korin shakes her head in disbelief. I catch tiny signs that this conversation has her stressed out..." 
    hide korin

    show ecmc jacket_v2 pin determined at left3
    "So I step forward." 
    mckorin "Connie, if you're going to call anyone, call Gael." 
    mckorin "If you're so hellbent on bothering the top brass with your paranoid delusions..."
    mckorin "...At least bring it to the person that Griffin Vega said I was to report directly to for this assignment." 
    "I whip out my ARCware with one hand." 

    show ecmc jacket_v2 pin angry at left3
    mckorin "Hell, I'll call her for you." 
   
    hide connie
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(Is that what you want? To deal with an FDI agent this early in the morning?)" 
    hide ecmc

    show ecmc jacket_v2 pin angry at left3
    show connie casual angry at right3
    "I pull up Gael's contact card, and Connie replaces the panicked look on her face with a scowl." 
    co "Don't be ridiculous! You're blowing this way out of proportion." 
    mckorin "So I {i}shouldn't{/i} call her?" 
    "She rolls her eyes to try and hide how flustered and angry she is." 
    "She calls back over her shoulder as she's marching away..." 
    
    hide ecmc
    hide connie
    show connie casual_cu angry_cu at connie_cu
    co "I'm watching you, got it?" 
    co "I won't let you ruin D.I.V.A.A.'s reputation!" 
    
    scene bg ecm_office_lab_on at bg with wiperightdissolve
    stop music
    play music ecmtechgameloop1

    "Up in the lab, Eko helps me set up the recovery databank." 

    show ecmc nojacket_v2 pin basic at left3
    show eko casual glasses pin basic at right3
    mckorin "How's everything going with the lab shut down?" 

    show eko casual glasses pin sad at right3
    "Eko gives me a worried look." 
    ek "Much more secure...but no closer to any definitive answers."
    hide eko
    
    show ecmc nojacket_v2 pin basic at centre
    "The day passes. I watch the progress bar slowly inch toward the finish..."

    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Come on. Please be worth it...)" 
    hide ecmc

    show ecmc nojacket_v2 pin sad at centre
    "I find myself wishing that Korin would stop by, but the day passes without even a glimpse of her." 
    hide ecmc

    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(It's probably for the best that she keeps her distance after what happened with Connie this morning.)" 
    hide ecmc

    "Still, the drive works toward repair...and I find myself fretting and missing Korin." 
    "The process continues long past closing time." 

    stop music
    play music ecmcalmeveryday4

    show korin nojacket pin basic at centre:
        yoffset 50
        easein 0.4 yoffset -10
        easein 0.2 yoffset 0
    with dissolve
    "And finally, Korin stops by." 
    "I perk up at once, feeling renewed with energy upon seeing her." 

    show korin nojacket pin smile at left3
    show eko casual pin glasses basic at right3
    ko "Eko, if you want to lock up and take off, I can make sure we're all set here." 

    show eko casual pin glasses smile at right3
    "Eko looks thankful and relieved. She bids us good night." 
    ek "Eager to see what you uncover in the morning!" 

    hide korin
    show ecmc nojacket_v2 pin smile at left3
    mckorin "You bet. Have a good night, Eko!" 

    hide ecmc
    hide eko
    show korin nojacket pin smile at centre
    "Once she's gone, Korin opens her bag and pulls out two sets of chopsticks and two take-out boxes." 

    show ecmc nojacket_v2 pin surprised at left3
    show korin nojacket pin smile at right3
    ko "Okay, do not tell Eko we ate in the lab. But I'm starving, and I figured you were, too." 

    show ecmc nojacket_v2 pin smile at left3
    mckorin "Poké!! This place is my favorite! How did you know?" 
    "Korin finishes chewing a big bite of tuna before answering." 

    show korin nojacket pin smirk at right3
    ko "Whenever we had a late night, your dad would always try to get us to order from there." 

    show korin nojacket pin smile at right3
    ko "He'd wave that menu around and be like, 'How about poké? It's my daughter's favorite!'" 
    "I laugh at her impression of him, but my heart twists a little, thinking about him." 
    ko "And I'd be all, 'Then order it with your daughter! Sheesh!'" 
    ko "I think it was his favorite, too. But he'd use any excuse he could to talk about you." 

    show ecmc nojacket_v2 pin determined at left3
    "I dig into my dinner, trying not to think too much about my dad right now." 

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu determined_cu at ecmc_cu
    "(Not until I'm out of this hot water with my status at D.I.V.A.A..)" 
    hide ecmc

    show ecmc nojacket_v2 pin determined at left3
    show korin nojacket pin basic at right3
    "Thinking of that, I check on the hard drive status again." 
    mckorin "Still a ways to go..." 
    ko "It'd be way longer if we left the entire process up to Skye, though." 

    show korin nojacket pin smile at right3
    ko "We did the right thing by bringing it back here." 

    show korin nojacket pin smile at right3:
        ease 0.4 right4
    "Korin leans back in her chair as she eats, putting one foot up on the table." 

    show ecmc nojacket_v2 pin smile at left3:
        ease 0.4 left4
    "I do the same, and with Korin here, I feel myself start to relax for the first time all day." 
    ko "That was a real gamble you took with Connie this morning." 

    show ecmc nojacket_v2 pin surprised at left4
    mckorin "Was it?" 

    show korin nojacket pin smirk at right4
    ko "If she'd called your bluff about contacting Gael..." 

    show ecmc nojacket_v2 pin smile at left4
    mckorin "I knew she wouldn't, though." 

    show korin nojacket pin surprised at right4
    "Korin tilts her head at me." 

    show ecmc nojacket_v2 pin determined at left4
    mckorin "D.I.V.A.A., and its reputation...{i}that's{/i} what's at stake here." 
    mckorin "But me? I'm at risk every second of being fired before I've even got my foot in the door." 
    mckorin "I've got nothing left to lose, and D.I.V.A.A. has everything to lose. Connie knew that." 

    show korin nojacket pin smirk at right4
    "Korin shakes her head, looking impressed." 
    ko "You...you're trouble. I'm keeping my eye on you." 

    show ecmc nojacket_v2 pin smile at left4
    mckorin "Yeah, because you've been overlooking me so much before now." 
    "She smirks at me from across the table." 
    ko "Can you blame me?" 

    show ecmc nojacket_v2 pin basic at left4
    "I don't know what to say to that...so I take another big bite of poké." 

    show ecmc nojacket_v2 pin sad at left4
    mckorin "I guess I should just be thankful with how lucky we've been so far." 

    show korin nojacket pin surprised at right4
    "Korin widens her eyes and nods appreciatively." 
    ko "No kidding. But I don't think you can chalk it all up to luck." 

    show korin nojacket pin smile at right4
    ko "There's no denying it: you're just good at what you do." 
    ko "It'll be a damn shame if we don't recover that drive and Dom has to make good on his word." 

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(Maybe it wouldn't be {i}all{/i} bad. I could ask Korin if she...)" 
    hide ecmc

    show ecmc nojacket_v2 pin surprised at left4
    show korin nojacket pin smile at right4:
    "I stop that line of thinking...but not as harshly as I've done before." 

    show ecmc nojacket_v2 pin determined at left4
    "And then I let myself really think about it." 

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu basic_cu at ecmc_cu
    "(I could ask Korin out. Like, on a real date. Not me depending on her, or her looking after me...)" 
    hide ecmc

    show ecmc nojacket_v2 pin surprised at left4
    show korin nojacket pin smile at right4
    "I'm getting to the bottom of my take-out box, when my hand starts to cramp." 

    show ecmc nojacket_v2 pin sad at left4
    "I put down my chopsticks and painfully flex my hand, trying to rub the pain away." 

    show korin nojacket pin surprised at right4
    ko "You okay?" 
    mckorin "Too much typing and tinkering. The stress of this week is catching up to me...or more specifically, my hands." 

    show korin nojacket pin smile at right4
    ko "Oh, here! Try this. It's a pressure point technique I use whenever I need to." 
    "She demonstrates on her own hands." 
    "I try to replicate her motions, but...I'm just not getting it right." 

    show korin nojacket pin smirk at right4
    ko "No, no, try again. It's easy..." 

    show ecmc nojacket_v2 pin determined at left4
    mckorin "Oh, if it's so easy, you do it!" 

    show korin nojacket pin surprised at right4
    "Korin raises her eyebrows." 
    ko "I could. You want me to?" 

    show ecmc nojacket_v2 pin surprised at left4
    mckorin "Want you to...what? Massage my hands?" 

    hide korin
    hide ecmc
    show ecmc nojacket_v2_cu embarrassed_cu blush_cu at ecmc_cu
    "(I mean, yes. I want that.)" 

    show ecmc nojacket_v2_cu surprised_cu blush_cu at ecmc_cu
    "(But could I handle being that close to her while she's...touching me?)" 
    hide ecmc

    show korin nojacket_cu smirk_cu at korin_cu
    ko "It's okay if you want me to just teach you again from afar, but..." 

    show korin nojacket_cu smile_cu at korin_cu
    ko "I hate to see you in pain, and honestly, this technique really works." 

    hide korin
    $menuhideborder = True
    menu korins1e9c3:
        "A. Let Korin massage your hands" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show ecmc nojacket_v2 pin sad at left4
            show korin nojacket pin smile at right4
            mckorin "Well...I {i}am{/i} in a lot of pain." 

            show korin nojacket pin smile at right4:
                ease 0.4 right3
            "Korin puts aside her chopsticks and stands up at once." 

            show ecmc nojacket_v2 pin surprised at left4
            mckorin "You can finish your food first, you know!" 


            show korin nojacket pin smile behind ecmc at right3:
                ease 0.6 centre xoffset -50
            "Korin just shakes her head and pulls a chair over." 
            "When she sits, she's close enough that her knees brush against mine." 
            ko "Is this okay? Can I get closer?" 

            show ecmc nojacket_v2 pin determined at left4
            "I nod. I offer her my dominant hand, and she takes it in both of hers, turning my palm up." 
            "Her hands are soft and cool to the touch, and I find myself hoping she won't stray too near my wrist and feel my pulse." 
            "Her fingers smooth over the muscles in my fingers. Then, she presses her fingertips into pressure points on my palm." 

            show ecmc nojacket_v2 pin surprised at left4
            mckorin "Oh! So that's how you..." 

            hide korin
            hide ecmc
            show ecmc nojacket_v2_cu smile_cu at ecmc_cu
            "({i}Ohhh{i}.)"
            hide ecmc

            show ecmc nojacket_v2 pin smile at left4
            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            "My whole body slacks as the tight pain in my hand and wrist suddenly releases." 

            show ecmc nojacket_v2 pin embarrassed at left4
            "I hold my breath to keep whatever noise is burbling up inside me from slipping out." 

            show korin nojacket pin surprised behind ecmc at centre:
                xoffset -50
            "Korin looks up in alarm." 
            ko "Are you okay? Am I hurting you?" 
            "I'm caught between nodding and shaking my head and end up doing some sort of bobblehead move instead." 
            mckorin "It's good. It feels really...good." 

            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            "I feel some of the tension in my chest release at the sound of Korin's laughter." 

            show ecmc nojacket_v2 pin surprised at left4
            mckorin "Holy crap, it's like magic. Where'd you even learn this?" 
            ko "I worked this case once...your dad might have told you about it."
            ko "The case was a series of victims of identity theft via facial recognition software." 

            show korin nojacket pin smirk behind ecmc at centre:
                xoffset -50
            ko "We discovered that the victims all had one thing in common: they all frequented this one massage parlor." 

            hide korin
            hide ecmc
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            "(Whaaat?)" 
            hide ecmc

            show ecmc nojacket_v2 pin basic at left4
            show korin nojacket pin smirk behind ecmc at centre:
                xoffset -50
            ko "So, I went in to investigate and made friends with an employee that later wanted to serve as an informant." 
            ko "Turns out they were taking facial scans of clients from the face cradles on their massage tables and 3D printing them." 

            show ecmc nojacket_v2 pin surprised at left4
            mckorin "What?!" 
            "Korin shrugs, like {i}it's the job{/i}." 

            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            ko "I gave the F.D.I. a heads-up about our informant. Saved her a lot of trouble in the subsequent sting operation." 
            ko "As a thank-you, she taught me this technique. And I'd say it's one of the most useful tools I've learned on the job." 
            "I can't help thinking about Korin growing closer with this mystery masseuse." 
            mckorin "Are you two still friends?" 
            ko "Oh, of course." 

            show korin nojacket pin smirk behind ecmc at centre:
                xoffset -50
            ko "She even set me up with her daughter."
            mckorin "Oh??" 

            show korin nojacket pin sad behind ecmc at centre:
                xoffset -50
            ko "Yeah. It didn't work out between us, but--" 

            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            ko "Whoa, I just felt a huge knot of tension release. Did you feel it?" 

            hide korin
            hide ecmc
            show ecmc nojacket_v2_cu embarrassed_cu blush_cu at ecmc_cu
            "(Oh, I felt it.)" 
            hide ecmc

            show ecmc nojacket_v2 pin smile at left4
            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            mckorin "Huh? No. Weird!" 

            show korin nojacket pin sad behind ecmc at centre:
                xoffset -50
            ko "You've got to get rid of that claw-hand you do when you use your ARCware." 

            show ecmc nojacket_v2 pin surprised at left4
            mckorin "You can tell that just by feeling my tendons?!" 

            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            ko "I've seen you do it!" 
            ko "But, also...yeah. A little bit." 
            ko "You're one of those whole-hand coders. On my hand, I don't have such developed muscles here..." 

            show ecmc nojacket_v2 pin basic at left4
            "She moves her fingertips in small circles to demonstrate. She finishes that hand and moves on to my other one." 
            ko "And see, I'm guessing you're kind of ambidextrous, too?" 

            show ecmc nojacket_v2 pin sleep at left4
            "I nod. My eyes slip closed involuntarily."  

            hide korin
            hide ecmc
            show ecmc nojacket_v2_cu embarrassed_cu at ecmc_cu
            "(She's noticing so much.)"

            hide korin
            hide ecmc
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            "(What else does she notice about me?)" 
            hide ecmc

            show ecmc nojacket_v2 pin surprised at left4
            show korin nojacket pin basic behind ecmc at centre:
                xoffset -50
            "I open my eyes and see Korin looking closely at my palm." 
            mckorin "What is it?" 

            show korin nojacket pin sad behind ecmc at centre:
                xoffset -50
            "She straightens up, hiding a guilty look." 
            ko "Nothing." 

            show ecmc nojacket_v2 pin smile at left4
            mckorin "Were you reading my palm?" 

            show korin nojacket pin surprised behind ecmc at centre:
                xoffset -50
            "Korin scoffs." 

            show korin nojacket pin basic behind ecmc at centre:
                xoffset -50
            ko "What? No! Don't be ridiculous...where would I even learn something like that?" 
            mckorin "I don't know...maybe some informant in a case involving psychics, or something?" 

            show korin nojacket pin sad behind ecmc at centre:
                xoffset -50
            "Korin keeps her eyes down on my hands." 

            show ecmc nojacket_v2 pin surprised at left4
            mckorin "Unless...you studied it yourself?" 

            show ecmc nojacket_v2 pin smile at left4
            mckorin "...Oh my bot, you {i}did{/i}, didn't you?" 

            show korin nojacket pin smile behind ecmc at centre:
                xoffset -50
            ko "You know, I can also give a mean neck massage. Want one?" 

            show ecmc nojacket_v2 pin embarrassed at left4
            "I bite my lip to keep from laughing." 
            mckorin "Is this to keep me from asking about how you know how to read palms?" 

            hide ecmc
            hide korin
            show korin nojacket_cu angry_cu at korin_cu
            "Korin stands up and puts her hands on her hips as she stands over me." 
            ko "Neck massage. Yes or no?" 
            hide korin
 
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            mckorin "...Yes please." 

            show ecmc nojacket_v2_cu smile_cu at ecmc_cu
            mckorin "As long as you're not planning to snap my neck because I know your deep, dark palmistry secret." 
            hide ecmc

            show korin nojacket_cu smirk_cu at korin_cu
            "I hear Korin give a low chuckle and feel her hands on the back of my neck." 

            show korin nojacket_cu smile_cu at korin_cu
            ko "Scraps...you're safe with me." 
            "I let my head loll forward as her fingers deftly work through knots of tension from the base of my skull down to my shoulders." 
            hide korin

            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            "(Ohhh...)" 
            hide ecmc

            show korin nojacket_cu smirk_cu at korin_cu
            ko "That being said..." 

            show korin nojacket_cu smirk_cu at centre with dissolve:
                rotate 180 xalign 0.5 ycenter 0.20
            "Korin tilts my head up so I'm looking up at her, upside-down in my field of vision." 
            ko "If you tell anyone at D.I.V.A.A. about it, you're scuffed." 
            hide korin

            show ecmc nojacket_v2_cu smile_cu at ecmc_cu
            mckorin "Your secret's safe with me."
            hide ecmc

        "B. Just deal with it":
            $menuhideborder = False
            show ecmc nojacket_v2 pin surprised at left4
            show korin nojacket pin smirk at right4
            mckorin "I...appreciate it. But I'll live." 
            ko "Your loss, Scraps...but if you change your mind, let me know."
            hide ecmc
            hide korin

    show korin nojacket pin sad at centre
    "Korin stifles a yawn." 

    hide korin
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(She looks exhausted...)" 
    hide ecmc

    show ecmc nojacket_v2 pin sad at left3
    show korin nojacket pin sad at right3
    mckorin "Hey, you were up all last night, weren't you?" 
    mckorin "You really should go home and get some rest." 

    show korin nojacket pin surprised at right3
    ko "But..." 

    show ecmc nojacket_v2 pin smile at left3
    "I get up to clear away her take-out." 
    mckorin "Eko locked up the lab, remember?" 
    mckorin "I'll be fine." 

    show korin nojacket pin surprised behind ecmc at right3:
        ease 0.4 centre
    "Korin moves closer to me. My breathing catches..."

    hide ecmc
    hide korin
    show korin nojacket_cu smile_cu at korin_cu
    "She hugs me. Lightly, and it only lasts a moment..." 
    hide korin

    show ecmc nojacket_v2_cu embarrassed_cu blush_cu at ecmc_cu
    "(But we've never done that before.)" 
    hide ecmc

    show ecmc nojacket_v2 pin embarrassed at left3
    show korin nojacket pin smile behind ecmc at centre
    ko "Thanks. I really am beat..." 

    show ecmc nojacket_v2 pin smile at left3
    mckorin "Take care, Korin. See you in the morning." 

    scene bg ecm_office_lab_on at bg with fade
    stop music
    play music ecmtense3

    "The night drifts on. I keep watching the progress bar tick closer and closer to its finish."
    "But my focus starts to drift. The machines whir and lull me to sleep..." 

    scene black at bg
    scene bg ecm_office_lab_on at bg with eye_open
    scene black at bg with eye_shut
    scene bg ecm_office_lab_on at bg with eye_open
    "I don't know how long it's been when I wake up to the sensation of someone restraining me." 

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.
    
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

