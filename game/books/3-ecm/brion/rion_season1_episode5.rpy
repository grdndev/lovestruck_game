label rion_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_rion_s1_ei2 with fade:
        transform_anchor True zoom 1.0 xpos 1.0 ypos 0.5 xanchor 1.0 yanchor 0.5
        linear 5 zoom 0.65
    play music ecmromantic3

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "I look down at Rion, my face heating as I realise how close our bodies are, my legs sandwiched between his."
    "(Oh my bot! What should I do?! This is so awkward!)"
    "(Should I get up? Should I apologise? Make a joke?!)"
    "I start to look around in panic, doing my best to avoid Rion's gaze, as I try to figure out how best to get out of this position."
    ri "Um, [genericfn]?"
    "I look down at Rion to see him smirking at me."

    scene bg ecm_traincar_on at bg with fade
    show rion jacket_cu smirk_cu at rion_cu
    ri "Could you get off me?"
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Oh, yeah! Of course!"

    stop music
    play music ecmcalmeveryday4

    scene bg ecm_traincar_on at bg
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    with hpunch
    "Feeling absolutely mortified, I shift to the side so quickly that I bump my elbow against the floor."

    show ecmc jacket_v2_cu sad_cu
    "(Ugh. Why am I so injury prone?)"
    hide ecmc

    show rion jacket pin basic at left1plus, step_in
    show ecmc jacket_v2 pin embarrassed at right1plus, step_in
    "Rion helps us both to our feet, but I still feel unsteady, my entire body shaking slightly."
    ri "That was a very graceful fall."
    "I look closely at Rion, but his gaze is stoic."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(I can't tell if that's a compliment or not!)"
    hide ecmc
    hide rion

    $menuhideborder = True
    menu rions1e5c1:
        "A. Thank him for cushioning my fall.":
            $menuhideborder = False

            show rion jacket pin basic left1
            show rion jacket pin smile at right1plus
            mcrion "Thanks for cushioning my fall."

            show rion jacket smirk
            ri "Well, we're a team after all, but when I said I'd support you, that wasn't exactly what I meant."

        "B. Make a joke about falling for him.":
            $menuhideborder = False

            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin surprised at right1plus
            mcrion "I guess that's one way to show I'm falling for you!"

            show rion jacket surprised
            "I notice Rion's eyes widen as soon as the joke leaves my lips."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(Crap! That didn't land the way I meant it to!)"
            hide ecmc


        "C. Angrily comment on the rude passenger.":
            $menuhideborder = False

            show rion jacket pin basic at left1
            show ecmc jacket_v2 pin blush determined at right1plus
            mcrion "I can't believe how rude that passenger was!"

            show ecmc jacket_v2 sad -blush
            "I rub my rib cage where the stranger elbowed me and grimace."
            mcrion "That's definitely going to bruise."


    show ecmc jacket_v2 pin basic at right1plus:
        pause 0.1
        easein 0.6 right1
    show rion jacket pin basic at left1
    "I move back beside Rion, limping very slightly."

    show rion jacket sad
    ri "Is your leg still giving you trouble?"

    show ecmc jacket_v2 sad
    mcrion "No. I think I may have done something to my foot when we fell."

    show rion jacket smirk
    "Rion raises an eyebrow very slightly at me, his lips quirking up in amusement."
    ri "You really are accident prone."

    show rion jacket smile
    ri "Let me take a look."

    show rion jacket basic:
        transform_anchor True rotate 0
        easein_circ 0.2 rotate 4 yoffset -10 xoffset 15
        linear 0.4 yoffset 150
        linear 0.4 yoffset 250 alpha 0.0

    show ecmc jacket_v2 basic
    "Rion bends down beside me and carefully lifts my pant leg to take a closer look."
    hide rion

    hide ecmc
    show rion jacket_cu smile_cu at rion_cu
    ri "Hold on to my shoulders. I'm going to lift your foot to get a better look."
    hide rion

    "I grip on to Rion's shoulders as he gently lifts my foot, his fingertips prodding and pressing against my ankle."

    show rion jacket_cu basic_cu at rion_cu
    ri "Does this hurt?"
    hide rion

    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    mcrion "No."
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    "Rion continues to examine my foot, his brow furrowed in concentration as he carefully bends it one way then the other."

    show rion jacket_cu surprised_cu
    ri "What about this?"
    hide rion

    show ecmc jacket_v2_cu angry_cu at ecmc_cu
    "Rion presses his thumb into a spot on my foot and I let out a hiss."
    hide ecmc

    show rion jacket_cu basic_cu at rion_cu
    ri "Alright. It looks like you have a small bruise."
    hide rion

    show ecmc jacket_v2 pin basic at right1plus
    show rion jacket pin basic at left1:
        yoffset 200 alpha 0.0
        easein_back 0.6 yoffset 0 alpha 1.0
    "Rion gently lowers my foot to the ground and stands back up."

    show rion jacket smirk
    ri "You should be fine, but let me know if it gets worse."

    show ecmc jacket_v2 smile
    mcrion "Thank you for checking it out."
    ri "Of course. I really need you in one piece if you're going to be helping me with this investigation."

    stop music
    play music ecmmctheme
    scene bg ecm_generic_office_on at bg with fade

    "Once we get back to HQ, I follow Rion into his office."

    show rion black pin smirk at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "Alright. Let's go through the evidence."

    show rion black basic
    ri "We know Skye found that part in the junkyard and likely sold it to the murderer."

    show rion black angry
    ri "We know the buyer was anonymous, so once we pull on that thread, new information should shake loose."

    show rion black basic
    show ecmc jacket_v2 determined
    mcrion "We also know that a lot of the victims have ties to Blythe's gallery."

    show rion black sad
    ri "Yes, and there's too many for it to just be a coincidence."

    show rion black angry_sleep
    show ecmc jacket_v2 basic
    "Rion scrunches up his face in concentration, then he sighs, leaning forward as he rests his head in his hands."

    show rion black sad
    ri "I think the fact that most of the artwork there featured themes of robotics and consciousness is likely significant."
    ri "But I can't figure out how it all links together."

    show ecmc jacket_v2 surprised
    mcrion "Maybe the killer used the artwork to hide hidden messages and is killing people who discover his secrets?"

    show ecmc jacket_v2 sad
    ri "I don't think that's it, but it could be a possibility."

    show ecmc jacket_v2 determined
    mcrion "Maybe the killer is looking for victims who are fascinated by the robotic modifications to the artwork?"

    show ecmc jacket_v2 surprised
    mcrion "Since instead of modifying art with technology, the killer wants to modify humans?"

    show rion black smile
    ri "I think we're getting closer."

    show ecmc jacket_v2 basic
    show rion black basic
    "Rion taps his finger against his chin as he looks up at the ceiling."
    ri "I think it'll be helpful to go to Blythe's big exhibition when it opens."

    show rion black surprised
    ri "We can see her patrons for ourselves, and possibly identify potential suspects."

    stop music
    play music ecmdomtheme

    hide rion
    hide ecmc
    show dominick uniform basic headpiece pin at centre, step_in
    "Just then, the door opens and a younger-looking man in a gold-motif uniform enters."

    show dominick uniform smirk
    babyfacel "Rion, there you are."

    show dominick uniform basic at right2
    show ecmc jacket_v2 pin basic at left2
    "The man turns to look at me and gives me a polite nod."
    babyfacel "Hello, Hatchling."
    hide dominick

    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I met this guy at training, but I don't remember his name! Was it something like Broderick or Dorian? No, that's not right...)"
    hide ecmc

    show dominick uniform pin headpiece basic at right2
    show ecmc jacket_v2 pin surprised at left2
    mcrion "Hi...um..."

    hide ecmc
    show rion black pin basic at left2
    show dominick uniform angry
    "The man in front of me lets out an exasperated sigh and looks at Rion, clearly unimpressed."
    babyfacel "Oh bot. They're getting slower with every generation."

    hide rion
    show ecmc jacket_v2 pin embarrassed at left2
    "He looks back at me, his lips pursed in annoyance."
    do "I'm Dominick Vega. Griffin Detective, Dominick Vega. Founder and owner of D.I.V.A.A.."
    do "You'd better not forget that again."

    show ecmc jacket_v2 surprised
    mcrion "I...of course! I'm sorry, Sir."

    hide dominick
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "My face flushes in embarrassment, but out of the corner of my eye I see Rion give a subtle eye roll at Dominick."

    show ecmc jacket_v2_cu sad_cu
    "(Maybe Dominick's always like this...)"
    hide ecmc

    show rion black pin basic at left4
    show ecmc jacket_v2 pin basic at left1:
        xoffset 20
    show dominick uniform pin headpiece basic at right4
    do "Well, it appears that the two of you seem to be working productively together."
    do "I wasn't sure your request was a good idea, Rion, and I agreed to pair you both against my better judgement."

    show dominick uniform angry
    "Dominick turns back to face me and narrows his eyes."
    do "I expect big things from you, Hatchling."

    hide rion
    hide ecmc
    hide dominick

    $menuhideborder = True
    menu rions1e5c2:

        "A. Be confident.":
            $menuhideborder = False
            show rion black pin basic at left4
            show ecmc jacket_v2 pin smile at left1:
                xoffset 20
            show dominick uniform pin headpiece basic at right4
            mcrion "I won't let you down."

            show ecmc jacket_v2 embarrassed
            show dominick uniform angry
            do "That's what they all say."

        "B. Question him.":
            $menuhideborder = False
            show rion black pin basic at left4
            show ecmc jacket_v2 pin surprised at left1:
                xoffset 20
            show dominick uniform pin headpiece basic at right4
            mcrion "What kind of things?"

            show ecmc jacket_v2 embarrassed
            show dominick uniform angry
            do "This generation really is getting dumber."
            do "Figure it out, Hatchling."

        "C. Joking response.":
            $menuhideborder = False
            show rion black pin basic at left4
            show ecmc jacket_v2 pin smile at left1:
                xoffset 20
            show dominick uniform pin headpiece basic at right4
            mcrion "So, no pressure?"

            show ecmc jacket_v2 embarrassed
            show dominick uniform angry
            do "If you can't handle pressure, Hatchling, you'll never become an investigator."

    show rion black surprised
    show ecmc jacket_v2 basic
    show dominick uniform basic
    ri "So, Dominick, I know this isn't just a friendly visit."

    show dominick uniform sad
    do "Right. I have some bad news."

    show dominick uniform angry
    do "The FDI is taking over your case and they won't tell me why."
    do "They'll be sending over a liaison, Gael, to ask questions and examine all the evidence."

    hide rion
    hide dominick
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(What?! We're losing the case?)"

    show ecmc jacket_v2_cu embarrassed_cu
    "My heart sinks a little."
    "(Rion will be so disappointed...and does that mean he won't be my trainer anymore?)"
    hide ecmc

    show rion black pin angry at left4
    show ecmc jacket_v2 pin embarrassed at left1:
        xoffset 20
    show dominick uniform pin headpiece basic at right4
    "I look at Rion who purses his lips in annoyance."
    ri "Why are they taking over this case now?"
    ri "We're already getting back on track!"

    show dominick uniform angry
    do "Are you? Do you even have a suspect yet?"
    ri "Dom, he was literally in my hands a couple days ago."
    ri "Handing over the materials will only delay the investigation and give the killer more time to hide!"
    do "Gael is reasonable. It wouldn't surprise me if she wants you and the Hatchling to continue working on the case."
    ri "Can you make sure that happens?"
    do "I can't force the FDI to do anything. At worst, you'll be dismissed from the case."

    show ecmc jacket_v2 sad
    mcrion "And at best?"

    show dominick uniform basic
    do "At best, you'll still be on the case, but Gael will be directing you."
    ri "This is so glitched up!"

    show dominick uniform angry
    do "Just don't embarrass me, Rion. Our relationship with the FDI is important."

    show rion black sad
    show dominick uniform angry at right4, out_right
    "Dominick leaves Rion's office and Rion slumps down in his chair."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu sad_cu at ecmc_cu
    mcrion "Rion..."
    hide ecmc

    show rion black pin angry_sleep at left2
    show ecmc jacket_v2 pin embarrassed at right2
    "I awkwardly hesitate, torn between going over to him and staying where I am."

    stop music
    play music ecmemotional2
    show rion black smirk
    "Rion looks up and gives me a thin-lipped smile."
    ri "It's alright, [genericfn]. These things happen."
    ri "I'm fine. It's fine. Everything's fine."

    show rion black sad at step_out
    "Rion lets out another frustrated sigh, then he stands up and heads towards the door."
    hide rion

    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Is he leaving?!)"
    hide ecmc

    show rion black_cu smirk_cu at rion_cu
    "Just as Rion reaches the door, he turns back and looks at me, an eyebrow raised."
    ri "Aren't you coming?"
    hide rion

    show ecmc jacket_v2 pin surprised at centre, step_out
    pause 0.4
    "I leap to my feet, stumbling slightly, before hastily following after him."

    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(I really don't know how to read Rion. I wonder where we're going.)"

    stop music
    play music ecmromantic2
    scene bg ecm_rooftop_sunset at bg with fade
    "I follow Rion up to D.I.V.A.A.'s rooftop. It's quiet and peaceful up here."
    "The sun is starting to set now, bathing the surroundings in a dim, orange glow."
    "And we're completely alone."

    show rion black pin basic at centre
    "Rion leans back against the building, looking out at the skyline."
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(Should I join him? Something tells me Rion likes being left alone, but he asked me to come!)"

    show ecmc jacket_v2_cu embarrassed_cu
    "(Or maybe he was just being polite? Maybe I should have stayed downstairs?)"
    hide ecmc

    show ecmc jacket_v2 pin determined at centre
    "I put my hands in my pockets, then pull them out and cross my arms, then put them back in my pockets again as I look out at the skyline."
    hide ecmc

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(I think it's best I wait for Rion to speak first.)"
    hide ecmc

    show rion black pin sad at left1plus
    show ecmc jacket_v2 pin embarrassed at right1plus
    "I sneak a glance at Rion. He's still staring out at the skyline, but his forehead is knitted in concentration."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(He's probably thinking about what Dominick said. I wonder how much the FDI involvement will affect his investigation.)"
    hide ecmc

    show rion black pin sad at left1plus
    show ecmc jacket_v2 pin embarrassed at right1plus
    ri "What a bug in the system. The FDI is going to delay everything."
    "Rion reaches up and absentmindedly starts fiddling with his cybernetic eye."
    ri "Gael will need to be brought up to speed, and she'll likely want to do her own follow up which is seriously going to delay things."
    mcrion "Do you think Gael will bump us off the investigation?"
    "Rion shakes his head as he continues fiddling with his eye."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    "(I think that's a stress reaction. Rion doesn't even seem to be aware he's doing it.)"
    hide ecmc

    show rion black pin sad at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    ri "Nah. I know Gael. She won't kick us off, but there's still going to be a huge delay as there's a lot of evidence to sift through."
    ri "I've been working on this case for a long time."
    ri "If everything's held up, the trail will likely go cold."

    show ecmc jacket_v2 sad
    mcrion "What do you think we should do?"

    show rion black surprised
    ri "Well, we could always work around Gael."
    ri "I mean, we'd still keep her informed, but it would be on a need-to-know basis."

    show rion black basic
    show ecmc jacket_v2 surprised
    mcrion "What do you mean?"

    show ecmc jacket_v2 basic
    ri "I mean, Gael only needs to know the important things. She doesn't need to know about any hunches or leads until we have solid evidence."

    show rion black smirk
    ri "Or we could just work behind her back."

    show ecmc jacket_v2 embarrassed
    mcrion "I think it's better to play by the rules."

    show rion black basic
    show ecmc jacket_v2 determined
    mcrion "If the FDI catches us playing things loose, they might take us off the case!"

    show rion black sad
    show ecmc jacket_v2 sad
    ri "That's true, but we can't afford to let the trail go cold again."
    ri "Besides, we don't even know when Gael will take over."
    ri "We can always just work as fast as possible until then."

    show ecmc jacket_v2 smile
    mcrion "Well, that would work. That way we wouldn't technically be going behind their back."
    ri "It's strange that the FDI is taking over. There's definitely a reason behind it. It can't just be a turf thing."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(That {i}is{/i} unusual. I wonder what's going on?!)"
    hide ecmc

    show rion black pin sad at left1plus
    show ecmc jacket_v2 pin basic at right1plus
    "Rion continues fiddling with his eye and I notice he's getting a little more forceful."

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "(Rion seemed a bit sensitive about his eye when we were talking to Blythe, but he won't stop touching it.)"
    hide ecmc

    show rion black pin sad at left1plus
    show ecmc jacket_v2 pin sad at right1plus
    mcrion "Rion, is your eye okay?"
    ri "No."

    show rion black angry_sleep
    "Rion gets out a grunt, then drops his hands as he blinks uncomfortably, like something is caught in his eye."

    show rion black sad
    ri "The focusing lenses are a tad out of alignment and it's getting annoying."

    show rion black basic
    show ecmc jacket_v2 basic
    "Rion starts to fiddle again, then he looks at me, a thoughtful expression on his face."

    hide ecmc
    hide rion
    show rion black_cu surprised_cu at rion_cu
    ri "You're good with tech, right scrapper?"

    show rion black_cu smirk_cu
    ri "Maybe you could check it out and see what's wrong?"
    hide rion

    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "Me?!"
    "I look back at Rion in shock."

    show ecmc jacket_v2_cu embarrassed_cu
    "(I've seen similar technology and I probably {i}can{/i} fix it...but just the thought of being so close to Rion's face...!)"
    hide ecmc

    show rion black_cu smile_cu at rion_cu
    ri "I've seen the way you handle tech, you're no slouch."
    hide rion

    show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
    "I hesitate, feeling a little frozen as my hands start to sweat."
    hide ecmc

    show rion black_cu smile_cu at rion_cu
    ri "What do you say, [genericfn]? I'd really appreciate it if you give it a shot."
    hide rion

    $menuhideborder = True
    menu rions1e5c3:
        "A. Help Rion adjust his eye." (paidchoice = "paidchoice"):
            $menuhideborder = False

            show rion black pin smirk at left1plus
            show ecmc jacket_v2 pin surprised at right1plus
            mcrion "Alright, I'll do my best!"

            stop music
            play music ecmromantic1
            "Rion smirks, his eyes crinkling."
            ri "I know you can do this."

            show ecmc jacket_v2 embarrassed
            mcrion "Can you sit down? You're a bit too tall for me."

            show rion black smirk at left1plus:
                ease_back 0.4 yoffset 180
            "Rion sits down on the concrete and I kneel down beside him."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            "(This is better...)"
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "I hesitate, then wipe the sweat off my palms before gently cupping Rion's face and turning it to face me."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(I'm so close to him...I hope my breath doesn't stink.)"
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "I lean in and do my best to focus on Rion's eye, ignoring the way my heart beats faster."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "Is this the latest Cybereye 6-K-2 model?"
            hide ecmc

            show rion black_cu smile_cu at rion_cu
            ri "That's right."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "Did you add any optical enhancements?"
            hide ecmc

            show rion black_cu smile_cu at rion_cu
            ri "Just a few magnifying and image enhancements. This model had all the capabilities I wanted."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "This is the best model on the market, but some of the components are highly advanced and notoriously finicky."

            show ecmc jacket_v2_cu sad_cu
            mcrion "I'm guessing you have frequent issues with it?"
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "Rion gives a slight shrug of his shoulders."
            ri "I need to tweak it more than some of my older models, but I never really thought much about it."
            hide rion

            show rion black pin basic at left2:
                yoffset 180
            show ecmc jacket_v2 pin basic at centre:
                pause 0.1
                easein 0.4 right1plus
            "I pull back and start looking through my backpack for my tools, trying to ignore the pounding of my heart."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
            "(I know I can fix this, but I really don't want to drop the ball.)"
            hide ecmc

            show rion black pin basic at left2:
                yoffset 180
            show ecmc jacket_v2 pin basic at right1plus
            mcrion "Do you ever get anyone else to look at your eye?"

            show rion black smirk
            ri "Just technicians and doctors."

            show ecmc jacket_v2 surprised
            "I look up from my bag as Rion smirks at me."
            ri "You're the first person outside of that."
            mcrion "Then I hope you don't regret asking me!"

            show rion black smile
            show ecmc jacket_v2 embarrassed
            ri "Relax, [genericfn]. I'm sure you'll do just fine."

            show rion black basic
            show ecmc jacket_v2 basic at right1plus:
                easein 0.4 centre
            "I find the tool I was looking for and turn back to face Rion."

            hide rion
            hide ecmc
            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "Alright, hold still."
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "I lean in a little and place my forefinger and thumb around Rion's eye as I gently part his eyelids to get a better look."
            hide rion

            "Using my tool, I carefully inspect Rion's eye, being careful not to scratch anything."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            mcrion "You're right. The lenses are out of alignment."
            hide ecmc

            show rion black_cu sad_cu at rion_cu
            ri "I think they've been out of whack for a while. I've tried to fix them at home."
            ri "I have recalibration tools, but they never seem to do the job. Sometimes just giving it a whack works."
            hide rion

            show ecmc jacket_v2_cu angry_cu at ecmc_cu
            mcrion "You shouldn't do that. You should always make sure it's recalibrated properly or you could make it worse!"

            show ecmc jacket_v2_cu smile_cu
            mcrion "If you ever need a hand at the office, I always have this tool on me. It should do the job perfectly."
            hide ecmc

            "I lean back in, but as I get a whiff of Rion's woodsy aftershave I shiver slightly, causing my hands to shake."

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "(I need to stay steady!)"
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "I try to ignore Rion and pretend that I'm fixing some old retrotech as I quickly get to work on his eye."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "There. I think I'm done."
            hide ecmc

            show rion black_cu basic_cu at rion_cu
            "I stare into Rion's eye, checking that everything's in alignment."
            hide rion

            show ecmc jacket_v2_cu smile_cu at ecmc_cu
            mcrion "There...you're all set."
            hide ecmc

            show rion black_cu smile_cu at rion_cu
            ri "Thank you, [genericfn]."
            hide rion

            show ecmc jacket_v2_cu surprised_cu at ecmc_cu
            "Rion's voice comes out soft, his breath brushing against my lips, and I suddenly realize I'm still gazing into his eyes, my nose almost touching his."
            hide ecmc

            show rion black_cu smirk_cu at rion_cu
            "I resist the urge to run my fingertips down Rion's chiseled jawline as I take in his entire face, my eyes slowly dropping to his lips."
            hide rion

            show ecmc jacket_v2_cu embarrassed_cu at ecmc_cu
            "My entire body tenses and my heart skips a beat as my lips part instinctively."

            show ecmc jacket_v2_cu surprised_cu
            "(Oh glitch! Abort mission!)"

            show rion black pin basic at left2:
                yoffset 160
            show ecmc jacket_v2 pin surprised blush at centre:
                parallel:
                    easein_circ 0.6 xoffset 130
                parallel:
                    ease_back 0.6 yoffset 180
            "I blush furiously and pull away so quickly that I land on my butt."

            show rion black surprised
            show ecmc jacket_v2 surprised at centre:
                ease_back 0.4 yoffset 0
            "Rion looks at me in confusion as I awkwardly get to my feet."

            show ecmc jacket_v2 smile
            mcrion "So...how's the eye?"

            show rion black basic
            show ecmc jacket_v2 basic -blush
            "Rion blinks a couple times, then he looks around the rooftop."

            show rion black smile
            ri "Everything seems to be perfect."

            show rion black smile at left2:
                ease_back 0.4 yoffset 0
            "Rion gives me a firm nod, before he gets to his feet and brushes himself off."

            hide ecmc
            hide rion
            show rion black_cu smile_cu at rion_cu
            ri "Thanks, [genericfn]."
            ri "If my eye acts up again, I'll always come to you for help first."
            hide rion
        "B. Quit before trying.":
            $menuhideborder = False

            show rion black pin basic at left1plus
            show ecmc jacket_v2 pin sad at right1plus
            mcrion "I'm sorry, Rion, but I really don't want to make the problem worse!"

            show rion black sad
            "Rion tweaks his eye a bit as his forehead furrows slightly."
            ri "Alright, suit yourself."

            show rion black smile
            ri "But anytime you want to help, you're welcome to."

    show rion black surprised at left1plus
    show ecmc jacket_v2 basic at right1plus
    ri "You know, your techy-ness reminds me of someone."

    show ecmc jacket_v2 surprised
    mcrion "It does? Who?"

    stop music
    play music ecmupbeateveryday1

    show rion black smirk
    ri "I'm assuming your dad taught you about electronics growing up?"

    hide rion
    hide ecmc
    show ecmc jacket_v2_cu surprised_cu at ecmc_cu
    mcrion "You knew my dad?!"
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
