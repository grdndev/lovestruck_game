label maxime_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_sushirestaurant_lightson at bg
    play music msctense

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc jacket_hairdown basic at left4
    show maxime casual basic at right4
    "Maxime fills me in on our plan as we make our way to the pricey sushi restaurant Wikus selected for us to eat at."
    mx "I want to lift his phone and have a quick look through it while he's distracted."
    show mscmc jacket_hairdown surprised
    mcmax "What if he suspects we stole it?"
    show mscmc jacket_hairdown smile
    show maxime casual smirk
    mx "Oh, he'll never know it was missing—because it'll be back in his pocket by the end of the night."
    "I turn to Maxime in admiration of his confidence."
    mcmax "So you're pulling sleight of hand... twice?"
    show maxime casual basic
    mx "I'll have my lovely assistant direction his attention elsewhere, like any good magic trick. Are you alright with that?"
    show mscmc jacket_hairdown embarrassed
    show maxime casual smile
    "It takes me a moment to realize that I'm the 'lovely assistant' in this equation, and I hope my blush isn't showing."
    show mscmc jacket_hairdown smile
    mcmax "Anything in particular you'd like me to do?"
    show maxime casual basic
    mx "Just keep him talking and looking towards you instead of me."
    show mscmc jacket_hairdown grin
    mcmax "That shouldn't be too hard—in my experience, tech bros like him love a captive female audience."
    show maxime casual smile
    "Maxime laughs as his eyes scan the restaurant."

    play music mscsuspense
    hide mscmc
    hide maxime
    show wikus casual surprise at centre
    "Wikus notices us and waves us over to this table in the far corner."
    show wikus casual basic
    ws "[genericfn]! Maxime! I think we're all on a first name basis now, aren't we."
    show wikus casual smile
    "He doesn't wait for a response, pointing to the menu."
    ws "I've already ordered for us. You want to try the gunkan."
    hide wikus
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Okay, I guess we're trying the gunkan.)"
    show mscmc jacket_hairdown smile at left4
    show maxime casual basic behind mscmc at left1
    show wikus casual basic at right4
    "We talk pleasantries about the ocean conditions, when I notice the waiter approaching with our gunkan remarkably quickly."
    hide maxime
    hide wikus
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(And remembering the bloody shirt we found in the office...I'm not surprised that he scares them.)"
    show mscmc jacket_hairdown surprised at left4:
        ease 1 xoffset -30
        ease 0.8 xoffset 0
    show maxime casual basic behind mscmc at left1
    show wikus casual basic at right4
    "Maxime nudges my leg under the table to signal me to get Wikus talking, in a move that feels distractingly like playing footsie."
    mcmax "So, Mr. Sap—Wikus."

    hide mscmc
    hide maxime
    hide wikus
    $menuhideborder = True
    menu maximee06c1:
        "A. Ask him to mansplain sushi to you.":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left4
            show maxime casual basic behind mscmc at left1
            show wikus casual basic at right4
            mcmax "I have to confess, I've always wanted to get into sushi, but I don't know where to start. Any tips for beginners?"
            show wikus casual smile
            "Wikus straightens up, pleased."
            ws "The first step is asking the right person for advice! Before anything else, scratch California Rolls off your list. That's fake sushi."
            show mscmc jacket_hairdown grin
            show maxime casual basic:
                ease 1.2 xpos stagepos[1]-40
            pause 1.2
            "I nod, keeping my eyes wide and seemingly interested as Maxime shifts minutely."
        "B. Why did you want to talk to us?":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left4
            show maxime casual basic behind mscmc at left1
            show wikus casual basic at right4
            mcmax "It was kind of you to invite us out. What did I do to deserve such special treatment?"
            "Wikus pauses, eying me up and down as if sussing out how much I know."
            show wikus casual angry
            show maxime casual basic:
                ease 1.2 xpos stagepos[1]-40
            pause 1.2
            "I keep my face neutral, inviting his questioning while Maxime subtly slips his arm under the table."
            show wikus casual smile
            ws "I've always got my eye on the Next Big Thing, and that could very well be you, missy."
            show mscmc jacket_hairdown surprised
            ws "Call it being ahead of the curve on surf news."
            show mscmc jacket_hairdown basic
            "He winks."
        "C. Where are you from?":
            $menuhideborder = False
            show mscmc jacket_hairdown smile at left4
            show maxime casual basic behind mscmc at left1
            show wikus casual basic at right4
            mcmax "So, where are you from? I feel like I don't know much about you, other than that you're a patron of the surf community."
            show wikus casual angry
            "Wikus eyes me shrewdly over his drink, choosing his words carefully."
            show wikus casual smile
            ws "I'm from...a little coastal town in South Africa. No one's ever heard of it."
            show mscmc jacket_hairdown grin
            show maxime casual basic:
                ease 1.2 xpos stagepos[1]-40
            pause 1.2
            show wikus casual surprise
            mcmax "Oh, my aunt vacationed in Cape Town once. She said it was lovely."
            show mscmc jacket_hairdown smile
            show wikus casual smile
            ws "Yeah, it's kinda like that, but not as big of a city."
            hide maxime
            hide maxime
            show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
            "(Except for the part where it's probably a mermaid town under the water.)"


    show mscmc jacket_hairdown smile at left4
    show maxime casual basic behind mscmc,wikus:
        xpos stagepos[1]-40
    show wikus casual smile at right4
    "Beside me, Maxime calmly picks up his chopsticks."
    show mscmc jacket_hairdown surprised
    show wikus casual surprise
    show maxime casual surprised:
        ease 0.4 xpos stagepos[1]+80
        ease 0.3 xpos stagepos[1]-100
    pause 0.7
    "At lightning speed, a glob of wasabi goes shooting off Maxime's plate..."
    show mscmc jacket_hairdown smile
    "Seemingly by accident, and splatters right in the middle of Wikus' shirt collar."
    show maxime casual sad
    show wikus casual angry:
        ease 0.15 yoffset -30
        ease 0.15 yoffset 0
    "Wikus leaps up as if he's been stung."
    ws "Damn it, this is tailored!"
    mx "I'm {i}so{/i} sorry..."
    show mscmc jacket_hairdown surprised
    show maxime casual basic
    show wikus casual angry at out_right
    "Wikus sprints away before we can say anything else, yelling and pushing a waiter back."
    show maxime casual smile
    ws "I have exactly one minute to get this stain out!"
    show mscmc jacket_hairdown smile
    "Once he's gone, the sushi restaurant feels strangely quiet."
    show mscmc jacket_hairdown surprised
    show maxime casual smirk
    "Maxime nudges me under the table, and I look down to find Wikus' phone resting in his lap."
    show mscmc jacket_hairdown smile:
        ease 0.6 xpos stagepos[1]-220
    show maxime casual embarrassed
    "I scoot nearer to Maxime, keeping an eye on the hallway leading to the restrooms."
    show maxime casual basic
    mcmax "What if we can't figure out his passcode?"
    show mscmc jacket_hairdown surprised
    show maxime casual smirk
    mx "Camilla gave me his birthdate."
    show maxime casual smile
    "He punches four numbers in, and the phone miraculously unlocks."
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(That was a TV-spy move!)"
    show mscmc jacket_hairdown grin at left3
    show maxime casual basic behind mscmc at left1
    mx "It's the go-to password for a man who's full of himself. Alright, Wikus, let's see what you're hiding."
    show mscmc jacket_hairdown surprised
    show maxime casual smirk
    "Without thinking, I lay my hand on Maxime's shoulder, pointing to one of the app icons."
    show maxime casual basic
    mcmax "I know that app! Trina uses it to check the security cam footage at the Surf Shack."
    show mscmc jacket_hairdown basic
    show maxime casual surprised
    "Maxime raises his eyebrows."
    show mscmc jacket_hairdown surprised
    show maxime casual basic
    mx "Interesting. Wonder why he doesn't let his security team handle that."
    show mscmc jacket_hairdown basic
    "He opens the app, and a grainy live feed pops up on screen."
    show mscmc jacket_hairdown sad
    "It shows a dark windowless lab, far removed from the polished neatness of the tournament headquarters."
    show mscmc jacket_hairdown surprised
    mcmax "Where {i}is{/i} that?"
    show maxime casual angry
    "There's some sort of machine just out of view, and iron bars separate the room in half."
    show mscmc jacket_hairdown sad
    "Something shifts in the shadows, and my grip on Maxime's shoulder tightens."
    show mscmc jacket_hairdown surprised
    mcmax "Oh my God, there's someone down there, behind the bars!"
    show mscmc jacket_hairdown sad
    "Whoever it is is slumped against the bars, a tousled head of sea-bleached blond hair resting on his knees."
    show mscmc jacket_hairdown angry
    "I keep my voice hushed, whispering franctically."
    mcmax "That's Raymond! Wikus really did kidnap him. We need to help him!"
    show mscmc jacket_hairdown sad
    show maxime casual angry
    "I look at Maxime helplessly, but he's all business, already flipping through Wikus' other apps."
    mx "Look at his notes app."
    show mscmc jacket_hairdown surprised
    mcmax "'Subject is recovering physically, though mental state remains tenuous. Will continue to monitor.' Is he talking about Raymond?!"
    mx "Apparently the habit of unethical experimentation dies hard. Human experimentation though, that's messed up."
    show mscmc jacket_hairdown sad
    show maxime casual basic
    "Maxime is grimly determined, but perfectly composed, so that none of the servers or guests notice anything wrong."
    show mscmc jacket_hairdown angry
    "I can't say the same for myself, and I'm sure he can feel my hand shaking on his shoulder."
    show maxime casual sad
    mx "[genericfn]."
    hide mscmc
    show maxime casual_cu sad_cu at maxime_cu
    "When Maxime turns to me, his voice is gentile, and he lays his hand over mine."
    mx "I know, it's an awful thing to see. Take a few deep breaths."
    show mscmc jacket_hairdown sad at left3
    show maxime casual angry behind mscmc at left1
    "I shudder, looking at the place where Wikus was sitting moments before."
    show maxime casual sad
    mcmax "I can't believe I'm having dinner with...I don't even know what to call him. The kind of person who kidnaps people for science."
    hide mscmc
    show maxime casual_cu sad_cu at maxime_cu
    "Maxime shifts his hand so he's securely gripping my shoulder."
    "His palm feels rough and warm, grounding me."
    show maxime casual_cu basic_cu
    mx "If you need to leave..."

    hide maxime
    $menuhideborder = True
    menu maximee06c2:
        "A. I'll let you know.":
            $menuhideborder = False
            show mscmc jacket_hairdown sleep at left3
            show maxime casual basic behind mscmc at left1
            "I nod swallowing hard."
            show mscmc jacket_hairdown basic
            show maxime casual sad
            mcmax "I'll let you know if it's getting to be too much. I promise—I wouldn't do anything to jeopardize your mission."
            show mscmc jacket_hairdown smile
            "I smile, trying to appear reassuring."
            show mscmc jacket_hairdown basic
            mcmax "Right now, I'm okay though. But I'm {i}furious{/i} with Wikus."
        "B. We've got to save Raymond.":
            $menuhideborder = False
            show mscmc jacket_hairdown sleep at left3
            show maxime casual sad behind mscmc at left1
            "I shake my head, smoothing my hair back and trying to ground myself."
            show mscmc jacket_hairdown angry
            show maxime casual basic
            mcmax "It doesn't matter how I feel—I can't step away now."
            show mscmc jacket_hairdown sad
            show maxime casual sad
            mcmax "I'd never forgive myself for knowing someone was in trouble but leaving before I had helped get them out of it."

        "C. I'm not letting you do this alone.":
            $menuhideborder = False
            show mscmc jacket_hairdown basic at left3
            show maxime casual sad behind mscmc at left1
            mcmax "No way."
            "I shake my head firmly, finding comfort in our familiar argument."
            show mscmc jacket_hairdown angry
            show maxime casual basic
            mcmax "I'm not letting you go up against this freak on your own."
            mcmax "I know you can handle yourself, but it's better to have a buddy. Someone to watch your back."
            "I squeeze his arm affectionately."

    show mscmc jacket_hairdown angry at left3
    show maxime casual angry behind mscmc at left1
    "Maxime nods understandingly."
    show mscmc jacket_hairdown surprised
    mx "Whatever happens with Wikus, I won't let anything happen to you."
    show mscmc jacket_hairdown basic
    show maxime casual basic
    mx "Right now, we've just got to get through lunch, and not let on that we know anything. Do you think you can do that?"
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I think I'd better get it together fast before Wikus comes back.)"
    show mscmc jacket_hairdown basic at left3
    show maxime casual basic behind mscmc at left1
    "I sit up straighter, glaring at the restroom doors."
    mcmax "I'm ready. Let's sneak Dr. Evil his phone back."

    play music mscaction
    show mscmc jacket_hairdown smile
    show wikus casual basic at right4, right_in
    "By the time Wikus returns, I've composed my face into a neutral smile."
    show mscmc jacket_hairdown sad
    "His shirt is damp and rumpled, which makes him look faintly unhinged."
    show mscmc jacket_hairdown smile
    "I smile apologetically."
    mcmax "Hey, Wikus. How's your shirt?"
    show wikus casual smile
    "He returns my smile with one that's more of a grimace."
    show mscmc jacket_hairdown basic
    show wikus casual basic
    ws "I know the manufacturer. I'll ask for a new one, gratis."
    show wikus casual smile
    ws "Now, to finish this gunkan."
    show mscmc jacket_hairdown sleep
    "He tucks in greedily."
    show mscmc jacket_hairdown basic
    "I glance at Maxime, the phone in his hand and obscured by the table."
    show mscmc jacket_hairdown surprised
    mcmax "So, I..."
    show wikus casual surprise
    ws "Is something wrong with your meal?"
    "Wikus jabs his chopsticks suspiciously at my plate."
    show wikus casual smile
    ws "You haven't eaten much. I'll tell the chef to make it again..."
    show mscmc jacket_hairdown grin
    show wikus casual surprise
    mcmax "No, no, it's perfectly fine! I'm a light eater is all."
    show mscmc jacket_hairdown surprised
    "Feeling his gaze on me, I hastily stuff a roll in my mouth, aware that the table is ominously silent."
    show wikus casual smile
    ws "Well?"
    show mscmc jacket_hairdown grin
    "I smile awkwardly, my cheeks full of rice."
    show maxime casual sad
    mcmax "'S great!"
    show maxime casual basic
    show wikus casual angry
    "To my horror, Wikus looks between Maxime and me, as if suspecting us of colluding."
    show mscmc jacket_hairdown sad
    show maxime casual smile
    "Maxime relaxes his shoulders, looking innocent and at-ease even as Wikus' phone rests against his knee."
    show mscmc jacket_hairdown basic
    ws "Did I miss something?"
    show mscmc jacket_hairdown surprised
    show maxime casual sad
    mcmax "What? No, not at all!"
    hide maxime
    hide wikus
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(How could he possibly know?!)"
    show mscmc jacket_hairdown surprised at left3
    show maxime casual basic behind mscmc at left1
    show wikus casual smile at right4
    "Wikus folds his hands, leaning over the table with a condescending smile."
    ws "Really. Because I've been around the block a few times, and I know when a man and a woman are hiding something."
    hide maxime
    hide wikus
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Phew! If he thinks we've been making out inthe corner at least that throw shim off the scent.)"

    play music mscsuspense
    show mscmc jacket_hairdown basic at left3
    show maxime casual basic behind mscmc,wikus at left1:
        xpos stagepos[1]-100
        ease 0.5 xpos stagepos[1]
    show wikus casual smile at right4:
        xpos stagepos[1]+270
        ease 0.5 xpos stagepos[1]+220
    "Maxime tries to take advantage of Wikus patrinizing me, but as he leans forward, Wikus leans back, shoulder checking him."
    show mscmc jacket_hairdown surprised
    show maxime casual surprised
    show wikus casual surprise
    mx "Pardon me."
    show mscmc jacket_hairdown basic
    show wikus casual angry
    "Wikus shoots Maxime a heavy glare."
    "In a panic, I blurt out the first thing that comes to mind."

    hide mscmc
    hide maxime
    hide wikus
    $menuhideborder = True
    menu maximee06c3:
        "A. Ahh, my contact!":
            $menuhideborder = False
            show mscmc jacket_hairdown sleep at left3
            show maxime casual basic behind mscmc,wikus at centre
            show wikus casual angry at right3
            mcmax "Ahh, I lost a contact!"
            show mscmc jacket_hairdown sad:
                ease 0.3 yoffset 120
            show maxime casual smirk
            pause 0.3
            "I drop to my hands and knees, bumping the table as I crawl around beneath it."
            show maxime casual basic:
                ease 0.6 xoffset 40
                ease 0.3 xoffset 0
            show wikus casual basic
            pause 0.9
            "The waiter hurries over, fussing along with Wikus, and in the ensuing chaos Maxime neatly slips the phone into Wikus' pocket."
            show maxime casual sad
            "Maxime peers under the table, making a show of concern."
            show wikus casual angry
            mx "Did you find it?"
            mcmax "No, it's probably trampled by now...Oh well."
            show mscmc jacket_hairdown sad:
                ease 0.3 yoffset 0
            pause 0.3
            "I sigh, sliding back into my seat."
        "B. Oh no, I'm so klutzy!":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left3:
                ease 0.8 xoffset -50
            show maxime casual basic behind mscmc,wikus at centre
            show wikus casual angry at right3
            pause 0.8
            "I shift my foot, pretending to get caught in the strap of my purse."
            show maxime casual smirk
            mcmax "Oh!"
            show mscmc jacket_hairdown surprised:
                ease 0.3 xoffset 40
            show maxime casual basic
            show wikus casual surprise
            pause 0.3
            "I stumble forward, as clumsy as a plot device in a YA novel."
            show mscmc jacket_hairdown smile
            show maxime casual smirk
            show wikus casual basic
            mcmax "Jeeze, I'm all feet when I'm not surfing."
            show mscmc jacket_hairdown grin
            show maxime casual basic
            "I laugh nervously, grasping the table and setting the dishes rattling."
            show mscmc jacket_hairdown basic
            show maxime casual basic:
                ease 0.6 xoffset 40
                ease 0.3 xoffset 0
            show wikus casual angry
            pause 0.9
            "Wikus eyes me disapprovingly, giving Maxime ample time to slip the phone back in the evil man's pocket."
            show mscmc jacket_hairdown grin:
                ease 0.8 xoffset 0
            show wikus casual basic
            pause 0.8
            ws "Careful, that's an expensive bottle of sake."
        "C. Waiter, please help us.":
            $menuhideborder = False
            show mscmc jacket_hairdown sad at left3
            show maxime casual basic behind mscmc,wikus at centre
            show wikus casual angry at right3
            "I manage to catch the eyes of our waiter, giving him a pained expression."
            "He nods in sympathy, grimacing at the back of Wikus' head."
            show mscmc jacket_hairdown surprised
            show maxime casual smirk
            show wikus casual surprise
            "A moment later, a gust of flame shoots up in the kitchen, prompting Wikus to snap his head around."
            show maxime casual basic:
                ease 0.6 xoffset 40
                ease 0.3 xoffset 0
            pause 0.9
            $sidecharone = "Chef"
            sid1 "Nothing to worry about, everything's under control!"
            show mscmc jacket_hairdown smile
            show wikus casual basic
            "When Wikus turns back to us, rolling his eyes, the phone is safely returned to his jacket pocket."

    show mscmc jacket_hairdown smile at left3
    show maxime casual basic at centre
    show wikus casual angry at right3
    "Wikus gives the sushi restaurant a last dissatisfied look, tossing his napkin aside."
    ws "Well, that was an...odd lunch. Shall we?"
    show mscmc jacket_hairdown smile at out_left
    pause 0.2
    show maxime casual basic at out_left
    show wikus casual smile
    "He gestures me ahead politely, and Maxime and I thankfully exit the dark restaurant for the sunny boardwalk beyond."

    scene bg msc_boardwalk_sunset_people at bg with wiperightdissolve
    play music mscbeach
    show mscmc jacket_hairdown basic at left1plus
    show maxime casual basic behind mscmc at right1plus
    "We keep our gaits slow and casual until we're out of sight of Wikus and the restaurant."
    show mscmc jacket_hairdown grin
    show maxime casual surprised
    "When we reach the familiar, comforting sight of the boardwalk carousel, I start to giggle nervously."
    show mscmc jacket_hairdown sad
    show maxime casual basic
    mcmax "That was close..."
    show mscmc jacket_hairdown smile
    show maxime casual smile
    "Maxime lets out a chuckle of his own and relieved sigh."
    mx "Laughter's a good way to let the nerves out."
    show mscmc jacket_hairdown basic
    show maxime casual basic:
        ease 0.5 xoffset -60
    "He puts his hand on my back as I wipe my eyes, then I suddenly sober up, remembering wehat we saw on Wikus' phone."
    show mscmc jacket_hairdown sad
    show maxime casual sad
    mcmax "God...poor Raymond."
    "Maxime puts his arm around my shoulders, giving me a reassuring squeeze."
    show maxime casual basic
    mx "I know. You were amazing in there, though."
    mx "We're going to help Raymond. Is there any way I can make that terrible lunch up to you? A small reward for spy work well done?"
    show mscmc jacket_hairdown basic
    "He nods towards the shops along the boardwalk, trying to coax a smile from me."
    hide maxime
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(If he's really offering me anything, what I want most is to get him to open up more.)"
    show mscmc jacket_hairdown surprised at left1plus
    show maxime casual basic behind mscmc at right1plus:
        xoffset -60
    "I'm seized with an idea."
    show mscmc jacket_hairdown basic
    mcmax "Can we play Ask Me Anything? There's things I want to know about you."
    show maxime casual surprised
    mx "Really? That's what you want?"
    hide mscmc
    hide maxime
    show maxime casual_cu smile_cu at maxime_cu
    "He cocks his head, then shrugs willingly."
    mx "Go for it."

    hide maxime
    $menuhideborder = True
    menu maximee06c4:
        "A. Ask Maxime about love and his past." (paidchoice = "paidchoice"):
            $menuhideborder = False
            play music mscromance
            show mscmc jacket_hairdown smile at left1plus
            show maxime casual basic behind mscmc at right1plus:
                xoffset -60
            "I turn to Maxime coyly, slowing my steps as we walk along the promenade."
            show maxime casual surprised
            mcmax "Alright, what's your 'type'?"
            show maxime casual embarrassed
            "Maxime chuckles, possibly out of nerves, but then gives me an innocent look."
            show maxime casual smirk
            mx "My type of what? Surfboards?"
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmax "Come on, play fair. You promised me a game of Ask Me Anything."
            show mscmc jacket_hairdown embarrassed
            show maxime casual smile
            "Maxime raises his eyebrows, more amused than anything."
            show mscmc jacket_hairdown smile
            show maxime casual basic
            mx "Well, I don't really have a type for looks."
            show maxime casual smile
            mx "I like women with a passion for something."
            show maxime casual basic
            mx "I love to be able to learn something from who I'm dating, and maybe she can learn stuff from me, I don't know."
            hide mscmc
            hide maxime
            show maxime casual_cu embarrassed_cu at maxime_cu
            mx "And I like 'em a little fiery."
            show maxime casual_cu smirk_cu
            "He winks at me, then clears his throat, seeming surprised at his own boldness."
            show mscmc jacket_hairdown embarrassed at left1plus
            show maxime casual sleep behind mscmc at right1plus:
                xoffset -60
            "I'm also left flustered, and quickly distract him with another question."
            show mscmc jacket_hairdown smile
            show maxime casual basic
            mcmax "Question two! Have you had any serious relationships before?"
            show mscmc jacket_hairdown surprised
            show maxime casual sleep
            "He shakes his head, chuckling."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "I've had two girlfriends. The first one, Lara, was in high school. Broke up when we got into different colleges. Tragic."
            show mscmc jacket_hairdown surprised
            mcmax "Under-the-sea high school."
            show mscmc jacket_hairdown grin
            mx "Yes, mer school. And before you ask, it's all tests and homework too, it just happens to be under the sea."
            show mscmc jacket_hairdown smile
            mcmax "That's a bummer. I had this great vision of you and Lara learning to herd dolphins."
            "He snorts, but my joke appears to have put him more at ease."
            mx "Trust me, the dolphins are fine without our meddling."
            show mscmc jacket_hairdown basic
            show maxime casual basic
            mx "After college, I dated another girl."
            show maxime casual sad
            "He hesitates, his gaze briefly turning out towards the beach."
            show maxime casual basic
            mx "But it was around that time I started working for my government branch."
            show mscmc jacket_hairdown surprised
            show maxime casual sad
            mx "I wasn't allowed to tell her anything about my job. She was smart, and she could tell I was hiding something."
            show maxime casual basic
            mx "It wasn't fair to her, dating someone who would always keep secrets and get called away for days on end."
            show mscmc jacket_hairdown basic
            mx "I don't blame her for moving on. I have too now."
            show mscmc jacket_hairdown sad
            mcmax "Oh."
            show mscmc jacket_hairdown sad:
                ease 0.6 xoffset 30
            pause 0.6
            "I reach out and briefly brush his arm."
            show mscmc jacket_hairdown basic
            show maxime casual smile
            "He smiles thankfully, then sighs."
            show mscmc jacket_hairdown surprised
            show maxime casual sleep
            mx "It's a lesson I had to learn at some point: working as a spy requires a certain level of loneliness."
            show maxime casual sad
            mx "At the time I believed the work I was doing was worth it."
            show maxime casual angry
            "He trails off, pausing to admire the ocean, unspoken words hanging in the air."
            hide maxime
            hide mscmc
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(So maybe he doesn't think the loneliness is worth it anymore...)"
            show mscmc jacket_hairdown_cu sad_cu
            "(His job demands so much of him. He couldn't tell anyone what he was doing or what kind of danger he's constantly in.)"
            show mscmc jacket_hairdown_cu smile_cu
            "(I'm glad he found me again. At least I can be here for him, if only for a little while.)"
            hide mscmc
            show maxime casual_cu smile_cu at maxime_cu
            "He shakes his head, then turns to me, voice lightening and sounding a little playful."
            show maxime casual_cu smirk_cu
            mx "Well, what about you? Can I ask about your type?"
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I snort, kicking a stray pebble off the boardwalk and back onto the sand."
            show mscmc jacket_hairdown_cu basic_cu
            mcmax "All my relationships have been pretty short lived."
            show mscmc jacket_hairdown_cu smile_cu
            mcmax "I mean, I thought I was in love one time, but looking back it was only an infatuation."
            show mscmc jacket_hairdown basic at left1plus:
                xoffset 30
            show maxime casual basic behind mscmc at right1plus:
                xoffset -60
                ease 0.8 xoffset 0
            pause 0.8
            "I wonder if I'm oversharing, but Maxime leans on the nearest railing, listening attentively, so I keep talking."
            mcmax "I'm not sure I've ever really been in love, like, really in love. I suppose that's a common twenty-something conundrum, though."
            show mscmc jacket_hairdown sad
            show maxime casual smile
            "Maxime chuckles, warm and smooth."
            show mscmc jacket_hairdown embarrassed
            mx "I don't know about that. Love is the sort of thing that when you know, you know."
            mx "There won't be any doubts left in your mind when it happens. Love's too powerful a feeling to leave room for doubt."
            show mscmc jacket_hairdown surprised
            mcmax "Really?"
            "I badly want that to be true, but it sounds almost too romantic, like a fairy tale."
            hide mscmc
        "B. Get flustered.":
            $menuhideborder = False
            play music mscromance
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcmax "I am flustered."
            hide mscmc

    show maxime casual_cu embarrassed_cu at maxime_cu
    "I turn to Maxime, a question on my lips, and find him staring at me, his eyes meeting mine."
    "I'm stunned into silence, the sea breeze blowing gently around us."
    show maxime casual_cu smile_cu
    mx "[genericfn]..."
    show maxime casual_cu basic_cu
    "Maxime reaches for me, his hand hovering between us."
    show maxime casual_cu smirk_cu
    "My heart is pounding."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mcmax "Yes?"
    hide mscmc
    scene bg msc_maxime_s1_ei2 at bg with fade:
        xanchor 0.1
        yanchor 0.6
        linear 8 yanchor 0.25
    pause
    "He pulls me into his arms, gentle but firm."
    "My feet are swept off the deck as he leans me back in an elegant and graceful dip, his face only inches from mine."
    "I gasp, as his eyes fall to my lips."
    "(Please, please kiss me, Maxime!)"

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
