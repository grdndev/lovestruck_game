
label ghost_season1_episode5:
    $tbc = False
    scene bg main_day at bg
    play music litegetitdone

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() at the bottom.
    
    #"We waste a few minutes arguing over it, but I finally manage to convince Mackenzie to point me in the general direction of Labasque's forest hideout."
    #show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    #"(Mostly I think she just didn't want to send me into a dangerous situation alone, which would be pretty understandable if I wasn't literally dead.)"
    #hide ghostmc
    #"After that, it doesn't take a lot of aimless wandering in the forest before I start seeing vampires pop up."
    show mac cop angry at centre
    ma "No, absolutely not."
    hide mac
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Mackenzie does not agree that it's a brilliant idea.)"
    hide ghostmc
    show mac cop angry at left3
    show ghostmc casual sad at right3
    "She's glowering at me, now, and the longer I keep pushing for this the worse it gets."
    hide mac
    hide ghostmc
    show diego glassesdoctor sad at right4 behind jd
    show razi casual sad at left4 behind jd
    show jd casual surprised at centre
    "Based on the weird looks she's getting from the others, I'm not the only one confused."
    hide jd
    hide razi
    hide diego
    show ghostmc casual angry at centre
    ghostmc "Seriously, why not?"
    show ghostmc casual surprised
    ghostmc "That vampire didn't even see me! I can just head into the forest and do a quick head-count."
    show ghostmc casual sarcastic
    ghostmc "It's... not how I expected to be spending my afternoon, when I woke up this morning, but other than that..."
    show ghostmc casual sarcastic at right3
    show mac cop angry at left3
    ma "I'm not sending you alone into the forest, [genericfn]- certainly not to spy on vampires."
    ma "It's way too dangerous."
    show ghostmc casual basic
    "I stare blankly up at her for a good long moment, utterly dumbstruck."
    show ghostmc casual_cu surprised_cu at ghostmc_cu
    hide mac
    "(Did she forget, or something?)"
    hide ghostmc
    show mac cop sad at centre
    "Mac winces."
    ma "I- I know that sounds-"
    "She sighs, pinching the bridge of her nose."
    ma "You're a ghost, but that doesn't mean you're actually invincible."
    show mac cop angry
    ma "When Grace shows up tomorrow, I don't want to have to tell her that she just missed her sister because I put her in harm's way."
    ma "Again."
    show mac cop angry at left3
    show ghostmc casual sad at right3
    ghostmc "Mackenzie..."
    hide mac
    show diego glassesdoctor sad at left3
    di "Mackenize... does actually make a good point."
    di "Whatever masked you from the messenger might not work against his mistress- in fact, I'd be astonished if it did."
    hide diego
    show razi casual sad at left3
    ra "And if you do get caught, there's rituals, wards, salt circles- ghosts aren't completely untouchable. You could find yourself trapped, or exorcised."
    hide razi
    show jd casual angry at left3
    jd "Oh, absolutely do NOT get exorcised."
    hide jd
    hide ghostmc
    $menuhideborder = True
    menu ge5c1:
        "1. Why not?":
            $menuhideborder = False
            show jd casual angry at left3
            show ghostmc casual surprised at right3
            ghostmc "Why not?"
            show ghostmc casual sarcastic
            ghostmc "Specifically, I mean. What would happen?"
            show jd casual basic at left3
            show ghostmc casual surprised at right3
            jd "Well, you'd go to hell, which isn't great."
            show ghostmc casual sad
            ghostmc "...Because of the eternal torture?"
            show jd casual sad
            jd "Worse- you'd probably have to talk to my dad at some point."
            show jd casual basic
            jd "There's torture too, though, yeah."
            hide jd
        "2. I wasn't planning on it.":
            $menuhideborder = False
            show ghostmc casual sarcastic at centre
            ghostmc "It's not exactly on my bucket list, JD."
            show ghostmc casual_cu surprised_cu at hiflmc_cu
            "(Wait...)"
            show ghostmc casual_cu angry_cu at hiflmc_cu
            "(My bucket list!)"
            show ghostmc casual_cu angry_cu at hiflmc_cu
            "(Damn it! I never got that Australian beach trip.)"
            show ghostmc casual_cu sarcastic_cu at hiflmc_cu
            "(I wonder if it still counts if I get my sister to do that stuff in my place?)"
        "3. I was planning on it.":
            $menuhideborder = False
            show ghostmc casual angry at centre
            ghostmc "Oh, you know what? I was actually looking forward to getting exorcised, but now that you've told me not to, I think I simply won't."
            hide ghostmc
            show jd casual surprised at centre
            "JD blinks, taken aback by the sudden bite in my voice."
            hide jd
            show ghostmc casual_cu sad_cu at hiflmc_cu
            "...I am too, if I'm being honest."
            show ghostmc casual sad at centre
            ghostmc "...Sorry. I'm having a bad day. I shouldn't take it out-"
            show ghostmc casual sad at right3
            show jd casual basic at left3
            jd "Nah, I get it."
            hide jd
    show ghostmc casual sarcastic at centre
    ghostmc "Okay, so maybe I'm not actually immortal- but so what?"
    show ghostmc casual angry at centre
    ghostmc "I just watched a vampire declare war on the town! Am I supposed to just sit around while you all get Capri Sunned?"
    show ghostmc casual angry at right3
    show diego glassesdoctor basic at left3
    di "You could."
    show ghostmc casual surprised at right3
    ghostmc "What?"
    hide diego
    show mac cop sad at left3
    ma "You don't owe us, or this town, a single thing, [genericfn]."
    ma "I don't know why you'd even {i}want{/i} to help us. You've... earned your rest."
    hide mac
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(What's THAT supposed to mean?)"
    show ghostmc casual angry at right3
    show mac cop sad at left3
    ghostmc "Why the hell wouldn't I want to help you?"
    show ghostmc casual surprised at right3
    ghostmc "You're- we're friends!"
    show ghostmc casual sad at right3
    ghostmc "..."
    show ghostmc casual sarcastic at right3
    ghostmc "Well. Okay, Razi and JD are my friends."
    hide mac
    hide ghostmc
    show razi casual smirk at left3
    show jd casual smirk at right3
    jd "Aw."
    hide jd
    hide razi
    show mac cop surprised at left3
    show ghostmc casual angry at right3
    ghostmc "But I know you and the doc, and it'd suck if you died, too!"
    show ghostmc casual sarcastic
    ghostmc "Also, in case you forgot: You all saved my sister's life."
    show ghostmc casual angry
    ghostmc "If you're looking for a reason I should help you, that's the only one I'll ever need."
    show mac cop sad at left3
    ma "You- you don't owe us for-"
    ghostmc "Yes. I do."
    "I don't leave any room for argument, and Mac actually seems to relent, my point finally hitting home."
    hide mac
    show ghostmc casual_cu happy_cu at hiflmc_cu
    "(Never argue with a big sister.)"
    hide ghostmc
    show mac cop happy at centre
    ma "...Okay. Thank you. We could definitely use the help."
    show mac cop smirk at centre
    ma "I see where Grace gets her attitude from."
    hide mac
    show ghostmc casual happy at centre
    ghostmc "Does that mean I made the team? Sign me up to the..."
    show ghostmc casual sarcastic at centre
    ghostmc "Do you guys have like, a superhero team name, or...?"
    show ghostmc casual sarcastic at right3
    show jd casual smirk at left3
    jd "We've got a group chat."
    show ghostmc casual surprised at right3
    ghostmc "Really? Send me an in-"
    show ghostmc casual sarcastic at right3
    ghostmc "Wait, I don't have hands."
    show ghostmc casual sad at right3
    ghostmc "...Or a phone."
    show ghostmc casual angry
    ghostmc "Yep, this still sucks."
    hide jd
    show diego glassesdoctor sad at left3
    di "You're... not missing much."
    "Diego uses his enviably solid hands to pull a phone from his pocket, and, after a few taps, lets me take a peek at the screen."
    show groupchat at bg with dissolve
    "He scrolls up a ways through the history, but it seems to be mostly a space for JD to make monster jokes, and everyone else to tell them to shut it."
    "Grace's face shows up a few times, too, but her messages are far and few between."
    show ghostmc casual surprised at right3
    show diego glassesdoctor sad at left3
    hide groupchat with dissolve
    ghostmc "'Havenfall's Finest?'"
    show ghostmc casual happy at right3
    ghostmc "Aw, you {i}do{/i} have a superhero team name."
    show diego glassesdoctor angry
    di "We do not."
    hide diego
    show jd casual smirk at left3
    jd "We totally do."
    hide jd
    hide ghostmc
    show mac cop basic at centre
    stop music fadeout 0.5
    pause 0.5
    play music getitdone
    "Mackenzie clears her throat, cutting through the banter."
    ma "Alright- if we're doing this, then let's do it."
    ma "We need to prepare for a fight."
    show mac cop angry at centre
    ma "Davies- help Razi ward the bowling alley."
    show jd casual smirk at left3
    show mac cop basic at right3
    "JD makes a gesture that is very technically a salute."
    jd "Yes ma'am."
    hide mac
    show razi casual sad at right3
    ra "...You can help. Just don't try to drink the holy water, again."
    show jd casual basic at left3
    jd "Yeah, it tasted pretty bad."
    show razi casual angry at right3
    ra "That's because it burned your tongue off."
    hide razi
    hide jd
    "The two head off into the bowling alley, bickering as they go."
    show mac cop basic at centre
    ma "Diego, can you run over what you know about Labasque with me, again?"
    show diego glassesdoctor sleep at left3
    show mac cop basic at right3
    di "Certainly."
    show diego glassesdoctor angry at left3
    di "I suspect I could fill several books with what I know of Liliane Labasque."
    ma "I'll take an abridged version, please."
    hide diego
    show mac cop basic at left3
    show ghostmc casual basic at right3
    "Then she turns to me."
    ma "And [genericfn]..."
    show mac cop smirk 
    "She smirks, and points off into the distance, more or less in the direction of the big water tower on the edge of town."
    ma "Camp's that way."
    show mac cop basic 
    ma "I'd offer to drive you to the forest's edge, but..."
    show mac cop basic at left3
    show ghostmc casual sad at right3
    ghostmc "I'd just fall out of the car."
    ma "Try to get an estimate of how many we're dealing with."
    ma "If any of them happen to be chatting about secret battle tactics out in the open, that'd be great too."
    show ghostmc casual angry at right3
    ghostmc "Got it."
    hide mac
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(Time to haunt some vampires.)"
    hide mac
    hide ghostmc
    ##Make a point about how mc is joining the team officially- she wants to help, like her sister did.
    ##Joke about group chat. I dunno, figure it out.
    show bg nolovers_lane_day with fade
    stop music fadeout 0.5
    pause 0.5
    play music hifleveryday
    "It doesn't take particularly long for me to start seeing signs of the coven."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(The way Mackenzie had been talking, I'd expected some kind of secret army, hiding atop the trees and building spike-traps.)"
    show ghostmc casual_cu surprised_cu
    "(Forget hiding- these guys aren't even trying to be subtle!)"
    hide ghostmc
    "I all but walk into a group out in the open, a gaggle of teens standing around in a circle, discussing the merits of various blood types."
    $sidecharone = "Preppy Vampire"
    $sidechartwo = "Jock Vampire"
    $sidecharthree = "Goth Vampire"
    sid1 "No, never serve guests O Positive- it's literally pleb tier."
    sid2 "What? What's wrong with-"
    sid3 "Don't listen to her- nothing's wrong with O-Pos. She's just trying to get you to buy into that weird AB-Neg pyramid scheme."
    sid1 "I keep telling you, it's {i}not{/i} a pyramid scheme!"
    "She punctuates this by angrily stamping a foot."
    sid1 "AB Negative blood is clinically proven to-"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I hate to interrupt this meeting of the minds, but...)"
    show ghostmc casual happy at centre
    ghostmc "Hello, fellow teens. Can {i}I{/i} buy some blood?"
    hide ghostmc
    "The teens (who could all be older than me, I have to remind myself) don't so much as twitch when I address them."
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(Guess they can't see me.)"
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(What's going on? Doctor Escalona can see me just fine, so why can't these vampires?)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(There must be something I'm missing here.)"
    hide ghostmc
    "The thought is actually a little encouraging, but I don't stop to ponder the implications of my ghost rules having wiggle-room."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I've got less than nine hours before people in town start getting non-consensual neck piercings.)"
    show ghostmc casual_cu angry_cu
    "(I have recon to do.)"
    hide ghostmc
    "Mackenzie had guessed right- there's definitely more than a couple dozen vampires in the forest."
    show girl1 casual vampirebasic at right3
    show vampguy casual humanbasic at left3
    "I keep on pushing soundlessly through the brush, and I encounter more and more of them the closer I get to the middle of their encampment."
    "It's mostly a bunch of tents, with the odd tarp and blanket stretched out on the ground, occupied by bored vampires having hushed conversations."
    "One thing makes itself clear very quickly:"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    hide girl1
    hide vampguy
    "(This... doesn't really look like an army.)"
    hide ghostmc
    show girl1 casual vampireangry at right3
    show vampguy casual humansurprised at left3
    "It seems like just about everyone around me is exhausted, snappish, and having a generally shitty time."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    hide girl1
    hide vampguy
    "(I don't know what I had expected- screaming drill sergeants and groups of burly dudes sparring in a ring?)"
    show ghostmc casual_cu sad_cu
    "(Cages full of crying humans?)"
    show ghostmc casual_cu sarcastic_cu
    "(Diego had made it sound like I'd probably find human 'cattle', but that particular feature seems to be absent here.)"
    hide ghostmc
    show swmgirl4 casual basic at centre
    "There are a few humans, though- or at least, non-vampires, with natural eye tones rather than the deep reds shared by the undead residents."
    show boy1 casual vampirebasic at centre
    show swmgirl4 casual basic at right2 behind boy1
    "They don't seem to be prisoners, exactly, but each is paired with a particular vampire,"
    show swmgirl4 casual happy at right2 behind boy1
    "following them around, and spending a concerning amount of time gazing blissfully at the backs of their heads."
    hide swmgirl4
    hide boy1
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Creepy.)"
    hide ghostmc
    "I've passed by a number of those tents before I remember that etiquette doesn't really apply to ghosts, and that I could try sticking my head inside."
    "Of course, most seem to have closed flaps, made of a light canvas material that nonetheless doesn't budge an inch when I try to push on it."
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...Damn it.)"
    show ghostmc casual_cu angry_cu
    "(Lives are at stake. I can't half-ass this.)"
    "(Grow up, [genericfn]. You're a ghost, so act like one.)"
    hide ghostmc
    "I pick the closest tent, close my eyes, and take a big step right through the wall."
    show bg blackscreen with dissolve
    "The sensation is vaguely like being scraped gently with sandpaper, but over my whole body."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(I can't decide if it's nice or horrific.)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(That's been the vibe of this whole ghost thing so far, to be honest.)"
    hide ghostmc
    show bg tentclosed with dissolve
    "Once I'm pretty certain all of me is inside the tent, I finally open my eyes to take a peek."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(...And, of course this one's empty.)"
    hide ghostmc
    "Five tents later, and I have to admit that phasing through solid matter isn't as terrifying as I'd made it out to be."
    show ghostmc casual_cu happy_cu at hiflmc_cu
    "(It's actually kinda fun, so long as I don't end up inside a person.)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I'm never doing that again.)"
    hide ghostmc
    "On the other hand, I haven't really learned anything useful, either."
    "Only three of the tents I check even have occupants, with not a one of them discussing military strategy."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Unless the couple I saw snuggling together in the same sleeping bag were having a {i}very{/i} different conversation than what I suspected.)"
    hide ghostmc
    show bg nolovers_lane_day
    show liliane casual_cu angry_cu at liliane_cu
    with dissolve
    "I exit the latest tent, only to find myself standing nose-to-nose with one of the locals."
    show ghostmc casual surprised at right1
    show liliane casual angry at left1
    show ghostmc casual surprised at right3 with ease
    "I'm getting pretty good at avoiding collisions, so I quickly sidestep- but instead of walking past, she just stops in place, and stares right at me."
    hide liliane
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(She can't... see me, right?)"
    hide ghostmc
    show liliane casual happy at centre
    $sidechartwo = "Vampire"
    "The vampire seems to come to a conclusion, and an easy-going smile suddenly lights up her face."
    sid2 "Well, hey there, little ghost!"
    hide liliane
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(She {i}can{/i} see me!)"
    show ghostmc casual_cu sad_cu
    "(...Maybe?)"
    hide ghostmc
    show liliane casual angry at centre
    "She squints in my general direction as if I were way off in the distance, her eyes finally settling on what I sincerely hope she thinks is my face."
    hide liliane
    show ghostmc casual_cu blush_cu at hiflmc_cu
    "(She's, uh. Off by a few inches.)"
    show liliane casual happy at left3
    show ghostmc casual blush at right3
    "The woman is {i}tall{/i}, and jaw-droppingly gorgeous- the kind of person I'd probably love to have stare at me like that, in a different context."
    hide liliane
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Part of that context being, 'both of us are alive'.)"
    $sidechartwo = "Vampire"
    hide ghostmc
    show liliane casual basic at centre
    sid2 "So, you lost? Or just skeeving on my people for the heck of it?"
    hide liliane
    hide ghostmc
    "My shock at somehow ending up in a conversation with the enemy is briefly overridden by sheer indignation."
    show ghostmc casual angry at centre
    ghostmc "I'm not 'skeeving' on anyone!"
    hide ghostmc
    "Then my brain catches up."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "('Her' people?)"
    $sidechartwo = "Liliane Labasque, maybe?"
    hide ghostmc
    show liliane casual basic at centre
    sid2 "You're kinda a runt, huh? You a kid, or just short?"
    show liliane casual angry
    "Her face darkens at the thought."
    hide liliane
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(I guess even vampires who take human thralls can agree that dead kids are bad.)"
    show ghostmc casual sarcastic at centre
    ghostmc "Neither. My eyes are up here."
    show ghostmc casual sarcastic at right3
    show liliane casual basic at left3
    sid2 "Oh."
    "She adjusts her gaze up a bit, but I can tell she's just guessing from the way her eyes don't really stay in one spot."
    hide ghostmc
    hide liliane
    show swmgirl4 casual surprised at right3
    show girl1 casual vampirebasic at left3
    "Based on the weird looks we're getting from nearby curious onlookers, I get the feeling that she's the only one who can even tell I'm here at all."
    hide girl1
    hide swmgirl4
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(I'm invisible to everyone except a handful of supernaturals in town, and also this one random vampire in the forest can kinda see me.)"
    show ghostmc casual_cu angry_cu
    "(The rules on how my new body works are starting to feel a little arbitrary.)"
    show ghostmc casual basic at centre
    ghostmc "Are you Liliane Labasque?"
    show ghostmc casual basic at right3
    show liliane casual happy at left3
    li "Guilty as charged!"
    show liliane casual basic
    li "I've gotta ask- wasn't one of my boys that got you, right?"
    li "Because that would make this awkward."
    hide liliane
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(That was a little blunt, but okay.)"
    show ghostmc casual basic at right3
    show liliane casual basic at left3
    ghostmc "I don't think so."
    show ghostmc casual sad at right3
    ghostmc "The ones who, uh. 'Got' me, didn't have a coven."
    li "Yeah, that tracks. My people don't leave bodies, not if they want to keep being my people."
    show liliane casual happy
    li "Begs the question, though- what brings you to my home away from home, little ghostie?"
    li "Is this haunting business, or pleasure?"
    hide liliane
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(I was {i}really{/i} not prepared for this. What do I even tell her?)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(...I mean, I guess it wouldn't hurt to just ask the obvious.)"
    show ghostmc casual basic at centre
    ghostmc "Business, I guess?"
    ghostmc "Is there any chance I could convince you to not do the war thing with Havenfall?"
    show ghostmc casual sad
    ghostmc "Uh. Please?"
    hide ghostmc
    show liliane casual angry at centre
    stop music fadeout 0.5
    pause 0.5
    play music diego
    "Liliane's eyes narrow, and she straightens from her casual, affected slouch to loom over me."
    hide liliane
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(If I wasn't, you know, intangible, I'd probably be pretty intimidated.)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(...I might be a little intimidated anyway.)"
    hide ghostmc
    show liliane casual angry at centre
    li "Oh. You're part of Hunt's little gang, are you?"
    show liliane casual angry at centre
    li "Figures. The cute ones are always a pain in the ass."
    show liliane casual angry at left3
    show ghostmc casual sarcastic at right3
    ghostmc "You literally have no idea what I look like."
    li "I'll tell you what I've told your Sheriff a hundred times, then- we're not wolves. We're not going to live in the forest like animals." 
    show ghostmc casual surprised
    ghostmc "So you're seriously going to war because Mackenzie isn't letting you stay in town?"
    "Liliane scoffs."
    li "We can't stay in town, step foot in town, look at the town- Get Hunt going and she'll say we can't even think about the damn town."
    li "All because, years ago, this poor little human got her neck torn out by some..."
    hide ghostmc
    show liliane casual basic at centre
    "Liliane blinks, her lips parting into an 'o' of surprise as she connects a few dots."
    show liliane casual basic
    li "...Was that you?"
    show ghostmc casual sarcastic at right3
    show liliane casual basic at left3
    ghostmc "Guilty as charged."
    show liliane casual sad
    "Liliane winces."
    li "Yeah, okay. Sorry. Didn't mean any offense- not usually one to make light of the dead, especially not to their face."
    show liliane casual basic
    li "That makes you [genericfn], right? The {i}other{/i} [genericln] girl."
    show ghostmc casual surprised
    ghostmc "You know Grace?"
    show liliane casual happy
    "Liliane laughs, though it sounds a little too sharp to be entirely genuine."
    show liliane casual basic
    li "Who doesn't." 
    li "She's dusted a few too many of my boys for me to say I {i}like{/i} her, particularly, but she's got a good head on her shoulders."
    ghostmc "'Dusted'?"
    hide ghostmc
    show liliane casual basic at centre
    "With her hands, Liliane mimes something that looks like a balloon popping, or a little explosion, and she makes a 'poof' sound."
    li "When vamps die, we turn to ash."
    li "Plus side: Makes cleanup real easy."
    show ghostmc casual sad at right3
    show liliane casual basic at left3
    ghostmc "...So my sister's killed some of your people?"
    hide liliane
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(I knew she was a vampire hunter-)"
    show ghostmc casual_cu sarcastic_cu
    "(Sorry, 'freelance supernatural problem solver'-)"
    show ghostmc casual_cu sad_cu
    "(But it's still so hard to believe my baby sister has actually killed people.)"
    hide ghostmc
    show liliane casual basic at centre
    "Liliane waves it off."
    li "No hard feelings, really- can't say any of them didn't deserve it."
    "She sighs wearily, and crosses her arms over her chest."
    show liliane casual angry
    li "'Course, if you're here, then I guess Grace'll be showing up sooner or later, too. Can't say I'm looking forward to tussling with her."
    hide liliane
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "('Tussling?')"
    show ghostmc casual_cu angry_cu
    "(Oh, no. There will be no 'tussling' with my sister.)"
    show liliane casual sad at left1 behind ghostmc
    show ghostmc casual angry at right1
    "Before I can think twice about it, I'm an inch away from Liliane's face, poking her hard in the chest with my index finger."
    ghostmc "No."
    ghostmc "You're {i}not{/i} touching Grace."
    show liliane casual sad at left3 with ease
    "I've reached all the way down into Liliane's heart before she reacts to my proximity, with a hurried step back and a yelp of disgust."
    show liliane casual angry
    li "Jesus- that feels fucking weird!"
    ghostmc "I said-"
    li "Yeah, I heard you!"
    li "Look, like I said- I don't have anything against the woman."
    li "But if she shows up to keep me and my people from getting out of this fucking forest, then I'll drain her dry."
    li "Don't like it? Then make sure I don't have to."
    hide liliane
    hide ghostmc
    #show ghostmc casual_cu angry_cu at hiflmc_cu
    "I can actually feel the exact moment where, in life, I would have gone ballistic."
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(The fact that she's an unfathomably ancient vampire wouldn't have held much weight against her threat to {i}kill{/i} my sister.)"
    show ghostmc casual basic at centre
    "But like earlier, in the bowling alley, I'm able to more or less keep my cool." 
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Actually, I'm starting to get the sneaking suspicion that I don't have any other option.)"
    show ghostmc casual sarcastic at right3
    show liliane casual angry at left3
    ghostmc "Pretty sure that if she shows up, it'll be to stop you from draining the {i}town{/i} dry."
    hide ghostmc
    show liliane casual angry at centre
    "Liliane throws her hands up, looking deeply exasperated."
    li "Oh, for fuck's- I'm not going to hurt the little humans!"
    li "Hell, most of us are loaded- your small business owners are going to {i}love{/i} us."
    hide liliane
    show ghostmc casual surprised at right3
    show liliane casual angry at left3
    ghostmc "So Dr. Escalona was wrong? Havenfall's big enough to support the coven safely?"
    hide liliane
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Not sure how it'd be safe to have a group of people randomly biting folks, even if there {i}was{/i} enough blood to go around, but I'll defer to the doc.)"
    hide ghostmc
    show liliane casual basic at centre
    "That gives Liliane pause. She shakes her head slowly, her face grim."
    li "...No, Diego's right. Not gonna deny that if we stuck around too long, Havenfall would probably end up a ghost town."
    li "Well, more than it already is."
    show liliane casual basic at left3
    show ghostmc casual sarcastic at right3
    ghostmc "Oh, good one."
    show liliane casual sad
    li "What? No, I didn't mean-"
    show liliane casual angry
    "She huffs in frustration."
    
    li "Look, it doesn't matter, because we were never going to stay long enough to do any real damage."
    li "All I want is to keep what's left of my people safe and fed while I figure out how to take back-"
    show liliane casual sad at left4 with ease
    "Then she cuts herself off, eyes widening as she jerks back, as if from an open flame."
    li "Why am I even-"
    show liliane casual angry
    li "What do you think you're doing?"
    show ghostmc casual surprised
    ghostmc "Huh?"
    hide ghostmc
    hide liliane
    "I whip my head around to try and spot whatever's freaked her out, but the only thing behind me is that empty tent."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Anyway, what was she saying about her people? Did something happen to them?)"
    "(If this is 'what's left of her people', then how big was her coven {i}before{/i} that!?)"
    hide ghostmc
    show liliane casual happy at centre
    li "Tricksy one, aren't you?"
    "She's wearing that easy smile from earlier, but her tone has completely changed- now, she sounds as cold and hard as steel."
    li "Clever- but you're not getting anything else out of me, ghostie girl."
    hide liliane
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(What tricks? I literally just asked.)"
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Is she just pissed off she let something slip?)"
    show ghostmc casual_cu angry_cu
    "(How is that my fault?)"
    hide ghostmc
    show liliane casual angry at centre
    li "Now get the fuck out of my camp, or I'll exorcise you."
    show ghostmc casual surprised at right3
    show liliane casual angry at left3
    ghostmc "Is that a real thing?"
    li "You wanna find out?"
    hide liliane
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(I really don't!)"
    hide ghostmc
    hide liliane
    "I turn to leave..."
    show liliane casual angry at centre
    "...And have to turn right back around to face the quietly fuming Liliane, because I have a small problem."
    show ghostmc casual sad at right3
    show liliane casual angry at left3
    ghostmc "Uh. This is gonna sound stupid, but..."
    li "What."
    ghostmc "I... might be kinda lost?"
    hide liliane
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(I had been so focused on finding the vampires that I had forgotten to pay attention to exactly where I was walking.)"
    hide ghostmc
    "Lush greenery stretches before me in all directions, beautiful and yet identical to pretty much any other stretch of forest on the planet."
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(Dying has changed me in a lot of ways that I'm still figuring out, but I guess we can rule out any improvements to my IQ.)"
    hide ghostmc
    show liliane casual basic at centre
    li "You're lost."
    "That tight anger ebbs from Liliane's face, or at least is more easily masked by her sheer astonishment."
    show liliane casual sad
    li "How does a ghost get lost?"
    show liliane casual sad at left3
    show ghostmc casual angry at right3
    ghostmc "I'm new!"
    li "Can't you just float out of here?"
    "She points skyward."
    show liliane casual angry
    li "Go up and look around- I'm not going to hold your hand."
    ghostmc "No, I can't {i}float{/i}."
    hide liliane
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(...Actually, hold up, {i}can{/i} I float?)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(That's like, one of the top three things that a ghost does.)"
    hide ghostmc
    "I take a look down at my feet, which appear to be planted quite firmly on the ground- albeit with one of my shoes partially embedded in a large rock."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(For that matter, how am I even standing on the ground?)"
    show ghostmc casual_cu sad_cu at hiflmc_cu
    "(Shouldn't I be falling right through it, like everything else?)"
    play music "<from 2>audio/hifl/suspense.mp3"
    show ghostmc casual surprised at centre
    show ghostmc casual surprised at ghostdrop1 with ease
    "I regret having that thought {i}immediately{/i}, when I actually do begin to lurch downwards."
    ghostmc "Oh, shit-"
    show ghostmc casual surprised at ghostdrop2 with ease
    "My lurch becomes an outright fall and, within moments, I've slipped completely below the forest floor."
    
    
    # show ghostmc casual glassesbasic at centre
    # "Once everyone's left, I just kinda... stand there, right in front of my tombstone."
    # show ghostmc casual glassesangry at centre
    # "I stand there, and I try my darnedest to conjure up an actual feeling about it."
    # show ghostmc casual_cu glassessarcastic_cu at hiflmc_cu
    # "(I'm pretty sure it's supposed to make me feel sad, or something.)"
    # show ghostmc casual_cu glassessarcastic_cu
    # "(Mostly, I feel a little grossed out.)"
    # show ghostmc casual_cu glassessurprised_cu
    # "(Am I really just decomposing down there?)"
    # show ghostmc casual_cu glassessad_cu
    # "(Ugh, I could actually look, if I wanted, since I apparently don't need light to see. What a horrible thought.)"
    # "(...And strangely tempting.)"
    
    # hide ghostmc
    # "I'm just considering whether or not to make the worst decision of my unlife, when I suddenly become aware of the grass crunching right behind me."
    # show ghostmc casual glassessurprised at centre
    # "I whip around to see..."
    # show ghostmc casual glassessurprised at left3
    # show grace casual basic at right3
    # stop music fadeout 0.5
    # pause 0.5
    # play music gracehunter fadein 0.5
    # gr "...Hi, sis."

    # show grace casual basic at centre
    # "But she's not looking at me."
    # hide grace
    # show ghostmc casual_cu sad_cu at hiflmc_cu
    # "(...No. She's just looking at a different me.)"
    $ tobecontinued()
    show bg hifltbc at bg with fade
    pause

    $ resets()
