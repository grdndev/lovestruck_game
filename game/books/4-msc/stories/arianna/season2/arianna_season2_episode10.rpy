label arianna_season2_episode10:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mc_bedroom_sunset at bg
    play music mscsadtimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "After the sculpture disaster and packing what we could from Arianna's studio, we're back at my place."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(We're hiding out since Casper signed Arianna and Queenie's name on the art piece.)"
    "(Land is hopefully the last place the mer government would be looking for Arianna.)"
    hide mscmc
    show arianna dress sad at left2:
        pause 0.1
        ease 1.2 right2
        pause 0.1
        ease 1.2 left2
        repeat
    pause 1.5
    "Arianna paces up and down my room, her shellphone gripped between her hands."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "I knew we shouldn't have trusted Casper. He felt like bad news and now he put us all in danger!"
    mcarianna sad "I thought he was on our side."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Arianna was hesitant to trust him in the first place and now I wish I'd listented to her.)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairdown sad at left1
    "Arianna rapidly punches in a number on her phone and puts it up to her ear."
    ai "And why won't Grandma Queenie pick up my calls?!"
    ai "She probably doesn't even know she's wanted right now because she doesn't watch TV."
    mcarianna "Don't you think she would've watched the news today to see the art piece?"
    mcarianna "Maybe she just went into hiding too."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I want to stay optimistic for Arianna's sake, but it is worrisome not knowing where Queenie is.)"
    hide mscmc
    show arianna dress sad at centre:
        pause 0.1
        easeout 0.4 xoffset 20
        block:
            ease 0.8 xoffset -20
            ease 0.8 xoffset 20
            repeat
    "Arianna tries the number again as she chews on her thumb nail."
    show arianna dress_cu sad_cu at arianna_cu
    mcarianna "What if her phone's off? She might not even know you've been calling."
    ai "Or she's been taken into custody."
    ai "If she saw the news, she would know that this is a dire situation!"
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I need to calm Arianna down—I don't want her spiraling out wondering about Queenie.)"
    show mscmc jacket_hairdown sad at left1:
        xoffset -40
        pause 0.1
        easein 0.4 xoffset 0
    show arianna dress sad at right1plus behind mscmc:
        xoffset 50
        pause 0.2
        easein 0.4 xoffset 0
    "I stand up from the bed and move in front of Arianna to stop her pacing."
    mcarianna "I know it's scary, but as of right now, we have no way of knowing what happened."
    mcarianna "Queenie might be perfectly fine, okay?"
    ai "I know, but if we don't know where she is..."
    "Arianna tosses her phone onto the bed and puts her hands through her hair, her eyes looking past me."
    ai "If my grandma is gone, that means the resistance is going to look to me now."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(So not only is it about Queenie being missing, but she's worried about leading them.)"
    show arianna dress sad at right1plus behind mscmc
    show mscmc jacket_hairdown sad at left1
    ai "I'm not a good leader! What do I even say to them?"
    ai "What the resistance does right now is going to impact everything!"
    ai "If I fail everyone, then the resistance is done for."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Arianna wouldn't fail everyone. She would make an incredible leader.)"
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "I put my hands on Arianna's shoulders and she meets my eyes."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcarianna "Hey, breathe."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    ai "What if I fail them?"
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    mcarianna "You're not going to fail them."

    stop music fadeout 0.5
    play music mscromanceconfession fadein 1.0
    hide mscmc
    "I guide Arianna to sit down on the bed and she complies with a soft sigh."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Arianna is extraordinarily capable and smart. I know that whatever comes her way, she can handle it.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress sad at right1
    ai "I work so hard every day to seem like I'm strong and can handle things."
    ai "But I would let everyone down if they could see me like this."
    mcarianna "That's not true."
    scene arianna_s2_mini2 at bg with dissolve
    "I gently take Arianna's hand in mine, stroking her knuckles with my thumb like she has so many times with my own."
    "After a moment, I feel a small squeeze in return."
    "I hope the warmth of my hand relaxes her like hers does for me."
    "(Arianna... I won't let go if you won't.)"
    ai "Can I stay here?"
    "Her voice is soft and muffled slightly."
    ai "Just like this...maybe...in your arms?"

    $ menuhideborder = True
    menu ariannas2e10c1:
        "A. Keep Arianna safe in your arms!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            scene bg msc_mc_bedroom_sunset at bg
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(I wish that I could take all of her worries away, but for now, this is all I can do for her.)"
            show mscmc jacket_hairdown grin at centre:
                xoffset -40
            show arianna dress sad at right2
            mcarianna "For however long you need."
            mcarianna "Go ahead—let it out. Everything that's on your mind."
            show mscmc smile
            show arianna:
                easein_back 0.5 right1
            "Arianna squeezes me and sniffles slightly."
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            ai "I don't know what I'll do if my grandma is arrested."
            ai "What if I never get to see her again?"
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I don't want her to think like that...it's breaking my heart to hear her so sad.)"
            show mscmc jacket_hairdown sad at left1:
                xoffset 25
            show arianna dress sad at right1
            ai "Not only do I never get to see her, but I also become the resistance leader."
            ai "Then what?"
            "Arianna raises her head and lets out a sad laugh."
            ai "What if I'm not a good leader? Everyone is in danger right now."
            ai "People need me, but I don't know if I can do this."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
                xoffset 0
            "(She doesn't see what I see in her. What everyone sees in her.)"
            "(No one would turn to her if they didn't think she could handle it.)"
            show mscmc jacket_hairdown sad at left1:
                xoffset 25
            show arianna dress sad at right1:
                transform_anchor True rotate 0
                rotate -5 yoffset 60 xoffset -72
            "I stroke my hand down Arianna's back and she rests her head on my shoulder again."
            ai "If I can't lead or mess up, the government will come down on all of us."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
                xoffset 0
            "(She's so worried about failing her people, but when has she ever?)"
            show mscmc jacket_hairdown sad at left1:
                xoffset 25
            show arianna dress sad at right1:
                transform_anchor True rotate 0
                rotate -5 yoffset 60 xoffset -72
            mcarianna "Why do you think you can't lead?"
            ai "Just look at me. I'm a mess."
            mcarianna "Arianna, Queenie has always trusted you to do this."
            hide mscmc
            hide arianna
            show arianna dress_cu sad_cu at arianna_cu
            "I lean back so that I can see Arianna's face, her eyes shimmering and her lower lip trembling."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcarianna "You've been a huge part of the resistance since the beginning."
            mcarianna grin_cu "You believe in it and fight for it."
            show mscmc embarrassed_cu
            "(Ever since I met Arianna, I have been so amazed by her strength and passion.)"
            show mscmc grin_cu
            "(And I've seen how much this resistance means to her.)"
            show mscmc jacket_hairdown basic at left1:
                xoffset 25
            show arianna dress basic at right1:
                transform_anchor True rotate 0
                rotate -5 yoffset 60 xoffset -72
            mcarianna "The resistance chose you to make the art piece for the square."
            mcarianna grin "You were in charge of making something so insanely monumental!"
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
                xoffset 0
            "(If Casper hadn't ruined it, it would've been really awesome.)"
            show mscmc jacket_hairdown grin at left1:
                xoffset 25
            show arianna dress basic at right1:
                transform_anchor True rotate 0
                rotate -5 yoffset 60 xoffset -72
            mcarianna "Do you think the resistance would've asked you to do that if they didn't trust you?"
            show mscmc smile
            show arianna sad
            "Arianna's eyes fall and she shrugs."
            ai "I guess not..."
            mcarianna grin "{i}Your{/i} studio was the place people would gather."
            mcarianna "Arianna, you've always been a central part of the resistance."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu:
                xoffset 0
            "(Her people believe in her—they always have.)"
            hide mscmc
            show arianna dress_cu basic_cu at arianna_cu
            "I put my hand under Arianna's chin, tilting her head up."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "You're brilliant and have always been able to take on a challenge."
            mcarianna "Sure, I know it's gonna be hard, but I know you can do this."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "A very bashful smile curls her lips."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "(I'll be by her side the whole time. However much she needs me, I'll be there.)"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            ai "Ever since I was little, I would watch my grandma lead."
            ai "She always looked and sounded so confident—like nothing could stop her."
            ai "I wanted to be just like her."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "And you are. It sounds like you just described yourself."
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            "Arianna takes my hand from her chin, threading her fingers through mine."
            ai "You're too kind to me."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Because I know you can do this. Whatever the resistance or government throws at you."
            "(If Queenie were here, she'd be telling Arianna the same thing.)"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            "Arianna looks at me for a long while until she takes a big breath."
            ai "Thinking about my grandma has always given me strength."
            hide arianna
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            mcarianna "What do you think she would do right now?"
            show mscmc jacket_hairdown smile at left1:
                xoffset 25
            show arianna dress basic at right1
            "Arianna lets go of my hand and stands up."
            ai grin "No one lose hope—this is just the beginning for the resistance!"
            ai "It might be tough but we've been through tougher."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu:
                xoffset 0
            "(She's pretending to be Queenie, but this is all Arianna. She {i}can{/i} do this.)"
            show mscmc jacket_hairdown smile at left1:
                xoffset 25
            show arianna dress grin at right2
            "Arianna looks at me and laughs softly."
            ai "I think she'd say something like that."
            mcarianna grin "If you ask me, it looks like you already know what to do."
            ai "You really think so?"
            show arianna:
                easein 0.5 right1
            "Arianna sits next to me again."
            show arianna smile
            mcarianna "No matter what happens, Queenie will be proud of you and so will I."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu:
                xoffset 0
            "(I think Arianna is starting to understand that too.)"
            show mscmc jacket_hairdown grin at left1:
                xoffset 25
            show arianna dress smile at right1
            "Arianna nods to herself and blows out a breath."
            ai grin "Yeah. You're right."

        "B. We shouldn't...":
            $ menuhideborder = False
            scene bg msc_mc_bedroom_sunset at bg
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I hate seeing her so upset, but…we shouldn't do this.)"
            show arianna dress sad at right1 behind mscmc
            show mscmc jacket_hairdown sad at left1
            mcarianna "Let me get you water, okay?"
            mcarianna "I think that and some quiet will help calm you down."
            ai "Okay..."
            show mscmc:
                parallel:
                    linear 0.4 xoffset -100
                parallel:
                    linear 0.4 alpha 0.0
            "Arianna waits for me on the bed as I get her a glass of water."
            show mscmc:
                parallel:
                    linear 0.4 alpha 1.0
                parallel:
                    easein 0.4 xoffset 0
            "We sit there for as long as Arianna needs, neither of us speaking."
    stop music fadeout 0.5
    play music mscarianna fadein 1.0
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Once Arianna seems collected again, she smiles."
    ai grin_cu "Thank you for being here with me and helping me feel better."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    mcarianna "I'm a part of this too and I'll always be here for you."
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    "Arianna takes my hand with both of hers, her thumbs pressing into my skin."
    hide arianna
    "She places a kiss on the back of my hand."
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "(Maybe this isn't how friends act, but...I don't really care.)"
    hide mscmc

    play sound "audio/sfx/bubbles_003_6397.mp3" loop
    "Arianna's shellphone rings on the bed behind us."
    show mscmc jacket_hairdown surprised at left1
    show arianna dress basic at right1plus
    mcarianna "You think it's Queenie?"
    ai sad "I hope so."
    show mscmc basic
    stop sound fadeout 0.5
    "Arianna brings the phone to her ear, her other hand on her necklace."
    ai surprised "Hello?"
    show mscmc sad
    show arianna sad
    "Arianna shakes her head at me."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Not Queenie then.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress sad at right1plus behind mscmc
    ai "I don't know where Queenie is, I've been trying to get a hold of her."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(So it's someone from the resistance. It's time for Arianna to step up.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress sad at right1plus behind mscmc
    "Arianna nods as she listens on the phone and she glances at me."
    show mscmc grin
    "I give her my best 'you can do this' face."
    show mscmc smile
    ai "I know it doesn't look good right now, but we can't lose hope."
    ai "We might not know where Queenie is, but I'm still here."
    "Arianna loosely sits her hand over mine like she needs it for comfort."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(She sounds in control and calm. Like a leader.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress sad at right1plus behind mscmc
    ai "Everyone needs to lay low and go into hiding."
    ai angry "Make sure that everyone is accounted for."
    hide arianna
    show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
    "Pride for Arianna makes my heart swell as I watch the determined look on her face."
    show mscmc grin_cu
    "(She can do this. Everyone already believes in her.)"
    show mscmc jacket_hairdown smile at left1
    show arianna dress sad at right1plus behind mscmc
    ai "When it's time, I'll get back to you about the next steps."
    ai "Be careful."
    show arianna smile
    "Arianna hangs up and gives me a shaky smile."
    mcarianna grin "How do you feel? I think you sounded great."
    ai grin "I feel like...maybe I can actually do this. It's scary, but the resistance needs me."
    hide arianna
    show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
    "(I don't think the resistance could be in better hands.)"
    show mscmc jacket_hairdown grin at left1
    show arianna dress grin at right1plus behind mscmc
    "Arianna gives my hand a final squeeze before standing with a sudden crease between her brows."

    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show mscmc basic
    ai angry "There's still the issue of Casper though."
    hide arianna
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e10c2:
        "A. We can't let him slip out.":
            $ menuhideborder = False
            show arianna dress angry at right1plus
            show mscmc jacket_hairdown basic at left1
            mcarianna "We can't let him slip out of this one."
            ai "Of course he makes such a huge statement with his banner and then runs off."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(The least he can do is take responsibility for what he did.)"

        "B. He needs a reality check.":
            $ menuhideborder = False
            show arianna dress angry at right1plus
            show mscmc jacket_hairdown sad at left1
            mcarianna "He can't do whatever he wants."
            mcarianna "Casper needs a serious reality check after all of this."
            ai "Oh, I'll give him a reality check alright."

        "C. I wanted to belive in him.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I do feel a little hurt at what Casper did.)"
            show arianna dress basic at right1plus behind mscmc
            show mscmc jacket_hairdown sad at left1
            mcarianna "I wanted to believe in him. I thought he was listening to us."
            ai angry "We all wanted to belive in him, but he made his choice."

    show arianna dress angry at right1plus behind mscmc
    show mscmc jacket_hairdown sad at left1
    mcarianna "Why do you think he did it?"
    ai "Does it really matter at this point? We can hear him out, but what's done is done."
    mcarianna "I guess you're right... You think he's hiding somewhere?"
    ai "I'm sure of it."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(He told us it was cowardly to stay anonymous, but now that his name is out there, I don't see him on the frontlines.)"
    show mscmc jacket_hairdown surprised at left1
    show arianna dress basic at right1plus behind mscmc
    mcarianna "Do you know anything about Casper? Like, somewhere that he would go or likes?"
    show arianna angry
    show mscmc sad
    "Arianna purses her lips and leans against my dresser."
    ai "He's an odd guy. I don't know too much about him."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Finding him won't fix anything, but he needs to know how badly he jeopardized us.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress basic at right1plus behind mscmc
    mcarianna "Has he ever said anything about where he lives?"
    mcarianna "Any...hobbies?"
    ai angry "Actually, maybe I do remember him mentioning a place he goes to."
    "Arianna's eyebrows scrunch in thought."
    ai "I think he said something about this cave down the coast once."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Any lead is better than none. The sooner we find him, the better.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress angry at right1plus behind mscmc
    ai "We should go. I don't want to lose him and we need to sort this out."
    show arianna:
        easein_back 0.4 xoffset 40
    show mscmc:
        pause 0.1
        easein_back 0.4 xoffset 40
    "Arianna takes my hand quickly, but then seems to think twice about it."
    ai surprised "Unless...you don't want to go."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(Even if I didn't have a part in the resistance, I still wouldn't let Arianna go alone.)"
    show mscmc jacket_hairdown smile at left1:
        xoffset 40
    show arianna dress basic at right1plus behind mscmc:
        xoffset 40
    mcarianna "I definitely want to go. We're in this together."
    show arianna grin
    "Arianna grins, but she lets go of my hand anyways and grabs my backpack."
    hide mscmc
    hide arianna
    "She tosses my pocketknife into it."
    show mscmc jacket_hairdown smile at left1:
        xoffset 40
    show arianna dress grin at right1plus behind mscmc:
        xoffset 40
    ai "Uh, just in case, y'know?"
    mcarianna grin "Why on earth do we need that?"
    show mscmc smile
    ai "Last time we were dealing with someone unhinged, we both got kidnapped."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu:
        xoffset 0
    "(She's not wrong, but Casper isn't the same as Mia. At least, I don't think so.)"
    show mscmc jacket_hairdown surprised at left1:
        xoffset 40
    show arianna dress basic at right1plus behind mscmc:
        xoffset 40
    mcarianna "Yeah, but it's Casper...do you really think he would physically try to hurt us?"
    show mscmc basic
    ai sad "I don't know, but better safe than sorry."
    hide mscmc
    hide arianna
    "Arianna grabs some old rope from under my bed and throws it into the bag."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I haven't known Casper for long, but I like to hope that he won't try to harm us.)"

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    scene bg msc_labeach_night at bg with fade
    "With a packed bag, Arianna leads me to the rocky coast the cave is at."
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(It feels eerie out here, like we're sneaking into a villain's lair.)"
    "(But I don't want to see Casper as a villain. He just needs some help.)"
    show mscmc casual_hairup smile at left1
    show arianna dress basic at right2
    mcarianna "Okay, let's do this."
    show mscmc basic:
        easein_back 0.5 xoffset 30
    show arianna:
        pause 0.1
        easein_back 0.5 right1plus
    "I move forward, but Arianna stops me by putting a hand on my arm."
    ai sad "You really don't need to come with me if you don't want."
    ai "It's alright if you want to hang back."
    hide arianna
    show mscmc casual_hairup_cu angry_cu at mscmc_cu
    "(That's the second time now she's said I don't have to come. No way that's happening.)"
    hide mscmc

    $ menuhideborder = True
    menu ariannas2e10c3:
        "A. Stop trying to get rid of me.":
            $ menuhideborder = False
            show mscmc casual_hairup sad at left1:
                xoffset 30
            show arianna dress basic at right1plus
            mcarianna "Stop trying to get rid of me, okay?"
            mcarianna grin "You're stuck with me."
            show arianna grin
            "Arianna grins."
            ai "I would never try to get rid of you."

        "B. Do you want me to?":
            $ menuhideborder = False
            show mscmc casual_hairup sad at left1:
                xoffset 30
            show arianna dress sad at right1plus
            mcarianna "Do you want me to hang back?"
            ai "I don't want you to get hurt."
            mcarianna "And I don't want you to get hurt either."

        "C. We're going together.":
            $ menuhideborder = False
            show mscmc casual_hairup angry at left1:
                xoffset 30
            show arianna dress basic at right1plus
            mcarianna "I am not letting you confront him alone."
            mcarianna "We're going together."

    show arianna basic
    mcarianna sad "Casper also betrayed my trust and I'd like to give him a piece of my mind."
    show mscmc basic
    show arianna sad
    "Arianna taps the back of her hand against mine before I feel her fingers lace through my own."
    ai grin "Alright. Together."
    hide mscmc
    hide arianna
    "We traverse over the coast and follow it around until we see an entrance to the cave."

    scene bg msc_siren_coastal_cave at bg with dissolve
    "It's dim and damp as we step inside, but when my eyes adjust, I see a pool in the middle."
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    mcarianna "Casper? You here?"
    show mscmc sad_cu
    "(Definitely not a creepy spot for someone to hangout in.)"
    hide mscmc
    show casper casual basic at centre:
        yoffset 350 alpha 0.0
        pause 0.1
        parallel:
            easein_back 0.5 yoffset 150
        parallel:
            linear 0.5 alpha 1.0
    "As Arianna and I walk in, there's a ripple in the water and then Casper appears."
    cs confused "Why are you here?"
    show casper basic at left3:
        yoffset 180
    show arianna dress angry at right4
    ai "Why do you think? You just screwed the resistance over!"
    show arianna:
        easein 0.4 right3
    "Arianna steps to the edge of the pool and throws her hands up."
    cs confused "Me? When you're in a war, you have to put everything on the line!"
    show bg with hpunch
    "Casper slams his fists down on the cave floor."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(You shouldn't put everything on the line if it means dealing the final blow to your own side.)"
    hide mscmc
    show arianna dress angry at right3
    show casper casual confused at left3:
        yoffset 180
    cs "Holding back means the death of your ideals!"
    ai "You put everyone in danger! This isn't just one fight, Casper."
    show arianna:
        easein 0.4 right1
    "Arianna throws my backpack down as she stands over Casper, her voice stern."
    hide casper
    show arianna dress_cu angry_cu at arianna_cu
    ai "It's one in many and you have to make sure you can fight another day."
    ai "But you ruined that."
    show casper casual basic at left3:
        yoffset 180
    show arianna dress angry at right3
    "Arianna fixes him with a cold glare and he drops his eyes for a moment."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(She's right and he knows it.)"
    hide mscmc
    show casper casual basic at left1plus:
        yoffset 180
    show arianna dress basic at right3
    cs "I...I realized I shouldn't have done that after I saw the sculpture go live."
    cs sleep "That's not how I should've gone about it."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(Okay, at least he's a bit remorseful.)"
    hide mscmc
    show casper casual_cu basic_cu at casper_cu
    "Then there's a fire in his eyes again and he points a finger at Arianna."
    cs confused_cu "But, why do you get to  be angry at me? You should be helping me!"
    cs "I've made a bigger revolutionary impact than you ever will because you're a coward!"
    hide casper
    show arianna dress_cu angry_cu at arianna_cu
    "Arianna clenches her jaw."
    hide arianna
    show mscmc casual_hairup_cu angry_cu at mscmc_cu
    "(The only revolutionary impact he made is completely destroying the revolution!)"
    hide mscmc
    show casper casual confused at left2:
        yoffset 180
    show arianna dress angry at right3
    cs "Your grandma was training you to take over, but you're not willing to take any risks!"
    "Arianna blows a steady breath out through her nose in an obvious attempt to keep it together."
    ai "You have to fix this, Casper. My grandma is in jail because of you."
    ai "Turn yourself in in exchange for her to be released."
    ai "I'm not letting you leave until you agree."
    hide casper
    hide arianna
    show mscmc casual_hairup_cu sad_cu at mscmc_cu
    "(There's no way Casper will turn himself in. Not willingly, at least.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    show casper casual_cu basic_cu at truecenter:
        anchor (0.5, 0.5) xoffset -80 yoffset 50
    "Casper's face contorts into a mix of pure disbelief and rage."
    cs confused_cu "You think you can just boss me around?"
    play sound big_splash
    show casper:
        transform_anchor True anchor (0.5, 0.5) xoffset -80 yoffset 50
        linear 0.4 alpha 0.0 zoom 1.5 blur 10
    "Casper lurches out of the water and his hands clamp around my arms."
    hide casper
    show mscmc casual_hairup_cu surprised_cu at mscmc_cu
    "(Oh shit! No, no, no!)"
    hide mscmc
    play sound splash01
    "I'm pulled off my feet and over the edge into the cold water."
    "My wet clothes feel heavy and suffocating against my skin."
    show arianna dress_cu surprised_cu at arianna_cu
    ai "Casper-!"
    hide arianna
    show casper casual_cu basic_cu at casper_cu:
        transform_anchor True zoom 0.7 xoffset 100 yoffset 70
    show mscmc casual_hairup_cu sad_cu at mscmc_cu:
        transform_anchor True zoom 0.7 xoffset -130 yoffset 160

    play sound unsheathingsmallknife_99372
    "The sharp edge of a blade presses into my throat."
    cs confused_cu "You're letting me leave."

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
