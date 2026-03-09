label fiona_season1_episode9:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg_wll_town_hall_lights at bg with fade
    play music wlleverydayupbeat1

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show fiona cape surprised at right1
    show wllmc coat basic at left1plus
    "Fiona is silent for a long moment, and I wait on tenterhooks, wondering why the answer is taking so long."
    show fiona cape smirk
    mb "You know, maybe there's a way we can do this without the ring at all."
    mb "Witches are supposed to have incredible powers, after all."
    show wllmc coat sad
    mcfiona "You're forgetting I don't know the first thing about being a witch."
    show fiona cape grin
    mb "True. But that's a solvable problem."
    show fiona cape smirk
    mb "Especially when you've got a gal who knows basically everything there is to know about magic."
    show fiona cape grin
    "She presses a hand to her chest self-importantly, and then breaks face by laughing."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(I can't help thinking, did she dodge my question, or just not hear it?)"
    hide wllmc
    show fiona cape grin at right1
    show wllmc coat angry at left1plus
    "I bite my lip, the words itching to get out."
    hide fiona
    hide wllmc
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(What do you think of love, Fiona Eichen?)"
    "(Do I dare to ask you twice, and risk you guessing the answer might actually mean something to me?)"
    hide wllmc

    $menuhideborder = True
    menu fionas1e9c1:
        "Ask Fiona about love while you still have the nerve." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show fiona cape grin at right1
            show wllmc coat smirk at left1plus
            mcfiona "Don't think you can wheedle your way out of answering my question."
            mcfiona "I gave you a little honesty, I want some in return."
            show fiona cape smirk
            mb "You want a philosophical essay on the nature of love?"
            show wllmc coat smile
            mcfiona "By all means. Hit me with whatever scholarly article you've got tucked away in that weird brain of yours."
            show fiona cape smile
            "Fiona giggles."
            show fiona cape grin
            mb "How did you know? I've actually thought about writing one."
            mb "That's the thing about being a fortune teller. You see so many kinds of love."
            show wllmc coat grin
            mcfiona "I guess everyone wants to know if they'll find someone special."
            mb "Exactly."
            show fiona cape smile
            mb "There's the people so desperate for love they can't see it staring them in the face."
            show wllmc coat smallsmile
            mb "The ones who are convinced they fall in love once a month, but flit like moths from lamp to lamp."
            mb "The ones who furiously deny they have feelings at all, even as every step pulls them deeper in."
            show wllmc coat surprised
            mcfiona "Do you ever see 'true' love?"
            show fiona cape sad
            "Fiona shifts from foot to foot, looking away."
            mb "What do you mean by that?"
            show fiona cape smile
            mb "There's all kinds of love in the world, right? I mean, the love parents have for their children, that's pretty damn true when it's there."
            show wllmc coat sad
            mcfiona "I suppose."
            "Now it's my turn to get shifty."
            show fiona cape surprised
            mb "Oh, I'm sorry. I didn't mean to bring up bad memories."
            show wllmc coat smallsmile
            mcfiona "Not your fault. It's not like mine hated me or anything. They're decent folk. They just found my oddity hard to bear."
            hide wllmc
            hide fiona
            show fiona cape_cu sad_cu at fiona_cu
            "Fiona wraps her arms tight around me and gives me a squeeze."
            mb "That must have been painful."
            hide fiona
            show fiona cape sad at right1
            show wllmc coat basic at left1plus
            "She leans back a little so she can look at me."
            mb "My family are all just as odd as I am, if not more so."
            show wllmc coat sad
            mcfiona "That sounds terrifying."
            mb "Absolutely. But it makes them easy to love."
            show fiona cape smile
            mb "And I love my friends, too. That's another kind of true love, if you ask me."
            show wllmc coat smirk
            mcfiona "Really? Even Cecelia?"
            show fiona cape grin
            mb "Especially Cecelia. I'd die for her in a heartbeat, though I wouldn't want her in my bed."
            show wllmc coat basic
            "The way Fiona says it makes me realize how alone I am."
            hide fiona
            hide wllmc
            show wllmc coat_cu basic_cu at wllmc_cu
            "(When we met on the train, I thought the two of us were peas in a pod, but that's not true.)"
            show wllmc coat_cu sad_cu
            "(She's got a job, she's got friends, she's got a whole life.)"
            hide wllmc
            show fiona cape_cu smile_cu at fiona_cu
            "Fiona's fingers brush my cheek."
            mb "You got lost for a moment. What thoughts pulled you away from me?"
            mb "They must have been very serious, to distract you from how wonderful I am."
            hide fiona
            show wllmc coat_cu smirk_cu at wllmc_cu
            mcfiona "Actually, I was thinking about how outrageously evasive you are."
            mcfiona "I asked you about your feelings on romantic love, and you've said hundreds of words and not given me a straight answer."
            hide wllmc
            show fiona cape_cu smirk_cu at fiona_cu
            mb "How very obstinate and bullheaded of you to see through me like that."
            hide fiona
            show wllmc coat_cu smile_cu at wllmc_cu
            mcfiona "Yeah, I'm a stubborn bitch."
            hide wllmc
            show fiona cape_cu grin_cu at fiona_cu
            "Fiona laughs, and because my arms are still around her, I feel it ripple through my whole body."
            hide fiona
            show wllmc coat_cu grin_cu at wllmc_cu
            "(It still surprises me how much I like just talking with Fiona. It's as much fun as doing a job, and it feels almost as risky too.)"
            hide wllmc
            show fiona cape grin at right1
            show wllmc coat smile at left1plus
            mb "Well, if you must know..."
            hide wllmc
            hide fiona
            show fiona cape_cu sad_cu at fiona_cu
            "She looks down, bringing the crown of her head level with my nose..."
            "And I catch that sandalwood scent again, underlaid with something sweet and something floral."
            mb "I've never been in love."
            mb "When you say that, people like to reassure you. Tell you you never know what's around the corner."
            mb "But for me, the future's not exactly a closed book."
            hide fiona
            show fiona cape sad at right1
            show wllmc coat surprised at left1plus
            mcfiona "And you're okay with that?"
            show wllmc coat sad
            mb "Mostly. I have my 'what-if' moments. Love is a beautiful dream, and I like beautiful things."
            hide wllmc
            hide fiona
            show fiona cape_cu smile_cu at fiona_cu
            "She looks back up, and her honey-sweet eyes dance with laughter as they catch mine."
            mb "That's probably why I enjoy your company so much."
            hide fiona
            show fiona cape smile at right1
            show wllmc coat smirk at left1plus
            mcfiona "Smooth words to get a woman into your bed."
            show fiona cape smirk
            mb "Of course. That's where beautiful women look best."
            "She dances her fingers up my arm, and then slides them round my neck."
            show fiona cape smile
            mb "And that's why we should get back to work."
            show wllmc coat smile
            mcfiona "Horrible goblin."
            hide wllmc
            hide fiona
            "As we leave, I can't help thinking that my earlier comment remains true."
            show wllmc coat_cu sad_cu at wllmc_cu
            "(So many words, and every one felt like she was evading the topic with a deft hand.)"
        "Stay silent.":
            $menuhideborder = False
            show wllmc coat_cu angry_cu at wllmc_cu
            "(I don't.)"
            hide wllmc
            show fiona cape smile at right1
            show wllmc coat sad at left1plus
            "The impulse fades, leaving me feeling momentarily doleful."
            show fiona cape basic
            mcfiona "Come on, let's get out of here."

    scene bg_wll_apothecary_lights at bg
    stop music fadeout 1.0
    play music wlleverydaycalm3 fadein 1.0
    show wllmc coat basic at left2
    show fiona cape smile at right1plus
    with fade
    "The next day, Fiona and I set up in the apothecary's, and between serving customers, we get to work on my actual magical training."
    mb "Before you can dazzle the world with your skills, we need to teach you the basics."
    "She takes a bite of the apple I brought her as I lean over her shoulder to read the book she left open."
    show wllmc coat smirk
    mcfiona "Looks like a lot of mumbo jumbo to me. All this stuff about entropy and tapping into the forces of the universe."
    show fiona cape smirk
    mb "That book is new and theoretical. I'll tell you what you need to know."
    show wllmc coat smallsmile
    show fiona cape smile
    mb "Magic comes from the minds and wills of living beings."
    mb "That little spark inside your head that says 'I want to live. I want to do great things.'"
    show wllmc coat sad
    mcfiona "That ain't a spark for me. It's a raging wildfire."
    show wllmc coat sad behind fiona:
        easein 0.4 left1
    show fiona cape smile:
        easein 0.4 right1
    "Somehow, somewhere along the way, Fiona and I moved closer together."
    "It only takes the slightest movement to pull her into my arms."
    show wllmc coat smirk
    mcfiona "Maybe that's why I can never resist the things I want."
    show fiona cape smirk
    mb "What excuse does that give me?"
    hide wllmc
    hide fiona
    show fiona cape_cu sleep_cu at fiona_cu
    "She pushes herself up onto her toes and kisses me..."
    "And whatever lesson I was supposed to be learning seems so much less important than the sweetness of her lips."
    hide fiona
    show wllmc coat smallsmile at left2
    show fiona cape basic at right1plus
    "We do get back to it eventually, since Fiona can be irritatingly diligent."
    show wllmc coat surprised
    mcfiona "So what's the difference between witches and mystics and whatever the rest of the Ward are?"
    show fiona cape smirk
    mb "The rest of the Ward keep their own secrets and tell their own stories, you nosy thing."

    scene bg_wll_mc_room_day at bg with fade
    stop music fadeout 1.0
    play music wlleverydaycalm1 fadein 1.0
    "We're in my bedroom today, lying on the floor and looking at each other, books forgotten at our feet."
    show wllmc skirt smallsmile at left2
    show fiona dress smile at right1plus
    mb "But witches and mystics do have similar powers."
    mb "Except, I'm riding on someone's coattails, while you're flying under your own power."
    show wllmc skirt smirk
    mcfiona "No wonder you all think witches are so special."
    show fiona dress smirk
    mb "I think you're special for lots of reasons, my pearl."
    show wllmc skirt embarrassed
    show fiona dress smirk behind wllmc:
        easein 0.4 centre xoffset 44
    "She reaches out and brushes a curl from my cheek, and I forget whatever I was going to ask next."
    hide fiona
    hide wllmc
    show wllmc skirt_cu smile_cu at wllmc_cu
    "(In spite of Fiona's moment of temptation in the hot spring, we've kept to our bargain.)"
    show wllmc skirt_cu smirk_cu at wllmc_cu
    "(We might kiss and touch, but there's a line we've held ourselves back from crossing. For now.)"

    scene bg_wll_apothecary_lights at bg with fade
    stop music fadeout 1.0
    play music wlleverydayupbeat3 fadein 1.0
    "I do learn some magic, when I'm not distracting Fiona with more fun activities."
    show wllmc coat surprised at left2
    show fiona cape smile at right1plus
    mcfiona "Why do I even need to memorize spells? If magic is just will, can't I snap my fingers and make anything happen?"
    mb "I mean, yes. In theory. It's not usually so easy in practice though."
    mb "It's like water. Over time, spells etch out a groove, a riverbed in the fabric of the world."
    show wllmc coat smile
    mcfiona "So if you follow them, you get to the sea."
    show fiona cape grin
    mb "I adore it when you complete my metaphors."
    show wllmc coat smirk
    mcfiona "I've never been great at taking the route I'm supposed to."
    show fiona cape smile
    mb "I know. That's why I find you so exciting. I might not be able to see your future, but I know it all the same."
    show fiona cape grin
    mb "Someday, you're going to revolutionize everything. I can't wait to see it."
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(That's a lot of pressure to live up to.)"

    scene bg_wll_cemetery_night_lights at bg with fade
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    "That night, we head back to the graveyard for some actual ghost-cleansing practice."
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(We're on a deadline, after all, and Sunmok is still giving the town trouble.)"
    hide wllmc
    show nathan redcoat_hat angry_hat at left3
    show sascha belt angry_hat at right4
    "Nathan and Sascha are already there, arms folded, eyeing each other up like two territorial tom-cats."
    hide nathan
    hide sascha
    show wllmc vest_hat smirk at left2
    show fiona cloak grin at right1plus
    mcfiona "My my, look at all this tension. Seems to me you boys need a release."
    show fiona cloak smirk
    mb "That's what I've been saying for years."
    hide wllmc
    hide fiona
    show nathan redcoat_hat angry_hat at left3
    show sascha belt angry_hat at right4
    "They give us identical filthy looks, but at least it stops them hissing at each other."
    wc "I'm ready to go if you are, [genericfn]."

    scene white:
        matrixcolor TintMatrix("#bddcff")
    pause 0.1
    scene bg_wll_cemetery_night_lights at bg
    show fog_effect:
        alpha 0.7
    show nathan_ghost_effect
    show nathan ghost angry_ghost at centre
    with dissolve
    "He shrugs his shoulders, and blue light explodes from under his skin, dropping the temperature and making me shiver."
    hide nathan_ghost_effect
    hide nathan
    hide fog_effect
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(He's a ghost!)"
    hide wllmc
    show wllmc vest_hat basic at centre
    "I school my face into a calm mask."
    hide wllmc
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(Number one rule, never show shock or fear.)"
    hide wllmc
    show wllmc vest_hat smirk at left2
    show fiona cloak basic at right1plus
    mcfiona "Well. Everyone in the Ward sure is full of surprises."
    show fiona cloak smirk
    "Fiona rolls her eyes at me."
    mb "It's okay to say you think he's cool, you know. Even by our standards, Nate's pretty special."
    "I take the high road and ignore her, but something else has me hesitating."
    show wllmc vest_hat sad
    mcfiona "Are you sure this won't hurt you?"
    hide wllmc
    hide fiona
    show fog_effect:
        alpha 0.7
    show nathan_ghost_effect
    show nathan ghost smirk_ghost at centre
    wc "Don't sweat it. You don't have to see the ritual all the way through."
    hide nathan_ghost_effect
    hide nathan
    hide fog_effect
    show wllmc vest_hat sad at left2
    show fiona cloak smirk at right1plus
    mb "If I think you're putting him in danger, I'll break the spell."
    show wllmc vest_hat basic
    "I look down at the words of the ritual, written in Fiona's messy handwriting."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(It's based on the cleansing spells she uses for objects.)"
    hide wllmc
    show wllmc vest_hat sad at centre
    "As I recite the words and sprinkle the salt and ash on Nathan, I find myself feeling nervous."
    hide wllmc
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(Please let this work. Power, help me out. Let me find the strength I need to see this through.)"
    hide wllmc
    show wllmc vest_hat sad at centre
    "I finish the spell, and there's a moment of silence."
    hide wllmc
    show fog_effect:
        alpha 0.7
    show nathan_ghost_effect
    show nathan ghost basic_ghost at centre
    wc "Is that it?"
    scene bg_wll_cemetery_night_lights at bg
    show wllmc vest_hat surprised at centre
    with hpunch
    "The ground shakes, and a huge gout of ash and sparks and smoke soars into the air."
    show fog_effect with dissolve:
        alpha 0.5
    $sidecharone = "Earth-shaking Voice"
    sid1 "Summoned at last! Finally, I emerge, and now the whole world will tremble."
    hide wllmc
    hide fog_effect
    show fiona cloak angry at centre
    mb "[genericfn], get back!"
    hide fiona
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(What have I done?)"
    hide wllmc
    show enzo familiar angry at centre
    "The smoke clears, and I stop short as I see what was hiding inside."
    hide enzo
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    "(What is that? It's... kind of cute, actually.)"
    hide wllmc
    show wllmc vest_hat surprised at left2
    show enzo familiar smile at right3
    $sidecharone = "Fuzzy Spirit"
    sid1 "Finally, Mistress! I thought a genius like you would have called on me months ago."
    mcfiona "Are you... talking to me?"
    sid1 "Of course! You called for power, and here I am. One familiar, at the ready. Nice to finally meet you, Mistress. I'm Enzo."
    hide wllmc
    hide enzo

    $menuhideborder = True
    menu fionas1e9c2:
        "Hi, Enzo.":
            $menuhideborder = False
            show wllmc vest_hat grin at left2
            show enzo familiar smile at right3
            mcfiona "Hi, Enzo. I'm [genericfn]."
            hide enzo
            hide wllmc
            show wllmc vest_hat_cu angry_cu at wllmc_cu
            "(Goddess, I sound like it's my first day at school or something.)"
            hide wllmc
            show wllmc vest_hat surprised at left2
            show enzo familiar smile at right3
            enz "Oh, I know who you are, Mistress. I've been waiting for you for a long time."
        "Sorry I kept you waiting?":
            $menuhideborder = False
            show wllmc vest_hat sad at left2
            show enzo familiar smile at right3
            mcfiona "Oh, uh, hi? Sorry I kept you waiting?"
            enz "Very gracious of you to apologize, Mistress, but it's fine. I'm just glad to be here now!"
        "You certainly are familiar.":
            $menuhideborder = False
            show wllmc vest_hat smirk at left2
            show enzo familiar smile at right3
            mcfiona "You certainly are familiar. Overly-so, I might even say."
            "Enzo cackles."
            enz "A wit! You and I are going to get on just fine."

    hide wllmc
    hide enzo
    show fiona cloak surprised at centre
    "A muffled squeak sounds, and I see that Fiona has pressed her hands to her mouth, eyes wide."
    show fiona cloak grin at left2
    show enzo familiar smile at right3
    mb "You. Are. Adorable! Can I pet you?"
    show fiona cloak grin:
        easein 0.4 left1 xoffset 20
    show enzo familiar angry:
        pause 0.1
        easein 0.4 right4
    "She reaches out a hand tentatively, and Enzo zooms away, scowling at her."
    enz "Who's this weirdo?"
    show wllmc vest_hat smile at left4 behind fiona with dissolve
    "I slide an arm around Fiona's shoulders."
    show wllmc vest_hat smirk
    mcfiona "This is Fiona. She's a certified menace."
    enz "Yeah, I can see that. Mystics are always trouble."
    hide enzo
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(It seems like he knows a lot more about the supernatural than I do.)"
    hide wllmc
    show wllmc vest_hat smirk at left4
    show fiona cloak grin at left1:
        xoffset 20
    show enzo familiar angry at right4
    mcfiona "Hey Enzo, I know you just got here, but can you tell me why my spell didn't work?"
    show enzo familiar sad
    "I explain what we were trying to do, and Enzo shakes his head."
    enz "Sorry to say it, Mistress, but that's a no-go. Even for a witch, cleansing ghosts just doesn't work that way."
    show wllmc vest_hat sad
    show fiona cloak sad
    "I slump."
    mcfiona "So we're back to square one."

    scene bg_wll_town_streets_night_lights at bg with wiperightdissolve
    stop music fadeout 1.0
    play music wlleverydaycalm3 fadein 1.0
    "Fiona and I take Enzo on a get-to-know-you tour of Wisp Willow."
    show wllmc vest_hat smallsmile at left4
    show fiona cloak surprised at left1:
        xoffset 20
    show enzo familiar basic at right4
    "As we pass the general store, Fiona stops, and then turns around."
    mb "I just remembered I need to buy some beans. Can we stop in?"
    show wllmc vest_hat smile
    mcfiona "Sure thing. Enzo, you wait here."

    play sound "audio/sfx/bell-store-entrance-ding.mp3"
    scene bg_wll_general_store_night_lights_stocked at bg
    show diana casual basicglasses at centre
    with wiperightdissolve
    "We step through the door, and right in front of us is Diana, browsing the canned goods."
    hide diana
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(Fiona. Did you see she was going to be here?)"
    hide wllmc
    show wllmc vest_hat angry at left3
    show fiona cloak basic at right3
    "I make the thieves' cant gesture for 'mark', and Fiona shrugs."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    "(That's not a no.)"
    hide wllmc
    show fiona cloak smile at left3
    show diana casual basicglasses at right3
    mb "Diana! Fancy meeting you here. Though it is a small town."
    "Behind her back, her fingers crook into a familiar shape."
    hide fiona
    hide diana
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(It's the gesture for pickpocketing. She's going to try and take Diana's ring.)"
    hide wllmc
    show fiona cloak smile at left3
    show diana casual smileglasses at right3
    fc "Oh, hello."
    "Her smile is a little strained, like she doesn't quite know what to say."
    hide fiona
    hide diana
    show wllmc vest_hat_cu angry_cu at wllmc_cu
    "(Sheriff McGann must have told her we were the ones to return the locket. I can't blame her if she has suspicions.)"
    hide wllmc
    show wllmc vest_hat angry at left3
    show fiona cloak angry at right3
    "Fiona moves, and I tip my head to the side, knowing she'll know it means no."
    hide fiona
    hide wllmc
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    "(I've got a different plan.)"
    hide wllmc
    show wllmc vest_hat smallsmile at left3
    show diana casual surprisedglasses at right3
    mcfiona "Look, Diana, we should talk."
    hide wllmc
    hide diana
    show fiona cloak basic at centre
    "I wait for Fiona to step in, to cut me off, but she doesn't."
    hide fiona
    show wllmc vest_hat surprised at left3
    show diana casual surprisedglasses at right3
    fc "About what?"
    show wllmc vest_hat sad
    mcfiona "About Sunmok."
    show diana casual sadglasses
    "Diana stiffens, and her fingers lock together."
    fc "...I see. Let's step outside."

    scene bg_wll_town_streets_night_lights at bg
    show wllmc vest_hat sad at left3
    show diana casual sadglasses at right3
    with wiperightdissolve
    stop music fadeout 1.0
    play music wllsadsong1 fadein 1.0
    "In the cool air of the street, Diana watches me warily."
    mcfiona "This is yours, I think."
    show diana casual surprisedglasses
    "I pull her photograph out of my pocket and hand it to her. Diana's mouth twists."
    show diana casual sadglasses
    fc "You two seem to have made a habit of finding my things. I wonder why that is."
    mcfiona "I didn't realize it until we saw the photo, but the ghost we told you about before, it's Sunmok."
    "Diana's shoulders hunch, and her fingers trace over the lines of her wife's face."
    fc "Oh, Sunny, what have you become?"
    hide diana
    hide wllmc
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(I can't tell if she's not surprised because she knows more than she's letting on, or if the sadness is just stronger than the shock.)"
    hide wllmc
    show fiona cloak sad at left3
    show diana casual sadglasses at right3
    mb "I'm sorry. The ghost isn't really Sunny. Just a distorted echo."
    show diana casual sleepglasses
    "Diana closes her eyes."
    show diana casual sadglasses
    fc "Are you sure? Couldn't she be in there somewhere?"
    hide fiona
    hide diana
    show wllmc vest_hat_cu sad_cu at wllmc_cu
    "(Diana's love has outlasted death.. No wonder Sunmok can't leave.)"
    hide wllmc
    show fiona cloak surprised at left3
    show diana casual sadglasses at right3
    mb "I'm sure. Do you think Sunny would ever try and hurt anyone?"
    fc "Never. She was so kind, so gentle."
    hide fiona
    show wllmc vest_hat angry at left3
    mcfiona "We want to help her."
    fc "How?"
    hide wllmc
    show fiona cloak angry at left3
    mb "We can put her soul to rest if we find the item that's tethering her to this world."
    show diana casual surprisedglasses
    "Diana's eyes widen slightly."
    fc "The locket..."
    "Neither of us says anything."
    fc "But it didn't work? She's still here, after all."
    hide fiona
    show wllmc vest_hat angry at left3
    mcfiona "We think it's your ring."
    show diana casual sadglasses
    "As soon as I say it, Diana's hand closes instinctively."
    fc "No, you can't. I can't bear to see it tarnished the way the locket was."
    hide wllmc
    hide diana

    $menuhideborder = True
    menu fionas1e9c3:
        "It'll save people's lives.":
            $menuhideborder = False
            show wllmc vest_hat sad at left3
            show diana casual sadglasses at right3
            mcfiona "I know it's hard, but giving us that ring will save people's lives."
            mcfiona "I've felt first-hand what a ghost can do. It's no laughing matter."
        "We'll take care of it.":
            $menuhideborder = False
            show wllmc vest_hat sad at left3
            show diana casual sadglasses at right3
            mcfiona "We'll take good care of it. As much as we can."
            fc "Forgive me if I don't give that promise much weight."
        "Sunny will come after you.":
            $menuhideborder = False
            show fiona cape angry at left3
            show diana casual sadglasses at right3
            "I look to Fiona, not sure what to say, and she steps in."
            mb "Sunmok hasn't attacked you yet, but while you wear that ring, you're a target. I don't want you to get hurt."

    show diana casual sleepglasses
    "Diana bites her lip, her thumb rubbing and rubbing at the smooth gold band."
    show diana casual sadglasses
    fc "I need time to think. Maybe, maybe if you help me with something..."
    fc "But I can't decide right now. I have to sleep on it."
    hide wllmc
    show fiona cloak basic at left3
    mb "Thank you for hearing us out, Diana. We'll talk tomorrow."
    hide diana
    hide fiona

    stop music fadeout 1.0
    play music wllsomber1 fadein 1.0
    show fiona cloak_cu basic_cu at fiona_cu
    "Diana walks away, and Fiona slips an arm around my waist."
    mb "You handled that really well."
    hide fiona
    show fiona cloak basic at right1
    show wllmc vest_hat surprised at left1plus
    mcfiona "You're not mad at me for breaking the Ward's rules?"
    show fiona cloak smirk
    "Fiona winks."
    mb "You're not part of the Ward. I have no authority over what you do or don't tell people."

    scene fiona_s1_mini6 at bg
    show cinema_fov at cinema_fov_in
    pause 1.0
    "I pinch her cheek, genuinely delighted."
    "(I knew we were on the same side really.)"
    show cinema_fov at cinema_fov_out

    scene bg_wll_town_streets_night_lights at bg
    show fiona cloak smirk at right1
    show wllmc vest_hat grin at left1plus
    with fade
    mcfiona "You and your loopholes."
    hide wllmc
    hide fiona
    show fiona cloak_cu surprised_purple_cu at fiona_cu
    mb "{i}A cathedral built over a thousand years burns to the ground in a day. A stuck gramophone skips and rewinds its song.{/i}"
    "A familiar light spills out of her eyes, and there's nothing I can do but wait for it to pass."
    hide fiona
    show wllmc vest_hat surprised at left1plus
    show enzo familiar smirk at right3
    enz "That's the trouble with mystics. Their powers come at the most inconvenient times."
    show wllmc vest_hat sad
    mcfiona "You're telling me."
    hide wllmc
    hide enzo
    show fiona cloak_cu smile_cu at fiona_cu
    "Fiona comes back to herself with a startling laugh, her whole face lit up with amusement."
    show fiona cloak_cu grin_cu
    mb "Well well well! That wasn't what I expected at all."
    hide fiona
    show wllmc vest_hat_cu smirk_cu at wllmc_cu
    mcfiona "I don't trust that sinister smile. What's going on?"
    hide wllmc
    show fiona cloak_cu smirk_cu at fiona_cu
    mb "I hope you're ready for an adventure, 'girlfriend'."
    hide fiona
    show wllmc vest_hat_cu surprised_cu at wllmc_cu
    "(What on earth did she see?)"
    hide wllmc

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

