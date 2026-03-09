label lexi_season1_episode8:

    $tbc = False
    scene bg msc_mansion_exterior_sunset at bg
    play music mscaction

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "Lexi makes it pretty clear we won't be getting a hold of this book by asking nicely, so we decide to take a more stealthy approach."
    show mscmc jacket_hairdown basic at left1
    show lexi casual basic at right1
    "I bump my shoulder into Lexi as we walk around the block near Emporia's house for what seems like the hundredth time."
    show mscmc jacket_hairdown surprised
    mclexi "We've been walking around the block for hours.. is she ever going to leave?"
    show lexi casual smile
    lx "We'll get our chance, don't worry. Better safe than sorry, right?"
    show mscmc jacket_hairdown basic
    "I nod and look up the street to the gaudy mansion. We don't want to get too close until we have an opening."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I wish there was some way to force her out of the house so we could sneak in.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left1
    show lexi casual smile at right1
    lx "Hey, hand me your phone."
    show mscmc jacket_hairdown basic
    "I give Lexi a bewildered look, but I pull my phone out of my pocket and hand it to her."
    show lexi casual bigsmile
    "After a few seconds of fidgeting at the keys, Lexi holds the phone to her ear and puts on a fake smile."

    lx "Hi there! May I speak to Ms. Emporia Lid please?"

    "Lexi's voice is high-pitched and overly polite."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(The perfect customer service voice... I like her normal voice better. What's her plan?)"
    hide mscmc
    show mscmc jacket_hairdown basic at left1
    show lexi casual bigsmile at right1
    lx "This is her speaking? Fantastic! I'm down here doing inventory at the port and we have a crate here marked with your name."

    lx "According to the paperwork it was rushed through customs and there is an extra fee that needs to be paid."

    "I can barely make out the sound of an annoyed woman's voice talking down to Lexi through the phone."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(She sounds upset, so Lexi's trick seems to be working.)"
    show mscmc jacket_hairdown basic at left1
    show lexi casual bigsmile at right1
    lx "I'm so sorry to hear that. No, unfortunately, you would have to come in person to meet with the harbormaster to get the item."

    lx "Yes, it's because it was rushed through customs and it's high value. I'm so sorry."
    show mscmc jacket_hairdown surprised
    "Lexi gives me an energetic thumbs up as I hear Emporia yelling to someone away from the phone."

    lx "You'll be here within the hour? Sounds great! We'll see you soon!"
    show lexi casual sleep
    "Lexi's shoulders sag slightly as she lets out a heavy sigh and hands me back my phone."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Jackpot! She's so cool.)"
    hide mscmc
    show mscmc jacket_hairdown grin at left1
    show lexi casual smile at right1
    mclexi "I can't believe she fell for that!"

    "Lexi grabs her shoulder with her hand and starts rotating her arm in a circle to stretch it out, all with a smug smile."

    lx "Of course it worked! I'm a pro, remember?"
    show mscmc jacket_hairdown smile
    mclexi "Do you think she suspects anything?"

    lx "Nah. She's a rich collector and she probably thought I was just some stupid customer service woman."
    show lexi casual sad
    lx "I just feel bad for the harbormaster when she gets there.."

    "I blurt out a little snicker, and quickly slap a hand over my mouth."
    show lexi casual bigsmile
    "Lexi grins at me, pleased with herself, then points past me toward the mansion."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Someone is coming out! Finally!)"
    hide mscmc
    show mscmc jacket_hairdown angry at left2:
        easein 0.4 yoffset 50
    show lexi casual angry at right2:
        easein 0.4 yoffset 50
    "Lexi and I crouch behind a stone wall, peeking through the iron fence on top."
    hide mscmc
    hide lexi
    show emporia casual angry at centre
    "We watch as a petite woman with brown hair pulled up into an elegant bun leaves the mansion with what must be her butler."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(That must be Emporia. She looks... Well, rich and mean. Is she really that dangerous?)"
    hide mscmc
    show mscmc jacket_hairdown angry at left2:
        yoffset 50
    show lexi casual angry at right2:
        yoffset 50
    "The two of them get into a ritzy black car and drive down the long driveway before turning down the street and out of sight."
    show mscmc jacket_hairdown smile
    show lexi casual bigsmile
    lx "Finally! You ready?"

    "My heart starts to pound in my chest as I hype myself up."
    show mscmc jacket_hairdown grin
    mclexi "Now or never, right?"
    show mscmc jacket_hairdown grin:
        easein 0.4 yoffset -25
    show lexi casual bigsmile:
        easein 0.4 yoffset -25
    pause
    show mscmc jacket_hairdown grin at out_left
    show lexi casual bigsmile at out_left
    "Lexi swaggers across the mansion lawn and I follow behind her."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Everything has changed so much since Lexi came back into the picture..)"

    "(I'm breaking into an exiled mer's house with the sexiest woman on earth.)"
    show mscmc jacket_hairdown_cu grin_cu
    "(I could get used to this...)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3
    show lexi casual angry at right3
    "I open and close my fists in excitement as we get to the wall of the mansion and I notice Lexi toss something into a nearby bush."
    show mscmc jacket_hairdown surprised
    mclexi "What was that?"
    show lexi casual smile
    "Lexi grins slyly and winks."

    lx "So, are you a top or a bottom?"
    show mscmc jacket_hairdown embarrassed
    "My face goes red with confusion as she points up at a slightly ajar ornate window on the second story of the mansion."
    hide lexi
    hide mscmc
    $menuhideborder = True
    menu lexis1e8c1:
        "A. Hesitate.":
            $menuhideborder = False
            show mscmc jacket_hairdown embarrassed at left3
            show lexi casual bigsmile at right3
            mclexi "Uhh..."

            "Lexi grins at my faltered answer, but she spares me anymore teasing."

            lx "My legs are probably stronger, you climb up me while I balance and pull yourself through with that paddle strength you have."
            show mscmc jacket_hairdown surprised
            show lexi casual bigsmile:
                easein 0.4 yoffset +50
            "Lexi situates her back against the wall like she is sitting in a chair and smacks the top of her thigh while smiling devilishly at me."

            lx "Scuttle up, cutie."

        "B. Top.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left3
            show lexi casual smile at right3
            mclexi "Top."
            show lexi casual surprised
            "Lexi pulls her face back in surprise at my statement."
            show mscmc jacket_hairdown grin
            show lexi casual smile
            "I can’t help but to feel proud that I could surprise her at all."
            show lexi casual smile:
                easein 0.4 yoffset +50
            "Lexi faces me and situates her back against the wall and spreads her legs to gain balance."

            "She rubs the sides of her thighs while smiling at me and faces her palms toward the sky."

            lx "All right, time to prove it. Get up there."


        "C. Bottom.":
            $menuhideborder = False
            show mscmc jacket_hairdown embarrassed at left3
            show lexi casual smile at right3
            mclexi "B-bottom?"
            show mscmc jacket_hairdown grin
            show lexi casual smile:
                easein 0.4 yoffset +50
            "Lexi lets out a chuckle as my face flushes bright red in embarrassment. She leans against the wall and braces herself for me to climb up."
            show lexi casual bigsmile
            lx "That definitely sounds like my kinda girl! But for today I really need you to get on top."

    show mscmc jacket_hairdown embarrassed:
        easein 0.4 xoffset 300
    show lexi casual bigsmile
    "I push Lexi's hair off her shoulders and straddle her as I stare up at the open window."

    "My mind starts to wander, thinking about her warmth and how vulnerable I am, at the mercy of her strength like this..."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Focus! I have to keep my composure and get to that window for Lexi, no distractions.)"
    show mscmc jacket_hairdown angry at left3:
        xoffset 300

    show lexi casual bigsmile at right3:
        yoffset +50
    "As I stand on Lexi's legs and reach for the window sill I realize that Lexi is eye level with my hips."
    hide lexi
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "My body quivers from the closeness of her breath and I look down to see Lexi smirking leviously at me."

    lx "This is a wonderful view. I knew I picked the right girl for the job."

    "I shiver with excitement at Lexi's approval. She teasingly rubs her hands up the back of my thighs."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I'm not going to be able to keep my balance if she rubs her hands on me like that. I'd rather just drop down and...)"
    hide mscmc
    show lexi casual_cu embarrassed_cu at lexi_cu
    "I take a deep breath to regain my composure and continue limbing up to Lexi's shoulders. I can feel her eyes watching me."
    hide lexi
    "I swing open the window and pull myself through."

    "Once I'm in, I lean out, stretching my arm down as far as it will go with my palm wide open."
    show lexi casual_cu smile_cu at lexi_cu
    lx "You ready for me?"
    hide lexi
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mclexi "Go for it!"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    "Lexi jogs a short distance away from the wall. She crouches into the starting position for a sprint and looks up at me."

    "As she takes off toward the mansion wall the muscles in her calves strain and I can't help but lick my lips."
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's so strong and lithe; every move she makes is so purposeful.)"
    hide mscmc
    "Lexi takes a giant leap off the ground and her toes meet the wall as if she is literally running up the side of the mansion."

    "Our hands clasp and I pull Lexi through the window. It goes accordingly, almost, until I lose my footing and almost knock the two of us over."
    scene bg msc_mansion_interior_sunset at bg with wiperight
    stop music fadeout 1.0
    play music mscsuspense
    "I manage to catch myself though, and catch Lexi in my arms too as we fall into Emporia's living room."
    show lexi casual_cu embarrassed_cu at lexi_cu
    "Her chest heaves against mine as she gets her breath back. I hope she can't hear how fast my heart is beating right now."
    show lexi casual_cu smile_cu
    lx "Seems like we're falling on top of each other a lot lately."
    hide lexi
    show mscmc jacket_hairdown surprised at left1
    show lexi casual smile at right1 behind mscmc
    "She shoots me a wink as we straighten up and I look at the finely decorated room we're in."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Wow. This place is a lot posher than I was expecting. The furniture alone is worth more than I could ever make surfing.)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi swipes my chin with her thumb gently but swiftly with a wide smile on her face."

    lx "I'm impressed with you lately. You'd make a pretty treasure hunting partner."
    show lexi casual_cu embarrassed_cu
    "The feeling of her soft fingers on my chin makes my legs a little weak and her praise loops in my head."
    hide lexi
    "We split up to check the bookshelves decorating the far walls."
    show mscmc jacket_hairdown basic at left3
    show lexi casual basic at right3
    lx "Do you see the book anywhere?"

    mclexi "Nothing yet."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(There are so many books on these shelves! How are we supposed to find the one we're looking for before—)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3
    show lexi casual angry at right3
    "We hear the sound of a large door downstairs slam shut and a woman yelling at someone."

    "Lexi and I freeze."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's back already?! We need to get out of here!)"
    hide mscmc
    show mscmc jacket_hairdown angry at left3
    show lexi casual angry at right3
    "My palms feel clammy as I look and nod my head to the window next to the shelf Lexi is searching."

    "Lexi shakes her head, mouthing 'the book' to me. Her eyes sharpen just past me, and she points."

    "Next to the door is a small bookshelf inserted into the wall with a single tome sitting on it."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(That must be it!)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3:
        easein 0.4 xoffset 50
    show lexi casual angry at right3
    stop music fadeout 1.0
    play music mscdanger
    "As I tiptoe across the room towards the tome, I hear the sound of high heels clacking up marble stairs just outside."

    "I gently slide the heavy tome off the shelf, biting my cheek as I hear Emporia's voice right on the other side of the door."

    "It sounds like she's giving orders to someone."

    bn "I'm going to retire to my room. Draw up a bath for me."

    $sidecharone = "Butler"

    sid1 "Would you like to take your tea in the living room while you wait for your bath, ma'am?"
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Crap! He couldn't just let her go to her room to wait?!)"
    hide mscmc
    show mscmc jacket_hairdown angry at left3:
        xoffset 50
    show lexi casual surprised at right3
    "My heart pounds in my chest and I shoot Lexi a wide-eyed frantic look for instructions."

    "Lexi gestures down with her hands, signaling at me to 'calm down', and I take a deep breath to try and settle my nerves."

    bn "You idiot! Did I stutter? I'm positive I said that I would be retiring to my room. So draw me a bath and come get me when it's ready!"

    sid1 "Very good, ma'am."
    show mscmc jacket_hairdown grin
    "The sound of multiple footsteps walking away from the door sends a wave of relief through me, and I turn to Lexi with a proud grin."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(We got it! It might have been luck, but who cares!)"
    hide mscmc
    show mscmc jacket_hairdown grin at left3:
        xoffset 50
    show lexi casual surprised at right3
    "I pump my fist, the one holding the book, in a victory gesture."

    "Lexi's eyes go wide as I do my dance, but not because of my success."
    show mscmc jacket_hairdown surprised
    "The heavy tome smacks the mid-level trim of the wall next to me and I feel the blood drain from my face."

    "It feels like neither of us breathe, for one dreadful second. The footsteps stop."

    bn "What the hell was that sound? I thought I said I'l take my tea in my room?!"

    sid1 "Pardon, ma'am, but no one has entered that room."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(No, no, no! They're going to come in and there's not enough time for us both to climb down from the window.)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3:
        xoffset 50
    show lexi casual surprised at right3
    "My heart beats a million miles a minute as my eyes desperately dart around the room for an alternate escape route, but there are none."
    show lexi casual basic
    "Lexi's face is expressionless as she eyes the window next to her. A cold shiver goes down my spine."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Hannah had messed up when Lexi left her. She's not going to leave me here, is she?)"
    hide mscmc
    show mscmc jacket_hairdown sad at left3:
        xoffset 50
    show lexi casual sad at right3
    "I start to feel nauseated as I hear the doorknob behind me begin to turn and I look at Lexi  pleadingly."
    show lexi casual bigsmile
    "But Lexi's red lips pull into a grin, and I notice a small remote-looking object in her hand."

    "She presses a button on the remote and suddenly the room shakes slightly as an explosion goes off outside."
    hide lexi
    hide mscmc
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What the-?! When did she... Is that what she threw in the bushes earlier?!)"
    hide mscmc
    show mscmc jacket_hairdown surprised at left3:
        xoffset 50
    show lexi casual bigsmile at right3
    "The pungent smell of smoke wafts through the open window as I hear the sound of hurried footsteps running downstairs and shouting."
    show lexi casual bigsmile at centre, out_left
    show mscmc jacket_hairdown surprised at out_left
    "Without missing a beat, Lexi runs across the room and snatches up my hand, pulling me to the window."
    scene bg msc_mansion_exterior_sunset at bg with wiperight
    "She lets me climb down first with the book before quickly following me down and, without a word..."

    "...We sprint across the mansion grounds to make our getaway."
    scene bg msc_day_lightson_uv at bg with wiperight
    stop music fadeout 1.0
    play music msclexiuv
    show mscmc casual_hairdown sad at left3
    show lexi casual angry at right2:
        easein 0.4 xoffset +100
    "Lexi paces back and forth through the UV as I sit dejectedly on the couch."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(She didn't say much on the way back after... She must be really upset with me.)"
    hide mscmc
    show mscmc casual_hairdown sad at left3
    show lexi casual angry at right2:
        xoffset +100
    "Lexi cries out exasperatedly, rubbing the bridge of her nose with her fingers."
    show lexi casual angry at right2:
        easein 0.4 xoffset -100
    lx "Do you know how much danger you were in?!"

    lx "If Emporia had caught us, we'd be in her basement tied up while she did who-knows-what to us right now!"
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Tied up in the basement? What the hell?)"
    hide mscmc
    show mscmc casual_hairdown surprised at left3
    show lexi casual angry at right2
    mclexi "What are you talking about?"
    show lexi casual angry at right2:
        easein 0.4 xoffset -100
    lx "She's downright cruel, [genericfn]! She literally captures people to torture them for fun!"
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(That sure would have been nice to know before going in there!)"
    show mscmc casual_hairdown surprised at left3
    show lexi casual angry at right2:
        easein 0.4 xoffset +75
    lx "You could have gotten seriously hurt, [genericfn]!"
    show mscmc casual_hairdown angry
    mclexi "How was I supposed to know the stakes were so high? You didn't exactly go into specifics!"
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(I made a mistake, but she should have told me how dangerous Emporia was!)"
    hide mscmc
    show mscmc casual_hairdown angry at left3
    show lexi casual sad at right3
    "Lexi's shoulders sag as she stops pacing and looks at me with downturned eyes."

    lx "You—you're right, I should have. I just... if something happened to you.."
    show mscmc casual_hairdown surprised
    show lexi casual angry
    lx "I know you were excited, but you shouldn't be celebrating until after the job is done!"
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(She's right. I put us both in danger because I was careless.)"

    "(But maybe I would have been more cautious if she had been more open about things instead of trying to be cool and mysterious all the time.)"
    hide mscmc
    $menuhideborder = True
    menu lexis1e8c2:
        "A. Keep your cool.":
            $menuhideborder = False
            show mscmc casual_hairdown surprised at left3
            show lexi casual angry at right3
            "I slowly push myself up off of the couch and stand in front of Lexi."
            hide lexi
            hide mscmc
            show mscmc casual_hairdown_cu angry_cu at mscmc_cu
            "(I need to let her know that she was in the wrong, too.)"
            hide mscmc
            show mscmc casual_hairdown angry at left3:
                easein 0.4 xoffset +100
            show lexi casual angry at right3
            mclexi "I get that you're frustrated with me, Lexi, but you could have told me how crazy Emporia actually was."

            mclexi "Not to mention you just winked at me when you tossed a bomb in the front yard!"

            mclexi "These were things you definitely should have shared with me."
            show lexi casual sad
            "Lexi makes a noise, as if to protest, but swallows it back."

        "B. This is so frustrating!.":
            $menuhideborder = False
            show mscmc casual_hairdown angry at left3:
                easein 0.4 xoffset +100
            show lexi casual angry at right3
            "I jump off of the couch, my blood getting hotter the more I think of the things Lexi kept from me going into the break-in."

            mclexi "You’re blaming me for messing up, but you’re the one that had to try and be all mysterious and cool about things!"

            mclexi "You don’t think it would have been pertinent information to tell me Emporia"
            mclexi "likes to torture people and how screwed we were if we got caught?"

            mclexi "Or when I asked you what you tossed in the front yard, you couldn’t have told me it was a bomb?!"
            show lexi casual sad
            "Lexi recoils, just a bit, working her mouth but not producing any words for a moment."

        "C. Give her the silent treatment.":
            $menuhideborder = False
            show mscmc casual_hairdown angry at left3:
                easein 0.4 xoffset +100
            show lexi casual angry at right3
            "Without saying a word I push myself off the couch and move to the far side of the UV, arms crossed and nose pointed high."

            "Lexi groans."

            lx "The cold shoulder? Really? I’m trying to teach you a lesson for next time, I-!"
            show lexi casual sad
            "She goes quiet. After a few seconds, I peek back at her. She looks lost in a whirlwind of thoughts, glaring at nothing."
    show lexi casual angry at right3
    lx "I just..."
    hide lexi
    hide mscmc
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Is she going to be mad? I've never seen her this stressed about anything before.)"
    hide mscmc
    show mscmc casual_hairdown angry at left2:
        easein 0.4 xoffset +100
    show lexi casual angry at right2 behind mscmc:
        easein 0.4 xoffset -100
    "Suddenly Lexi grabs me by the shirt and pulls me to her."
    hide lexi
    hide mscmc
    stop music fadeout 1.0
    play music mscromance
    "The next thing I know, I feel her lips pressing against mine in a fervent kiss."

    "Her hair brushes my face as we kiss, filling my senses with the familiar scent of ocean water and flowers."

    "My body trembles and I let a moan slip. In the brief moment Lexi and I stop kissing, I inhale sharply in excitement."
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Every time I smell her hair I feel like I'm going to swoon. I could get lost in it.)"
    hide mscmc
    "I lean into Lexi and kiss her back as her hands wrap tightly around my waist."

    "As our mouths dance together, I run my fingers up Lexi's arm, leaving a trail of goosebumps on her."

    "When I reach her shoulder, I wrap my arms around her neck. I need to be close to her, as close as I can be."
    show lexi casual_cu surprised_cu at lexi_cu
    "Lexi pulls her head back and lets out a satisfying gasp that shakes me to my core."
    hide lexi
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(I don't want to hold back anymore, Lexi, I know you feel the same way.)"
    hide mscmc
    "Lexi takes my wrist from her shoulder, interlocking her soft fingers in mine."

    "Her other hand runs up my spine and the nape of my neck."
    show lexi casual_cu angry_cu at lexi_cu
    "She stops when she reaches the back of my head, and I gasp, thrilled, as she clutches my hair and yanks my head to meet her eyes."

    lx "Don't you ever scare me like that again."

    "Her words are whisper mixed with a growl, her eyes hot as she looks into mine. My skin tingles in excitement."
    hide lexi
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Another side of her I've never seen before. She's ordering me around but I—I like it.)"

    mclexi "I won't do something like that again."
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "Promise me."
    hide lexi
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mclexi "I promise."
    hide mscmc
    "As I whisper out the words, the last rays of sunlight shining through the windows of the UV fade away."
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(It's gotten so dim. It's... alluring.)"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    "Lexi pulls my head back slightly by my hair. In the setting light of the UV, she looks like a huntress that's found her prey."

    lx "Since you promised, maybe I'll give you a surprise."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at lexi_cu
    "I cock my eyebrow."

    mclexi "A surprise?"
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    "Lexi gently grabs me by the chin with her free hand, a devious grin on her face."

    lx "Only if you do everything I say. If you can be a good girl, you'll get the surprise."
    hide lexi
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(I can be a good girl for you, Lexi.)"
    hide mscmc
    show lexi casual_cu bigsmile_cu at lexi_cu
    lx "Now I want to hear you say it. Tell me you'll be my good girl."
    hide lexi
    $menuhideborder = True
    menu lexis1e8c3:
        "A. Be Lexi's good girl."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "I’ll be your good girl, promise."

            "I look up at Lexi with wide, eager eyes and bite my lower lip."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Can you? If you’re not good, I won’t let you off so easily."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mclexi "I promise... So please give me my surprise? I’ll be really, REALLY good for you."
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            "Lexi breaks out into a wide smile as she looks my face over. I see the tip of her tongue glance across her lips, and I swallow in anticipation."

            "Her green eyes bore into me and I feel an exciting sense of helplessness coursing through my body."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(It’s like I’m one of her books she’s studying and she’s breaking down every detail of me.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "Lexi’s firm grip tugs harder on my hair and as I stare into her eyes I see a glint of satisfaction in them."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(She likes what she sees. That means I’m being the good girl she wants...)"
            hide mscmc
            "My eyes half close as a soft moan escapes my lips. Lexi wraps her free arm around my waist and pulls me to her."

            "Her strength holds me tightly to her, making it impossible to get away even if I wanted to."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(I don’t. My heart is racing with excitement.)"
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            lx "That’s a good girl. But you better not disappoint me."
            hide lexi
            "I shake my head slightly to try and tell Lexi I won’t disappoint her, but all moving my head does is tug my hair even more."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(She’s got every part of me trapped in her grip. My body… my soul… everything is hers right now.)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "Did I say you could move? You’re only allowed to do exactly as I say or I’ll stop right now."

            "I whimper in protest as Lexi’s threat but obey her command and stay completely still."

            lx "That’s my good girl. You’re such a quick learner."

            "Lexi’s praise is like music to my ears and her assertive tone sends shivers down my spine."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(I’m so into this. I did NOT know I’d be so into this!)"
            hide mscmc
            "She lets go of my hair, causing me to gasp, and runs the tip of her index finger across my cheek."

            "Her long nail slowly works its way down to the side of my neck, shooting a chill through me."

            "It takes everything I have to stop myself from shivering."
            show lexi casual_cu bigsmile_cu at lexi_cu
            "My obedience elicits a satisfied grin from Lexi and she runs her fingers lower, down the center of my chest."

            "She lingers there for a moment, circling her finger in my cleavage sending shocks of electricity over my skin."
            hide lexi
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "(It would be so easy for her to just take my top off. Maybe if I keep behaving...)"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "You haven’t moved a muscle. Do you not like me touching you like this?"

            "I go to shake my head but immediately stop, remembering Lexi’s order not to move."
            show lexi casual_cu bigsmile_cu
            "Lexi licks her lips again with a smug grin."

            lx "I almost had you. You really are a good girl, aren’t you? Nod if you agree."
            show lexi casual_cu smile_cu
            "I nod ever so slightly and Lexi eyes me hungrily."
            hide lexi
            show mscmc casual_hairdown_cu
            "(She’s so hot like this. I’d do anything she asks right now.)"
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            lx "How about I give you a little reward for behaving…"

            "Lexi leans her face closer and barely brushes her lips against mine, then to the side over my cheek."

            lx "You’re mesmerizing to me."
            show lexi casual_cu angry_cu at lexi_cu
            "Impulsively, my mouth moves; I want to fluster to such enticing praise, but she gives me a sharp look."

            lx "Don’t argue, or I’ll have to reprimand you."
            hide lexi
            "Her warm breath raises the hair on the back of my neck and I feel the finger she had on my chest move lower down my torso."

            "An intoxicating feeling of pleasure takes me over as she runs her lips down my neck, kissing my skin gently every so often..."

            "And whispering about how proud she is of me."
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(The touch of her lips on my skin is more than I can take. I don’t know how much longer I’ll be able to stay still for her...)"
            hide mscmc
            "I feel my knees begin to shake as Lexi’s hand at my waist moves lower and rests on the inside of my thigh."
            show lexi casual_cu smile_cu
            "She inhales deeply at the feeling of my quivering body and without warning, her hand retreats to cup my cheek."

            lx "That’s my good, good girl."
            hide lexi
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "I can’t help blushing, and roll my eyes out of habit. Lexi withdraws her hand."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "I thought I said you couldn’t move."

            "Her hand comes right back, a light but sharp clap against my cheek. I gasp, and the stars I see are from pure thrill."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(Why have I never done anything like this before?)"
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            lx "Are you my bad good girl?"

            "With the wicked smile still on her face, Lexi yanks my leg up to her waist, running her nails up the skin of my thigh."
            hide lexi
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "Lexi-..."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "I instinctively cling to her, digging my nails into her shoulder blades slightly. Lexi gasps a little, the faintest laugh on her breath."

            lx "Now you’re really breaking the rules… So much for your surprise."
            hide lexi
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "I look up at Lexi with a pouty frown."

            mclexi "What was the surprise going to be?"
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            lx "It was going to be a kiss… and maybe something else, but I guess you’ll never know."
            show lexi casual_cu bigsmile_cu
            "I give Lexi my best puppy dog eyes and she sighs with a sly grin."

            lx "Aw. How can I say no to a face like that?"

        "B. Freeze up.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mclexi "I'll be..."

            "My words get caught in my throat as my mind feels blank from the whirlwind of emotions running through me."
            hide mscmc
            show lexi casual_cu smile_cu at lexi_cu
            "I can feel my skin tingling as Lexi continues to firmly pull on my hair and I can barely keep on my feet; my knees are shaking with want."

            lx "So you won't be a good girl? That's okay, I know how to deal with disobedient girls..."
    scene bg msc_lexi_s1_ei3 at bg with fade:
        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    "Lexi shoves me back onto the couch, her eyes hungry as she throws her legs over me and straddles me."

    "The feeling of her weight on my lap sends a wave of pleasure through me as she saucily places a finger to my wanting lips."

    "She rubs her palms firmly on my chest and collarbone, and her smug smile tells me she can feel my heart racing under my skin."

    "Her hands run down my body, her fingers creating a burning trail over me until she reaches the bottom of my shirt."

    "I'm breathing fast, my hands grasping at her waist, blindly searching for the buttons on her shorts and the permission to undo them."

    "(Please, no more games, Lexi.)"

    "To my delight, she wraps her fingers around the bottom hem of my shirt and looks down at me with lustful eyes."

    "(Please...!)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
