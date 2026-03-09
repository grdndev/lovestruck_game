label mac_season2_episode5:

    $tbc = False
    scene hifl_prologue at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "For once, sunlight wakes me up instead of an alarm."

    "After slowly opening my eyes to adjust to the light, I’m about to sit up and stretch when I realise Mackenzie is still asleep."

    "Sometime in the middle of the night, she must have turned over to face me."

    "Most of the blankets are on my side, but Mackenzie’s body is right against mine, one arm keeping me in a light embrace."

    "(Never mind.  Moving can wait.)"
    "(I don’t think I’ve ever seen her look this relaxed.)"

    "Even when we’re having fun together, I can always feel Mackenzie’s power like a coiled spring, alert and aware."

    "I don’t think it’s something she can turn off, but in slumber, it’s only the faintest buzz under her skin."

    mcmac "I guess alphas don’t get days off."

    mcmac "No wonder you run so hot all the time, Mac."

    "Shifting as carefully as I can, I trace my fingers up Mackenzie’s back to the nape of her neck, brushing against the line where her hair is cut short."

    "She lets out a little happy hum, but her eyes stay closed."

    mcmac "How many times do I have to sleep in your bed before we’re girlfriends?"

    mcmac "There’s got to be a moving truck rule about that or something."

    "I laugh softly to myself, not wanting to wake her up quite yet."

    mcmac "I keep thinking about it."

    "(Except I don’t want to push her.)"
    "(My world’s been turned upside down, but so has hers in plenty of ways.)"
    "(With Beau trying to cause trouble, being alpha is probably the first thing on Mac’s mind.)"
    "(Messing that up might get her hurt.)"

    mcmac "Being here is good, though. Really good."

    mcmac "I never imagined I’d end up with the gorgeous sheriff, that’s for sure."

    ma "I’m flattered."

    "I jump at Mackenzie’s voice vibrating against our shared pillow, my fingers jerking away from the back of her neck."

    "She grins at me, eyes still half-lidded with sleep."

    "(Oh god, I hope she only heard that last part.)"

    ma "You can put your hand back."

    mcmac "You’d like that, wouldn’t you?"

    ma "Uh-huh."

    "Mackenzie’s arm tightens around me, and I laugh as I’m pulled on top of her and into a tight hug."

    mcmac "It’s a little harder from this position."

    ma "There are always trade-offs in life."

    "I try to look up and stick my tongue out at her, but the world is a bit too blurry."

    "Settling my weight back on Mackenzie’s hips, I take my glasses off and clean them on my shirt, hoping I’m not ruining the moment."

    mcmac "Sorry. I shouldn’t have slept in these."

    ma "Nothing to apologise for from where I’m sitting."

    "(Oh.)"

    "(...Yeah, I’m good where I am too..)"
    $menuhideborder = True
    menu macs2e5c1:
        "A. I end up on top of you a lot.":
            $menuhideborder = False
            mcmac "I’m noticing that I end up on top of you a lot.."

            ma "Is that a bad thing?"

            mcmac "No, I definitely endorse this trend."

        "B. Must be pretty comfortable.":
            $menuhideborder = False

        "C. Enjoying the view?":
            $menuhideborder = False
            mcmac "Enjoying the view?"

            ma "More than you know."

            mcmac "No way. It's mutual, trust me."

    "I lean down to give Mackenzie a kiss, lingering long enough that I’m not sure if I want to pull away."

    "(We could just... not leave the bed this morning.)"

    ma "Much as I hate to say this, you’re going to have to move eventually."

    mcmac "Why?"

    ma "Because if I don’t workout soon before breakfast, you’re going to have a starving wolf on your hands."

    "(And what if I’m into that?)"

    mcmac "That’s not as convincing as you want it to be."

    "Mackenzie sits up, and although I stay in her lap, she’s suddenly taller than me again, our faces just inches apart."

    ma "How about you help me workout and then we eat together?"

    mcmac "Is there a lot of cardio involved?"

    ma "There certainly can be."

    mcmac "Count me in."

    "(I could totally become a morning person if it’s always like this.)"

    "Breakfast with Mackenzie is something out of a domestic dream, but unfortunately she has to go to work afterwards."

    "I text Razi to ask about work, only for him to say the bowling alley is dead, but I can come in later anyway."

    "(Slow days are really going to start costing me.)"

    "The diner has free newspapers and cheap coffee, so I head over there to cool my heels."

    "I’ve just sat down when a girl in the waitress uniform catches my eye."

    mcmac "Grace?!"

    "She turns around, and I lock eyes with Gwen."

    "My shock vanishes, replaced by a complicated mix of disappointment and embarrassment."

    gwe "It’s Gwen. But don’t worry, I think you were drunk the other night when I told you."

    mcmac "No, I... I’m sorry."

    mcmac "What are you doing here, though? Shouldn’t you be at the bowling alley?"

    gwe "Razi said if I’m staying here for a little while, I should learn what the town’s like."

    gwe "I walked in here for breakfast, and ended up with a job."

    "(Luce must have hired her on the spot. Damn it.)"

    mcmac "That's great."

    "It’s not, but I don’t want to rain on Gwen’s parade."

    "After she takes my order and leaves to help someone else, I leave my booth and go up to the counter, waiting for Luce to turn around and see me."

    lu "Morning, [genericfn]."

    lu "Did the new girl skip you over? She’s just starting."

    mcmac "I was wondering why there was a new girl at all."

    mcmac "You told me you were waiting for Grace to come back."

    "She frowns, and I know the Midwest look of annoyance disguised as mild discomfort far too well."

    lu "I am, but in the meantime, I need another hand around here."

    lu "The diner’s busier most places. We get a lot of truckers through here, and tourists on their way somewhere."

    "(But she replaced Grace without a second thought.)"

    mcmac "And if my sister comes back tomorrow?"

    lu "Then I’ll have two waitresses for once."

    lu "They’re nice girls, they’ll learn to split tips."

    $menuhideborder = True
    menu macs2e5c2:
        "A. Whatever.":
            $menuhideborder = False
            mcmac "Whatever."

            "The acid in my voice earns me a look from Luce that I can only describe as condescending."

            lu "Go drink your coffee, [genericfn]. I think you need it."

        "B. Thanks, I guess.":
            $menuhideborder = False
            mcmac "Thanks, I guess."

            "(It’s hard to be grateful when it sends like she doesn’t care.)"

            lu "You’re welcome."

        "C. We have bills to pay.":
            $menuhideborder = False
            mcmac "We've got bills to pay, Luce."

            lu "I know, honey, but so does everyone else in town."
            lu "Learn to make do."

    "It takes everything in me to peacefully go back to my seat instead of storming out, but the cup of coffee waiting at the booth helps."

    "I tip a couple packets of sugar in and take a long sip."

    "(No wonder Grace didn’t want to come back.)"
    "(Before I started getting closer to Mac and the rest, I wanted to do the same thing. To leave and never look back.)"

    "I watch Gwen make her rounds around the diner, smiling with every order she takes."

    "The mailman leaves a big tip behind for her, and I think Elmer is getting an instant crush from his usual spot in the corner."

    mcmac "Great."

    mcmac "She fits in perfectly."

    "I can’t find it in me to be angry, not while knowing Beau was targeting her, but there’s still a particular sort of frustration brewing in my chest."

    "(Doesn’t anyone here know what would have happened to them a few days ago if we hadn’t stepped in?)"

    "(Grace disappeared, and the entire town got to write off a werewolf invasion. But it’s just a haze now.)"

    mcmac "So they’ll never appreciate it. They don’t even care."

    mcmac "...No one should need a reason to feel bad about a missing girl."

    gwe "You doing okay over here?"

    "Gwen is standing right by the edge of the booth, coffee pot in hand. I force a smile."

    mcmac "I’m fine. Heading out for work,"

    gwe "Tell Razi I say hi. He and JD were really nice."

    mcmac "I will. Have a good shift."

    "I pay my bill, and walk out of the diner before I say something I regret."

    "I spend the first part of my shift rearranging bottles at the bar, and it only gets slower from there."

    "One kid comes in to chuck quarters at one of the arcade machines until she beats her old high score, then leaves me to silence."

    "(Most people would kill for a day where they got paid to do nothing, but I really could have used the work to clear my head.)"

    jd "Rough day?"

    "JD stands in the back doorway with their arms full of bowling balls, and I manage a small smile back."

    mcmac "Something at the diner pissed me off earlier. That’s all."

    jd "I could juggle these if it makes you feel better."

    "I almost agree, then imagine one of the bowling balls making a hole in the ceiling Razi getting pissed."

    "The last thing I need right now is my boss mad at me."

    mcmac "I’m good, thanks."

    jd "Suit yourself."

    jd "If no one comes in soon, though, I might start making modern art sculptures."

    "(Why do I have a feeling that would involve a lot of fire?)"

    mcmac "Well, while you’re setting up a budding artistic career…"

    mcmac "How was Gwen? Staying here, I mean."

    "JD smiles, then shrugs as if it’s too much of a break from their usual disaffected demeanour."

    jd "Not bad for a teenager. She crashed on my side for the night."

    jd "We got along pretty well. I didn’t get any new details, but ditching where you’re from…I get that."

    "(Of course they do. Gwen is getting along with everyone.)"

    "(Is it because she’s not human? Isn’t that the only thing that makes her different from Grace?)"

    jd "Hey."

    "I snap out of my angry spiral of thoughts, and JD’s humor from a moment before is gone."

    jd "If you don’t want to talk about it, that’s fine, but something’s brewing."

    jd "It’s written all over your face. You and the sheriff alright?"

    mcmac "It has nothing to do with Mac."

    mcmac "I just figured out that my sister had a superpower this whole time. She was fucking invisible."

    "I toss the rag in my hands down into the sink and leave the bar before JD can say another word."

    "Once I’m out the door and on the street, I let out a deep breath and check the time."

    "(Guess I’m taking my lunch break now.)"
    "(I think Mac’s off around this time too, and she’s right across this way…)"
    $menuhideborder = True
    menu macs2e5c3:
        "A. Join Mac on her lunch break." (paidchoice = "paidchoice"):
            $menuhideborder = False

            "(I can’t stay pissed off if I’m around her.)"
            "(I’ll pick up some food from the diner and bring it over as a surprise.)"

            "Of course, Gwen is still on duty when I come in the diner’s front door."

            "Her cheery little wave sets my teeth on edge, but I make my order without complaint, counting down the seconds before I can pay and get out of here."

            "(Why couldn’t Grace be here too? Hell, maybe they would have been friends.)"

            "(Instead, Gwen’s making everyone forget about my sister.)"

            gwe "Have a good day!"

            mcmac "Right."

            "I can almost feel the grey cloud hanging over my head when I bring the food into Mackenzie’s office."

            "She’s talking with Elmer, who is listening with rapt attention."

            ma "Just drive a clean loop around town,  alright?"
            ma "And check on the farms in the back. My dad called this morning and said something’s been bothering his neighbour’s animals."
            ma "Make sure we don’t have kids setting firecrackers off in the woods again."

            elm "You got it, Sheriff."

            "He practically bounces out the door past me, excited to go on patrol alone, and I catch Mackenzie’s eye by holding up the bag of food."

            "She smiles wide, summoning me over to the desk with a tilt of her head."

            ma "Lunch, huh? This is great."

            mcmac "Yeah. Thought you might be hungry."

            "The cheer I try and put into my voice doesn’t quite take, and Mackenzie hesitated after I set the bag down."

            ma "Doesn’t seem like that’s the only thing on your mind, though."

            ma "What’s up?"

            mcmac "It’s..."

            mcmac "You’re going to think I’m petty."

            ma "Despite the name, being petty isn’t actually a crime. I’m listening, [genericfn]."

            "Those words alone are a relief, and I sit on the edge of Mackenzie’s desk,"

            "trying to be as close to her as I can without breaking the professional line hanging between us."

            "(Hard to overlook that with the sheriff’s star printed on everything.)"

            gwe "It’s about Gwen."

            gwe "Except she hasn’t done anything. She’s just existing, right in all the places where…"

            "I look down at the floor, biting my lip."

            ma "Where Grace was?"

            mcmac "...Yeah. Am I being that obvious?"

            ma "Gwen’s about the same age, same look. She was in danger, except age got saved in time."

            "That’s it. The sticking point right there, and I feel tears well up in my eyes in a hot rush."

            "Mackenzie’s hand catches around my wrist, a gentle anchor."

            "Her thumb draws slow, soothing circles over the pulse there before she pulls me towards her."

            ma "Come here."

            "I end up in Mackenzie’s lap, and my face flushes pink as her arms surround me in a warm embrace."

            mcmac "You’re at work."

            ma "I don’t care. You need this."

            ma "And besides, I run this place. Decorum is whatever I say it is."

            "I let out a weak laugh at that, burying my face in Mackenzie’s shoulder."

            "Her hands slowly stroke up and down my back until breathing is easy again."

            mcmac "I miss her so much."

            ma "I know."
            ma"But I also know Grace wouldn’t want you being so upset you make yourself sick."
            ma "So we’re going to cool off, then sit down and eat, okay?"

            "I nod, letting the warmth radiating from Mackenzie’s body sink into new."

            "When my shoulders relax, the rest of my muscles give in with it, and she presses a kiss to the top of my head."

            ma "Better?"

            mcmac "Yeah."

            mcmac "Is that some kind of alpha magic I should know about? Calming people down?"

            ma "I mean, it’s probably because you’re my girlfr…"

            "Mackenzie stops short, and now she’s the one who’s tense."

            "(We really need to have that conversation. But probably not while I’m in her lap.)"

            mcmac "Hungry?"

            ma "Starved."

            "I untangle myself from Mackenzie’s arms so I can start unpacking the food, but I can feel her eyes on me the whole time."

            "When I hand her one of the sandwiches and our fingers brush, my face goes red as a traffic light."

            ma "Is this a double? You already know my order."

            mcmac "Please. I think you’re the only person in town who can actually finish Luce’s special in one sitting."

            "We both laugh, and after that it’s easier to talk."

            "(I know Mac and I will get there. It’s just a matter of time.)"

        "B. Go stew about things in your truck.":
            $menuhideborder = False

            "(I'm going to pick up some food and blow off some steam.)"

            "There's only one place to go unless I want to risk getting something out of the gas station's heat-'em-up corner, so I duck back into the diner."

            "Luce is minding the stove, and Gwen pops up to greet me."

            gwe "Hey! Getting something to eat?"

            mcmac "…Yeah. Tell Luce I want my usual."

            "She nods and hurries off behind the counter, leaving me glowering by the cash register until Luce hands over a bag of food."

            "We don't exchange pleasantries, just my debit card, and I head back to my truck."

            "I drive to the edge of town before opening up my food, but I'm worked up enough that the first bite is just short of tasteless."

            mcmac "Great."

            mcmac "Can anything cooperate with me today?"

            "Chewing through every last bite makes me grimace a little, but I'm not going to waste food and money."

            mcmac "If I had money, this would be easier."

            mcmac "I could hire a private investigator to find Grace, and keep the lights on without having to babysit the bowling alley."

            "Guilt sours the back of my tongue."

            "Razi was kind enough to give me my job without any references, but we see so little traffic, I don't have any justification asking for a raise."

            "Then I remember the money Mackenzie offered, enough to let me leave. And I refused every dollar."

            "(I don't want to rely on her for that. It isn't fair.)"

            mcmac "Maybe I should start investing in lottery tickets."

            mcmac "That's what the mail guy does."

            "After bundling up my trash, I start up my truck again. My break's already almost over."

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
