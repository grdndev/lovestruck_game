label lexi_season1_episode12:

    $tbc = False
    scene bg msc_museum_displays_night at bg
    play music mscsuspense2

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(That's a gun... That's a gun!)"
    show mscmc jacket_hairup_cu basic_cu
    "Panic sets in fast, but I fight it down as much as I can. I steel my jaw, and make sure my feet are centered underneath me."
    show mscmc jacket_hairup_cu sad_cu
    "(Don't make any sudden movements, [genericfn], just breathe.)"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    "Lexi is glaring daggers just past me at Hannah, who is gripping my arm with one hand and training her gun on me with the other."

    "Lexi doesn't lose her cool, but the way her nostrils flutter and fists clench shows a depth of anger I've never seen in her before."
    hide lexi
    show mscmc jacket_hairup sad at left1
    show hannah casual angry at left4 behind mscmc
    show lexi casual angry at right3
    lx "Let her go, Hannah. Now."
    show hannah casual smile
    hj "You're not in a position to be making demands this time."
    show hannah casual angry
    "I feel like I'm not in my own body right now; like somehow I'm watching this all unfold from the sideline."
    hide lexi
    hide mscmc
    hide hannah
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(It's like I'm being swallowed up in a riptide; powerless and scared.)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1
    show hannah casual angry at left4 behind mscmc
    show lexi casual angry at right3
    hj "Put the orb down slowly, and step away from it, Lexi. Then I'll let your crush go."
    show mscmc jacket_hairup sleep
    "Hannah just wants the orb because Lexi beat her to it and she can't let go of Lexi cutting ties with her."
    hide lexi
    hide mscmc
    hide hannah
    show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
    "(I know Lexi will choose me. I know she won't leave me high and dry. I have to believe that...)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "I watch as Lexi's eyes shift around the room, taking in the situation. She looks at Hannah, me, the orb, the exits..."
    hide lexi
    show mscmc jacket_hairup surprised at left1
    show hannah casual angry at left4 behind mscmc
    show lexi casual smile at right3
    "A terrifying thought strikes me."
    hide mscmc
    hide lexi
    hide hannah
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(She's not going to run with it, is she? No, she wouldn't leave me—would she?)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1
    show hannah casual angry at left4 behind mscmc
    show lexi casual smile at right3
    "I'm starting to feel lightheaded. I think I'm hyperventilating, but there's so much going on at once it's hard to focus on anything."
    show mscmc jacket_hairup sad
    hj "Stop dawdling, Lexi. If you try anything funny, your friend here won't be leaving this museum."
    hide mscmc
    hide lexi
    hide hannah
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Is Hannah really going to freakin' shoot me?!)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1
    show hannah casual basic at left4 behind mscmc
    show lexi casual angry at right3
    "Lexi's gaze settles on Hannah again, her glare sharp enough to cut."
    hide mscmc
    hide lexi
    hide hannah
    show mscmc jacket_hairup_cu sleep_cu at mscmc_cu
    "(Please, Lexi...)"
    hide mscmc
    show mscmc jacket_hairup surprised at left1
    show hannah casual basic at left4 behind mscmc
    show lexi casual smile at right3
    stop music fadeout 1.0
    play music msclexi
    lx "Fine, Hannah. Come and get it."
    #lexi animation of going down and up
    show lexi casual smile
    "Lexi lowers her hand and the orb like she's going to place it on the floor—but at the last minute she throws it high into the air."
    show hannah casual sad
    hj "Are you out of your-?!"
    hide lexi
    hide mscmc
    hide hannah
    stop music fadeout 1.0
    play music mscaction
    "Hannah pushes me to the floor out of her way as she lunges for the orb soaring through the air, just reaching the peak of its flight."
    show hannah casual angry at centre:
        easein 0.5 yoffset +70
    "I see Hannah dive for it as I feel strong, assuring hands grab onto my waist."
    hide hannah
    show lexi casual_cu smile_cu at lexi_cu
    lx "[genericfn]!"
    show lexi casual_cu embarrassed_cu
    "A hand grabs my cheek, warm and familiar. I'm pulled to look up at Lexi, staring back at me with a rattled expression."
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(What is that look in her eye? Has she ever looked at me like this? I feel like her eyes are lighting a fire inside me.)"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "Are you okay?"
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    mclexi "I... I..."
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "My mind starts to catch up again."

    "Lexi's touch feels amazing but I start to tremble and tears sting the back of my eyes."
    hide lexi
    show hannah casual angry at centre, step_out
    "Blinking them away, I barely spot Hannah disappearing down the hallway clutching the orb to her chest."
    hide hannah
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    mclexi "Wait, she's getting away-!"
    stop music fadeout 1.0
    play music mscromance
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "Screw her—{i}Are you hurt{/i}?"
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Lexi...)"
    show mscmc jacket_hairup_cu embarrassed_cu
    mclexi "N-no, no, I'm okay. Just shook up."
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    "Lexi finally lets out a breath she must have been holding. Her hand pushes my hair back behind my ear as she looks me over."
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    mclexi "But Hannah—she has the orb-!"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "She can keep it for all I care."
    hide lexi
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(She chose me over a priceless magic artifact... I knew she would.)"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "Come on, let's get out of here. Can you stand? Put your arm around me ..."
    hide lexi
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    mclexi "I—I'm okay, Lexi, really."
    show mscmc jacket_hairup_cu embarrassed_cu
    mclexi "Just... thank you."
    scene bg msc_siren_park_night at bg with wiperight
    "We get back outside, but Hannah is nowhere to be seen. She's long gone—and so is the orb."
    show mscmc jacket_hairup sad at left1
    show lexi casual basic at right1 behind mscmc
    "Lexi stays close to me in case I need the support, but my mind just keeps spinning around what happened."
    hide lexi
    hide mscmc
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(Lexi is mysterious and hard to read in a lot of ways, but... I feel like I can trust her, really trust her.)"
    hide mscmc
    show mscmc jacket_hairup smile at left1
    show lexi casual surprised at right1 behind mscmc
    mclexi "You saved me... Even though it meant giving up a piece of treasure."
    show lexi casual embarrassed
    "Lexi actually gets flustered, quickly turning her face away and hurrying out a response."
    show lexi casual smile
    lx "Of course I did—you don't have to make it sound like you thought I wouldn't."
    show mscmc jacket_hairup embarrassed
    mclexi "That's not it, I just..."
    show mscmc jacket_hairup sad
    show lexi casual surprised
    mclexi "When you hesitated, I just got scared..."
    show mscmc jacket_hairup smile
    show lexi casual sad
    "Lexi looks at me, concern peeking through her usually well-composed expression. I smile shakily."
    show lexi casual embarrassed
    mclexi "I've just never been so glad to have a fear proven wrong, that's all."
    show mscmc jacket_hairup embarrassed
    mclexi "Maybe the choice was obvious to you, but I know..."

    mclexi "It's just, trust is earned, you know? And you really earned some back there."
    show lexi casual smile
    "Lexi deflates a little, and belatedly sighs out a laugh. She takes my hand in hers; protective but gentle."

    lx "I hope one day you can trust me completely. Don't worry, I'll earn it."
    hide mscmc
    hide lexi
    show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
    "(I think she will.)"
    scene bg msc_night_lightson_uv at bg with clockwise_wipe
    stop music fadeout 1.0
    play music msclexiuv
    "The trip back to Lexi's UV is kind of a blur."
    show mscmc casual_hairdown smile at centre
    "I wouldn't believe it's already morning if I hadn't seen the sun come up as we swam out."
    show mscmc casual_hairdown sleep
    "I sit on the couch. The events of last night still feel a little unreal."
    hide mscmc
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(Thank god we're both safe. She saved me.)"
    show mscmc casual_hairdown_cu sad_cu
    "(But...we lost the orb. To Hannah, no less—it's unlikely I'll ever figure out what that artifact has to do with me now.)"
    hide mscmc
    show mscmc casual_hairdown sad at centre
    "I sigh heavily and wonder what it all could've meant."
    hide mscmc
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Maybe it was just a fluke anyway... that it caused a reaction in me.)"
    stop music fadeout 1.0
    play music msclexi
    show mscmc casual_hairdown surprised at left2
    show lexi casual bigsmile at right2
    lx "Here."
    show mscmc casual_hairdown smile
    show lexi casual smile
    "I startle, and look up to find Lexi holding out a cup of tea. I fumble out a thank-you as I take it, warming my hands on the ceramic."
    show mscmc casual_hairdown embarrassed
    show lexi casual embarrassed:
        easein 0.4 xoffset -140
    "Lexi wraps a blanket around my shoulders and then hers as she sits next to me and rests her hand on my knee."
    show lexi casual smile
    "I realize how she's been showing me a different side of her lately, and can't help a small laugh. I love her complexity."
    show lexi casual surprised
    mclexi "I didn't know you had such a caregiving side to you."
    show lexi casual embarrassed
    "Lexi gives me a brief smile, feigning annoyance, but I catch the little blush on her cheeks."
    show lexi casual surprised
    lx "Sometimes it's nice to take care of people for a change. Besides, I think you could really use it."
    show mscmc casual_hairdown embarrassed
    show lexi casual smile
    "She moves her hand softly and slowly up my leg and then back down, then stops and glances at me."

    "I don't move her hand, the weight of it is grounding, but also sends tingles shooting throughout my body."

    mclexi "I really appreciate it."
    show lexi casual surprised
    lx "Yeah?"
    show mscmc casual_hairdown smile
    show lexi casual sad
    lx "I just... you're probably going through a lot right now. I... I didn't realise the stakes were so high going in, I..."
    show lexi casual surprised
    "She trails off, looking out at nothing in particular. I lean in closer to gently bump my shoulder with hers."
    show lexi casual embarrassed
    mclexi "It's okay. You stuck by me, that's what's important."
    stop music fadeout 1.0
    play music mscromance
    hide mscmc
    hide lexi
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi smiles, soft and even a bit bashful. She leans against me in kind."
    show lexi casual_cu sleep_cu
    lx "Still, I'm... I'm sorry. You shouldn't have had to experience any of that."
    hide lexi
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    mclexi "Yeah, well... Hannah shouldn't be such a dangerous, infuriating person."
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    "That brings a big laugh out of Lexi, bright and surprised. I can't help but grin at the sound of it."
    show lexi casual_cu smile_cu
    lx "You've got that right."
    show lexi casual_cu embarrassed_cu
    "She continues to run her finger up and down my thigh right below my shorts. I glance at her hand, then up at her."
    stop music fadeout 1.0
    play music mscpassionateromance
    show lexi casual_cu smile_cu
    "She's looking back at me. The smallest hint of her more mischievous, self is returning to her gaze as she bats her lashes."
    show lexi casual_cu smile_cu
    lx "You're sure you don't have bruises or sore spots or anything?"
    hide lexi
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    mclexi "Yeah, I'm okay..."

    "(She's being so gentle, but what's that look in her eye. She looks like... like she wants me... all of me.)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "No? No pain you need to be distracted from by a hot mer?"
    hide lexi
    $menuhideborder = True
    menu lexis1e12c1:
        "A. Allow Lexi to distract you from your pain!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "I can’t help but laugh, charmed and blushing."

            mclexi "Well, now that you mention it, I suppose I’ve got some pains you could distract me from."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "She takes the tea from my hands, setting it on an end table. Then crawls back over to me on all fours, pinning me with her stare."

            lx "I’ll do my best."

            "She leans over me and picks up my hand, then kisses it softly. It almost feels like the touch of butterfly wings."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "You’re right I don’t feel the pain as much now. But there’s other spots too…"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi smiles salaciously and lets her fingers lightly run over my skin."

            lx "Here? Let me bring your attention elsewhere."

            "Slowly, she kisses up my exposed side as she runs her hands over my hips and brings my hands to her body."
            hide lexi
            "She moves close to my lips, and I hold my breath anticipating… Then her lips crash against mine as we grab at one another."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "Your distraction is working."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "I know exactly what I’m doing here. I may be good at breaking things, but I’m also a healer."
            show lexi casual_cu embarrassed_cu
            "I laugh at her teasing. Her lips brush against my jaw; then she takes my hand again and kisses my fingertips."
            show lexi casual_cu smile_cu
            lx "So you feel better?"
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Definitely getting there, but..."
            hide mscmc
            show lexi casual_cu embarrassed_cu at lexi_cu
            "Lexi smiles at me then leans in to shower me with kisses that are light and playful, then she brushes our noses against one another."

            lx "You’re a tough case, aren’t you?"
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I guess the adrenaline rush finally wore off."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Not to worry, I’ll be your adrenaline rush, baby."
            hide lexi
            "Her hand gently cups my cheek, and she kisses the side of my neck, slowly moving down to my collarbone."

            "She throws one of her legs over my lap and straddles me as we keep kissing."

            "Her hips grind against mine as my hands press against the softness of her body, our lips interlocked, the only two people in the world..."
            show lexi casual_cu smile_cu at lexi_cu
            "She responds to my desire with her own of equal strength. She sits up higher, looking down at me through her long lashes."
            show lexi casual_cu embarrassed_cu
            lx "Close your eyes."
            hide lexi
            "I do, expecting a kiss on the lips but… I feel her lips on one of my eyelids then the other, and it makes me blush brightly."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "Lexi, don’t ever stop kissing me."
            hide mscmc
            show lexi casual_cu surprised_cu at mscmc_cu
            "Lexi looks into my eyes, suddenly, surprised."
            show lexi casual_cu embarrassed_cu
            lx "Careful what you wish for."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "Not when it comes to you. I refuse."

            "She snickers, and her lips meet mine. I sigh into the soft, wonderful sensation."
            hide mscmc
            "We stay like that, tangles in one another, feeling one another, for what seem like forever and at the same time only a second."

            "We grab at each other’s clothes. We both want to to take things further, I can feel it in the way she touches me and see it in her eyes."

            "Her hands start wandering and exploring, past the waistband of my shorts, her fingertips lightning me up with every touch."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "Lexi..."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Mmmm?"
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "Please..."
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            "She smiles over me, leaning even closer. I can feel the warmth of her lips, smell their flowery vibrant berry tint."
            show lexi casual_cu smile_cu
            lx "I want to hear you say that again."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "Please, Lexi."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Please...?"
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mclexi "I want you."
            hide mscmc
            "She grins, and finally, {i}finally{/i} meets my lips again with a hot hungry kiss. I moan into the taste of it, as our bodies come together."

            "I explore her with my hands too, noting every raised scar. It reminds me of the sea floor, soft sand with its rugged bits. She feels wonderful."
            show lexi casual_cu embarrassed_cu at lexi_cu
            "Lexi draws back to take a breath, her face flushed as she laughs."

            lx "Is this okay?"
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "Yes. It’s more than ok. It’s fucking great."
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            lx "You know, I think you’re right."
            hide lexi
            "I light up with laughter as she kisses and nibs at my jaw, my neck, my collarbone… Still gentle, but wanting."

            "I can feel our hearts rushing together."

            "When her lips meet mine again, it’s like fireworks."

            "I wrap my arms around her shoulders, leaning back into the couch as she grinds against me."
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(I need this so badly. I need her.)"

        "B. Panic.":
            $menuhideborder = False

            "The notion is so adorable I panic and take a big gulp from my tea. Too big, in fact, it burns down my throat like molten lava."

            mclexi "Oh, son of—!"

            lx "Oh no-!"

            "She hurries to grab a cup of much cooler water, while I wave air into my open mouth. She quickly returns and holds the glass to my lips."

            "The entire time, I can see her struggling to hold back her laughter."

            "It puts the cutest expression on her face; I can't help but also laugh a little."

            "We crack up at my ineptitude as she withdraws the water."

            "Our eyes linger on each other, until she kisses me deeply, pressing me back into the couch."
    hide lexi
    hide mscmc
    "The effects of our chaotic night seem to fade into the background as we become enveloped in one another."

    "Her skin is hot to the touch as I reach into her bustier and her hand works its way into my shorts."

    "I move down and undo the button on her shorts as she watches me smirking, and I tug off her shorts. She's only in her bodysuit now."

    "As more and more of our clothes come off, I feel closer to her than I ever have, and not just physically."
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(This is it. It's happening. Me and Lexi!)"
    hide mscmc
    "With a burst of eagerness, I sit up and kiss Lexi deeply, desperately. She moans, grasping at my hair as we rock against one another."

    "But all too suddenly, the heat of her skin against mine seems to disappear..."
    scene bg msc_mcs_vision at bg with eye_open_slow
    stop music fadeout 1.0
    play music mscmcvisions
    "I open my eyes, expecting to see Lexi's face, only to find the ocean all around and above me."
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Wait—a vision?! NOW?!! Come on!)"
    hide mscmc
    "As disappointed as I am to be having a vision now of all moments, I can't help but relax in the sway of the underwater current."

    "I look up, and as I expect, the mermaid is there again, swimming around high above me."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Who are you, I wonder...)"
    hide mscmc
    stop music fadeout 1.0
    play music mscmcvisionvoice
    "Then I notice something different. I hear a voice!"

    "I can't tell if it's coming from the mermaid or not, but I quickly realize it's the same voice I heard at the museum."

    "And... I understand what they're saying this time!"

    "Part of me realizes they're still speaking that ancient mer language, but for some reason I can understand!"

    $sidecharone = "Mysterious Voice"

    sid1 "Listen..."

    "I focus hard on the voice, it's trying to tell me something."

    "I hear something else now though. A bunch of background noise, like somewhere human and busy, and..."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Hannah's voice!?)"
    hide mscmc
    $sidechartwo = "Hannah's voice"

    sid2 "One ticket for Buenos Aires."

    "(She's buying a plane ticket! Is the mermaid showing me this?)"

    "Hannah and the sound of, what I now realize is, an airport fade away. The vision voice speaks to me again."

    sid1 "Go. Claim what is yours."

    "(What is... mine?)"

    "I blink..."
    scene bg msc_night_lightson_uv at bg with eye_open_slow
    show lexi casual_cu sad_cu at lexi_cu with eye_open_slow
    stop music fadeout 1.0
    play music msclexi
    "Then, I open my eyes—and see Lexi's concerned face looking down at me."
    show lexi casual_cu smile_cu
    "Lexi's hand strokes my hair, and I realize I'm laying on the UV couch with my head in her lap."

    lx "Welcome back."

    "Lexi teases, but she looks relieved. I drag myself up to a seated position, my mind spinning from the vision."

    lx "What'd you see this time? The mermaid again?"
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Yes, and I heard the voice from the museum."

    "(Could it have been the mermaid talking to me? That's never happened before...)"

    mclexi "I don't know how, but I could understand this time, even though they were still speaking that old mer language."
    hide mscmc
    show lexi casual_cu surprised_cu at lexi_cu
    "Lexi sits up, looking interested."
    show lexi casual_cu bigsmile_cu
    lx "What did they say?"
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "They told me to listen, and then I heard Hannah buying a plane ticket to Buenos Aires."

    mclexi "Then the mermaid, or whoever, told me to 'claim what's mine'."
    hide mscmc
    show lexi casual_cu surprised_cu at lexi_cu
    "Lexi blinks at me, clearly as surprised as I feel. Then she lights up with a grin, and jumps to her feet."
    show lexi casual_cu bigsmile_cu
    lx "Well, what are we waiting for? We're going to Buenos Aires!"
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "What, like—right now? Lexi-!"
    hide mscmc
    show mscmc casual_hairdown surprised at left3
    show lexi swim bigsmile at right3
    "She looks halfway to hopping into the driver's seat and piloting us to Buenos Aires already, before turning back to me with a big smile."

    lx "When else?"
    show lexi swim surprised
    mclexi "I can't just up and leave all of a sudden! What about-?"
    show lexi swim smile
    "Lexi crosses her arms, smirking playfully at me. She shifts her curvy hip out to the side, reminding me she's not wearing her shorts."
    show lexi swim embarrassed
    lx "What about...?"

    mclexi "About...uh..."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu sleep_cu at mscmc_cu
    "(I forget what I was saying!)"
    show mscmc casual_hairdown surprised at left3
    show lexi swim smile at right3:
        easein 0.4 xoffset -225
    "Lexi strides over to me, placing a fingertip under my chin and lifting my head so our gaze meets."
    hide lexi
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "I think I know you well enough to know you're dying for me to whisk you off your feet on a daring and dangerous adventure."
    show lexi casual_cu embarrassed_cu
    lx "I want that too, I want you, I want us... and I want to go after what's yours with you. And... I have a UV that can get us there."
    show lexi casual_cu smile_cu
    lx "Come on an international treasure hunt with me, be with me... Please."
    hide lexi
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(She's right about—well, all of that—but I can't just...!)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "You're not scared, are you?"
    hide lexi
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "I pout up at her."

    mclexi "You know I'm not scared. But I have responsibilities here... If I just up and left...."
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi rolls her eyes, fondly. Then runs her hands over my body as she steps close enough so that we're pressed up againt each other."
    hide lexi
    show mscmc casual_hairdown embarrassed at left1
    show lexi swim smile at centre:
        easein 0.4 xoffset 300
    "The she gets up and struts sultrily across the UV, hips swaying with every step."
    hide lexi
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "My mouth goes dry as she spins back around on her toes and looks deeply into my eyes..."

    "She poses in the doorway that leads to the other half of the UV that I've never seen before."

    "Her bedroom must be back there behind her."
    scene bg msc_lexi_s1_ei4 at bg with fade:
        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    "Everything from her daring expression to the way she's posing her body for me to admire, has me overcome with desire."

    "(It's literally not fair how 'makes me wanna run away with you' gorgeous she is. Maybe I should...)"

    lx "You want to come to Buenos Aires. You want me. Just say, yes. I'm yours if you do."

    mclexi "Yes."

    "(I can't help my response, it's out of my lips before I even have time to think.)"

    "(But once I say it I know I've made the right decision.)"

    "Lexi smiles, dazzling me with her roguish charm and undeniable beauty and my heart feels like its dancing as I walk over to her."

    lx "Oh, there's one last thing I should mention before our trip..."

    lx "The UV only has one bed..."

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
