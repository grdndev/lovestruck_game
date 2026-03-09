label arianna_season1_episode1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg
    play music mscarianna

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show mscmc casual_hairdown basic at centre
    "The door closes behind a leaving customer and I blow out a long sigh."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(What a slow day.)"
    hide mscmc
    "Through the window I can see that even the beach looks weirdly dead compared to usual."

    show arianna_s0_mini2 at bg as ei
    with fade
    "The picture of Arianna's gorgeous silver eyes is still fresh in my mind."

    show mscmc casual_hairdown sad at centre behind ei
    hide ei with dissolve
    mcarianna "No, don't do it."
    show mscmc basic
    "I step back from the counter and lightly slap my cheeks a few times."
    mcarianna sad "[genericfn], don't think about her."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Arianna never even called me on the shellphone she gave me. Not like I care.)"

    stop music fadeout 0.5
    play music mscsurfshop fadein 1.0
    play sound "<to 0.5>audio/sfx/bell-store-entrance-ding.mp3"
    queue sound fight_fall2
    scene bg msc_surf_shop_day at bg with hpunch
    "The door flies open with a force that makes the floor shake."
    show trina casual smile at centre
    so "Guess who I saw?!"
    hide trina
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(Welcome back, Trina.)"
    show mscmc casual_hairdown grin at left2
    show trina casual basic at right2
    mcarianna "Who?"
    so smile "Guess!"
    mcarianna sad "Trina..."
    show mscmc surprised
    so "I saw Arianna!"
    hide trina
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Like, {i}the{/i} Arianna?!)"
    show mscmc casual_hairdown surprised at left2
    show trina casual basic at right2
    mcarianna "With legs? Walking around and stuff?"
    show trina angry
    "Trina's face scrunches up."
    show mscmc sleep
    so smile "No, her legs were mysteriously missing. Yes, she was walking with legs, you weirdo."
    show trina basic
    mcarianna grin "Well, you know, just because of her job. Party mermaid, remember?"
    so smile "Oh, right. She was off the clock then, if that's what you meant."
    hide trina
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I'm the only one who knows that Arianna's a real-life mermaid. Guess I still need to be careful.)"

    scene white
    pause 0.1
    scene bg msc_tide_pools_sunset at bg:
        pause 0.2
        linear 0.6 matrixcolor SaturationMatrix(0.0)
    show mscmc jacket_hairdown surprised at left3:
        pause 0.2
        linear 0.6 matrixcolor SaturationMatrix(0.0)
    show arianna siren smile at right3:
        pause 0.2
        linear 0.6 matrixcolor SaturationMatrix(0.0)
    with Dissolve(0.3)
    ai "You're the first person I've ever shown."
    show arianna basic
    mcarianna "I don't really understand what's going on."
    ai grin "[genericfn], I'm trying to tell you that I'm a mermaid!"

    scene white
    pause 0.1
    scene bg msc_surf_shop_day at bg
    show mscmc casual_hairdown surprised at centre
    with Dissolve(0.3)
    mcarianna "Where was she?"
    hide mscmc
    play sound "audio/sfx/MSC_Sound_Effects/bell-store-entrance-ding.mp3"
    "The shop door chimes and there's a hopeful jolt in my heart that it's Arianna."
    show trina casual smile at centre
    so "Hey, Maxime."
    hide trina
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Of course it isn't Arianna.)"
    hide mscmc
    show maxime casual basic at centre
    "Maxime raises his hand in a partial wave and nods at us."
    hide maxime
    show trina casual smile at centre
    so "What's up?"
    hide trina
    show maxime casual basic at centre:
        alpha 0.0
        linear 0.5 alpha 1.0
    "He walks around the counter to the whiteboard with the surfing classes schedule on it."
    mx smile "Just adjusting a time."
    show maxime basic
    "Maxime erases something with his finger and fills it in with a new time."
    show maxime:
        linear 0.5 alpha 0.0 xoffset 100
    "He leaves with another nod."
    hide maxime
    show mscmc casual_hairdown smile at centre
    mcarianna "See ya."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I'm glad Trina was able to hire a new surf instructor, but he barely says anything.)"
    show mscmc casual_hairdown smile at left2
    show trina casual smile at right2
    so "Right, anyways. Arianna."
    show mscmc basic
    so "She was on the beach. I told her about how that high-roller wanted to commission pieces."
    mcarianna "Oh yeah, the person who bought all of her art work during the surf shop fundraiser?"
    so "Yep, Emporia Lid or something, and how she wants to meet with Arianna."
    hide trina
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(So, Arianna's really just walking around on land somewhere. Why didn't she call me?)"
    "(I thought she would reach out to me.)"
    show mscmc casual_hairdown sad at left2
    show trina casual basic at right2
    mcarianna "She didn't tell me she was here."
    show mscmc basic
    show trina sad
    "Trina's face falls in a sympathetic frown, but she hardens quickly."
    show mscmc sad
    so smile "Dude, you're way too good for her anyways. I say forget about her."
    mcarianna basic "Trina, come on."
    so sad "What? She's cool and all, but there's no use wasting feelings on her."
    so basic "Especially when she left out of the blue and then didn't let you now she was back."
    hide mscmc
    hide trina

    $ menuhideborder = True
    menu ariannas1e1c1:
        "A. Defend Arianna.":
            $ menuhideborder = False
            show mscmc casual_hairdown sad at left2
            show trina casual basic at right2
            mcarianna "Look, I don't want to hear it."
            mcarianna basic "She didn't just up and leave--we said our goodbyes and stuff."
            mcarianna "It was all on good terms."
            hide trina
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(Arianna wouldn't purposefully ignore me. At least, I hope not.)"
        "B. Say you were just friends.":
            $ menuhideborder = False
            show mscmc casual_hairdown surprised at left2
            show trina casual basic at right2
            mcarianna "We were just friends, okay? We helped each other out while she was in town."
            mcarianna basic "Nothing else. No leading on. That was it."
        "C. Maybe Trina's right.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu sad_cu at mscmc_cu
            "(I know why Arianna left and I'm not upset about that, but she could've called me.)"
            "(But I don't want to assume the worst yet.)"
            show mscmc casual_hairdown surprised at left2
            show trina casual basic at right2
            mcarianna "I bet Arianna's just been super busy. Who hasn't?"
    show mscmc casual_hairdown basic at left2
    show trina casual sad at right2
    "Trina crosses her arms with her lips pursed."
    so "Mhm. Sure, if that's what helps you sleep at night."
    show trina basic
    mcarianna smile "It is."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    scene bg msc_mc_bedroom_day at bg with fade
    "After the rest of my shift and a few surfing lessons, my bed calls to me."
    "I fidget with the corners of the surf magazine that's meant to be a distraction from my thoughts."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Maybe she regrets telling me about being a mermaid?)"
    "(But, she's the one who kissed my cheek!)"
    hide mscmc
    "I look over at the shellphone sitting on my nightstand."
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    mcarianna "Why won't you call me?"
    "(I mean, I didn't call her either...but still!)"
    hide mscmc
    play sound "audio/sfx/bubbles_003_6397.mp3" loop
    "The shell vibrates, a string of bubbling noises follow."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Wait, is she calling me right now?!)"
    hide mscmc
    "I sit up and scooch to the side of my bed, taking the ringing shell with a shaky hand."
    stop sound fadeout 0.5
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    mcarianna "It's fine. Be cool. Be calm. It's just a phone call. On a shell."
    hide mscmc
    "I take a deep breath and blow it out as I put the shell to my ear."
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Uh...hello?"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        alpha 0.75
    ai "Hey!"
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "Nothing can stop the giddy joy that settles over me at the sound of her voice."
    show mscmc embarrassed_cu
    "(That one word is enough to erase how down I just felt about her.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        alpha 0.75
    ai "I need to tell you something!"
    ai surprised_cu "Did you know that the seed of the avocado is sooo big because giant sloths used to eat them?"
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(What the hell is she talking about?)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas1e1c2:
        "A. Let her continue.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "The confusion I feel is greater than my joy at hearing her voice."
            "(Did I miss something? Did she accidentally call the wrong person?)"
            show mscmc smile_cu
            "I stay quiet in hopes of finding out what on earth she's talking about."
        "B. Pretend you now what she's talking about.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Uh, yeah, totally. That's evolution for you."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu:
                alpha 0.75
            ai "It's great, right?"
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Really great."
            show mscmc surprised_cu
            "(I don't know what this phone call is supposed to mean.)"
        "C. What?":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mcarianna "........"
            mcarianna "Huh?"
            "(Did we ever talk about sloths before?)"
    hide mscmc
    "There's a long pause from Arianna, but I can make out some distant chatter around her."
    show arianna dress_cu sad_cu at arianna_cu:
        alpha 0.75
    ai "Sorry, that was...I don't know. We haven't talked in a bit, so I just didn't know what to say."
    ai grin_cu "And I'm learning new things and I thought maybe you'd like to know a fun fact."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "(Aw, ok that's silly but actually pretty sweet.)"
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu:
        alpha 0.75
    "Arianna pauses again."
    ai grin_cu "They ate the avocados whole!"
    "The random fact and the quickness of her speech makes it seem like Arianna has been sipping something other than water."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "The tension from the phone call completely fizzles away, I don't even try to hide my laugh."
    mcarianna "Arianna, did you drunk call me?"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu:
        alpha 0.75
    ai "Are you annoyed?"
    hide arianna
    show mscmc casual_hairdown_cu smile_cu at mscmc_cu
    "(Saying it's cute would be weird, right? I gotta play it carefree, yet safe.)"
    mcarianna grin_cu "Far from annoyed--I think it's funny."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu:
        alpha 0.75
    ai "I was just really nervous, so I maybeeeee had a beer or two first."
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Nervous about what?"
    show mscmc embarrassed_cu
    "(Nervous about talking to me?)"
    hide mscmc
    "There's a muffled shuffling from the other end."
    "???" "...shell...?"
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Is she with someone? Arianna sounds like she's at a restaurant or something.)"
    hide mscmc
    show arianna dress_cu surprised_cu at arianna_cu:
        alpha 0.75
    ai "Oh yeah, I just really really love talking to the ocean."
    hide arianna
    "Her voice pulls away from the phone as she responds to whoever that is."
    "The other person says something else, but I can't make it out."
    show arianna dress_cu grin_cu at arianna_cu:
        alpha 0.75
    ai "I know, right? I'm sure you can find your girlfriend a shell just as pretty."
    ai "Okay. What was I saying?"
    "Her voice is clear again, focus seemingly back on her shellphone."
    hide arianna
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    mcarianna "Who was that?"
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu:
        alpha 0.75
    ai "I forgot I'm surrounded by {i}humans{/i}."
    "Arianna sounds like she has a hand cupped around her mouth."
    ai grin_cu "I miss you."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "I bite down on my bottom lip, resisting the urge to giggle like a kid whose crush likes them back."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        alpha 0.75
    ai "Can I actually get one more, uh, Red Moon? Is that what it was called? Thanks!"
    "Her voice comes and goes as she orders another beer."
    ai "[genericfn], you should come here!"
    hide arianna
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    mcarianna "Where are you?"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        alpha 0.75
    ai "{i}Your{/i} bar! Jerry's."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(She called it {i}my{/i} bar. Adorable.)"
    mcarianna grin_cu "Alright. I'm on my way."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu:
        alpha 0.75
    ai "Great, I'll buy you a Red Moon!"

    stop music fadeout 0.5
    play music mscbeach fadein 1.0
    scene bg msc_beach_bar_sunset at bg with clockwise_wipe
    "The walk to the beach bar is somehow the longest and shortest walk of my life."
    show arianna dress smile at centre
    "The bar is starting to get fairly busy at this time of day, but she's not hard to spot."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(God, Arianna's just as stunning as I remember.)"
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress smile at right2 behind mscmc
    "She's sitting at the bar, one hand wrapped loosely around her necklace."
    mcarianna grin "Come here often?"
    ai grin "Ah! You're here!"
    show arianna:
        easein 0.4 right1
    show mscmc:
        pause 0.1
        easein_back 0.4 left1
    "Arianna stands so that she can engulf me in a hug, she smells like a sweet ocean breeze."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Oh wow.)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "It's great to see you again."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Is it possible for someone to be this beautiful?)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "What are you drinking? It's my treat."
    show mscmc jacket_hairdown smile at left1
    show arianna dress smile at right1:
        pause 0.1
        easein 0.3 right2
    "Arianna sits back down and pulls out the stool beside her for me."
    mcarianna grin "Whatever you're having is fine, but..."
    ai grin "Jerry, another Red Moon for my favorite human please."
    hide mscmc
    hide arianna
    show jerry casual smile at centre
    jr "Good to see you, [genericfn]. Your friend here is very excited to be back."
    hide jerry
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown grin at left1plus
    mcarianna "How could she not be? It's the best bar in town."
    hide mscmc
    hide arianna
    show jerry casual smile at centre
    "Jerry reaches under the counter for the beer, popping it open before sliding it towards me."
    hide jerry
    show arianna dress smile at right1plus
    show mscmc jacket_hairdown grin at left1plus
    mcarianna "So, what are you doing here, Arianna?"
    ai grin "You could sound a little happier to see me."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I don't think there's enough words to describe how happy I really am.)"
    show arianna dress smile at right1plus behind mscmc
    show mscmc jacket_hairdown grin at left1plus
    mcarianna "It's just a surprise, especially seeing you {i}walking{/i} around."
    show mscmc smile
    "Arianna shrugs, twirling a strand of hair around her finger."
    ai grin "Honestly, it was a spur of the moment type thing."
    ai "I was swimming along this morning and thought, 'Hey, why not?'"
    "I fight to keep my heart from dropping."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(What did I want her to say? That it was so she could see me?)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairdown basic at left1plus
    "She goes from twirling her hair to tugging on it gently, her eyes flicking down."
    ai "I was planning on calling you--sooner, I mean. But, I got...cold fins."
    mcarianna surprised "Why were you scared to call me?"
    ai embarrassed "It's kinda--I don't know-- an embarrassing reason."
    show arianna grin
    "She laughs again, this time it's short and quiet with nerves."
    hide mscmc
    show arianna dress_cu smile_cu at truecenter:
        anchor(0.5, 0.4) transform_anchor True alpha 0.0
        pause 0.1
        linear 0.5 zoom 1.25 alpha 1.0
    "Her eyes finally meet mine again and she brushes my hair away from my ear as she leans in."
    ai grin_cu "Do you really want to know?"
    hide arianna

    $ menuhideborder = True
    menu ariannas1e1c3:
        "A. Encourage Arianna to open up!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(When she puts it like that, how can I say no?)"
            show arianna dress smile at right2 behind mscmc
            show mscmc jacket_hairdown smile at left1
            "I push down the heat that builds from her touch."
            mcarianna grin "Of course I want to know."
            show mscmc:
                easein_back 0.5 xoffset 30
            show arianna grin:
                pause 0.2
                easein_back 0.4 xoffset 20
            "I nudge her arm with my elbow."
            mcarianna surprised "I'm not that scary, am I?"
            show mscmc smile
            "Arianna laughs to herself and shakes her head, finally letting go of her hair."
            ai smile "Okay, I'll tell you...just don't laugh, okay?"
            show arianna grin
            mcarianna grin "When you phrase it like that-"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu:
                xoffset 0
            ai "Promise or I won't tell you."
            show arianna smile_cu
            "Arianna meets me with a stern gaze, but the corners of her lips turn up ever so slightly."
            show arianna dress basic at right2
            show mscmc jacket_hairdown grin at left1
            mcarianna "Promise."
            "For show, I put my hand over my heart."
            show mscmc basic
            ai embarrassed "I was worried you wouldn't want to see me."
            show arianna basic
            show mscmc surprised
            "While it is a little humorous, I can't help but feel her tug on my heartstrings."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(What about the last time we met would make her think I wouldn't want to see her?)"
            show arianna dress sad at right2 behind mscmc
            show mscmc jacket_hairdown basic at left1
            ai "I left really quickly after everything kind of came to an end."
            show mscmc sad
            ai "And I thought we were fine, but then I just kept wondering what if that wasn't true."
            ai "I don't know. It was just the thought of you rejecting me that was scary."
            "There's some relief in knowing that Arianna was worried about the same things I was."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(We were both scared that the other one didn't want to see each other.)"
            show arianna dress surprised at right2 behind mscmc
            show mscmc jacket_hairdown grin at left1
            mcarianna "Arianna, you don't need to worry about it."
            show arianna grin
            mcarianna "In fact, it made me really happy when you called me."
            ai embarrassed "It did?"
            show arianna surprised
            mcarianna "Yeah."
            show arianna grin
            "She fixes me with a soft smile, her eyes shimmering in the glow of the barlights."
            show mscmc basic
            ai sad "I kept thinking how awful it would be if you didn't want to be friends."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Totally platonic friends. Yep.)"
            show arianna dress sad at right2 behind mscmc
            show mscmc jacket_hairdown grin at left1
            mcarianna "Of course I want to be friends with you. We went through a lot together, didn't we?"
            ai smile "We had a lot of fun."
            show arianna grin
            mcarianna "And we can keep having fun. You don't need to feel nervous about hanging out."
            show mscmc smile
            "Arianna laughs with red cheeks."
            ai "I know it was silly. I could even imagine you sitting here saying this."
            ai embarrassed "I just couldn't help but be a little nervous."
            ai "You're kind of intimidating."
            "Arianna smirks at me as she raises her beer for a sip."
            mcarianna surprised "What? No way."
            hide arianna
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(If anyone's intimidating, it's Arianna!)"
            show arianna dress embarrassed at right2 behind mscmc
            show mscmc jacket_hairdown surprised at left1
            ai "I can't explain it well. It's more like an aura about you."
            ai grin "Like this very electric passion and determination."
            mcarianna grin "Sounds like a compliment."
            ai "Oh, it is."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(To think that I was so worried earlier with Trina.)"
            show mscmc grin_cu
            "(Arianna still feels exactly the same. We're good.)"
            show arianna dress basic at right2 behind mscmc
            show mscmc jacket_hairdown grin at left1
            mcarianna "You can call me whenever you want, seriously."
            ai surprised "Aren't you a busy woman?"
            mcarianna "Yeah, but I can always make time. Don't be scared to call me."
            show mscmc smile
            ai grin "You could call me too, y'know."
            show arianna sad
            "Arianna's lips come together in a pout."
            show mscmc sad
            ai "I don't remember getting any calls either."
            mcarianna grin "We'll both keep in touch, deal?"
            ai grin "Deal."
            "Arianna takes my hand in a warm handshake that reminds me of how this all started."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Hopefully this time around can be a lot more peaceful than last.)"

        "B. Don't push it.":
            $ menuhideborder = False
            show arianna dress smile at right2
            show mscmc jacket_hairdown surprised at left1
            "Her touch and tone send my heart beating a mile a minute."
            mcarianna "If you don't want to, it's fine."
            show mscmc basic
            show arianna basic
            "Arianna turns back to her drink with a shrug."
            ai grin "Guess I'll keep my secrets."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Why {i}was{/i} she scared to call me, though?)"
            show mscmc sad_cu
            "(Ugh, whatever. Too late now.)"

    show arianna dress smile behind mscmc at right2
    show mscmc jacket_hairdown grin at left1
    mcarianna "So, Trina said she saw you earlier. Told you about those commissions."
    show arianna basic
    mcarianna "That's great news. Are you going to meet with this Emporia person?"
    show mscmc smile
    "I nurse on my drink with raised brows while Arianna taps the rim of her glass."
    ai sad "Yeah, I know and I'm excited, but..."
    mcarianna "Also scared?"
    show mscmc basic
    ai basic "She's a human and on top of that, my art hasn't always been received with open arms."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I remember her saying that other mermaids didn't find a lot of value in it because it's made with recycled materials.)"
    show mscmc basic_cu
    "(But I don't want Arianna to let an opportunity slip by.)"
    show arianna dress basic at right2 behind mscmc
    show mscmc jacket_hairdown grin at left1
    mcarianna "I can go with you if you want."
    show mscmc smile
    ai surprised "You would?"
    mcarianna grin "Of course!"
    ai grin "You truly are my favorite human."
    mcarianna "I better be."
    show mscmc smile
    ai "What've you been up to? Enough about me."
    mcarianna grin "I was kind of scouted by this cool water gear company that may want to sponsor me."
    mcarianna "I'm trying to lock that in."
    ai surprised "So you'd get your face on a wetsuit?"
    mcarianna "Nothing that flashy, but that would be fun."
    show mscmc smile
    ai grin "Look at us, swimming the current to success."
    "Arianna rests her hand on the bar counter, her pinky almost to mine."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I want to hold her hand. Would that be too much?)"
    show arianna dress grin at right2 behind mscmc:
        pause 0.1
        easein 0.4 right1plus
    show mscmc jacket_hairdown smile at left1
    "Arianna answers my thoughts as she puts her hand over mine, squeezing."
    ai "Seems like we're partners in crime once again."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(And I couldn't be happier.)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairdown basic at left1
    "She yawns then and rubs at one of her eyes."
    mcarianna surprised "Where are you staying tonight? Hope you're not going to sleep on the beach."
    show arianna basic
    mcarianna "You know you can just stay at my place if you want."
    ai surprised "Are you sure? I don't want you to think I just want a free room."
    show mscmc smile
    show arianna grin
    "The tiredness in her eyes is momentarily replaced with eagerness."
    mcarianna grin "I definitely don't think that. Seriously, it's fine."
    mcarianna "Let's finish our drinks and head back."
    hide mscmc
    hide arianna
    "We take our time with our beers and then I take Arianna to my room."

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    scene bg msc_mc_bedroom_night_lights at bg with fade
    show arianna dress basic at centre:
        xoffset -100 alpha 0.0
        parallel:
            easein_back 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    "Arianna moves ahead of me, stumbling through the doorway."
    ai grin "I do remember how comfortable your bed is."
    hide arianna with dissolve
    "She falls back onto my bed, arms spread out above her head."
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(Just two girls hanging out. Don't get in your head about it.)"
    hide mscmc
    show arianna dress smile at centre
    ai "I promise I'll get up and sleep on the floor."
    hide arianna
    show mscmc casual_hairdown surprised at centre
    mcarianna "We can share the bed if you want. You don't have to sleep on the floor."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Really? Yay!"
    show arianna dress grin at left1:
        pause 0.1
        easein_back 0.4 left2
    show mscmc casual_hairdown smile at right2 behind arianna
    "Arianna rolls onto the left side of the bed with a content hum as she snuggles into my pillow."
    ai "Good night, [genericfn]."
    mcarianna grin "Night. Tomorrow we can reach out to this Emporia Lid art buyer person."

    scene bg msc_mc_bedroom_night at bg
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    with dissolve
    "(And just like that, Arianna's back in my life.)"
    "(This better not all be a dream.)"




    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
