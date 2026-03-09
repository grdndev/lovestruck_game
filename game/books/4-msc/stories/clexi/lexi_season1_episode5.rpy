label lexi_season1_episode5:

    $tbc = False
    scene bg msc_beach_bar_day at bg with dissolve
    play music msctense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show lexi casual basic at left1
    show hannah casual angry at right1 behind lexi
    "Hannah rages past me and shoves her finger in Lexi's face."

    lx "Hannah, get your finger out of my face."

    "Lexi barely glances at Hannah before turning her attention back to her coffee and taking a leisurely sip."
    hide lexi
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Lexi barely even looked at Hannah and the way her body is completely relaxed even though Hannah is being so aggressive...)"

    "(It's like this is boring to her. Her guard is completely down. Isn't she worried about Hannah at all?)"
    hide mscmc
    show jerry casual angry at centre
    "I glance at Jerry to try and ascertain his feelings on the situation."

    "He continues to prep the bar for the evening, but his tense shoulders let me know he's ready to step in if the situation gets out of hand."
    hide jerry
    show lexi casual basic at left1
    show hannah casual angry at right1 behind lexi
    hj "Don't tell me what the hell to do."
    hide lexi
    hide hannah
    show lexi casual_cu basic_cu at lexi_cu:
        xpos 300
    show hannah casual_cu angry_cu at hannah_cu behind lexi:
        xpos 775
    "Spit flies from Hannah's mouth as she snaps at Lexi."

    hj "...and if you think for a second that I'll forgive you for using me as a scapegoat-!"
    show lexi casual_cu sleep_cu
    "Lexi thrums her fingers on the bar, putting her back to Hannah."
    show lexi casual_cu smile_cu
    lx "It wasn't my fault, Hannah. Jeez. We were both there. You messed up and got caught"

    lx "What did you want me to do? Turn myself in?"
    show hannah casual_cu sad_cu
    "Hannah opens her mouth to retort, but stumbles in her response."
    show hannah casual_cu angry_cu
    hj "That's not-! God! This is what I hate about you! You could have done anything to help me and you just left me to rot."
    hide lexi
    hide hannah
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Can mermaids even go to human jail?)"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu:
        xpos 300
    show hannah casual_cu angry_cu at hannah_cu behind lexi:
        xpos 775
    lx "I don't know what you want me to say. I haven't seen or spoken to you in years..."
    show lexi casual_cu angry_cu
    lx "...and now you're over here yelling about how I did you dirty."

    "A fire ignites in Hannah's eyes at Lexi's comment."

    "Her sunglasses break with a crunch as she squeezes them in her hand."
    hide lexi
    hide hannah
    show jerry casual angry at centre
    "Jerry tenses at the sound and I can tell that he's ready to jump in if an actual fight breaks out."
    hide jerry
    show lexi casual_cu angry_cu at lexi_cu:
        xpos 300
    show hannah casual_cu angry_cu at hannah_cu behind lexi:
        xpos 775
    hj "You're unreal. You really don't think that you're in the wrong, do you?"

    lx "No, I don't. We didn't end things amicably and I wasn't about to be your prison pen pal."
    hide lexi
    hide hannah
    show hannah casual_cu angry_cu at hannah_cu
    "Hannah grits her teeth before she turns her attention to me."

    "I defensively put my hands up in front of me to show it's not my fight."
    hide hannah
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Great now, now she's trying to drag me into this.)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3
    show hannah casual sad at right3
    "She ignores my gesture and lowers the volume of her voice, trying to come off as helpless and wounded."

    hj "Do you see? She doesn't give a damn about what she did to me! Do you really think you'll be any different?!"
    hide hannah
    hide mscmc
    $menuhideborder = True
    menu lexis1e5c1:
        "A. It's the same story from you every time...":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show hannah casual sad at right3
            "I feel a snap in the back of my mind and any patience I had with Hannah evaporates."

            mclexi "It’s the same story every time I see you."
            show hannah casual angry
            hj "Why are you-?! I just-!"

            "She doesn’t finish her words but instead raises her white knuckled clenched fist in the air..."

            "Before throwing her fists down at her sides and stomping her foot."


        "B. This is between the two of you.":
            $menuhideborder = False
            show mscmc jacket_hairdown angry at left3
            show hannah casual sad at right3
            mclexi "This isn't about me. Hannah. This is between the two of you."
            show hannah casual angry
            hj "I'm trying to help you! Why don't you understand that?!"
            hide mscmc
            hide hannah
            show hannah casual_cu sad_cu at hannah_cu
            "Hannah's brow furrows and her eyes sink in desperation as she looks at me pleadingly."
            hide hannah
        "C. We're different.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left3
            show hannah casual sad at right3
            mclexi "I’m not you, Hannah. The relationship I have with Lexi is a different one."
            show hannah casual angry
            hj "You don’t know that!"

            "Hannah steps towards me with her arms out pleading for me to listen, but I edge away from her."
            hide mscmc
            show jerry casual angry at left3
            "At the same time, Jerry puts his hand out in front of me as a warning to Hannah."
    hide jerry
    hide mscmc
    hide hannah
    show hannah casual_cu angry_cu at hannah_cu
    hj "You know what?! I've had it. This is your last chance, Sweetwater."
    hide hannah
    show mscmc jacket_hairdown surprised at left3
    show lexi casual surprised at right3
    "Lexi and I exchange glances."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Last chance for what? To apologize to her?)"
    hide mscmc
    show lexi casual angry at left3
    show hannah casual angry at right3
    lx "I genuinely have no idea what you're talking about."

    hj "Fine. If that's how it's going to be... you're going to regret this."
    hide hannah
    hide lexi
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Now she's making threats. She's acting so irrational!)"
    show mscmc jacket_hairdown_cu sad_cu
    "(If she'd just calm down and talk it out maybe we could come to an understanding.)"
    hide mscmc
    show jerry casual angry at left3
    show hannah casual angry at right3
    jr "I think that's about enough. I've been silent while you all hashed it out, but you're not going to threaten people here."

    jr "I think it's time for you to go."
    show hannah casual sad
    "Hannah looks at Jerry like he's her next target, but after sizing him up seems to think better of it."
    hide hannah
    hide jerry
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Good choice, Hannah. Jerry's a nice guy, but that's not a fight you'd win.)"
    hide mscmc
    show jerry casual angry at left3
    show hannah casual angry at right3
    hj "I was just leaving anyway. I have no interest in a place that serves trash like her."
    hide hannah
    hide jerry
    show hannah casual_cu angry_cu at hannah_cu
    hj "I gave you a chance, Sweetwater. Everything that happens now, you brought on yourself."
    hide hannah
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Lexi hasn't even done anything.)"
    stop music fadeout 1.0
    play music mscmctheme
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show lexi casual angry at right3
    mclexi "Wow, Hannah really is... something."
    show lexi casual basic
    "Lexi shrugs and leans back against the bar."

    lx "She's something alright. Don't let her get to you. People like that just like to cause trouble for no reason."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Maybe. But I wish I knew more about what happened.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show lexi casual smile at right3
    lx "What I'm more interested in is the reaction you had to the orb. I really want to see you interact with it more."

    lx "What if you touched it? Who knows what would happen."
    show mscmc jacket_hairdown smile
    mclexi "They'll be closed by the time we get over there if we leave now. Why don't we go tomorrow?"

    "Lexi chuckles and shakes her head."
    show lexi casual sad
    lx "That would be... So, fun fact, I might be on a watchlist at that museum."
    show mscmc jacket_hairdown surprised
    mclexi "A watch list? What the hell does that mean?!"

    lx "So back in the day, when I was still a nobody at treasure hunting, I had the bright idea to try and steal a jewel from that museum."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Treasure hunting, treasure stealing, close enough I guess.)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3
    show lexi casual sad at right3
    mclexi "If you're banned, what do we do?"
    show lexi casual bigsmile
    "Lexi grins devilishly at me and sits up excitedly."

    lx "We break in! It'll be fun!"
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(An intrusive thought about Lexi abandoning Hannah flashes through my mind. I don't think Lexi would do that to me.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show lexi casual bigsmile at right3
    mclexi "Are you sure there's no other way?"
    show lexi casual angry
    "Lexi furrows her brow and looks off into space as she thinks for a moment."
    show lexi casual smile
    lx "No. I'm pretty sure it's our only option."
    show mscmc jacket_hairdown sleep
    "I sigh reluctantly and rub the bridge of my nose."
    show lexi casual sad
    lx "You're thinking about Hannah, aren't you?"
    show mscmc jacket_hairdown surprised
    mclexi "I..."
    show lexi casual sad behind mscmc:
        easein 0.4 xoffset -200
    "Before I can answer Lexi cups my face in her hands."
    hide lexi
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "I'm not going to bail on you like I did Hannah. It's different with us."

    "She strokes my cheek with her thumb and I lean my face into her hand."
    hide lexi
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mclexi "Promise?"
    hide mscmc
    show mscmc jacket_hairdown sad at left1
    show lexi casual bigsmile at centre behind mscmc
    "Lexi lets my face go and jumps to her feet with a reassuring smile on her face."

    lx "On my honor as a treasure hunter, I promise."
    show mscmc jacket_hairdown smile
    "I stifle back a laugh as she raises her hand in the air declaratively and looks to the sky."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I'll just have to trust her. She hasn't given me any reason to doubt her, so I'm sure it will be fine.)"
    show mscmc jacket_hairdown grin at left1
    show lexi casual bigsmile at centre behind mscmc
    mclexi "Okay. Let's do this."
    scene bg msc_siren_park_night at bg with wiperight
    stop music fadeout 1.0
    play music mscsuspense
    "We stand on the museum's park grounds in the early hours of the morning."
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(I can't believe I'm doing this.)"
    show mscmc jacket_hairup basic at left3
    show lexi casual smile at right3
    lx "I love old architecture."

    "She looks lovingly at the old stately-looking building before forming a rectangle with her fingers like she's framing it."

    lx "Modern buildings are so... blocky. I get that it's more efficient, but they're so forgettable."
    show mscmc jacket_hairup surprised
    mclexi "Is it going to make it harder to sneak in?"
    show mscmc jacket_hairup sleep
    "I take a deep breath to steady my nerves as I contemplate the danger of what we're planning."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(This is crazy! My heart is pounding just thinking about it.)"
    show mscmc jacket_hairup_cu surprised_cu
    "(I would never do stuff like this if it weren't for Lexi. But I'm okay with it for some reason?)"
    show mscmc jacket_hairup_cu smile_cu
    "(The danger of it... this inexplicable thrill, I really do feel so present with her... I could get used to this.)"
    show mscmc jacket_hairup basic at left3
    show lexi casual smile at right3
    lx "The modern art museum I broke into a few years ago was a massive pain..."

    lx "But an old one like this will probably still rely mostly on analog locks and maybe some cameras."
    show mscmc jacket_hairup smile
    mclexi "Well that's good news at least. What do I need to do?"
    show lexi casual bigsmile
    "Lexi grins mischievously and eyes me up and down."

    lx "You just have to do whatever I say."
    show mscmc jacket_hairup grin
    "I can't stop myself from smirking."

    mclexi "Everything?"

    "I raise my eyebrows suggestively."
    show lexi casual smile
    lx "Everything."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(It was a joke, but I mean I'm not opposed to it...)"
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    lx "So here's the real question. Do you want to break in with me or should I go by myself and open the back door for you from the inside?"

    lx "I know you're curious what it will be like. Break in with me!"
    hide lexi
    $menuhideborder = True
    menu lexis1e5c2:
        "A. Take Lexi's hand and go with her!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairup grin at left3
            show lexi casual bigsmile at right3
            mclexi "I’m ready."
            hide mscmc
            hide lexi
            "I take Lexi’s hand and she starts walking us leisurely down the side path along the museum building."
            show mscmc jacket_hairup basic at left1
            show lexi casual angry at right1 behind mscmc
            lx "Okay, so the first thing we need to do is circle and look for cameras."

            "She swings our hands back and forth as we walk, inconspicuously looking up every once in a while for cameras."
            show mscmc jacket_hairup surprised
            mclexi "What if someone sees us?"
            show lexi casual smile
            lx "It’s no problem. We’re just two lovers walking around enjoying the atmosphere."
            hide lexi
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "I stumble back as Lexi pushes me into the wall and leans her face in next to mine, pressing our cheeks together."
            hide lexi
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(She’s so close and she just said we were masquerading as lovers. I wonder how far she’ll take this.)"
            hide mscmc
            "Her breath tickles my neck as her soft chest presses against me and I can feel my body start to tingle with excitement."

            "I place my hands on her slender waist and I can feel her inhale deeply at my touch."

            "The sound of her startled breath in my ears sends a shiver down my spine and it takes Lexi a moment to compose herself."

            "When she steadies her breathing, she whispers gently in my ear."
            show lexi casual_cu smile_cu at lexi_cu
            lx "Look up, over there in the corner."
            hide lexi
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "I glance past Lexi, doing my best to ignore the tight, excited feeling in my chest."
            show mscmc jacket_hairup_cu angry_cu
            "At the corner of the building is a camera pointed down the sidewalk..."
            show mscmc jacket_hairup_cu surprised_cu
            "...but even my inexperienced eyes can tell that it has a blind spot by a window a bit further down the wall."

            mclexi "The camera, right? How do we get over to the window without-?"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi breathes gently into my ear and pins my hands against the wall on either side of my head."

            lx "Everything I say, remember?"
            hide lexi
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "My knees tremble at her whisper and I nod attentively."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Good. Now I want you to take charge and get us over there."
            hide lexi
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Take charge? How does… She’s the one holding me against the wall and...)"

            "The hidden message behind Lexi’s words dawns on me."
            show mscmc jacket_hairup_cu smile_cu
            "(If a couple on a walk were to suddenly get hot and heavy… I can push Lexi over there like I’m going to kiss her.)"

            "(Then if we get caught on camera it’ll just look like we’re making out.)"
            hide mscmc
            "Without giving her any warning, I push off against the wall and shove Lexi back a little."

            "At the same time, I grab her shirt and pull her body against mine."
            show lexi casual_cu surprised_cu at lexi_cu
            "Her eyes widen in surprise at my aggressiveness and I roll with the moment, sliding my hands down her torso into the back pockets of her shorts."
            hide lexi
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Maybe the plan can wait and we can just… No, I need to focus.)"
            hide mscmc
            "I take a few steps forward and push the two of us under the window, cushioning Lexi as we run into the wall."
            show lexi casual_cu smile_cu at lexi_cu
            lx "Good girl."

            "She whispers the words into my ear sending a jolt of excitement through my body and making my knees tremble."

            lx "Okay, now let’s open this window up and get inside."
            hide lexi
            show mscmc jacket_hairup basic at left3
            show lexi casual basic at right3
            "Lexi steps away from me, making my heart sink a little, and starts to examine the window."

            lx "Okay, give me a boost."
            show mscmc jacket_hairup surprised
            show lexi casual smile
            mclexi "You’re just going to open it? What if there’s an alarm?"

            "Lexi smirks confidently at me."

            lx "Just trust me."
            hide lexi
            hide mscmc
            show mscmc jacket_hairup_cu smile_cu at mscmc_cu
            "(Just do everything she says, right? Honestly, I don’t mind it.)"
            hide mscmc
            show mscmc jacket_hairup smile at left3
            show lexi casual smile at right3
            lx "Get on your knee."
            show mscmc jacket_hairup smile:
                easein 0.4 yoffset +90
            "Lexi’s voice is firm and assertive and I immediately obey her command."

            lx "Good."
            show lexi casual bigsmile
            "There’s a hint of amusement in her voice and her lips curls into a smug grin."

            lx "Now interlock your fingers and boost me up."
            show lexi casual bigsmile:
                easein 0.4 xoffset -170
            "I interlock my hands for Lexi to stand on."
            show lexi casual bigsmile:
                easein 0.4 xoffset -300
            pause
            show mscmc jacket_hairup angry:
                easein 0.4 yoffset +50
            show lexi casual bigsmile:
                easein 0.4 yoffset -50
            "Her boots press hard on the palm of my hand, sending a dull pain through it that I try to ignore as I raise her up."
            hide lexi
            hide mscmc
            "It takes a minute, but Lexi gets the window open and I help push her through by pressing on her firm thighs."
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(She’s so light. This is so much easier than it was pulling her up the stairs to the apartment six months ago. Her tail was so heavy.)"
            hide mscmc
            "A few seconds pass before Lexi leans back out of the window and holds her hand out to help me up."

            "I grab her hand firmly and jump as she pulls me. And with some effort, we get me up to the windowsill."
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(That was easier than I thought it’d be. I’m pretty good at-.)"
            scene bg msc_museum_displays_night at bg with wiperight
            show lexi casual_cu surprised_cu at lexi_cu
            "Halfway through the window, I lose my balance and tumble forward onto Lexi, pinning her underneath me."
            hide lexi
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(That was so loud! We’re going to get caught because of me!)"
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            "But the museum seems empty and quiet, and Lexi bursts out laughing underneath me."

            lx "We should get going?"
            hide lexi
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "I blush and stand up before offering my hand to Lexi."
            show mscmc jacket_hairup_cu surprised_cu
            mclexi "How did you know there wasn’t an alarm?"
            hide mscmc
            show mscmc jacket_hairup surprised at left1
            show lexi casual smile at right1 behind mscmc
            "Lexi takes my hand firmly and stands as she points to the windowsill. I notice several cigarette butts scattered around it."

            lx "There were butts outside the windows on the ground too."

            lx "I figured this was where the guards take breaks when they’re too lazy to go outside."
            show mscmc jacket_hairup smile
            mclexi "Ok, I’m into you in work mode."
            show lexi casual bigsmile
            "Lexi grins proudly."

            lx "Tricks of the trade. Where’s the orb in this place?"

        "B. It's too risky.":
            $menuhideborder = False

            mclexi "It's too risky. I don't want to mess up and get us caught."

            "Lexi looks down disappointed, but then shrugs it off with a smile."

            lx "Okay, then just head around back and I'll open the door for you."

            "Without giving me a chance to respond, Lexi disappears into the night."

            "About half an hour passes as I lean against the wall by the back door of the museum waiting for Lexi."

            "(It's taking her a long time. What do I do if she gets caught?)"

            "Suddenly, the heavy metal door next to me bursts open and I jump back, my heart pounding violently in my chest."

            "Lexi pokes her head out of the doorway, her lip curled to the side in a sly grin."

            lx "Did I scare you?"

            mclexi "You busted out like that on purpose."

            lx "Yep! Now, let's go!"
    scene bg msc_museum_displays_night at bg with wiperight
    "I guide Lexi to the room where the orb is displayed."
    show mscmc jacket_hairup sad at left3
    show lexi casual basic at right3
    "I tried to be sneaky and stick to the shadows..."
    show lexi casual bigsmile
    "But Lexi let out an amused hearty laugh that echoed through the empty hall and strolled past me."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu smile_cu at mscmc_cu
    "(I hope her laugh doesn't alert the guards. She knows what she's doing, though, so I'm sure it's fine.)"
    show mscmc jacket_hairup basic at left3
    show lexi casual basic at right3
    mclexi "There it is."

    "I point across the room and as soon as my eyes settle on the orb."
    show mscmc jacket_hairup sad
    "I feel a longing sensation course through my body, as if I'm searching for a part of me I didn't know I was missing."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(That's a different feeling from the last time. Every time I'm near the orb it's a new feeling...)"
    hide mscmc
    show mscmc jacket_hairup sad at left3:
        easein 0.4 xoffset +30
    show lexi casual basic at right3:
        easein 0.4 xoffset -30
    "We stand in front of it, and Lexi scans it over, inquisitively."

    "Her long green hair cascades over her shoulder, shining in the bright museum lights and exposing her tanned neck."
    show lexi casual angry
    "She brings her thumb and index finger to her chin and strokes it thoughtfully as she squints at the orb."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(I love that studious look on her.)"

    "(She's always doing crazy adrenaline-fueled things, but at the end of the day she's just a history nerd.)"

    "(That contrast is what makes her so special.)"
    hide mscmc
    show mscmc jacket_hairup basic at left3:
        xoffset +30
    show lexi casual angry at right3:
        xoffset -30
    lx "It's beautiful. As elegant as I remember. The markings should be significant..."

    lx "But I don't recognize them at all. I might have a book though..."

    lx "And it still doesn't explain..."
    stop music fadeout 1.0
    play music mscmcvisionvoice
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "Suddenly, I hear faint chanting, as if a beautiful chorus is getting closer and closer."
    hide mscmc
    "Lexi's voice starts to fade away."
    scene bg msc_mcs_vision at bg with dissolve
    "Before I know it, I'm drifting underwater and I can't quite remember what I was just doing."
    show mscmc jacket_hairup_cu smile_cu at mscmc_cu
    "(I was with Lexi, maybe? But this is nice. I like being underwater like this.)"

    "(It's nostalgic.)"
    hide mscmc
    "But then the music is fading, as is the reality of the ocean depths around me."
    stop music fadeout 1.0
    play music mscmagicartifact
    scene bg msc_museum_displays_night at bg with eye_open_slow
    show lexi casual_cu sad_cu at lexi_cu
    "Suddenly, I find myself half-laying in Lexi's lap on the museum floor."
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(She's looking into my eyes with concern, she must've caught me, which means I must've fainted!)"

    mclexi "How long was I out?"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "Maybe ten seconds."
    show lexi casual_cu surprised_cu
    "Lexi's look of concern changes to one of excited interest after hearing me speak normally."

    lx "But whats really interesting is."
    hide lexi
    "She points at the orb and its pattern is moving!"

    "The intricate lines ebb and flow across its surface."
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Oh man, we woke it up.)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1
    show lexi casual smile at right1 behind mscmc
    lx "Whatever happened just activated it. So, whatever happens next should be good."

    lx "In conclusion, you are connected to the orb somehow and it's causing your visions. But... it also gets excited around you."

    "Lexi shoots me a flirty glance."
    show mscmc jacket_hairup embarrassed
    mclexi "It doesn't make sense that an old mer object and I are affecting each other, I'm a hum..."
    show mscmc jacket_hairup angry
    show lexi casual angry
    "Lexi and I whip our heads around as a loud gasp flls the exhibit hall."
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu
    "(Hannah!? Are you kidding me right now! When is this woman not here?)"
    stop music fadeout 1.0
    play music mscantagonist
    hide mscmc
    show lexi casual angry at left3
    show hannah casual angry at right3
    "Lexi puts her hands on her hips and adopts a power pose as she stares Hannah down."
    hide lexi
    hide hannah
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu
    "(She really knows how to keep her cool in the face of the unexpected. Actually, no, it checks out that she kind of thrives on chaos.)"
    hide mscmc
    show lexi casual angry at left3
    show hannah casual angry at right3
    lx "Oh, look who it is. So all that talk about me stealing this orb was just a front so you could take it and frame me?"

    lx "I get it now, I see the plan."

    lx "But why drag [genericfn] into all this?"
    show hannah casual smile
    "Hannah chuckles softly and puts her hand on her hip."

    hj "Me? You're the one that brought her here. I only wanted to steal the orb and have you take the fall."

    hj "But it seems that I was right about you trying to steal the orb for yourself."
    show hannah casual angry
    hj "[genericfn] tried to convince me you'd changed, but I guess in the end you're still the same person that left me to rot."

    $menuhideborder = True
    menu lexis1e5c3:
        "A. Why is revenge so important to you?":
            $menuhideborder = False
            show mscmc jacket_hairup angry at left3
            show hannah casual angry at right3
            mclexi "Why is getting back at Lexi so important to you?"
            show hannah casual smile
            "Hannah’s cheek twitches slightly and her face bunches up in a grimace."

            hj "She betrayed and abandoned me. I only want her to get what she deserves. What’s so wrong with that?"


        "B. Why do you want the orb?":
            $menuhideborder = False
            show mscmc jacket_hairup angry at left3
            show hannah casual angry at right3
            mclexi "Are you really just stealing the orb to pin it on Lexi?"
            show hannah casual sad
            "Hannah shakes her head and sighs heavily."

            hj "Pinning the theft on Lexi is my main goal, but I won’t deny that I’m planning on selling the orb for cash, too."

            hj "It’s not exactly easy to make money when you’ve been locked up for five years."

        "C. We're not trying to steal the orb.":
            $menuhideborder = False

            mclexi "We're not here to steal the orb. We just needed to look at it."

            "Hannah chuckles softly to herself and fans her face with her hand sarcastically."

            hj "And I'm the queen of England!"

            hj "Seems strange that you'd need to break into the museum in the middle of the night just to look at an exhibit."
    hide lexi
    hide mscmc
    hide hannah
    show lexi casual basic at left3
    show hannah casual angry at right3
    lx "So now what, Hannah? We've clearly interrupted your plan."
    show hannah casual basic
    "Hannah looks past us at the orb and shrugs."

    hj "My plans haven't changed. Unless you plan on stopping me..."
    hide lexi
    hide hannah
    show lexi casual_cu basic_cu at lexi_cu
    "My shoulders tense at Hannah's challenge and I look at Lexi."

    "To my surprise her body is completely relaxed and she's twirling the ends of her hair around her finger."
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(We're in a bad spot. Why is Lexi not worried? She must have a plan.)"
    show mscmc jacket_hairup_cu angry_cu
    "I feel my chest start tighten as the standoff drags on and my hands start to shake."
    hide mscmc
    show lexi casual_cu basic_cu at lexi_cu
    "Lexi suddenly slips her fingers through mine and holds onto my hand."
    show lexi casual_cu smile_cu
    "She squeezes reassuringly and raises her eyebrows at me, silently telling me that everything will be okay."
    hide lexi
    show lexi casual basic at left3
    show hannah casual basic at right3
    lx "I'm not just going to let you steal the orb."
    show lexi casual smile
    lx "Neither of us want to get caught tonight, maybe we just all walk away this time and try again another day, huh?"
    show hannah casual angry
    "Hannah's lips pull back into a sneer."

    hj "As if you wouldn't just take the loot when I walked away. I'm not going to fall for any of your tricks, Sweetwater."
    hide lexi
    show mscmc jacket_hairup surprised at left3
    hj "What about you, [genericfn]? Do you really trust Lexi?"
    hide mscmc
    hide hannah
    show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
    "I squeeze Lexi's hand firmly, gently rubbing her thumb with mine and take a deep breath."
    show mscmc jacket_hairup_cu angry_cu
    "(I don't know if I can completely trust Lexi. But if Hannah doesn't back off, we're all going to be in trouble.)"
    hide mscmc
    show mscmc jacket_hairup angry at left3
    show hannah casual angry at right3
    mclexi "None of us want to get caught, Hannah. Let's just do what Lexi says and leave before-!"
    #seen needs to become the color red due to alarm
    scene bg msc_museum_displays_night at bg, red_tint
    show mscmc jacket_hairup surprised at left3, red_tint
    show hannah casual sad at right3, red_tint
    "As if on queue, an alarm blares through the museum hSall and all three of us stare at each other, wide eyed."
    hide mscmc
    hide hannah
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu, red_tint
    "(Shit! We need to get out of here!)"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu, red_tint
    "Lexi's grip tightens on my hand to the point it hurts and I can tell by her stiff shoulders and clenched jaw that we're in trouble."
    hide lexi
    show lexi casual angry at left3, red_tint
    show hannah casual sad at right3, red_tint
    lx "What did you do, Hannah?!"
    show hannah casual angry
    "Hannah's eyes dart around the room in a panic as several yells can be heard over the alarm."

    hj "Me?! I didn't-!"

    "She's so flustered she doesn't finish her sentence."
    hide lexi
    hide hannah
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu, red_tint
    "(We don't have time for this! We need to leave, now!)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
