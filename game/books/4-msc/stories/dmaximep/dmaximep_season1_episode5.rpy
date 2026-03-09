label dmaximep_season1_episode5:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_surf_shop_day at bg
    play music mscsurfshop

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "I spend the rest of the day manning the surf shack with Trina..."
    "Though it's just before the late-afternoon rush, and we're left with a lot of time for chatting."

    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(It's hard to relax when I keep expecting Camilla to walk through the door, though.)"
    "(That offer to 'drop by' sounded a hell of a lot like a threat.)"

    show mscmc casual_hairdown smile at left2
    show trina casual smile at right1
    so "So how was your morning, [genericfn]? Get some good practice in?"
    "I turn to find Trina rearraging her rack of sunglasses in boredom."

    show mscmc casual_hairdown surprised
    show trina casual basic
    mcmaxime "Actually, yeah—I met up with Maxime."

    show trina casual smile
    so "How interesting..."

    show mscmc casual_hairdown smile
    show trina casual sad
    "Trina purses her lips, admiring her reflection in a pair of aviators."

    show trina casual smile
    so "And it went well?"

    show mscmc casual_hairdown grin
    show trina casual basic
    mcmaxime "Yeah! I caught every wave, and he's really great at noticing areas where I need to improve."
    mcmaxime "I think I've got a real chance of getting on the podium this time with Maxime's help."

    show mscmc casual_hairdown basic
    show trina casual smile
    so "Oh [genericfn]."

    show trina casual basic
    "Trina rolls her eyes affectionately, turning around to face me."
    so "I know you've got a real chance, you're a great waterwoman. I meant how did things go with {i}Maxime{/i}."

    hide mscmc
    hide trina
    show trina casual_cu smile_cu at trina_cu
    so "As in, is romance blooming?"
    "She leans on the counter, batting her eyelashes."

    hide trina
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcmaxime "Oh come on!"

    show mscmc casual_hairdown surprised at left2
    show trina casual smile at right1
    "I sputter, trying to busy myself with the till, but Trina practically flops over the counter, eager to meet my eye."

    show mscmc casual_hairdown embarrassed
    so "Ooh, you seem unusually flustered. I take it that means you like him?"

    show mscmc casual_hairdown angry
    mcmaxime "No I don't!"

    hide mscmc
    hide trina
    "I answer so quickly that Trina arches her eyebrows, undeterred, while I'm forced to frantically confront all the 'feelings' I've been squashing."

    show mscmc casual_hairdown embarrassed at left2
    show trina casual smile at right1
    so "Right, I totally believe you."

    show mscmc casual_hairdown sad
    show trina casual basic
    mcmaxime "Come on, Trina—I have a competition in three days! I don't have time for a crush."

    show mscmc casual_hairdown surprised
    show trina casual smile
    so "Very logical, but the heart does what it wants."

    show mscmc casual_hairdown sad
    mcmaxime "That sounds like something out of your romance novels."
    so "Well, someone has to be the romantic in this friendship."
    "She winks, and I realize that she's not giving up until she's gotten at least some admission from me."

    hide trina
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(That's Trina, stubborn as a mule.)"

    hide mscmc
    $menuhideborder = True
    menu maximee5c1:
        "A. He's handsome.":
            $menuhideborder = False
            show mscmc casual_hairdown embarrassed at left2
            show trina casual basic at right1
            mcmaxime "Alright, I'll admit it, he's super hot—I can't exactly argue with that. When I first saw him I thought he was some kind of swimwear model."
        "B. He's a gentleman.":
            $menuhideborder = False
            show mscmc casual_hairdown sad at left2
            show trina casual basic at right1
            mcmaxime "I mean, I do like him—he's a sweet guy, and he's been such a gentleman with me."
            show mscmc casual_hairdown smile
            mcmaxime "He brought me ice cream when I tweaked my leg, and he always walks me back to the shop at night. I appreciate that."
        "C. He's really talented.":
            $menuhideborder = False
            show mscmc casual_hairdown sad at left2
            show trina casual basic at right1
            mcmaxime "I'll admit, he's probably the most interesting person I've ever met."
            show mscmc casual_hairdown surprised
            mcmaxime "Did you know he's an amazing artist as well as a surfer? And he even took some sports med classes just because."

    show mscmc casual_hairdown basic at left2
    show trina casual smile at right1
    "Trina giggles, gratified, but before she can respond further the bell above the door jingles."

    hide mscmc
    hide trina
    "I look up, half afraid I'll find Camilla lurking there, but it's just an older man with a bright pink sunburn."
    $sidecharone = "Thart Looks Painful"
    sid1 "Uh, you guys got any SPF 50...?"
    "Trina hurries over to help him, leaving me off the hook—for the moment."

    scene bg msc_ocean_wide_day at bg with clockwise_wipe
    play music mscaction
    "My last practice session with Maxime goes well, and I make sure to throw in plenty of tricks as if I were already surfing for a panel of judges."
    "Maxime calls out to me as I pop up from the water."

    show maxime shorts smile surfboard at centre
    mx "That was great, [genericfn]! Nice tail slide."

    hide maxime
    "As I paddle towards him, he offers his palm, and I realize with a happy jolt that he's asking for a hi-five."

    show mscmc surfer_hairup_cu grin_cu at mscmc_cu
    mcmaxime "Thanks!"

    hide mscmc
    "I try to keep things casual as I slap my palm to his, even though the contact electrifies me."

    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu
    "(I don't think we've touched since I asked about his injury...)"
    "(I like being near him, and feeling comfortable with each other.)"

    show mscmc surfer_hairup_cu sad_cu
    "I reluctantly remember that this is our last practice session, and that Maxime won't be coming to the competition."
    "(I wish he would...I'd feel more in control just knowing he was watching from the sidelines.)"
    "(I promised I didn't mind, though—but that was before I got to know him!)"
    "(I want to make him proud.)"

    show mscmc surfer_hairup basic surfboard at left2
    show maxime shorts smile surfboard at right3
    mx "You alright there?"
    "Maxime knocks playfully on my board, drawing my attention back to him."

    show mscmc surfer_hairup grin surfboard
    show maxime shorts basic surfboard
    mcmaxime "Oh yeah sorry! What were you saying?"

    show mscmc surfer_hairup smile surfboard
    show maxime shorts smile surfboard
    mx "Just that your form is looking great, as usual. You know what my final piece of advice is."
    "He winks, while I playfully roll my eyes."

    show mscmc surfer_hairup grin surfboard
    show maxime shorts basic surfboard
    mcmaxime "'Listen to the breath of the ocean.'"

    show mscmc surfer_hairup sad surfboard
    mcmaxime "You know I trust you, Maxime, but I just don't see myself becoming one with the ocean by tomorrow."

    show mscmc surfer_hairup grin surfboard
    mcmaxime "I'll stil try to hear the ocean, though. For you."

    show mscmc surfer_hairup smile surfboard
    show maxime shorts embarrassed surfboard
    "His cheeks color slightly, and he smooths it over with an easy smile."

    show maxime shorts smile surfboard
    mx "Well, I appreciate that, but I've actually got one more trick up my sleeve for later that might help you."
    mx "Go on and get some rest in the meantime. We don't want to wear you out before tomorrow."
    mx "I'll find you in a bit."

    show maxime shorts smile surfboard at out_right_slow
    "He pats my shoulder, sending another electric thrill through me, and turns to paddle away."

    hide maxime
    hide mscmc
    scene bg msc_labeach_day at bg
    play music mschappytimes
    "I make my way back to the beach, my thoughts still buzzing."

    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Does he really have a way to make me 'breathe with the ocean'? What does that even feel like?)"

    hide mscmc
    scene bg msc_boardwalk_day_people at bg
    "I prop my board against the railing of the boardwalk, watching the sunlight glint and reflect off the waves."

    show mscmc surfer_hairup basic at left1plus
    show dawn jacket grin at right2
    dw "Hey champion. You psyching yourself up?"
    "Dawn flops on the railing beyond me, grinning."

    show mscmc surfer_hairup grin
    show dawn jacket smile
    mcmaxime "Something like that."

    show mscmc surfer_hairup smile
    show dawn jacket grin
    dw "You feel ready?"

    show mscmc surfer_hairup grin
    mcmaxime "I was born ready."
    "I toss my locs off my shoulder, and Dawn laughs, playfully punching my arm."

    show mscmc surfer_hairup smile
    dw "Yeah, I know it. Trina and I made a sign for cheering you on. Hope you dig glitter."

    show mscmc surfer_hairup grin
    show dawn jacket smile
    mcmaxime "Thanks, Dawn. I really appreciate that."

    show mscmc surfer_hairup surprised
    mcmaxime "Oh, there's something I wanted to ask you—do you know Camilla?"

    show dawn jacket angry
    "Dawn makes a face."

    show mscmc surfer_hairup basic
    dw "You want a professional answer, or...?"

    show mscmc surfer_hairup grin
    mcmaxime "Anything."

    show mscmc surfer_hairup basic
    show dawn jacket surprised
    dw "Okay. Officially, I know she works in a land branch of the mer government."
    dw "Her mom's kinda a big deal—she's like, an ambassador to the humans or something."

    show dawn jacket angry
    dw "Personally, I think Camilla's a B."

    show mscmc surfer_hairup grin
    show dawn jacket smile
    "I laugh despite myself."
    mcmaxime "Having met her, I can see why she wouldn't be your cup of tea."

    hide dawn
    show mscmc surfer_hairup_cu basic_cu at mscmc_cu
    "(But it seems like Dawn doesn't know the full extent of what Camilla does...or that Maxime is a spy.)"

    show mscmc surfer_hairup_cu surprised_cu
    "(And yet Maxime trusted me with that knowledge. Why? I wonder if he was lonely, keeping a secret like that.)"

    show mscmc surfer_hairup smile at left1plus
    show dawn jacket grin at right2
    dw "Got any other questions about mermaid life—anything more fin than Camilla?"

    show mscmc surfer_hairup grin
    mcmaxime "Of course, if you're offering!"

    hide mscmc
    hide dawn
    $menuhideborder = True
    menu maximec5c2:
        "A. Are you from the portal city?":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left1plus
            show dawn jacket smile at right2
            mcmaxime "Maxime mentioned a nearby mer city through a portal. Is that where you're from?"
            show mscmc surfer_hairup smile
            show dawn jacket grin
            dw "Yup. The portal city's out at seas but there's folks from lakes too. All mer can live in any type of water though."
        "B. How is a mer city built?":
            $menuhideborder = False
            show mscmc surfer_hairup surprised at left1plus
            show dawn jacket smile at right2
            mcmaxime "Where do mermaids build their cities in the ocean? Are you nearer to the surface, or deep down?"
            show mscmc surfer_hairup smile
            show dawn jacket surprised
            dw "Well, it depends—some mermaids live deeper. Some are from around the surface, like Maxime."
            show dawn jacket grin
            dw "I'm also from near the surface of the ocean. But all mers can live in any type of water."
        "C. What does your tail look like?":
            $menuhideborder = False
            show mscmc surfer_hairup grin at left1plus
            show dawn jacket smile at right2
            mcmaxime "Can I ask what color your tail is? Maxime's is blue with yellow fins."
            show mscmc surfer_hairup smile
            show dawn jacket grin
            dw "Yeah, that's 'cause he's a saltwater mer. We've always got tropical scales."
            dw "I'm more of a... well, you'll just have to wait and see sometime."

    show mscmc surfer_hairup surprised at left1plus
    show dawn jacket grin at right2
    mcmaxime "Cool!"

    hide mscmc
    hide dawn
    show maxime shorts smile at centre
    mx "Hey Dawn, are you distrating my prize surfer?"
    "Maxime whistles playfully, coming down the pier towards us."
    mx "[genericfn], if you're free later tonight, I think we can fit another lesson at our 'secret spot'—you know?"

    hide maxime
    show mscmc surfer_hairup smile at left1plus
    show dawn jacket grin at right2
    dw "Ooh, secret spot? Sounds fun—don't let me keep ya."

    show dawn jacket grin at out_right_slow
    "Dawn pushes off the railing, chuckling."

    hide mscmc
    scene bg msc_labeach_night at bg with clockwise_wipe
    play music mscromance
    show mscmc jacket_hairdown smile at left2
    show maxime casual smile at right2
    "That evening, I meet Maxime at our 'secret cove', and his face lights up when he sees me scrambling down the rocks."
    mx "[genericfn]! I'm glad you came."
    "I come to a stop just in front of him, and look up to find him beaming with genuine pleasure."

    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(It's almost like this is more to him than just our lessons...)"

    show mscmc jacket_hairdown_cu embarrassed_cu
    "(Could he be feeling something stronger too?)"

    hide mscmc
    "I'm terrified and electrified at the prospect, but Maxime quickly distracts me when he starts tugging off his shirt."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Right. swimsuits!)"

    show mscmc jacket_hairdown_cu embarrassed_cu
    "(Whatever you do, [genericfn], don't stare at his abs...or his arms, or face for that matter.)"
    "(At least, don't stare too hard.)"

    show mscmc bikini_hairdown embarrassed at left2
    show maxime shorts basic at right2
    "I clumsily hop out of my own shorts, face hot as I try not to watch him."

    show maxime shorts smile
    mx "You ready?"
    mcmaxime "Y-yeah!"

    hide mscmc
    hide maxime
    scene bg msc_ocean_wide_night at bg with dissolve
    play sound splash02
    "The water is pleasantly warm, soothing my nerves as the waves lap at our legs."
    stop sound

    "I sink deeper into the water, breathing out and inhaling the smell of seas salt and night air."

    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(It doesn't matter how I'm feeling—I can always count on the ocean to calm me down.)"

    show mscmc bikini_hairdown_cu grin_cu
    "(That's partly what drew me to surfing.)"

    hide mscmc
    show sparkle_spike_effect behind maxime at holo_mask
    show maxime mermaid smile at step_in with dissolve:
        xpos stagepos[1]-100
        ease 1 xpos stagepos[1]
    "Maxime dives briefly under the water, and when he breaks the surface he arches his mermaid tail, the brilliant colors shimmering."

    hide maxime
    hide sparkle_spike_effect
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    mcmaxime "Wow..."

    show mscmc bikini_hairdown smile at left2
    show maxime mermaid basic at right2 behind mscmc
    "I inch nearer, taking advantage of our close proximity to admire all the stripes and notches I hadn't seen before."

    show maxime mermaid embarrassed
    mx "Yes?"

    show maxime mermaid basic
    "Maxime rolls over onto his back, batting the water playfully with his tail."

    show mscmc bikini_hairdown grin
    mcmaxime "Sorry. It's still amazing and magical to me. I don't think I'll ever get used to it."

    # why was this necessary??
    hide maxime
    show mscmc bikini_hairdown smile
    show maxime mermaid smile at right2 behind mscmc
    mx "Funny, that's how I feel when I watch you on the water."

    show mscmc bikini_hairdown surprised
    show maxime mermaid basic
    mcmaxime "Really? You're not just saying that?"

    show maxime mermaid smile
    mx "Of course not. If I didn't know better, I'd say you were a mermaid."

    show maxime mermaid basic
    "Before I can properly digest this, he flicks his tail, straightening up."

    show mscmc bikini_hairdown smile
    show maxime mermaid smile
    mx "How about a little friendly competition before we train? It seems like it's been a while since you've had fun in the water."

    show mscmc bikini_hairdown grin
    show maxime mermaid basic
    mcmaxime "Oho, a competition? You know how to get me."
    "I clap my hands together, rubbing them."
    mcmaxime "So, what's the game?"

    show mscmc bikini_hairdown smile
    show maxime mermaid smile
    mx "Diving. There's a lot of shells in this cove—we'll see who can collect the most in one go. Maybe I'll give you something if you win..."

    hide maxime
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(He already had me at 'competition', but I love the invitation to show off.)"

    hide mscmc
    show maxime mermaid_cu smile_cu at maxime_cu
    mx "And I admit, it's partly because I really want to see you swim underwater. There's something about you..."

    hide maxime
    $menuhideborder = True
    menu maximee5c3:
        "A. Beat Maxime at his game!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc bikini_hairdown grin at left2
            show maxime mermaid basic at right2
            mcmaxime "Challenge accepted!"
            hide mscmc
            hide maxime
            scene bg msc_underwater_night at bg with dissolve
            "I dive beneath the water before he can stop me, giggling and sending bubbles cascading to the surface."
            show maxime mermaid_cu smirk_cu at maxime_cu
            mx "Hey!"
            hide maxime
            "Maxime laughs in protest, quickly cutting below the waves like a bolt of lightning."
            show maxime mermaid smile at centre, swoop
            "He flicks his tail, easily shooting down to the sandy bottom."
            hide maxime
            "I make a big frog kick with my legs, close behind him and moving easily through the water."
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(No way I'm letting that tail get the better of me!)"
            hide mscmc
            "My night vision's good, and I've never had trouble keeping my eyes open underwater—I've always been able to see clearly when swimming."
            "I move around the dark rocks that break up the sandy ocean floor, keeping alert for flashes of white and pink, or rainbow abolone shells."
            "Whenever I spot a shell, I snatch it, crading my collection in my arms."
            show maxime mermaid smile at centre
            "I glance over at Maxime, who's easily darting among the rocks, his eyes piercing the dimness."
            hide maxime
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "Even so, I manage to gather a good amount, my fingers picking nimbly through the sand, so focused that I almost forget that I'm not on land."
            hide mscmc
            "My arms are full of shells when my lungs finally start to throb, urging me to the surface."
            "I kick upwards, making for the reflection of the moon."
            scene bg msc_ocean_wide_night at bg with dissolve
            "Breaking the surface, I take a deep breath, and to my surprise Maxime appears a moment after me, shaking his head."
            show mscmc bikini_hairdown smile at left2
            show maxime mermaid smile behind mscmc at right2
            mx "Where did you learn to dive like that?"
            mx "And have you always been able to hold your breath that long?"
            show maxime mermaid surprised
            "He speaks without thinking, then startles, realizing what he's just said."
            show mscmc bikini_hairdown grin
            show maxime mermaid basic
            "I laugh casually, preening."
            mcmaxime "I guess I learned to swim and dive so young I don't remember the actual learning."
            mcmaxime "Anyway, here are my shells. Did I win? Let me see yours!"
            hide maxime
            hide mscmc
            scene bg msc_labeach_night at bg with dissolve
            "I start to lay them out on a nearby rock, counting."
            "They're a pretty collection of smooth, creamy colors, with one shining abolone that I'm particularly proud of."
            show mscmc bikini_hairdown grin at left2
            show maxime mermaid basic behind mscmc at right2
            mcmaxime "Eight...nine...an even ten! Excellent."
            show mscmc bikini_hairdown smile
            show maxime mermaid smile
            "I turn to Maxime expectantly, and find him smiling, laying his shells in a pile on the shore."
            mx "I got nine. You win."
            show mscmc bikini_hairdown surprised
            show maxime mermaid basic
            mcmaxime "Wait, I win?"
            "It takes me a moment to fully process this, but I count his shells for myself, and sure enough."
            show mscmc bikini_hairdown grin
            mcmaxime "Heh, looks like you got beat by a human at a diving contest."
            show maxime mermaid smile
            "I giggle, poking his shoulder teasingly, and his smile turns into a grin."
            show mscmc bikini_hairdown smile
            mx "I thought I might. I saw you go under a wave while practicing, and I was amazed at how long you could hold your breath."
            mx "And the dark didn't bother you much either."
            show maxime mermaid surprised
            "He cocks his head at me, seeming genuinely confused."
            show mscmc bikini_hairdown grin
            show maxime mermaid basic
            mcmaxime "Well, I promise I'm not a secret werewolf or anything. I just eat lots of healthy carrots."
            mcmaxime "You and Dawn are the only secret supernaturals here."
            show maxime mermaid surprised
            "I snicker, but Maxime is still watching me, his expression shifting to something thoughtful and difficult to place."
            show mscmc bikini_hairdown surprised
            show maxime mermaid basic
            mcmaxime "What is it?"
            "He shakes his head, finally remembering himself."
            show mscmc bikini_hairdown smile
            show maxime mermaid smile
            mx "It's nothing—I'm sorry, I didn't mean to stare."
            mx "I'm just very impressed with you."
            hide maxime
            show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
            "(That's just what I've wanted to hear!)"
            "(But I've got to play it cool.)"
            show mscmc bikini_hairdown grin at left2
            show maxime mermaid basic behind mscmc at right2
            mcmaxime "Well, That's probably because I'm an impressive person."
            show mscmc bikini_hairdown smile
            "I lean back on the water smugly, as Maxime laughs."
            show maxime mermaid smile
            mx "That you are. Shall we return these shells to Mother Ocean?"
            hide mscmc
            hide maxime
            scene bg msc_ocean_wide_night at bg with dissolve
            "I nod and gather up my shells, cradling them gently in my arms."
            "Maxime releases his shells one-by-one, watch them slowly down until they land on a cushion of sand."
            show mscmc bikini_hairdown smile at left2
            show maxime mermaid smile behind mscmc at right2
            mx "I think that was the perfect preamble to our lesson. Are you reasy to become one with the ocean?"
            show mscmc bikini_hairdown grin
            mcmaxime "Yes—I can do this!"
            hide mscmc
            hide maxime
        "B. Back down":
            $menuhideborder = False
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            mcmaxime "Hey there! [genericfn] again! It would seem that we do not have this choice on file either. We'll just say I do not play Maxime's game and pout."
            mcmaxime "Apologies again for the inconvenience!"
            hide mscmc

    show mscmc bikini_hairdown smile at left2
    show maxime mermaid smile behind mscmc at right2
    mx "Alright, let's get started. I'm going to help you hear the ocean breathe."
    mx "Dive with me to that cluster of rocks right there."
    hide mscmc
    hide maxime
    play sound big_splash loop
    "He points and dives below the surface, and I follow him after taking a deep breath."
    stop sound
    scene bg msc_underwater_night at bg with dissolve
    show mscmc bikini_hairdown smile at left2
    show maxime mermaid smile behind mscmc at right2
    "I open my eyes in the deep blue of the water, and see Maxime waving at me."
    mx "Right here."
    "When he speaks, his voice rings clearly in my head as if he were talking on land, but I can only nod in return."
    mx "As merfolk, we're one with the ocean, so our breathing can be in sync with it."
    mx "Place your hand over my heart and I'll help you listen. Is that alright?"

    hide mscmc
    hide maxime
    scene bg msc_maxime_s1_ei2 at bg with fade:
        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    "I nod, the water keeping me from blushing too much, and he takes my hand, laying it over his strong chest."
    "I feel the steady rhythm of his heart beneath my palm, and shut my eyes, focusing on our touch and the way the water rushes past us."
    "(Underneath the waves, with Maxime so close, my hand on his warm chest, it's easy to forget about all my cares and worrie back on land.)"
    "(It's just us and the ocean.)"
    "Suddenly, I feel a blossoming in my mind as I fully grasp just how vast the ocean is—a living, breathing thing, constantly in motion."
    "I kick my legs, the pounding of my own heart syncing up with Maxime's and the movement of the waves."
    mx "You've got it!"

    scene black at bg with fade
    scene bg msc_underwater_night at bg with eye_open_slow
    show maxime mermaid_cu smile_cu at maxime_cu
    "I open my eyes to find Maxime smiling, senseing something in my touch."
    "I smile back, and he gently tugs me towards the surface where I take a deep breath of air."

    hide maxime
    scene bg msc_ocean_wide_night at bg with dissolve
    show mscmc bikini_hairdown smile at left2
    show maxime mermaid smile behind mscmc at right2
    mx "I knew you could do it—I could tell there was something different about you! How do you feel?"
    show mscmc bikini_hairdown grin
    show maxime mermaid basic
    mcmaxime "I feel so peaceful, but so alert at the same time."
    show mscmc bikini_hairdown embarrassed
    "I glance down, and realize that he's still got his hand over mine."
    show maxime mermaid embarrassed
    "Our eyes meet, but neither of us pull away, simply treading water and gazing deep into each other's eyes."

    show mscmc bikini_hairdown grin
    show maxime mermaid basic
    mcmaxime "...Thank you, Maxime. Thank you for showing me the ocean the way it truly is."

    hide mscmc
    show maxime mermaid_cu smile_cu at maxime_cu
    mx "You're welcome, [genericfn]."

    hide maxime
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I'm so ready to crush this competition tomorrow! I have to...)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
