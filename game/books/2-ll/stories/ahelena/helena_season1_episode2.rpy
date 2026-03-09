label helena_season1_episode2:

    $tbc = False
    scene bg_165 at bg
    play music ll_everyday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show llmc modern basic at left3
    show helena armour basic  at right3
    "She takes me through a labyrinth of doors and halls until we reach a large bedroom, awash in silver and blue."
    "Everything inside looks outrageously expensive, but Helena guides me over to the bed before I can ask who It belongs to."
    hk "Ignore the concerns of the others, my Queen."
    show helena armour sad
    hk "I should have understood your state to begin with. The strange speech and your clothes."
    show llmc modern surprised
    mc "Is there something wrong with my clothes?"
    hk "I..."
    hk "Only that they are nothing compared to your previous finery."
    show llmc modern happy
    "Helena looks worried for a moment, like she might have insulted me, but when I smile, her shoulders relax."
    show helena armour basic
    hk "You really do not remember this place?"
    hk "It is your bedroom, after all."
    show llmc modern smile
    mc "Sweet, really?"
    mc "I could definitely get used to a place like this."
    show helena armour surprised
    "Helena opens her mouth to say something, brow furrowing in confusion before she gives up."
    show helena armour basic
    "She leaves the bed, only to drop down to her knees in front of me."
    show llmc modern surprised
    mc "Um..."
    hide llmc
    hide helena
    show llmc altmodern altblush at centre
    "(Don't blush. Don't-!)"
    hide llmc
    show helena armour basic at centre
    "Her head ducks down, hands searching underneath the frame of the bed itself,"
    "And I manage to ward off how flustered I am when Helena pulls out a small metal chest."
    show helena armour sleep
    "She murmurs something under her breath, and a blue spark jumps from her fingertips, entering the lock."
    show llmc modern basic at left3
    show helena armour basic at right3
    "It clicks open, and Helena places the chest beside me before opening the lid."
    "Inside on a bed of plush blue velvet is a bunch of jagged metal pieces."
    show llmc modern surprised
    mc "Uh, are those supposed to look like that?"
    show helena armour sad
    hk "No, my Queen. This is what remains of your crown."
    hk "It was destroyed in the moments before your death, and we recovered what we could."
    hide llmc
    hide helena
    show llmc modern_cu surprised_cu at centre
    "(My death?!)"
    hide llmc
    show llmc modern basic at left3
    show helena armour basic at right3
    mc "Wait a second."
    show llmc modern surprised
    mc "So the reason all of you are so surprised to see me is because I look like your dead queen brought back to life?"
    hk "You are her. It is only a matter of arousing your memory."
    hide llmc
    hide helena
    show llmc altmordern_cu altblush_cu at centre
    "(Not how I would have used the word 'aroused', but it's a free country.)"
    show llmc altmodern_cu altsad_cu
    "(Or maybe it's not. I don't actually know what kind of country this is at all.)"
    hide llmc
    show llmc modern basic at left3
    show helena armour basic at right3
    hk "The night before you perished, my Queen, you told me the crown was the key to your resurrection."
    hk "I believed that meant bringing you back in body."
    show helena armour sad
    hk "I cast every spell I could think of, but even the fragments reflected my magic."
    show helena armour basic
    hk "Now I see it was intended to awaken your mind."
    hide llmc
    hide helena
    show llmc modern_cu happy_cu at centre
    "(Being awake would be a good thing right now, so I'm cool with that.)"
    hide llmc
    show llmc modern basic at left3
    show helena armour basic at right3
    mc "What do I do with the pieces?"
    hk "Touch them, I believe."
    hk "Perhaps you will be able to channel your own magic into forging the crown together once more."
    "I'm not sure about that, but I place my hands over the broken crown, grabbing the largest piece."
    show llmc modern surprised
    stop music fadeout 1.0
    play music ll_suspense
    "A burst of energy shocks my fingers as it glows blue, and I drop it right away."
    mc "Ow."
    show helena armour surprised
    hk "My Queen?"
    show llmc altmodern altsad
    "The pain fades, but I don't think anything's changed."
    "Nothing new comes to mind, and the bedroom around me seems just as unfamiliar as before."
    show llmc modern basic
    mc "Sorry. Still me."
    show helena armour sad
    hk "..."
    hk "How is this possible?"
    show llmc altmodern altsad
    mc "Maybe because it's broken? I really don't know."
    show llmc modern basic
    mc "Can't you just tell me what she was like? What you think I'm supposed to be like?"
    "Helena frowns in quiet consideration before nodding."
    show helena armour basic
    hk "If you believe that will be of assistance, of course."
    show helena armour smirk
    hk "You, my Queen, were a revolutionary."
    hk "A woman who fell in love with the old King of this realm only to have your heart shattered."
    show helena armour angry
    hk "Those in his inner circle sought to stifle your ambition, and they were punished for their arrogance."
    show helena modern basic
    hk "But it began a great war, and for years, every day was nothing but slaughter."
    hide llmc
    hide helena
    show llmc modern_cu surprised_cu at centre
    "(That's horrible!)"
    hide llmc
    show llmc modern surprised at left3
    show helena armour basic at right3
    hk "I fought at your side gladly, but we were driven back."
    show helena armour sad
    hk "A lord that served the King led an army right to your doorstep."
    hk "In the conflict, you were slain."
    show llmc modern basic
    show helena armour sleep
    "Sorrow rends Helena's voice, and she pauses, taking in a deep breath."
    show helena armour sad
    hk "If I had not believed there was hope of your return, I would have surrendered then and there."
    show helena armour happy
    hk "But I did not, and my faith was rewarded."
    hide llmc
    hide helena
    show llmc modern_cu basic_cu at centre
    "(I'm pretty sure she thinks of me as a lot more than a ruler.)"
    hide llmc

    $menuhideborder = True
    menu helenas1e2c1:
        "A. Was she your mentor?":
            $menuhideborder = True
            show llmc modern basic at left3
            show helena armour basic at right3
            mc "Was the Witch Queen your mentor?"
            show helena armour happy
            hk "Of course you were. My magic would not be half of what it is now without you."

        "B. Were we together?":
            show llmc modern surprised at left3
            show helena armour basic  at right3
            mc "Were we together? I mean, you and the Witch Queen."
            show helena armour surprised
            hk "Intimately?"
            show helena armour sad
            hk "...I suppose you would have forgotten that as well."

        #"C. Is this a religious thing?":
    hide llmc
    hide helena
    show llmc altmodern_cu altsad_cu at centre
    "(I feel like I'm stringing her along.)"
    hide llmc
    show llmc modern surprised at left3
    show helena armour basic at right3
    mc "Helena, I don't think I'm this Witch Queen at all. Maybe I look like her but-!"
    show helena armour angry
    hk "You must be!"
    "Anger snaps into Helena's voice, but more than that is desperation."
    "On her knees in front of me, she looks like a wounded wolf, trying not to lash out."
    hide llmc
    hide helena
    show llmc modern_cu basic_cu at centre
    "(Okay, let's think this through.)"
    show llmc altmodern_cu altsad_cu
    "(I don't want to upset Helena more, but we've got to clear the air somehow.)"
    "(...Even if I wouldn't be very logical if someone close to me had died and came back as some kind of forgetful clone.)"
    hide llmc
    show llmc modern basic at left3
    show helena armour angry at right3
    mc "Can I tell you my name, Helena?"
    mc "The one I'm used to hearing."
    show helena armour sad
    hk "I...I suppose."
    show llmc modern happy
    mc "It's [genericfn]. [genericfn] [genericln]."
    show llmc altmodern altsad
    mc "I don't remember anything about this war you're talking about, but I can see how much damage it caused."
    mc "That's why all the other generals were tense, right? Why Alain got so pissed off?"
    hk "Yes. We have been exiled to this castle since your death."
    hk "There is little we can do but occasionally strike outside these borders to ensure our enemies do not think us complacent."
    show llmc modern happy at left3
    stop music fadeout 1.0
    play music ll_lightromance
    mc "I'm a pretty big fan of living. And it seems like you are too."
    mc "So how about we work together to bring your Queen back, just the way she was?"
    show helena armour basic
    "Helena goes quiet for a long moment, staring at me until I offer a hand to bring her up off the floor."
    show llmc modern basic at left2
    show helena armour basic at right2
    "She takes it with a light grip, and settles stiffly next to me on the bed."
    show helena armour sad
    hk "You have no idea how strange it is to hear such words leaving your lips."
    hk "To see you in such clothes, acting as you do."
    hk "Were you an imposter, I would expect the facade to be kept up as long as possible, but instead you…"
    hk "You are kind, as if you truly lack any recollection of how much blood was spilled in your name."
    hk "That is a mercy I did not believe could exist."
    hide llmc
    show helena armour basic at centre
    "Helena's entire body tenses, her hands pressed together tightly in her lap."
    "I can't tell if she's sad or angry, but regardless, she's supremely upset."
    show llmc modern basic at left2
    show helena armour surprised at right2
    mc "Helena."
    show helena armour sad
    "She looks at me, eyes narrowed and wary."
    mc "Did you fight in the war to protect the Witch Queen? Because you cared for her?"
    show helena armour happy
    hk "Of course."
    hk "I owe you...her...everything I am."
    show llmc modern happy
    mc "Sounds pretty noble to me."
    hide llmc
    show helena armour surprised at centre
    "A startled glance is my only answer before Helena stands up, putting a deliberate distance between the two of us."
    show helena armour sad
    hk "I must tell the others the crown was not enough to restore your memory."
    hk "Whatever Magnus' plans are must wait. You are in no state to lead an army."

    $menuhideborder = True
    menu helenas1e2c2:
        "A. Helena, stay with me." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show llmc altmodern_cu altsad_cu at centre
            "(I don't want to be alone in this room.)"
            show llmc modern_cu basic_cu
            "(Helena's been protecting me since we met.)"
            hide llmc
            show llmc altmodern sad_side at left3
            show helena armour basic at right3
            mc "Does it have to be now?"
            show helena armour sad
            hk "I will not lie to them."
            show llmc modern surprised
            mc "That's not what I said."
            show llmc altmodern sad_side
            mc "Can you just stay with me a little while longer?"
            show helena armour surprised
            "Helena visibly hesitates, eyes flickering towards the bedroom door."
            show helena armour basic
            "Silence stretches out into a long, tense minute before she relents, turning back towards the bed."
            hk "I am not sure how pleasant you expect my company to be."
            show llmc modern happy
            mc "You realize that I don't remember you, right?"
            mc "That means I want to know more about who you are."
            show helena armour blush
            "That catches her off-guard completely, and I have to hold back a smile when heat rises to Helena's face."
            "(She's cute when she's flustered.)"
            hk "I suppose that is true."
            show llmc modern smile
            mc "Then sit back down."
            show llmc modern basic at left1
            show helena armour sad at right1
            "I pat the bed beside me, and this time Helena sits a few inches closer."
            "Her posture isn't any less rigid, though."
            hide llmc
            hide helena
            show llmc modern_cu basic_cu at centre
            "(What are some good starter questions?)"
            show llmc altmodern_cu altsad_cu
            "(...I'm kind of used to clicking from those huge lists in dating apps.)"
            hide llmc
            show llmc modern happy at left1
            show helena armour sad at right1
            mc "How about you tell me where you're from? Or about your family?"
            show llmc modern surprised
            show helena armour angry
            "Helena's gaze darkens, and I bite my tongue, realizing I just punched a nerve."
            mc "No family. Just you."
            show llmc modern basic
            show helena armour basic
            hk "I was born Helena Klein in a village that no longer exists about, mm, thirty years ago."
            hk "There is little of note. I have no noble bloodline, which made my innate skill for sorcery a surprise."
            show llmc modern surprised
            mc "So you really cast spells, huh?"
            show llmc modern happy
            mc "I saw the fire you made against those wolves."
            mc "That was wild."
            show helena armour sleep
            hk "That is but a small fraction of my power."
            show helena armour basic
            hk "Your...the Witch Queen's tutelage unleashed my full potential."
            hk "I can make a shield strong enough that a hundred men cannot break it."
            hk "I can will myself miles away in the blink of an eye."
            hide llmc
            hide helena
            show llmc modern_cu surprised_cu at centre
            "(Holy shit.)"
            show llmc basic_cu smile_cu
            "(That's pretty cool.)"
            hide llmc
            show llmc modern smile at left1
            show helena armour basic at right1
            mc "How do you do it? Can you teach me?"
            show llmc modern basic
            show helena armour sad
            "Helena frowns before shaking her head."
            hk "Your own ability must be sealed away with your memories, my Queen."
            show helena armour basic
            hk "It is a facet of the soul."
            hk "I have seen a single spell turn the tide of battle under your hands, watched entire armies break and run rather than face you."
            hk "I hoped, that with your guidance, I would one day be able to do the same."
            show llmc modern happy
            mc "That's some ambition."
            hide llmc
            hide helena
            show helena armour_cu basic_cu at centre
            stop music fadeout 1.0
            play music ll_helena
            "Helena moves in a blur and I'm suddenly pinned back against the bed, her body above mine, face just inches away."
            "When she leans even closer, my breath catches."
            show helena armour_cu sad_cu
            hk "Are you testing me?"
            hk "Is this a game? Seeing if I am clever enough to pierce through your ruse?"
            hide helena
            show llmc modern_cu surprised_cu at centre
            mc "What?"
            mc "No."
            hide llmc
            show helena armour_cu basic_cu at centre
            hk "I accept my past."
            hk "All that I have done, misguided or otherwise."
            show helena armour sad
            hk "Do not torture me by pretending."
            hide helena
            show llmc modern_cu surprised_cu at centre
            mc "Helena, I'm not."
            mc "I promise I'm not."
            "(What kind of person was the Witch Queen for her to even think that was a possibility?)"
            hide llmc
            show helena armour_cu sad_cu at centre
            "She huffs, and a lock of platinum hair falls against my face."
            hide helena
            scene bg_165 at bg
            show llmc modern basic at left3
            show helena armour sad at right3
            "When Helena realizes how close we are, she pulls away, murmuring an apology under her breath."
            hide llmc
            hide helena
            show llmc altmodern_cu altsad_cu at centre
            "(Damn. I wasn't really minding that part.)"
            hide llmc
            show llmc modern basic at left3
            show helena armour basic at right3
            mc "Maybe you could tell me a little about-!"
        "B. Let her go.":
            $menuhideborder = False








    show llmc modern surprised
    "A sharp pain goes through my temples and I gasp."
    show llmc altmodern altsleep
    "Everything suddenly seems too bright, so I close my eyes."
    show helena armour surprised
    hk "[genericfn]?"

    show llmc altmodern altsleep at left4:
        linear 0.75 blur 5
        linear 0.75 blur 0
    show helena armour surprised at right4:
        linear 0.75 blur 5
        linear 0.75 blur 0
    show bg_165:
        linear 0.75 blur 5 zoom 1.5
    scene bg_143 at bg with dissolve:
        linear 0.75 zoom 1.0

    #scene bg wqcastle_exterior_v3 with dissolve
    "Images flash through my mind, splintered moments."
    show helena swordarmour angry at centre
    "I see Helena on a battlefield, using her magic to wall off the bridge to the castle."
    hide helena
    "On the other side, dozens of soldiers fight to break through."

    show bg_161 at bg with dissolve
    "Their banner has a wolf's head, and when I focus on that, an empty throne takes its place."

    scene bg_165 at bg with fade
    show llmc altmodern sad_side at centre
    mc "Ow, god. That really hurts."
    show llmc modern basic at left2
    show helena armour sad at right2
    "I force my eyes open, breathing hard, and Helena is right next to me."
    "Equal parts fear and concern dominate her expression, watching me closely."
    hk "Are you well?"
    show llmc modern basic
    mc "Headache. A real bad one."
    hk "The toll exacted on your body must be greater than I thought."
    hide llmc
    show helena armour basic at centre
    "She stands up from the bed and starts searching through the nearby armoire, plucking out a small container a moment later."
    "There's some sort of herb inside, and Helena presses it into my hand."
    show llmc modern basic at left3
    show helena armour basic at right3
    hk "Eat it. The salve is temporary, but potent."
    show llmc altmodern sad_side
    "The leaf tastes terribly bitter, but I manage to chew and swallow it down."
    show llmc modern basic
    hk "Rest while I speak to the other generals."
    hk "You will need all your strength for the days ahead."

    show bg_166 at bg with dissolve
    "With a wave of her hand, the light in the room dims, and exhaustion washes over me in the darkness."
    hide helena
    show llmc altmodern altsleep at centre
    "Before Helena even closes the door on her way out, I fall asleep."

    scene bg_165 with fade
    show llmc altmodern sad_side at centre
    stop music fadeout 1.0
    play music ll_everyday
    "I wake up in a tangle of the sheets, rubbing my eyes to clear away the remnants of sleep."
    show llmc modern basic at left2
    show helena witchcasual basic2
    "When my vision focuses, I find Helena sitting on the bed right next to me."
    hide llmc
    hide helena
    show llmc altmodern_cu altblush_cuat centre
    "(Woah. Good morning.)"
    hide llmc
    show llmc modern basic at left2
    show helena witchcasual basic at right2
    mc "Everything okay?"
    hk "I would ask the same to you."
    hk "Do you feel any different?"
    show llmc altmodern altsad
    "My head stopped hurting after I passed out, but those violent images jump into my thoughts again."
    hide llmc
    hide helena
    show llmc altmodern_cu altsad_cu at centre
    "(Were those supposed to be memories?)"
    show llmc modern_cu surprised_cu
    "(I can't really be the Witch Queen, right? There's no way.)"
    hide llmc
    show llmc modern basic at left2
    show helena witchcasual basic at right2
    mc "Not really."
    show helena witchcasual sad
    "Helena looks disappointed, but nods in acceptance nonetheless."
    show helena witchcasual basic
    hk "I spoke to Alain last night."
    hk "He knew you in your youth, and was startled to hear that you did not even remember him."
    show helena witchcasual sad
    hk "That you could be made so different is…frightening in a way."
    show llmc witchcasual smile
    mc "I'd be all about having magic and fancy clothes if I could snap my fingers and do it, trust me."
    hk "Hmm."
    show helena witchcasual basic
    hk "Clothes we can certainly take care of."
    hk "Strip."
    hide helena
    show llmc altnaked altblush at centre
    stop music fadeout 1.0
    play music ll_literomance
    "The sudden command leaves my face red, but I start taking off my shirt as Helena goes to the dresser and starts putting together an outfit."
    show llmc altnaked altblush at left3
    show helena witchcasual basic at right3
    "By the time she turns around, I'm down to my underwear and trying not to be self-conscious."
    "Her eyes sweep over me from head to toe, lingering long enough that my heart starts pounding in my chest."
    show helena witchcasual happy
    hk "I am thankful your beauty remains intact."
    mc "Thankful, huh?"
    hide llmc
    hide helena
    show llmc altnaked_cu altblush_cu at centre
    "(God, my face is burning so hot it could cook an egg.)"
    hide llmc
    show llmc naked basic at left3
    show helena witchcasual at right3
    "She doesn't answer, offering a pair of dark trousers for me to put on."
    show llmc altcasual altsad
    "They fit perfectly, and I try not to think too hard about that as Helena pulls a tunic down over my head,"
    show llmc casual basic
    "Carefully tightening the laces and smoothing out the wrinkles when it's on."
    hk "This is not as regal as your formal wear, but it is hardy enough."
    show helena witchcasual happy
    hk "And more comfortable than full armor."
    show helena witchcasual basic
    show llmc altcasual altblush
    "Every time her fingers brush over my body, I have to fight not to react,"
    show helena witchcasual basic at left1 behind llmc
    "But I shiver when Helena presses against my back, slipping a belt around my hips and drawing the ends tightly together."
    "A vest comes after, buckles braced from my stomach to right under my breasts."
    show llmc casual basic
    show helena witchcasual basic at right3
    "Then she offers a pair of bracers to me that seem to be made of real leather."
    hk "Sit on the bed and put these on."
    show helena witchcasual happy
    hk "I will take care of your boots."
    show llmc altcasual altblush
    show helena witchcasual basic
    "I start fumbling with the thick laces as Helena kneels and guides my foot into the first boot,"
    "Intensely focused while doing the ties up my calf one by one."
    hide llmc
    hide helena

    $menuhideborder = True
    menu helenas1e2c3:
        "A. You don't have to do this.":
            $menuhideborder = False
            show llmc casual basic at left3
            show helena witchcasual basic at right3
            mc "You don't have to do all this, you know."
            mc "I'm sure I'd figure it out eventually."
            show helena witchcasual happy
            hk "It is no burden. I have a handmaiden's practice when it comes to you, my Queen."

        "B. Thank you.":
            $menuhideborder = False
            show llmc modern happy at left3
            show helena witchcasual basic at right3
            mc "Thank you."
            show helena armour blush
            hk "There is no need for gratitude."

        "C. Is this a regular thing?":
            $menuhideborder = False
            show llmc casual surprised at left3
            show helena witchcasual at right3
            mc "Is this a regular thing for you?"
            show helena witchcasual happy
            hk "It was once, when I found myself in the queen's chambers more often."
            hk "She did not like the interruption of servants in the morning."

    hide helena
    show llmc casual basic at centre
    "Once Helena has dressed me completely, I get up to look in the mirror."
    show llmc casual happy
    "It's weird to see myself wearing something so medieval, but she's right: the clothes are pretty comfortable."
    hide llmc
    show helena witchcasual_cu basic_cu at centre
    "Her eyes lock on mine in the reflection, and I'm lost in that dark gaze for just a moment."
    hide helena
    show llmc casual basic at left3
    show helena witchcasual basic at right3
    hk "I will instruct you how to act like the Witch Queen the best I can."
    hk "Even if Alain and the others may not take much comfort from it, perhaps it will stir your memories."
    show llmc casual happy
    mc "Sure. Worth a shot."
    hide llmc
    hide helena
    show llmc casual_cu happy_cu at centre
    "(I did promise I would help her, even if I don't think there's much I can do.)"
    hide llmc
    show llmc casual happy at left3
    show helena witchcasual happy at right3
    hk "To breakfast then."
    show llmc casual surprised
    "My stomach grumbles in response."
    show llmc casual happy
    mc "Please."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
