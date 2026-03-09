label lexi_season1_episode6:

    $tbc = False
    scene bg msc_museum_displays_night at bg, red_tint with dissolve
    play music mscsuspense2

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show lexi casual_cu angry_cu at lexi_cu, red_tint
    "The museum alarm blares as I look over at Lexi whose jaw is clenched, eyes scanning the area."

    "She relaxes a little as the initial shock of the alarm wears off, but her grip on my hand is strong."
    hide lexi
    show mscmc jacket_hairup_cu sleep_cu at mscmc_cu, red_tint
    "(I need to be ready for whatever Lexi says we have to do next. I just need to stay focused.)"
    hide mscmc
    show lexi casual angry at left3, red_tint
    show hannah casual sad at right3, red_tint
    lx "Hannah, did you seriously set off the alarm?"
    show lexi casual basic at left3, red_tint
    "Lexi can't help but let a disbelieving little laugh slip out from between her pursed lips as she tries to suppress it."
    show lexi casual smile at left3, red_tint
    show hannah casual angry at right3, red_tint
    lx "And you are still try to blame me for getting caught last time? Classic Hannah."

    "Hannah's jaw clenches and her eyes narrow into a murderous glare, but she doesn't have time to respond to Lexi's jab."
    hide lexi
    hide hannah
    "We all turn as we hear at least three guards approaching from the far entrance to the exhibit hall."
    show lexi casual bigsmile at left3, red_tint
    show hannah casual angry at right3, red_tint
    lx "It seems like we've got company. Try not to get caught this time, Hannah."
    hide lexi
    hide hannah
    show hannah casual_cu angry_cu at hannah_cu, red_tint
    "I glance at Hannah one last time as Lexi pulls me past her."

    "Hannah's eyes dart back and forth around the room and as we run by she turns to run in the opposite direction."
    scene bg msc_museum_displays_night at bg with wiperight

    "Lexi pulls me behind her as we rush out of the hall into some unlit, roped off section of the museum."

    "There are several dark rooms on either side of the hall and at the end is a double door that leads directly outside."
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(We can probably escape if we go for the exit, but maybe it would be better to hide...)"
    hide mscmc
    $menuhideborder = True
    menu lexis1e6c1:
        "A. Rush for the exit.":
            $menuhideborder = False
            show mscmc jacket_hairup surprised at left1 behind lexi
            show lexi casual basic at right1
            mclexi "The exit is right there!"
            hide lexi
            hide mscmc
            "I pull away from Lexi and sprint to the metal double doors at the end of the hall."
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(This was too easy!)"
            hide mscmc
            show mscmc jacket_hairup surprised at centre
            "My heart pounds as I run, and I can feel adrenaline course through my veins as I get to the doors and slam into the metal bar to open them."

            "To my surprise, the doors don’t budge."
            hide mscmc
            "I feel Lexi frantically grab my hand and pull me into a dark side room, just as multiple footsteps clatter down the hall we’d just run down."

            "We crouch down behind a stack of cardboard boxes and wait when suddenly the overhead lights flick on."

        "B. Hide in a side room.":
            $menuhideborder = False
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Our best bet is to hide in one of these rooms.)"
            hide mscmc
            "I feel a rush of excitement as I pull Lexi behind me and into one of the dark side rooms."

            "The only light shining into the room is a small bit of pale moonlight coming in from a window on the far wall."

            "The room itself is filled with various exhibits, all covered in white sheets."
            show mscmc jacket_hairup_cu angry_cu at mscmc_cu
            "(Now we just need to stay hidden behind one of these and wait for the guards to-.)"
            scene bg msc_museum_displays_day at bg
            "I blink rapidly as the lights of the room suddenly come on..."

        "C. Leave it up to Lexi.":
            $menuhideborder = False
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(I have no idea what we're supposed to do! Lexi is the pro!)"
            hide mscmc
            show mscmc jacket_hairup angry at left1 behind lexi
            show lexi casual angry at right1
            mclexi "What do we do?!"

            "My heart pounds as I furrow my brows and look at Lexi desperately for an answer."

            lx "This way!"
            show mscmc jacket_hairup angry at out_right
            show lexi casual angry at out_right
            "Lexi pulls me by the hand to one of the dark side rooms."
            hide mscmc
            hide lexi
            "I can barely see as she guides me with deliberate, calculated steps through the room."

            "Around us are dozens of crates and pieces of torn down scaffolding, but none of these obstacles hinder Lexi's movements."
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(She knows exactly where she's going. It's like she had this route planned already.)"
            show mscmc jacket_hairup_cu smile_cu
            "(If this is how break ins are with her, I could get used to this.)"
            scene bg msc_museum_displays_day at bg with dissolve

            "Suddenly, the sound of several pounding footsteps echo in the hallway we came from..."

            "And Lexi jerks me behind a statue as the room's lights flick on."
    scene bg msc_museum_displays_day at bg
    "I peek from our hiding spot to look for the guards and I see three of them standing in the entrance to the room we're in."

    $sidecharone = "Chunky Buzzcut Guard"
    $sidechartwo = "Ripped Bald Guard"
    $sidecharthree = "Old Mustached Guard"

    sid1 "Did you see anyone?"

    sid2 "I thought I saw someone dart into this room. What about you?"

    sid3 "We'll have to check all the rooms anyways, so if you think you saw someone, we might as well start here."
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu
    "(Crap! The only exit is that window over there, but if they come in here they'll definitely see us run for it.)"
    hide mscmc
    "The guards don't say anything as they slowly prowl into the room and I duck back behind my hiding spot."
    show lexi casual_cu smile_cu at lexi_cu
    "My stomach flips as I hear the guards getting closer, Lexi gives my hand a confident squeeze."
    hide lexi
    show mscmc jacket_hairup_cu smile_cu at mscmc_cu
    "(Her self-assured expression is focused and calm...)"

    "(And her grip around my hand really makes me feel like she's always going to be there for me.)"
    show mscmc jacket_hairup_cu surprised_cu
    "(Will she?)"
    show mscmc jacket_hairup_cu angry_cu
    mclexi "What now? They know where we are!"

    "I hiss the words through tight lips as quietly as I can, doing everything I can to control my flight instinct."
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    "Lexi's eyes flit around the room and I start to bounce up and down anxiously."

    lx "Okay, I'm going to make a distraction, then we're gonna climb out that window over there."
    show lexi casual_cu smile_cu
    "She pulls a small metal ball from her pocket and holds it up to me with a sly grin."
    hide lexi
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(That'll be a perfect distraction! I thought she was just winging this break in, but she came prepared.)"
    hide mscmc
    show lexi casual angry at left1:
        easein 0.4 xoffset 600
    "Without a word, Lexi whips her hand out from our hiding spot and hurls the metal projectile past the guards and into the room across the hall."
    hide lexi
    sid2 "Over in that room!"

    "The ripped bald guard sprints out of the room with the other two guards in tow, giving Lexi and I the window of opportunity we needed."
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(If we had some dramatic music playing this would be really cool! Like one of those heist movies.)"
    hide mscmc
    show mscmc jacket_hairup angry at right3, out_left
    show lexi casual angry at right2, out_left
    "We sprint across the room, keeping as low and quiet as possible."
    hide mscmc
    hide lexi
    show mscmc jacket_hairup angry at left_in, left1 behind lexi
    show lexi casual angry at left_in, right1
    "When we get to the window Lexi tries to open it..."

    "But it's stuck!"
    show mscmc jacket_hairup surprised
    lx "It's stuck tight. Give me a second..."
    show lexi casual angry:
        easein 0.4 xoffset 200
    "Lexi's toned arms flex tightly as she pushes on the stubborn window. But after struggling until her face is bright red, she gives up."
    show mscmc jacket_hairup angry
    mclexi "Let me help."

    "I scoot as close as I can to Lexi, until we're practically standing on top of one another."

    "I can feel Lexi's firm bicep flex against mine as we push up on the window together."
    show mscmc jacket_hairup angry:
        easein 0.4 xoffset 150
    "The window creaks loudly as it finally starts to give way before finally slamming open and throwing me off balance."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu
    "(There's no way the guards didn't hear that. We need to leave, NOW!)"
    show mscmc jacket_hairup angry at left3
    show lexi casual angry at centre
    "A cold sweat breaks out over me and I can feel myself getting overwhelmed by the adrenaline and anxiety mixing together."

    "Behind us I can hear the guards yelling at one another from across the hall as the alarm echoes through the museum."
    show lexi casual smile
    lx "You first."
    #rain for all outside scenes in this episode
    scene bg msc_siren_park_night at bg
    show mscmc jacket_hairup angry at centre, step_in
    "I quickly crawl through the window and drop down into the dark street."
    hide mscmc
    show lexi casual angry at centre, step_in
    "Lexi follows quickly after me and just as we turn to run I hear one of the guards bang on the window, yelling for us to stop."
    stop music fadeout 1.0
    play music mscmctheme
    hide lexi
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(We made it! Now we just need to get out of here before the cops come and we'll be home free!)"

    "I grin broadly as I bask in the success of our daring escape."

    "(They were so close to catching us! If Lexi hadn't come prepared with that distraction...)"
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    "I fight back the urge to giggle as the excitement in my chest builds and I look to see Lexi beaming with pride at me."

    "She grabs my hand and starts sprinting away with me in tow as a light rain falls around us."
    hide lexi
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(My heart feels like it's about to explode!)"

    "(It's like that nervous rush when I'm not sure if I'm going to wipe out on a wave.)"

    "I can't stop smiling as we race away from the museum and I replay every moment of our escape in my head."

    "(Lexi was right when she said this was going to be fun! I can't believe she does this kind of thing all the time!)"
    scene bg msc_lastreet_night at bg with wiperight
    "We don't stop running until we're blocks away from the museum and completely soaked through by the now-heavy rain."
    show mscmc jacket_hairdown grin at left1
    show lexi casual bigsmile at right1 behind mscmc
    "Lexi still holds my hand in hers."

    "She finally slows to a stop and I follow her lead, as she changes her grip on my hand to intertwine her fingers with mine."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I'm out of breath, we almost just caught breaking and entering, and all I can think about is her hand in mine.)"
    show mscmc jacket_hairdown grin at left1
    show lexi casual bigsmile at right1 behind mscmc
    mclexi "That... was... crazy!?"

    "I place my hands on my thighs as I catch my breath and I look up at Lexi."

    "Lexi's clothes cling to her body, accentuating the curve where her hips meet her waist."

    "Strands of wet green hair cling to the parts of her exposed chest that peek out from the neck line of her shirt."
    show mscmc jacket_hairdown embarrassed
    "My throat tightens with excitement as my eyes travel down her body."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's breathtaking. I wish I could feel her pressed against me.)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed at left1
    show lexi casual smile at right1 behind mscmc
    lx "Almost getting caught is half the fun of the job."
    show mscmc jacket_hairdown surprised
    show lexi casual bigsmile
    "I look up at her, my eyes wide with shock, at her comment, but her smile tells me that she's kidding, or probably kidding anyway."
    show bg msc_alley_night at bg
    stop music fadeout 1.0
    play music mscromance
    show mscmc jacket_hairdown embarrassed
    "She makes for a nearby alleyway and holds her hand out for me to follow suit."

    "I take her hand and she gently pulls me into the narrow street, barely lit by the light of a nearby streetlamp."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(There's something urgent in her touch but when I look at her she's fully focused on me and I feel a delighted shiver run through me.)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Her grip on me tightens and my breath catches in my chest as she slowly, so achingly slowly, closes the distance between us."
    hide lexi
    "Our lips brush softly for just a second before everything we've been holding back is unleashed as our mouths crash against each other."

    "Her kiss is wild and burns with passion. She is warm against me as the run soaks us and we cling to each other."

    "Lexi wraps her hand around the back of my neck, pulling me into her."

    "My body trembles from exhaustion and excitement and all I want is more of Lexi. I want all of her..."
    show lexi casual_cu bigsmile_cu at lexi_cu
    "...but she pauses, snatching away her lips with a teasing grin."

    "Then her smile softens and she presses her forehead against mine as we breath each other in."

    lx "I've wanted to kiss you like this since I saw you at the tidepools for the first time again."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Really?"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "She nods, rubbing her nose gently against mine."

    lx "You've been on my mind non-stop for the past six months..."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mclexi "I had no idea..."
    show mscmc jacket_hairdown_cu sad_cu
    mclexi "When you said you didn't come back because of me, I thought it meant you didn't miss me."
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    lx "Of course I did."

    "Lexi smiles as if I said something ridiculous..."
    scene bg msc_lexi_s1_mini1 at bg with dissolve
    "Then leans her head closer to mine as her hand finds its way back to my waist and swiftly pulls me flush against her."

    lx "Do you want me to keep showing you how much I've missed you?"

    $menuhideborder = True
    menu lexis1e6c2:
        "A. Show me how much you missed me!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            scene bg msc_alley_night at bg with dissolve
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mclexi "Yes."
            #weird diagonal parallel zoom thing that i don't think I can pull
            scene bg msc_lexi_s1_ei2 at bg with dissolve:

                yanchor 0.4
                parallel:
                    linear 8 xanchor 0.1
                parallel:
                    linear 8 yanchor 0.1
                parallel:
                    linear 8 zoom 0.7
            "In a blur, Lexi spins us, then pushes me up against the hard alley wall..."

            "Her body against mine as one of her arms rests on the wall by my head."

            "(Everything feels like it’s been leading to this moment between us. I need her right now.)"

            "She leans in, then stops just millimeters from my lips..."

            "And we look at each other from hooded eyes as the palpable tension between us grows."

            "(I want her to devour me.)"

            "Rain falls all around us as she looks deeply into my eyes, as if she’s looking for treasure there."

            "Her wet red lips part as she keeps me pinned and suspended in glorious longing."

            lx "Good girl."

            "(The words make my knees want to buckle but Lexi’s pressing me so tightly against the wall that she’s holding me up.)"
            scene bg msc_alley_night at bg with dissolve
            "Lexi presses her lush lips against mine and I lose myself to the velvet touch of her embrace."

            "Each kiss from her is stronger than the last and her hand runs down my body, hooking onto my waistline."

            "My senses start to overwhelm me, giving me a high that I only ever get on the ocean."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(More. Touch me more. I need your touch, Lexi.)"
            hide mscmc
            "My body quivers as I kiss Lexi, and I dig my fingers lightly into her back to let her know I missed her just as much."

            "Her wet hair sticks to her face as I hold her cheeks in my palms, the warmth of her staves off the chill of the night rain."

            "Lexi takes my hand from her cheek and kisses my palm as she stares deep into my eyes."

            "I feel my chest stutter as I try to breathe for the first time seemingly since I said yes to her."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(The feeling of her lips on my skin, the way each kiss sends a jolt of electricity through my body... it’s overwhelming but so amazing.)"
            hide mscmc
            "Lexi presses her soft lips to my collarbone and grazes me lightly with her teeth, as she presses her hips into mine."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "I let out an involuntary soft gasp."
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            "I feel her grin into the crease of my neck."
            hide lexi
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Oh, she liked that.)"
            hide mscmc
            "I run my hands down the sides of Lexi’s body, feeling the toned muscles of her torso underneath her wet clothes."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I never want to let her go. She feels so beautiful under my hands, so solid and wonderful.)"
            hide mscmc
            "I kiss her cheek and trail my lips down to hers where she greets me with eager kissing."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            mclexi "Why didn’t you kiss me sooner?"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "She sighs and pulls away to lean her forehead gently into my lips, and I kiss her softly when she does."

            lx "I didn’t want you to think I was using you... in any way."

            "My heart flutters as I look into her large green eyes and I stroke her hand gently with my finger."
            hide lexi
            "She inhales deeply as I kiss her neck, my lips barely touching her skin with each kiss."
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(This vulnerable side of her is so different from her normal laissez-faire attitude. It’s a special side of her only I get to see...)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "I look into Lexi’s eyes before kissing her hard."

            "An urge to be closer to her grips me and I wrap my arms around her in a strong embrace, pulling her even closer."
            hide lexi
            "Lexi doesn’t resist, but instead tilts her head to the side and runs her hands down my back to slip them into my back pockets."

            "I feel her hand squeeze me as I move my lips from her neck to her collarbone and giggle in delight as Lexi smirks down at me."

            "Then she bends her face down to mine and I eagerly welcome the dance of our mouths."

            "Her tongue presses against mine and I lose all sense of the rain or the alley around us."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(I wish we could live in this moment together forever.)"
            #lightning
            hide mscmc
            show mscmc jacket_hairdown surprised at left1 behind lexi
            show lexi casual surprised at right1
            "A bright flash of lightning splits the sky and my eyes shoot open of their own accord at the brightness."
            show lexi casual smile
            lx "Want to go someplace warm?"

            "I look at her and she has an expression on her face I haven’t seen before, it’s more… tender than the smiles I’ve seen on her before."
            show mscmc jacket_hairdown embarrassed
            "I bite my bottom lip and nod in anticipation."

            mclexi "My place?"
            show lexi casual bigsmile
            "Lexi grins and takes my hand in hers in a tight grip."
            hide lexi
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            lx "Your place sounds perfect."

        "B. Hesitate.":
            $menuhideborder = False
            scene bg msc_alley_night at bg with dissolve
            show mscmc jacket_hairdown surprised at left1 behind lexi
            show lexi casual smile at right1
            mclexi "That... I..."
            show lexi casual bigsmile at right1:
                easein 0.4 xoffset 100
            "I fumble my words as I try to come up with an appropriate response, but Lexi just smiles and takes a step back."

            lx "Sorry. I didn't mean to spring something so heavy on you all of a sudden."
            show mscmc jacket_hairdown smile
            "She chuckles to herself and wipes some water from her face with a grin."

            lx "Besides, we should get inside. It's pouring."

            "As she finishes speaking, a flash of lightning illuminates the sky, followed by a rumble of thunder."
            show mscmc jacket_hairdown grin
            mclexi "Let's head back to my place."
    scene bg msc_boardwalk_night_lights at bg with wiperight
    show mscmc jacket_hairdown smile at left1
    show lexi casual smile at right1 behind mscmc
    "As we walk to my place along the boardwalk the rain keeps beating down on us."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Tonight has been amazing but I could use getting out of these wet clothes.)"
    hide mscmc
    show mscmc jacket_hairdown smile at left1
    show lexi casual smile at right1 behind mscmc
    "Lexi stands next to me, holding my hand."
    show lexi casual bigsmile
    "Her soaked clothes cling to her athletic body and she grins at me with a cocked eyebrow as she catches me staring."
    show mscmc jacket_hairdown embarrassed
    lx "See something you like?"

    "She giggles playful at me as my cheeks flush and I take my keys out to unlock the apartment door."
    #no rain inside of the apartment
    show bg msc_mchomeentryway_lightsoff at bg with wiperight
    show mscmc jacket_hairdown basic
    "I put the key in the lock, but to my surprise, it's already unlocked."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I must have forgotten to lock it.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left1
    show lexi casual surprised at right1 behind mscmc
    "I open the door but as I do I realize there's someone inside waiting in the dark hall."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is it a burglar?)"

    $sidecharone = "Dark Figure"
    stop music fadeout 1.0
    play music msctense
    hide mscmc
    show mscmc jacket_hairdown surprised at left1
    show lexi casual angry at right1 behind mscmc
    sid1 "I've been waiting for you two to get here..."
    hide lexi
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    "At the sound of Hannah's voice coming from the person in the dark, Lexi blows past me and grabs Hannah."
    show lexi casual angry at left1
    show hannah casual angry at right1 behind lexi
    lx "You don't come here."

    "Lexi's guttural tone shakes me to my core."
    #animation of lexi kicking Hannah out
    show hannah casual angry at right1, out_right
    "Lexi brings her other hand up to also hold onto Hannah and shoves her back out the door into the street."
    hide hannah
    hide lexi
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Damn, does Lexi know how to fight? That was a pretty effective move.)"
    scene bg msc_boardwalk_night_lights_people at bg with wiperight
    show lexi casual angry at left3
    show hannah casual angry at right3
    "Lexi stalks up to Hannah who is still recovering her balance out in the street."

    lx "Don't you ever. EVER. Come to [genericfn]'s apartment. I will mess you up."
    show hannah casual sad
    "Hannah looks a little shaken from the quick turn of events but she recovers enough to glare at Lexi with hatred."
    show hannah casual angry
    hj "So aggressive! I didn't think you'd be so protective over [genericfn] seeing as she's been lying to you."
    hide lexi
    hide hannah
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Jesus, what the hell is Hannah on about now?)"
    hide mscmc
    show lexi casual basic at left3
    show hannah casual angry at right3
    "Lexi's face becomes a smooth neutral mask as she looks at Hannah..."

    lx "The fact that you can be this annoying is truly mind-blowing, Hannah."

    "Hannah wipes rain from her face with her hand before pushing her tousled bangs back."

    hj "You think you're so great, Lexi. But [genericfn] came to talk to me this morning. I bet she didn't tell you that, did she?"
    hide hannah
    hide lexi
    show lexi casual_cu surprised_cu at lexi_cu
    "Lexi glances at me unsure of how to respond to Hannah."
    hide lexi
    show lexi casual basic at left3
    show hannah casual angry at right3
    hj "She came to the museum the other day to talk to me, about you. And she didn't tell you, did she?"

    "A sick feeling wells up in my chest at Hannah's words and Lexi looks at me, her face never wavering from the calm mask she put in place."
    hide lexi
    hide hannah
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Hannah's trying to mess with everyone's head!)"
    hide mscmc
    show lexi casual sad at right3
    show mscmc jacket_hairdown sad at left3
    mclexi "Lexi..."
    hide lexi
    hide mscmc
    $menuhideborder = True
    menu lexis1e6c3:
        "A. I can easily explain.":
            $menuhideborder = False
            show lexi casual sad at right3
            show mscmc jacket_hairdown sad at left3
            mclexi "...it’s not like that! I went there to try and get her to leave you alone."
            show lexi casual basic
            "Lexi’s eyes narrow."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(She’ll believe me... right?)"
            hide mscmc
            show lexi casual sad at right3
            show mscmc jacket_hairdown angry at left3
            lx "That..."
            show lexi casual smile
            lx "That sounds just like you."
            hide mscmc
            hide lexi
            show lexi casual_cu bigsmile_cu at lexi_cu
            "Lexi gives me a confident grin before turning her attention back at Hannah, who is caught off guard that her tactic didn’t work."

        "B. She's trying to turn us against each other":
            $menuhideborder = False
            show lexi casual angry at right3
            show mscmc jacket_hairdown angry at left3
            mclexi "...she's just trying to turn us against each other!"
            show lexi casual bigsmile
            "Lexi grins and nods subtly to me."

            lx "I know she is. Even if she's telling the truth, I know you wouldn't have done it without a good reason."
            hide lexi
            show mscmc jacket_hairdown grin
            show hannah casual angry at right3
            "My heart jumps a little at Lexi's trusting words and I smile smugly at Hannah, who is glowering at me in contempt. "

        "C. Say nothing.":
            $menuhideborder = False
            show lexi casual sad at right3
            show mscmc jacket_hairdown angry at left3
            mclexi "Lexi, I..."

            "My tongue feels dry and sticks to the roof of my mouth as I try to come up with the right words to say."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Hannah isn’t lying. I did go talk to her and kept it from Lexi.)"

            "(I was trying to help, but would Lexi believe me if I said that?)"
            hide mscmc
            show lexi casual sad at right3
            show mscmc jacket_hairdown angry at left3
            "My shoulders sag as I look down at the wet ground and I rub the bridge of my nose with my fingers."
            hide mscmc
            hide lexi
            show lexi casual_cu smile_cu at lexi_cu
            lx "Hey."
            show lexi casual_cu basic_cu
            "I look up to find Lexi smiling gently at me."
            show lexi casual_cu smile_cu
            "She gently brushes the back of my hand with her fingers and looks at me with warm eyes."

            lx "I’m sure you had your reasons. You don’t need to explain."
    hide lexi
    hide hannah
    hide mscmc
    show hannah casual angry at centre
    hj "You're both so stupid!"
    hide hannah
    "Lexi wraps her arm around me."
    #lightning flash
    "Thunder cracks in the distance as the two square off and a chill runs down my spine."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(The way she's facing off with Hannah in this storm is so dramatic.)"

    "(It feels like they could start fighting at any moment!)"
    hide mscmc
    show hannah casual sad at centre
    "Hannah says something but I can't hear what."

    "Her words are barely audible over the rainfall, but her sudden vacant expression triggers alarms in my head."
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu  at mscmc_cu
    "(Something's wrong. Normally she would be yelling at Lexi. Why is she so quiet all of a sudden?)"
    hide mscmc
    show lexi casual angry at left3
    show hannah casual sad at right3
    hj "It's fine. But since [genericfn] is your girl now, don't think I'm just coming after you anymore, Lexi."
    hide lexi
    hide hannah
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(This does not seem like a good thing.)"
    hide mscmc
    show lexi casual angry at left3
    show hannah casual angry at right3
    hj "I saw the orb react to you two in the museum. Now that I know it's magical, there's no chance in hell I'm letting you two have it."

    hj "A mer artifact is worth a small fortune, but a magical mer artifact? That will set me up for life."

    hj "I'm going to be the one to steal it and if you two get in my way... I'll make sure you live to regret it."
    hide lexi
    hide hannah
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi steps back under the awning and wraps her arm around my waist, pulling me to her."

    lx "Big talk for someone who's never been able to back it up. Bring it on. You'll never beat us to it."
    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
