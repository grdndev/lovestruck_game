label arianna_season2_episode3:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_beach_bar_day at bg
    play music mscsadtimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "Arianna has gone to reason with a political extremist and I, needing to distract myself from that fact, head to Jerry's."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I wish Arianna didn't have to meet with Casper. The guy looks like bad news.)"
    hide mscmc
    show maxime casual basic at left1plus
    show dawn casual grin at right2
    "Maxime and Dawn are at the bar counter, smoothies in hand."
    hide maxime
    hide dawn
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I haven't seen Maxime since he arrested Mia/Emporia for the mer government.)"
    hide mscmc
    show jerry casual smile at centre
    "As Jerry waves to me from behind the bar, Dawn and Maxime turn around."

    hide jerry
    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show maxime casual smile at left1plus
    show dawn casual grin at right2
    dw "Hey, surfer girl."
    "Dawn pats the stool next to them."
    hide maxime
    hide dawn
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Dawn and Maxime are best friends...Do they even know Maxime's a merman? Are they also a merperson?)"
    hide mscmc
    show jerry casual smile at centre
    jr "No Arianna with you today?"
    hide jerry
    show mscmc jacket_hairdown smile at left1plus
    show dawn casual basic at right2
    "I plop down next to Dawn."
    mcarianna basic "She's busy today."
    hide dawn
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(At least Arianna has Queenie there. For a grandma she seemed like she could hold her own in a dicey situation.)"
    show mscmc jacket_hairdown basic at left1plus
    show maxime casual basic at right3
    mx "How's the shop?"
    mcarianna smile "Trina's holding down the fort."
    "Maxime glances at his smoothie and takes a sip nonchalantly, he's got the government agent poker face down pretty good."
    hide maxime
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(I still can't believe that he's a merman and works for the mer government.)"
    show mscmc jacket_hairdown basic at left1plus
    show maxime casual basic at right3
    mcarianna "Are you teaching a lot of surf classes today?"
    mx smile "Two. One in about an hour."
    hide maxime
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Arianna told him {i}I'm{/i} half-mer so the government wouldn't realize a human knows about merpeople stuff.)"
    "(I'm not totally sure he bought it, but he doesn't seem to be looking into the claim or anything.)"
    show mscmc jacket_hairdown smile at left2
    show jerry casual basic at right2
    jr "What're you having today, [genericfn]?"
    show jerry smile
    mcarianna grin "Jerry's special Smoothie of Madness, of course."
    "Jerry grabs a tall glass and beams at me. He loves it when people order his namesake smoothie."
    jr "Good taste."
    hide jerry
    show maxime casual basic at right3
    mcarianna smile "What've you guys been up to?"
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I really need to distract myself from thinking about Arianna.)"
    hide mscmc
    show jerry casual smile at left2
    show dawn casual smile at right2
    dw "Jerry was just catching us up on his love life."
    hide jerry
    hide dawn
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "I feel my eyebrows shoot up."
    mcarianna grin_cu "Whaaaat? You have a girl?"
    hide mscmc
    show jerry casual smile at centre
    "Jerry laughs and shakes his head as he slices up a banana on a cutting board."
    jr "I'm working on it, okay?"
    hide jerry
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(God, me too, Jerry. It's rough out here.)"
    show mscmc jacket_hairdown grin at left1plus
    show jerry casual basic at right3
    mcarianna "Do I know her?"
    jr smile "I don't think so. You might've seen her at the bar before."
    jr sad "Her name's Allegra."
    hide jerry
    show dawn casual embarrassed at right2
    dw "{i}Allegra{/i}. He's in love."
    hide mscmc
    hide dawn
    show jerry casual smile at centre
    "Jerry ducks his head and dumps different fruits into the blender."
    hide jerry
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I wonder if that's what I look like when I talk about Arianna.)"
    show mscmc jacket_hairdown smile at left1plus
    show jerry casual sad at right3
    jr "She's...pretty amazing."
    jr smile "She's a single mom and super fun."
    show jerry sad
    mcarianna grin "Does she know you like her?"
    show jerry angry
    "Jerry starts the blender and holds up a finger for us to wait until the sound is gone."
    hide mscmc
    hide jerry
    "When the smoothie is blended, he pours the purple drink into the tall glass and slides it over to me with pride in his work."
    show mscmc jacket_hairdown smile at left1plus
    show jerry casual smile at right3
    jr "I think she knows. We've hung out a few times."

    hide jerry
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I know this talk is for Jerry, but I may definitely keep in mind what everyone's advice is going to be.)"
    "(She knows I like her, right? I think she likes me too. It's just neither of us has just...)"
    hide mscmc
    show jerry casual sad at left2
    show dawn casual embarrassed at right2
    jr "I want her to know that I'm serious. Like, take it from casual little dates here and there to, she's mine and I'm hers."
    show jerry smile
    dw grin "Grand! Gesture! You need a grand gesture, my friend."
    jr sad "I just don't know what."
    "Jerry rests his elbows on the counter and rubs his hands over his face."
    hide jerry
    hide dawn

    $ menuhideborder = True
    menu ariannas2e3c1:
        "A. A fancy dinner?":
            $ menuhideborder = False
            show mscmc jacket_hairdown grin at left1plus
            show jerry casual basic at right3
            mcarianna "Maybe take her out for a really fancy dinner?"
            show mscmc sad
            jr sleep "We've gone to a nice place before. I jsut blew it cuase I didn't kiss her after when I walked her to her door."
            hide mscmc
            hide jerry
            show dawn casual grin at centre
            dw "Needs more spice."
            hide dawn

        "B. I think flowers are a good start.":
            $ menuhideborder = False
            show mscmc jacket_hairdown grin at left1plus
            show jerry casual basic at right3
            mcarianna "I think flowers are always nice."
            hide mscmc
            hide jerry
            show maxime casual smirk at centre
            mx "Yeah, lots of flowers, like an overwhelming amount."
            hide maxime
            show mscmc jacket_hairdown smile at left1plus
            show jerry casual sad at right3
            mcarianna "But, I get wanting there to be more to the gesture than that."

        "C. What kind of stuff is she into?":
            $ menuhideborder = False
            show mscmc jacket_hairdown smile at left1plus
            show jerry casual basic at right3
            mcarianna "Well, what kind of stuff is she into?"
            show jerry smile
            mcarianna grin "There's loads of things to do and see around here. Maybe, like, a day trip?"

    show mscmc jacket_hairdown smile at left1plus
    show jerry casual smile at right3
    jr "I want to do something {i}special{/i} special, you know?"
    mcarianna surprised "Yeah...I feel you."
    hide jerry
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I should do a grand gesture with Arianna. I have to show her I {i}like{/i} her!)"
    show mscmc jacket_hairdown sad at left1plus
    show jerry casual basic at right3
    jr "I want to be there for her, intentionally move in ways that show her my feelings and make her feel appreciated, ya know?"
    hide jerry
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Jerry, you are going to make me cry in this beach bar...)"
    hide mscmc
    show jerry casual_cu smile_cu at jerry_cu
    jr "Phew, I haven't felt like this in years."

    hide jerry
    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show dawn casual_cu embarrassed_cu at dawn_cu
    dw "Hell, I'll watch the bar! Go get her, right now! You have to!"
    show jerry casual smile at left2
    show dawn casual surprised at right2
    jr "I am not leaving my bar in your hands, Dawn. No offense."
    hide jerry
    hide dawn
    show mscmc jacket_hairdown basic at centre
    "I push my drink towards Jerry and firmly push my chair back as I stand with determination."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I'm going to swim to Arianna's studio and surprise her when she gets back.)"

    stop music fadeout 0.5
    play music mscsurfcompetition fadein 1.0
    "(I've got the magic shell now, nothing's stopping me. I'm going to get my girl!)"
    show mscmc jacket_hairdown basic at left1plus
    show dawn casual smile at right2
    dw "Leaving already?"
    hide mscmc
    show jerry casual basic at left2
    jr "You've been thinking about Arianna, haven't you?"
    show jerry smile
    show dawn grin
    "Dawn raises an eyebrow at me and my face flushes."
    hide jerry
    hide dawn
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Am I that obvious? Jeez, guys, let a girl think she's got a little mystery to her.)"
    mcarianna surprised_cu "No...Well..Yeah."
    hide mscmc
    show jerry casual smile at left2
    show dawn casual embarrassed at right2
    jr "Don't let us stand in the way of love."
    hide jerry
    hide dawn
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Whatever you decide, Jerry, let me know how it goes with {i}Allegra{/i}."
    mcarianna sad_cu "No matter what, I think she'll be able to see how much you care."
    hide mscmc
    show jerry casual smile at left2
    show dawn casual embarrassed at right2
    dw "Be fearless, [genericfn]."
    "Dawn's eyes twinkle a beautiful sky blue as they say this to me, I get the feeling Dawn loves love."
    hide jerry
    hide dawn
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Fearless. Yes.)"
    show mscmc sad_cu
    "(Oh god.)"

    scene bg msc_mc_bedroom_day at bg with fade
    "I leave the bar and go back to my place to change into my bathing suit."
    play sound knocking
    "I hear Trina's footsteps in the hall and then there's a light knock on my door."
    show trina casual basic at centre:
        alpha 0.0
        pause 0.1
        linear 0.4 alpha 1.0
    "Trina steps in and leans against the door frame, watching me as I grab things and look over at her."
    show mscmc bikini_hairdown smile at left1
    show trina casual smile at right2
    so "Hey."
    mcarianna grin "What's up?"
    show mscmc smile
    show trina basic
    "She shifts her weight onto one leg."
    show mscmc surprised
    so "You okay?"
    hide trina
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(The short answer would be no because of mer politics stuff, but I can't tell Trina that. I wish she just knew everything.)"
    show mscmc basic_cu
    "(I'm just stressed about Arianna and this Casper business. One day I'll tell Trina everything and we'll laugh about it.)"
    show mscmc bikini_hairdown smile at left1
    show trina casual basic at right2
    mcarianna "Why wouldn't I be?"

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show mscmc basic
    "Trina shrugs."
    so sad "I dunno. You seem tense."
    show trina basic
    mcarianna sad "I'm good."
    show mscmc surprised
    so "Is it stuff with Arianna?"
    hide trina
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(I don't want Trina to think I'm shutting her out. I don't want to shut her out.)"
    show mscmc bikini_hairdown grin at left1
    show trina casual basic at right2
    mcarianna "It's not Arianna, we're alright. I'm just overwhelmed with competition sign-ups and scheduling shit."
    so smile "Oh right, it's that time of year, huh. I know, I know."
    mcarianna basic "I'm just heading out to meet Arianna at the beach to finally chill. Nothing's wrong."
    show mscmc sleep
    so "Alright, I've got your back if you need a brawler or anything."
    mcarianna grin "I know, thanks."
    show trina sad:
        pause 0.2
        linear 0.4 xoffset 100 alpha 0.0
    "Trina hovers for a second like she wants to say more, but she leaves and closes the door."
    hide trina
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(It's killing me to lie to Trina. I love that bitch.)"

    stop music fadeout 0.5
    play music mscsurfcompetition fadein 1.0
    scene bg msc_labeach_day at bg with fade
    "I finally make it to the beach, shell in hand, and wade into the water."
    scene bg msc_ocean_wide_day at bg
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    with dissolve
    "(This will be my first time using this shell alone.)"
    show mscmc sleep_cu
    "I take a deep breath and blow it out to psych myself up."
    show mscmc smile_cu
    "(It's just as easy as breathing. I can do this.)"
    hide mscmc
    stop music fadeout 0.5
    play music mscunderwaterromance fadein 1.0
    $ wavy_transition("bg msc_ocean_wide_day", "bg msc_underwater_day")
    scene bg msc_underwater_day at bg with dissolve
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(It's still weird, but I know what I'm doing.)"
    hide mscmc
    "There is a very sweet sense of satisfaction as I start swimming towards Arianna's studio, never having to surface for air."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Look at me, breathing water and shit.)"
    scene bg msc_arianna_studio_day at bg with fade
    "When I get to Arianna's studio, I peek in through the hole in the side of the ship."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(She's not back. Perfect. I can surprise her!)"
    hide mscmc
    "I swim inside and over to half-finished sculptures in the corner."
    "Voice from outside that sounds like Arianna?" "...fine."
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "Arianna's voice in the distance makes my heart leap."
    "(I'm doing this. Grand romantic gesture!)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e3c2:
        "A. Greet Arianna at the entrance.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(I don't want to give Arianna a serious fright.)"
            show mscmc embarrassed_cu
            "As excitement bubbles up inside of me, I start swimming towards the entrance."
            "(I think she'll be proud I used the shell on my own.)"
        "B. Jump out and surprise her.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(It might be a little fun to jump out and surprise her.)"
            "(Or it could give her a heart attack, but all in good nature.)"
            "I swim towards the side of the entrance, ready to pop out."
        "C. Lay yourself out on a table.":
            $ menuhideborder = False
            "I swim over top of one of the tables, and consider possible sultry poses."
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(I'll be all like 'Hey, welcome back. I was waiting for you'.)"
            "(Yeah, that's good!)"

    hide mscmc
    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    "But then the sound of another voice makes me pause. She's not alone."
    qn "Stop being so difficult. It's not like we have you tied up."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(It doesn't sound like Queenie's saying that to Arianna.)"
    hide mscmc
    "Someone who is definitely not Arianna or Queenie" "You two are the ones being difficult."
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Oh shit! Are they bringing the anti-art extremist guy {i}here{/i}?!)"
    "(I need to hide! I'm definitely not supposed to be part of the serious talk they want to have with him.)"
    hide mscmc
    "I swim behind a cluster of sculptures and sculpting materials in the back of the studio."

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    show queenie casual angry at centre:
        xoffset 40 alpha 0.0
        pause 0.2
        linear 0.4 alpha 1.0
    show arianna siren angry at right4:
        alpha 0.0
        pause 0.1
        linear 0.4 alpha 1.0
    show casper casual sleep at left3:
        alpha 0.0
        pause 0.3
        linear 0.4 alpha 1.0
    "Arianna is leading the group as they enter, Casper follows, blindfolded and being led by the arm by Queenie."
    cs "I just don't see why it's completely necessary to blindfold me at this juncture."
    qn "Because you could rat out our location to the govnernment if you know how to get here. We told you, we just want to talk."
    cs "Get on with it then."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(So much for my romantic gesture timing. This could be bad if he sees me, the government isn't hype about humans either.)"
    hide mscmc
    show queenie casual basic at centre:
        xoffset 40
    show arianna siren angry at right4
    show casper casual angry at left3
    "Arianna and Queenie exchange nods before Arianna pulls off his blindfold."
    show casper confused
    "He blinks a few times and then sweeps his gaze over the studio."
    hide queenie
    hide arianna
    show casper casual_cu basic_cu at casper_cu
    "For a frantic second, I think his eyes land on me, huddled behind some stuff in the back."
    hide casper
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Oh nononono.)"
    hide mscmc
    "I duck further down, holding my breath."
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Did he see me?!)"
    hide mscmc
    show queenie casual basic at centre:
        xoffset 40
    show arianna siren basic at right4
    show casper casual confused at left3
    cs "What is this place?"
    show casper smile
    ai angry "A safe place."
    cs angry "Hmph."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Okay, he didn't see me, apparently.)"
    hide mscmc
    show queenie casual basic at centre:
        xoffset 40
    show arianna siren basic at right4
    show casper casual basic at left3
    "I peek around the side of the piece again and see him scowling at Arianna and Queenie."
    show arianna angry
    cs angry "So what do you want?"
    show casper basic
    ai basic "We just want to talk, Casper. Honestly."
    show casper angry
    "His face scrunches into a scowl and he crosses his arms."
    cs "Get it over with. I already know you people's talking points."
    ai "We just want to explain to you why we do the things we do."
    show casper confused
    show queenie smile
    ai "The resistance isn't what you think it is."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Arianna seems so in command and focused, I've only seen her before like this when she does art.)"
    hide mscmc
    show queenie casual sad at centre:
        xoffset 40
    show arianna siren basic at right4
    show casper casual sleep at left3
    qn "You've been misled, Casper. The government has fed you lies your whole life."
    show queenie basic
    cs angry "You really think I'll listen to you two? Pathetic."
    show casper confused
    show queenie smile
    show arianna sleep
    "Arianna rolls her eyes, but Queenie gives her a gentle pat on the shoulder."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(Can a talk like this really work on someone like him?)"
    hide mscmc
    show queenie casual basic at centre:
        xoffset 40
    show arianna siren smile at right4
    show casper casual basic at left3
    ai "Magic and art are means of self-expression and realization."
    show casper confused
    ai "Our power lies in our true selves, and that's why the government restricts our exploration of what we contain within ourselves."
    show casper angry
    ai basic "Magic belongs to the people. The few in power hoard their status and resources by hurting everyone else."
    show arianna basic
    "Arianna looks down at her hand and rubs at her ring."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu angry_cu at mscmc_cu
    "(You tell him, Arianna! Her voice is so sure when she speaks like this, she'd be great at giving speeches.)"
    hide mscmc
    show queenie casual smile at centre:
        xoffset 40
    show arianna siren basic at right4
    show casper casual confused at left3
    ai "It's all about control. Magic and art need to be decriminalized and redistributed so people have control of their lives and identities."
    show casper smile
    "Casper laughs, loud and annoying."
    show casper angry
    qn basic "By helping the government, you're helping them hurt you."
    "Casper points a finger aggressively at Arianna and Queenie."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Unfortunately, it still looks like they aren't getting through to him.)"
    hide mscmc
    show queenie casual angry at centre:
        xoffset 40
    show arianna siren angry at right4
    show casper casual smile at left3
    cs "You two are wrong and going against our governing leaders is a mistake."
    show queenie basic
    show arianna basic
    cs angry "The people shouldn't have magic. It would only be abused. Everything is as it should be."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(He doesn't understand...)"
    hide mscmc
    show queenie casual basic at centre:
        xoffset 40
    show arianna siren angry at right4
    show casper casual smile at left3
    cs "It doesn't matter what you think, you're wrong."
    "Casper turns sharply, the end of his tail nearly hitting Arianna."
    cs "I'm going to turn you two in. I've seen your faces. You'll be arrested and I'll be the one who puts a stop to this resistance."
    hide casper
    hide queenie
    hide arianna
    show mscmc bikini_hairdown_cu angry_cu at mscmc_cu
    "(This isn't good!)"
    mcarianna surprised_cu "Wait!"
    hide mscmc

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show queenie casual smile at centre:
        xoffset 40
    show arianna siren surprised at right4
    show casper casual confused at left3
    "I slap a hand over my mouth as they all turn to the back of the room."
    hide queenie
    hide arianna
    hide casper
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Oh god, why did I do that?!)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e3c3:
        "A. Freeze.":
            $ menuhideborder = False
            show queenie casual smile at centre:
                xoffset 40
            show arianna siren surprised at right4
            show casper casual confused at left3
            "I stay still, hand to my mouth as Arianna's eyes widen."
            hide queenie
            hide arianna
            hide casper
            show mscmc bikini_hairdown_cu sleep_cu at mscmc_cu
            "(Please tell me I didn't just seriously make this worse.)"
            "(I shouldn't have said anything. Oh my god.)"
        "B. Act natural.":
            $ menuhideborder = False
            show mscmc bikini_hairdown smile at centre
            "I rest my elbow on the sculpture next to me and clear my throat."
            mcarianna grin "Hey...guys."
            mcarianna basic "Fancy seeing you here."
        "C. You've already done it, just roll with it.":
            $ menuhideborder = False
            show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
            "(To hell with it! I already gave myself away.)"
            mcarianna "Don't leave yet. Just...hear them out."
            show mscmc grin_cu
            "(I have no idea what I am going to say.)"


    hide mscmc
    show queenie casual smile at centre:
        xoffset 40
    show arianna siren surprised at right4
    show casper casual basic at left3
    "Arianna's mouth is still open but Queenie is beaming at me."
    show casper smile
    "Casper tilts his head."
    hide queenie
    hide arianna
    hide casper
    show mscmc bikini_hairdown_cu sad_cu at mscmc_cu
    "(I just gotta say something good and save the day. Oh no.)"
    hide mscmc
    show casper casual_cu smile_cu at casper_cu
    cs "A human..."
    hide casper
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(What have I done?)"
    "I'm half-tempted to just go back to my hiding spot and pretend like this never happened."
    hide mscmc
    show arianna siren_cu angry_cu at arianna_cu
    ai "She has nothing to do with this, Casper."
    hide arianna
    show mscmc bikini_hairdown surprised at right1plus
    show arianna siren angry at left1:
        xoffset 100 alpha 0.0
        linear 0.5 xoffset 30 alpha 1.0
    pause 0.3
    "Arianna swims in front of me, protectively."
    hide arianna
    hide mscmc
    show casper casual_cu basic_cu at casper_cu
    "Casper looks between Arianna and I and the anger on his face begins to soften."
    hide casper
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Ok, think, think, think. Be good in a crisis. Say the exact right thing!)"
    hide mscmc
    show casper casual_cu smile_cu at casper_cu
    "Casper puts a hand to his chin."
    cs "This just got interesting."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
