label rion_season1_episode1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_prologue_mini1 at bg with fade
    play music ecmmctheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    mcrion "The year is 2188. I grew up thinking I lived in a golden age, but crimes involving AI, cybernetics, and the virtu-net are rampant."
    mcrion "To keep up with it all, government's outsource half of all law enforcement to private agencies."

    scene bg ecm_prologue_mini2 at bg with fade
    mcrion "My home, Los Angeles, is a sprawl of neon and grime that reeks of passion and desperation."
    mcrion "But, only a few outfits in this city actually care about helping people."

    scene bg ecm_prologue_mini3 at bg with fade
    mcrion "I joined with the best one, D.I.V.A.A., but it's always competing with old guard operations like the F.D.I. and L.A.M.P.."
    mcrion "My dad is one of the top investigators working for D.I.V.A.A., and he went missing over a year ago."

    scene bg ecm_prologue_mini4 at bg with fade
    mcrion "I'll keep moving up the ranks and investigate the truth."
    mcrion "LA is full of secrets, but if I pursue what's in my heart, I hope I'll uncover more than I ever desired."

    stop music
    play music ecmsuspense2
    scene bg ecm_alleyway_day at bg with fade

    show ecmc jacket_v2 pin basic at centre
    "I walk down an alleyway, squeezing past crates and dumpsters. It's only day one of training, but I expected a more interesting investigation."

    hide ecmc
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(At least no one will say I didn't follow orders.)"
    hide ecmc

    "I notice the lid of one of the dumpsters is slightly ajar. Flies cluster around it and nowhere else. I catch a whiff of rotten meat."

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(Just spoiled food, right?)"
    hide ecmc

    "I place my hand over the lid and the hairs on the back of my neck stand up. "

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Here goes nothing.)"
    hide ecmc

    "I lift the lid and freeze. "

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Oh my bot!"
    "(It's a body!)"

    show ecmc jacket_v2_cu embarrassed_cu
    mcrion "Okay, okay. Deep breaths. Step one, record with ARCware headset and observe."
    "My heart rate slows as I talk myself through analyzing the scene."

    show ecmc jacket_v2_cu surprised_cu
    mcrion "There is a device clamped tightly to the left arm. Looks homemade. It has dozens of transistors and an amperage dial."
    mcrion "It may be a DIY restraint, but at full power this would probably stop someone's heart."

    hide ecmc
    "As I lean in to get a closer look, I become aware of footsteps growing louder right as someone in a mask knocks me to the ground."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "What the glitch?!"
    hide ecmc

    stop music
    play music ecmaction1

    show anton hood at centre
    "The masked man frantically looks at me, taking in my D.I.V.A.A. uniform and badge, and notices the open dumpster."

    hide anton
    window hide
    show anton hood_cu at anton_cu:
        transform_anchor True zoom 1.4
    show anton_zoom_hood at centre:
        transform_anchor True zoom 4.0 xpos 0.5 ypos 0.5
    show anton_zoom_hood at centre with dissolve:
        transform_anchor True zoom 4.4
    show anton_zoom_hood at centre with dissolve:
        transform_anchor True zoom 4.8
    show anton_zoom_hood at centre with dissolve:
        transform_anchor True zoom 5.2
        linear 0.2 alpha 0.0

    "I try to stand up, but the man deftly frees the savage restraint from the body and slaps it on my left arm."
    hide anton

    show blue_spark_effect
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "He flicks the dial, and electricity floods my body. I try to rip the restraint off, but the shocks clench my hands shut."
    hide ecmc
    hide blue_spark_effect

    window hide
    scene bg ecm_rion_s1_ei1 with fade:
        transform_anchor True zoom 1.55 xpos 0.0 ypos 1.0 xanchor 0.0 yanchor 1.0
        linear 5 xanchor 1.0 yanchor 0.0 xpos 1.2 ypos 0.0
    pause

    "I hear pounding footsteps and strain my head to see a striking man in a D.I.V.A.A. jacket sprinting towards us."
    window hide
    show bg ecm_rion_s1_ei1:
        linear 4 zoom 0.65 xpos 1.0
    pause
    "(That's not my trainer...Why is a Phoenix Investigator here?)"
    "He crosses the distance in microseconds, his body strong and agile."
    "He fluidly vaults over a dumpster jutting into the alley."
    "Stray papers flutter as he sails through the air."
    "(He moves like an android...)"

    scene bg ecm_alleyway_day at bg with fade
    show rion jacket pin angry at left2:
        xoffset -130
        easein_back 0.4 xoffset 0
    show anton hood at right2:
        xoffset -50
        pause 0.2
        easein_back 0.4 xoffset 0
    "The agent lands and delivers a blow to the attacker."

    hide rion
    hide anton
    show blue_spark_effect
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "I continue trying to pull the restraint off and watch my saviour dodge swings from the masked attacker."
    hide ecmc
    hide blue_spark_effect

    show rion jacket_cu angry_cu at rion_cu
    strongagile "Stop resisting!"

    hide rion
    show anton hood_cu at anton_cu
    "The masked man drives a punch right at the Phoenix Investigator's face which he blocks at the last second."
    maskm "Are you going to waste time with me, or save the trainee?"

    hide anton
    show blue_spark_effect
    show ecmc jacket_v2 pin embarrassed at centre
    "The agile investigator glances back at me. I try to scrape the restraint off on the pavement but I can't move a muscle or gain any leverage."
    hide ecmc
    hide blue_spark_effect

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(I'm a D.I.V.A.A. agent, I can handle this!)"
    hide ecmc

    show rion jacket pin angry at left2
    show anton hood at right2
    "The superagent turns back to the attacker and throws another punch."

    hide anton
    hide rion
    show rion jacket_cu angry_cu at rion_cu
    strongagile "You won't get away with killing all those people!"

    hide rion
    show blue_spark_effect
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Ahh!"
    hide blue_spark_effect

    hide ecmc
    show rion jacket pin surprised at left2
    show anton hood at right2
    "The agent glances at me, then back at the attacker."

    hide rion
    hide anton
    show blue_spark_effect
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "I want to yell that I'll be okay, that he should focus on the suspect, but I can barely make my lungs work."
    hide ecmc
    hide blue_spark_effect

    show rion jacket_cu angry_cu at rion_cu
    toughsavior "Hang in there, Hatchling."
    hide rion

    show rion jacket pin angry at left2
    show anton hood at right2
    "The agent dodges another strike from the attacker just as another burst of pain makes me groan."
    "My saviour looks back at me again, warring instincts clear on his face."

    hide anton
    show blue_spark_effect:
        xpos 0.5
    show rion jacket pin surprised at left1plus, left_in
    show ecmc jacket_v2 pin sad at right1plus
    "He runs over to me."
    hide blue_spark_effect

    hide ecmc
    hide rion
    show anton hood at centre
    maskm "It took you three years to find me, detective. You'll never have another chance."

    show anton hood at centre, out_right
    pause 0.4
    "The masked man sprints away as my saviour gently steadies me."
    hide anton

    show blue_spark_effect
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(No, he's getting away!)"
    hide ecmc
    hide blue_spark_effect


    show blue_spark_effect:
        xpos 0.5
    show rion jacket pin basic at left1
    show ecmc jacket_v2 pin sad at right1
    mcrion "What...are you..."

    toughsavior "Shh... Talking will make it hurt more. Let me remove this."

    stop music
    play music ecmromantic3

    hide blue_spark_effect with Dissolve(1.0)
    pause 0.4
    show ecmc jacket_v2 pin sad at right1:
        parallel:
            easein_circ 0.4 right2
        parallel:
            linear 0.4 yoffset 80
    "He quickly unclamps the device from my arm and my entire body goes numb."

    show ecmc jacket_v2 surprised
    mcrion "We...have to go after him!"
    superagent "Relax, Hatchling."

    show rion jacket basic at left1:
        easein 0.4 centre
        easein_back 0.6 left1
    pause 0.4
    show ecmc jacket_v2 embarrassed:
        parallel:
            ease_circ 0.4 right1
        parallel:
            linear 0.2 yoffset 70
            linear 0.4 yoffset 120
    "The super agent gently places me on my right side and massages up and down my left arm, his touch soothing."

    hide ecmc
    hide rion
    show rion jacket_cu basic_cu at rion_cu
    "Up close, I can't help noticing his sharp features and piercing gaze."
    toughsavior "How are you feeling?"
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "I'm feeling..."
    hide ecmc

    $menuhideborder = True
    menu rions1e1c1:
        "A. Better, thanks to you.":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin sad at right1:
                yoffset 120
            mcrion "Better. I don't know what I would have done if you hadn't shown up."

            show rion jacket smirk
            show ecmc jacket_v2 basic
            "The agent looks at me, a smile tugging at the corners of his lips."
            toughsavior "Something tells me you would have been okay."

        "B. Really weak.":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin sad at right1:
                yoffset 120
            mcrion "Like I could sleep forever."

            show rion jacket surprised
            "My saviour looks at me, his expression filled with concern."
            toughsavior "That device looked like it was sucking the life out of you."

        "C. Angry! He got away!":
            $menuhideborder = False
            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin angry at right1:
                yoffset 120
            mcrion "I'm just mad he got away."
            toughsavior "Don't worry. I'm faster than him."

    hide ecmc
    show rion jacket pin basic at centre, step_in
    "The agent hands me the device then stands up."

    show rion jacket pin basic at left2
    show ecmc jacket_v2 pin basic at right2
    strongsavior "Let your trainer know what happened, and take this back to HQ."

    stop music
    play music ecmmctheme
    show ecmc jacket_v2 surprised
    mcrion "Isn't that against protocol? I'm still a Hatchling."

    strongsavior "You are, but I can still chase the suspect and this evidence is critical."
    strongsavior "If anyone asks, tell them I ordered you to bend the rules, I'll take the heat."

    show rion jacket smirk at left2, out_left
    pause 0.4
    "He winks at me, then sprints after the masked man."
    hide rion

    show ecmc jacket_v2 blush surprised at centre
    "(Wow...)"

    hide ecmc
    show enver casual basic at centre, step_in:
        transform_anchor True
        easeout_back 0.4 yoffset 20
        parallel:
            easein_back 0.6 yoffset 0
        parallel:
            linear 0.6 zoom 1.1
    "Minutes later, I'm finally able to start moving my arms and legs just as my trainer, Enver, runs down the alley."

    show enver casual sad
    en "Whoa, are you alright, [genericfn]?!"

    hide enver
    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "I force a weak smile at him."
    mcrion "I'm okay."
    hide ecmc

    show enver casual sad at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    en "Yeah, and I'm a moon princess. That 'grin and bear it' routine hasn't worked on me since high school."

    show ecmc jacket_v2 smile
    mcrion "And I haven't let you pull your 'big-brother' routine on me since high school, either."

    show enver casual smile
    "Enver chuckles affectionately and helps me to my feet."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "My nerves still tingle as we walk. I think about my saviour's soothing hands, and warmth spreads over my arm."

    stop music
    play music ecmcalmeveryday4
    scene bg ecm_office_lab_on at bg with wiperightdissolve

    "The next couple of hours fly by. Enver and I work with local law enforcement to move the body to a hospital to be autopsied."
    "We end up at the D.I.V.A.A. lab with the scratch-built restraint, but I haven't heard news of my super agent."

    show ecmc jacket_v2 pin smile at right3
    show enver casual basic at left3
    mcrion "Thanks for today, Enver. I'm lucky that I got you as my first trainer."

    show enver casual smile
    en "I may have called in a couple of favors."

    show ecmc jacket_v2 sad
    show enver casual basic
    mcrion "I still can't believe I found a body on my first day..."

    show enver casual sad
    en "I just wanted to send you on a milk run. We find black market tech stashed there sometimes, but never bodies."

    show ecmc jacket_v2 basic
    en "I should've known you'd find something like that on your first day. It's like you were born to do this."

    show ecmc jacket_v2 smile
    show enver casual basic
    mcrion "It's a good thing that the amazing Phoenix Investigator showed up."
    mcrion "Do you know who I'm talking about? He's really fit, with white hair, and has one of those high-end cybernetic eyes."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(And really attractive in an effortless, unassuming way...)"
    hide ecmc

    show enver casual smile at left3
    show ecmc jacket_v2 pin basic at right3
    en "Oh, that's Rion. He's been trying to nab a serial killer suspect since {i}forever{/i}."

    show enver casual basic
    show ecmc jacket_v2 basic
    en "I'm a little shocked he let the suspect go to help you out."

    show ecmc jacket_v2 surprised
    mcrion "Well..."
    hide ecmc
    hide enver

    $menuhideborder = True
    menu rions1e1c2:
        "A.He probably felt bad for me.":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at right3
            show enver casual basic at left3
            mcrion "I was lying on the floor spasming!"

            show enver casual sad
            en "Rion's one of the most focused people I know. He always has his sights set on the ‘greater good'."
            en "He thinks short term pain is worth it for the right outcome."

        "B. Maybe he was just helping because I'm new.":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at right3
            show enver casual basic at left3
            mcrion "He was probably just being nice."

            show enver casual sad
            en "No...Rion thinks it's good for newbies to be pushed out of the nest."

        "C. I hope he caught them in the end!":
            $menuhideborder = False
            show ecmc jacket_v2 pin sad at right3
            show enver casual basic at left3
            mcrion "I'd feel so bad if he lost them because of me!"

            show enver casual smile
            en "Don't worry about that."
            en "Rion makes his own choices and he won't blame you for the outcome of his decisions."

    show enver casual sad
    show ecmc jacket_v2 basic
    en "How are you feeling, anyway?"

    show ecmc jacket_v2 smile
    mcrion "Much better."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "But, nearly all my muscles are still tingly."

    show ecmc jacket_v2_cu angry_cu
    "(I am {i}not{/i} getting a medical waiver on my first day! I'm positive it'll wear off soon.)"
    hide ecmc

    show enver casual smile at left3
    show ecmc jacket_v2 pin basic at right3
    en "Mhm...Well, let's get this device stored and catalogued."

    hide ecmc
    hide enver
    show eko casual basic pin glasses at centre, step_in
    pause 0.4
    "Enver leads me over to an android at the lab counter."

    show enver casual basic at left4
    show ecmc jacket_v2 pin basic at left1
    show eko casual smile at right4
    hitechcharm "Hi, Enver. It's nice to see you. Who's this?"

    show enver casual smile
    en "This is [genericfn], one of the new trainees. MC, meet Eko."

    show ecmc jacket_v2 smile
    mcrion "It's so great to meet you!"

    hide eko
    hide enver
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Whoa, her sensor-suite is out of this world!)"
    hide ecmc

    show enver casual basic at left4
    show ecmc jacket_v2 pin surprised at left1
    show eko casual pin glasses basic at right4
    mcrion "I don't mean to sound rude, but I've never seen sensors like yours before!"
    mcrion "I thought multi-spatial sensors were still undergoing testing."

    show ecmc jacket_v2 basic
    show eko casual smile
    "Eko beams proudly."
    ek "I enjoy that you noticed! Many of my components are not yet currently available to the public."

    show enver casual smile
    en "And that's partly why you're so awesome."
    en "Eko just happens to be one of the very best people at D.I.V.A.A.!"

    show eko casual surprised
    ek "Please, Enver. You're just saying that because I let you take naps in here and keep food for you!"

    show eko casual basic
    en "Even if you didn't do that, you'd still be my favorite."

    show eko casual surprised
    ek "Did you come here just to compliment me, Enver, or do you need something?"

    show enver casual basic
    show eko casual basic
    en "Ultra-Hatchling over here found this weird thing at a crime scene. We need to store it for Rion's case."

    show eko casual smile
    ek "It's good to hear there's new evidence. Let me know if you need anything."
    show eko casual smile at right4, out_right
    pause 0.6
    hide eko
    hide ecmc
    hide enver
    show enver casual_cu smile_cu at enver_cu
    en "Alright, [genericfn] , let's pull up the right form, then we need to take photos to upload, then we need to run a deep scan."
    hide enver

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "I follow Enver's instructions, but my mind wanders."
    hide ecmc

    show enver casual basic at left2
    show ecmc jacket_v2 pin surprised at right2
    mcrion "Does Rion have a particular way he likes evidence stored?"

    show enver casual sad
    en "Yes. With half the fields blank, most of the photos missing, and scans on every other piece of evidence."

    show enver casual basic
    "I stare at him, shocked."

    show enver casual smile
    en "I'm kidding! No, no particular way. He's just known for cutting a corner or two here and there."
    en "He can get away with it, though, with the results he produces. Why do you want to know?"

    show ecmc jacket_v2 smile
    mcrion "Just, you know. It's his case, and he trusted me to bring the evidence back."
    en "Right."
    mcrion "I just want to make sure I'm making a good impression on future coworkers."

    show ecmc jacket_v2 embarrassed
    en "I'll let him know you want to impress him."

    show ecmc jacket_v2 smile
    mcrion "Oh, no, you don't have to do that!"
    en "It's alright, Rion and I go way back, we chat all the time."

    show ecmc jacket_v2 surprised
    mcrion "What?!"

    show enver casual smile at left2:
        pause 0.2
        easein 0.2 left3
        easein 0.2 left2
    show ecmc jacket_v2 angry at right2:
        easein_back 0.4 right1
    "I playfully punch Enver's arm as he chuckles."
    mcrion "Couldn't you have told me that earlier?"
    en "And miss out on your fangirling?"

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "I blush hard, knowing Enver can read me like a book, and try to focus on processing the restraint."
    hide ecmc

    stop music
    play music ecmcalmeveryday3

    scene bg ecm_office_cafe_on at bg with fade
    "Early the next day, I wait with the other trainees in the main D.I.V.A.A. meeting area for our daily trainer assignments."

    show ecmc jacket_v2_cu smile_cu at ecmc_cu
    "(It was fun working with Enver on my first day, but I can't wait to see how other agents do things around here.)"
    hide ecmc

    show ecmc jacket_v2 pin basic at centre
    "I flex my hands, still trying to work out the prickly sensations."
    hide ecmc

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    "(The guy who put that restraint together has a sick mind.)"
    hide ecmc

    "I can't help but overhear some of the conversations of other trainees."
    enthustrainee "Did you hear about Rion? I heard he saved another trainee!"
    oncaffeine "I heard that too! Whoever that girl is is so lucky!"
    oncaffeine "A brush with death for Rion to save me? Yes please."

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Knowing my luck, I'll never get paired with Rion, but it {i}would{/i} be awesome to work with him!)"
    hide ecmc

    stop music
    play music ecmriontheme

    show rion black basic at centre, step_in
    "Just then, Rion enters the room. He looks around, and our eyes lock."

    hide rion
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "Rion heads towards me and my heart starts to beat faster."
    hide ecmc

    show rion black_cu pin_cu basic_cu at rion_cu:
        transform_anchor True
        zoom 0.56 xpos 180 ypos 30
        left_in
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu:
        transform_anchor True
        zoom 0.5 xpos 450 ypos 1.0
    "He nonchalantly leans against the wall beside me."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu surprised_cu at ecmc_cu
    "(Get a grip, [genericfn]. Don't let your inner fan girl freak out!)"
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1
    "I look up at Rion. He gives me a nod in acknowledgment."
    ri "Hey, Hatchling."

    show ecmc jacket_v2 surprised
    mcrion "Oh...uh...hi! I mean, hey!"

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(So much for staying calm and natural...)"
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1
    ri "How are you feeling after yesterday?"
    ri "Enver updated me. Any nerve issues?"

    show ecmc jacket_v2 smile
    show rion black surprised
    mcrion "Nothing serious, I can handle a little glitch."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "(I am {i}not{/i} going to let a few tingles interrupt my training.)"

    show ecmc jacket_v2_cu smile_cu
    "(It was nice of Rion to ask...but he probably treats all the trainees like this.)"

    hide ecmc
    "I watch as other trainers match up with trainees and head out."

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin smile at right1
    mcrion "So...thanks again for taking that restraint off me yesterday."
    "Rion shrugs casually."
    ri "Don't mention it. I'm just glad you're alright."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Should I ask him about the case? Did he catch that guy? Probably not, otherwise everyone would be talking about it.)"

    show ecmc jacket_v2_cu sad_cu
    "(I better leave it alone for now.)"
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin smile at right1
    mcrion "I wonder who my trainer will be today."
    ri "Probably no one you have to impress."

    show ecmc jacket_v2 sad
    "A lingering silence creeps in."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu surprised_cu at ecmc_cu
    "(Why is small talk the worst???)"
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin basic at right1
    ri "Excited to be in the field?"

    show ecmc jacket_v2 smile
    mcrion "Of course! I've wanted to be a D.I.V.A.A. agent ever since I was a kid."

    show rion black smirk
    ri "Good spirit."

    show rion black basic
    show ecmc jacket_v2 sad
    "Without thinking, I flex my hands, trying to wring out the tingles."
    ri "I thought you said you weren't hurt?"

    show ecmc jacket_v2 smile
    mcrion "My nerves must not be fully healed yet. It's really nothing."
    ri "Did you at least fill out your work injury forms?"

    show rion black surprised
    show ecmc jacket_v2 sad
    mcrion "No...?"
    "Rion lets out a frustrated sigh."
    ri "Enver should have helped you with that."

    show rion black basic
    mcrion "I...might've downplayed the injury a bit."
    ri "Come on, let's go handle it now."

    show ecmc jacket_v2 surprised
    mcrion "Right now?"
    ri "Right now."

    show rion black smirk
    ri "I'll show you around a bit. Point out all the fun things trainees aren't supposed to see."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
    "(It {i}would{/i} be nice to spend some one-on-one time with Rion.)"

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin surprised at right1
    mcrion "What if my name gets called while we're gone?"

    hide ecmc
    hide rion
    show rion black_cu basic_cu at rion_cu
    ri "Then I'll personally track your trainer down for you."

    show rion black_cu smirk_cu
    ri "Come on, let me show you around."
    hide rion
    $menuhideborder = True
    menu rions1e1c3:
        "A. Accept Rion's insider tour." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin smile at right1
            mcrion "Sure, that sounds good to me!"

            stop music
            play music ecmromantic1
            scene bg ecm_office_hq_on at bg with wipeleftdissolve
            "I follow Rion through the D.I.V.A.A. offices."

            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin surprised at right1
            mcrion "I've never gone this far into HQ before."
            ri "Eh, it's not all that special."

            show ecmc jacket_v2 smile
            mcrion "Well, it's cool to see D.I.V.A.A. investigators during their day-to-day."
            mcrion "I'm used to just getting the trainee-eye-view of things."

            show rion black smirk
            "Rion eyes me, the corners of his lips quirking up into a smile."
            ri "This will become routine pretty fast, Hatchling."

            hide ecmc
            hide rion
            "Rion looks around us as we walk, searching for highlights to point out."

            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin basic at right1
            ri "Take Oron over there, one of my favorite technology whizzes."
            ri "He's always busy, but I have a hidden stash of chocolate bars to bribe him when I need help."

            show rion black basic
            "Rion lowers his voice, conspiratorially."
            ri "I happen to know Cosmic Bars are his favorite. Get him a king size, and he'll bump you to the top of the queue."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(Insider tips already?)"
            hide ecmc

            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin basic at right1
            ri "And that lady over there is Portia. She's a fiend for gum and can seem a bit like an airhead, but don't let that fool you."
            ri "She's whip smart and can do triple integral calculations in her head. And I do mean {i}any{/i}."

            show rion black smirk
            ri "She's the first person I go to for help with my sports bets."

            hide rion
            hide ecmc
            "Rion and I pass by several more people and he continues to give me a quick run-down on how he navigates the office."
            "I try to mentally record everything Rion says, but I quickly start to lose track."

            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin sad at right1
            mcrion "Ugh, there's no way I'll remember all of this today!"

            show rion black smirk
            ri "Come on, I'm giving you the inside scoop here. Not every trainee gets this kind of treatment."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "My cheeks flush, and I glance away, unsure how to respond."
            hide ecmc

            "Rion continues striding confidently down the hallway and I almost have to jog to catch up."

            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin basic at right1
            ri "Over to the left is the stationary room. It's restocked every Tuesday, but it empties out pretty fast."

            show rion black smirk
            "Rion winks at me, conspiratorially."

            show rion black basic
            ri "If you ever need anything, you can come see me. Just don't tell your trainers where you get the best stuff."

            show ecmc jacket_v2 smile
            mcrion "Are you a supply hoarder?"

            show rion black smirk
            ri "Just with the good stuff!"

            show rion black basic
            show ecmc jacket_v2 basic
            ri "Now up ahead on the right is the break room."
            ri "The snacks are usually decent, but if you want good coffee you better bring your own."

            show ecmc jacket_v2 smile
            mcrion "Do you have a secret stash or something?"

            hide ecmc
            hide rion
            show rion black_cu smirk_cu at rion_cu
            ri "Ah, the Hatchling learns."
            ri "If you're nice to me, maybe I'll let you have some."
            hide rion

            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin blush smile at right1
            "Rion grins at me and I smile back, my heart fluttering a little."
            show ecmc jacket_v2 -blush smile
            mcrion "Thanks for this induction, Rion. This all feels a little less intimidating."

            show rion black basic
            ri "This will be your playground soon enough."

            show ecmc jacket_v2 basic
            "Rion stops outside a door and puts his hand on the doorknob, then hesitates."

            show rion black surprised
            ri "Just as heads up: Connie can be a bit prickly, but I'll have your back."

            stop music
            play music ecmmctheme
            scene bg ecm_generic_office_on at bg with dissolve

            "Before I can respond, Rion opens the door then leads me into a small office."

            show rion black pin basic at left4
            show ecmc jacket_v2 pin basic at left1
            show connie casual basic at right4
            ri "Connie, this is [genericfn], one of the trainees."
            ri "[genericfn], Connie is Griffin Investigator Dominick's assistant."

            show connie casual angry
            co "What do you need, Rion? The trainees are supposed to be waiting in the cafeteria."

            show connie casual basic
            ri "[genericfn] was injured in the field yesterday. She needs to fill out the injury form."

            show connie casual angry
            co "Yesterday?! That form should have been filed as soon as you returned to HQ!"

            hide rion
            hide connie
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(My injury wasn't that serious though! I think...)"
            hide ecmc

            show rion black pin basic at left4
            show ecmc jacket_v2 pin basic at left1
            show connie casual angry at right4
            ri "Mission got in the way, you know how it goes."
            co "Hmph. I suppose I'll let it slide. [genericfn] is still in training, but don't let it happen again."

            show connie casual basic
            "Connie hands us the tablet, and Rion and I quickly fill it out."
            ri "Come on. We should get back to the other trainees."

            hide rion
            hide connie
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "I hope my trainer hasn't left without me."
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            ri "I'm sure they're waiting for you."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "I hope so! I really want to make a good impression."
            hide ecmc

            show rion black_cu smirk_cu at rion_cu
            ri "Something tells me your trainer will understand."

            scene bg ecm_office_cafe_on at bg with wipeleftdissolve
            "Rion and I walk back to the cafeteria, side by side, our arms brushing together every now and then."

        "B. Stay in the room.":
            $menuhideborder = False
            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin sad at right1
            mcrion "I should really stay here to make sure I hear my name being called."
            ri "You know, Hatchling, you really should learn the fine art of rule bending."
            "Rion looks unimpressed and my heart sinks."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu sad_cu at ecmc_cu
            "(Maybe I should have gone with him?)"
            hide ecmc

    "It doesn't take long for every other trainee to get their assignments and filter out of the room."

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "I look around in panic."
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin sad at right1plus
    mcrion "Where's my trainer? Do they know I'm here? Please tell me I didn't screw up a procedure..."
    ri "Don't worry. Your training started the moment I walked up to you."

    show rion black smirk
    show ecmc jacket_v2 basic
    "Rion flashes me a wink."

    hide ecmc
    hide rion
    show rion black_cu smirk_cu at rion_cu
    ri "I'll be your trainer for today."

    hide rion
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "What?! Why didn't you say anything?"
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc jacket_v2 pin surprised at right1plus
    "My new trainer gives me a half-hearted shrug."
    ri "I wanted to see how long it took you to notice that I wasn't looking for my trainee."

    show rion black smirk
    ri "Your people skills need a little sharpening, Hatchling. But don't worry, we're going to work on it."

    show rion black basic
    ri "Let's get going. We have a big day ahead of us."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu blush_cu smile_cu at ecmc_cu
    "(Oh my bot...I hope today goes well!)"

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

