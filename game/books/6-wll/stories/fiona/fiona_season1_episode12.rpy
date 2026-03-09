label fiona_season1_episode12:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_ward_hq_lights_off at bg
    play music wllsadsong1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show fiona cloak sad at right1
    show wllmc coat surprised at left1
    "Fiona's words hit me with unexpected force."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Why was she so scared to ask for a hug?)"
    hide wllmc
    show fiona cloak sad at right1
    show wllmc coat sad at left1
    "But I reach out and take her into my arms, and she clings to me as tightly as she can."
    show wllmc coat smirk
    mcfiona "Everything's gonna be okay. There isn't a ghost in the whole wide world that can stand against the two of us."
    "She nods, but her grip is still death-tight, and a seed of uncertainty plants itself in my heart."
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(I've never seen Fiona fearful of the future before. She lives in it, swims through it every day.)"
    show wllmc coat_cu surprised_cu
    "(So what's different this time?)"
    hide wllmc
    show fiona cloak_cu smile_cu at fiona_cu
    "But Fiona doesn't say anything else. She just holds onto me, and when she lets me go, her face is its usual serene mask."

    scene bg_wll_town_streets_day at bg with fade
    stop music fadeout 1.0
    play music wlleverydayupbeat1 fadein 1.0
    "We meet the next morning outside the boarding house."
    show wllmc coat_hat_cu angry_cu at wllmc_cu
    "(Today's the day. Make or break.)"
    hide wllmc
    show wllmc coat_hat smallsmile at left3
    show fiona cloak smile at right3
    mb "Okay, let's go over everything one more time."
    show fiona cloak sad
    "I give Fiona an amused look out of the corner of my eyes, and she looks vaguely guilty."
    mb "Humor me."
    show wllmc coat_hat smirk
    mcfiona "I know what's going to happen. We go into the town hall, put on the show of our lives, and Diana is overcome with wonder and gratitude."
    show wllmc coat_hat grin
    mcfiona "'Oh wow,' she says, 'you two are the greatest acting talent I've ever seen, here's my wedding ring.' Bing bang boom, we're done."
    show fiona cloak smirk
    mb "Now who's the psychic?"
    show wllmc coat_hat smallsmile
    show fiona cloak pout
    mb "But look, getting the wedding ring isn't the difficult part. It's what comes next."
    show wllmc coat_hat angry
    show fiona cloak angry
    mb "The ghost is going to be waiting, and as soon as we take it, she'll strike."
    mcfiona "So we have to be fast."
    mb "Exactly. If we don't bind her in time, she could do real, serious damage. The whole town could be at risk."
    show wllmc coat_hat smirk
    mcfiona "But we won't let that happen."
    mcfiona "We'll lay her to rest, and then you and I will get our {i}well-earned reward{/i}."
    show fiona cloak sad
    mb "Mmm."
    "The fact that Fiona doesn't rise to my bait tells me something is really wrong."
    hide fiona
    hide wllmc
    show wllmc coat_hat_cu surprised_cu at wllmc_cu
    "(She's still afraid. But why?)"
    show bg_wll_town_streets_day behind wllmc as pulse_effect:
        align(0.5, 0.5) transform_anchor True alpha 0.2
        linear 0.8 zoom 2.0 alpha 0.0
    pause 1.0
    hide pulse_effect
    hide wllmc
    show wllmc coat_hat surprised at left3
    show fiona cloak surprised at right3
    "An impulse flashes through my mind, and as usual, I follow it."
    show wllmc coat_hat angry
    mcfiona "Quick, in here."
    hide wllmc
    hide fiona
    "I pull Fiona into the nearest alley."
    show fiona cloak surprised at right1
    show wllmc coat_hat angry at left1
    mcfiona "I need you to kiss me. Right now."
    hide wllmc
    hide fiona
    show fiona cloak_cu sleep_cu at fiona_cu
    "Fiona looks startled, but she doesn't ask questions. She just reaches up and presses her lips to mine."
    hide fiona
    show wllmc coat_hat_cu embarrassed_cu at wllmc_cu
    "(Mmm, feels good.)"
    hide wllmc
    show fiona cloak surprised at right1
    show wllmc coat_hat grin at left1
    "I let myself enjoy the kiss as fully as I can, and when I pull back, Fiona looks a little dazed."
    show wllmc coat_hat smile
    mb "What was that for?"
    show wllmc coat_hat sad
    mcfiona "I had a vision of the future where I didn't kiss you, and it was very bad."
    mb "Why? What happened?"
    show wllmc coat_hat smirk
    mcfiona "I didn't get a kiss."
    show fiona cloak grin
    "Fiona laughs."
    show wllmc coat_hat smallsmile
    mcfiona "Look, I can tell you're worried about today. What's got you so bent out of shape?"
    show fiona cloak sad
    mb "It's... when I was looking at the future last night, I only saw one outcome."
    show wllmc coat_hat surprised
    mb "Everything goes perfectly. I get the ring, I do the spell, Diana asks to say goodbye, and the ghost gets cleansed."
    hide wllmc
    hide fiona

    $menuhideborder = True
    menu fionas1e12c1:
        "Sounds good to me.":
            $menuhideborder = False
            show fiona cloak sad at right1
            show wllmc coat_hat smirk at left1
            mcfiona "Sounds good to me. Nothing I like better than an easy job."
            mb "It's wrong. The future isn't like this. It makes me certain I'm missing something."
        "Was I in those visions?":
            $menuhideborder = False
            show fiona cloak sad at right1
            show wllmc coat_hat smirk at left1
            mcfiona "Was I in your visions at all?"
            show wllmc coat_hat surprised
            "Fiona shakes her head, and I know I've hit the mark."
            mb "Not one."
        "It seems too simple.":
            $menuhideborder = False
            show fiona cloak sad at right1
            show wllmc coat_hat smirk at left1
            mcfiona "That seems too simple."
            mb "Exactly my feelings. There's something I'm not seeing, and that's never a good thing."
    show wllmc coat_hat sad
    mcfiona "Sorry I'm making your job harder. At least you know I've got your back in the fight."
    show fiona cloak angry
    "Fiona's eyes darken as her gaze drops, the shadow turning gold to amber."
    mb "That's what I'm most worried about. If I can't see you, how can I protect you?"
    show wllmc coat_hat smirk
    mcfiona "Oh come on, you know me. I'm as tough as nails. Nothing's gonna get me."
    show fiona cloak pout
    mb "You promise?"
    show wllmc coat_hat grin
    mcfiona "I promise."
    hide fiona
    hide wllmc
    "She kisses me again, deeper and more passionately, and then presses her forehead to mine."
    show fiona cloak_cu angry_cu at fiona_cu
    mb "Okay then. Let's go give Sunmok the peace she deserves."

    scene bg_wll_town_hall_lights at bg
    show fiona warden grin at centre
    with wiperightdissolve
    stop music fadeout 1.0
    play music wlleverydayupbeat3 fadein 1.0
    "The performance goes according to Fiona's prediction, and the crowd is suitably wowed by Fiona's incredible sleight of hand."
    hide fiona
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(She makes it look so easy. Honestly, they'd be even more impressed if they knew what hard work she put in.)"
    hide wllmc

    stop music fadeout 1.0
    play music wllsomber1 fadein 1.0
    show diana casual smileglasses at centre
    "After the show, Diana basically drags us away from the crowd so she can gush, a huge, beaming smile on her face."
    show wllmc skirt smile at left3
    show diana casual smileglasses at right1plus
    fc "Oh, I'm so glad I asked you to perform! What a delight, seeing 'The Theft of a Moonlit Heart performed by people in love!"
    hide diana
    hide wllmc
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(Um, excuse you?)"
    hide wllmc
    show wllmc skirt basic at left3
    show diana casual smileglasses at right1plus
    fc "Sunny and I actually put on a very similar performance back when we were courting. Sunny was always interested in amateur theatrics."
    hide wllmc
    show fiona warden smile at left3
    mb "I'm really glad you enjoyed it, Diana."
    fc "There were so many little details to appreciate!"
    fc "The way your body language mirrored each other, the way you reacted so instinctively to each other..."
    hide diana
    hide fiona
    show fiona warden_cu sad_cu at fiona_cu
    "Fiona's eyes meet mine, and not for the first time, I see my own expression mirrored there."
    hide fiona
    show wllmc skirt_cu sad_cu at wllmc_cu
    "(It's the agonizing feeling of having to agree with something that's not true for the sake of a job.)"
    hide wllmc
    show fiona warden smile at left3
    show diana casual smileglasses at right1plus
    fc "You know, I've seen some great actors in my time."
    fc "I even once saw Kean perform Macbeth. But even immense talent isn't a substitute for real feeling."
    hide fiona
    hide diana
    show wllmc skirt_cu sad_cu at wllmc_cu
    "(I don't know where she's getting this stuff from. I guess she's just projecting what she and Sunny had onto us.)"
    show wllmc skirt_cu basic_cu
    "(Yeah, that must be it.)"
    hide wllmc
    show fiona warden sad at left3
    show diana casual smileglasses at right1plus
    "I can tell Fiona is about as uncomfortable with what Diana said as I am, but she keeps the conversation going."
    mb "I'm sad I never got to meet Sunmok. She seems like she was a really fascinating person."
    show diana casual sadglasses
    fc "Yes, she was truly remarkable. She made my world brighter just by being there."
    show fiona warden surprised
    "Fiona's gaze drifts to me for a moment, and then she jerks it back to Diana and keeps talking."
    show fiona warden smile
    mb "I know some memorial rites from Guryeo that my family practices. If you want, I'd be happy to perform one with you for Sunny."
    hide fiona
    hide diana
    show wllmc skirt_cu smile_cu at wllmc_cu
    "(That's the thing about Fiona that's really remarkable. Even when she's running a job, she still cares about people.)"
    hide wllmc
    show fiona warden smile at left3
    show diana casual smileglasses at right1plus
    fc "I would truly appreciate that."
    show diana casual sadglasses
    "Her hand brushes her wedding ring, turning it around her finger."
    fc "I know that letting Sunny be at peace is the right thing to do, but I don't know how to say goodbye."
    show fiona warden sad
    fc "When she died, I was out of my mind with grief. Desperate for some way, any way, to see her again."
    fc "Back then, if you'd told me she was a ghost, I would have been thrilled."
    hide fiona
    hide diana

    $menuhideborder = True
    menu fionas1e12c2:
        "She wouldn't want this.":
            $menuhideborder = False
            show wllmc skirt sad at left3
            show diana casual sadglasses at right1plus
            mcfiona "I don't think Sunny would want to be a ghost, from the way you're describing her."
            mcfiona "I know I wouldn't. It seems like a pretty raw deal, all things considered."
        "You don't have to say goodbye.":
            $menuhideborder = False
            show wllmc skirt sad at left3
            show diana casual sadglasses at right1plus
            mcfiona "You know, you don't have to say goodbye if you're not ready. Sunny was your wife, I can't blame you for holding on."
            mcfiona "But you can remember her without having a menacing angry ghost around."
        "It's not really her.":
            $menuhideborder = False
            show wllmc skirt sad at left3
            show diana casual sadglasses at right1plus
            mcfiona "If it makes you feel better, that ghost isn't really Sunny. Not in any meaningful way."
            mcfiona "I've met it a few times, and it's nothing like the person you're describing."

    show diana casual smileglasses
    "Diana smiles wanly."
    fc "Thank you for trying to comfort me. But I don't need it. This isn't about what I want."
    show wllmc skirt smallsmile
    fc "It's about what Sunny would want, and what's best for the town."
    hide wllmc
    show diana casual basicglasses at centre
    "And with that, she pulls her ring off her finger and drops it into Fiona's hand."
    hide diana
    show wllmc skirt basic at left3
    show fiona warden basic at right2
    mb "[genericfn], salt."
    show wllmc skirt smallsmile
    mcfiona "On it."
    hide wllmc
    hide fiona
    "I pull the pouch of salt from my hip and start drawing a thick line of it in a circle around Fiona."
    show wllmc skirt smallsmile at left3
    show fiona warden surprised at right2
    mb "Where's my chalk?"
    show wllmc skirt smile
    show fiona warden basic
    mcfiona "Take mine."

    scene white
    pause 0.1
    scene bg_wll_town_hall_lights_off at bg
    show wllmc skirt surprised at left3
    show fiona warden angry at right2
    with dissolve
    stop music fadeout 1.0
    play music wllsuspense1 fadein 1.0
    "I toss it to her, and as I do, the lights begin to flicker."
    mcfiona "She's coming!"
    show wllmc skirt angry
    "I finish the salt circle and pull out my revolver, checking the barrel to see the six silver-coated bullets."
    hide fiona
    hide wllmc
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(Sascha said these ones were blessed, too. He wouldn't even touch them.)"
    hide wllmc
    play sound "audio/sfx/gunshot_2.mp3"
    stop music fadeout 1.0
    play music wllaction1 fadein 1.0
    show sunmok ghost veryangry at centre:
        alpha 0.5 transform_anchor True zoom 0.9
        linear 1.0 zoom 1.0 alpha 1.0
    "The ghost lunges out of nowhere at Fiona and I fire a shot directly through her."
    hide sunmok
    show wllmc skirt angry at left3
    show fiona warden angry at right2
    mb "Good! Keep her attention."
    mcfiona "Do you think shooting her again will work?"
    mb "Yes. If you aim for her heart."
    hide wllmc
    hide fiona
    show diana casual surprisedglasses at centre
    "Diana is watching everything with wide eyes, her hands pressed over her mouth."
    hide diana
    show wllmc skirt angry at left3
    show fiona warden angry at right2
    mcfiona "Okay, got it."
    hide wllmc
    hide fiona
    play sound "audio/sfx/gunshot_2.mp3"
    show sunmok ghost veryangry at centre, shake
    "The ghost swoops in again, and I take my aim carefully and let off another shot. It works, and her cold, angry gaze focuses on me."
    hide sunmok
    show wllmc skirt_cu angry_cu at wllmc_cu
    "(Hey there, me again. The bane of your existence.)"
    hide wllmc
    show wllmc skirt angry at centre
    mcfiona "Enzo, now!"
    hide wllmc
    show wllmc skirt_cu angry_cu at wllmc_cu
    "(Last time we fought, I didn't have a familiar. We'll see how you like it now that things are a bit more even.)"
    hide wllmc
    show sunmok ghost veryangry at centre
    show enzo familiar angry at right2:
        yoffset -550
        easein 0.3 yoffset 0
    "Enzo swoops down out of the shadows, where he was hiding, and sprinkles a rain of salt over the ghost."
    show sunmok ghost veryangry at shake
    "She screams."
    hide sunmok
    show wllmc skirt grin behind enzo at centre
    show enzo:
        xoffset 450
    mcfiona "Good work, buddy!"
    show enzo:
        easein 0.4 xoffset 20
    enz "I got her good, Mistress, didn't I?"
    hide enzo
    hide wllmc
    show fiona warden angry at centre
    "I reach out with my mind and push the scattered salt crystals, linking up with the circle around Fiona and holding the ghost in stasis."
    mb "Okay. The purification ritual is ready to go."
    show fiona at left3
    show diana casual surprisedglasses at right2
    "She looks at Diana."
    mb "This is your last chance. If you want to say goodbye, it has to be now."
    hide fiona
    show diana casual sadglasses at centre
    "Diana nods. Wet lines on her cheeks gleam in green light the ghost is emitting."
    show diana at left3
    show sunmok ghost veryangry at right1plus behind diana
    fc "Oh Sunny, I'm sorry you're suffering like this. I wish I could see you again. The real you."
    fc "I miss you every day. I'll never forget you."
    show diana casual surprisedglasses
    show sunmok:
        pause 0.1
        ease 0.1 alpha 0.0
        ease 0.1 alpha 0.8
        repeat 3
        alpha 1.0
    "The ghost ripples, and then screams, and it's the most terrifying sound I've ever heard."
    hide diana
    hide sunmok
    show fiona warden angry at centre
    mb "No!"
    hide fiona
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(Why did she say that? Nothing's wrong.)"
    hide wllmc
    show sunmok ghost veryangry at centre
    "But the future comes crashing down on us."

    show bg_wll_town_hall_lights_off
    show sunmok at shake
    "As Fiona scrambles, the ghost screams again, and the brazier falls over, spilling glowing coals across the room."
    hide sunmok
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(Oh no.)"
    hide wllmc
    show fiona warden surprised at centre
    "Fiona scrambles to put the coals out with her cloak."
    hide fiona
    show sunmok ghost veryangry at right1
    show diana casual basicglasses at left4
    "As she does, the herbs needed for the purification ritual catch fire, and the ghost swoops at Diana."
    hide diana
    hide sunmok
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(What do I do?)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e12c3:
        "Help put out the fire.":
            $menuhideborder = False
            show wllmc skirt angry at centre
            "I drop to my knees beside Fiona and use the butt of my gun to push the coals back into their container."
            hide wllmc
            show wllmc skirt_cu surprised_cu at wllmc_cu
            "(The last thing we need is the floor turning to tinder.)"
            hide wllmc
        "Save the herbs!":
            $menuhideborder = False
            show wllmc skirt angry at centre
            "I grab the remaining herbs away from the fire."
            hide wllmc
            show wllmc skirt_cu surprised_cu at wllmc_cu
            "(It's not much, but it's better than nothing, right? Maybe we can still make this work.)"
            hide wllmc
        "Get Enzo to protect Diana.":
            $menuhideborder = False
            show wllmc skirt angry at centre
            mcfiona "Enzo, protect Diana!"
            hide wllmc
            show sunmok ghost veryangry at right1
            show diana casual basicglasses at left3
            show enzo familiar angry at centre:
                yoffset -550
                xoffset -600
                parallel:
                    easeout_circ 0.4 yoffset 0
                parallel:
                    linear 0.4 xoffset -50
            "My fearsome little familiar swoops down in front of Diana, but the ghost hardly notices him."
            show enzo:
                parallel:
                    easein_circ 0.4 yoffset -450
                parallel:
                    linear 0.4 xoffset 500 alpha 0.5
            "She bats him aside with one sweep of her arm."
            hide enzo

    show sunmok ghost basic at right1
    show diana casual basicglasses at left3
    "The ghost stops in front of Diana, but she doesn't attack. She reaches out to Diana."
    hide sunmok
    hide diana
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(Does she know who Diana is? Did she remember something?)"
    hide wllmc
    show sunmok ghost basic at right1
    show diana casual sadglasses at left3
    $sidecharone = "Ghost"
    sid1 "You... sad... why?"
    hide sunmok
    hide diana
    show wllmc skirt angry at centre
    mcfiona "Sunny, if you remember Diana, then do this for her! She doesn't want you to hurt anyone else."
    hide wllmc
    show sunmok ghost angry at centre
    "The ghost whips around to glare at me."
    show sunmok ghost veryangry
    sid1 "Sad!"
    hide sunmok
    show wllmc skirt angry at centre
    "It's so loud it's hardly a word, just a shriek that rips through me, raising a primal fear that destroys any thought in my head."
    hide wllmc
    show sunmok ghost veryangry at centre
    sid1 "You... power... key... unlocked..."
    hide sunmok
    show wllmc skirt sad at centre
    "There's an intense pressure in my head, and the thought of trying to lift my gun and point it at her feels like the hardest thing in the world."
    hide wllmc
    show sunmok ghost_cu sad_cu at sunmok_cu
    sid1 "Give me... power... save me!"
    hide sunmok
    show wllmc skirt surprised at centre
    "The revolver falls from my nerveless fingers."
    hide wllmc
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(No!)"
    hide wllmc
    show fiona warden sad at centre:
        yoffset 100
        pause 0.1
        easein 0.4 yoffset 0
    "Time seems to be moving treacle slow. I see Fiona scrambling to her feet."
    show fiona warden angry
    mb "[genericfn]! [genericfn] run!"
    hide fiona
    show wllmc skirt angry at centre
    "I want to. I really do. I can feel Enzo in my mind, trying to push me, trying to help me."
    hide wllmc
    show enzo familiar_cu angry_cu at enzo_cu
    enz "Don't give in, Mistress! You can fight this!"
    hide enzo
    show wllmc skirt_cu angry_cu at wllmc_cu
    "(He's right. I'm tougher than this.)"
    hide wllmc
    show sunmok ghost_cu veryangry_cu at sunmok_cu
    "The ghost is coming right at me, her face twisted and distorted with pure rage."
    hide sunmok
    show fiona warden_cu angry_purple_cu at fiona_cu
    "Fiona flings herself forward, her eyes glowing as her powers activate, and she tries to put herself between the ghost and me."

    scene fiona_s1_ei4:
        align(0.5, 0.0) transform_anchor True zoom 2.3 xoffset 1100 yoffset -170
        pause 1.0
        linear 5.0 xoffset -200 yoffset -300 zoom 1.7
    with fade
    pause
    "(Fiona, no!)"
    "I can't say it. It's taking everything I have just to stay conscious, just to stay me, as the ghost's rage and pain and sorrow fill my head."
    "(Fiona.)"
    window hide
    show fiona_s1_ei4:
        linear 4.0 zoom 0.85 xoffset 0 yoffset -50
    pause
    "It's all I have time to think. The ghost swoops through Fiona, making her cry out, and slides into my body."
    "(Fiona. Please be okay.)"
    "(Sorry I didn't keep our promise.)"

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
