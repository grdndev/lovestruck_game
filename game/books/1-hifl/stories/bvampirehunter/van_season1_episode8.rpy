label van_season1_episode8:

    $tbc = False
    scene bg bowling at bg
    play music hiflliteromance
    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show hiflmc casual sad at right3
    show vanessa casual basic at left3
    mcvan "Vanessa."
    show hiflmc casual basic
    mcvan "I want you to keep protecting me."
    show hiflmc casual sad
    mcvan "I don’t care that you needed help yesterday."
    mcvan "It was my own fault, anyway."
    show hiflmc casual basic
    mcvan "So far you’ve done an amazing job keeping me safe."
    mcvan "I can’t imagine anyone could do better."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu basic_cu at hiflmc_cu
    "(Plus, I don’t think I’d want to spend this much time in close quarters with anyone else.)"
    show hiflmc casual_cu happy_cu
    "(Vanessa is gorgeous, and passionate, and a lot of fun to hang out with.)"
    "(And I {i}really{/i} want to get to know her better.)"
    show hiflmc casual basic at right3
    show vanessa casual sad at left3
    "Vanessa looks like she’s not sure if I’m making fun of her or not."
    va "...Really?"
    show hiflmc casual happy
    mcvan "Absolutely."
    show vanessa casual happy
    show hiflmc casual blush
    "A slow, genuine smile spreads across her face, and my heart stutters."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(She has to stop doing that.)"
    "(I can’t take much more of this.)"
    hide hiflmc
    show hiflmc casual basic at right2
    show vanessa casual basic at left2
    "She looks me dead in the eye and takes one of my hands in both of hers, her expression sobering a bit."
    show vanessa casual angry
    va "I swear on my life and on the Helsing name that I will protect you, no matter what."
    va "I will defend you from any and every creature who would harm you."
    va "I will keep you safe. I promise."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Wow.)"
    hide hiflmc
    show hiflmc casual surprised at right2
    show vanessa casual angry at left2
    "The combination of her direct gaze, her vow to protect me, and the feeling of her warm hands on my own is almost too much."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e8c1:
        "A. I trust you.":
            $menuhideborder = False
            show hiflmc casual basic at right2
            show vanessa casual basic at left2
            mcvan "I know you will. I trust you."
            show vanessa casual happy
            "I didn’t think it was possible, but her smile grows even brighter."
        "B. Don't die for me.":
            $menuhideborder = False
            show hiflmc casual surprised at right2
            show vanessa casual basic at left2
            mcvan "How about you don’t die for me, and instead we work together to win this?"
            show vanessa casual sad
            va "I never work with other people, but..."
            show vanessa casual basic
            va "If the two of us working together, or even working with them, is what it takes to keep you safe..."
            va "Then that’s what I’ll do."
        "C. Get overwhelmed.":
            $menuhideborder = False
            show hiflmc casual surprised at right2
            show vanessa casual basic at left2
            "I struggle to find something to say in response, but I come up empty."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(What can you really say to someone who just swore to protect you with her life?)"
            hide hiflmc
            show jd casual basic at centre
            "JD interrupts before I can think of anything."
            hide jd
    hide hiflmc
    hide vanessa
    show jd casual surprised at centre
    stop music fadeout 1.0
    play music hifllitecomedy
    jd "Well, damn."
    show jd casual smirk
    jd "Who could argue with that?"
    "Just like that, the moment’s broken."
    hide jd
    show vanessa casual surprised at left3
    show hiflmc casual surprised at right3
    "Vanessa lets go of my hand, like she’s just realized she was still holding it."
    show hiflmc casual blush
    "I try my best not to miss the feeling of her hands around mine."
    show hiflmc casual happy
    mcvan "Thank you, Vanessa. Seriously."
    hide hiflmc
    hide vanessa
    show razi casual surprised at centre
    ra "I... guess that settles that, then."
    show razi casual basic
    ra "Just remember that we want to help, however we can."
    show razi casual happy
    ra "Please don’t hesitate to call us if you need us."
    hide razi
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Okay, sometimes my friends are pretty cool.)"
    hide hiflmc
    show razi casual happy at left3
    show hiflmc casual happy at right3
    mcvan "I definitely will. Thanks, Razi."
    hide hiflmc
    hide razi
    show vanessa casual sleep at centre
    "Vanessa sighs, looking reluctant."
    show vanessa casual basic
    va "If it comes to an emergency, I suppose the enemy of my enemy is my friend."
    show vanessa casual angry
    va "For the time being."
    hide vanessa
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Hey, it’s progress. I’ll take it.)"
    hide hiflmc
    show razi casual happy at left3
    show vanessa casual basic at right3
    "Razi gives Vanessa a startled grin, surprised by her concession."
    ra "Duly noted. I’m glad we can all work on the same team for now, then."
    hide vanessa
    show razi casual basic
    show hiflmc casual basic at right3
    ra "Also, [genericfn]..."
    ra "After the day you had yesterday, you should probably take the day off and catch your breath."
    hide razi
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(He’s not wrong.)"
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(And as much as I need the money from today’s shift, a mental health day sounds divine.)"
    hide hiflmc
    show hiflmc casual happy at right3
    show vanessa casual basic at left3
    "We say our goodbyes and head out into a bright, sunny day."
    scene bg main_day at bg with wiperight
    pause 0.5
    show vanessa casual basic at left3
    show hiflmc casual basic at right3
    stop music fadeout 1.0
    play music hifleveryday
    va "So, since it looks like you have the day off... what is there to do in this town?"
    show hiflmc casual surprised
    "Before I can think of an answer, my stomach growls again. This time even louder."
    show hiflmc casual blush
    show vanessa casual happy
    "Vanessa laughs, and again I’m struck by the difference between how she acts when we’re alone versus how she is with the others."
    show vanessa casual smirk
    va "Sounds like lunch is our first stop, then."
    va "Is the diner the only place to eat?"
    show hiflmc casual basic
    mcvan "Pretty much, unless you’re craving some bowling alley mozzarella sticks."
    va "I don’t think you can crave something you’ve never eaten before."
    show vanessa casual surprised
    va "Why? Are they really good?"
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Oh my god.)"
    hide hiflmc
    show vanessa casual basic at left3
    show hiflmc casual surprised at right3
    mcvan "You’ve never eaten mozzarella sticks before?!"
    show vanessa casual sad
    va "No... but now I get the sense that I need to."
    show hiflmc casual happy
    mcvan "Absolutely you do."
    mcvan "But later. For now, let’s get some real food."
    show bg diner_lights_on at bg with wipedown
    show hiflmc casual basic
    show vanessa casual basic
    "There aren’t many people at Luce’s diner at this time of day, so we grab a seat in a booth."
    hide hiflmc
    hide vanessa
    show luce casual basic at centre
    lu "Hi there, [genericfn]. You ladies ready to order?"
    show luce casual basic at left3
    show hiflmc casual basic at right3
    mcvan "Hey, Luce. I’ll have a cheeseburger and fries."
    hide luce
    show vanessa casual basic at left3
    mcvan "Vanessa?"
    hide hiflmc
    hide vanessa
    show luce casual angry at centre
    "Luce eyes Vanessa warily, and I resist the urge to roll my eyes."
    hide luce
    show vanessa casual basic at left3
    show hiflmc casual basic at right3
    va "What do you recommend?"
    show vanessa casual sad
    va "I barely had time to drink my coffee last time I was here."
    show vanessa casual basic
    show hiflmc casual happy
    mcvan "Well, what do you like?"
    va "I usually eat pretty healthy."
    va "Lean protein, fruits, and veggies, whole-grains, etcetera."
    hide vanessa
    show hiflmc casual surprised
    show luce casual basic at left3
    mcvan "Then uh... Luce, make that two burgers."
    show luce casual angry
    mcvan "But no bun on the second one. And a salad instead of fries, please."
    "Luce gives me the most affronted look I’ve ever seen."
    lu "Sure thing, hun."
    hide luce
    show hiflmc casual sarcastic at centre
    "The passive-aggressive judgment in her voice is a little ridiculous, even by this town’s standards."
    show hiflmc casual happy
    "It’s hard to resist the urge to laugh at the situation as she leaves."
    show hiflmc casual happy at right3
    show vanessa casual surprised at left3
    "Vanessa stares at me, baffled."
    va "Is there something wrong with what you ordered?"
    va "It sounded good..."
    mcvan "Nope. Nothing at all wrong with it."
    mcvan "We just don’t get a lot of health-conscious eaters in this town."
    hide hiflmc
    hide vanessa
    show luce casual angry at centre
    "Luce brings our food out."
    hide luce
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    "I dig in immediately, ravenous, but Vanessa takes her time."
    mcvan "So, what do you usually eat when you’re out monster hunting?"
    show vanessa casual smirk
    va "Well, my mini-kitchen is a life-saver."
    va "I get a lot of use of my rice-cooker."
    va "I meal-prep in advance too, when I have the time."
    show vanessa casual basic
    va "I live my life according to the food pyramid."
    va "I’m only human, so I have to keep to a pretty strict diet and fitness regimen to do what I do."
    show vanessa casual sad
    va "Since I don’t get certain... supernatural benefits that my enemies have."
    hide vanessa
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(And here I am, inhaling fries like a starved woman.)"
    "(It’s a wonder I haven’t just turned into a potato already.)"
    hide hiflmc
    show hiflmc casual surprised at right3
    show vanessa casual basic at left3
    mcvan "Well, uh, it’s clearly working for you."
    hide hiflc
    hide vanessa
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Oh god, why.)"
    "(How did that come out of my mouth.)"
    hide hiflmc
    show hiflmc casual basic at right3
    show vanessa casual sad at left3
    va "Thanks, though I need to step it up considering how poorly yesterday went."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Not... exactly what I meant.)"
    show hiflmc casual_cu blush_cu
    "(But hey, at least she didn’t recognize my terrible flirting.)"
    show hiflmc casual_cu basic_cu
    "(Time to shift gears, then.)"
    hide hiflmc
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    mcvan "You keep saying that you work alone."
    mcvan "So you’ve never had a partner, or anything?"
    va "No, never."
    show vanessa casual sad
    va "Working with others... let’s just say it’s more than strongly discouraged by the Helsing order."
    mcvan "So no partner, then."
    show hiflmc casual happy
    show vanessa casual basic
    mcvan "I bet there must be a lot of people who are really grateful to you for saving them, though."
    mcvan "Anything ever happen, there?"
    show vanessa casual sad
    show hiflmc casual basic
    "Vanessa furrows her eyebrows in question, like she’s not sure what I’m getting at."
    va "Of course many people are grateful towards me and try to offer me some kind of reward."
    va "But I don’t do this for rewards."
    show vanessa casual basic
    va "I have everything I need."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Oh my god, Vanessa.)"
    show hiflmc casual_cu basic_cu
    "(Okay, looks like being subtle is off the table, here.)"
    hide hiflmc
    show hiflmc casual basic at right3
    show vanessa casual basic at left3
    mcvan "So no girlfriends? Boyfriends?"
    show vanessa casual surprised
    "Vanessa’s eyes go wide, and a blush suffuses her cheeks."
    va "What? Where did that-?!"
    show vanessa casual sleep
    "She shakes her head."
    show vanessa casual basic
    va "No. I’ve never dated anyone."
    va "The order frowns on romantic partnerships almost more than business partnerships."
    va "And regardless, I move around too much."
    va "Work is my entire life– as it should be."
    show vanessa casual angry
    va "Protecting humanity is more important than having a girlfriend."
    hide hiflmc
    hide vanessa
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(She doesn’t even know enough about what she’s missing out on to realize that she is missing out.)"
    hide hiflmc
    show hiflmc casual surprised at right3
    show vanessa casual basic at left3
    mcvan "So you’ve never gotten to go on casual dates?"
    show hiflmc casual sad
    mcvan "Or even just hang out with friends?"
    "Vanessa shrugs, unbothered."
    va "No. It’s really fine, though. Honestly."
    show hiflmc casual basic
    mcvan "Well, do you want to?"
    show vanessa casual surprised
    va "Do I want to what?"
    show hiflmc casual happy
    mcvan "Go, do fun stuff together!"
    mcvan "You’ve got to stick with me for the time being anyway, so why not have some fun in the meantime?"
    show vanessa casual blush
    va "I guess there’s no harm in that... what did you have in mind?"
    mcvan "Have you ever been bowling?"
    va "No..."
    "She trails off, but excitement at the idea is clear on her face."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e8c2:
        "A. Take Vanessa to cosmic bowling night." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc casual happy at right3
            show vanessa casual blush at left3
            mcvan "Then let’s fix that!"
            show vanessa casual sad
            va "Are you sure you want to go back to work on your day off?"
            mcvan "It can be fun, when I’m not on the clock."
            "Vanessa still looks hesitant."
            show vanessa casual sad
            mcvan "Unless you don’t want to..."
            show hiflmc casual basic
            show vanessa casual surprised
            va "No, I do!"
            show vanessa casual sad
            va "I just don’t know how."
            show hiflmc casual happy
            mcvan "That’s not a problem! I can teach you, if you want."
            show vanessa casual blush
            va "...I have actually always wanted to try it."
            show vanessa casual sad
            va "I just never had the time, or friends to go with."
            hide vanessa
            hide hiflmc
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(I can’t imagine anyone not wanting to spend time with her.)"
            hide hiflmc
            show hiflmc casual happy at right3
            show vanessa casual sad at left3
            mcvan "Well, it’s time to change that."
            show vanessa casual smirk
            va "I’m looking forward to it."
            show vanessa casual happy
            va "Ooh, can I try the mozzarella sticks you mentioned earlier, too?"
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(It’s adorable the way she goes from hesitant to excited so quickly.)"
            hide hiflmc
            show hiflmc casual happy at right3
            show vanessa casual happy at left3
            mcvan "We can have as many mozzarella sticks as you want."
            scene bg bowling_cosmic at bg with clockwise_wipe
            stop music fadeout 1.0
            play music hifllitegetitdone
            "When we get back to the bowling alley, everyone but Razi is gone."
            show razi casual surprised at centre
            "He does a double-take when we walk in, obviously shocked to see us back so soon."
            ra "[genericfn]?"
            ra "What are you doing here? Is everything okay?"
            show razi casual surprised at left3
            show hiflmc casual basic at right3
            mcvan "Everything’s fine."
            mcvan "I’m actually here as a customer, this time."
            show razi casual smirk
            "I can tell the exact moment he grasps the situation, his expression sliding into a playful smirk."
            ra "Of course."
            ra "As you can see, you’ve got free run of the place, so pick whatever lane you want."
            show razi casual happy
            ra "Everything is on the house, for my favorite employee."
            show hiflmc casual surprised
            mcvan "You don’t have to do that..."
            ra "Seriously, go. Have fun. You’ve earned it."
            hide hiflmc
            hide razi
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(Well, who am I to argue with that?)"
            hide hiflmc
            show hiflmc casual surprised at right3
            show razi casual happy at left3
            mcvan "Seriously, thank you so much."
            mcvan "You’re the best."
            show hiflmc casual happy
            mcvan "Oh, and can we get a couple of orders of mozzarella sticks?"
            "Razi throws his head back and laughs."
            show razi casual smirk
            ra "I’m glad the recent excitement hasn’t done any harm to your appetite."
            ra "I’ll bring over your mozzarella sticks when they’re ready."
            mcvan "Thanks, boss."
            show hiflmc casual basic
            hide razi
            show vanessa casual basic at left3
            "I lead Vanessa over to the shoe rental kiosk. She eyes them with trepidation."
            show vanessa casual surprised
            va "Wait, you need special shoes for this?"
            va "That you... rent?"
            show hiflmc casual sad
            mcvan "They’re not the most comfortable shoes, but it’s a part of the experience."
            show hiflmc casual basic
            show vanessa casual basic
            "Vanessa nods solemnly."
            va "Of course."
            show vanessa casual smirk
            va "If I’m going to do this, I want to do it right."
            hide vanessa
            show hiflmc casual basic at centre
            "I duck back behind the counter and grab a couple of pairs of shoes."
            show hiflmc casual happy at right3
            show vanessa casual angry at left3
            "It’s extremely hard not to laugh at Vanessa as she puts hers on, grumbling about how they ruin her aesthetic."
            mcvan "I know they’re not exactly high fashion, but the bowling shoe look is pretty universal."
            show hiflmc casual basic
            show vanessa casual basic
            va "I’m sure high-heeled bowling shoes exist somewhere."
            show vanessa casual sad
            va "But I suppose I can deal with these for the sake of the authenticity of the experience."
            show hiflmc casual happy
            mcvan "That's the spirit."
            show vanessa casual basic
            "We head to a lane, and I help Vanessa enter our names in the machine."
            mcvan "Bowling itself is not super complicated."
            mcvan "You just run up to the line and throw the ball, in as straight a line as you can."
            mcvan "The tricky part is throwing it with enough precision and power to knock down all the pins."
            hide vanessa
            show hiflmc casual basic at centre
            "I go first, to show her how it’s done."
            mcvan "So you want to take three long steps toward the line..."
            mcvan "And time it so that your non-dominant foot lands as you reach the peak of your swing."
            show hiflmc casual happy
            mcvan "Like so."
            show hiflmc casual angry
            "I throw my bowling ball as hard as I can, and manage to knock down about 6 pins."
            show hiflmc casual surprised
            "(Not my best, but not bad.)"
            show hiflmc casual basic
            "On my second swing, I knock down three of the remaining four."
            show hiflmc casual happy at right3
            show vanessa casual basic at left3
            mcvan "See? Not too hard."
            hide hiflmc
            show vanessa casual basic at centre
            "Vanessa picks out a medium-weight, dark purple, sparkly bowling ball."
            show vanessa casual basic at left1
            show hiflmc casual basic at right1 behind vanessa
            "I stand behind her, helping her find her stance."
            show hiflmc casual blush
            "It’s hard not to get flustered by the proximity, but I try to stay friendly and helpful."
            show hiflmc casual basic
            mcvan "Remember, rhythm and timing are key."
            va "This kind of reminds me of when I was first learning to use my whip."
            show vanessa casual smirk
            va "Those are important to keep in mind with that, as well."
            va "I think I’m ready to try."
            hide hiflmc
            show vanessa casual basic at centre
            "She strides forward and throws the ball with perfect form, knocking down all ten pins."
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(Of course she’s a natural at this.)"
            show hiflmc casual_cu blush_cu at hiflmc_cu
            "(I don’t think there’s anything she can’t do well.)"
            hide hiflmc
            show hiflmc casual basic at right3
            show vanessa casual happy at left3
            "She turns to me with a beaming, excited grin."
            va "I did it!"
            show hiflmc casual happy
            mcvan "You were awesome!"
            show hiflmc casual surprised at right1
            show vanessa casual happy at left1 behind hiflmc
            "She hugs me just as Razi drops off the mozzarella sticks."
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(Oh my god we’re hugging.)"
            show hiflmc casual_cu blush_cu
            "(This is fine. I’m fine. It’s a friendly hug.)"
            "(I’m not going to do anything stupid like comment on how good she smells.)"
            hide hiflmc
            show hiflmc casual blush at right1
            show vanessa casual happy at left1 behind hiflmc
            "I cough once and gesture to the mozzarella sticks."
            show hiflmc casual happy
            mcvan "Time to celebrate your newfound skills!"
            show hiflmc casual basic at right3
            show vanessa casual surprised at left3
            "Vanessa bites into the mozzarella stick, and immediately her face lights up."
            show vanessa casual smirk
            va "This is the best thing I’ve ever eaten."
            show hiflmc casual happy
            mcvan "I know, right?"
            hide hiflmc
            hide vanessa
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(When was the last time she got to just relax and enjoy herself like this?)"
            show hiflmc casual_cu happy_cu
            "(I’m glad we did this.)"
            "(I think we both needed it.)"
        "B. Don't take her out.":
            $menuhideborder = False
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(On second thought, Vanessa probably won’t have a great time with the supernaturals...)"
            show hiflmc casual_cu sarcastic_cu
            "(And I really don’t want to push my luck on the progress she made today.)"
            hide hiflmc
            show hiflmc casual basic at right3
            show vanessa casual basic at left3
            mcvan "You know what?"
            mcvan "Let's save that for another time."
            show hiflmc casual happy
            mcvan "Why don't I just give you a tour of the town instead?"
            show vanessa casual smirk
            va "I'd like that."
    scene bg van_interior_loft_night at bg with fade
    pause 0.5
    show hiflmc casual happy at right3
    show vanessa casual smirk at left3
    stop music fadeout 1.0
    play music hiflliteromance
    "We're both in a great mood when we get back to the van."
    show hiflmc casual surprised
    mcvan "By the way, does your van have a name or something we can call it?"
    show hiflmc casual sarcastic
    mcvan "Van’s van is fun to say the first couple of times, but it must get old."
    show hiflmc casual basic
    show vanessa casual surprised
    va "I hadn’t really thought about it..."
    show vanessa casual smirk
    va "But you’re welcome to give it a name, if you want."
    show hiflmc casual happy
    mcvan "Give me some time to think up a really good one, and I’ll get back to you."
    show vanessa casual happy
    "Vanessa laughs."
    show vanessa casual smirk
    va "Sounds like a plan."
    hide hiflmc
    show vanessa casual basic at centre
    "Vanessa turns to me with a more serious expression."
    va "Thank you for today."
    va "I haven’t had that much fun in a long time."
    show vanessa casual sad
    va "Or possibly ever."
    show vanessa casual smirk
    va "So. It meant a lot."
    show vanessa casual smirk at left3
    show hiflmc casual blush at right3
    "Heat rises to my face."
    mcvan "I’m glad you had so much fun."
    show hiflmc casual happy
    mcvan "I had a good time too."
    show vanessa casual surprised
    va "Really?"
    mcvan "Yeah! I like spending time with you."
    show hiflmc casual sad
    "Of course I immediately ruin the moment with an enormous yawn."
    show vanessa casual basic
    va "We should probably go to sleep soon."
    va "Today was fun, but tomorrow we get back to work."
    mcvan "Yeah, I guess you're right."
    show hiflmc casual surprised
    show vanessa naked basic
    "Vanessa takes off her dress, and I freeze in place."
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Oh my god?!)"
    "(What?!)"
    hide hiflmc
    show hiflmc casual surprised at right3
    show vanessa naked basic at left3
    "She looks at me curiously."
    va "Make yourself comfortable."
    show vanessa naked sad
    va "I’m sorry we didn’t think to grab your pajamas from home, but we can do that soon."
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Right.)"
    "(She’s just getting changed.)"
    "(Of course.)"
    hide hiflmc
    show hiflmc casual blush at right3
    show vanessa naked basic at left3
    "She strips down to her underwear, which are a gorgeous matching lace lingerie set that renders me absolutely speechless."
    hide vanessa
    hide hiflmc
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(Just... wow.)"
    show hiflmc casual_cu surprised_cu
    "(Wait. No.)"
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Eyeballs back in your head, [genericfn], stop staring.)"
    hide hiflmc
    show hiflmc pajamas noglassesbasic at centre
    "I turn around and change out of most of my clothes, keeping on my t-shirt."
    show hiflmc casual_cu noglassessarcastic_cu at hiflmc_cu
    "(Vanessa may feel comfortable sleeping in her underwear, but I definitely don’t.)"
    hide hiflmc
    show hiflmc pajamas noglassesbasic at right3
    show vanessa naked basic at left3
    mcvan "Hey, do you have a spare blanket I can use tonight?"
    show vanessa naked sad
    "Vanessa suddenly looks concerned, darting towards the heating control panel."
    va "Is it too cold in here?"
    show hiflmc pajamas noglassessurprised
    mcvan "No, it’s fine, don’t worry!"
    show hiflmc pajamas noglassesbasic
    mcvan "A blanket will just help me sleep better in the passenger seat, that’s all."
    show vanessa naked basic
    va "Why would you sleep in the passenger seat when there’s a perfectly good bed right here?"
    show hiflmc pajamas noglassessurprised
    "I look back at the bed, which continues to be as small as it was last night."
    mcvan "If you're sure..."
    show hiflmc pajamas noglassesblush at right2
    show vanessa naked basic at left2
    "We climb into her bed, and I focus very hard on anything other than all the places where our bodies are touching."
    hide hiflmc
    hide vanessa
    show hiflmc pajamas_cu noglassesblush_cu at hiflmc_cu
    "(This is so much.)"
    show hiflmc pajamas_cu noglassessarcastic_cu
    "(There’s no way I’m going to fall asleep like this.)"
    show hiflmc pajamas_cu noglassessurprised_cu
    "(Maybe if I scoot back...?)"
    hide hiflmc
    show hiflmc pajamas noglassesbasic at right2
    show vanessa naked basic at left2
    "I try to shift and give us both a sliver of personal space, but..."
    show hiflmc pajamas noglassessurprised at right3
    "I nearly fall over the edge."
    scene vanessa3 at bg:
        yanchor 0.1
        linear 8 zoom 0.4
    stop music fadeout 1.0
    play music hiflheavyromance
    pause
    "Vanessa wraps an arm around me with those lightning-quick reflexes and pulls me closer to her."
    "(Oh god, her face is so close now.)"
    "(Come on, [genericfn], say something to make this less awkward.)"
    menu vans1e8c3:
        "A. Fancy meeting you here.":
            mcvan "Uh... Fancy meeting you here?"
            "Vanessa snorts with laughter, but it does nothing to diffuse the redness on her cheeks."
        "B. My hero.":
            mcvan "Wow, even when there are no vampires to fight, you’re still my hero."
            "Vanessa blushes furiously, eyes going wide."
            va "I mean-!"
            va "I just-!"
            va "You were-!"
            va "I... Uh..."
            va "You're welcome?"
        "C. Falling is bad.":
            mcvan "Thanks for catching me."
            mcvan "Falling would be... bad."
            "She laughs gently."
            va "I did promise to protect you."
    "Despite how loudly my heart is pounding from the closeness, I feel strangely comfortable in Vanessa’s arms."
    "I feel safe with her in a way that I’ve never felt with anyone else."
    "(Maybe it’s because I know that she’ll protect me no matter what?)"
    "(But maybe it’s just... her.)"
    "(How fierce and dedicated she is, and how kind and gentle she can be.)"
    "(Whatever it is...)"
    "(I trust her in a way I’ve never really trusted anyone before.)"
    "Soothed by the steady rhythm of her breathing, and the comfort of her arms, I fall asleep quickly."
    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
