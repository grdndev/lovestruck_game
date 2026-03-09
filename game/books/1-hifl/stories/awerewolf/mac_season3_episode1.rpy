label mac_season3_episode1:

    $tbc = False
    scene bg hifl_sheriff at bg
    play music hifleveryday

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    "Gwen lunges for me."

    "I dodge as fast as I can, putting a broken chair between us,"

    "But one of her claws still catches on my shirt and rips right through the sleeve."

    gwe "Is that how you're going to play it? Cat and mouse?"
    gwe "You'll exhaust yourself a long time before I do, human."

    "Shifting back by inches, I move as close to Mackenzie as I can."

    "I don't want her to be alone when she's hurting, even if this is the end of things"

    mcmac "Is there nothing you want?"
    mcmac "Anything I could give you so you'd stop this."

    gwe "No."
    gwe "At this point, it's personal."

    "Mackenzie snarls from behind me, collapsing down to one knee."

    "Behind the burst of rage are throaty whimpers of pain, her claws biting into her own arm around where the knife dug in."

    mcmac "Mac, it's okay."
    mcmac "Just look at me."

    "She does, but the glimmer of humanity in her eyes is waning fast."

    "Every muscle in her body tenses and jerks, and I'm not sure if she's trying to fight a deeper change or shift back entirely."

    "(Can Mac even do that?)"
    "(Fuck, I have no idea what silver really does to werewolves.)"
    "(Besides killing them.)"


    gwe "Are you done?"

    mcmac "Were you really waiting for me to say goodbye?"

    gwe "Call it professional courtesy."

    "I want nothing more than to flip Gwen off, but I kneel next to Mackenzie instead."

    "She stiffens at first,"

    "But when I run my fingers through her hair, gently stroking between each ear Mackenzie groans in miserable relief."

    "(Just get it over with, Gwen.)"
    "(Stab me in the back so I can return as a ghost and haunt you literally forever.)"

    "Footsteps carry behind me, slow and deliberate,"

    "And I ignore the spike of fear that pierces through me, keeping my eyes on Mackenzie instead."

    mcmac "I told you I wasn't going anywhere. That I'm with you."

    "Then the front door is knocked right off its hinges."

    "I jerk around to look at the noise, but it's not Gwen."

    "A woman stands in the doorway, dark hair flowing down her shoulders."

    "The look in her eyes is purely predatory as she uncoils a whip from underneath her coat."

    "The long tail curves around her ankles like a serpent."

    gwe "Who the hell are you?!"

    $sidecharone = "Whip-Wielding Huntress"
    sid1"Your curtain call."

    "It's impossible not to stare as the whip lashes out and loops right around Gwen's wrist."

    "She hisses, trying to pull free when the other woman draws a pistol and aims it right between Gwen's eyes."

    sid1 "Made you look, monster."

    "She pulls the trigger, and Gwen dodges by a hair."

    "The next shot is blocked by a swipe of her claws, and my jaw drops as fragments of metal fall to the floor like shrapnel."

    gwe "Shoot me again and I'll—!"

    sid1 "You'll do what?"
    sid1 "If you could regenerate the damage, you wouldn't bother getting out of the way."

    "For the first time since she burst into the bowling alley, I see fear in Gwen's eyes."

    "It isn't feigned in the least, and she tugs herself away from the whip like a wounded animal in a trap."

    $menuhideborder = True
    menu macs3e1c1:
        "A. Join the fight with Gwen.":
            $menuhideborder = False
            show hiflmc casual_cu angry_cu at hiflmc_cu
            "(She's outnumbered now. I want to win.)"
            hide hiflmc
            show hiflmc casual angry at right3
            show gwen bansheecasual bansheesurprised at left3
            "Scrambling for a weapon, I pick up a shattered piece of furniture from the floor and chuck it at Gwen's back."
            "It actually hits her, and her yelp of pain is more satisfying than it should be."
            hide hiflmc
            hide gwen
        "B. Try and help Mac stand.":
            $menuhideborder = False
            "(This is our chance to get out of here.)"

            mcmac "Mac, come on."

            "I hook my arms under Mackenzie's, doing my best to get her back to her feet,"

            "but the choked sound of pain that follows makes me hesitate."
        "C. Stay out of the way.":
            $menuhideborder = False
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(I'm not getting in the middle of that.)"
            hide hiflmc
            show hiflmc casual sad at right2
            show mac wolfdrooptank wolfsleep at left2
            "Pressing my body protectively against Mackenzie's,"
            "I take a deep breath, trying to ignore the ring from the gunshots reverberating through my head."
            hide hiflmc
            hide mac
    "A hard blow from the back of the gun sends Gwen sprawling, and by the time she recovers to her knees,"

    "The huntress has the barrel aimed right at her heart instead."

    sid1 "Let justice be done."

    "Gwen is fast, but not quite fast enough."

    "The bullet catches in her arm as she jerks away, and after a howl of pain, she throws herself right out the nearest window."

    "Glass goes flying, and Gwen's shadow darts towards the foyer."

    mcmac "Holy shit."

    "My breathless exclamation catches the huntress' attention,"

    "And she sets the safety on her pistol before taking a step towards me."

    sid1 "Are you alright?"

    mcmac "I am, but Mac..."

    "Her eyes narrow in concern at the state of Mackenzie's arm,"

    "But when the huntress moves closer, Mackenzie snaps her teeth in an obvious threat."

    ma "Back off!"

    "The words sound almost nothing like her, more growl than syllable,"

    "But the huntress puts both her hands up in a mild surrender."

    sid1 "That silver knife on the floor did you in, right?"
    sid1 "I'm just going to take a look at it."

    "After holstering her gun, the huntress crouches down to pick up the blade with care, examining it with a frown."

    sid1 "That went deep."

    mcmac "What does that mean?"

    sid1 "You don't know?"

    mcmac "I'm human. This is…this is all still pretty new to me."

    "Admitting that makes me feel helpless, but I know Mackenzie needs help."

    "I'll take any information I can get."

    sid1 "Silver corrupts a werewolf's blood."
    sid1 "The longer it lingers, the more damage it does."

    mcmac "So how do I fix it?"

    sid1 "Sorry, I'm no healer."
    sid1 "I've used silver myself when the occasion called for it, but I'm guessing your wolf here is local and not rogue."

    mcmac "She's the alpha of Havenfall."

    "A curious look flickers through the huntress' eyes, but she acknowledges my words with a nod."

    sid1 "Then get her to her pack."
    sid1 "I need to go chase that banshee down."

    mcmac "She doesn't have one."
    mcmac "Mackenzie only has me."

    sid1 "..."
    sid1 "You better find someone with a cure fast, then."
    sid1 "She looks like she's about to wolf out."

    mcmac "Isn't she already—!"

    "Hesitation catches my words when I look back at Mackenzie again."

    "Her eyes are golden in a way I've never seen before, glinting with a feral light."

    "(Mac told me she didn't know how to transform all the way, but what if it happens by accident?)"

    sid1 "A full-body change would kill her in this state."
    sid1 "Impressive as it looks, shifting is a lot of physical trauma packed into a couple seconds."
    sid1 "And anything that leads the silver to her heart faster is a mistake."

    $menuhideborder = True
    menu macs3e1c2:
        "A. How do you know all this?":
            $menuhideborder = False
            show hiflmc casual surprised at right3
            show vanessa huntress hatangry at left3
            mcmac "How do you know all this?"
            show vanessa huntress hatbasic
            sid1 "Time and practice, mostly."
            show vanessa huntress hatsmirk
            sid1 "And the occasional monster-hunting tome passed down the family line."
        "B. Are you human too?":
            $menuhideborder = False
            show hiflmc casual surprised at right3
            show vanessa huntress hatbasic at left3
            mcmac "Are you human too?"
            show vanessa huntress hatsmirk
            sid1 "Much to the fury of my prey, yes."
            sid1 "Monsters aren't anywhere near as unstoppable as they seem."
        "C. Can I stop it?":
            $menuhideborder = False
            mcmac "How do I stop it?"

            sid1 "Try and keep things under control."

            sid1 "She trusts you enough to touch her, which is already a good headstart."

    "(There is so much going on right now, I feel like my head is going to explode.)"

    mcmac "Why are you after Gwen?"

    sid1 "This town isn't the first place she's caused havoc."
    sid1 "I hunt the creatures that fall out of line, and I'm good at it."
    sid1 "Havenfall makes things a little bit more complicated, but that's alright."

    "(Complicated how?)"
    "(I guess it makes sense that in a world of monsters, there would be monster slayers, but I still didn't expect to meet one.)"

    sid1 "The more time you waste here, the less your wolf has left."
    sid1 "So go."

    "Before I can answer, the huntress is gone in a flutter of leather, following the path that Gwen had taken towards the forest."

    mcmac "Damn it."
    mcmac "Okay, Mac. I'm getting you out of here."

    "I've never been so aware of how much bigger than me Mackenzie is until now."

    "Helping her to stand takes every ounce of strength I have,"

    "And then another ounce more to get us walking out of the house and into my truck."

    "She's quieter now, quiet enough that a different kind of worry is making me shake."


    mcmac "I'm going to take you home, Mac."
    mcmac "Just stay with me."

    "Dialing Razi's number as quick as I can, I set the call on speakerphone before starting the engine and hitting the gas."

    ra "[genericfn]? You're up late."

    mcmac "Gwen stabbed Mac with silver."

    ra "...What?"

    mcmac "She's really hurt, Razi! I don't know what to do."
    mcmac "I have no idea how long she can hold on."

    ra "Which house is closer? Yours or hers?"

    mcmac "Mine."

    ra "Then get her there. I'm sending Diego your way."

    "(Right, he's a doctor. Thank...)"
    "(Okay, thanking any kind of god for a vampire is probably a bad idea, but I'm grateful anyway.)"

    mcmac "Thank you."
    mcmac "I'm driving as fast as I can."

    ra "Stay safe."
    ra "Is Gwen still out there? I'll send JD after her."

    mcmac "Someone else went after Gwen. That's the only reason we're still alive."

    ra "Who?"

    mcmac "I'll fill you in later."

    ra "Right. Okay, I'll ask JD to keep an eye on things"
    ra "We've had enough trouble with uninvited guests lately."

    "(Understatement of the century, Razi.)"

    "He hangs up, and I speed down a couple of backstreets before parking in front of my house."

    "I get out and go around to open the door for Mackenzie, only to jump when someone steps out of the shadows."

    di "Let me help you."

    mcmac "How are you already..."
    mcmac "Never mind."

    di "I'll get Mackenzie into the house. Carry the cooler inside."

    "I have no idea what he's talking about until I see the small styrofoam cooler by my front door."

    "It's cold to the touch when I pick it up, but I shuffle it under one arm before fetching my keys."

    mcmac "Where do you want this?"

    di "On a table somewhere."
    di "I also need an invitation."

    "Turning around in confusion, I realize Diego is standing still on my porch, Mackenzie's arm slung around his shoulder."

    "Mackenzie is growling a little, but still conscious."

    mcmac "Oh, sorry!"
    mcmac "Diego Escalona, ​​please come in."

    di "There's no need to be that formal, but I appreciate it."

    "Diego guides Mackenzie over to my couch before sitting her down."

    "When he pops open the cooler, I take one glance inside it before recoiling."

    mcmac "Are those bags of blood?"

    di "It's her emergency plan. I hoped I'd never have to use it."
    di "Now help me hold her arm out."
    di "I need to put in an IV, and in this state..."
    di "She will not react well to more pain."

    "I'm already on the edge of freaking out, and it takes a couple of deep breaths before I can join Mackenzie on the couch."

    "She turns to nuzzle me, and I return it with a soft whisper of her name, guiding my fingers down her arm."

    mcmac "Relax for me, Mac."
    mcmac "This will stop everything from hurting."

    "(At least, I hope so.)"

    "I see Diego prepping a needle out of the corner of my eye, and immediately look away."

    "Mackenzie lets out a threatening growl a moment later, but I keep my hands in constant contact, trying to distract her."
    $menuhideborder = True
    menu macs3e1c3:
        "A. What exactly are you doing, Diego?":
            $menuhideborder = False
            show hiflmc casual surprised at right3
            show diego casual basic at left3
            mcmac "What exactly are you doing, Diego?"
            show diego casual angry
            di "Performing a very ill-advised blood transfusion."
            di "But there's not a lot of ways to flush silver out of a werewolf's system."
        "B. Are you sure this is going to work?":
            $menuhideborder = False
            show hiflmc casual sad at right3
            show diego casual basic at left3
            mcmac "Are you sure this is going to work?"
            show diego casual sad
            di "Mackenzie seemed convinced, although this was a while ago."
            di "I have to applaud her for such a contingency, unpleasant as it may be."
        "C. Why is she like this?":
            $menuhideborder = False
            mcmac "Why is she like this?"
            mcmac "So... wolfed out?"

            di "At the end of the day, she isn't human."
            di "Her instincts are different."
            di "An all-out defense is the only protection one can have on the edge of death."

    hide hiflmc
    hide diego
    "Mackenzie gasps in pain, chest heaving with quick, sharp breaths."

    di "Don't you dare die on me, Mackenzie Hunt."
    di "Hold onto her, [genericfn]."
    di "Close your eyes, breathe with her, and let me work."

    "I do."

    "There's nothing else I can do except listen for the beat of Mackenzie's heart, hoping beyond hope that she'll be okay."
    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
