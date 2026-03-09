label dmaximep_season1_episode1:
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

    show trina casual smile at centre
    so "[genericfn], catch!"

    hide trina
    show mscmc casual_hairdown surprised at centre
    "I look up just in time as Trina, my boss and best friend, tosses me a pair of water shoes."

    show mscmc casual_hairdown grin
    "She cheers, pumping her fist when I catch them neatly out of the air."

    hide mscmc
    show trina casual smile at centre
    so "Great reflexes! Just what our next hometown surf champion needs."
    so "And just what all those big corporate sponsors are looking for."

    hide trina
    show mscmc casual_hairdown smile at centre
    "I roll my eyes as I wrap the shoes in tissue paper, packing them away in a box."

    show mscmc casual_hairdown grin at centre
    mcmaxime "Ah yes, I'll be the queen of waterproof sunscreen, with my own commercials and everything."

    hide mscmc
    show trina casual_cu basic_cu at trina_cu
    "Trina leans over the register, chin resting on her fist as she eyes me shrewdly."

    hide trina
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I know that look--it means she's about to lay some truth down.)"

    hide mscmc
    show trina casual sad at centre
    so "Well, corporate sponsors pave the way to assuming your title of queen of the ocean."

    hide trina
    show mscmc casual_hairdown smile at centre
    "I chuckle, shaking my head."
    mcmaxime "That's for the future. What I {i}really{/i} need right now is a pro trainer."

    hide mscmc
    show trina casual smile at centre
    so "Hm, haven't found anyone yet?"

    hide trina
    show mscmc casual_hairdown sleep at centre
    "I sigh, beginning to stack boxes."

    show mscmc casual_hairdown sad
    mcmaxime "...No."

    hide mscmc
    show trina casual smile at centre
    so "I see. Only the best for our [genericfn]."

    "She grins, tapping away at her cash register, while I set my hand on my hip."

    hide trina
    show mscmc casual_hairdown sad at centre
    mcmaxime "You think I'm being too picky?"

    hide mscmc
    show trina casual smile at centre
    so "I didn't say that...Ooh!"

    hide trina
    play sound "audio/sfx/bell-store-entrance-ding.mp3"
    queue sound "audio/sfx/79_door open.mp3"
    "She grabs my arm, tugging me behind the counter as the bell above her door jingles."

    stop sound
    show mscmc casual_hairdown basic at left2
    show trina casual smile at right1
    so "Have you met my newest instructor?"
    show mscmc casual_hairdown sad
    show trina casual basic
    mcmaxime "No, why are we whispering...?"
    show mscmc casual_hairdown surprised
    show trina casual smile
    so "Because that's him!"

    hide trina
    hide mscmc
    show maxime casual basic
    "She points to the man who's just stepped through the door, so tall he has to stoop under the dangling puka shells."

    hide maxime
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    "(Oh wow...)"

    hide mscmc
    show maxime casual basic
    "My eyes pause on his broad shoulders, muscles clearly visible under his shirt."

    hide maxime
    scene bg msc_maxime_s0_mini1 at bg with dissolve
    "When I finally raise my gaze, I'm struck by the contrast of his chiseled cheekbones with the sensitive softness in his eyes and mouth."
    "(Trina, how the hell did you get a sportswear model as your new instructor?!)"

    scene bg msc_surf_shop_day at bg with fade
    "I can feel Trina watching me with satisfaction, and I quickly shake my shoulders to clear my head."

    show mscmc casual_hairdown surprised at left2
    show trina casual smile at right1
    so "His name's Maxime. Maxime Okun."

    show trina casual basic
    mcmaxime "Okay."

    show mscmc casual_hairdown basic
    show trina casual smile
    so "Just thought you might like to know..."

    hide trina
    hide mscmc
    "She winks, and I make an exasperated noise in the back of my throat."

    show mscmc casual_hairdown embarrassed at left2
    show trina casual smile at right1
    mcmaxime "Trina, we're on the clock."

    hide trina
    hide mscmc
    "I turn abruptly, absently reaching for the stack of water shoe boxes, and suddnely slam into a solid wall of muscle."
    "Boxes and sunglasses scatter over the floor, and I'm enveloped in the warm smell of sea salt and is that paint?"

    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    mcmaxime "Gah!"

    hide mscmc
    show maxime casual_cu surprised_cu at maxime_cu
    mx "Hey!"

    hide maxime
    "We trip over each other's legs, spilling to the floor amongst all the items we've knocked over."

    $menuhideborder = True
    menu maximee1c1:
        "A. Apologize.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "I stammer, flustered."
            mcmaxime "Shoot, I'm so sorry, I wasn't looking where I was going."
            hide mscmc
        "B. Play it cool.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mcmaxime "Oops--you okay there?"
            hide mscmc
        "C. Be cheery.":
            $menuhideborder = False
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            "I flash him my most winning smile, brushing my hair behind my ear."
            mcmaxime "And here I thought we were going to have a slow day, looks like things are picking up!"
            hide mscmc

    show maxime casual basic
    "He doesn't respond, focused on gathering up everything we've spilled."

    hide maxime
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Okay...)"

    hide mscmc
    show maxime casual_cu basic_cu at maxime_cu
    "His hand brushes mine, his warm, calloused palm sending a pleasant shiver up my arm."

    hide maxime
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    "(And just like that, I'm imagining what it would be like to have that hand over my bare waist...)"

    hide mscmc
    show maxime casual_cu sad_cu at maxime_cu
    mx "You should look where you're going."

    hide maxime
    "He speaks curtly, yanking his hand back and leaving me feeling strangely cold."

    show mscmc casual_hairdown basic at left2
    show maxime casual basic at right2
    mcmaxime "Trina and I can pick everything up, It is our job, technically."

    show mscmc casual_hairdown grin
    show maxime casual sad
    "I chuckle, but he doesn't reciprocate, avoiding my eye entirely."

    show mscmc casual_hairdown basic
    show maxime casual basic
    mx "I've got it."

    hide mscmc
    hide maxime
    "He easily gathers everything in his arms and lays our wares on the counter for Trina, who gives him a questioning look."

    show trina casual basic at left2
    show maxime casual basic at right2
    mx "I just came to add a lesson to the board."

    hide trina
    show maxime casual basic at centre
    "Sidestepping me, he scrawls another name on Trina's chalkboard that displays all the lessons for the day."

    "I wait for him to say something, or at least acknowledge me, but he only nods to Trina, making brusquely for the door."

    hide maxime
    show mscmc casual_hairdown_cu angry_cu at mscmc_cu
    "(Super tall, super hot, and...a super jerk, I guess.)"
    hide mscmc

    scene bg msc_boardwalk_day at bg with fade
    play music mscbeach

    "I finish my junior surf lessons with the local kids later that afternoon."

    show mscmc jacket_hairdown basic at centre
    "I take a leisurely walk along the pier, stopping to grab a scoop of the lychee ice cream the kids keep telling me about."

    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(It's a beautiful day, and this ice cream is worth the hype...but I'm still grumpy about Maxime.)"

    show mscmc jacket_hairdown_cu angry_cu
    "(It takes two to run into each other, buddy.)"

    scene bg msc_labeach_day at bg with dissolve

    "I pause by the edge of the pier, shading my eyes as I admire the sun glinting off the waves."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Whoa, who's that guy?!)"

    hide mscmc
    scene bg msc_maxime_s0_mini2 at bg with dissolve
    "I watch as the surfer furthest out springs from the water, leaping onto his board with perfect timing to catch a wave that's careening to shore."
    "I grip my ice cream cup, half afraid he'll wipe out, but he rides it all the way back to shore past all the other surfers."

    scene bg msc_labeach_day at bg with dissolve
    "He hops off once he hits the shallows, grabbing his board and shaking his damp braids back."

    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Oh, you have got to be kidding me.)"

    hide mscmc
    show sparkle_spike_effect behind maxime
    show maxime shorts basic at centre
    "I plop down on the nearest bench, glaring as Maxime tugs his board up the beach, his bare chest glistening."

    hide sparkle_spike_effect
    hide maxime
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(Super hot, massive jerk, AND he surfs like he was born in the water. How is any of that fair?)"

    hide mscmc
    "I grumble, stirring my ice cream, when I hear a whistle behind me."

    show dawn jacket grin at centre with dissolve:
            zoom 0.9
            ease 1 zoom 1
    $sidecharone = "California Drawl"
    sid1 "Heyyy, future-champion. This seat taken?"


    show mscmc jacket_hairdown grin at left2
    show dawn jacket grin at right2
    "I turn, smiling as a familiar face plops down next to me."

    show mscmc jacket_hairdown smile
    show dawn jacket smile
    "Dawn looks as relaxed as ever in a shaggy purple jacket, their hair mussed by the wind and spray."

    "I know that despite their casual demeanor, they were probbly up with the sun windsurfing."

    show mscmc jacket_hairdown grin
    mcmaxime "Hey Dawn! How were the waves this morning?"

    show mscmc jacket_hairdown smile
    show dawn jacket grin
    "Dawn stretches, slinging their arms over the back of the bench."
    dw "They were alright, moderately gnarly. What're you up to, sussing out the competition?"

    hide mscmc
    hide dawn
    "I can't help it--my eyes dart back to Maxime, and Dawn follows my gaze."

    "He's paddling towards the horizon again, arms moving in easy, strong circles."

    show mscmc jacket_hairdown surprised at left2
    show dawn jacket smile at right2
    mcmaxime "Trina's newest hire--Maxime. He's pretty good, isn't he?"

    show mscmc jacket_hairdown smile
    show dawn jacket grin
    dw "Sure, the guy used to be pro."

    show mscmc jacket_hairdown surprised
    mcmaxime "What?!"

    "I turn to them in surprise."

    show mscmc jacket_hairdown sad
    show dawn jacket smile
    mcmaxime "I mean, I can believe it, having just watched him in action, but I had no idea!"

    show dawn jacket sad
    "Dawn winces, pushing their blond hair back."
    dw "Yeah...he had an accident that took him out of the game."

    hide mscmc
    hide dawn
    "I frown, glacing at Maxime, who's once again managed to situate himself perfectly, poised and waiting for the next big wave."

    show mscmc jacket_hairdown sad at left2
    show dawn jacket sad at right2
    mcmaxime "He seems fine...{i}better{/i} than fine. He makes it all look so effortless."

    show dawn jacket smile
    "Dawn hums, folding their arms and watching the surfers and boogie-boarders bob on the waves."

    show dawn jacket surprised
    dw "I dunno. Maybe don't bring it up with him, yeah? It's kind of a touchy subject."

    show mscmc jacket_hairdown surprised
    show dawn jacket smile
    mcmaxime "Of course. How do you know all this, though?"

    show dawn jacket grin
    "Dawn smiles secretly, parially hidden behind their curtain of hair."
    dw "Aw, we've known each other since we were kids. Our families go way back."
    dw "You seem awfully interested in him."

    show mscmc jacket_hairdown smile
    "They quirk an eyebrow suggestively, still lazing against the bench."

    hide dawn
    hide mscmc
    $menuhideborder = True
    menu maximee1c2:
        "A. He's my coworker.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show dawn jacket smile at right2
            mcmaxime "Well, since Trina hired him he's kinda like my...coworker."
            "I consider complaining about our first meeting but stow it."
            hide mscmc
            hide dawn
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(I'm willing to play nice, even if Maxime isn't.)"
            hide mscmc
        "B. He's impressive.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show dawn jacket smile at right2
            mcmaxime "Well, he stands out in a crowd, doesn't he?"
            show mscmc jacket_hairdown smile
            show dawn jacket grin
            dw "Ha, I feel that. Dude's like, over 6'1."
            hide dawn
            hide mscmc
        "C. He's got mad skills.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show dawn jacket smile at right2
            mcmaxime "Of course I'm interested--he's far and away the best surfer out there. Possibly at the pier."
            hide dawn
            hide mscmc

    "As we sit there I realize something."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I'm determined to win, so much so that I'm willing to put up with Maxime's attitude.)"
    mcmaxime "...And I think he's just the coach I need for the competition. So, I'm going to make him an offer today."

    show mscmc jacket_hairdown_cu angry_cu
    "(I've decided that just now, so there's no going back! I'm going to have to win him over.)"

    show mscmc jacket_hairdown basic at left2
    show dawn jacket basic at right2
    "I turn to Dawn, half-challenging them to say anything."

    show dawn jacket smile
    "They're as placid as ever, and merely raise and eyebrow at me, moderately intrigued."

    show dawn jacket grin
    dw "Oh, for real? Sweet."

    hide mscmc
    hide dawn

    scene bg msc_beach_bar_sunset at bg with clockwise_wipe
    play music mscmctheme

    "As the sun sets over the water, I wander towards my room at the surf shop, passing by our local beachfront bar."

    "It's fairly empty on a weekday, save for a familiar pair of broad shoulders slouched over the counter."

    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(No way!)"

    show mscmc jacket_hairdown_cu grin_cu
    "(This must be a sign from the surf gods. TIme to make my move.)"

    hide mscmc
    "I slide onto the stool next to Maxime, already wearing my most winning smile."

    show mscmc jacket_hairdown grin at left2
    show maxime casual basic at right2
    mcmaxime "Hey."
    "His shoulders tighten, and his eyes dart towards me briefly, then hurriedly back to the paperback book he's reading."
    mx "...Hey,"

    show maxime casual surprised
    mcmaxime "I've got a little proposition for you."
    "Maxime's eyebrows shoot up to his hairline, the most expressive I've ever seen him."

    show mscmc jacket_hairdown basic
    show maxime casual smirk
    mx "Sorry, I'm not looking to be propositioned."

    show mscmc jacket_hairdown surprised
    show maxime casual smile
    mcmaxime "WHat? No no no, not like that!"

    show mscmc jacket_hairdown embarrassed
    show maxime casual basic
    "I wave my hands frantically, willing the blush out of my cheeks."

    show mscmc jacket_hairdown grin
    mcmaxime "I mean I want you as my surf instructor! I'm in the competition this weekend, and I hear you're the real deal. What do you think?"

    show maxime casual angry
    "Maxime purses his lips, his grip on his book tightening."

    show maxime casual basic
    mx "I see. But, I'm not interested in giving private lessons either. Sorry."

    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Ugh, I knew he'd be a difficult sell.)"

    show mscmc jacket_hairdown grin at left2
    show maxime casual smirk at right2
    mcmaxime "Hey, I'm not asking for much--just a few evening sessions until the competition, so it won't conflict with our teaching."

    show maxime casual basic
    mcmaxime "I could even take on a few of your kiddie lessons, if you're worried about hours."

    show mscmc jacket_hairdown smile
    "I lean against the bar, trying to catch his eye and see if I'm at all succeeding in buttering him up."

    "Unfortunately, he's as immovable as ever."

    show maxime casual sad
    mx "Miss..."

    show mscmc jacket_hairdown grin
    mcmaxime "[genericfn], just call me [genericfn]."

    show mscmc jacket_hairdown basic
    mx "[genericfn], I'm really not the instructor you're looking for."

    show mscmc jacket_hairdown grin
    mcmaxime "Why don't you let me be the judge of that?"

    hide maxime
    hide mscmc
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I lean in, leaving him no chance of returning to his book, and look up through my eyelashes."

    hide mscmc
    show maxime casual_cu basic_cu at maxime_cu
    "Maxime swallows, eyes finally locking with mine, and I can't help but notice the way his gaze drifts to my lips."

    show maxime casual_cu smile_cu
    "He tries to brush his reaction off with a chuckle."
    mx "So, the plan is to flirt with me into agreeing now?"

    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I bite back a thrilled shiver at his open acknowledgement."

    show mscmc jacket_hairdown_cu grin_cu
    mcmaxime "Is it working?"

    hide mscmc
    show maxime casual_cu basic_cu at maxime_cu
    mx "Mm..."
    "He considers me over his book, a slight smile tugging at his lips."

    show maxime casual_cu smirk_cu
    mx "I mean, is that all you got?"

    hide maxime
    "I gasp, offended."

    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcmaxime "Oh, I haven't even started, mister!"

    hide mscmc
    show maxime casual_cu smirk_cu at maxime_cu
    "Maxime is unruffled, seeming, for once, enjoying a little back-and-forth as he leans casually on the bar."
    mx "Alright. Show me what you've got, then."

    hide maxime
    $menuhideborder = True
    menu maximee1c3:
        "A. Show Maxime what you've got!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            "I cross my legs in response, leaning on the bar like some sort of old west cowgirl."
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "Jerry, my usual, and another of whatever this handsome guy is drinking."
            hide mscmc
            hide maxime
            "Jerry the bartender, ever the wingman, shoots me a thumbs-up."
            jr "One shot of mezcal and one painkiller coming right up."
            "I turn smugly back to Maxime, who's watching the proceedings with quiet interest."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(And promptly feel my mouth go dry just looking at him in the rose-tinted light.)"
            show mscmc jacket_hairdown_cu embarrassed_cu
            "(How do you flirt with someone that good-looking? He must know he's built like Hercules. What can I even say?)"
            hide mscmc
            show mscmc jacket_hairdown sad at left2
            show maxime casual basic at right2
            mcmaxime "Uh..."
            hide mscmc
            hide maxime
            "Jerry slams my painkiller on the counter, a bit of liquid courage."

            "I take a hasty sip, then point vaguely at Maxime."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Just blurt something out! Anything is better than awkward silence!)"
            hide mscmc
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "If you were a food, you'd be a fine-apple--like this drink."
            hide mscmc
            hide maxime
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(...Okay, not {i}anything{/i}.)"
            hide mscmc
            "Maxime was just about to raise his mezcal to his lips, and preemptively sputters, clapping a hand over his mouth."
            show mscmc jacket_hairdown sad at left2
            show maxime casual smile at right2
            mx "God, that was {i}bad{/i}..."
            "Even so, he's wheezing in surprised laughter, and actually reaches up to wipe his eye."
            show mscmc jacket_hairdown grin
            "I find myself laughing along, any embarrassment forgotten."
            mcmaxime "Well, I got you laughing, didn't I?"
            show mscmc jacket_hairdown sad
            show maxime casual basic
            "I smile, enjoying the light I've managed to coax out of him, then sign with a rueful chuckle."
            mcmaxime "Okay, maybe I'm not the Casanova I thought I was. Nobody said flirting was easy."
            show maxime casual smirk
            "Maxime grins, mischievous and fleeting."
            mx "I'd have thought it would be easy for a pretty woman."
            show mscmc jacket_hairdown surprised
            "I choke on my sip of painkiller, my entire face going up in flames."
            hide mscmc
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Unbelievable--he's a pro-surfer, {i}and{/i} a secret pro-flirter!)"
            show mscmc jacket_hairdown_cu sad_cu
            "(He's bamboozled me twice!)"
            hide mscmc
            show mscmc jacket_hairdown surprised at left2
            show maxime casual smirk at right2
            mcmaxime "Hold on, apparently you've been Mister Casanova all along!"
            hide mscmc
            hide maxime
            "I look up in shock, and our eyes finally lock for a good, long look."
            show maxime casual_cu basic_cu at maxime_cu
            "His eyes are a warm golden color, deep, with secrets like the bottom of the ocean, but also welcoming, and playful in the light."
            hide maxime
            "My lips part, and I feel locked in place, desperately wondering with he sees in me that has him so riveted"

            "Then Jerry turns on the ice blender, and we're snapped back to reality, breaking our gazes with flushed cheeks."
            show mscmc jacket_hairdown basic at left2
            show maxime casual basic at right2
            "I keep my voice soft, no longer worried about appearing alluring or in control."
            show mscmc jacket_hairdown grin
            mcmaxime "So, what book are you reading?"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            "He smiles faintly, lifting the cover to show me."
            hide mscmc
            hide maxime
            "It's a well-loved paperback, with an illustration of a girl in a meadow surrounded by animals."
            show mscmc jacket_hairdown smile at left2
            show maxime casual smile at right2
            mx "{i}Tales of the Wild{/i}--it's a fantasy series."
            mx "A girl winds up in a faraway land full of people who can shift into animals."
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmaxime "That's fun! It's an adventure story?"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "It's got a bit of everything--adventure, political intrigue, romance. Just how I like them."
            "He grins as my heart does a somersault."
            hide mscmc
            hide maxime
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Handsome {i}and{/i} he like romance subplots? Now that's just unfair.)"
            hide mscmc
            "I toy with one of my locs, trying to look casual."
            show mscmc jacket_hairdown grin at left2
            show maxime casual basic at right2
            mcmaxime "So you read a lot of fantasy?"
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Yeah, fantasy and sci-fi are my favorites. I like imagining different worlds, and different ways of being. Are you a big reader?"
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmaxime "I used to be as a kid, but then my free time got eaten up by after-school sports."
            mcmaxime "Don't get me wrong, I loved it--skateboarding was my big escape as a teen--but I do miss tearing through a good book."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "I'll pass {i}Tales of the Wild{/i} along to you when I'm done. I got it from a little lending library, so it deserves another good home."
            "He smiles easily, and for the moment I feel perfectly content and at ease, just the two of us relaxing at the bar."
            show maxime casual basic
            "To my surprise, he clears his throat, initiating a new line of converasetion."
            show maxime casual smile
            mx "You know, you shouldn't sell yourself short on flirting. You're nice to talk to; you ask good questions."
            show mscmc jacket_hairdown sad
            show maxime casual smirk
            mx "When you're not dealing out cheesy pick-up lines, that is."
            show mscmc jacket_hairdown grin
            show maxime casual smile
            "I roll my eyes instinctively, but can't stop myself from beaming, and when I look back at Maxime, he's doing the same."
            hide mscmc
            hide maxime
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(Good--I feel like I've finally built a bridge between us!)"
            hide mscmc
        "B. Sputter.":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left2
            show maxime casual basic at right2
            "I open my mouth to retort, and I feel my train of thought come to a crashing halt."
            hide mscmc
            hide maxime
            show maxime casual_cu basic_cu at maxime_cu
            "I stare up at Maxime, taking in his broad shoulders and expressive eyes, which are twinkling as he watches me."
            hide maxime
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Maxime is so hot...And hot people make me forget all my slick moves...)"
            show mscmc jacket_hairdown_cu angry_cu
            "(Wait, why are talking about flirting? It's winning the competition that's important!)"
            hide mscmc
            show mscmc jacket_hairdown basic at left2
            show maxime casual basic at right2
            "I shake my head furiously, grounding myself."
            hide mscmc
            hide maxime

    show mscmc jacket_hairdown grin at left2
    show maxime casual basic at right2
    mcmaxime "Look, I'm really serious about having you give me some pointers. I saw you on the water this afternoon--you're {i}amazing{/i}."

    hide mscmc
    hide maxime
    "Before he can protest, I reach out, laying my hand over his arm."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Which I've been secretly wanting to do since we met.)"

    hide mscmc
    show mscmc jacket_hairdown grin at left2
    show maxime casual basic at right2
    mcmaxime "Look, I can't pay much right now, I'll be honest with you, but I'll give you any of my winnings from the competition."
    mcmaxime "I think, working with you, I stand a really good chance of winning."
    show maxime casual sad
    "I beam confidently, but Maxime shakes his head, drawing away from me and closing up like a proverbial clam."
    show mscmc jacket_hairdown basic
    mx "If all you care about is winning, then you've set yourself up with a dream that could be snatched away at a moment's notice."
    show mscmc jacket_hairdown sad
    mcmaxime "But-!"
    "He stands up, sliding a pile of rumpled bills towards the bartender."
    mx "I'll cover hers."
    hide mscmc
    hide maxime
    "He starts to leave, and I leap up, calling after him."
    show mscmc jacket_hairdown surprised at centre
    mcmaxime "Don't think this is over--I'm going to persuade you, one way or another!"
    hide mscmc
    "To my surprise, he chuckles, looking back over his shoulder."
    show maxime casual smile at centre
    mx "Well, I'm looking forward to that."
    hide maxime
    "I'm not going to give up. I need to win him over."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(...but how?)"

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
