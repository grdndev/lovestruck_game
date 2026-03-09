label van_season1_episode5:

    $tbc = False
    scene bg bowling_regular at bg
    play music hifleveryday
    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False
    show razi casual basic at centre
    ra "Well... I guess you can't really ask for better protection than a Helsing."
    show razi casual sad
    ra "But if you need help, don't hesitate to call us."
    hide razi
    show jd casual smirk at centre
    jd "Yeah, we'll come flying in and kick some ass."
    hide jd
    show hiflmc bowling basic at centre
    mcvan "I promise I'll call if things get out of control."
    hide hiflmc
    show vanessa huntress hatbasic at centre
    va "Which they won't."
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    mcvan "(How can she sound so confident?)"
    mcvan "(Isn't she freaked out at all?)"
    scene bg road_night at bg
    stop music fadeout 1.0
    play music hiflsad
    show van_back_night at bg
    show van_middle_night at bg
    show van_front_night at bg
    show hiflmc bowling basic at left4 behind van_front_night:
        ypos 725
    show vanessa huntress hatbasic at right4 behind van_front_night:
        ypos 725
    "We leave out the back."
    show hiflmc bowling sad
    "I spend the entire ride fiddling with the radio, nervous energy buzzing through my system."
    scene bg heroine_home_lights at bg
    "As soon as we're inside with the door locked behind us, I can't take it anymore."
    show hiflmc bowling surprised at centre
    mcvan "How can you not be worried?"
    mcvan "Two vampires have attacked me two days in a row."
    show hiflmc bowling surprised at right4
    show vanessa huntress basic at left4
    va "What would be the point? I know we'll beat them."
    show hiflmc bowling angry
    mcvan "But you can't know that!"
    mcvan "And all I can do is stand there and wait to be rescued or kidnapped, like some kind of silly damsel in distress."
    show vanessa huntress sad
    va "Well, first of all, no one thinks you're a damsel in distress."
    va "It's not like you're trained for this."
    va "There's no shame in needing a professional to protect you."
    show hiflmc bowling sarcastic
    mcvan "Easy for you to say! I'm the one losing control over my own life."
    show hiflmc bowling sad
    mcvan "I feel like... like the entire world is imploding around me and I can't do anything about it."
    hide vanessa
    show hiflmc bowling sad at centre
    "I sink onto the couch."
    show hiflmc bowling sad at right2
    show vanessa huntress basic at left2
    "Vanessa joins me a moment later."
    mcvan "I just... don't know what to do."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    mcvan "(Why can't I keep it together?)"
    show hiflmc bowling_cu sad_cu
    mcvan "(I haven't broken down like this in years.)"
    hide hiflmc
    show hiflmc bowling sad at right2
    show vanessa huntress basic at left2
    "She reaches out and pats my shoulder awkwardly."
    va "If it makes you feel better, you're actually handling this all a lot better than others I've protected."
    show vanessa huntress smirk
    va "One time, I was guarding this guy from some demons who were trying to steal a magical heirloom of his."
    va "He had like three breakdowns on the first day alone."
    show vanessa huntress sad
    va "And those demons were way less dangerous... than..."
    "Her eyes go wide and she blushes as she realizes what she just implied."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(Oh god, she's so bad at this, it's actually kind of cute.)"
    show hiflmc bowling sad at right2
    show vanessa huntress blush at left2
    va "Not that you're really in danger, or that this is too dangerous for me to handle."
    va "Seriously, I'm extremely equipped to protect you, you don't have to worry."
    stop music fadeout 1.0
    play music hiflliteromance
    show hiflmc bowling happy
    "Despite my earlier freak out, I can't help but laugh at her scrambling to reassure me."
    show vanessa huntress sad
    "She looks put-out at my laughter, nearly pouting."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Scratch that, she's seriously cute.)"
    show hiflmc bowling_cu happy_cu
    "(How is it that just being around her can make me feel so much better?)"
    hide hiflmc
    $menuhideborder = True
    menu vane5c1:
        "A. Reassure her.":
            $menuhideborder = False
            show hiflmc bowling happy at right2
            show vanessa huntress sad at left2
            mcvan "Don't worry about it, Vanessa, I know what you meant."
            show vanessa huntress happy
            "She cracks a grin and pretends to wipe sweat from her brow."
            va "That's a relief."
        "B. Tease her playfully.":
            $menuhideborder = False
            show hiflmc bowling happy at right2
            show vanessa huntress sad at left2
            mcvan "Clearly, you have the whole 'vampire fighting' thing in the bag."
            mcvan "But you might need remedial lessons on 'comforting scared civilians'..."
            show vanessa huntress smirk
            va "Well if that's the way you feel, maybe I should just leave you to fight the vampires on your own."
            "But at least she's laughing instead of pouting, now."
            hide vanessa
            show hiflmc bowling_cu happy_cu at hiflmc_cu
            "(Score one for [genericfn].)"
            hide hiflmc
        "C. Compliment her.":
            $menuhideborder = False
            show hiflmc bowling basic at right2
            show vanessa huntress sad at left2
            "I bump her shoulder with mine."
            show hiflmc bowling happy
            mcvan "Aw, come on, I know you're equipped to protect me."
            mcvan "Don't think I didn't see those badass moves with the whip."
            show vanessa huntress surprised
            va "What, that? That's nothing -- I can do way better than that."
            show vanessa huntress smirk
    show vanessa huntress basic at left2
    show hiflmc bowling basic at right2
    mcvan "Also..."
    mcvan "I know I haven't said it yet, but..."
    show hiflmc bowling happy
    mcvan "Thanks for protecting me earlier."
    mcvan "I don't know what would've happened if you hadn't been there."
    show vanessa huntress blush
    "Her face breaks into a radiant grin, a blush spreading across her cheeks as she ducks her head."
    show hiflmc bowling blush
    "I feel my heart stutter for a moment."
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(How can one woman be so unfairly gorgeous?)"
    hide hiflmc
    show hiflmc bowling basic at right2
    show vanessa huntress smirk at left2
    va "It's not a big deal, really. I'm just doing my job."
    show hiflmc bowling happy
    mcvan "Well, it's a big deal to me, so thank you."
    "After talking with Vanessa, I feel like I can breathe again, like the walls of my life aren't crumbling around me anymore."
    show vanessa huntress basic
    va "So what, exactly, did Li say to you earlier?"
    stop music fadeout 1.0
    play music hifleveryday
    show hiflmc bowling basic
    "With her by my side, I'm able to recount what Li said without panicking again."
    show vanessa huntress angry
    va "Hmm."
    show vanessa huntress basic
    va "Do you have any idea what Li meant by 'born to be his bride?'"
    show hiflmc bowling sad
    mcvan "Not that I can think of."
    show vanessa huntress sad
    mcvan "She mentioned this being in your blood. Is it possible there's a clue in your family history?"
    show hiflmc bowling basic
    "I shake my head."
    show hiflmc bowling sarcastic
    mcvan "I wasn't lying when I said my family is exceedingly, boringly normal."
    show vanessa huntress basic
    va "Even if your family is 'normal,' it's definitely possible they'd had some interaction with the supernatural before."
    va "Supernatural creatures really aren't as rare as most people believe."
    show hiflmc bowling basic
    mcvan "Well, old family records would be in my parents' office."
    show hiflmc bowling sad
    mcvan "If you really think it's worth investigating..."
    show vanessa huntress smirk
    va "I do."
    show vanessa huntress sad
    va "Do you mind if I change into something more comfortable first, though?"
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Oh, duh.)"
    show hiflmc bowling_cu sarcastic_cu
    "(There's no way an outfit that intimidating is in any way comfortable to wear.)"
    hide hiflmc
    show hiflmc bowling happy at right2
    show vanessa huntress basic at left2
    mcvan "Yeah, go ahead."
    scene bg parents_room_night_lights at bg with clockwise_wipe
    "Once she’s changed into her everyday wear, I lead Vanessa back to my parents’ study."
    "There’s dust everywhere, but otherwise, it’s the same as ever."
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Of course it is. It’s not like Grace or I ever come in here...)"
    show hiflmc bowling_cu sarcastic_cu
    "(Who has time to sit and grieve for my dead parents when repression and avoidance work so much better?)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    "I start searching through the filing cabinet, while Vanessa peruses the bookcase."
    hide vanessa
    show hiflmc bowling basic at centre
    "I’m elbow-deep in old graded papers when Vanessa calls my name."
    hide hiflmc
    show vanessa casual basic at centre
    va "I found something."
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    mcvan "What? What is it?"
    va "It’s a keypad, probably for a vault."
    va "Do you have any idea what the combination could be?"
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(A vault? I know I haven’t been in here since they died, but still...)"
    "(What would they have needed a vault for?)"
    show hiflmc bowling_cu sarcastic_cu
    "(All the expensive valuables we don’t have?)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    mcvan "I have no idea. Let me try..."
    show hiflmc bowling sad
    "I put in a few different combinations –my parents’ birthdays, their wedding day– but no luck."
    show hiflmc bowling basic
    "My eye catches on an old picture of me and Grace that’s gathering dust on the bookcase."
    show hiflmc bowling surprised
    mcvan "They wouldn’t..."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(But I have to try.)"
    hide hiflmc
    show hiflmc bowling surprised at right4
    show vanessa casual basic at left4
    "I put in my own birthday, and I hear a click."
    show hiflmc bowling surprised at right1
    show vanessa casual angry at left1
    "Vanessa pushes me behind her immediately, shielding me like she thinks a bomb’s about to go off."
    scene bg parents_room_secret_night_lights at bg with dissolve
    stop music fadeout 1.0
    play music vanessa
    "Instead, the bookcase itself moves to the side, revealing a hidden room."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Okay, what?)"
    "(How did my parents manage to keep an entire secret room hidden from us?)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "The room is filled with weapons –some I recognise, most I don’t."

    mcvan "What is this place?"
    hide hiflmc
    show vanessa casual basic at centre
    "Vanessa is already further inside, picking up and testing out the various weapons and gadgets."
    show vanessa casual surprised
    va "It’s awesome is what it is. I haven’t seen one of these models in years."
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Is that a gun?)"
    show hiflmc bowling_cu sarcastic_cu
    "(You know what? No. I don’t want to know.)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual smirk at left4
    va "If your ‘boringly normal’ parents had all of this, maybe my family isn’t as strange as I thought."
    show hiflmc bowling surprised
    mcvan "No, this is definitely all weird. I guess my family just wasn’t as normal as I thought."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(The real question is: why the hell did my parents have an entire armory hidden inside our house?)"
    hide hiflmc
    show vanessa casual happy at centre
    "Vanessa snaps me out of my thoughts with an eager grin, holding up a long, slightly curved sword."

    va "This is so cool. I haven’t gotten to use some of these since I was still in training."
    show vanessa casual blush
    va "They’re not all always the most... practical, in real-life situations."
    show vanessa casual smirk
    va "But they’re so badass."
    va "Do you want a demo?"
    hide vanessa
    $menuhideborder = True
    menu vans1e5c2:
        "A. Let Vanessa give you a hands-on demo."(paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(I still can’t believe that my parents have a whole secret room full of weapons.)"
            show hiflmc bowling_cu happy_cu
            "(But Vanessa’s excitement over all of this makes it almost worth it.)"
            "(She’s like a kid in a candy store.)"
            "(Except, a grown woman in an armory filled with deadly weapons.)"
            hide hiflmc
            show hiflmc bowling basic at right4
            show vanessa casual smirk at left4
            mcvan "I’d love that, actually. If you don’t mind."
            show vanessa casual happy
            va "Mind? Not at all. I never get to do this."
            show hiflmc bowling surprised
            mcvan "Soo... what’s the one you’re holding now?"
            show vanessa casual sad
            "She blinks, looking at the sword in her hand."
            va "Wait, really? I thought this was a pretty common one."
            show hiflmc bowling basic
            "I shrug."
            show hiflmc bowling sarcastic
            mcvan "This may surprise you, but I’ve never really needed to research weapons before."
            show vanessa casual smirk
            "She smiles patiently."
            va "Well, this one is called a Katana. It’s a standard-length Japanese sword."
            va "This one isn’t particularly decorative, but some of them can be really gorgeous."
            show vanessa casual basic
            va "It is surprisingly sharp, considering this stuff hasn’t been touched in years."
            "She swings it through the air, getting a feel for it, and then nods at me."
            show vanessa casual smirk
            va "Maybe go stand a little farther back, so I can really demonstrate for you."
            show hiflmc bowling surprised
            "I move back, intrigued."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(It’s almost strange how much more at ease she looks with a weapon in her hands.)"
            hide hiflmc
            show vanessa casual basic at centre
            "She bows to me."
            "The next thing I know, she starts moving around the room."
            "Her footword is so graceful, her movements so smooth and fluid, it almost seems like she’s dancing."
            "There’s a lot less sword-swinging than I expected, but when she does, the katana slices through the air in sharp, swift movements."
            show vanessa casual angry
            "She grunts softly with each strike, her arms flexing and tensing."
            "It’s mesmerizing."
            hide vanessa
            show hiflmc bowling_cu blush_cu at hiflmc_cu
            "(I couldn’t look away if I wanted to.)"
            hide hiflmc
            show vanessa casual basic at centre
            "She finished by sliding the sword back into the sheath in one gliding motion, then bows again."
            show vanessa casual smirk
            va "Well? What’d you think?"
            show hiflmc bowling surprised at right4
            show vanessa casual smirk at left4
            "I fight to unglue my tongue from the roof of my mouth."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu blush_cu at hiflmc_cu
            "(I think you’re the most unbearably attractive woman I’ve ever met.)"
            "(And you could probably stab me with that sword and I’d say thank you.)"
            hide hiflmc
            show hiflmc bowling blush at right4
            show vanessa casual smirk at left4
            mcvan "That sure was... something."
            hide hiflmc
            show vanessa casual happy at centre
            "She grins and puts the katana back on the weapons rack, then looks around for the next thing to demonstrate."
            show vanessa casual surprised
            va "Your parents had shuriken?"
            "She holds up a round, four-pointed... thing."
            hide vanessa
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(I have no idea what that is, but it looks really sharp.)"
            hide hiflmc
            show hiflmc bowling surprised at right4
            show vanessa casual surprised at left4
            mcvan "Uhh, maybe save demonstrating those for another time."
            show vanessa casual sad
            "She pouts but puts it back."
            va "Oh, alright. If we’re going to keep it simple..."
            show hiflmc bowling basic
            show vanessa casual smirk
            va "Ooh, okay, these will do nicely."
            show hiflmc bowling surprised
            "She holds up a pair of long wooden sticks."
            mcvan "Are those batons?"
            show hiflmc bowling basic
            mcvan "What, are you going to twirl them?"
            show vanessa casual happy
            "She laughs."
            va "Baton-twirling isn’t my specialty, I’m afraid."
            show vanessa casual smirk
            va "Besides – these aren’t batons."
            show vanessa casual basic
            va "They’re called escrima sticks. Mostly used in Filipino martial arts."
            show hiflmc bowling surprised
            mcvan "You studied Filipino martial arts?"
            show vanessa casual smirk
            "Vanessa smirks."
            show hiflmc bowling basic
            va "I’ve studied a dozen different martial arts, actually."
            show hiflmc bowling blush
            "I swallow against my suddenly dry throat."
            mcvan "...Oh."
            show vanessa casual basic
            va "Come over here, I’ll show you how to use them."
            show hiflmc bowling surprised
            mcvan "Really? Are you sure?"
            show hiflmc bowling basic
            va "Weren’t you the one saying you don’t know how to defend yourself?"
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(Well, she’s not wrong...)"
            hide hiflmc
            show hiflmc bowling basic at right2
            show vanessa casual basic at left2
            "I make my way over to her, and she hands the sticks to me."
            show hiflmc bowling surprised
            mcvan "So, what, do I just... swing them? Like a bat?"
            show vanessa casual smirk
            va "The useful thing about escrima sticks is that they’re light enough that you can move quickly..."
            va "But still solid enough to make the hits hurt."
            show hiflmc bowling basic
            va "Especially if you target a nerve cluster, or a vital spot."
            show hiflmc bowling sarcastic
            mcvan "Knowing me, I’ll probably wind up hitting myself in the face."
            show vanessa casual basic
            show hiflmc bowling basic
            "She shakes her head."
            va "Don’t worry. For now, we’ll focus on just the movements."
            va "They should be like extensions of your arms..."
            hide hiflmc
            hide vanessa
            show vanessa_s1_mini5 at bg with dissolve:
                zoom 0.4
            "She moves behind me and puts her arms around mine, guiding my hands."
            "(Oh god, too close!)"
            "She’s definitely saying something as she guides me through the motions, but I have no idea what."
            "All I can focus on is the feeling of her flush against my back, and her deceptively powerful arms guiding mine."
            "(I’m too bi for this.)"
            "(She’s really trying to kill me.)"
            hide vanessa_s1_mini5
            show hiflmc bowling blush at right4
            show vanessa casual basic at left4
            "I pull away, laughing nervously."
            mcvan "I, uh, think maybe we should leave the self-defense lesson for another time."
            mcvan "I think I’m just gonna go... look for more clues."

        "B. Turn her down.":
            $menuhideborder
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Watching Vanessa show off with the weapons is tempting, but the timing just doesn’t feel right.)"
            hide hiflmc
            show hiflmc bowling sad at right4
            show vanessa casual smirk at left4
            mcvan "Sorry, Vanessa. Maybe another time, when my world is a little less topsy-turvy."
            va "Oh, of course."
            show vanessa casual blush
            va "Sorry, I got a little caught up in the excitement of new toys."
            show hiflmc bowling basic
            mcvan "You can stay in here if you want– I’m going to go look through the study some more."
    scene bg parents_room_secret_night_lights at bg with fade
    show vanessa casual basic at centre
    "I’m absorbed in some old documents when Vanessa comes back in, carrying an armful of weapons."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(A taser, brass knuckles, grenades again, and... a very sharp-looking knife.)"
    show hiflmc bowling surprised at right4
    show vanessa casual basic at left4
    mcvan "Um. What?"
    show vanessa casual sad
    show hiflmc bowling basic
    va "You should keep these on you for protection."
    va "Besides, they’re all yours, anyway. It’d be a shame to let them keep gathering dust."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I don’t know how I feel about carrying weapons, though...)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual happy at left4
    "She must see through my hesitation, because she smiles at me reassuringly."
    va "You don’t have to use them, but you should keep them on you just in case."
    show hiflmc bowling sad
    mcvan "I’m just not sure how I feel about carrying around such a sharp knife."
    show vanessa casual basic
    va "It’s fine– it’ll go in a sheath, and it’ll just be there in case you need it. Not a big deal."
    show hiflmc bowling surprised
    mcvan "And the grenades? Are they filled with more holy water?"
    va "These? They’re just flashbangs."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vans1e5c3:
        "A. Ask about the grenades.":
            $menuhideborder = False
            show hiflmc bowling basic at right4
            show vanessa casual basic at left4
            mcvan "Why would I need flashbang grenades?"
            show vanessa casual sad
            "Vanessa looks at me like I’ve started speaking another language."
            va "Why wouldn’t you need flashbang grenades?"
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(I’m not even gonna touch that.)"

        "B. Thank her.":
            $menuhideborder = False
            show hiflmc bowling sad at right4
            show vanessa casual basic at left4
            mcvan "Well... thanks."
            show vanessa casual sad
            mcvan "I guess my parents would’ve wanted me to use this stuff."
            va "I’m sure your parents would want you to be safe."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(Get your act together, [genericfn], this is not the time to get emotional.)"
        "C. Joke about it.":
            $menuhideborder = False
            show hiflmc bowling happy at right4
            show vanessa casual basic at left4
            mcvan "Whoever said ‘diamonds are a girl’s best friend’ clearly hadn’t met you."
            mcvan "It’s obvious that weapons are really a girl’s best friend."
            va "Well, obviously. Weapons are so much more practical."
            hide hiflmc
            hide vanessa
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            "(Really?)"
            "(Not even a little laugh?)"
    hide hiflmc
    hide vanessa
    show hiflmc bowling basic at centre
    "I go back to looking through a binder of old family documents."
    "I flip a page and find an old piece of parchment under a protective sheet of plastic."
    show hiflmc bowling surprised
    "(This has to be hundreds of years old, at least!)"
    show hiflmc bowling basic
    "It’s hard to make out most of it, but it seems to be an old diary entry, from the perspective of a young woman."
    show hiflmc bowling sad
    "I look for any kind of signature, but if her script is hard to read, her signature is worse."
    "The first name is illegible, but I can just make out [genericln]."
    show hiflmc bowling surprised
    mcvan "Uh, Vanessa? I think I found something."
    show hiflmc bowling basic at right2
    show vanessa casual basic at left2
    "Vanessa’s at my side in an instant."
    va "What is it?"
    show hiflmc bowling surprised
    mcvan "An old diary entry. Hundreds of years old."
    mcvan"I think it was written by one of my ancestors."
    show hiflmc bowling basic
    "I show Vanessa the signature."
    show hiflmc bowling sad
    mcvan "She was... trying to run away from an arranged marriage, I think?"
    mcvan "She calls him ‘peculiar’, saying that he preferred to meet her ‘at the midnight hour’."
    mcvan "Which is weird, but not supernatural, necessarily."
    show hiflmc bowling basic
    mcvan "... Except that she also describes his eyes as a ‘cruel vermillion’."
    show vanessa casual angry
    va "Sounds like a vampire to me."
    va "Anything else? Does she mention a name, a location – anything useful?"
    show hiflmc bowling sad
    mcvan "Unfortunately, no."
    show vanessa casual basic
    mcvan "She does say that there were other oddities about him..."
    show hiflmc bowling basic
    mcvan "Like his strange fondness for bats, or that she occasionally lost track of him in the shadows."
    mcvan "But it seems like she was able to escape and start a new life far away."
    show vanessa casual sad
    va "Well, at least she got a happy ending. Though that’s less helpful for us."
    show vanessa casual basic
    mcvan "In the last few lines she says"
    mcvan "‘I pray this is the last I have seen of him, but I fear he shall find me again someday.’"
    show hiflmc bowling surprised
    mcvan "Any thoughts? Is it normal for vampires to try to marry humans?"
    show hiflmc bowling basic
    show vanessa casual sleep
    "Vanessa taps her finger against her chin in thought."
    show vanessa casual sad
    va "No, it’s really not."
    show vanessa casual basic
    va "I can only think of one vampire who was famous for taking brides..."
    va "But he’s dead."
    show hiflmc bowling surprised
    show vanessa casual surprised
    "I’m about to ask her who she’s talking about when we’re interrupted by a knock at the door."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Who would be knocking at this hour?)"
    scene bg heroine_home_lights at bg with wipedown
    show hiflmc bowling basic at right3
    show vanessa casual basic at left3
    "We quietly make our way to the front entrance."
    hide hiflmc
    hide vanessa
    show bg mc_house_ext_fog at bg with dissolve
    show li casual basic at centre
    stop music fadeout 1.0
    play music hiflsuspense
    "I pull back the curtain to see who’s outside, only to see Siniang Li waiting, still as a statue."
    hide li
    hide bc mc_house_ext_fog
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(How does she know where I live?)"
    hide hiflmc
    show bg mc_house_ext_fog at bg
    show li casual_cu vampirehappy_cu at li_cu
    "She turns in my direction, and our eyes lock."
    "For a moment I’m frozen by her chilling crimson stare."
    hide li
    show li casual vampirebasic at left1 behind grace
    show grace casual sad at right1
    "And then I notice Grace, held captive in Li’s arms."
    hide li
    hide grace
    hide bg mc_house_ext_fog
    show bg heroine_home_lights at bg
    show hiflmc bowling surprised at centre
    "The blood drains from my face."
    "(No! Not my sister!)"
    mcvan "Grace!"
    hide hiflmc
    show vanessa casual angry at centre
    "I throw the door open, ignoring Vanessa hissing my name warningly."
    hide vanessa
    show bg mc_house_ext_fog at bg
    show li casual vampirebasic at right3 behind grace
    show grace casual sad at right5
    show hiflmc bowling angry at left4
    mcvan "Let go of her!"

    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
