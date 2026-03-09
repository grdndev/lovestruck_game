label arianna_season1_episode11:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mansion_interior_day at bg
    play music mscantagonist

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    $ sidecharone = "Mia"

    show mscmc jacket_hairdown surprised at right1plus
    show arianna dress angry at left1
    "Arianna stands between Mia and me."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(So it was all a trap after all.)"
    hide mscmc
    show emporia casual smile at centre
    "Mia laughs with a hand to her mouth and Arianna stiffens."
    sid1 "Aw, how sweet! You're trying to protect her, Arianna. Your human pet."
    hide emporia
    show mscmc jacket_hairdown angry at right1plus
    show arianna dress angry at left1
    mcarianna "I'm no one's pet. You've obviously got some serious issues."
    hide arianna
    hide mscmc
    show emporia casual basic at centre
    "Mia doesn't even look at me, her eyes are trained solely on Arianna."
    hide emporia
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress angry at left1
    "Arianna's eyes are cold as she glares at Mia and her shoulders rise and fall with heavy breaths."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I've never seen Arianna like this before.)"
    show mscmc jacket_hairdown basic at right5
    show arianna dress angry at right1plus
    show emporia casual smile at left4
    sid1 "You really care about [genericfn], don't you? Precious."
    ai sad "Mia, why are you doing this?"
    "There's a slight note of pleading behind the anger in Arianna's voice."
    ai "I thought we were friends when we were little."
    ai "What happened to you?"
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It had to be something bad for Emporia...Mia to become this delusional.)"
    show mscmc jacket_hairdown basic at right5
    show arianna dress angry at right1plus
    show emporia casual angry at left4
    sid1 "What happened to me?"
    show emporia basic
    "Mia steps forward but Arianna doesn't move, keeping me behind her."
    show emporia angry
    sid1 "{i}You{/i} happened to me."
    sid1 "It's never mattered to you how our society sees the arts or how you're treated."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I know that the mer government doesn't make it easy to be an artist.)"
    show mscmc sad_cu
    "(Mia's wrong though. It does matter to Arianna, that's why she joined the art resistance.)"
    hide mscmc
    show emporia casual angry at centre
    sid1 "You always followed your dream to be an artist, and you're not even good at it. I could've been great."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What the hell? She's mad that Arianna is an artist and she's...not?)"
    hide mscmc
    show emporia casual angry at centre
    sid1 "I chose to conform. To live the life that our society wanted me to live."
    sid1 "And I was miserable."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(None of this is Arianna's fault.)"
    show mscmc jacket_hairdown basic at right5
    show arianna dress basic at right1plus
    show emporia casual angry at left4
    sid1 "So, I decided to hell with the rules and then I was exiled from the society I wasted my life conforming to."
    show arianna surprised
    sid1 "I deserve what you have, not you. I deserve your life, and I'm going to take it."
    show arianna grin
    "Arianna shakes her head with a laugh of disbelief."
    ai angry "You don't know a thing about my life or what it means to be an artist."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Could this be a good time to get the jump on Mia? She's completely distracted with Arianna.)"
    "(From there, Arianna and I could figure out where to go.)"
    show mscmc jacket_hairdown angry at right5
    show arianna dress basic at right1plus
    show emporia casual angry at left4
    sid1 "Of course I do, and I hate you with every fiber of my being for having what should be mine."
    show arianna angry
    sid1 "I'm going to take this life of yours and make it mine."
    hide arianna
    hide emporia
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Is this a good time to strike?)"
    hide mscmc
    show arianna dress_cu basic_cu at arianna_cu
    "Arianna looks back at me and then drops her eyes until she takes a breath."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(What's with that look? Did she think of a way to get us out of this?)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "Let [genericfn] go, it's obviously me you have a problem with. I'll do what you want, just let her go."
    hide arianna

    $ menuhideborder = True
    menu ariannas1e11c1:
        "A. What?!":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            mcarianna "What?!"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            "Arianna flinches a little at my voice, shaking her head."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(That's never been part of the plan!)"
            hide mscmc
        "B. Uh, no.":
            $ menuhideborder = False
            show mscmc jacket_hairdown angry at right1plus
            show arianna dress basic at left1
            mcarianna "I'm staying here."
            ai sad "[genericfn], let me do this!"
            hide arianna
            hide mscmc
            show emporia casual_cu angry_cu at emporia_cu
            sid1 "Be quiet."
        "C. We're getting out of this together.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
            "(Like hell I'm leaving without Arianna!)"
            show mscmc jacket_hairdown angry at right1plus
            show arianna dress basic behind mscmc at left1
            mcarianna "No way. We're getting out of here, Arianna."
            mcarianna "I'm not leaving without you."
            hide arianna
            hide mscmc

    show emporia casual_cu smile_cu at emporia_cu
    sid1 "No, I want [genericfn] too now that I see how much you care. This'll be fun."
    hide emporia
    show mscmc jacket_hairdown basic at right1plus
    show arianna dress angry at left1
    "Arianna raises her fists."
    ai "Fine. Then I'll fight our way out."
    show mscmc angry
    "I raise my bat alongside Arianna."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Mia can't take us, it's 2 against 1.)"
    hide mscmc
    show emporia casual smile at centre
    sid1 "James, I'm finished here."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(James? The butler-)"
    hide mscmc
    "I feel something come down on my head from behind."

    scene black with dissolve
    "Everything goes black."
    play sound air_horn
    scene bg msc_jail_cell at bg with eye_open
    "The sound of an air horn brings me back to find Arianna and I both tied up back in the basement cell."
    show emporia casual smile at centre
    "Mia stands outside of the cell with an airhorn, her butler at her side with a thick baton hanging from either of his hands."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(That's what he must've knocked us out with.)"
    show mscmc jacket_hairdown surprised at right4
    show emporia casual angry at left4
    "Mia regards me with an annoyed click of her tongue, pointing her finger at me."
    show mscmc angry
    sid1 "You know, you were a nuisance."
    show mscmc sad
    show emporia smile
    sid1 "But now that I see how Arianna looks at you, I've made other arrangements."
    show emporia at out_left
    "Mia taps a hand to her butler's shoulder and he follows her out of the basement."
    hide emporia
    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "The back of my head pounds in agony and the binds are chafing against my wrists."
    show mscmc jacket_hairdown sad at left2
    show arianna dress sad behind mscmc at right2
    ai "I'm sorry."
    mcarianna surprised "Huh?"
    "When I look at Arianna, she doesn't meet my eyes."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I don't want her to feel like she has to apologize to me.)"
    show mscmc jacket_hairdown sad at left2
    show arianna dress sad behind mscmc at right2
    mcarianna "Arianna..."
    "Arianna chews on her lip as she looks at the floor, her brows furrowed."
    mcarianna "I don't blame you for any of this. This isn't your fault."
    ai "She wants to hurt you. She wants to hurt you because of me."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(What can I say to make her feel better?)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "Arianna looks at me with heavy eyes."
    ai "I won't let her do anything else to you."
    ai angry_cu "I'll protect you--no matter what it takes. I won't let Mia touch you."
    ai smile_cu "I swear it--I'll keep you safe."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I can't ignore this feeling anymore, I've fallen for her.)"
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "The passion and intensity in her eyes and voice takes my breath away."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(All I want is to be with Arianna. No matter where we are.)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    ai "I..."
    "Arianna leans towards me as much as she can, looking into my eyes."
    ai basic_cu "I care about you. I want you to know that."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "Every fiber of my being wants to reach out to her. Hold her. Touch her. But this damn rope!"
    show mscmc embarrassed_cu
    "(Arianna's eyes have mine entranced, I don't even want to look away. Even here, even now, she makes me feel safe.)"
    "(I want to make her feel safe too.)"
    show mscmc jacket_hairdown sad at left2
    show arianna dress basic behind mscmc at right2
    mcarianna "I know I'm not, like the greatest hero. I couldn't even get you out."
    mcarianna "I thought I was prepared and ready, but I messed up."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I should have waited for Maxime.)"
    show mscmc jacket_hairdown sad at left2
    show arianna dress surprised behind mscmc at right2
    ai "You didn't mess up."
    show mscmc basic
    show arianna basic
    "Arianna's tone is firm, her eyes burning into mine."
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    ai grin "You did perfectly, my human. You restored my hope. And you brought me this nifty little knife."
    show mscmc surprised
    "Arianna winks at me as she opens her hand and in it is my pocket knife."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Arianna still has it!)"
    show mscmc jacket_hairdown surprised at left2
    show arianna dress grin behind mscmc at right2
    mcarianna "How didn't they get it from you?"
    "She does her best attempt to shrug while tied up."
    ai "Perks of having big hands."
    mcarianna grin "You could've told me sooner!"
    ai embarrassed "I like a well-timed reveal."
    "I shake my head in disbelief, laughing lightly."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She sure loves dramatics, doesn't she?)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress sad behind mscmc at right2
    "She struggles a bit, but she gets the knife positioned behind the rope and starts cutting."
    show mscmc smile
    ai grin "We're getting out of here. I'm getting {i}you{/i} out."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I need to stay hopeful. Arianna will save us if she gets her hands free.)"
    show mscmc jacket_hairdown sad at left2
    show arianna dress basic behind mscmc at right2
    "I lean back to check on her progress and it looks like she hasn't even cut anything yet."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(These ropes are way too thick. Who knows how long it could take to get through them?)"
    show mscmc jacket_hairdown sad at left2
    show arianna dress basic behind mscmc at right2
    "Exhaustion starts to weigh me down and my adrenaline is completely gone."
    ai angry "I'll keep you safe, I promise."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's trying so hard for me. I can't give up.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress smile behind mscmc at right2
    ai "What do you want to do when we're out?"
    ai grin "When there's no Mia and we're safe."
    ai "Think about that. Because it's going to happen, we can't let her win by plunging us into despair. She's trying to get us to give up."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Maybe that will help us feel better. Something to look forward to when this is over.)"
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "I know what I want to do and...it's something with you. Do you want to hear it?"
    hide arianna

    $ menuhideborder = True
    menu ariannas1e11c2:
        "A. Hear Arianna's plan for when you're free!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mscromance fadein 1.0
            show mscmc jacket_hairdown grin at left2
            show arianna dress smile behind mscmc at right2
            mcarianna "Yeah, tell me what it is."
            show arianna embarrassed
            "Her lips quirk up and a pale blush spreads across her cheeks."
            show mscmc embarrassed
            ai "It's a bit hopelessly romantic."
            mcarianna "Already sounds perfect."
            "Arianna takes a small breath and shrugs, acting somewhat hesitant."
            ai "I want to be on the boardwalk, holding hands with you."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(That's her dream for when we get out of here?)"
            "(I'd like to be there too.)"
            "That inexplicable desire for Arianna makes my heart ache."
            show mscmc jacket_hairdown embarrassed at left2
            show arianna dress grin behind mscmc at right2
            ai "Look at fun human things and drink beer and goof around."
            ai sad "I don't know. It doesn't have to be the boardwalk if you don't want."
            show arianna embarrassed
            "Her blush on her cheeks is deeper now and her rope cutting motions slow."
            ai grin "I just want to be with you."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I would go anywhere with her. Anywhere {i}for{/i} her.)"
            show mscmc jacket_hairdown embarrassed at left2
            show arianna dress grin behind mscmc at right2
            ai "Maybe we can watch the sunset on the beach."
            ai "Or sit at Jerry's. Or cuddle on your bed watching another movie."
            show arianna embarrassed
            "Like she's invigorated by what she's saying, Arianna starts sawing away again."
            mcarianna grin "Well, we don't have to pick one thing. We can do all of it if you want."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(There's still so much of my world that I want to show her.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress grin behind mscmc at right2
            ai "Let's plan out our day then."
            mcarianna "We'll do breakfast at Jerry's and then hit up the beach for surfing and swimming."
            ai "Then we'll go to the boardwalk. Maybe you'll do a yoga class with me?"
            mcarianna "Maybe."
            show mscmc embarrassed
            ai embarrassed "What if it's a {i}private{/i} lesson?"
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "The way she emphasizes 'private' makes my ears burn."
            "(That, I could definitely get talked into.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress embarrassed behind mscmc at right2
            mcarianna "It's tempting."
            show mscmc embarrassed
            ai grin "And then we'll take our drinks to the beach and watch the sun go down."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "Longing for this day to happen only fuels my desire to get the hell out of Mia's place."
            show mscmc jacket_hairdown embarrassed at left2
            show arianna dress grin behind mscmc at right2
            ai "When the sun goes down, you'll take me back to your place and show me another movie."
            ai "Do you want to do anything else?"
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(A very very long list of things actually.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress grin behind mscmc at right2
            mcarianna "Don't forget to hold my hand."
            "Arianna laughs, cheeks still red."
            ai "I haven't forgotten. The handholding is a part of all of it."
            ai embarrassed "So, there. I told you mine."
            "She looks at me expectantly."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I guess now it's my turn.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress smile behind mscmc at right2
            mcarianna "What do I want to do?"
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "The question makes the reality of everything hit a little harder."
            "(Arianna wants to make me feel better. Even through all of this, she's putting me first.)"
            "(She's trying so hard to keep us grounded.)"
            show mscmc sleep_cu
            "I take a leveling breath."
            show mscmc smile_cu
            "(Where my happy place is. Where I feel safe and calm.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress smile behind mscmc at right2
            mcarianna "I want to be on the ocean."
            show arianna grin
            "Arianna perks up as I start speaking, hanging onto my words."
            mcarianna "Waiting on my board with the breeze and the seagulls overhead and you swimming around me."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I would give anything to be surfing right now. To be out of this basement.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress grin behind mscmc at right2
            mcarianna "Not a care in the world. Just the waves and...us."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I don't want to be alone anymore.)"
            show mscmc embarrassed_cu
            "(Arianna came into my life like a hurricane and then there's never been a dull moment since.)"
            show mscmc jacket_hairdown smile at left2
            show arianna dress smile behind mscmc at right2
            "Thinking about that almost makes me want to laugh."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Nothing in my life has been the same since I met Arianna.)"
            show mscmc embarrassed_cu
            "(I wouldn't trade it for anything.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress grin behind mscmc at right2
            mcarianna "You'll be swimming around and showing off, as you do."
            show arianna embarrassed
            "Arianna laughs softly."
            ai grin "You love it."
            mcarianna "I do."
            "Arianna taps her knee against mine."
            mcarianna "And maybe soon I can see the inside of your studio."
            mcarianna "I'll rent some scuba gear and you can show me around."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Someday I want to see the rest of her world, even if it's not easy.)"
            show mscmc jacket_hairdown grin at left2
            show arianna dress grin behind mscmc at right2
            ai "Then it'll happen--I'll make sure of it."
            ai embarrassed "What're you doing later tonight?"
            mcarianna "I think I'm a little...tied up at the moment, but I'll let you know."
            show arianna grin
            "We both laugh, quiet and soft like it's the only thing we can hang on to."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's keeping me sane right now.)"
            show mscmc sad_cu
            "(It's hard to think about where we could be later today.)"
            show mscmc grin_cu
            "(But I need to stay strong and hold onto this hope.)"
            hide mscmc

        "B. You don't feel up to it.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Arianna is just trying to keep my mood up, but I can't think of anything else right now.)"
            show mscmc jacket_hairdown sad at left2
            show arianna dress basic behind mscmc at right2
            mcarianna "I don't know...I'm sorry. I just want to get out of here"
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(All I want to focus on is our escape.)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna nods in understanding, a sympathetic smile on her lips."
            ai "I'll get us out, I promise."
            hide arianna

    play sound stairs
    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    show emporia casual basic at centre with dissolve
    "The clack of heels on stairs signals Mia's return."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "I'm filled with a sense of dread at what she might have planned."
    "(I hope Arianna is almost done cutting through her binds with that tiny knife.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress basic behind mscmc at right2
    "A part of me wants to check, but I can't bring attention to what Arianna is doing."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Please don't let Mia notice.)"
    hide mscmc
    show emporia casual smile at centre
    "Mia hovers outside of the cell bars and takes in a deep breath like she's smelling the air."
    sid1 "There aren't words that can describe the joy I feel seeing you like this, Arianna."
    sid1 "Defeated. Pathetic. Helpless."
    hide emporia

    $ menuhideborder = True
    menu ariannas1e11c3:
        "A. Don't listen to her.":
            $ menuhideborder = False
            show arianna dress angry at right1plus
            show mscmc jacket_hairdown basic at left2
            "Arianna clenches her jaw, her brows furrowed at Mia."
            mcarianna angry "Don't listen to her, Arianna."
            mcarianna "She wants to get you worked up."
            hide arianna

        "B. Oh my god, just shut up already.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
            "(I'm tired of hearing her voice. She's so smug and it pisses me off.)"
            show mscmc jacket_hairdown angry at right4
            show emporia casual sad at left4
            mcarianna "Will you just shut up already?"
            show emporia angry
            mcarianna "We get it."

        "C. You're disgusting.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
            "Everything about Mia causes a pit to form in my stomach."
            show mscmc jacket_hairdown angry at right4
            show emporia casual angry at left4
            mcarianna "You're disgusting."

    hide mscmc
    show emporia casual_cu sad_cu at emporia_cu
    "Mia flicks her eyes over to me."
    show emporia smile_cu
    sid1 "Arianna, why so pitifully desperate to protect this girl?"
    hide emporia
    show arianna dress angry at right1plus
    show mscmc jacket_hairdown angry at left2
    "Arianna stiffens and her eyes narrow at Mia, but Mia seems delighted."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Even if Arianna gets herself free, I don't know if we could make it out.)"
    show emporia casual basic at left3
    show mscmc jacket_hairdown basic at right3
    "Mia taps a finger to her chin and looks me up and down."
    show mscmc sad
    "Just having her eyes on me sends chills down my spine."

    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    show mscmc surprised
    show emporia smile
    sid1 "I think I'll torture her in front of you for a laugh, Arianna."
    hide emporia
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Whoa, wait a minute! Torture me?!)"
    show mscmc sad_cu
    "(Is this actually happening?!)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "{i}Mia{/i}."
    show arianna dress angry at right1plus
    show mscmc jacket_hairdown angry at left2
    "Arianna bristles beside me, her voice sharp with warning in a way I've never heard before."
    hide arianna
    hide mscmc
    show emporia casual smile at centre
    "Mia laughs, cruel and sick."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Nothing's going to get through to her.)"
    hide mscmc
    show emporia casual smile at centre
    sid1 "You're making this too easy, Arianna."
    show emporia angry
    "Mia's eyes widen and she throws her arms out for a grand gesture."
    sid1 "You think you're protecting her by telling me to back off?"
    show emporia smile
    sid1 "Oh no, dear. It's just the opposite."
    hide emporia
    show arianna dress_cu angry_cu at arianna_cu
    ai "Mia. Don't do this."
    "It's clear Arianna is trying to keep her voice level, but she knows how bad this is."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Mia doesn't mean real torture right? Even she isn't that sick in the head.)"
    show emporia casual smile at left4
    show mscmc jacket_hairdown sad at right3
    "Mia swings open the cell door and I instinctively press myself as far back as I can."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I don't want Mia anywhere near me.)"
    show mscmc jacket_hairdown sad at right3
    show emporia casual smile at left4:
        pause 0.1
        ease 0.3 left2
    "Mia steps forward and I flinch away as she reaches for me."
    hide emporia
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I can't even defend myself! I could bite her or kick or-)"
    hide mscmc
    show arianna dress_cu angry_cu at arianna_cu
    ai "Don't {i}fucking{/i} touch her."
    show emporia casual angry at left4:
        xoffset -30
    show arianna dress angry at right4
    show mscmc jacket_hairdown sad behind arianna at right1plus
    "Mia snaps her hand back and practically growls under her breath."
    sid1 "Look at you. Completely obsessed with this human."
    "Her eyes go back and forth between Arianna and me, a range of unreadable emotions passing over her face."
    show emporia at out_left
    "Then Mia laughs loudly and steps out of the cell."
    hide emporia
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Mia's lost it. There's no rationalizing with someone like this.)"
    hide mscmc
    show emporia casual angry at centre
    sid1 "I see it in both of your eyes. The way you look like you'd do anything for each other, how sickly sweet."
    hide emporia
    show arianna dress sad at right2
    show mscmc jacket_hairdown sad at left1plus
    "Arianna glances at me, her lower lip quivering just the slightest bit."
    hide arianna
    hide mscmc
    show emporia casual smile at centre
    "Mia holds up a dark kind of tool wrap thing and waves it around."
    sid1 "And, Arianna, how will you look when I'm finished slicing up your pet?"

    scene arianna_s1_mini4 at bg with dissolve
    "Mia unrolls the carrying case."
    "(Holy shit.)"
    "I feel woozy as I see the many shining and sharp surgical tools laid out neatly in a row."
    "(So, she was serious about the torture. Great, wonderful.)"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
