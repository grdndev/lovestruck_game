label helena_season1_episode1:

    $tbc = False
    scene bg ll_chicago_rain at bg
    play music ll_everyday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show llmc modern basic at centre
    "They call Chicago the Windy City for a reason."
    show llmc altmodern altsad at left3
    show solaire sophie basic at right3
    "I shiver as Sophie and I step out of work and onto the street, grimacing at the grey clouds lingering in the sky above."
    "It looks like it's about to rain, or worse."
    show llmc modern basic
    mchelena "Did you bring your umbrella?"
    show solaire sophie sad
    sp "Not today. We're probably going to have to hustle over to the Red Line for a train."
    show llmc altmodern altsad
    mchelena "I hate taking the train when it's storming."
    sp "Same here, girl, but the alternative is getting drenched."
    show solaire basic
    sp "Unless you want to kill some time in the city before going home."
    show llmc modern happy
    mchelena "I'm up for it. Friend date at the Chinese place?"
    sp "Hmm."
    show solaire sophie happy
    sp "How about a movie?"
    "Sophie gets a wicked look in her eye, the sort I only see when she's about to drag me into some sort of adventure."
    mchelena "What movie, exactly?"
    sp "Well, I caught this preview last night when I was on a streaming binge.."
    show llmc modern smile
    mchelena "I can't believe you still don't use an adblocker like everyone else in our age bracket."
    show solaire sophie angry
    sp "Don't interrupt! I was trying to make this dramatic."
    show llmc modern happy
    mchelena "Alright, drama away."
    show solaire sophie sad
    "Sophie puts a hand to her heart, letting out an exaggerated sigh of longing."
    sp "Our heroine is caught between two dark forces trying to seduce her."
    sp "She knows she shouldn't give in, but the chance to save a corrupted heart drives her into their arms-!"
    show llmc modern surprised
    mchelena "Wait, both the love interests are evil?"
    show llmc modern angry
    mchelena "This better not be another vampire-werewolf thing."
    show solaire sophie angry
    sp "What's wrong with vampires and werewolves?"
    show solaire sophie happy
    sp "You either get some immortal sugar daddy who needs to be comforted about his existence or a hot protector who can transform into a wolf."
    sp "Who wouldn't want to do that?"
    show llmc altmodern altsad
    mchelena "Fair. We could all use someone to take care of our student loans."
    show solaire sophie sad
    sp "God, don't remind me."
    sp "This is supposed to be about having fun tonight, not doing the thousand yard stare at my future."
    show solaire sophie basic
    sp "Besides, there's no vampires or werewolves in this. Just magic."
    show llmc modern angry
    mchelena "Let me guess."
    mchelena "Two pale, brooding guys and a really overwrought forbidden fruit metaphor."
    show solaire sophie surprised
    sp "No! One of them's a woman."
    hide llmc
    hide solaire
    show llmc modern_cu happy_cu at centre
    "(...Okay, that's a little more interesting.)"
    show llmc altmodern_cu altblush_cu
    "(No, I can't be that shallow. Can I?)"
    hide llmc
    show llmc modern surprised at left3
    show solaire sophie basic at right3
    "Then Sophie tells me who the actress playing the villainess is."
    hide llmc
    hide solaire
    show llmc altmodern_cu altblush_cu at centre
    "(I'm definitely that shallow.)"
    hide llmc
    show llmc modern smile at left3
    show solaire sophie basic at right3
    mchelena "You know, last time you and I went to a movie like that, I had to cover your eyes because you got so flustered."
    show solaire sophie angry
    sp "Don't you judge me. I'm not the only single one in this boat, girl."
    show llmc modern surprised
    mchelena "Well, I..."
    hide llmc
    hide solaire
    show llmc altmodern_cu altsad_cu at centre
    "(Yeah. It's been a while.)"
    hide llmc
    show llmc modern basic at left3
    show solaire sophie angry at right3
    mchelena "But I'm probably not going to find the love of my life in the Rogers Park theatre."
    show solaire sophie basic
    sp "You never know."
    sp "What's your hard line, anyway? Something a person you date absolutely has to have."
    hide llmc
    hide solaire
    $menuhideborder = True

    menu helenas1e1c1:
        "A. Be shallow.":
            show llmc modern happy at left3
            show solaire sophie basic at right3
            mchelena "Can we start with them being hot? I'll take that for now."
            show solaire sophie happy
            sp "Ah, the eye candy route."
            sp "Fast burn, fast crash. But I feel you."

        "B. Be discerning.":
            show llmc modern happy at left3
            show solaire sophie basic at right3
            mchelena "Just one thing? I want to say smart or kind or..."
            mchelena "Someone who always stood up for me. That has my back no matter what."
            show solaire sophie happy
            sp "That'd be nice, wouldn't it?"

        "C. The heart matters the most.":
            show llmc modern happy at left3
            show solaire sophie basic at right3
            mchelena "I want them to love me as much as I love them."
            mchelena "Maybe that's not a trait, really, but when you care for someone that much, the other stuff doesn't matter, you know?"
            show solaire sophie happy
            sp "Aww. That's sweet."

    show llmc modern surprised
    show solaire sophie surprised

    stop music fadeout 1.0
    play music ll_suspense
    show rain
    "A rolling peal of thunder booms over our heads, and Sophie and I both shriek as rain comes pouring down in a torrent."
    "She starts running down the street with her purse over her head, and I run to follow."
    hide solaire
    show llmc modern surprised at centre
    pause 1.75
    "My foot slips against wet concrete and I lurch to catch myself, but when I look up, I can't see Sophie at all."
    mchelena "Shit. Did she go left or right?"

    show bg_001 at bg
    hide rain
    #play sound "<from 1 to 10>sfx/thunder.mp3"
    pause 0.1
    show bg_999 at bg with dissolve
    "Then a bolt of bright light blinds me. I hit the ground, shocked, and the rest of the world fades to a dizzying blur."
    show bg_137 at bg with dissolve
    "When I manage to open my eyes again, there's no street, only dark and wet earth."
    hide llmc
    show llmc modern_cu surprised_cu at centre
    "(What? Where am I?)"
    hide llmc
    show llmc altmodern altsad at centre
    "I sit up slowly, grimacing as mud sticks to my jeans."
    "A forest of huge trees surround me, gnarled branches and roots so thick that I can barely see the stars in the sky overhead."
    show llmc modern surprised
    mchelena "Did I pass out? It's night time now."
    mchelena "How did I get out of the city?"
    mchelena "Shawnee Forest is like...six hours away."
    hide llmc
    show llmc altmodern_cu altsad_cu at centre
    "(And the worst field trip of my fifth grade life. Just going to put that out there.)"
    hide llmc
    show llmc modern basic at centre
    "My head still aches a little as I stand up and turn a full circle, looking for any sign of a trail or a ranger station."
    "There's nothing but more trees, buzzing insect wings and the occasional rustle through the leaves."
    show llmc modern angry
    mchelena "God, I really should have been a Girl Scout."
    mchelena "If I just pick a direction and walk, I'll have to find something."
    show llmc altmodern altsad
    "Sticks crunch under my feet with every step, and I wince, trying to keep quiet."
    show llmc modern surprised
    "It's only when I slow down that I hear shouting in the distance."
    "Shouting and a low, feral growl."
    hide llmc
    show llmc altmodern_cu altsad_cu at centre
    "(Please don't be a bear.)"
    hide llmc
    show llmc modern basic at centre
    mchelena "Whoever that is probably needs help. And I need help."
    show llmc modern angry
    mchelena "We can help each other and then get out of this creepy-ass forest."
    "Ignoring the lump of fear in my throat, I weave my way through the branches and bushes towards the noise."
    show llmc modern surprised
    "When I get closer, I realize there's actually two voices."
    unknown "Shall we kill them?"
    unknown "No. The more blood we spill, the more will come."
    unknown "That is his game, Alain."
    hide llmc
    show llmc modern_cu surprised_cu at centre
    "(Oh god. Are they being attacked?)"
    "(Did I end up in the serial murder forest?)"
    hide llmc
    show llmc modern surprised at centre
    "I dare to peek past a thick tree trunk, my jaw dropping at what I see."
    stop music fadeout 1.0
    play music ll_helena

    scene helena1 at bg with fade:

        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    "Blue fire explodes outward, surrounding a beautiful woman in a cloak of crackling flame."
    "Her armor shines with accents of blue and white, silver blades glinting in the light of her flames."
    "She moves almost faster than I can see, driving off a pack of wolves with quick slices and cuts."
    "An echo of the cerulean blaze follows after, and the beasts yelp to get away from it, retreating into the shadows."

    scene bg dark_forest_rain with fade
    show llmc modern_cu surprised_cu at centre
    "(She did it!)"
    hide llmc
    show alain speararmour angry at centre
    ar "Petty bastard. At least his tricks are little match for your sorcery, Helena."
    hide alain
    show helena swordarmour sad at centre
    hk "We had both planned to patrol alone. Think if we had."
    hide helena
    show llmc altmodern_cu altsad_cu at centre
    "(Alright, this is definitely some sort of weird dream. I probably fell and hit my head.)"
    show llmc modern_cu basic_cu
    "(But until some poor EMT wakes me up, I might as well stick with the heroes of this piece.)"
    hide llmc
    show helena swordarmour angry at left2
    show alain speararmour angry at right2
    "I step out from around the tree into the clearing, only for Helena and Alain to whirl around and face me with their swords pointing outward."
    hide helena
    hide alain
    show llmc modern surprised at centre
    "Holding back a yelp, I raise my hands in obvious surrender."
    mchelena "Totally not a wolf!"
    hide llmc
    show helena swordarmour surprised at left2
    show alain speararmour surprised at right2
    hk "Alain. She..."
    ar "By the realms, this is a blessed day."
    hide helena
    show llmc modern surprised at left3
    show alain armour basic at right3
    "I blink in confusion as Alain puts his two-bladed sword down and drops to one knee, almost bowing his head all the way to the ground."
    ar "My glorious queen."
    mchelena "Queen?"
    hide alain
    show llmc modern at left2
    show helena armour basic at right2 behind llmc
    pause 1.0
    "The question barely leaves my lips before Helena lets her swords fall and wraps her arms around me in a tight embrace."
    show llmc altmodern altblush
    "She's so tall that my face ends up right against her chest."
    hide llmc
    hide helena
    show llmc altmodern_cu altblush_cu at centre
    "(This is definitely a dream, oh my god.)"
    hide llmc
    show llmc modern surprised at left2
    show helena armour happy at right2 behind llmc
    hk "My Queen, I feared you would never return."
    hide llmc
    hide helena
    $menuhideborder = True
    menu helenas1e1c2:
        "A. Stay still as you can.":
            $menuhideborder = False
            show llmc modern surprised at left2
            show helena armour happy at right2 behind llmc
            "I have no idea what's going on."
            "The hug is nice, but I'm not exactly sure who Helena is, if I should break away or pull her closer."

        "B. Hug Helena back.":
            $menuhideborder = False
            show llmc altmodern altblush at left2
            show helena armour happy at right2 behind llmc
            "Ignoring the warmth rising to my face, I slip my arms around Helena's back."
            show helena armour surprised
            "She stiffens for a second, like she didn't expect to be touched."

        "C. Try to pry her off.":
            $menuhideborder = False
            show llmc modern surprised at left2
            show helena armour happy at right2 behind llmc
            "(She's really strong. I'm going to lose a rib.)"
            "I twist and shimmy a little bit, trying to jostle Helena's hands loose, but from my position, it doesn't let me do much but nudge her shoulder."

    show llmc modern basic at left3
    show helena armour blush at right3
    "After a tense second, Helena releases me and steps back."
    show helena armour sleep
    "Her face is pink, although she takes a deep breath and draws a look of cold, regal composure back together."
    show helena armour basic
    hk "Apologies, my Queen. I should not have been so presumptive."
    "She bows at the waist, but her eyes never leave me."
    hide llmc
    hide helena
    show llmc modern_cu happy_cu at centre
    "(Queen, huh? I'll roll with it.)"
    hide llmc_head
    show llmc modern happy at left3
    show helena armour at right3
    llmc "It's okay. You just surprised me."
    show helena armour face_sad
    hide llmc
    show alain armour angry at left3
    "She and Alain share a sharp look, and he gets to his feet."
    ar "We must bring her back to the castle. It is not safe here."
    hk "Indeed."
    hide alain
    show llmc modern at left3
    hk "Please, your majesty, let us do the honor of escorting you."
    hide llmc
    hide helena
    show llmc modern_cu happy_cu at centre
    "(How am I going to say no to that?)"

    scene bg_141 at bg with fade
    "Helena and Alain walk with me along a heavy beaten path until I see towering columns of marble and crystal piercing the sky."
    "I know they said 'castle', but this looks like something that burst out a fairytale."
    show llmc modern surprised at centre
    llmc "Wow."
    show Mc at left3
    show helena armour happy at right3
    hk "Welcome home, my Queen."
    hide llmc
    hide helena
    "We walk across a wide stone bridge and under a series of curved arches through the two massive front doors."

    scene bg_144 at bg with wipeleft
    show llmc altside altsad at centre
    stop music fadeout 1.0
    play music ll_suspense
    "A cool rush of wind makes me shiver as they open, then swing shut behind us with a low thud."
    show llmc modern surprised
    "Ornate metal details and stained glass stands out from every corner, but what catches my eyes is an albino raven atop a high plinth."
    "It stares at me, then flies off down the hall in a flurry of wings."
    hide llmc
    show alain armour angry at centre
    ar "Jinhai has seen us."
    hide alain
    show helena armour face_sad at centre
    hk "Of course he has. Pray he brings the others."
    hide helena
    show llmc modern surprised at centre
    "Neither one of them sound too happy about that, but I don't have time to figure out why when another set of doors open."
    hide llmc
    show lennox casual angry at left3_far
    show magnus casual angry at centre_magnus
    show Jinhai angry at right3_far
    "Three men walk into the hall together, although the only thing they have in common is the color of their clothes."
    hide lennox
    hide magnus
    hide Jinhai
    show alain armour happy at centre
    ar "Magnus! Look upon the light of our Queen's face and be joyous."
    hide alain
    show magnus casual angry at centre_magnus
    "The tallest of the trio, Magnus frowns at me, cutting an intimidating shape in his pointed armor."
    show magnus casual at centre_left
    show Jinhai angry at right3_25
    "Then he looks to the man at his left, who has long hair and...pointed ears?!"
    hide magnus
    hide Jinhai
    show llmc modern_cu surprised_cu at centre
    "(Okay, so we're going full Dungeons and Dragons. Got it, brain.)"
    hide llmc_head
    show magnus casual angry at centre_left
    show Jinhai angry at right3_25
    mv "Your scouts were right, Jinhai."
    jj "Are they ever wrong?"
    hide magnus
    hide Jinhai
    show lennox casual happy at left3
    show llmc altside altsad at right3
    "The last man smiles at me, but he's showing so many teeth I feel a shiver go down my spine."
    show lennox casual at left3
    pause 0.5
    "When he steps forward to get a closer look, I have to fight the urge to take a step back."
    misc "She does not glow half as bright without her crown."
    hide lennox
    hide llmc
    show helena armour angry at centre
    hk "Mind your tongue."
    show lennox casual angry at left3
    show helena armour at right3
    misc "I bend to her command, Helena, not yours."
    hide lennox
    hide helena
    show lennox casual_head at centre
    "From the stare he's giving me, he must expect something, but I can't guess what."
    hide lennox_head
    show lennox casual at centre_close_left
    show llmc altside altsad at right3
    llmc "Sorry. I don't know who you are."
    hide lennox
    show Mc at centre
    "Every eye on the room falls on me."
    show llmc modern surprised
    "Under five intense gazes, I lock up, worried I've just done something awful."
    hide llmc
    show magnus casual angry at centre_magnus
    mv "How is it possible the Witch Queen does not recognize one of her own generals?"
    hide magnus
    show llmc modern_cu surprised_cu at centre
    "(Wait, Witch Queen?)"
    hide llmc_head
    show alain armour face_smirk at centre
    ar "She has just returned to us, Magnus. Or perhaps Lennox is simply not memorable."
    hide alain
    show Jinhai face_creepy at centre
    "Alain chuckles low, and Jinhai cracks a smile."
    hide Jinhai
    show lennox casual angry at centre
    "Lennox, the man in the robes, narrows his eyes."
    hide lennox
    show alain armour happy at centre
    ar "We should be celebrating! How can you be dour when the time for our triumph has returned?"
    hide alain
    show magnus casual angry at centre_magnus
    mv "There will be triumph when our armies gather again, when we are not pushed into the smallest corner of our territory."
    mv "Even our most loyal are beginning to buckle under."
    hide magnus
    show alain armour angry at centre
    ar "Do you think only with your sword?!"
    hide alain
    show llmc modern surprised at centre_left_15 zorder 2
    show helena armour at centre_close_right
    "Helena places a hand on my shoulder."
    hide llmc
    hide helena
    show magnus casual angry at centre
    show alain armour angry at right1
    "I don't understand why until Alain roughly knocks a chair onto the floor, getting right up in Magnus' face."
    hide magnus
    hide alain
    show llmc modern surprised at left1
    show helena armour at right1
    "I jump as wood shatters at my feet, and Helena's fingers give a light squeeze."
    hk "His temper has found a new edge without you, my Queen. I will have a servant fix the chair."
    show llmc altside altsad
    llmc "T-Thank you."
    hide llmc
    hide helena
    show magnus casual angry at centre
    show alain armour angry at right1
    ar "You only lead us in her absence, Magnus. Unless your warmongering has given you new ambition."
    ar "Shall I cut it out of you?"
    mv "I dare you to try, boy."
    show magnus casual at left3
    show alain armour at right4
    show lennox casual angry at centre
    "Lennox moves to intercept, placing hands on both men's chests to keep them physically apart."
    "Magnus grits his teeth, one hand clenching into a mailed fist."
    hide alain
    hide magnus
    la "Use your words, gentlemen. Our Queen has punished more useful creatures for less."
    show lennox casual happy
    "Then he looks at me, raising an eyebrow."
    la "Have you not?"
    hide lennox
    show llmc modern_cu surprised_cu at centre
    "(Wait, what the hell does he want me to say?)"
    hide llmc
    $menuhideborder = True
    menu helenas1e1c3:
        "A. I don't want to punish anyone.":
            $menuhideborder =  False

        "B. Why are you asking me?":
            $menuhideborder = False
            show llmc modern surprised at centre
            mc "Why are you asking me?"
            show Mc at pos_left
            show lennox casual surprised at right3
            lennox "Why? What do you mean why?"
            lennox "I would think it is obvious."

        "C. Let them figure it out.":
            $menuhideborder = False
            show llmc modern angry at centre
            mc "Let them figure it out, Lennox."
            mc "I'm pretty sure they're both adults."
            show Mc at pos_left
            show lennox casual angry at right3
            lennox "Truly?"
    hide llmc
    show Lennox at centre
    "Lennox's jaw tightens, caught between anger and confusion, but Helena turns me to face her directly."
    hide lennox
    show helena armour_cu basic_cu  at centre
    "Fingers slip under my chin, tilting my eyes upward so I can see no one else."
    hk "My Queen, what were the last orders you gave me before you perished?"
    hide helena
    show llmc altmodern_cu altsad_cu at centre
    mchelena "..."
    show llmc modern_cu angry_cu
    "(I have no fucking idea. Does it matter?)"
    "(Is dream logic going to apply here?)"
    show llmc modern_cu basic_cu
    mchelena "I...I don't remember."
    hide llmc
    show llmc modern basic at left2
    show helena armour basic at right2
    "Helena nods decisively before her touch fades, attention turning to the other generals."
    hk "Her mind has clearly not recovered from being made flesh."
    hk "Of course she cannot give orders in such a state, if she does not even remember her purpose here."
    hide llmc
    hide helena
    show magnus casual angry at centre
    magnus "That is madness. A Queen with no memory cannot lead us!"
    show magnus casual angry at left1
    show helena armour angry at right2
    hk "I did not say it was permanent, Magnus."
    hide magnus
    show Helena basic
    show llmc modern basic at pos_left
    hk "Come with me, my Queen. Even if you do not know it now, you prepared me for this moment."
    show llmc modern basic at left1
    show helena armour basic at right1 behind llmc
    "Helena puts an arm around my back and sweeps me out of the hall before any of the men can say another word."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
