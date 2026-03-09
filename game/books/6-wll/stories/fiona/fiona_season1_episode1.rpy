label fiona_season1_episode1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene wll_prologue_s1_mini1 at bg
    show cinema_fov
    play music wllspookymysterious1 fadein 1.0

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    "Strange tales come crawling out of the west—but so do stories that ignite a traveler's dreams."
    "What's a tall tale of otherworldly critters told around the fire, when the west promises riches, romance, and adventure?"
    scene wll_prologue_s1_mini2 at bg
    show cinema_fov
    with dissolve
    "People ride westward to find a new life—or to run from the life they've been living."
    "For most people, Solano Territory is the end of the line, but legend has it that there's a whole Otherworld out there on the frontier."
    scene fiona_s1_mini_prologue at bg
    show cinema_fov
    with smokey_transition
    "Rumors abound of a powerful soothsayer, a woman whose eyes see the yet-to-come as clear as the here-and-now."
    "Tempting to ask for your future, perhaps, but dangerous too. Can you bear what those golden eyes will see in your mind? In your heart?"
    show cinema_fov at cinema_fov_out

    scene bg_wll_train_car_day at bg
    show wllmc coat_cu angry_cu at wllmc_cu
    with fade
    stop music fadeout 1.0
    play music wlltense2 fadein 1.0
    "(Hells and damnation, why did that stupid old woman have to wake up?)"
    hide wllmc
    show wllmc coat angry at centre
    "I race down the train, dodging startled passengers and the rattling food cart."
    hide wllmc
    show wllmc coat_cu angry_cu at wllmc_cu
    "(I don't think the conductor got a good look at my face, but I need to figure out where to hide or I'm done for.)"
    hide wllmc
    show wllmc coat angry at centre
    "The thought of getting caught is an acid taste in my mouth."
    hide wllmc
    show wllmc coat_cu basic_cu at wllmc_cu
    "(This is my big chance. Get to Serpent's River territory, get away from the law, get a fresh start.)"
    show wllmc coat_cu angry_cu
    "(I can't let my dreams be scuppered now.)"
    hide wllmc
    show wllmc coat surprised at centre
    "I notice a train car with an open door, and seize my chance, sliding in as quiet as I can."
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(With luck, maybe it's empty.)"
    hide wllmc
    show wllmc coat sad at centre
    "As usual, though, luck doesn't know my name."
    hide wllmc
    show fiona hood basic_hood at left3
    show diana casual basicglasses at right3
    $sidecharone = "Honeyed Voice"
    sid1"I understand completely. But what you're asking for doesn't come easy."
    sid1 "For the reading to work, I'll need an object of emotional value to act as a linchpin."
    show diana casual surprisedglasses
    $sidecharone = "Nervous Voice"
    sid1 "Something of emotional value?"
    "I peer into the car and see an older woman and a hooded figure sitting across from each other."
    "The older woman is fingering a locket around her neck."
    hide fiona
    hide diana
    show wllmc coat_cu smile_cu at wllmc_cu
    "(The deck of big cards on the table tells me all I need to know about the con that's running.)"
    hide wllmc
    show fiona hood basic_hood at left3
    show diana casual surprisedglasses at right3
    $sidechartwo = "Silver-tongued Scam Artist"
    sid2 "I can see you touching that locket around your neck. Do you think it would serve?"
    hide fiona
    hide diana
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(I can't believe she's being so blatant and the client hasn't noticed. This woman almost deserves to get scammed.)"
    hide wllmc
    "But I can't resist throwing a wrench in the works either."
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Rules are you should never interfere with another gal's con, but something about this one just rubs me the wrong way.)"
    hide wllmc

    # TODO : Check choice button padding
    $menuhideborder = True
    menu fionas1e1c1:
        "Emotional value? More like actual value.":
            $menuhideborder = False
            show wllmc coat smirk at left3
            show fiona hood surprised_hood at right3
            mcfiona "Emotional value? Is that what we're calling it now?"
            mcfiona "Because it looks to me as if what you're really after is a big lump of pure silver."
        "Never trust anyone wearing a big cloak.":
            $menuhideborder = False
            show wllmc coat smirk at left3
            show diana casual basicglasses at right3
            mcfiona "Never trust a fortune teller in a cloak and hood. They wear them so you can't follow their movements."
            mcfiona "Makes it easier to stack the deck."
            hide diana
        "Another phony Spiritualist.":
            $menuhideborder = False
            show wllmc coat smirk at left3
            show diana casual basicglasses at right3
            mcfiona "Another phony Spiritualist? I was just reading in the paper about one who got busted back in New Amster."
            mcfiona "I guess as crimes go, fake fortune telling at least has style."
            hide diana

    hide wllmc
    show fiona hood angry_hood at centre
    "The hooded figure jerks and turns her head slightly, then waves a hand in my direction."
    show fiona hood basic_hood at left3
    show diana casual basicglasses at right3
    sid2 "I deal with unbelievers all the time. It's true that there are lots of pretenders to my throne."
    sid2 "But I promise, if you are the least bit unsatisfied with my reading, the locket will remain yours."
    show diana casual surprisedglasses
    "The client hesitates, looking back and forth between me and the fortune-teller."
    hide fiona
    show wllmc coat smirk at left3
    show diana casual surprisedglasses at right3
    mcfiona "If you're so unsure, why don't you watch her read my future first? That should tell you everything you need to know."
    hide diana
    hide wllmc
    show wllmc coat_cu grin_cu at wllmc_cu
    "(After all, she hasn't had time to case me the way she's obviously studied her mark. And I know how to hold a poker face.)"
    hide wllmc
    show fiona hood surprised_hood at left3
    show diana casual sadglasses at right3
    $sidecharone = "Nervous Client"
    sid1 "I think I should leave. Perhaps we can do this another time."
    "She stands up and looks down at the fortune teller."
    sid1 "I'm sorry."
    show fiona hood basic
    sid2 "Don't be. I know we'll meet again, very soon."
    hide fiona
    hide diana
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(Damn, that's a pretty good line.)"
    hide wllmc
    show diana casual smileglasses at centre
    "The woman blinks, smiles a faint smile, and leaves. As she passes me, I dip my hand into her pocket and come away with her pocketbook."
    hide diana
    show wllmc coat_cu smallsmile_cu at wllmc_cu
    "(I mean, I already knew she was an easy mark. And at least its contents will be less than the cost of that locket.)"
    show wllmc coat_cu smirk_cu
    "(Call it a protector's fee.)"

    hide wllmc
    show wllmc coat smallsmile at left3
    show fiona hood angry_hood at right3
    $sidechartwo = "Scam Artist"
    sid2 "Well, you must be very pleased with yourself."
    show fiona hood smirk_hood
    sid2 "Do you really have such a moral objection to fortune telling, or were you just hoping to get me alone?"

    hide wllmc
    hide fiona
    stop music fadeout 1.0
    play music wlleverydaycalm3 fadein 1.0
    show fiona hood_cu smirk_hood_cu at fiona_cu
    "As I draw closer I get my first look at her unshadowed face."
    "Thick lashes ring bright gold eyes above a playful smirk."
    hide fiona
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(Oh. She's pretty!)"
    hide wllmc
    show wllmc coat smirk at left3
    show fiona hood smirk_hood at right3
    mcfiona "I have a moral objection to someone doing their job badly."
    mcfiona "You can't just ask for the locket outright. Have a little subtlety."
    show fiona hood grin_hood
    "The woman laughs, and then holds out a slim, long-fingered hand to me."
    sid2 "I can see we're operating under a misunderstanding."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    sid2 "I'm Fiona Eichen, the truest reader of the future west of New Amster."
    "I take her hand and shake it, enjoying the cool press of her fingers against my palm."
    hide fiona
    show wllmc coat grin at centre:
        xoffset -20
    show fiona hood smile_hood at right3
    mcfiona "[genericfn] [genericln]. I'm a lady not easily hoodwinked by a smooth scam."
    show fiona hood smirk_hood
    mb "Oh really?"
    show wllmc coat smallsmile
    "She takes her cards in hand and shuffles them, one rippling arc from palm to palm."
    show wllmc coat smirk
    mcfiona "Wow. How magical. Shuffling cards, a trick I definitely haven't seen fifty times."
    mb "It's true. Lots of people can shuffle cards. But not many can do this."

    scene fiona_s1_ei1 with fade:
        zoom 1.5 align(0.5, 1.0)
        linear 6.0 yoffset 1800
    stop music fadeout 1.0
    play music wllfionatheme fadein 1.0
    pause
    "She twists her wrist, and the cards fly up into the air, almost seeming to hover around me."
    window hide
    show fiona_s1_ei1:
        linear 3.5 yoffset 960
    pause
    "(How is she doing that? Wires? Magnets? Some kind of optical illusion?)"
    "Fiona plucks a card from the air and holds it up in front of her."
    mb "Well? Care to try me out?"
    "Her pert mouth curves up into an absolutely provocative smile."
    "(I bet that mouth would look less smug after a thorough kissing.)"
    scene bg_wll_train_car_sunset at bg
    show wllmc coat embarrassed at left2
    show fiona hood smile_hood at right3
    with fade
    "I bury that thought as fast as it comes to me, and focus on the unanswered challenge."
    hide fiona
    hide wllmc
    show wllmc coat_cu smirk_cu at wllmc_cu
    "(My heart might be beating a little faster than usual, but I never back down when pushed into a corner.)"
    hide wllmc
    show wllmc coat smirk at left2
    show fiona hood smile_hood at right3
    mcfiona "Looks like you've got some pretty good tricks, but don't get too confident."
    mcfiona "I might be more than you can handle."
    show fiona hood smirk_hood
    mb "I certainly hope you are."
    show wllmc coat smirk behind fiona at left3:
        easein 0.4 centre xoffset -20
    "I sit down on the bench at her side, watching her hands carefully as she lays out the reading."
    show fiona hood smile_hood
    mb "Do you know much about the tarot?"
    show wllmc coat smallsmile
    mcfiona "It's never been my forte. But who knows, maybe you'll convince me it's worth adding to my repertoire."
    show fiona hood smirk_hood
    mb "We'll just have to see."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    "She flips over the cards and lays them out in a pattern..."
    hide fiona
    "The Fool, the Page of Wands, The Hanged Man, the Knight of Cups, The Lovers, and the Wheel of Fortune."
    show fiona hood_cu surprised_hood_cu at fiona_cu
    "For a moment, Fiona looks almost startled."
    hide fiona
    show wllmc coat smallsmile at centre:
        xoffset -20
    show fiona hood surprised_hood at right3
    mb "I didn't..."
    show fiona hood smile_hood
    "Then she shakes her head and smiles."
    mb "The Fool? Well that's certainly appropriate."
    show wllmc coat smirk
    mcfiona "Just what are you implying, Ms. Eichen?"
    show fiona hood smirk_hood
    mb "Please, Fiona. I think we're well past the point of misses and ma'ams."
    "She winks."
    show wllmc coat smallsmile
    mb "And The Fool is perfect because it's the card for someone at the start of a journey."
    "Her hand reaches out and touches the illustration of a man walking cheerfully down a road, a bindle over his shoulder."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "Like a young woman venturing west to seek her fortune, for example."
    hide fiona
    show wllmc coat_cu smallsmile_cu at wllmc_cu
    "I touch the card too, tracing the cliff edge he walks beside, and my fingers not-at-all-accidentally brush hers."
    hide wllmc
    show wllmc coat surprised behind fiona at centre:
        xoffset -20
    show fiona hood smirk_hood at right3
    mcfiona "Is this supposed to be me?"
    hide wllmc
    hide fiona

    $menuhideborder = True
    menu fionas1e1c2:
        "How cliche.":
            $menuhideborder = False
            show wllmc coat smirk behind fiona at centre:
                xoffset -20
            show fiona hood smirk_hood at right3
            mcfiona "How cliche. I admit, a fortune would be nice, but I'd settle for a comfortable independence and my freedom."
            show fiona hood grin_hood
            mb "That's the biggest lie you've told since you stepped through my door. I can see at once you're a woman of ambition."
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            mb "It's your most charming quality."
        "What's next? A tall, dark, handsome stranger?":
            $menuhideborder = False
            show wllmc coat smirk behind fiona at centre:
                xoffset -20
            show fiona hood smirk_hood at right3
            mcfiona "What's next? A tall, dark, handsome stranger?"
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            mb "No, that's already happened. Well, excluding tall. A woman can't have everything, I suppose."
        "Subtlety really isn't your strong suit.":
            $menuhideborder =False
            show wllmc coat smirk behind fiona at centre:
                xoffset -20
            show fiona hood smirk_hood at right3
            mcfiona "Subtlety really isn't your strong suit, is it? Surely the point of the cards is to have an unexpected insight into the client."
            hide wllmc
            hide fiona
            show fiona hood_cu smirk_hood_cu at fiona_cu
            mb "My, aren't you impatient? Are you always the kind of girl who likes dessert before dinner?"

    hide fiona
    show wllmc coat grin behind fiona at centre:
        xoffset -20
    show fiona hood smirk_hood at right3
    mcfiona "Don't think you can butter over a blunder so easily, Fiona."
    show wllmc coat smirk
    mcfiona "If you can't give better insight than 'a woman on a train is traveling' I'm leaving."
    show fiona hood smile_hood
    mb "Well then look at this card."
    show wllmc coat embarrassed
    "She taps the Hanged Man, and my hand follows hers again, not-at-all-accidentally pressing my body closer to hers."
    show wllmc coat angry
    mcfiona "He looks pretty unhappy, poor man. Is that supposed to be a threat?"
    show fiona hood grin_hood
    "Fiona laughs and waves a hand."
    mb "No need to be afraid, [genericfn]. The Hanged Man is the card of contemplation."
    mb "What this tells me is that a tarot reading is just what you needed."
    show wllmc coat smirk
    mcfiona "Oh, of course. The cards themselves insist that I give you all my money, no doubt."
    show fiona hood smile_hood
    mb "No, that would be the six of pentacles."
    hide wllmc
    hide fiona
    show fiona hood_cu smile_hood_cu at fiona_cu
    "She dips her hand into the deck and pulls out the card, showing me the image of a king handing out gold to a crowd."
    hide fiona
    show wllmc coat smallsmile behind fiona at centre:
        xoffset -20
    show fiona hood smile_hood at right3
    mcfiona "Very pretty. But you realize you just showed me that your deck was stacked."
    show fiona hood smirk_hood
    mb "Or that the cards I need always come to my hand. I'm not the kind of girl who takes chances."
    show wllmc coat surprised
    "Against my better judgment, I find myself impressed."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Maybe she doesn't have to be subtle because she's just that good.)"
    hide wllmc
    show fiona hood_cu surprised_hood_cu at fiona_cu
    "Suddenly, Fiona stiffens, her gaze going blank and far away."
    hide fiona
    show wllmc coat surprised behind fiona at centre:
        xoffset -20
    show fiona hood surprised_hood at right3
    mcfiona "Something the matter?"

    hide wllmc
    hide fiona
    stop music fadeout 1.0
    play music wllspookymysterious1 fadein 1.0
    show fiona hood_cu sleep_hood_cu at fiona_cu
    "When she answers, her voice even sounds different, deeper and raspier."
    mb "Twelve locks have each their key, but the thirteenth is forced open."
    mb "Lightning on the horizon is the first warning of a sudden storm."
    hide fiona
    show wllmc coat_cu sad_cu at wllmc_cu
    "(Oh no! Is she having one of those episodes? Like John who lived down the street?)"
    show wllmc coat_cu surprised_cu
    "(Do I need to lay her on her side or put something soft in her mouth?)"
    hide wllmc
    show wllmc coat sad behind fiona at centre:
        xoffset -20
    show fiona hood surprised_hood at right3:
        pause 0.1
        easein 0.2 xoffset 20
    "I reach out and touch her shoulder, and Fiona jerks back into the moment."
    show wllmc coat surprised
    mb "The conductor is coming. And he looks furious."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Did she hear him? How good are her ears? I can't hear anything.)"
    hide wllmc
    show wllmc coat angry behind fiona at centre:
        xoffset -20
    show fiona hood surprised at right3:
        xoffset 20
    mcfiona "Well isn't that just the nine hells? It's possible he's after me for a, hmm, minor indiscretion."
    show wllmc coat surprised
    show fiona hood smirk_hood
    mb "Well in that case..."
    show fiona hood smile_hood
    "Her eyes drop to the table for a moment, and then she smiles."
    hide wllmc
    hide fiona
    show fiona hood_cu smirk_hood_cu at fiona_cu
    mb "You better kiss me quick, [genericfn]. And act like you really mean it."
    hide fiona
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Did she know what I wanted from the start?)"
    hide wllmc

    stop music fadeout 1.0
    play music wllromancelight2 fadein 1.0
    "But I don't even have time to think about the question before Fiona's lips are on mine."
    "My first impression is a heady waft of incense."
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(Does she {i}bathe{/i} in sandalwood?)"
    hide wllmc
    "Then I feel the delicious press of her soft lips against mine, and the brush of her thumb on my cheek."
    show wllmc coat_cu embarrassed_cu at wllmc_cu
    "(She certainly knows what she's doing. It's been a long time since I had a kiss this skillful.)"
    hide wllmc
    "I let myself sink into the pure pleasure of it, but as I do, everything shudders."
    show mc_instinct at full_size with dissolve:
        alpha 0.7
    hide mc_instinct with dissolve
    "A breeze whirls through the car, despite the closed window, and an electric shock lights me up from head to toe."
    show fiona hood_cu surprised_hood_cu at fiona_cu
    mb "Oh!"
    "I open my eyes and find her looking at me. She's all I can see, we're so close."
    show fiona hood_cu smirk_hood_cu
    mb "You've been holding out on me, [genericfn]. I should have known."
    mb "A kiss that electric doesn't come from nowhere."
    hide fiona

    $menuhideborder = True
    menu fionas1e1c3:
        "You felt it too?":
            $menuhideborder = False
            show wllmc coat surprised behind fiona at left1
            show fiona hood smirk_hood at right1
            mcfiona "You felt it too?"
            mb "The whole world must have felt that. People ten carriages down will be wondering why their hair just stood on end."
        "I don't know what you mean.":
            $menuhideborder = False
            show wllmc coat smirk behind fiona at left1
            show fiona hood smirk_hood at right1
            mcfiona "I have no idea what you mean. I'll take the compliment though."
            mb "Oh, you want to play it coy? Well by all means. But I'll figure you out sooner or later."
        "It's what people call chemistry.":
            $menuhideborder = False
            show wllmc coat smirk behind fiona at left1
            show fiona hood smirk_hood at right1
            mcfiona "I think it's what people call chemistry."
            mb "Really? Because I'd rather call it magic."

    hide wllmc
    hide fiona
    "She leans in and kisses me again, a tender press to the corner of my mouth just as the door opens."
    $sidecharone = "Conductor"
    sid1 "Oh, ah, oh, I'm sorry."
    show wllmc coat surprised at left1
    show fiona hood surprised_hood at right1:
        pause 0.1
        easein 0.4 right2
    "Fiona pulls away from me, just enough to look at the flustered official."
    hide fiona
    hide wllmc
    show wllmc coat_cu grin_cu at wllmc_cu
    "(You have to admire a woman who can make a grown man turn beet red just by raising an eyebrow at him.)"
    hide wllmc
    show wllmc coat basic behind fiona at left1
    show fiona hood surprised_hood at right2
    mb "Is there a problem?"
    hide wllmc
    hide fiona
    sid1 "Well, I'm afraid there is. Your, ah, companion has been accused of riffling through the other passengers' belongings."
    show wllmc coat_cu angry_cu at wllmc_cu
    "(Riffling? An insulting name for the deft sleight of hand I was performing.)"
    hide wllmc
    show wllmc coat smallsmile behind fiona at left1
    show fiona hood surprised_hood at right2
    mb "Oh sir, there must be some mistake. She's been in here with me this whole time."
    show fiona hood smile_hood
    "Fiona stokes a finger down my cheek."
    mb "And my sugar plum would never do anything like that. She's such a good girl."
    hide fiona
    hide wllmc
    show wllmc coat_cu grin_cu at wllmc_cu
    "(She should be grateful I have such a good poker face, because it's taking everything I have not to laugh.)"
    hide wllmc
    show wllmc coat smallsmile behind fiona at left1
    show fiona hood smile_hood at right2
    sid1 "Well, in that case, can I ask to see your tickets? Just so we can get this cleared up."
    show fiona hood grin_hood
    mb "Of course."
    show wllmc coat basic
    "I grab her arm, trying to signal silently."
    hide fiona
    hide wllmc
    show wllmc coat_cu sad_cu at wllmc_cu
    "(I don't have a ticket.)"
    hide wllmc
    show wllmc coat surprised behind fiona at left1
    show fiona hood grin_hood at right2
    "But Fiona reaches into her bag and pulls out two tickets, handing them over with a smile."
    hide fiona
    hide wllmc
    show wllmc coat_cu surprised_cu at wllmc_cu
    "(Wait, what? Why does she have two?)"
    hide wllmc
    show wllmc coat surprised behind fiona at left1
    show fiona hood grin_hood at right2
    mb "Oh sugar plum, look! Wisp Willow is coming up. You've never seen it before, have you?"
    show wllmc coat smile
    mcfiona "No, never, my darling."
    mb "Well then we should go get a better look! Leave the tickets on the seat when you're done, sir."
    hide wllmc
    hide fiona
    "She grabs my arm and pulls me out the door, down to the back of the train."
    show wllmc coat surprised behind fiona at left1plus
    show fiona hood basic_hood at right2
    mcfiona "What's going on?"
    show fiona hood smile_hood
    mb "We're admiring the picturesque view, of course."
    "She tucks her arm through mine and leans in close, her lips moving against my ear."

    scene bg_wll_train_station_sunset_nt at bg
    show fiona hood_cu smirk_hood_cu at fiona_cu
    with dissolve
    stop music fadeout 1.0
    play music wllaction1 fadein 1.0
    mb "Get ready to jump."
    mb "We have about thirty seconds before the conductor realizes those tickets are fake."

    scene wll_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

