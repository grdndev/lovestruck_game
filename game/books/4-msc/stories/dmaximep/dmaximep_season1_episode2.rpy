label dmaximep_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_labeach_day at bg
    play music mscaction

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "The next morning, Trina and I slip down to the beach before classes."

    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Normally waking up early and practicing before work makes me feel great.)"
    "(But today I'm still bummed about Maxime.)"

    hide mscmc
    "I follow Trina into the surf, the foam lapping at our legs."
    play sound "audio/sfx/splash03.mp3"

    scene bg msc_ocean_wide_day at bg with dissolve
    "Once the water is up to our ribs, we hop on our boards, paddling out like seals."

    stop sound
    show trina casual smile surfboard at centre
    so "Go ahead, I'm not quite ready."

    hide trina
    "Trina settles on her board, tying her hair back and waving me towards the open water, which is heavy with what feels like ideal waves."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Alright, [genericfn], you've got this. Don't let sour puss Maxime ruin your stride...)"

    hide mscmc
    "It's a mistake--I picture Maxime's face as I pop up onto my feet."

    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    mcmaxime "Gah!"

    hide mscmc
    "The wave clips me and I tip forward, face-planting into the surf."
    "I break the water with a gasp, shaking my wet locs."

    show trina casual basic surfboard at centre
    so "You okay? What happened?"

    hide trina
    "I brace my arms on my board, furious with myself"

    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(What happened? I almost don't want to admit it.)"

    $menuhideborder = True
    hide mscmc
    menu maximee2c1:
        "A. Make excuses.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            mcmaxime "I'm just...ugh, I was just distracted. I'll do better on the next wave."
            hide mscmc
        "B. Get frustrated.":
            $menuhideborder = False
            "I slap the water ineffectually, growling under my breath."
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            mcmaxime "I'm irritating the hell out of myself, is what I'm doing"
            hide mscmc
        "C. Take a breather.":
            $menuhideborder = False
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            mcmaxime "I just need a breather."
            "I haul myself onto my board, laying back and blinking at the sun as I try to gather my thoughts."
            hide mscmc

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Come on [genericfn], this won't do just days before the competition!)"
    "(We are {i}not{/i} letting Maxime's well-chiseled jaw ruin this for us.)"

    hide mscmc
    "Trina drifts towards me, letting the waves carry her."

    show mscmc surfer_hairup sad surfboard at left2
    show trina casual sad surfboard at right2
    so "Come on, what's {i}really{/i} bugging you? You know I can always tell when something's bothering you."
    "I turn my head to look at her as I lay on my board."
    mcmaxime "I asked Maxime to train me for the competition--just to give me a few pointers."

    show mscmc surfer_hairup angry surfboard
    so "But he said no, {i}and{/i} he basically said that competitions are the worst and not worth working for!"
    so "I just don't get where that came from. We were having a perfectly nice conversation at the bar."

    show mscmc surfer_hairup sad surfboard
    "I flick the water despondently, and Trina reaches over to pat my head."
    so "Don't take it personally, [genericfn]. Competitive surfing isn't for everyone."

    show trina casual smile surfboard
    so "Most surfers aren't your brand of workaholic--er, I mean 'go-getter'."

    show mscmc surfer_hairup smile surfboard
    "She winks, grinning, and I roll my eyes, though she's managed to coax a smile from me."

    hide mscmc
    hide trina
    "I finally sigh, pulling myself up to scan the sea for the next big wave."

    show mscmc surfer_hairup surprised surfboard at left2
    show trina casual basic surfboard at right2
    mcmaxime "I'm not mad that he doesn't like competitions--he's entitled to his opinion."

    show mscmc surfer_hairup sad surfboard
    mcmaxime "I'm just so frustrated because he's clearly the best waterman at the pier, so of course I want him as my trainer."

    show mscmc surfer_hairup grin surfboard
    mcmaxime "'Cause I'm a go-getter."

    show mscmc surfer_hairup basic surfboard
    show trina casual smile surfboard
    so "Oh come on, there's other fish in the great blue sea! Don't get so fixated on Maxime that you miss a wave."

    show mscmc surfer_hairup sad surfboard
    show trina casual basic surfboard
    mcmaxime "As if!"

    hide mscmc
    hide trina
    "I scoff, already paddling to catch the next surge as Trina laughs from her board."

    show mscmc surfer_hairup_cu angry_cu at mscmc_cu
    "(Here we go, flawless mount!)"

    hide mscmc
    "I push myself up and leap onto my board just as the wave is arching."
    "This time, my feet find the perfectly balanced position I've been cultivating for years, and my stance is strong and steady."
    "I ride the wave as Trina cheers, then turn around and paddle back to her."

    show mscmc surfer_hairup grin surfboard at left2
    show trina casual basic surfboard at right2
    mcmaxime "How's that for focus?"
    "I beam at her smugly, but Trina continues to sit on her board, her chin resting on her fist."

    show mscmc surfer_hairup basic surfboard
    show trina casual smile surfboard
    so "Actually, I was thinking about it...do you realize that Maxime's exchanged more words with you than anyone else at the pier?"
    so "Even me, and I'm his boss!"
    so "I'll bet he does want to spend more time with you, deep down."

    show mscmc surfer_hairup sad surfboard
    show trina casual basic surfboard
    mcmaxime "But he literally said..."

    show trina casual smile surfboard
    so "Maybe he doesn't want to teach you because he {i}likes{/i} you!"

    hide mscmc
    hide trina
    "Trina gasps in delight, clapping her hands together, while I try to paddle near enough to splash her."

    show mscmc surfer_hairup angry surfboard at left2
    show trina casual smile surfboard at right2
    mcmaxime "Trina, you're being ridiculous!"
    so "Am I? Think about it while I catch this wave."

    hide mscmc
    hide trina
    "She blows a kiss back at me, taking advantage of the roll of the waves to paddle out of reach and leave me with my thoughts."

    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Maxime's into me, so he...Doesn't want to spend time together? That doesn't make any sense!)"
    "(Or does it?)"
    hide mscmc

    scene bg msc_labeach_night at bg with dissolve
    play music mscbeach
    "My head is still spinning once I've finished my classes and eaten dinner, and I find I'm far too buzzed to go straight to bed."

    show mscmc jacket_hairup_cu smile_cu at mscmc_cu
    "(And I've got my own special spot!)"

    hide mscmc
    "I don't know for sure that I'm the only person who's discovered it, but I've never seen anyone else there."
    "I found it by accident while exploring the south end, and now I carefully pick my way over the spray-dampened rocks."
    "When I catch sight of the dark water, I gasp, noticing something swimming in circles."

    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(There is someone here!)"

    show mscmc jacket_hairup_cu smile_cu
    "(Or maybe it's a dolphin?)"

    hide mscmc
    "The shape in the water suddenly breaks the surface, performing an acrobatic leap in the air."

    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    "(It must be a dolphin, with a tail like that! But dolphins don't usually come so close to shore.)"

    hide mscmc
    "I inch nearer, angling myself so the moonlight will give me a better look."

    play sound "audio/sfx/splash03.mp3"
    play music mscmaxime
    scene bg msc_maxime_s1_ei1 at bg with fade:
        yanchor 0.6
        linear 8 yanchor 0.1
    pause
    play sound "audio/sfx/splash03.mp3"
    "Just as I hoped, the swimming shape leaps again, this time illuminated by the moon."
    "({i}Maxime?!{/i})"
    "He throws back his head, sending cascading water droplets that catch the moonlight like jewels."
    "But the tail...{i}his tail{/i} is still there."
    "(Except it can't be. Mermaids aren't real--no matter how much an ocean-loving girl like me wishes they were.)"
    "(It must be one of those fake mermaid tails. But it looks so real, the way it moves!)"

    scene bg msc_labeach_night at bg with fade
    "I slip behind the rocks, trying to sort out in my mind as Maxime hits the water again."

    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Is this real?)"

    play sound "audio/sfx/splash03.mp3"
    hide mscmc
    show maxime shorts basic at centre
    "I hear a splashing at the edge of the water, and peer cautiously around to find Maxime. now wearing swim trunks over his very human legs."

    hide maxime
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(Is the darkness playing tricks on me?)"

    show mscmc jacket_hairup_cu angry_cu
    "(I need to know. I don't care if I'm being silly--if I don't find out the truth, I'll never stop wondering if I saw something magical.)"
    "(And there's only one way to find out.)"

    hide mscmc
    "I hop up before I can think better of it, raising my hand in greeting."

    play music mscsuspense
    show mscmc jacket_hairup grin at centre
    mcmaxime "Hey, Maxime!"

    hide mscmc
    show maxime shorts surprised at centre
    "Maxime jumps, yelping and spinning around to where I'm standing."

    show maxime shorts basic
    "When he finally recognizes me, he just stares, searching my face."
    "I scuff my shoe awkwardly, wondering what he's looking for."

    hide maxime
    show mscmc jacket_hairup sad at centre
    mcmaxime "I'm sorry, I didn't mean to startle you."

    show mscmc jacket_hairup smile
    "I chuckle, trying to set him at ease, but he still seems tense--almost haunted."

    hide mscmc
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "(There's no way I can make this less awkward, so I might as well go all-out.)"
    mcmaxime "Hey, this might come across as a really strange question, but are you a merman?"

    hide mscmc
    show maxime shorts_cu surprised_cu at maxime_cu
    "I wait patiently, as Maxime's eyes widen."
    "He clenches his jaw, finally speaking in a cold, clipped voice."

    hide maxime
    show mscmc jacket_hairup basic at left2
    show maxime shorts angry at right2
    mx "What did you see?"

    show mscmc jacket_hairup surprised
    mcmaxime "Well, since you asked, I saw you with what I thought was a very realistic fish tail."

    show mscmc jacket_hairup sad
    mcmaxime "So it's not an unreasonable question, all considered."
    "Maxime's gaze hardens, and he tightens his fist."
    mx "Who are you working for?"

    show mscmc jacket_hairup surprised
    mcmaxime "Uh...Trina, at the surf shack? Same as you."

    show mscmc jacket_hairup basic
    show maxime shorts surprised
    "His expression shifts to puzzled, and he looks me and down again."
    mx "...You really don't know what I'm talking about, do you? How'd you find this place anyway?"

    show mscmc jacket_hairup surprised
    show maxime shorts basic
    mcmaxime "I could ask you the same thing! I always thought this part of the beach was my little secret."

    hide mscmc
    hide maxime
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Normally, I'd be upset at losing my little zen spot, but the possible existence of mermaids more than makes up for it.)"

    hide mscmc
    show mscmc jacket_hairup surprised at left2
    show maxime shorts sad at right2
    "Maxime considers me for a moment, then sighs, letting his shoulders sag."
    mx "Yes, I'm merfolk. Well, half-human, half-mer."
    mcmaxime "It's real...Mermaids are real..."

    show mscmc jacket_hairup grin
    mcmaxime "Wait, are there other mermaids out there? Or is this your personal superpower?"

    show maxime shorts surprised
    "He blinks, caught off-guard."

    show mscmc jacket_hairup smile
    mx "Superpower...? No, I'm not the only one. We've got our own cities and families, same as humans."

    show maxime shorts sad
    "He glances away, almost embarrassed."

    hide mscmc
    hide maxime

    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    mcmaxime "EEEE!"

    play music mscbeach
    hide mscmc
    "I squeal, dancing on the sand, making Maxime stare at me in disbelief."

    show mscmc jacket_hairup_cu grin_cu at mscmc_cu
    mcmaxime "This is so cool!!"

    hide mscmc
    show mscmc jacket_hairup grin at left2
    show maxime shorts surprised at right2
    mx "Is it?"

    show maxime shorts smile
    "He watches me dubiously, but begins to crack a smile at my excitement despite himself."
    mcmaxime "Oh my god, I have so many questions!"
    "Maxime raises his hands, motioning for calm."
    mx "Let's take it easy. I'll give you five free minutes of questions that I'll answer, how's that sound?"

    hide mscmc
    hide maxime
    $menuhideborder = True
    menu maximee2c2:
        "A. Ask Maxime all the questions on your mind!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
            "(Oh damn!)"
            hide mscmc
            show mscmc jacket_hairup surprised at left2
            show maxime shorts basic at right2
            "I blurt out the first question that pops into my head--the obvious one."
            mcmaxime "How do you turn into a merman? I mean, how can you go from having legs to have a tail and back?"
            show maxime shorts smile
            "Maxime folds his arms, humoring me, but genuinely amused."
            mx "That's actually a complicated question. Most merfolk need magic to walk on land, but since I'm half-human, it comes natural."
            show maxime shorts smirk
            mx "Next question?"
            show mscmc jacket_hairup grin
            "He checks a non-existent watch teasingly, as I scramble for more."
            show maxime shorts basic
            mcmaxime "Uh, okay--tell me more about these mermaids cities that are apparently out in the ocean? How doesn't the Coast Guard know about them?"
            show mscmc jacket_hairup smile
            show maxime shorts smile
            "Maxime chuckles, shaking his head and gesturing out to the water."
            mx "Mer aren't swimming around under all the boats and windsurfers."
            mx "There's a portal you have to go through to get to the cities. It wouldn't show up on any ship's radar. Magic, remember?"
            show mscmc jacket_hairup surprised
            mcmaxime "Whoa..."
            show maxime shorts basic
            "I trail off, needing a moment to process the existence of not only merfolk, but magical portal cities."
            show mscmc jacket_hairup grin
            mcmaxime "Ah, wait a moment, since you're half-merman...Is that why you surf so well?"
            mcmaxime "I mean, you're very talented, but when I saw you on the water, you made it look so easy. Like you didn't have to even think."
            "He strokes his chin, eyeing the moon and mulling it over."
            show mscmc jacket_hairup smile
            show maxime shorts smile
            mx "I suppose I might have a little advantage, since I've grown up in the water."
            mx "And our people have to be attuned with the ocean--it's our home, after all."
            show maxime shorts basic
            "I wait for more, but Maxime just sets his hand on his hip, waiting for my next question."
            hide mscmc
            hide maxime
            show mscmc jacket_hairup_cu grin_cu at mscmc_cu
            "(Not sure what that means, but I've got a more pressing question.)"
            hide mscmc
            show mscmc jacket_hairup grin at left2
            show maxime shorts basic at right2
            mcmaxime "Okay--can I see your tail again?"
            show maxime shorts smile
            "Maxime raises his eyebrows, but I'm practically overflowing with giddiness, and this seems to set him at ease."
            hide mscmc
            hide maxime
            show mscmc jacket_hairup_cu embarrassed_cu at mscmc_cu
            "(I really do just think it's cool, Maxime!)"
            hide mscmc
            show mscmc jacket_hairup smile at left2
            show maxime shorts smile at right2
            mx "Well...sure, but I'd rather show you back in the water. I don't want to be a seal flopping around on land."
            hide mscmc
            hide maxime
            "He laughs, making for the water, and gestures at me to follow."
            show mscmc bikini_hairup smile at centre
            "I toss my shirt off, slipping into the water in my bikini."
            hide mscmc
            play sound "audio/sfx/splash03.mp3"
            "The water ripples away from our shoulders, and Maxime breaks the surface, raising his slick, shining tail from the water."
            stop sound
            show maxime mermaid smile at right2
            show mscmc bikini_hairup grin at left2
            mcmaxime "That is so cool..."
            "I can tell just from the glinting moonlight that it must be very colorful in the light of day, the scales practically shining."
            hide mscmc
            hide maxime
            show mscmc bikini_hairup_cu embarrassed_cu at mscmc_cu
            "(Beautiful, too...Not that I can say that out loud.)"
            "(In fact, I'd better stop staring, but he's got me mesmerized, watching the way his tail coils.)"
            hide mscmc
            "He floats on his back, arching his tail and splashing the water lightly."
            show mscmc bikini_hairup smile at left2
            show maxime mermaid smile at right2 behind mscmc
            mx "Satisfied?"
            hide mscmc
            hide maxime
            show mscmc bikini_hairup_cu sad_cu at mscmc_cu
            "(Actually, I kinda want to touch it, but that would be way too forward.)"
            hide mscmc
            "I suddenly realize how intensely I've been staring, and quickly look away trying to play it cool."
            show mscmc bikini_hairup grin at centre
            mcmaxime "It's pretty neat! Shall we head back to shore?"
            hide mscmc
            show maxime mermaid basic at centre
            show sparkle_spike_effect behind maxime with dissolve
            # add crop transform to above to stick it to maxime's sprite
            show maxime shorts basic at centre with dissolve
            "Maxime lazily drifts back to shore, emerging with a pair of legs a moment later."
            hide sparkle_spike_effect
            hide maxime
            "He shakes his braids free of water as I pull my shirt and jacket back on."
            show mscmc jacket_hairup smile at left2
            show maxime shorts smile at right2
            mx "Any more questions? You've got a little under thirty seconds..."
            show mscmc jacket_hairup grin
            show maxime shorts basic
            mcmaxime "I do have one, actually, if you don't mind."
            show mscmc jacket_hairup smile
            "I turn to him seriously, watching the way the moonlight glints off his wet shoulders."
            mcmaxime "Where'd you come from, Maxime Okun?"
            show mscmc jacket_hairup surprised
            show maxime shorts sad
            "Maxime considers me, his expression obscured by the night."
            show maxime shorts basic
            "Finally, he speaks."
            show mscmc jacket_hairup basic
            show maxime shorts surprised
            mx "Well, I've never settled long in one place--I was always travelling the world for surf competitions."
            mx "Then that all ended, so...I came here. It's nice and quiet."
            show maxime shorts sad
            "He sighs, taking a moment to admire the rocks, the water, and the soft sand."
            hide mscmc
            hide maxime
            show mscmc jacket_hairup_cu sad_cu at mscmc_cu
            "(That just brings up more questions...But it seems like a painful subject for him, like Dawn said.)"
            "(He looks so at-ease and happy here by the water.)"
            show mscmc jacket_hairup grin at left2
            show maxime shorts basic at right2
            "I just smile, reaching out to touch his arm lightly."
            mcmaxime "Thanks for answering my questions. I really do appreciate it, and I think being half-mermaid is cool beyond belief."
            show maxime shorts smile
            "Maxime looks at me in surprise, then breaks out in a light, thankful chuckle."
            hide mscmc
            hide maxime
        "B. Choke on excitement.":
            $menuhideborder = False
            "I have so many questions I barely know where to start, and when I open my mouth it feels like they all bottleneck."
            show mscmc jacket_hairup_cu sad_cu at mscmc_cu
            "(You know...I did just discover a huge world sercret. Maybe I should let Maxime do the talking.)"
            hide mscmc
            show mscmc jacket_hairup sad at left2
            show maxime shorts basic at right2
            "Maxime nods sympathetically at my silence."
            show maxime shorts surprised
            mx "I know, it's a lot to take in."
            hide mscmc
            hide maxime

    show mscmc jacket_hairup basic at left2
    show maxime shorts sad at right2
    "Then he sighs, his smile fading into seriousness."
    mx "I need to get going."
    hide mscmc
    hide maxime
    "There's something final in his words, as he turns back to the pier I feel a prickle at the back of my neck."
    show mscmc jacket_hairup sad at left2
    show maxime shorts sad at right2
    mcmaxime "What do you mean?"
    "He hesitates, seeming reluctant to break away, then turns to me."
    mx "You know my big secret. I need to get back on the road and find a new town where as far as everyone knows, I'm just another beach bum."
    show mscmc jacket_hairup surprised
    mcmaxime "W-wait a minute!"
    show maxime shorts smile
    "The corner of his mouth twitches in a faint smile."
    mx "Look, it's not personal--you seem nice."
    mx "And I'm not really worried about you spilling the bean--no one in town would believe you, honestly."
    hide maxime
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    "(Damn, I guess that's true...)"
    show mscmc jacket_hairup sad at left2
    show maxime shorts angry at right2
    mx "But there's people out there who know what I am, and if they overheard you, I'd be in trouble...and so would you. So I've got to be careful."
    show maxime shorts sad
    show maxime shorts sad at out_right with dissolve
    "He raises his hand in a vague farewell, turning away again."
    hide maxime
    show mscmc jacket_hairup_cu surprised_cu at mscmc_cu
    mcmaxime "Wait, please!"
    hide mscmc

    show maxime shorts surprised:
        xpos stagepos[1]+220
        ease 0.35 xpos stagepos[1]+180

    show mscmc jacket_hairup sad behind maxime:
        xpos stagepos[1]-180
        pause 0.5
        ease 0.35 xpos stagepos[1]-60
        ease 0.35 xpos stagepos[1]-75

    "I run after him, grabbing his arm."
    "Maxime arches an eyebrow down at me."

    show mscmc jacket_hairup surprised
    show maxime shorts basic
    mcmaxime "When I say I won't tell anyone, I mean it--I always keep my promises! I wouldn't even tell Trina, and she's my best friend."

    show mscmc jacket_hairup smile
    mcmaxime "It's your secret. You have a right to it."

    show maxime shorts sad
    "Maxime hesitates, his eyes darting between the lights of the pier and me, but at least he's stopped trying to pull away."

    show mscmc jacket_hairup sad
    mx "I appreciate it, but I've just met you. Being in my posiiton, it's hard to trust people. You understand."

    show mscmc jacket_hairup sad:
        xpos stagepos[1]-75
        ease 0.35 xpos stagepos[1]-110

    "I pull my hand back, embarrassed."

    show mscmc jacket_hairup grin
    mcmaxime "Well, you shouldn't have to leave on account of me."

    show maxime shorts basic
    mcmaxime "I've got an idea! I'll get something out of the deal if you stay, so you it's in my best interest to keep my mouth buttoned."

    show mscmc jacket_hairup smile
    "I motion toward my lips, pretending to throw away an invisible key."

    show maxime shorts smile
    "Maxime crosses his arms, amused despite himself."
    mx "Gee, I wonder what your deal could possibly be..."

    show mscmc jacket_hairup grin
    mcmaxime "You guessed it--you're going to give me pointers for the competition!"
    "I bounce on my heels, then remember myself, trying to sober up."

    show mscmc jacket_hairup sad
    mcmaxime "I-I mean, you can still leave, if you want to...I won't force you to stay at the pier."
    mcmaxime "But I really, really hope you'll consider trusting me and teaching me some of your moves."

    hide maxime
    show mscmc jacket_hairup_cu sad_cu at mscmc_cu
    "I widen my eyes, looking up at him like a hopeful seal pup. Time seems to stand still as I wait for his reply."
    hide mscmc

    $tobecontinued()

    scene msc_tbc at bg with fade
    pause
    $ resets()
