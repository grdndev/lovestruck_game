##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode8:
    $tbc = False

    ##Change these to suit the story
    scene bg hifl_sheriff at bg
    play music hiflgetitdone

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show hiflmc casual basic at centre
    "The next morning, Mackenzie calls me down to the sheriff’s office."
    hide hiflmc
    show elmer casual basic at left4
    show mac cop basic at right4
    "When I head inside, I find her talking with the deputy, who looks a bit embarrassed."

    $sidecharone = "Deputy"

    sid1 "I'm sorry Sheriff. That's all I got out of her."

    ma "An ID is at least something."
    show mac cop sad
    ma "Wisconsin's a bit of a drive just for the sake of showing up and making trouble."

    sid1 "Yeah, I know."

    sid1 "The gun wasn't registered, but she didn't have a criminal record."

    sid1 "Hasn’t said a word in twelve hours, either."
    show mac cop basic
    ma "I'll handle that. Keys?"
    hide elmer
    hide mac
    show annabelle casual basic at centre
    "He passes over the keys and I follow Mackenzie over to the cell where the werewolf sits, staring off into space until we approach."
    show annabelle casual angry
    "Her mouth curves in a sneer before she loudly jingles her shackles, smacking the chain against the bedframe."
    show annabelle casual angry at left4
    show mac cop basic at right4
    ma "Damien got your tongue?"

    $sidechartwo = "Werewolf"

    sid2 "What would I have to say to you?"

    sid2 "After we run this town, I'm going to take that badge of your's and pin it on my chest."

    "Mackenzie is thoroughly unimpressed."
    show mac cop basic at centre behind annabelle
    "She unlocks the cell door and hauls the werewolf to her feet with one hand, pushing her towards the interrogation room."

    "There’s no struggle, but I’m wary nonetheless."
    hide annabelle
    show mac cop basic at right4
    show hiflmc casual basic at left4
    mcmac "How is this going to go?"

    ma "Well, some of that is your choice."

    ma "I have to perform an interrogation."
    show mac cop sad
    ma "But if you want to see if she knows anything about Grace, I won't stop you."
    hide mac
    hide hiflmc
    $menuhideborder = True


    menu mace8c1:
        "A. Time for good cop, bad cop." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc casual happy at left4
            show mac cop basic at right4
            mcmac "Can I be the good cop?"
            show mac cop smirk
            ma "Oh, I look forward to seeing it."
            hide hiflmc
            show annabelle casual basic at left4
            "Mackenzie brings the werewolf over to a chair and makes her sit before locking her cuffs to a ring jutting out from the bottom of the table."
            show hiflmc casual basic at centre
            "Then she gestures for me to sit there, which I do, casually in the other womans's space."
            show annabelle casual angry
            sid2 "What the hell is she doing here?"
            show mac cop angry
            ma "Is there a problem?"

            sid2 "Damien wants her. You want her."

            sid2 "What makes a human so damn special that even her sister is worth something?"
            show hiflmc casual happy
            "Clearly I'm putting her on edge, but I force a smile."
            show annabelle casual surprised
            mcmac "Do you want to talk about Grace?"

            mcmac "You don't have to get in trouble for this if she's okay."
            show annabelle casual basic
            sid2 "..."
            hide hiflmc
            "She turns her head away from me, but Mackenzie is right there, looming in the corner of the other werewolf's vision."

            ma "She asked you a question."
            show annabelle casual angry
            sid2 "You let prey do the talking for you?"

            sid2 "No wonder Damien thought this place was easy pickings."
            show mac cop smirk
            "Mackenzie lets out a soft chuckle and kicks her boot out."
            show annabelle casual surprised
            "It hits the leg of the chair, sharply tilting the werewolf backwards until Mackenzie catches it a couple inches above the ground."
            hide mac
            hide annabelle
            show hiflmc casual_cu surprised_cu at hiflmc_cu
            "(Wow. Her reflexes are no joke.)"
            hide hiflmc
            show mac cop smirk at right4
            show annabelle casual angry at left4
            ma "Do you want to know who she is?"

            "The cuffs strain around the werewolf's wrists, her jaw twitching with rage."
            show mac cop angry
            ma "[genericfn] is the only reason you even have a chance in here."

            ma "And that's why you came into town packing the gun, isn't it?"
            show mac cop smirk
            ma "If you had to challenge me tooth to claw, you know exactly what would happen."

            ma "How long did your hair take to dry last time?"
            show annabelle casual basic
            sid2 "..."

            "With a casual shove, Mackenzie sets the chair back in place."
            hide mac
            show hiflmc casual surprised at right4
            "Its feet clang against concrete, making the table under me wobble a little."
            show hiflmc casual angry
            mcmac "We already know Damien is planning something."
            show annabelle casual angry
            sid2 "You don't know shit."
            show hiflmc casual angry at right2
            show mac cop basic at right5
            "Mackenzie takes the chance to pull out the note we found in the office, passing it over to me."
            show hiflmc casual surprised
            "I flash the paper at the werewolf, tilting my head curiously."
            hide mac
            show hiflmc casual surprised at right4
            mcmac "Then what's this?"
            show annabelle casual basic
            sid2 "..."

            sid2 "Just some garbage."
            show hiflmc casual sarcastic
            mcmac "Must have been pretty important for Damien to keep carrying it around."

            mcmac "Or were you supposed to keep track of it and dropped it in the mess? That's real sloppy."

            "She swallows hard, trying to keep from looking me right in the eye."
            hide hiflmc
            show mac cop angry at right4
            ma "Does she need to repeat the question?"
            show annabelle casual angry
            sid2 "What, are you going to kill me for being loyal?"

            sid2 "Pack is pack. I'm not going to break just because you bare your teeth."
            show mac cop surprised
            ma "What pack? You're not a Rider."
            show annabelle casual surprised
            "The werewolf freezes for just a second, but it's long enough for me to read the fear that flickers across her eyes."
            hide mac
            hide annabelle
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(Ooh, jackpot.)"
            hide hiflmc
            show mac cop basic at right4
            show annabelle casual surprised at left4
            ma "You're a wanderer."

            ma "Someone hanging onto Damien's coattails hoping he'll put in a good word."
            show annabelle casual angry
            sid2 "Shut up."
            show mac cop sad
            ma "Hate to break it to you, but you backed the wrong wolf."

            ma "Your 'leader' is writing a check he can't cash."

            sid2 "There are a hell of a lot more of us than there are of you."
            show mac cop basic
            ma "It's about quality, not quantity."

            ma "I didn't sense a single alpha in your so-called pack."
            show mac cop angry
            sid2 "Like you even know what that means-!"
            hide mac
            hide annabelle
            show mackenzie_s1_mini11 at bg
            stop music fadeout 1.0
            play music mackenziehunt
            "Mackenzie's palm slams against the table, hard enough to stop the werewolf short before I see her eyes melt into a bright gold."
            hide mackenzie_s1_mini11 at bg
            show annabelle wolfcasual wolfsurprised at left4
            show mac earscop wolfbasic at centre
            "Instead of backing down, Mackenzie leans down an inch from her face, gaze just as bright."

            ma "Try me."

            ma "I'll have you baring your throat in no time."
            show annabelle wolfcasual wolfbasic
            "For a long, tense moment, there's nothing but silence."

            "Then the werewolf starts to tremble, unable to look away from Mackenzie."
            show mac earscop wolfgrowl
            ma "Now."
            show mac earscop wolfbasic
            sid2 "The eclipse is-!"

            sid2 "Damien needs it in order to take you out."
            show mac earscop wolfsurprised
            ma "Why? What does that matter?"

            sid2 "He's never said. He just told us to be ready."
            show mac earscop wolfbasic
            ma "And where is Grace?"

            sid2 "With him, last I saw."

            sid2 "But he's always moving."
            hide annabelle
            show hiflmc casual basic at left4
            show mac earscop wolfbasic at right4
            "Mackenzie stares a moment longer before relenting, giving a brief glance my way."
            show mac cop basic
            "I nod back, satisfied, and her eyes slip back to their usual green."
            hide hiflmc
            hide mac
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(I think she's figured out how to pull the alpha card. Nice!)"
            hide hiflmc
            "We lock out wayward werewolf back up and leave her in the deputy's care."

        "B. Keep your distance.":
            $menuhideborder = False
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(With my luck, that woman would break her chains to finish what she tried to start at the lake.)"
            hide hiflmc
            show mac cop basic at right4
            show hiflmc casual happy at left4
            mcmac "If it's okay, I'm going to hang out here."
            show hiflmc casual surprised
            show annabelle casual basic at right4
            sid2 "Ooh."

            sid2 "You reek of fear, girl. Did I scare you that badly?"
            show hiflmc casual sarcastic
            mcmac "I'm sorry, which one of us is chained up right now?"
            show annabelle casual angry
            sid2 "For the moment."
            show mac cop angry at right4
            show annabelle casual angry at right2
            "She makes a lunge for me, but Mackenzie yanks her back hard before the werewolf can move more than a few inches."

            "It was just a fake out, but my heart is still hammering in my chest as Mackenzie pushes her into the interrogation room."
            hide hiflmc
            show mac cop angry at right4
            show annabelle casual angry at left1
            ma "Sit down."

            ma "And that's not a request. I will happily make you."
            show annabelle casual basic at left4
            "The werewolf complies as passive aggressively as possible, sprawling in the seat once Mackenzie locks her cuffs to the table."

            "Mackenzie doesn’t bother sitting down, towering over her prisoner."
            show annabelle casual basic
            sid2 "Woof."
            show mac cop basic
            ma "That's cute."

            ma "Now, how about you tell me what this means?"
            show mac cop basic at right1
            "She pulls the note we found out of her pocket and places it right in front of the werewolf, leaning down close to get in her face."

            ma "Damien's scent is all over this, so don't try telling me it's got nothing to do with you."

            sid2 "Looks like trash to me."
            show mac cop smirk
            ma "Funny, I was about to say the same thing."

            ma "You're not a Rider, are you?"

            ma "I don't think any of the wolves running with Damien are."
            show annabelle casual angry
            "The werewolf’s jaw tightens, then she looks straight forward, away from Mackenzie."

            ma "What did he promise you, huh?"

            ma "A home? Redemption from whatever sent you running across state lines?"

            sid2 "That's none of your goddamn business."
            show mac cop angry
            ma "You made it my business the moment you walked in here like you owned the place."

            ma "So tell me what you're planning."

            ma "And tell me where Grace [genericln] is."

            ma "It's the only way you get out of this with a slap on the wrist."
            show annabelle casual basic
            sid2 "Heh."

            sid2 "Make me."

            "Mackenzie’s hand snaps forward, and for a second, I think she’s going to hit her."
            show annabelle casual surprised at left1
            "Instead, she catches the werewolf by the jaw, yanking her chin up so they’re locked eye to eye."
            stop music fadeout 1.0
            play music mackenziehunt
            show annabelle wolfcasual wolfsurprised
            show mac earscop wolfbasic
            "The werewolf’s eyes suddenly bleed gold—and so do Mackenzie’s."

            ma "Don't make me ask again."

            sid2 "Damien needs the eclipse to happen to make his next move."

            sid2 "I don't know why! I swear!"
            hide mac
            hide annabelle
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(So much for her acting tough. What just happened?)"
            show hiflmc casual_cu surprised_cu
            "(...Is that an alpha thing?)"
            hide hiflmc
            show mac earscop wolfbasic at left1
            show annabelle wolfcasual wolfsurprised at right4
            "Mackenzie lets go of her and straightens up, crossing her arms."
            show mac cop basic
            show annabelle casual surprised
            "Their gazes both shift back into their human colors, but the other werewolf looks dazed."

            ma "Anything else?"
            show annabelle casual basic
            "She shakes her head, shoulders slumping as she stares down at the floor."
            hide mac
            hide annabelle
            show hiflmc casual_cu angry_cu at hiflmc_cu
            "(So that’s Damien’s plan. But what about Grace?)"
            hide hiflmc
            "We lock our wayward werewolf back up and leave her in the deputy’s care."

    scene bg main_day at bg
    pause
    show mac cop basic at right4
    show hiflmc casual basic at left4
    "Mackenzie makes an excuse about following up a lead, but after the two of us step outside."

    "She leads me over to the bowling alley and through the front door."
    show bg bowling at bg
    show hiflmc casual surprised at left4
    show mac cop basic at right4
    mcmac "What's up?"

    ma "I'm not done asking questions."
    hide hiflmc
    hide mac
    show razi casual happy at left4
    show jd casual basic at right4
    "Razi waves when he sees us, but JD tilts their head a little."
    hide razi
    show hiflmc casual sad at left5
    show mac cop basic at centre
    show jd casual sad
    jd "You two look serious. Is everything alright?"
    show jd casual basic
    mcmac "It could be better."

    ma "Is Diego around?"
    hide jd
    show razi casual basic at right4 behind mac
    ra "I can give him a call if you'd like."
    show mac cop sad
    ma "Please. This discussion involves everyone."
    hide razi
    show mac cop sad at right4
    "Everyone settles around a table, and I take my seat next to Mackenzie."
    hide hiflmc
    hide mac
    show diego casual glassesbasic at centre
    "Diego arrives a few minutes later, glasses guarding his eyes, and sits down in the last chair."

    di "I assume things have been escalating."

    di "One of my patients mentioned the attempted robbery at the diner last night."
    show diego casual glassesbasic at left4
    show mac cop basic at right4
    ma "It was one of Damien's followers."

    ma "She's cooling her heels in a cell right now, but she gave something up."
    hide diego
    show jd casual smirk at left4
    jd "Oh? You're stealing all the fun parts, Mac."
    hide mac
    show hiflmc casual sad at right4
    mcmac "She said something about an eclipse."

    mcmac "That Damien needs it in order to get rid of Mackenzie."
    hide jd
    show razi casual surprised at left4
    ra "An eclipse? I mean, the moon affects her kind more than any other."
    hide razi
    show diego casual glassesbasic at left4
    di "Otherwise known as a blood moon, when it falls behind the Earth's shadow."
    hide diego
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Oh, a blood moon. That’s not super ominous or anything.)"

    "(Who names this stuff?)"
    hide hiflmc
    show diego casual glassesbasic at left4
    show jd casual basic at right4
    jd "There are solar eclipses too, you know."
    hide diego
    show razi casual basic at left4
    ra "The important part is how it's going to complicate things."
    hide jd
    show mac cop sad at right4
    ma "That's the problem. I don't know."

    ma "The last lunar eclipse was before my first change."

    ma "If it had an effect, I didn't feel it."
    hide razi
    show jd casual sad at left4
    jd "I can only guess, then. The moon doesn't do anything to me."
    hide jd
    show razi casual sad at left4
    ra "It makes illusion magic easier on my end, but that doesn't help you much."
    hide mac
    hide razi
    show diego casual glassesbasic at centre
    "We all look at Diego, who simply shrugs."

    di "Darkness is darkness."

    di "Whether the moon is visible or not has never mattered."
    hide diego
    show hiflmc casual basic at left4
    show mac cop basic at right4
    mcmac "Even if we don't know what it does, shouldn't we know when it is?"
    show mac cop surprised
    ma "That's a good point."

    mcmac "Let me check on my phone."
    hide mac
    show hiflmc casual happy at centre
    "Thankfully, the internet is happy to tell me the next lunar eclipse isn’t for two months."
    show hiflmc casual sarcastic
    "Unfortunately, that doesn’t make any sense."
    show hiflmc casual sarcastic at left4
    show mac cop surprised at right4
    mcmac "Two months? Why would Damien need to wait that long?"
    show mac cop angry
    ma "He wouldn't. Not when he's being so aggressive now."
    hide hiflmc
    show diego casual glassesbasic at left4
    di "Perhaps it's for some sort of ritual?"

    di "You told me he belongs to the Rider pack, yes?"

    di "The land may need to be dedicated to their name."
    show mac cop surprised
    ma "Because it's belonged to my family for so long?"

    ma "Maybe."
    hide diego
    show mac cop angry at centre
    "She frowns, a line tensing between her brows."
    show mac cop sad
    ma "I barely even remember my great-grandparents."

    ma "I wish they were alive to tell me anything about this."
    hide mac
    show mackenzie_s1_mini7 at bg
    "I reach under the table for Mackenzie’s hand, giving it a light squeeze."
    stop music fadeout 1.0
    play music hiflliteromance

    "Much to my surprise, she squeezes back hard, our knees bumping together."
    hide mackenzie_s1_mini7
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(Don’t blush, don’t blush.)"
    show hiflmc casual_cu sarcastic_cu
    "(Everyone’s right here!)"
    hide hiflmc
    show hiflmc casual blush at left1
    show mac cop sad at right2
    mcmac "Um..."

    "Every pair of eyes lands right on me and I gulp."
    hide hiflmc
    hide mac
    $menuhideborder = True
    menu mace8c2:
        "A. Crack a joke.":
            $menuhideborder = False
            show hiflmc casual happy at left2
            show mac cop sad at right2
            mcmac "She'll be a natural at this."
            mcmac "I mean, a werewolf with the last name hunt has to be."

            ma "One of the benefits of almost no one knowing what I am means that I never hear that joke."
            hide hiflmc
            show razi casual smirk at left4
            ra "She's not wrong, though."
            hide razi
            hide mac
        "B. Support Mackenzie.":
            $menuhideborder = False
            show hiflmc casual happy at left1
            show mac cop sad at right2
            mcmac "We'll figure this out together, Mackenzie."
            show hiflmc casual sad
            mcmac "There's so much you've already learned, and you've had to do it all yourself."
            show mac cop sleep
            ma "Yeah."
            show mac cop smirk
            ma "...I've never realized how lonely that is until now."
            hide mac
            hide hiflmc
        "C. Just shrug.":
            $menuhideborder = False
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(I've got nothing.)"
            hide hiflmc
            show hiflmc casual basic at centre
            mcmac "What's everyone looking at me for?"
            show hiflmc casual sarcastic
            mcmac "I'm definitely not the supernatural expert here."
            show hiflmc casual surprised at left4
            show jd casual smirk at right4
            jd "No, just our token meddling mortal."
            show hiflmc casual angry
            mcmac "Hey!"
            hide jd
            hide hiflmc

    stop music fadeout 1.0
    play music hifleveryday
    show mac cop basic at right3
    show hiflmc casual blush at left3
    "Mackenzie’s hand gently slips away from mine, but our legs stay pressed together, which is enough of a distraction."
    hide hiflmc
    show mac cop basic at centre
    ma "I guess we'll have to keep investigating."

    ma "Damien seems deadset on this eclipse, and I need to figure out why."
    show diego casual glassesbasic at left4
    show mac cop basic at right4
    di "Any hints about Grace?"
    show mac cop sad
    ma "Only that she still seems to be alive."
    hide mac
    hide diego
    show hiflmc casual sad at centre
    "I’m happy about that, of course, but that doesn’t make it any less frustrating that we can’t find her."

    "Where could Damien have hidden my sister for so long?"
    hide hiflmc
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(I have a feeling we’ll only find out when we take the fight to him.)"
    scene bg main_night at bg
    show mac cop basic at left3
    show hiflmc casual surprised at right3
    "The sun’s set by the time Mackenzie and I leave the bowling alley, but she stops me with a soft touch to the arm when I turn towards my truck."

    ma "Are you going home?"
    show hiflmc casual basic
    mcmac "That was the plan."

    ma "I don't think it's safe."

    ma "Not after what Damien did to the office, after the diner."
    show hiflmc casual sarcastic
    mcmac "It's the only house I've got."
    show hiflmc casual surprised
    ma "You could stay with me instead."

    mcmac "I..."
    show hiflmc casual blush
    "I want to. Every part of me wants to, even if I’m a little guilty about it not being for the right reasons."
    hide mac
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(Mackenzie’s priority is keeping me safe and I’m—!)"
    show hiflmc casual_cu blush_cu
    "(God, I don’t think I’ve ever crushed this hard on someone.)"
    hide hiflmc
    show mac cop surprised at left3
    show hiflmc casual blush at right3
    ma "[genericfn]?"

    mcmac "Yeah. Yeah, of course."
    show hiflmc casual happy
    mcmac "Take me to the bunker, sheriff."
    show mac cop smirk
    ma "Oh, come on. I have an actual house."
    scene bg road_night at bg
    "She does, and it’s a nice place by the treeline, tucked away from everyone else’s houses."
    show hiflmc casual happy at centre
    "I park my truck in Mackenzie’s driveway, tasting the crisp night air while she unlocks the door."
    show bg mackenzie_bedroom_lights at bg
    show hiflmc casual happy at right4
    show mac cop basic at left4
    "Lights get flipped on along the way, but Mackenzie doesn’t pause until we reach her room."
    show hiflmc casual surprised
    "I stop right in the doorway, letting out a little sound of surprise."
    hide mac
    hide hiflmc
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(That’s a LOT of comic books!)"
    hide hiflmc
    "I’d expected a sort of serious, utilitarian vibe, but Mackenzie’s room is full of color,"

    "Bright posters framed around the walls and hundreds of covers organised on massive shelves."
    show mac cop surprised at left4
    show hiflmc casual happy at right4
    mcmac "You weren't kidding about the superhero thing, huh?"
    show mac cop blush
    ma "Oh."

    ma "Um, no. It's a big hobby of mine."

    "She blushes a bit, turning to look back at me."

    ma "Kind of nerdy, huh?"
    $menuhideborder = True
    hide mac
    hide hiflmc

    menu mace8c3:
        "A. More like awesome.":
            $menuhideborder = False
            show mac cop blush at left4
            show hiflmc casual happy at right4
            mcmac "More like awesome."
            mcmac "How long have you been collecting this stuff?"

            ma "Since I was a kid."
            ma "I never spent my allowance on anything else."
            ma "My dad even took me to a convention in Chicago once."
            ma "It blew my mind."
        "B. Yeah, kind of.":
            $menuhideborder = False
            show mac cop blush at left4
            show hiflmc casual happy at right4
            mcmac "Kind of, but it's still impressive."
            mcmac "My movie collection isn't even a tenth of this size."

            ma "Don't even ask how much it all cost."
            ma "This is a lifetime investment."

        "C. It's very you.":
            $menuhideborder = False
            show mac cop blush at left4
            show hiflmc casual happy at right4
            mcmac "No, it suits you."
            mcmac "I can only imagine how much time it took to get all this together."

            ma "A lot. Even more to organize it."
            ma "Although, I don't have a lot of time to actually read my comics these days."

    show mac cop happy at left4
    "Mackenzie smiles, her usual confident air returning."

    ma "Want to see some of my favorites?"

    mcmac "Give me the grand tour."
    show mac cop happy at left2
    show hiflmc casual happy at right2
    "I can only stand there amazed as Mackenzie explains what she has on the shelves, down to the date everything was printed."

    "She even has some autographed issues carefully sealed up in plastic, but takes them out to show me the covers."
    show mac cop blush
    ma "It’s kind of silly, I guess, but since I didn’t have any other werewolves to grow up with..."

    ma "This became my place to connect to people with powers like mine."
    show mac cop smirk
    ma "Turning into a wolf isn’t even a blip on the superpowered radar, you know?"

    mcmac "I don't think that's silly at all."

    mcmac "You are pretty much truth, justice, and the werewolf way, Sheriff."
    stop music fadeout 1.0
    play music hiflliteromance
    ma "Mac."
    show hiflmc casual surprised
    mcmac "What?"

    ma "Call me Mac. I'm not the sheriff in my own house."
    show hiflmc casual blush
    "The playful way she says it makes my face heat up, but I’m not going down without a fight."

    mcmac "Does that mean you're off-duty now?"
    show mac cop happy
    ma "Of course."

    ma "If I didn't take a break once in a while, I'd lose my head."
    show hiflmc casual happy
    "I respect her work, but that doesn’t mean it’s not nice to see Mackenzie this way."

    "She’s let me get in close, shared a part of herself I don’t think anyone else has seen."
    hide hiflmc
    hide mac
    show mac cop_cu basic_cu at mac_cu
    "When she takes a step forward, my breath catches."

    "Mackenzie doesn’t even have to touch me for me to feel her heat, the power of her presence."
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    mcmac "You should relax more."

    mcmac "I like it when you smile."
    hide hiflmc
    show mac cop_cu smirk_cu at mac_cu
    ma "Yeah?"

    ma "I like when you smile too."
    hide mac
    stop music fadeout 1.0
    play music hiflheavyromance
    "Calloused fingers gently cup my cheek before Mackenzie leans down to capture my mouth in a kiss."

    "It starts out soft, but I tilt my head up to meet her lips, not quite believing what’s happening even as we press close."
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(Please don’t tell me I passed out in her bed and this is just a really killer dream.)"
    hide hiflmc
    show mac cop_cu blush_cu at mac_cu
    ma "Is this okay?"
    hide mac
    show hiflmc casual_cu blush_cu at hiflmc_cu
    mcmac "It's so, so okay."
    hide hiflmc
    "She kisses me again and I grab hold of Mackenzie’s shoulder, chasing that warmth until I’ve lost myself completely."

    "I’m falling and falling, but she’s right there to catch me."
    show hiflmc casual_cu sad_cu at hiflmc_cu
    mcmac "That's totally unfair."
    hide hiflmc
    show mac cop_cu surprised_cu at mac_cu
    ma "What is?"
    hide mac
    show hiflmc casual_cu blush_cu at hiflmc_cu
    mcmac "You can't be a good kisser too."

    mcmac "You're gorgeous and have a great job."

    mcmac "That is more than enough, even leaving out the fact that you are totally a werewolf."
    hide hiflmc
    show mac cop_cu smirk_cu at mac_cu
    ma "Sorry. I always did the extra credit growing up."
    hide mac
    show hiflmc casual_cu happy_cu at hiflmc_cu
    mcmac "You're not sorry at all."
    hide hiflmc
    show mac cop_cu smirk_cu at mac_cu
    ma "Not at all."

    ma "Although if I knew I was going to get that kind of compliment, I’d have kissed you sooner."

    "She seems determined to make me turn red as a tomato, but before I can argue, Mackenzie’s radio buzzes."
    stop music fadeout 1.0
    play music hiflgetitdone
    show mac cop_cu surprised_cu at mac_cu
    "The smile vanishes and she takes a step back, tapping the button on the side."
    hide mac
    show mac cop basic at left3
    show hiflmc casual sad at right3
    ma "This is Sheriff Hunt. Repeat that?"
    show mac cop surprised
    show hiflmc casual surprised
    sid1 "She broke out! Sheriff, you have to get down here!"
    show hiflmc casual angry
    "I don’t even have to ask who ‘she’ is."
    hide mac
    hide hiflmc
    show hiflmc casual_cu sarcastic_cu at hiflmc_cu
    "(This isn't good.)"
    hide hiflmc

    $tobecontinued()
    show bg hifltbc at bg
    with fade

    pause
    $ resets()
