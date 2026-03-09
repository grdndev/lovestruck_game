label arianna_season2_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_sunset at bg
    play music mscsuspense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(How did Casper even get this shell phone number? I thought only Arianna knew about this phone.)"
    show arianna bikini surprised at right1plus behind mscmc
    show mscmc bikini_hairdown surprised at left1
    mcarianna "Oh, Casper. Hey."
    show arianna angry
    "I emphasize his name to Arianna and she frowns."
    hide mscmc
    hide arianna
    cs "I want to meet with you."
    show arianna bikini sad at right1plus
    show mscmc bikini_hairdown surprised at left1
    mcarianna "You want to meet with me?"
    show arianna angry:
        easein 0.4 xoffset -95
    "Arianna presses herself into my side, trying to listen in."
    hide arianna
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(Arianna is definitely not syked about this.)"
    hide mscmc
    cs "You grew up outside of mer society, outside of our world, yet you still side with the resistance."
    cs "You're a human and yet, you care about us, uh merpeople."
    "He pauses and I try not to get distracted by the smell of Arianna's hair as I handle a possibly very important call."
    cs "I'll be at the tide pools at midnight, two days time."
    cs "I'm not sure I can trust Arianna or Queenie. You need to show up alone if they want anything from me."
    show mscmc bikini_hairdown_cu angry_cu at mscmc_cu
    "(Alone? I {i}just{/i} joined the resistance and he is intense.)"
    show arianna bikini angry at centre behind mscmc:
        xoffset 55
    show mscmc bikini_hairdown angry at centre:
        xoffset -60
    mcarianna "Okay..."
    hide arianna
    hide mscmc
    cs "If you don't show up alone, I'll know I can't trust any of you."
    "The line goes dead."

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna bikini angry at right1
    show mscmc bikini_hairdown sad at left1
    ai "I don't like it."
    mcarianna "Casper asked me to meet him alone to talk. Alone."
    show mscmc basic
    ai sad "When?"
    mcarianna "Two days."
    show arianna sleep
    "Arianna sucks in a breath and shakes her head."
    hide mscmc
    hide arianna

    $ menuhideborder = True
    menu ariannas2e5c1:
        "A. I know this isn't ideal...":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
            "(It's no secret that Arianna isn't Casper's biggest fan.)"
            show arianna bikini basic at right1 behind mscmc
            show mscmc bikini_hairdown basic at left1
            mcarianna "You don't like it."
            ai sleep "I don't."
        "B. Should I go?":
            $ menuhideborder = False
            show arianna bikini basic at right1
            show mscmc bikini_hairdown basic at left1
            mcarianna "What do you think?"
            show arianna angry
            "Arianna pinches the edge of her nose."
            ai sleep "I don't know...I don't want you alone with him."
        "C. Do you think he's lying about wanting to talk?":
            $ menuhideborder = False
            show arianna bikini basic at right1
            show mscmc bikini_hairdown basic at left1
            mcarianna "Do you think it's some kind of set-up?"
            show arianna sleep
            mcarianna "Casper seemed genuinely reflective when he left your studio, but he's hard to read."
            ai "We don't know enough about him. Who knows what he's up to?"

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    ai smile "Regardless, I do need to go brief Grandma Queenie about that phone call."
    mcarianna smile "Okay. You going now?"
    show arianna:
        linear 0.5 alpha 0.0 xoffset 100
    "Arianna nods at me and then grabs my hand sending tingles up my arm as she stands and walks back towards the vast ocean."
    hide mscmc
    show arianna bikini embarrassed at centre:
        alpha 1.0 xoffset 0
    ai "Meet me at Jerry's in an hour? You owe me a beer."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    mcarianna "No, you owe {i}me{/i} a beer."
    hide mscmc
    show arianna bikini grin at right1:
        transform_anchor True zoom 0.85 yoffset 30
    ai "Whatever you say. As long as you and me are sipping beers in one hours time, it's all good."
    play sound splash03
    show arianna embarrassed:
        parallel:
            easeout_back 0.4 yoffset 300
        parallel:
            easein 0.4 xoffset 60
        parallel:
            linear 0.4 alpha 0.0
    "She turns and slinks into the water on her neverending legs, then shoots me one last angelic look over her shoulder before diving under."
    hide arianna
    show mscmc bikini_hairdown_cu sleep_cu at mscmc_cu
    "(Does Casper really want to hear {i}my{/i} thoughts on the resistance?)"

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    scene bg msc_beach_bar_sunset at bg with clockwise_wipe
    "I go to Jerry's, to kill time while Arianna updates Queenie, and sit at the counter."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Will Queenie want me to meet with Casper? Do I want to?)"
    show jerry casual smile at left4
    show mscmc jacket_hairdown basic at right4
    "Jerry shoots finger guns at me when he sees me."
    show mscmc smile
    jr "Let me guess, a beer?"
    mcarianna grin "I'll do some coconut water to start, thanks."
    hide jerry
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I know Arianna was shook up by Casper calling my shell phone. She doesn't trust him, I don't exactly trust him either, but.)"
    show jerry casual sad at left4
    show mscmc jacket_hairdown surprised at right4
    "Jerry's face softens and he rests his elbows across from me."
    jr basic "How'd your girl stuff work out?"
    show jerry smile
    mcarianna smile "Oh, what? Uh, fine. Arianna'll be coming through later."
    hide jerry
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Maybe Jerry can give me some input on this resistance and Casper thing.)"

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    show jerry casual smile at left4
    show mscmc jacket_hairdown surprised at right4
    mcarianna "Can I ask you something?"
    show mscmc smile
    jr "What's up?"
    show jerry basic
    mcarianna basic "You work at a bar. You get all kinds of people coming here."
    "Jerry nods along as I figure out what I'm trying to ask."
    show jerry smile
    mcarianna "Out of all those people...how do you know who you can trust? Or, who's going to be trouble?"
    show mscmc smile
    "Jerry raises a brow at me but smiles at the same time so I know he's not judging me."
    mcarianna basic "This is all hypothetical, of course."
    "He's clearly unconvinced, but plays along as he leans back to think."
    jr basic "Well, being a bartender, a lot of customers open up to you."
    jr "When they're alone or troubled, I'm an unbiased, in most cases, third party they can talk to."
    mcarianna smile "I'm a prime example right now, asking you for advice."
    "Jerry hums to himself and gives me a bit of a harder look than usual."
    jr "You should trust everyone when you first meet them unless your gut gives you a reason not to."
    hide jerry
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(There are already reasons to doubt Casper.)"
    show jerry casual smile at left4
    show mscmc jacket_hairdown smile at right4
    jr "When people feel trust from you, they're more likely to be real with you, comfortable."
    jr "Decide where boundaries should be set once you see their true selves and intentions."
    show mscmc grin
    jr "You should assume the best in people cause you can always shut it down real quick after that if you pick up bad vibes."
    hide jerry
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Jerry might be on to something. I want to give Casper the benefit of the doubt.)"
    show jerry casual basic at left4
    show mscmc jacket_hairdown smile at right4
    "Jerry puts his hands down on the counter and looks into my eyes."
    jr smile "And the same goes for love. Dive in cause you can always bail later if things go south."
    hide jerry
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Love? Is he talking about Arianna and me?)"
    hide mscmc
    show arianna dress grin at centre
    ai "Hey!"

    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show mscmc jacket_hairdown embarrassed at left1
    show arianna dress grin at right1 behind mscmc:
        xoffset 100 alpha 0.0
        pause 0.1
        linear 0.5 xoffset 0 alpha 1.0
    "Arianna comes up beside me, running her hand over my back as she sits and scooches her stool closer to mine."
    hide mscmc
    hide arianna
    show jerry casual smile at centre:
        pause 0.1
        linear 0.5 xoffset -100 alpha 0.0
    jr "Let me know if y'all need anything."
    hide jerry
    show arianna dress sad at right1
    show mscmc jacket_hairdown embarrassed at left1
    "As Jerry leaves to attend to other customers, Arianna sighs."
    mcarianna surprised "What did your grandma say?"
    ai basic "She's all for it, but she thinks it's up to you...I still don't like it."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Arianna got really blindsided by the whole 'Emporia is Mia' thing. I think she trusts less easily now.)"
    show arianna dress basic at right1 behind mscmc
    show mscmc jacket_hairdown smile at left1
    mcarianna "I know, but he could be of use to the resistance and I really don't think he means to hurt me...at this point."
    show arianna smile
    mcarianna "I think we should try."
    ai "Thank you for helping the resistance. I'm going to make you take this to your meeting with him though."
    "Arianna holds out a small, silver whistle engraved with delicate waves on a silver chain."
    ai "If you blow this, I hear it no matter where you are, even if one or both of us is underwater. I asked Queenie to magic it for us."
    show arianna embarrassed
    mcarianna embarrassed "I love this whistle. You are going to hear this thing going off all the time. Kidding, thank you, Arianna."

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    scene bg msc_tide_pools_night at bg with clockwise_wipe
    "Finally, night falls on the day I'm supposed to meet Casper and I'm ready at the tide pools, my silver whistle in my pocket."
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(I hope this goes well. I know Arianna is worried as hell right now.)"
    show mscmc jacket_hairdown sleep at centre
    "I play with the whistle in my pocket between my fingers and take a deep breath."
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(I don't exactly want to be alone with Casper, but I want to help the resistance. And I think I can do this.)"
    hide mscmc
    "I scan the dark water, looking for any sign of him."
    "The longer I wait, the more jumpy I get, listening to the sounds of the coast at night."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Maybe he isn't coming?)"
    hide mscmc
    show casper casual basic at centre:
        yoffset 530
        pause 0.1
        easein_back 0.7 yoffset 200
    "Then, Casper's head surfaces a little ways from the lip of the rocky pools."
    hide casper
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "I tell myself that I'm calm but I can feel my heart beating in my chest."
    show mscmc smile_cu
    "(Okay. Just got to talk to him about why hoarding power and suppressing personal expression is bad.)"
    show mscmc jacket_hairdown basic at left3
    show casper casual basic at right3:
        xoffset 300 yoffset 400 alpha 0.0
        pause 0.1
        parallel:
            easein_back 0.7 yoffset 200
        parallel:
            ease 0.7 xoffset 0
        parallel:
            linear 0.7 alpha 1.0
    "He swims forward as he looks around. Then spots me and silently pulls himself up onto the edge of the tidepools."
    hide casper
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(If anything happens, I can just run, he can't chase me on land.)"
    show mscmc jacket_hairdown basic at left3
    show casper casual basic at right3:
        yoffset 200
    cs "You came alone."
    show mscmc:
        easein 0.3 xoffset 10
        pause 0.2
        easein 0.3 xoffset 20
    "I step towards where he's sitting, one small step at a time."
    show casper angry
    mcarianna smile "I did."
    "As I get within arm's length, I see his shoulders tense and I stop."
    hide casper
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu:
        xoffset 0
    "(He's nervous too.)"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show mscmc jacket_hairdown surprised at left3:
        xoffset 20
    show casper casual smile at right3:
        yoffset 200
    cs "I'm a little afraid of humans still."
    mcarianna "Likewise."
    show mscmc basic
    show casper angry
    "A dark look falls on his face as he regards me."
    cs "I've heard stories about humans, some capture merpeople."
    show mscmc surprised
    cs "Experiment on them, dissect them, do horrific things."
    hide mscmc
    hide casper

    $ menuhideborder = True
    menu ariannas2e5c2:
        "A. I'm definitely not into that stuff.":
            $ menuhideborder = False
            show mscmc jacket_hairdown surprised at left3:
                xoffset 20
            show casper casual angry at right3:
                yoffset 200
            mcarianna "I'm not one of those humans."
            cs basic "You swear?"
            show casper smile
            mcarianna basic "As long as you don't do that kind of thing to me either, we're all good."
        "B. I've heard bad things about mermaids.":
            $ menuhideborder = False
            show mscmc jacket_hairdown surprised at left3:
                xoffset 20
            show casper casual basic at right3:
                yoffset 200
            mcarianna "Well, I've heard some stories about some violent, dangerous mermaids."
            show casper confused
            mcarianna basic "They toy with humans, then pull them under the water and drown them."
            cs basic "I have no intention of harming you."
        "C. Are most merpeople afraid of humans?":
            $ menuhideborder = False
            show mscmc jacket_hairdown surprised at left3:
                xoffset 20
            show casper casual basic at right3:
                yoffset 200
            mcarianna "Are a lot of merpeople afraid of humans?"
            show mscmc basic
            cs angry "Most don't know any different. There's a lot of unchecked info swirling around."
            mcarianna smile "If it makes you feel any better, I'm kind of scared of you too."

    show mscmc basic
    show casper basic
    "There's a quiet moment."
    show mscmc smile
    show casper smile
    "A grin breaks out across his face and we both laugh."
    hide casper
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Maybe he isn't so bad afterall.)"
    show mscmc jacket_hairdown basic at left3:
        xoffset 20
    show casper casual basic at right3:
        yoffset 200
    cs "I wanted to ask you what you think about my government."
    cs "It's all I've ever known--I grew up learning how great we are, I mean, how great it is."
    hide casper
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu:
        xoffset 0
    mcarianna "But that doesn't mean you were taught the truth."
    show mscmc jacket_hairdown basic at left3:
        xoffset 20
    show casper casual basic at right3:
        yoffset 200
    mcarianna "I want to ask {i}you{/i} a question. Why are you so against art? Is it just out of loyalty to the values of your government?"
    show casper confused
    mcarianna smile "Art is an amazing thing."
    show casper basic
    "Casper lowers his head."
    show mscmc surprised
    cs "I know that it can be."
    hide casper
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(He sounds...sad?)"
    show mscmc jacket_hairdown basic at left3:
        xoffset 20
    show casper casual confused at right3:
        yoffset 200
    mcarianna "Did something happen?"

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    show casper sleep
    "He takes a deep breath."
    cs angry "When I was little, one of my uncles used to make beautiful art, in secret."
    cs "But my mother turned him in because he was a traitor."
    show casper angry
    mcarianna "Why did she turn her family in?"
    show mscmc sad
    cs sleep "She said my uncle was putting all of us in danger."
    hide casper
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(That's messed up. I can't imagine having to make a choice like that.)"
    show mscmc jacket_hairdown sad at left3:
        xoffset 20
    show casper casual angry at right3:
        yoffset 200
    "Casper clenches his hands into fists, as he eyes the calm water."
    cs basic "I was...so angry at {i}him{/i}. But I also didn't understand how something so beautiful could bring so much pain?"
    show mscmc basic
    cs angry "I kept thinking, why did he have to make art? Was art more important than our safety? Our family?"
    show mscmc smile
    cs confused "I hadn't really seen art since back then. But then, I saw Arianna's art and talked to you and..."
    hide casper
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(He's really reevaluating a lot of things from his past right now.)"
    show mscmc jacket_hairdown surprised at left3:
        xoffset 20
    show casper casual confused at right3:
        yoffset 200
    cs "Has my whole life been a lie?"
    mcarianna smile "What matters is what you do going forward."
    show casper sleep
    "Casper meets my eyes and his shoulders sag."
    show mscmc surprised
    cs "Actually...I lied to {i}you{/i} too. Lying is so easy for me these days."
    hide casper
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu:
        xoffset 0
    "(Huh? Did he just make up a family tragedy?)"
    show mscmc jacket_hairdown surprised at left3:
        xoffset 20
    show casper casual confused at right3:
        yoffset 200
    cs "When I was little, I was amazed by my uncle's art."
    cs smile "I went into his workshop one night and tried to recreate the kind of things he made."
    hide casper
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(Oh...)"
    show mscmc jacket_hairdown surprised at left3:
        xoffset 20
    show casper casual sleep at right3:
        yoffset 200
    cs "My mother found me. She turned my uncle in because of me, to save me."
    show casper basic
    mcarianna sad "Casper...It wasn't your fault. You were a child. You didn't mean for that to happen."
    show casper angry
    "He says nothing at first, but then he pulls his shoulders back and sits up straight."
    hide mscmc
    show casper casual_cu basic_cu at casper_cu:
        yoffset 0
    cs "I want to join the resistance."

    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    scene bg msc_boardwalk_night_lights at bg with clockwise_wipe
    "Casper leaves and I go to the boardwalk to meet up with Arianna."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(What happened with his uncle is terrible.)"
    "(He doesn't need to play into the government's lies anymore.)"
    show mscmc jacket_hairdown embarrassed at left1:
        xoffset -20
        pause 0.1
        easein 0.7 xoffset 50
    show arianna dress smile at right1 behind mscmc with dissolve:
        xoffset -30
    "Arms wrap around me from behind and pull me into a warm and sweet smelling (but with a twinge of salt) embrace."
    ai grin "You're back, and alive, and in one piece!"
    show mscmc surprised
    "Arianna's scent wafts around me and her arms tighten as she lifts me off my feet and twirls me."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
        xoffset 0
    "(I wasn't gone for long, but I missed her and I love when she swings me around like it's nothing.)"
    show arianna dress grin at right1 behind mscmc:
        xoffset -30
    show mscmc jacket_hairdown grin at left1:
        xoffset 50
    mcarianna "I told you it would be fine."
    show arianna embarrassed
    "Arianna holds me out in front of her and gives me a once over."
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu:
        xoffset 0
    "She pushes back one of my locks gently and looks deep into my eyes."
    ai smile_cu "You're sure everything went okay?"
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mcarianna "I swear that I am totally fine and it went ok."
    show arianna dress sad at right1 behind mscmc:
        xoffset -30
    show mscmc jacket_hairdown surprised at left1:
        xoffset 50
    "Arianna drops her hands and huffs."
    ai "I was so anxious, I thought I was going to explode."
    show mscmc embarrassed
    ai "I kept thinking I heard the whistle and all I wanted was to go after you."
    show mscmc sad
    show arianna basic
    "She grabs hold of her necklace and shakes her head."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(I know what it's like to be that worried about someone you care about. I've felt that way about her.)"
    show arianna dress surprised at right1 behind mscmc:
        xoffset -30
    show mscmc jacket_hairdown basic at left1:
        xoffset 50
    ai "Today has just been so much. Oh jeez, I haven't even eaten anything."
    show arianna basic
    mcarianna surprised "What? Arianna, you need to eat."
    ai "I totally do! But, what did Casper say?"
    hide arianna
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu:
        xoffset 0
    "(I {i}will{/i} make sure she eats once we're done talking.)"

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    show arianna dress surprised at right1 behind mscmc:
        xoffset -30
    show mscmc jacket_hairdown smile at left1:
        xoffset 50
    mcarianna "He's joining the resistance."
    ai "Are you serious?!"
    mcarianna grin "Yeah. He told me why he's acted the way he has up til now and how we managed to get to him."
    mcarianna sad "His uncle was arrested for art Casper made when he was little."
    show mscmc basic
    show arianna sad
    "Arianna grimaces empathetically."
    ai "Oof."
    mcarianna sad "I guess he felt so guilty about it that he decided art is evil and should be condemned."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(Maybe Casper can find a way to forgive himself by being part of the resistance.)"
    show arianna dress basic at right1 behind mscmc:
        xoffset -30
    show mscmc jacket_hairdown basic at left1:
        xoffset 50
    "Arianna folds her arms."
    show mscmc surprised
    ai "I should tell my grandma, maybe the resistance can find where his uncle is locked up, help Casper get a message to him or something."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu:
        xoffset 0
    "(Good, it looks like she's not as anti-Casper anymore.)"
    show arianna dress angry at right1 behind mscmc:
        xoffset -30
    show mscmc jacket_hairdown basic at left1:
        xoffset 50
    ai "Do you think he was telling the truth, though?"
    show arianna surprised
    mcarianna smile "I do, and he said that your art brought up a lot of things from his past when he first saw your studio."
    ai "Really?"
    show arianna smile
    mcarianna "Mhm."
    ai "That's...kind of nice actually."
    show mscmc grin
    show arianna embarrassed
    "Arianna's stomach grumbles and she blushes sheepishly as I laugh."
    show mscmc smile
    ai grin "Want to get some food before going home?"
    mcarianna grin "It's kind of late, but I do know a sushi place that's still open."
    show mscmc surprised
    ai "Is it a restaurant? Like, a real one?"
    mcarianna "Yes, it's a real restaurant."
    ai "I've never been to a human restaurant before! We've never gone! Except for the beach bar, but, you know."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu:
        xoffset 0
    "(I guess I really have only taken her to Jerry's or gotten delivery.)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "She flashes me some huge, pleading puppy-dog eyes."
    ai embarrassed_cu "Can we go, please?"
    hide arianna

    $ menuhideborder = True
    menu ariannas2e5c3:
        "A. Take Arianna for midnight sushi!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(How could anyone say no to her when she looks like that?)"
            show arianna dress grin at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown grin at left1:
                xoffset 50
            mcarianna "Of course! let's go!"

            stop music fadeout 0.5
            play music mscromance fadein 1.0
            ai embarrassed "Are you doting on me?"
            show mscmc embarrassed
            "She smiles coyly at me as she teases me and I feel my heart jump in my chest."
            mcarianna "Maybe a little."
            "Arianna takes both my hands and pulls me close."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu:
                xoffset 0
            ai "I love it."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(So do I.)"
            "My heart pounds at our proximity and I can already feel my palms tingling from the touch of hers."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Take me there? Dinner's on me tonight!"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Right this way."
            show arianna dress grin at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown embarrassed at left1:
                xoffset 50
            "I keep hold of one of Arianna's hands as we walk down the boardwalk to the restaurant."

            stop music fadeout 0.5
            play music mscmctheme fadein 1.0
            scene bg msc_sushirestaurant_lightson at bg
            show arianna dress_cu grin_cu at arianna_cu
            with diagonal_wipe
            ai "Ooooo, I like the vibes of this place!"
            hide arianna
            "We sit at a small, cozy table in the back and I hand Arianna a menu."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Being at a real restaurant makes it feel like a date...)"
            show arianna dress grin at right2 behind mscmc
            show mscmc jacket_hairdown smile at left1plus
            ai "Do you eat a lot of sushi?"
            mcarianna grin "Sometimes, but I usually end up eating the exact same meals every day."
            show mscmc surprised
            show arianna smile
            "Arianna reaches out fluidly and gently pokes me in the middle of my forehead."
            ai grin "Expand your diet, please."
            show arianna smile
            mcarianna grin "I cook sometimes, but I do order a lot of delivery."
            show arianna grin
            mcarianna surprised "So, merpeople have sushi?"
            ai "Well, yeah. Fish are our main source of protein."
            ai "I'm sure there's some differences, but it's all the same raw fish. There's also mer cuisines that don't have it raw, but I love sushi!"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Makes sense, I guess.)"
            show arianna dress smile at right2 behind mscmc
            show mscmc jacket_hairdown smile at left1plus
            "Arianna sets down the menu as the server comes over."
            hide mscmc
            hide arianna
            "Server" "Hi, how are you doing tonight?"
            show arianna dress grin at right2
            show mscmc jacket_hairdown surprised at left1plus
            ai "Fantastic! We are actually ready to order."
            mcarianna "We are?"
            show mscmc embarrassed
            show arianna embarrassed
            "Arianna winks at me and it sends thrills shooting down my spine."
            ai grin "Have a little faith."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Well, I'll try whatever she gets. I have more than faith in her familiarity with seafood.)"
            hide mscmc
            "Arianna orders different kinds of rolls and sashimi."
            show arianna dress grin at right2
            show mscmc jacket_hairdown surprised at left1plus
            ai "Oh, and a bottle of champagne please. We're celebrating tonight."
            hide mscmc
            hide arianna
            "After taking our order, the server leaves us be."
            show arianna dress smile at right2
            show mscmc jacket_hairdown smile at left1plus
            mcarianna "What're we celebrating? Casper joining?"
            show mscmc embarrassed
            ai grin "That your meeting went well and that you returned to me unharmed!"
            mcarianna grin "I'll cheers to that."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Tonight could have turned out very different, I'm so happy I'm here with Arianna.)"
            hide mscmc
            "The service is quick and soon we have trays of sushi and our champagne bucket."

            stop music fadeout 0.5
            play music mscarianna fadein 1.0
            show arianna dress grin at right2
            show mscmc jacket_hairdown smile at left1plus
            ai "Okay, so have you ever tried unagi?"

            play sound beerpour_91033
            show arianna smile
            "Arianna starts filling up our glasses as she eagerly looks at me with her stormcloud colored eyes."
            mcarianna grin "That's eel right? I've never had it."
            ai grin "It's {i}amazing{/i}. Try it."
            "She slides me my glass and then points to the unagi on the tray."
            mcarianna "I'm always open to new things, here goes."
            show mscmc basic
            "Arianna watches me intensely as I eat, trying to gauge my reaction."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's so cute. I can't believe I didn't take her to a proper restaurant sooner.)"
            show arianna dress grin at right2 behind mscmc
            show mscmc jacket_hairdown grin at left1plus
            ai "Weeeellll?"
            show arianna smile
            mcarianna "Yeah, it's pretty damn good."
            ai embarrassed "My lady only has the finest of tastes."
            show mscmc embarrassed
            "Arianna holds her glass up and swirls her drink around as she playacts being snooty and my heart flip flops."
            hide mscmc
            hide arianna
            "We continue eating with gusto when the sushi chef, a short woman, approaches our table."
            "Chef" "For you two, a special roll for your celebration. On the house."
            "The chef beams with pride as she sets down a plate on our table heaped with colorful fish meat."
            show arianna dress grin at right2
            show mscmc jacket_hairdown surprised at left1plus
            ai "Thank you! That's so nice!"
            hide mscmc
            hide arianna
            "Chef" "What are you ladies celebrating tonight? You looked so happy, I couldn't help but whip this up for you two."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Oh, you know. A merpeople resistance win. The usual.)"
            show arianna dress grin at right2 behind mscmc:
                pause 0.1
                easein 0.5 right1 xoffset -30
            show mscmc jacket_hairdown surprised at left1plus
            "Arianna slides her hand across the table and takes mine."
            hide mscmc

            stop music fadeout 0.5
            play music mscromance fadein 1.0
            show arianna dress_cu embarrassed_cu at arianna_cu:
                xoffset 0
            ai "It's our wedding anniversary."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "I choke on my drink and start coughing."
            show mscmc embarrassed_cu
            "(Our what?!)"
            show arianna dress grin at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown embarrassed at left1plus
            ai "I always tell you not to drink so fast, {i}darling{/i}."
            hide mscmc
            hide arianna
            "Chef" "Would you like me to bring you some more water?"
            show arianna dress smile at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown smile at left1plus
            "I shake my head while patting the middle of my chest."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(A warning for my heart would be nice, Arianna.)"
            show arianna dress grin at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown grin at left1plus
            mcarianna "No, no. Just went down the wrong pipe."
            hide mscmc
            hide arianna
            "Chef" "Well, congratulations! What a special night it is."
            "Chef" "How did you two meet?"
            show arianna dress embarrassed at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown embarrassed at left1plus
            "Arianna raises her eyebrows at me as she rubs the back of my hand."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She wants us to put on a little show, the drama queen.)"
            show arianna dress embarrassed at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown grin at left1plus
            mcarianna "We met in Colorado a few years ago. I was on a snowboarding trip."
            mcarianna "Arianna ran into me on the slopes and broke my arm."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Lucky for Arianna, I am a master at making up shit.)"
            show arianna dress grin at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown surprised at left1plus
            ai "It wasn't broken, sweetheart. You just sprained your wrist."
            show mscmc embarrassed
            ai embarrassed "But it {i}was{/i} love at first sight."
            hide arianna
            hide mscmc
            "The chef clasps her hands together."
            "Chef" "We often find love when we least expect it. Please, enjoy the rest of your evening."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She thinks we're in love...)"
            show arianna dress grin at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown embarrassed at left1plus
            "Arianna nudges my knee under the table with hers."
            ai "I don't even know what snowboarding is."
            show arianna surprised
            mcarianna grin "It's like surfing, but on snow."
            show mscmc embarrassed
            ai embarrassed "I'm sorry I sprained your wrist, honey."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I could get used to Arianna calling me 'honey.')"
            show arianna dress embarrassed at right1 behind mscmc:
                xoffset -30
            show mscmc jacket_hairdown embarrassed at left1plus
            mcarianna "It was worth it."
            hide mscmc
            hide arianna
            "We finish up our meal and go back to my place, very full and giggly."

        "B. Eh, I want to go to bed.":
            $ menuhideborder = False
            show arianna dress basic at right1
            show mscmc jacket_hairdown sad at left1
            mcarianna "Well, I can show you how to order it online if you don't mind? I'm super tired, actually."
            mcarianna basic "I'll probably crash while you wait for the food and eat."
            "I pull out my phone and go to the food delivery app, Arianna leaning over my shoulder."
            mcarianna smile "Pick what you want, and they'll bring it to the house."
            ai smile "Nice."
            "I hand Arianna my phone to let her look as we head back to my room above the surf shop."

    stop music fadeout 0.5
    play music msctense fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with clockwise_wipe
    play sound honk_alarm_repeat_loop_101015 loop
    "Arianna sits on my bed when suddenly an urgent sound starts playing from her pocket."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown surprised at left1
    "Arianna's face pales instantly as she reaches in her pocket."
    mcarianna "What is that?"
    stop sound
    ai angry "My shellphone."
    ai "It's the studio's alarm system. Someone's broken in."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
