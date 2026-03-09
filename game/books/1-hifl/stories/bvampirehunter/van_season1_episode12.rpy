label van_season1_episode12:

    $tbc = False
    scene bg bowling at bg
    play music mackenziehunt
    pause

    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show hiflmc bowling surprised at right4
    show vanessa casual basic at left4
    mcvan "I'm sorry, {i}what{/i}?"
    show vanessa casual sad
    va "They want you to come with me back to HQ."
    "Vanessa actually looks nervous, worrying at her lip."
    va "I think it's a good idea."
    "I want to say I'll go, just to wipe the unsure expression off her face but..."
    show hiflmc bowling basic
    mcvan "I trust you, Vanessa."
    show hiflmc bowling sad
    mcvan "But I just don't know about the rest of the order."
    mcvan "Aren't they really strict about not working with others?"
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Aren't they the ones who made sure that Vanessa lived her whole life isolated and alone?)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    va "Usually, yes. But they agree your protection is a top priority."
    va "And there is nowhere in the world safer from Vampires than Headquarters."
    hide hiflmc
    hide vanessa
    show vanessa casual_cu sad_cu at vanessa_cu
    "She looks into my eyes, full of sincerity."
    va "I just want to keep you safe."
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(How am I supposed to say no to that?)"
    hide hiflmc
    show hiflmc bowling sad at right4
    show vanessa casual sad at left4
    mcvan "I guess I'm just nervous."
    show vanessa casual smirk
    va "Don't worry, I'll be with you the whole time."
    show hiflmc bowling basic
    show vanessa casual basic
    va "I won't abandon you."
    show vanessa casual angry
    va "I promise."
    hide vanessa
    hide hiflmc
    show razi casual sad at centre
    stop music fadeout 1.0
    play music hiflgetitdone
    "Razi clears his throat awkwardly, breaking the moment."
    hide razi
    show hiflmc bowling blush at centre
    "I blush, realizing we've just had that whole conversation in front of everyone."
    hide hiflmc
    show jd casual basic at centre
    jd "Helsing HQ, huh?"
    show jd casual angry
    jd "Sounds kinda uptight, if you ask me."
    hide jd
    show razi casual basic at centre
    ra "Maybe, but Vanessa's not wrong."
    ra "They can offer [genericfn] the very best protection."
    hide razi
    show diego doctor glassesbasic at centre
    di "But at what cost?"
    di "What price have they attached to this protection?"
    show diego doctor glassesbasic at right4
    show vanessa casual angry at left4
    va "No price!"
    va "Protecting [genericfn] is of the utmost importance to the Order."
    va "Keeping humans safe from vampires is our mission."
    show diego doctor glassessad
    "Diego looks skeptical, but doesn't argue further."
    hide vanessa
    hide diego
    show mac cop basic at centre
    Sheriff "I think it's a good idea."
    show mac cop angry
    Sheriff "They can offer you proper protectiuon, and with you gone, Li and her thralls won't feel the need to hang around here."
    hide mac
    show razi casual sad at centre
    ra "Whatever you choose, please... be careful."
    hide razi
    show hiflmc bowling sad at centre
    "I take a deep breath and turn to Vanessa."
    show hiflmc bowling happy at right4
    show vanessa casual basic at left4
    mcvan "Alright, let's go check out this fancy HQ of yours."

    scene bg road_night at bg with clockwise_wipe
    show van_back_night at bg
    show van_middle_night at bg
    show van_front_night at bg
    show hiflmc casual basic at left4 behind van_front_night:
        ypos 725
    "I feel like I'm on autopilot as I pack my bags and we drive out of town."
    "Night falls in the blink of an eye, and we make a final stop at the gas station on the outskirts of Havenfall."
    show hiflmc casual surprised
    "(I can't believe I'm really leaving...)"
    show hiflmc casual sad
    "(I've always wanted to get out of Havenfall,)"
    show hiflmc casual sarcastic
    "(But I never really thought that being hunted by the Bride of Dracula would be the reason for it.)"
    show hiflmc casual sad
    "(I wonder what Grace would think of all of this...)"
    show hiflmc casual surprised
    mcvan "Oh my god, I didn't tell Grace I was leaving.)"
    "I pull out my phone, but we must be in a deadzone, because I've got no service."
    scene bg gas_station_night at bg with wiperight
    show hiflmc casual basic at right4
    show vanessa huntress hatbasic at left4
    "I leave the van and turn to Vanessa, who's filling up the tank."
    mcvan "I'm going to try and find somewhere with cell reception."
    mcvan "I want to call Grace and let her know I'm heading out of town."
    show vanessa huntress hatsad
    va "Alright, just don't wander too far."
    show hiflmc casual happy
    mcvan "I won't, I promise."
    scene bg road_night at bg with dissolve
    pause 0.5
    show hiflmc casual angry at centre
    "With a stake in one hand and my phone in the other, I walk down the road for several minutes, searching for reception."
    show hiflmc casual surprised
    "I finally get a couple of bars, and immediately dial Grace."
    scene bg phone_dorm_room at bg
    show grace casual_cu basic_cu at grace_cu

    gr "Hey, [genericfn], what's up?"
    hide grace
    show bg road_night at bg
    show hiflmc casual surprised at centre
    "It strikes me that I haven't talked to her since all this started."
    "Suddenly, I have no idea how to tell her I'm leaving."
    show hiflmc casual sad
    mcvan "It's been a few days since we've talked and I've missed you."
    show hiflmc casual basic
    mcvan "How's school?"
    show hiflmc casual happy
    mcvan "Are you making friends?"
    hide hiflmc
    show bg phone_dorm_room at bg
    show grace casual_cu happy_cu at grace_cu

    gr "School is fine, and I've actually-!"
    hide grace
    show bg road_night at bg
    show hiflmc casual sad at centre
    "The connection goes staticky, and I wander a little farther down the road until the connection is strong again."
    show hiflmc casual happy
    mcvan "Sorry, I couldn't quite hear that. But I'm glad things are going well!"
    hide hiflmc
    show bg phone_dorm_room at bg
    show grace casual_cu sad_cu at grace_cu

    gr "Okay..."
    "Her tone goes suspicious."
    show grace casual_cu basic_cu
    gr "Now, what's the real reason you called?"
    show grace casual_cu sad_cu
    gr "Your voice is doing that 'I've got a secret' thing."
    scene bg road_night at bg
    $menuhideborder = True
    menu vans1e12c1:
        "A. Deny it.":
            $menuhideborder = False
            show hiflmc casual surprised at centre
            mcvan "What? My voice doesn't do anything like that."
            hide hiflmc
            show bg phone_dorm_room at bg
            show grace casual_cu happy_cu at grace_cu

            "Grace laughs."
            gr "It totally does. Now spill."
        "B. 'Fess up.":
            $menuhideborder = False
            show hiflmc casual sad at centre
            "I let out a sigh."
            show hiflmc casual sarcastic
            "(Should've known Grace could sniff out a secret even from dozens of miles away.)"

        "C. Laugh nervously.":
            $menuhideborder = False
            show hiflmc casual happy at centre
            "I try to laugh it off, but even to me it sounds nervous."
            mcvan "Whaaat? Can't I just call to check in on my baby sister?"
            "Grace rolls her eyes exactly as I imagined she would."
            hide hiflmc
            show bg phone_dorm_room at bg
            show grace casual_cu basic_cu at grace_cu

            gr "Sure you can. But you didn't."
    scene bg road_night at bg
    show hiflmc casual basic at centre
    mcvan "Okay, fine."
    show hiflmc casual basic
    mcvan "The truth is, I'm heading out of town for a little while."
    hide hiflmc
    show bg phone_dorm_room at bg
    show grace casual_cu sad_cu at grace_cu

    gr "Like for how long?"
    hide grace
    show bg road_night at bg
    show hiflmc casual surprised at centre
    mcvan "I'm not sure yet. But everything's fine!"
    show hiflmc casual basic
    mcvan "Just keep focusing on school and making friends."
    show hiflmc casual sad
    mcvan "And please be careful. Safety first, at all times."
    mcvan "And don't invite strangers into your room."
    show hiflmc casual basic
    "(I may be laying it on a little thick, but I can't help it.)"
    show hiflmc casual sad
    "(The thought of Grace getting attacked at school has panic drawing at my throat.)"
    hide hiflmc
    show bg phone_dorm_room at bg
    show grace casual_cu happy_cu at grace_cu

    gr "Okay, weirdo."
    gr "I promise I'll be careful."
    hide grace
    show bg road_night at bg
    show hiflmc casual surprised at centre
    "I look around, realizing that I've wandered far enough away that I can't see Vanessa or the gas station anymore."
    show hiflmc casual basic
    mcvan "Hey, I gotta go. But I'll call you again soon."
    show hiflmc casual happy
    mcvan "I love you."
    hide hiflmc
    show bg phone_dorm_room at bg
    show grace casual_cu happy_cu at grace_cu

    gr "Love you too, sis."
    hide grace
    show bg road_night at bg
    show hiflmc casual basic at centre
    stop music fadeout 1.0
    play music hiflsuspense
    "I hang up and start walking back toward the gas station, clutching the stake tightly."
    show hiflmc casual sad
    "The night is preternatually still, quiet in a way that feels wrong."
    "(I don't know why, but something feels... off.)"
    show bg gas_station_night at bg with dissolve
    "I rush back as quickly as I can, expecting to find Vanessa waiting impatiently."
    "Instead the same eerie stillness permeates the gas station."
    hide hiflmc
    show vanessa huntress hatbasic at centre
    "Vanessa stands facing away from me, stiff as a board and unmoving."
    "The pump lies haphazardly on the ground at her side, a puddle of gas spreading at her feet."
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Oh no.)"
    hide hiflmc
    show hiflmc casual surprised at centre
    "I run faster, dashing towards Vanessa."
    hide hiflmc
    show vanessa huntress hatbasic at left4
    show li casual happy at right4
    "And then I spot Li, standing across from her, practically glowing with victory, a satisfied smirk on her lips."
    hide vanessa
    hide li
    show hiflmc casual basic at centre
    "I stop short, just out of Li's sight."
    hide hiflmc
    show vanessa huntress hatbasic at left4
    show li casual happy at right4
    sinli "You should have known better than to take me on by yourself, young Helsing."
    "She monologues with clear relish, her voice suffused with vindictive joy."
    show li casual basic
    sinli "There is nowhere you can take [genericln] where she will be safe."
    show li casual happy
    sinli "I will always be one step ahead."
    show li casual basic
    sinli "Do you see now how outmatched you are?"
    show vanessa huntress hatsad
    "As if on cue, Vanessa flinches."
    show li casual happy
    "Li laughs, taking obvious pleasure in Vanessa's suffering."
    sinli "I suppose not, trapped as you are inside of your worst memory."
    sinli "To make such a rookie mistake... what would your superiors think of you?"
    hide vanessa
    hide li
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Come on, I have a ton of weapons on me, I have to be able to do something!)"
    "(I have to save Vanessa!)"
    hide hiflmc
    $menuhideborder = True
    menu vans1e12c2:
        "A. Rescue Vanessa!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(What weapons do I have?!)"
            show hiflmc casual_cu angry_cu
            "(I need to keep her away long enough for me to get ot Vanessa and break her free of whatever illusion Li's trapped her in.)"
            hide hiflmc
            show hiflmc casual angry at centre
            "I search my pockets and find a couple of grenades, a stake, and a knife."
            show hiflmc casual happy
            mcvan "Yes!"
            "For a second, I feel a flare of hope."
            show hiflmc casual angry
            "(These grenades should do the trick.)"
            show hiflmc casual surprised
            "(I take back all the sarcastic comments I ever made about Vanessa's hoard of weapons.)"
            show hiflmc casual happy
            "(These things are {i}amazing{/i}.)"
            show hiflmc casual angry
            stop music fadeout 1.0
            play music hiflaction
            "I rush forward, pulling the pin on a flash grenade and throwing it."
            hide hiflmc
            show li casual angry at centre
            "I shield my eyes just in time, but Li's screech of outrage tells me that the grenade worked."
            sinli "You wretched girl!"
            show li casual angry at left4
            show hiflmc casual angry at right4
            "While she's blinded, I take the opportunity to throw a few rocks at her, from all different directions."
            hide li
            hide hiflmc
            show hiflmc casual_cu angry_cu at hiflmc_cu
            "(I just need to confuse her enough that she doesn't know exactly where I am.)"
            hide hiflmc
            show hiflmc casual angry at right4
            show li casual angry at left4
            sinli "You will regret this night, [genericln]!"
            mcvan "Not as much as you will!"
            "I punctuate my retort with a holy water grenade, which I chuck right at her feet."
            "It detonates, and she hisses in pain, the blessed water sizzling where it touches her skin."
            hide hiflmc
            hide li
            stop music fadeout 1.0
            play music hiflsad
            "She retreats into darkness for the moment to recoup."
            show hiflmc casual_cu angry_cu at hiflmc_cu
            "(That should take care of Li for now.)"
            hide hiflmc
            show hiflmc casual surprised at right2
            show vanessa huntress hatsad at left2
            "With Li recovering, there's nothing stopping me from running to Vanessa's side."
            mcvan "Vanessa, wake up!"
            mcvan "It's just an illusion--it's not real!"
            "She continues looking blankly into the distance, heartbreak written all across her features."
            show hiflmc casual angry at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            "I grab her shoulders and shake her."
            mcvan "Snap out of it, dammit!"
            show hiflmc casual sad
            "Still no reaction."
            show hiflmc casual angry
            mcvan "You can fight this, I believe in you!"
            mcvan "You're so strong. I know you can beat this if you just try."
            hide hiflmc
            hide vanessa
            show vanessa huntress_cu hatsad_cu at vanessa_cu
            "Vanessa's face twitches, and my heart leaps."
            va "Don't hurt them!"
            hide vanessa
            show hiflmc casual sad at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            "The hope sinks in my chest."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Okay, that didn't work.)"
            show hiflmc casual_cu basic_cu
            "(Maybe if I talk her through the vision?)"
            show hiflmc casual_cu surprised_cu
            "(Like with a lucid dream?)"
            hide hiflmc
            show hiflmc casual surprised at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            mcvan "Don't hurt who, Vanessa?"
            "But she doesn't respond."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(I guess not.)"
            show hiflmc casual_cu angry_cu
            "(Think, [genericfn].)"
            show hiflmc casual_cu basic_cu
            "(Razi said a strong emotional reaction should be able to break the illusion, right?)"
            hide hiflmc
            show hiflmc casual sad at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            mcvan "Vanessa, please, I need you!"
            show hiflmc casual surprised
            mcvan "You swore you would protect me. You promised not to abandon me!"
            show hiflmc casual sad
            mcvan "I thought Helsings were supposed to keep their word."
            show hiflmc casual angry
            mcvan "But how can you do that if you're stuck in some dumb illusion?"
            "There's no flicker of emotion, not even a miniscule change in her expression."
            show hiflmc casual basic
            mcvan "How about this?"
            show hiflmc casual angry
            mcvan "If you don't snap out of it, Li is going to take me and use me to resurrect Dracula..."
            mcvan "And then probably kill me when she's done."
            show hiflmc casual sarcastic
            mcvan "I'll be dead and Dracula will be alive--or undead again, whatever--and the Order will probably blame you."
            show hiflmc casual angry
            mcvan "How's {i}that{/i} for an emotional reaction?"
            show hiflmc casual basic
            "Nothing. Not even a blink."
            show hiflmc casual sad
            "Her thousand-yard stare into the darkness finally pushes me over the edge."
            hide hiflmc
            hide vanessa
            show vanessa_s1_mini11 at bg:
                zoom 0.4
            "I grab her face with both of my hands, cradling her jaw and directing her gaze at mine."
            "Look at me!"
            "I need you."
            "I can’t do this without you."
            "I’ve barely known you for a week and yet the thought of losing you hurts too much to think about!"
            "I care about you so much that seeing you like this..."
            "It hurts me too."
            "Did you hear that?!"
            "Seeing you suffering causes me pain too!"
            "And you don’t want to hurt me, right?"
            "So for me, please, fight back! Don’t let Li win!"
            hide vanessa_s1_mini11
            show hiflmc casual sad at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            "Like a floodgate lifting, all the thoughts and feelings I've kept bottled up come spilling out."
            "I look desperately into her eyes for any sign that this is working, but she just stares at me distantly, unseeing."
            show hiflmc casual angry
            mcvan "Fuck!"
            show hiflmc casual sad
            "I feel tears of frustation build up at the corner of my eyes, and reach up to wipe them away."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Why isn't anything working? What do I have to do to save her?)"
            "(Why can't I save her the way she's saved me over and over again?)"
            hide hiflmc
            show hiflmc casual sad at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            mcvan "Come on, Vanessa, I need you to tell me what to do here."
            mcvan "What can I do to wake you up?"
            hide vanessa
            hide hiflmc
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(I'm running out of time.)"
            "(It won't be long before Li is recovered enough to come at me again...)"
            show hiflmc casual_cu angry_cu
            "(And this time I won't be able to hold her off.)"

        "B. Hide behind the van.":
            $menuhideborder = False
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Then again, if even Vanessa got taken down, I stand no chance against Li.)"
            "(And anyway, she's after me.)"
            "(The best thing I can do right now is stay hidden and out of sight.)"
            hide hiflmc
            show hiflmc casual surprised at centre
            "I duck behind the van, heart hammering in my chest."
            "Scrambling to pull out my phone, I hope desperately that I have at least one or two bars.)"
            show hiflmc casual sad
            "Unfortunately, the gas station is just as much of a deadzone as it was earlier."
            "Still, I try calling Razi anyway."
            show hiflmc casual angry
            "(Come on, come on, someone, anyone-!)"
            show hiflmc casual sad
            "But no dice."
            "I can't reach Razi, or Sheriff Hunt, or any of the others."
            "Even my texts fail to send."
            "(Guess I'm really on my own here.)"
            show hiflmc casual basic
            "I peek out at Vanessa again."
            hide hiflmc
            show vanessa huntess hatsad at centre
            "She's still frozen, her face twisted in anguish."
            "My heart gives a painful lurch."
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(I don't know what Li is making her relive, but I've never seen her look like that before.)"
            "(Not even when she was physically injured.)"
            show hiflmc casual_cu sad_cu
            "(Seeing her hurting like this is killing me.)"
            "(I'd do anything to make it stop, to end that suffering for her.)"
            hide hiflmc
            show hiflmc casual basic at centre
            "What was it Razi had said, about ending the illusions...?"
            show hiflmc casual surprised
            "A strong emotional response?"
            show hiflmc casual angry
            "(I don't know if I can do that, but I can damn well try!)"
            "I feel inside my pockets and pull out one of the flash grenades Vanessa gave me."
            show hiflmc casual happy
            "(This should do nicely.)"
            show hiflmc casual basic
            "I take a deep breath, leaning back against the van."
            show hiflmc casual angry
            "(You can do this, [genericfn].)"
            "(You've escaped from her before. This is no different.)"
            show hiflmc casual sad
            "I ignore the part of myself that it is different, because Vanessa's not on her way to rescue me this time."
            show hiflmc casual angry
            "I don't have time for that kind of self-doubt right now."
            "Vanessa's life is on the line."
            show hiflmc casual angry at right4
            show li casual angry at left4
            "The next moment, I dart out from behind the van as quickly as possible, pulling the pin and chucking the grenade at Li."
            hide li
            show hiflmc casual angry at centre
            "I close my eyes as I turn to Vanessa, too busy trying not to get blinded myself to see if it worked on Li."
            hide hiflmc
            show vanessa huntress_cu hatsad_cu at vanessa_cu
            "Vanessa looks heartbroken as she stares, unseeing, into the night."
            "Her already pale face is nearly ashen in moonlight."
            hide vanessa
            show hiflmc casual angry at right1
            show vanessa huntress hatsad at left1 behind hiflmc
            mcvan "Come on, Vanessa, snap out of it!"
            show hiflmc casual surprised
            mcvan "Whatever you're seeing, it isn't real!"
            "I try getting in front of her face, waving a hand in front of her eyes."
            show hiflmc casual sad
            "Nothing seems to work."
            hide vanessa
            hide hiflmc
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(I don't know what to do or say to break her out of this.)"
            stop music fadeout 1.0
            play music hiflsad
    hide hiflmc
    hide vanessa
    show li casual angry at centre
    "Out of the corner of my eye, I see Li starting to approach."
    hide li
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(I'm out of time.)"
    "(What more can I do?)"
    show hiflmc casual_cu surprised_cu
    "And then it hits me."
    "One last ditch attempt."
    show hiflmc casual_cu sad_cu
    "(She'll forgive me for this if it saves both our lives, right?)"
    stop music fadeout 1.0
    play music hiflheavyromance
    scene vanessa4 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 8 yanchor 0.1
    "I put my hands on her neck and draw her in for a kiss."
    "The second our lips connect, all other thought is wiped from my head."
    "Her lips are softer than I could’ve imagined, and she’s so warm."
    "Every part of me feels extra sensitive and hyper-aware of what’s going on, but also distant, lost in the moment."
    "So lost in the moment, in fact, that I almost don’t notice when she starts kissing me back."
    "I open my eyes and see Vanessa looking back at me with full recognition, instead of that awful vacant stare."
    "With that comes the memory of why I kissed her in the first place, and I pull back, my lips still tingling."
    scene bg gas_station_night at bg with fade
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(...Wow.)"
    hide hiflmc
    show vanessa huntress_cu hatsurprised_cu at vanessa_cu
    "Vanessa looks stunned, raising a hand to her lips."
    show vanessa huntress_cu hatblush_cu
    va "Miracle romance..."
    "She speaks in a breathy whisper, so quiet I have to strain to hear her."
    "Still, the fact that she's talking at all is a massive relief."
    hide vanessa
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(All I want to do is spend the rest of the night kissing her, but we have bigger fish to fry.)"
    hide hiflmc
    show hiflmc casual happy at right1
    show vanessa huntress hatblush at left1 behind hiflmc
    mcvan "Welcome back."
    show vanessa huntress hathappy
    "Vanessa smiles at me, and I smile back reflexively, so wide my cheeks hurt."
    stop music fadeout 1.0
    play music hiflmaintheme
    "And then, of course, Li ruins it."
    hide hiflmc
    hide vanessa
    show li casual basic at centre
    sinli "How sweet."
    show li casual angry
    sinli "Sickeningly so."
    hide li
    show vanessa huntress hatangry at centre
    "Anger slams down on Vanessa's face, destroying the soft face she'd been wearing."
    show vanessa huntress hatangry at left3
    show li casual basic at right3
    va "You should have escaped while you still had the chance."
    hide li
    show hiflmc casual basic at right1
    show vanessa huntress hatblush at left1 behind hiflmc
    "I grab Vanessa's hand and she turns to look at me, warmth returning to her eyes."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e12c3:
        "A. Let's do this together.":
            $menuhideborder = False
            show hiflmc casual angry at right1
            show vanessa huntress hatblush at left1 behind hiflmc
            mcvan "Come on, let's do this together."
            show vanessa huntress angry
            va "We'll make sure she never hurts you or anyone else again."
        "B. Kick her ass.":
            $menuhideborder = False
            show hiflmc casual angry at right1
            show vanessa huntress hatblush at left1 behind hiflmc
            mcvan "Kick her ass, Vanessa."
            mcvan "Make her regret ever messing with us."
            show vanessa huntress hatsmirk
            "Vanessa grins almost ferally."
            mcvan "Oh, I will."
        "C. I believe in you.":
            $menuhideborder = False
            show hiflmc casual basic at right1
            show vanessa huntress hatblush at left1 behind hiflmc
            "I squeeze her hand."
            mcvan "You can do this, Vanessa. I believe in you."
            "Vanessa squeezes back."
            show vanessa huntress hatsmirk
            va "I made you a promise that I don't intend to break."
    hide hiflmc
    show vanessa whiphuntress hatangry at centre
    "She lets go of my hand and turns back to Li, resolve burning under her skin and making her almost glow with confidence."
    va "I know how your illusion works now, Vampire!"
    va "Cheap tricks won't work on me again!"
    "She readjusts her grip on her whip, cracking it against the ground as she pulls out her gun."
    hide vanessa
    show hiflmc casual surprised at centre
    "I watch as she rakes her gaze over our surroundings, devising a plan."
    show hiflmc casual angry
    "I pull out the stake and grip it tightly, just in case."
    hide hiflmc
    show vanessa whiphuntress hatangry at centre
    "Vanessa is at the top of her game as she darts forward, faster than Li can react."
    hide vanessa
    show vanessa huntress hatangry at left3
    show li casual angry at right3
    "She shoots at Li over and over again, forcing her to dodge until Li is right where Vanessa wants her."
    "Li is too busy avoiding Vanessa's blessed bullets to notice that she's stepped awfully close to the puddle of gasoline from earlier."
    "Her plans clicks in my head in an instant."
    hide vanessa
    hide li
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Good thinking, Vanessa!)"
    hide hiflmc
    show vanessa whiphuntress hatangry at left3
    show li casual angry at right3
    "Vanessa lashes out with the whip, ensnaring a furious Li."
    va "Now, [genericfn]!"
    hide li
    hide vanessa
    show hiflmc casual angry at centre
    mcvan "On it!"
    show hiflmc casual angry at left3
    show li casual surprised at right3
    "I grab the gas pump from where it’s lying on the concrete, spraying gasoline all over Li."
    hide hiflmc
    hide li
    show vanessa huntress hatbasic at centre
    "Vanessa instantly holsters her gun, pulling out a lighter."
    "She ignites it, tossing it onto the puddle of gas in what feels like slow motion"
    show vanessa huntress hatangry
    va "Run!"
    show hiflmc casual angry at right1
    show vanessa huntress hatblush at left1 behind hiflmc
    "She sprints back toward me, grabbing my arm and pulling me as far away as possible."
    hide hiflmc
    hide vanessa
    #bats
    show jdfire:
        xpos 0
    "In a bright blaze, Li catches fire with a pained shriek of rage before vanishing into a fiery swarm of bats."
    hide jdfire
    show hiflmc casual surprised at right1
    show vanessa huntress hatsurprised at left1 behind hiflmc
    "We stand there, panting, staring at each other in disbelief."
    mcvan "Did she just survive being set on fire?"
    show vanessa huntress hatsurprised
    va "It seems like it."
    va "But even for a vampire of her age, that’s a significant injury."
    show vanessa huntress hatangry
    va "One she won’t recoup from quickly."
    show vanessa huntress hatbasic
    va "She’ll be out of commission for the foreseeable future."
    show hiflmc casual happy
    "I feel a smile spread across my face."
    mcvan "So we... we really won."
    show vanessa huntress hathappy
    "Vanessa smiles back just as widely, her eyes shining."
    va "We really won."
    scene bg heroine_home_lights at bg with clockwise_wipe
    stop music fadeout 1.0
    play music hifleveryday
    "After all of the excitement, we decide to head back to Havenfall instead of going immediately to Headquarters."
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(It’s not like we’re in danger form Li at the moment, anyway.)"
    hide hiflmc
    show hiflmc casual basic at right4
    show vanessa huntress basic at left4
    "We both need to rest after everything– especially Vanessa, who refuses to talk about what she saw in the illusion."
    show hiflmc casual sad
    "By the time we get back to my house, the adrenaline has mostly faded and I feel about ready to collapse."
    show hiflmc casual blush
    "The only thing keeping me alert is the nervous energy that sparks across my skin every time I get close to Vanessa."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(I can’t stop thinking about that kiss.)"
    "(I want to talk to her about it, ask her how she felt about it, if she’d to do it again...)"
    show hiflmc casual_cu sad_cu
    "(But how do I even begin to approach that?)"
    show hiflmc casual_cu sarcastic_cu
    "(Sorry I kissed you without asking first, but it did snap you out of the illusion, and you didn’t seem to mind?)"
    show hiflmc casual_cu blush_cu
    "(It was a really good kiss and I would very much like to do it again?)"
    hide hiflmc
    show hiflmc casual blush at right4
    show vanessa huntress basic at left4
    "Just the thought of starting that conversation makes my cheeks burn."
    hide vanessa
    show hiflmc casual blush at centre
    "I avoid eye-contact, looking around at my living room instead, and notice how messy it’s gotten over the past week or so."
    show hiflmc casual surprised
    mcvan "Oh wow. I should really clean up around here."
    show hiflmc casual surprised
    mcvan "It’s still a mess from when Grace and I packed her stuff for school."
    show hiflmc casual sarcastic at right4
    show vanessa huntress basic at left4
    va "That makes sense. I’ll help."
    show hiflmc casual surprised
    mcvan "You don’t have to-!"
    show vanessa huntress smirk
    va "Two hands are better than one, right?"
    show hiflmc casual blush
    mcvan "Right. Yes. Absolutely."
    scene bg heroine_home_lights at bg with fade
    stop music fadeout 1.0
    play music hiflliteromance
    show hiflmc casual basic at right4
    show vanessa huntress basic at left4
    "We spend a while cleaning in silence, stealing glances at each other every so often."
    "When the living room finally feels less like a disaster zone, and more of a place where I’m not ashamed to have the girl I like in it..."
    "We take a break."
    show hiflmc casual blush
    "Even just sitting on the couch together makes my whole body tingle with awareness."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(I can’t just... un-know what it feels like to kiss her.)"
    hide hiflmc
    show hiflmc casual surprised at right4
    show vanessa huntress surprised at left4
    "Vanessa and I speak at the same time."
    mcvan "So uh..."
    va "About earlier..."
    show hiflmc casual blush
    show vanessa huntress blush
    "We pause, laughing awkwardly."
    show vanessa huntress smirk
    va "You can go first."
    show hiflmc casual surprised
    mcvan "No, that's fine, what were you going to say?"
    show vanessa huntress blush
    "Vanessa goes red, stammering."
    show hiflmc casual basic
    va "Well I uh."
    va "I mean, earlier."
    va "That was..."
    show hiflmc casual blush
    "I can’t help the blush that rises to my cheeks at that."
    mcvan "Yeah. It was..."
    mcvan "Did you, uh... I mean, was it-?"
    show hiflmc casual surprised
    stop music fadeout 1.0
    play music hiflsuspense
    "I’m cut off by the sound of her phone ringing."
    show vanessa huntress basic
    "Immediately, she schools her expression into a more serious look."
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(As if whoever’s on the other end of the line could tell if she displayed any sort of emotion.)"
    hide hiflmc
    show hiflmc casual basic at right4
    show vanessa huntress sad at left4
    va "I have to answer this, I’m sorry."
    show hiflmc casual happy
    mcvan "Don’t worry about it, it’s fine, do what you have to do."
    hide hiflmc
    show vanessa huntress basic at centre
    "She answers, and I’m close enough this time to hear the cold voice on the other end of the line."

    $sidecharone = "Mysterious Voice"
    sid1 "Huntress Helsing, you have new orders."
    sid1 "Eliminate [genericfn] [genericln] in order to prevent Dracula’s rebirth."
    sid1 "That is all."

    "The voice on the other end hangs up abruptly, not even waiting for Vanessa to respond."
    show hiflmc casual surprised at right4
    show vanessa huntress basic at left4
    "I feel the blood drain from my face."
    mcvan "Vanessa...?"
    $tobecontinued()
    scene bg hifltbc2 at bg
    with fade

    pause
    $ resets()
