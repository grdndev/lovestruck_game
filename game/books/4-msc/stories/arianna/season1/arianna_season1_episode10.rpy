label arianna_season1_episode10:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mc_bedroom_day at bg
    play music mscsuspense2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "I look down at the shell phone in my hands, Emporia's laugh from a few seconds ago replaying in my head."
    "The silence of my room only amplifies the rush of blood in my ears."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Emporia kidnapped Arianna!)"
    hide mscmc
    "I throw the phone onto my bed and frantically look around my room for some kind of weapon."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I have to help Arianna! Who knows what Emporia is capable of?)"
    show mscmc angry_cu
    "(Why is Emporia doing this?)"
    mcarianna sad_cu "What do I do? What do I do?"
    "(I can't go to anyone about this! Emporia is the exiled mer, Mia, which means this is a mermaid thing.)"
    show mscmc surprised_cu
    "(Wait, there is someone I can call!)"
    "(Maxime works for the mer government and they've been looking for Emporia/Mia!)"
    show mscmc sad_cu
    "(If he finds out Arianna told a human about everything she could get in really big trouble, but...)"
    "(Her life is more important.)"
    hide mscmc
    "I pull out my phone, my hands quaking with adrenaline and fear and everything in between."
    "I click to call Maxime and muster all the courage that I have to tell him about Emporia."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(He's going to realize I know about mermaids.)"
    hide mscmc
    mx "It's Maxime."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Maxime, I have to tell you-!"
    hide mscmc
    mx "I'll call you back when I get a chance."
    play sound "audio/sfx/com beep.mp3"
    "There's a beep."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Voicemail?! Shit!)"
    "(I need to say something. Something not too crazy, but good enough.)"
    mcarianna angry_cu "I know where Mia Diplore is."
    hide mscmc
    "Then I leave him her address and hang up."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Okay. Right. I did it. That's all I can do with Maxime.)"
    show mscmc angry_cu
    "(I can't just wait for him to call back though, I have to save Arianna!)"
    hide mscmc
    "Having some kind of weapon is the move, but I don't exactly own a lot of options."
    "My pocket knife is sitting on my dresser and I slip it into my pocket."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(That's something, but not enough. It's really small--I'm not sure that could really stop anyone.)"
    "There's a few beer bottles on my nightstand from the other night."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I could smash the bottom off one and use that? No, I'm probably more likely to hurt myself with something like that.)"
    hide mscmc
    "I start rooting through my drawers and bathroom, looking for literally anything."
    "My can of spray deodorant catches my eye."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(This could work.)"
    hide mscmc
    "I snag a lighter and hold it in front of the deodorant nozzle."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Burn Emporia's place down? Well, not with Arianna inside.)"
    show mscmc surprised_cu
    "(Though, it might be enough to scare the hell out of Emporia if I bust in with a flamethrower.)"
    hide mscmc

    stop music fadeout 0.5
    play music mscsuspense fadein 1.0
    so "Helloooooo, I'm coming in! Hope you're decent!"
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Crap, Trina! Now's not a good time!)"
    hide mscmc
    play sound knocking
    show trina casual basic at centre with dissolve
    "There's a quick knock on my door and then Trina steps into my room."
    show mscmc jacket_hairdown surprised at left2
    show trina at right2
    "She looks at the \"flamethrower\" in my hands and I feel like a deer in headlights."
    so sad "What're you doin'...in here?"
    mcarianna "Uh...nothing."
    so "Dude, are you making a flamethrower?"
    hide mscmc
    hide trina

    $menuhideborder = True
    menu ariannas1e10c1:
        "A. Haha. No...":
            $menuhideborder = False
            show mscmc jacket_hairdown grin at left2
            show trina casual sad at right2
            "I clear my throat and try an unconvincing laugh."
            mcarianna "What? No. Why would I...do that?"
            show mscmc basic
            so "Well, it looks like you're making a flamethrower."
        "B. Yes?":
            $menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show trina casual sad at right2
            "I look down at the lighter and shrug."
            mcarianna sad "Um, yes?"
            so "For?"
            mcarianna "Science?"
        "C. It's a social media trend I'm doing.":
            $ menuhideborder = False
            show mscmc jacket_hairdown surprised at left2
            show trina casual basic at right2
            mcarianna "No, I saw a video of people doing this."
            mcarianna "Just seeing how it would work."
            so sad "Alright, well, don't burn the shop, and the place where we live, down."

    show trina basic
    mcarianna sad "Actually, uh, can I borrow your softball bat?"
    hide trina
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Trina keeps her old bat under the counter. Mostly to threaten Hamish with now and again.)"
    show mscmc jacket_hairdown basic at left2
    show trina casual sad at right2
    so "Should I be worried?"
    mcarianna sad "No?"
    "Trina gives me a skeptical frown."
    so "You're freaking me out a little bit."
    hide trina
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I can't tell Trina what's going on, but I don't want her to worry about it.)"
    show mscmc jacket_hairdown surprised at left2
    show trina casual basic at right2
    mcarianna "I'm all good. I, uh, am gonna play some softball later. That's all."
    so smile "Oh, really? Can I join? I should be free later."
    hide trina
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Need an excuse!)"
    show mscmc jacket_hairdown grin at left2
    show trina casual basic at right2
    mcarianna "I'm teaching Arianna to play. Just us two."
    show mscmc basic
    show trina smile
    "Trina smirks and crosses her arms."
    so "Ahh, so it's a date. All this energy makes sense now. I'll go get the bat."
    hide trina
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Thank god.)"
    hide mscmc
    show trina casual smile at centre
    "Trina starts to leave, a hand thrown over her shoulder."
    so "Just don't bash in any skulls tonight, okay? I can't afford to bail you out."

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    scene bg msc_mansion_exterior_day at bg with clockwise_wipe
    "After stuffing everything into a backpack with the bat sticking out so I can grab it if needed, I go to Emporia's."
    "I grip onto the straps of my bag as I cautiously edge around the side of her house."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "My mind is buzzing and I'm hyper aware of my clothes touching my clammy skin."
    show mscmc angry_cu
    "(I still can't believe this is actually happening. I'm all alone and have no idea what I'm doing...but Arianna needs me.)"
    hide mscmc
    "I see an open window on the second floor and I steel myself."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(That's my way in.)"
    hide mscmc
    "Making sure my backpack is secure, I put my foot on the ledge of the first floor window."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Calm down. I can't risk falling.)"
    hide mscmc
    "I hoist myself up and grab onto the ledge above me, waiting for a moment so I can listen."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(I don't hear anything or anyone. Thank goodness for my upper body strength from surfing.)"
    hide mscmc
    "Once I pull myself up to the second window, I peer in."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(No sign of anyone. Thank you surfing for giving me the strength to get up here.)"
    hide mscmc
    "I climb through the window as quiet as possible."

    scene bg msc_mansion_interior_day at bg with dissolve
    "As I scan the room, the realization that I've only ever been in the foyer and living room sinks in."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(I don't know where to look. How am I supposed to find Arianna? This place is huge.)"
    hide mscmc
    "I tiptoe forward, trying each step before I take it to make sure the floor doesn't creak."

    $ menuhideborder = True
    menu ariannas1e10c2:
        "A. Try the door on the right.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(I guess I just need to start looking everywhere.)"
            hide mscmc
            "There's a door on the right that's closed and I press my ear against it."
            "When I hear nothing, I try the handle."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(It's locked.)"
        "B. Take a minute to make sure you're alone.":
            $ menuhideborder = False
            "Though I know I don't have all the time in the world, I stop moving."
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I can't be recklessly walking through this house.)"
            hide mscmc
            "It's hard to hear over my own heavy breathing, but I truly don't hear a single other thing."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(Maybe no one's home?)"
        "C. Check for clues.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Maybe there's a clue somewhere that will tell mw where Arianna is.)"
            hide mscmc
            "As I look around, even checking under the table, nothing seems out of the ordinary."
            show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
            "(This room look exactly the same as it always has.)"

    hide mscmc
    "But then something on the floor catches my eye."
    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    "There's a dark splatter on the ground by the hallway."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Is that...?)"
    hide mscmc
    "I approach the partially dried dark red substance. It's blood."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Oh my god. Oh my god.)"
    hide mscmc
    "I blow out a quiet breath, trying to shut down the overwhelming panic."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Is that Arianna's? Please don't be Arianna's.)"
    "(If it is...Emporia hurt her.)"
    "There's a small trail of small red smudges leading down the hall."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Arianna could be at the end of this.)"
    hide mscmc
    "My panic is suddenly replaced with determination."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(I have to find her. Now.)"
    hide mscmc
    "I follow the trail down to the first floor, around more corners, until there's a door with stairs behind it leading to the basement."
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(Oh god, not the basement.)"
    hide mscmc
    "I pull the bat out of my backpack and descend."

    stop music fadeout 0.5
    play music mscsadtimes fadein 1.0
    scene bg msc_jail_cell at bg
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    with dissolve
    "(Please let Arianna be okay. Please. Please.)"
    hide mscmc
    "My heart pounds so much it's almost hard to breathe."
    show arianna dress sleep at centre with dissolve:
        transform_anchor True zoom 0.75 yoffset 40
    "The basement is dim and as my eyes adjust, I see Arianna tied up in the back of a cell."
    "Her hair's ruffled and her clothes are askew but..."
    hide arianna
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(She's alive and looks mostly okay!)"
    hide mscmc
    show arianna dress_cu surprised_cu at arianna_cu
    "Arianna raises her head with a deep set scowl on her face and then her eyes widen."
    hide arianna

    scene arianna_04_s1e10 with fade:
        align (0.5, 1.0) transform_anchor True zoom 1.3
        pause 0.5
        linear 6.0 yoffset 1280
    pause 6.5
    mcarianna "Oh my god, Arianna."
    "A smile spreads across her face as she locks eyes with me, for a moment, I forget my fear."
    "Joy and relief at the sight of seeing her, and her smile, floods over me."
    ai "You came for me."
    "(No matter what happens, I'm going to get her out.)"
    mcarianna "Of course I did."

    scene bg msc_jail_cell at bg
    show arianna dress_cu surprised_cu at arianna_cu
    with fade
    "Arianna's smile suddenly disappears and that spark of happiness in her eyes becomes worry."
    ai sad_cu "You can't be here."
    "Her voice is low and frantic."
    ai "This could be a trap. She may want to imprison you too!"
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(What?! There's no way in hell I would leave her now.)"
    "(She wants to keep me safe, but I need to keep her safe too.)"
    show mscmc jacket_hairdown angry at left2
    show arianna dress basic behind mscmc at right2
    mcarianna "Well, if it's a trap, I've already fallen for it because I'm {i}not{/i} leaving you."
    mcarianna surprised "I don't think anyone's home right now either."
    hide arianna
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(Emporia shouldn't know I'm here. We have the upper hand.)"
    show mscmc jacket_hairdown basic at left2
    show arianna dress sad behind mscmc at right2
    ai "But-!"
    mcarianna angry "No, 'buts'. I just got you back."
    show mscmc basic
    "She makes a tiny whine of disapproval, but there's a small smile on her face."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    ai "My hero."
    hide arianna
    "Bat in hand, I approach the cell and when I try the bars, I'm shocked to see it's unlocked."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Why would it be open?)"
    "(Maybe Emporia just didn't see any reason to lock it since Arianna is already tied up. Whatever, it works in our favor.)"
    hide mscmc
    "I enter the cell and kneel beside Arianna, dropping the bat so I can get my knife out to cut the rope tied around her wrists."
    show arianna dress basic at right1plus
    show mscmc jacket_hairdown sad at left1
    mcarianna "Are you okay?"
    ai sad "I'm fine. I just...feel so stupid for not recognizing Mia."
    ai "We were kids the last time I saw her but when she took her mask off I was like, oh shit I see it. Stupid."
    mcarianna "You're not stupid."
    mcarianna "And you never could've expected that she would be up to something like this."
    "When her hands are free, Arianna rubs at her wrists, but she winces when she starts to move."
    show arianna basic
    mcarianna surprised "Did she hurt you? Where? I saw blood and-"
    ai sad "It's just a cut. I got knocked into something sharp by the butler when he dragged me down here."
    hide arianna
    hide mscmc
    "My heart sinks as Arianna points to a cut on the back of her leg."
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(It's actually not that bad, at least compared to what I was imagining while following the trail of blood.)"
    show mscmc jacket_hairdown sad at left1
    show arianna dress surprised behind mscmc at right1plus
    ai "I need to wrap it. I can't leave it like this while we try to get out of here."
    hide arianna
    hide mscmc
    "She rips a piece off the bottom of her dress."
    show arianna dress sad at right1plus
    show mscmc jacket_hairdown basic at left1
    ai "Um...I know you just broke in here and saved me...but I might ask one more thing of you."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "Arianna fidgets with the dress piece, looking somewhat ashamed."
    ai "Looking at blood makes me feel lightheaded."
    ai "Can you wrap my leg for me?"
    hide arianna

    $ menuhideborder = True
    menu ariannas1e10c3:
        "A. Tend to Arianna's wound!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            stop music fadeout 0.5
            play music mscromance fadein 1.0
            show arianna dress smile at right1plus
            show mscmc jacket_hairdown grin at left1
            mcarianna "Of course I'll do it."
            "There's a soft smile of relief on her face as I take the cloth from her."
            show mscmc smile
            ai grin "You're too sweet."
            mcarianna grin "What kind of a hero would I be if I weren't?"
            hide arianna
            hide mscmc
            "I scooch closer to her and rest my hand on the side of her leg, gauging the cut."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            "(Luckily, it doesn't look too deep.)"
            "(We need to get antibiotics on this but for now I just have to wrap it with the cloth from her dress.)"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            ai "Do you think it'll scar?"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "If it does, it'll look pretty badass. Scars are hot."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "So you'll think I'm hot?"
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            "Her teasing makes me chuckle and I look at her."
            mcarianna embarrassed_cu "Yeah."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna smiles warmly and it makes me want to never look away."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I've never been this scared about losing someone before.)"
            mcarianna "I saw your blood upstairs, I thought maybe..."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna puts her hand to my face and the tenderness in her eyes gives me comfort."
            ai grin_cu "I'm okay."
            show arianna smile_cu
            "Her voice is nearly a whisper and she taps her forehead to mine."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcarianna "I was so worried about you."
            "(Emporia has proven to be too much of a wildcard. I still have no idea what she's capable of.)"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna's deep gaze makes me feel rooted to the spot."
            ai basic_cu "[genericfn], everything's alright now."
            show arianna smile_cu
            "She holds me with her eyes and I want to believe her."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Everything {i}will{/i} be alright, but we need to get out of here first.)"
            hide mscmc
            "I look back down at my hands with the wrap, ignoring the way my heart beats."
            show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
            mcarianna "Let me know if I'm hurting you."
            hide mscmc
            "I start to wrap the cloth over her leg, taking great care to make the wrap firm but as gently as I can."
            show arianna dress_cu grin_cu at arianna_cu
            ai "I'm really a damsel in distress. I'll save you in return sometime."
            show arianna sad_cu
            "She laughs to herself, but it turns into a sigh."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(Arianna must be tired, but at least she's trying to keep her spirits up.)"
            mcarianna grin_cu "I don't mind, really. Everyone used to get hurt all the time at my skatepark growing up."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            ai "You really amaze me."
            "There's a dreamy tone to her voice."
            ai grin_cu "You're really kind to me and always so cool about everything."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "(Because I really care about her.)"
            mcarianna sad_cu "I'm not always cool."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "You are to me."
            "I look up at Arianna and she looks like she's memorizing every detail of my face."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "Arianna draws her thumb down my cheek in a caress and a tingle goes through me."
            "(I love the way her hands feel on my skin.)"
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            ai "I never wanted you to be in danger because of me, but I'm really glad you're here."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcarianna "Of course I'm here. How could I have lived with myself if I hadn't come after you?"
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna's hand leaves my cheek as she brushes one of my locs behind my ear."
            hide arianna
            show mscmc jacket_hairdown_cu embarrassed_cu at mscmc_cu
            "I tie off the wrap as a blush burns its way across my cheeks."
            "(Flirt later, [genericfn].)"
            show mscmc jacket_hairdown surprised at left1
            show arianna dress basic behind mscmc at right1plus
            mcarianna "Is that too tight?"
            show arianna smile
            "She shakes her head with a smile and stretches out her leg."
            show mscmc smile
            ai grin "No--thank you."
            show arianna basic
            mcarianna sad "I couldn't stop thinking about you either."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(It felt like my whole world was crashing down around me knowing Emporia had her.)"
            "(I wish none of this had ever happened, but I'm here now.)"
            show mscmc jacket_hairdown sad at left1
            show arianna dress basic behind mscmc at right1plus
            mcarianna "Getting you out of here has been the only thing on my mind. It still is."
            mcarianna "I'll always come after you if you need me."
            show arianna smile
            "Arianna squeezes my hand."
            show mscmc smile
            ai grin "And I'll always come after you."
            hide arianna
            hide mscmc
            "She moves her leg to the side and looks at the wrap."
            show arianna dress_cu grin_cu at arianna_cu
            ai "It looks good."
            hide arianna
            show mscmc jacket_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Can you walk on it?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Oh, yeah. It's not that bad. Honestly."
            ai "Thank you again."

        "B. Let her do it.":
            $ menuhideborder = False
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            "(I don't know how good I'll be at wrapping her leg.)"
            show mscmc jacket_hairdown sad at left1
            show arianna dress sad behind mscmc at right1plus
            "It must take me too long to respond becaues Arianna shakes her head."
            ai smile "It's alright, I should be able to do it."
            show arianna sleep
            "She takes a few breaths like she's hyping herself up."
            ai sad "I totally got this."
            hide mscmc
            show arianna dress_cu sad_cu at arianna_cu
            "She stretches her leg out, her face paling."
            hide arianna
            show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
            mcarianna "Don't think about it."
            show mscmc jacket_hairdown sad at left1
            show arianna dress sad behind mscmc at right1plus
            "Arianna inhales a deep breath through her nose and releases through her mouth."
            "She manages to wrap her leg."

    hide arianna
    stop music fadeout 0.5
    play music mscsuspense2 fadein 1.0
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Here. Take this."
    hide mscmc
    show arianna dress_cu sad_cu at arianna_cu
    "I hand Arianna my pocket knife and she takes it with a frown."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(If we both have a weapon, we'll stand a better chance.)"
    show mscmc angry_cu
    "(There's no way Emporia can take us both.)"
    show mscmc jacket_hairdown basic at left1
    show arianna dress surprised behind mscmc at right1plus
    ai "Your knife?"
    show arianna basic
    mcarianna sad "It'd make me feel better if you had something to defend yourself with."
    ai surprised "It's kind of small."
    mcarianna smile "Well, I don't exactly have a secret weapon stash at home."
    hide arianna
    hide mscmc
    "I help Arianna get to her feet and grab Trina's bat."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(We're ready.)"
    show mscmc jacket_hairdown angry at left1
    show arianna dress basic behind mscmc at right1plus
    mcarianna "Let's get out of here."
    hide arianna
    hide mscmc
    "Arianna takes the lead and I creep up behind her, my hands around the bat."

    scene bg msc_mansion_interior_day at bg with fade
    "When we come upstairs, it's still quiet."
    show mscmc jacket_hairdown_cu smile_cu at mscmc_cu
    "(So far so good.)"
    show mscmc surprised_cu
    "(We might actually get out of here.)"
    hide mscmc
    stop music fadeout 0.5
    play music mscdanger fadein 1.0
    play sound heel_click
    "A jold of fear shoots through me as I hear someone slow-clapping and the click of heels enter the room."
    $ sidecharone = "Emporia..uh, Mia actually?"
    sid1 "Did you two really think you could just leave?"
    show emporia casual smile at centre:
        transform_anchor True zoom 0.9 alpha 0.0
        linear 1.0 zoom 1.0 alpha 1.0
    "Mia emerges from around the corner with a sick smile, no longer wearing her mask."
    hide emporia
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(She's alone, which means her butler is still around here somewhere.)"
    show mscmc surprised_cu
    "(Despite being on her own, Mia doesn't seem to have any weapons.)"
    hide mscmc
    show emporia casual_cu smile_cu at emporia_cu
    $ sidecharone = "Mia"
    sid1 "You walked right into my trap."
    hide emporia
    show mscmc jacket_hairdown surprised at right1plus
    show arianna dress angry at left1
    "Arianna puts an arm out in front of me and tucks me back behind her protectively."

    scene bg msc_msctbc at bg with fade
    $ tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
