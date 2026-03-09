label arianna_season2_episode1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_day at bg
    play music mscbeach

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show arianna dress smile at centre
    "Arianna swings her legs over the boardwalk, ice cream cone in hand."
    ai surprised "I think I have an idea about getting my magic ring back from Camilla."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "She's been scheming since Mia was arrested. Camilla confiscated Arianna's ring that lets her go between human and mer form."
    show mscmc embarrassed_cu
    "(For the time being, Arianna's trapped as a human and honestly, I don't hate the forced proximity.)"
    show arianna dress grin behind mscmc at right1plus
    show mscmc jacket_hairdown smile at left1plus
    mcarianna "Oh?"
    show mscmc embarrassed
    show arianna surprised
    "A drop of melted ice cream from Arianna's cone drips onto her leg."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Her leg extends out of the slit in her dress and I want to wipe the ice cream off for her...)"
    show arianna dress smile behind mscmc at right1plus
    show mscmc jacket_hairdown embarrassed at left1plus
    "Arianna wipes away ice cream off her leg with the side of her hand and I try to get it together."
    show mscmc surprised
    ai grin "So, I'll need three strands of hair from Camilla, aragonite, and a shark tooth."
    hide mscmc
    hide arianna

    $ menuhideborder = True
    menu ariannas2e1c1:
        "A. Okay, hold on.":
            $ menuhideborder = False
            show arianna dress smile at right1plus
            show mscmc jacket_hairdown grin at left1plus
            "I put my hand up"
            show arianna sad
            mcarianna "I feel like you jumped five steps ahead."
            ai grin "Hear me out."
        "B. Camilla's hair?":
            $ menuhideborder = False
            show arianna dress sleep at right1plus
            show mscmc jacket_hairdown surprised at left1plus
            mcarianna "How the hell are we supposed to get Camilla's hair?"
            ai grin "We'll figure something out."
            show mscmc grin
            "I roll my eyes at her good-naturedly."
        "C. It already sounds crazy.":
            $ menuhideborder = False
            show arianna dress surprised at right1plus
            show mscmc jacket_hairdown surprised at left1plus
            mcarianna "It already sounds crazy."
            show mscmc smile
            ai grin "Can I continue please?"
            show mscmc basic
            "I sigh."
            mcarianna grin "Go on."

    show arianna smile
    show mscmc embarrassed
    "Arianna languidly licks the spire of ice cream in her hand and I try to act natural."
    show mscmc surprised
    ai grin "I'll go to an underwater volcano-there's one not too far from here."
    ai "Then, I'll throw in Camilla's hair first and say-"
    mcarianna "Is this a spell or something?"
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's joking about all this, right?)"
    show arianna dress grin behind mscmc at right1plus
    show mscmc jacket_hairdown surprised at left1plus
    ai "No, I can't do magic which is {i}why{/i} I need the magic shark tooth I mentioned."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Silly me. Can't believe I forgot the magic shark tooth."
    show arianna dress surprised behind mscmc at right1plus
    show mscmc jacket_hairdown smile at left1plus
    mcarianna "Is that really the only way to get your tail back?"
    show mscmc surprised
    ai basic "No...it's not...I can just call my grandma."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Right! Her grandma's a sea witch who made her the original magic ring that she needs to replace.)"
    show arianna dress sad behind mscmc at right1plus
    show mscmc jacket_hairdown basic at left1plus
    "Arianna sighs loudly and leans back on one hand."
    show mscmc surprised
    ai "I didn't want to call her."
    show arianna surprised
    mcarianna basic "Gonna get in trouble for hanging out with a human?"
    show mscmc smile
    show arianna grin
    "I prod her side with a finger and she giggles."
    show mscmc basic
    ai sad "No, it's actually because she's going to give me a hard time about losing the ring."
    show mscmc surprised
    ai embarrassed "I...lose stuff a lot, actually, and my family likes to joke about it."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(That actually doesn't surprise me about her.)"
    show arianna dress grin behind mscmc at right1plus
    show mscmc jacket_hairdown surprised at left1plus
    ai "Oh, you can meet her! She can be a bit strict, but she's a lot of fun."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Meeting Arianna's grandma? It sounds like they're close.)"
    show arianna dress smile behind mscmc at right1plus
    show mscmc jacket_hairdown embarrassed at left1plus
    mcarianna "What're you gonna tell her about us? Uh, I mean, me."
    ai embarrassed "I'll tell her we're {i}really{/i} good friends."
    show mscmc sleep
    show arianna smile
    "(Is that all that I am?)"
    show mscmc smile
    show arianna grin
    "But the fire in Arianna's eyes brings me back from my worries."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I'm overthinking things.)"
    show arianna dress grin behind mscmc at right1plus
    show mscmc jacket_hairdown surprised at left1plus
    ai "{i}And{/i} I'm definitely going to tell her that you recently saved my life."
    show arianna embarrassed:
        easein 0.4 right1
    show mscmc embarrassed
    "Arianna takes one of my hands in both of hers and gives it a soft squeeze while she looka at me sweetly."
    show mscmc surprised
    ai surprised "You know, she might even give {i}you{/i} a magic item. She makes them herself."
    show arianna grin
    mcarianna "Wait, really?! She might give me a magic token?"
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(A magic item of my own? Maybe it would be one that would let me have a mermaid tail.)"
    show arianna dress grin behind mscmc at right1
    show mscmc jacket_hairdown grin at left1plus
    ai "Grandma loves giving gifts. I don't know, it's her thing."
    show mscmc smile
    ai surprised "You know, there's an old traditional way merfolk have of thanking an elder for a gift."
    show arianna grin
    mcarianna grin "Like a ritual?"
    ai "Yeah! Can I show you? It would make my grandma happy if the chance ever came up and you busted it out."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I'll do whatever to make a good impression on Arianna's family!)"
    show arianna dress embarrassed behind mscmc at right1
    show mscmc jacket_hairdown grin at left1plus
    mcarianna "Totally! What do I do?"
    hide arianna
    hide mscmc
    "Arianna picks up a shell in the sand and holds it out to me."
    show arianna dress grin behind mscmc at right1
    show mscmc jacket_hairdown surprised at left1plus
    ai "Pretend this is a gift. Give it to me."
    show mscmc smile
    "I do as she says."
    hide mscmc
    hide arianna
    "She takes the shell with both her hands and bows her head as she holds it out."
    show arianna dress_cu grin_cu at arianna_cu
    ai "This shows respect towards the one giving it to you."
    show arianna sleep_cu
    "Then she raises the shell slightly over her head."
    show arianna grin_cu
    ai "The accepting of the item from the one it once belonged to."
    show arianna dress sleep at centre
    "She pulls the shell to her chest, holding it just below her neck."
    ai grin "And now the item belonging to you."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Okay, I can definitely do that!)"
    show arianna dress grin behind mscmc at right1plus
    show mscmc jacket_hairdown embarrassed at left1plus
    "Arianna bows her head at me again then breaks character as she tosses the shell with a laugh."
    show mscmc smile
    ai "Alright, let's get this phone call to Grandma Queenie over with."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I hope Arianna's grandma likes me. I get to meet another mermaid!)"

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_tide_pools_day at bg with clockwise_wipe
    "On a brief phone call, Arianna and her grandmother agreed for us all to meet at the tidepools later that day."
    "Finally, it's time and we go to the agreed upon location. The sky is blue and clear and the water is calm today."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I didn't think I'd be meeting her grandma today! I hope she's cool.)"
    show arianna dress smile behind mscmc at right1
    show mscmc jacket_hairdown embarrassed at left1
    "Arianna sets a hand on my shoulder and it feels reassuring and intimate as she moves to stand closer to me."
    show mscmc smile
    ai "Are you nervous?"
    show arianna grin
    mcarianna basic "A little."
    show mscmc embarrassed
    ai "Awww, you have nothing to fear, my human."
    "Her hand trails down my bicep before she points to the water."
    show mscmc surprised
    ai "There she is!"

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    hide arianna
    hide mscmc
    show queenie casual smile at centre
    "The head of an older woman surfaces and she waves towards us with a warm smile."
    hide Queenie
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Grandma Queenie!)"
    hide mscmc
    show queenie casual smile at centre
    "The tip of a tail that ends in many thin long fins pokes out near where her head has surfaced."
    hide queenie
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(God, all mermaids just have such beautiful tails!)"
    show arianna dress grin behind mscmc at right1
    show mscmc jacket_hairdown smile at left1
    ai "Grandma Queenie!"
    "Arianna leaves my side as she goes over to the edge of the tide pools."
    hide arianna
    hide mscmc
    show queenie casual_cu smile_cu at queenie_cu
    "Arianna's Grandma" "Arianna!"
    show queenie casual smile at left1plus
    show arianna dress grin at right1plus
    "I follow awkwardly while Arianna bends down to hug Queenie."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She looks like a really cool grandma.)"
    hide mscmc
    show queenie casual sad at left1plus
    show arianna dress surprised at right1
    qn "Calling me up only when you need something?"
    show queenie smile
    ai grin "I would never! I love seeing you."
    show arianna basic
    "Arianna's grandma pinches her cheek before looking over to me."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Gotta make a good impression on the family!)"
    show mscmc jacket_hairdown smile at left4
    show queenie casual smile at centre behind mscmc
    show arianna dress grin at right4
    qn "You must be [genericfn]."
    show arianna smile
    mcarianna grin "Hello."
    qn "Call me Queenie, dear."
    show arianna grin
    show queenie basic
    "Queenie rests her arms on the edge of the tide pools as she looks at us."
    qn smile "Pardon me for coming without my legs, but I had more than enough time on land in my wild youth."
    show mscmc surprised
    show arianna basic
    qn "And far too many stories from '69. Humans know how to throw a music festival."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Was she at Woodstock?)"
    show mscmc jacket_hairdown grin at left4
    show queenie casual smile at centre behind mscmc
    show arianna dress grin at right4
    "Arianna taps her fingers together and grins largely at Queenie."
    show mscmc smile
    show queenie basic
    ai smile "Do you have another ring for me, maybe?"
    show mscmc surprised
    show arianna basic
    qn sleep "Arianna, you need to keep better track of your things."
    show mscmc grin
    qn basic "They're not infinite, you know."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Arianna really does lose things a lot!)"
    show mscmc jacket_hairdown smile at left4
    show queenie casual smile at centre behind mscmc
    show arianna dress grin at right4
    "Queenie opens her palm to Arianna and in her hand is a ring."
    qn basic "Here you are."
    show queenie smile
    ai "Thank-"
    show mscmc surprised
    show queenie basic
    show arianna sad
    "Queenie closes her hand and pulls it away from Arianna, fixing her with a stern look."
    hide mscmc
    hide arianna
    show queenie casual_cu angry_cu at queenie_cu
    qn "Don't lose it."
    hide queenie
    show arianna dress_cu sleep_cu at arianna_cu
    ai "I wont."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I'm seeing a different side of Arianna with her grandma...How is she always achieving new levels of cuteness?)"
    hide mscmc
    show queenie casual smile at left3
    show arianna dress grin at right1
    "Queenie shakes her head as she hands the ring to Arianna who's looking overjoyed to have it."
    hide arianna

    stop music fadeout 0.5
    play music mscmagicartifact fadein 1.0
    show mscmc jacket_hairdown surprised at left1plus behind queenie
    show queenie at right1
    qn "And this is for you."
    "Queenie gives me a warm look and then reaches under the water."
    qn basic "This is for saving my granddaughter's life."
    show queenie smile
    "She pulls up a small, smooth seashell with a red glow around it."
    hide queenie
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Oh my god!!!!!! That is totally a magical shell. This is so awesome!)"
    show mscmc grin_cu
    "(Tail. Please give me a mer form.)"
    hide mscmc
    show queenie casual_cu smile_cu at queenie_cu
    qn "This allows you to speak and breathe underwater."
    "She closes my hands around it and gives me a good pat."
    hide queenie
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Breathe and speak UNDERWATER? Oh! Now would be a good time to do the \"thank you\" ceremony Arianna showed me.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna bumps me with her shoulder and nods to her grandma."
    hide arianna

    $ menuhideborder = True
    menu ariannas2e1c2:
        "A. Make a good impression on Arianna's grandma!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mschappytimes fadein 1.0
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Okay, now's my time to shine. Just like how Arianna showed me.)"
            show mscmc jacket_hairdown grin at left4
            show queenie casual basic at centre behind mscmc
            show arianna dress grin at right4
            "I take the shell and hold it out with my hands, bowing my head."
            qn smile "Is this what I think it is?"
            ai "She's a natural."
            mcarianna embarrassed "You guys are making me nervous."
            qn "Let the girl do her thing, Arianna."
            show mscmc sleep
            "Then I hold the shell above my head."
            hide queenie
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Portraying the separation of the shell from Queenie.)"
            show mscmc jacket_hairdown grin at left4
            show queenie casual smile at centre behind mscmc
            show arianna dress grin at right4
            "I try to ignore the way Arianna looks like she can barely stand still."
            hide queenie
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Okay and now to show that it's mine.)"
            show mscmc jacket_hairdown sleep at left4
            show queenie casual sleep at centre behind mscmc
            show arianna dress grin at right4
            "I close my hands tighter around the shell and pull it to my chest."
            show queenie smile
            mcarianna grin "Thank you."
            show mscmc sleep
            show queenie sleep
            "As I say that, I bow my head again."
            hide queenie
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Nailed it!)"
            show mscmc jacket_hairdown embarrassed at left4
            show queenie casual smile at centre behind mscmc
            show arianna dress grin at right4
            "Queenie claps softly and nods at Arianna."
            qn "My, my. I must say that I'm impressed!"
            show mscmc grin
            qn "You've made an old mermaid very happy."
            hide queenie
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "I feel like a kid who just performed at the school talent show."
            "(I'm glad Arianna showed me that--Queenie looks delighted!)"
            show mscmc jacket_hairdown embarrassed at right1plus
            show arianna dress grin behind mscmc at left1plus:
                pause 0.1
                easein 0.5 left1 xoffset 60
            "Arianna wraps her arms around me and pulls me into a beautifully suffocating hug."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(There are times when I love being short and being chest level with Arianna is one of them.)"
            show arianna dress grin behind mscmc at left3
            show mscmc jacket_hairdown embarrassed at left1:
                xoffset 40
            show queenie casual basic at right4
            ai "See? Isn't she great, grandma?"
            show queenie smile
            "Arianna steps behind me, her arms thrown over my shoulders."
            hide arianna
            hide queenie
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(I can feel her heartbeat against my back.)"
            show arianna dress grin behind mscmc at left3
            show mscmc jacket_hairdown smile at left1:
                xoffset 40
            show queenie casual basic at right4
            mcarianna "Arianna told me about the ceremony."
            mcarianna grin "I wanted to properly express my thanks, this means a lot to me."
            "I turn the glowing red shell over in my hands and feel giddy."
            hide arianna
            hide queenie
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu:
                xoffset 0
            "(I can go in Arianna's underwater ship-wreck art studio now!)"
            show arianna dress grin behind mscmc at left3
            show mscmc jacket_hairdown grin at left1:
                xoffset 40
            show queenie casual smile at right4
            ai "I may have told [genericfn] that you would bring her something."
            qn "What can I say? I take care of my girls."
            ai smile "Hear that, my human? You're one of her girls now."
            show arianna surprised
            show mscmc smile
            "Arianna seems to realize that she called me by a cute nickname in front of her grandma and stops."
            show arianna embarrassed
            show mscmc embarrassed
            "She pushes her hair behind her ears and ducks her head slightly as Queenie chuckles."
            qn "Oh, is that what you call [genericfn], Arianna? You two are pretty cute, I must say."
            hide arianna
            hide queenie
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "A blush burns across my face."
            hide mscmc
            show arianna dress_cu basic_cu at arianna_cu
            ai "She {i}is{/i} my favorite human."
            hide arianna
            show queenie casual_cu smile_cu at queenie_cu
            qn "I see."
            hide queenie
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I hope that Arianna never stops calling me her favorite human.)"
            show mscmc jacket_hairdown grin at left1plus
            show arianna dress grin behind mscmc at right1plus
            ai "And now we can do all sorts of stuff together, underwater! You're going to be on my turf now!"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I can't wait for Arianna to show me more of her world!)"
            show mscmc jacket_hairdown smile at left1plus
            show queenie casual smile at right2
            qn "[genericfn], you really were a natural with that ritual."
            qn "It dates back many centuries in our culture."
            show mscmc surprised
            qn "I'm surprised a human captured the flow of feeling for it so well. It's more than the movements."
            show mscmc smile
            qn "It's about the meaning."
            hide mscmc
            show arianna dress smile behind queenie at left1
            "Queenie wags a finger at Arianna."
            show arianna surprised
            qn basic "She's a keeper, Arianna. This human of yours."
            hide arianna
            hide queenie
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(That sounds a lot like grandma's approval.)"
            show mscmc embarrassed_cu
            "(Not that I'm asking for Arianna's hand or anything, but it does feel nice.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna looks at me with a soft smile and I melt."
            ai "Trust me, I already know."
            ai smile_cu "She saved my life {i}and{/i} my grandma likes her."
            ai grin_cu "She's special for sure."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I want to grab her and kiss her right here.)"
            hide mscmc
            show queenie casual_cu smile_cu at queenie_cu
            "Queenie chuckles."
            hide queenie
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Oh right, her grandma's here...)"
            show mscmc jacket_hairdown basic at left1plus
            show queenie casual smile at right2
            "Queenie looks at me, a hand on one side of her mouth."
            qn basic "Arianna's right though, I am hard to please."
            mcarianna grin "Then I must be lucky."
            qn "It's not about luck, dear."
            hide mscmc
            show queenie casual_cu smile_cu at queenie_cu
            "Queenie winks at me."

        "B. You're too nervous.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(There weren't that many steps in the ritual, but oh god, I just forgot all of them.)"
            show mscmc jacket_hairdown sad at left4
            show queenie casual basic at centre behind mscmc
            show arianna dress grin at right4
            "I look down at the shell and feel myself choking on what to do."
            show arianna smile
            mcarianna smile "Thank you."
            show mscmc basic
            show queenie smile
            show arianna grin
            "Arianna steps up beside me and bows her head, outstretching her hands and then pulling them back in."
            hide queenie
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Arianna's covering for me because I didn't do any of the ritual. I messed up.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Thank you, grandmother."
            hide arianna
            show queenie casual_cu smile_cu at queenie_cu
            "Queenie gives me an understanding smile."
            qn "You're very welcome, both of you."

    show mscmc jacket_hairdown basic at left4
    show queenie casual basic at centre behind mscmc
    show arianna dress basic at right4
    "As I slip the shell into my pocket, Queenie turns to Arianna."
    show mscmc surprised
    qn "Arianna, it's your turn on the project. We're almost there. We need your focus back on the resistance."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Project? Resistance? Arianna did say she was part of an artist resistance group that opposed the government.)"
    show mscmc jacket_hairdown surprised at left4
    show queenie casual basic at centre behind mscmc
    show arianna dress basic at right4
    qn "We need you to finalize the installation you designed, and you'll need to stay under the radar while you do."
    qn "Neptria will fill you in on everything."
    ai grin "Oh, Neptria's working with us again? That's cool."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I am...so very lost.)"
    show mscmc jacket_hairdown surprised at left4
    show queenie casual basic at centre behind mscmc
    show arianna dress smile at right4
    "Queenie then looks back to me."
    show arianna surprised
    qn "Maybe you're just hanging around because you have a crush on my granddaughter."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She does not hold back!)"
    show mscmc jacket_hairdown embarrassed at left4
    show queenie casual basic at centre behind mscmc
    show arianna dress embarrassed at right4
    "I know my face is bright red and I can't bring myself to look at Arianna."
    show mscmc surprised
    show arianna sleep
    qn smile "But, you know, we could use your help in the resistance too."
    show arianna embarrassed
    qn basic "The mer world can use all the help it can get right now."
    show arianna surprised
    qn smile "And, who knows, maybe there will be a mer form in it for you too."
    hide queenie
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(A mer form!)"
    show mscmc jacket_hairdown surprised at left4
    show queenie casual smile at centre behind mscmc
    show arianna dress grin at right4
    qn "Now, I've got to get back. Love you, Arianna. Keep an eye out for Neptria."
    show mscmc smile
    ai grin "Love you too. See you soon!"
    show mscmc embarrassed
    show queenie:
        pause 0.2
        transform_anchor True zoom 0.8 alpha 0.8 xoffset 100 yoffset 80
        parallel:
            easein 0.5 xoffset 0
        parallel:
            easein 0.5 yoffset 200 knot -100 knot 200
        parallel:
            linear 0.5 alpha 0.0 zoom 0.7
    "Queenie ducks under the water and disappears, and Arianna and I are alone at the tide pools."
    hide arianna
    hide queenie
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(A lot of stuff just happened. Resistance. Project. Someone named Neptria. A magic shell!)"
    show mscmc jacket_hairdown surprised at left1
    show arianna dress embarrassed behind mscmc at right1plus
    "Arianna laughs and fiddles with her necklace."
    show mscmc embarrassed
    ai "You know, when she said you have a crush on me...she just likes to joke around."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Yeah. A joke...)"
    show mscmc jacket_hairdown grin at left1
    show arianna dress embarrassed behind mscmc at right1plus
    mcarianna "Oh, yeah I could tell. Ha ha. She's...funny."
    show mscmc embarrassed
    "I rub at the back of my neck knowing full well I must be red as a berry."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I guess Queenie is perceptive.)"
    show mscmc jacket_hairdown embarrassed at left1
    show arianna dress embarrassed behind mscmc at right1plus
    "Arianna's cheeks are pink as she drops her gaze."
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Whenever she wants to talk about us, I'm here for it.)"
    show mscmc jacket_hairdown surprised at left1
    show arianna dress basic behind mscmc at right1plus
    mcarianna "So what's with this resistance project thing you need to work on?"
    show arianna surprised
    mcarianna smile "I want to help, I believe in what you're fighting for in your world."
    show arianna grin
    "Arianna motions for me to follow her back towards the boardwalk, the sun setting at our backs."
    show bg msc_boardwalk_sunset_people at bg with clockwise_wipe
    ai surprised "Well, you know how I said that magic and art are closely linked in our society."
    ai basic "The resistnace is mostly artists and magic users, outcasts but also anyone who's interested."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Does that ever include some humans?)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress basic behind mscmc at right1plus
    ai "As you saw when Camilla took my ring, the government hoards magic."
    show mscmc surprised
    ai angry "We're working against that--the draconian control of magic and self-expression."
    show arianna basic
    "As Arianna speaks, she gestures a lot with her hands."
    mcarianna "So, what's the project you're doing for the resistance?"
    show mscmc smile
    ai grin "Basically, we're making a huge installation art piece."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Very cool, and very Arianna.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress grin behind mscmc at right1plus
    ai "Pieces of the sculpture are imbued with magic and anyone can take those detachable pieces home with them."
    mcarianna surprised "You're giving magic back to the people?"
    ai "Yes! And this stuff can't be traced, so it's safe."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I'm assuming the magic items that we have also can't be traced.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress basic behind mscmc at right1plus
    ai "This type of magic that we're distributing cancels out the surveillance magic the government uses."
    show arianna grin
    mcarianna grin "Right on."
    show mscmc embarrassed
    show arianna embarrassed:
        easein 0.4 right1
    "Arianna puts her arm through mine and presses herself against my side."
    ai grin "I've got to finish making the detachable parts of the sculpture, so I've got a lot to do."

    scene bg msc_surf_shop_night at bg with fade
    "The sun is down when we get back to the surf shop and Trina is on her way out."
    show trina casual smile at centre
    so "Oh, hey! I'm taking off. I need a drink!"
    show trina:
        linear 0.5 xoffset 100 alpha 0.0
    "Trina throws a wave over her shoulder."
    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    "Arianna and I have just settled in when the bell over the shop door rings."
    show neptria casual basic at centre with dissolve
    "A beautiful woman dressed in alt black clothes, with spiked hair walks into the shop purposefully."
    show neptria smile
    "Oh wow, who is she?!" "This is where you've been hiding out?"
    show arianna dress grin at left2
    show neptria at right3
    ai "Nice, right?"
    hide arianna
    hide neptria
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Ohhh, she knows Arianna. Is this Neptria?)"
    hide mscmc
    show arianna dress grin at left2
    show neptria casual smile at right3
    "Really cool goth girl" "Sure. If you're a {i}human{/i}. I prefer darker places."
    "She talks with a dry tone and a blank expression, but there's also a sardonic quirk to her lips."
    hide arianna
    hide neptria
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Ok, she's cool.)"
    show mscmc casual_hairdown smile at left3
    show arianna dress grin behind mscmc at right1
    show neptria casual basic at right5
    ai "[genericfn], this is Neptria. She works with the resistance...sometimes."
    mcarianna grin "Nice to meet you."
    "Neptria takes a moment to look me over and her eyes meet mine briefly before she shrugs."
    nt "Ditto."
    hide mscmc
    hide arianna
    show neptria casual basic at centre
    "Neptria walks up to the counter, the chains on her belt jingling."
    nt "You need to see this."
    hide neptria
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(Straight to the point.)"
    hide mscmc
    "Neptria leans her upper half on the counter as she pulls out a human smartphone."
    "She clicks play on a video she has pulled up."
    show mscmc casual_hairdown basic at left3
    show arianna dress basic behind mscmc at right1
    show neptria casual smile at right5
    nt "The resistance hacked into Maritas security footage."
    "The video is grainy and black and white, it was taken at night and there's a merman pulling down a statue of a coral."
    nt basic "This is Casper, an extremist, or {i}patriot{/i}, who's been sabotaging resistance efforts."
    hide mscmc
    hide arianna
    hide neptria
    "The video ends with the man seeming visibly worked up and distressed."

    $ menuhideborder = True
    menu ariannas2e1c3:
        "A. Are there a lot of people like him?":
            $ menuhideborder = False
            show arianna dress basic at centre:
                xoffset 30
            show mscmc casual_hairdown surprised at left3
            show neptria casual basic at right4
            mcarianna "Are there a lot of extremists that side with the government?"
            show arianna angry
            nt "No, but a lot of mer support the government."
        "B. Is he dangerous?":
            $ menuhideborder = False
            show arianna dress basic at centre:
                xoffset 30
            show mscmc casual_hairdown surprised at left3
            show neptria casual basic at right4
            mcarianna "Is he...dangerous?"
            nt "He's confused."
            ai angry "But, we don't really know what he's capable of."
        "C. Has anyone tried to stop him?":
            $ menuhideborder = False
            show arianna dress basic at centre:
                xoffset 30
            show mscmc casual_hairdown surprised at left3
            show neptria casual basic at right4
            mcarianna "Has anyone tried to stop him before?"
            nt smile "You mean our illegal resistance?"
            show neptria basic
            ai angry "We have to be careful. We could get arrested. He has the powers that be on his side."

    show mscmc basic
    nt smile "He's been fed lies his whole life. He thinks he's doing what's right."
    show mscmc surprised
    show arianna basic
    nt basic "Queenie told you about meeting with him, right Arianna?"
    hide arianna
    hide neptria
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(She's going to meet with {i}that{/i} guy?!)"
    show arianna dress angry behind mscmc at centre:
        xoffset 30
    show mscmc casual_hairdown sad at left3
    show neptria casual basic at right4
    ai "Yeah. We're hoping that we can get him onto our side if we explain some things. Deprogram him."
    hide neptria
    show mscmc casual_hairdown surprised at left1
    show arianna dress smile at right1plus:
        pause 0.1
        easein 0.4 right1
    "Arianna takes both my hands and holds them close to her as she addresses me."
    show mscmc basic
    ai "My grandma told you that she wants you to help with the resistance."
    show mscmc grin
    ai grin "Help me build this sculpture for my people."
    hide arianna
    hide mscmc
    show neptria casual_cu smile_cu at neptria_cu
    "Neptria looks at me with a very small spark of interest for the first time, and puts a hand on her hip."
    hide neptria
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Am I ready to join a mermaid resistance group and fight their government?)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "You in?"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
