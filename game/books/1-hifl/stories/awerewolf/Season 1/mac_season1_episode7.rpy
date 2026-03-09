##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode7:
    $tbc = False

    ##Change these to suit the story
    scene bg hifl_sheriff at bg
    play music hiflsad

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(Home? I'm not going home after all this.)"

    hide hiflmc
    show hiflmc bowling angry at right4
    show mac tank basic at left4

    mcmac "What are you going to do that's different?"
    show mac tank surprised
    ma "Excuse me?"

    mcmac "What changes if I leave?"

    mcmac "You have one less set of eyes watching your back."

    mcmac "You lose the only other person that really knows what's happening right now."
    show hiflmc bowling sad
    mcmac "I know you've kept things from Razi and the others."

    mcmac "That's your business."
    show hiflmc bowling basic
    mcmac "But you've already told me."

    mcmac "I accept it, all of it."
    show mac tank angry
    ma "I told you more than I should."
    hide hiflmc
    hide mac
    show mac tank_cu angry_cu at mac_cu
    "I take a step forward, putting myself on the very edge of Mackenzie's personal space."

    "It only does so much when she's taller than me, but I'll take all the advantage I can get."
    hide mac
    show hiflmc bowling_cu basic_cu at hiflmc_cu
    mcmac "Tell me you regret it."

    mcmac "Say that to my face and I'll go."
    hide hiflmc
    show mac tank_cu angry_cu at mac_cu
    "Mackenzie opens her mouth, only for it to snap shut a second later."
    show mac tank_cu sleep_cu
    "She stares me down for a long moment before sighing, reaching up to rub the tension from her temples."
    show mac tank_cu sad_cu
    ma "You're playing with loaded dice there, [genericfn]."
    $menuhideborder = True
    hide mac

    menu mace7c1:
        "A. But am I wrong?":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            mcmac "But am I wrong?"
            hide hiflmc
            show mac tank_cu angry_cu at mac_cu
            ma "I didn't say that."
            show mac tank_cu sad_cu
            ma "Wrong or right, this isn't a fight I can afford to lose."
        "B. Only because I have to.":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            mcmac "Only because I have to."
            show hiflmc bowling_cu happy_cu
            mcmac "You're a tough nut to crack."
            hide hiflmc
            show mac tank_cu sad_cu at mac_cu
            ma "Not as tough as I'd like to think, some days."

        "C. I'm worried about you.":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at hiflmc_cu
            mcmac "I'm worried about you."
            hide hiflmc
            show mac tank_cu sad_cu at mac_cu
            ma "Between the two of us, I'm the one who should be worried."

    hide mac
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    mcmac "And if Damien shows up..."
    hide hiflmc
    show mackenzie_s1_mini11 at bg
    "Mackenzie's eyes light up at that, tension coiling through her stance."
    hide mackenzie_s1_mini11
    show mac tank_cu angry_cu at mac_cu
    ma "I'm not letting him near you."
    hide mac
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    mcmac "I know."
    show hiflmc bowling_cu sad_cu
    mcmac "But I don't want him near you either."
    show hiflmc bowling_cu angry_cu
    mcmac "The fact that he'd attack this place in broad daylight-!"
    hide hiflmc
    show mac tank_cu angry_cu at mac_cu
    ma "Means he's either fearless or lost his head."
    show mac tank_cu basic_cu
    ma "Right now, I honestly couldn't tell you which."
    hide mac
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    mcmac "Let me help you take care of the damage."

    mcmac "I'll be like your pack. I mean it."
    hide hiflmc
    show mac tank_cu sad_cu at mac_cu
    "She lets out a soft sigh, rubbing the back of her neck."
    stop music fadeout 1.0
    play music hifleveryday

    show mac tank_cu smirk_cu at mac_cu
    ma "You know that still means I'm in charge, right?"
    hide mac
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    mcmac "Do you hear me complaining?"
    hide hiflmc
    show mac tank_cu smirk_cu at mac_cu
    ma "No. I see you smiling because you won the argument."
    hide mac
    show hiflmc bowling blush at right3
    show mac tank happy at left3
    "Being called out makes me blush, but then Mackenzie smiles too, and I don't mind in the least."
    hide hiflmc
    hide mac
    show mac tank_cu happy_cu at mac_cu
    ma "Let's clean the rest of this place up."

    ma "Maybe Damien got sloppy and left something useful behind."
    hide mac
    show hiflmc bowling basic at right4
    show mac tank basic at left4
    "There's so much glass to pick up, dozens of files tosses haphazardly around the floor."

    "But Mackenzie and I carefully work through the mess."
    hide hiflmc
    show mac tank basic at centre

    "We've almost finished when she crouches down and picks up a crumpled note."
    hide mac
    show mackenzie_s1_mini6 at bg
    "A circle is drawn in the center in pen, but underneath the handwriting is three messy words."
    hide mackenzie_s1_mini6
    show hiflmc bowling surprised at right4
    show mac tank basic at left4
    mcmac "At the eclipse?"

    mcmac "What does that mean?"
    show mac tank angry
    ma "I don't have a clue, but..."

    "She brings the paper up to her face and breathes in."

    ma "It was definitely in Damien's hands at some point."

    ma "Maybe after we throw him in one of these cells, I'll ask him about it."
    show hiflmc bowling basic
    mcmac "Where are you going to put it?"
    show hiflmc bowling sarcastic
    mcmac "He stole the case file, right?"

    ma "Unfortunately. I'll just have to keep the evidence locked up in my car for now."
    show mac tank sad
    ma "Not like this sort of case is going to court anyway."
    hide mac
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(No, she has to play both judge and jury.)"

    "(I just hope Damien isn't the executioner.)"
    hide hiflmc
    show mac tank sad at left4
    show hiflmc bowling basic at right4
    mcmac "True. Let me just put the drawers back in and we'll be done."
    hide mac
    show hiflmc bowling basic at centre
    "My phone buzzes when Mackenzie steps away to put the broom back, and when I check my phjone, there's a text from Luce."

    lu "I've got Grace's pay for the week. You want to pick it up?"
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Shit, I probably should. The phone bill's due.)"

    "(Knowing those vultures, they wouldn't give me a delay just because my sister's missing.)"
    hide hiflmc
    show hiflmc bowling basic at centre
    $sidecharone = "Text"
    sid1 "Yeah, Luce. I'll be right there."

    scene bg diner_lights_on at bg
    pause

    show hiflmc casual basic at centre
    "Mackenzie has to finish sealing off the office to make sure no one else can break in."

    "I give her a head’s up before heading over to the bowling alley for a change of clothes, then to the diner."
    show hiflmc casual sad
    "It doesn’t feel right stepping inside and not seeing Grace at the counter."
    show hiflmc casual sad at left5
    show luce casual basic at right5
    lu "Evening, [genericfn]."

    lu "I take it by your look that Grace is still in the wind, yeah?"
    hide hiflmc
    hide luce
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(No, Luce, some asshole werewolf took her and the only person I can talk about that with is the sheriff we all know and love.)"
    hide hiflmc
    show hiflmc casual sad at left4
    show luce casual basic at right4
    mcmac "I'm still looking for her."

    lu "Sorry to say I haven't heard anything."

    lu "Check's for three days with tips. Let me know if she turns up."

    "I pocket the check, hating that I need the money so much."

    "It should be Grace's to spend, not mine."

    mcmac "I will."
    show hiflmc casual happy
    mcmac "Any chance I can get a cup of coffee to go?"

    lu "Sure, girl. On the house."
    hide luce
    show hiflmc casual surprised at centre
    stop music fadeout 1.0
    play music hiflsuspense
    "I’ve just sat down at the counter when the door swings open, hard enough for it to slam against the inside of the window."
    show hiflmc casual surprised at left4
    show annabelle casual basic at right4
    "Everyone jumps and I turn, locking eyes with the werewolf that Mackenzie tossed into the lake."
    hide hiflmc
    hide annabelle
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Are you fucking kidding me right now?)"

    $sidecharone = "Werewolf"
    hide hiflmc
    show annabelle casual basic at centre
    sid1 "Evenin', everyone."

    sid1 "Hands in the air before things get messy."
    show annabelle casual basic at right4
    show luce casual basic at left4
    "She flashes a gun under her shirt and I see Luce freeze, caught halfway between the register and the coffee machine."
    hide annabelle
    show luce casual basic at centre
    "I’ve glimpsed a shotgun under the counter before, but I don’t think she’s close enough to reach it."

    $sidechartwo = "Customer"
    hide luce
    show mailman casual basic at left4
    show annabelle casual basic at right4
    sid2 "Who the hell are you?"
    hide mailman
    show annabelle casual angry at centre
    sid1 "The one who can nail you between the eyes at a hundred yards."

    sid1 "Here and this close?"

    sid1 "You'll be kissing heaven in two seconds flat."
    show annabelle casual angry at right4
    show hiflmc casual surprised at left4
    "He shuts up after that and I stay still as I can, hoping she doesn’t recognise me."
    hide hiflmc
    show luce casual basic at left4
    show annabelle casual basic
    "Taking the gun out, the werewolf Lay’s it right against the counter, the barrel pointing towards Luce."

    sid1 "Everything in the drawer, please."
    hide annabelle
    hide luce
    show hiflmc casual surprised at right4
    show mac glassescop basic at left4
    "I see a figure approaching the front door and bite my tongue until I realise it’s Mackenzie."
    show mac glassescop angry
    "She stops just outside it, fingers right on the handle, and frowns when our eyes meet."
    hide mac
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(I probably look terrified.)"
    $menuhideborder = True
    hide hiflmc
    menu mace7c2:
        "A. Gesture for her to come in.":
            $menuhideborder = False
            show mac glassescop angry at left4
            show hiflmc casual angry  at right4
            "Using the hand I know the werewolf can't see, I imitate a gun, tilting my head to the right."

            "Then I gesture for Mackenzie to come inside, wanting this nightmare to end as soon as possible."

        "B. Mouth something.":
            $menuhideborder = False
            show mac glassescop angry at left4
            show hiflmc casual sad at right4
            mcmac "She's got a gun."
            show mac glassescop surprised
            "I see Mackenzie mouth a 'what' before her eyes snap wide."
            show mac glassescop basic
            "A cool look falls across her face, and she gives me a determined nod before stepping forward."

        "C. Stay frozen":
            $menuhideborder = False
            show mac glassescop angry at left4
            show hiflmc casual sad at right4
            "(I can't ruin her chance to pull off a surprise.)"

            "Swallowing hard, my eyes flick in the werewolf's direction, hoping it gives Mackenzie at least a little bit to go on."
    hide mac
    hide hiflmc
    show luce casual basic at left4
    show annabelle casual basic at right4
    sid1 "I sure hope that's everything."

    sid1 "I'd hate to have to come back and take out the internet."
    stop music fadeout 1.0
    play music hiflaction
    hide luce
    show annabelle casual angry at centre
    "The door swings open and she whirls around, pistol leveled right at chest-height."
    show annabelle casual angry at right4
    show mac glassescop basic at left4
    "But Mackenzie is there with her own weapon, the barrel level."
    show annabelle casual basic
    "I see the werewolf's finger twitch near the trigger, but she holds back."

    sid1 "Lovely night we're having, Sheriff."

    ma "I'm counting down from five."

    ma "Put the weapon on the floor or I open fire."
    show annabelle casual surprised
    sid1 "Yeah, right. Like you carry silver on—!"

    ma "Four. Three."

    "There’s a split second of hesitation, but right before I think Mackenzie is going to pull the trigger..."
    show mac glassescop angry at right1 behind annabelle
    "She lunges forward and rips the pistol out of the werewolf’s hand."

    "She yelps in pain, and the weapon clatters on tile before Mackenzie pins her to the counter, one arm wedged sharply back."

    ma "I don't need it."
    show hiflmc casual surprised at left5
    ma "[genericfn], take a few steps back."

    "I do, edging back out of my seat, and Mackenzie flips the safety back on her pistol."

    "She holsters it without her eyes leaving the other werewolf."

    "Metal clicks as she wrenches a pair of handcuffs into place around her wrists, and I hear sighs of relief from around the diner."

    ma "You're under arrest."
    show mac glassescop angry at right2 behind annabelle
    "Mackenzie leans forward, and I hear her hiss right in the werewolf's ear."

    ma "Try and bust out of these and you won't enjoy the consequences."
    show mac glassescop basic at right1 behind annabelle
    show annabelle casual basic
    "Then Mackenzie straightens up, keeping a firm hold on her prisoner before tapping the radio on her shoulder."

    ma "Hey, deputy. I've got a pickup for you."
    hide mac
    hide annabelle
    hide hiflmc
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "(Jesus. I’m glad she was here.)"
    scene bg diner_lights_on at bg
    stop music fadeout 1.0
    play music hifleveryday
    pause
    show annabelle casual basic at right2
    show elmer casual basic at left2 behind annabelle
    "I’m surprised the deputy is so eager to be back on the case after his scare."

    "But Mackenzie lets him lock the werewolf up, although a set of shackles gets added to her outfit."
    hide elmer
    hide annabelle
    show hiflmc casual sad at centre
    "Once she’s gone, I can breathe easy again."
    show hiflmc casual sad at left4
    show mac glassescop basic at right4
    mcmac "What the hell is going on here?"

    ma "Hopefully we'll find out. Deputy's going to run her ID."
    show mac glassescop sad
    ma "This might seem like a bad time for it, but are you hungry?"
    show mac glassescop smirk
    ma "I actually came over to eat."
    show hiflmc casual happy
    mcmac "I'm starving. Let's do it."
    hide hiflmc
    show luce casual basic at left4
    "Luce makes us a huge to-go bag of the house special, but not after giving Mackenzie a tight handshake and her thanks."
    scene bg main_day at bg
    pause
    show hiflmc casual happy at left4
    show mac glassescop happy at right4
    "Mackenzie’s smiling as we walk out to my truck, and now that the adrenaline’s gone, I can smile too."

    mcmac "Where do you want to go?"

    ma "Somewhere out of the way."

    mcmac "I've got an idea."
    scene bg road_day at bg
    pause


    "There’s a nice stretch of land on the outside of town, and I park by the side of the road so we can get out and sit."
    show mac cop happy at left2
    show hiflmc casual happy at right2
    "Mackenzie opens up our bag and passes out the sandwiches, making my stomach growl as they’re unwrapped."

    ma "Luce's food is too good, huh?"

    mcmac "Tell me about it. It's one of the only things I'd miss about this place."
    show hiflmc casual surprised
    show mac cop sad
    "The second the words leave my mouth, I bite my tongue, wondering how to walk that back."

    ma "You always wanted to get out of here, didn't you?"
    show hiflmc casual sad
    mcmac "Yeah."

    mcmac "I don't know, I did. But it's such a double-edged sword."
    show hiflmc casual sarcastic
    mcmac "Either I move to a place where no one knows me..."

    ma "Or stay in the place where everyone knows you."
    stop music fadeout 1.0
    play music hiflliteromance
    scene mac3 at bg with fade:
        zoom 0.5
        yanchor 0.1
        linear 8 yanchor 0.4



    "I nod, my shoulder bumping against Mackenzie's as I take another bite of my sandwich."

    "She leans into the contact a little, but her eyes are on the falling sun, watching it sink into the horizon."

    "(In moments like this, leaving seems like the last thing I want to do.)"

    "(But can I keep this feeling? What happens after Mackenzie takes out Damien?)"

    "(I'm only human, but maybe we could...)"

    ma "Now you're frowning at me."

    mcmac "Sorry! I was just thinking too hard."

    mcmac "A lot's happened today, especially with you playing superhero in the diner."

    ma "I was just doing my job."
    $menuhideborder = True

    menu mace7c3:

        "A. Tease her.":
            $menuhideborder = False

            mcmac "Oh, come on. You looked cool as hell taking her gun."

            mcmac "I know you saw the look on her face."

            ma "I wasn't going for style points. But I'm glad you liked it."

        "B. Take things seriously.":
            $menuhideborder = False

            mcmac "I know you were, but your job is important."
            mcmac "Whether it's on the werewolf side of things or not."

            ma"They seem to be crossing over more than I'm comfortable with these past few days."

        "C. Pile on the compliments.":
            $menuhideborder = False

            mcmac "No, no, no. You don't get to be modest after that."

            mcmac "You were amazing, Mackenzie."

            mcmac "Everyone in the diner saw that."

            ma "I...mm. Thank you."
    "I bump my shoulder against Mackenzie’s and she bumps right back, making me laugh when I nearly topple over."

    mcmac "Hey, I'm outclassed here!"

    ma "Don't start a fight you can't finish, [genericfn]."
    scene bg road_night at bg
    show hiflmc casual happy at right2
    show mac cop happy at left2

    "We settle side by side again when the sun sinks below the horizon, and I can feel Mackenzie’s warmth through my shirt."

    "It’s comforting but intense, although as far as I can tell, it comes naturally."
    hide hiflmc
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    "(Maybe running hot is a werewolf thing?)"
    show hiflmc casual_cu blush_cu
    "(Temperature-wise, I mean. Not that she’s not also hot.)"
    show hiflmc casual_cu sarcastic_cu
    "(Oh god, I’m ending this conversation with myself right now.)"
    hide hiflmc
    show mac cop sad at left2
    show hiflmc casual basic at right2
    ma "I'm sorry for what happened earlier."
    show hiflmc casual surprised
    mcmac "Huh?"

    ma "At the police station."

    ma "I kept trying to push you away when I should know better."
    show hiflmc casual sad
    mcmac "You're used to being the only person you can rely on, aren't you?"

    ma "Yeah, but that's not a good excuse when someone's genuinely offering help."
    show hiflmc casual happy
    mcmac "I get it, though."

    mcmac "Everyone thought the old sheriff was going to work until she croaked, but then she left you in charge."

    mcmac "And you're what, twenty-seven?"
    show mac cop smirk
    "Mackenzie raises a brow, but the wicked edge to her smile makes my heart jump."

    ma "Been keeping track of how old I am?"
    show hiflmc casual blush
    mcmac "Um."

    mcmac "There is no right way to answer that and you know it."

    ma "Got me there."
    show hiflmc casual happy
    mcmac "Good, because you're stuck with me."

    mcmac "Pack for life, sheriff."
    show mac cop happy
    "She laughs, and shakes her head, but we finish our meal in companionable silence together..."

    "Staying close and watching the stars."
    hide mac
    hide hiflmc
    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
