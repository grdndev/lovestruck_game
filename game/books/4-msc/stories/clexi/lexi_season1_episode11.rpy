label lexi_season1_episode11:

    $tbc = False
    scene bg msc_siren_park_night at bg
    play music mscsuspense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "Stepping onto the museum grounds, a whole flurry of emotions dance in the pit of my stomach. Excitement, nervousness, doubt..."
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(We're really doing this. Can we really do this?)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "I look at Lexi, whose eyes are trained ahead at the museum building. She's got that focused furrow to her brow, but she's smiling."

    "My doubt melts away. She wouldn't have brought me here if she wasn't sure."
    hide lexi
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu
    "(Yeah, we got this.)"
    hide mscmc
    show mscmc jacket_hairup surprised at left2
    show lexi casual basic at right2
    lx "So, there's just one little hiccup in this whole plan—but we can totally handle it."

    lx "Before we go in though..."
    show lexi casual angry
    "She looks me in the eye, her expression suddenly serious. I don't know what to expect."
    show lexi casual basic
    lx "I've got some tricks of the trade to teach you. If you're up for it."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(She's going to teach me...)"
    hide mscmc
    show mscmc jacket_hairup smile at left2
    show lexi casual bigsmile at right2
    mclexi "I promise I'll only use your gifts of knowledge for good."
    show mscmc jacket_hairup grin
    "Lexi cracks up; I feel proud for dispelling any concerned look from her face."
    show mscmc jacket_hairup smile
    show lexi casual smile
    lx "Eh, morally gray is good enough."
    show mscmc jacket_hairup embarrassed
    show lexi casual smile:
        easein 0.4 xoffset 100
    "She beckons me across the grounds to the side of the museum, then opens up an electrical panel built into the wall."
    show mscmc jacket_hairup surprised:
        easein 0.4 xoffset 100
    "I peer inside, trying to make sense of all the differently colored wires and switches."

    mclexi "Is this the alarm system?"
    show mscmc jacket_hairup embarrassed
    lx "And the site of my lesson in mischief for you."
    show mscmc jacket_hairup grin
    "Excitement swells in me."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(All right, disarming a security system! Let's do this.)"
    hide mscmc
    show mscmc jacket_hairup grin at right1 behind lexi
    show lexi casual basic at right3
    show mscmc jacket_hairup surprised at left2:
        xoffset 100

    "Before I can so much as lift my hands though, Lexi puts one of hers on top of mine. That flicker of seriousness reappears behind her eyes."

    lx "Listen, a system like this isn't going to be as simple as breaking the box and calling it a day. This is...not easy."
    show lexi casual embarrassed
    stop music fadeout 1.0
    play music mscromanceconfession
    lx "If you're going to pass my test, you'll have to do everything exactly as I say. Can you follow my every command?"
    hide lexi
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "She lifts my hand to the panel, as she steps behind me. My breath catches, feeling her breath against my neck as she leans close."
    show lexi casual_cu smile_cu
    lx "Can you be a good girl and do that for me?"
    hide lexi
    $menuhideborder = True
    menu lexis1e11c1:
        "A. Try to be very, very obedient for Lexi."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
            "I steady my breath and nod."
            show mscmc jacket_hairup_cu embarrassed_cu
            mclexi "I can be good. I can be very good."
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "Lexi’s soft sigh of laughter brushes across my skin, thrilling and hot."
            show lexi casual_cu smile_cu
            lx "Good. Now, listen closely..."
            hide lexi
            "As Lexi instructs me, I carefully begin to snip wires inside the panel."

            "It’s nerve-wrecking at first, but each time I cut a wire without incident, I feel a sense of pride, and Lexi’s hands."
            show lexi casual_cu smile_cu at lexi_cu
            "All the while, Lexi’s voice whispers to me. Commands, mostly, but interspersed with praise and rewards."
            hide lexi
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "I gasp softly as her lips press against my neck, her hands low on my waist and toying with the edge of my shirt."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Cut that blue wire next."

            "I move to do so, but Lexi’s fingers continue playing with my shirt and teasing the skin just beneath it."
            hide lexi
            "I close my eyes and take a breath, trying to concentrate. In the cool night air though, Lexi feels so hot and alive..."
            show lexi casual_cu smile_cu at lexi_cu
            "Then all of a sudden, she withdraws her hands. The loss of her touch is almost sharp, like a papercut."

            lx "I didn’t say to stop. Didn’t you say you could behave for me?"
            hide lexi
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(The authority in her voice is thrilling; my mouth is going dry!)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "I said, cut the blue wire."
            show lexi casual_cu embarrassed_cu
            "I do as she says. When the wire separates, I feel Lexi’s lips smile against my skin. Her hands return, their warmth an exciting relief."

            lx "Good. Next, cross it with the green..."
            hide lexi
            "For all her displays of control, I start to figure out how she only touches and teases me when I’m not at risk of cutting the wrong wire."

            "Her hands are as deft as her commands, fingers stroking my waist, then up my spine, back down my arms again..."
            show lexi casual_cu smile_cu at lexi_cu
            lx "That’s my good girl."
            show lexi casual_cu embarrassed_cu
            "She whispers it against my ear, her voice wispy and hot. It takes all my willpower not to lean back into her, craving her the way I do."

            "Her lips trail down my neck—but she stops midway..."
            show lexi casual_cu surprised_cu
            lx "Did you hear something?"
            hide lexi
            show mscmc jacket_hairup_cu basic_cu at mscmc_cu
            "I focus through the blood rushing in my ears looking around, but I don’t see or hear anything that’s cause for alarm."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Then Lexi laughs, her voice darkening with the tone of a reprimand."

            lx "Ah-ah, you broke the rules, I didn’t say to stop."
            hide lexi
            show mscmc jacket_hairup_cu sad_cu at mscmc_cu
            "Realizing the ruse for what it is, I cast a playful pout over my shoulder."
            show mscmc jacket_hairup_cu embarrassed_cu
            mclexi "That was a dirty trick."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Oh no, I know tricks much dirtier than that."
            show lexi casual_cu embarrassed_cu
            "She leans in and kisses the corner of my mouth, dispelling a bit of my sourness."
            show lexi casual_cu smile_cu
            lx "Now focus. Take that wire there and cross it with the red one you cut earlier…"
            hide lexi
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "I do so, and jump a bit when some lights inside the panel flash and then go dead."
            show mscmc jacket_hairup_cu grin_cu
            mclexi "Okay, what’s next?"
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            lx "Nothing. You’re all done."
            hide lexi
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(Oh, thank god, I did it without setting off the alarm.)"
            hide mscmc
            "Lexi draws away again and the nighttime chill rushes in to meet me."
            show lexi casual_cu smile_cu at lexi_cu
            "When I turn around, she’s grinning at me."

            lx "Excellent work. You’re a very good listener."

            lx "Maybe in the future, we’ll see how well you follow instructions under different circumstances..."

            "She taps her lip with a finger, but all I can do is stand there and blush."
            hide lexi
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            mclexi "Do with me what you will."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Oh, I will."
            hide lexi
            "She leans in and kisses me, her strength causing me to stumble and press my back to the wall. I’m thrilled by her neediness."
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(Glad I’m not the only one worked up...)"
            hide mscmc
            show mscmc jacket_hairup embarrassed at left3
            show lexi casual smile at right2
            "She breaks away with a mischievous laugh. I go to playfully swat her but she’s too fast, dancing out of my reach with a smirk."

            lx "Good girls are patient, you know."
            hide lexi
            hide mscmc
            show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
            "(Well played, Lexi.)"
            hide mscmc
            "It’s strange; I couldn’t feel the electricity running though the panel when it was active, but now the museum grounds feel just a little quieter."
            show mscmc jacket_hairup_cu smile_cu at mscmc_cu
            "(Or maybe that’s my overwhelming relief that we don’t have to worry about the alarms anymore...)"

        "B. You can't! Your hands are shaking!":
            $menuhideborder = False
            show lexi casual_cu smile_cu at lexi_cu
            "I can see the flirtatious look in her eye, but all I feel is the color drain from my face."
            hide lexi
            show mscmc jacket_hairup surprised at right1 behind lexi
            show lexi casual smile at right3
            mclexi "Um—no? My hands are trembling—if I get one thing wrong, we'll be in hot water!"
            show lexi casual bigsmile
            "Lexi laughs, but there's a stiffness to it. I can tell she's a bit disappointed, even if she hides it well."

            lx "Fine, fine, I'll handle it."
            hide mscmc
            hide lexi
            "It's strange; I couldn't feel the electricity running through the panel when it was active, but now the museum grounds feels just a little quieter."
            show mscmc jacket_hairup_cu smile_cu at mscmc_cu
            "(Or maybe that's my overwhelming relief that we don't have to worry about the alarms anymore...)"
    hide mscmc
    show mscmc jacket_hairup smile at left3
    show lexi casual bigsmile at right2
    stop music fadeout 1.0
    play music mscloveinterest
    lx "Now that that's out of the way... Let's go."
    hide lexi
    hide mscmc
    show lexi casual basic at centre
    "Lexi moves around the building with a gracefulness like water and the intensity of a panther on the prowl."

    "She plucks a lockpick out of her pocket, twirling it around her fingers before positioning it in the lock of the museum's side door."

    "She's not just powerful, she's dextrous—I can't help but admire how she can go from bold strides to careful maneuvers."
    hide lexi
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(I'll never get tired of her confidence and grace.)"
    hide mscmc
    show lexi casual angry at centre
    "I'm not much help standing here waiting for the lock to give way, but I keep an eye out for guards."
    show mscmc jacket_hairup smile at right2
    show lexi casual angry at left2
    lx "I've almost got it. Stay close to me when we head in, okay?"

    mclexi "You don't have to tell me twice."
    show lexi casual smile
    lx "Tsk, charmer."

    "I hear a big click, and Lexi's whispered 'yes' as the lock gives."
    hide lexi
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    "She pushes the door open, at first careful, then with a grandiose sweep of the arm and a grin my way."
    show lexi casual_cu smile_cu
    lx "We're in."
    scene bg msc_museum_displays_night at bg with wiperight
    stop music fadeout 1.0
    play music msctense
    "I have to squint through the darkness of the unlit museum."
    show mscmc jacket_hairup surprised at left1 behind lexi
    show lexi casual basic at right1
    "Then I see it—the orb! In my excitement I start to move towards it, but Lexi's arm shoots out in front of me, blocking my path."
    show lexi casual smile
    lx "Hold your seahorses a sec. This won't be as easy as it looks."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Right—security traps.)"
    show mscmc jacket_hairup surprised at left1 behind lexi
    show lexi casual angry at right1
    "Lexi pulls out a makeup compact from her back pocket and flicks it open."
    show lexi casual smile
    "She blows powder out into the open hallway, and I marvel as dozens of red lasers light up before us."

    lx "Ugh, why does it always have to be lasers?"

    mclexi "Is there another panel we can disable, maybe?"

    lx "If there is, it won't be on this side of all this. Come on, follow me."
    show lexi casual bigsmile:
        easein 0.4 xoffset 600
    "I expect her to turn away from the lasers and go down a clear hallway or something, but instead she starts running straight for them!"

    mclexi "Wait-!"
    hide lexi
    hide mscmc
    show lexi casual smile at centre, step_in
    pause
    "Smooth as fluid, Lexi threads her lithe body through a gap in the lasers, and somersaults as she hits the ground on the other side."
    hide lexi
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(What the f-?!)"
    hide mscmc
    show lexi casual bigsmile at centre, out_left
    "I can see the rise of her chest as she takes a deep breath, and begins curving and winding her way through more of the lasers."
    hide lexi
    "Not a single muscle buckles or twitches as she works; it's mesmerizing."
    show lexi casual basic at centre, step_in
    "Like watching a gymnast jump and pirouette like it's nothing."
    hide lexi
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(Things I didn't know I needed in my life: Lexi doing impossibly cool, sexy things with her flexibility.)"
    hide mscmc
    show lexi casual basic at centre:
        easein 0.6 yoffset +50
    "She turns her back to the next set of lasers and bends backwards until her hands touch the floor..."
    show lexi casual basic:
        easein 0.6 xoffset +50

        easein 0.6 yoffset -15

    "Then kicks her legs up and through the other side."

    "Her skin glistens faintly with a trace of sweat, reflecting off the lasers as she makes her way through."
    hide lexi
    show lexi casual_cu smile_cu at lexi_cu
    "She ends her incredible display with a wink at me and I almost faint."
    hide lexi
    show mscmc jacket_hairup grin at left3
    show lexi casual embarrassed at right2
    mclexi "That was amazing!"
    show lexi casual bigsmile
    lx "It's nothing, really. Come on, you're up."
    show mscmc jacket_hairup surprised
    "It's like my brain shorts out for a second."

    mclexi "You want {i}me{/i} to do that?"
    show lexi casual sad
    "Lexi props her hands on her hips, pouting."

    lx "Are you my good girl or aren't you?"
    show lexi casual bigsmile
    "I stammer for a reply but Lexi laughs delightedly."
    show mscmc jacket_hairup sleep
    lx "I'm kidding."
    show lexi casual smile at right3
    "She reaches out to the wall, and flicks what I guess is a switch. The lasers all disappear."
    show mscmc jacket_hairup smile
    lx "I found the spot to disable them, by the way."
    show mscmc jacket_hairup grin
    "A laugh tumbles out of me, breathless."
    hide mscmc
    hide lexi
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(She is dangerous, but god is it fun.)"
    show mscmc jacket_hairup surprised at left1 behind lexi
    show lexi casual bigsmile at right1
    "I rejoin Lexi as she starts looking over the glass case that contains our prize. I'm caught off guard realizing how close to the orb I am."
    hide mscmc
    hide lexi
    show mscmc jacket_hairup_cu basic_cu at mscmc_cu
    "(I can see all the details, the way it shimmers—even the half-unlatched lock on the display case.)"

    "(I can't believe we're really in the home stretch.)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1 behind lexi
    show lexi casual bigsmile at right1
    lx "I've never seen anything like this, let alone lifted something like this. This is... amazing."
    show lexi casual surprised
    "Lexi's eyes are wide with curiosity and wonder as she stares at the orb."
    show mscmc jacket_hairup embarrassed
    "For all her showing off, I can tell moments like these are the real thrill for her."
    show lexi casual basic
    show mscmc jacket_hairup basic
    lx "How do you feel? Any visions?"

    mclexi "I'm okay. No visions yet."
    show mscmc jacket_hairup surprised
    show lexi casual smile
    mclexi "What are we going to do with it?"
    show mscmc jacket_hairup embarrassed
    show lexi casual bigsmile
    "Lexi grins, a look of genuine inspiration on her face. It's unexpected and gorgeous."
    show lexi casual smile
    lx "Well, for starters, we're going to figure out what you and an ancient mer artifact have to do with each other, and go from there."
    show mscmc jacket_hairup smile
    lx "I also have a pretty good hunch a contact of mine will be very interested in hearing about all this."

    "She reaches out to delicately open the door of the display case."
    show lexi casual sad
    "I spot a brief frown on her face, but she doesn't say anything, and the door gives without a fuss."
    show lexi casual basic
    stop music fadeout 1.0
    play music mscmcvisionvoice
    "I hold my breath as she picks up the orb, giving it a closer look. I can't help but reach out and touch it; it's cool and smooth."

    "The sound of someone speaking brushes my senses. I try to focus on what's being said, but I can't quite make it out..."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
    "(It sounds old... and very beautiful.)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1 behind lexi
    show lexi casual basic at right1
    "Remembering myself, I withdraw my hand."

    "The voice disappears."
    show mscmc jacket_hairup basic
    stop music fadeout 1.0
    play music mscsadtimes
    "I look sharply at Lexi, but I'm struggling to get words out of my mouth."
    show mscmc jacket_hairup surprised
    show lexi casual surprised
    lx "What?"

    mclexi "Did—didn't you hear that voice speaking just now?"
    show mscmc jacket_hairup sleep
    lx "No...?"
    show mscmc jacket_hairup sad
    mclexi "It was there just a second ago—it was saying...saying..."

    "I trail off, realizing from Lexi's bewildered expression she really must not have heard it. She gives the orb a curious look."
    show lexi casual basic
    lx "Interesting... How are you both connected, I wonder..."

    lx "Ugh, questions for later—don't touch it again until we're out of here, okay? We don't want you going into a vision trance just yet."
    show mscmc jacket_hairup basic
    "I drag my hand down my face, still a bit disoriented from what I heard."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Why could only I hear it? What does this artifact have to do with me...?)"
    hide mscmc
    show mscmc jacket_hairup sad at left1 behind lexi
    show lexi casual sad at right1
    lx "What did the voice say?"

    mclexi "I don't... I couldn't understand it, but..."
    show mscmc jacket_hairup surprised
    show lexi casual surprised
    mclexi "Wait, I remember one word, I think."

    mclexi "'Rementius'?"
    show mscmc jacket_hairup sad
    "Lexi stares at me, stunned into momentary silence. I start to feel nervous."

    mclexi "Do you know what it means?"
    show mscmc jacket_hairup surprised
    show lexi casual basic
    lx "It... it means 'remember' in a dead mer language. More or less, anyway—the meaning varies a little depending on context."
    show mscmc jacket_hairup basic
    show lexi casual surprised
    "She gives the orb another look over, more careful, even reverent this time."
    hide lexi
    hide mscmc
    show lexi casual_cu surprised_cu at lexi_cu
    lx "Could this artifact contain history or...or the memories of an ancient mer?"
    hide lexi
    show mscmc jacket_hairup sad at left1 behind lexi
    show lexi casual angry at right1
    "She goes quiet for a moment, contemplating."

    "I have no idea what she's thinking right now."
    show mscmc jacket_hairup surprised
    show lexi casual surprised
    lx "This orb is very, very powerful. More so than I imagined—and I already knew it was unlike anything I've tried to get my hands on before."
    hide lexi
    hide mscmc
    $menuhideborder = True
    menu lexis1e11c2:
        "A. What could it have to do with me?":
            $menuhideborder = False
            show mscmc jacket_hairup sad at left1 behind lexi
            show lexi casual angry at right1
            mclexi "What does something that powerful have to do with... a human? With me?"

            lx "I don't know. Clearly you are connected to it somehow, and whatever that reason is, I promise we'll figure this out."
            hide mscmc
            hide lexi
            show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
            "(This feels like a dream or something...)"
            hide mscmc

        "B. How did it wind up in a human museum?":
            $menuhideborder = False
            show mscmc jacket_hairup sad at left1 behind lexi
            show lexi casual angry at right1
            mclexi "How does an artifact like that wind up in a human museum though?"

            lx "I’ve been asking myself that ever since I found out about it."
            show lexi casual basic
            lx "But it obviously reacts to you, so maybe it was meant to find its way here all along…"


        "C. Could the memories be useful?":
            $menuhideborder = False
            show mscmc jacket_hairup surprised at left1 behind lexi
            show lexi casual angry at right1
            mclexi "Could the memories of whatever inside it be useful somehow?"
            show lexi casual smile
            lx "Maybe, you’re going to have to remember more words first."
            hide lexi
            hide mscmc
            show mscmc jacket_hairup_cu basic_cu at mscmc_cu
            "(True. Too bad I don’t speak any ancient mer...)"
            hide mscmc
    show mscmc jacket_hairup sad at left1 behind lexi
    show lexi casual basic at right1
    "The mystery of it all feels too big to me. The hallway feels more exposed than before, and I shudder."
    hide mscmc
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(I'm actually starting to get a bit freaked out.)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1 behind lexi
    show lexi casual smile at right1
    lx "One thing is for sure: for whatever reason, you're a piece of this puzzle too."
    show mscmc jacket_hairup sad
    mclexi "I just wish I had any idea what the puzzle was supposed to be..."

    "Lexi smiles, teasing, but a bit sympathetic too."
    show lexi casual embarrassed
    lx "Don't worry, you'll have me. We'll do this together, whatever 'this is'."
    show mscmc jacket_hairup smile
    "I sigh a little laugh."

    mclexi "Thanks, Lexi. Can you glean anything else from it?"

    "Lexi gives it another careful look, turning it gently in her hands. She's not afraid of it, but she definitely respects its power."
    show mscmc jacket_hairup basic
    show lexi casual basic
    lx "Not in this dark museum. We better..."
    hide mscmc with dissolve
    hide lexi with dissolve
    stop music fadeout 1.0
    play music mscsuspense2
    "I stop listening, but not on purpose--the hallway seems to suddenly spin and the floor almost comes out from under me."

    "I don't know what's going on at first. I think I'm falling for a second, until I'm pulled back and pinned against someone wiry and strong."
    show lexi casual_cu angry_cu at lexi_cu
    "Across from me, I see Lexi stiffen. Then a familiar woman's voice cuts through the air from behind my shoulder."
    hide lexi
    show mscmc jacket_hairup_cu angry_cu at mscmc_cu
    "(No way-!)"
    hide mscmc
    show hannah casual_cu angry_cu at hannah_cu
    "I throw my head back, but all I register is a gun in Hannah's free hand... trained on me."

    hj "Don't. Move."

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
