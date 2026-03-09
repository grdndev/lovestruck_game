label arianna_season2_episode12:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_hidden_cove_sunset at bg
    play music mscromanceconfession

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "The moonlight bounces off agitated water of breaking waves all around Arianna and I, as she holds me against her."
    window hide
    show arianna_08_s2e12 with fade:
        align(0.5, 1.0) zoom 1.3
        pause 0.3
        linear 8.0 align(0.5, 0.0) yoffset -220
    pause 8.3
    "Our lips are both parted, our faces mere inches apart."
    "She lets her eyes fall shut. Confidently, she pulls me flush against her as she closes the small distance remaining between our lips and bodies."
    "Her lips press against mine, her kiss hot and urgent as the cool water breaks over us and our mouths and bodies break over one another."
    "(I want to drown in her.)"
    "Her mouth is sweet like strawberries in the summer but her touch is firm as her hands caress and grasp my face, torso, thighs, and ass."
    hide arianna_08_s2e12 with fade
    "My body is burning with desire and I nearly whine in protest when Arianna breaks the kiss."
    show arianna dress_cu grin_cu at arianna_cu
    "She grins at me and pushes an errant loc back behind my ear, but as she does her eyes become watery."
    show mscmc casual_hairup sad at left1 behind arianna
    show arianna dress sad at right1
    mcarianna "Oh no, no, no, no, please don't be sad, Arianna. Everything's ok."
    show arianna:
        easein 0.4 xoffset -60
    "She takes my hand in hers and leans in."
    hide arianna
    hide mscmc
    "She presses a featherlight kiss to my lips and my mouth immediately mourns the memory of hers when she quickly pulls away again."
    show arianna dress_cu sad_cu at arianna_cu:
        transform_anchor True zoom 1.1 yoffset -20 xoffset 40 blur 3 alpha 0.0
        linear 0.5 zoom 1.0 yoffset 0 xoffset 20 blur 0 alpha 1.0
    pause 0.5
    ai "I know that everything's complicated...and that's mostly my fault."
    show arianna smile_cu
    "She laughs weakly."
    ai sad_cu "I'm really trying to figure things out, figure myself out, I promise. It's hard. But all I want—right now, at this moment—is to keep kissing you."
    "Arianna smiles sadly at me as she cups my cheek and runs her thumb over my mouth. Her eyes become filled with longing."
    hide arianna

    $ menuhideborder = True
    menu ariannas2e12c1:
        "A. Kiss Arianna like she's never been kissed before!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc casual_hairup_cu sad_cu at mscmc_cu
            "(I know that Arianna wants this as much as I do.)"
            "(She's so scared, but she doesn't need to be.)"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            "I take Arianna's face in my hands and feel how soft her cheeks are under my thumbs."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(She wants me to make the first move this time.)"
            hide mscmc
            "I kiss her and Arianna presses herself into me, one of her hands going to my wrist."
            "Like the first time we kissed, it feels like we're the only two people on the planet."
            "Each shaky breath we share makes my pool of desire for her grow and grow."
            "Arianna smiles against my lips and her hands snake around my waist."
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Please, touch me more.)"
            hide mscmc
            "I thread a hand in her silky hair, pulling her in as deep as I can."
            "She moans into my mouth and it feels like I lose all sense of myself."
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(I love the way she sounds. The way she feels. God, everything about her.)"
            hide mscmc
            "My other hand slides up her thigh and she shivers under my fingers."
            show arianna dress_cu grin_cu at arianna_cu
            "Then she giggles, pulling back enough so that she can rest her forehead against mine."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            mcarianna "What?"
            show mscmc embarrassed_cu
            "(She is so sexy, but also so fucking cute.)"
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "You're really getting into it."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            mcarianna "Me? What about you?"
            hide mscmc
            show arianna dress_cu embarrassed_cu at truecenter:
                anchor(0.5, 0.4) transform_anchor True zoom 1.0
                easein 0.4 zoom 1.05
                easein 0.4 zoom 1.0
            "She gives me a soft peck."
            ai grin_cu "Don't stop, okay?"
            hide arianna
            "Her voice drops and she drags my hand further up her thigh as she leans her mouth to my ear."
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "I really like it."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Oh, the things she could do to me.)"
            hide mscmc
            "I pull her lips back to mine and I feel her fingers play around my abdomen."
            "So light and delicate that it's a bit ticklish."
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            mcarianna "You can touch other parts of me if you want."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            "Arianna hums against my lips."
            ai grin_cu "I'm taking my time."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(It'll feel good no matter where she touches me, so I'm not complaining.)"
            mcarianna "Tease."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna laughs and her hands slide around my back."
            ai embarrassed_cu "I think you could learn a thing or two about patience."
            ai "About building tension."
            hide arianna
            "Arianna kisses me softly."
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "About passion."
            hide arianna
            "She kisses my lips again and then the corner of my mouth."
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(Arianna is absolutely undoing me on this beach and I do not care if I seem desperate.)"
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "I could give you a lesson if you want."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            mcarianna "If I remember correctly, you kissed me first."
            mcarianna "You're the one who didn't have any patience."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Well, can you really blame me?"
            hide arianna
            "She smiles innocently before claiming my lips again and sliding her hands along my back."
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "You just taste {i}so{/i} good."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(I gave being the dominant one my best shot, but I am utterly powerless against her.)"
            hide mscmc
            "Her lips trail hot kisses along my jaw."
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "And I can't get enough of how you feel against me."
            hide arianna
            "Arianna lays me back in the sand and leans over me, her hair cascading around my face."
            "I lock my arms over her shoulders and pull her down to meet me."
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(I don't care if I'm picking sand off my clothes for the next ten years.)"
            hide mscmc
            "Every time her lips meet mine, I feel like I'm skydiving."
            "My heart beats fast in my chest and my skin feels hot."
            "All I want is for this feeling to never end."
            "I squirm under her wandering hands and wish that our bodies could be even closer."
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(I need her hands on my skin. I need her everywhere.)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu:
                transform_anchor True zoom 1.1 yoffset -20 xoffset 40 blur 3 alpha 0.0
                linear 0.5 zoom 1.0 yoffset 0 xoffset 20 blur 0 alpha 1.0
            "When Arianna breaks her lips from mine, I want to protest."
            ai embarrassed_cu "[genericfn]-"
            hide arianna
            play sound "<to 3>audio/sfx/MSC_Sound_Effects/splash02.mp3"
            "There's a splash from the ocean and Arianna and I both sit up."

        "B. Be unsure.":
            $ menuhideborder = False
            show mscmc casual_hairup_cu sad_cu at mscmc_cu
            "(Should we really do this?)"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            "Arianna immediately sits back when I don't respond."
            ai "Sorry...we don't have to."
            ai "I don't want to pressure you."
            hide arianna
            "Then there's a noise from the water."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show queenie casual smile at left1:
        yoffset 250 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 180
        parallel:
            linear 0.4 alpha 1.0
    "An insane amount of relief goes through me as I see Queenie surface."
    hide queenie
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(She's okay! We knew she wasn't arrested, but we still didn't know where she was.)"
    hide mscmc
    show queenie casual_cu smile_cu at queenie_cu
    qn "Girls! Good to see you're alright."
    hide queenie
    show arianna dress_cu grin_cu at arianna_cu
    ai "Grandma Queenie!"
    hide arianna
    "Arianna rushes forward into the water and hugs Queenie."
    show queenie casual smile at left1
    show arianna dress grin at right1
    ai "I tried to call you! I thought you got arrested!"
    qn "I went into hiding as soon as I saw the news and I figured you two would do the same."
    hide arianna
    hide queenie
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(Probably a good idea that she did. If she'd been arrested, today would've been very different.)"
    hide mscmc
    show queenie casual sad at left1
    show arianna dress basic at right1
    qn "I'm sorry I didn't call you, but I was worried that they'd try to track my calls."
    show queenie smile
    ai surprised "Oh, yeah...probably a good idea."
    show queenie casual basic at right1
    show arianna smile at right4
    show mscmc casual_hairup smile at left4:
        alpha 0.0 xoffset -80
        easein 0.4 alpha 1.0 xoffset 0
    "Arianna sits back in the shallow water and I come over to join the two of them."
    qn angry "That boy, Casper, what was he thinking?"
    qn "The resistance is going to need to rethink our plan now."
    hide queenie
    hide arianna
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(We have some good news for Queenie and the entire resistance.)"
    show queenie casual angry at right1
    show arianna dress smile at right4
    show mscmc casual_hairup surprised at left4
    mcarianna "Actually, the resistance is going to be okay. For the time being, at least."
    ai surprised "Yeah, we...fixed it."
    show queenie sad
    "Queenie looks between Arianna and I with her eyebrows up."
    qn "What happened?"
    hide queenie
    hide arianna
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(I feel like I still can't believe what we just went through, so this is a good way to process it.)"
    show queenie casual sad at right1
    show arianna dress basic at right4
    show mscmc casual_hairup sad at left4
    mcarianna "We went to confront Casper about the banner and threat."
    ai sad "And it turned into a fight."
    ai "Maxime showed up, but Casper admitted he was wrong and Maxime arrested him."
    hide queenie
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(We kind of owe Maxime big time for letting us go twice now.)"
    show queenie casual sad at right1
    show arianna dress basic at right4
    show mscmc casual_hairup surprised at left4
    mcarianna "Casper's going to act as the head of the resistance so that the government will back off."
    show mscmc basic
    show queenie basic
    "Queenie's mouth opens lightly in shock, her eyebrows knit."
    qn "And...you two are alright?"
    show mscmc embarrassed
    show arianna grin
    "Arianna slips her hand into mine and when she smiles at me, my cheeks burn."
    ai "We are. I'm glad we're all okay."
    show arianna basic
    mcarianna surprised "There was something kind of weird though during the fight with Casper."
    mcarianna "Out of nowhere, there was just this loud noise and then a shower of bright light."
    ai surprised "Yeah, it...kind of saved us. Do you know what that could've been, Grandma Queenie?"
    hide arianna
    hide queenie
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(If anyone knows, it would be the sea witch.)"
    show queenie casual basic at right1
    show arianna dress basic at right4
    show mscmc casual_hairup basic at left4
    "Queenie puts a hand to her chin, taking in what we said."
    qn smile "Interesting...well, I'm not sure off the top of my head, but I can think on it."
    qn "But I'm glad you two are okay. You work quick, no one else was arrested."
    qn "You make a good team."
    show arianna smile
    "Arianna squeezes my hand."
    ai "We really do."
    hide arianna
    hide queenie
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(I've never connected with someone like Arianna before. I hope we can always be a team.)"
    show queenie casual smile at right1
    show arianna dress smile at right4
    show mscmc casual_hairup basic at left4
    qn "And, I think that you, [genericfn], have proven yourself worthy of a tail."
    show mscmc surprised
    "A jolt of shock goes through me."
    mcarianna "Really?!"
    show arianna grin
    "I see Arianna grinning out of the corner of my eye."
    hide arianna
    hide queenie
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(I never thought this day would come!)"
    show queenie casual smile at right1
    show arianna dress grin at right4
    show mscmc casual_hairup grin at left4
    qn "Really."
    qn "Meet me tomorrow afternoon and I'll have a magic item ready for you."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    scene bg msc_mc_bedroom_day at bg with fade
    "When it's the next day, I feel like I can barely contain myself."
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Breathing underwater is awesome enough, but actually being a mermaid? Holy shit!)"
    show mscmc casual_hairdown grin at left2
    show arianna dress smile at right2
    mcarianna "I can't believe Queenie's really giving me a tail!"
    mcarianna "This is, like, every person's dream!"
    "Arianna chuckles from the edge of my bed as she watches me walk up and down my room."
    ai grin "Well, like Queenie said, you definitely deserve it."
    ai "If there's one human I want underwater, it's you."
    hide mscmc
    hide arianna

    $ menuhideborder = True
    menu ariannas2e12c2:
        "A. I hope my tail is cool!":
            $ menuhideborder = False
            show mscmc casual_hairdown grin at left2
            show arianna dress smile at right2
            mcarianna "I wonder what my tail's gonna look like. I hope it's cool!"
            mcarianna "What influence a tail's color?"
            show arianna grin
            "Arianna shrugs apologetically."
            ai "I don't know—I was born with mine."
        "B. What should we do first?":
            $ menuhideborder = False
            show mscmc casual_hairdown grin at left2
            show arianna dress smile at right2
            "I tap a finger to my chin."
            mcarianna "Having a mermaid form means that I can go way more places."
            mcarianna "Maybe I can finally see a mer city? What do you think?"
            ai grin "As long as we're careful, I don't see why not."
        "C. It'll be weird not to have legs.":
            $ menuhideborder = False
            show mscmc casual_hairdown grin at left2
            show arianna dress smile at right2
            mcarianna "I've never not had legs before. I wonder what it'll feel like."
            ai grin "There will be an adjustment period for sure, but nothing you can't handle."
            ai "It might be easier to go from legs to tail than tail to legs."

    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(The possibilities are endless! Thanks to the magic shell I have, I'm already comfortable in the water.)"
    show mscmc embarrassed_cu
    "(And...I can spend way more time with Arianna.)"
    show mscmc casual_hairdown embarrassed at left2
    show arianna dress grin at right2
    "I stop my anxious walk and see Arianna smiling at me."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(What will this mean for our future? We can go anywhere we want together.)"
    show mscmc casual_hairdown smile at left2
    show arianna dress grin at right2 behind mscmc
    "Arianna leans back on her hands, the sweetest look in her eyes."
    ai "You won't have to hide every time someone comes knocking on my studio."
    mcarianna grin "I'll need some kind of mermaid backstory."
    ai "We'll think of something good for it, don't worry."
    show mscmc:
        easein 0.4 left1
    show arianna smile
    pause 0.4
    "Arianna reaches her hand out, asking for mine."
    ai grin "You having a tail...well, it'll make things a lot easier for us."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(As if we were in a real relationship?)"
    show mscmc casual_hairdown smile at left1
    show arianna dress smile at right2 behind mscmc:
        pause 0.1
        easein 0.4 right1
    pause 0.5
    "I put my hand in hers and she pulls me to stand between her legs."
    ai embarrassed "If we did, you know, get together we could split our time between land and sea."
    mcarianna "It's sweet you've been thinking about it, but I'm okay staying friends."
    mcarianna grin "I don't want you to get into something you don't want or you're not ready for."
    mcarianna "So long as I can stay in your life, I'm happy."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Even if it might be kind of hard and a little bit blurry with us kissing.)"

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show mscmc casual_hairdown embarrassed at left1
    show arianna dress grin at right1 behind mscmc
    "Arianna shakes her head as she takes my other hand."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "But, I don't want to be just friends."
    show arianna embarrassed_cu
    "An intensity shines in her eyes."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(I don't want to get ahead of myself, but this might be the best thing I've ever heard.)"
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "I was really scared before, but you've shown me that that doesn't mean that I can't go after what I want."
    ai "If it's you, I can face my fears."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "I want to think of something to say, but I feel like I can barely breathe."
    "(She means so much to me.)"
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "What I really want is you."
    hide arianna
    "Arianna pulls my hands to either side of her on the bed and I lower myself to kiss her."
    "I'm hyper aware of how her fingers slide up my arms and over my shoulders and around my neck."
    "I sigh into her and she smiles as she kisses me."
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(I could kiss her for the rest of my life and die happy.)"
    hide mscmc
    "Every spot her hands touch leaves an electrifying trail along my skin."
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Touching someone has never felt this good. I think I might get addicted.)"
    hide mscmc
    "My hands start to move up Arianna's waist and she pulls back from me, still agonizingly close."
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "We should go meet my grandma."
    show arianna grin_cu
    "Arianna presses her forehead to mine for a moment and then grins."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Kissing Arianna is so nice that I literally almost forgot I was getting a mermaid tail.)"
    show mscmc casual_hairdown grin at left1
    show arianna dress embarrassed at right1 behind mscmc
    "The excitement over getting another magical item consumes me again and I laugh."
    mcarianna "I'm gonna turn into a mermaid! Holy shit!"
    show arianna:
        easein 0.4 xoffset -40
        pause 0.1
        easein 0.4 xoffset -20
    "Arianna places a kiss to the corner of my mouth and holds my face in her hands."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        xoffset 0
    ai "You are {i}so precious{/i}."
    hide arianna

    stop music fadeout 0.5
    play music mscunderwaterromance fadein 1.0
    $ wavy_transition("bg msc_mc_bedroom_day", "bg msc_underwater_ship_day")
    scene bg msc_underwater_ship_day at bg with dissolve
    "Arianna and I swim out to meet Queenie and I feel like I'm shaking from excitement."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Every time I think I can't be more amazed with the mer world, I am!)"
    "(With a tail, I can really be a part of it and Arianna's life.)"
    show queenie casual smile at left3 behind mscmc
    show arianna siren basic at right4 behind mscmc
    show mscmc bikini_hairdown smile at right1
    qn "How are you feeling, [genericfn]?"
    mcarianna grin "Like I'm dreaming."
    show arianna smile:
        easein 0.2 xoffset -10
        pause 0.2
        easein 0.2 xoffset 0
    "Arianna pinches me and I pull my arm back to rub at the spot."
    mcarianna "Ow?"
    ai grin "You're not dreaming, silly."
    show mscmc basic
    show arianna smile
    qn basic "Do you feel you're ready to accept this gift, [genericfn]?"
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(When she puts it that way, it sounds pretty serious.)"
    "(I've been so happy, I haven't been thinking about what a big deal this must be to Queenie and Arianna. They're trusting me with their world.)"
    show queenie casual basic at left3 behind mscmc
    show arianna siren smile at right4 behind mscmc
    show mscmc bikini_hairdown grin at right1
    mcarianna "I'm ready."
    show queenie smile
    "Queenie smiles warmly and holds up a closed fist."
    show queenie sad
    show mscmc basic
    "She reaches her hand out to me, but then hesitates."
    qn "Well, you have more than proven yourself to me."
    qn angry "But keep in mind that this is a great responsibility and a great power."
    "Queenie fixes me with a somewhat stern eye and I nod."
    show mscmc smile
    qn smile "Use it as you please, but be mindful of that."
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(This is something that I've always wanted. Something that I've been told is impossible.)"
    "(I won't think of this lightly.)"
    show queenie casual basic at left3 behind mscmc
    show arianna siren smile at right4 behind mscmc
    show mscmc bikini_hairdown grin at right1
    mcarianna "I promise not to do any evil."
    show queenie:
        easein 0.4 left1plus
    "Queenie places a ring that looks like Arianna's into my hand."
    hide queenie
    hide mscmc
    hide arianna
    "It flows with the current and the deep penetrative sun rays make the ring look like it's dimly glowing."
    show queenie casual_cu smile_cu at queenie_cu
    qn "Enjoy it."
    hide queenie
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I can at least show my thanks by doing the respectful thank you that Arianna taught me.)"
    show queenie casual smile at left3 behind mscmc
    show mscmc bikini_hairdown grin at right2:
        pause 0.1
        easein 0.5 xoffset -40
        pause 0.1
        parallel:
            easeout_back 0.5 yoffset -50
            pause 0.1
            easein_circ 0.5 yoffset 0
        parallel:
            easein 0.5 xoffset -20
            pause 0.1
            easeout 0.5 xoffset 20
    pause 1.8
    "So, I hold the ring out and bring it up and then bring it back to myself."
    hide queenie
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu:
        xoffset 0
    "(It's important to show my respect for their culture since they're inviting me in.)"
    show queenie casual smile at left3 behind mscmc
    show mscmc bikini_hairdown grin at right1plus:
        yoffset 25
    show arianna siren grin at right4 behind mscmc:
        yoffset -10 xoffset 100 alpha 0.0
        pause 0.1
        easein_back 0.4 xoffset 0 alpha 1.0
    "Queenie nods in appreciation, but I'm almost knocked over by Arianna hugging me."
    ai "I can't believe you're going to have a mermaid form."
    show mscmc embarrassed
    ai "It feels like everything is falling into place for us."
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu:
        yoffset 0
    "I take a moment to enjoy the feeling of Arianna on me."
    "(This is a big step for the two of us and also maybe the first real step to a relationship?)"
    show arianna siren grin at right1 behind mscmc
    show mscmc bikini_hairdown grin at left1
    mcarianna "I hope my legs aren't the only attractive thing about me."
    show mscmc embarrassed
    show arianna embarrassed
    "Arianna laughs and holds me out at arms length, her cheeks red."
    ai "They're nice, but not the only thing you have going for you. Trust me."
    show arianna grin:
        easein 0.4 right2
    "Arianna swims back to give me some room and I look down at the ring in my hand."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(This will change my life forever.)"
    show mscmc bikini_hairdown grin at left1
    show arianna siren grin at right2 behind mscmc
    ai "Okay, okay, put it on!"
    "Arianna puts her hands to her mouth, a grin poking through."
    mcarianna "Okay!"
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(This is it! I'm not sure I'm gonna miss my legs!)"
    hide mscmc
    "I suck in a breath and hold it as I slide the ring onto my finger."
    show arianna siren_cu grin_cu at arianna_cu
    ai "Now, just give it a good rub and think about your legs turning into a tail."
    hide arianna
    "I rub my thumb gently over the ring."
    "Nothing happens."

    $ menuhideborder = True
    menu ariannas2e12c3:
        "A. Try it again.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(Maybe my body just needs to warm up to the magic.)"
            hide mscmc
            "I rub the ring again, this time with some elbow grease."
            show arianna siren_cu sad_cu at arianna_cu
            "Arianna frowns."

        "B. Think harder.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
            "(Am I thinking hard enough? Tail. No more legs. Please, give me a tail.)"
            hide mscmc
            "I close my eyes for a second, trying to focus on the way the ring feels on my finger."
            "But I don't feel anything change."

        "C. Uh...":
            $ menuhideborder = False
            show arianna siren basic at right1plus
            show mscmc bikini_hairdown surprised at left1plus
            mcarianna "Uh...just rub the ring?"
            show arianna sad
            "Arianna nods slowly, but I can tell her excitement is already going down."
            mcarianna sad "I don't think it's working."

    show arianna siren sad at right1plus
    show mscmc bikini_hairdown sad at left1plus
    mcarianna "Am I...doing it wrong?"
    ai "No."
    show queenie casual basic at left4 behind arianna
    show arianna at right4
    show mscmc at right1
    "Arianna puts a hand on my arm and looks at Queenie with a frown."
    ai "Did you mess up the spell?"
    qn sad "I haven't messed up a spell in decades."
    hide arianna
    hide queenie
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Maybe it was {i}me{/i} who messed up the spell... Is there something wrong with me?)"
    show queenie casual sad at left4 behind mscmc
    show arianna siren grin at right4 behind mscmc
    show mscmc bikini_hairdown sad at right1
    "It's hard to hide the disappointment I feel, but Arianna gives me a hopeful smile."
    ai "Don't worry! We'll fix it!"
    ai "Right, Grandma Queenie?"
    "Queenie tilts her head at me and her eyes narrow slightly."
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(She looks like she knows what I did wrong. As long as we can get it sorted, I'm fine.)"
    show arianna siren basic at right4 behind mscmc
    show queenie casual sad at left4 behind arianna
    show mscmc bikini_hairdown sad at right1
    qn "There's only one reason that the magic wouldn't work."
    show queenie:
        easein 0.4 left1plus
    "Queenie swims up to me and takes my face in her hands."
    hide mscmc
    hide arianna
    show queenie casual_cu sad_cu at queenie_cu
    "There's almost a sad smile on her face."
    hide queenie
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(It doesn't seem like good news. What if I can never have a tail?)"
    hide mscmc
    show queenie casual_cu sad_cu at queenie_cu
    qn "If magic inside the bearer is contending with the item's magic, it won't work."
    hide queenie
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Magic in...me?"
    hide mscmc
    show queenie casual_cu smile_cu at queenie_cu
    qn "There's mer magic inside of you, it's waking up."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
