label arianna_season1_episode6:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg msc_mc_bedroom_night_lights at bg
    play music mscsadtimes

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show arianna dress basic at right1plus
    show mscmc casual_hairdown basic at left1
    "Arianna sits on the bed next to me, her hand nudging my leg."
    ai sad "What's going on?"
    mcarianna angry "First it was stupid Hamish and now my content isn't good enough for this sponsorship deal."
    show mscmc sad
    ai "They said that?"
    mcarianna "My videos don't stand out."
    ai surprised "That's dumb. You're an amazing surfer! Your video content shouldn't change that."
    mcarianna "I'll be representing them, so I guess they can say whatever they want."
    hide arianna
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(Arianna and I are both jumping through hoops for our careers right now.)"
    show mscmc casual_hairdown sad at left1
    show arianna dress angry behind mscmc at right1plus
    ai "I'll help you, okay? We're not letting this ruin your chances of getting that sponsorship."
    show mscmc smile
    ai grin "We can come up with something."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    show mscmc grin
    show arianna surprised
    "There's a low grumble from Arianna's stomach and we both laugh."
    ai grin "But I...can't think on an empty stomach."
    hide mscmc
    hide arianna
    "Arianna's stomach demands food, so I order us a pizza and some beer."

    scene bg msc_mc_bedroom_night_lights at bg
    show arianna dress embarrassed at right1plus
    show mscmc casual_hairdown smile at left1
    with clockwise_wipe
    ai "So, you need to spice your stuff up basically?"
    show arianna sleep
    "Arianna bites the point off her slice, her can of beer in her other hand."
    show arianna surprised
    mcarianna grin "Right."
    show mscmc smile
    ai grin "Do, lik, a backflip off your board or something."
    show arianna basic
    mcarianna sad "It's more about the shots."
    mcarianna surprised "We could maybe get our hands on a drone for an aerial view?"
    ai sad "They're cool, but aren't they expensive?"
    mcarianna sad "For sure."
    show arianna basic
    "Arianna sets her pizza down and wipes off her hand."
    show mscmc smile
    ai grin "Let me see what you've got."
    hide mscmc
    hide arianna
    "She takes my phone and begins scrolling through my social media."
    show arianna dress surprised at right1plus
    show mscmc casual_hairdown smile at left1
    ai "Who takes most of your pictures? Trina?"
    show arianna basic
    mcarianna "Yeah, and sometimes I take some."
    show mscmc basic
    ai surprised "You need more of an aesthetic. It's kind of all thrown together."
    show mscmc embarrassed
    ai grin "Like, you're really talented and these don't properly showcase that."
    ai "You need some cooler poses too for your shots on the beach."
    show mscmc surprised
    ai embarrassed "You're adorable in every picture, I swear, but they're not looking for adorable."
    hide mscmc
    hide arianna
    "I sit silently as Arianna drags my social media."
    show mscmc casual_hairdown_cu basic_cu at mscmc_cu
    "(I never thought this would be something that I'd have to worry about so much.)"
    show arianna dress grin behind mscmc at right1plus
    show mscmc casual_hairdown basic at left1
    ai "I actually have an idea! What if I filmed you from under the water, or like, inside the wave you're riding?"
    ai "That could be some of the pizzaz they're looking for."
    mcarianna grin "I do have an underwater camera! That could actually work."
    ai embarrassed "And I'll make sure I get all of your angles."
    show mscmc embarrassed
    "She winks at me as she holds my phone out."
    mcarianna grin "We could do it tomorrow?"
    ai grin "Yeah! I can just work on my pieces afterwards."
    hide arianna
    show mscmc casual_hairdown_cu sad_cu at mscmc_cu
    "(I can't lose my sponsorship over something silly like my social media branding skils.)"

    stop music fadeout 0.5
    play music mscmctheme fadein 1.0
    show mscmc grin_cu
    "(This is gonna work.)"
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna glances past me and then a smirk grows on her face."
    ai grin_cu "Hey, get on the bed."
    hide arianna
    show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
    mcarianna "Why?"
    hide mscmc
    show arianna dress_cu grin_cu at arianna_cu
    ai "Stand up like you're surfing. We're practicing!"
    ai "Let me see your poses and smolder."
    show arianna dress grin at right1plus:
        transform_anchor True zoom 0.52 yoffset 72 xoffset -10
    "Arianna gets up and pats the bed, waiting for me."
    ai embarrassed "Sure it's not the same without you in that hot bikini, but I can imagine."
    hide arianna
    show mscmc casual_hairdown_cu grin_cu at mscmc_cu
    "I let out an awkward laugh."
    show mscmc embarrassed_cu
    "(She makes me feel like my mind is melting, yet she can say stuff like that with such confidence.)"
    mcarianna "Come on..."
    hide mscmc
    show arianna dress_cu surprised_cu at arianna_cu
    ai "What? You're hot and you know it. Now get on the bed."
    hide arianna
    show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
    mcarianna "I don't even know how to do poses."
    hide mscmc
    show arianna dress_cu smile_cu at arianna_cu
    "Arianna runs a finger down my arm."
    ai embarrassed_cu "Then I'll help you--I'll move you into poses."
    hide arianna

    $ menuhideborder = True
    menu ariannas1e6c1:
        "A. Hands-on pose practice with Arianna!" (paidchoice = "paidchoice"):
            $ menuhideborder = False
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "This is so embarrassing."
            hide mscmc
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "Less whining, more posing."
            hide arianna
            "I do as I'm told and get onto my bed, standing in my stance as if I'm surfing."
            "Arianna walks around the bed with her hand on her chin, nodding to herself."
            show arianna dress_cu smile_cu at arianna_cu
            ai "You look so stiff."
            hide arianna
            show mscmc casual_hairdown_cu basic_cu at mscmc_cu
            mcarianna "Probably because I'm fake surfing."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            ai "With that kind of attitude, you're never gonna get the sponsorship."
            ai grin_cu "Now, work it!"
            show mscmc casual_hairdown grin at left1
            show arianna dress smile at right2
            "With a defeated laugh, I strike a flashier pose for Arianna--even getting my arms into it."
            show mscmc smile
            show arianna:
                easein 0.5 yoffset 140
            "She crouches down and pretends to take a picture with her hands."
            ai grin "In many ways, the work of a critic is easy."
            mcarianna grin "This good enough?"
            ai embarrassed "You're definitely a babe."
            show mscmc embarrassed
            "I roll my eyes to stave off the oncoming blush."
            mcarianna "Is that the only criteria?"
            ai grin "For me it is."
            hide mscmc
            show arianna dress_cu basic_cu at arianna_cu:
                yoffset 0
            "Arianan tilts her head at me, actually looking like she's thinking for real."
            ai smile_cu "I'll be able to get some really cool shots under the water."
            ai grin_cu "I'm thinking a rotating shot from inside the wave as you catch it."
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "So you'll just be spinning underneath me?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Try not to hit me."
            show mscmc casual_hairdown basic at left1
            show arianna dress smile at right2
            "Arianna drops her fake camera and holds her hand up to me."
            ai grin "Okay, not get down here."
            mcarianna surprised "Done already?"
            ai "Neptune, no. We're just getting started! I want to see some land poses."
            show arianna:
                easein 0.4 right1plus
            show mscmc smile:
                easein 0.4 xoffset 30
            "Arianna helps me off the bed, but doesn't let go of my hand."
            show mscmc embarrassed
            show arianna:
                easein 0.5 xoffset -20
            "Instead, she directs it to my hip, her fingers slowly dragging across my skin as she pulls away."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu:
                xoffset 0
            "She stands in front of me, looking down with half-lidded eyes and her lips parted."
            ai grin_cu "You look like a supermodel."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            mcarianna "You're the one who looks like a supermodel."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "I want to keep her gaze, but I know that I won't be able to speak if I do."
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "You're tall and elegant and gorgeous."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            "Arianna's hand comes up underneath my chin, tilting my head back up."
            ai embarrassed_cu "You really think I'm gorgeous?"
            hide arianna
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            "(Say something good! Don't panic!)"
            mcarianna embarrassed_cu "...yes."
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            ai "Well, I think you're like the sun rising over the ocean. A sky that's blue and orange."
            ai embarrassed_cu "And every morning I see you, you take my breath away."
            hide arianna
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mcarianna "How am I supposed to compete with that?"
            show mscmc casual_hairdown embarrassed at left1:
                xoffset -20
            show arianna dress grin behind mscmc at right1plus:
                xoffset -50
                pause 0.1
                easein 0.5 xoffset 0
            "Arianna laughs and backs up."
            ai smile "Put your other hand behind your head--kind of gripping your hair."
            show mscmc smile
            show arianna grin
            "I do what she says and she grins, using her finger camera again."
            show mscmc embarrassed
            ai "Now rest your weight on your left leg."
            "Arianna performs her fake photoshoot, getting every possible angle that she can."
            show mscmc smile
            ai "I do have one last request."
            show arianna smile
            mcarianna grin "Shoot."
            ai grin "Would you lay on the bed?"
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu:
                xoffset 0
            "(Saying yes to this practice session falls under the best and worst choices I've ever made.)"
            "(Worst because I don't know how much more my heart can take of Arianna looking at me like this.)"
            hide mscmc
            show arianna dress smile at centre
            "Arianna bites on the nail of her thumb as I climb back onto my bed."
            ai grin "Scooch down a little. I don't want your whole head on the pillows."
            hide arianna
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "I stare up at the ceiling, folding my hands over my stomach as I listen to my heartbeat."
            hide mscmc
            show arianna dress_cu smile_cu at arianna_cu
            ai "Do something else with your hands."
            hide arianna
            "The bed creaks and Arianna climbs over top of me."
            show mscmc casual_hairdown_cu surprised_cu at mscmc_cu
            mcarianna "Like what?"
            hide mscmc
            "My mouth is dry as she straddles me, moving my arms to either side of my head."
            show arianna dress_cu embarrassed_cu at arianna_cu
            ai "Like that."
            hide arianna
            "Arianna takes another fake picture."
            show arianna dress_cu grin_cu at arianna_cu
            ai "I think that's enough practice for today."
            hide arianna
            show mscmc casual_hairdown_cu grin_cu at mscmc_cu
            mcarianna "Get everything you need?"
            hide mscmc
            show arianna dress_cu grin_cu at arianna_cu
            "Arianna brushes her hair behind her ears and smiles with a nod as she rolls away."
            ai embarrassed_cu "And then some."
            hide arianna
            stop music fadeout 0.5
            play music mscromance fadein 1.0
            "She breaks the tense atmosphere with a loud hum."
            show arianna dress grin at right1plus
            show mscmc casual_hairdown basic at left1
            ai "Look, that company would be stupid to not take you."
            show arianna basic
            mcarianna sad "I hope so."

        "B. You're too embarrassed.":
            $ menuhideborder = False
            show mscmc casual_hairdown_cu embarrassed_cu at mscmc_cu
            "(It would be so embarrassing to do this right now especially knowing how she's looking at me.)"
            show mscmc casual_hairdown sad at left1
            show arianna dress basic behind mscmc at right1plus
            mcarianna "We don't need to practice for pictures, right? Besides, I'm so tired."
            show mscmc basic
            ai surprised "Too tired to stand on your bed?"
            show arianna basic
            mcarianna sad "Yes..."
            show mscmc smile
            ai smile "Alright, no worries."

    hide arianna
    hide mscmc
    "A yawn from Arianna tells me that it's time for lights out."
    "Arianna gets on her respective side of the bed as I hit the lights."
    scene bg msc_mc_bedroom_night at bg
    show arianna dress_cu smile_cu at arianna_cu
    ai "Sweet dreams, [genericfn]."

    stop music fadeout 0.5
    play music mschappytimes fadein 1.0
    scene bg msc_beach_bar_day at bg with fade
    "The next morning, Arianna and I are at Jerry's for breakfast."
    show arianna dress surprised at right1plus:
        xoffset 20
    show mscmc jacket_hairdown smile at left1
    ai "After you ate the sun, all this light started pouring out of your eyes and mouth."
    ai "It was kinda really beautiful? But you also ended up burning the whole world."
    show arianna smile
    mcarianna grin "Are your dreams always so...exciting?"
    ai grin "No. I'm usually just really confused."
    mcarianna sad "I don't remember, like, any of my dreams."
    ai sad "I feel like you're somebody who has stress dreams about school even though you're out of school."
    mcarianna "They always take place in math class."
    ai "That's rough."
    hide mscmc
    hide arianna

    stop music fadeout 0.5
    play music mscantagonist fadein 1.0
    play sound phone_ringing
    "My phone rings and fear for my sponsorship makes my heart stop."
    "But it's actually worse than Phil from High Tide."
    show arianna dress basic at right1plus:
        xoffset 20
    show mscmc jacket_hairdown surprised at left1
    mcarianna "It's Emporia!"
    show arianna surprised
    "Arianna nearly chokes on the smoothie she's slurping."
    show arianna basic
    mcarianna smile "Hello, this is [genericfn] speaking."
    hide arianna
    hide mscmc
    "There's a sharp breath on the other end."
    bn "I need to speak with Arianna."
    show mscmc jacket_hairdown_cu basic_cu at mscmc_cu
    "(Would it kill her to say hello? At least pretend to be nice.)"
    show arianna dress basic behind mscmc at right1plus:
        xoffset 20
    show mscmc jacket_hairdown smile at left1
    mcarianna "One moment."
    show mscmc basic
    "I put my hand over the phone and pull it away from me."
    mcarianna surprised "She wants to talk to you."
    show mscmc basic
    ai sad "Okay."
    show arianna basic
    "Putting the phone on speaker, I set it between us."
    ai grin "Hi, Emporia. What's up?"
    hide arianna
    hide mscmc
    bn "I haven't been able to sleep knowing you might disappoint me again with one of the other pieces."
    bn "This first piece is too bright. It nearly hurts my eyes to look at it."
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(She is such a bitch for no reason!)"
    hide mscmc
    bn "Did you spray this with paint?"
    show arianna dress surprised at right1plus:
        xoffset 20
    show mscmc jacket_hairdown basic at left1
    ai "No, it's just the metal I use. It's a softer metal, so it's easier to work with."
    ai "I could use a different material if that's what you want."
    hide arianna
    hide mscmc
    bn "No, I like the material, it's just too shiny for me."
    show arianna dress surprised at right1plus:
        xoffset 20
    show mscmc jacket_hairdown basic at left1
    ai "It's really not that shiny. It's actually pretty dull in comparison to.."
    hide arianna
    hide mscmc
    bn "Then paint over it."
    show arianna dress sad at right1plus:
        xoffset 20
    show mscmc jacket_hairdown basic at left1
    ai "It doesn't hold paint well but..."
    show mscmc angry
    "I can hear the distressed irritation in Arianna's voice."
    hide arianna
    show mscmc jacket_hairdown_cu sad_cu at mscmc_cu
    "(if it were me, I'd probably just hang up. I wouldn't be able to work with this woman.)"
    hide mscmc
    bn "But I am your client, am I not? I'm paying you to do as I ask."
    bn "And so you shall do as I ask. Correct?"
    show arianna dress sad at right1plus:
        xoffset 20
    show mscmc jacket_hairdown sad at left1
    "Arianna bites down on her bottom lip and rolls her eyes at me."
    show mscmc angry
    ai "...yeah."
    hide arianna
    hide mscmc
    bn "Good, now then, did you get enough sleep last night?"
    show mscmc jacket_hairdown_cu surprised_cu at mscmc_cu
    "(Why does that matter?)"
    show arianna dress sad behind mscmc at right1plus:
        xoffset 20
    show mscmc jacket_hairdown sleep at left1
    ai "Uh, I think so."
    hide arianna
    hide mscmc
    bn "Have you been eating well? What do you usually eat in a day?"
    show arianna dress sad at right1plus:
        xoffset 20
    show mscmc jacket_hairdown angry at left1
    ai "I'm a little confused--what does this have to do with my work?"
    hide arianna
    hide mscmc
    bn "It has everything to do with the work!"
    "Emporia's voice raises."
    bn "How can you make good pieces if you're malnourished or sleep deprived?"
    bn "A healthy body and healthy mind is a necessity"
    bn "I'll have my people send you a regiment to follow."
    bn "What vitamins to take and when to work out and such. That should help."
    show arianna dress sad at right1plus:
        xoffset 20
    show mscmc jacket_hairdown sad at left1
    ai "I don't really think that's-"
    hide arianna
    hide mscmc
    bn "Nonsense. This is very important to me and it should be to you as well."
    show arianna dress sad at right1plus:
        xoffset 20
    show mscmc jacket_hairdown sad at left1
    "I shake my head at Arianna and she nods in agreement."
    hide arianna
    show mscmc jacket_hairdown_cu angry_cu at mscmc_cu
    "(This is insane! Emporia might be paying Arianna, but she doesn't own her.)"
    show arianna dress angry behind mscmc at right1plus:
        xoffset 20
    show mscmc jacket_hairdown sad at left1
    ai "Yeah. Sure. Alright."
    hide arianna
    hide mscmc
    "Emporia seems to let out a sigh."
    bn "Good. Well, I'll let you get back to work. Have a nice day."
    "The line goes dead."

    $ menuhideborder = True
    menu ariannas1e6c2:
        "A. What the hell?":
            $ menuhideborder = False
            show arianna dress sad at right1plus:
                xoffset 20
            show mscmc jacket_hairdown surprised at left1
            mcarianna "Um, what the hell was that about?"
            mcarianna angry "She's nuts!"
            show mscmc sad
            ai "I'm just as shocked as you are."

        "B. You are not doing that.":
            $ menuhideborder = False
            show arianna dress sad at right1plus:
                xoffset 20
            show mscmc jacket_hairdown angry at left1
            mcarianna "You are not doing that. I should call her back and tell her."
            ai basic "Look, there's no way I would follow her stupid regiment."
            show mscmc sad
            ai sad "Just trying to keep the peace."

        "C. Do you want to keep working with her?":
            $ menuhideborder = False
            show arianna dress sad at right1plus:
                xoffset 20
            show mscmc jacket_hairdown sad at left1
            mcarianna "Do you even want to keep working with her?"
            mcarianna angry "She's a nightmare."
            show mscmc sad
            ai basic "I need this."

    show arianna sad
    mcarianna angry "I don't like her."
    ai "And you think I do?"
    mcarianna "There's something off about her. She's...creepy towards you."
    show arianna smile
    show mscmc basic
    "Arianna puts an assuring hand over mine."
    ai grin "Look, I know and I hate this as much as you, but I'm getting it done."
    ai "I'll finish the pieces, get paid, and never talk to her again."

    stop music fadeout 0.5
    play music mscaction fadein 1.0
    scene bg msc_boardwalk_day_people at bg with clockwise_wipe
    "After my surf lessons for the kiddies end for the day, I head back to the surf shop."
    "I left Arianna at home with a movie while I had to work."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(I wonder what she thinks about vampires? Are sirens the mermaid equivalent of vampires?)"
    show mscmc smile_cu
    "(And would she be a mermaid werewolf because she can turn into a human?)"
    show mscmc grin_cu
    "(I'll see what she has to say when I'm home.)"
    show mscmc surprised_cu
    "(Wait, shit, did I leave my keys back there?)"
    hide mscmc
    "I stop to dig into my bag, having no memory of putting my keys away."
    show mscmc surfer_hairup grin at centre
    mcarianna "Thank god."
    hide mscmc
    "Seeing my keys fills me with relief as I pull them out, but then they slip out of my hands."
    "Luckily, they don't go far and as I bend down to grab them, I see Maxime standing below the boardwalk on the sand."

    $ menuhideborder = True
    menu ariannas1e6c3:
        "A. Say hi.":
            $ menuhideborder = False
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(I wonder if he's on his way to one of his lessons.)"
            hide mscmc
            "I'm about to call out to him when I realize he's standing with someone else."
        "B. Keep walking.":
            $ menuhideborder = False
            show mscmc surfer_hairup_cu sad_cu at mscmc_cu
            "(I don't want to bother him. He always seems busy when I see him.)"
            hide mscmc
            "I grab my keys and stand, but another voice catches my attention."
        "C. See what he's up to.":
            $ menuhideborder = False
            "Not that I'm in the business of spying, but I do want to know what he's up to."
            show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
            "(What does Maxime do in his free time? I know nothing about him.)"
            hide mscmc
            "But it seems like he's not alone."

    stop music fadeout 0.5
    play music msctense fadein 1.0
    show maxime casual sad at left2
    show camilla casual basic at right2
    "A woman that I've never seen before is standing close to him."
    hide maxime
    hide camilla
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(He has a girlfriend? No way! I have to tell Trina.)"
    hide mscmc
    show maxime casual sad at left2
    show camilla casual basic at right2
    mx "Camilla, we'll get this sorted."
    hide maxime
    hide camilla
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Are they fighting? This is awkward and definitely not something I should watch.)"
    hide mscmc
    "Keys in hand, I start to slink away."
    hide mscmc
    show maxime casual basic at left2
    show camilla casual angry at right2
    cm "We exile mermaids for the better, not to make things worse!"
    hide maxime
    hide camilla
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Huh?!)"
    hide mscmc
    "I freeze."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(She just said mermaids. With a straight face. To Maxime!)"
    hide mscmc
    show maxime casual basic at left2
    show camilla casual angry at right2
    mx "I know that the exile is in the area. She's not far."
    show maxime sad
    cm "Mia Diplore loose in human territory. Could it be any worse?"
    hide maxime
    hide camilla
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Human territory...are they not human?)"
    "(And who the hell is Mia Diplore?!)"
    hide mscmc
    show maxime casual sad at left2
    show camilla casual angry at right2
    cm "She's dangerous, Maxime. Who knows what she'll do?"
    mx angry "Mia can't hide forever--it's not in her nature. We'll find her soon."
    show maxime basic
    cm "Shes's made a mockery of us in the mer government. We can't catch {i}one{/i} exile!"
    hide maxime
    hide camilla
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Mer government? Maxime is a member of the mer government?)"
    show mscmc sad_cu
    "My stomach knots."
    show mscmc surprised_cu
    "(So he's a mermaid too...Does Arianna know him? Does he know Arianna?)"
    show mscmc sad_cu
    "I feel like my head is spinning."
    "This is somehow more shocking than when Arianna told me she was a mermaid."
    "(So when Maxime asked me if I'd seen anyone strange, he meant this Mia Diplore person?)"
    "(What if he knows I know about mermaids? Would that get Arianna in trouble?)"
    hide mscmc
    show maxime casual basic at left2
    show camilla casual angry at right2
    cm "We need to act fast. We don't have time to waste."
    cm "So while you finish your {i}surfing{/i} lessons, I'll keep looking."
    show camilla sad
    "Camilla lets out a heavy sigh, her gaze suddenly turning towards me."
    hide maxime
    hide camilla
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Crap!)"
    show mscmc surfer_hairup basic at centre
    "I jump back, pretending like I was looking at anything but them."
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Thank god Maxime didn't see me--I need to tell Arianna!)"

    scene bg msc_surf_shop_day at bg with fade
    "When I get back to the shop, I'm glad to see that Trina isn't around."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(What the hell did I just overhear?)"
    hide mscmc
    "I lean against the door and blow out a long breath."
    show mscmc surfer_hairup_cu sad_cu at mscmc_cu
    "(Maxime. Mia Diplore.)"
    hide mscmc
    play sound phone_vibrating
    "My phone buzzes in my pocket--it's a text from Arianna asking if there's a sequel to the movie."
    "Below the text, there's a notification from my word scramble app."
    "It says that I haven't hit my words found goal for the day."
    show mscmc surfer_hairup_cu surprised_cu at mscmc_cu
    "(Words found...)"
    "The name Mia Diplore echoes in my mind."
    show mscmc angry_cu
    "(It sounds kind of familiar. I'm missing something here.)"
    show mscmc sad_cu
    "(Strange women. Emporia Lid. Mia Diplore. Scrambled letters.)"
    mcarianna surprised_cu "Emporia Lid!"
    "I put my hand over my mouth."
    "(It's an anagram for Mia Diplore!)"

    scene bg msc_msctbc at bg with fade
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
