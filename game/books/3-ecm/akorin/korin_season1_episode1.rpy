
label korin_season1_episode1:

    $tbc = False
    scene bg ecm_prologue_mini1 at bg
    play music ecmmctheme

    pause

    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    mckorin "The year is 2188. I grew up thinking I lived in a golden age, but crimes involving AI, cybernetics, and the virtu-net are rampant."

    mckorin "To keep up with it all, governments outsource half of all law enforcement to private agencies."

    scene bg ecm_prologue_mini2 at bg with dissolve

    mckorin "My home, Los Angeles, is a sprawl of neon and grime that reeks of passion and desperation."

    mckorin "But, only a few outfits in this city actually care about helping people."

    scene bg ecm_prologue_mini3 at bg with dissolve

    mckorin "I joined with the best one, D.I.V.A.A., but it's always competing with old guard operations like the F.D.I. and L.A.M.P.."

    mckorin "My dad is one of the top investigators working for D.I.V.A.A., and he went missing over a year ago."

    scene bg ecm_prologue_mini4 at bg with dissolve

    mckorin "I'll keep moving up the ranks and investigating the truth."

    mckorin "LA is full of secrets, but if I pursue what's in my heart, I hope I'll uncover more than I ever desired."

    stop music fadeout 1.0
    play music ecmupbeateveryday4
    scene bg ecm_office_hq_on at bg
    pause

    show ecmc jacket_v2 basic headset pin at centre
    "The common area at D.I.V.A.A. Headquarters buzzes with trainees."

    "I'm among them...and I'm starting to panic."
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu headset_cu pin_cu at ecmc_cu
    "(ARCware? {i}ARCware??{/i} Why aren't you in my bag?)"

    show ecmc jacket_v2_cu sad_cu headset_cu pin_cu

    "(Please, PLEASE don't tell me I left it at home.)"

    show ecmc jacket_v2_cu surprised_cu headset_cu pin_cu

    "I put a hand on my head...and nearly collapse with relief."
    show ecmc jacket_v2_cu smile_cu headset_cu pin_cu

    "(On my head, of course. Crisis aver--)"
    hide ecmc
    show ecmc jacket_v2 surprised headset pin at centre

    "Another trainee bumbles through the crowd and collides with me."

    mckorin "Sorry!"
    show ecmc jacket_v2 sad headset pin
    "We're both fine, but my uniform is not."
    hide ecmc
    show ecmc jacket_v2_cu angry_cu headset_cu pin_cu at ecmc_cu
    "(Grease stain! Seriously? On my first day?)"
    hide ecmc
    show ecmc jacket_v2 surprised headset pin at centre
    "The room grows suddenly quiet. I look up."
    hide ecmc
    show korin jacket basic pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    "My eyes stop on a woman who's just walked in."

    "She sashays in with such ease that the rest of the world seems to pause. "

    "She scans the room, her eyes considering each trainee."
    hide korin
    hide bird
    show ecmc jacket_v2_cu determined_cu headset_cu pin_cu at ecmc_cu
    "(Why does she look so familiar...)"
    hide ecmc
    show korin jacket basic pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    "I recognize her personal assistant bot right away."

    "My brain connects the circuits, and I realize who I'm looking at."
    hide korin
    hide bird
    show ecmc jacket_v2_cu smile_cu headset_cu pin_cu at ecmc_cu
    "(Korin! Dad's old partner...)"

    "She brushes a lock of hair out of her face and tucks it behind her ear."
    hide ecmc
    show korin jacket basic pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    "I'm staring now. I can't help it."
    hide korin
    hide bird
    show ecmc jacket_v2_cu surprised_cu headset_cu pin_cu at ecmc_cu
    "(What's she doing here?)"
    hide ecmc
    show korin jacket surprised pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    "Korin catches my eye. My heart leaps."
    $menuhideborder = True
    hide korin
    hide bird
    menu korine1c1:
        "A. Smile!":
            $menuhideborder = False
            show korin jacket smile pin at centre
            show bird normal at centre, birdbob:
                xoffset 200 ypos 200
            "I smile at Korin. Even better--she returns it!"
        "B. Wave?":
            $menuhideborder = False
            show korin jacket basic pin at centre
            show bird normal at centre, birdbob:
                xoffset 200 ypos 200
            "I lift my hand up and give her a way!"
            show korin jacket smile pin at centre
            "She smiles in return, but seems amused."
        "C. Look away":
            $menuhideborder = False
            show ecmc jacket_v2 embarrassed headset pin at centre
            "I look down... and am reminded of the huge, embarrassing grease stain on my uniform."
            hide ecmc
    show korin jacket basic pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    "Korin turns her attention to the whole room."
    show korin jacket smile pin
    kor "Welcome, cadets. I'm Phoenix Detective Korin Reyes, your instructor and orientation leader."
    hide korin
    hide bird
    show ecmc jacket_v2_cu surprised_cu headset_cu pin_cu at ecmc_cu
    "(She's my {i}instructor?!{/i})"
    hide ecmc
    show korin jacket smile pin bird at centre
    "Korin goes over our training agenda. I'm still stunned..."
    hide korin
    show ecmc jacket_v2_cu surprised_cu headset_cu pin_cu at ecmc_cu
    "(I knew Korin was closer to my age than Dad's.)"

    "(She must be really good at her job if she's training rookies already!)"
    hide ecmc
    show korin jacket smile pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    kor "Most of you are thinking it's going to be smooth sailing since you made it out of the Academy."

    kor "Don't hold on to that vision for long. Your training as Hatchlings will affect future opportunities as official detectives for D.I.V.A.A."

    kor "But follow my guidance, and we'll make sure you're all booted into D.I.V.A.A.-ready shape in no time."
    hide korin
    hide bird
    show ecmc jacket_v2_cu smile_cu headset_cu pin_cu at ecmc_cu
    "I smile, comforted by her words."
    hide ecmc
    show korin jacket smile pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    kor "Oh, and one more thing..."
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    kor "Since we're going to be working closely together, spare the 'Phoenix Reyes’. Just call me Korin."
    hide korin
    show ecmc jacket_v2 smile headset pin at centre
    "She dismisses us to get ready for the day's outing. I gather my things as people file out around me."
    hide ecmc
    show korin jacket smile pin at centre
    show bird normal at centre, birdbob:
        xoffset 200 ypos 200
    kor "Hatchling [genericln]!"
    hide korin
    hide bird
    show ecmc jacket_v2 surprised headset pin at centre
    "My heart skips. It's the first time I've been called by my formal rank by a D.I.V.A.A. agent. I throw my shoulders back and snap to attention."
    show ecmc jacket_v2 surprised headset pin at left2
    show korin jacket basic pin  at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    mckorin "Y-yes, Phoenix Detective Reyes?"
    scene bg ecm_korin_s1_ei1 at bg with fade:

        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    "Korin grins as she approaches."

    kor "Relax, rookie. Just had to keep you on your toes for my formal introduction."

    "She extends her hand to me, and I shake it."

    "(She's so different than I imagined... social, confident, easygoing.)"

    "(With the way Dad talked about her, I figured she'd be a lot more like me.)"
    scene bg ecm_office_hq_on at bg
    show ecmc jacket_v2 basic headset pin at left2
    show korin jacket basic pin at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    kor "I've had a look at your academy transcript."
    show korin jacket surprised pin
    kor "Top of your class! Very impressive."
    show korin jacket smile pin
    kor "Your dad would have been really proud of you, you know."
    show ecmc jacket_v2 sad headset pin
    "My heart swells at her kind words, but sinks just a little bit."
    hide ecmc
    hide bird
    hide korin
    show ecmc jacket_v2_cu sad_cu headset_cu pin_cu at ecmc_cu
    "(It figures she thinks he's gone for good, too. Everybody does.)"
    hide ecmc
    show ecmc jacket_v2 sad headset pin at left2
    show korin jacket smile pin at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    mckorin "Thanks. It's been hard without him here. I miss him every day."
    show korin jacket sad pin
    "Korin's eyes soften as she searches my expression."

    kor "If you ever need some time, just--"
    show ecmc jacket_v2 smile headset pin
    mckorin "Actually, focusing on making it through the Academy has helped a lot."
    show korin jacket basic pin
    kor "Oh?"
    hide ecmc
    hide bird
    hide korin
    show ecmc jacket_v2_cu smile_cu headset_cu pin_cu at ecmc_cu
    "(Yeah. Helped me get the tools to investigate what really happened to Dad.)"

    hide ecmc
    show ecmc jacket_v2 sad headset pin at left2
    show korin jacket smile pin at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    mckorin "It's been a whole year since he disappeared."
    show ecmc jacket_v2 determined headset pin
    mckorin "If I can carry on his legacy, then in a way, part of him will always be here."
    hide ecmc
    hide bird
    hide korin
    show ecmc jacket_v2_cu determined_cu headset_cu pin_cu at ecmc_cu
    "(Until I find out where he disappeared to and bring him back.)"
    hide ecmc
    show ecmc jacket_v2 determined headset pin at left2
    show korin jacket sad pin at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    "Korin blinks, looking touched by my words."

    kor "Huh. I never thought about it that way."

    kor "Well, the offer stands. You need help with anything at all, just let me know."
    show ecmc jacket_v2 smile headset pin
    "I duck my head in thanks, and notice the stain down on my shirt."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu smile_cu headset_cu pin_cu at ecmc_cu
    "(...Anything?)"
    hide ecmc
    show ecmc jacket_v2 surprised headset pin at left2
    show korin jacket sad pin at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    mckorin "Actually..."
    show korin jacket smile pin
    "Korin quirks a grin as I look up at her again."

    "I point at the stain, about to explain myself..."
    show ecmc jacket_v2 embarrassed pin headset
    "But she's a step ahead. Korin pulls a stick of ScrubIRL. My cheeks grow warm."

    mckorin "You just...had that ready?"
    show korin jacket smirk pin
    kor "Look, I'm a fully-fledged investigator. I try to be prepared for everything."

    mckorin "You noticed it when you first saw me, didn't you?"

    kor "Maybe."
    show korin jacket smile pin
    kor "The important thing is you weren't afraid to ask for help."

    "Our fingers brush as I reach for the stick. A jolt runs through me."
    hide ecmc
    hide korin
    hide bird
    show ecmc jacket_v2_cu surprised_cu headset_cu pin_cu at ecmc_cu
    "(Jeez, I must be more nervous about making a good impression than I thought.)"
    hide ecmc
    show ecmc jacket_v2 smile headset pin at left2
    show korin jacket smile pin at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    mckorin "Well... thank you."

    kor "My pleasure."
    show ecmc jacket_v2 determined headset pin
    "I use the stick and let it work over the stain, the gel lifting the grease right out."

    "As I do, Korin's little assistant bot starts beeping."
    show korin jacket surprised pin
    kor "Baby Bird, what now?"

    bb "{i}Bwee! Bwee! Bwee!{/i}"
    show korin jacket sad pin

    kor "Son of a glitch. Not again..."

    "Exasperated, Korin gently grabs the bot out of the air."

    kor "It's been like this for a week. Tried to find a fix, but..."
    show ecmc jacket_v2 smile pin headset
    mckorin "Can I see?"
    show korin jacket smile pin
    kor "Be my guest."

    "I slip on my ARCware and open up the holo settings interface."
    show ecmc jacket_v2 determined pin headset
    mckorin "Is this the same one my dad fixed up a few years back?"
    show korin jacket smile pin
    "Korin's eyes lit up."

    kor "You remember that?"
    show ecmc jacket_v2 embarrassed pin headset
    "Nervous, I stay focused on the bot."

    mckorin "It's an obsolete model, but it's a good find. You get it at a Pop-Up, or something?"
    show korin jacket surprised pin
    kor "And deal with those retrotech-loving waregeeks? Nooo way. I found BB here in a scrapyard myself."
    show ecmc jacket_v2 angry pin headset
    "I bite back a scoff."
    hide ecmc
    hide korin
    hide bird
    show korin jacket_cu embarrassed_cu pin_cu blush_cu at korin_cu
    "Korin looks at me, and I catch just the slightest hint of color in her cheeks."
    hide korin
    show ecmc jacket_v2 angry pin headset at left2
    show korin jacket smile pin blush at right2
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    kor "...Unless {i}you're{/i} one of those waregeeks, in which case I just mean, you guys are sooo cool and intimidating."

    "I put on an airy voice."
    show ecmc jacket_v2 smile pin headset
    mckorin "Our preferred term is {i}scrapper{/i}."
    show korin jacket smile pin blush
    "Korin laughs."
    show korin jacket smirk pin blush
    kor "Noted. But it serves you right for calling BB 'obsolete.'"
    show ecmc jacket_v2 determined pin headset
    "I look pointedly at Baby Bird."
    show ecmc jacket_v2 sad pin headset
    mckorin "My apologies."

    bb "{i}Bwee! Bwee! Bwee!{/i}"
    show ecmc jacket_v2 surprised pin headset
    "Finally, I spot the bug in the interface."
    show ecmc jacket_v2 smile pin headset
    mckorin "Well, here's your problem. Just a logic loop error."

    "I execute commands in my ARCware, apply them to Baby Bird's settings, and close the interface."
    show bird normal at right2, birdbob:
        xoffset 200 ypos 200
    "Baby Bird blinks and sings a reset tune before flitting dutifully back to Korin's shoulder."

    mckorin "Shouldn't happen again. But if it does, I already owe you for the Scrub stick."
    show korin jacket smile pin blush
    kor "Then wouldn't this make us even?"
    hide korin
    hide bird
    hide ecmc
    show korin jacket_cu smirk_cu pin_cu at korin_cu
    "Korin winks, smiles, and...I short-circuit. I can't think of anything to say."

    kor "Glad we could help each other out, Scraps. Eager to see how else you surprise me today."
    scene bg ecm_junkyard_day at bg with wipeleft
    show ecmc jacket_v2 basic pin headset at centre
    "Hours later, I and the other cadets are across town, carefully picking through an industrial scrapyard."

    "It's the location of a major cold case at D.I.V.A.A., and we've been given individual sections to analyze and report on."
    hide ecmc
    show korin jacket basic pin at centre
    "Occasionally, I sneak glances at Korin working one-on-one with the other trainees."
    hide korin
    show ecmc jacket_v2_cu determined_cu pin_cu headset_cu at ecmc_cu
    "(But she's not the one I need to watch out for.)"
    hide ecmc
    show connie casual basic at centre
    "Connie Summers, personal assistant to D.I.V.A.A.'s highest ranking investigator, has been circling us like a drone."

    "From what I've overheard, she's evaluating us for a report she's going to submit to her boss."
    hide connie
    show korin jacket basic pin at right2
    show ecmc jacket_v2 basic pin headset at left2
    "When it's my turn with Korin, I give her a detailed report of my sector."
    show korin jacket smile pin
    kor "Clearly you've put a lot of analysis into this. Well done."
    show ecmc jacket_v2 smile pin headset
    "Glowing from the words of her praise, I continue."

    mckorin "I was {i}also{/i} able to tag the RFID serial numbers from the parts I found. For example--"
    show korin jacket basic pin
    kor "Okay. I'm going to cut you off right there."
    show ecmc jacket_v2 sad pin headset
    "My heart sinks a little."

    mckorin "Did I do something wrong...?"
    show korin jacket smile pin
    "That makes her laugh."

    kor "[genericfn], You're sprinting. You're practically lapping the other trainees."

    kor "This level of analysis is impressive, but it's not sustainable. You're going to overclock and burn out on your first day."
    show ecmc jacket_v2 basic pin headset
    "I let out a breath and nod."
    show ecmc jacket_v2 determined pin headset
    kor "Pace myself. Got it."
    show korin jacket sad pin
    kor "I was worried this was going to be a problem with you. Being ahead of everyone else…"

    "Hearing that from her just makes me want to show off more."

    kor "But I'll tell you what I told the others."
    hide korin
    hide ecmc
    show korin jacket_cu smirk_cu at korin_cu
    "She looks around to make sure we're not being overheard before lowering her voice."

    kor "Don't worry so much about Connie's report."
    hide korin
    show ecmc jacket_v2 surprised pin headset at left2
    show korin jacket smirk pin at right2
    mckorin "Isn't it going directly to the section leader?"
    show korin jacket basic pin
    kor "Dom's getting that report, yes, but he'll be interested in Connie's efforts, not yours."
    show korin jacket smile pin
    kor "Besides, if she can see what I can see, I have no doubt her report on you will be glowing."
    show korin jacket basic pin at right3
    show ecmc jacket_v2 sad pin headset
    "She turns away like she's moving on. I can't help craving more of her time."
    show ecmc jacket_v2 surprised pin headset
    "I blurt out the first thing that comes to mind."

    mckorin "Anything I can improve on? Anything?"
    show korin jacket smile pin
    "Korin turns back to me, grinning."

    mckorin "I mean...I don't want some special advantage over my peers, or anything."
    show korin jacket smile pin at right1
    "Korin leans in and lowers her voice."
    hide ecmc
    hide korin
    show korin jacket_cu smirk_cu at korin_cu
    kor "Little late for that, dontcha think?"
    show korin jacket_cu basic_cu
    kor "I have a tip for you, but it's not something I usually talk about on a trainee's first day."
    hide korin
    show ecmc jacket_v2_cu determined_cu pin_cu headset_cu at ecmc_cu
    "(A personal lesson from Korin? I could listen to her all day.)"
    hide ecmc
    show korin jacket_cu smirk_cu at korin_cu
    kor "But you're ready for a little more than that, aren't you?"
    $menuhideborder = True
    menu korine1c2:
        "A. Accept Korin's personal lesson." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin jacket smirk pin at right1
            show ecmc jacket_v2 smile pin headset at left2
            mckorin "I'll take that lead, show me what you've got."

            kor "Trainees should normally focus on the basics: detection, analysis, deduction, and collecting."

            kor "Developing those makes a solid foundation you can use to house your intuition."
            hide korin
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
            "(...Intuition? Really?)"
            hide ecmc
            show korin jacket smirk pin at right1
            show ecmc jacket_v2 surprised pin headset at left2
            mckorin "Oh. Um..."

            show korin jacket smirk pin
            "Korin grins and tilts her head, giving me a knowing look."

            kor "Yeah, I know. Every analytical brain's worst fear: conclusions without conscious reasoning!"
            show ecmc jacket_v2 basic pin headset
            kor "But intuition as we use it here means more than that."
            show korin jacket basic pin
            kor "We use it to test an assumption, to try and build the case based on our analysis of the evidence."
            hide korin with dissolve
            hide ecmc with dissolve
            "She paces around behind me and I turn to follow her, awed by the graceful way she moves, dauntless even in her heels on the uneven ground."
            show korin jacket basic pin at right1 with dissolve
            show ecmc jacket_v2 smile pin headset at left2 with dissolve
            kor "And don't assume intuition is some granted talent. It's a skill, like any other."
            show ecmc jacket_v2 surprised pin headset
            mckorin "Then...how do I build it?"
            show korin jacket smirk pin
            kor "Empathy. Lived experiences that allow you to put yourself in the mind of others."
            hide korin
            hide ecmc
            show ecmc jacket_v2_cu smile_cu headset_cu at ecmc_cu
            "(I could keep listening to her all day...)"
            hide ecmc
            show korin jacket smirk pin at right1
            show ecmc jacket_v2 surprised pin headset at left2
            "I shake off the dreamy feeling taking over."
            hide korin
            hide ecmc
            show ecmc jacket_v2_cu embarrassed_cu headset_cu blush_cu at ecmc_cu
            "(Because of the {i}work{/i}. I'm captivated by the work. That's all.)"
            hide ecmc
            show korin jacket smirk pin at right1
            show ecmc jacket_v2 surprised pin headset at left2
            kor "If you're missing a key piece of evidence, how do you find it?"
            show ecmc jacket_v2 smile pin headset
            mckorin "Put yourself in the mind of the person that made it."
            show korin jacket smirk pin at centre behind ecmc
            "She steps closer. I feel my heart skip as she puts her hands on my shoulders and turns me around."
            hide ecmc
            hide korin
            show korin jacket_cu basic_cu at korin_cu:
                xpos 400
            show ecmc jacket_v2_cu basic_cu headset_cu at ecmc_cu:
                xpos -200

            "Her words are soft, close to my ear."

            kor "Tell me about this place. Build a narrative."
            show ecmc jacket_v2_cu determined_cu headset_cu
            mckorin "I see equipment gutted for valuable components."
            show korin jacket_cu smirk_cu
            kor "And you see the gaps for missing pieces because..."
            show ecmc jacket_v2_cu smile_cu headset_cu
            mckorin "Because I'm a scrapper. I spend a lot of my spare time in junkyards just like this."
            show korin jacket_cu basic_cu
            kor "How come?"
            show ecmc jacket_v2_cu surprised_cu headset_cu
            mckorin "People discard things here all the time. Things like…"

            "I pick up a stringy piece of busted hardware attached to a finger-sized drive I hadn't seen before."
            show ecmc jacket_v2_cu determined_cu headset_cu
            mckorin "Domestic tech in an industrial scrapyard that's under D.I.V.A.A. surveillance..."

            "I look to Korin for a hint, but she gives nothing away."

            mckorin "...Someone put it here on purpose."

            kor "Why?"

            mckorin "The appeal of RunBacks is they use a programmable subroutine set to capture memories of specific faces."
            show korin jacket_cu smirk_cu
            kor "Sounds useful."
            show korin jacket_cu surprised_cu
            mckorin "The trouble with these older models, though, is you couldn't get rid of a memory imprint calibration."

            "Korin looks a little lost, so I cut to the chase:"

            mckorin "If it was calibrated forever to someone the user didn't want to remember anymore, it'd be useless."

            kor "So you think whoever put this here is hiding something from their past?"
            show ecmc jacket_v2_cu sad_cu headset_cu
            mckorin "Eh..."

            kor "What does your intuition tell you?"
            show korin jacket_cu basic_cu
            mckorin "More likely, someone threw it here to try and {i}forget{/i} someone from their past."

            mckorin "A piece of retro tech that can be calibrated only once to a specific face?"

            mckorin "It's the ultimate gift from a scrapper in love."

            mckorin "But...relationships end all the time..."
            show korin jacket_cu sad_cu
            kor "Whoever put it here didn't have the heart to destroy it themselves?"
            show ecmc jacket_v2_cu surprised_cu headset_cu
            mckorin "They threw it here, knowing someone else would do it for them."
            hide ecmc
            hide korin
            show ecmc jacket_v2 smile pin headset at left1
            show korin jacket smile pin at right1 behind ecmc
            "Korin folds her arms, looking impressed."

            kor "Fascinating!"
            show ecmc jacket_v2 basic pin headset
            show korin jacket sad pin
            kor "...And a little sad."

            "She unsheathes an evidence bag and logs the drive using her own ARCware."
            show korin jacket basic pin
            kor "We'll let our techs take a look. I'd love to see if you're right."

            kor "Even if you're not, maybe it'll lead to valuable evidence in the case."
            hide ecmc
            hide korin
            show korin jacket_cu smile_cu at korin_cu
            kor "Good work, [genericfn]. I knew you'd catch on quick."
            hide korin
            show ecmc jacket_v2 smile pin headset at left1
            show korin jacket smirk pin at right1 behind ecmc
            "Her compliment makes me feel like I'm floating."
            hide korin
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
            "(She probably makes all the trainees feel this way. Right?)"
            hide ecmc
            show ecmc jacket_v2 basic pin headset at left1
            show korin jacket smirk pin at right1 behind ecmc
            kor "Funny how people get so attached to old tech..."
            show ecmc jacket_v2 surprised pin headset
            mckorin "...Speaking of, where is Baby Bird?"
            show korin jacket smile pin
            kor "Oh, I don't bring it out in the field."
            show ecmc jacket_v2 basic pin headset
            mckorin "It's handy around the office. Out here, it'd just get in your way, right?"
            hide ecmc
            hide korin
            show ecmc jacket_v2_cu smile_cu headset_cu at ecmc_cu
            "({i}Funny how people get so attached to old tech,{/i} she said.)"
            hide ecmc
            show ecmc jacket_v2 smile pin headset at left1
            show korin jacket basic pin at right1 behind ecmc
            mckorin "But that's not all of it, is it?"

            mckorin "Obsolete as it is, you'd be devastated if something happened to it while you were out in the field."
            show korin jacket smile
            kor "Hey, I didn't say you could use these skills on {i}me!{/i}"

            "She gives my shoulder a playful little push, emboldening me a bit."

            mckorin "Better watch out. Who knows what deep, dark secrets I'll pick out about you next?"

            "Korin laughs and brushes her hair out of her face. Just as I think I've caught her by surprise..."
            hide ecmc
            hide korin
            show korin jacket_cu smile_cu at korin_cu
            kor "I hope you like what you find."
            hide korin
            show ecmc jacket_v2 surprised pin headset at left2
            show korin jacket smile pin at right1
            "...I'm on my back foot again."

        "B. Reject the opportunity.":
            $menuhideborder = False
            show korin jacket basic pin at right1
            show ecmc jacket_v2 basic pin headset at left2
            mckorin "I appreciate the offer...but maybe I should figure this out for myself."

            "Korin shrugs."

            kor "Flag me down if you change your mind."
    hide ecmc
    hide korin
    show korin jacket surprised pin at centre
    "Korin looks out at the rest of the trainees."
    hide ecmc
    hide korin
    show korin jacket_cu smile_cu at korin_cu
    kor "I should get back to it. Great work, though. And good luck with the rest of your report!"
    hide korin
    show ecmc jacket_v2 determined pin headset at centre
    "Korin leaves, and I focus on my sector."

    "Most of the equipment has been gutted, but I'm a scrapper. I know just where to look in places like this."
    show ecmc jacket_v2 surprised pin headset
    "Fortune favors me as a palm-sized drive falls into my hands from the rusted-out remains of a defunct work cube."
    hide ecmc
    show ecmc jacket_v2_cu smile_cu headset_cu at ecmc_cu
    "(Well, hello. What are you doing here?)"
    hide ecmc
    show ecmc jacket_v2 surprised pin headset at centre
    "In the grooves of the serial number, I see faint traces of..."
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
    "(Um. Is that blood?)"
    hide ecmc
    show ecmc jacket_v2 determined pin headset at centre
    "I stop myself, remembering D.I.V.A.A. procedure."
    hide ecmc
    show ecmc jacket_v2_cu determined_cu headset_cu at ecmc_cu
    "(All evidence must be logged by an ARCware scan before further handling.)"
    hide ecmc
    show ecmc jacket_v2 surprised pin headset at centre
    "I slip on my interface and start the scan. The contents of the drive appear in a garbled text box."
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
    "(Wait, is it corrupted?)"
    hide ecmc
    show ecmc jacket_v2 sad pin headset at centre
    "A pit forms in my gut."
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
    "(No--it's {i}being{/i} corrupted!)"
    show ecmc jacket_v2_cu angry_cu headset_cu at ecmc_cu
    "(But it's impossible for a scan to do that!)"
    hide ecmc
    show ecmc jacket_v2 angry headset pin at centre
    "I open my interface and start executing commands to try and stop the spread."

    "The drive whines like it's fighting me."
    show connie casual basic at right3 with dissolve
    "I'm concentrating so hard, I don't notice footsteps behind me."

    con "What's going on?"

    "There's no time to answer her."
    show connie casual angry
    con "You're... hey! What are you doing?!"
    $menuhideborder = True
    menu korine1c3:
        "A. There's something wrong!":
            $menuhideborder = False
            show ecmc jacket_v2 angry pin headset at centre
            show connie casual angry at right3
            mckorin "There's something wrong with this drive! I'm trying to focus on fixing it!"
        "B. I don't have time to explain!":
            $menuhideborder = False
            show ecmc jacket_v2 angry pin headset at centre
            show connie casual angry at right3
            mckorin "I don't have time to explain what you don't have time to understand! Just let me focus on stopping this…"

        "C. Scuff off! I need to concentrate!":
            $menuhideborder = False
            show ecmc jacket_v2 angry pin headset at centre
            show connie casual angry at right3
            mckorin "Scuff off! I need to concentrate!"

            con "{i}Excuse me?!{/i}"
            hide ecmc
            hide connie
            show ecmc jacket_v2_cu sad_cu headset_cu at ecmc_cu
            "(Okay. That was probably not the best thing to say to Griffin Detective Vega's personal assistant...)"
            hide ecmc
    show ecmc jacket_v2 surprised pin headset at left1
    show connie casual angry at right3
    "I flinch as Connie practically shrieks at me."

    con "You're ruining evidence!"
    show ecmc jacket_v2 angry pin headset
    "I jab a finished command into my interface and whirl around to face her."

    mckorin "I'm {i}saving{/i} evidence!"
    show ecmc jacket_v2 surprised pin headset
    "I realize we're making a scene, drawing attention."

    con "Phoenix Reyes! You need to come over here this instant."
    hide connie
    hide ecmc
    show korin jacket basic pin at centre
    "Korin blinks in surprise at Connie's order, but keeps her expression otherwise neutral."
    hide korin
    show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
    "(How does she {i}do{/i} that?)"
    hide ecmc
    show ecmc jacket_v2 surprised headset pin at left3
    show connie casual angry at centre
    show korin jacket basic pin at right3 with dissolve
    kor "I'm right here. What's the problem?"

    con "This cadet just ruined a piece of evidence!"
    show ecmc jacket_v2 angry headset pin
    mckorin "No, I didn't!"

    con "She's executing commands to reformat the drive!"

    mckorin "To stop corruption from wiping the entire thing!"
    show ecmc jacket_v2 sad headset pin
    kor "Everyone, stop."

    "Korin doesn't raise her voice, but her suddenly serious tone makes us all go still."

    "Connie, unfortunately, recovers before I do."

    con "She's violated Article 1 of the D.I.V.A.A. Investigative Procedural Guideline!"
    show korin jacket surprised
    kor "And is yelling about it going to fix that, Ms. Summers?"

    "Connie's mouth snaps shut, but her glare stays."
    show ecmc jacket_v2 surprised headset pin
    kor "That report of yours will actually be of some use to Dom now."
    show korin jacket basic pin
    kor "I suggest you get to work on it, instead of trying to do my job of disciplining my trainees."
    hide connie with dissolve
    "Connie is taken aback. After a moment, she storms away from me, but I feel my blood run cold."
    hide korin
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
    "(Did Korin say…{i}disciplining?{/i})"
    hide ecmc
    show ecmc jacket_v2 sad pin headset at left2
    show korin jacket basic pin at centre behind ecmc
    "Korin puts a hand on my shoulder."
    show korin jacket sad
    kor "You okay?"

    mckorin "I just want the chance to explain what happened."

    kor "But are you okay?"

    "Something about Korin's presence calms me."
    show ecmc jacket_v2 sleep pin headset
    "I take a deep breath, steadying breath and nod."
    show ecmc jacket_v2 basic pin headset
    mckorin "I'm fine."

    "Korin turns to address the rest of the crowd."
    show korin jacket smile pin
    show ecmc jacket_v2 surprised pin headset
    kor "Why don't you walk the group through which protocols you followed, and exactly what happened when you did?"

    "I feel myself start to sweat, but Korin gives me an encouraging nod."

    kor "It'll give Ms. Summers a chance to {i}accurately{/i} capture what happened in her report."
    hide ecmc
    hide korin
    show ecmc jacket_v2_cu determined_cu at ecmc_cu
    "(Okay. Good. Korin's looking out for me, and I can set the record straight.)"
    hide ecmc
    show ecmc jacket_v2 basic pin headset at left2
    show korin jacket smile pin at right1 behind ecmc
    "I repeat step-by-step the protocols I followed."
    show korin jacket smirk
    kor "Sounds to me like you followed Article 1 to the letter."
    hide ecmc
    hide korin
    show connie casual smile at centre
    "Connie speaks up from the back of the group."

    con "And if we're following Article 1 to the letter, she'll still be subject to Addendum 5.04.17."
    hide connie
    show ecmc jacket_v2 basic pin headset at left2
    show korin jacket sad pin at right1 behind ecmc
    "Korin's expression grows stiff."

    kor "That Addendum, Ms. Summers, is too advanced for these cadets to know offhand."

    kor "It's way, {i}way{/i} too harsh for this situation."
    hide ecmc
    hide korin
    show ecmc jacket_v2_cu surprised_cu headset_cu at ecmc_cu
    "(Korin said our work during training is going to affect our opportunities as official investigators.)"
    show ecmc jacket_v2_cu sad_cu headset_cu
    "(Oh bot. What's going to happen to me?)"
    hide ecmc
    show connie casual angry at centre
    con "That's up to Griffin Vega to decide. It'll be your word against his."
    hide connie
    show korin jacket_cu smirk_cu at korin_cu
    "My legs feel like jelly, but Korin puts a steadying hand on my shoulder."

    kor "Yes. I guess it will."

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False


    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
