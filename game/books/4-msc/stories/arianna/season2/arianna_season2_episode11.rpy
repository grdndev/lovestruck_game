label arianna_season2_episode11:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_siren_coastal_cave at bg
    play music mscdanger
    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show casper casual_cu basic_cu at casper_cu:
        transform_anchor True zoom 0.7 xoffset 100 yoffset 70
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu:
        transform_anchor True zoom 0.7 xoffset -130 yoffset 160
    "I feel the point of Casper's blade press against my skin."
    mcarianna sad_cu "Casper, don't do this!"
    hide casper
    hide mscmc
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(I never thought that he was dangerous like this!)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "Get off of her!"
    play sound splash03
    show casper casual angry at left1plus behind arianna:
        yoffset 100
        pause 0.6
        easein_back 0.4 centre xoffset 8
    show mscmc casual_hairup surprised at left5:
        yoffset 100
        pause 0.7
        easein_back 0.4 left2
    show arianna siren angry at right6:
        xoffset 50 yoffset 40
        pause 0.1
        parallel:
            ease 0.4 xoffset -80
            centre xoffset 0
            pause 0.1
            easein_back 0.4 right2
        parallel:
            easeout_back 0.4 yoffset 300
            yoffset 140
            pause 0.1
            easein 0.3 yoffset 100
        parallel:
            linear 0.4 alpha 0.0
            pause 0.1
            linear 0.4 alpha 1.0
    "Arianna dives into the water and grabs Casper from the side and his knife drops."
    hide mscmc
    hide casper
    show arianna siren_cu angry_cu at arianna_cu:
        yoffset 0
    ai "What the hell are you doing?! You can't run away from this!"
    play sound big_splash
    show casper casual angry at left1 behind arianna:
        yoffset 100
        pause 0.1
        easein_back 0.4 xoffset 20
    show arianna siren angry at right1:
        yoffset 80
        pause 0.2
        easein_back 0.5 right3
    "I pull myself out of the water as Casper pushes Arianna off of him."
    hide arianna
    show casper casual_cu confused_cu at casper_cu:
        yoffset 0 xoffset 0
    cs "It's already happened! It doesn't matter anymore!"
    show casper casual confused at left2:
        yoffset 100
        pause 0.1
        easein_back 0.4 xoffset 90
        easein_back 0.4 xoffset 0
    show arianna siren angry at right3:
        yoffset 100
        pause 0.2
        easein_back 0.5 right1
    "Casper makes a desperate dive for his knife, but Arianna stops him with her tail."
    hide casper
    show arianna siren_cu angry_cu at arianna_cu:
        yoffset 0
    ai "It does matter!"
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Shit, they're fighting! What do I do? What do I do?)"
    hide mscmc

    play sound big_splash
    show casper casual angry at left5:
        yoffset 250 alpha 0.0 xoffset -80
        pause 0.2
        parallel:
            linear 0.4 alpha 1.0
            pause 0.2
            linear 0.3 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 130
            pause 0.1
            easeout_back 0.4 yoffset 250
        parallel:
            easein 0.4 xoffset 0
            pause 0.1
            easein 0.4 xoffset 80
    show arianna siren angry at left2:
        yoffset 200 alpha 0.0 xoffset -80
        pause 0.1
        parallel:
            linear 0.4 alpha 1.0
            pause 0.2
            linear 0.3 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 90
            pause 0.1
            easeout_back 0.4 yoffset 200
        parallel:
            easein 0.4 xoffset 0
            pause 0.1
            easein 0.4 xoffset 80
    pause 1.2
    show arianna at right3 behind casper:
        yoffset 200 alpha 0.0 xoffset -80
        pause 0.1
        parallel:
            linear 0.4 alpha 1.0
            pause 0.2
            linear 0.3 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 90
            pause 0.1
            easeout_back 0.4 yoffset 200
        parallel:
            easein 0.4 xoffset 0
            pause 0.1
            easein 0.4 xoffset 80
    show casper at right1:
        yoffset 250 alpha 0.0 xoffset -80
        pause 0.2
        parallel:
            linear 0.4 alpha 1.0
            pause 0.2
            linear 0.3 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 130
            pause 0.1
            easeout_back 0.4 yoffset 250
        parallel:
            easein 0.4 xoffset 0
            pause 0.1
            easein 0.4 xoffset 80
    pause 1.2
    "Arianna and casper go under the water and then surface again, water splashing from their tails."
    hide arianna
    hide casper
    "In the flurry of tails and hands, I can barely even tell what's going on."
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(My knife's in the bag!)"
    hide mscmc
    show casper casual confused at left1:
        yoffset 110 xoffset -80 alpha 0.0
        pause 0.5
        parallel:
            easein_back 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    show arianna siren sad at right1:
        transform_anchor True yoffset 200 alpha 0.0 rotate 0
        pause 0.1
        parallel:
            linear 0.4 alpha 1.0
            pause 0.2
            linear 0.3 alpha 0.0
        parallel:
            easein_back 0.4 yoffset 180
            pause 0.1
            rotate 5
            easein 0.4 xoffset 170
    pause 0.6
    "I scramble over to my backpack, but I freeze as Casper throws Arianna against the edge."
    hide arianna
    hide casper
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "Fear for her makes my heart stop."
    show mscmc angry_cu
    "(Don't hurt her, Casper!)"
    mcarianna "Arianna!"
    hide mscmc
    show white
    play sound "<to 6>audio/sfx/thunder_25689.mp3" fadeout 1
    pause 0.1
    hide white with dissolve
    "There's a loud crack and a flash of blinding white light."
    "I raise my hand over my eyes, squinting."
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(Huh? What was that? It was almost like lightning or something.)"
    hide mscmc
    show casper casual confused at centre:
        yoffset 100
        pause 0.1
        easein_back 0.4 left1
    show arianna siren surprised at right2:
        yoffset 100
    "When it fades, Casper pulls away from Arianna in confusion."
    show arianna angry:
        parallel:
            easein 0.4 xoffset 100
        parallel:
            linear 0.4 alpha 0.0
    pause 0.4
    show arianna at left2 behind casper:
        xoffset -100
        pause 0.1
        parallel:
            easein_back 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    show casper:
        pause 0.3
        easein_back 0.4 right1
    "But Arianna uses that to grab Casper from behind and pin him against the edge of the pool."
    hide arianna
    hide casper
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(Whatever that was...it saved Arianna. We can't let this opportunity slip by!)"
    mcarianna sad_cu "Casper, you can't change the past."
    show arianna siren basic at left5:
        yoffset 100
    show casper casual basic at left1:
        yoffset 110
    show mscmc casual_hairup sad at right4
    "At my voice, Casper's struggle against Arianna weakens and he looks up at me."
    mcarianna "You can't change what you've done or what happened to your family."
    mcarianna "But that doesn't mean you have to be controlled by the past."
    hide arianna
    hide casper
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(I know there's sense in him. He can do the right thing.)"
    show arianna siren basic at left5:
        yoffset 100
    show casper casual basic at left1:
        yoffset 110
    show mscmc casual_hairup sad at right4
    mcarianna "You can try to pave a better future. A better version of the world and of yourself."
    show arianna angry
    "With her tail keeping him pinned, Arianna reaches for the bag and pulls out the rope."
    show arianna basic
    "He doesn't even try to resist as she ties his hands and ties the other end around a pointed rock."
    show casper sleep
    "Casper drops his head and begins muttering to himself."
    hide arianna
    hide casper
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(He completely gave up. I dont think he really wanted to hurt either of us.)"
    hide mscmc
    show arianna siren_cu sad_cu at arianna_cu
    ai "Did he hurt you?"
    show mscmc casual_hairup sad at right4 behind arianna
    show arianna siren sad at left3:
        yoffset 100
        pause 0.1
        easein 0.5 centre
    "Arianna swims in front of me. Her chest heaving with heavy, tired breaths."
    hide mscmc
    show arianna siren_cu sad_cu at arianna_cu:
        yoffset 0
    "She cups my face in her hands and I watch as water drips from her hair."
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(If Arianna hadn't won, would Casper let us go?)"
    "(I don't want to think about that.)"
    show mscmc casual_hairup smile at right1
    show arianna siren sad at left1:
        yoffset 150 xoffset 30
    mcarianna "No, I'm alright...thanks to you. Looks like you saved me."
    show arianna smile
    "Arianna smiles and I feel a sense of calm."
    ai grin "I won't let anything happen to you—no matter what it takes, I'll always save you."
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Has she always been my knight in shining armor?)"
    show mscmc casual_hairup smile at right1
    show arianna siren grin at left1:
        yoffset 150 xoffset 30
    "I put my hands over hers."
    show arianna smile
    mcarianna sad "Are {i}you{/i} okay? That didn't look like an easy fight."
    show mscmc smile
    ai surprised "I'm fine now that you're safe, but..."
    show mscmc basic
    ai "What was that bright light?"
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(It happened right when Arianna was losing, but she wouldn't know if it was magic, right?)"
    hide mscmc
    "The water in the pool begins to ripple."

    stop music fadeout 0.5
    play music mscmaxime fadein 1.0
    show maxime mermaid basic at centre:
        yoffset 250 alpha 0.0
        pause 0.1
        parallel:
            easein_back 0.4 yoffset 100
        parallel:
            linear 0.4 alpha 1.0
    "Maxime surfaces, water runs down the front of his face and drips into the water."
    hide maxime
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Even after everything with Casper, we've still been found by the government.)"
    "(Is this it?)"
    "My heart sinks."
    hide mscmc
    show maxime mermaid sad at left5:
        yoffset 80 xoffset 20
    show casper casual basic at centre:
        yoffset 160 xoffset 20
    show arianna siren sad at right4:
        yoffset 130 xoffset 20
    mx "I've been looking for you, Casper and Arianna. There's a warrant out for your arrest."
    "Casper doesn't even look up."
    hide maxime
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Will Maxime even listen to us if we try to explain what happened?)"
    hide mscmc
    show maxime mermaid sad at left3:
        yoffset 80
    show arianna siren sad at right3:
        yoffset 130
    "Arianna meets my eyes with a sigh before she looks at Maxime."
    ai "Has my grandma been arrested?"
    mx "No."
    hide maxime
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(At least Queenie is safe for the time being, but I can't let Arianna get arrested.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e11c1:
        "A. Try to appeal to Maxime.":
            $ menuhideborder = False
            show maxime mermaid sad at left3:
                yoffset 130
            show mscmc casual_hairup sad at right3
            mcarianna "Maxime, we're friends, right? You don't have to do this."
            mx "This is my job, [genericfn]. I can't walk away."
            mx "Sorry."
        "B. Explain what happened.":
            $ menuhideborder = False
            show maxime mermaid sad at left3:
                yoffset 130
            show mscmc casual_hairup sad at right3
            mcarianna "I know what it looks like, but the resistance isn't dangerous."
            mcarianna "That threat wasn't a collective decision and it's not serious."
            mx "It doesn't matter. I have my orders."
        "C. Hold your tongue.":
            $ menuhideborder = False
            show maxime mermaid sad at left3:
                yoffset 130
            show mscmc casual_hairup sad at right3
            "I open my mouth to say something but then stop myself."
            hide maxime
            show mscmc casual_hairup_cu sad_cu at mscmc_cu
            "(I don't want to make it worse.)"
            "(What could I even say to get us out of this?)"

    hide mscmc
    show maxime mermaid_cu sad_cu at maxime_cu:
        yoffset 0
    "Maxime sighs and starts to speak, but then he hesitates."
    hide maxime
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(He looks like he's sympathetic, but I don't feel hopeful.)"
    hide mscmc
    show maxime mermaid_cu sad_cu at maxime_cu
    mx "I believe in what the resistance is fighting for, but..."
    mx "I can't let you all leave."
    hide maxime
    show casper casual_cu basic_cu at casper_cu
    "Casper raises his head and his eyes meet mine."
    cs confused_cu "I don't want to be like this anymore."
    show casper casual basic at centre:
        yoffset 110
    "All eyes fall on him and he holds his chin up."
    hide casper
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(Did I get through to him when he was fighting Arianna?)"
    show casper casual confused at left3:
        yoffset 156
    show mscmc casual_hairup basic at right5
    show arianna siren basic at right2:
        yoffset 120
    cs "I shouldn't have done that—I betrayed your trust in me."
    cs "When I joined the resistance, I was overwhelmed with excitement."
    cs "I felt like I couldn't contain myself and that you guys weren't doing enough."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(He was fired up the moment he said he'd join.)"
    show casper casual basic at left3:
        yoffset 156
    show mscmc casual_hairup sad at right5
    show arianna siren angry at right2:
        yoffset 120
    "Arianna crosses her arms and I put a hand on her shoulder."
    ai "You weren't listening to us."
    cs confused "I know."
    hide arianna
    hide mscmc
    show maxime mermaid sad at left3:
        yoffset 76
    show casper basic at right3
    cs "Maxime, I was the one who made that threat and I signed Arianna and Queenie's names."
    hide casper
    show maxime basic
    show arianna siren basic at right2:
        yoffset 110
    "Maxime glances at Arianna."
    mx surprised "You weren't involved?"
    ai "No."
    hide maxime
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Please, Maxime. Let Arianna go.)"
    show casper casual confused at left3:
        yoffset 156
    show mscmc casual_hairup basic at right5
    show arianna siren basic at right2:
        yoffset 120
    cs "I just get so wrapped up in my emotions and I jump from one side to the other."
    cs "It's such an intense feeling to follow what I think is right."
    mcarianna surprised "You can still follow what you think is right, but, uh, just..."
    show mscmc sad
    "I rub my fingers over my throat, trying to forget the way his knife felt."
    mcarianna "Just not at the expense of others."
    show arianna sad
    "Arianna meets my eyes and places a tender hand over mine."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu smile_cu at mscmc_cu
    "(This is the second time now that my life has been on the line, but Arianna always manages to make me feel better.)"
    show casper casual angry at left3:
        yoffset 156
    show mscmc casual_hairup basic at right5
    show arianna siren basic at right2:
        yoffset 120
    cs "I was really mad at you and Arianna. And then when Arianna blamed me..."
    cs confused "I didn't want to hurt you, [genericfn]. I don't know what came over me."
    show arianna angry
    "Arianna's shoulder tenses under my hand and her fingers tighten around my palm."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(It does make me feel better hearing him say that, but it was still terrifying.)"
    show casper casual confused at left3:
        yoffset 156
    show mscmc casual_hairup basic at right5
    show arianna siren basic at right2:
        yoffset 120
    cs "Sometimes, I don't even know who I am, but...I know who I don't want to be."
    "Casper's voice dips and he looks down at the water."

    hide casper
    hide arianna
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e11c2:
        "A. That's a good step.":
            $ menuhideborder = False
            show casper casual confused at left3:
                yoffset 156
            show mscmc casual_hairup smile at right5
            show arianna siren basic at right2:
                yoffset 120
            mcarianna "Recognizing that is a good step in the right direction."
            mcarianna "It's not always easy."
            show mscmc sad
            cs confused "I'm scared of what could've happened to you if Arianna didn't stop me."
        "B. It's not too late to change.":
            $ menuhideborder = False
            show casper casual basic at left3:
                yoffset 156
            show mscmc casual_hairup smile at right5
            show arianna siren basic at right2:
                yoffset 120
            mcarianna "It's not too late to change, Casper."
            mcarianna "In the future, you can still make the impacts that you want to."
            cs "I really do want to help people."

        "C. Think of your family.":
            $ menuhideborder = False
            show casper casual basic at left3:
                yoffset 156
            show mscmc casual_hairup sad at right5
            show arianna siren basic at right2:
                yoffset 120
            mcarianna "Think of your family. Your uncle."
            mcarianna "I don't think he would want to see you go down this path."
            cs confused "No...he would be disappointed in me."

    show mscmc basic
    cs confused "I want to do what's right for everyone this time."
    show arianna angry
    "Arianna raises an eyebrow at him, her face still stern."
    ai "Do you really mean that?"
    cs "I do."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(I wish that things hadn't ended up this way, but at least Casper's willing to change.)"
    show casper casual basic at left3:
        yoffset 156
    show mscmc casual_hairup basic at right5
    show arianna siren angry at right2:
        yoffset 120
    ai "Then you know what you need to do."
    hide arianna
    hide mscmc
    show maxime mermaid basic at left3 behind casper:
        yoffset 76
    show casper at right2
    "Casper nods and looks to Maxime, a newfound resolve in his eyes."
    cs confused "Maxime, arrest me. Please. Tell your bosses that I'm the leader of the resistance."
    cs "They'll think you've dealt a huge blow to the resistance, so hopefully they'll back off."
    hide maxime
    hide casper
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(If the government believes that, there's still hope for the resistance.)"
    hide mscmc
    show maxime mermaid surprised at left3:
        yoffset 76
    show casper casual basic at right2:
        yoffset 156
    mx "Are you sure?"
    cs confused "Is there another way?"
    mx sad "No. I suppose not."
    show maxime angry
    show casper basic
    "Maxime straightens his shoulders and there's a strong air of business around him."
    mx "Casper, you're under arrest for heading the resistance and threatening the government."
    show maxime basic:
        easein 0.4 left1
    "Maxime undoes the makeshift rope tie and handcuffs Casper."
    hide maxime
    hide casper
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(Maxime wants to do his job, but he also wants to help us where he can and I appreciate that.)"
    "(We'd be totally screwed if he weren't a good guy.)"
    show mscmc casual_hairup basic at right1
    show arianna siren smile at left1:
        yoffset 140 xoffset 30
    ai "Thank you, Maxime."
    show arianna sad
    "Arianna's shoulders drop and she looks completely spent."
    hide mscmc
    hide arianna
    show maxime mermaid basic at left1:
        yoffset 50
    show casper casual basic at right2:
        yoffset 100
    mx "This should be enough to get the government off of the resistance for now."
    mx sad "But I recommend staying quiet for a while."
    show maxime:
        parallel:
            easein 0.4 xoffset -80
        parallel:
            linear 0.4 alpha 0.0
    show casper:
        parallel:
            easein 0.4 xoffset -130
        parallel:
            linear 0.4 alpha 0.0
    "Maxime takes hold of Casper and pulls him away from the edge."
    hide maxime
    hide casper
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Casper made a serious threat to the government...who knows how long he'll be imprisoned?)"
    show maxime mermaid basic at left4:
        yoffset 76 xoffset -10
    show casper casual basic at left1:
        yoffset 130 xoffset 30
    show mscmc casual_hairup basic at right5
    "Casper hesitantly looks at me, his head slightly bowed."
    cs confused "I'm sorry...I never really wanted to hurt you."
    cs "I can't help anyone the way I am now, but one day, I hope that I can."
    "The regret in his voice is clear."
    hide maxime
    hide casper
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Putting him down won't help him. What matters is that he wants to change and move forward.)"
    show maxime mermaid basic at left4:
        yoffset 76 xoffset -10
    show casper casual basic at left1:
        yoffset 130 xoffset 30
    show mscmc casual_hairup smile at right5
    mcarianna "It's alright, Casper. Maybe we'll see each other again someday."
    cs smile "I hope so"
    show casper:
        parallel:
            linear 0.4 yoffset 250 knot 0 knot 250
        parallel:
            easein 0.4 xoffset -80
        parallel:
            linear 0.4 alpha 0.0
    show maxime:
        pause 0.1
        parallel:
            linear 0.4 yoffset 250 knot 0 knot 250
        parallel:
            easein 0.4 xoffset -80
        parallel:
            linear 0.4 alpha 0.0
    "Maxime and Casper disappear under the water."

    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    scene bg msc_labeach_night at bg with fade
    "When we get back to the beach, everything feels quiet and peaceful."
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(Everything happened so fast and now it's just over and...we're okay.)"
    show mscmc casual_hairup basic at centre:
        yoffset 84 xoffset -40
    show arianna dress sad at centre behind mscmc:
        yoffset 50 xoffset 80
        pause 0.1
        parallel:
            easein 0.4 xoffset 38
        parallel:
            easein_back 0.4  yoffset 0
    "Arianna wraps her arms around my shoulders and hugs me from behind."
    show mscmc smile
    "I relax into her arms, relief like none other flowing over."
    ai "That was...insane. I can't believe Maxime let us go and that Casper actually turned himself in."
    ai smile "But at least we're alright. How are you feeling?"
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu:
        yoffset 0 xoffset 0
    "I'm more than alright as I feel her warmth against my back and her voice in my ear."
    "(Every time she holds me in her arms, I feel more comfort than words can describe.)"
    "(Safe and at home.)"
    show mscmc casual_hairup surprised at centre:
        yoffset 84 xoffset -40
    show arianna dress basic at centre behind mscmc:
        xoffset 38
    mcarianna "I'm kind of at a loss for words."
    show mscmc embarrassed
    "Her arms around me are firm and secure and it's as though I fet perfectly in them."
    show mscmc smile
    ai grin "Me too. It felt like the end of the world this morning."
    mcarianna grin "Somehow, we made it."
    hide arianna
    hide mscmc
    "I turn around in her arms so that we can face each other and she smiles."
    show arianna dress_cu smile_cu at arianna_cu
    "The stars reflect in her eyes and I feel the best kind of butterflies in my stomach."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(It's not just her touch that makes me feel at home. It's her smile and her eyes too.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "We always manage to make it out, don't we?"
    hide arianna
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    mcarianna "Don't make it sound like it's easy."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna laces her fingers with mine."
    ai grin_cu "The resistance will live to fight another day. It's not over."
    ai "And the government doesn't have my grandma which is such a relief."
    hide arianna
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    "(As long as Queenie isn't in prison, I'm happy. Hopefully that means she did see the news.)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    ai "We still don't know where she is, but I'm sure she's fine."
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    mcarianna "Queenie is always so welcoming and nice to me."
    mcarianna grin_cu "I'm glad she's okay."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna smiles widely."
    ai "I'm sure she would be very happy to hear that."
    hide arianna
    "Arianna leans into my ear and her breath makes my skin burn."
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "Can I tell you a secret?"
    ai grin_cu "I think you're amazing."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(Pfft. She's so cute.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna laughs and steps back so that she can see my face."
    hide arianna
    show mscmc casual_hairup_cu grin_cu at mscmc_cu
    mcarianna "You're the one who just saved me from a knife to the throat."
    mcarianna "I think {i}you're{/i} amazing."
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    "I push her shoulder lightly and she catches my hand."
    ai grin_cu "What if we're both amazing?"
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(If it were possible for my eyes to turn into hearts, they would.)"
    mcarianna grin_cu "Hmmm... I think I can live with that."
    show mscmc casual_hairup smile at left1
    show arianna dress smile at right1 behind mscmc
    "Still with my hand in hers, Arianna pulls us down onto the sand where we can finally collapse."
    hide mscmc
    hide arianna
    "We look up at the night sky, feeling each other's touch and listening to the waves."
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(I could fall asleep here in her arms.)"
    show mscmc casual_hairup grin at left1
    show arianna dress smile at right1 behind mscmc
    mcarianna "We should probably head home."
    ai grin "Yeah, probably."
    show mscmc smile
    show arianna smile
    "Neither of us move."
    ai sad "Actually, I don't really want to go anywhere."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna looks over at me and her eyes take my breath away."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(I'll never get tired of seeing her.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Everything has been so insane...I just want one moment here. With you."
    "Her voice gets gentler as her lips slowly quirk up."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(She finally looks relaxed. Truly at peace now that everything is behind us.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Look at the stars with me for a little bit?"

    hide arianna
    $ menuhideborder = True
    menu ariannas2e11c3:
        "A. Stargaze with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            mcarianna "Okay."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "A smile spreads on her face and she faces the sky again."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(I wish that every moment between us could be like this.)"
            show mscmc grin_cu
            "(No more bad guys and stress, just...being together.)"
            show mscmc casual_hairup smile at left1
            show arianna dress grin at right1 behind mscmc
            ai "Look."
            "Arianna points up at the sky."
            ai "That's the Great King!"
            mcarianna grin "Ursa Major?"
            ai "If I meant Ursa Major, I would've said Ursa Major."
            "Arianna lets her hand drop down and we laugh."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "(I guess mer people would have different names for the stars.)"
            show mscmc casual_hairup grin at left1
            show arianna dress grin at right1 behind mscmc
            ai "Ursa Major? That's what humans call it?"
            mcarianna "Yeah, it means like Great Bear or something. Because it looks like a bear."
            show mscmc smile
            show arianna smile
            "Arianna shifts her head so she could look at it from a different angle."
            ai grin "There aren't a lot of mer people who come up to look at the stars."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "(I wonder what it was like for Arianna to see the stars for the first time.)"
            show mscmc embarrassed_cu
            "(Wish I could've seen her reaction.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile at right1 behind mscmc
            mcarianna "Can you see them well under the water?"
            show mscmc smile
            ai sad "Not really and most mer people don't want to come up at night to look."
            ai grin "We do have the stars mapped out though. A long time ago, they were used for navigating."
            "Arianna glances over at me and her silver eyes are practically glowing in the moonlight."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(It's almost like there's little stars in her eyes.)"
            show mscmc casual_hairup smile at left1
            show arianna dress grin at right1 behind mscmc
            ai "They're not used for that anymore, but I do still like hearing stories about the stars."
            mcarianna grin "Tell me something then. Why do you call it the Great King?"
            show mscmc smile
            ai "Back before there were stars, there was a god of the sea, called the Great King."
            ai "He made the moon to create tides and then the stars to guide his people."
            "Arianna traces her fingers through the air, following the constellation."
            ai "He always wanted to be able to watch over his people, so he turned himself into a part of the sky."
            hide arianna
            show mscmc casual_hairup_cu smile_cu at mscmc_cu
            "(I don't know why, but I never thought mermaids would have myths or creation stories like that.)"
            show mscmc grin_cu
            "(I'm sure my human version would sound just as outlandish.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile at right1 behind mscmc
            mcarianna "Do you think it's real?"
            ai grin "It could be, but who knows? Maybe they're really just stars."
            mcarianna "It'd be cool if it's real."
            show mscmc embarrassed
            "Arianna brushes a speck of sand away from my cheek and then throws her arm over my chest."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "(Great King, if you're listening, please watch over Arianna and I. Help me to always protect her.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile at right1
            mcarianna "Do you guys know about zodiac signs?"
            ai surprised "What's that?"
            mcarianna "Based on when you were born, you fall into a certain zodiac."
            mcarianna "It's like, the alignment of the moon and planets when you were born."
            show arianna grin:
                parallel:
                    easein_back 0.5 yoffset 50
                parallel:
                    easein 0.5 xoffset -75
            "I put my arm out for Arianna to rest her head on and she does so happily."
            hide arianna
            show mscmc casual_hairup_cu grin_cu at mscmc_cu
            "(Astrology and zodiac signs sound like something that would be right up Arianna's alley.)"
            show mscmc casual_hairup grin at left1
            show arianna dress smile at right1:
                yoffset 50 xoffset -75
            mcarianna "You can use zodiacs to, like, predict behavior and fortunes and stuff."
            mcarianna "Trina knows way more about it than I do."
            show arianna grin
            "Arianna's face lights up."
            ai "That's so cool! What's my zodiac?"
            mcarianna "Well, your birthday's June 17th so you're a Gemini."
            ai "Is that good?"
            hide arianna
            show mscmc casual_hairup_cu smile_cu at mscmc_cu
            "(Gemini is all about duality. Arianna's very multifaceted.)"
            show mscmc casual_hairup grin at left1
            show arianna dress grin at right1:
                yoffset 50 xoffset -75
            mcarianna "We can look up your daily horoscope when we get home."
            mcarianna "That's like...your fortune for the day."
            ai "You can get one for every single day?"
            mcarianna "Yeah, crazy, right? But, it's more of a, 'take what resonates with you' thing."
            mcarianna "It's just cool to be self-reflective and learn how people behave differently from one another sometimes."
            show arianna smile
            "Arianna makes a hum of thought and looks up at the sky."
            hide arianna
            show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
            "(I'm glad everything worked out today. If it hadn't, we wouldn't be here like this.)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Her limbs unfold as she stands and takes my hand, silently—"
            show mscmc casual_hairup smile at left1 behind arianna
            show arianna dress smile at right1
            "Walking me towards the edge of the water, looking back at me with something in her eye I haven't seen before."
            mcarianna grin "You know I'll follow you anywhere, but where are you taking me?"
            ai embarrassed "Thanks for staying out with me. I needed this."
            hide arianna
            hide mscmc
            "Arianna sits right at the edge of the water as small waves break around her and drags me down to sit opposite her."
            show arianna dress_cu smile_cu at arianna_cu
            ai "The ocean should be part of this."
            hide arianna
            show mscmc casual_hairup_cu surprised_cu at mscmc_cu
            mcarianna "Part of what?"
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu:
                transform_anchor True
                pause 0.2
                linear 0.5 zoom 1.1 yoffset -20
            "Arianna leans in close to me, and I instinctively do the same."
            "I notice how the waves crashing around us are soaking her billowy dress, making it cling to her body."

        "B. Let's go home.":
            $ menuhideborder = False
            show arianna dress basic at right1
            show mscmc casual_hairup sad at left1
            mcarianna "I don't think we should stay out for too long. We should try to get some rest."
            ai sad "Yeah, you're probably right..."
            show mscmc surprised
            show arianna smile
            "Arianna gives me a wicked grin and I can't help it, my heart speeds up as she shines in the night before me."
            ai grin "But just...before we go back, follow me."
            hide mscmc
            hide arianna
            "Her fingers wind their way through mine as she leads me towards the water's edge..."
            "She turns back beckoning now and then to fix me with her gaze."
            show arianna dress_cu embarrassed_cu at arianna_cu
            "She pulls me down into the break of the small but ambitious waves..."
            "And holds onto my hands as we stare at each other, the moon blessing us from above."

    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(I want to kiss her...I know we said we wouldn't...)"
    hide mscmc
    "Arianna pulls me close, I'm practically in her lap but she doesn't pull away or giggle."
    "I relax into her body, warm and solid, but with a certain softness to some parts."
    show arianna dress_cu embarrassed_cu at arianna_cu
    "She looks at me like she's lost in a desert and I'm an oasis."
    "Her big, luminous eyes flick down to my lips as she tilts her head ever so slightly on her lithe neck..."
    "...And we regard each other anew in the waves."
    hide arianna
    show mscmc casual_hairup_cu embarrassed_cu at mscmc_cu
    "(She wants me.)"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
