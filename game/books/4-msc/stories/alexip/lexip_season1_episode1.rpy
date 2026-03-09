label lexip_season1_episode1:

    $tbc = False
    scene bg msc_prologue at bg with dissolve
    play music mscmctheme

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False


    show bg msc_beach_bar_day at bg
    pause

    show mscmc jacket_hairdown smile at left3
    show trina casual smile at right3

    "A cool morning breeze blows on my face as my best friend and I drink our morning smoothies and stare out onto the ocean swells. "
    hide trina
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(If the wind stays light like the radio says, today will be a great day to practice surfing.)"
    hide mscmc

    show mscmc jacket_hairdown surprised at left3
    show trina casual basic at right3
    mclexi "I don't understand how you can drink those."
    show trina casual smile
    so "Just because you don't like kale doesn't mean no one else does."
    show mscmc jacket_hairdown grin
    mclexi "Wouldn't you rather be sipping on a delicious fruit smoothie instead?"
    show mscmc jacket_hairdown smile
    show trina casual basic
    "Trina rolls her eyes and ignores me, electing to bob her head to the music playing on the radio instead. "
    show trina casual smile
    so "Maybe if you focused less on surfing and what I'm drinking..."
    show mscmc jacket_hairdown sad
    mclexi "Oof. Low blow. But it's fine. I can focus on dating once I make it into the World Surf League."

    so "As much as you're out on the water, if anyone can do it, it'll be you."
    show mscmc jacket_hairdown smile
    "Trina raises her cup into the air to toast me."
    hide trina
    hide mscmc
    $menuhideborder = True
    menu lexis0e1c1:
        "A. Of course I can!":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left3
            show trina casual smile at right3
            "I tap the rim of my smoothie to hers before taking a long sip."

            mclexi "Of course! Nothing is going to stop me. This time next year you'll be asking for my autograph."

            "Trina grins deviously."

            so "Only so I can put it up on the wall of the surf shop to bring in more customers."

        "B. Be humble.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left3
            show trina casual smile at right3
            "I tap my smoothie cup to hers and take a short sip."
            show mscmc jacket_hairdown sad
            show trina casual sad
            mclexi "I hope so. I know I’m good, but I feel like I should be out practicing more."
            show trina casual angry
            so "As if! You practically live in the water!"

        "C. Ignore her.":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left3
            show trina casual basic at right3
            "I ignore Trina, getting lost in my own thoughts."
            hide trina
            hide mscmc
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I know I’m good, but I have so much work to do...)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left3
            show trina casual angry at right3
            so "I know that look. It’s the ‘I can do more’ look you get."
            show mscmc jacket_hairdown basic
            "I shrug."
            show mscmc jacket_hairdown sad
            mclexi "I just want to be the best is all."

    hide trina
    hide mscmc
    "Suddenly, Jerry, the large jovial owner of the bar comes out from the back, smiling broadly at us."

    jr "You girls celebrating?"
    show trina casual smile at centre
    so "Yep! The future success of [genericfn]!"
    hide trina
    jr "Amen to that. If anyone can do it, it'll be you kid."
    show mscmc jacket_hairdown embarrassed at centre
    "I blush at the compliments being showered on me."

    mclexi "I still have a ways to go, but it's nice to know people believe in me."
    hide mscmc
    jr "How's the business been, Trina? I've been packed in the evenings with all the new tourists around."
    show trina casual smile at centre
    so "It's been fantastic! Who would have thought that a famous treasure hunter coming to town would bring this many people to the area."
    hide trina
    show mscmc jacket_hairdown surprised at centre
    mclexi "Speaking of..."
    hide mscmc
    $sidecharone = "Radio Host"

    sid1 "With us we have Ned Lewis, famous treasure hunter and documentarian. So what made you choose this area, Ned?"

    dt "Well, as you know, I've made a name for myself by finding treasures in places no one has thought to look, and I have a hunch about this place."
    show mscmc jacket_hairdown angry at left3
    show trina casual basic at right3
    mclexi "A hunch, huh? So not only is he an ass, but he sounds like a con man, too."

    "Trina shrugs."

    so "As insufferable as he and his camera lackey were the other day, at least he's brought me a bunch of new customers."

    mclexi "Right? He came in like he owned the place and barely even acknowledged our existence."
    show mscmc jacket_hairdown basic
    show trina casual smile
    so "He did buy a lot, though, and I'm not about to complain about a big spender."

    so "Anyways, it's time for me to open up and make that money. You coming with or are you going out to crush it?"
    show mscmc jacket_hairdown grin
    mclexi "You know me, gotta catch those waves when I can."

    scene bg msc_ocean_wide_day at bg with clockwise_wipe
    stop music fadeout 1.0
    play music mscbeach
    show surfboard_acc_back behind mscmc
    show mscmc surfer_hairup smile at centre

    "I sit on my board and bob on the water as I look at the open ocean around me."
    hide surfboard_acc_back
    hide mscmsc
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu

    "(Good. No one is around. It means the shoobie-tourist-wanna-be-treasure hunters haven't found my special spot yet.)"

    "(That means no distractions and no one to bother me.)"
    hide mscmc
    show surfboard_acc_back behind mscmc
    show mscmc surfer_hairup surprised at centre
    "A few minutes pass and I begin to wonder where all the waves are when I spot a heavy one headed towards me."
    hide surfboard_acc_back
    hide mscmsc
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Yes! I haven't seen a wave this awesome in weeks!)"
    hide mscmc
    show surfboard_acc_back behind mscmc
    show mscmc surfer_hairup surprised at centre
    "As the wave approaches me, I move to pop up on my board, but before I do, I notice an intriguing shine under the water."
    hide surfboard_acc_back
    hide mscmsc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Could that be...?)"
    hide mscmc
    "I hesitate to investigate, as the massive wave continues to rush towards me."
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Damn it!)"
    hide mscmc
    show surfboard_acc_back behind mscmc
    show mscmc surfer_hairup angry at centre
    hide mscmc with dissolve
    #needs animation of falling off surfboard
    "As the wave reaches me, I duck-dive under it."
    scene bg msc_underwater_day at bg
    #animation shiny in centre of screen
    "A feeling of regret washes over me, but as I look down through the water, I can clearly see a gold coin glittering on the ocean floor."
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(This better be worth it.)"
    hide mscmc
    "I undo my ankle leash and swim as fast as I can to the coin so I can grab it before my board begins to float away."
    stop music fadeout 1.0
    play music msclexi
    show bg msc_lexi_short_mini1 at bg with dissolve
    "(Almost...)"

    "As I reach for the coin, I jump as I feel another hand gently brush against mine."

    "(Who...?)"
    hide bg lexi_short_mini1 with dissolve
    scene bg msc_underwater_day at bg with dissolve
    show lexi mermaid_cu surprised_cu at lexi_cu
    "My eyes dart to the owner of the hand who has quickly withdrawn it and is holding it to her chest."
    hide lexi
    show lexi mermaid surprised at centre
    #animation of floating
    "Which is moving up and down like she's breathing, and instead of legs..."
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(IS THAT A TAIL?!)"
    hide mscmc
    show lexi mermaid basic at centre
    "It takes me several moments to tear my eyes away from the majestic mermaid floating in the water in front of me."
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(What do I do? Am I seeing things?)"
    hide mscmc
    "Unable to process the situation, I clench the golden coin tightly in my hand and swim to my board on the surface."
    scene bg msc_ocean_wide_day at bg
    show surfboard_acc_back behind mscmc
    show mscmc surfer_hairup surprised at centre with dissolve
    "I spit out the water that drips in my mouth as I take my first breath, throwing my arms over my surfboard."
    hide surfboard_acc_back
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Was that an actual mermaid? That's impossible. The smoothie Jerry made this morning was probably bad. Or maybe heat stroke?)"
    hide mscmc
    "I try to wrangle my thoughts, but only one floats to the surface."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(What if it really was a mermaid?)"
    hide mscmc
    "I think about how much I obsessed about mermaids when I was younger, constantly"

    "watching movies and playing dress up."

    $sidecharone = "Sassy Voice"

    sid1 "I think you have my coin..."
    show surfboard back behind mscmc at left3
    show mscmc surfer_hairup surprised at left3

    show lexi mermaid smile at right3
    "I jump at the sound of the self-assured voice, and spin around to find the possible mermaid treading water behind me."
    hide mscmc
    hide lexi
    show lexi mermaid_cu smile_cu at lexi_cu
    "Her hand is held out expectantly, with her lips curled in a cocky grin."
    hide lexi
    #show surfboard_acc_back at left3
    show mscmc surfer_hairup surprised at left3

    show lexi mermaid smile at right3
    mclexi "Mermaid."
    show lexi mermaid surprised
    "I blurt out the word without thinking and the possible mermaid is immediately taken aback."

    $sidecharone = "Possible Mermaid"

    sid1 "What? Where?"

    "She looks around dramatically."

    sid1 "I don't see any. Did they swim away?"
    hide lexi
    hide mscmc
    hide surfboard
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(If that's how you want to play it...)"
    hide mscmc
    show surfboard_acc_back
    show mscmc surfer_hairup surprised at centre
    hide mscmc with dissolve
    #falling animation
    "Without saying anything, I dive underwater and swim as quickly as I can towards the ocean floor doing my best to pretend I spotted another coin."
    hide surfboard_acc_back
    show lexi mermaid surprised at centre
    hide lexi with dissolve
    #diving animation
    "The possible mermaid falls for my ruse and shoots past me to the sea floor."
    show bg msc_underwater_day at bg
    show lexi mermaid basic at centre:
        ypos -500
    "Revealing a rainbow and speckled tail."
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(She really is a mermaid! No, I have to be going crazy. This is impossible.)"
    scene bg msc_ocean_wide_day at bg
    show surfboard_acc_back behind mscmc
    show mscmc surfer_hairup surprised at centre

    "I swim back to the surface in shock and lean my back over my board to stare at the clear blue sky."
    show mscmc surfer_hairup sad
    mclexi "If I'm hallucinating this badly, I might be in trouble..."

    $sidecharone = "For Sure Mermaid"
    show mscmc
    hide surfboard_acc_back
    show lexi mermaid_cu smile_cu at lexi_cu
    sid1 "You're not hallucinating, but now that you've seen me, we need to have a talk."

    "I look down my body to see the mermaid floating next to my board."
    hide lexi
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid smile at right3
    sid1 "What's your name?"

    mclexi "[genericfn]."
    show lexi mermaid smile at centre
    "The mermaid leans on my board with me and I find myself lost in her shining green eyes."
    hide mscmc
    hide lexi
    show lexi mermaid_cu smile_cu at lexi_cu
    sid1 "You have really beautiful eyes, [genericfn]."
    hide lexi
    show surfboard_acc_back
    show mscmc surfer_hairup embarrassed at centre
    #animation of falling and getting back on surfboard
    "My cheeks flush at the comment and I roll off of my board into the water and stay there for a moment before coming back up to the surface."
    hide lexi
    hide surfboard_acc_back
    hide mscmc
    "(Did she really just say I have beautiful eyes?)"
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    sid1 "Are you okay?"
    hide mscmc
    show mscmc surfer_hairup embarrassed at left3
    show lexi mermaid surprised at right3
    "I nod, trying my best to calm down."

    mclexi "Yea, I'm fine. What's your name?"
    show lexi mermaid smile
    "The mermaid smiles and flips her hair dramatically over her shoulder."
    show mscmc surfer_hairup surprised
    sid1 "I'm Lexi, the greatest treasure hunter in all of the oceans."
    show mscmc surfer_hairup grin
    "I try my best to hold back from laughing at the introduction since I can't tell if she's"

    "intentionally being dramatic or not."
    show mscmc surfer_hairup smile
    mclexi "Well, Lexi, what did you want to talk about?"
    #lexi animation of diving under and up again
    "Lexi vanishes under the water and pops up next to me, splashing my face a little as she surfaces."

    lx "So here's the thing. You've obviously seen I'm a mermaid, and that's against the law. So now I'm going to have to kill you."
    show lexi mermaid bigsmile
    "My face blanches as she gives me a toothy smile."
    show lexi mermaid sad
    lx "I'm joking! But the part about being in trouble is true. If the mer police find out, they'll definitely throw me in jail. I've had a few priors."
    show mscmc surfer_hairup sad
    show lexi mermaid surprised
    mclexi "That seems a bit extreme, but okay. Is this fairytale creature law or just mermaids?"

    "Lexi's brow furrows at the comment."
    show mscmc surfer_hairup basic
    lx "Fairytale creatures?"

    "I shrug."
    show mscmc surfer_hairup sad
    mclexi "Like fairies or gnomes or vampires. I don't know. Classic magical creatures."
    show mscmc surfer_hairup surprised
    show lexi mermaid surprised
    lx "So, no idea what any of those are, but it seems like you have a lot of magical creatures on land."

    "I shake my head, realizing I've confused her."
    show mscmc surfer_hairup sad
    mclexi "No! They're not real. Or I don't think? Actually now that I'm talking to you, I'm not sure."
    show lexi mermaid bigsmile
    "Lexi laughs as I visibly try to wrangle my reality back into place."
    show mscmc surfer_hairup surprised
    lx "Well I'm definitely real, and I definitely really need you to promise me you won't tell anyone about me or try to capture me."
    show mscmc surfer_hairup sad
    show lexi mermaid basic
    mclexi "First off, no one would believe me if I told them. Secondly, why would I try and catch you?"
    show mscmc surfer_hairup surprised
    mclexi "I've never heard of anything like that. Besides, mermaids have always been my thing since I was little."
    show mscmc surfer_hairup smile
    show lexi mermaid surprised
    mclexi "There's no way I'd ever let anything happen to you."

    lx "So I'm the first mermaid you've ever met?"
    show lexi mermaid smile
    "I nod."
    hide lexi
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Then how about this. How about we have a competition for the coin?"
    hide lexi
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    mclexi "I'm not sure why I'd compete for my own coin, I found it first, but what did you have in mind?"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    "Lexi flashes a confident smile."

    lx "We'll show one another the coolest trick we can do in the water."
    hide lexi
    "I bite my lip in excitement."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(See a mermaid do a water trick? That would literally be the craziest thing to ever happen to me!)"
    hide mscmc
    show lexi mermaid_cu smile_cu at lexi_cu
    lx "Want to see my trick?"
    hide lexi
    $menuhideborder = True
    menu lexis0e1c2:
        "A. Check out Lexi's cool trick."(paidchoice = "paidchoice"):
            $menuhideborder = False
            stop music fadeout 1.0
            play music mscloveinterest

            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mclexi "That coin is as good as mine."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "Lexi’s eyes light up at my agreement and she grins from ear to ear."
            show lexi mermaid_cu smile_cu
            lx "Don’t count on it! I’ll have you know that I never lose!"
            #Animation time woooooo, lexi dives underwater and does tricks for the next few lines
            show mscmc surfer_hairup surprised at left3
            show lexi mermaid smile at right3:
                easein 0.4 yoffset -60
                easein 0.4 yoffset 500
            "She doesn’t give me a chance to respond before disappearing under the water."
            hide mscmc
            show lexi mermaid bigsmile at centre:
                easein 0.4 yoffset 560
                easein 0.4 yoffset -60
            "A few moments pass before Lexi bursts out of the water and does a corkscrew flip over me."

            "Spraying water into the air that falls on me like a gentle rain."
            show lexi mermaid bigsmile:
                easein 0.4 yoffset -60
                easein 0.4 yoffset 500
            hide lexi
            "Rainbows form in the air in her wake, and when she finally disappears back under the water, the air around me shimmers."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            "(This is so awesome!)"
            hide mscmc
            show mscmc surfer_hairup surprised at centre
            "I feel giddy as I watch Lexi continue to somersault and flip around me until she disappears, leaving me floating in a cool ocean mist of rainbows."
            show mscmc surfer_hairup surprised at left3
            show lexi mermaid bigsmile at right3:
                easein 0.4

            "As I bask in the moment, Lexi casually floats on her back next to my surfboard."

            lx "So, how’d I do? Pretty amazing, right?"

            "I try to think of a response, but instead of speaking, my mouth just hangs open in awe."
            show lexi mermaid smile
            lx "That good, huh? Don’t worry, that’s the normal reaction."
            hide mscmc
            hide lexi
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "She flashes me a charming smile, making it clear that she thinks she already won the competition."
            hide lexi
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mclexi "It was pretty cool, I guess, but it’s nothing compared to what I can do."
            show mscmc surfer_hairup_cu smile_cu at mscmc_cu
            "(I’ve got to play it off, just like I would at a surfing competition. I can’t let my opponent see me flustered!)"
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            "Lexi cocks her eyebrow at my nonchalant statement before turning upright."

            lx "Only pretty cool? You don’t have to lie, I know it was sick."
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "She grins in a way that lets me know she’s seen right through my facade and I shift on my board, mildly embarrassed."
            hide lexi
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            mclexi "Don’t get too full of yourself, yet. I’m not just going to roll over and let you win!"
            show mscmc surfer_hairup_cu angry_cu at mscmc_cu
            "(Okay, I’ve got to get it together. Got to impress the beautiful mermaid.)"
            hide mscmc
            "I look out onto the water and smile as I see a decent sized wave headed my way."
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mclexi "Prepare to be awed!"
            hide mscmc
            show mscmc surfer_hairup smile at centre:
                easein 0.2 yoffset -60
            stop music fadeout 1.0
            play music mscsurftraining

            "I start paddling and as the wave hits, I pop up on my board and instantly get a feel for the force under me."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "I can feel the power and weight behind it, and as I adjust my feet I look out and see Lexi waving at me."
            hide lexi
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "(Here goes nothing!)"
            hide mscmc
            show mscmc surfer_hairup smile at centre:
                yoffset -60
            "I lean into my bottom turn and gain momentum before shooting up the face of the wave and spinning my board in the air."

            "As I come back down the wave, I tailslide my board."
            show mscmc surfer_hairup smile at centre:
                easein 0.4 yoffset 60
            "Before doing another bottom turn, I crouch low and stare down the tube that the wave is beginning to form."

            "I ride the barrel, and as the water surrounds me I feel my heart race from the excitement."
            hide mscmc
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(But it feels different this time… Is it because I know Lexi is watching?)"
            hide mscmc
            "I almost slip on my board at the thought, but keep my balance, riding the wave out until it eventually collapses."
            show lexi mermaid_cu surprised_cu at lexi_cu
            lx "Okay, that was amazing. Not even because you’re a human, that was just all around..."
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            "She shakes her hands around her head as she squeals in excitement and I feel myself blushing at the praise."
            hide lexi
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mclexi "I’m glad you liked it. I just wish the wave had been bigger. Then I really would have blown your mind."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "No, but for real I’ve never seen anything like that before."
            hide lexi
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "I shrug, trying to play off just how happy Lexi’s praise is making me."
            hide mscmc
            show lexi mermaid_cu bigsmile_cu at lexi_cu
            lx "Without a doubt, you definitely get the coin."
            hide lexi
            show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
            "I look at the coin in my hand, my heart flutters at just how impressed Lexi is with me."
            hide mscmc
            show lexi mermaid_cu smile_cu at lexi_cu
            lx "Don’t get too attached to it, though. Next time I’m definitely going to win."
            hide lexi
            show mscmc surfer_hairup_cu grin_cu at mscmc_cu
            mclexi "You can try!"


        "B. Refuse Lexi's challenge.":
            $menuhideborder = False
            show mscmc surfer_hairup surprised at left3
            show lexi mermaid surprised at right3
            mclexi "You're crazy! You don't have anything to lose if we compete!"
            show mscmc surfer_hairup grin
            show lexi mermaid angry
            "I flip the coin into the air and catch it, playfully taunting Lexi before tucking the coin in the pocket of my wetsuit."
            show lexi mermaid smile
            lx "Fine, I'll just get it from you later somehow."
    hide mscmc
    hide lexi
    stop music fadeout 1.0
    play music mscsuspense

    show mscmc surfer_hairup surprised at left3
    show lexi mermaid surprised at right3
    mclexi "Do you hear that?"

    "Lexi and I both turn and look into the distance and to my surprise there's a massive yacht slowly approaching us."
    show lexi mermaid angry
    lx "Son of a lamprey! I know that boat."

    "She looks around shiftily and I can tell she's debating whether or not to bolt."
    show lexi mermaid sad
    lx "Gah! I can't leave. They're close enough they might have spotted us with binoculars. Just play it cool if they come over."

    mclexi "Whose yacht is it?"
    show lexi mermaid angry
    lx "We've run into one another before, and it was hard to explain how I was in the middle of the ocean without a boat."
    hide lexi
    hide mscmc
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(That makes sense. If I saw a random person swimming this far out without a boat or a board, I'd definitely be suspicious.)"
    hide mscmc
    show mscmc surfer_hairup surprised at left3
    show lexi mermaid surprised at right3
    "It doesn't take long for the yacht to reach us, and as Lexi and I look up, a familiar head leans over."
    hide mscmc
    hide lexi
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(I know this guy... He's that arrogant documentarian that blew Trina and I off at the surf shop the other day.)"
    hide mscmc
    show bg msc_yacht_day at bg with dissolve
    show ned vest basic at centre with dissolve
    stop music fadeout 1.0
    play music mscantagonist
    dt "Well what do we have here. Two beautiful ladies out in the middle of the ocean."

    "He looks us up and down, and I suddenly feel very uncomfortable."
    show ned vest angry
    dt "Wait a minute... Aren't you that stupid girl that took my last find?"
    show ned vest smile
    "He pauses and a malicious smile creeps onto his face."

    dt "Looks like you don't have a boat this time, either."
    hide bg yacht_day
    hide ned
    show bg msc_ocean_wide_day at bg
    show lexi mermaid_cu sad_cu at lexi_cu
    "Lexi looks away uncomfortably and I feel her tail press gently against my leg underneath my surfboard."
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Is she trying to tell me something?)"
    hide mscmc
    show bg msc_yacht_day at bg
    show ned vest basic at left3
    show diver suit basic snorkel at right3 with dissolve
    "As I try to understand the signal Lexi is trying to send me, a man in full snorkel gear and an underwater camera pops out from behind Ned."

    $sidecharone = "Cameraman"

    sid1 "Yeah, that's definitely her, boss. She's the one that we saw out in the middle of nowhere last year."

    sid1 "Remember, it was when she took that ship's wheel you found."
    show ned vest angry
    dt "It was a rhetorical question, dingus."
    hide bg yacht_day
    hide ned
    hide diver
    show bg msc_ocean_wide_day at bg
    show lexi mermaid_cu angry_cu at lexi_cu
    lx "First off, I found that ship's wheel first."

    "I turn back to Lexi to find that any apprehension she previously had is gone, replaced with a look of defiance that perfectly suits her."
    show lexi mermaid_cu smile_cu
    lx "And since I'm already here, I guess your go to plan is to just follow a real treasure hunter around and try to steal the loot."
    hide lexi
    show bg msc_yacht_day at bg
    show ned vest angry at left3
    show diver suit basic snorkel at right3
    "Ned's face burns red at the comment."

    dt "Whatever. As for you..."
    show ned vest smile
    "He looks at me and I immediately wish I could punch him in the face."

    dt "Why don't you ditch the thief and come join me and dingus here?"

    $sidecharone = "Dingus"

    sid1 "Yea, we're way cooler than..."

    "Ned rolls his eyes."
    show ned vest angry
    dt "Would you shut your idiot mouth already and make sure everyone is ready for the dive?"
    hide ned
    hide diver
    show bg msc_ocean_wide_day at bg
    $menuhideborder = True
    menu lexis0e1c3:
        "A. Comment on how he is treating his cameraman.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(Did he really just push that guy?)"
            hide mscmc
            show mscmc surfer_hairup angry at centre
            mclexi "Wow, yea. I definitely want to come up on the yacht after watching you bully your employee."
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest angry at left3
            show diver suit basic snorkel at right3
            dt "Maybe if he wasn’t such an idiot... Wait, I don’t owe you an explanation!"
            hide diver
            hide ned

        "B. Tell him what an entitled jerk he is.":
            $menuhideborder = False
            show mscmc surfer_hairup angry at centre
            mclexi "Yea, I don’t really like to hang with people that think they’re entitled to everything."

            mclexi "I bet you can only afford the yacht because you stole other people’s finds."
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest angry at left3
            show diver suit basic snorkel at right3
            "Ned’s lips purse at the accusation and I can tell I hit a sore spot."

            dt "I’ll have you know I’ve worked for everything I have!"
            hide ned
            hide diver

        "C. Ignore him to protect Lexi's secret.":
            $menuhideborder = False

            "I want nothing more than to tell Ned off, but I remind myself that Lexi is on the verge of being found out."
            show mscmc surfer_hairup basic at centre
            mclexi "I think I'm good here, thanks."
            hide mscmc
            show bg msc_yacht_day at bg
            show ned vest basic at left3
            show diver suit basic snorkel at right3
            "Ned cocks his eyebrow, his gaze falling on Lexi before coming back to me."

            dt "Come on, I'm way more fun than that loot poacher."
            hide ned
            hide diver
            show bg msc_ocean_wide_day at bg
            show mscmc surfer_hairup angry at centre
            mclexi "How about I..."
            hide mscmc
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "(Calm down. I can't go off on this idiot or else he might do something that will give away Lexi.)"
            show mscmc surfer_hairup smile at centre
            mclexi "Like I said, I'm fine here."
            hide mscmc

    show bg msc_yacht_day at bg
    show ned vest_cu basic_cu at ned_cu
    dt "Fine, if you want to stay with that little thief, so be it. But just know I'm looking into you, thief."
    show ned vest_cu smile_cu
    "He grins smugly at Lexi, and I can see in his eyes that he suspects something about Lexi."

    dt "Now the both of you clear out. If the green haired one is here, that means this is the perfect place to start looking for treasure."
    hide ned
    show bg msc_ocean_wide_day at bg
    show lexi mermaid_cu angry_cu at lexi_cu
    lx "Well the jokes on you then, because I'm not treasure hunting, I'm here to watch my girlfriend surf. So buzz off!"
    hide lexi
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Her what?!)"
    hide mscmc
    $tobecontinued()

    show msc_tbc at bg with fade
    pause
    $ resets()
