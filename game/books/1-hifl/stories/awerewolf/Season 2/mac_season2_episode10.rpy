label mac_season2_episode10:

    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "Gwen throws her head back and lets out an ear-piercing shriek."

    "It's loud enough to leave me dizzy, and even Mackenzie winces, but refuses to let go of Gwen's cuffed arms."

    "When the sound dies away, I feel shaky, and she couldn't be more smug if she tried."

    ma "You done?"

    gwe "Uh-huh. Take me away, officer."

    mcmac "What was that for?"

    gwe "You'll find out."

    "Clearly tired of Gwen's smart mouth, Mackenzie yanks her away from the car and right into the sheriff's office."

    "Elmer looks up when we come in, his jaw dropping at the sight of Gwen."

    elm "Uh, sheriff? What's going on?"

    ma "Don't worry about it, Elmer. Keep working."

    "Discomfort rolls off Elmer in waves, but he nods, and Mackenzie keeps walking Gwen back until we're in the interrogation room."

    "I close the door behind us, and Gwen is put in the chair there, her cuffs locked to the table."

    gwe "Cozy."

    ma "I imagine this isn't the first time you've been a room like this."

    gwe "Usually as a 'witness'."

    "She flutters her eyelashes before laughing."

    gwe "Everyone knows about that terrible murder, but I can't imagine who would ever do such a thing to poor, sweet So-and-So."

    "(Christ.)"

    mcmac "I don't care if it's rude anymore. What the hell are you?"

    gwe "I'm rare. That's all you get to know."

    "Mackenzie leans against the table, towering over Gwen."

    "Her eyes burn bright gold, and the next words are punctuated with primal force."

    ma "Answer her question."

    "I remember Annabelle shrinking into herself when Mackenzie did this before, but Gwen only smiles back."

    gwe "You can only yank other wolves' chains, but not mine. Nice try."

    "The change bleeds away again, but Mackenzie's glare is just as sharp."

    ma "Who's paying you to do this?"

    gwe "Someone who should have given me more money for this much trouble."

    gwe "One werewolf is no big deal, but a djinn and a vampire? Not to mention whatever JD is."

    mcmac "You don't know?"

    gwe "I have a couple guesses."

    gwe "But between demons, devils, and cryptids, I'd rather not make a mistake."

    ma "You've already made plenty of mistakes."

    ma "Twice now you've tried to kill me, and no dice."

    "Gwen shrugs, clearly unbothered."

    gwe "Third time's the charm?"

    gwe "The first try was a wash, anyway. Your girl here woke up when she shouldn't have."

    "(And I'm so glad I did.)"

    $menuhideborder = True
    menu macs2e10c1:
        "A. What will make you stop?":
            $menuhideborder = False
            mcmac "What will make you stop coming after Mac?"

            gwe "Please, if it was that easy, no one would hire me."

            gwe "The deal was struck, human. No take backs."

        "B. You can't win here.":
            $menuhideborder = False

            mcmac "Gwen, you can't win here. We know what you look like."

            mcmac "And everything you plan to do."

            gwe "Honestly, it's even better when I kill someone who knows what's coming."


        "C. How about a trade?":
            $menuhideborder = False
            mcmac "How about a trade?"

            mcmac "Drop the killing and tell us who paid you, then you can go."

            gwe "Hah! Not a chance in hell."

    "(I can think of a few people that might have hired her, but how do we prove it?)"

    mcmac "Does the name Grace mean anything to you?"

    "Despite the question coming out of nowhere, Gwen doesn't even try to hide her response. She shakes her head."

    gwe "Oh, wait. Is that your sister?"

    gwe "Razi mentioned something about her going missing. But uh, that wasn't me."

    gwe "I'm new here. And kidnappings are way too complicated."

    mcmac "Yeah, the Rider pack found that out pretty fast."

    "Gwen raises an eyebrow, frowning at me."

    gwe "You sure your family's human?"

    gwe "Most mortals don't slip a werewolf's leash when they're wanted."

    mcmac "What's that supposed to mean?"

    gwe "Just that your sister better be careful with the company she keeps."

    gwe "Chances are, wherever she's gone, whoever lives in the darkness won't be half as kind as your pet sheriff here."

    "(Yeah, I've already figured that part out.)"

    "Another round of interrogation turns up nothing."

    "Gwen seems content to run Mackenzie and I in circles, dropping a dozen contradictory hints and shrugging off half the questions."

    "Eventually, we have to give up. Mackenzie leaves Gwen locked up while we head back into the office."

    mcmac "Is there anything else we can do?"

    ma "I don't think so."

    ma "It's not like I'm going to torture her. She knows I can't keep her locked up forever."

    elm "Why would you?"

    "The deputy pipes up from his desk, giving the door to the interrogation room an odd look."

    elm "What did Gwen even do?"

    ma "Deputy, she robbed the diner that she works at."

    ma "In fact, you should go in there and take all the money in her pockets as evidence."

    elm "That just doesn't sound like her."

    "Mackenzie frowns, suddenly none too impressed."

    ma "Elmer, did I ask for your opinion on the suspect? Or did I tell you to take care of evidence?"

    elm "...The second one."

    ma "Then hop to it. I need to go talk to Luce."

    "Mackenzie puts a hand on my arm, and I take the signal to follow her out of the office."

    "When we walk back into the diner, Luce is chatting with the mailman."

    ma "Hey Luce, you got a second?"

    lu "I hope you've got a second, Sheriff."

    lu "Because I'd like to know why you dragged my waitress off in cuffs."

    mcmac "I caught her taking cash out of the register, that's why."

    "Luce frowns deeply at me, and the mailman does too."

    "(Wait, what did I do?)"

    lu "You sure about that, [genericfn]?"

    ma "Her pockets were stuffed with money, Luce. Check the drawer."

    lu "I did."

    lu "It's something I would have rather talked to her about, not given the third degree."

    mail "Everyone knows Gwen is a good kid."

    mcmac "You're joking."

    "The two of them stare at me in unison, and a cold chill slowly creeps up my back."

    "(Okay, something's wrong here.)"

    $menuhideborder = True
    menu macs2e10c2:
        "A. You feeling okay?":
            $menuhideborder = False

            mcmac "Are you both feeling okay?"

            lu "I’m angry is what I am."

            mail "And I think she’s got a good reason to be."

        "B. 'Good' doesn't make up for this.":
            $menuhideborder = False
            mcmac "Uh, 'good' doesn't make up for someone robbing you, last I checked."

            lu "Lord, girl, you're making it sound like she held me up at gunpoint."

            "(No, she shoved you in a closet.)"

            "(You just thought it was an accident.)"

        "C. Gwen's a thief.":
            $menuhideborder = False

    "Mackenzie steps between us, raw confusion on her face."

    ma "Are you telling me to overlook Gwen cleaning you out?"

    lu "She's a kid, Sheriff."

    lu "You jumped the gun."

    ma "I damn well did not."

    "For a second Mackenzie and Luce have a stand-off, but Luce breaks away from it first, not bothering to hide her distaste."

    lu "I know what your job is, but I think you've been listening to [genericfn] a bit too much."

    lu "She's always telling stories."

    "(More like calling you out on your bullshit, lady.)"

    ma "This has nothing to do with her."

    lu "Ever since Grace ran off-!"

    "My entire body tenses, but Mackenzie snaps to defend me."

    ma "Gwen committed a crime, and Grace is still a missing person on my books."

    ma "That makes them both my responsibility, and it's my call who I arrest."

    lu "When you use your good judgment."

    ma "Excuse me?"

    ma "You sure don't mind me exercising my judgment on every trucker who's had one too many and tries to skip out on a bill."

    ma "But running out with a whole register is an honest mistake?"

    "Mackenzie sounds more shocked than mad, and I can't really blame her."

    "The whole town has always trusted the sheriff—that's the way things work."

    lu "I meant what I said."

    lu "Let Gwen go, Sheriff."

    "(Hell no! We just caught Gwen after she tried to kill Mac twice.)"

    ma "That's not happening, Luce."

    ma "She stays put until I finish investigating her connection to other crimes."

    lu "I'm not at liberty to say."

    lu "How much is Gwen's bail, then? I'll pay it."

    mcmac "With what money? She just ripped you off."

    ma "I haven't brought her in front of a judge yet. There's no bail."

    lu "Then there's no real charges, are there?"

    "Luce barrels past Mackenzie out of the diner and towards the sheriff's office."

    "I'm shocked for a moment, then run to catch up."

    "Except when Mackenzie and I step out onto Main Street, most of the town is there."

    "They're all gathered close together, looking angry to a one."

    ma "Hey, you're all blocking the road."

    ma "Get on the sidewalks before someone gets hurt."

    $sidecharone = "Townie"

    sid1 "We're here for Gwen."

    "Several others mumble their agreement, continuing to glare at us in unison."

    mcmac "What?"

    "(This is really bad.)"

    mcmac "Mac, we got to get back to where she's locked up."

    ma "Yeah, we do."

    "Ignoring the crowd for now, we push our way back into the sheriff's office."

    "Gwen is standing beside Elmer, talking to him and giving a casual little flip of her hair."

    "Because someone took her cuffs off."

    "(This keeps getting worse. What is happening?)"

    ma "Elmer, why isn't Gwen still locked up?"

    "He freezes, glancing at Gwen."

    "She smiles back at him, and Elmer's shoulders straighten up, confidence suddenly blazing in his eyes."

    elm "Because she shouldn't have been."

    elm "Why are we giving her the hard sell for petty theft?"

    lu "Are you alright, sweetheart?"

    "My chest tightens with anger as Gwen puts on a scared face, turning the full force of it on Luce."

    gwe "This is just a misunderstanding, right?"

    gwe "I didn't mean anything by it."

    gwe "I just, I don't have anyone else or any place to go..."

    "(For fuck's sake.)"

    ma "That's a lie. You've been sleeping at Razi's place."

    gwe "He kicked me out!"

    mcmac "Yeah, because you're a—!"

    "I bite my tongue, stopping short."

    "Luce and Elmer are right there, which means I have to keep my mouth shut."

    gwe "I'm a what?"

    gwe "Are you going to start calling me names now, [genericfn]?"

    $menuhideborder = True
    menu macs2e10c3:
        "A. I wish I could.":
            $menuhideborder = False
            mcmac "Oh, trust me. I wish I could."

            mcmac "You'd deserve every one of them."

        "B. You know what I meant.":
            $menuhideborder = False

        "C. Don't even get me going.":
            $menuhideborder = False
            mcmac "Don't even get me going."
            mcmac "I have a whole list, made up special just for you."

    elm "Sheriff, you didn't arrest Gwen because of a grudge, did you?"

    "Mackenzie's eyes go wide."

    "There's anger in that gaze, sure, but underneath it is a bone-deep pain at the accusation."

    "(They have no idea. She could have been killed.)"

    ma "Do you want to run that by me one more time, deputy?"

    elm "It just seems like these two don't get along."

    elm "And it's pretty obvious you and [genericfn] are..."

    ma "Are what?"

    "The steel in Mackenzie's voice cuts right through whatever armor Gwen's approval has given him, and Elmer falls silent."

    ma "You work for me, Elmer."

    ma "That means following my orders, whether you like it or not."

    ma "If you don't like that, leave your badge on the desk."

    lu "Well, Gwen works for me, Sheriff."

    lu "And I'm not pressing charges."

    lu "She gives back the money, no harm no foul."

    gwe "Of course I will. I'm so sorry."

    elm "Um, I actually have the money."

    "He hands over the evidence bag to Luce,"

    "who doesn't even bother to count it before putting an arm around Gwen's shoulders to shepherd her out of the office."

    "When Mackenzie and I turn towards the door, all of the townsfolk are standing right outside the windows, staring."

    "(That's SO creepy!)"

    gwe "Wow, I've made so many new friends since coming here."

    "When Mackenzie and I turn towards the door, all of the townsfolk are standing right outside the windows, staring."

    "(That's SO creepy!)"

    gwe "Wow, I've made so many new friends since coming here."

    gwe "See you, Sheriff."

    "Mackenzie's hands clench into fists as the door swings shut behind Gwen and Luce."

    ma "I don't have a choice."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
