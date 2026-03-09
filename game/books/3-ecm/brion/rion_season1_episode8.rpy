label rion_season1_episode8:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_office_lab_on at bg with fade
    play music ecmtense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "After Gael's call, Rion and I quickly leave the gallery and head to the lab at HQ."

    show ecmc jacket_v1_cu surprised_cu at ecmc_cu
    "(It's so eerie being here at this hour! The building is basically empty...)"
    hide ecmc

    show gael uniform glasses basic at centre
    "Rion and I find Gael waiting for us, looking completely frazzled."
    ga "Thanks for coming back so quickly."

    show rion jacket pin basic at left2
    show gael uniform basic at right3
    "Rion nods at Gael then straightens up, his expression serious."
    ri "What's the problem?"
    ri "I know you wouldn't have called us back if it wasn't urgent."
    ga "You're right, this is definitely urgent."
    ga "I've been working on cataloguing the evidence in your case in the F.D.I. database, but a lot of the data has been seriously corrupted."

    show rion jacket surprised
    ri "Corrupted?!"

    show rion jacket basic
    ga "A lot of it's completely unusable or tampered with so badly that it can't be trusted."

    hide rion
    show ecmc jacket_v1 pin surprised at left2
    mcrion "What about the list of buyers that we added today?"
    ga "That's been corrupted as well."

    hide ecmc
    show rion jacket pin sad at left2
    ri "How could this have happened?"

    show gael uniform angry
    "Gael looks at Rion and narrows her eyes slightly."
    ga "You tell me. No one else has touched that evidence."

    show rion jacket angry
    "Rion crosses his arms over his chest, his eye tweaking slightly in irritation."
    ri "Gael, I don't know what you're implying, but I would never sabotage the evidence on a case I've been working so hard on."
    hide gael
    hide rion

    $menuhideborder = True
    menu rions1e8c1:
        "A. Suggest the computer's glitched.":
            $menuhideborder = False

            show gael uniform glasses angry at right3
            show ecmc jacket_v1 pin surprised at left2
            mcrion "Maybe the computers glitched?"
            ga "D.I.V.A.A. has a lot of controls in place to make sure that can't happen."
            ga "If there was a glitch, we'd be able to identify it and rectify the problem."

        "B. Ask if the system was hacked.":
            $menuhideborder = False
            show gael uniform glasses angry at right3
            show ecmc jacket_v1 pin surprised at left2
            mcrion "Do you think the system could have been hacked?"
            ga "I already got Eko to take a look. There was definitely no outside interference."
            ga "This was an inside job."

        "C. Check the security cameras.":
            $menuhideborder = False
            show gael uniform glasses angry at right3
            show ecmc jacket_v1 pin surprised at left2
            mcrion "Did you check the security cameras? Maybe something unusual happened?"
            mcrion "Or maybe someone made a mistake while cataloguing new evidence?"
            ga "I've already checked the cameras and there's no sign of anything unusual occurring."

    hide ecmc
    show rion jacket pin angry at left2
    ga "If I didn't know any better, Rion...I'd {i}almost{/i} say you were messing with things out of spite."
    ri "I wouldn't do that to you, Gael."
    "I look over at Rion, who's rolling his eyes, clearly annoyed but also unbothered."

    hide rion
    hide gael
    show ecmc jacket_v1_cu sad_cu at ecmc_cu
    "(I think Gael and Rion must have a pretty good relationship. Rion doesn't seem offended at all.)"
    hide ecmc

    show gael uniform glasses basic at right3
    show rion jacket pin basic at left2
    ga "I know you wouldn't, but it's crucial that both of you play ball with me."
    ga "There's a bit more going on here that meets the eye, so we need to tread carefully."

    hide rion
    hide gael
    show ecmc jacket_v1_cu surprised_cu at ecmc_cu
    "(What does {i}that{/i} mean? What isn't she telling us?)"
    hide ecmc

    show gael uniform glasses sad at right3
    show rion jacket pin basic at left2
    ri "You have my word, Gael. We'll stick to our agreement and won't go behind your back."
    "Gael nods, then collects her bag and straightens up."

    show gael uniform basic
    ga "I have to get going. Tomorrow we'll need to see what we can do about this evidence."

    show gael uniform basic at step_out
    "Gael leaves and I turn to Rion, feeling dejected."

    show ecmc jacket_v1 sad at right2
    mcrion "I can't believe it! All that hard work has gone to waste if none of the evidence can be used."

    show rion jacket pin smirk at left2
    "Rion shakes his head and gives my shoulder a reassuring squeeze."
    ri "Don't worry, [genericfn]. We'll figure something out."

    show rion jacket smile
    ri "Tomorrow's a new day."

    show ecmc jacket_v1 embarrassed
    ri "I'll see you here, and we'll hit it again."

    scene bg ecm_office_hq_on at bg with fade
    stop music
    play music ecmcalmeveryday4
    "The next morning, I arrive at the office bright and early with donuts for myself and Rion."

    show ecmc nojacket_v2_cu embarrassed_cu at ecmc_cu
    "(I really hope Rion likes the flavor I picked!)"
    hide ecmc

    show rion black pin basic at left2
    show ecmc nojacket_v2 pin basic at right2, right_in
    "I spot Rion across the room and quickly make my way over."

    show rion black smile
    show ecmc nojacket_v2 embarrassed
    ri "Morning, Hatchling."

    show ecmc nojacket_v2 smile
    mcrion "Good morning, Rion!"

    show rion black smirk
    show ecmc nojacket_v2 embarrassed
    "I look down at the bag in my hand, then hold it towards Rion, a slight blush spreading on my cheeks."
    mcrion "I got you a donut. I hope you like this flavor."

    show rion black smirk at left2:
        easein 0.4 left1
    "Rion takes the donut from me and takes a bite while I shuffle awkwardly, waiting for his reaction."

    show rion black smile
    ri "Pretty good, very close to my favorite kind."

    show rion black smirk
    show ecmc nojacket_v2 smile
    "The corner of Rion's lips turn into a smirk and I can't help but grin back, my heart beating a little faster."

    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(I'm so glad Rion likes it...but I wonder what his favorite type is?)"
    show ecmc nojacket_v2_cu embarrassed_cu
    "(I should ask, but I don't want him to think I'm being annoying!)"
    hide ecmc

    "I walk over to my desk with thoughts of how to figure out Rion's favorite flavors swirling through my mind."
    "I'm so distracted that I don't notice the coffee on my desk until I sit down."

    show rion black pin smirk at left1plus
    show ecmc nojacket_v2 pin surprised at right2
    mcrion "Oh, what's this?"

    show rion black smile
    ri "Since the coffee I got you last time was cold, I thought I'd get you a different one."

    show ecmc nojacket_v2 smile
    "I smile at Rion, then take a sip of the coffee."

    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    mcrion "Oh..."
    "I do my best to keep a straight face, but the coffee is so sweet that I can't help but scrunch my face up."
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc nojacket_v2 pin sad at right2
    "Rion notices my face and glances down at the coffee in my hand."
    ri "Not your style?"
    mcrion "Well..."

    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Maybe the first sip was just too sugary?)"
    "I take another sip and scrunch up my face again."
    hide ecmc

    show rion black pin basic at left1plus
    show ecmc nojacket_v2 pin sad at right2
    mcrion "It's hot...but it's far too sweet for me."

    show rion black smile
    "Rion shrugs with a relaxed smile on his face."
    ri "It was the daily special, I thought you might like it."

    show rion black smirk
    ri "Don't worry. I won't be offended if you toss it."
    "I feel a bit guilty as I throw the drink away."

    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(It was really nice of Rion to get me a coffee, but I can barely even sip that!)"
    hide ecmc

    show rion black pin sad at left1plus
    show ecmc nojacket_v2 pin sad at right2
    ri "Sorry, Hatchling. I should've gotten you something different."

    show ecmc nojacket_v2 smile
    mcrion "It's alright. I appreciate the thought!"

    show rion black smile
    ri "At least now I know what not to get you next time."
    "I can't help but smile at Rion's last words."

    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu smile_cu at ecmc_cu
    "(So...there'll be a next time? Is he thinking about me more often??)"

    show ecmc nojacket_v2_cu embarrassed_cu
    "(No, no, we're just partners. He probably always does nice things like this for the people he works with. Maybe.)"
    hide ecmc

    show rion black pin smile at left1plus
    show ecmc nojacket_v2 pin basic at right2
    ri "I was about to go finish my coffee and donut on the roof."
    ri "I usually head up there alone, but I wouldn't mind the company this morning."
    "Rion smiles at me and holds up the cup in his hand."
    ri "If you join me, you can have my coffee."
    hide rion
    hide ecmc

    $menuhideborder = True
    menu rions1e8c2:
        "A. Accept Rion's coffee and relax with him on the roof." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show rion black pin smirk at left1plus
            show ecmc nojacket_v2 pin smile at right2
            mcrion "Well, I could definitely use a caffeine fix today!"
            mcrion "Sure, I'll join you."

            show rion black smile
            "Rion grins at me then looks towards the fire escape."

            stop music
            play music ecmromantic1
            ri "Come on. I always sneak up this way so no one sees me."

            scene bg ecm_rooftop_day at bg with clockwise_wipe
            "Rion leads me up to the rooftop, then we lean against the stair house wall as we take in the city."
            "Down below, the streets are busy with people rushing to get to work, but up here on the rooftop it's quiet and peaceful."

            show rion black pin smirk at left1plus
            show ecmc nojacket_v2 pin smile at right2
            mcrion "It's nice up here at this time."

            show rion black smile
            ri "Yeah. I enjoy the quiet. I usually get this place all to myself."
            hide rion
            hide ecmc
            hide window
            scene bg ecm_rion_s1_ei3 with fade:
                zoom 1.4 xanchor 0.5 yanchor 1.0 xpos 0.5 ypos 1.14
                linear 5 yanchor 0.0 ypos -0.36 xpos 0.55
            pause
            "Rion turns slightly to face me and holds out his coffee."
            ri "I believe I promised you this."
            "I smile back at Rion and reach for the coffee cup, causing our fingers to graze."
            "Just the slight touch causes my heart to beat frantically."
            "I can feel my face heating as he smirks at me."
            "(I need to relax! That touch has to have been accidental...right?)"
            scene bg ecm_rooftop_day at bg with fade

            "I take a sip, feeling relieved that it's nowhere near as sweet as the candy store explosion Rion gave me earlier."

            show rion black pin smile at left2
            show ecmc nojacket_v2 pin basic at right1plus
            ri "What do you think?"

            show ecmc nojacket_v2 smile
            mcrion "I like it."

            hide rion
            hide ecmc
            "I take another sip and look out at the city, thoughtfully."

            show rion black pin smirk at left2
            show ecmc nojacket_v2 pin smile at right1plus
            mcrion "It's a dark roast, a little more bitter than what I'd usually get, but I still really like it."
            mcrion "The splash of milk with the cinnamon and sprinkle of sugar bring it all together."
            "Rion looks at me in amusement."

            show rion black smile
            show ecmc nojacket_v2 basic
            ri "I'm impressed, [genericfn]. You can really pick all that up just by tasting it?"
            "I shrug, nonchalantly, and take another sip."

            show ecmc nojacket_v2 smile
            mcrion "I know my coffee."

            show rion black basic
            show ecmc nojacket_v2 basic
            "As I sip on the coffee, Rion takes a few more bites of his donut."

            show rion black sad
            "A few moments later I hear him coughing."

            show ecmc nojacket_v2 surprised
            mcrion "Are you okay?"
            ri "I just got some donut stuck in my throat. Could I have a sip of that coffee?"

            show ecmc nojacket_v2 basic
            "I hand Rion his coffee, expecting him to take the lid off."

            hide ecmc
            hide rion
            show rion black_cu basic_cu at rion_cu
            "Instead, he takes a swig from the lid before handing it back to me."
            hide rion

            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            "(Rion's lips just touched this!)"

            show ecmc nojacket_v2_cu blush_cu surprised_cu
            "My heart thumps at the thought and I stare at the lid as I think about how it would feel to have Rion's lips on {i}mine{/i}."

            hide ecmc
            show rion black pin basic at left2
            show ecmc nojacket_v2 pin surprised at right1plus
            "I realize I'm staring at the coffee, so I quickly take a sip."

            show ecmc nojacket_v2 embarrassed
            "I sneak a glance at Rion who's looking out over the city again as he finishes off his donut."

            show ecmc nojacket_v2 smile
            mcrion "Thanks for giving me your drink, Rion. You really didn't have to."

            show rion black smirk
            "Rion shrugs then turns to face me again, leaning on his side against the railing."
            ri "After getting you the wrong coffee earlier, it's the least I could do. Besides, you brought donuts."

            show rion black basic
            show ecmc nojacket_v2 surprised
            mcrion "Why did you think I'd like that drink, anyway? It's completely different to yours!"

            show rion black smile
            ri "Well, it was the special of the day and I thought it had a cute name."

            show rion black smirk
            ri "It reminded me of you."

            hide rion
            hide ecmc
            show ecmc nojacket_v2_cu blush_cu surprised_cu at ecmc_cu
            "(What? Does Rion think I'm cute?!)"
            hide ecmc

            show rion black pin smile at left2
            show ecmc nojacket_v2 pin surprised at right1plus
            ri "I mean, because you seem to like cute things."

            hide rion
            hide ecmc
            show ecmc nojacket_v2_cu sad_cu at ecmc_cu
            "(Oh...)"
            "My heart sinks a bit."

            show ecmc nojacket_v2_cu embarrassed_cu
            "(It was still nice that the coffee reminded Rion of me, even if I didn't like it.)"
            hide ecmc

            "I look out over the city, doing my best to keep my expression neutral."

            show rion black pin basic at left2
            show ecmc nojacket_v2 pin smile at right1plus
            mcrion "I really do like it up here. You can see almost the entire city!"

            show ecmc nojacket_v2 basic
            "I look down at the sprawling neighborhoods."

            show ecmc nojacket_v2 sad
            mcrion "I've lived in LA my whole life, but the city is so huge there are a lot of neighborhoods I've never been to."

            show rion black smirk
            ri "That doesn't surprise me. Most people don't voluntarily go to the slums."

            show rion black basic
            mcrion "Not just that, though."
            "I look over to the west."
            mcrion "I haven't been to a beach since I was a kid. I heard the new artificial beach is supposed to be great."
            mcrion "I also really want to check out that retro neighborhood out East."
            mcrion "I heard they've tried to preserve as much of old LA as possible, so even the roads use an old asphalt formula."

            show rion black smile
            show ecmc nojacket_v2 basic
            ri "Those sound like great places to check out once things at work calm down."

            show ecmc nojacket_v2 blush embarrassed
            "Rion smiles at me, causing my heart to flutter."

            hide rion
            hide ecmc
            show ecmc nojacket_v2_cu blush_cu embarrassed_cu at ecmc_cu
            "(Does he want to check those places out with me??)"
            hide ecmc

            show rion black pin basic at left2
            show ecmc nojacket_v2 pin basic at right1plus
            "Rion glances at the almost-empty coffee cup in my hand."

            show rion black smile
            ri "Done?"

            show ecmc nojacket_v2 smile
            "I gulp down the rest and give Rion a smile."
            mcrion "Done."

            show rion black sad
            show ecmc nojacket_v2 basic
            ri "Come on, we should go to the lab and check out how badly the evidence has been corrupted."

        "B. Be without caffeine.":
            $menuhideborder = False
            show rion black pin surprised at left1plus
            show ecmc nojacket_v2 pin basic at right2
            mcrion "Thanks Rion, but I really want to get started on work."
            show rion black pin sad
            "Rion's face falls but he nods."
            show rion black pin basic
            ri "You're right. We should go see how badly the evidence has been corrupted."
            "Rion quickly downs the rest of his coffee and throws the cup in the trash."
            ri "Come on. Let's go speak to Eko."

    scene bg ecm_office_lab_on at bg with fade
    stop music
    play music ecmcalmeveryday2
    "Rion and I head to Eko's lab and pull out all Rion's case files."

    show rion black pin sad at left2
    show ecmc nojacket_v2 pin sad at right1plus
    ri "Gael wasn't kidding. Nearly everything has been corrupted..."

    hide rion
    hide ecmc
    show eko casual glasses pin angry at centre, step_in
    "Eko walks over, a scowl on her face."

    show eko casual angry at right4
    show rion black pin sad at left4
    show ecmc nojacket_v2 pin sad at left1
    ek "I heard about the data corruption. I can't believe that could happen to evidence stored in my lab!"
    ri "It's not your fault, Eko."
    mcrion "Was there a security breach?"

    show eko casual sad
    ek "No! I checked all the data logs and security footage. Nothing out of the ordinary happened last night."
    ri "Is it possible to restore all the evidence?"
    ek "It is, but that could take days if not weeks!"
    "Rion sighs and I can see how disheartened he feels."

    hide eko
    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    "(Rion's spent so much time on this case!)"
    "(It must be a terrible feeling to hear that all your work has been damaged.)"
    hide ecmc

    stop music
    play music ecmaction1
    show anton casual angry at centre, step_in
    "Before I can say anything, Anton barges into the lab and storms up to Rion and me."

    show anton casual angry at left3
    show rion black pin basic at right4
    show ecmc nojacket_v2 pin basic at right1
    an "You two! I need to speak to both of you."

    show rion black angry
    ri "Can't this wait, Anton? We have important case business to worry about right now."

    show rion black basic
    an "This is important case business."
    an "I spoke to Blythe at the end of the night and she told me you were both {i}harassing{/i} her."

    show ecmc nojacket_v2 surprised
    mcrion "What?! We weren't harassing Blythe!"
    an "Well, Blythe seems to think differently."
    an "She also told me that you technically broke into the gallery a few days ago and were causing scenes at her exhibit!"
    "Anton looks between me and Rion, a furious glare on his face."

    hide anton
    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(I didn't realize Anton cared so much about Blythe!)"
    hide ecmc

    show anton casual basic at left3
    show rion black pin angry at right4
    show ecmc nojacket_v2 pin basic at right1
    ri "Your intel's bad, Anton. We were just doing our jobs."

    show ecmc nojacket_v2 surprised
    mcrion "Right! Every conversation we had was perfectly civil and professional."

    show anton casual angry
    show rion black basic
    "Anton scoffs in disbelief."
    an "Do you {i}understand{/i} how important Blythe is to our work? How few people as important as her are on D.I.V.A.A.'s side?"
    an "D.I.V.A.A. is championing technological change and the two of you could damage that reputation."
    "Anton turns to me with a snarl."

    hide rion
    hide ecmc
    hide anton
    show anton casual_cu angry_cu at anton_cu
    an "Blythe specifically said you were rude to her, [genericfn]."
    hide anton

    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    mcrion "What?!"
    hide ecmc

    $menuhideborder = True
    menu rions1e8c3:
        "A. I wasn't rude!":
            $menuhideborder = False
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            mcrion "I was very polite to Blythe!"
        "B. Blythe doesn't understand sarcasm!":
            $menuhideborder = False
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            mcrion "If I was rude, it was just a misunderstanding."
        "C. Blythe is a liar!":
            $menuhideborder = False
            show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
            mcrion "We seemed to be getting along!"

    hide ecmc
    show anton casual basic at left3
    show rion black pin angry at right4
    show ecmc nojacket_v2 pin basic at right1
    ri "I'm not sure exactly what Blythe said, Anton. Maybe she was just intimidated by [genericfn]."

    show anton casual angry
    an "Intimidated? By what, exactly?"

    hide anton
    hide ecmc
    hide rion
    show rion black_cu basic_cu at rion_cu
    ri "[genericfn] has quite an extensive knowledge of technology and was able to ask Blythe insightful questions."
    "I sneak a glance at Rion who's staring at Anton, his face devoid of emotion."
    ri "[genericfn] conducted herself with total professionalism last night and in no way was she rude."
    hide rion

    show ecmc nojacket_v2_cu embarrassed_cu at ecmc_cu
    "(That's a really nice compliment... Does he really mean all those things?)"
    hide ecmc

    show anton casual angry at left3
    show rion black pin basic at right4
    show ecmc nojacket_v2 pin basic at right1
    an "The two of you really had no business being at an event like that."
    an "You glitched up in front of someone important and D.I.V.A.A.'s reputation could be damaged!"
    an "Who knows who Blythe's going to talk to about this. This agency doesn't run on optimism!"

    show rion black angry
    ri "Anton, [genericfn] and I did a great job and got some leads we were after. Even if Blythe is upset, it's unfounded."
    ri "Why do you care so much, anyway? Dom's the one who needs to worry about D.I.V.A.A.'s reputation."
    an "Because D.I.V.A.A.'s reputation is important to me! We're {i}safeguarding{/i} technological change and doing important work."
    an "Humanity needs to be prepared for the next step, I will {i}not{/i} let you two jeopardize that."

    hide rion
    hide ecmc
    hide anton
    show anton casual_cu angry_cu at anton_cu
    an "Now, leave Blythe alone!"
    hide anton

    show anton casual angry at left3, step_out
    show rion black pin basic at right4
    show ecmc nojacket_v2 pin basic at right1
    "Before Rion or I can respond, Anton whirls around and storms angrily from the room."
    hide anton

    hide rion
    hide ecmc
    show ecmc nojacket_v2_cu surprised_cu at ecmc_cu
    "(Blythe and Anton care so much about cybernetics and human advancement. What's that all about?)"
    hide ecmc

    stop music
    play music ecmcalmeveryday2

    show ecmc nojacket_v2_cu sad_cu
    "(Do they just have the same philosophies, or do they talk a lot more than we thought?)"
    hide ecmc

    show rion black pin angry at right1
    show ecmc nojacket_v2 pin basic at left1plus
    "Rion rolls his eyes at Anton's retreating back, then turns to face me."

    show rion black smirk
    ri "Forget Anton. It sounds like someone didn't have his coffee this morning."
    ri "We have evidence to sort out."

    hide rion
    hide ecmc
    show eko casual glasses pin sad at centre, step_in
    "Just then, Eko walks over, her expression grim."

    show eko casual basic at right4
    show rion black pin basic at left1
    show ecmc nojacket_v2 pin basic at left4
    ek "Rion, I've fully analyzed all the data errors. I still don't know what happened!"

    show rion black sad
    ri "Can you restore it all?"

    show eko casual sad
    ek "I can, however I'm not sure how long it will take."

    show eko casual basic
    show rion black basic
    show ecmc nojacket_v2 surprised
    ri "Could you prioritize Skye's buyer list, Eko? It's the one piece of evidence we haven't been able to properly inspect yet."

    show eko casual basic at right4, step_out
    "Eko nods and heads back to her lab table."
    hide eko

    hide ecmc
    hide rion
    show rion black_cu basic_cu at rion_cu
    "I let out a sigh and turn to Rion who's looking at me with a thoughtful expression on his face."
    hide rion

    show ecmc nojacket_v2_cu sad_cu at ecmc_cu
    mcrion "What now?"
    hide ecmc

    show rion black pin sad at left1
    show ecmc nojacket_v2 pin sad at right1
    ri "Don't look so disheartened, [genericfn]."
    mcrion "I feel like we've taken several steps back..."

    show rion black basic
    show ecmc nojacket_v2 embarrassed
    "Rion touches my arm, reassuringly, and I instantly feel a little calmer."

    stop music
    play music ecmromantic3
    show rion black smile
    "I look up at Rion's eyes and he grins at me."
    ri "We've had a lot of speed bumps these past few days."
    ri "I think we should go grab a bite of stress relief."
    hide rion
    hide ecmc

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

