define unknown = Character("???",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define Sheriff = Character("Sheriff Hunt",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define mail = Character("Mail Carrier",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define doc = Character("Dr. Escalona",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])

label van_season1_episode4:

    $tbc = False
    scene bg main_fog at bg
    play music hiflsuspense
    pause

    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Wait... red eyes?)"
    "(Another vampire?!)"
    "(This can't be happening.)"

    hide hiflmc
    show hiflmc bowling angry at right4
    show li casual basic at left4
    mcvan "I don't know who you are, but I only have one sister, and you're sure as hell not her."
    show li casual happy
    "The woman laughs, practically dripping condescension."
    $sidecharone = "Mysterious Woman"
    sid1 "Not yet, but I soon will be."
    hide li
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(What was it Vanessa said?)"
    show hiflmc bowling_cu basic_cu
    "(Vampires can't enter a place unless you give them permission?)"
    show hiflmc bowling_cu surprised_cu
    "(Maybe if I could just get back into the bowling alley...)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "I turn around and try to open the door, but it's already locked."
    hide hiflmc
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(I shouldn't have locked it.)"
    "(Damn!)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "I frantically search my pocket for keys."
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Of all the times-!)"
    hide hiflmc
    show hiflmc bowling sad at centre
    "I finally find them, but my hands are shaking so badly that the keys drop the pavement."
    show hiflmc bowling angry
    "Giving up on the door, I swipe my keys off the ground and run."
    hide hiflmc
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(I have to put a little more distance between us.)"
    hide hiflmc
    show li casual happy at centre
    "The woman chuckles."
    sid1 "You have nothing to fear."
    sid1 "To be among us, to be his Bride, is an honor."
    hide li
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Bride?)"
    "(The vampire from yesterday said the same thing.)"
    show hiflmc bowling_cu angry_cu
    "(That can't be a coincidence.)"
    hide hiflmc
    show hiflmc bowling sarcastic at right4
    show li casual basic at left4
    mcvan "Thanks, but I'm not really looking to settle down right now."
    show li casual happy
    sid1 "You will be a Queen--more powerful than you can imagine."
    show hiflmc bowling angry
    mcvan "All women are Queens, lady."
    show li casual surprised
    sid1 "You cannot escape your destiny, [genericfn]."
    sid1 "It is in your blood."
    hide li
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Wait, what?)"
    hide hiflmc
    $menuhideborder = True
    menu vane4c1:
        "A. Shut her down.":
            $menuhideborder = False
            show hiflmc bowling angry at right4
            show li casual basic at left4
            mcvan "I don't know what you're talking about."
            sid1 "You will, in time."
            hide li
            hide hiflmc
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            mcvan "Great, more cryptic non-answers."
            hide hiflmc
        "B. Play it off with a joke.":
            $menuhideborder = False
            show hiflmc bowling sarcastic at right4
            show li casual basic at left4
            mcvan "There's nothing in my blood except for a dozen cups of coffeee."
            sid1 "Joke all you like, but you were born to be his bride."
            sid1 "There is no escape."
            hide hiflmc
            hide li
        "C. Ask her for answers directly.":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show li casual basic at left4
            mcvan "I'm nobody!"
            mcvan "Why does 'He' want me in particular?"
            show hiflmc bowling angry
            mcvan "Aren't there better choices for 'Him' out there?"
            sid1 "No. It must be you."
            hide li
            hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Stall, stall, I gotta stall until someone comes to help me.)"
    hide hiflmc
    show hiflmc bowling sarcastic at right4
    show li casual basic at left4
    mcvan "My mom was an engineer and my dad was a professor--no royalty, I promise."
    show hiflmc bowling angry
    mcvan "There's no way this could be 'in my blood.'"
    mcvan "Besides, am I supposed to trust you about my supposed 'destiny' when I don't even know your name?"
    show li casual happy
    "She smiles coldly."
    sid1 "Fair enough. My name is Siniang Li."
    show li casual basic
    sinli "Does that satisfy you?"
    show hiflmc bowling basic
    mcvan "I guess."
    show hiflmc bowling sarcastic
    mcvan "I don't suppose you'll share any other tidbits with me? Or explain what's going on?"
    mcvan "Who is 'He' anyway?"
    show hiflmc bowling surprised
    show li casual surprised
    "She opens her mouth, but whatever she's about to say is interrupted by the loud screech of tires."
    "The smell of burning rubber hits me first, followed by the welcome sight of headlights."
    hide li
    hide hiflmc
    show van_middle_night at bg
    show vanessa huntress hatangry at right4:
        ypos 725
    show van_front_night at bg
    "The van screeches to a halt in the middle of the street."
    stop music fadeout 1.0
    play music hiflaction
    scene vanessa2 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 8 yanchor 0.1
    pause

    "Vanessa saunters out like something out of a movie,"
    "Cracking her whip threateningly, somehow still managing to look glamorous."
    "(Oh thank god, she's here.)"
    "Vanessa strides towards me, looking fiercely protective."
    scene bg main_fog at bg
    show li casual angry at centre
    "Li's attention shifts completely toward Vanessa, demeanor changing."
    hide li
    show li casual_cu angry_cu at li_cu
    "Her stance is more aggressive, her fury almost tangible."
    show li casual_cu vampireangry_cu with dissolve
    "Her eyes start to glow brighter, and her fangs visibly elongate."
    hide li
    show vanessa whiphuntress hatangry at left2
    show hiflmc bowling surprised at right3 behind vanessa
    va "I came as quickly as I could. Are you hurt?"
    hide hiflmc
    hide vanessa
    show li casual vampireangry at centre
    sinli "Have you nothing better to do than chase after those of us who walk in the shadows?"
    show li casual vampirebasic
    sinli "[genericfn] and I were simply having a pleasant chat."
    show li casual vampireangry
    sinli "Isn't that right?"
    show li casual vampireangry at left4
    show hiflmc bowling surprised at right4
    "She shoots me a threatening look with those piercing crimson eyes."
    hide li
    hide hiflmc
    show vanessa whiphuntress hatangry at centre
    va "Quiet, bloodsucker. You'd better focus on me unless you want to be a pile of dust at my feet."
    "She looks so confident, so in her element, it's hard to do anything other than believe in her."
    hide vanessa
    show li casual vampireangry at centre
    sinli "You possess the arrogance of youth."
    sinli "You will not sound so confident when you are dead at my feet, child."
    show li casual vampireangry at left4
    show vanessa whiphuntress hatangry at right4
    va "Bring it on, Leech."
    va "We'll see who lands on top."
    #ripple effect goes here
    show li casual vampireangry at left2
    "Li lunges at Vanessa faster than I can see, and I flinch back."
    "Vanessa reacts instantaneously, lashing out with her whip before Li's claws can reach her."
    hide vanessa
    show li casual vampirebasic at centre
    "The whip wraps around Li's wrist..."
    #bat effect goes here
    hide li
    "But the vampire scatters into a swarm of something."
    show li casual vampirebasic at centre
    "And reappears a few feet away."
    hide li
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Are those bats?)"
    "(Is that a real thing?)"
    hide hiflmc
    show vanessa whiphuntress hatangry at centre
    va "Just... stay... still!"
    show vanessa whiphuntress hatangry at right4
    show li casual basic at left4
    "Vanessa grunts as she aims blow after blow at Li, who keeps vanishing into her swarm of bats before the strikes can land."
    hide vanessa
    show li casual happy at centre
    sinli "You are tenacious, I grant you that, but you are hundreds of years too young to fight me seriously."
    hide li
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(These two are... much more evenly matched than the fight from last night.)"
    show hiflmc bowling_cu sad_cu
    "(Vanessa can handle this, right?)"
    show hiflmc bowling_cu angry_cu
    "(This is what she does--no way is she going to let one measly vampire get the best of her.)"
    show hiflmc bowling_cu surprised_cu
    "(But... just in case, I should try to help, right?)"
    hide hiflmc
    $menuhideborder = True
    menu vane4c2:
        "A. Encourage Vanessa":
            $menuhideborder = False
            show hiflmc bowling angry at centre
            mcvan "I believe in you, Vanessa!"
            mcvan "You got this, no problem!"
            hide hiflmc
            show vanessa whiphuntress hatangry at centre
            "Vanessa doesn't respond, focused on the fight, but her next attack seems more confident."
        "B. Insult Li.":
            $menuhideborder = False
            show hiflmc bowling happy at centre
            mcvan "From where I'm standing, it looks like Vanessa's doing more than fine."
            mcvan "Are you sure vampires can't get senile?"
            hide hiflmc
            show li casual vampireangry at centre
            sinli "Insolent girl!"
            hide li
            show vanessa whiphuntress hatsmirk at centre
        "C. Stay out of it.":
            $menuhideborder = False
            show hiflmc bowling_cu sad_cu at centre
            "(No... I'd better not.)"
            "(I don't want to accidentally distract Vanessa.)"
            "(She looks so focused, I don't want her to lose concentration and get hurt.)"
            hide hiflmc
    show vanessa whiphuntress hatangry at right4
    show li casual vampireangry at left4
    "Vanessa finally manages to land a solid blow, her whip cracking across Li's arm with a nasty-sounding thwack."
    show vanessa whiphuntress hatsmirk
    "She smirks."
    va "What can I say? I'm a prodigy."
    hide li
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(I'll bet you are.)"
    "(It's almost worth being in mortal danger just to watch her work.)"
    hide hiflmc
    show li casual vampireangry at centre
    "Li snarls, ready to launch another attack, but she's interrupted by the doors of the bowling alley slamming open."
    hide li
    show razi casual surprised at left4
    show jd casual surprised at right4
    "Razi and JD rush out, taking in the scene with wide eyes."
    hide razi
    hide jd
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(No, no, no--they need to go back inside and be safe!)"
    "(Vanessa won't be able to protect all of us.)"
    hide hiflmc
    show vanessa whiphuntress hatsurprised at centre
    "Vanessa is equally distracted by their sudden appearance, unfortunately giving Li the opening she was waiting for."
    hide vanessa
    # bat effect goes here
    show hiflmc bowling surprised at right2
    show li casual vampireangry at left2 behind hiflmc
    "Li disappears in a flurry of bats, reappearing right behind me, holding her incredibly sharp claws at my throat."
    sinli "This was not how I wished to do this, but you have left me no choice."
    sinli "I shall just have to take you now, and convince you later."
    "I freeze, but as soon as she's done talking, an enourmous fireball comes flying toward us."
    #JD flame effect goes here
    show hiflmc bowling surprised at right4
    show li casual vampireangry at left4
    "She lets me go as she vanishes, and I jump out of the way just in time."
    hide li
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Where did that come from?)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "I look back at the others, expecting them to be equally confused."
    stop music fadeout 1.0
    play music razinassar
    show razi djinn angry at left4
    show jd casualwings devilangry at right4 behind razi
    "Instead, I find Razi and JD... transformed?!"
    hide jd
    hide razi
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(What?!)"
    "(Where did Razi's shirt go?)"
    "(Are those... wings on JD's back?)"
    hide hiflmc
    show li casual basic at centre
    sinli "Calling in backup? Not typical strategy for a Helsing."
    show li casual happy
    sinli "I suppose the standards must be slipping."
    hide li
    show razi djinn surprised at left4
    show jd casualwings devilsurprised at right4 behind razi
    "JD and Vanessa both do a double-take at the name, attention shifting to Vanessa..."
    hide jd
    hide razi
    show vanessa whiphuntress hatbasic at centre
    "Whose face is unreadable."
    hide vanessa
    show li casual basic at centre
    sinli "Nevertheless, I shall take my leave."
    show li casual angry
    sinli "But make no mistake--I will be back."
    #bats
    hide li with dissolve
    "With that parting shot, she once again dissolves into a swarm of bats."
    show razi djinn surprised at left4
    show jd casualwings devilsurprised at right4 behind razi
    "Razi and JD start to jog over, speaking almost simultaneously."
    hide razi
    show jd casualwings devilsurprised at centre
    jd "You okay, [genericfn]? Who was that?!"
    hide jd
    show razi djinn surprised at centre
    ra "What happened, [genericfn]? Did she hurt you?"
    hide razi
    show hiflmc bowling surprised at centre
    "Despite their strange new appearances, I'm touched by their concern."
    "(If they hadn't come when they did, Vanessa might really have lost that fight...)"
    show hiflmc bowling surprised at right4
    show vanessa huntress hatangry at left4
    "Vanessa sprints toward me, looking as fiercely protective as she had earlier."
    show hiflmc bowling blush
    "Knowing that I'm the complete focus of all that intensity makes my heart skip a beat."
    hide hiflmc
    hide vanessa
    show razi djinn basic at left4
    show jd casualwings devilbasic at right4 behind razi
    "She immediately puts herself between me, Razi, and JD who stop in their tracks."
    hide jd
    hide razi
    show vanessa huntress hatangry at right1
    show hiflmc bowling surprised at left2 behind vanessa
    va "Don't come any closer!"
    hide hiflmc
    hide vanessa
    show jd casualwings devilangry at centre
    jd "What, us?! We're not the enemies!"
    hide jd
    show razi djinn basic at centre
    ra "We would never harm [genericfn], Vanessa."
    ra "Nor you, though I'm not sure you could say the same."
    show razi djinn angry
    ra "Helsing."
    hide razi
    show vanessa huntress hatangry at right1
    show hiflmc bowling surprised at left2 behind vanessa
    mcvan "Not to be rude, but I have so many questions."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Like when the hell this became my life.)"
    "(This is all so nuts, Grace is never going to believe me about any of this.)"
    hide hiflmc
    show razi djinn happy at right4
    show hiflmc bowling basic at left4
    "Razi shoots a small snmile my way, but his eyes stay cautious."
    ra "Of course. You're right to be curious."
    hide razi
    hide hiflmc
    show jd casualwings devilhappy at centre
    jd "Look on the bright side: your life just got ten times more interesting."
    show razi djinn angry at left4
    show jd casualwings devilhappy at right4 behind razi
    "Razi gives JD a look."
    hide jd
    show razi djinn basic at centre
    ra "Why don't we go inside, where it's safer and more... discreet?"
    hide razi
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(That's probably a good idea.)"

    show hiflmc bowling surprised at right1
    show vanessa huntress hatsurprised at left3 behind hiflmc
    "I move to head inside, but Vanessa blocks me, incredulous."
    va "You still trust them?"
    show vanessa huntress hatangry
    va "They've clearly been lying to you all this time."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(She's not wrong, but... JD and Razi are my friends.)"
    "(My only friends.)"
    "(If I can't trust them, I can't trust anyone.)"
    hide hiflmc
    show hiflmc bowling sad at right1
    show vanessa huntress hatangry at left3 behind hiflmc
    mcvan "I'd be dead or kidnapped if they hadn't stepped in."
    show hiflmc bowling basic
    mcvan "The least we can do is go inside and hear them out."
    va "I don't like it."
    show hiflmc bowling sad
    mcvan "Listen, I really appreciate how seriously you're taking your promise, but I trust them."
    mcvan "Do you trust me?"
    show vanessa huntress hatsleep
    "She looks at me for a long moment, then sighs."
    show vanessa huntress hatbasic
    va "Of course."
    va "I guess if you're determined to go with them no matter what, I have to go too."
    show hiflmc bowling happy
    "I beam at her."
    mcvan "You won't regret it, you'll see."
    show vanessa huntress hatsmirk
    "She shakes her head, looking like she already regrets it, but there's a small smile curling at the edges of her lips."

    scene bg bowling_regular at bg with fade
    stop music fadeout 1.0
    play music hiflgetitdone
    pause

    "We head inside after JD and Razi, but Vanessa sticks close to my side."

    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Not that I'm complaining about a gorgeous woman sticking to me like glue.)"
    hide hiflmc
    show jd casual basic at right4
    show razi casual basic at left4
    "Inside, they both look like their everyday selves..."
    "Razi is leaning against the bar while JD is sitting withv their heels kicked up onto the table."
    show jd casual angry
    jd "Hey, should we call Mac and Diego in for this?"
    "Razi shakes his head."
    ra "No, not right now."
    hide jd
    hide razi
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Why would Sheriff Hunt and Dr. Escalona need to be here?)"
    show hiflmc bowling_cu sad_cu
    "(No, that's a question for later.)"
    show hiflmc bowling_cu sarcastic_cu
    "(There are more pressing concerns right now, like...)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    mcvan "Just what are you two?"
    show hiflmc bowling surprised at right4
    show razi casual happy at left4
    "Razi smiles patiently at me."
    ra "I'm a Djinn."
    hide razi
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Oh. Okay. Sure, why not?)"
    hide hiflmc
    show jd casual happy at centre
    "JD grins impishly."
    jd "Go on, guess."
    hide jd
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Well, at least JD is still JD, no matter what kind of supernatural creature they are.)"
    hide hiflmc
    $menuhideborder = True
    menu vane4c3:
        "A. Tease them.":
            $menuhideborder = False
            show jd casual happy at left4
            show hiflmc bowling sarcastic at right4
            mcvan "I don't know, is there a 'rearranging bowling shoes and making solo-cup pyramids' monster."
            show jd casual sad
            "JD clutches their chest and feigns distress."
            jd "Oh. [genericfn], you wound me."
            hide jd
            hide hiflmc
        "B. Guess seriously.":
            $menuhideborder = False
            show jd casual happy at left4
            show hiflmc bowling surprised at right4
            mcvan "Ah... Maybe some kind of... demon? Because of the wings? And the horns?"
            show hiflmc bowling sad
            mcvan "Sorry if that's offensive."
            show jd casual smirk
            jd "Nah, it's fine, you're on the right track!"
            "JD laughs."
            hide jd
            hide hiflmc
        "C. Give up.":
            $menuhideborder = False
            show jd casual happy at left4
            show hiflmc bowling sad at right4
            mcvan "I really had no idea. Can't you just tell me?"
            show jd casual surprised
            jd "Now where's the fun in that?"
            hide jd
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            mcvan "(Well, same old JD, for better or more annoying.)"
            hide hiflmc
    show hiflmc bowling surprised at centre
    mcvan "So... why is this all happening to me, exactly? And why now?"
    show hiflmc bowling basic at right4
    show razi casual basic at left4
    ra "My family has protected this area for centuries, making it a Haven for supernatural creatures who need it."
    ra "Thus the name."
    hide hiflmc
    show vanessa huntress hatsad at right4
    va "And you don't think that's... unwise?"
    show vanessa huntress hatbasic
    va "Most creatures would take advantage of that hospitality."
    show razi casual angry
    "Razi gives her a sour look."
    ra "Most of the time they're peaceful, and when they'rte not, we deal with them."
    show razi casual basic
    ra "We try to keep things lowkey, and it's woirked so far."
    ra "There's really no need for anyone to swoop in and cause trouble."
    show razi casual angry
    "He looks at Vanessa pointedly, like he thinks she's the one to blame for the commotion."
    hide razi
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(And Vanessa does not look impressed.)"
    hide hiflmc
    show vanessa huntress hatangry at centre
    va "Maybe it works under normal circumstances, but the vampire that attacked [genericfn] yesterday certainly wasn't lying low."
    va "And I'm not sure what you think that scene outside was..."
    va "But considering that's the second vampire to attack her in two days, you may want to reconsider you approach."
    hide vanessa
    show jd casual surprised at centre
    jd "Wait, really? Two in two days?"
    hide jd
    show razi casual surprised at centre
    ra "Is that true, [genericfn]? Why didn't you tell us?"
    show razi casual surprised at left4
    show hiflmc bowling sarcastic at right4
    mcvan "Well it's not like I knew you were a Djinn yesterday!"
    show hiflmc bowling sad
    mcvan "I thought if I told you I was attacked by a vampire, you'd have me committed."
    show hiflmc bowling basic
    mcvan "Besides, Vanessa's done a great job protecting me."
    show razi casual sad
    ra "Be that as it may, we know now, and can help protect you as well."
    hide hiflmc
    hide razi
    show jd casual happy at centre
    jd "Yeah, we can definitely help! We're awesome at protecting people."
    hide jd
    show vanessa huntress hatbasic at centre
    "Vanessa stares at them coolly."
    va "I swore to protect [genericfn], which means I will stay and guard her until the threat is dealt with."
    va "And I work alone."
    show vanessa huntress hatangry
    va "I especially don't work with... supernaturals."
    hide vanessa
    show jd casual angry at centre
    jd "There's no way we're just gonna sit around while [genericfn] is in danger!"
    hide jd
    show razi casual angry at centre
    ra "You would turn away valuable resources just to spare your pride?"
    hide razi
    show vanessa huntress hatangry at centre
    va "This isn't about pride!"
    va "It's my calling--my duty to protect humanity from vampires."
    va "If it means giving my life, so be it."
    "She's speaking so passionately, I can almost feel the strength of her belief."
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(I can't even imagine being that self-assured about anything.)"
    "It takes my breath away."
    hide hiflmc
    show vanessa huntress hatangry at centre
    va "But no matter what it takes, I will keep [genericfn] safe."



    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
