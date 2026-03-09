label maxime_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_maxime_studio_sunset at bg
    play music mscsuspense

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcmax "I've got a better idea: you'll be my trainer, and I'll help you spy on Sapor!"
    show mscmc jacket_hairdown smile at left2
    show maxime casual surprised at right2
    "I wait expectantly, watching a flurry of emotions pass over Maxime's face."
    hide maxime
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Of course he doesn't want to get me involved—that's just the kind of guy he is—but I can tell he doesn't want to part ways so soon.)"
    show mscmc jacket_hairdown basic at left2
    show maxime casual sad at right2
    "When he speaks, his words are careful and measured."
    mx "[genericfn], I know you want to help, but I'd worry about you if you were involved. We don't know what Sapor's planning."
    show mscmc jacket_hairdown smile
    "I nod, trying to hide a smile."
    mcmax "I know—it's a complete unknown. So wouldn't we both feel better if I was in-the-loop?"
    show maxime casual smile
    "Maxime chuckles despite himself, shaking his head."
    show maxime casual smirk
    mx "Don't think I don't see what you're doing."
    show maxime casual sad
    mx "You make a fair point, though—I want you to know what you're getting into with Sapor, even if nothing comes of it."
    show mscmc jacket_hairdown basic
    show maxime casual basic
    "He lays his palms together, leaning forward seriously."
    mx "I mentioned Sapor's terminated research with the university."
    mx "I don't have access to the university's records, but I know from my own briefing that a lot of his theories are pretty...out there."
    show maxime casual sad
    mx "I've heard the term 'mad scientist' slung around when referring to him."

    hide mscmc
    hide maxime
    $menuhideborder = True
    menu maximee02c1:
        "A. Seriously?":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show maxime casual basic at right2
            mcmax "Really?"
            mcmax "These days, it seems like you have to do something really over-the-top to get labeled a 'mad scientist'."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "Well, I'll admit, we mer love a good scandal as mich as humans do, so there's probably some exaggeration going on."
            show mscmc jacket_hairdown basic
            show maxime casual sad
            mx "It's possible we're overreacting—but Camilla and I still want to plau it safe."
        "B. That must be an exaggeration.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show maxime casual basic at right2
            mcmax "Okay, but that must be an exaggeration. What is he, a villain from a spy novel?"
            show maxime casual smile
            "Maxime smiles despite himself."
            show mscmc jacket_hairdown smile
            mx "I don't mean to imply he has a secret volcano base—though I'll never say never."
            show mscmc jacket_hairdown basic
            show maxime casual sad
            mx "But I don't like the thought of a guy known for unethical experiments running a tournament for a bunch of surfers."
        "C. Big yikes.":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show maxime casual basic at right2
            "My eyes widen, images straight out of a superhero comic flashing through my mind."
            mcmax "Oof. That's a red flag if I ever heard one."
            show maxime casual smile
            "Maxime smiles, gratified."
            show mscmc jacket_hairdown basic
            show maxime casual sad
            mx "I'm glad you agree."
            mx "Like I said, headquarters hasn't given him much thought, but this tournament business is too strange to be entirely innocent."


    play music mscmaxime
    "Maxime inclines his head."
    mx "We don't have any solid evidence yet."
    show maxime casual surprised
    mx "For all we know, he might just be integrating into land-dweller society now that he's out of a job in Maritas."
    show maxime casual sad
    mx "He's not the bureau's top priority, but Camilla's wary of him, and this is one point I'm inclined to agree with her on."
    show maxime casual basic
    "He arches an eyebrow, as if sizing me up for how I'd do in a fight against a so-called 'mad scientist'."
    hide maxime
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(But I won't be denied!)"
    show mscmc jacket_hairdown grin at left2
    show maxime casual basic at right2
    mcmax "Right! So if we're going to be spending time around this guy, it would be better if we had each other's backs."
    show mscmc jacket_hairdown surprised
    mcmax "I mean, not that you need the help—and I can probably look after myself—but..."
    show mscmc jacket_hairdown grin
    mcmax "Well, I want to help you, and I want to make sure that everyone in the tournament is safe."
    show mscmc jacket_hairdown smile
    show maxime casual sad
    "Maxime taps the edge of the counter, still deliberating."
    show maxime casual smile
    mx "I always planned to keep an eye on out—not that you need it, but just because I like you."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(He likes me! I mean, I thought so, but it's nice to hear him say it out loud.)"
    show mscmc jacket_hairdown basic at left2
    show maxime casual sad at right2
    "Before I can jump in, Maxime sighs, growing serious."
    mx "But involving civilians in my line of work doesn't feel right."
    show mscmc jacket_hairdown surprised
    mcmax "I know I'm not trained for this kind of thing—but do I have to be your cover story?"
    "I lay my hand dramatically over my heart."
    show mscmc jacket_hairdown angry
    show maxime casual basic
    mcmax "And I promise, on my surfboard, that I'll follow your lead and do what you say."
    mcmax "...For the spy stuff, that is."
    show maxime casual smile
    "I mock-glare, and Maxime snorts, giving in to amusement."
    show mscmc jacket_hairdown smile
    mx "Trust me, I know you're your own boss. I wouldn't dream of ordering you around."
    "I smile, folding my hands in my lap."
    show mscmc jacket_hairdown grin
    mcmax "See, this is what I like about you, Maxime Okun."
    show maxime casual embarrassed
    "He flushes and clears his throat, quickly turning back to business."
    show maxime casual smile
    mx "But I appreciate the promise, and the offer."
    show maxime casual smirk
    mx "Alright, you're in, Miss Cover Story."
    hide mscmc
    show maxime casual_cu smile_cu at maxime_cu
    "He extends his hand, and I eagerly shake in agreement, enjoying the feeling of his warm, calloused palm."
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcmax "Glad to hear it, 'partner'!"
    show mscmc jacket_hairdown smile at left2
    show maxime casual smile at right2
    "Maxime grins, but his eyes briefly cloud, and he clears his throat, glancing out the window."
    show maxime casual sad
    mx "Listen, I'm glad we'll get a little more time together...But my job..."
    show mscmc jacket_hairdown sad
    "He hesitates, struggling over his words, and I take pity on him."
    show mscmc jacket_hairdown grin
    mcmax "I get it. We're working friends, just like when you taught at the Surf Shack—only with more espionage."
    show maxime casual smile
    "Maxime shoots me a quick, thankful smile."
    hide mscmc
    show maxime casual_cu basic_cu at maxime_cu
    "His eyes linger on my lips before rising to meet my gaze."
    hide maxime
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "I feel as though I'm caught in a trance, afraid to move and break the spell, but he finally stands up, stretching and glancing around."
    show mscmc jacket_hairdown smile at left2
    show maxime casual smile at right2
    mx "Can I walk you home? Otherwise I'll worry until you text."

    scene bg msc_maxime_studio_night at bg
    show mscmc jacket_hairdown grin at left2
    show maxime casual smile at right2
    "I hop up, excited to spend a little more time with him as the sun finishes its slow descent beneath the horizon."
    mcmax "Of course! Wouldn't want to run into any mad scientists on the beach, would I?"

    hide mscmc
    hide maxime
    scene bg msc_labeach_night at bg with fade
    play music mscmctheme
    "It's a lovely, clear night, and Maxime and I walk along the beach, the break of the waves a soothing backdrop."
    show mscmc jacket_hairdown grin at left2
    show maxime casual basic at right2
    mcmax "It really is good to see you again."
    show maxime casual smile
    mx "You too, super star. I'm glad to see you doing so well, and keeping up with the competitions."
    show mscmc jacket_hairdown embarrassed
    "He smiles at me, and when I glance back at him I have a sudden urge to grab his hand, but force it away."

    play music mscromance
    hide maxime
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Come on, [genericfn]—you promised!)"
    "(We're just friends, working together. We can't be anything else.)"
    show mscmc jacket_hairdown smile at left2
    show maxime casual basic at right2
    "I shove my hands in my pockets, trying to distract myself."
    show mscmc jacket_hairdown grin
    mcmax "So, what have you been doing with yourself these past few months?"
    show mscmc jacket_hairdown smile
    mx "I had to go back to Maritas for a training course—regular recertification stuff."
    "He shrugs, then glances out over the sea wistfully."
    show maxime casual embarrassed
    mx "I thought about you a lot..."
    mx "I even wrote you a letter, though I was too embarrassed to send it."
    show mscmc jacket_hairdown grin
    "I stumble over the sand, staring up at him excitedly."
    mcmax "Wait, you wrote me a letter?! What do you mean 'embarrassed'? You should have sent it!"
    "Maxime rubs the back of his neck bashfully."
    show maxime casual smile
    mx "Well, you know me...I'm a visual artist, not a writer. Words just don't come out right for me sometimes."
    mx "It wasn't a very good letter, I ended up throwing it into the North Pacific Current."
    show maxime casual basic
    mcmax "Dramatic! You surprise me, emo-boy."
    show maxime casual smile
    "He breaks out in a laugh, then glances coyly at me."
    hide mscmc
    show maxime casual_cu embarrassed_cu at maxime_cu
    mx "Well, I could tell you what it said, if you're interested."

    hide maxime
    $menuhideborder = True
    menu maximee02c2:
        "A. Find out what Maxime wrote in his letter to you!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "I lean in, grinning impishly."
            mcmax "Oh, I would be {i}very{/i} interested to hear what you wrote to me."
            show mscmc jacket_hairdown grin at left2
            show maxime casual embarrassed at right2
            "Maxime clears his throat, cheeks turning a darker shade, and his eyes quickly flicker out to sea."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Aw, is it easier if he's not looking at me? That's kind of cute.)"
            "(Honestly, it's sweet how bashful he is sometimes.)"
            "(I know he says he has a hard time showing his feelings, but I appreciate that he never tries to put up a tough-guy front.)"
            show mscmc jacket_hairdown smile at left2
            show maxime casual basic at right2
            mx "I started out apologizing for only being able to write you a letter. It didn't seem quite enough, after the time we spent together."
            show mscmc jacket_hairdown grin
            show maxime casual embarrassed
            mcmax "I don't know about that. People don't send enough letter these days—it's a nice gesture."
            "He's still too shy to look at me, but I notice his mouth twitch in a faint smile, pleased."
            mx "Well, I'll keep that in mind for the future."
            show mscmc jacket_hairdown smile
            show maxime casual sad
            mx "Then I realized I should really be apologizing for having up and left, and dragging you into my business in the first place."
            show mscmc jacket_hairdown grin
            show maxime casual smile
            mcmax "That's a lot of apologies you didn't really need to make."
            mx "Yeah, I could sense it was getting a bit excessive."
            show mscmc jacket_hairdown smile
            show maxime casual sad
            mx "I went back and forth for a while, worrying about whether you'd get bored of me and stop reading."
            show mscmc jacket_hairdown basic
            show maxime casual smile
            "I sigh, fond but exasperated."
            show mscmc jacket_hairdown grin
            show maxime casual basic
            mcmax "That certainly sounds like something you'd do."
            show mscmc jacket_hairdown sad
            show maxime casual sad
            "He kicks the sand where it's dampened by the waves, ruminating."
            show mscmc jacket_hairdown basic
            mx "What I really wanted to say, before I got myself all muddled, was 'thanks for everything'."
            show mscmc jacket_hairdown embarrassed
            mx "It meant a lot, finding someone to share my secrets with."
            show mscmc jacket_hairdown basic
            show maxime casual smile
            mx "But the letter was getting so rambly and in serious danger of becoming melodramatic."
            show mscmc jacket_hairdown smile
            show maxime casual basic
            "I snicker, hiding my laugh behind my hand."
            show mscmc jacket_hairdown grin
            mcmax "Maxime, I'm not sure your definition of 'melodramatic' is really fair to yourself. There's nothing wrong with being expressive."
            show mscmc jacket_hairdown smile
            show maxime casual smile
            mx "I suppose not. But I couldn't seem to get the words right, so that's about when I banished the letter to the North Pacific Current."
            mx "It seemed appropriate, like maybe the currents would carry the essence of what I was trying to say to you—I don't know, something poetic like that."
            show maxime casual sad
            "He shakes his head, exasperated with himself, and I reach out to touch his arm."
            show mscmc jacket_hairdown grin
            mcmax "Aw, we're all allowed a flowery letter now and again, Maxime! Come on."
            show mscmc jacket_hairdown grin behind maxime:
                ease 0.3 xpos stagepos[1]-133
                ease 0.3 xpos stagepos[1]-140
            pause 0.3
            show maxime casual surprised:
                ease 0.3 xpos stagepos[1]+157
                ease 0.3 xpos stagepos[1]+160
            "I take his arm gently, tugging him towards the edge of the water so we can keep strolling."
            show maxime casual embarrassed
            "He makes a show of hesitating, but I can see his smile through the moonlight, and he lets me pull him along."
            show mscmc jacket_hairdown smile
            show maxime casual surprised
            mx "Actually, I did briefly try to salvage the letter."
            show maxime casual embarrassed
            mx "But then I {i}really{/i} had to throw it away before I embarrassed myself beyond all help."
            show mscmc jacket_hairdown grin
            "He wait, clearly goading me, and I happily play along."
            mcmax "Oh {i}really?{/i} And what did you write?"
            "Maxime mutters sheepishly, but he's still grinning, starting to enjoy the joke."
            mx "I may-or-may-not have written something about how beautiful you look in the moonlight."
            "I gasp, but just barely manage to keep myself from reacting, remembering our earlier promise."
            hide maxime
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Maxime's a spy, so we can't get involved.)"
            show mscmc jacket_hairdown_cu smile_cu
            "(We're just good friends! Good friends out of an evening walk!)"
            show mscmc jacket_hairdown smile behind maxime:
                xpos stagepos[1]-140
            show maxime casual embarrassed:
                xpos stagepos[1]+160
            "Maxime chuckles ruefully, rubbing the back of his neck."
            show maxime casual smile
            mx "I think I was going a little nuts on my training course, out on a base away from the city. I made me think about you even more than I usually do."
            show maxime casual basic
            "I'm tempted to ask how often constitutes 'usual', but before I can blurt it out, Maxime turns to me, his gaze soft."
            hide mscmc
            show maxime casual_cu basic_cu at maxime_cu
            "I'm suddenly reminded how much I love his eyes, warm haze, inviting and expressive even when Maxime's being stoic."
            hide maxime
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(And when those eyes are trained on me, and full of admiration...)"
            "I get a pleasurable shiver up and down my spine."
            "(Oh boy, am I smitten...)"
            show mscmc jacket_hairdown grin behind maxime:
                xpos stagepos[1]-140
            show maxime casual embarrassed:
                xpos stagepos[1]+160
            "I bite my lip happily, folding my arms in a sort of half-hug to try and contain my giddiness."
            mcmax "Well, thank you for telling me about the letter. Any time you want to send me a letter I'd be happy to get one."
            show maxime casual smile
            mx "Noted. I'll send you a real nice one, with a red ribbon and everything. But no melodrama."
            mcmax "Oh, please don't worry about it sounding 'melodramatic'. I like a guy who doesn't take himself too seriously."
            show mscmc jacket_hairdown embarrassed
            show maxime casual embarrassed
            "I wink, patting his shoulder again, and then quickly look back at the water, aware that we're both blushing."
            hide mscmc
            hide maxime
        "B. Don't bother.":
            $menuhideborder = False

    "We finally reach the Surf Shack, and I step onto the back porch, turning around for one last look at Maxime."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Don't start wishing we could do more, [genericfn]...It's too tempting.)"
    show mscmc jacket_hairdown grin at left2
    show maxime casual smile at right2
    mcmax "Thanks for the escort."
    "I raise a hand in farewell, and Maxime does the same—also, apparently, looking for something to do with his hands."
    mx "Anytime. I'll see you at the tournament's opening ceremony tomorrow."
    show maxime casual smirk
    mx "It should be {i}very{/i} interesting."

    scene bg msc_event_venue_lightson at bg with clockwise_wipe
    play music mschappytimes
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcmax "Wow, this place is packed!"
    hide mscmc
    "I look around the competition hall, thrilled to see not only my fellow surfers..."
    "But vendors, sports writers, and locals who've come to watch the competition."
    $sidecharone = "Tiny Voice"
    sid1 "Oh my gosh, Maxime Okun is here!"
    "I hear a squeal from within the crowd, and 3 kids manage to squeeze their way past the sea of legs, eagerly waving posters and magazine cutouts."
    $sidecharone = "Small Surf Fan"
    sid1 "Mr. Okun, will you please sign my poster?"
    show mscmc jacket_hairdown smile at left2
    show maxime casual surprised at right2
    "Maxime looks a little surprised at the sudden fanclub, but his face melts into a gentle smile, and he borrows apen from a nearby table."
    show maxime casual smile
    mx "Of course. What's your name, little man?"
    hide maxime
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "I settle back to watch this heart-melting spectacle, breaking off to occsaionally wave to a familiar face."
    hide mscmc
    "Someone taps my shoulder, and I turn, grinning at the sight of someone {i}very{/i} familiar."

    play music mscjavier
    show mscmc jacket_hairdown grin at left2
    show javier casual smile at right2
    mcmax "Javier! There's my favorite surf nemesis!"
    show javier casual surprised
    "Javier places his hand over his heart, pretending to be wounded."
    show javier casual smile
    jv "Don't tell me you've acquired any other nemeses. My ego won't be able to take it."
    show javier casual grin
    jv "I'll have to steal the gold from you this time, just to remind you who's your ultimate, all time, rival numero uno."
    hide javier
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "I roll my eyes, waving Maxime over."
    show mscmc jacket_hairdown grin behind maxime:
        xpos stagepos[1]-60
    show javier casual smile at right4
    show maxime casual basic at left4
    mcmax "Maxime, this is Javier, my surfing nemesis. Javier, this is my trainer, Maxime."
    show javier casual grin
    show mscmc jacket_hairdown smile
    "Javier lights up, recognizing him just like the kids did as a former pro surfer."
    jv "Oh, I know Maxime by reputation."
    jv "Pleasure to meet you—[genericfn] and I have been at each other's throats since she joined the circuit."
    show maxime casual smile
    mx "Hey, it's nice to have a rival to keep you on your toes."
    hide mscmc
    hide javier
    hide maxime

    play music mscsurfcompetition
    "Someone at the podium calls for attention, and we quickly find three seats amid the rustling and excited whispers."
    show wikus casual smile at centre
    "A man in an aloha shirt steps up to the mic, smiling at everyone."
    hide wikus
    show mscmc jacket_hairdown smile behind maxime at left1plus
    show maxime casual basic at right3
    show maxime casual basic:
        ease 0.3 xpos stagepos[1]+155
        ease 0.3 xpos stagepos[1]+160
    "Maxime nudges me gently in the arm."
    show maxime casual sad
    mx "That's my guy."
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(He looks like any other tech entrepreneur...Although that smile doesn't quite reach his eyes.)"
    show mscmc jacket_hairdown_cu smile_cu
    "(Not that that's an unusual vibe for the wealthy around here.)"
    hide mscmc
    show wikus casual smile at centre
    $sidecharone = "Wikus Sapor"
    sid1 "Wow, what a crowd! I must be doing something right."
    "He waits for the obliging chuckles to follow his show of humility."
    ws "Thank you all for being here, this tournament couldn't have happened without you—obviously, you're the most important piece."
    show wikus casual basic
    ws "I prefer to keep the babble short and get down to business, so that's what I'm going to do for you. No long-winded speeches."
    ws "The tournament consists of four events, including the final and semi final."
    ws "If you want to move on to the next round, then you need a top score to avoid getting cut."
    show wikus casual smile
    ws "From where I stand, I see a sea of talent and ambition in front of me. So I'm looking forward to a fierce competition."
    "He raises his strawberry champagne, and the crowd chuckles, graitifed."
    hide wikus
    show mscmc jacket_hairdown smile at left1plus
    show javier casual smile at right2
    "Javier nudges me excitedly."
    jv "Think you're a top talent, [genericln]?"
    show javier casual grin
    "I smirk back, momentarily lost in the excitement of the tournament."
    show mscmc jacket_hairdown grin
    show javier casual smile
    mcmax "Oh, I know I'll be in the finals. Hopefully you'll be able to join me."
    hide mscmc
    hide javier
    "After the opening speech, the crowd gradually disperses to network and enjoy plates of expensive finger food."
    show javier casual smile at centre, out_right
    "Javier drifts off, making friends everywhere he turns."

    play music msctense
    "I follow him with my eyes, and notice Wikus and a young, bronzed surfer who I haven't met deep in conversation, their heads bent together."
    show mscmc jacket_hairdown surprised at left1plus
    show maxime casual basic behind mscmc at right2
    mcmax "I wonder who that is?"
    show mscmc jacket_hairdown basic
    "Maxime whispers out of the corner of his mouth."
    mx "Don't stare. Try to use your peripheral vision."
    show mscmc jacket_hairdown surprised
    mcmax "Right! Sorry."
    hide mscmc
    hide maxime
    "I train my gaze on the nearest vendor, while keeping tabs on Wikus and the young surfer in his bright orange shirt."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(And now I can see Wikus coming towards me, in my super-spy peripheral vision.)"

    play music mscantagonist
    show mscmc jacket_hairdown basic at left2
    show wikus casual smile at right2
    ws "Ms. [genericln]!"
    "He appears in front of us, all smiles, and offers me his hand."
    ws "It's a joy to meet you! I've had the pleasure of watching your rise from afar, but now I get to watch up close. I'm a lucky man."
    show mscmc jacket_hairdown surprised
    "He's caught me completely off-guard with the compliments, and I'm left unsure how to react."

    hide mscmc
    hide wikus
    $menuhideborder = True
    menu maximee02c3:
        "A. Act like everything's cool.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show wikus casual smile at right2
            "I answer Wikus with a brilliant smile, the kind I use on particularly difficult customers at the Surf Shack."
            mcmax "That's so kind of you to say, Mr. Sapor! It's really an honor to be here."
            hide mscmc
        "B. Drop a little warning.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show wikus casual smile at right2
            mcmax "I'm so excited to be here, Mr. Sapor! I've already met lots of interesting people."
            "I smile around the hall."
            hide mscmc
        "C. Tease out some info.":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show wikus casual smile at right2
            mcmax "I should be thanking you, Mr. Sapor. You're doing so much for the surfing community by hosting this tournament."
            mcmax "What gave you this inspiration?"
            "He just smiles."
            hide mscmc

    show wikus casual_cu smile_cu at wikus_cu
    ws "Wikus, please—Mr. Sapor was my father, as they say."
    hide wikus
    show mscmc jacket_hairdown smile behind maxime:
        xpos stagepos[1]-60
    show wikus casual basic at right5
    show maxime casual basic at left4
    "I feel Maxime brush up against me, a solid, reassuring presence."
    "When I glance at him, his expression is placid and mildly interested, even as he studies Wikus."
    show mscmc jacket_hairdown grin
    mcmax "This is Maxime Okun, my trainer."
    "I half expect Wikus to start fawning like the kids, but he barely spares Maxime a nod."

    play music mscdanger
    hide maxime
    hide mscmc
    show wikus casual basic at centre:
        yoffset 30
        block:
            parallel:
                ease 0.4 yoffset -50
            parallel:
                ease 0.4 zoom 1.1
            parallel:
                ease 0.4 xoffset -15
        block:
            parallel:
                ease 0.4 zoom 1.25
            parallel:
                ease 0.4 yoffset 5
            parallel:
                ease 0.4 xoffset -35
    "Instead he leans in towards me, close enough that I can smell his aftershave."

    hide wikus
    show wikus casual_cu basic_cu at wikus_cu
    "His eyes rake over my face and suddenly I feel like something in a Petri dish."
    hide wikus
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Whoa there, buddy!)"
    show mscmc jacket_hairdown surprised at centre:
        zoom 1.25
        xoffset -50
        yoffset -45
        block:
            parallel:
                ease 0.4 zoom 1.17
            parallel:
                ease 0.4 xoffset -35
            parallel:
                ease 0.4 yoffset -80
        block:
            parallel:
                ease 0.4 zoom 1.05
            parallel:
                ease 0.4 xpos stagepos[1]+35
            parallel:
                ease 0.4 yoffset 5
    "I back up instinctively, feeling the weight of his studying stare."

    hide mscmc
    show mscmc jacket_hairdown surprised behind maxime:
        xpos stagepos[1]-60
    show wikus casual smile at right5
    show maxime casual angry at left4
    "There's a loaded silence while Maxime glares at Wikus over my head, but Wikus just smiles."
    show mscmc jacket_hairdown basic
    ws "Well, it's been a pleasure, young lady—I promise I've got big plans for a talent such as yourself."
    ws "Pardon me."
    show mscmc jacket_hairdown surprised
    show maxime casual basic
    show wikus casual smile at out_right
    "He steps neatly away, approaching a group of journalists, and leaves me exchanging raised eyebrows with Maxime."
    hide maxime
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcmax "That was weird."
    hide mscmc
    show maxime casual_cu angry_cu at maxime_cu
    "Maxime lays his hands on my shoulder, grip firm."
    mx "Yeah...it was."
    hide maxime

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    scene bg msc_tbc at bg with fade
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
