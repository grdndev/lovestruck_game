label arianna_season1_episode12:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_jail_cell at bg
    play music mscdanger

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    $ sidecharone = "Mia"

    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Mia is really going to...torture me?)"
    "Nausea brews in my stomach and at the back of my throat."
    "(This isn't happening, right?)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    "Arianna's eyes have gone fiery."
    ai "If you do anything to her, Mia, I will make you regret it."
    show arianna dress angry at right1
    show mscmc jacket_hairdown sad at left2:
        xoffset 20
    "Arianna is trembling with rage."
    hide arianna
    hide mscmc
    show emporia casual smile at centre
    sid1 "How does it feel knowing that you can't do anything about it, hm?"
    sid1 "Watching from the sidelines while you lose everything you care about."
    "Mia picks up a particularly sharp and frightening looking instrument, inspecting it."
    hide emporia

    $ menuhideborder = True
    menu ariannas1e12c1:
        "A. Don't panic.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(It's fine. Everything's fine. Don't panic.)"
            "(I don't want Mia to know I'm scared.)"
            "I inhale a very sharp breath and blow it out slowly."
        "B. Panic":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "Seeing her hold that tool makes me lightheaded and makes my stomach churn."
            "The rope starts to feel too tight around my wrists and my vision is spotty."
            "(No, no, no.)"
        "C. Struggle against your binds.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "The most primal sense of fight or flight kicks in."
            show mscmc angry_cu
            "(I'm {i}not{/i} getting tortured today!)"
            show mscmc jacket_hairdown sad at left2
            show arianna dress sad at right1plus
            "I struggle and pull against the rope around my wrists in a way that makes Mia laugh."
            hide arianna
            hide mscmc
            show emporia casual smile at centre
            sid1 "You get an A for effort."
            hide emporia

    show mscmc jacket_hairdown sad at left2
    show arianna dress angry behind mscmc at right1plus
    ai "You call me pathetic? For what?"
    hide arianna
    hide mscmc
    show emporia casual sad at centre
    "Arianna's voice raises and Mia halts, eyes snapping to Arianna."
    hide emporia
    show arianna dress_cu angry_cu at arianna_cu
    ai "For living a life that I've fought for and enjoy? The same life you want to steal from me?"
    ai "You're the pathetic one, Mia. You're a coward and all you know is how to run and hide."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "Arianna's intensity has me in awe."
    show mscmc embarrassed_cu
    "(She really is so strong.)"
    hide mscmc
    show emporia casual angry at centre
    "Mia's lips twitch into a scowl."
    hide emporia
    show arianna dress_cu sad_cu at arianna_cu
    ai "My life isn't perfect. In fact, sometimes it really really sucks."
    ai angry_cu "I'm an outcast. I chose to live this life and I have to deal with it every day."
    ai "But this is still how I want to live."
    show arianna dress angry at right1plus
    show mscmc jacket_hairdown surprised at left1plus
    "Arianna's arms flex against the rope."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She has to be almost out!)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "You think I'm just going to sit here and watch while you do what you want?"
    ai "You're wrong. I'm going to fight for what I have."
    ai "I'm going to fight for the art that I love."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "Arianna looks at me, heaving with anger."
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "And the people that I love."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Let her have it, Arianna!)"
    hide mscmc
    show emporia casual_cu angry_cu at emporia_cu
    sid1 "Then I will break that spirit of yours!"
    show emporia casual angry at left5:
        pause 0.1
        ease 0.4 left2
    show mscmc jacket_hairdown sad behind emporia at right1plus
    "Mia storms back into the cell and grabs my face, her nails digging into my cheeks."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Shit, here we go!)"
    mcarianna angry_cu "Get off of me!"
    stop music fadeout 0.5
    play music msctense fadein 1.0
    show mscmc jacket_hairdown surprised at right5
    show emporia casual angry at left1plus:
        pause 0.4
        easein_back 0.4 left3
        pause 0.2
        easein_back 0.4 left4
    show arianna dress angry at right1:
        pause 0.1
        easeout_back 0.3 xoffset -50
        easein_back 0.3 xoffset -80
        pause 0.2
        easein_back 0.3 xoffset -140
    pause 1.5
    "But Arianna grabs Mia's wrist and pushes her away from me."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's cut through her ropes! Oh, thank god!)"
    hide mscmc
    show emporia casual_cu angry_cu at emporia_cu
    "Mia's face twists in the fit of anger and shock."
    sid1 "You little-!"
    show bg_msc_jail_cell behind emporia as pulse_effect:
        align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.3
        linear 0.6 zoom 2.0 alpha 0.0
    pause 0.6
    hide emporia
    hide pulse_effect
    show arianna dress_cu angry_cu at arianna_cu
    "Arianna punches Mia in the jaw, making her stumble back."
    ai "Shut up."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Holy shit!)"
    hide mscmc
    show emporia casual sad at centre
    "Mia is momentarily stunned, her face pale as she rubs at her jaw."
    hide emporia
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress basic at left1plus
    "Arianna puts the pocket knife into my hands and steps in front of me."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Thank you, Arianna!)"
    hide mscmc
    show emporia casual angry at centre
    "Mia sloppily throws the scalpel in her hands and it misses Arianna, skittering across the floor."
    show bg_msc_jail_cell behind emporia as pulse_effect:
        align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.3
        linear 0.6 zoom 2.0 alpha 0.0
    pause 0.8
    hide emporia
    "Arianna and Mia run to each other, clashing in a mess of punches and kicks."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I can't believe I'm still tied up!)"
    hide mscmc
    "Neither seems to be trained in fighting but they're scrappy and giving it their all."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "I start cutting at my rope with the knife."
    "(I can't let Arianna get hurt! Even though she does seem to be landing more blows in this fight.)"
    hide mscmc
    show arianna dress angry at centre:
        xoffset 20
        pause 0.2
        easein_back 0.5 xoffset 120
    show emporia casual angry at left4:
        pause 0.1
        easein_back 0.5 xoffset 130
    "Mia manages to grab Arianna around the waist and slams her against the table, a few tools flying off."
    sid1 "You don't deserve your happiness, I do!"
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "I cut the binds as fast as I can, trying to not let the knife slip out of my sweating hands."
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    "Arianna grabs the roll of tools and throws it over Mia's head before pushing her off."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Come on, little knife! Cut!)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "You ruined your own life! God, take responsibility for your shit already."
    show bg_msc_jail_cell behind arianna as pulse_effect:
        align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.3
        linear 0.6 zoom 2.0 alpha 0.0
    pause 0.6
    hide arianna
    show emporia casual_cu angry_cu at emporia_cu
    "Mia rushes at Arianna, making a sound that's a mix between a growl and a yell."
    hide emporia
    "Arianna narrowly ducks out of the way and Mia catches herself against the cell bars."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I think I'm almost through the rope!)"
    show bg_msc_jail_cell behind mscmc as pulse_effect:
        align(0.5, 0.5) transform_anchor True zoom 1.1 alpha 0.3
        linear 0.6 zoom 2.0 alpha 0.0
    pause 0.6
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    "As Mia spins around, Arianna slams her back into the bars with her shoulder."
    hide arianna
    show emporia casual_cu sleep_cu at emporia_cu
    "Mia's head snaps back into the metal."

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show arianna dress sad behind emporia at centre:
        xoffset 60 alpha 0.2
        pause 0.1
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein_back 0.4 xoffset 0
    show emporia casual sleep:
        align(0.5, 0.5) yoffset 300 rotate 0 xpos stagepos[1] + 130 alpha 0.4
        rotate -28
        parallel:
            linear 0.4 alpha 1.0
        parallel:
            easein_back 0.4 yoffset 380
    pause 0.5
    "She goes limp and Arianna flinches as she catches Mia's body in her arms."
    ai "I didn't..."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna beat her!)"
    "I feel the ropes finally fall from my wrists."
    hide mscmc
    show arianna dress sad behind emporia at centre
    show emporia casual sleep:
        align(0.5, 0.5) yoffset 380 rotate 0 xpos stagepos[1] + 130
        rotate -28
    ai "I..."
    "Arianna holds Mia's limp body and sinks to the floor, eyes wide and lost."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "With my hands finally free, I scramble to my feet and over to Arianna."
    "(I can't believe they just fought. I don't even think I can process it.)"
    show mscmc jacket_hairdown basic at right2
    show arianna dress sad at left1
    show emporia casual sleep:
        align(0.5, 0.5) yoffset 400 rotate 0 xpos 480
        rotate -30
    ai "Is she...?"
    show mscmc sad
    show emporia casual sleep:
        align(0.5, 0.5) yoffset 400 rotate 0 xpos 480
        rotate -30
        pause 0.1
        linear 0.7 yoffset 700 alpha 0.0
    pause 0.8
    "Arianna shakes her head and sets Mia down, moving away and into me as I kneel beside her."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(While she may be knocked out, Mia still seems very much alive. She's breathing and I don't see any blood.)"
    show mscmc jacket_hairdown smile at right2
    show arianna dress sad at left1
    mcarianna "No, no. She's fine. You did so good, Arianna."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "I brush the hair away from Arianna's face and tilt her chin up to look at me."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    mcarianna "It's okay."
    hide mscmc
    show arianna dress_cu sleep_cu at arianna_cu
    "I rest a hand on Arianna's cheek and Arianna leans into my touch."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She's sharking. Oh, Arianna.)"
    mcarianna "Look, she isn't bleeding or anything. She's knocked out. Probably has a concussion."
    hide mscmc
    show arianna dress_cu basic_cu at arianna_cu
    "Arianna nods numbly, glancing down at Mia."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Arianna did what she needed to. There was no other way.)"
    show mscmc angry_cu
    "(But we can't wait around for her to wake up or for that butler to come down here.)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "I put my other hand on Arianna's face, cradling her cheek."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcarianna "Arianna, we need to get out of here, okay?"
    hide mscmc
    "Fast footsteps approach and set off every alarm in my body."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Shit, it's the butler!)"
    hide mscmc

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    show maxime casual angry at centre
    mx "Are you alright?"
    show maxime surprised
    "Maxime runs down the stairs, something resembling a gun in his hands."
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Oh my god, you finally showed...yeah, we're fine, I mean considering."
    hide mscmc
    show maxime casual basic at centre
    "He looks over at us briefly before scoping out the rest of the basement."
    mx sad "I got your phone call."
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Probably one hell of a call to get from me.)"
    hide mscmc
    show camilla casual basic at centre
    "Camilla comes down behind him, her eyes taking in the scene and then falling on the unconscious Mia."
    cm smile "I see you two handled it."
    show mscmc jacket_hairdown basic at right5
    show arianna dress basic at right1plus
    show camilla casual basic at left4
    "Camilla eyes Arianna as she steps over Mia's body and crouches, cuffing Mia's hands."
    mcarianna surprised "Wait, there's someone else. Emporia's butler-!"
    cm smile "We took care of him. He's tied up upstairs."
    hide arianna
    hide camilla
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(So, we did it? We're safe?)"
    show mscmc jacket_hairdown basic at right5
    show maxime casual basic at left3
    show arianna dress basic at right1plus
    "Maxime comes over to us and holds his hand out to Arianna to help her up."
    mx surprised "What happened here?"
    hide arianna
    hide maxime
    hide mscmc

    $ menuhideborder = True
    menu ariannas1e12c2:
        "A. I don't even know.":
            $ menuhideborder = False
            show maxime casual sad at left3
            show mscmc jacket_hairdown sad at right3
            "I rub at my temples, a stress headache in the works."
            mcarianna "To be honest, I can't really explain it right now."
            mcarianna "I don't even know."

        "B. She tricked us.":
            $ menuhideborder = False
            show maxime casual surprised at left3
            show mscmc jacket_hairdown sad at right3
            mcarianna "She tricked us, that's what happened."
            hide maxime
            hide mscmc
            show arianna dress sad at centre
            "Arianna runs her fingers over her necklace."
            ai "Yeah and I fell for it."
            hide arianna

        "C. A lot.":
            $ menuhideborder = False
            show maxime casual sad at left3
            show mscmc jacket_hairdown sad at right3
            mcarianna "A lot happened, Maxime."
            mcarianna "Mia took Arianna hostage and was gonna start torturing people."

    show maxime casual sad at left3
    show mscmc jacket_hairdown sad at right3
    mx "How do you know Mia?"
    mcarianna surprised "Remember that lady I was trying to look up? Yeah."
    show mscmc basic
    "Maxime nods, realization dawning on his face. He must've just figured out the anagram."
    hide maxime
    hide mscmc
    show camilla casual angry at centre
    cm "I'm more interested in who {i}you{/i} are."
    show camilla at left3
    show mscmc jacket_hairdown basic at right4
    "Camilla turns her attention to me, her arms crossed."
    hide camilla
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(She's gonna find out I'm a human who knows about mers. Crap.)"
    show camilla casual angry at left3
    show mscmc jacket_hairdown basic at right4
    cm "How do you know about Mia? And how do you know we were looking for her?"
    mcarianna surprised "I, uh, overheard you two talking on the beach."
    hide camilla
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "And she's half-mer. We're both from Maritas."
    show arianna dress grin at left1
    show mscmc jacket_hairdown surprised at right1
    "Arianna pipes up with a hand on the small of my back."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Good one, Arianna. Let's hope they buy it.)"
    hide mscmc
    show camilla casual basic at left3
    show maxime casual basic at right2
    "Camilla nods absently, but Maxime raises a brow at me."
    hide camilla
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Does he buy it?)"
    hide mscmc
    show maxime casual basic at centre
    "He doesn't pursue the issue anymore though."
    hide maxime
    show camilla casual basic at left3
    show arianna dress basic at right3
    "Camilla nods at Arianna."
    cm smile "And you, I'll be taking that illegal magic ring of yours. I'm guessing that's how you have legs right now."
    ai surprised "What?! No way."
    hide arianna
    hide camilla
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I completely forgot about Arianna's ring.)"
    hide mscmc
    show camilla casual basic at left3
    show arianna dress surprised at right3
    cm "I won't write you up for having it, but it's still an illegal magic item so in order to do my job I have to confiscate it."
    show arianna sad
    "Arianna draws her hand in, protecting the ring."
    ai "I'm not giving it to you."
    cm angry "If you insist, I can have you arrested and take it by force if you'd prefer."
    hide arianna
    hide camilla
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It might be Camilla's job, but she doesn't need to be a bitch about it.)"
    hide mscmc
    show camilla casual basic at left3
    show arianna dress sad at right3
    ai "No, it's fine..."
    "Arianna takes off her ring, slowly and with a few grumbles before handing it to Camilla."
    ai "How am I supposed to get my tail back?"
    "Camilla slips it into her pocket and shrugs."
    show arianna angry
    cm smirk "Not my problem."
    hide arianna
    hide camilla
    show maxime casual basic at centre
    mx "You two can leave. Try to take it easy, stay away from exiles. Camilla and I will take it from here."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_labeach_day at bg
    "I thought we might never have the chance again, but the next day Arianna and I are sitting on the beach, toes in the sand."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Less than 24 hours ago we were tied up in Mia's basement.)"
    show mscmc sleep_cu
    "(We made it out.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress basic behind mscmc at right1plus
    mcarianna "Are you okay? I mean, with what happened with Mia?"
    ai smile "Yeah."
    show mscmc basic
    "Arianna hums in thought and rests her chin on her knees."
    ai sad "I've never been in a fight before. I've never hurt someone like that."
    ai angry "I'd do it again in a heartbeat to protect you though."
    show arianna smile
    mcarianna grin "You really saved me, you know."
    show arianna embarrassed
    "Arianna laughs bashfully, brushing her hair behind her ears."
    mcarianna "Really. Thank you."
    show mscmc embarrassed
    "Arianna takes my hand and kisses the back of it before holding it to her chest."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Her lips are soft.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress sad behind mscmc at right1plus
    ai "I hoped things would be different if I stayed up here for my art, not as dangerous as pursuing art in the mer world but..."
    "Arianna lets my hand drop from her chest, but she doesn't let go."
    mcarianna sad "To be fair, what just happened to us isn't...typical."
    mcarianna grin "I promise not every human art buyer is going to be an evil mermaid in disguise."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It's not fair. She was so excited for this job and it turned into such an awful thing.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress sad behind mscmc at right1plus
    ai "Well, yeah. It does suck. Big time."
    show mscmc basic
    ai "Mia Diplore...she was the last person I ever expected to see up here."
    ai angry "And to think she was harboring this wild obsession with me."
    show arianna sad
    mcarianna sad "Yeah, that was a shock to say the least."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Actually, shock is an understatement.)"
    show mscmc jacket_hairdown embarrassed at left1
    show arianna dress basic behind mscmc at right1plus
    "Arianna nods, rubbing her thumb over the back of my hand."
    show mscmc basic
    show arianna sleep
    "Then she groans and closes her eyes."

    $ menuhideborder = True
    menu ariannas1e12c3:
        "A. You made some great sculptures though!":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown surprised at left1
            mcarianna "But you didn't waste your time. You made three incredible sculptures!"
            show arianna sad
            mcarianna smile "You worked hard and it showed."
        "B. Who cares?":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown sad at left1
            mcarianna "Yeah, but..."
            mcarianna grin "Who cares, right? This doesn't change who you are as an artist."
            mcarianna "Anyone would be lucky to have you do work for them."
        "C. I know.":
            $ menuhideborder = False
            show arianna dress basic at right1plus
            show mscmc jacket_hairdown smile at left1
            mcarianna "I know. You put a lot of love and care into your work."
            show arianna sad
            mcarianna grin "It's okay to be upset about that, but tihs is just a small hitch."
            show arianna smile
            mcarianna "Arianna Natida is going to be a huge name in the art world, just you wait."

    show arianna smile
    "Arianna starts to smile."
    mcarianna grin "I'd buy your art for all the money it's worth if I could!"
    show arianna grin
    "I drop her hand and throw my arms up for exaggeration and she giggles."
    mcarianna "Hell, there's loads of people who will buy your stuff. We just need to get your name out there."
    ai "You think so?"
    show arianna smile
    mcarianna "I know so. Even though I'm kinda biased because of our...friendship, I still know you're incredibly talented, like objectively."
    show arianna grin
    "Arianna flips her hair over her shoulder and grins at me."
    hide mscmc
    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show arianna dress_cu grin_cu at arianna_cu
    ai "Praise me more?"
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcarianna "As much as you want."
    "(Anything to make her feel better and let her know just how special she is.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "I'm not the only one who deserves praise here."
    ai "We've both been through a lot and come a long way."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "She takes both of my hands, pulling us in closer to each other as she searches my eyes."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    ai "Thank you. For everything. You mean so much to me, I hope you know."
    ai grin_cu "[genericfn], I want to keep you in my life."
    ai "And I want to be in every bit of yours."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "The sound of the waves dulls and I can only hear the sound of my own heart pounding."
    "(Can she hear it too?)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    ai "I know mine is a mess of a life right now but..."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "The care that I have for her courses through my body."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna's eyes shimmer."
    hide arianna
    "I lean forward and press my lips to her cheek, delicate and sweet."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mcarianna "I don't want to be anywhere else."
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "Me neither. I'll be with you every step of the way."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "As Arianna looks at me, I'm sure my face is as red as hers."
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "I've never met anyone like you."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I can't remember a time I was ever this happy with someone.)"
    mcarianna grin_cu "Me too."
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "I'll fight for you and everything that we have as long as you want me to."
    hide arianna

    $ menuhideborder = True
    menu ariannas1e12c4:
        "A. Tell Arianna you'll fight too!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I hold Arianna's hands tighter, afraid this could all go away."
            show mscmc sad_cu
            "(If things had turned out differently at Mia's, we wouldn't be here like this.)"
            show mscmc jacket_hairdown smile at left1
            show arianna dress smile behind mscmc at right1plus
            mcarianna "I know and I'll fight for us too. I'm not going to let this go."
            show arianna grin
            mcarianna grin "I want you in my life. For every shitty part of it."
            show mscmc sad
            show arianna sad
            "Arianna's eyes widen slightly until they grow watery, her lip trembling."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I didn't say anything wrong, did I?)"
            show mscmc jacket_hairdown sad at left1
            show arianna dress sad behind mscmc at right1plus
            mcarianna "What is it?"
            "There's a softness in my voice that I feel like I've never heard."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I don't want to make you cry, Arianna.)"
            show mscmc jacket_hairdown smile at left1
            show arianna dress smile behind mscmc at right1plus
            "She sniffles and then laughs like she's fighting off tears."
            ai grin "I'm just so happy."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Every time I look at her or talk to her, I know there's no coming back from my realization about my feelings for her.)"
            "When she smiles, I have butterflies in my stomach, every damn time."
            show mscmc jacket_hairdown smile at left1
            show arianna dress grin behind mscmc at right1plus
            ai "What we have is special, isn't it?"
            mcarianna grin "Yeah. I'm not going to let you go."
            ai "Then make sure to hold on."
            mcarianna "I will."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            "Arianna's eyes glance down to my lips and she tilts her head."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(What're you thinking about, Arianna? You can do whatever you'd like to me.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Is it okay if I hold onto you too?"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "What kind of question is that?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Your surfing career is really about to take off with High Tide."
            ai sad_cu "What if you get a bunch of surfer groupies?"
            "Arianna fakes a pout, a twinge of jealousy in her voice."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's way too cute.)"
            "(As if I'd ever sideline Arianna for some kind of groupie.)"
            show mscmc jacket_hairdown grin at left1
            show arianna dress basic behind mscmc at right1plus
            mcarianna "Something tells me I'm not going to be {i}that{/i} famous."
            ai grin "I think you're cute and talented enough."
            show arianna smile
            mcarianna "Well, you might have to stay by my side to keep me grounded during my fame."
            show arianna grin
            "A grin blossoms on her face."
            ai "If you'll have me, I intend to."
            mcarianna "You are more than welcome."
            "Arianan looks down at our hands and her grip grows tighter."
            show mscmc embarrassed
            ai embarrassed "I've never had something like this in my life. {i}someone{/i} like you."
            show mscmc smile
            ai sad "It's hard to trust people. Like, really trust them."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(It makes me so happy to have her open up to me.)"
            show mscmc jacket_hairdown sad at left1
            show arianna dress sad behind mscmc at right1plus
            "Vulnerability flashes across her face as she sighs."
            hide mscmc
            show arianna dress_cu sleep_cu at arianna_cu
            "I let go of Arianna's hands and take her face in my hands."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I feel brave and bold and strong when I'm with her.)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "She leans forward, her lips parted slightly."
            ai embarrassed_cu "I really do like it when you compliment me."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "The low tone of her voice makes my body heat up."
            mcarianna "I know."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "I'll fight off every one of your wild obsessed fans if I have to."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "I'm looking forward to it. I saw how you were with Mia."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            "Arianna smiles sheepishly."
            ai "I didn't scare you off did I?"
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I kind of really loved it.)"
            mcarianna grin_cu "Actually, it was just the opposite."
            mcarianna "I've never seen you like that before."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "I have layers."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Well, I'm looking forward to seeing all of it."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "And I can't wait to see yours."
            "As I stroke her cheeks with my thumbs, Arianna practically nuzzles into my hands."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I will always fight for this.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "My human."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "My mermaid."

        "B. Say nothing.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "I want to say something, but I can't find the words."
            show mscmc embarrassed_cu
            "(I'm happy here with her.)"
            show mscmc jacket_hairdown smile at left1
            show arianna dress smile behind mscmc at right1plus
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(What we have is good. So good.)"
            hide mscmc
            "I listen to the calm waves with a full heart."
    show mscmc jacket_hairdown grin at left1
    show arianna dress basic behind mscmc at right1plus
    mcarianna "So, what's next in your messy life?"
    mcarianna "What madness are you going to get me involved in now?"
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I never thought I'd be pulled this deep into mermaid shenanigans.)"
    show mscmc grin_cu
    "(Can't complain.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress surprised behind mscmc at right1plus
    ai "I've got to get my ring back. Or any magical item that'll give me back my tail."
    show arianna smile
    show mscmc smile
    "Arianna smirks and winks at me."
    ai grin "Even if we have to steal it back."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
