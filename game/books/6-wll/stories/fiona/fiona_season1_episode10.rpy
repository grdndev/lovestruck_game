label fiona_season1_episode10:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_mc_room_day at bg
    play music wlleverydaycalm3

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show wllmc skirt surprised at centre
    "The sun is still clinging to the horizon like a sulky child when Fiona bangs the door of my room."
    show wllmc skirt sad at left3
    show fiona cloak basic at right3
    mcfiona "Fiona, I was sleeping."
    show fiona cloak grin
    mb "I know, but look! I brought you breakfast. Besides, you'll forgive me when you see what the plan is."
    show wllmc skirt smallsmile
    "Once I've eaten, Fiona pulls out an old, tattered paperback."
    mb "Here it is! Our holy grail!"
    show wllmc skirt surprised
    mcfiona "How exactly is 'The Theft of A Moonlit Heart' going to help us with our ghost?"
    hide fiona
    hide wllmc
    show wllmc skirt_cu sad_cu at wllmc_cu
    "(I read that book on the journey from New Amster to Franklin. It was pretty run of the mill, honestly.)"
    hide wllmc
    show wllmc skirt smallsmile at left3
    show fiona cloak smile at right3
    mb "One of the performances for Wisp Willow's fifty year celebration has dropped out. Diana is desperately hunting for a replacement."
    "She pets the cover of the book."
    show fiona cloak smirk
    mb "And this is Diana's favorite romance. So we're going to reenact a scene."
    show wllmc skirt angry
    "A sudden suspicion washes over me."
    mcfiona "Which one?"
    show fiona cloak grin
    mb "This one! Where the witch uses her cards to show the bandit that she's in love with her."
    "She uses one finger to point to herself as the witch and me as the bandit."
    hide fiona
    hide wllmc
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(No wonder she was making jokes about us being girlfriends.)"
    hide wllmc
    show wllmc skirt smirk at left3
    show fiona cloak grin at right3
    mcfiona "And this really gets Diana to give us her wedding ring?"
    show fiona cloak smirk
    mb "That's what I saw."
    mb "And at least in my vision, I saw myself giving it back to her, too."
    show wllmc skirt smile
    mcfiona "Well, that's one thing off my mind."
    show enzo familiar smile at centre behind wllmc:
        alpha 0.7 xoffset -200 yoffset 180
        easein 0.5 alpha 1.0 xoffset 0 yoffset 0
    enz "I think it sounds like fun, Mistress! You can dazzle the world with your theatrical talent."
    show wllmc skirt smirk
    mcfiona "I think this one's going to be more on Fiona. Card tricks, I assume?"
    show fiona cloak smile
    show enzo familiar smirk
    "Fiona pulls her cards out and fans them in the air, making them ripple back and forth between her hands."
    mb "It's been a while since I got to show off for a crowd."
    show wllmc skirt surprised
    show fiona cloak grin
    "She does the deftest false transfer I've ever seen, and something in my chest lurches a little."
    hide fiona
    hide wllmc
    hide enzo
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(I mean, who wouldn't be impressed by Fiona in her element?)"
    hide wllmc
    show wllmc skirt smallsmile at left3
    show fiona cloak basic at right3
    "At first, planning the scene and the card tricks we'll do is pretty fun."
    show wllmc skirt surprised
    "But when it comes time to actually rehearse the lines, we find ourselves faltering."
    mcfiona "I don't know what you're talking about, Adelaide. The only feeling in my heart is for your money."
    show fiona cloak angry
    mb "Don't lie to me, Elena. I know your sense of justice. This was never about the money."
    show fiona cloak angry:
        pause 0.1
        ease 0.5 centre xoffset 20
    "She palms the Justice card, and presses it against my chest."
    hide wllmc
    hide fiona
    show fiona cloak_cu angry_cu at fiona_cu
    mb "It was always about you and me."
    "Fiona's golden eyes are my whole world as she looks up at me."
    hide fiona
    "Somewhere in the background, a strange breeze ruffles the curtains."
    show wllmc skirt surprised at left1
    show enzo familiar surprised at right1plus
    enz "Your magic's getting away from you, Mistress. You might want to rein it in a bit."
    hide wllmc
    hide enzo
    show fiona cloak_cu sad_cu at fiona_cu
    "The moment breaks, and Fiona's gaze falls."
    hide fiona
    show wllmc skirt smallsmile at left1
    show enzo familiar surprised at right1plus
    mcfiona "I'm okay, Enzo. But do you think you could give us some time alone? I don't think we're ready for an audience just yet."
    show enzo familiar smirk
    "Enzo winks at me, which for some reason I find very annoying."
    enz "Say no more. I get where you're coming from."
    hide wllmc
    hide enzo
    "Unfortunately, things don't get much better once he's gone."
    show wllmc skirt smallsmile at left3
    show fiona cloak basic at right3
    mb "Okay, so my next line is 'I spent my whole life listening to the whispers of the cards.'"
    show fiona cloak smirk
    mb "I need to stack the deck while I'm saying it. Can you pull me into your arms? And do something showy with your hands?"
    show wllmc skirt smile
    mcfiona "How about this?"
    show wllmc skirt smile:
        easein 0.5 centre
    show fiona cloak surprised:
        pause 0.4
        ease 0.3 right2
    "I reach out and wrap one arm around her waist, while the other twists into her braids, pulling her head back so that our eyes meet."
    hide wllmc
    hide fiona
    show fiona cloak_cu grin_cu at fiona_cu
    mb "Perfect! You're a genius, my pearl."
    scene bg_wll_mc_room_day at bg
    show wllmc skirt_cu surprised_cu at wllmc_cu
    with hpunch
    "In a discordant cacophony, the picture frames on the wall shake furiously, and the old violin snaps every string."
    hide wllmc
    show wllmc skirt surprised at centre:
        pause 0.1
        easein 0.4 left2
    show fiona cloak surprised at right2
    "I jerk away from Fiona."
    hide fiona
    hide wllmc
    show wllmc skirt_cu sad_cu at wllmc_cu
    "(Why does my magic always act up at the worst times?)"
    "(I want her to think I'm cool, but here comes my magic, ready to ruin the show and make me look like a doltish mooncalf.)"
    hide wllmc
    show wllmc skirt surprised at left2
    show fiona cloak surprised at right2:
        pause 0.1
        easein 0.5 right1 xoffset -20
    "Fiona surges after me, cards scattering on the floor as she reaches up to press her hands to my face."
    hide wllmc
    hide fiona
    show fiona cloak_cu smile_cu at fiona_cu
    mb "Don't run away! Let yourself feel what's happening! This is a wonderful opportunity to improve your control."
    "Her eyes are butter-smooth and soft, as honey-sweet as the words dripping from her tongue."
    mb "Come on, sweet treasure. Trust me. Let me help you."
    hide fiona
    show wllmc skirt_cu surprised_cu at wllmc_cu
    "(Does she really mean that? Or am I just going to look like more of an idiot if I say yes?)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e10c1:
        "Learn more control from Fiona." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show wllmc skirt_cu smallsmile_cu at wllmc_cu
            mcfiona "I'll take any help that will get this under control."
            hide wllmc
            show fiona cloak_cu grin_cu at fiona_cu
            "Fiona's eyes crinkle."
            mb "That's my girl."
            hide fiona
            show wllmc skirt basic at left2
            show fiona cloak smile at right1plus
            "She takes her hands from my face, and my magic simmers down."
            show wllmc skirt smirk
            mcfiona "It's weird. I can {i}feel{/i} my magic. That hot spring of yours really did something to me."
            mcfiona "I don't suppose I can undo it?"
            show fiona cloak grin
            "Fiona laughs."
            mb "We probably should have expected this, honestly! I wouldn't be surprised if it takes a while for your magic to settle down."
            show fiona cloak smile
            mb "But we can definitely try and help it in the short term."
            show wllmc skirt smallsmile
            mcfiona "So what's the plan?"
            show wllmc skirt surprised
            show fiona cloak smile behind wllmc:
                pause 0.1
                easein 0.4 right1 xoffset -20
            "Fiona reaches up and strokes my cheek, and I feel my magic start to surge again."
            show wllmc skirt sad
            mcfiona "See, that just makes it worse."
            mb "And isn't that interesting."
            hide wllmc
            hide fiona
            show fiona cloak_cu smile_cu at fiona_cu
            "She leans in, her lips just inches from mine."
            mb "What's your magic telling me that you won't, hmm?"
            hide fiona
            show wllmc skirt_cu smirk_cu at wllmc_cu
            mcfiona "It's telling me that you're a dangerous menace."
            hide wllmc
            "One of Fiona's hands slides along my thigh. The floorboards beneath our feet groan."
            show wllmc skirt_cu embarrassed_cu at wllmc_cu
            mcfiona "If you destroy this room to prove a point, Donna will be furious with you."
            hide wllmc
            show fiona cloak_cu smile_cu at fiona_cu
            mb "So we'll take it slow."
            hide fiona
            "She gestures for me to sit down, and I do."
            show wllmc skirt basic at left3
            show fiona cloak smile at right2
            mb "Okay. Let's try this. I'll tell you where I'm going to touch you first, see if that helps."
            "She sits down across from me."
            mb "I'm going to start by taking your hand."
            hide fiona
            hide wllmc
            show wllmc skirt_cu smallsmile_cu at wllmc_cu
            "(I can handle that.)"
            hide wllmc
            show fiona cloak smile at right2:
                pause 0.1
                ease 0.6 right1
            show wllmc skirt basic at left3
            "She reaches out and interlaces our fingers."
            show fiona cloak grin
            mb "There we go! Nice and easy."
            show wllmc skirt sad
            mcfiona "If this was enough to set my magic off, I think I'd have to crawl into a hole and die of embarrassment."
            show fiona cloak smirk
            mb "Fair. Okay, let me try something a bit more advanced. I'm going to slide my hand across your cheek and up into your hair."
            show wllmc skirt embarrassed
            "The way she says it, cool and soft, sets the fire in my blood raging."
            hide fiona
            hide wllmc
            show wllmc skirt_cu embarrassed_cu at wllmc_cu
            "(I can do this. I can.)"
            hide wllmc
            "But as soon as her hand touches me, her fingers finding the sensitive skin of my scalp, I lose all control again."
            show wllmc skirt angry at left3
            show fiona cloak surprised at right1
            mcfiona "Ugh, why is this so hard?"
            show fiona cloak sad
            mb "I don't know."
            "She frowns, and thinks for a minute."
            mb "What is your magic saying that you can't?"
            hide fiona
            hide wllmc
            show wllmc skirt_cu sad_cu at wllmc_cu
            "(That I want you. How much I want you. How a loop of every kiss we've shared burns on the back of my eyelids as I fall asleep.)"
            hide wllmc
            show wllmc skirt sad at left3
            show fiona cloak surprised at right1
            mcfiona "That I'm a fool."
            show wllmc skirt smallsmile
            mcfiona "Maybe this will work better if we try the other way around. If you let me touch you."
            show fiona cloak grin
            mb "Any time you want to, my treasure."
            show wllmc skirt smile
            show fiona cloak smile
            "She folds her hands in her lap and puts on a face of false innocence, a mask I want to break as soon as I see it."
            mcfiona "Here I come."
            hide wllmc
            hide fiona
            show fiona cloak_cu smile_cu at fiona_cu
            "I reach for her face, and cup it between my palms, then tilt her head to the side so I can kiss her neck."
            hide fiona
            show wllmc skirt_cu smile_cu at wllmc_cu
            "(I'm close to the spot where she applies her perfume. It smells so good, layering over the warm scent of her body.)"
            hide wllmc
            show fiona cloak_cu embarrassed_cu at fiona_cu
            mb "Mmm. That's very nice."
            hide fiona
            "I tug on her braids, tipping her head back to bare the long white column of her throat and lick at her, feeling more ravenous by the moment."
            show wllmc skirt_cu smirk_cu at wllmc_cu
            "(It's not enough. I want more.)"
            hide wllmc
            "My magic is clamoring at my mind, about to spill over."
            show wllmc skirt_cu embarrassed_cu at wllmc_cu
            "(Isn't this enough? What more can I do?)"
            hide wllmc
            "I know the answer, and with a groan of frustration, I bring my lips to Fiona's."
            show wllmc skirt_cu embarrassed_cu at wllmc_cu
            "(Ah, she feels so good.)"
            hide wllmc
            "She opens her mouth to my tongue, her desire equal to my own, and for the first time, my magic quiets."
            show fiona cloak smile at right1
            show wllmc skirt smile at left1plus
            "When we pull apart, I give her a rueful smile."
            mcfiona "Well, that worked."
            mb "It did. But it's not exactly a practical solution for the stage."
            show wllmc skirt smirk
            mcfiona "Not really, no. I guess we can try something different?"
            show fiona cloak grin
            mb "Back to the drawing board it is."
            show fiona cloak smirk
            mb "Well, maybe after just one more kiss."
            hide fiona
            hide wllmc
            "She leans in again, and I let her take what she wants from me."
            show wllmc skirt_cu smirk_cu at wllmc_cu
            "(It certainly takes the edge off my magic, though it doesn't sate it completely.)"
            "(The way things are going, it feels hard to imagine anything that could do that.)"
            hide wllmc
        "Push your magic away.":
            $menuhideborder = False
            show wllmc skirt_cu sad_cu at wllmc_cu
            mcfiona "No. No, we have more important things to do."
            hide wllmc
            show fiona cloak surprised at right1:
                xoffset -20
            show wllmc skirt sad at left2:
                pause 0.1
                easein 0.4 left3
            "I pull away from her, too many years of hiding and concealment keeping me in my old patterns."
            show fiona cloak sad
            mb "As you wish."
            show fiona cloak smile
            "She slides her arm through mine and leans against me for a moment."
            hide wllmc
            hide fiona
            show fiona cloak_cu smile_cu at fiona_cu
            mb "I'll never make you do anything you don't want to, I hope you know that."
            hide fiona
    "We keep practicing, but as evening draws in, I can feel how frustrated we both are."
    show wllmc skirt_cu sad_cu at wllmc_cu
    "(My powers are still going haywire, and working around them is making the performance difficult.)"
    hide wllmc
    show fiona cloak smile at right1
    show wllmc skirt sad at left1plus
    mb "I think we've done as much as we can on our own. Let's show what we have to the Ward."

    scene bg_wll_ward_hq_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wlleverydayupbeat1 fadein 1.0
    "Fiona and I set up an impromptu stage in the Ward headquarters, and our performance begins."
    show wllmc coat_cu angry_cu at wllmc_cu
    "(We're going to be very careful not to trigger my magic this time.)"
    hide wllmc
    show fiona cloak smile at centre
    mb "There you are, Elena. I've been waiting for you."
    hide fiona
    "The premise of 'Theft of a Moonlit Heart' is that Fiona's character..."
    "Adelaide, is a powerful witch seeking revenge on a man who wronged her."
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Fiona certainly seems comfortable in the part, playing up all her mysterious qualities.)"
    hide wllmc
    "My character, Elena, is the bandit who helps her track her target down, but with secret motives of her own."
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Surprise surprise, the secret is love.)"
    hide wllmc
    "The moment we've chosen to reenact is near the end, when Adelaide reveals that she's known about Elena's feelings all along."
    show wllmc coat angry at left3
    show fiona cloak basic at right2
    mcfiona "I've come for what I'm owed. The thousand gold pieces you staked on the head of Robert Harker."
    show fiona cloak angry
    "As the scene goes on, Adelaide uses her cards to interrogate Elena's motives, forcing her to reveal the truth."
    hide fiona
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(This is where Fiona's tricks come in, and they're the only part either of us is happy with.)"
    hide wllmc
    show wllmc coat angry at left3
    show fiona cloak smirk at right3
    "At last, Adelaide draws the fateful card, The Lovers."
    show wllmc coat surprised
    mb "Don't you see it, Elena? This is where fate was leading us all along. There's nothing to be afraid of anymore!"
    show fiona cloak grin
    mb "I love you too."
    show fiona cloak grin behind wllmc:
        pause 0.1
        easein 0.4 right1
    show wllmc coat surprised:
        pause 0.3
        easein 0.4 left1 xoffset -20
    "She gestures dramatically, and then pulls me in for the passionate kiss that ends the scene."
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(And it's not that I'm complaining about a chance to kiss Fiona, but something about it doesn't feel right.)"
    hide wllmc
    show fiona cloak basic at right1:
        pause 0.1
        easein 0.5 right1plus
    show wllmc coat basic at left1:
        xoffset -20
        pause 0.1
        easein 0.5 left2
    "Fiona and I break apart and turn to the others."
    show fiona cloak smile
    mb "Well, what do you think?"
    mcfiona "And be honest."
    hide fiona
    show enzo familiar smile at right2
    enz "If I were Elena, I would have just taken the gold."
    hide enzo
    show wllmc coat surprised
    show nathan redcasual_bandana surprised at right3
    wc "I don't understand why Elena's so stuck on hiding her feelings. What's she got to lose by being honest?"
    show wllmc coat angry
    mcfiona "Okay, less criticism of the story, more criticism of our performance."
    hide nathan
    show sascha vest smirk at right3
    sasch "I mean isn't it obvious?"
    "He arches an eyebrow at us, his smile sardonic and amused."
    show wllmc coat sad
    mcfiona "If it was obvious, we wouldn't be here."
    show wllmc coat surprised
    show sascha vest grin
    sasch "You're trying to hide the spark between you, when you should be showing it off."
    hide sascha
    show cecelia dunevest basic at right3
    "Cecelia nods."
    show wllmc coat sad
    vr "You're acting the part of lovers, but your performance is less passionate on stage than off."
    hide wllmc
    show fiona cloak sad at left2
    show cecelia dunevest sad at right3
    vr "Especially you, Fiona. You're holding back."
    hide fiona
    hide cecelia
    show wllmc coat_cu sad_cu at wllmc_cu
    "(Because she's trying not to trigger my magic.)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e10c2:
        "Fiona's doing most of the work.":
            $menuhideborder = False
            show wllmc coat angry at left2
            show cecelia dunevest angry at right3
            mcfiona "Fiona's doing most of the work, with all her card tricks. She shouldn't have to carry the performance too."
            vr "Fiona can do more than one thing at a time."
            hide wllmc
        "Our relationship's nothing like this.":
            $menuhideborder = False
            show wllmc coat angry at left2
            show cecelia dunevest angry at right3
            mcfiona "Well of course the stuff on stage doesn't feel like us. Our relationship is nothing like the story."
            hide cecelia
            show sascha vest smirk at right4
            sasch "Oh? Want to bet?"
            hide wllmc
            hide sascha
        "Look to Fiona.":
            $menuhideborder = False
            show wllmc coat sad at left2
            show fiona cloak sad at right3
            "I hesitate, not sure how much Fiona is comfortable telling the Ward."
            hide fiona
            hide wllmc
            show wllmc coat_cu angry_cu at wllmc_cu
            "(In my opinion, nothing would do just fine.)"
            hide wllmc

    show fiona cloak sad at left2
    show cecelia dunevest angry at right3
    "Fiona sighs and her shoulders slump."
    show fiona cloak angry
    show cecelia dunevest basic
    mb "Okay, more passion."
    show fiona cloak basic
    mb "We've been running into some problems with [genericfn]'s magic, but we can work on that too."
    show cecelia dunevest smile behind fiona:
        pause 0.1
        easein 0.4 right1
    "Cecelia smiles, and claps a hand on Fiona's shoulder."
    vr "That's what I like to hear. I'm sure you'll figure it out."

    scene bg_wll_mc_room_lights_on at bg with fade
    stop music fadeout 1.0
    play music wlleverydaycalm3 fadein 1.0
    "Fiona and I slink back to the boarding house to do some more work."
    show fiona cloak basic at right3
    show wllmc skirt basic at left3
    mb "Maybe if we get really comfortable, that will help."
    show wllmc skirt smile:
        pause 0.1
        ease 0.6 centre
    show fiona cloak basic:
        pause 0.3
        easein 0.3 right2
    "She opens her arms, and when I step into them, wraps them tightly around my waist."
    show wllmc skirt smirk
    mcfiona "How long are we meant to stay like this?"
    show fiona cloak smirk
    mb "Are you complaining?"
    hide wllmc
    hide fiona
    show fiona cloak_cu smirk_cu at fiona_cu
    "She leans her head forwards, resting it against my chest."
    mb "Because I'm not."
    "I rest my head on top of hers."
    hide fiona
    show wllmc skirt_cu smile_cu at wllmc_cu
    "(It does feel natural. Like she belongs here.)"
    show wllmc skirt_cu surprised_cu
    "But as I think about the way we're touching, every soft curve I can feel against mine, my magic flares up again."
    show wllmc skirt_cu angry_cu
    mcfiona "Ugh, why does it keep doing this? It wasn't before."
    hide wllmc
    show fiona cloak_cu basic_cu at fiona_cu
    mb "It's probably because of the ritual bath. You're more open to your magic than you ever have been before."
    hide fiona
    show wllmc skirt_cu angry_cu at wllmc_cu
    mcfiona "In that case, I'd like to seal it up again. All it does is cause me problems."
    hide wllmc
    show fiona cloak smile at right1
    show wllmc skirt surprised at left1plus
    "I lean back and look at her."
    mcfiona "I'm surprised you aren't complaining about it more, honestly."
    show fiona cloak surprised
    mb "I would never! Your magic is amazing and I adore it."
    show fiona cloak grin
    mb "It's only been a couple of days, and you've already done so much with it!"
    show wllmc skirt sad
    mcfiona "I just don't want it to ruin our plan."
    show wllmc skirt surprised
    mb "And that's why you have me. The all-seeing eye!"
    show fiona cloak smile
    "She reaches up and taps her forehead right in the place where her third eye emerges."
    show wllmc skirt sad
    mcfiona "But you can't see me."
    show fiona cloak smirk
    mb "Now whose turn is it to be annoyed with their powers? I still don't know why that's happening."
    show wllmc skirt smile
    "She wriggles out of our hug and sits down on the floor, patting the ground next to her."
    hide wllmc
    hide fiona
    show fiona cloak_cu smile_cu at fiona_cu
    mb "What's your opinion on destiny? Do you think the future is set in stone?"
    hide fiona
    "I sit down beside her, and she weaves her fingers with mine."

    $menuhideborder = True
    menu fionas1e10c3:
        "I make my own path.":
            $menuhideborder = False
            show fiona cloak smile at right1
            show wllmc skirt smirk at left1plus
            mcfiona "I make my own path. No one controls my future but me."
        "Choice only means so much.":
            $menuhideborder = False
            show fiona cloak smile at right1
            show wllmc skirt smirk at left1plus
            mcfiona "I mean, I make my own choices. But choice only means so much in a big world."
        "I don't know anymore.":
            $menuhideborder = False
            show fiona cloak smile at right1
            show wllmc skirt smirk at left1plus
            mcfiona "I don't know anymore. I used to have an opinion, but then I met you."

    show wllmc skirt smallsmile
    "Fiona nods."
    mb "Seeing the future the way I do, I know just how big and small choices really are."
    show fiona cloak smirk
    mb "One choice in the right place can make the difference between life and death."
    show fiona cloak sad
    mb "But on the other hand, when you compare a simple human to something like my patron, we have an effect so small it's almost negligible."
    show wllmc skirt sad
    mcfiona "So it's not worth doing anything?"
    show fiona cloak surprised
    mb "On the contrary, it's worth doing everything."
    show fiona cloak angry
    mb "There's no rule that says the future has to be better than the past. The universe doesn't care about justice, or mercy, or love."
    mb "Those things only exist because we choose them. Every hour of every day."
    show wllmc skirt angry
    mcfiona "I don't see your point."
    show fiona cloak smile
    mb "My point is that I have a responsibility to use all my powers to make good choices."
    mb "I'll make sure everything turns out alright. I promise."
    show wllmc skirt smile
    "I take her hand and kiss her palm."
    mb "There's nothing to worry about."
    show wllmc skirt smirk
    mcfiona "There's a million things to worry about. But thank you."
    show fiona cloak surprised
    "I kiss her wrist, and she shudders slightly."
    show fiona cloak smirk
    mb "You know, maybe we've been going about this the wrong way."
    mb "Trying to ignore it, trying to pretend we're not feeling... this."
    hide wllmc
    hide fiona
    "She moves to sit on my lap, her knees bracketing my hips."
    show fiona cloak_cu angry_cu at fiona_cu
    mb "But we can't ignore it. We can't fight it. Maybe we should just give in."
    "Her lips drop to my neck."
    hide fiona
    show wllmc skirt_cu smile_cu at wllmc_cu
    mcfiona "What happened to rewarding ourselves when the job is done?"
    "My protest is half-hearted at best. My hands are already tracing their way down Fiona's sides, my fingers itching to slip under the fabric."
    hide wllmc
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "There's such a thing as being too patient."
    hide fiona
    "She reaches for the fastening of my shirt."
    show fiona cloak_cu grin_cu at fiona_cu
    mb "Won't you say yes, my pearl? I've been aching for you since the moment we met."
    "The word is a breath, but it burns like fire when it leaves my lips."
    hide fiona
    show wllmc skirt_cu grin_cu at wllmc_cu
    mcfiona "Yes."
    hide wllmc

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
