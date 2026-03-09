##Important! Only include this ONCE. You can move it into a different file, "\"but you only want to define your story once.
##Update the episode and season counts here.
label ghost_season1_episode3:
    $tbc = False
    scene bg main_day at bg
    play music hifleveryday

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() at the bottom.
    "We head out into the street, Razi managing to hold the door for me in a way that feels gentlemanly, and not because I can't touch the frame."
    show ghostmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(I know I'm being stupid about this. I can probably just walk right through the wall, if I want, but...)"
    show ghostmc vestlesscasual_cu sad_cu at hiflmc_cu
    "(I really don't want to.)"
    hide ghostmc
    "We arrive at the bowling alley to find it with the sign flipped over to 'closed', even though it's probably not even one o'clock yet."
    show razi casual basic at centre
    "If he's bothered by the loss of today's business, Razi doesn't show it, just nodding once in satisfaction before holding the door for me again."
    hide razi
    show bg bowling with dissolve
    play music getitdone
    "There's an eclectic little crowd waiting for us inside, sitting around the bar and chatting quietly amongst themselves."
    "The few customers that had actually been here to bowl- a handful of kids and their parents, for the most part- have all vanished."
    show ghostmc vestlesscasual_cu basic_cu at hiflmc_cu
    if persistent.s1e2tamFlag:
        $sidecharthree = "Tamara"
    else:
        $sidecharthree = "Tam"
    "(Looks like [sidecharthree]'s taken off as well.)"
    show ghostmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(I guess she's not part of the 'in group.')"
    hide ghostmc
    show jd casual surprised at centre
    "JD's there, and they're the first to see us as we walk in."
    show jd casual sad
    "They don't quite meet my eyes, but in a different way to [sidecharthree] or Luce- in this case, they're actively avoiding my gaze."
    hide jd
    show mac cop surprised at centre
    "Sheriff Mackenzie Hunt's there too, and when {i}she{/i} sees me, she's on her feet in the blink of an eye, looking utterly bewildered."
    show mac cop basic
    "There's something else there, too, a flicker of emotion that crosses her face, too fast for me to parse."
    show mac cop surprised
    $sidechartwo = "Mackenzie"
    sid2 "I don't believe it."
    show mac cop angry at centre
    sid2 "I was damn sure this was going to be one of your stupid pranks, Davies."
    show jd casual angry at right3
    show mac cop angry at left3
    jd "Bite me, Mac, I'm not in the mood."
    sid2 "Don't tempt me."
    show ghostmc vestlesscasual basic at right3
    hide jd
    show mac cop basic
    sid2 "It's good to see you, [genericfn]."
    hide mac
    show ghostmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(Is it? I'm having a hard time reading how she actually feels about it, to be honest.)"
    show ghostmc vestlesscasual surprised at right3
    show mac cop basic at left3
    ghostmc "Uh, yeah. Likewise, Sheriff."
    hide mac
    show ghostmc vestlesscasual_cu basic_cu at hiflmc_cu
    "(I've never really spoken to the Sheriff- to Mackenzie, before.)"
    show ghostmc vestlesscasual_cu sarcastic_cu
    "(It's not that I don't like her or anything, I just... never really had a reason to talk to a cop.)"
    "(Thankfully.)"
    hide ghostmc
    hide mac
    "The third and final person at the bar takes me entirely by surprise."
    show ghostmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(I had expected to see JD, and a cop kinda makes sense- but what's the doc doing here?)"
    show ghostmc vestlesscasual surprised at centre
    ghostmc "Dr. Escalona?"
    show ghostmc vestlesscasual surprised at right3
    show diego glassesdoctor happy at left3
    $sidecharone = "Dr. Escalona"
    sid1 "Hello, [genericfn]."
    show diego glassesdoctor smirk
    sid1 "Nice shirt."
    hide diego
    show ghostmc vestlesscasual surprised at centre
    "Confused, I inspect the article of clothing in question, and..."
    show ghostmc vestlesscasual_cu angry_cu at hiflmc_cu
    "(Ugh. Great.)"
    "(No blood, but I do get the pizza grease stain from the night {i}before{/i} I died. Perfect.)"
    hide ghostmc
    show ghostmc vestlesscasual_cu basic_cu at hiflmc_cu
    "(I wonder if I can...)"
    show ghostmc vestlesscasual sleep at centre
    "I close my eyes, and think about my favorite vest."
    "I know for a fact that it covers this particular stain perfectly, because that's exactly how I did it the day I died, when I went for groceries."
    show ghostmc casual sleep with dissolve
    "It's actually pretty easy to change, now that I know I can do it."
    hide ghostmc
    show diego glassesdoctor surprised at centre
    "I open my eyes to see Dr. Escalona staring at me like I just grew a second head."
    sid1 "That's... quite impressive."
    sid1 "I don't believe I've ever seen a ghost who can alter their appearance like that. Although..."
    show diego glassesdoctor smirk
    sid1 "I notice you didn't actually change out of the dirty shirt."
    show diego glassesdoctor at left3
    show ghostmc casual angry at right3
    ghostmc "It's a perfectly good shirt!"
    hide diego
    show jd casual sad at left3
    show ghostmc casual angry at right3
    jd "...Hey, [genericfn]."
    show ghostmc casual basic
    ghostmc "Hey, yourself."
    jd "Sorry. About being an asshole, before."
    show jd casual sad
    jd "I just- I really didn't think I'd see you again."
    show jd casual angry
    jd "Then I did see you again, and instead of like, hugging you or something, I just tried to find a reason I shouldn't."
    show ghostmc casual sarcastic
    ghostmc "Yeah, well, to be fair, I don't think there's a how-to guide on meeting dead friends."
    show jd casual smirk
    jd "I want ten copies of that book right now."
    show jd casual basic
    jd "...Are we cool?"
    show ghostmc casual happy
    ghostmc "Yes, we're cool."
    show ghostmc casual happy
    ghostmc "And you can try to hug me if you want, but if my head ends up inside you, I will find a way to vomit in there."
    show ghostmc casual happy at right1
    show jd casual basic at left1
    with ease
    show jd casual sad
    "The hug... doesn't work, but it at least goes better than Razi's hug did. JD is extremely careful to avoid letting any part of me enter their body."
    hide jd
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "I think both of us appreciate that."
    show ghostmc casual basic at centre
    ghostmc "So, I've got a question."
    show ghostmc casual basic at right3
    show razi casual smirk at left3
    ra "Just the one?"
    show ghostmc casual sarcastic
    ghostmc "How is it that a cop, a doctor, a bowling-alley proprietor and, uh..."
    hide razi
    show mac cop smirk at left3
    sid2 "A felon?"
    hide ghostmc
    show jd casual angry at right3
    jd "That is technically inaccurate!"
    show jd casual smirk
    jd "I haven't been convicted of anything." 
    hide jd
    hide mac
    show ghostmc casual sarcastic at centre
    ghostmc "...And someone who is not technically a felon, all know about ghosts, and can see me when Luce and the new girl can't?"
    ghostmc "Should I be worried? You're not ghost hunters or whatever, right?"
    show ghostmc casual surprised at right3
    show mac cop basic at left3
    sid2 "No, we're not. You're completely safe."
    hide mac
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(...You know, I had thought I was just joking, but it's actually sorta a relief to hear her say it.)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Maybe getting murdered makes you paranoid?)"
    show razi casual basic at left3
    show ghostmc casual basic at right3
    ra "As for why only we can see you... I'm no ghost expert, but I do know that all four of us have something in common."
    show ghostmc casual sarcastic
    ghostmc "Which is?"
    hide razi
    show jd casual smirk at left3
    jd "Fun fact: There's not a single human in the building."
    show ghostmc casual surprised
    show jd casualhorns devilsmirk with dissolve
    "The transformation is fast, and JD makes it look almost mundane- but the effect is anything but."
    ghostmc "Are- are those {i}horns{/i}?"
    show jd casualhorns devilsmirk
    jd "They're sure as hell not noses."
    ghostmc "But what are- what...?"
    show jd casualhorns devilhappy
    jd "I'm an actual demon. From actual hell."
    hide jd
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Hell is real!?)"
    show ghostmc casual_cu sarcastic_cu
    "(That's... not actually that surprising, come to think of it. Ghosts have to end up somewhere.)"
    show ghostmc casual_cu sad_cu
    "(I'll try not to think about that one too much.)"
    hide ghostmc
    "I whip my head around to look at the others."
    show ghostmc casual surprised at centre
    ghostmc "Demons."
    ghostmc "You're all demons?"
    $menuhideborder = True
    hide ghostmc
    menu ge2c2:
        #"A. Yes" (paidchoice = "paidchoice"):
        "1. Look at Mackenzie":
            $menuhideborder = False
            $sidecharthree = "werewolves"
            show mac cop basic at centre
            sid2 "No."
            show mac earscop wolfsmirk with dissolve
            sid2"I'm a werewolf. Unsurprisingly, only the hellion's from hell."
            show mac earscop wolfsmirk at left3
            show ghostmc casual surprised at right3
            ghostmc "Oh, wow!"
            show ghostmc casual happy
            ghostmc "...Your ears are cool."
            show ghostmc casual happy
            ghostmc "If I had hands, I'd ask if I could touch them."
            sid2 "If you had hands, I'd think about it."
            show jd casual smirk at right3
            show mac earscop wolfangry at left3
            hide ghostmc
            sid2 "{i}You{/i} think about it, Davies, and you're going in a cell."
            show jd casual surprised at right3
            jd "I didn't do anything!"
            sid2 "And you won't."
            hide mac
            hide jd
        "2. Look at Dr. Escalona":
            $menuhideborder = False
            $sidecharthree = "vampires"
            show diego glassesdoctor sleep at centre
            sid1"There's a few pseudoscientific theories about our connection to hell, but..."
            show diego glassesdoctor vampirebasic with dissolve
            sid1"In most respects, vampires are very much unlike demons."
            show razi casual sad at right3
            hide ghostmc
            show diego glassesdoctor vampirebasic at left3
            ra "Diego, we cannot have this argument again."
            $ sidecharone = "Diego"
            show diego glassesdoctor vampireangry at left3
            sid1"I can if you will."
            show razi casual angry at right3
            ra "Fine. Explain why holy oil-"
            sid1"Razi, if you mention holy oil to me one more time, I'm going to start buying my blood from Labasque's coven instead."
            show razi casual smirk at right3
            ra "Oh, good- ask her about holy oil while you're there."
            hide razi
            hide diego
            show ghostmc casual surprised at centre
            ghostmc "Uh...?"
            show ghostmc casual surprised at right3
            show mac cop basic at left3
            sid2 "I'm not sitting through this again."
            show mac cop angry at left3
            sid2 "Both of you, shut it- I've got work to do, today."
            hide mac
        " 3. Look at Razi":
            $menuhideborder = False
            $sidecharthree = "djinn"
            show razi casual surprised at centre
            ra "Me? A demon?"
            show razi djinn smirk at centre with dissolve
            ra "I'm wounded, [genericfn]. You'd compare me to JD?"
            show razi djinn smirk at left3
            show ghostmc casual surprised at right3
            ghostmc "..."
            show ghostmc casual sarcastic at right3
            ghostmc "Razi."
            ra "Yes?"
            ghostmc "Where's your shirt?"
            ra "A great and powerful djinn like myself has no need for your mortal 'shirts.'"
            hide ghostmc
            show jd casual angry at right3
            jd "Sure, it's fine for you to do it, but if I come to work naked it's 'against company policy.'"
            show razi djinn basic
            ra "Sorry, Jordan- I don't make the rules."
            show jd casual surprised
            jd "Yes, you do! You do that!"
            hide jd
            hide razi
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Ghosts, demons, [sidecharthree]... I've been surrounded by impossible things my whole life, and just didn't know about it.)"
    show ghostmc casual surprised at centre
    ghostmc "So... if I'm getting this straight, you think that only people like you-"
    if persistent.s1e2tamFlag:
        $sidecharthree = "Tamara"
    else:
        $sidecharthree = "Tam"
    show ghostmc casual sarcastic
    ghostmc  "People like {i}us{/i}, I guess, can see me?"
    show razi casual sad at left3
    show ghostmc casual sarcastic at right3
    ra"It's just a theory. Ghosts aren't all exactly the same, but... that seems to be the case for you."
    hide razi
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...I'm pretty sure Grace wasn't secretly a demon.)"
    "(If he's right, then my sister won't even be able to see me.)"
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(She'll just walk through me like [sidecharthree] did, and I'll see her-)"
    show ghostmc casual surprised at right3
    show razi casual basic at left3
    ra "[genericfn], there's things we can do- you're not going to be stuck invisible for the rest of your life."
    show razi casual sad at left3
    ra "...afterlife."
    show ghostmc casual sad at right3
    ghostmc "And how long is that going to be? My 'afterlife'?"
    ra "...I wish I could tell you."
    hide razi
    hide ghostmc
    "There's a long silence, after that."
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(The reunion's been fun, but I guess you can't really joke away how messed up the situation is.)"
    show ghostmc casual_cu sad_cu
    "(A woman was murdered, after all. She just... happened to be me.)"
    show ghostmc casual_cu sarcastic_cu
    "(Yeesh. Change of topic time.)"
    show ghostmc casual basic at centre
    ghostmc "So, uh- where is Grace, anyway? Razi, you said she's out of town?"
    show ghostmc casual basic
    ghostmc "You still haven't told me what this amazing job of hers is."
    show ghostmc casual basic at right3
    show jd casual happy at left3
    jd "Oh, you're going to {i}love{/i} this."
    show ghostmc casual sarcastic
    ghostmc "Why do I get the feeling that I will not, in fact, love this."
    hide jd
    show razi casual sad at left3
    ra "Probably because you won't. Grace is..."
    "Razi hesitates."
    ra "Let's say that she's heavily involved with supernatural affairs."
    show ghostmc casual surprised
    ghostmc "What does that mean?"
    hide razi
    show mac cop basic at left3
    sid2 "Think vampire hunter."
    show ghostmc casual sarcastic
    ghostmc "Bullshit."
    show mac cop smirk at left3
    sid2 "Nope. Completely true."
    show mac cop happy at left3
    sid2 "Your sister's the one- and only one- in the business that I'd trust in my town."
    hide mac
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(She's not joking.)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...She's not joking.)"
    show ghostmc casual surprised at centre
    ghostmc "That's- that's literally the most dangerous sounding job she could possibly have!"
    show razi casual surprised at left3
    show ghostmc casual angry at right3
    ghostmc "Razi!"
    ra "What?"
    ghostmc "You said it was a dream job!" 
    ra "I never said it was {i}your{/i} dream job! It's hers!"
    show razi casual smirk
    ra "Besides, you don't even know how much she's making. That girl has more money than she knows what to do with, the poor thing."
    hide razi
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...I hate how good of an argument that is for me.)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(Still, you shouldn't have to be a vampire hunter just to pay the bills!)"
    show ghostmc casual sarcastic at centre
    ghostmc "And you're okay with this, Doc?"
    show ghostmc casual basic at right3
    show diego glassesdoctor sad at left3
    sid1 "I was... wary of her, at first, I suppose."
    show diego glassesdoctor happy
    sid1 "But Grace has proven to be one of the few in her profession who can distinguish between different and dangerous."
    show diego glassesdoctor basic
    sid1 "Besides, she isn't just a {i}vampire hunter{/i}- that's reductive. She's more of a... 'freelance supernatural problem solver', I believe she likes to say."
    show diego glassesdoctor happy
    sid1 "I've found she always favors words over violence."
    show ghostmc casual sarcastic at right3
    ghostmc "Thanks for clarifying, because you guys were making her sound like {i}Van Helsing{/i} for a sec, there."
    show diego glassesdoctor smirk
    sid1 "Oh, trust me, they've met. From what I've seen, your sister {i}very much{/i} likes Van Helsing."
    hide diego
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(What. Does. That. Mean!?)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(What does that mean!?)"
    "(I don't want my sister hanging around with Van Helsing! I didn't think I'd ever have to worry about that!!)"
    show ghostmc casual angry at centre
    ghostmc "I'm still not happy about this."
    show ghostmc casual sarcastic at centre
    ghostmc "How do you even become a... 'freelance supernatural problem solver'?"
    show ghostmc casual sad
    ghostmc "Grace was never a fighter, not even a little bit. What happened?"
    show ghostmc casual sad at right3
    show jd casual sad at left3
    jd "...Well, her sister was murdered, for one thing."
    show ghostmc casual surprised
    ghostmc "I mean, sure, but what does that have to do with-"
    hide jd
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Wait a second.)"
    show ghostmc casual sad at centre
    ghostmc "Who killed me?"
    show ghostmc casual sarcastic
    ghostmc "...{i}What{/i} killed me?"
    show ghostmc casual basic at right3
    show mac cop sad at left3
    sid2 "You've hit the nail right on the head."
    "Mackenzie gives me that unreadable look again, and she hesitates for just a moment before continuing."
    show mac cop angry at left3
    stop music fadeout 0.5
    pause 0.5
    play music mackenziehunt
    sid2 "Five years ago, a pair of covenless vampires entered my territory."
    show mac cop sad
    sid2 "I... I trusted them. I even allowed them to stay in town, with the understanding that the people of Havenfall weren't on the menu."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    hide mac
    "(Is she saying I was killed by those vampires?)"
    show ghostmc casual_cu sad_cu
    "(...Those vampires that she let in?)"
    show ghostmc casual basic at right3
    show mac cop sad at left3
    ghostmc "I see."
    ghostmc "Can I ask why you let them stay?"
    "Mackenzie takes a deep, shuddering breath."
    sid2 "The thing is, Havenfall was always intended to be what it sounds like, a {i}haven{/i}- in particular, for supernatural folk with nowhere else to go."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    hide mac
    "(Uh. It was?)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(That's news to me.)"
    hide ghostmc
    #show ghostmc casual basic at right3
    show mac cop sad at centre
    sid2 "Vampires without covens are particularly vulnerable- to competing vampires, and to any vampire hunters that lack Grace [genericln]'s discretion."
    sid2 "This is my territory, and that makes it my responsibility to provide that haven, without judgement or discrimination."
    show mac cop angry at centre
    sid2 "But I was just as responsible for the safety of Havenfall's people, and I made a mistake in trusting those two."
    show mac cop sad at centre
    sid2 "...That mistake got you killed, [genericfn]."
    sid2 "I'm sorry. I know it doesn't fix anything, but I am truly sorry."
    hide mac
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    if persistent.s1e2angerFlag:
        "(It's just like I told Razi- I'm angry, but I don't {i}feel{/i} angry, not physically. I have no heart to race, and there's no angry tears in the tank.)"
        show ghostmc casual_cu sarcastic_cu at hiflmc_cu
        "(There's no tank, for that matter.)"
    else:
        "(It's strange. I'm angry, I know I am- but I don't {i}feel{/i} angry, not physically. My heart isn't pounding, and my eyes aren't tearing up.)"
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(I want to be furious, to rage at the first person I can point a finger at, but I just don't think I work like that any more.)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I guess your blood can't boil if you don't have any blood to begin with.)"
    show ghostmc casual_cu sad_cu
    "(Blaming Mackenzie would be so easy, but what was she supposed to do? Turn away any vampires who need help?)"
    "(If Havenfall's really supposed to be this safe place for vulnerable supernatural folks, then that wouldn't be right, not without good reason.)"
    show ghostmc casual basic at centre
    ghostmc "Okay."
    show mac cop surprised at left3
    show ghostmc casual basic at right3
    sid2 "'Okay?'"
    sid2 "What do you mean?"
    ghostmc "I mean that I accept your apology. I..."
    show ghostmc casual sad
    ghostmc "I don't think it was really your fault, Sheriff, not entirely, not if I'm understanding it right."
    show ghostmc casual angry
    ghostmc "Sounds to me like some douchebags abused your trust, and ruined it for everyone."
    show ghostmc casual sarcastic
    ghostmc "...Well. Mostly for me and Grace, I guess."
    hide ghostmc
    show mac cop angry at centre
    "Mackenzie opens and closes her mouth a few times, her expression darkening with each false start until she looks ready to start swinging."
    sid2 "No."
    sid2 "No, you can't really mean that."
    show mac cop sad
    "Her voice, normally so steely and inflexible, cracks along the edges as she drops to a near whisper."
    sid2 "It- it {i}was{/i} my fault."
    hide mac
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Five years is a long time to carry that kind of guilt.)"
    "(I don't want anyone feeling like that because of me. Even if they could have done better. Even if I deserved for them to do better.)"
    show ghostmc casual sarcastic at centre
    ghostmc "Yeah, well, I say it wasn't." 
    show ghostmc casual angry at right3
    show mac cop surprised at left3
    ghostmc "No arguing, okay? I've forgiven you already, Mackenzie Hunt."
    ghostmc "Just take what you learned and do better next time." 
    show mac cop surprised at left3
    sid2 "I... Yes."
    show mac cop angry at left3
    sid2 "I will. I have been- I'm not making the same mistake again, I swear it."
    show mac cop happy
    sid2 "...Hearing you say that is really something, [genericfn]. Thank you."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    hide mac
    "(Did I really just give an order to a cop?)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu 
    "(...More to the point, did she really just accept that order, like it was a normal thing to do?)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Seems like dying really does a lot to boost your standing in the community.)"
    hide ghostmc
    "Everyone else has just been quietly listening to Mackenzie and I talk, and from the looks on their faces, they're pretty happy with how it shook out."
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(I wonder how many times they've all told her the exact same thing?)"
    show ghostmc casual_cu happy_cu at hiflmc_cu
    "(Probably carries a little more weight coming from me.)"
    show ghostmc casual basic at centre
    stop music fadeout 0.5
    pause 0.5
    play music getitdone
    ghostmc "Okay."
    show ghostmc casual sarcastic
    ghostmc "So, I died. I know that bit."
    show ghostmc casual basic
    ghostmc "What happened after?"
    show ghostmc casual basic at right3
    show razi casual sad at left3
    ra "In theory, we should have attempted to cover everything up."
    show ghostmc casual surprised
    ghostmc "What? Why?"
    hide razi
    show diego glassesdoctor basic at left3
    sid1 "For the same reason you're only learning about us now. When humans hear about things like vampire attacks, things get very dangerous for us."
    show ghostmc casual_cu basic_cu at hiflmc_cu
    hide diego
    "(...Something about that rubs me the wrong way, if I'm being honest.)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Not the keeping yourself safe part, but... well, it's hard not to wonder how things might have gone if I'd known a little more, that night.)"
    hide ghostmc
    show razi casual sad at centre
    ra "But it just... it didn't feel right to lie to your sister. Besides, she saw the whole thing happen."
    hide razi
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(I'd been afraid of that. She shouldn't have had to see that, not ever.)"
    show ghostmc casual sad at right3
    show razi casual sad at left3
    ra "At that point, the cat was out of the bag."
    show jd casual smirk at left3
    hide razi
    show ghostmc casual surprised at right3
    jd "Nah, I'd say the cat was fine until just after, when the four of us rolled up to your house to save her, and beat the shit out of that asshole."
    show diego glassesdoctor sad at left3
    hide jd
    sid1 "When we saw what had happened, subtlety stopped being a priority."
    show ghostmc casual sarcastic at right3
    ghostmc "I'm getting the feeling that subtlety wasn't your thing to begin with."
    hide diego
    show ghostmc casual sarcastic at centre
    ghostmc "So, you saved my sister from vampires- thanks for that, by the way-"
    show ghostmc casual sarcastic at right3
    show jd casual smirk at left3
    jd "You're welcome."
    show ghostmc casual surprised at right3
    ghostmc "And then you taught her how to fight stuff? I'm still not seeing a throughline, here."
    hide jd
    show razi casual sad at left3
    ra "Not exactly. Remember how I said a lot of things happened, after you died?"
    show ghostmc casual sad
    ghostmc "...Yeah?"
    ra "I know it doesn't make sense to think so, but losing you... I don't know. It seemed like after that, things just started to go wrong."
    ra "Stray vampires were only the start of Havenfall's problems. We've had rogue werewolves, shapeshifters, zombies-"
    show ghostmc casual surprised
    ghostmc "Zombies!?"
    hide razi
    show jd casual smirk at centre
    hide ghostmc
    "JD suddenly bites at nothing, their teeth clicking together loud enough to make me feel sorry for their dentist."
    jd "That was a fun week."
    show jd casual smirk at right3
    show razi casual angry at left3
    ra "It was absolutely not a fun week."
    hide jd
    hide razi
    show mac cop sad at left3
    show ghostmc casual surprised at right3
    sid2 "I promise, we did everything in our power to keep your sister safe- but she always seemed to get caught up in the middle of things anyway."
    show mac cop smirk
    sid2 "Eventually, she told us that enough was enough, and picked up a stake."
    show ghostmc casual happy
    ghostmc "...Okay, now {i}that{/i} sounds like her."
    ghostmc "She's always had an independent streak."
    hide mac
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I'd know. She used to fight me at every possible point, when she was younger.)"
    show ghostmc casual_cu sad_cu
    "(It must have been so galling to have her big sister become her parental figure, all of a sudden.)"
    show ghostmc casual happy at centre
    ghostmc "So, I guess she helped you fix everything?"
    show ghostmc casual happy at right3
    show mac cop sad at left3
    sid2 "Not 'helped'. She's still out there helping, right now."
    show ghostmc casual surprised
    sid2 "Things... haven't actually gotten any better. Our problems in Havenfall have mostly just been a symptom of greater upheaval."
    ghostmc "What kind of upheaval?"
    hide ghostmc
    hide mac
    show diego glassesdoctor sad at centre
    sid1 "Take your pick. Demon populations are on the rise, and cities are seeing werewolves run packless through the streets."
    hide diego
    show jd casual smirk at centre
    jd "They're chasing the demons."
    hide jd 
    show diego glassesdoctor angry at centre
    sid1 "Then there's all the infighting amongst the vampire covens- more of it than usual, anyway."
    show diego glassesdoctor smirk at centre
    sid1 "...I've also heard about a particularly unfashionable ghost who just threw the whole ghost rulebook out the window."
    show diego glassesdoctor smirk at left3
    show ghostmc casual angry at right3
    ghostmc "If you think I won't haunt you just because you did house calls, Doc, you're going to be disappointed."
    hide mac
    hide diego
    show razi casual sad at left3
    ra "Grace doesn't exactly get time to visit, anymore- there's always someone who needs her help."
    hide ghostmc
    show mac cop basic at right3
    ma "Quite frankly, that's us, right now- which is actually what I was coming to tell you, Razi, before the guest of honor showed up."
    "Razi sucks air through his teeth, face set in a wince."
    ra "Your negotiations fell through?"
    show mac cop angry at right3
    ma "She didn't even show up- Just sent another of her damned thralls as messenger, which she knows I hate."
    hide razi
    show mac cop angry at left3
    show ghostmc casual surprised at right3
    ghostmc "Woah, rewind: who are we talking about?"
    show mac cop basic at left3
    ma "...You've come at an interesting time, [genericfn]- starting to wonder if there's not a reason for it."
    ma "We've got vampire problems."
    hide mac
    hide ghostmc
    $ tobecontinued()
    show bg hifltbc at bg with fade
    pause

    $ resets()
