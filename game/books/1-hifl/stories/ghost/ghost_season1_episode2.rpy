

label ghost_season1_episode2:
    #Show your first background, and start the music here:
    $tbc = False
    scene bg bowling at bg
    play music sad
    pause
    #Pause waits for the user to click once
    #Putting nothing here means we stay on the first background when dialogue starts.

    #Leave these guys right here! Or things will get weird.
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False


    #And NOW you're free to do pretty much whatever, so long as you leave resets() at the bottom.
    $sidecharone = "Tam"
    show ghostmc bowling surprised at centre
    ghostmc "What's happening?"
    ghostmc "Why do I look like a..."
    show ghostmc bowling sad
    ghostmc "Like a..."
    hide ghostmc
    show tamara casual sad at centre
    "I can hear Tam talking up by the bar, still acting as though a person didn't just leap clear out of her body."
    sid1 "You're both kinda freaking me out, not gonna lie."
    show tamara casual sad at right3
    show jd casual sad at left3
    sid1 "JD, what's going on with you? Are you okay?"
    show tamara casual angry
    sid1 "Look, is this about that phone call? If someone's hassling you, I'll-"
    hide tamara
    hide jd
    show razi casual sad at centre
    "Razi walks around the counter, and drops down to kneel by my side."
    "He doesn't say anything- he just looks at me, eyes filled with warmth and sadness both, and he waits."
    show ghostmc bowling sad at right2
    show razi casual sad at left2
    ghostmc "Guess you can still see me, huh?"
    ra "I can. You're not alone."
    ghostmc "Please help me, Razi. I don't understand."
    ra "I know. And I will."
    show razi casual happy
    ra "Everything's going to be okay."
    hide razi
    hide ghostmc
    "And then Razi does what he always does when I'm having a bad day."
    "He gives me one of those big, warm hugs. The kind that always seem to fix everything, at least for a little while."
    hide ghostmc
    hide razi
    show bg insideperson
    $renpy.sound.play("audio/sfx/general/heartbeat1.wav", loop=True)
    "He tries to."
    stop sound
    show bg bowling at bg
    show razi casual surprised at left2
    show ghostmc bowling surprised at centre
    show ghostmc bowling at right2 with ease
    ghostmc "No!"
    ra "[genericfn]!"
    show razi casual sad 
    ra "It's- it's alright. You're okay-"
    show ghostmc bowling angry
    ghostmc "No, I'm not!"
    hide razi
    show ghostmc bowling_cu angry_cu at hiflmc_cu
    "(Everything was fine before I came to work!)"
    show ghostmc bowling_cu sad_cu
    "(I just... I just need to go home.)"
    show ghostmc bowling_cu basic_cu
    "(Yeah. I'll go to bed, and sleep it off. No problem.)"
    hide ghostmc
    "I get to my feet, wobbling uncertainly as I do- my body doesn't feel right, like there's no real weight to it."
    show ghostmc bowling_cu surprised_cu at hiflmc_cu
    "(How did I not notice that before?)"
    hide ghostmc
    show razi casual surprised at centre
    "Razi comes up with me, hands hovering anxiously, but never touching."
    hide razi
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(...Because he actually can't touch me.)"
    hide ghostmc
    "As I head to the door, I hear Razi call after me."
    show razi casual sad at centre
    ra "[genericfn], please- don't leave."
    "He doesn't make any move to follow me any farther than that."
    hide razi
    show ghostmc bowling sad at centre
    "I reach the door, and grab the handle."
    ghostmc"..."
    show ghostmc bowling surprised
    "No, I grab air. I watch with equal parts horror and fascination as my hand slips right through the solid metal."
    show ghostmc bowling sad
    ghostmc "No, come on."
    ghostmc "Please..."
    "I try again and again, no matter how many times I try, I can't make the handle move even an inch."
    show ghostmc bowling angry
    ghostmc "Fuck!" 
    ghostmc "Let me out!"
    show ghostmc bowling_cu angry_cu at hiflmc_cu
    "(This is so stupid! I got {i}in{/i} here, didn't I?)"
    hide ghostmc
    show jd casual surprised at centre
    "Suddenly JD's there, and without a word, they carefully reach around me to push on the door handle."
    show ghostmc bowling_cu surprised_cu at hiflmc_cu
    hide jd
    "(It opens just fine, for them!)"
    show jd casual surprised at left3
    show ghostmc bowling surprised at right3
    ghostmc "..."
    show ghostmc bowling angry at right3
    ghostmc "Whatever."
    hide ghostmc
    hide jd
    stop music fadeout 0.5
    pause 0.5
    play music hifleveryday
    show bg main_day
    "I storm out into the main street, and the warm light of day makes things feel a little more normal, if not better."
    show ghostmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Even if I can't actually feel that warmth.)"
    show ghostmc bowling_cu angry_cu
    "(For some reason.)"
    show jd casual surprised at centre
    hide ghostmc
    jd "[genericfn]! Wait up!"
    show jd casual surprised at left3
    show ghostmc bowling angry at right3
    ghostmc "Go away, JD."
    hide jd
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(Intellectually, I know this- whatever this is- isn't JD's fault, or Razi's, or even Tam's.)"
    show ghostmc bowling_cu angry_cu
    "(Emotionally, I want them all to leave me the hell alone until I've had a chance to think.)"
    show jd casual angry at centre
    hide ghostmc
    "JD's boots do stop clomping along behind me, but when I stop to glance over my shoulder, their owner doesn't look happy about it."
    jd "At least tell me where you're going!"
    show ghostmc bowling angry at right3
    show jd casual angry at left3
    ghostmc "I'm going home."
    show ghostmc bowling sarcastic
    ghostmc "I'm gonna go to sleep. I'll wake up when things make sense again."
    show jd casual surprised
    jd "They're not going to!"
    show jd casual angry
    jd "Look, [genericfn], I know this sucks hard, but it's something you have to deal with."
    show ghostmc bowling angry
    ghostmc "Oh, like how you were 'dealing with it'?"
    show ghostmc bowling sarcastic
    ghostmc "Should I start treating people like garbage for no reason?"
    show jd casual sad
    jd "..."
    show ghostmc bowling sarcastic
    ghostmc "That's right. I'm going..."
    hide ghostmc
    hide jd
    "I spin around to locate my truck, but..."
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(To be honest, I haven't got a single clue where I parked it.)"
    hide ghostmc
    "Then I spot the diner, and my blood runs cold."
    show ghostmc bowling_cu surprised_cu at hiflmc_cu
    "(Grace!)"
    hide ghostmc
    "..."
    show ghostmc bowling_cu happy_cu at hiflmc_cu
    "(Of course. I just need to go talk to my sister- {i}that's{/i} what I'm missing.)"
    show ghostmc bowling happy at centre
    ghostmc "Actually, scratch that- I'm going to Luce's."
    show ghostmc bowling happy at right3
    show jd casual surprised at left3
    jd "You're hungry? Can you even eat?"
    show ghostmc bowling angry
    ghostmc "What's that supposed to-"
    show ghostmc bowling sarcastic
    ghostmc "Look, I'm not going for lunch, JD, I'm going to talk to Grace."
    jd "Grace? But she's-"
    show ghostmc bowling sad
    ghostmc "Just... Go back inside and help the new girl, okay? And tell Razi I'm sorry about ditching."
    ghostmc "I guess I'm taking a sick day."
    show jd casual sad
    jd "...Yeah. Okay."
    hide jd
    hide ghostmc
    "I almost regret sending them off once I approach the diner, finding another closed door in my way."
    show ghostmc bowling angry at centre
    "I try my luck with this one, too, but after a few minutes of cursing- and no sweating whatsoever- I'm no closer to getting inside the building."
    show ghostmc bowling surprised at right3
    show girl1 casual angry at centre
    "Fortunately, one of the teens I saw on the street earlier comes to my rescue, almost blowing the door clean off its hinges as she storms out."
    hide girl1
    show ghostmc bowling_cu sarcastic_cu at hiflmc_cu
    "(From the bowling alley, to the diner, then back to the bowling alley.)"
    "(Havenfall is just packed full of excitement for the kids.)"
    hide ghostmc

    show bg diner_lights_on at bg
    show luce casual angry at centre
    with dissolve
    "Luce herself is at the counter as I sidle past the girl, and she's wearing a heavy frown as she rummages through the till."
    hide luce
    "Grace is nowhere to be seen."
    show ghostmc bowling_cu basic_cu at hiflmc_cu
    "(Which is okay.)"
    "(Completely okay. She's just in the back.)"
    show luce casual basic at right3
    show ghostmc bowling basic at left4
    ghostmc "Hey, Luce."
    ghostmc "Is it okay if I borrow Grace for a sec?"
    "Luce keeps sorting through the morning's earnings, not even sparing me a glance."
    $sidecharone = "Luce"
    sid1 "...twenty, thirty, forty..."
    show ghostmc bowling sad
    ghostmc "...Luce?"
    show ghostmc bowling surprised
    show luce casual angry at right3
    "She tsks in disapproval, which is probably the first normal reaction I've gotten today."
    hide luce
    show ghostmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Luce is always tsking about Grace and I.)"
    hide ghostmc
    show luce casual angry at centre
    "That tiny ember of hope is dashed when she just sighs, and starts to mutter despondently to herself."
    sid1 "Damn it all."
    sid1 "All these new weirdos in town, and none of them want to buy a fucking burger."
    show luce casual angry at right3
    show ghostmc bowling angry at left4
    ghostmc "Try using salt!"
    show ghostmc bowling sarcastic at left4
    ghostmc "Look, I'm gonna go back and talk to my sister. I won't touch anything."
    hide luce
    show ghostmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Not for lack of trying.)"
    show luce casual angry at centre
    hide ghostmc
    "Luce doesn't raise any objections, which I decide counts as implicit permission, at the very least."
    hide luce
    "The door into the back room is always wedged open, so I can just walk right in without having to think about it too much."
    "There's only one person inside, busily unpacking various cans of sauce from a cardboard box."
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(...Another person I don't recognise.)"
    "(Why isn't Grace here?)"
    show ghostmc bowling_cu surprised_cu at hiflmc_cu
    "(Where's my sister!?)"
    hide ghostmc
    #show luce casual basic at left4
    sid1 "Well, now, if it isn't Razi Nassar!"
    show luce casual basic at right3
    show razi casual happy at left4
    "I return to the front of the diner in a daze, to find a smiling Razi standing opposite Luce at the counter."
    show razi casual sad
    hide luce
    show ghostmc bowling sad at right3
    "His smile flickers a little when he spots me drifting out behind her, but only for the briefest of moments."
    hide ghostmc
    hide razi
    show luce casual basic at centre
    sid1 "Not often I see you in here- What can I get you?"
    show luce casual basic at right3
    show razi casual smirk at left4
    ra "Luce, I must confess- I've been laying awake at night thinking about your coffee."
    sid1 "Changed your mind, have you?"
    show luce casual angry
    sid1 "What was it you told the Sheriff last time you were here...? \"Tastes like piss\", I think?"
    show razi casual smirk
    ra "Why, that was but a ruse- I was hoping she'd give me hers."
    show luce casual basic
    sid1 "Your fancy coffee machine's broken, huh?"
    show razi casual sad
    ra "I haven't had a cup in three days. I'll beg if I must."
    sid1 "Oh, go sit down, you big drama queen. I'll get your coffee."
    show razi casual happy
    ra "You're a treasure, Luce."
    show razi casual basic
    hide luce
    show ghostmc bowling sad at right3
    "Razi shoots me a significant look, then nods towards one of the booths, the farthest one from the counter."
    hide razi
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(...Yeah, okay. Maybe JD was right- it's time I stopped running from this.)"
    show ghostmc bowling_cu basic_cu at hiflmc_cu
    "(Razi can see me, unlike Tam and Luce, so I'm willing to bet that means he knows a few things I don't.)"
    "(If nothing else, I know he'll help me look for Grace.)"
    show ghostmc bowling sad at right3
    show razi casual sad at left3
    "I take the seat opposite Razi, and we just kinda... look at each other, for a moment."
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    hide razi
    "(What do you even say?)"
    show ghostmc bowling sad at right3
    show razi casual sad at left3
    ra "How are you feeling?"
    $menuhideborder = True
    hide razi
    hide ghostmc
    menu ge2c1:
        #"A. Yes" (paidchoice = "paidchoice"):
        "1. Bad.":
            $ persistent.s1e2angerFlag = False
            $ persistent.s1e2tamFlag = False
            $menuhideborder = False
            show ghostmc bowling sad at right3
            show razi casual sad at left3
            ghostmc "It's kinda like I'm stuck in a nightmare."
            show ghostmc bowling sarcastic at right3
            ghostmc "Except, you know, instead of waking up when something awful happens, something even more awful happens."
            ra "...That sounds rough."
            show ghostmc bowling angry at right3
            ghostmc "I'm late for work, then JD's pissed at me for no reason, then someone sits on me..."
            show ghostmc bowling basic at right3
            ghostmc "Yes. I think I'm having a rough day."
        "2. I don't know.":
            $ persistent.s1e2angerFlag = True
            $ persistent.s1e2tamFlag = False
            $menuhideborder = False
            show ghostmc bowling sad at right3
            show razi casual sad at left3
            ghostmc "A lot's happening really fast, and none of it makes sense, you know?"
            ra "I can imagine."
            ghostmc "I'm so scared, but I don't {i}feel{/i} scared, not- not physically. I'm not breathing hard. My heart isn't racing."
            ghostmc "...I don't even think I have a heartbeat."
        "3. Don't ask.":
            $ persistent.s1e2angerFlag = False
            $ persistent.s1e2tamFlag = True
            $menuhideborder = False
            show razi casual sad at left3
            show ghostmc bowling angry at right3
            ghostmc "Don't ask me that."
            ghostmc "If I could pick up a pen, I'd fill a whole book with the feelings I'm having right now."
            show ghostmc bowling sarcastic at right3
            ghostmc "Nobody would want to read it because of the chapter where I talk about the squishy parts inside that Tam girl's head."
            show razi casual smirk
            ra "Tamara certainly would."
            
    show ghostmc bowling sad
    ghostmc "What's happening to me, Razi?"
    show razi casual sad
    "Razi hesitates."
    show ghostmc bowling surprised
    ra "Are you asking me because you don't know, or because you do know, but don't want it to be true?"
    show ghostmc bowling sad
    stop music fadeout 0.5
    pause 0.5
    play music sad
    ghostmc "..."
    ghostmc "How did I die?"
    hide ghostmc
    show razi casual sleep at centre
    "Razi closes his eyes, and takes a deep, unsteady breath."
    show razi casual sad at centre
    ra "[genericfn]... you were murdered."
    hide razi
    show ghostmc bowling_cu surprised_cu at hiflmc_cu
    "(Murdered?)"
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(No. No, that's not possible.)"
    hide ghostmc
    show razi casual sad at centre
    "I guess Razi can read the disbelief on my face, because he shakes his head urgently."
    ra "No, please, just listen- It's true. I wouldn't lie to you, you know that."
    hide razi
    show ghostmc bowling_cu sad_cu at hiflmc_cu
    "(...I do know that.)"
    hide ghostmc
    show razi casual angry
    "His expression darkens."
    ra "This guy, he... he pulled a rotten trick, got you out of the house alone- and then-"
    show razi casual surprised at left3
    show ghostmc bowling surprised at right3
    ghostmc "The letter!"
    hide ghostmc
    hide razi
    show ghostmc bowling_cu surprised_cu at hiflmc_cu
    "(Oh my god, it was {i}actually{/i} a trap!)"
    show ghostmc bowling_cu angry_cu
    "(If I ended up on an episode of \"Backwater Murders\" I'm going to do so much goddamn haunting.)"
    show razi casual basic
    hide ghostmc
    ra "...What do you remember?"
    show razi casual basic at left3
    show ghostmc bowling basic at right3
    ghostmc "Not a lot. It's all a little fuzzy."
    show razi casual surprised
    show ghostmc vestlesscasual basic with dissolve
    ghostmc "Someone left a letter on the front porch."
    show ghostmc vestlesscasual sad
    ghostmc "I thought it was- I {i}knew{/i} it was sketchy, but then it started to rain, and I thought it might be important, and..."
    show razi casual sad
    ghostmc "..."
    show ghostmc vestlesscasual angry
    ghostmc "Ugh!"
    ghostmc "That was so fucking stupid." 
    show razi casual sad
    ra "[genericfn], it wasn't your fault. Please, don't blame yourself for-"
    ghostmc "Like hell, it wasn't! It's my {i}job{/i} to stay safe, so I can look after-"
    hide razi
    hide ghostmc
    "Another awful puzzle piece falls into place."
    show ghostmc vestlesscasual_cu surprised_cu at hiflmc_cu
    hide razi
    "(Oh, god.)"
    "(Grace was with me.)"
    show razi casual sad at left3
    show ghostmc vestlesscasual surprised at right3
    ghostmc "Razi, where's Grace?"
    show ghostmc vestlesscasual sad
    ghostmc "She- she was there, and I don't know where she is. Please, don't tell me-"
    show razi casual happy
    ra "No, Grace is just fine, [genericfn]. I can promise you that."
    show razi casual smirk
    ra "Your sister is, no exaggeration whatsoever, the toughest person I've ever met."
    hide razi
    show ghostmc vestlesscasual sleep at centre
    "A weight I didn't even realize I'd been carrying is lifted off my shoulders."
    "I take a deep breath, only stopping when I discover there's not actually a limit to just how deep that can be, since I apparently have no lungs."
    show ghostmc vestlesscasual_cu basic_cu at hiflmc_cu
    "(I think I've been worried about what happened to her that night since I first woke up, even if I didn't really know it.)"
    show ghostmc vestlesscasual_cu basic_cu at hiflmc_cu
    "(I'm still confused, and I guess my memories are all over the place- but Grace is okay.)"
    show razi casual happy at left3
    show ghostmc vestlesscasual basic at right3
    ghostmc "Good. Okay. That's good."
    ghostmc "Do you know where she is? I thought I drove her to work, like I always do, but..."
    hide razi
    hide ghostmc
    show luce casual angry at centre
    "I look over to the counter, where Luce is busy fussing over Razi's coffee."
    hide luce
    show razi casual basic at left3
    show ghostmc vestlesscasual basic at right3
    ghostmc "Well, she's not here."
    show ghostmc vestlesscasual sarcastic
    ghostmc "And now that I'm thinking about it, I'm not actually sure how I drove my truck here in the first place."
    show razi casual sad
    ra "I'm... fairly certain you didn't."   
    ra "Ghosts can teleport, and you don't even have to be a ghost to convince yourself of things that didn't happen."
    hide razi
    show ghostmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(They can?)"
    show ghostmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(And Razi is a ghost expert... how?)"
    show ghostmc vestlesscasual basic at right3
    show razi casual basic at left3
    ra "As for where Grace is..."
    show razi casual sad
    ra "[genericfn], you have to understand, you... you didn't just die yesterday. It's been a while."
    hide razi
    show ghostmc vestlesscasual_cu sad_cu at hiflmc_cu
    "(Figures. JD did say it'd been \"too long\" for me to be a ghost.)"
    show ghostmc vestlesscasual_cu sarcastic_cu
    "(Another person who talks about ghosts like they're common knowledge.)"
    show ghostmc vestlesscasual_cu angry_cu
    "(Little punk was holding out on me. They knew about ghosts, and never told me? Being into crap like that is my whole thing!)"
    show ghostmc vestlesscasual sad at right3
    show razi casual basic at left3
    ghostmc "...How long?"
    show razi casual sad
    ra "It'll be five years next month."
    hide razi
    hide ghostmc
    "It might have hurt a little less for Razi to just straight up punch me in the face- not that he would, or even could."
    show razi casual sad at centre
    "The worst part is, from the pitying look he's giving me, he knows it."
    hide razi
    show ghostmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(Almost five years...)"
    show ghostmc vestlesscasual_cu sad_cu at hiflmc_cu
    "(That'd make Grace my age.)"
    "(She's a real adult now, and I didn't even get to see it happen.)"
    hide ghostmc
    show razi casual basic at centre
    "When I finally manage to look up at Razi, he's idly stirring a cup of Luce's awful coffee, making no moves to actually drink it."
    hide razi
    show luce casual angry at centre
    "Luce clearly made good on her promise at some point, and is now back at her station, shooting suspicious glances our way."
    hide luce
    show ghostmc vestlesscasual sad at centre
    ghostmc "Did... did she at least get to go to college?"
    #hide ghostmc
    "My voice comes out as barely more than a whisper. It sounds how I feel- small, sad, and utterly helpless."
    show ghostmc vestlesscasual_cu sad_cu at hiflmc_cu
    "(Another question I'm asking even though I already know the answer.)"
    "(After Grandma died, it was just us. Grace didn't have anyone to rely on but me.)"
    "(It was already going to be a struggle to put her through college, even after she picked up work.)"
    show ghostmc vestlesscasual_cu sarcastic_cu
    "(If she was even able to pay bills and stay fed on just whatever crappy jobs she could pick up around here, that's a miracle in itself.)"
    show ghostmc vestlesscasual sad at right3
    show razi casual sad at left3
    ra "...No. A lot happened, after you died."
    ra "College was never in the cards."
    ghostmc "That was all I ever wanted, Razi."
    show ghostmc vestlesscasual angry
    ghostmc "Grace was supposed to- she was going to go to college, get out of this town and live her goddamn life."
    hide ghostmc
    hide razi
    show ghostmc vestlesscasual_cu sad_cu at hiflmc_cu
    "(Like... like I wanted to, before everything went wrong.)"
    show razi casual happy at left3
    show ghostmc vestlesscasual sad at right3
    ra "But that's what I'm trying to tell you, [genericfn]- Grace {i}did{/i} get out of town."
    show ghostmc vestlesscasual surprised at right3
    ghostmc "She did?"
    ghostmc "So she's not even- where is she?"
    ra "Grace isn't just living her life, she's thriving in it."
    show razi casual smirk
    ra "Dream job and everything. Like I said, the woman's tough as nails."
    show ghostmc vestlesscasual surprised
    ghostmc "She's an actress?"
    show razi casual surprised
    ra "What?"
    show razi casual happy
    ra "No, her- well, okay, so maybe her dreams changed a little."
    show razi casual sad
    ra "...They changed a lot, actually."
    show razi casual basic
    ra "But the point is, she loves what she does now."
    ra "She's good at it- scary good- and she makes a real difference in the world."
    show razi casual happy
    ra "She's happy."
    show ghostmc vestlesscasual basic
    ghostmc "Happy..."
    hide razi
    show ghostmc vestlesscasual_cu basic_cu at hiflmc_cu
    "(That's the important thing, right? Even if she didn't get to college, if she's happy, then...)"
    show ghostmc vestlesscasual happy at centre
    stop music fadeout 0.5
    pause 0.5
    play music hifleveryday
    ghostmc "Thanks, Razi."
    ghostmc "I actually feel way better."
    show razi casual smirk at left3
    show ghostmc vestlesscasual happy at right3
    ra "I thought you might."
    show ghostmc vestlesscasual sarcastic
    ghostmc "I mean, I'm still dead."
    ghostmc "And apparently I'm cursed to forever wear your stupid..."
    hide razi
    show ghostmc vestlesscasual_cu surprised_cu at hiflmc_cu
    "(Wait, what the heck? I'm like 300\% sure I was wearing the bowling alley uniform when I walked in here.)"
    show ghostmc vestlesscasual_cu sarcastic_cu
    "(I don't even know {i}how{/i} I'd change.)"
    hide ghostmc
    show razi casual happy at centre
    "Razi sees me goggling at my shirt, and laughs."
    ra "You did that."
    show ghostmc vestlesscasual surprised at right3
    show razi casual happy at left3
    ghostmc "I did? When? How?"
    show razi casual smirk
    ra "Just now, while we were talking. You didn't even realize you were doing it, did you?"
    ra "You're lucky, you know."
    show ghostmc vestlesscasual basic
    ghostmc "..."
    ghostmc "Am I, now."
    hide ghostmc
    show razi casual surprised at centre
    "There's no real heat in the words, but Razi winces like I'm winding up to slap him."
    ra "No, I didn't mean-"
    show razi casual sad
    "He sighs."
    ra "...Sorry."
    show razi casual basic
    ra "All I meant to say is that ghosts aren't known for changing their outfits on a whim."
    show razi casual sad 
    ra "I think if they could, you'd see fewer of them with bloodstains."
    show razi casual basic
    hide razi
    show ghostmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(So I'm not just a ghost, I'm a weird ghost.)"
    show ghostmc vestlesscasual_cu happy_cu at hiflmc_cu
    "(Eh, whatever. Not gonna complain about getting out of the uniform.)"
    show ghostmc vestlesscasual basic at right3
    show razi casual basic at left3
    ghostmc "Speaking of what ghosts can and can't do:"
    show ghostmc vestlesscasual sarcastic at right3
    ghostmc "Care to explain to me why you and JD are apparently Havenfall's resident ghost experts?"
    show ghostmc vestlesscasual angry at right3
    ghostmc "And why nobody thought to mention them to me?"
    show razi casual smirk
    ra "I can do one better than that."
    "Razi gets to his feet, and slaps a twenty on the table to pay for his untouched coffee."
    hide razi
    show ghostmc vestlesscasual_cu sarcastic_cu at hiflmc_cu
    "(Oh, Luce'll love that.)"
    hide ghostmc
    show razi casual happy at centre
    ra "We should head back to the bowling alley- there's a few folks there who'll be very happy to see you."
    show ghostmc vestlesscasual sarcastic at right3
    show razi casual happy at left3
    ghostmc "Assuming they {i}can{/i} see me."
    show razi casual smirk
    ra "I can, can't I?"
    hide razi
    hide ghostmc

    $tobecontinued()

    show bg hifltbc with fade
    pause
    $ resets()
