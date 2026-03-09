label lexip_season1_episode4:

    $tbc = False
    scene bg msc_surf_shop_day at bg
    play music mscsuspense

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show ned vest basic at centre

    dt "Do you believe in mermaids?"
    hide ned
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Do we believe in mermaids? Does he know something about Lexi?)"
    hide mscmc
    show mscmc casual_hairdown angry at left3
    show ned vest basic at right3
    lx "What kind of stupid question is that? Of course we don't, we're not little kids."

    dt "Shame..."
    hide ned
    hide mscmc
    show trina casual basic at centre
    so "Hey, are you guys..."
    show trina casual sad at left1:
        easein 0.4 xpos 550
    show ned vest basic at right3
    "Trina bumps into Ned as she makes her way into the shop."
    show trina casual angry
    so "I'm sor- Oh, it's just you."
    show ned vest basic at right3:
        easein 0.5 xpos 2000

    "Ned doesn't say anything as he ignores Trina and leaves."
    hide ned
    so "What was that all about?"
    show trina casual angry at right3
    show mscmc casual_hairdown angry at left3
    mclexi "Nothing. It was just Ned being an ass again."
    show trina casual sad
    show mscmc casual_hairdown basic
    so "Not surprising. Are you okay, Lexi?"
    hide mscmc
    hide trina
    show lexi casual surprised at centre
    "I turn my attention to Lexi and realize how shocked she looks."
    hide lexi
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Did he get to her that much? How can I protect Lexi from him?)"
    hide mscmc
    show lexi casual surprised at centre
    lx "Yea, I'm fine. I'm just..."
    hide lexi with dissolve
    "Without another word, Lexi gets up and heads out the back towards my room, leaving Trina staring at me with a puzzled look."
    show trina casual sad at right3
    show mscmc casual_hairdown surprised at left3
    so "For 'nothing' she seems pretty upset."
    show mscmc casual_hairdown sad
    mclexi "Yeah. He was just being really inappropriate with her."
    show trina casual basic
    so "Well I can take over here, why don't you go check up on her?"
    show mscmc casual_hairdown surprised
    mclexi "Are you sure?"
    show trina casual smile
    so "Yeah, I've got things covered here."
    show mscmc casual_hairdown grin
    mclexi "Thanks bestie."
    scene bg msc_mc_bedroom_day at bg
    stop music fadeout 1.0
    play music mscsadtimes
    show lexi casual angry at centre
    "As I open the door, I find Lexi lying on my bed."

    "She's flipping through the tattered, water-damaged book she had brought from her UV while furiously scribbling notes."

    "She doesn't seem to notice me at all. As I stare at her, I realize just how determined she is to locate the treasure before Ned."
    hide lexi
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(The way her hair is cascading down her face and that focused look... She's so beautiful like this.)"
    hide mscmc
    $menuhideborder = True
    menu lexis0e4c1:
        "A. Clear my throat to get Lexi's attention.":
            $menuhideborder = False
            show mscmc casual_hairdown smile at left2
            show lexi casual angry at right2
            "I clear my throat loudly to let Lexi know that I’m there, but she doesn’t look up from her book."
            show mscmc casual_hairdown sad
            show lexi casual surprised
            mclexi "Are you okay? You ran out of there so quickly..."
            show lexi casual sad
            lx "Yea, I’m fine. I just, I don’t know. He got to me a little."
            show mscmc casual_hairdown grin
            mclexi "I get that. It’s funny how your first move is to bury your nose in a book."
            show lexi casual bigsmile
            "Lexi looks up at me this time, she grins at my teasing."
            show mscmc casual_hairdown grin:
                easein 0.4 xpos 450
            "Taking advantage of the slightly better mood, I lay on the bed next to her."



        "B. Sneak up on Lexi.":
            $menuhideborder = False
            show mscmc casual_hairdown basic at left2:
                easein 0.25 xpos 250
            show lexi casual surprised at right2
            "I tip-toe as sneakily as I can towards the bed, and as I make it to Lexi, she turns her head."
            show mscmc casual_hairdown surprised
            show lexi casual smile
            lx "I know you’re there, dummy."

            "She smiles amused at my antics."

            mclexi "Ugh! Well I tried!"
            show mscmc casual_hairdown grin:
                easein 0.4 xpos 450
            "Accepting my defeat, I fall onto the bed next to Lexi and look out the window."


        "C. Plop down on the bed next to Lexi":
            $menuhideborder = False
            show mscmc casual_hairdown grin at left2:
                easein 0.4 xpos 450
            show lexi casual surprised at right2
            "Without saying anything, I jump onto the bed, plopping down next to Lexi and causing her to bounce a little."
            show lexi casual smile
            mclexi "You doing okay?"

            "Lexi chuckles, and I can tell my obnoxious entrance brightened her mood, even if just by a little."

            lx "Yeah, I'm doing better, though now I've got a surf jock bothering me while I'm reading!"
            show lexi casual bigsmile
            "We stare at one another before we both laugh."
    show mscmc casual_hairdown surprised
    show lexi casual basic
    mclexi "I wonder how Ned could know that you're a mermaid..."
    show lexi casual angry
    lx "I can think of a few people that might sell me out."
    show lexi casual basic
    mclexi "What do you mean?"
    hide lexi
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    "Lexi's expression turns sour as she looks out into space, then it softens and she rolls on her back."
    show lexi casual_cu basic_cu
    lx "Treasure hunting is pretty competitive and I've definitely had to be a little underhanded once or twice to get my loot."
    show lexi casual_cu angry_cu
    lx "There's one person in particular that would love to out me to Ned, but who knows."

    "She shrugs, rolling back over and flipping through the book again."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(What?! How can you say something like that and not give details!)"
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    lx "Regardless of how he might have found out about me, the best thing to do is to find this treasure fast and get out of here."
    hide lexi
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    mclexi "Is there anything I can do to help?"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "Not unless you can figure out what this journal is talking about. The captain that hid the treasure was quite cryptic in his writing."
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "What do you mean?"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "He talks about spirals that rise and fall, and other stuff that doesn't make sense. It's driving me insane!"
    hide lexi
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Do you mind if I look at it?"
    hide mscmc
    show lexi casual_cu sad_cu at lexi_cu
    lx "Sure. I'm not getting anywhere."
    hide lexi
    "She slides the book to me and as I look through the pages they're filled with vague statements about swirls, spirals, and flows."

    "Scattered throughout the text are drawings of spirals with arrows, but they all seem to point in different directions."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(He talks about this rising and falling... And we know the treasure is somewhere around here... What rises and falls?)"
    hide mscmc
    stop music fadeout 1.0
    play music mscmctheme
    show mscmc casual_hairdown surprised at left2:
        xpos 500
        easein 0.4 xpos 450
        easein 0.4 xpos 500
    show lexi casual surprised at right2
    "The answer hits me and I suddenly grab Lexi's arm, startling her."

    lx "What's wrong?!"
    show mscmc casual_hairdown grin
    mclexi "I figured it out! The captain is referring to the tide! The swirls and stuff are him using whirlpools as landmarks!"
    show lexi casual bigsmile
    "Lexi's eyes light up as she stares at me, her deep green eyes sparkling."

    lx "You're a genius! Do you know where he might be talking about?"
    show mscmc casual_hairdown sad
    "My shoulders sag as the energy drains from me and I shake my head."

    mclexi "I don't. I've never seen anywhere around here that has whirlpools like that."

    lx "That's fine! This is our first-!"
    show mscmc casual_hairdown surprised
    show lexi casual surprised
    "A melodic tune, my alarm, plays from my phone and interrupts Lexi."

    mclexi "Crap. I forgot I told Trina I'd close up the shop today."
    show mscmc casual_hairdown smile
    show lexi casual bigsmile
    lx "I'll come down with you."
    hide lexi with dissolve
    hide mscmc with dissolve
    "Lexi jumps off the bed with the book tucked under her arm."
    scene bg msc_surf_shop_day at bg with wiperight
    show mscmc casual_hairdown sad at left3
    show trina casual basic at right3
    mclexi "Hey Trina! I forgot I said I'd close tonight."

    so "It's fine, I wasn't going to do much, just going to Jerry's for..."
    show mscmc casual_hairdown surprised
    show trina casual smile
    "Trina pauses as Lexi enters behind me and she grins at me."

    so "Actually, I can handle things here tonight."
    show trina casual smile:
        easein 0.4 xpos 500
    "She leans in and whispers in my ear."

    so "She seemed really upset earlier. Why don't you take her on a date to unwind?"

    so "The historical society is putting up some exhibits on the pier."
    hide mscmc
    hide trina
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(A date?! That's right, we're 'dating'.)"
    hide mscmc
    show mscmc casual_hairdown embarrassed at centre
    "I nod, and turn to Lexi."
    show mscmc casual_hairdown embarrassed at left3
    show lexi casual bigsmile at right3
    mclexi "Do you want to go to the ` and check out the exhibits, Lexi?"
    hide lexi
    hide mscmc
    show trina casual smile at centre
    "I glance at Trina to reaffirm that it's okay and she nods with a broad smile."

    so "You two go have fun!"
    hide trina
    show mscmc casual_hairdown grin at left3
    show lexi casual bigsmile at right3
    mclexi "You heard it! Let's go before she changes her mind!"
    scene bg msc_boardwalk_night_lights at bg with clockwise_wipe
    stop music fadeout 1.0
    play music msclexi
    "As we arrive at the boardwalk, we find it bustling with tourists and locals alike and it feels like everyone is caught up in treasure fever."

    "Placed amongst the usual attractions are small pop-up tents, each showing off different historical exhibits."
    show mscmc jacket_hairdown smile at left3
    show lexi casual surprised at right3
    lx "There are so many people here! Is it normally this busy?"

    mclexi "Nope. It's thanks to Ned. Everyone heard a famous person was here hunting for treasure and now we have a bunch of tourists everywhere."
    show lexi casual angry
    "Lexi frowns."

    lx "Of course it has something to do with Ned. Still, this is pretty awesome! I've never been around this many humans before."
    show lexi casual bigsmile
    "We walk around for a few minutes, Lexi eagerly taking in her surroundings until she suddenly stops dead in her tracks."

    lx "Look-!"
    show mscmc jacket_hairdown surprised
    show lexi casual bigsmile:
        easein 0.4 xpos 450
    pause
    show lexi casual bigsmile:
        easein 0.4 xpos 650
    show mscmc jacket_hairdown surprised:
        easein 0.4 xpos 450
    "Before I have a chance to see what Lexi is talking about, she grabs my hand and begins to pull me towards a booth."

    mclexi "What-?!"

    "A moment later, I find myself in front of a newly set up booth showing various antiques and artifacts."
    show mscmc jacket_hairdown embarrassed
    "As Lexi looks over the exhibits, she continues to pull me along by my hand and I find myself more focused on her touch than the items."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She grabbed my hand so casually! And she hasn't let go!)"
    hide mscmc
    show mscmc jacket_hairdown embarrassed behind lexi:
        xpos 450
    show lexi casual bigsmile:
        xpos 650
    "My heart is pounding in my chest and it takes me a moment to realize Lexi is talking to me."
    show mscmc jacket_hairdown surprised
    lx "...are fakes, but even the replicas are really well made!"

    mclexi "Are they? I don't know anything about this stuff, but it's really interesting. Do you think any of it could help us find the treasure?"

    "Lexi shrugs, but her excited energy doesn't dampen."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(She's so cute when she's talking about history like this!)"
    show mscmc jacket_hairdown surprised behind lexi:
        xpos 450
    show lexi casual surprised:
        xpos 650
    lx "This vase is a real one!"

    mclexi "How can you tell?"
    show lexi casual bigsmile
    "A proud smile beams on Lexi's face."

    lx "You can tell by the gunk in the cracks. Also, if you look at the wear around the base..."
    show mscmc jacket_hairdown grin
    show lexi casual smile
    lx "You have no idea what I'm talking about, do you."

    "I shake my head."

    mclexi "I don't, but you definitely seem to be in your element, you nerd."
    show lexi casual surprised
    lx "I'm not a nerd!"
    show lexi casual bigsmile
    "She shoves me lightly on the arm, and I shove her back. The next thing I know we're giggling with each other."
    hide lexi
    hide mscmc
    show lexi casual_cu surprised_cu at lexi_cu
    "Lexi's eyes widen with wonder as she points to the other side of the boardwalk."

    lx "What. Is. That?"
    hide lexi
    "I look across the pier to where Lexi is pointing and see a watergun carnival game."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Over there? It's a game."
    hide mscmc
    show lexi casual_cu angry_cu at lexi_cu
    "Lexi gives me an annoyed frown."

    lx "I get that. I'm talking about THAT!"
    hide lexi
    "I follow her finger and I realize she's not pointing at the game, but instead the massive stuffed plushy hanging above it."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mclexi "Oh, that? It's a monster from a popular game."
    hide mscmc
    show lexi casual_cu  bigsmile_cu at lexi_cu
    lx "It looks just like a... What are they called? Cat! But it has a tail like mine!"

    "I can feel the excitement pouring off of Lexi."
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What if...)"
    show mscmc jacket_hairdown_cu grin_cu
    mclexi "Well, since we're dating and all, why don't I win it for you?"
    hide mscmc
    show lexi casual_cu smile_cu at lexi_cu
    lx "You can win it for me... If you can beat me!"
    hide lexi
    "Before I can object, I feel Lexi pull me again and a few moments later we're in front of the water gun game stall."
    show lexi casual_cu smile_cu at lexi_cu
    lx "Let's do this! The winner gets to give the plushie to whomever they want... And they get the gold coin!"
    hide lexi
    $menuhideborder = True
    menu lexis0e4c2:
        "A. Kick Lexi's ass to win her the plushie."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show lexi casual smile at right2
            mclexi "You’re on!"
            stop music fadeout 1.0
            play music mschappytimes
            "I pull the gold coin from my pocket and slam it on the counter between us."
            hide lexi
            hide mscmc
            show lexi casual_cu bigsmile_cu at lexi_cu
            "Lexi’s eyes ignite with excitement and she smacks her hands down on the game stall counter."

            lx "Let’s do this!"
            hide lexi
            $sidecharone = "Bored Teenage Worker"

            sid1 "So does that mean you two are going to play? That’ll be $5 each."
            show mscmc jacket_hairdown smile at centre

            "I pull out my wallet and give the worker $10."
            show mscmc jacket_hairdown smile at left2
            show lexi casual smile at right2
            "Then we both plop down on the worn black stools behind the water blasters."
            hide lexi
            hide mscmc
            sid1 "Alright... The goal is to get your mermaid thing to the finish line first. Just spray the center."
            show mscmc jacket_hairdown angry at left2
            show lexi casual angry at right2
            "Lexi and I look at one another, exchanging determined looks."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I’ve played this game so many times over the years. There’s no way I can lose!)"
            hide mscmc
            sid1 "Okay, start when the bell rings."
            show mscmc jacket_hairdown angry at left2
            show lexi casual angry at right2
            "Almost immediately the loud bell signaling the start of the race goes off and I press the buttons on my blaster."
            show lexi casual surprised
            "I hit my target dead center without needing to adjust before glancing at Lexi."
            hide lexi
            hide mscmc
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(She missed! There’s no way she can catch up now!)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left2
            show lexi casual smile at right2
            "I look up at the mermaids, slowly making their way across the backboard of the stall, and to my surprise, Lexi’s mermaid is in front of mine!"
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(What the hell?!)"
            hide mscmc
            show mscmc jacket_hairdown sad at left2
            show lexi casual smile at right2
            "Glancing at Lexi’s blaster and back to mine, I realize the issue. The water from her blaster is significantly stronger than mine."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(At this rate... I have no other choice!)"
            hide mscmc
            show mscmc jacket_hairdown grin at left2:
                easein 0.4 xpos 450
                easein 0.4 xpos 500
            show lexi casual surprised at right2
            "I bump my shoulder into Lexi, throwing her aim off for a moment and putting myself back in the lead."

            lx "Hey! That’s cheating!"
            show lexi casual bigsmile
            mclexi "All’s fair in love and war!"
            show lexi casual smile
            lx "Oh yeah?"
            show mscmc jacket_hairdown surprised
            show lexi casual smile:

                easein 0.4 xpos 600
                easein 0.4 xpos 650
            "Lexi immediately bumps me back, throwing off my aim and taking the lead from me again."
            show mscmc jacket_hairdown grin
            mclexi "That's it!"
            show mscmc jacket_hairdown grin:

                easein 0.4 xpos 450
                easein 0.4 xpos 500
            "Before Lexi can protest, I poke her in the side and she bursts out laughing and leans to protect herself, throwing off her shot."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Is she ticklish? I’ll have to remember that.)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left2
            show lexi casual surprised at right2
            mclexi "It’s over!"
            show mscmc jacket_hairdown grin
            "The ear-piercing buzzer sounds off as my mermaid barely finishes before Lexi’s and I jump out of my seat."

            mclexi "Ha! I told you I’d win!"
            show  lexi casual angry
            lx "What! Not fair!"

            "She stick her bottom lip and puts on a fake pouty face and I can’t help but end my taunting."
            hide lexi
            hide mscmc
            sid1 "Which prize did you want?"
            show mscmc jacket_hairdown grin at centre
            mclexi "That one please!"
            show mscmc jacket_hairdown grin lexiplush
            "I point to the blue mermaid cat monster that Lexi had been enthralled with and hug it as the attendant hands it to me."
            show mscmc jacket_hairdown grin lexiplush at left2
            show lexi casual basic at right2
            mclexi "It’s so much softer than I thought it’d be!"
            show mscmc jacket_hairdown smile lexiplush
            show lexi casual surprised
            mclexi "If only I had a cute girlfriend to give this to... Oh, wait!"
            show mscmc jacket_hairdown grin lexiplush
            show lexi casual embarrassed
            "I hold the plushie in front of my face and start to wiggle its paws to make it seem alive."

            $sidechartwo = "[genericfn] As Stuffed Animal"
            show lexi casual bigsmile
            sid2 "Hi there! You look pretty cute. Can I go home with you?"

            lx "Aw. You’re really cute, too! I’d love to take you home with me! I have the perfect place for you in the UV!"
            hide mscmc
            show mscmc jacket_hairdown grin at left2 behind lexi
            show lexi casual bigsmile plush:
                easein 0.4 xpos 500
                easein 0.4 xpos 600
            "She snatches the toy from my hands and immediately holds it up in the air and marvels at it."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(She’s going to put it in the UV? With her valuable collection...)"
            hide mscmc
            show mscmc jacket_hairdown grin at left2 behind lexi
            show lexi casual smile plush at right2
            lx "I’m so lucky to have such a charming fake girlfriend."

            mclexi "I know, I’m amazing."

            "I flip my hair over my shoulder and smirk at Lexi."

            mclexi "Though I’m an even better real girlfriend."

            lx "Is that so? Maybe I’ll just have to find out someday."
            show mscmc jacket_hairdown embarrassed
            show lexi casual embarrassed
            "My heart skips a beat and my cheeks flush and begin to burn, and to my surprise, Lexi’s blushing too."
            hide mscmc
            hide lexi
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Did she really just say that?!)"
            hide mscmc
            show mscmc jacket_hairdown embarrassed at left2 behind lexi
            show lexi casual embarrassed plush at right2
            mclexi "I mean.. Wait, that’s... Maybe when you can finally get this coin from me, we’ll see."
            show mscmc jacket_hairdown grin
            show lexi casual smile
            "I wave the coin in front of Lexi, taunting her with it."
            show mscmc jacket_hairdown surprised
            "Suddenly, something behind her catches my eye as she puts the plushie in her bag."

        "B. Tell her she can buy a better one online.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show lexi casual surprised  at right2
            mclexi "How about I just buy you one online? Then you can pick from other ones too."
            show lexi casual bigsmile
            lx "There are other ones?! You definitely have to show me when we get back."
            show mscmc jacket_hairdown surprised
            mclexi "Definitely! There are a bunch of—Wait, what is that?"
    stop music
    play music mscromance
    show mscmc jacket_hairdown surprised at left2:
        easein 0.9 xpos 1950
    show lexi casual surprised at right2
    "I rush past Lexi to a blown-up picture of the beach being displayed in the tent adjacent to the game stall."
    hide mscmc
    hide lexi
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mclexi "Lexi! Come here and look at this picture!"
    hide mscmc
    show lexi casual_cu surprised_cu at lexi_cu
    lx "What picture?"
    hide lexi
    show mscmc jacket_hairdown surprised at left3
    show lexi casual surprised at right3
    mclexi "Here!"
    show lexi casual basic
    lx "It's nice, I guess?"

    mclexi "No! It's a picture of the shore. I know that area! Those rocks aren't there anymore!"

    mclexi "Here. These rocks are still there, they separate a small section of the beach that I go to sometimes."
    show mscmc jacket_hairdown smile
    "I point to some rocks in the picture before pointing at another set."
    show lexi casual surprised
    mclexi "These aren't there anymore. They must have cleared them out at some point."
    show mscmc jacket_hairdown grin
    mclexi "Without the rocks there, the currents in the water probably changed, dispersing any whirlpools in that area."

    "Lexi's eyes shift from the picture to me and then back to the picture."
    show lexi casual smile
    lx "That means..."

    $menuhideborder = True
    menu lexis0e4c3:
        "A. Blurt out the answer.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi casual bigsmile at right3
            mclexi "We know where to look for the treasure!"


        "B. Wait for Lexi to figure it out.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi casual bigsmile at right3
            lx "We know where to look for the treasure!"


        "C. Say it with Lexi.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show lexi casual bigsmile at right3
            mclexi "We know where to look—."

            lx "For the treasure!"

    lx "We found it! We really found it!"
    hide mscmc
    hide lexi
    show lexi casual_cu bigsmile_cu at lexi_cu
    mclexi "You did it [genericfn]!"

    "Lexi grabs my face in her hands and beams at me, her eyes glittering from the boardwalk lights."
    show lexi casual_cu smile_cu
    "The world stands still as Lexi's face moves closer to mine."

    "(Is she about to kiss me?)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
