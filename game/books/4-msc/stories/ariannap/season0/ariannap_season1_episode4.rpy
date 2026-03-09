label ariannap_season1_episode4:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_ocean_wide_sunset at bg
    play music mscmctheme

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    "It was a restless night, but Arianna and I are up early and back in the water."
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu basic_cu at mscmc_cu
    "(I dragged Arianna out to the ocean before she could tell me about her plan.)"
    show mscmc sad_cu
    "(Even with all this hectic stuff going on, I can't slack off on training.)"
    show surfboard back at left3:
        xoffset -30
    show mscmc surfer_hairup basic at left3:
        yoffset 50
    show arianna siren smile at right3:
        yoffset 90
    "As I paddle back to Arianna, satisfied with my ride, she applauds me."
    show mscmc smile
    "Her wet hair falls over her shoulders and sticks to her chest."
    hide arianna
    show surfboard back_cu at centre:
        xoffset 0
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(Practice is practice but...I might be a little distracted.)"
    show surfboard back at left3:
        xoffset -30
    show mscmc surfer_hairup smile at left3:
        yoffset 50
    show arianna siren embarrassed at right3:
        yoffset 90
    ai "You're actually pretty good at surfing."

    hide surfboard
    hide mscmc
    hide arianna

    $ menuhideborder = True
    menu ariannas0e4c1:
        "A. Compliment Arianna's art.":
            $ menuhideborder = False
            show surfboard back at left3:
                xoffset -30
            show mscmc surfer_hairup grin at left3:
                yoffset 50
            show arianna siren smile at right3:
                yoffset 90
            mcariannaprev "And you're actually pretty good at sculpting."
            hide surfboard
            hide mscmc
            show arianna siren_cu embarrassed_cu at arianna_cu:
                yoffset 0
            "Arianna's face flushes briefly."
            show surfboard back at left3:
                xoffset -30
            show mscmc surfer_hairup grin at left3:
                yoffset 50
            show arianna siren embarrassed at right3:
                yoffset 90
            ai "Oh, thanks."
        "B. Be humble.":
            $ menuhideborder = False
            show surfboard back at left3:
                xoffset -30
            show mscmc surfer_hairup smile at left3:
                yoffset 50
            show arianna siren smile at right3:
                yoffset 90
            mcariannaprev "I'm happy with where I am, but I still have a long way to go."
            show arianna sleep
            "Arianna nods in encouragement."
        "C. Tell her your worked for it.":
            $ menuhideborder = False
            show surfboard back at left3:
                xoffset -30
            show mscmc surfer_hairup smile at left3:
                yoffset 50
            show arianna siren smile at right3:
                yoffset 90
            mcariannaprev "Hard work pays off."
            mcariannaprev "I have to stay dedicated."

    hide arianna
    show surfboard at centre
    show mscmc at centre
    "I pull my arm over my opposite shoulder in a stretch to brush off the compliment, though I'm grateful."
    hide surfboard
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu:
        yoffset 0
    "Arianna's lips part slightly as she watches me stretch."
    hide arianna
    show surfboard back_cu at centre:
        pause 0.2
        easein 0.4 yoffset 5
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu:
        pause 0.2
        easein 0.4 yoffset 5
    "(Was she watching me the whole time?)"
    show surfboard at centre:
        pause 0.1
        easein 0.4 yoffset 0
    show mscmc embarrassed_cu at mscmc_cu:
        pause 0.1
        easein 0.4 yoffset 0
    "(Not like there was much for her to do.)"
    show surfboard back at centre:
        xoffset -20
    show mscmc surfer_hairup basic at centre:
        yoffset 50
    "Heat rushes through my chest and I let my arm fall back down, albeit rather slowly."
    show surfboard back at left3:
        xoffset -30
    show mscmc surfer_hairup basic at left3:
        yoffset 50
    show arianna siren surprised at right3:
        yoffset 90
    ai "I can't believe you work out so early {i}every{/i} day."
    show arianna smile:
        easein 0.4 yoffset 95
    ai "I'm usually still asleep."
    show arianna:
        easein 0.4 yoffset 90
    mcariannaprev smile "I have to start early to catch the waves."
    hide surfboard
    hide mscmc
    show arianna siren_cu smile_cu at arianna_cu:
        yoffset 0 xoffset 0
    "Arianna sweeps her hair behind her while feigning a haughty look."
    show arianna siren smile at centre:
        yoffset 90
    ai "I need my beauty sleep."
    hide arianna

    show surfboard back_cu at centre:
        xoffset 40
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu
    "(Beauty sleep is exactly how I'd describe last night.)"
    "(Speaking of last night, I think it's time we talk about her plan.)"
    show surfboard back at left3:
        xoffset -30
    show mscmc surfer_hairup surprised at left3:
        yoffset 50
    show arianna siren smile at right3:
        yoffset 90
    mcariannaprev "Alright so, what's your grand plan for Hamish?"
    show mscmc basic
    show arianna grin:
        easein 0.4 yoffset 95
    ai "Right. Get ready for this."

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    show arianna angry:
        easein 0.4 yoffset 90
    "Arianna slaps her palms onto my board, her forehead creasing."
    ai smile "First, we get my art fom the bar."
    ai "Next, break into Hamish's office and put it there."
    hide arianna
    show surfboard back_cu at centre:
        xoffset 0
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu:
        yoffset 0
    "(Oh boy. So that's two counts of breaking and entering.)"
    hide surfboard
    hide mscmc
    show arianna siren smile at centre:
        yoffset 90
    ai "We'll make the office really smoky and then hide in the vents."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Where on earth is this plan going?)"
    hide surfboard
    hide mscmc
    show arianna siren smile at centre:
        yoffset 90
    ai "When Hamish comes in, the spooky voice in the vest - that's me - will talk to him."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(This has to be a joke. A spooky voice in the vent, really?)"
    show surfboard back at left3:
        xoffset -30
        pause 0.1
        easein 0.4 yoffset 5
    show mscmc surfer_hairup surprised at left3:
        yoffset 50
        pause 0.1
        easein 0.4 yoffset 55
    show arianna siren grin at right3:
        yoffset 90
    ai "I'll say that I'm an ancient water spirit and that he should never steal from the ocean."
    show surfboard:
        easein 0.4 yoffset 0
    show mscmc:
        easein 0.4 yoffset 50
    ai "Or buy the surf shop."
    hide surfboard
    hide mscmc
    show arianna siren_cu grin_cu at arianna_cu:
        yoffset 0
    "As I look over at Arianna's face, I see pure determination shimmering in her eyes."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(I'm getting the feeling she isn't kidding...)"
    hide surfboard
    hide mscmc
    show arianna siren grin at centre:
        yoffset 90
    ai "And then, we take back the pieces again. End of plan."
    show arianna smile
    "Arianna dusts her hands off with a satisfied nod. She looks at me eagerly."
    show surfboard back at left3:
        xoffset -30
    show mscmc surfer_hairup grin at left3:
        yoffset 50
    show arianna siren angry at right3:
        yoffset 90
    "I laugh a little, which makes Arianna's face set in a flicker of annoyance."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu grin_cu at mscmc_cu:
        yoffset 0
    "(She's so theatrical even in planning.)"
    "(That's something I really like about her.)"
    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show surfboard back at centre
    show mscmc surfer_hairup surprised at centre:
        yoffset 50
    mcariannaprev "Arianna, why don't you just come forward as the artist?"
    mcariannaprev basic "It'd be a lot less complicated."
    hide surfboard
    hide mscmc
    show arianna siren sleep at left1plus:
        yoffset 90
        pause 0.2
        easein 0.6 centre
    "Arianna shifts underneath the water."
    show arianna basic
    "She starts to fidget with on of her waist finss."
    ai "You can just say you don't like the plan."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu basic_cu at mscmc_cu
    "(That's the second time she's deflected the idea of coming forward as the artist.)"
    show mscmc sad_cu
    "(I don't know why it bothers her so much.)"
    hide surfboard
    hide mscmc
    show arianna siren sad at centre:
        yoffset 90
    "Her eyes leave mine as she looks past me and out at the water."
    hide arianna
    show surfboard back_cu at centre
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(No matter the reason, I hate seeing her deflate like this)"
    show surfboard back
    show mscmc surfer_hairup sad at centre:
        yoffset 50
    mcariannaprev "Of course I'll help you get your art back from the bar, but the rest of the plan..."
    mcariannaprev smile "Needs some work."
    hide surfboard
    hide mscmc
    show arianna siren grin at centre:
        yoffset 90
    "Arianna squeals in delight as she looks back to me, her hands clasped under her chin."
    ai "It's gonna be great!"
    hide arianna
    show surfboard back at centre:
        xoffset -20
    show mscmc surfer_hairup smile at centre:
        yoffset 50
    "Her infectious joy makes me smile."
    show surfboard back_cu:
        xoffset 0
    show mscmc surfer_hairup_cu smile_cu at mscmc_cu:
        yoffset 0
    "(It's almost like I want to do anything to keep her happy. It's worth it to see her like this.)"
    show surfboard back:
        xoffset -20
    show mscmc surfer_hairup embarrassed at centre:
        yoffset 50
    "My smile falters and a blush creeps over me."
    show surfboard back_cu:
        xoffset 0
    show mscmc surfer_hairup_cu embarrassed_cu at mscmc_cu:
        yoffset 0
    "(When did I start feeling like this?)"

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    scene bg msc_beach_bar_day at bg with fade
    "The sun is up, but it's still fairly early by the time we creep around back of Jerry's Beach Bar."
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(It'll be awkward if we get caught red-handed, but there's no turning back.)"
    show mscmc smile_cu
    "(We got this.)"
    "(Besides, I know Jerry and I could talk us out of it.)"
    show mscmc jacket_hairdown smile at centre
    mcariannaprev "It's too early for anyone to be here, so we should be good to go."
    hide mscmc
    show arianna dress_cu surprised_cu at arianna_cu
    "Arianna holds a finter to her mouth."
    show arianna dress surprised at centre
    ai "Shush! We're trying to be stealthy."
    hide arianna
    "As she says that, her foot snags on something and she stumbles forward."
    "She catches herself on her hands in an awkward crouch."
    show mscmc jacket_hairdown grin at centre
    mcariannaprev "Very stealthy."
    "I laugh as I put my hand to my chest."
    hide mscmc
    show arianna dress surprised at centre
    ai "Hey, don't laugh!"
    show arianna smile
    "Arianna quirks a smile, unable to hold in her own laughter."
    hide arianna
    "I calm down and point to the back door."
    "It's not too tall, so it's our best bet."
    show mscmc jacket_hairdown surprised at centre
    mcariannaprev "We could try climbing over. It shouldn't be too hard."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Though once we're in, getting the sculpture out is a different story.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress sad at right3
    ai "You're definitely the one better suited for climbing."
    "Arianna pauses, a nail between her teeth as she looks me up and down."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She has the ability to make me feel extremely self-conscious and flattered at the same time.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress sad at right3
    ai "You're more...compact."
    show arianna basic
    mcariannaprev surprised "Hey, not all of us can be supermodel tall."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I'm not {i}that{/i} short.)"
    show mscmc jacket_hairdown smile at left2
    show arianna dress smile at right3
    mcariannaprev "But, you're right about me climbing. Give me a boost."
    hide mscmc
    hide arianna
    "I move over to Arianna and demonstrate how she should lock her hands for me to step in."
    show arianna dress smile at centre
    "Arianna mimics my hands and spreads her legs in a sturdier stance."
    ai basic "Up and over."
    hide arianna
    "I put a steadying hand on Arianna's shoulder."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Compared to her calloused hands, her shoulders are so much softer.)"
    hide mscmc
    "Hoping she can't feel the sweat on my palm, I get ready to step into her hand."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Don't think about how she's eye level with my chest.)"
    hide mscmc
    "A gruff voice singing makes us freeze."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(That's Jerry!)"
    show arianna dress surprised behind mscmc at right1plus:
        xoffset -20
    show mscmc jacket_hairdown surprised at left1plus
    mcariannaprev "That's the owner! Act natural."
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    show arianna basic
    "Arianna moves towards me and I step back against the wall."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Looking up at her like this...her eyelashes are so long.)"
    show mscmc jacket_hairdown surprised at left1plus
    show arianna dress embarrassed behind mscmc at right1plus:
        xoffset -20
        pause 0.2
        easein 0.6 right1 xoffset -25
    "She comes even closer and puts her arm against the wall by my head."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Arianna wouldn't actually make a move right now, would she?)"
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "She leans in, her forehead nearly to mine and my breath hitches."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Everytime I look into her eyes, it's like discovering a new star in the sky.)"
    show arianna dress basic behind mscmc at right1
    show mscmc jacket_hairdown sleep at left1
    "I swallow, having a hard time processing my own thoughts."
    show mscmc basic
    show arianna embarrassed
    "Her eyelids drop and I see her gaze flick down to my lips for just a second."
    hide mscmc
    hide arianna
    jr "Excuse me, girls. Don't mean to interrupt."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Oh my god, he totally thought we were making out!)"
    "(What kind of plan was that, Arianna?!)"
    hide mscmc
    "Jerry swings his keys around his finger as he comes around."
    show mscmc jacket_hairdown smile at centre
    jr "Ah, [genericfn]. Mornin'."
    hide mscmc

    $ menuhideborder = True
    menu ariannas0e4c2:
        "A. Say nothing was going on.":
            $ menuhideborder = False
            show mscmc jacket_hairdown embarrassed at centre
            mcariannaprev "Hey, Jerry. Sorry we were just, uh..."
            show mscmc at left1plus
            show arianna dress basic behind mscmc at right1
            "I glance at Arianna and feel my face heat up."
            "Hanging out."

        "B. Continue acting \"natural\".":
            $ menuhideborder = False
            show mscmc jacket_hairdown smile at centre
            "Still pressed against the wall by Arianna's proximity, I give Jerry a half salute."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Nothing to see here, Jerry.)"
            show mscmc jacket_hairdown smile at centre
            mcariannaprev "Good morning."

        "C. Just nod in embarrassment.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(This is Arianna's idea of acting natural?)"
            show mscmc jacket_hairdown embarrassed at centre
            "I can't even respond to Jerry, feeling far too flustered."

    show mscmc embarrassed at left1plus
    show arianna dress smile behind mscmc at right1:
        pause 0.1
        easein 0.7 right2
    "Arianna steps away as she smiles at Jerry."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(If Jerry had just kept walking, maybe we could've stayed like that.)"
    hide mscmc
    "Jerry laughs as he walks past us to unlock the door."
    jr "Trina at the shop already?"
    show mscmc jacket_hairdown smile at centre
    mcariannaprev "Yeah, probably."
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(And Trina would be laughing herself to death if she saw Arianna and me get caught like this.)"
    hide mscmc
    "Jerry pushes the door open and lets out a wistful sounding sigh."
    jr "You two and that shop mean a lot to this community. So did her daddy, rest his soul."
    jr "It doesn't sit right with us how the shop's gonna disappear."
    show mscmc jacket_hairdown basic at centre
    "Jerry gives me a small pat on the shoulder."
    jr "We're all here for you. We want to help in any way we can."
    show mscmc smile
    "I nod in appreciation and take a breath."

    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(It's good to know everyone else is thinking of the shop too.)"
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    mcariannaprev "Thank you, I'll let Trina know."
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress basic behind mscmc at right2
    "Jerry starts walking into the bar backwards with a smile."
    jr "Now, you two can stay here if you'd like, but the shop opens soon."
    show mscmc surprised
    show arianna grin
    jr "You might not want an audience."
    show mscmc smile
    show arianna basic
    "We leave Jerry at the bar with quick goodbyes and walk out to the beach."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(We couldn't get her sculpture back and I feel terrible.)"
    hide mscmc
    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    show arianna dress angry at centre
    "Arianna is silent, her eyes to the sand and her jaw tight."
    show bg msc_labeach_day at bg with wiperightdissolve
    ai "I don't know what to do."
    show arianna sad
    "Arianna clutches onto her necklace and blows out a defeated breath."
    hide arianna

    $ menuhideborder = True
    menu ariannas0e4c3:
        "A. Tell her not to worry.":
            $ menuhideborder = False
            show mscmc jacket_hairdown sad at centre
            mcariannaprev "It'll be okay. We'll figure something out."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(We've made it this far...not that we're very far.)"
        "B. Solemnly agree.":
            $ menuhideborder = False
            show mscmc jacket_hairdown sleep at centre
            "I match her sigh with my own."
            mcariannaprev sad "Same."
        "C. Try to make her laugh":
            $ menuhideborder = False
            show mscmc jacket_hairdown basic at centre
            mcariannaprev "Good thing Jerry didn't know what we were up to."
            mcariannaprev smile "It would've been awkward if he'd caught us while I was half over the wall."
            "I give a laugh in an attempt to lighten the mood."

    hide mscmc
    show arianna dress sad at centre
    "Arianna gives little response, almost as if she didn't hear me."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(This has to be about more than not getting her art back.)"
    "(Something's really bothering her.)"
    show mscmc jacket_hairdown sad at left1plus
    show arianna dress sad behind mscmc at right2
    mcariannaprev "Hey."
    show mscmc basic
    "I put my hand on Arianna's arm to stop her walking."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I need her to talk to me.)"
    show mscmc jacket_hairdown basic at left1plus
    show arianna dress sad behind mscmc at right2
    mcariannaprev "Let's stop for a second."
    hide mscmc
    hide arianna
    "I sit down on the sand and pull her down next to me."
    show mscmc jacket_hairdown basic at left1plus
    show arianna dress sad behind mscmc at right2
    ai "Okay."
    "Her eyes fall to my hand still lightly on her wrist."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Touching her still feels electrifying, but it's something I'm familiar with now.)"
    show mscmc smile_cu
    "(It's comforting and intoxicating at the same time.)"
    show mscmc jacket_hairdown basic at left1plus
    show arianna dress surprised behind mscmc at right2
    ai "Now what?"
    show arianna basic
    "As I take my hand back, I let my fingers slide across her skin."
    mcariannaprev smile "It's so nice out. Just sit with me for a sec?"
    show arianna sad
    "Arianna nods, a somewhat confused expresson on her face."
    show mscmc sleep
    show arianna basic
    "Taking a breath, I close my eyes."
    hide arianna
    show mscmc jacket_hairdown_cu sleep_cu at mscmc_cu
    "(I wish we could sit here and enjoy the breeze and the sounds for as long as we wanted.)"
    show mscmc jacket_hairdown basic at left1plus
    show arianna dress basic behind mscmc at right2
    "I open my eyes and find Arianna watching me with a clouded gaze I can't distinguish."
    mcariannaprev "Arianna, I want to know what's going on and help you if I can."
    mcariannaprev surprised "You don't have to tell me, but why are you so against coming out as the artist?"
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(That seems to be the root of the problem.)"
    show mscmc sad_cu
    "(She shuts down everytime I mention it.)"
    hide mscmc
    show arianna dress surprised at centre
    "Arianna seems about to speak, but then snaps her mouth shut with a frown."
    ai sad "I use trinkets and items from your world and mine to make my sculptures."
    "She buries her fingers in the sand and raises her hand up, watching the sand fall."
    ai "But in my world, high art is made with treasures like pearls or living coral."
    "Arianna draws a line through the sand."
    ai "No one with influence sees me as a real artist and...sometimes I feel that way too."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(So she doesn't want to say she's the artist because she doesn't feel like she can.)"
    hide mscmc
    show arianna dress sad at centre
    ai "I'm scared of coming forward, okay?"
    show arianna sleep
    "Her hand clenches in the sand and she looks away, her other hand pulling at her hair."
    "Arianna's harsh tone startles me for a moment, but it dissipates quickly."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I know she isn't mad at me. But she shouldn't be mad at herself either.)"
    show mscmc jacket_hairdown sad at left1plus
    show arianna dress basic behind mscmc at right2
    "In hopes that Arianna will look at me, I place a hand on her shoulder."
    "Arianna tenses slightly at my touch, but I feel her shoulder relax as she turns to me."
    mcariannaprev basic "Do you think I'm a real surfer?"
    ai sleep "Yeah."
    mcariannaprev "Me too. I might not be a pro yet, but that doesn't matter."
    mcariannaprev smile "I'm a surfer because I do it all the time. I love doing it and I always try to get better."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Even if I can't nail that barrel yet, it's the fact that I'm trying.)"
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress basic behind mscmc at right2
    mcariannaprev "You're a real artist, Arianna, because that's what you commit your life to."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show arianna grin
    "Arianna smiles, a grateful look in her eyes and my heart thrums in my chest."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(I could melt into a puddle right here and not because of the sun.)"
    show mscmc jacket_hairdown smile at left1plus
    show arianna dress grin behind mscmc at right2
    "Arianna puts her hand over mine, her fingers wrapping around in a squeeze."
    ai "I want to show you something."
    mcariannaprev surprised "Oh, okay...what?"
    "Arianna nods her head towards the ocean with a giggle."
    show mscmc basic
    ai "Something under the sea."

    scene msc_tbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
