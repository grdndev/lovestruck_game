label maxime_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_wikus_office_day at bg
    play music mscsuspense2
    # PLAY ALARM SOUND

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    # STOP ALARM SOUND
    show maxime casual_cu angry_cu at maxime_cu
    "Maxime stares at the bloodied shirt as we bend over it, his mouth a thin, grim line."
    hide maxime
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Suddenly everything feels a lot more real.)"
    show mscmc jacket_hairup surprised at left3:
        yoffset 60
    show maxime casual angry at right3:
        yoffset 60
    mx "This changes things. We need to get you away from here."
    show mscmc jacket_hairup basic:
        ease 0.7 yoffset 0
    "I straighten up, trying to clear my head, though I'm caught somewhere between horror and a desperate need to know what happened."
    # PLAY ALARM SOUND
    show mscmc jacket_hairup surprised
    mcmax "You're not taking me off the case, are you?"
    # STOP ALARM SOUND
    show mscmc jacket_hairup sad
    show maxime casual sad
    mcmax "I don't want to just walk away, not when we know somebody's been hurt—!"
    # PLAY ALARM SOUND
    show mscmc jacket_hairup surprised
    show maxime casual surprised
    "Maxime raises his finger, preparing to lecture me, when the fire alarm abruptly silences."
    # STOP ALARM SOUND
    show maxime casual angry
    "He looks up glaring at the walls."
    show mscmc jacket_hairup basic
    show maxime casual basic
    mx "We'll talk about this later."
    show white
    show mscmc jacket_hairup surprised
    show maxime casual angry
    pause 0.2
    # PLAY CAMERA SHUTTER
    show white:
        ease 0.5 alpha 0.0
    pause 0.6
    show maxime casual angry:
        ease 0.3 yoffset 0
    pause 0.3
    show maxime casual angry at out_left
    pause 0.3
    show mscmc jacket_hairup surprised at out_left
    "Maxime hurriedly snaps a picture of the shirt with his phone, then ushers me out of the building."

    scene bg msc_boardwalk_day_people at bg with wiperightdissolve
    play music msctense
    show maxime casual angry at right3,left_in
    show mscmc jacket_hairup sad at left2,left_in
    "We inch our way around the building, finally spilling out onto the safety of the boardwalk."
    show maxime casual basic
    mx "Act natural. Loosen your shoulders, like we've been strolling down the pier."
    hide maxime
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Wow, he's not wrong—I hadn't realized, but my shoulders are practically up to my ears.)"
    hide mscmc
    show maxime casual_cu angry_cu at maxime_cu
    "Even though his posture is relaxed, Maxime keeps running his eyes suspiciously along the boardwalk."
    show mscmc jacket_hairup basic at left2,walking
    show maxime casual basic at right3,walking
    "I take a deep breath and fall into step beside him."
    "Surfers are making their way to the beach after work, joined by locals out for their evening strolls."
    mcmax "Where to now?"
    mx "My studio. We can talk privately there."
    
    play music mscaction
    show mscmc jacket_hairup surprised at left2
    show maxime casual basic at right3
    "An elderly woman stumbles, catching herself before she hits the boardwalk..."
    show maxime casual angry
    "As a teenage boy sprints away, clutching the woman's purse."
    $sidecharone = "Elderly Woman"
    sid1 "Please stop him, my purse—!"
    hide mscmc
    show maxime casual basic at centre
    "Maxime tenses, arms raised as he prepares to tackle the teen."
    hide maxime
    show mscmc jacket_hairup grin at centre
    mcmax "'Scuse me, I need to borrow this for a sec!"
    show mscmc jacket_hairup angry:
        ease 0.5 xoffset -70
        ease 0.5 xoffset 0
        ease 0.3 xoffset 120
    "I grab a boogie board from a bewildered tourist, hefting it and leaping towards the purse snatcher."
    mcmax "No purse snatchers on this boardwalk!"
    show mscmc jacket_hairup surprised:
        ease 0.5 yoffset -30
        parallel:
            ease 0.3 yoffset 0
        parallel:
            ease 0.3 xoffset 190
    pause 0.5
    play sound fight_hit
    "I swing the boogie board down, catching the thief on the top of the head and making him stumble and drop the purse."
    hide mscmc
    show maxime casual sad at left2:
        ease 0.5 yoffset 30
        ease 0.5 yoffset 0
        ease 0.5 xoffset 180
        ease 0.5 yoffset 60
    "Maxime quickly grabs the purse away from him, hurrying over to help the old woman up."

    play music mschappytimes
    mx "Are you hurt, ma'am?"
    hide maxime
    show mscmc jacket_hairup basic at left1
    "She glances at the thief where he's trying to scramble up, while I loom over him with the boogie board."
    show mscmc jacket_hairup smile
    sid1 "You can let him go. I hope he's learned his lesson."
    hide mscmc
    show maxime casual smile at right2
    show mscmc jacket_hairup basic at left2, right_in
    "As the thief scuttles away, I return the boogie board and join Maxime and the old woman, who's all smiles."
    show mscmc jacket_hairup smile
    sid1 "I can't thank you both enough. You make an impressive couple, that's for sure!"
    show mscmc jacket_hairup embarrassed
    show maxime casual embarrassed
    mx "Oh, we..."
    show mscmc jacket_hairup grin
    show maxime casual surprised
    "Maxime starts to protest, but the old lady seems so happy that we let it slide."
    show maxime casual basic
    "We wave as she continues down the boardwalk, and once she's gone, I turn to Maxime with a smug smile."
    show mscmc jacket_hairup smile
    mcmax "So, like I've been telling you, I can handle myself."
    show maxime casual smile
    "He shakes his head, but I can see the smile playing on his lips."
    mx "Alright, I won't argue with your hands-on demonstration. I know I wouldn't be able to persuade you off the case anyway."
    show maxime casual basic
    mx "But there won't always be a convenient boogie board at hand."
    show maxime casual smile
    show mscmc jacket_hairup surprised
    mx "Let me show you some basic self-defense moves back at the studio."
    hide maxime
    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(I want Maxime to teach me super spy skills! Yes, I want to pretend-spar and roll around on the floor together...!)"
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "We've reached the path to his studio, and he turns to me hopefully."
    mx "I'd feel a lot better if you let me teach you some moves. Please, for me?"

    hide maxime
    $menuhideborder = True
    menu maximee05c1:
        "A. Let's get physical!"(paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "I grin broadly, trying to stow any thoughts of rolling around on the floor and getting touchy-feely."
            mcmax "That's what I'm talking about! Lead the way, coach."
            hide mscmc

            scene bg msc_maxime_studio_day at bg with clockwise_wipe
            play music mscmaxime
            show maxime casual basic at centre
            "Inside the studio, Maxime lays a large rubber mat out on the floor."
            show maxime casual smirk
            mx "You're an athlete, so we can go a little more advanced—maybe you can even knock me down."
            show mscmc jacket_hairup surprised at left3
            show maxime casual smirk at right3
            "I look dubiously from Maxime's broad shoulders then down at my smaller frame."
            show mscmc jacket_hairup smile
            show maxime casual smile
            mcmax "Well, I'm not so sure about that, but I appreciate the vote of confidence."
            show maxime casual smirk
            "He chuckles, waving me over to the mat."
            show maxime casual smile
            mx "You'd be surprised what you can do if you know how to plant your feet and leverage someone's weight against them."
            mx "Let's start with a scenario where an attacker comes from behind."
            mx "I'll come up behind you and take hold of your arms. Is that alright?"
            "He watches me gently for any signs of nerves, and I throw him a thumbs-up, getting into position with my back to him."
            hide maxime
            show mscmc jacket_hairup_cu smile_cu at mscmc_cu
            "(Maxime is probably the best self defense teacher you could ask for.)"
            show mscmc jacket_hairup embarrassed at left3
            show maxime casual basic behind mscmc at right3:
                ease 0.5 xoffset -220
            "I feel his palms on my upper arms, warm and familiar."
            mx "Now, I've got your arms, but you can still move your legs."
            show mscmc jacket_hairup_cu basic_cu at mscmc_cu:
                xoffset -180
            show maxime casual_cu smirk_cu behind mscmc at maxime_cu:
                xoffset 180
            "He leans forward, speaking over my shoulder with my back pressed against his brawny chest."
            show mscmc jacket_hairup_cu embarrassed_cu
            "I can feel his breath hot on my cheek, and it sends a pleasurable shiver up my spine."
            show maxime casual_cu basic_cu
            mx "You can always kick backwards between the attacker's legs, but you might have more success stepping hard on his foot."
            show mscmc jacket_hairup_cu surprised_cu
            mcmax "Will that be enough to knock someone off?"
            show maxime casual_cu smile_cu
            mx "Probably not on its own, but it'll give you an opportunity to get free. Raise your foot for me?"
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu:
                xoffset -180
                ease 0.6 xoffset -150
            "I do as he asks, conscious of the way of our thighs are brushing."
            show maxime casual_cu basic_cu
            mx "When you bring your heel down, you'll do more damage by hitting higher on the foot at the sensitive part of the arch."
            show mscmc jacket_hairup_cu grin_cu
            show maxime casual_cu smile_cu
            mx "But you want to come down really hard, no hesitation."
            mcmax "Oh, I {i}will{/i} give the bad guy a broken foot, don't worry about that."
            show maxime casual_cu embarrassed_cu
            show mscmc jacket_hairup_cu smile_cu at mscmc_cu:
                xoffset -150
                ease 0.7 yoffset -60
                ease 0.2 yoffset 0
            "To show I mean business, I stamp down hard on the mat next to his foot, with force."
            show mscmc jacket_hairup_cu embarrassed_cu
            show maxime casual_cu smile_cu
            "As I twist around, I catch Maxime's proud grin."
            show maxime casual_cu embarrassed_cu
            mx "I had a feeling that wouldn't be a problem for you."
            show mscmc jacket_hairup_cu smile_cu
            show maxime casual_cu smile_cu
            mx "Alright, now the attacker is caught off guard. Try to break an arm free and give an elbow to the nose, or neck if you can't reach."
            hide maxime
            hide mscmc
            show maxime casual smile behind mscmc at centre
            show mscmc jacket_hairup embarrassed at left2:
                pause 0.2
                ease 0.4 xoffset 80
            pause 0.6
            "His hands briefly go to my waist, turning me in the correct pivot, and I follow his guidance like a dancer."
            show mscmc jacket_hairup grin
            mcmax "Pow, elbow."
            mx "Good. And if you can't get your arms free, there's always a classic headbutt."
            show mscmc jacket_hairup embarrassed
            show maxime casual basic
            mx "Are you comfortable praciticing a chokehold? I wouldn't apply any pressure, just mimic the positioning. It's ok if you don't want to."
            show maxime casual smile
            "I bite my tongue before I can blurt out anything that would embarrass us both and shoot him another thumbs-up."
            show mscmc jacket_hairup smile
            mcmax "Wikus' mad science experiments won't hold back, so neither should you."
            show maxime casual smirk
            "Maxime's mouth quirks in a half-grin."
            show mscmc jacket_hairup surprised
            show maxime casual smile
            mx "You wouldn't be able to handle me if I weren't holding back."
            show mscmc jacket_hairup embarrassed
            show maxime casual smirk
            "His voice drops an octave, and the huskiness sets my heart pounding."
            hide mscmc
            show maxime casual_cu smirk_cu at maxime_cu
            "He places his hands on my shoulders and smoothly presses me against the wall, then his hand comes to rest loosely around my throat."
            show maxime casual_cu embarrassed_cu
            "I blush, and Maxime must notice, because he clears his throat and quickly looks away, embarrassed."
            mx "Like this, your arms and legs are still, um, completely free."
            show maxime casual_cu basic_cu
            mx "So you can do two things. Grab my hands and apply pressure at the highest point of the thumb muscle..."
            "I do as he says, though I'm not sure how I could possibly pry his strong hands away even if I was trying as hard as I could."
            mx "Now pull down."
            "As soon as I move I can feel my weight shift, giving me leverage."
            show maxime casual_cu smile_cu
            mx "You got it."
            "Maxime stares into my eyes, still standing incredibly close."
            show maxime casual_cu embarrassed_cu
            mx "You're pretty good at this stuff."
            hide maxime
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "I share his grin, feeling giddy."
            "(Yeah...it does feel natural, or maybe it's just being around him.)"
            hide mscmc
        "B. Too tired.":
            $menuhideborder = False
            show mscmc jacket_hairup_cu basic_cu at mscmc_cu
            mcmax "Too tired."
            hide mscmc

    scene bg msc_surfcompetition_day_people at bg with clockwise_wipe
    play music mscsurfcompetition
    show mscmc surfer_hairup smile at centre
    "I do alright in the next day's competition round..."
    "Pulling off an advanced floater that lands me safely on the podium—and with a spot in the semi-finals!"
    show mscmc surfer_hairup sad
    "It's neatly executed, with no points deducted, but somehow, I'm still not quite satisfied with my performance."
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(I'm still missing a little {i}je ne sais quoi{/i}.)"
    "(It doesn't help that I keep looking over my shoulder for Wikus, and worrying about what could have happened to the missing surfer.)"
    hide mscmc
    show maxime shorts smile at centre
    "Maxime waves to me from the sand, offering me a sports drink and a towel and taking my board in hand."
    mx "Good eye today. You definitely caught the best wave out there."
    show mscmc surfer_hairup sad at left3
    show maxime shorts sad at right3
    "I tilt my head from side-to-side, still not entirely pleased with myself."
    mcmax "It still felt a little...lacking in character."
    mcmax "I keep meaning to ask you to help me create a more artistic performance, but I got distracted by Wikus Sapor kidnapping people."
    "Maxime nods, sympathizing."
    mx "Hardly your fault."
    hide mscmc
    hide maxime
    show javier swim grin at centre:
        zoom 0.75
        xoffset 50
        yoffset 70
    jv "There's the comeback kid!"
    show javier swim smile:
        parallel:
            ease 0.8 zoom 1.0
        parallel:
            ease 0.8 xoffset 0
        parallel:
            ease 0.8 yoffset 0
    "Javier waves to us as he makes his was across the beach, his hair still slick and damp."
    hide javier
    show mscmc surfer_hairup smile at left3
    show maxime shorts basic at right4
    show javier swim smile behind mscmc,maxime at centre,right_in
    "Maxime frowns as Javier inserts himself between us, chatting easily."
    show mscmc surfer_hairup grin
    "As much as I'd like a moment alone with Maxime, I turn to Javier with a pleasant smile."
    show mscmc surfer_hairup smile
    mcmax "Hiya, Nemesis. Glad to see you're still hanging in there."
    show mscmc surfer_hairup grin
    show javier swim grin
    jv "Yup, you'll have to contend with me for another round—and you'll be stuck with me again at the gala this evening."
    mcmax "Well, I'm looking forward to thoroughly beating you."
    show mscmc surfer_hairup smile
    show javier swim smile
    jv "Funny, I was going to say the same thing."
    show javier swim angry
    "Maxime clears his throat pointedly, folding his arms."
    show mscmc surfer_hairup embarrassed
    show javier swim grin
    jv "Oh, sorry, didn't mean to interrupt. It's good to see you too—must be nice to be training a natural talent like [genericfn], eh?"
    show mscmc surfer_hairup grin
    mx "It really is."
    show mscmc surfer_hairup smile
    show javier swim basic
    "An awkward silence falls between the three of us as the sea breeze picks up."
    show mscmc surfer_hairup grin
    show javier swim smile
    jv "Well, I want to stretch and wash off before the gala. Take care of yourself, [genericfn]."
    show mscmc surfer_hairup smile
    mcmax "You too."
    show mscmc surfer_hairup sad
    show javier swim smile at step_out
    "I'm tempted to give him some kind of warning about what happened to Raymond, but have to settle for a seemingly carefree wave."
    show mscmc surfer_hairup basic
    "Once Javier's left, I turn back to Maxime, puzzled."

    hide mscmc
    hide maxime
    $menuhideborder = True
    menu maximee05c2:
        "A. You okay?":
            $menuhideborder = False
            show mscmc surfer_hairup surprised at left3
            show maxime shorts surprised at right4
            mcmax "You okay?"
            show mscmc surfer_hairup basic
            show maxime shorts basic
            "Maxime turns to me in surprise, his arms loosening."
            mx "What? Yes, I'm fine."
            show mscmc surfer_hairup smile
            show maxime shorts embarrassed
            mcmax "You seemed a little...Quiet. More than usual."
            show mscmc surfer_hairup basic
            show maxime shorts basic
            "Maxime merely shrugs."
            mx "You know how I am. I'm no good with strangers...Even if he is a friend of yours."
        "B. What was that?":
            $menuhideborder = False
            show mscmc surfer_hairup surprised at left3
            show maxime shorts basic at right4
            "I set my hands on my hip, eyebrows raised."
            show mscmc surfer_hairup smile
            mcmax "What was that?"
            show mscmc surfer_hairup basic
            show maxime shorts surprised
            mx "What was what?"
            show mscmc surfer_hairup smile
            show maxime shorts sad
            mcmax "You kept sizing up Javier. We know he's not behing Raymond's disappearance—we found the smoking gun in Wikus' study."
            show mscmc surfer_hairup surprised
            show maxime shorts embarrassed
            mx "Of course. I know he isn't the kidnapper."
            show mscmc surfer_hairup smile
            show maxime shorts smirk
            mx "I don't know, this is my usual expression. I'm cursed with RBF."
        "C. Don't you like Javier?":
            $menuhideborder = False
            show mscmc surfer_hairup basic at left3
            show maxime shorts basic at right4
            "I turn to Maxime, asking bluntly."
            show maxime shorts surprised
            mcmax "Do you not like Javier?"
            show maxime shorts basic
            mx "What? No! He's...fine."
            show mscmc surfer_hairup smile
            show maxime shorts sad
            "He gives Javier and his receding footprints in the sand a dubious look."


    show mscmc surfer_hairup smile at left3
    show maxime shorts embarrassed at right4
    "I decide to let it slide, taking a sip of my sports drink."
    hide maxime
    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(We have {i}way{/i} bigger problems right now.)"

    scene bg msc_event_venue_lightson at bg with fade
    play music msclexiclub
    show mscmc jacket_hairdown smile at left3
    show trina casual smile at right3
    "I take Trina to the Semi-Final Gala as my plus one since Maxime got his own invite..."
    hide mscmc
    hide trina
    show dawn jacket smile at left2
    show maxime casual smile at right3
    "And when we arrive him and Dawn are already waiting for us."
    hide dawn
    show mscmc jacket_hairdown grin at left2
    mcmax "Looks like you found yourself a plus one too!"
    "Maxime smiles, but there's a thoughfulness to his gaze as he watches me walk over."
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I can't help myself—I keep wondering what it would be like to go to a gala with Maxime as my date.)"
    show mscmc jacket_hairdown grin at left2
    show dawn jacket grin at right3
    dw "Hey there, semi-finals contender. I heard a rumor that there are shrimp cocktails on the premises."
    hide dawn
    show trina casual smile at right3
    so "I'm expecting lots of fancy little finger foods."
    hide mscmc
    hide trina
    show wikus casual smile at left2
    show javier casual smile at right2
    "Wikus is in the center of the room in conversation with Javier and a group of surfers, who are all obligingly laughing at his jokes."
    hide wikus
    show javier casual_cu smile_cu at javier_cu
    "Javier notices me and winks knowingly, pretending to be deeply interested in whatever Wikus is saying."
    hide javier
    show dawn jacket smile at left3
    show maxime casual smile at right3
    mx "Actually, you're in luck—there's a buffet over there."
    show dawn jacket grin
    dw "Score!"
    show dawn jacket grin at out_right
    show maxime casual smile at out_right
    "Dawn and Trina pounce on the buffet with Maxime and me following close behind..."
    "All of us jostling elbows with a ravenous group of surfers and athletes."
    show mscmc jacket_hairdown surprised at centre:
        ease 0.3 xoffset -30
    pause 0.3
    mcmax "Oof!"
    "A particularly burly guy forces me back before I can grab a plate."
    hide dawn
    show maxime casual basic behind mscmc at right3, right_in
    "I glare at him, trying to figure out how to wriggle my way back in, when Maxime appears calmly at my side."
    show mscmc jacket_hairdown angry
    show maxime casual smile
    mx "Pardon us."
    show mscmc jacket_hairdown smile
    "He somehow manages to part the waters of the crowd, making a space with his solid presence."
    mx "After you."
    hide maxime
    hide mscmc
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Chivalry is never dead so long as Maxime's around.)"
    show mscmc jacket_hairdown embarrassed at centre:
        xoffset -30
    show maxime casual smile behind mscmc at right3
    mcmax "Thanks!"
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "I grab each of us a plate, and Maxime pulls my chair out for me when we return to our table."
    hide maxime
    show trina casual smile at centre
    so "Guys!"
    show dawn jacket grin behind trina at right2, step_in
    "Trina appears mext to us, bouncing excitedly, and Dawn joins her with a more leisurely stride."
    so "Who wants to join me on the dance floor?"
    "Dawn leans in, offering her their hand."
    dw "I could go for a 'turn about the floor'."
    show trina casual smile at step_out
    show dawn jacket grin at step_out
    "They hurry off to the dance floor as the electric music pounds."
    show mscmc jacket_hairdown smile at left3
    show maxime casual smile at right3
    "The floor kills up with couples and pairs casually swaying to the beat."
    mcmax "Maxime."
    "I turn to him hopefully, and find him watching the dancers with fascination."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(I'd give anything to know what he's thinking about right now.)"
    show mscmc jacket_hairdown smile at left3
    show maxime casual basic at right3
    mx "Yes?"
    show maxime casual smile
    show mscmc jacket_hairdown smile:
        ease 0.6 xoffset 80
    "He turns his full attention to me, and I reach out my hand."
    show mscmc jacket_hairdown embarrassed
    show maxime casual surprised
    mcmax "I know it's not really your thing, but...Do you want to dance with me?"
    show mscmc jacket_hairdown grin
    show maxime casual embarrassed
    "Maxime stammers, flustered, and seems torn between taking my hand and retreating shyly."
    mx "Well...I don't really like dancing in front of people..."
    hide mscmc
    hide maxime

    scene bg msc_maxime_s1_mini2 at bg with dissolve
    play music mscmaxime
    "He lowers his voice shyly."
    mx "But I would like to dance with you. Maybe we could find somewhere where it's just us?"
    "He reaches towards me, then hesitates just short of taking my hand."

    $menuhideborder = True
    menu maximee05c3:
        "A. Private dance with Maxime!" (paidchoice="paidchoice"):
            $menuhideborder = False
            scene bg msc_event_venue_lightson at bg with dissolve
            show maxime casual_cu smile_cu at maxime_cu
            "I inch nearer to Maxime, as though we're in on a secret."
            hide maxime
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcmax "Alright! Where should we go?"
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "Maxime glances around, then nods out to the hallway off the main room that's partially shielded by potted plants."
            show mscmc jacket_hairdown smile at left1
            show maxime casual basic behind mscmc at right1
            "He offers me his arm, and I cozy up to him, letting him lead me gallantly from the main floor."
            show maxime casual sad
            mx "Now, I don't want you to get your hopes up too high...I have to confess, I've never danced on legs before."
            mcmax "That's alright. That means you've danced in the sea, haven't you?"
            show maxime casual smile
            "It's a beautiful visual, and for a moment I wish I could join him in dancing underwater."
            mx "I have, but it's a different experience. It's slower, and you let the waves carry you."
            
            play music mscromance
            "As if on cue, the band shifts to a slow, sultry song that reminds me of waves lapping against the shore."
            show mscmc jacket_hairdown smile:
                ease 0.4 xoffset 100
            show maxime casual embarrassed:
                ease 0.4 xoffset 100
            "Maxime flushes at the romantic crooning of the trumpeter, and leads me to shelter behind the potted plants."
            show mscmc jacket_hairdown grin:
                ease 0.5 xoffset 120
            show maxime casual embarrassed:
                ease 0.5 xoffset 80
            "He looks at me a bit helplessly, and I reach out, taking his hand in mine and moving it to my waist."
            hide maxime
            hide mscmc
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Something I've been dreaming of practically since we met...)"
            show mscmc jacket_hairdown grin at left1:
                xoffset 120
            show maxime casual embarrassed behind mscmc at right1:
                xoffset 80
            "It's tempting to dissolve into butterflies-in-the-stomach, but I resolve to keep it together."
            mcmax "Like this. I'll put my hand on your shoulder, and then our other hands will touch."
            show mscmc jacket_hairdown grin:
                ease 0.5 xoffset 80
            show maxime casual embarrassed:
                ease 0.5 xoffset 40
            "I raise our linked hands above our shoulders, taking the lead."
            mcmax "With human dancing, you match your partner's movements. The idea is to glide across the dance floor."
            mcmax "When I step back, you'll put your foot forward. Does that make sense?"
            show maxime casual angry
            mx "I think so..."
            show maxime casual basic
            "He glances between the leaves of the nearest elephant plant, watching in awe."
            "Some of the best dancers swirl around, seeming to barely touch the ground."
            hide maxime
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(I wonder what's he's thinking...)"
            "(I'm definitely fantasizing about gliding around the floor and wearing a pretty dress.)"
            show mscmc jacket_hairdown_cu embarrassed_cu
            "(Ooh, the thought of Maxime in a nice suit...)"
            show mscmc jacket_hairdown grin at left1:
                xoffset 80
            show maxime casual sad behind mscmc at right1:
                xoffset 40
            mx "It seems complicated."
            show mscmc jacket_hairdown smile
            show maxime casual embarrassed
            mcmax "Don't worry, it's just you and me."
            show mscmc jacket_hairdown smile:
                ease 0.6 xoffset 40
                pause 0.3
                ease 0.6 xoffset 10
            show maxime casual surprised:
                ease 0.6 xoffset 0
                pause 0.3
                ease 0.6 xoffset -30
            pause 1.5
            mcmax "Think of it as stepping in a box formation, touching each of the corners. One-two-step, one-two-step."
            show mscmc jacket_hairdown grin
            show maxime casual smile
            mcmax "See? We're turning like the other dancers."
            show maxime casual sad
            "Maxime's a quick study, he adjusts his hold on my waist."
            hide maxime
            hide mscmc
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Ooh, that makes me feel some kind of way!)"
            show mscmc jacket_hairdown embarrassed at left1:
                xoffset 10
                ease 0.6 xoffset 50
            show maxime casual smile behind mscmc at right1:
                xoffset -30
                ease 0.6 xoffset 10 
            pause 0.6
            mx "One-two-step...Okay, I think I've got it."
            show mscmc jacket_hairdown surprised:
                pause 0.3
                ease 0.6 xoffset 10
            show maxime casual smile:
                ease 0.6 xoffset -30
            pause 0.9
            "He looks up at me with a smile so heartwarming I actually miss a step."
            mx "How am I doing?"
            show mscmc jacket_hairdown embarrassed
            mcmax "You're doing great!"
            show mscmc jacket_hairdown grin:
                ease 0.6 xoffset 40
                ease 0.3 xoffset 0
            show maxime casual embarrassed:
                ease 0.6 xoffset 0
                ease 0.3 xoffset -40
            pause 0.9
            "I giggle as we pick up speed, tracing circles around the porch."
            mcmax "Thank you for dancing with me. I know it's not your thing, but I'm having a really nice time."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "It's not that I don't like dancing, I just...don't usually. I guess I was afraid."
            show maxime casual smirk
            mx "But you're a good teacher. I'm not nervous when I'm dancing with you."
            show mscmc jacket_hairdown embarrassed:
                ease 0.5 xoffset -30
                ease 0.3 xoffset 10
            show maxime casual smirk:
                ease 0.5 xoffset 0
            pause 0.8
            "He lifts my hand lightly, letting me do a spin under his arched arm."
            show mscmc jacket_hairdown grin
            "I smile at him proudly, letting him catch me."
            show mscmc jacket_hairdown smile
            mcmax "I knew you'd pick it up quickly. You've got that sense of artistry."
            show mscmc jacket_hairdown grin
            show maxime casual smirk
            mcmax "And look, now you can say you know how to waltz."
            show maxime casual basic
            "He clears his throat, glancing back at the dance floor."
            show maxime casual embarrassed
            mx "Actually, there was something I wanted to try..."
            show mscmc jacket_hairdown surprised
            show maxime casual basic
            mcmax "Oh really? A dance move?"
            show mscmc jacket_hairdown surprised:
                ease 0.5 xoffset -20
                ease 0.3 xoffset 20
            show maxime casual basic:
                ease 0.5 xoffset 40
            pause 0.8
            "He lifts his hand again, and I obediently do another turn."
            show maxime casual smile
            show mscmc jacket_hairdown surprised:
                # parallel:
                #     linear 0.8 yoffset 10
                parallel:
                    linear 0.8 xpos stagepos[1]-20
                parallel:
                    xanchor 0.5
                    #yanchor 0.6
                    linear 0.8 rotate_pad True rotate 15
            pause 0.8
            "As I fall back into him, he surprises me by tucking his arm under my back, sweeping my feet off the floor and dipping me."
            hide mscmc
            hide maxime
            show maxime casual_cu smile_cu at maxime_cu
            "The move leaves me breathless, our faces almost touching as we gaze deep into each other's eyes."
            show maxime casual_cu embarrassed_cu
            "I shift my hand from his shoulder to his neck, feeling as though time has become suspended."
            hide maxime
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            mcmax "Wow."
            hide mscmc
            show maxime casual_cu smirk_cu at maxime_cu
            "Maxime grins, a little bashful."
            mx "Good move?"
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I can feel my cheeks practically glowing, and nod breathlessly."
            mcmax "Pretty good."
            show mscmc jacket_hairdown smile at left1
            show maxime casual embarrassed behind mscmc at right1
            "He sets me gently on my feet as the music winds down, my hand lingering in his."
            show mscmc jacket_hairdown sad:
                ease 0.8 xoffset -30
            show maxime casual smile:
                ease 0.8 xoffset 30
            "I give his hand a squeeze, reluctantly pulling away."
            show mscmc jacket_hairdown smile
            mcmax "Thanks again for dancing with me, Maxime. That was perfect."
            "I'm sure my eyes asre shining like stars, and Maxime chuckles, still shy."
            mx "Thank you for teaching me."
            show maxime casual smirk
            mx "Only, can you promise not to tell Dawn about this? Otherwise they'll never let me hear the end of it."
            show mscmc jacket_hairdown grin
            show maxime casual sad
            mx "Or they'll try to drag me to Lindy Hop Night, which is worse."
            show mscmc jacket_hairdown grin:
                ease 0.4 xoffset 0
            "He shudders, and I laugh, patting his shoulder consolingly."
            show maxime casual smile
            mcmax "Don't worry, that dance will remain just for us."
            show maxime casual basic
            mcmax "Shall we head back?"
            show mscmc jacket_hairdown grin at step_out
            show maxime casual smile at step_out
            pause 0.4
            "Maxime offers me his arm again and we return to our seats."
            hide mscmc
            hide maxime
        "B. Stay at the party.":
            $menuhideborder = False
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            mcmax "No thank you!"
            hide mscmc

    play music mscantagonist
    show wikus casual smile at centre, step_in
    ws "There you are!"
    "Wikus suddenly appears, beaming in a flawlessly pressed aloha shirt."
    show mscmc jacket_hairdown surprised at left3
    show maxime casual angry at right4
    show wikus casual smile behind mscmc,maxime
    mcmax "Mr. Sapor, you were looking for me?"
    show maxime casual basic
    "My heart is pounding, but I can feel Maxime sitting close beside me, strong and reassuring as he coolly eyes Wikus."
    ws "Both of you."
    "Wikus claps us each on the shoulder."
    show mscmc jacket_hairdown sad
    "I flinch, but Maxime doesn't budge."
    show mscmc jacket_hairdown basic
    ws "I wanted to invite you both out to dinner tomorrow, just the three of us."
    show mscmc jacket_hairdown surprised
    ws "I know a great place, the sushi joint on the boardwalk. Say seven o'clock?"
    show mscmc jacket_hairdown basic
    show maxime casual smile
    "I'm not sure what to say, but Maxime takes charge and nudges me under the table, giving Wikus a smile."
    mx "We'd be delighted for the opportunity, Mr. Sapor. Tomorrow at seven o'clock."

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.