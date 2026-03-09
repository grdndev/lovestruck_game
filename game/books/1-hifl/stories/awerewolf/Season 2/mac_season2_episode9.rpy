label mac_season2_episode9:

    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "Mackenzie jumps down from the truck, unlocking the doors so I can get inside."

    "She takes the driver's seat, letting out a low growl before starting the engine."

    ma "I trusted her."

    ma "I can't believe I bought that story about Beau."

    mcmac "Everyone did, Mac."

    mcmac "It's not like the guy didn't threaten you right before she showed up."

    ma "I know."

    ma "But I can't offer protection to one person and jeopardize everyone else. She could have killed you."

    mcmac "She didn't touch me. You kept me safe."

    "With a faint nod, Mackenzie hits the gas, and we zip away from the drive-in and back towards the main road."

    "The tires of my truck squeal as she brakes outside the bowling alley, and we both hurry inside."

    ra "Hey, we're clos—!"

    ra "Mac? You wolfed out for a reason?"

    "Mackenzie shifts back after a moment's hesitation, reaching up to brush her hair back in place where furred ears were a moment ago."

    ma "Yeah. Because Gwen just tried to kill me and [genericfn]."

    ra "What?"

    ma "You might want to call the others."

    "Razi shouts for JD to come downstairs before calling Diego."

    "The doctor shows up a few minutes later, his expression grim."

    di "So, what happened?"

    "Mackenzie and I explain the ambush, and by the end of it, Razi looks like he needs a drink."

    "JD, on the other hand, sighs and relaxes against the bar."

    jd "You really can't trust kids these days, huh?"

    jd "I was bad at that age, but I wasn't an assassin."

    ra "JD, Mac and [genericfn] could have been killed."

    jd "I know."

    jd "What I also know is that we fucked up and missed the signs of this, so let's deal with that."

    ma "I was the one who missed the signs."

    ma "This is my responsibility."

    di "You took a scared girl at her word, Mackenzie."

    di "More people should do that. It just so happened that Gwen took advantage of it."

    jd "Any idea what she is?"

    mcmac "Full of claws and sass, mostly."

    ma "Honestly, if it's not someone local, I only know stories."

    ma "Gwen could be anything."

    $menuhideborder = True
    menu macs2e9c1:
        "A. Does it matter what she is?":
            $menuhideborder = False
            mcmac "Does it really matter what she is?"

            jd "Well, it would give us a good idea of weaknesses."

            jd "Trust me, there's nothing more embarrassing than trying to stab someone and having the knife bounce off."
        "B. We need to stop her.":
            $menuhideborder = False

        "C. Gwen is dangerous.":
            $menuhideborder = False

            mcmac "What Gwen is? She's dangerous."

            ra "Without a doubt."

            ra "She was sleeping here, and I had no idea."

    "(I should have told everyone about her little claw trick in the diner earlier.)"

    "(Still, I was right to be uncomfortable around her.)"

    di "The fact is, Havenfall is unusual."

    di "Our different kinds rarely manage to cooperate beyond the occasional temporary truce, much less live in close quarters."

    ra "But it's known as a sanctuary."

    di "It is. But I am rarely surprised when someone outside our circle acts in bad faith against a different supernatural sort."

    mcmac "I didn't have any idea about that."

    mcmac "She just gave me the creeps."

    jd "And now you're all vindicated, huh?"

    mcmac "I mean..."

    "I smile a little, but Mackenzie raises a brow."

    ma "We were still attacked for our trouble. Twice."

    "(Okay, so I shouldn't be too smug about it.)"

    "(It's just nice to be right after being so oblivious to all this supernatural stuff.)"

    mcmac "Then what's next?"

    ma "We make a plan to stop her."

    jd "I'm all in on that."

    di "As am I."

    di "Part of why I live in Havenfall is how peaceful it is. I'd like to keep it that way."

    "Razi nods, crossing his arms. The sting of betrayal lingers in his eyes, and I can't help feeling bad for him."

    ra "Let's get started."

    "After a long discussion at the bowling alley, Mackenzie drives me home."

    "I tell her to crash on the couch, then duck into the kitchen to make us some hot chocolate so we can relax."

    "Turns out, I have a bunch of little moon-shaped marshmallows in the back of a cabinet, and I throw them on top before bringing the cups over."

    mcmac "Special delivery."

    ma "Thanks. It smells great."

    "I squeeze onto the couch next to her, then take a long sip of the hot chocolate."

    "Being at home is nice, but having Mackenzie right beside me means everything feels safe."

    mcmac "You know, I caught what you said to Gwen."

    ma "Which part? That she couldn't get the jump on me again?"

    mcmac "Noooo."

    "After drawing out the word, I smile."

    mcmac "The part where you implied you'd kick her ass twice as hard because she threatened me."

    mcmac "Threatened your girlfriend."

    "My face heats up before I can stop it, and I look into the hot chocolate like the steam coiling from it will give me an excuse."

    "Mackenzie grins, then moves to tuck her free arm up and around my shoulders."

    ma "You like me calling you that, huh?"

    mcmac "I really do."

    "A light tug draws me into a kiss, and I return it until I've kissed all the s Mackenzie' mouth."

    "It takes a little while, but every second is a pleasure."

    mcmac "And I like having a girlfriend."

    mcmac "Even if the phrase 'I'm dating a hot werewolf cop' still makes my head spin."

    "Mackenzie laughs, the sound a warm rumble in her chest."

    ma "The first two I was born with, you know."

    mcmac "Hey, inherited or not, you maximize your full potential, okay?"

    mcmac "Sounds like I'm leveling up in a video game."

    mcmac "You sure about that?"

    mcmac "Maybe I should start saving up to buy you a super hero costume."

    "Her blush makes me grin, and I lean over to kiss Mackenzie's cheek."

    mcmac "Or not, if you like staying undercover."

    ma "Half my life's undercover. I used to wonder how detectives did it, but now I realize..."

    ma "You just have to. It becomes second nature."

    $menuhideborder = True
    menu macs2e9c2:
        "A. Do you wish it was different?":
            $menuhideborder = False
            mcmac "Do you wish things were different?"

            mcmac "That you didn't have to hide being a werewolf?"

            ma "Sometimes."

            ma "But honestly, my life seems to get even more complicated whenever people find out."

            ma "If everyone knew? I can't even imagine."

        "B. I like you just the way you are.":
            $menuhideborder = False
            mcmac "I like you just the way you are, Mac."

            ma "I know you do."

            ma "And I appreciate that keeping things under wraps doesn't bother you."

            mcmac "Of course not. I want to keep you safe."

        "C. At least were in it together.":
            $ menuhideborder = False
            mcmac "At least we're keeping the secret together, right?"

            ma "Yeah, that makes it a lot easier."

            ma "Trust me, when I first found out about Razi, I was so relieved."

            mcmac "Because someone else knew exactly how you felt."

    "(After a night like this, I want Mac to rest.)"

    mcmac "How about I toss on a cheesy documentary for us to laugh at?"

    ma "What do you have on the roster?"

    mcmac "How about The Alien Conspiracy in American High Schools?"

    ma "With a title like that, how can I pass it up?"

    "I queue it up on the TV, relaxing in Mac's embrace while we finish off our hot chocolate."

    "It's nice to unwind, even if only for a little while."

    ma "You doing okay after what happened?"

    mcmac "With Gwen?"

    ma "With her, with Grace."

    ma "With wolves like Annabelle turning up on your doorstep."

    "I take a moment to think it over, watching all the ridiculously photoshopped diagrams playing in the documentary."

    mcmac "I'll feel better once I know Gwen's off our tail."

    mcmac "And when Grace is home. But I'm making it through."

    mcmac "As for Annabelle..."

    ma "Hmm?"

    mcmac "At least she didn't seem like as big of a jerk as Damien."

    ma "That's not a high bar to clear."

    mcmac "True."

    mcmac "But it'd be nice if we had more people to back us up against Beau, you know?"

    ma "...Yeah."

    ma "Yeah, I know."

    "Mackenzie goes quiet after that, but she doesn't seem upset."

    "If anything she's contemplative, and I lean against her shoulder, offering quiet comfort while she sorts things out."

    "I drop Mackenzie off at work in the morning, snagging some coffee from the gas station before parking across from the bowling alley."

    "The idea of going into the diner has me on edge after how much Gwen has been there."

    "Still, I pocket my keys, glancing across the street and through the diner's windows."

    "There aren't any customers, but I see someone hunched over the cash register."

    "(Shit, it has to be Gwen. How could she even think to show her face after what happened?)"

    "(That's not Luce.)"

    "Heart hammering quickly in my chest, I carefully inch over to the diner, trying to get a better look."

    "The drawer of the register is yanked out, and Gwen is casually counting the money before shoving it in her pockets."

    mcmac "What the hell?"

    mcmac "Is she going to rob the diner and split because she couldn't kill Mackenzie?"

    "(Maybe this is weird, but I sure hope Mac's life was worth more than the daily take from a diner register.)"

    "(Otherwise, that's just insulting.)"

    mcmac "She hasn't seen me yet."

    mcmac "What should I do?"

    "Going after her myself seems out of the question. Mackenzie is right next door, and fast enough to grab Gwen if she runs."

    $menuhideborder = True
    menu macs2e9c3:
        "A. Call Mac for help." (paidchoice = "paidchoice"):
            $menuhideborder = False

            "(But I don't want Gwen to see me running over to the station.)"

            "Instead, I duck down behind the closest car and pull out my phone, keeping an eye out in case the diner door swings open."

            "After one ring, Mackenzie picks up."

            ma "Hey what's up?"

            ma "Did I leave something at your place last night?"

            mcmac "No, you're fine."

            mcmac "But Gwen is in the diner."

            "Mackenzie falls silent for a moment."

            ma "Is there anyone in there with her? Potential hostages?"

            mcmac "I didn't see anyone, but Luce should be there."

            mcmac "I see her sedan down the street."

            ma "Alright, so one maybe."

            ma "What's she doing in there? Pretending to work?"

            mcmac "She's tearing the register apart and taking all the cash."

            ma "That's pretty bold for a couple hundred bucks."

            mcmac "I know, but we have to stop her, right?"

            ma "Of course we do."

            ma "I'm going to walk on over there. Stay put until I crack the door open alright?"

            mcmac "You got it."

            ma "Hey, I…"

            ma "Be careful. I'll just be a minute."

            "(What was she going to say before that?)"

            mcmac "Don't worry. She can't see me."

            "Mackenzie hangs up and I put my phone away."

            "A moment later, I hear the sheriff's door swung open, and track Mackenzie's footsteps under the car until she stops in front of the diner."

            "Standing up as slowly as I can, I move in behind her, but Gwen notices us both in an instant."

            gwe "Afternoon, officer."

            "She makes a show of counting the money in her hands before fucking it right into her pocket."

            "(What an asshole.)"

            ma "I'm going to need you to put your hands up and step away from the counter."

            gwe "Oh, really? We're going to do this that way?"

            gwe "Cute, it's almost like you're an actual cop."

            ma "This badge isn't for show. Neither is the gun."

            "Gwen rolls her eyes, plucking one last bill out of the register."

            gwe "Come on, sheriff. You know the optics of that."

            gwe "You don't get to shoot teenage girls like me. People make a fuss."

            ma "I bet that face is real handy for your work, huh?"

            gwe "Of course. I'm harmless."

            "Mackenzie shifts a step forward and Gwen's eyes narrow. She shoves the empty register drawer back in with a thunk."

            ma "You're not getting out of here, Gwen."

            gwe "Yeah, I am."

            gwe "Want to know why?"

            "She smiles, then looks towards the back door of the diner."

            gwe "Luce, you doing okay back there?!"

            lu "The door's still stuck, Gwen!"

            lu "Are you sure the key didn't work?"

            gwe "It didn't. Do you want me to call a locksmith?"

            lu "Oh, sweetie, we only have one of those and I'm pretty sure he's hungover right now."

            gwe "I'll go run next door for help then."

            "Dropping the innocence out of her expression, Gwen turns back to us with a smile."

            gwe "Listen, I'm walking out of here one way or another."

            gwe "It's your choice if Luce gets gutted in the process. No skin off my nose."

            ma "You won't make it to that door."

            gwe "We'll see about that."

            "Gwen shoves the register with a burst of strength, sending it flying off the counter."

            "Mackenzie has to catch it to keep it from being knocked over, and Gwen tosses herself over the counter before dashing past me."

            mcmac "Oh, goddamn it."

            ma "I was thinking the same thing."

            "Mackenzie drops the register back in place with a loud ding."

            ma "Get Luce out of the back. I'll catch her."

            mcmac "Be careful."

            "Mackenzie nods, then sprints out of the diner."

            "I move behind the counter, then kick away the wedge Gwen must have put under the back door."

            "When I open it, Luce is standing there looking mystified."

            lu "You're not Gwen."

            mcmac "No, but I'm going to go get her. Later!"

            "I leave before Luce can ask any questions, making my way back onto the street."

            "The good news is that Mackenzie caught up to Gwen. The bad news is that they're fighting each other."

            "It's nowhere as violent as the fight at the drive-in, but it takes a moment for Mackenzie to wrangle Gwen's hands behind her back."

            ma "You managed ten feet. I'll give you that."

        "B. Get Luce.":
            $menuhideborder = False

            "(It's Luce's diner. She needs to know.)"

            "(But where is she?)"

            "I glance around and catch sight of Luce's old sedan down the way, but it's empty."

            "She wasn't in the gas station, and she never sets foot in the bowling alley."

            mcmac "Damn, is she inside the diner?"

            mcmac "Maybe Gwen hurt her."

            "Using that thought to steel myself, I yank the diner door open and step inside."

            "Gwen's head snaps up, and she smirks at me."

            gwe "Sorry, diner's closed."

            mcmac "You're a thief and a killer. Charming."

            gwe "Listen, if it pays the bills, I'm not picky."

            gwe "Now waltz out of here before I paint the windows red with you."

            "Swallowing past my nerves, I take another step forward instead."

            "When I do, the back door of the diner rattles, and I hear Luce from behind it."

            lu "Gwen, sweetheart, I think the door's stuck."

            lu "Can you come over and pry it open on your side?"

            "(Okay, Luce is still alive. Better than the alternative.)"

            gwe "One second! I'm with a customer."

            "Gwen's cheery mask falls away as she folds the last of the money into her pockets, then shoves the register shut."

            gwe "You're brave for a human, but let's make things clear."

            gwe "I'm about to walk out of this diner, and if you try to stop me, you won't even have a chance to scream for your wolf. Got it?"

            "She struts past me before I can say a word, and I hate that I'm trembling."

            "When the diner door swings shut behind Gwen, I duck past the counter to let Luce out of the back."

            lu "[genericfn]? What are you doing here?"

            mcmac "Don't worry about it. Just stay inside, okay?"

            "Ignoring her confused look, I turn and dash back out of the diner, looking for any sign of Gwen."

            "What I find is her having a standoff with Mackenzie in the middle of the street."

            gwe "Can I help you, officer?"

            ma "You smell like money. Strange, because you haven't finished your job yet."

            gwe "Luce gave me a raise. She's a sweet old lady."

            mcmac "Mac, she robbed the place!"

            "Gwen sneers at me."

            gwe "Thanks for your input, Nancy Drew."

            gwe "It doesn't matter what I did. Sheriff's not fast enough to catch me without changing."

            ma "You think so?"

            ma "Let's find out."

            gwe "You wouldn't. Not in broad daylight."

            "Mackenzie darts forward and Gwen immediately starts running the other way."

            "She hooks a hard right into the alley, but I know that one—it's a dead end."

            "And Mackenzie knows that too."

            gwe "Get your hands off me!"

            gwe "Trust me, wolf, you're going to regret it."

            ma "A minute ago, you said I wouldn't be able to catch you."

            ma "So turns out I don't have a lot of confidence in your promises."

            "Gwen growls as she's dragged from the alley and back onto the street."

    "Mackenzie presses down on Gwen's back while the other locks handcuffs around narrow wrists."

    ma "You're under arrest."

    gwe "For what exactly?"

    ma "Right now? Petty theft."

    ma "After you and I talk in private? Then well, we'll see."

    gwe "Good luck with that."

    mcmac "You tried to murder her."

    gwe "Really? I think that will be your word against mine."

    gwe "Unless you actually plan to go to court and tell them I'm a big bad monster."

    "Sarcasm drips from Gwen's words like venom, and when she smiles at me, a knot of cold fear twists in the center of my stomach."

    gwe "Just wait."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
