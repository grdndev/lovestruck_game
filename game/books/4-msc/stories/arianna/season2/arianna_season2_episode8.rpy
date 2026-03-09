label arianna_season2_episode8:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_arianna_studio_day at bg
    play music mscmagicartifact

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Oh, hell yes, I am ready to see some mer magic! I wonder if Neptria has some magic abilities like Queenie.)"
    hide mscmc
    show neptria siren smile at centre:
        xoffset 480 yoffset -100 alpha 0.0
        pause 0.1
        parallel:
            pause 0.1
            easein_back 1.0 xoffset 0
        parallel:
            linear 0.9 yoffset 0 alpha 1.0
    pause 1.0
    "As Neptria sets her bag down, she looks around the studio and her gaze settles on me."
    "This is the first time I've seen her in mer form. Her tail is a solid shiny black and not like other mer tails I've seen so far."
    hide neptria
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Are all mermaids just insanely beautiful or something?)"
    show mscmc bikini_hairdown grin at left3
    show neptria siren basic at right3
    mcarianna "Neptria, hey. Nice to see you again."
    show neptria smile
    "Neptria flashes me a quick smirk before going back to rummaging through her bag."
    nt "Sure it is."
    hide mscmc
    hide neptria
    show queenie casual basic at left1
    qn "Arianna and [genericfn], help us clear some space over here, we need to mark the symbols on the floor."
    hide queenie
    "Following Arianna's lead, I start clearing things around the serpent sculpture's body that's been waitign in the back of the studio."
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I'm really going to witness magic, real magic performed by mermaids. I always knew it was real, it had to be.)"
    show arianna siren grin at right1plus behind mscmc
    show mscmc bikini_hairdown embarrassed at left1plus
    ai "It feels like we're inducting you into a super secret club."
    "Arianna winks at me over one of the tables then pushes off it to come be next to me."
    mcarianna grin "That's kind of what's happening, right?"
    show mscmc embarrassed
    ai "Welcome to the mer magic club, my human."
    hide mscmc
    hide arianna
    show queenie casual basic at left1
    "Queenie pulls out colorful shells of different shapes and sizes and begins placing them around."
    hide queenie
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(I've never even seen those types of shells before. Are they magic too?)"
    hide mscmc
    show queenie casual smile at left1
    qn "Now lay out the scales around the body."
    hide queenie
    show mscmc bikini_hairdown smile at left2
    show arianna siren smile at right2
    "Arianna and I start hauling over all the scales we've spent days laboring over. The atmosphere seems to grow serious."
    hide mscmc
    hide arianna
    show neptria siren basic at centre
    "Neptria begins to pour a red powder from a small pouch into intricate designs on the studio floor."
    hide neptria
    show arianna siren basic at right2
    show mscmc bikini_hairdown basic at left1plus
    "I look at Arianna questioningly."
    show mscmc smile
    ai grin "It's a pretty big spell, so there's a lot of setup."
    hide arianna
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Queenie and Neptria are so focused right now. It almost feels holy.)"

    stop music fadeout 0.5
    play music mscneptria fadein 1.0
    show arianna siren smile at left1 behind mscmc
    show mscmc bikini_hairdown smile at left4
    show neptria siren basic at right5
    "Arianna and I finish placing the scales and Neptria flags us over to stand in front of the serpent."
    nt "You will both be part of the casting too."
    show mscmc surprised
    show neptria smile
    "Arianna nods as I'm filled with confusion."
    mcarianna "Me? I don't...have magic powers though."
    show mscmc surprised
    show arianna surprised
    nt angry "You don't? Shit, we built our whole spell around you."
    hide arianna
    hide neptria
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Please tell me she's joking. She knows I'm a human.)"
    show arianna siren basic at left1 behind mscmc
    show mscmc bikini_hairdown surprised at left4
    show neptria siren grin at right5
    "Neptria slaps her forehead as she shakes her head with a chuckle."
    show mscmc embarrassed
    show neptria smile
    ai grin "Knock it off, Neptria."
    show mscmc smile
    "Arianna puts a hand on my shoulder."
    show arianna smile
    nt basic "We just need you and Arianna to lend your energy to the spell."
    nt "You two made these pieces, so you need to focus on the purpose of the magic."
    hide arianna
    hide mscmc
    hide neptria

    $ menuhideborder = True
    menu ariannas2e8c1:
        "A. That doesn't sound too difficult.":
            $ menuhideborder = False
            show arianna siren smile at left1
            show mscmc bikini_hairdown grin at left4
            show neptria siren basic at right5
            mcarianna "Just focus on the piece?"
            show neptria smile
            mcarianna "That doesn't sound too difficult."
            show mscmc smile
            nt basic "It's as easy as you make it."

        "B. Like I'm a battery?":
            $ menuhideborder = False
            show arianna siren smile at left1
            show mscmc bikini_hairdown grin at left4
            show neptria siren smile at right5
            mcarianna "Oh, so Arianna and I are like batteries?"
            nt basic "Pretty much."
            hide arianna
            hide neptria
            show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
            "(I've never been used as a battery before.)"

        "C. Do spells always need extra people?":
            $ menuhideborder = False
            show arianna siren smile at left1
            show mscmc bikini_hairdown smile at left4
            show neptria siren basic at right5
            mcarianna "Do you always need to use other people as energy for spells?"
            nt smile "Depends on the spell. This one needs it though."

    hide neptria
    hide mscmc
    show arianna bikini_cu grin_cu at arianna_cu
    "Arianna takes my hand and grins."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show arianna embarrassed_cu
    ai "All we have to do is hold hands while they cast and think about what we want this to achieve."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Hold hands with Arianna during the casting of a magic spell? I can manage that.)"
    hide mscmc
    show queenie casual basic at left1
    qn "Alright, we're ready, let's do this."
    show queenie smile
    show neptria siren basic at right3:
        xoffset 100 alpha 0.0
        parallel:
            easein 0.4 xoffset 0
        parallel:
            linear 0.4 alpha 1.0
    "Queenie ushers Neptria over with a hand and winks at me."
    hide queenie
    hide neptria
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "(Queenie always makes me feel welcome. I'm sure she knows I'm a little nervous.)"
    hide mscmc
    "Queenie and Neptria stand either side of the serpent while Arianna and I face each other in front of it."
    show arianna siren grin at right1plus
    show mscmc bikini_hairdown smile at left1plus
    mcarianna "Just hold hands and think about the purpose of the sculpture. Got it."
    ai "Think about how we're going to empower people."
    show arianna embarrassed:
        easein 0.5 right1
    show mscmc embarrassed:
        pause 0.1
        easein 0.5 left1
    "Arianna's eyes are full of hope as she takes both my hands in hers and we smile as our fingers rest on each other."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(God, she's so amazing and holding her hands always makes me feel so warm inside even at the bottom of the ocean.)"

    hide mscmc
    hide arianna
    stop music fadeout 0.5
    play music mscbigmagic fadein 1.0
    show queenie casual sleep at left1plus
    show neptria siren sleep at right3
    "Neptria and Queenie close their eyes and begin to chant in a language I can't understand."
    show white
    pause 0.1
    hide white with Dissolve(0.3)
    show sparkle_column behind queenie:
        matrixcolor TintMatrix("#9100d9") xoffset 150 zoom 1.2
    show sparkle_column as queenie_magic behind queenie:
        matrixcolor TintMatrix("#f78707") xoffset -150 zoom 1.2
    "Their voices grow louder and a crackle of energy goes through the water."
    "Vibrant pulsating swirls of orange and purple spark up around the scales spread on the floor, illuminating the studio."
    hide sparkle_column
    hide queenie_magic
    hide queenie
    hide neptria
    show mscmc bikini_hairdown_cu surprised_cu at mscmc_cu
    "(Holy shit, this is actual magic, real magic, it's real.)"
    hide mscmc
    show sparkle_column:
        matrixcolor TintMatrix("#9100d9") xoffset 150 zoom 1.2
    show sparkle_column as quenie_magic:
        matrixcolor TintMatrix("#f78707") xoffset -150 zoom 1.2
    "The bright swirls spiral around the room."

    window hide
    scene arianna_07_s2e8 with fade:
        align (0.5, 1.0) zoom 1.3 transform_anchor True yoffset 320
    pause 0.2
    show arianna_07_s2e8:
        linear 5.0 yoffset 1190
    pause 5.5
    "Arianna squeezes my hands and I meet her beautiful grey eyes."
    "(This is something that we're helping to create, we're part of something bigger than just ourselves.)"
    "The orange and purple energy careens around Arianna and I but we hold each other's gaze."
    "Her hair blows back softly like there's a breeze and I see the colors of the magic around us reflected on her face."
    "(She's beautiful. She's everything.)"
    "As the energy circles around our hands, an electrifying tingling travels up my arms."

    scene bg msc_arianna_studio_day at bg
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    with fade
    "(It feels like my veins are full of soda!)"
    hide mscmc
    show sparkle_column:
        matrixcolor TintMatrix("#9100d9") xoffset 150 zoom 1.2
    show sparkle_column as queenie_magic:
        matrixcolor TintMatrix("#f78707") xoffset -150 zoom 1.2
    "The swirling energy returns to the scales that start to float and then attach themselves to the serpent sculpture's body."
    hide sparkle_column with dissolve
    hide queenie_magic with dissolve
    "They glow brighter and brighter until they slowly begin to dim. Then they return to their normal colors and the magic seems to dissipate."

    stop music fadeout 0.5
    play music mscmagicartifact fadein 1.0
    show queenie casual smile at left1
    show neptria siren smile at right2
    "Neptria and Queenie stop chanting and open their eyes."
    qn "Great job, ladies."
    hide queenie
    hide neptria
    show mscmc bikini_hairdown_cu smile_cu at mscmc_cu
    "The sizzle I felt in my veins is gone, but I still feel elated."
    show mscmc grin_cu
    "(That was electrifying. Like I was actually connecting with the magic!)"
    show arianna siren grin at left2 behind mscmc:
        xoffset 15
    show mscmc bikini_hairdown smile at left4:
        xoffset -20
    show queenie casual smile at right2
    show neptria siren basic at right6
    qn "[genericfn], what did you think?"

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    mcarianna grin "Uh, that was really cool!"
    show mscmc embarrassed
    "Arianna squeals and gives my hands a final squeeze before she lets go."
    show arianna smile
    show queenie basic
    nt "The art piece will be installed in the square tonight."
    hide arianna
    hide queenie
    hide neptria
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(I can't believe it's actually time for this to go public and help people. It felt so far away before.)"
    hide mscmc
    show neptria siren basic at centre
    "Neptria starts picking up her things and putting them back into the bag she brought."
    hide neptria
    show arianna siren grin at right2
    show mscmc bikini_hairdown smile at left1plus
    ai "There's gonna be media coverage!"
    show arianna embarrassed:
        easein 0.4 right1plus
    show mscmc:
        pause 0.1
        easein_back 0.4 left1
    "Arianna turns to me and pulls me close."
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu
    ai "We can come here and watch it on the news tomorrow!"
    hide arianna
    show queenie casual smile at left1
    qn "We should have a little party! I'll let Casper know."
    hide queenie

    $ wavy_transition("bg msc_arianna_studio_day", "bg msc_tide_pools_sunset")
    scene bg msc_tide_pools_sunset at bg with dissolve
    "The group of us swim up to the tide pools as the sun starts setting."
    show arianna bikini_cu grin_cu at arianna_cu
    ai "Ahhh, we did it!"
    show mscmc bikini_hairdown embarrassed at left1plus
    show arianna bikini grin at right2:
        yoffset 130
        pause 0.1
        easein_back 0.4 yoffset 0
    pause 0.4
    "Arianna pulls herself onto the edge of the tide pool, with legs now, and kicks her feet in the water."
    hide arianna
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(Never thought I'd be hanging out with a gang of mermaids.)"
    hide mscmc
    show casper casual smile at centre:
        yoffset 520 alpha 0.0
        parallel:
            easein_back 0.5 yoffset 200
        parallel:
            linear 0.4 alpha 1.0
    "Casper's head pops up from the water with a grin."
    cs "So it's done? The sculpture's ready?"
    show mscmc bikini_hairdown grin at left2
    show casper at right3
    mcarianna "All ready!"
    hide casper
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(All of our hard work is gonna pay off.)"
    show mscmc bikini_hairdown smile at left2
    show queenie casual smile at right2:
        yoffset 180
    qn "Everybody, thank you."
    show mscmc grin
    show queenie:
        easein 0.4 right1plus
    "Queenie puts her hand over mine in a light pat."
    qn "This will be a turning point for the resistance and the people."
    hide mscmc
    hide queenie

    $ menuhideborder = True
    menu ariannas2e8c2:
        "A. That was some awesome magic!":
            $ menuhideborder = False
            show mscmc bikini_hairdown grin at left2
            show queenie casual smile at right1plus:
                yoffset 180
            mcarianna "That spell was amazing to watch and be a part of."
            qn "And you did wonderfully."
            hide queenie

        "B. I'm kinda nervous.":
            $ menuhideborder = False
            show mscmc bikini_hairdown grin at left2
            show queenie casual smile at right1plus:
                yoffset 180
            mcarianna "It's gonna be a big deal tomorrow."
            hide queenie
            show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
            "(I've never been a part of something this monumental.)"
            show mscmc bikini_hairdown grin at left2
            show queenie casual smile at right1plus:
                yoffset 180
            mcarianna "I'm a little nervous."
            hide queenie
            show arianna bikini grin at right2
            ai "Me too, but in a good way."

        "C. How do you think it'll go down?":
            $ menuhideborder = False
            show mscmc bikini_hairdown surprised at left2
            show queenie casual basic at right1plus:
                yoffset 180
            mcarianna "How will it go down do you guys think?"
            show queenie smile
            mcarianna grin "The government will be pissed, right?"
            hide queenie
            show mscmc smile
            show neptria siren smile at right3:
                yoffset 100
            nt "They're always pissed."
            hide neptria
            show arianna bikini grin at right2
            ai "If this goes well, it could lead to a lot of other change too."

    hide mscmc
    hide arianna
    show neptria siren smile at centre:
        yoffset 40
    "Neptria then pushes away from the edge of the rocky pools."

    stop music fadeout 0.5
    play music mscneptria fadein 1.0
    nt "Well, this was nice, but I have other things going on. Good work everyone."
    hide neptria
    show mscmc bikini_hairdown_cu grin_cu at mscmc_cu
    "(She's so mysterious and seems to keep to herself. Will I ever get to know more about her?)"
    show mscmc bikini_hairdown smile at left1plus
    show neptria siren basic at right3:
        yoffset 100
    "Neptria waves half-heartedly at Queenie, but then her eyes land on me."
    nt "Thanks for your help with the spell."
    mcarianna grin "No problem. It was kinda fun."
    show mscmc basic
    "Her purple eyes linger on me as I try to think of something else to say."
    hide neptria
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(Is there something else she wants to say?)"
    show mscmc bikini_hairdown surprised at left1plus
    show neptria siren smile at right3:
        yoffset 100
    "Then she shrugs, turns away, and dives under the water."
    play sound splash01
    show neptria:
        parallel:
            easein 0.5 xoffset 200
        parallel:
            easeout_back 0.5 yoffset 400
        parallel:
            linear 0.5 alpha 0.0
    "The tips of her tail rises up once before she's gone."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    hide mscmc
    hide neptria
    show casper casual basic at centre:
        yoffset 140
    cs "I actually need to go too."
    show casper angry:
        easein 0.2 yoffset 150
        easein_back 0.4 yoffset 80
    "Casper also pulls away from the tide pool and straightens up."
    hide casper
    show mscmc bikini_hairdown_cu basic_cu at mscmc_cu
    "(Huh? He looks a little twitchy.)"
    show mscmc bikini_hairdown smile at left2
    show casper casual basic at right3:
        yoffset 90
    mcarianna "You just got here!"
    show mscmc basic
    cs confused "I have something to do."
    hide casper
    show arianna bikini basic at right1 behind mscmc
    "Arianna rests an arm on my shoulder"
    show mscmc smile
    ai "We'll catch you later, Casper."
    hide mscmc
    hide arianna
    show casper casual basic at centre:
        yoffset 86
        pause 0.1
        parallel:
            easein 0.5 xoffset 150
        parallel:
            easeout_back 0.5 yoffset 400
        parallel:
            linear 0.5 alpha 0.0
    play sound splash01
    "Casper leaves with a quick wave."
    hide casper
    show arianna bikini grin at right1
    show mscmc bikini_hairdown basic at left1plus
    ai "And then there were three. So much for our little party."
    show mscmc embarrassed
    "Arianna leans more heavily into me, bringing our bodies closer."
    hide arianna
    show mscmc bikini_hairdown_cu embarrassed_cu at mscmc_cu
    "(Maybe we didn't actually cast the spell, but Arianna and I fueled it with our energy.)"
    "(Like, it was this thing that only the two of us could do together.)"
    show mscmc bikini_hairdown surprised at left4
    show arianna bikini surprised at left1
    show queenie casual smile at right4:
        yoffset 194
    qn "Not three for long—you two should go celebrate by yourselves."
    show mscmc smile
    qn "You don't need an old lady cramping your style."
    ai grin "You're too cool to cramp our style."
    show queenie:
        easein 0.4 right2
    "Queenie takes Arianna's hand briefly and laughs."
    qn "Maybe, but I do have a date to get to. Go enjoy yourselves."

    stop music fadeout 0.5
    play music mscreggae fadein 1.0
    scene bg msc_beach_bar_sunset at bg with clockwise_wipe
    "It's becoming something of our spot, so Arianna and I go to Jerry's to celebrate."
    "When we get there, it's in full swing with a live band and a dance floor set up in the sand out in front of the bar."
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown grin at left1
    ai "What's all this?"
    mcarianna "Reggae night! I forgot it was today. They do it every now and then."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(This is perfect! I wanted to bring Arianna to one of these.)"
    show arianna dress grin at right1plus behind mscmc
    show mscmc jacket_hairdown grin at left1
    "Arianna's face lights up with delight as she takes it all in."
    mcarianna "I love this band!!"
    show arianna surprised
    mcarianna "Do you listen to live music a lot? Or see bands?"
    hide mscmc
    hide arianna
    "Arianna and I sit at the counter, watching people laugh and dance and the musicians do their thing."
    show arianna dress grin at right1plus
    show mscmc jacket_hairdown smile at left1
    ai "I've been to a few underground shows before, but you know..."
    show mscmc sad
    ai sad "Government hates expression and art so, yeah. There's not a lot."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Aw. I guess that makes sense. Music has always been a way for people to come together.)"
    show mscmc grin_cu
    "(But, I'll try to make sure that Arianna has an awesome time tonight.)"
    show arianna dress smile at right1plus behind mscmc
    show mscmc jacket_hairdown embarrassed at left1
    mcarianna "Well then, welcome to a great experience! Let me be your guide."
    show arianna grin
    mcarianna grin "Music and dance is a huge part of Jamaican culture. My parents raised me on it."
    ai "I love dancing, but I'm not the best at it."
    ai "I just kinda go with the flow. Move to the music."
    show mscmc embarrassed
    show arianna:
        around (0.5, 1.0) rotate 0 xoffset -303 yoffset -118
        linear 0.3 rotate 2
        block:
            linear 0.7 rotate -2
            linear 0.7 rotate 2
            repeat
    "Arianna kind of sways in her seat as a mock sneak peek."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(Okay. I {i}have{/i} to see her actually dance.)"
    show arianna dress smile at right1plus behind mscmc
    show mscmc jacket_hairdown grin at left1
    mcarianna "Can I see?"
    show arianna embarrassed
    "Arianna laughs, an embarrassed blush on her face, but she does get up."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Since you asked nicely..."
    show arianna dress smile at centre
    "She waits to get a feel for the music before she starts."
    show arianna grin:
        transform_anchor True rotate 0
        easein 0.6 rotate -2 yoffset -30 xoffset -20
        easein 0.6 rotate 0 yoffset 0 xoffset 0
        repeat
    "It's a lot of her putting her arms up and waving them around as she sways and spins."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(So cute!)"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "I laugh and Arianna obviously enjoys my reaction as she shoots me a beautiful smile."
    ai embarrassed_cu "You're not gonna make me dance alone, are you?"
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    mcarianna "I could never."
    show mscmc jacket_hairdown grin at left2:
        transform_anchor True rotate 0
        pause 0.1
        block:
            easein 0.6 rotate -2 yoffset -30 xoffset -20
            easein 0.6 rotate 0 yoffset 0 xoffset 0
            repeat
    show arianna dress grin at right2:
        transform_anchor True rotate 0
        easein 0.6 rotate -2 yoffset -30 xoffset -20
        easein 0.6 rotate 0 yoffset 0 xoffset 0
        repeat
    "I slide off my stool and mimic Arianna's style of dancing."
    hide arianna
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    ai "Do you know how to dance?"
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcarianna "Kind of, you've just got to move to the beat."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Is there a certain style of Jamaican dance?"
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(If there's a good beat and you've got rhythm, it's easy to let your body move with it.)"
    show mscmc jacket_hairdown embarrassed at left1plus
    show arianna dress grin at right3
    mcarianna "I do know how to whine a little. My cousins taught me, but they're waaaayy better at it than me."
    ai "Whine? What's that?"
    mcarianna grin "Uh, well, it's a lot of moving your hips."
    hide mscmc
    hide arianna
    "I stop my Arianna-style dancing and circle my hips up and down to the beat a little to show Arianna."
    show arianna dress_cu embarrassed_cu at arianna_cu
    ai "Oh, that's kinda hot."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "Her bluntness makes me blush."
    mcarianna grin_cu "Yeah, it's definitely a sensual type of dance."
    mcarianna embarrassed_cu "Couples whine against each other sometimes."
    hide mscmc
    show arianna dress_cu embarrassed_cu at arianna_cu
    "Arianna bites her lip and then a grin breaks out onto her lips."
    ai "Will you...show me?"
    hide arianna

    $ menuhideborder = True
    menu ariannas2e8c3:
        "A. Whine with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Yes, a thousand times yes."
            show mscmc embarrassed_cu
            "(Of course, me showing Arianna means that...)"
            show arianna dress embarrassed at right2 behind mscmc
            show mscmc jacket_hairdown smile at left2
            ai "So, you said couples whine together..."
            mcarianna embarrassed "Both people face forward and one dances against the other."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I'm trying my hardest to sound nonchalant and cool, but my heart is racing."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "So, will you dance on me?"
            "Arianna absentmindedly plays with her hair, her eyes roving down my body."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I want to be pressed up against her.)"
            "I hold my hand out to her and when she takes it I twirl in so that my back is against the front of her body."
            show arianna dress embarrassed at right1plus behind mscmc
            show mscmc jacket_hairdown embarrassed at left1
            mcarianna "I can dance on you if you want."
            show arianna grin
            "Arianna laughs and places her hands on my hips, pulling me against her gently."
            ai embarrassed "Please do."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Don't need to tell me twice.)"
            hide mscmc
            "I soften my knees and lean forward slightly to press further back into her hips as I feel her eyes on my subtly arched back."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(It's a good thing she won't be able to see how red my face is.)"
            hide mscmc
            "I listen to the music and place my hands over Arianna's, holding them against my lower torso."

            "I start to move my hips against her and I hear Arianna suck in a breath."
            stop music fadeout 0.5
            play music mscpassionateromance fadein 1.0
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I should say goodbye to any coherent thoughts right now.)"
            show arianna dress smile at left1 behind mscmc:
                xoffset 42 yoffset -10
            show mscmc jacket_hairdown smile at right1:
                transform_anchor True rotate 0 yoffset 30 xoffset -16
                rotate 2
            mcarianna "You can move your hands over me."
            show mscmc embarrassed
            ai embarrassed "Like this?"
            show mscmc:
                easein 0.3 xoffset -32
            "Arianna's hands wrap further around me and down towards the hem of my pands before slowly moving back up my sides."
            mcarianna "Perfect."
            hide arianna
            hide mscmc
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Usually, we're both a little hesitant and embarrassed, but there's something about live music.)"
            "(Arianna's being really bold. God, it's hot.)"
            hide mscmc
            "I feel the rhythm of the music and Arianna pressing herself back against me, I let myself get into it as we move together."
            show arianna dress_cu embarrassed_cu at arianna_cu:
                transform_anchor True zoom 0.75 xoffset -70 yoffset 40
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                transform_anchor True zoom 0.68 xoffset 100 yoffset 160
            "Arianna's fingers graze the exposed skin of my abdomen and I can feel her soft breaths on the side of my neck."
            mcarianna "What do you think?"
            show mscmc sleep_cu
            "Arianna leans her lips to my ear and her nails dig into my skin around my waist ever so slightly."
            show mscmc embarrassed_cu
            ai "I think you're really good at dancing."
            hide arianna
            hide mscmc
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(And it feels really good to dance with her.)"
            hide mscmc
            "Arianna holds me firmly and I press harder into her."
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's following my every move so well. All I can think about is how her body feels agaisnt mine.)"
            hide mscmc
            "Arianna's hands settle back on my waist as she leans forward to whisper in my ear."
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "I've wanted to touch you like this."
            "Her voice in my ear makes my skin burn and my breath speed up."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Arianna's hands are on me. And I'm pressed against her.)"
            hide mscmc
            "I put my hands over hers and turn to face her, looking up at my tall mermaid."
            show mscmc jacket_hairdown embarrassed at left2
            show arianna dress surprised at right1plus
            mcarianna "Do you want to try dancing on me?"
            show mscmc grin
            ai embarrassed "Yes! But I don't know how good I'll be at it."
            mcarianna "As long as you have fun."
            show mscmc smile:
                easein 0.5 right1plus xoffset 16
            show arianna:
                easein 0.4 centre xoffset -10
            "I step around behind her and Arianna smirks, reaching back to guide my hands to her hips."
            show mscmc embarrassed
            ai "Is this so you can have your hands on me now?"
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(I'll take whatever she wants to give.)"
            show mscmc:
                transform_anchor True zoom 0.69 xoffset 60 yoffset 10
            show arianna dress_cu embarrassed_cu at arianna_cu:
                transform_anchor True zoom 0.8 xoffset -110 yoffset 30
                pause 0.1
                easein 0.4 xoffset -75
            "Arianna takes my hands and brings them around her waist as she leans back into me."
            ai "You can be honest."
            show arianna dress_cu embarrassed_cu at arianna_cu:
                transform_anchor True zoom 0.8 xoffset -75 yoffset 30
                easein 0.4 xoffset -50
            "I pull her back against me so there's no space left between us."
            mcarianna grin_cu "Might be."
            show mscmc embarrassed_cu
            ai "How am I doing?"
            hide arianna
            hide mscmc
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(The fact that I can barely speak shows she's doing pretty good.)"
            hide mscmc
            "Arianna moves against me to the music and I keep hold of her."
            "A thousand tingles zap through my body as she grinds into me."

            stop music fadeout 0.5
            play music mscreggae fadein 1.0
            show arianna dress_cu grin_cu at arianna_cu
            ai "You made this look so effortless and fluid! This is hard!"
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Maybe she's not whining properly, but it still feels mind-numbingly incredible.)"
            mcarianna grin_cu "It's in my blood, what can I say?"
            hide mscmc
            "While she's not on beat, it's still a very good attempt."
            show arianna dress_cu grin_cu at arianna_cu
            ai "Ok, I think I'm doing it."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "Whatever you're doing, I'm loving every second of it. Don't stop."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            "Arianna closes her fingers over mine on her waist and looks over her shoulder at me."
            show arianna grin_cu
            "Her eyes are shimmering and her lips are curled into a perfect smile."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(She's as beautiful as the sunset.)"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Whining is maybe my new favorite thing."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "For someone who wasn't born with legs, you're not too shabby."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "I'll take that as a compliment."

        "B. You can't hang.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Dancing up on Arianna?)"
            show mscmc embarrassed_cu
            "The thought of that alone makes my body burn."
            show arianna dress basic at right2 behind mscmc
            show mscmc jacket_hairdown embarrassed at left1plus
            mcarianna "Uh, maybe another time."
            ai smile "Where's all your confidence now?"
            "Arianna puts a hand on her hip."
            mcarianna "Gone."

    scene bg msc_beach_bar_night_lights at bg
    "Arianna and I sit back down at the bar as night finally falls."
    "Arianna orders the fun drink special of the night called, \"Jerry's Beach Blaster\"."

    stop music fadeout 0.5
    play music mscromance fadein 1.0
    show arianna dress grin at right2
    show mscmc jacket_hairdown smile at left1
    mcarianna "They call it the 'blaster' because it gets you blasted."
    ai "Have you ever had it?"
    show mscmc grin
    show arianna surprised
    "Arianna takes a hesitant sip and then nods in satisfaction."
    mcarianna "Nah, but I heard it's good. Can I try?"
    ai grin "Here."
    "Arianna dips the tip of her finger into the drink."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(What is she...)"
    scene arianna_s2_mini1 at bg with dissolve
    "She reaches towards me and runs her wet finger over my lips."
    "(Oh my god.)"
    "Her finger lingers there as her eyes melt into mine."
    "The rest of the bar fades."
    scene bg msc_beach_bar_night_lights at bg
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    with dissolve
    "(Everything she does gives me butterflies.)"
    hide mscmc
    show arianna dress_cu embarrassed_cu at truecenter:
        anchor (0.5, 0.43)
    "As she pulls her finger away, her eyes rest on my lips."
    show arianna dress_cu smile_cu at truecenter:
        transform_anchor True anchor (0.5, 0.43)
        linear 0.5 zoom 1.08
    "Arianna moves forward and closes the space between us until our noses almost touch."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "My heart pounds and I feel like I can barely breathe."
    show mscmc embarrassed_cu
    "(Please kiss me.)"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
