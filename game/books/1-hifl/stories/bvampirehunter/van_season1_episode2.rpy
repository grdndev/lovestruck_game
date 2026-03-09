define unknown = Character("???",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define Sheriff = Character("Sheriff Hunt",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define mail = Character("Mail Carrier",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define doc = Character("Dr. Escalona",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])

label van_season1_episode2:

    $tbc = False
    scene bg road_fog at bg
    play music hiflsuspense
    pause

    $hidetextbox = True
    $ renpy.block_rollback()
    $hideborders = False

    show hiflmc bowling surprised at right4
    show vanessa whiphuntress hatangry at left4

    mcvan "Who are you?"

    "The question slips out of my mouth before I can stop myself, but I'm not sure what else I would say."

    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Is that guy really dead?)"
    "(Why did he turn to dust?)"
    show hiflmc bowling_cu sarcastic_cu
    "(He had fangs and red eyes, so I'm at least seventy percent sure this is a hallucination and I'm still in my wrecked truck.)"
    hide hiflmc
    show vanessa huntress hatbasic at centre
    "Vanessa lowers her pistol, thumb flicking the safety into place, and closes the distance between us in two powerful strides."
    "The black cloak flowing down Vanessa's shoulders gives her an intimidating silhouette."
    "Even though she's an inch or two shorter than I am without her heels."
    va "First things first."
    show vanessa huntress hatangry
    va "Are you okay? Did he bite you?"
    show vanessa huntress hatangry at left3
    show hiflmc bowling surprised at right3
    mcvan "Bit me? Why would he...?"
    "A single word hangs in the center of my mind."
    "I fight it the best I can, trying to drum up any other explanation other than the obvious."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Except the obvious isn't real.)"
    "(It's a monster out of books and movies.)"
    show hiflmc bowling_cu blush_cu
    "(...Or for a select few, a fictional but gorgeous love interest.)"
    hide hiflmc
    show vanessa huntress hatbasic at left3
    show hiflmc bowling surprised at right3
    mcvan "Wait. You're telling me that guy was a vampire?"
    "Vanessa nods, and there's not even a hint of humor in her eyes."
    show hiflmc bowling basic
    "She's examining every inch of me, and I tug the collar of my shirt open to catch her attention, proving there's not any marks."
    show hiflmc bowling surprised
    mcvan "He didn't even try to bite me, okay?"
    show hiflmc bowling sarcastic
    mcvan "So if I could get answers sometime tonight, that'd be great."
    va "Your answers are right there."
    "She gestures to the pile of ash at our feet."
    show hiflmc bowling surprised
    mcvan "You... you killed him."
    show vanessa huntress hatangry
    va "He was trying to kill you."
    va "And besides, he was dead a long time ago."
    va "I just finished the job."
    hide hiflmc
    hide vanessa
    $menuhideborder = True

    menu vane2c1:
        "A. Am I losing my mind?":
            $menuhideborder = False
            show vanessa huntress hatbasic at left3
            show hiflmc bowling surprised at right3
            mcvan "Am I losing my mind?"
            mcvan "Like, could you pinch me and clear up whether or not I'm awake?"
            va "You're sane, just in shock. No pinching required."
        "B. Vampires aren't real.":
            $menuhideborder = False
            show vanessa huntress hatbasic at left3
            show hiflmc bowling sad at right3
            mcvan "Vampires aren't real."
            mcvan "Everyone knows that. There's no way."
            va "Most people 'know' that because the supernatural tends to cause panic when it's not kept under wrap."
        "C. Thanks?":
            $menuhideborder = False
            show vanessa huntress hatbasic at left3
            show hiflmc bowling surprised at right3
            mcvan "Thanks?"
            show hiflmc bowling sad
            mcvan "For the life-saving part, I mean. The dead guy is still weird."
            va "Fair enough. You're welcome."
    hide hiflmc
    show vanessa huntress hatbasic at centre
    "Vanessa steps past me to look at my truck."
    show vanessa huntress hatsad
    "She winces, and considering how my ride is on a good day, I can't really judge."
    show vanessa huntress hatsad at left4
    show hiflmc bowling basic at right4
    va "Can you drive home in this thing?"
    show hiflmc bowling sad
    mcvan "No. It stalled out and I'm not sure what it'll take to start again."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(Besides, my hands are shaking so much I think I'd flip the damn truck again.)"
    hide hiflmc
    show vanessa huntress hatsad at centre
    "She glances back my way, concern working its way through that hard gaze."
    hide vanessa
    show vanessa huntress_cu hatsad_cu at vanessa_cu
    "It feels like her eyes could cut through steel if they wanted to, but in that moment, Vanessa looks gentle."
    hide vanessa
    show vanessa huntress hatbasic at left4
    show hiflmc bowling basic at right4
    va "I'll give you a ride home."
    va "You can call for a tow tomorrow when the fog clears."
    show hiflmc bowling surprised
    mcvan "You have a car? You were hitchhiking."
    va "I have a van. And I left it in Havenfall while I was on the hunt."
    show vanessa huntress hatangry
    va "Didn't make that mistake twice."
    hide hiflmc
    show vanessa huntress hatbasic at centre
    "Fear makes every step stiff as I follow Vanessa, expecting something or someone else to jump out of the mist."
    "She walks with unabashed confidence, leading me to a huge van with blacked-out windows."
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Okay, the creep factor just jumped up by a hundred.)"
    hide hiflmc
    show vanessa huntress hatbasic at left4
    show hiflmc bowling surprised at right4
    mcvan "That's your van?"
    va "More of a camper. Hop on in."
    show hiflmc bowling sad
    mcvan "I..."
    mcvan "I'm not so sure about that."
    "Vanessa turns around, coiling up her whip before clipping it to the loop on her hip."
    hide hiflmc
    hide vanessa
    stop music fadeout 1.0
    play music vanessa
    show vanessa_s1_mini3 at bg with dissolve:
        zoom 0.4
    "She produces her keys with a flourish, hanging them on one finger like a prize."
    va "I'm a good driver, I promise."
    hide vanessa_s1_mini3 with dissolve
    show bg road_fog at bg
    show hiflmc bowling surprised at right4
    show vanessa huntress hatsmirk at left4
    mcvan "It's not... listen, we met like six hours ago."
    mcvan "You have a lot of weapons and I have no idea what you actually want from me."
    show vanessa huntress hatsad
    va "Right now, what I want is to get you home."
    show vanessa huntress hatangry
    va "I swear on the Helsing name that my weapons are never turned against humans."
    show vanessa huntress hatbasic
    va "I keep us safe."
    show hiflmc bowling basic
    mcvan "Helsing."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "({i}Helsing{/i}?)"
    hide hiflmc
    show hiflmc bowling surprised at right4
    show vanessa huntress hatsmirk at left4
    mcvan "Like Van Helsing? The vampire... hunter."
    mcvan "Oh."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu sarcastic_cu at hiflmc_cu
    "(I'm definitely in a coma.)"
    show hiflmc bowling_cu happy_cu
    "(I should get in the van with the hot woman in leather and let unconsciousness take hold.)"
    hide hiflmc
    show hiflmc bowling basic at right4
    show vanessa huntress hatsad at left4
    va "I'll explain everything, but we have to be somewhere safe first, okay?"
    mcvan "Okay."
    show vanessa huntress hatbasic
    "She taps the keyfob to pop open the locks, then holds the passenger door wide open to let me in."
    hide vanessa
    hide hiflmc
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Polite and hot. Thanks, brain.)"

    hide hiflmc
    show van_middle_fog at bg
    show hiflmc bowling surprised at left4 behind van_front_fog:
        ypos 725
    show van_front_fog at bg
    "I climb up into the seat, only to be dazed by the dashboard in front of me."
    "There's a display for gasoline and mileage, but a wealth of gadgets are hooked up and stacked together alongside it."
    mcvan "That tracks the weather? And that..."
    mcvan "Heat signatures? She can track {i}heat signatures{/i} in her van?!"
    show hiflmc bowling sarcastic
    "(This is either a conspiracy theorist's wet dream or worst nightmare.)"
    show vanessa huntress hatbasic at right4 behind van_front_fog with dissolve:
        ypos 725
    show hiflmc bowling basic
    "Vanessa appears on the driver's side, slinging up into her padded chair and yanking the door shut."
    show hiflmc bowling surprised
    "When she puts in the keys, several more devices light up, beeping as they come to life."
    mcvan "You've got a wild setup in here."
    show vanessa huntress hatsmirk
    va "Sure do. All tools of the trade."
    show hiflmc bowling sad
    mcvan "The... vampire hunting trade?"
    show hiflmc bowling sarcastic
    "(Every time I say 'vampire' this feels a little more real.)"
    "(I'm not sure if that's a good thing or a bad thing.)"
    show hiflmc bowling sad
    va "There's a lot out there to hunt, [genericfn]."
    show hiflmc bowling sarcastic
    mcvan "Okay, if you go after deer with this van, you're cheating."
    show hiflmc bowling basic
    show vanessa huntress hatsmirk
    "She laughs, shaking her head before taking off the parking brake."
    "The engine is whisper-quiet, but I can feel the rumble of power when Vanessa eases onto the gas pedal."
    show vanessa huntress hatbasic
    va "Not deer that stay deer, anyway."
    show hiflmc bowling surprised
    mcvan "God, what is that supposed to mean?"
    va "Long story."
    show vanessa huntress hatsmirk
    va "But it taught me to check in with park rangers before I start running around federal land with a flamethrower."
    "(I have so many questions, I can't even begin to start.)"
    show hiflmc bowling surprised
    "(Let's go with the obvious.)"
    show hiflmc bowling basic
    mcvan "Is that your way of saying you have a flamethrower in the back seat?"
    show vanessa huntress hatsad
    va "No, it got trashed."
    show vanessa huntress hatsmirk
    va "But there's all kinds of fun wstuff in the rest of the van if you want to look around."
    show hiflmc bowling surprised
    mcvan "Really? You'd let me?"
    show vanessa huntress hatbasic
    va "You're already in on the big secret of the night."
    va "I'm not going to slap your wrist and tell you to keep your eyes closed."
    show hiflmc bowling basic
    "I turn to look over the shoulder of the seat, squinting to see in the darkness of the van."
    "There's so many shadows that I can't tell one thing from another, not without climbing back there to see."
    hide hiflmc
    hide vanessa
    $menuhideborder = True

    menu vane2c2:
        "A. Check out Vanessa's goods." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc bowling surprised at left4 behind van_front_fog:
                ypos 725
            show vanessa huntress hatbasic at right4 behind van_front_fog:
                ypos 725

            mcvan "You don't mind?"
            show vanessa huntress hatsmirk
            va "I really don't. Have fun."
            show hiflmc bowling basic
            "It's awkward climbing over the center console while Vanessa is driving, but she doesn't seem to be bothered by it."
            "There's a switch behind her seat, and when I flip it on, the whole back of the van is exposed."
            scene bg van_interior_lights at bg with wipeup
            show hiflmc bowling surprised at centre
            mcvan "Holy shit."
            hide hiflmc
            "There's another rack of tech on one wall, but the opposite side is lined with weapons from roof to roof."
            "Guns are locked in side-by-side with axes, knives, and sharp wooden..."
            show hiflmc bowling surprised at centre
            "(Stakes.)"
            show hiflmc bowling sarcastic
            "(Because of vampires. Of course.)"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatsmirk at right4:
                ypos 725
            show van_front_fog at bg
            va "Like what you see?"
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "Uh... Is this a box of grenades?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "Technically."
            va "There's blessed water in there and not shrapnel, though, so don't worry."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling basic at centre
            mcvan "Couldn't you use, like, water balloons?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatsmirk at right4:
                ypos 725
            show van_front_fog at bg
            "Vanessa's laughter carries all the way from the front of the car."
            va "Maybe? Never tried that."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "How much does this all cost?"
            mcvan "You've got an armory back here."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "Well..."
            va "It's all necessary. My work requires tons of specialized equipment."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling sarcastic at centre
            mcvan "That's not an answer."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatsad at right4:
                ypos 725
            show van_front_fog at bg
            va "I don't have a good price tag estimate on an axe forged in virgin silver."
            show vanessa huntress hatsmirk
            va "Let's go with 'a lot'."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            "(She must be loaded.)"
            "(Or maybe vampire hunting pays really well?)"
            show hiflmc bowling basic
            "(The question is, who signs those checks?"
            mcvan "It must have taken you an age to get all of this stuff."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "I've collected pieces here and there."
            va "But it's my duty to protect people, and I'll carry whatever it takes to do that."
            "It's funny. She's answering my questions but skipping out on a lot of the details."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling basic at centre
            mcvan "How long have you been doing this?"
            hide hiflmc
            show vanessa huntress_cu hatbasic_cu at vanessa_cu
            "Vanessa looks away from the road, just long enough to meet my eyes."
            show vanessa huntress_cu hatangry_cu
            va "I was born to do this."
            va "From day one. This is who I was meant to be."
            "From anyone else, the statement might have sounded cocky or cheesy, but her tone is stone cold serious."
            "There's no room to argue with the steel in Vanessa's voice."
            hide vanessa
            show hiflmc bowling surprised at centre
            mcvan "That's intense."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "It keeps things in perspective."
            va "There's no straying from the path if you never forget your goal."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            "(I guess that's true.)"
            show hiflmc bowling basic
            "I rack my mind for anything I care that much about, and the only answer I find is Grace."
            show hiflmc bowling sad
            "I'd do anything for her, except now I don't have to."
            show hiflmc bowling surprised
            "But my job and my hobbies?"
            show hiflmc bowling sarcastic
            "I'm not sure I could put my life on the line for bowling balls."
            show hiflmc bowling basic
            mcvan "So this vampire thing... you're serious."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "As a heart attack."
            show vanessa huntress hatangry
            va "Actually, vampires are worse."
            show vanessa huntress hatbasic
            va "But yeah, I'm serious."
            show vanessa huntress hatangry
            va "Immortal bloodsuckers do walk among us."
            va "Plenty of them get away with it too."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "And you stop that from happening?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "When I can."
            show vanessa huntress hatsad
            va "There's a lot more of them than there are of me, unfortunately."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling basic at centre
            mcvan "How do you tell who's a vampire?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatsmirk at right4:
                ypos 725
            show van_front_fog at bg
            va "The red eyes and fangs didn't clue you in?"
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "If they look like that all the time, everyone would notice."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatangry at right4:
                ypos 725
            show van_front_fog at bg
            va "You'd think."
            show vanessa huntress hatbasic
            va "But contacts and sunglasses are cheap, and fangs only show by choice."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling_cu surprised_cu at hiflmc_cu
            "(Does that mean there have been vampires in Havenfall this whole time and I didn't notice?)"
            "(That doesn't seem possible.)"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            "Except Vanessa's conviction is unwavering."
            "There isn't even a hint of doubt in her wods, only the confidence of a woman who has seen everything she's saying with her own two eyes."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling sad at centre
            mcvan "So it could be anyone?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "Well, not anyone."
            va "A vamp needs a certain number of people to feed off regularly to survive."
            va "That means you only find them in close quarters in cities."
            va "Unless you're super unlucky."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "What does 'unlucky' mean here?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatangry at right4:
                ypos 725
            show van_front_fog at bg
            va "A twenty leech coven when I only have five steaks."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "That sounds terrifying."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatsmirk at right4:
                ypos 725
            show van_front_fog at bg
            va "I'm still here, aren't I?"
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            mcvan "(It's still scary, even if she lived!)"
            show hiflmc bowling basic
            mcvan "Have you ever been bitten?"
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "Once or twice, but not enough for it to take."
            va "They've got to drain someone dry."
            va "'Protect your neck' is a really important adage for hunters."
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling surprised at centre
            "And yet she took down the one that attacked me with a single shot."
            "It was so clean and sudden, like a guillotine falling."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show van_front_fog at bg
            va "We're getting to the residential area."
            va "Want to punch your address into the GPS and get me to the right street?"
            hide van_middle_fog
            hide vanessa
            hide van_front_fog

            show bg van_interior_lights at bg
            show hiflmc bowling basic at centre
            mcvan "Yeah."
            hide hiflmc
            show bg road_fog at bg
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show hiflmc bowling surprised at left4:
                ypos 725
            show van_front_fog at bg
            "Climbing to the front is even more difficult than the other way around."
            show hiflmc bowling basic
            "But I manage to untangle my legs and fall back into the passenger seat."
            "Vanessa points out the GPS keyboard, and after a few taps, the little pulsing arrow swings toward my house."
            show hiflmc bowling surprised
            "(This has been one weird ride.)"
            show hiflmc bowling happy
            "(Weird, but good.)"


        "B. Keep your eyes on the road.":

            $menuhideborder = False
            show hiflmc bowling surprised at left4 behind van_front_fog:
                ypos 725
            show vanessa huntress hatbasic at right4 behind van_front_fog:
                ypos 725
            "(Wait. This is...)"
            show hiflmc bowling sad
            "(I shouldn't be getting involved in this.)"
            show hiflmc bowling angry
            "(I should get home and go to sleep.)"
            show hiflmc bowling sarcastic
            "(Or wake up.)"
            "(I don't even know.)"
            va "You doing okay over there?"
            show hiflmc bowling basic
            mcvan "Reevaluating my entire existence."
            va "Understandable. That's a pretty standard reaction to what you just saw."
            show hiflmc bowling surprised
            mcvan "None of this bothers you?"
            va "I've been dealing with it way too long for it to bother me."
            "(Vanessa doesn't look at much older than I am.)"
            show hiflmc bowling sarcastic
            "(Don't tell me she was a {i}teenage{/i} vampire slayer too.)"
            show hiflmc bowling basic
            "I look down at my hands."
            show hiflmc bowling sad
            "They're not shaking anymore, but I'm even more pale than usual."
            "And the fog pressing in on all sides of the van brings an oppressive chill with it."
            show vanessa huntress hatsmirk
            va "Making sure you have all ten fingers?"
            show hiflmc bowling sarcastic
            mcvan "That and looking for an anchor to reality."
            va "This is as real as it gets."
            show hiflmc bowling basic
            "That's less comforting than I think she wants it to be, but I let my focus fall on the road."
            hide van_middle_fog
            hide vanessa
            hide hiflmc
            hide van_front_fog
            "It should be so familiar after so many years of driving through it, except there's no landmarks to draw from."
            "No houses, no fields."
            "Everything is obscurted in endless mist except the dirt right in front of the van's fog lights."
            show van_middle_fog at bg
            show vanessa huntress hatbasic at right4:
                ypos 725
            show hiflmc bowling surprised at left4:
                ypos 725
            show van_front_fog at bg
            mcvan "How do you know where we're going? You're not from here."
            "Vanessa points to a screen in the middle of the dashboard."
            "It pulses with a radar, but when I look closer, there's a path being tracked through the center."
            show hiflmc bowling basic
            show vanessa huntress hatsmirk
            va "GPS. With a little extra boost."
            show vanessa huntress hatbasic
            va "Fog can throw off satellites if it's bad enough."
            show hiflmc bowling surprised
            mcvan "Huh."
            va "Punch in your address for me."
            show vanessa huntress hatsmirk
            va "Then you can sit back and relax."
            show hiflmc bowling basic
            mcvan "I'm not sure relaxing is in the cards, but I'm gload to see the GPS instantly redirect and guide Vanessa into the next narrow turn."
            "(Home is only a few minutes away.)"

    scene bg mc_house_ext_fog at bg with fade
    stop music fadeout 1.0
    play music hiflgetitdone
    show vanessa huntress hatangry at centre
    "Vanessa parks in my driveway, getting out before I even have a chance to open my door."
    "She makes a sweep around the whole car, eyes narrowed with suspicion."
    show hiflmc bowling surprised at right4
    show vanessa huntress hatangry at left4
    mcvan "What are you looking for?"
    va "Anything out of the ordinary."
    show vanessa huntress hatbasic
    va "No offense, but I don't know your neighborhood."
    show hiflmc bowling sarcastic
    mcvan "If the church lady next door is actually a vampire, I'd be pissed."
    mcvan "She lectures everyone who can hear about the Devil."
    show hiflmc bowling happy
    show vanessa huntress hatsmirk
    "Vanessa's subdued chuckle makes me smile."
    hide vanessa
    show hiflmc bowling basic at centre
    "I go up to the front door to unlock it, but she vanishes from view for a moment, cloak snapping around the corner of my house."
    hide hiflmc
    show vanessa huntress hatbasic at centre
    "A minute later she reappears, shoulder relaxed."
    va "Seems clear."
    show vanessa huntress hatangry
    va "Clear as it can be with all this damn fog, anyways."
    show hiflmc bowling basic at right4
    show vanessa huntress hatangry at left4
    mcvan "It's always like this."
    mcvan "Come on in."
    show vanessa huntress hatsurprised
    "I step through the door and hold it open, but Vanessa stops cold on my porch, raising an eyebrow at me."
    show hiflmc bowling surprised
    mcvan "...What?"
    show vanessa huntress hatsad
    va "Be careful who you invite into your house."
    show vanessa huntress hatangry
    va "Vampires can't cross the threshold unless you roll out the welcome mat."
    hide hiflmc
    hide vanessa
    $menuhideborder = True
    menu vane2c3:
        "A. But you're not a vampire.":
            $menuhideborder = False
            show hiflmc bowling basic at right4
            show vanessa huntress hatbasic at left4
            mcvan "But you're not a vampire."
            va "Do you recognize them on sight now?"
            show hiflmc bowling sad
            mcvan "I... no. Definitely not."

        "B. That's a real thing?":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show vanessa huntress hatbasic at left4
            mcvan "That's a real thing?"
            show vanessa huntress hatsmirk
            va "Tried and true."
            show hiflmc bowling sad
            mcvan "I never imagined this old place could keep anything out by the wind."

        "C. I'll remember that for next time.":
            $menuhideborder = False
            show hiflmc bowling surprised at right4
            show vanessa huntress hatbasic at left4
            mcvan "I'll remember that for next time."
            show vanessa huntress hatangry
            va "My hope is that there won't be a next time."
            show hiflmc bowling happy
            mcvan "Never mind. I like your way better."
    scene bg heroine_home_lights at bg with dissolve
    pause
    show vanessa huntress hatbasic at centre
    "Vanessa comes into the house, and I close and lock the door behind her."
    show vanessa huntress basic with dissolve
    "She takes off her hat and tucks it under one arm, straightening stray stands of her hair back into place."
    hide vanessa
    show hiflmc bowling_cu blush_cu at hiflmc_cu
    "(Still just as gorgeous as before.)"
    show hiflmc bowling_cu sarcastic_cu
    "(But I have to amend 'incredibly lethal' onto that description too.)"
    show hiflmc bowling basic at right4
    show vanessa huntress basic at left4
    mcvan "You said you had answers for me."
    va "Ask away."
    show hiflmc bowling sarcastic
    mcvan "Let's say I believe vampires are real."
    show hiflmc bowling angry
    mcvan "Okay, fine. Why are they here? Why do they want me?"
    va "You have a pulse, [genericfn]. That's why they want you."
    show hiflmc bowling surprised
    mcvan "No, but..."
    mcvan "That guy never tried to bite me. He said he was going to take me."
    show vanessa huntress surprised
    "Vanessa tilts her head, curiosity sharpening her eyes."
    va "Take you where?"
    show hiflmc bowling sad
    mcvan "That I don't know."
    show hiflmc bowling sarcastic
    mcvan "But apparently I'm the perfect bride for someone."
    show hiflmc bowling basic
    show vanessa huntress basic
    va "..."
    va "Bride. Is that the exact word he used?"
    show hiflmc bowling surprised
    mcvan "Yeah, it was. Why?"
    show vanessa huntress angry
    va "Because that means you're in serious danger."
    va "Although it explains why the bloodsuckers are flocking in like vultures."
    "I struggle to put two and two together."
    show hiflmc bowling sarcastic
    "How could I be valuable to any vampire when I'd never met one before tonight?"
    show hiflmc bowling basic
    mcvan "So I'm a target or something?"
    va "You're not a target. You're {i}the{/i} target."
    show vanessa huntress basic
    va "I'm not sure why you pulled that particular short straw, but it's not safe for you."
    "The silence in the house around me speaks for itself."
    show hiflmc bowling sad
    mcvan "But I am alone."
    mcvan "My sister started college today, and she was the last person I had left."
    "It comes out more pathetic than I want it to."
    "Grace is still alive, but having her room be empty across from our parents' makes my chest ache."
    va "No other family in the area?"
    show hiflmc bowling basic
    mcvan "My parents died a while back. Then my grandmother."
    show vanessa huntress sad
    va "I'm sorry."
    va "Didn't mean to pry at old scars."
    show hiflmc bowling sad
    mcvan "It's okay. You didn't know."
    mcvan "But this is the only safe haven I have."
    show vanessa huntress basic
    stop music fadeout 1.0
    play music hiflmaintheme
    va "Then I'll stay with you."
    hide hiflmc
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Wait, what?)"
    hide hiflmc
    show vanessa huntress_cu angry_cu at vanessa_cu
    va "You have my protection, [genericfn]."
    va "Nothing will come for you in the night while I'm here."
    "She sounds like a knight pledging an oath, fierce with determination."
    "I'm not sure how to react when we've only just met, and my whole world has been turned upside down."
    hide vanessa
    show hiflmc bowling_cu surprised_cu at hiflmc_cu
    "(Can I trust Vanessa?)"
    "(More importantly, what would happen to me without her here?)"


    $tobecontinued()
    scene bg hifltbc at bg
    with fade

    pause
    $ resets()
