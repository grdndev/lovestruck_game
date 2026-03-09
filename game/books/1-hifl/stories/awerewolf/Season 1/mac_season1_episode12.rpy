##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.

#define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode12:
    $tbc = False

    ##Change these to suit the story
    scene bg main_day_fog at bg
    play music mackenziehunt

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show mac cop angry at centre
    "Every time she’s changed, it’s always been fluid, almost beautiful."

    "But the eclipse must be forcing the transformation, and Mackenzie keeps fighting back."

    "It’s hurting her, and I want to do anything I can to stop the pain."
    show mac cop angry at left1
    show hiflmc casual sad at right4
    mcmac "Mac, take deep breaths, it’s okay."
    show mac cop angry at left4
    "My hand brushes her shoulder, but Mackenzie hisses and recoils."
    show hiflmc casual surprised
    ma "Don’t touch me."

    ma "I can’t control this... you need to—!"
    hide hiflmc
    show mac earscop wolfgrowl at centre
    "Mackenzie’s head tilts back, ears sprouting from her head and fangs snapping into place."

    "She howls loud enough for it to echo down the whole street, the sound ending in a low growl before Damien cackles."
    show mac earscop wolfbasic at left4
    show damien wolf wolfsmirk at right4
    dam "Welcome to the party, ‘Mac’!"

    dam "See, I didn’t need three days. I just needed this."
    hide damien
    hide mac
    show mackenzie_s1_mini12 at bg
    "He points up to the sky, grinning wildly, and all the other werewolves behind him laugh."
    hide mackenzie_s1_mini12
    show damien wolf wolfsmirk at centre
    dam "I remember when old man Rider told me that lunar eclipses cool the blood, lets the wolf sleep."
    show damien wolf wolfbasic
    dam "Oh, but when the sun is out too? Then we ain’t right."
    show damien wolf wolfsmirk
    dam "But I was ready for it. Let the chaos wash right over me."
    show mac earscop wolfgrowl at left4
    show damien wolf wolfsmirk at right4
    "Mackenzie snaps at him, body cooled tight and ready to spring, but Damien doesn’t even look threatened."

    dam "Who’s the alpha now, huh?"

    dam "Just try and pull one over on me when you can’t think straight."
    hide mac
    show hiflmc casual angry at left4
    mcmac "You fucking asshole."

    dam "Oh, I was getting to you."

    dam "This is your chance to run, girl."
    hide hiflmc
    hide damien
    show damien wolf_cu wolfsmirk_cu at damien_cu
    dam "Because when the blood starts spilling, everyone’s going to look like an enemy."
    hide damien
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(He thinks Mackenzie’s is going to attack me too.)"
    show hiflmc casual_cu angry_cu
    "(She wouldn’t.)"
    hide hiflmc
    show hiflmc casual angry at left4
    show damien wolf wolfbasic at right4
    mcmac "Where’s my sister, Damien? You said you’d bring her."
    show damien wolf wolfsmirk
    "He shrugs, then snorts laughing, putting a clawed hand over his mouth."

    dam "Who knows? She slipped the leash!"
    show hiflmc casual surprised
    mcmac "What?! When?"
    show damien wolf wolfbasic
    dam "I don’t know. But I don’t really care either."

    dam "Your sister was just one more piece of meat."
    hide hiflmc
    show mac earscop wolfgrowl at left4
    "Mackenzie lunges forward in a rage-filled blur, but Damien is ready for it."
    show mac earscop wolfsurprised
    show annabelle wolfcasual wolfsurprised at centre
    "He casually shoves one of his goons in front of her, sending them both sprawling to the ground."
    hide damien
    show mac earscop wolfgrowl
    show annabelle wolfcasual wolfangry
    "The other werewolf yelps and starts to fight, trying to get out from under Mackenzie’s weight,"
    show mac earscop wolfgrowl at left2
    show annabelle wolfcasual wolfangry at right4
    "But the second she scampers away, she’s being chased."
    hide annabelle
    hide mac
    show damien wolf wolfsmirk at right4
    show hiflmc casual surprised at left4
    dam "Oops. Distraction."
    hide hiflmc
    hide damien
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(Shit, Mackenzie isn’t focusing on him. Does just going after whatever threat is closest.)"
    hide hiflmc
    show damien wolf wolfsmirk at right5
    show hiflmc casual basic at left2
    show diego casual basic at left4 behind hiflmc
    di "[genericfn], I believe you should take his advice and leave."
    show damien wolf wolfangry
    dam "Back off, leech. Who asked you?"

    mcmac "I’m not going anywhere, Diego."
    hide hiflmc
    hide damien
    hide diego
    show annabelle wolfcasual wolfangry at centre
    "The rest of Damien’s pack move to circle us, a bloodthirsty, cackling chorus."
    stop music fadeout 1.0
    play music hiflmaintheme
    hide annabelle
    show hiflmc casual basic at right2
    show diego casual basic at left2 behind hiflmc

    di "Neither one of us are now."
    show diego casual vampireangry
    show hiflmc casual surprised at right4
    "His eyes glow red, canines jutting into sharp fangs, and I stumble back a step."

    "It’s one thing to hear he’s a vampire, and another to see it."
    hide hiflmc
    di "Come at me, dogs. I am more than ready."
    show diego casual vampiresmirk at left4
    show damien wolf wolfbasic at right4
    "Damien snorts, raising his hand like he’s about to give an order, but the door to the bowling alley bursts open."
    hide diego
    hide damien
    show razi djinn basic at right4
    #fire animation should be placed behind JD and blue smoke behind Razi
    show jd casualwings devilbasic at left4 behind razi
    "For a second, my vision is a blur of blue energy and fire, before I make sense of what I’m seeing."
    hide razi
    show hiflmc casual surprised at right4
    mcmac "JD has wings?!"
    hide jd
    show razi djinn basic at left4
    mcmac "And Razi, you're-!"

    ra "Here to contain things."
    hide razi
    hide hiflmc
    show jd casualwings devilbasic at centre
    jd "You want to fight Mac, wolf boy, that’s your business."
    show jd casualwings devilangry
    jd "But go for the rest of the town and I’ll rain a whole new kind of hell on you."
    hide jd
    show hiflmc casual surprised at centre
    "I don’t know what to do."
    show hiflmc casual surprised at left5
    show mac earscop wolfgrowl at right2
    show annabelle wolfcasual wolfsurprised at right5
    "I’m surrounded by pissed-off supernatural people on every side,"

    "and I can only watch as Mackenzie throws the goon into a car, hard enough the entire hood crumples like paper."
    hide hiflmc
    hide annabelle
    show mac earscop wolfgrowl at left4
    show damien wolf wolfsmirk at right4
    dam "Maaaaac! You’ve got to drop your toy and come fight me."

    dam "Or I’ll just tell my pack to tear you to pieces."
    hide damien
    hide mac
    show hiflmc casual_cu angry_cu at hiflmc_cu
    "(There has to be a way to help her get control back.)"
    hide hiflmc
    show hiflmc casual basic at right4
    show razi djinn basic at centre
    show jd casualwings devilangry at left4 behind razi
    mcmac "Razi, JD. I have to reach her."
    hide jd
    hide razi
    show hiflmc casual sad
    show diego casual vampireangry at left4
    mcmac "Diego, can you …"

    di "Hold them back? Yes."

    di "But only so many at a time."
    show hiflmc casual angry
    mcmac "Then I need a path forward."
    hide diego
    hide hiflmc
    show damien wolf wolfbasic at centre
    dam "To what? To your sheriff?"

    "Damien stalks forward, closing the distance between us in slow, swaggering steps."
    hide damien
    show damien wolf_cu wolfbasic_cu at damien_cu
    dam "Do you think you can save her?"
    show damien wolf_cu wolfsmirk_cu
    dam "That’s touching, really."
    hide damien
    $menuhideborder = True

    menu mace12c1:
        "A. I know I can.":
            $menuhideborder = False
            show hiflmc casual happy at right4
            show damien wolf wolfbasic at left4
            mcmac "I know I can."

            mcmac "You've been trying to scare me this whole time, but it just doesn't stick, Damien."
        "B. You made a bad bet.":
            $menuhideborder = False
            show hiflmc casual happy at right4
            show damien wolf wolfbasic at left4
            mcmac "You made a bad bet."

            mcmac "All this work to put Mac at a disadvantage and you didn’t even think she might have people who care for her."

        "C. You're heartless.":
            $menuhideborder = False
            show hiflmc casual angry at right4
            show damien wolf wolfbasic at left4
            mcmac "You're heartless"
            mcmac "Mac has always used her power to protect people, and all you care about is territory."

    show damien wolf wolfsmirk
    show hiflmc casual basic
    "He smirks, baring every bit of his fangs."

    dam "When Hunt's worn herself out, I'll show her who the real alpha is."

    dam "Maybe if she begs, I’ll give her a bone. Like yours."
    show hiflmc casual angry
    "Anger burns me from head to toe, but I gulp down a hard breath."

    "I have to keep control too, no matter how terrifying this is."
    hide hiflmc
    show damien wolf wolfsmirk at centre
    dam "Everyone! Get rid of [genericfn]’s friends for me."

    dam "I’ll reward anyone who brings me that vampire’s teeth."

    "The park turns their heads in unison towards us, and suddenly surges forward in a snarling mass of tooth and claw."
    hide damien
    show hiflmc casual surprised at centre
    stop music fadeout 1.0
    play music hiflsad
    "I have nowhere to run."
    show jd casualwings devilangry at right4 behind hiflmc
    "JD throws themself in front of me when two wolves try to tackle me to the ground, the sharp scent of brimstone and phosphorus cutting through the air."
    show razi djinn basic at left4
    "Razi comes to help on the defence, but Diego is having to fight half of them by himself."
    hide jd
    hide razi
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(We’re outnumbered three to one!)"
    hide hiflmc
    show damien wolf_cu wolfbasic_cu at damien_cu
    "Damien walks through the storm of the fight towards me, untouched."

    "When he reaches out to cup my jaw, I want to spit at him, but claws press sharp against my skin."
    dam "You should have come with me when you had the chance."
    hide damien
    show hiflmc casual_cu angry_cu at hiflmc_cu
    mcmac "Screw you."
    hide hiflmc
    show damien wolf_cu wolfbasic_cu at damien_cu
    dam "I told you the sheriff would betray you."

    dam "Either she’ll let me kill you, or the second I draw blood, she’ll come running."
    hide damien
    show hiflmc casual_cu sad_cu at hiflmc_cu
    "I swallow hard, fighting the instinctive fear in my body, that little animal voice that keeps screaming ‘predator!’ over and over."
    show hiflmc casual_cu angry_cu
    mcmac "Mackenzie’s not alone. I won’t leave her alone."
    hide hiflmc
    show damien wolf_cu wolfsmirk_cu at damien_cu
    dam "Oh, but she’s a beast like any other now."

    dam "I brought the alpha down low, and I’ll be taking my prize right here."

    dam "But the question is, should I really kill you? Or turn you?"

    "Damien bares his teeth, then licks his lips."

    dam "I think I’d like you to be part of my pack forever."
    show damien wolf_cu wolfangry_cu at damien_cu
    "He lunges for me, jaw snapping."
    hide damien
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(No!)"
    hide hiflmc
    $menuhideborder = True
    menu mace12c2:
        "A. Mackenzie, I need you!" (paidchoice = "paidchoice"):
            $menuhideborder = False
            show hiflmc casual_cu angry_cu at hiflmc_cu
            mcmac "Mackenzie, I need you!"
            hide hiflmc
            show hiflmc casual angry at left4
            show damien wolf wolfbasic at right4
            "I shout right into Damien's face, staggering him, and something pulls tight around my heart."

            "It's like a rope, an anchor, and there's an answer from the other side."
            hide hiflmc
            hide damien
            show hiflmc casual_cu surprised_cu at hiflmc_cu

            "(Please come to me, please—!)"
            hide hiflmc
            show hiflmc casual angry at left4
            show damien wolf wolfbasic at right4
            dam "What did you think that was going to do, huh?"
            show damien wolf wolfsmirk
            dam "She can't hear you right now, human."

            dam "All she hears is the moon telling her to hunt and kill."
            stop music fadeout 1.0
            play music hiflaction
            show hiflmc casual surprised
            ma "Speak for yourself, Damien."
            show hiflmc casual happy
            show damien wolf wolfbasic
            "Her voice has a rumbling edge to it, but it's unmistakably Mackenzie, and hope surges in my chest when Damien jerks around in surprise."
            hide damien
            hide hiflmc
            show mac earscop wolfsmirk at centre
            "Power rolls off Mackenzie in waves, eyes blazing with it."
            show mac earscop wolfsmirk at left4
            show damien wolf wolfangry at right4
            dam "How?!"

            ma "Your old man must have left out a crucial piece of the puzzle for you."

            ma "Every alpha has their own strength, but they also need someone to balance it."

            ma "They need a partner."

            dam "She's human!"
            show mac earscop wolfgrowl

            ma "She's {i}mine{/i}, and you tried to hurt her."
            show mac earscop wolfgrowl at right1
            "That's the only warning Damien gets before Mackenzie is right up in his face, a mere inch away."

            "She growls low, but it's a show of dominance—she's in perfect control, and he only has shreds of it left."

            dam "No, I don't give a damn what breed you are—!"

            dam "I'll rip that alpha hide off you and wear it like a cl…"
            hide mac
            show damien wolf wolfbasic at centre:
                zoom 0.5
            "Mackenzie slams her hands into Damien's chest, shoving him so hard that he goes careening down the street, landing right on top of a parked car."

            "The alarm goes off, metal crunching as he sags against it."
            hide damien
            show mac earscop wolfsmirk at centre
            ma "Try me."
            show mac earscop wolfsmirk at left3
            show hiflmc casual happy at right3
            "I let out a laugh that's equal parts disbelief and awe before Mackenzie turns to me, eyes still ablaze."
            stop music fadeout 1.0
            play music hiflliteromance
            "She smiles, drilling with raw confidence, and my heart does a happy little flip."
            hide mac
            hide hiflmc
            show hiflmc casual_cu happy_cu at hiflmc_cu
            "(It's Mac. It's all her.)"
            hide hiflmc
            show mac earscop wolfsmirk at left3
            show hiflmc casual happy at right3
            mcmac "Hey."

            ma "Hey."

            mcmac "You look good."

            ma "So do you."
            hide hiflmc
            hide mac
            show mac earscop_cu wolfsmirk_cu at mac_cu
            "Mackenzie pulls me into a fierce kiss, and I melt right against her."

            "My tongue briefly skirts her fangs and she lets out a pleased growl, holding my body flush against hers as the kiss deepens."

            "It's such a rush that I'm left dizzy with adrenaline when we break apart, glad Mackenzie's arms are there to steady me."
            show mac droopcop_cu wolfsad_cu
            ma "Did he hurt you?"
            hide mac
            show hiflmc casual_cu happy_cu at hiflmc_cu
            mcmac "No, I'm fine."
            hide hiflmc
            show mac droopcop_cu wolfsad_cu at mac_cu
            ma "...Did I hurt you?"

            "The worry in Mackenzie's voice is so at odds with her imposing posture."

            "But even with that alpha strength coursing through her blood, her heart's right there under the surface."
            hide mac
            show hiflmc casual_cu happy_cu at hiflmc_cu

            mcmac "No, Mac. You saved me."
            hide hiflmc
            show mac droopcop_cu wolfsad_cu at mac_cu
            ma "I should have gotten ahold of myself faster."
            show mac droopcop_cu sleep_cu
            ma "I fought so hard against the change."
            show mac droopcop_cu wolfsad_cu
            ma "I didn't want everyone to see me as a monster."
            hide mac
            show hiflmc casual_cu basic_cu at hiflmc_cu
            mcmac "You're not a monster. You've never been one."
            hide hiflmc
            show mac droopcop_cu wolfsad_cu at mac_cu
            ma "But I know what I look like."

            ma "So I struggled every step of the way until I heard my name..."
            show mac earscop_cu wolfbasic_cu
            ma "Then it was all so clear."

            ma "Everything I am, everything I could be."
            show mac earscop_cu wolfhappy_cu
            ma "And that I had to keep you safe."
            hide mac
            show hiflmc casual_cu happy_cu at hiflmc_cu
            mcmac "You did."
            hide hiflmc
            show mac earscop_cu wolfbasic_cu at mac_cu
            ma "No. My job isn't done yet."
            stop music fadeout 1.0
            play music hiflaction
            hide mac
            show damien wolf wolfbasic at centre:
                zoom 0.5
            "Steel creeks and whines as Damien pries himself out of the skeleton of the destroyed car,"

            "and he chucks the side mirror to the ground with an angry petulant curse."

            "Glass shatter, bouncing until it lands at Mackenzie's feet."
            hide damien
            show mac earscop wolfbasic at left3
            show hiflmc casual basic at right3
            ma "I've still got to take care of him."
            show hiflmc casual happy
            mcmac "He doesn't stand a chance, Mac."
            hide hiflmc
            hide mac
            show damien wolf wolfangry at centre
            dam "You... this is impossible!"
            show mac earscop wolfsmirk at left4
            show damien wolf wolfangry at right4
            ma "Having a little trouble with your words Damien?"

            ma "Must be the moonlight."

            "Damien staggers before managing to stand again, swaying like he's drunk."

            "Each step forward is shaky and pained, but the look in Damien's eyes is wild, frightening."
            hide mac
            hide damien
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(They say there's nothing more dangerous than a cornered animal.)"
            show hiflmc casual_cu sarcastic_cu
            "(I think a losing werewolf might be even worse.)"
            hide hiflmc
            show mac earscop wolfbasic at left3
            show hiflmc casual basic at right3
            mcmac "What do you need from me, Mac?"

            ma "You already brought me back."
            show mac earscop wolfsmirk
            ma "Now just watch while I teach him a lesson."
            hide hiflmc
            show mac earscop wolfhappy at centre
            "She steps away from me and out into the open street, claws and fangs eagerly bared."
            show mac earscop wolfbasic at left4
            show damien wolf wolfangry at right4
            "Damien draws himself up all talk and throws his head back to howl."

            "The rest of the pack answers with their own primal cries, but Mackenzie holds back, tense and ready to fight."

        "B. Try to escape.":
            $menuhideborder = False
            show hiflmc casual surprised at left4
            show damien wolf wolfbasic at right4
            "I jerk back as hard as I can, ignoring the scratch off Damien’s nails against my cheek."

            "His teeth close on empty air, but I lose my balance, falling back onto the ground."
            hide hiflmc
            hide damien
            show damien wolf_cu wolfbasic_cu at damien_cu
            "Scrambling away from him only buys me a few feet of space, which he steals back with a long stride forward."
            show damien wolf_cu wolfsmirk_cu
            dam "Where you going, girl?"

            dam "It’s a beautiful thing, you know."

            dam "You realize how the world really works."
            show damien wolf_cu wolfbasic_cu
            dam "Humans think they run this world, when they’re just here to be herded and fed upon."

            dam "You’ll be free to take whatever you want ...as long as you bow to me."
            hide damien
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(I think I’m going to be sick.)"
            show hiflmc casual_cu surprised_cu
            "I kick out at Damien when he leans down over me, but it’s like ramming my foot into a steel pole."
            hide hiflmc
            show damien wolf_cu wolfsmirk_cu at damien_cu
            "He laughs, briefly feigning a grimace of pain."

            dam "Ow, that might have bruised."
            hide damien
            show hiflmc casual_cu angry_cu at hiflmc_cu
            mcmac "Get away from me!"
            hide hiflmc
            show damien wolf_cu wolfbasic_cu at damien_cu
            dam "I don’t think so."
            show damien wolf_cu wolfsmirk_cu
            dam "You’re mine now."

            "Damien crouches over me with a feral grin, claws and teeth bared, and I close my eyes."
            hide damien
            show bg blackscreen at bg
            "(Maybe it will hurt less if I—!)"
            hide bg blackscreen
            show bg main_day_fog at bg
            stop music fadeout 1.0
            play music hiflaction
            show mac earscop wolfgrowl at left3
            show damien wolf wolfangry at right3
            "A solids bone-cracking this snaps me alert again, and I see Damien flying across the asphalt, a blur of movement tackling him to the ground."

            "Mackenzie rams her head down against his, knocking his skull back against the street."
            show damien wolf wolfsmirk
            dam "Ooh, someone’s protective."

            dam "I get it, you want to put your teeth in her yourself."
            show damien wolf wolfsmirk at right4
            "Mackenzie roars back, throwing a punch, but Damien dodges it."

            "Asphalt splinters under Mackenzie’s fist, leaving a hole inches deep."
            show damien wolf wolfbasic
            dam "That’s enough of that."
            show damien wolf wolfsmirk at right2
            show mac earscop wolfsurprised behind damien
            "Damien drives a new straight up into Mackenzie’s stomach, and she lets out a choked sound of pain."
            show mac earscop wolfsurprised at left4

            "It gives him the chance to throw her off him, laughing as she shakes off the daze."

            dam "Fine on, Sheriff. Scent the air a little."

            dam "Her blood’s right out in the open."
            hide damien
            hide mac
            show mac earscop_cu wolfgrowl_cu at mac_cu
            "I reach up to my cheek, feeling the wet sting there, and Mackenzie’s golden eyes snap to mine."

            "There’s no recognition, only a wounded wolf looking back at me."
            hide mac
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(Shit. Either he’ll attack her when her back is turned or...)"
            hide hiflmc
            show damien wolf wolfsmirk at right4
            show mac earscop wolfgrowl at left4
            dam "Do it! Show her the alpha you really are, Hunt!"
            hide damien
            show mac earscop wolfgrowl at left2

            show hiflmc casual sad at right4
            "Mackenzie takes a step forward and my chest tightens."

            "Something pulls at my heart, hard enough that I’m almost knocked breathless."
            hide mac
            hide hiflmc
            show hiflmc casual_cu sad_cu at hiflmc_cu
            "(I trust her. More than that, I—!)"
            hide hiflmc
            show mac earscop wolfgrowl at left2

            show hiflmc casual sad at right4
            mcmac "Mackenzie..."
            show hiflmc casual happy
            mcmac "Come back to me. I’m not afraid."
            show mac earscop wolfsurprised
            "Mackenzie’s hands clenched into tight fists and relax before she lets out a staggered breath, golden eyes going wide."
            show mac earscop wolfbasic
            "Focus bleeds back into her gaze, sudden and sharp awareness."

            ma "[genericfn]."
            hide mac
            hide hiflmc
            show damien wolf wolfangry at centre
            dam "What the hell?!"

    show mac earscop wolfbasic at left4
    show damien wolf wolfbasic at right4
    ma "I am the alpha of this state."

    ma "No one else can hold claim to it, much less an upstart like you, Damien."

    "Mackenzie doesn’t yell, but she doesn’t have to."
    hide damien
    hide mac
    show annabelle wolfcasual wolfbasic at centre
    "Her voice booms loud and clear over the chaos of the fighting, and when it does, I see the other werewolves go still."
    hide annabelle
    show jd casualwings devilsmirk at centre
    "JD takes the opportunity for what it is, sucker-punching the one standing closest,"
    show razi djinn basic at right4
    show jd casualwings devilsad at left4 behind razi
    "But Razi mutters for them to stop, the glow in his hands starting to fade."
    hide jd
    hide razi
    show damien wolf wolfangry at centre
    dam "What are you all waiting for? Get her!"
    show mac earscop wolfbasic at left4
    show damien wolf wolfbasic at right4
    ma "They won’t. Not anymore."

    "The scattered pack looks back and forth between Mackenzie and Damien,"

    "But the first werewolf that tries to take a step forward gets roughly shoved by another until he backs off."

    ma "You might have bullied your pack into this fight, but they’ll answer to me."

    ma "Every one of them."
    hide damien
    hide mac
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Jesus, they’re not even bonded to her.)"

    "(She’s so strong it doesn’t matter.)"
    hide hiflmc
    show mac earscop wolfbasic at left4
    show damien wolf wolfangry at right4
    dam "No!"
    show mac earscop wolfbasic at left2
    show damien wolf wolfangry at right2
    "Damien charges Mackenzie, making a broad slash at her face, but she ducks it before punching him right in the gut."

    "He claws at her shoulder and the full frenzy of the fight breaks through, blow after  blow exchanged."

    "The difference is, I can see Mackenzie has the advantage."

    "She lets soft hits through, but every one of them she lands on Damien nearly knocks him off his feet."

    $sidecharone = "Werewolf"
    $sidechartwo = "Werewolf #2"
    hide damien
    hide mac
    show annabelle wolfcasual wolfbasic at centre
    sid1 "Ooh, nice one!"

    sid2 "Get him!"
    show annabelle wolfcasual wolfbasic at left4
    show damien wolf wolfangry at right4
    dam "You’re supposed to be on my side, you b—!"
    hide annabelle
    show mac earscop wolfgrowl at left2
    show damien wolf wolfangry at right2
    "Mackenzie drives an elbow up into Damien’s chin and he chokes, teeth tinted with red froth."

    "I’m waiting for her to bring in the final strike when Damien reaches up under his shirt, grabbing for something."

    "It’s the hilt of a knife."
    hide mac
    hide damien
    show hiflmc casual surprised at centre
    "The blade flashes brighter than steel, and I realize what he has."
    hide hiflmc
    $menuhideborder = True
    menu mace12c3:
        "A. Silver!":
            $menuhideborder = False
            show hiflmc casual angry at left4
            show mac earscop wolfsurprised at right4
            mcmac "Mackenzie, he has silver!"

            mcmac "Don’t let him cut you!"

        "B. He's got a knife!":
            $menuhideborder = False
            show hiflmc casual angry at left4
            show mac earscop wolfsurprised at right4
            mcmac "Mackenzie, he has a knife!"

        "C. Mackenzie, move!":
            $menuhideborder = False
            show hiflmc casual_cu sarcastic_cu at hiflmc_cu
            "(Hell, I don't have time to explain.)"
            hide hiflmc
            show hiflmc casual angry at left4
            show mac earscop wolfsurprised at right4
            mcmac "Mackenzie, MOVE!"

    hide hiflmc

    show damien wolf wolfangry at right1
    show mac earscop wolfbasic at right4 behind damien
    "Damien lashes out with the knife, but Mackenzie steps to the side and catches his wrist, avoiding the cut entirely."

    "When she wrenches his arm back, his fingers go loose , sending the weapon clattering to the ground."
    show mac earscop wolfhappy
    ma "Nice knife."

    ma "Doesn’t do you much good if you don’t know how to use it."
    show mac earscop wolfbasic
    "A guttural snarl erupts from Damien’s throat, and he takes another swing at Mackenzie, only to get a solid fist right to the jaw."
    stop music fadeout 1.0
    play music hifleveryday
    show damien wolf wolfbasic at left4
    "His knees drop, sending him right to the ground when she lets go of him."

    dam "..."
    show mac earscop wolfsmirk
    ma "Oh, you’re not done talking."
    show mac earscop wolfbasic at left1 behind damien
    show hiflmc casual angry at right4
    "I run over to Mackenzie as she kneels over Damien, grabbing him by the front of his jacket."

    ma "Where is Grace? You said you’d bring her with you."
    show damien wolf wolfsmirk
    dam "Heh."

    "Damien coughs, his face a total mess, but the sound ends on a laugh."
    show hiflmc casual surprised
    dam "She ran away from me days ago. Before I came and took your girl."
    show mac earscop wolfgrowl
    ma "You’re lying."
    show damien wolf wolfbasic
    dam "Think what you want."

    dam "I’ve got a shredded rope to prove it."
    show damien wolf wolfsmirk
    dam "You should ask yourself why the little lost sheep didn’t run home."
    hide damien
    "Mackenzie pulls him closer, anger tightening her jaw, but Damien’s eyes roll back before he loses consciousness, sagging in her grip."
    show mac earscop wolfbasic
    ma "Damn it."
    show mac droopcop wolfsad
    ma "[genericfn], I'm sorry."
    show hiflmc casual angry
    mcmac "We’ll find out what happened. Just cuff his sorry ass."
    show mac earscop wolfsmirk
    ma "With pleasure."
    hide hiflmc
    hide mac
    show mackenzie_s1_mini10 at bg
    "A beam of light from overhead makes me wince, but when I look up, the moon is drifting away from the sun."
    hide mackenzie_s1_mini10
    show mac earscop wolfbasic at centre
    "Mackenzie follows my eyes, then looks to the rest of the werewolves."
    show mac earscop wolfgrowl
    ma "Go home!"

    ma "This land is mine, and I’ll punish any trespassers that try and act otherwise."
    hide mac
    show annabelle casual basic at centre
    "It’s impressive to see an entire crowd scatter, and as sunlight falls across the town again, their transformations bleed away."
    hide annabelle
    show razi casual happy at centre
    ra "And cut! That’s a wrap, folks."

    "Then I hear cheering."
    hide razi
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(Huh?)"
    hide hiflmc
    show elmer casual basic at right4
    show luce casual basic at centre
    show mailman casual basic at left4
    "Behind us is a group of the townsfolk, all clapping and watching in awe."
    hide luce
    hide elmer
    hide mailman
    show razi casual happy at centre
    "Next to them is a massive camera with Razi leaning against it, magic flowing from his fingertips."
    hide razi
    show jd casual happy at centre
    $sidecharone = "Jordan"
    sid1 "What an impressive performance!"
    show jd casual happy at left5
    show elmer casual basic at right5
    show luce casual basic at right3 behind elmer
    show mailman casual basic at right1 behind luce
    "JD snaps their fingers and everyone echoes the sentiment, all smiling as one."
    hide jd
    hide elmer
    hide luce
    hide mailman
    show hiflmc casual_cu surprised_cu at hiflmc_cu
    "(It’s like they have everybody hypnotized!)"
    hide hiflmc
    show razi casual basic at left4
    show jd casual happy at right4
    jd "Hey, Razi, should I bring them on down to Georgia?"
    show razi casual sad
    ra "Please don’t."

    ra "They’ll only think this was a movie if they wake up in their own houses."
    hide jd
    hide razi
    show hiflmc casual surprised at right4
    show mac earscop wolfbasic at left4

    mcmac "How is that possible?"
    show mac earscop wolfsmirk
    ma "It’s an illusion. I didn’t know either one of them were that powerful."
    hide hiflmc
    show diego casual happy at right4
    di "Call it a save for a good friend."
    show diego casual glasseshappy
    "Diego tucks his sunglasses back into place, smiling quietly."
    hide diego
    show hiflmc casual sarcastic at right4
    mcmac "So what are we doing with him?"

    "I point down to Damien, who is totally unconscious."
    show mac earscop wolfbasic
    show hiflmc casual basic
    ma "I’ll be speaking to the real Rider alpha."
    stop music fadeout 1.0
    play music hiflheavyromance
    show mac earscop wolfhappy
    ma "But for now..."

    ma "Come here."
    scene mac4 at bg with fade:
        zoom 0.5
        yanchor 0.6
        linear 10 yanchor 0.05
    pause

    "Mackenzie kisses me, and I welcome it with a soft hum, clutching at her shoulders."

    "I feel her transformation ripple through her, the sharpness of her teeth vanishing as green eyes anew."

    mcmac "So I’m the alpha’s partner, huh?"

    mcmac "Sounds like a good gig."

    ma "Ahem. I'll... tell you more about that later."
    hide mac4
    show bg main_day_fog at bg
    show jd casual smirk at centre
    "A chorus of cleared throats behind us makes me pull back, and I blush at the sight of JD’s raised brow"
    hide jd
    show razi casual happy at left4
    show diego casual glassessmirk at right4
    "Razi chuckles to himself, but Diego’s smile is far too knowing."
    hide razi
    hide diego
    show hiflmc casual_cu blush_cu at hiflmc_cu
    "(Whatever, I’m totally dating a werewolf and they’re not.)"

    "(Pretty sure I win this one.)"
    scene bg road_night at bg
    with fade
    stop music fadeout 1.0
    play music hifleveryday
    pause
    show truck_back_night at bg
    show hiflmc casual basic at right3:
        zoom 1.05
    show mac cop smirk  at left3:
        zoom 1.05
    show truck_front_night at bg
    "It takes hours to clean up the street and clear out the busted cars, but everyone in town goes home with a smile on their face thanks to JD."

    "Apparently, they’ll forget almost everything by the next morning."

    "Mac has the sheriff’s car put in for repairs, so I pick her up in my truck and decide to head right home."
    show hiflmc casual sarcastic
    "(We talked about dinner plans, but honestly after today, I’d rather brave my kitchen.)"
    show hiflmc casual happy
    mcmac "You were amazing, Mac."

    ma "I wasn’t going to go down without a fight."
    show mac cop sad
    show hiflmc casual sad

    mcmac "No, I just... I saw how hard it was to accept you were an alpha."

    mcmac "That it wasn't something you wanted."

    ma "What I don’t want is to control people."

    ma "Leading is fine and protecting is what I do best, but everyone lives should be their own."
    show hiflmc casual sarcastic
    mcmac "After they forget an entire pack of werewolves tore up Main Street."
    show mac cop happy
    ma "...Yeah, after that part."
    show bg mc_house_ext_night
    stop music fadeout 1.0
    play music hiflliteromance
    show truck_back_night at bg
    show hiflmc casual happy at right3:
        zoom 1.05
    show mac cop happy  at left3:
        zoom 1.05
    show truck_front_night at bg

    "We both laugh, and a warm feeling sits deep in my chest as I pull up to the house and park."

    show hiflmc casual happy at left1
    show mac cop smirk behind hiflmc
    "Once my seatbelt’s undone, I climb right into Mackenzie’s lap, slipping my arms around her neck."

    ma "Well, hello."

    mcmac "Hi. You’re not on patrol right now."

    ma "No, I’m not."

    "The first kiss is quick and messy, but we settle into it, and I shiver as Mackenzie grabs at me from behind, slotting our hips together."

    mcmac "Mm, as long as you want."
    show hiflmc casual blush
    mcmac "I like when you call me yours, you know."

    ma "Oh? Well, that’s a good thing."

    ma "Because that’s exactly what you are."

    "The heat infusing Mackenzie’s voice makes me shiver, and I urge her into another kiss,"

    "Muffling a moan against her mouth when calloused fingers slip up the back of my shirt."
    show mac cop happy
    "My knees squeeze in on either side against Mackenzie’s thighs, and she laughs softly against my lips."

    ma "Do we need to take this inside, Miss [genericln]?"
    show hiflmc casual happy
    mcmac "You tell me, Sheriff."

    mcmac "But I’m pretty sure I’ve got the best seat in the house."
    show mac cop smirk
    ma "I could give you a better one."
    show mac cop happy
    "I do a little wolf whistle, making her laugh."
    stop music fadeout 1.0
    play music mackenziehunt
    show mac cop surprised
    show hiflmc casual basic at right3
    "The sound is cut through by a loud buzzing, and it takes me a second to find my phone from where it fell on the console."
    show hiflmc casual sarcastic
    show mac cop basic

    "(Who is even calling me this late?)"

    mcmac "Hello?"

    $sidecharone = "???"
    show hiflmc casual surprised
    sid1 "Hey, sis."

    "(Grace?!)"
    show mac cop surprised
    mcmac "Grace, oh my god. Where are you?"
    show hiflmc casual sad
    mcmac "Are you okay?"

    mcmac "I know some scary guy named Damien had you, but we took care of him already so—!"

    gr "That doesn't matter."
    show hiflmc casual surprised
    mcmac "Of course it matters."
    show hiflmc casual sad
    mcmac "Sweetheart, just tell me where you are."

    mcmac "I’m in the truck right now, I’ll come get you."

    "Silence falls over the line, and for a moment I’m scared the call disconnected."

    "The numbers keep ticking by in my screen before I hear Grace whisper."
    show hiflmc casual surprised
    gr "I know what happened to Mom and Dad."
    hide truck_back_night
    hide mac
    hide hiflmc
    hide truck_front_night


    $tobecontinued()
    show bg hifltbc2 at bg
    with fade

    pause
    $ resets()
