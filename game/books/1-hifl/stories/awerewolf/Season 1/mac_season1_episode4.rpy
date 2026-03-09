##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.


#define mycharacter2 = Character("books.names[\"macfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label mac_season1_episode4:
    $tbc = False

    ##Change these to suit the story
    scene bg abandoned_house_moon_fog at bg
    play music hiflaction

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show hiflmc beaniecasual surprised at centre

    "I do the first thing I can think of."
    show hiflmc beaniecasual angry
    "Chucking a rock at a werewolf might be a little David and Goliath, but it's all I've got."
    hide hiflmc
    show mac earstank wolfbasic at right3
    show damien wolf wolfbasic at left3
    "The stone clocks him right in the temple, making him freeze just long enough for Mackenzie to slip his grasp."
    hide mac
    show hiflmc beaniecasual surprised at right3
    show damien wolf wolfangry at left1 behind hiflmc
    "She starts to circle him, body tense and ready to spring back into the fray, but he rounds on me and lunges forward."

    mcmac "Shit!"
    show hiflmc beaniecasual surprised at right5

    "I stumble back at the swipe of claws, the razor-sharp edge just skirting my skin."

    "It stings, suddenly flush with colour, but before he can slash at me again,"
    show mac earstank wolfgrowl at left3 behind damien
    "Mackenzie's arm comes around his throat from behind and locks tight."


    ma "Touch her again and I will kill you right here, Damien."

    dam "Gh—"

    dam "Good luck with that, Mac."
    show mac earstank wolfsurprised
    "He's wheezing and thrashing in her grasp, but manages to drive both elbows back into Mackenzie's ribs,"

    "So hard that I'm shocked not to hear a crack of bone."
    show mac earstank wolfsurprised at left5
    show damien wolf wolfsmirk
    "She still staggers, though, and Damien is quick to press the advantage."

    dam "That girl was just the beginning."

    dam "I'll take this one too, give myself a matching pair."
    hide mac
    hide damien
    show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
    "(Is he talking about Grace?)"
    show hiflmc beaniecasual surprised at centre
    "Terror and anger shakes me all at once, leaving my head spinning."
    hide hiflmc
    show mac earstank wolfbasic at left4
    show damien wolf wolfsmirk at right4
    ma "If, and only if you give her back right now..."

    ma "I won't hunt your hide all the way to the coast."
    show damien wolf wolfsmirk at centre
    show mac earstank wolfbasic at left4 behind damien

    "Damien smirks before darting forward to close the gap between them, snapping his teeth to try and find a hold on Mackenzie's shoulder."
    show mac earstank wolfbasic at left5
    "It's a brutal attempt, but she counters with a knee to the stomach, escaping with a small scrape."

    dam "You're alone, Hunt."

    dam "You always have been. When's the last time your line ran true?"
    show mac earstank wolfgrowl
    ma "My family's here. This is OUR territory."
    show damien wolf wolfbasic
    dam "Territory held by a single wolf."

    dam "No pack, no allegiances."
    show damien wolf wolfsmirk
    dam "All the cousins in the world don't matter if they can't shift."

    ma "You look pretty alone to me, Damien."

    dam "For now."
    show damien wolf wolfbasic at left3 behind mac
    "With those ominous words, he attacks Mackenzie again,"
    show mac earstank wolfangry at left5
    "But I'm left in awe at how she moves, parrying every blow before ramming Damien in a full-on tackle."

    "They hit the ground hard enough for me to wince, but he doesn't seem the least bit concerned."
    hide mac
    hide damien
    show hiflmc beaniecasual_cu angry_cu at hiflmc_cu
    "(Is this just a game to him? What the hell does he want with my sister?)"
    hide hiflmc
    show damien wolf wolfsmirk at right3
    show mac earstank wolfbasic at left3
    dam "These sheep are mine."

    dam "You can't protect these humans anymore, Mackenzie."

    dam "Give them to someone who will herd them properly."
    show mac earstank wolfgrowl
    ma "They're people, not animals!"

    dam "They serve the same purpose."
    show damien wolf wolfsmirk at right5
    "Rage leaves Mackenzie's eye blazing, but her next punch strikes empty ground when Damien dodges, throwing her off him."
    show mac earstank wolfsurprised
    "She has to catch herself before tumbling into the lake, springing back to her feet in open fury."
    show damien wolf wolfbasic
    show mac earstank wolfbasic
    dam "The Rider pack knows I'm making a move on this place."

    dam "When it's mine, I'll be their champion."
    show damien wolf wolfsmirk
    dam "So bow or run, sheriff."

    dam "This town isn't worth dying for."
    hide mac
    show damien wolf wolfsmirk at centre
    "He gives a mocking salute before diving right into the fog, so fast my eyes hurt from trying to track him."
    stop music fadeout 1.0
    play music mackenziehunt
    hide damien
    show mac earstank wolfbasic at left3
    show hiflmc beaniecasual surprised at right3
    "Mackenzie sniffs the air, trying to track Damien, and I recognise the power in her limbs."

    "She's about to take off like she did the night of the full moon."

    mcmac "Hey, wait a second."
    show hiflmc beaniecasual surprised at left1
    "I grab her without thinking."
    hide mac
    hide hiflmc
    show mackenzie_s1_mini11 at bg
    "The cool press of claws makes my heart stutter, but I refuse to let go, even when Mackenzie snaps to look at me with that golden gaze."
    $menuhideborder = True
    hide mackenzie_s1_mini11
    menu mace4c1:
        "1. Don't leave me alone.":
            $menuhideborder = False
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu:
                xpos 0.25
            show mac earstank_cu wolfbasic_cu at mac_cu behind hiflmc:
                xpos 0.75

            mcmac "I know you want to chase him, but please don't leave me alone here."
            mcmac "This fog, this house, another werewolf... it's too much."
        "2. You're hurt.":
            $menuhideborder = False
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu:
                xpos 0.25
            show mac earstank_cu wolfbasic_cu at mac_cu behind hiflmc:
                xpos 0.75
            mcmac "You're hurt. Don't go after him like this."

            mcmac "I know how powerful you are, but you're still bleeding."
            hide hiflmc
        "3. We need to look for Grace.":
            $menuhideborder = False
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu:
                xpos 0.25
            show mac earstank_cu wolfbasic_cu at mac_cu behind hiflmc:
                xpos 0.75
            mcmac "We have to look for Grace."
            mcmac "I know he's a threat, but she's the priority, right?"
    hide hiflmc
    show mac earsdroop_cu sleep_cu at mac_cu
    "The anger radiating from Mackenzie cools, her rigid shoulders relaxing by degrees."
    show mac tank_cu basic_cu at mac_cu
    "When she lets out a deep breath, every wolfish aspect fades from her skin, transformation so fluid I can only stare in awe."
    show mac tank basic at right3
    show hiflmc beaniecasual sad at left3
    ma "I'm going to check the house for your sister. Then we're going back to town."

    ma "And you need to go home. I'll drive."
    show hiflmc beaniecasual basic
    "I nod, overwhelmed with relief now that I know Mackenzie's not going anywhere."
    hide mac
    show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
    "(Right now, I'm not sure what I'd do without her.)"

    hide hiflmc

    scene bg road_night at bg with fade
    pause
    show truck_back_night at bg
    show hiflmc beaniecasual sad at left4:
        zoom 1.05
    show mac cop basic at right4:
        zoom 1.05
    show truck_front_night at bg

    "I give Mackenzie my keys, but she has to take a minute pulling her uniform shirt back on, jaw tense with pain."
    show hiflmc beaniecasual blush
    "I'm so tempted to offer help with the buttons, except I don't want her to take it the wrong way."

    ma "Come on. Let's get going."
    show hiflmc beaniecasual basic
    "She starts up the truck and peels away from the lake back to the main road, silence falling between us."

    "It feels like its own fog, buoyant with tension, and the urge to break it makes me speak up."

    mcmac "So there is another werewolf here."

    ma "... Yes."

    mcmac "And you knew his name."
    show hiflmc beaniecasual surprised
    mcmac "He was talking about packs and champions and bloodlines and—!"
    show hiflmc beaniecasual sad
    mcmac "You've got to tell me what's going on, Mackenzie."

    mcmac "I can't have someone bleeding in my car and not tell me why she did it."

    mcmac "No one's ever put themselves in harm's way like that for me."
    show mac cop sleep
    "Mackenzie sighs, fingers flexing around the steering wheel."
    show mac cop sad
    ma "You don't need to know any of that."

    mcmac "But I want..."

    ma "I said 'need'. It's sure as hell not going to make your life easier, [genericfn]."

    ma "Ignorance is bliss. Trust me on that."

    mcmac "I already know what you can do, what you are."
    show hiflmc beaniecasual happy
    mcmac "If that was the line, we've already crossed it."
    show mac cop basic
    ma "..."

    mcmac "It'll make protecting me easier if I'm not tripping into some secret werewolf ritual, won't it?"
    stop music fadeout 1.0
    play music hifleveryday
    show mac cop happy


    "That makes Mackenzie chuckle, shaking her head as if she can't believe what I'm saying."

    "Her smile is so warm, full of heart."
    show mac cop basic
    ma "First off, there's no ritual. Packs are... packs, groups of werewolves."

    ma "Honestly, the bond between a pack is a bit magical, but if you want the arcane details, I'm not the one to ask."
    show hiflmc beaniecasual surprised
    mcmac "Magic."

    mcmac "Right, of course that exists."
    show hiflmc beaniecasual sarcastic
    mcmac "Why would I think half the people I know being supernatural creatures was the limit."
    show mac cop smirk
    ma "To be fair, it is a little unusual."

    ma "Most wolf territories don't have djinn and vampires running around in them."
    show mac cop basic
    ma "When we own a space, we have the right to approve who comes in."
    show hiflmc beaniecasual happy
    mcmac "And you wanted some company?"
    show mac cop smirk
    ma "Heh. It wasn't my call then."

    ma "Razi's family has been here for a long time."

    ma "Diego's old enough to remember a little spat called the Revolutionary War."
    show hiflmc beaniecasual surprised
    mcmac "Jesus."
    show hiflmc beaniecasual basic
    show mac cop basic
    ma "Yeah. JD's the one exception."

    ma "I let them in by... special request."

    "There has to be a story behind that, but I'm more curious about Mackenzie herself."
    hide mac
    hide hiflmc
    $menuhideborder = True
    menu mace4c2:
        "1. Can you turn into a real wolf?":
            $menuhideborder = False
            show hiflmc beaniecasual basic at left3 behind truck_front_night:
                zoom 1.05
            show mac cop basic at right3 behind truck_front_night:
                zoom 1.05

            mcmac "I've seen you shift a few times, but can werewolves turn into actual wolves?"
            show mac cop surprised
            mcmac "Like the four-legged kind?"
            show mac cop basic
            ma "Some can. I've never had the knack for it."

            ma "They say you can learn, but I don't exactly have a teacher."
        "2. What about silver?":
            $menuhideborder = False
            show hiflmc beaniecasual basic at left3 behind truck_front_night:
                zoom 1.05
            show mac cop basic at right3 behind truck_front_night:
                zoom 1.05
            mcmac "What about silver? Is that a thing?"

            ma "Unfortunately."
            ma "The only saving grace is that it has to get into our blood to do real damage."
            show mac cop smirk
            ma "From a cut, swallowed, whatever. I just try not to keep it around."

        "3. Are you going to be okay?":
            $menuhideborder = False
            show hiflmc beaniecasual sad at left3 behind truck_front_night:
                zoom 1.05
            show mac cop basic at right3 behind truck_front_night:
                zoom 1.05
            mcmac "Are you gonna be okay though? Damien tried to do a number on you."

            ma "It'll heal."
            show mac cop smirk
            ma "Not in the blink of an eye, but I have a bit of an advantage there."
            ma "By morning, it'll be like the fight never happened."

    
    show mac cop basic at right3 behind truck_front_night:
        zoom 1.05
    show hiflmc beaniecasual basic at left3 behind truck_front_night:
        zoom 1.05
    "Mackenzie pulls up outside my house and kills the engine, but hesitates right before giving back the keys."
    show mac cop sad
    "Our eyes lock, the weight of her gaze seriously intense."

    ma "Do you believe me?"
    show hiflmc beaniecasual sad
    mcmac "..."
    show hiflmc beaniecasual surprised
    "(It's an out. She's giving me an out, so I can go back to my regular old life after we find Grace.)"
    show hiflmc beaniecasual basic
    show mac cop surprised
    mcmac "Yeah. I do."
    show mac cop smirk
    "She gives a firm nod, but I catch a flicker of a smile as we get out of the car together and go into the house."
    scene bg heroine_home_lights at bg
    show hiflmc beaniecasual basic at left1
    show mac cop basic at right2 behind hiflmc
    "Mackenzie stops me in the living room with a hand on my shoulder."

    ma "Sit down."
    hide mac
    show hiflmc beaniecasual blush
    "I do it without thinking, the authority in her voice absolute, but blush when she turns around and heads into another room."
    show hiflmc beaniecasual_cu blush_cu at hiflmc_cu
    "(Yes, ma'am. Thank you, officer. Ahem.)"
    show hiflmc beaniecasual surprised at left1
    show mac cop basic at right4
    "When Mackenzie returns with the first aid kit in my bathroom, I'm a little surprised."

    mcmac "How did you know where to find that?"
    show mac cop smirk
    ma "It wasn't in your truck. Bathroom or closet were the only options left."
    show mac cop sad
    ma "Now let me see your arm."
    show mac cop sad at right2 behind hiflmc
    "Mackenzie tears open the foil of an antiseptic wipe with her teeth and then runs the cool wipe across the scratches Damien left."
    show hiflmc beaniecasual sad
    "Only a few were deep enough to turn red, but it still stings a bit."
    show hiflmc beaniecasual blush
    mcmac "So this is probably a silly question because you're not freakingpromise out, but..."
    show mac cop surprised
    mcmac "Getting scratched by a werewolf doesn't mean I'll be howling at the next full moon, right?"
    show mac cop basic
    ma "No. But humans can be turned."
    show hiflmc beaniecasual surprised
    mcmac "Seriously?"

    ma "It takes a bite, and a deliberate one at that."
    show mac cop sad
    ma "\'You're responsible for whoever you change, so it's not common."
    hide mac
    show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
    "(I hate the thought that just crossed my mind.)"
    show hiflmc beaniecasual sad at left1
    show mac cop sad at right2

    mcmac "Do you think Damien's going to do that to Grace?"
    show mac cop surprised
    "Mackenize's hands go still against my skin."

    "The sting is gone, leaving nothing behind but the warmth of her fingertips."
    show mac cop angry
    ma "[genericfn], I wouldn't let that happen."
    show mac cop sad
    ma "He'd be a fool to even try, but I promise I'll get her back before anything like that goes on, okay?"

    mcmac "Okay."
    show mac cop surprised
    "She bandages my arm with care, but when Mackenzie moves to close the first aid kit, I catch her hand in my own."

    mcmac "Don't you still need that?"
    show mac cop basic
    ma "I'll be fine."
    show hiflmc beaniecasual sarcastic
    mcmac "Okay, I know you're tough as nails, but unless your blood magically evaporates, you're still hurt."

    mcmac "So please let me?"

    hide hiflmc
    show mac cop sad at centre
    "Mackenzie sighs but gives up on trying to close the kit, starting to unbutton her shirt instead."
    show hiflmc beaniecasual blush at left4
    show mac tank basic at right4
    "I try not to sneak too many peeks while I bring the bandages over to the couch, but the fact is..."

    "There’s now a very attractive woman sitting on my coffee table."
    show hiflmc beaniecasual basic
    show mac tank sad
    ma "Start with my shoulder if you don't mind. That's the deepest one."
    show hiflmc beaniecasual surprised at left2 behind mac
    show mac tank sad at right1
    "Now that I have a close-up look,I see a claw mark curving up from Mackenzie’s back into the meat of her shoulder."

    "And the stale scent of blood unsettles my stomach."
    show hiflmc beaniecasual sad
    "My hand shakes a little as I start cleaning the cut."
    hide mac
    show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
    "(I promised I’d help her. It’s silly to stop because I’m squeamish.)"
    show hiflmc beaniecasual sad at left2 behind mac
    show mac tank smirk at right1
    ma "Not used to this sort of thing, are you?"
    show hiflmc beaniecasual happy
    mcmac "I mean, Grace jammed her thumb in a door once, but it didn't bleed so..."
    hide hiflmc
    show mac tank smirk at centre
    "My nervous smile probably tells her everything she needs to know, but the frustration I expect never comes."

    "Mackenzie is nothing but calm, patient even when I start fumbling with the first bandage."
    show hiflmc beaniecasual blush at left2 behind mac
    show mac tank happy at right1
    ma "You're doing just fine."

    ma "So how's your job going?"
    show hiflmc beaniecasual surprised
    mcmac "What?"
    show mac tank smirk
    ma "Work. Your life. I want to hear more about you."
    show hiflmc beaniecasual blush
    "Heat rushes up my cheeks as I tape the bandage in place."

    mcmac "It's fine, I guess. I mean, for a bowling alley."

    mcmac "Razi's super nice and throws monthly employee parties even though there's like three of us here."
    show hiflmc beaniecasual happy
    mcmac "Probably to get through all the liquor, you know?"
    show mac tank happy
    "Mackenzie smiles like she does know, and the second claw mark is a bit easier to clean and bandage."
    show hiflmc beaniecasual basic
    "I go for a bite on the inside of her arm next, but the tape won’t stick, so I have to wrap it."

    mcmac "See if that one stays."
    hide mac
    hide hiflmc
    hide bg heroine_home_lights
    show mackenzie_s1_mini4 at bg
    stop music fadeout 1.0
    play music hiflliteromance
    "She flexes her arm to test the gauze and the inside of my mouth goes dry."

    "With my hand still there, I can feel the muscle ripple and tighten, which makes my fingers squeeze a bit tighter."
    hide mackenzie_s1_mini4
    show  bg heroine_home_lights at bg
    show hiflmc beaniecasual blush at left2 behind mac
    show mac tank blush at right1
    ma "Um..."
    show mac tank blush at right3
    "Our eyes meet for a fraction of a second before Mackenzie coughs and pulls her arm back."
    show hiflmc beaniecasual blush at left4
    "I retreat back against the couch, wondering if it’s possible for the cousins to swallow me whole."

    mcmac "Sorry."

    ma "Don't worry about it."
    hide mac
    show hiflmc beaniecasual_cu blush_cu at hiflmc_cu
    "(Is she blushing?)"
    show  hiflmc beaniecasual blush at left4
    show mac tank sad at right3
    ma "I should get going."

    ma "At the least, I need to make some rounds around town to make sure Damien’s not lurking."
    show mac tank basic
    show  hiflmc beaniecasual surprised

    "The professional mask has firmly fallen back into place, and my stomach does a little flip."
    show  hiflmc beaniecasual sad
    "I want to bring that smile back, her easy humor."
    hide mac
    show hiflmc beaniecasual_cu blush_cu at hiflmc_cu

    "(And if she touched me again like she did during the full moon...)"
    hide hiflmc
    $menuhideborder = True
    menu mace4c3:
        "1. Stay with me, please." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show  hiflmc beaniecasual sad at left4
            show mac tank basic at right4
            mcmac "You're going after him while you're still healing?"

            mcmac "That doesn't sound like a good idea."

            ma "He's hurt too, [genericfn]."
            show mac tank smirk
            ma "More than I am, I'd wager."
            hide mac
            show  hiflmc beaniecasual sad at centre
            "I stand up, seized by a sudden worry. Mackenzie should care about the risk to herself, even if people are in danger."
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(There's only one of her. Damien said so himself.)"
            show  hiflmc beaniecasual sad at left4
            show mac tank basic at right4
            mcmac "I know it's your responsibility, and not just as a werewolf."

            mcmac "But you have deputies, don't you? People who can flash the lights around."
            show mac tank sad
            ma "They're both young. Right out of college."
            show hiflmc beaniecasual surprised
            mcmac "But they're still cops."
            hide mac
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
            "(And if that doesn't convince her—!)"
            show  hiflmc beaniecasual sad at left4
            show mac tank surprised at right4
            mcmac "I just don't want to be alone with him out there right now, Mackenzie."

            mcmac "Could you stay a little while longer?"
            hide hiflmc
            show mac tank sad at centre
            "The cool and impassive gaze levelled my way starts to melt away, compassion trapped like heat under the surface."

            "I think it's always been there with Mackenzie, but she seems to try so damn hard to hide it."
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            "(I wonder why.)"
            show hiflmc beaniecasual surprised at left2
            show mac tank sad at right2 behind hiflmc
            "When she stands up again, I'm afraid Mackenzie is going to leave anyway, only for her to give my hand a light squeeze instead."
            show mac tank happy
            ma "Could I get a cup of coffee if I do?"

            ma "This day's worn me out."
            hide mac
            show hiflmc beaniecasual_cu happy_cu at hiflmc_cu
            "(I've never made an easier trade in my life.)"
            show hiflmc beaniecasual happy at left2
            show mac tank happy at right2 behind hiflmc
            mcmac "You bet."

            mcmac "Want anything in it?"

            ma "A little cream, if you don't mind."
            hide mac
            show hiflmc beaniecasual happy at centre
            "I retreat to the kitchen to make the coffee, glad for the French press so I don't have to sit around waiting for a pot to brew."
            show hiflmc beaniecasual surprised
            "Grace got it for me last Christmas because she knows I drink so much, and—!"
            show hiflmc beaniecasual sad
            mcmac "..."

            mcmac "We'll bring you home soon, sis."
            show hiflmc beaniecasual basic at left3
            show mac tank basic at right3
            "When I come back to the living room, cups in hand, Mackenzie is standing in front of my movie shelf and reading the titles."

            "Streaming's great when I want to binge watch, but I end up picking up a lot of DVDs from the gas station bargain bin too."
            show hiflmc beaniecasual happy
            mcmac "Find anything you like?"
            show mac tank smirk
            ma "You've got some superhero flicks here, so that caught my interest."
            hide mac
            hide hiflmc
            show mackenzie_s1_mini5 at bg
            "She turns when I offer the coffee, hands cupping around mine to make sure it doesn't spill as it's passed over."
            hide mackenzie_s1_mini5

            show hiflmc beaniecasual blush at left2
            show mac tank happy at right2 behind hiflmc
            "Mackenzie lets out a pleased sigh at the first sip, and I take a bit of pride in that."
            show mac tank happy at right4
            mcmac "Superheroes, huh?"

            ma "Yeah. I mean, this one's a remake but—!"
            show hiflmc beaniecasual angry
            "When she gestures to the film in question, I squint to make out the title."
            show hiflmc beaniecasual blush
            "I'm pretty sure I fell asleep watching it a few months ago, but I can barely remember the plot."
            show hiflmc beaniecasual happy
            ma "The actress they got was perfect."

            ma "And the effect they used to conceal her face looked so smooth."

            ma "I guess I'm biased because the character's a detective but there's not a lot of action movies with a woman on the cover, you know?"
            hide mac
            show hiflmc beaniecasual_cu surprised_cu at hiflmc_cu
            "(Oh, boy. She knows a hell a lot more about this than I do.)"
            show hiflmc beaniecasual blush at left2
            show mac tank surprised at right4
            mcmac "Kind of."

            mcmac "I hate to disappoint, but I'm more of a casual fan."
            show mac tank happy
            show hiflmc beaniecasual happy
            ma "That's okay."

            ma "I've just... always liked heroes like that."

            ma "People who are more than human, but do the right thing."

            mcmac "Because you have something in common."
            show mac tank blush
            "Mackenzie quietly clears her throat, then takes a long sip of her coffee."

            ma "I guess so. It's just kind of how my family works."

            mcmac "Having a protective streak a mile wide."
            show mac tank smirk
            ma "Exactly."

            ma "No one was surprised I became a cop when every cousin I have is in one service or another."
            show mac tank basic
            ma "My parents are kind of the outliers."

            ma "Dad prefers watching out for people at town councils and PTA meetings."

            mcmac "And your mom?"

            "I've run into Mackenzie's parents once or twice, but I can't say we're close."

            "Their farm is on the very edge of our county's boundaries, nestled in a huge field."
            show mac tank happy
            ma "She fosters the GSA over at the high school. It's sweet, actually."

            mcmac "Right. I remember that."
            show hiflmc beaniecasual sad
            mcmac "I only went to a couple of those meetings, though. I felt awkward."
            show mac tank surprised
            ma "Questioning?"
            show hiflmc beaniecasual happy
            mcmac "No, I'm super bi, just terrible at social interaction."
            show mac tank smirk
            ma "Fair enough."
            show hiflmc beaniecasual sad
            mcmac "I wish I had the kind of drive you do, though."

            mcmac "The passion to pursue something like that."
            show mac tank surprised
            ma "You want a badge?"

            mcmac "No, I want... meaning."
            hide hiflmc
            show mac tank_cu basic_cu at mac_cu
            "Mackenzie leans forward a little, and my half-step closer almost puts us eye-to-eye."

            "The gold of her wolfish self is pretty, but it's easy to lose myself in that deep green."
            show mac tank_cu happy_cu
            ma "I think you'll find it."
            show mac tank_cu sad_cu
            ma "But we've got to focus on staying safe right now, okay?"
            hide mac
            show hiflmc beaniecasual_cu sad_cu at hiflmc_cu
            mcmac "\Yeah."
            show hiflmc beaniecasual_cu basic_cu
            mcmac "I'll keep my guard up."
            hide hiflmc
            show mac tank_cu basic_cu at mac_cu
            "Except I can't do that with Mackenzie right in front of me."

            "Her full mouth is so close, close enough that if I tilted my head up and—!"
            show hiflmc beaniecasual surprised at left2
            show mac tank blush at right4
            "Our coffee cups clink together and she immediately leans back."

            ma "I really should be going."
            hide mac
            show hiflmc beaniecasual_cu sarcastic_cu at hiflmc_cu
            "(Oh, damn it.)"
            show hiflmc beaniecasual sad at left2
            show mac tank happy at right4
            ma "But I'll leave you my number, okay? Personal line."
            show mac tank smirk
            ma "If anything happens, call. I'll spin around a couple times and come save you."
            show hiflmc beaniecasual blush
            mcmac "... Okay."

            "I want to thank her, but I'm too flustered to do anything but say goodbye when Mackenzie hands over her number with a smile."
            hide mac
            show hiflmc beaniecasual blush at centre
            "She sets her empty coffee cup on the kitchen counter and goes out through the front door, leaving me alone with the shaky beat of my heart."
            hide hiflmc
            $tobecontinued()
            show bg hifltbc
            with fade

            pause
            $ resets()

        "2. Let her go.":
            stop music fadeout 1.0
            play music hifleveryday
            show  hiflmc beaniecasual sad at left4
            show mac tank basic at right4
            "(Damn it. It's not fair to keep Mackenzie from her job because I'm crushing hard.)"

            mcmac "Yeah, of course."

            mcmac "Uh, happy hunting?"

            show mac tank happy
            "That does get a laugh, enough to make my heart flutter before Mackenzie’s eyes bleed to gold again."
            show mac tank basic
            "She tosses her shirt over one shoulder and leaves, and I follow her out with my gaze until the front door clicks shut."
            hide mac
            show hiflmc beaniecasual sarcastic at centre
            mcmac "Ugh. Now what do I do with myself?"
            show hiflmc beaniecasual basic
            "Out of curiosity, I decide to look up werewolves online, wondering if there’s been any local rumours about them being real."

            "But everything that pops up is either fake apocalyptic or fights with sparkling vampires."
            show hiflmc beaniecasual sarcastic
            "(Diego doesn’t seem to be the glittery type.)"

            mcmac "“I should have asked Mackenzie more questions when I had the chance."
            show hiflmc casualbeanie_cu sad_cu at hiflmc_cu
            "Glancing back at the door, I sigh."

            "(Could I have convinced her to stay?)"
            hide hiflmc
            $tobecontinued()
            show bg hifltbc
            with fade

            pause
            $ resets()
