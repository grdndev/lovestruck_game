define unknown = Character("???",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define Sheriff = Character("Sheriff Hunt",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define mail = Character("Mail Carrier",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define doc = Character("Dr. Escalona",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])

label van_season1_episode1:

    $tbc = False
    scene hifl_prologue at bg
    play music hifllitegetitdone

    pause
    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show blackscreen at bg with dissolve
    show bg dorm_room at bg
    show hiflmc bowling basic at centre
    "It's strange looking at a college admission folder when I never had the chance to go."

    "A checklist stands out on the top, smudged with the marker I snagged from the orientation desk."
    show hiflmc bowling basic at right4
    show grace casual basic at left4
    mcvan "You have your student ID, right Grace?"
    show grace casual happy
    "My sister holds it up with pride, mimicking the cheesy smile in the picture."
    show grace casual sad
    gr "Yeah. And I'm stuck with this look for four years."
    gr "It's fifty bucks to replace it."
    show hiflmc bowling sad
    "I cringe."
    "Everything about this university is covered in dollar signs."
    "Every other building congratulates donors who spent tens of millions to get their names etches in brass."
    hide grace
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Ever since our parents passed away, Grace and I have been on the bleeding edge of working poor.)"

    "(She wouldn't even be here if it wasn't for a huge scholarship.)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show grace casual basic at left4
    mcvan "You can always get a job at the cafeteria. I saw they were hiring."
    show grace casual sad
    gr "I'm going to have to. Textbooks."
    show hiflmc bowling sarcastic
    "We echo each other's groans of dismay, and I mark off her ID on the list."
    show hiflmc bowling basic
    show grace casual basic
    "There's nothing left but 'move in', and Grace's little worn suitcase was the only thing we had to move."
    hide grace
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Thankfully, the dorm came with furniture.)"
    hide hiflmc
    show hiflmc bowling happy at right4
    show grace casual basic at left4
    mcvan "At least it'll pay better than the diner, yeah?"
    show hiflmc bowling sarcastic
    mcvan "Havenfall gets two new customers a day, if we're lucky."
    show hiflmc bowling basic
    gr "And most of the time they're just stopping for gas."
    show grace casual happy
    gr "This campure is ten times bigger than our whole town."
    "It's impossible not to wonder what it would be like if I was in Grace's place right now."
    "I miss exploring and learning new things."
    hide hiflmc
    hide grace
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Watching documentaries on the couch is all I get these days.)"
    show hiflmc bowling_cu sarcastic_cu
    "(Okay, self. Dial back the bitter.)"
    show hiflmc bowling_cu happy_cu
    "(It's her special day.)"
    hide hiflmc
    show hiflmc bowling happy at right4
    show grace casual basic at left4
    mcvan "You wouldn't be here if you hadn't worked your ass off, Grace."
    mcvan "I'm proud of you."
    show grace casual happy at left1
    show hiflmc bowling happy at right1 behind grace
    "Grace gives me a big hug, but that's also my cue to roll out and let her be independent."
    hide grace
    show hiflmc bowling surprised at right4
    show gwen casual surprised at left4
    "I almost run into a girl in the hallway who gives me a surprised look-- and a quick scan of my clothes."
    $sidecharone = "Teenage Girl"
    show gwen casual basic
    sid1 "Are you Grace [genericln]?"
    show hiflmc bowling basic
    mcvan "No, that's my baby sister. She's inside."
    show gwen casual happy
    sid1 "Nice! I'm her roommate."
    hide hiflmc
    hide gwen
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(And she looks so relieved that I'm not the one she's living with.)"
    hide hiflmc
    show hiflmc bowling happy at right4
    show gwen casual happy at left4
    "I keep my polite smile intact until the girl disappears, then sigh and grab my keys."
    hide gwen
    show hiflmc bowling sarcastic at centre
    "Time to head back to Havenfall."
    scene bg road_day at bg with wipeleft
    show truck_back_day at bg
    show hiflmc bowling basic at right3:
        zoom 1.05
    show truck_front_day at bg
    "The drive home is so quiet, I turn on the radio to keep myself company."
    show hiflmc bowling sad
    "(Now that Grace is gone, the whole house is empty.)"
    "(It'll be quiet all the time.)"
    "My stomach turns over at that, but then I see a figure standing on the far side of the road."
    stop music fadeout 1.0
    play music vanessa
    show vanessa_s1_mini2 at bg with dissolve:
        zoom 0.4
    "It's a woman in a chic black dress, standing with her thumb out to catch a ride."
    hide vanessa_s1_mini2
    show bg road_day at bg
    show truck_back_day at bg
    show hiflmc bowling surprised at right3:
        zoom 1.05
    show truck_front_day at bg
    mcvan "This road is the last place a girl should be cause out alone."
    mcvan "...I better pull over."
    show  hiflmc bowling basic
    "Slowing my truck to a stop, I lean over to roll down the passenger side window."
    mcvan "Hey, you need help getting somewhere?"
    $sidecharone = "Hot Hitchhiker"
    hide truck_back_day
    hide hiflmc
    hide truck_front_day
    show vanessa casual hatbasic at centre
    sid1 "If you don't mind."
    hide vanessa
    show bg road_day at bg
    show truck_back_day at bg
    show hiflmc bowling basic at right3:
        zoom 1.05
    show truck_front_day at bg
    mcvan "Hop in."
    hide truck_back_day
    hide hiflmc
    hide truck_front_day
    show vanessa casual hathappy at centre
    sid1 "Thanks!"
    hide vanessa
    show bg road_day at bg
    show truck_back_day at bg
    show hiflmc bowling basic at right3:
        zoom 1.05
    show vanessa casual hatbasic at left3:
        zoom 1.05
    show truck_front_day at bg
    "She slides into the empty seat and yanks the door shut."
    show hiflmc bowling blush
    "Now that I can get a good look at her, I'm stunned at how pretty she is."
    show hiflmc bowling sarcastic
    "(Of all the days for me to be heading into work.)"
    "(This uniform isn't doing me any favors.)"
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vane1c1:
        "A. Introduce yourself":
            $menuhideborder = False
            show hiflmc bowling basic at right3 behind truck_front_day:
                zoom 1.05
            show vanessa casual hatbasic at left3 behind truck_front_day:
                zoom 1.05
            mcvan "I'm [genericfn]."
            show vanessa casual hathappy
            sid1 "Nice to meet you."
            sid1 "And I appreciate the ride."
            show vanessa casual hatsad
            sid1 "I had a long walk ahead of me."
        "B. Compliment her.":
            $menuhideborder = False
            show hiflmc bowling happy at right3 behind truck_front_day:
                zoom 1.05
            show vanessa casual hatbasic at left3 behind truck_front_day:
                zoom 1.05
            mcvan "Your dress is amazing"
            show vanessa casual hathappy
            sid1 "Yeah? I ordered it online."
            show vanessa casual hatbasic
            sid1 "Same with everything, honestly. I move around a lot."

        "C. Stick to silence.":
            $menuhideborder = False
            show hiflmc bowling sarcastic at right3 behind truck_front_day:
                zoom 1.05
            show vanessa casual hatbasic at left3 behind truck_front_day:
                zoom 1.05
            mcvan "I don't want to see like a creep who's too interested."
            show hiflmc bowling blush
            "(Time to drive before she catches me staring.)"
    show vanessa casual hatbasic
    show hiflmc bowling basic
    "I hit the gas, ignoring the faint rattle of my truck's engine as it picks up speed."
    mcvan "Where you heading?"
    sid1 "Havenfall. You know it?"
    show hiflmc bowling surprised
    mcvan "Know it? I live there."
    show hiflmc bowling sarcastic
    "(But I'm not sure why a woman who looks like she just walked off the runway would want anything out of our one-stoplight town.)"
    show hiflmc bowling basic
    sid1 "Maybe you could tell me if the rumors are true, then."
    sid1 "You get a lot of scary stories out here."
    mcvan "We have plenty of rumors."
    show hiflmc bowling sarcastic
    mcvan "But that's because there's not much to do but gossip."
    show hiflmc bowling basic
    mcvan "The only scary thing Havenfall has is fog, though."
    mcvan "It rolls in out of nowhere sometimes, and you can't see an inch in front of your face."
    show hiflmc bowling sarcastic
    "(Driving in it is terrifying, but at least the roads are never busy.)"
    show hiflmc bowling basic
    show vanessa casual hatangry
    sid1 "Fog, huh?"
    show vanessa casual hatbasic
    sid1 "Has it always been around?"
    show hiflmc bowling surprised
    mcvan "As long as I can remember."
    show vanessa casual hatsmirk
    sid1 "Spooky."
    show hiflmc bowling basic
    show vanessa casual hatbasic
    "Our conversation fades to silence after that."
    show vanessa casual hatangry
    "But I catch her staring at the horizon with a grim look on her face, and I don't have the first idea why."

    scene bg main_day at bg
    stop music fadeout 1.0
    play music hifleveryday
    pause

    show hiflmc bowling basic at left4
    show vanessa casual hatbasic at right4
    "I drop the woman off at Main Street, refusing the twenty dollar bill she tries to give me for gasoline."
    hide vanessa
    show hiflmc bowling basic at centre
    "It's not like I had to go out of my way."
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(I should have asked for her number.)"
    show hiflmc bowling_cu sarcastic_cu
    "(Or... hell, her name.)"
    show hiflmc bowling_cu surprised_cu
    "(I'm so rude!)"
    hide hiflmc
    show hiflmc bowling angry at centre
    mcvan "How did that slip my mind?"
    show hiflmc bowling sarcastic
    "Muttering under my breath, I make my way into the bowling alley."
    show bg bowling_regular at bg with wipeleft
    show hiflmc bowling sarcastic at centre
    "There's no sign of any customers, but that doesn't mean I can skip my shift."
    hide hiflmc
    show razi casual basic at left4
    show diego doctor glassesbasic at right4
    "My boss is already at the bar, serving a glass of red to Dr. Escalona."
    hide diego
    show razi casual happy at centre
    "I wave to them both, and Razi gives me a sparkling smile."
    ra "Afternoon, [genericfn]."
    ra "Did Grace settle into her dorm alright?"
    show razi casual happy at left4
    show hiflmc bowling basic at right4
    mcvan "She did. I had to let her fly out of the nest."
    hide razi
    hide hiflmc
    show hiflmc bowling_cu sad_cu at hiflmc_cu
    "(Which sucks, but at least Razi cares enough to ask about her.)"
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(He let me come in late today too.)"
    hide hiflmc
    show razi casual basic at left4
    show hiflmc bowling surprised at right4
    mcvan "Where's JD?"
    ra "Hauling out the trash. They'll be back in a second."
    hide razi
    hide hiflmc
    show jd casual sleep at centre
    "True to form, JD swings back through the front with a yawn, running a hand back through the colorful mess of their hair."
    show hiflmc bowling sarcastic at right4
    show jd casual basic at left4
    mcvan "Why are you tired? It's like, two."
    show jd casual smirk
    jd "Listen, I have reasons for..."
    hide hiflmc
    hide jd
    show mac cop basic at centre
    "Sheriff Hunt strides in past the door before it swings shut, and JD freezes in place."
    hide mac
    show hiflmc bowling surprised at right4
    show jd casual angry at left4
    "I see them mouth a curse before turning around to greet her."
    hide hiflmc
    show mac cop basic at right4
    show jd casual happy at left4
    jd "Hey, Mac. Here to bowl on your lunch break?"
    show mac cop angry
    "Her eyes narrow, and I take a step back to remove myself from the conversation."
    "The sheriff has always been nice to me, but she's not a fan of the troublemakers."
    Sheriff "No, I'm here to find the person who was setting off 'fireworks' last night in the fields."
    show jd casual basic
    jd "No idea what you mean. I don't own any fireworks."
    Sheriff "Davies, it's not a joke. You can't make people's animals panic."
    show jd casual surprised
    jd "Listen, if we're going to get up in arms about any supposed crimes, you should be looking at [genericfn]."
    hide mac
    show hiflmc bowling surprised at right4
    mcvan "Uh, excuse me?"
    show jd casual smirk
    jd "I saw that woman you dropped off earlier. Hitchhiker, huh?"
    hide jd
    hide hiflmc
    show mac cop basic at centre
    "The sheriff rolls her eyes."
    Sheriff "That's not illegal unless she was blocking traffic."
    hide mac
    show razi casual surprised at centre
    ra "Still a surprise to have a newcomer, though."
    ra "What's she stopping here for?"
    show razi casual basic at left4
    show hiflmc bowling basic at right4
    mcvan "That's a good question."
    show hiflmc bowling sarcastic
    mcvan "The only thing she seemed interested in was the fog."
    hide razi
    hide hiflmc
    show diego doctor glassesangry at centre
    "The doctor raises an eyebrow just above the line of his sunglasses."
    doc "A rather strange thing to be concerned about."
    show razi casual basic at left4
    show diego doctor glassesbasic at right4
    ra "Probably not important, Diego."
    show razi casual smirk
    ra "I bet she's another hipster type taking pictures."
    doc "True enough."
    hide razi
    hide diego
    show hiflmc bowling basic at centre
    "JD gets taken aside for the full brunt of a lecture, which leaves me alone to clean up the lanes."
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Got to love my job.)"
    "(It's either that or not paying my bills.)"
    scene bg diner_lights_on at bg with fade
    stop music fadeout 1.0
    play music vanessa
    pause
    "I drop by the diner to pick up dinner, but for once I'm not the only one waiting in line."
    show vanessa_s0_mini1 at bg:
        zoom 0.4
    "The woman from before is sitting by the bar, toying with the necklace around her throat."
    hide vanessa_s0_mini1 with wipedown
    show bg diner_lights_on at bg
    show luce casual basic at centre
    lu "Coffee for Vanessa?"
    show luce casual basic at right4
    show vanessa casual basic at left4
    "She--{i}Vanessa{/i}--reaches over and takes a huge white mug from Luce's hands, filled almost to the brim with dark roast."
    hide luce
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    show hiflmc bowling_cu happy_cu
    "(Thanks for the save by proxy, Luce.)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa casual basic at left4
    "I step up to order my food, but Vanessa turns my way a second after I speak."
    show vanessa casual smirk
    show hiflmc bowling blush
    "She smiles, and my heart thumps against the inside of my chest."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(I have absolutely no resistance to a beautiful woman's attention.)"
    "(It's like my brain goes right out the window.)"
    hide hiflmc
    show hiflmc bowling blush at right4
    show vanessa casual smirk at left4
    va "Long time no see, stranger."
    hide vanessa
    hide hiflmc
    $menuhideborder = True
    menu vane1c2:
        "A. Nice to see you again.":
            $menuhideborder = False
            show hiflmc bowling basic at right4
            show vanessa casual smirk at left4
            mcvan "Nice to see you again."
            show hiflmc bowling surprised
            mcvan "Guess the lack of... anything interesting didn't scare you off."

        "B. How's the coffee?":
            $menuhideborder = False
            show hiflmc bowling basic at right4
            show vanessa casual smirk at left4
            mcvan "How's the coffee?"
            va "I've had worse. I'll take warm and fresh over instant any day."
        "C. Need another ride?":
            $menuhideborder = False
            show hiflmc bowling basic at right4
            show vanessa casual smirk at left4
            mcvan "Need another ride?"
            va "No, I'm good for now. But thank you."
    hide hiflmc
    hide vanessa
    show vanessa_s1_mini1 at bg with wiperight:
        zoom 0.2
    "Vanessa's eyes sweep over me from head to toe."
    "I'm not sure what she's looking for, but the intensity of her gaze makes me free like a deer in headlights."
    hide vanessa_s1_mini1
    show hiflmc bowling surprised at right4
    show vanessa casual angry at left4
    mcvan "Um."
    mcvan "Is your visit here going okay?"
    show vanessa casual sad
    va "Well, I haven't found what I'm on the hunt for quite yet."
    show vanessa casual angry
    va "But you should be careful. It gets dark here fast."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Of course it does.)"
    show hiflmc bowling_cu sarcastic_cu
    "(We're in the middle of nowhere.)"
    hide hiflmc
    show hiflmc bowling happy at right4
    show vanessa casual angry at left4
    mcvan "I just have to be careful about my truck stalling out."
    "I laugh to emphasize that I'm kidding, but Vanessa's hard look stays in place."
    show hiflmc bowling sad
    "Swallowing hard, I scramble for something else to say when Luce pushes the bag with my dinner across the counter."
    hide vanessa
    show luce casual basic at left4
    lu "Eat up, honey."
    show hiflmc bowling surprised
    mcvan "Will do. Thanks, Luce."
    hide luce
    show hiflmc bowling surprised at centre
    "I want to hurry my way out of the diner with my dignity intact."
    hide hiflmc
    show vanessa casual basic at centre
    "But Vanessa whips a pen from a band just beneath her skirt and starts writing on a napkin."
    show vanessa casual happy at left4
    show hiflmc bowling basic at right4
    "She hands it over to me with a smile, the chill in her eyes defrosting."
    va "I know you didn't want me to pay for gas, but you should at least have my number."
    va "Call if you need anything, okay?"
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu happy_cu at hiflmc_cu
    "(I have no idea if I'm being hit on or worried about, but I'm rolling with it.)"
    hide hiflmc
    show vanessa casual happy at left4
    show hiflmc bowling smirk at right4

    scene bg road_fog at bg with fade
    stop music fadeout 1.0
    play music hiflsuspense
    pause

    show truck_back_night at bg
    show hiflmc bowling basic at right3:
        zoom 1.05
    show truck_front_night at bg

    "Fog unfurls like a heavy hand across the road as I head out of town, so thick I can barely see past my windshield."

    "I have to go slow, but my truck is wheezing in protest, the engine threatening to give up the ghost."
    show hiflmc bowling sad
    mcvan "Come on, come on."
    show hiflmc bowling sarcastic
    mcvan "All we have to do is get home."
    show hiflmc bowling angry
    "I smack the dashboard with my fingers like that will somehow encourage it."
    show hiflmc bowling surprised
    "But when I look up, something is standing in the middle of the road."
    "It's so dark that I have no choice but to swerve and hope I don't hit it."
    "The whole truck shakes as I veer off into a ditch, wheels slipping against damp earth."
    "For a second I think it might tilt and flip on its size, but the brakes grind me to a halt at a dizzying but stable angle."
    show hiflmc bowling angry
    mcvan "Fuck."
    show hiflmc bowling sad
    "(I'm okay, just rattled. Deep breaths.)"
    "(And don't think about why the truck is so quiet.)"
    show hiflmc bowling angry
    "A few turns of the key don't bring the engine back to life, and neither does slowly bearing down on the gas."
    show hiflmc bowling sarcastic
    "With a sigh, I yank the keys out and pop off my seatbelt."
    "Let's make sure I didn't run over anyone."
    hide truck_back_night
    hide truck_front_night
    show hiflmc bowling sad at centre
    #fog effect should be rolling here
    "The fog seeps into my clothes as I walk, leaving a damp chill behind."
    "I grit my teeth to keep them from chattering, wrapping my arms tight around myself."
    show hiflmc bowling surprised
    "Someone is stretched across the road, eyes closed and still."
    mcvan "Oh, shit."
    mcvan "No, I didn't even feel an impact..."
    "I scramble to kneel by the person's side, looking for any sign of injury."
    show hiflmc bowling surprised at right3
    show boy1 casual vampiresleep at left3
    "It's a young man who looks far too pale, and he's icy to the touch when my fingers brush his cheek."
    mcvan "Maybe he was already dead?"
    mcvan "I have to check for a pulse."
    show hiflmc bowling surprised at right1
    show boy1 casual vampiresleep at left3 behind hiflmc
    "With another deep breath to steady myself against the tide of adrenaline, I press two fingers to his neck while leaning down to listen to his chest."
    "There's no sound or beat."
    show hiflmc bowling surprised at right4
    "A frigid hand seizes my wrist and I lurch back, a scream of shock escaping my throat."
    show boy1 casual basic at left3
    "The man's eyes open, red as freshly spilled blood."
    hide boy1
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(He's alive?!)"
    hide hiflmc
    show hiflmc bowling surprised at right4
    show boy1 casual basic at left3
    $sidecharone = "Strange Man"
    sid1 "You have been chosen for him, mortal."
    sid1 "You will be his bride."

    hide boy1
    hide hiflmc
    $menuhideborder = True

    menu vane1c3:
        "A. Run that by me one more time?":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show boy1 casual basic at left3
            mcvan "Run that by me one more time?"
            mcvan "Because you might have just been hit by a car, and we both could have concussions."
            hide boy1
            hide hiflmc
        "B. Don't you have other things to worry about?":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show boy1 casual basic at left3
            mcvan "Don't you have other things to worry about?"
            mcvan "Because you don't have a heartbeat, and that's a pretty important part of living."
            hide boy1
            hide hiflmc
        "C. Sorry, I'm taken!":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show boy1 casual basic at left3
            mcvan "Sorry, I'm taken!"
            hide boy1
            hide hiflmc
            show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
            "(Okay, I'm not, but I am nowhere near desperate enough to sign up for some corpse bride arrangement.)"
            hide hiflmc
    show boy1 casual_cu fangsangry_cu at boy1_cu
    "He hisses at me, baring a set of... fangs?!"
    hide boy1
    show hiflmc bowling surprised at right4
    show boy1 casual fangsangry at left3
    mcvan "This isn't happening."
    show boy1 casual fangsangry at left2
    "I keep saying those words like a prayer while wrenching my wrist free, kicking at the man when he tries to grab me again."
    "He gets to his feet so fast my vision blurs."
    sid1 "There is nowhere for you to run."
    hide hiflmc
    hide boy1
    show hiflmc bowling_cu angry_cu at hiflmc_cu
    "(That's not gonna stop me from trying.)"
    hide hiflmc
    show hiflmc bowling surprised at right4
    show boy1 casual fangsangry at left4
    "I dash down the road, but his footsteps keep coming closer and closer."
    show hiflmc bowling surprised at right2
    show boy1 casual fangsangry at left3 behind hiflmc
    "A horrifyingly strong grip seizes my shoulders and forces me to turn around."
    sid1 "You-!"
    "He goes still, fear spilling into those inhuman eyes."
    hide hiflmc
    show boy1 casual fangsangry at centre
    "The man stumbles back away from me, but the black spiral of a bullwhip snaps out and catches his wrist."
    hide boy1
    show hiflmc bowling surprised at centre
    mcvan "Huh?"
    hide hiflmc
    show boy1 casual fangsangry at centre
    "The sharp, searing crack of a bullet cuts through the fog and lands dead center in the man's chest."
    "He cries out, clawing at the wound as it glows white..."
    hide boy1 with dissolve
    "Before his entire body crumbles into a pile of ash."
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(...How? What?)"
    hide hiflmc
    show hiflmc bowling surprised at centre
    "I whirl around to the source of the shot, and my jaw drops."
    stop music fadeout 1.0
    play music hiflaction
    scene vanessa1 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    "A woman clad in a black cloak stands there, smoke curling from her pistol and melting into the fog."
    "The heavy handle of a whip rests in her opposite hand."
    "(I know her face!)"
    va "Another bloodsucker bites the dust."

    va "The innocent will never have anything to fear when Vanessa Helsing walks the night!"



    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
