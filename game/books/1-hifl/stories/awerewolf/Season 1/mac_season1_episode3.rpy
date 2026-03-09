##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode3:
    $tbc = False

    ##Change these to suit the story
    scene bg bowling at bg
    play music hiflgetitdone

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show hiflmc beaniecasual_cu angry_cu at hiflmc_cu
    "(The best defense is a good offense. I'm getting to the bottom of this.)"
    show hiflmc beaniecasual angry at left4
    show mac glassescop angry at right4
    mcmac "Are you going to tell me what's really going on?"
    mcmac "Don't tell me it's nothing. I heard enough."
    show razi casual sad at right4
    hide mac
    ra "[genericfn]-!"
    mcmac "Not you, Razi."
    hide razi
    show mac glassescop surprised at right4
    mcmac "Her. Mackenzie."
    show mac glassescop basic at right2
    "She takes slow steps forward, breaking the distance between us, but everyone else takes a half-step back."
    "It's not the way Mackenzie was on the full moon--on the prowl--but there's a reason she keeps this town in line."
    ma "Do you remember what I said to you?"
    "Green eyes do a quick scan of the room before her voice drops low."
    hide hiflmc
    show mac glassescop_cu basic_cu at mac_cu
    ma "About keeping my secret?"
    hide mac
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    mcmac "But they... know."
    mcmac "I just heard you tell them."
    show hiflmc beaniecasual_cu surprised_cu at hiflmcleft_cu
    show mac glassescop_cu basic_cu at macright_cu behind hiflmc
    "Mackenzie holds my gaze for a long moment, jaw tensing, and I'm lost for a moment."
    "She's so close and I don't know what she wants."
    "All I can do is guess and figure it out later."
    show hiflmc beaniecasual_cu basic_cu at hiflmc_cu
    hide mac
    mcmac "Okay. I will."
    hide hiflmc
    show mac glassescop_cu basic_cu at mac_cu
    ma "Good."
    ma "I am a werewolf."
    ma "And before you ask, yes, I've always been one. I was born this way."
    hide mac
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "Hearing the truth right from her shakes me, and I look around to everyone else, waiting for them to show some sort of surprise."
    "(This can't be totally normal to them, right? Unless-!)"
    show hiflmc beaniecasual surprised at centre
    hide mac
    mcmac "Are the rest of you werewolves too?"
    show hiflmc beaniecasual surprised at right4
    show jd tank angry at left4
    jd "Hell no."
    show mac glassescop smirk at right4
    hide hiflmc
    ma "Yeah, because your situation is so much better than mine."
    hide mac
    hide jd
    show razi casual smirk at left4
    show diego doctor glassessmirk at right4
    "Diego and Razi both laugh, exchanging a look that I don't understand."
    hide diego
    show hiflmc beaniecasual basic at right4
    ra "No, I'm not a werewolf. Just... different."
    hide hiflmc
    show diego doctor glassessmirk at right4
    di "Inhuman is one term, although not everyone finds that to be polite."
    hide diego
    hide razi
    show hiflmc beaniecasual surprised at centre
    "I pinch myself real quick, just in case. Nothing changes."
    show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
    "(Damn it.)"
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "(So if they're not werewolves, what are they?)"
    $menuhideborder = True
    hide hiflmc
    menu mace3c1:
        #"A. Yes" (paidchoice = "paidchoice"):
        "1. Ask Razi.":
            $menuhideborder = False
            show hiflmc beaniecasual basic at right4
            show razi casual basic at left4
            mcmac "What kind of different are you, boss?"
            show razi casual smirk
            ra "You probably won't believe me."
            show hiflmc beaniecasual sarcastic
            mcmac "At this rate, I'd believe the sky is purple."
            show hiflmc beaniecasual surprised
            ra "I'm a Djinn. Please don't say genie."
            hide razi
        "2. Look at Diego":
            $menuhideborder = False
            show hiflmc beaniecasual basic at right4
            show diego glassesdoctor basic at left4
            mcmac "Inhuman could mean a lot of things."
            show diego glassesdoctor sleep at left4
            di "Since we seem to be spilling secrets by the bucketfull, today..."
            show hiflmc beaniecasual surprised
            show diego glassesdoctor vampirebasic at left4 with dissolve
            di "I'm a vampire."
            show hiflmc beaniecasual sarcastic
            mcmac "You have GOT to be kidding me."
            hide diego
        "3. Poke JD.":
            $menuhideborder = False
            show hiflmc beaniecasual basic at right4
            show jd tank basic at left4
            mcmac "Give it up, JD. If you're not a werewolf, you are..."
            show jd tank surprised
            jd "Seriously?"
            show hiflmc beaniecasual basic at right4
            mcmac "Yeah, seriously."
            show jd tank basic
            jd "I'm a devil. From a couple of states over."
            hide jd
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "(I've known these people my whole life.)"
    "(It's not like we're all close, but I've seen them at the grocery store.)"
    "(We all show up to see fireworks on the 4th together!)"
    show hiflmc beaniecasual surprised at centre
    mcmac "Wow. Okay."
    show hiflmc beaniecasual sarcastic
    mcmac "Is this the part where I'm inducted into some weird monster cult?"
    show hiflmc beaniecasual basic
    mcmac "Or do you guys just like hanging out together?"
    show hiflmc beaniecasual basic at right4
    show mac glassescop basic at left4
    ma "It's a small town, [genericfn]. Not a lot of information leaves."
    ma "Everyone knows everyone. Trusts everyone."
    hide mac
    show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
    "(Kind of. My neighbours don't even seem to trust my sister.)"
    show hiflmc beaniecasual angry at right4
    show mac glassescop basic at left4
    mcmac "Then everyone should be helping me find Grace."
    mcmac "She's gone, and if none of you did it, I don't know who did."
    show mac glassescop sad at left4
    ma "Of course I'll help you."
    ma "Honestly, if my suspicions are right, I may be the only one who can."
    show hiflmc beaniecasual basic at right4
    hide mac
    show razi casual smirk at left4
    ra "I'd bet on that. Mac's the best tracker among us."
    show diego doctor glassessmirk at left4
    hide razi
    di "Unless there's blood involved."
    hide hiflmc
    show mac glassescop smirk at right4
    ma "I don't think we've ever had that competition, Diego, but I don't think I'd want to."
    di "Fair enough."
    hide mac
    hide diego
    show jd tank basic at left4
    show hiflmc beaniecasual basic at right4
    jd "Yeah, finding people is not what I do."
    show jd tank happy
    jd "But if you round up someone involved, give me a ring. They'll talk."
    show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
    hide jd
    "(That's... comforting. In a weird 'my life is kinda pulling apart at the seams' kind of way.)"
    hide hiflmc
    show mac glassescop_cu basic_cu at mac_cu
    "Mackenzie puts both hands on my shoulders, looking me in the eye."
    "I try to see the wolf in her again, to make sense of this, but there's nothing but her warm strength to read."
    show mac glassescop_cu basic_cu
    ma "I will find her, [genericfn]. I promise."
    hide mac
    show hiflmc beaniecasual_cu happy_cu at hiflmc_cu
    mcmac "Thank you."
    mcmac "Guess I'm in deep now, huh?"
    hide hiflmc
    show razi casual basic at left4
    show jd tank basic at centre
    show diego doctor glassesbasic at right4
    ra "You can talk about our...backgrounds...with anyone here, but otherwise it has to be a secret."
    show razi casual smirk
    ra "No passive aggressive posts on social media either, please."
    hide razi
    hide jd
    hide diego
    show hiflmc beaniecasual happy at centre
    mcmac "Yeah, I bet the internet made everything a little more complicated, didn't it?"
    show hiflmc beaniecasual happy at right4
    show diego doctor glassesbasic at left4
    di "That is an understatement."
    hide diego
    show razi casual basic at raziline1
    show jd tank basic at jdline1
    show diego doctor glassesbasic at diegoline1 behind hiflmc
    show hiflmc beaniecasual basic at hiflmcline1
    mcmac "Don't worry. Your secrets are safe with me."
    hide jd
    hide razi
    hide hiflmc
    hide diego
    scene bg hifl_sheriff at bg with fade
    stop music fadeout 1
    play music hifleveryday
    show hiflmc beaniecasual basic at right4
    show mac glassescop basic at left4
    "Mackenzie has me follow her back to the sheriff's office."
    "Her desk is the neatest of the bunch, but there's a fresh manila folder on it with my sister's name written on the tab."
    show hiflmc beaniecasual sad
    "She sets Grace's phone out for both of us to see, and my heart hurts a little when I stare at the charm on it."
    hide mac
    show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
    "(I'll bring you home soon, sis.)"
    show hiflmc beaniecasual basic at right4
    show mac glassescop basic at left4
    mcmac "Why did you take this out of the evidence bag?"
    ma "To clean it, first and foremost."
    show mac glassescop sad
    ma "Not exactly procedure, but we're working a little off the books here, already."
    show mac glassescop happy
    ma "But I was also hoping you could unlock it for me."
    show hiflmc beaniecasual surprised
    mcmac "Oh, sure."
    show hiflmc beaniecasual_cu happy_cu at hiflmc_cu
    hide mac
    "(Her code is my birthday, and mine is hers. Not exactly airtight security, but it's easy to remember.)"
    show hiflmc beaniecasual basic at centre
    "The first thing that pops up is my text. I dismiss the notification and go back to right after her shift."
    "There's a chain of messages, all from an unknown number."
    show hiflmc beaniecasual angry
    "They start out friendly, but I'm immediately on edge."
    show hiflmc beaniecasual angry at right1plus
    show mac glassescop basic at left1plus
    ma "'I know I shouldn't be texting you while you're working but'..."
    ma "But they did it anyway. Wonder why Grace forked over her number."
    show hiflmc beaniecasual sad
    mcmac "She's always had a really hard time making friends."
    mcmac "If someone offered to swap, she'd probably take them up on it."
    ma "Says here they planned to pick her up after her shift."
    mcmac "Yeah, but Luce let Grace go a little early. That's why I wasn't there in time."
    mcmac "But then..."
    show hiflmc beaniecasual basic
    mcmac "Grace agrees, but tells them she doesn't want to be home late."
    show hiflmc beaniecasual_cu angry_cu at hiflmc_cu
    hide mac
    "(I knew it! She'd never spend the night somewhere else, not without telling me.)"
    show hiflmc beaniecasual surprised at right1plus
    show mac glassescop basic at left1plus
    mcmac "That's suspicious, right?"
    show mac glassescop angry at left1plus
    ma "Very."
    ma "I never spent a lot of time with Grace, but that's because she's a good girl."
    show hiflmc beaniecasual basic
    ma "Never caused trouble."
    ma "The fact that she didn't even text you back tells me she'd already lost her phone by then."
    hide mac
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "(But why at the lake? What's there that was important?)"
    show hiflmc beaniecasual angry at right1plus
    show mac glassescop basic at left1plus
    mcmac "It has to have something to do with this guy."
    ma "The flirty one in the jacket, right?"
    mcmac "Yeah."
    show hiflmc beaniecasual sarcastic
    mcmac "Newcomers always stand out in a place like this."
    hide mac
    show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
    "(Rude or not, I can't imagine any of my neighbours doing something to hurt Grace.)"
    show hiflmc beaniecasual_cu sarcastic_cu
    "(They don't care enough to bother.)"
    show hiflmc beaniecasual basic at right1plus
    show mac glassescop basic at left1plus
    ma "Yeah, they do."
    ma "Now the question is what his motive would be."
    show hiflmc beaniecasual sad
    "I don't really want to think about all those possibilities, but I know Mackenzie has to."
    "This isn't her first case, not by far."
    show hiflmc beaniecasual basic
    mcmac "I have a different question."
    mcmac "Are we sure he's human?"
    show mac glassescop surprised
    show hiflmc beaniecasual surprised
    "Mackenzie raises a brow, and a nervous jolt goes down to the pit of my stomach before I glance around, confirming we're alone."
    show hiflmc beaniecasual sad
    mcmac "Sorry."
    show mac glassescop basic
    ma "Just be more careful next time."
    "I expected a harder slap on the wrist, and it makes me wonder why she's treating me with kid gloves."
    hide mac
    show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
    "(Is it because she knows I'm freaking out about Grace?)"
    "(Or because I figured out she's a werewolf?)"
    show hiflmc beaniecasual_cu surprised_cu
    "(I mean...what other reason would there be?)"
    show hiflmc beaniecasual basic at right1plus
    show mac glassescop sleep at left1plus
    ma "And to answer your question, no, I'm not sure."
    show mac glassescop sad
    ma "It's not always so easy to tell."
    $menuhideborder = True
    hide hiflmc
    hide mac
    menu mace3c2:
        #"A. Yes" (paidchoice = "paidchoice"):
        "1. Be more insistent.":
            $menuhideborder = False
            show hiflmc beaniecasual surprised at right1plus
            show mac glassescop basic at left1plus
            mcmac "There has to be some way. Razi said you were a good tracker."
            show mac glassescop angry
            ma "I am."
            show mac glassescop basic
            ma "But we wouldn't have stayed hidden for so long if it was that easy to pick us out of a crowd."
        "2. Try to encourage her.":
            $menuhideborder = False
            show hiflmc beaniecasual happy at right1plus
            show mac glassescop basic at left1plus
            mcmac "I know you'll figure it out. You've always kept us safe before."
            show mac glassescop happy
            ma "That's my job. I'm not about to lay it aside now."
    show hiflmc beaniecasual basic
    show mac glassescop sad
    "Mackenzie takes the phone from me and scrolls to the very last text message."
    "At the bottom is an offer from the stranger to go to a haunted house, daring Grace to be brave enough."
    show hiflmc beaniecasual surprised
    "And she said yes."
    mcmac "Haunted house?"
    ma "An abandoned place, I'd guess. There's only one of those in the town limits."
    ma "We should get down there ASAP."

    scene bg main_night at bg with fade
    show hiflmc beaniecasual basic at right3
    show mac cop basic at left3
    "I'm surprised when Mackenzie asks us to take my car, but the sheriff cruiser does stand out next to everything else."
    hide mac
    hide hiflmc
    show mackenzie_s1_mini11 at bg
    "She's so stiff that I almost offer to let her drive, only to stop short when there's a glint of gold in her eyes."
    hide mackenzie_s1_mini11
    show hiflmc beaniecasual surprised at right3
    show mac cop basic at left3
    "It's gone a blink later, but my heart still skips a beat."
    "(Guess that's not just a full moon thing.)"

    show truck_back_night at bg behind hiflmc
    show hiflmc beaniecasual surprised at right3 behind truck_front_day:
        zoom 1.25
        yoffset 65
        xoffset -90
    show mac cop basic at left3 behind truck_front_day:
        zoom 1.25
        yoffset -65
        xoffset -80
    show truck_front_day at bg

    "I can't just ignore it as we get into the car."
    mcmac "Everything alright over there?"
    ma "Trying to keep my senses attuned."
    show mac cop sad
    ma "It's a lot more difficult from a car. Sights, sounds, smells, it all changes in a blur."
    show hiflmc beaniecasual happy
    mcmac "As long as you're not going to wolf out on me."
    show mac cop angry
    show hiflmc beaniecasual sad
    "She frowns and I bite my tongue, wondering if I'm going to get through today without demolishing any opinion Mackenzie has of me."
    "(I just don't know where we stand.)"
    ma "I'm not a rabid animal, [genericfn]."
    mcmac "I know you're not."
    mcmac "Sorry, I make jokes when I'm stressed, and some of them are real bad."
    show mac cop sad
    ma "It's scary, huh?"
    mcmac "Honestly? A little bit."
    ma "Try to think of it a different way."
    show mac cop happy
    ma "If I was a superhero that happened to be inhumanely strong and had gold eyes, that'd be cool, wouldn't it?"
    show hiflmc beaniecasual basic
    mcmac "I...well, yeah."
    show hiflmc beaniecasual happy
    ma "You'd be the amazing Wolfwoman or something."
    mcmac "Not quite the stars and stripes, but I'll take it."
    "Her smile puts me at ease,"
    hide mac
    hide hiflmc
    show bg abandoned_house_moon
    stop music fadeout 1.0
    play music mackenziehunt
    hide truck_front_day
    hide truck_back_night
    "But that comfort fades as the moon starts to climb above the horizon and I pull up in front of the abandoned house."
    "It's falling apart, power cut, and the shadows around it seem darker than they should be."
    "(I've never been over here.)"
    "(I think it belonged to some family who didn't want to incorporate into the town.)"
    "(But clearly they pulled up roots and got out of dodge.)"
    show truck_back_night at bg behind hiflmc
    show hiflmc beaniecasual sad at right3 behind truck_front_night:
        zoom 1.25
        yoffset 65
        xoffset -90
    show mac cop basic at left3 behind truck_front_night:
        zoom 1.25
        yoffset -65
        xoffset -80
    show truck_front_night at bg
    mcmac "That looks creepy as hell, Mackenzie."
    ma "I know."
    show hiflmc beaniecasual surprised
    "Then she starts to unbutton her shirt."
    "I freeze, unsure if I should look away."
    show hiflmc beaniecasual blush
    show mac tank basic
    "Mackenzie folds the shirt over the back of her seat before going for her belt, and heat rushes up the back of my neck."
    show mac tank surprised
    mcmac "Uh, am I supposed to strip too or..."
    "(Oh god, I didn't mean it like it sounded.)"
    show mac tank happy
    "She laughs softly, hanging her duty belt over the blue folds of the shirt."
    ma "Not sure that would help much, but I appreciate your enthusiasm."
    show hiflmc beaniecasual surprised
    "(Wait, I remember the tank top she threw out earlier. It was in pieces."
    show mac tank basic
    mcmac "Do you think you're going to shift?"
    ma "Better to be prepared. New gear's expensive."
    show hiflmc beaniecasual blush
    "(That makes way more sense.)"
    show hiflmc beaniecasual sarcastic
    "(Tone down the thirst, self. She's just working.)"
    show hiflmc beaniecasual blush
    "(...And looking really damn good doing it.)"
    hide mac
    show hiflmc beaniecasual sad
    "Mackenzie gets out of the car, but I hesitate, looking at the house."
    "A cold, creeping feeling drifts along my spine, warning me that there's something wrong."
    hide truck_front_night
    hide truck_back_night
    hide hiflmc
    show mac tank basic at centre:
        zoom 1
    ma "Let's get moving."
    hide mac
    show truck_back_night at bg behind hiflmc
    show hiflmc beaniecasual sad at right3 behind truck_front_night:
        zoom 1.25
        yoffset 65
        xoffset -90
    show truck_front_night at bg
    mcmac "I--I don't think I want to."
    show mackenzie_s1_mini3 at bg
    hide truck_front_night
    hide truck_back_night
    hide hiflmc
    "She offers me her hand, smile wholly sincere."
    hide mackenzie_s1_mini3
    show mac tank_cu happy_cu at mac_cu
    ma "I'll protect you, [genericfn]."
    ma "You're always safe with me, no matter what shape I'm in."
    hide mac
    $menuhideborder = True
    menu mace3c3:
        #"A. Yes" (paidchoice = "paidchoice"):
        "1. Take Mackenzie's hand." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(I've seen plenty of horror movies. I know what happens when the group splits up.)"
            show hiflmc beaniecasual_cu happy_cu
            mcmac "Thanks."
            show hiflmc beaniecasual_cu blush_cu at hiflmc_cu:
                xoffset 300
            show mac tank_cu happy_cu at mac_cu:
                xoffset -300
            "I take Mackenzie's hand, surprised how warm her fingers are when they squeeze around mine."
            "It's so tempting to make a joke about her running hot, but I restrain myself."
            "Barely."
            hide mac
            hide hiflmc
            show mac tank sad at left1 behind hiflmc
            show hiflmc beaniecasual basic at right2
            ma "Keep close, alright?"
            ma "If something breaks or goes haywire, I can catch you, but only if you're in reach."
            show hiflmc beaniecasual happy
            mcmac "Got it."
            show hiflmc beaniecasual sad
            mcmac "Do you really think someone's in there?"
            mcmac "For your sister's sake, I hope so."
            hide hiflmc
            show mac tank sad at centre
            "Mackenzie does an inspection of the outside of the house first, but most of the windows are boarded up."
            "Or so busted that someone would have to crawl through glass to get in."
            show bg abandoned_house_moon_fog
            "As she searches, the wind starts to pick up, rolling in a thick fog from the lake."
            show mac tank basic at left1
            show hiflmc beaniecasual sad at right2
            "I shiver, creeped out as my truck is covered by the haze, nearly obscured from view."
            mcmac "Is it always like this at night?"
            show mac tank smirk
            ma "When the moon's high? Tends to be."
            show hiflmc beaniecasual sad at right1
            "Unfortunately, that doesn't make me feel much better, so I press closer to Mackenzie's side."
            "She doesn't complain, holding my hand tight as we loop back around to the front of the house."
            show mac tank basic
            ma "I don't hear anything, but we should probably still check inside."
            mcmac "I had a feeling you were going to say that."
            ma "For all we know, this place has a basement."
            hide mac
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(I don't want there to be a basement.)"
            show hiflmc beaniecasual_cu sarcastic_cu
            "(Everything goes wrong in basements."
            show mac tank basic at left1
            show hiflmc beaniecasual sad at right1
            mcmac "Okay."
            show hiflmc beaniecasual angry
            mcmac "For Grace. I'm doing this for Grace."
            show mac tank surprised at left1
            show hiflmc beaniecasual surprised at right1
            ma "We'll be fine. Just take a deep breath and-!"
            show mac tank angry
            "A growl interrupts Mackenzie from somewhere behind us and I feel the urge to bolt,"
            show mac tank_cu angry_cu at mac_cu behind hiflmc:
                xoffset -150
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu:
                xoffset 150
                yoffset 70
            stop music fadeout 1.0
            play music hiflliteromance
            "But her arms come around me in a tight, defensive embrace."
            "My cheek is pressed right against her chest, and I can feel the low rumble she gives back in turn."
            show hiflmc beaniecasual_cu blush_cu
            "(Woah. This is new.)"
            "(Jesus, how much does she bench press?)"
            show hiflmc beaniecasual_cu sad_cu
            mcmac "What is it?"
            ma "Shh."
            "I clam up, trying to keep my thoughts on the danger instead of Mackenzie's max reps."
            show hiflmc beaniecasual_cu blush_cu
            "It's a little hard to focus when her entire body is pressed against mine, radiating power and a threat to anything that comes near us."
            show hiflmc beaniecasual_cu surprised_cu
            show mac tank_cu smirk_cu
            "Gravel and grass crunch as something approaches, but Mackenzie relaxes by degrees, letting out a soft laugh."
            "When I look back over my shoulder and see bright eyes, I'm worried until I realise how low they are to the ground."
            show hiflmc beaniecasual_cu basic_cu
            ma "Just a coyote."
            ma "This is probably her territory."
            show mac tank_cu basic_cu
            ma "Go on, tsk! Get out of here!"
            "The boom in her voice sends the coyote darting back into the fog, eventually fading from earshot."
            show hiflmc beaniecasual_cu happy_cu
            mcmac "Could it understand you?"
            show mac tank_cu smirk_cu
            ma "No more than anyone else."
            show mac tank_cu happy_cu
            ma "I wish I could talk to animals, though. They probably give better witness statements."
            mcmac "Yeah, right."
            mcmac "You'd ask them where the robber went and they'd be like,"
            mcmac "Sheriff Hunt, did you hear about the drama with the rabbits yesterday?"
            ma "True enough."
            show mac tank_cu angry_cu
            show mac tank_cu surprised_cu
            play music hiflRsuspense
            "Then something wipes Mackenzie's smile away."
            hide mac
            hide hiflmc
            show mac tank angry at left1 behind hiflmc
            show hiflmc beaniecasual basic at right1
            "When she snaps to high alert, I can see her hackles raise, posture changing as she sniffs the air."
            show hiflmc beaniecasual surprised
            mcmac "Mackenzie?"
            show hiflmc beaniecasual surprised at right2
            "Her arms relax around me, letting me go, but she doesn't say a word before turning towards the house, eyes narrowing."
            mcmac "What's wrong?"
            ma "I need you to stay right here while I go into the house."
            mcmac "But I thought we were sticking together."
            ma "Not for this."
            show hiflmc beaniecasual sad
            ma "Stay here, still and quiet. You got me?"
            show mac tank happy
            "As if realising how brusque her words sound, Mackenzie manages a half-smile. It shows a lot of teeth."
            ma "Please. Okay?"
            mcmac "Yeah, you got it."
            hide hiflmc
            show mac tank basic at centre:
                zoom 0.7
                xoffset 78
                yoffset -10
            "She nods in acknowledgement before taking measured steps towards the front door, quiet as a ghost despite the aged wood of the porch."
            "After prying the door open, Mackenzie slips inside, disappearing into the shadows."
            hide mac
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(What could catch her attention like that?)"
            "(It was the same the night of the full moon, but she didn't find anything...I think.)"
            show hiflmc beaniecasual sad at centre
            "It's impossible to figure out how much I really know about Mackenzie at this point."
            "She's a fixture of this town, and I've always felt like the outsider."
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(Now, who can say?)"

        "2. Stay in the car.":
            $menuhideborder = False
            show truck_back_night at bg behind hiflmc
            show hiflmc beaniecasual sad at right3 behind truck_front_night:
                zoom 1.25
                yoffset 65
                xoffset -90
            show truck_front_night at bg
            "(Is she going to hold up the whole house if it falls on me?"
            mcmac "I'll keep an eye out here. You know, just in case someone sneaks out."
            hide truck_front_night
            hide truck_back_night
            hide hiflmc
            show mac tank surprised at centre
            ma "If you're scared--!"
            hide mac
            show truck_back_night at bg behind hiflmc
            show hiflmc beaniecasual sad at right3 behind truck_front_night:
                zoom 1.25
                yoffset 65
                xoffset -90
            show truck_front_night at bg
            mcmac "Okay, I am."
            show hiflmc beaniecasual basic
            mcmac "But I also trust you to find Grace if she's in there."
            hide truck_front_night
            hide truck_back_night
            hide hiflmc
            show mac tank sad at centre
            "Disappointment flashes through Mackenzie's eyes..."
            show mac tank basic
            "before she nods and pushes the passenger side door shut, walking up to the house."
            hide mac
            show truck_back_night at bg behind hiflmc
            show hiflmc beaniecasual basic at right3 behind truck_front_night:
                zoom 1.25
                yoffset 65
                xoffset -90
            show truck_front_night at bg
            "Now that I'm alone, I feel a little foolish."
            show hiflmc beaniecasual sad
            "There's not much to do in the truck except take in the creepy scenery, and it's getting darker by the minute."
            mcmac "It can't take that long to search a house, right?"
            mcmac "I'll be fine."
            "Heavy fog starts to roll in from the back of the house, and I realise how close the lake must be."
            "We're just on the other side of it."
            show hiflmc beaniecasual surprised
            $sidecharone = "???"
            sid1 "Grr!"
            "A sound from the front of the car startles me,"
            hide truck_front_night
            hide truck_back_night
            hide hiflmc
            show hiflmc beaniecasual surprised at centre
            "and I fumble my keys out of the ignition before flinging myself out of the truck, dashing towards the house."
            show hiflmc beaniecasual angry
            mcmac "I am NOT becoming an X-Files episode!"
    show hiflmc beaniecasual surprised at centre
    play music hiflaction
    "Glass breaks from inside and my head snaps up towards the windows."
    hide hiflmc
    "There's a horrible scratching sound before I hear wood buckle and break, part of the house bowing out like something's trying to force through."
    "Then it shatters into splinters, a blur of limbs tumbling together before the frenzy slams into the ground below."
    show mac earstank wolfgrowl at centre:
        zoom 0.7
        xoffset 80 - 100
        yoffset -10
    show damien wolf wolfangry at centre:
        zoom 0.75
        xoffset 80 + 100
        yoffset 20
    "Mackenzie snarls at the man beneath her, his eyes and fangs just like hers--"
    "--his jacket matching the one from the diner."
    hide mac
    hide damien
    show mac earstank_cu wolfgrowl_cu at mac_cu:
        xoffset -200
        yoffset 30
    show damien wolf_cu wolfangry_cu at damien_cu:
        xoffset 200
    "He draws back a set of razor-sharp claws to slash at her throat, rage burning in a golden predatory gaze."
    hide mac
    hide damien
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    mcmac "Mackenzie!"
    hide hiflmc


    $tobecontinued()

    show bg hifltbc with fade
    pause
    $ resets()


transform raziline1:
    xpos 195
    ypos 560
    zoom 0.80
transform jdline1:
    xpos 500
    ypos 600
    zoom 0.80
transform diegoline1:
    xpos 720
    ypos 0
    zoom 0.80
transform hiflmcline1:
    xpos 1020
    ypos 635
    zoom 0.80
