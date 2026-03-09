label korin_season1_episode12:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_generic_office_on at bg
    play music ecmupbeateveryday3

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    show ecmc jacket_v2 pin basic at left3
    show enver casual basic at right2
    mckorin "I manage to grab Enver at break."

    show ecmc jacket_v2 pin surprised
    mckorin "Hey! Where's Korin?"
    "He shrugs."
    en "That little bird of hers is getting our messages but she isn't responding."
    hide enver
    hide ecmc

    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(Baby bird? I wonder if it's acting up again.)"
    hide ecmc

    show enver casual basic at right2
    show ecmc jacket_v2 pin determined at left3
    en "She messaged me late last night and asked me to cover training for her today, but I haven't heard from her since."
    mckorin "Well...isn't anyone worried about her?"

    show enver casual sad at right2
    "Enver frowns at me."
    en "Okay, what's this really about?"

    show ecmc jacket_v2 pin sad at left3
    mckorin "Nothing! Except, you know, she seemed kind of weird last night..."

    show enver casual angry at right2
    "Enver's eyes go wide."
    en "Last night?! Did you guys--?!"

    show ecmc jacket_v2 pin surprised at left3
    mckorin "NO! Oh my god! Please keep your voice down! We just went out for drinks."

    show ecmc jacket_v2 pin sad at left3
    mckorin "She just seemed kind of rattled by the whole Anton thing. More rattled than me..."

    show enver casual sad at right2
    en "Well then, it sounds like you have your answer."

    show ecmc jacket_v2 pin angry at left3
    "I glare at him."
    en "Dom might know for sure what's up with her."

    show ecmc jacket_v2 pin surprised at left3
    mckorin "You're suggesting I talk to Dom?"

    show enver casual angry at right2
    en "WHAT? Nooo way! Aren't you listening?"

    show ecmc jacket_v2 pin sad at left3
    mckorin "I mean...you don't think..."

    show enver casual basic at right2
    "Enver patiently waits for me to spit it out."
    mckorin "I should...message her?"

    show enver casual angry at right2
    "Enver throws his hands up into the air."

    show enver casual smile at right2
    en "Now she gets it!"
    mckorin "If she's not responding to others, she's probably not going to respond to me..."

    show enver casual sad at right2
    "Enver rubs his temples."
    en "Look, if I weren't filling in for Korin today, I'd love to bat this back and forth with you all day. But I really don't have the time to."
    en "My advice for you, as your friend--and hell, even as your instructor!"

    show enver casual smile at right2
    en "Whatever you're thinking about doing? Just do it! Check in with her! Show her you care!"

    show ecmc jacket_v2 pin surprised at left3
    mckorin "What if I'm bugging her? What if she wants this time to herself?"
    en "Then she'll tell you that. Why are you being so weird about this?"
    mckorin "Because..."

    show ecmc jacket_v2 pin sad at left3
    "I wince."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(I really like her. And I think she likes me back.)"
    hide ecmc

    show enver casual smile at right2
    show ecmc jacket_v2 pin sad at left3
    "I can't quite tell if Enver can read everything on my face alone, but he seems to understand some of it."

    show enver casual basic at right2
    en "Okay. Real Talk: I know the two of you pretty well separately."
    en "And I've only seen little snippets of the two of you when you're together, but..."

    show enver casual sad at right2
    "He puts his hands out, shrugging."
    en "There's sparks there, okay?"

    show enver casual smile at right2
    en "So if you care about Korin, but you're afraid to say it, you don't have to {i}tell{/i} her."
    en "But you should {i}show{/i} her."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu pin_cu determined_cu at ecmc_cu
    "(I should. He's right. I defintely should.)"
    hide ecmc

    show enver casual smile at right2
    show ecmc jacket_v2 pin sad at left3
    en "Oh and, by the way...she's defintely single"

    $menuhideborder = True
    menu korins1e12c1:
        "A. So am I.":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left3
            show enver casual smile at right2
            mckorin "So am I."
            en "Uh. Yeah. That's why I mentioned it."

        "B. Are you sure?":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left3
            show enver casual smile at right2
            mckorin "Are you sure?"
            en "With how much she's been asking me lately to set her up with one of my friends, it'd be pretty weird if she wasn't."
            en "And the only friend left that I haven't set her up with is...you!"

        "C. Who asked?":
            $menuhideborder = False
            show ecmc jacket_v2 pin surprised at left3
            show enver casual smile at right2
            mckorin "Who asked? I didn't."
            en "Well, now you don't have to! You're welcome."

    show ecmc jacket_v2 pin embarrassed at left3
    mckorin "Whatever. I don't know why that information would matter to me."
    en "Look, I don't really care if you lie to me about all this...but what good is it doing you to lie to yourself?"

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu pin_cu embarrassed_cu at ecmc_cu
    "(Okay...he might have a point there.)"
    hide ecmc

    show enver casual basic at right2
    show ecmc jacket_v2 pin determined at left3
    "Before I can talk myself out of it, I pull open my ARCware in front of him and shoot Korin a quick message."
    mckorin "Just checking in to see how you're doing."

    hide enver
    hide ecmc
    show ecmc jacket_v2_cu pin_cu embarrassed_cu at ecmc_cu
    "(I miss you...)"
    hide ecmc

    show enver casual basic at right2
    show ecmc jacket_v2 pin surprised at left3
    "I breathe out and turn to say something to Enver, when I get a response right away."

    show enver casual smile at right2
    "Enver puts a hand to his mouth, covering up a knowing grin at me."

    show ecmc jacket_v2 pin smile at left3
    ko "Hey! Glad you reached out. I'm taking a personal day to process some things."
    ko "If you feel like you need that too, let me know and we can meet up..."
    "I look up at Enver who is already packing my things into my bag."
    en "Okay, you're excused. Go. Go!"

    scene bg ecm_elysian_park_day at bg with dissolve
    stop music fadeout 1.0
    play music ecmemotional3

    show korin casual basic at centre
    "I meet Korin at the park and find her sitting on a bench overlooking the city."

    show korin casual basic at right3
    show ecmc jacket_v2 pin smile at left3
    mckorin "Hey!"
    ko "Hey..."
    show ecmc jacket_v2 pin basic at slowcentre
    "I sit on the bench next to her, and she beckons me closer, scooting my way herself."

    hide ecmc
    hide korin
    show korin casual_cu sad_cu at korin_cu
    "And up close, I can see she looks...tired."
    "I put a hand on her shoulder and look into her eyes."
    hide korin

    show korin casual sad at right3
    show ecmc jacket_v2 pin sad at centre
    mckorin "Hey...I was worried about you. Enver said you weren't responding to people's messages."
    mckorin "What's going on?"

    show korin casual sleep at right3
    "Korin collects herself before answering."

    show korin casual basic at right3
    ko "I think that...finding out a fellow D.I.V.A.A agent was a serial killer kind of shook me up."

    show ecmc jacket_v2 pin determined at centre
    mckorin "{i}Allegedly{/i} a serial killer."

    show korin casual surprised at right3
    ko "But all the evidence he was trying to hide--"

    show ecmc jacket_v2 pin smile at centre
    mckorin "I know. I'm kidding!"

    show korin casual smile at right3
    "Korin looks at me incredulously, then laughs."
    ko "How are {i}you{/i} not rattled by all this?"

    show korin casual surprised at right3
    ko "How are you still working? Still functioning? Don't you think you need a break?"

    show ecmc jacket_v2 pin determined at centre
    mckorin "I think...maybe the gravity of it hasn't caught up with me yet."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu embarrassed_cu at ecmc_cu
    "(And it's a lot easier for me to be worried about you than to worry about myself.)"
    hide ecmc

    show korin casual surprised at right3
    show ecmc jacket_v2 pin determined at centre
    ko "I mean jeez, I realized I couldn't keep my 'trainer' face on today, so I had to get away..."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(She's not wearing a mask right now...)"
    hide ecmc

    show korin casual sad at right3
    show ecmc jacket_v2 pin determined at centre
    "I look down at her hand, which is curled over mine."
    ko "It was just too much for me to deal with right now."

    show ecmc jacket_v2 pin sad at centre
    mckorin "Is me being here to much, too?"

    show korin casual surprised at right3
    ko "No. I'm glad you're here."
    ko "Part of the reason I'm having trouble is because...well..."

    show korin casual sad at right3
    show ecmc jacket_v2 pin sad at centre
    ko "It was really hard seeing you in so much danger. When people close to me are in trouble..."
    "She winces."
    ko "Not that you and I are...I mean...we're not..."
    "I give her hand a squeeze."
    mckorin "I think recent circumstances have given us the opportunity to grow kind of close in a short amount of time."
    "Korin takes in my words, then nods in agreement. Then, she looks worried again."
    ko "If this is too much for a...I mean, I'm supposed to be your instructor..."
    mckorin "But you said that mask was staying off today."

    show ecmc jacket_v2 pin sad at centre
    mckorin "I didn't come here as a D.I.V.A.A. trainee. I came here as your friend."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
    "(It seems like there's something deeper going on with her here...)"
    hide ecmc

    show korin casual sad at right3
    show ecmc jacket_v2 pin smile at centre
    mckorin "So if there's anything you want to get off your chest, I'm all ears."

    hide ecmc
    hide korin
    show korin casual_cu smirk_cu at korin_cu
    "Korin looks at me, gratitude in her expression...but she still seems guarded."
    ko "There are some things I'd like to talk about."

    show korin casual_cu sad_cu at korin_cu
    ko "Some of it's really personal, and I don't even know how much I'll be able to get out."
    ko "But I don't want to burden you..."
    hide korin

    $menuhideborder = True
    menu korins1e12c2:
        "A. Listen to Korin talk about her feelings." (paidchoice = "paidchoice"):
            $menuhideborder = False
            show korin casual sad at right1
            show ecmc jacket_v2 pin smile at left1
            mckorin "Korin...you can talk to me."
            mckorin "You've been so supportive of me for so long. I want to give back for once."

            show korin casual smile at right1
            "Korin shakes her head, laughing."
            ko "You actually don't know how helpful you've been to me. When we're together, I feel like..."

            show korin casual sleep at right1
            "She takes a deep breath and starts over."

            show korin casual basic at right1
            show ecmc jacket_v2 pin determined at left1
            ko "I don't want you to think I supported you out of obligation to your dad, or anything like that."

            show korin casual sad at right1
            ko "That might be how it started out, but..."
            "I nod."

            show ecmc jacket_v2 pin smile at left1
            mckorin "You're a naturally caring person, Korin. It's one of the things I like most about you."
            mckorin "You make people feel seen. Like they belong. Like they have worth. You make {i}me{/i} feel that way."

            show ecmc jacket_v2 pin sad at left1
            "My stomach flips as I see Korin's lip tremble. "
            ko "There are things about my life that the people I work with don't know."
            ko "Dom knows...but only because he's my boss."
            mckorin "What about your family? Do they know?"

            hide ecmc
            hide korin
            show korin casual_cu sad_cu at korin_cu
            "She's quiet for a long time. Then, she slowly shakes her head."
            ko "No. They don't."
            ko "I didn't even tell your dad. Sometimes I think I should have, and sometimes I think he knew, but we never talked about it."
            ko "I'll just say that..."
            ko "These things that have happened, they make me worry too much about the people close to me."
            ko "And it's made it really hard for me to get close to people..."
            ko "Because I'm afraid of what might happen to me if something bad happens to them."

            show korin casual_cu surprised_cu at korin_cu
            ko "Does that make sense?"
            hide korin

            show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
            "(It makes it hard for her to get close to people?)"
            hide ecmc

            show korin casual surprised at right1
            show ecmc jacket_v2 pin surprised at left1
            mckorin "But...you're one of the most friendly people I've ever met."

            show korin casual smirk at right1
            "She sits up, smiling sadly."

            show ecmc jacket_v2 pin determined at left1
            ko "Yeah, I am. And It's sincere. But I'm not {i}close{/i} with anyone."

            show korin casual sad at right1
            ko "The advantage of being warm to everyone I meet is that few people try to look deeper, you know?"
            "I nod, getting it."
            mckorin "When people only see your good side, it seems like your only side."

            show korin casual smile at right1
            "Korin Laughs."
            ko "See, that's exactly what I'm talking about. After I got to know you, it felt like..."
            ko "It felt like you could see all sides of me. Just by looking."

            show ecmc jacket_v2 pin embarrassed at left1
            mckorin "And that scares you?"

            show korin casual surprised at right1
            ko "It..."
            "She holds back her answer so long that I can't tell if she ever knew it in the first place."

            show korin casual sad at right1
            ko "I don't even know if I'm ready to talk about it now."
            ko "And it's not because I don't want to share these things with you. I do, it's just..."

            hide ecmc
            hide korin
            show korin casual_cu sad_cu at korin_cu
            "She rakes a hand through her hair, and looks away from me, and I think I see the shine of tears in her eyes."
            ko "It's a lot of things. Not only that am I unsure if I can even talk about it yet, but..."
            ko "You know...if I'm leaning on you too much..."
            hide korin

            show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
            mckorin "Korin?"
            hide ecmc

            show korin casual_cu surprised_cu at korin_cu
            "She looks sheepishly at me."
            hide korin

            show ecmc jacket_v2_cu pin_cu sad_cu at ecmc_cu
            mckorin "I think it's been a long time since you leaned on anybody."

            show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
            mckorin "And me being here today... that's me, telling you that it's okay for you to lean on me."
            hide ecmc

            show korin casual_cu sad_cu at korin_cu
            "I put a hand on her arm, and a soft thrill buzzes through me when she bends into my touch."
            "I naturally shift, and she lets her head fall on my shoulder"
            ko "Is this okay?"
            hide korin

            show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
            mckorin "Yeah. It is."
            hide ecmc

            "I relax and let my cheek rest on the top of her head."

            show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
            "(Oh my god, her hair. It's so soft...)"

            show ecmc jacket_v2_cu pin_cu angry_cu at ecmc_cu
            "(Okay!! Not what I'm here for. I'm here to support Korin!)"

            show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
            mckorin "And it's okay. You don't have to tell me anything until you're ready."
            hide ecmc

            show korin casual_cu smirk_cu at korin_cu
            ko "Thanks for being patient with me."

            show korin casual_cu sad_cu at korin_cu
            ko "I want to tell you more, but...for my sake, I need to take it slow right now."
            hide korin

            show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
            mckorin "Okay. Just know...I'm ready to hear you out whenever you are."
            hide ecmc

            "We stay like that for some time. Korin leans on me, and together we watch people pass by."
            "When she finally sits up, she looks considerably more cheerful."

        "B. Shut the conversation down.":
            $menuhideborder = False

            show korin casual sad at right1
            show ecmc jacket_v2 pin sad at left1
            mckorin "It seems like you've got a lot to process still. And I don't want to pry..."

            show korin casual surprised at right1
            ko "It's not prying! It's..."

            show korin casual basic at right1
            ko "It's okay. But if you want to ask me about it later, please don't hesitate."
            hide korin
            hide ecmc

    show korin casual_cu smile_cu at korin_cu
    ko "Well, since we have the rest of the day to ourselves, you want to go walk around the rest of this park?"
    ko "And then maybe we could go explore the city a bit. I was going to go down to the marina later and watch the sunset..."

    hide korin
    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    mckorin "I think that sounds like the perfect way to spend our day."

    scene bg ecm_marinadelrey_sunset at bg with wiperightdissolve
    stop music
    play music ecmcalmeveryday4

    "At sunset, Korin and I make our way down to the marina. Seagulls soar overhead as we stroll down the boardwalk."
    show korin casual basic at right1plus
    show ecmc jacket_v2 pin smile at left1plus
    "My legs are tired from all the walking, and my voice is weary from all our talking...but I'm happier than I've felt in a long time"
    mckorin "I can't believe we just...skipped work the whole day."

    show korin casual smirk at right1plus
    ko "Hey, I think we deserve it, considering the circumstances."
    "She looks around at all the boardwalk shops."
    ko "You know what else I think we deserve? Boba tea."
    "She stops at one of the stalls and orders one for each of us."

    show korin casual smile at right1plus
    "As we stroll on, sipping happily away, Korin looks sideways at my cup."
    ko "What kind did you get, again? I want to try yours."

    $menuhideborder = True
    menu korins1e12c3:
        "A. Sure, go ahead.":
            $menuhideborder = False
            show korin casual basic at right1plus
            "I hand her my cup and she takes a sip."

            show korin casual smile at right1plus
            ko "Mm, what is this? I've never tried it before..."

            show ecmc jacket_v2 pin surprised at left1plus
            mckorin "Taro Flavor. You've never had it before?"

        "B. Only if I get to try yours!":
            $menuhideborder = False
            mckorin "Only If i get to try yours!"
            ko "Fine!"

            show korin casual basic at right1plus
            show ecmc jacket_v2 pin determined at left1plus
            "We hand off cups. Hers is sweet and bright, with lychee jelly at the bottom."
            mckorin "...I think I like yours better."
            show korin casual smile at right1plus
            ko "I was gonna say the same. Let's trade!"

        "C. What?! Get your own!":
            $menuhideborder = False

            show ecmc jacket_v2 pin surprised at left1plus
            mckorin "What?! No way, you get your own--"

            show korin casual sleep at right1plus
            "Before I can react, Korin leans over and takes a sip straight out of my cup. My jaw drops."

            show korin casual smile at right1plus
            mckorin "Boba thief!!"
            ko "Guilty! Mm, that's pretty good, though..."

            show ecmc jacket_v2 pin smile at left1plus
            "I extend my arm far on the other side to keep her from grabbing another drink. We both break down laughing."

    show ecmc jacket_v2 pin surprised at left1plus
    show korin casual smile at right1plus
    ko "You didn't have any trouble getting the day off, did you?"

    show ecmc jacket_v2 pin smile at left1plus
    mckorin "No way. Enver practically pushed me out the door."

    show korin casual smirk at right1plus
    ko "Yeah...I figured he might do something like that."
    "I watch her, trying to decipher what the secret smirk on her face might mean, when an idea clicks in my brain."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(Has Enver...been talking to Korin about me?)"

    show ecmc jacket_v2_cu pin_cu embarrassed_cu blush_cu at ecmc_cu
    "(Has Enver been talking to Korin about me...the same way he's been talking to me about Korin?)"
    hide ecmc

    show ecmc jacket_v2 pin smile at left1plus
    show korin casual smirk at right1plus
    mckorin "I wonder how he'd act if he could see us together right now."

    show korin casual smile at right1plus
    "Korin shakes her head."
    ko "UGH. He'd be insufferable, I just know it."

    show ecmc jacket_v2 pin surprised at left1plus
    mckorin "Because I'm a trainee? And you're my instructor?"

    show korin casual basic at right1plus
    "Korin's expression grows suddenly serious."
    ko "...Does that bother you?"
    "I pointedly look down at our linked arms, then back up at her."

    show korin casual smile at right1plus
    "Korin throws her head back and laughs."
    ko "Okay, yeah. I guess we're kind of past that at this point."

    show ecmc jacket_v2 pin smile at left1plus
    mckorin "Do you think so, detective?"
    ko "Stoppp!"

    show korin casual basic at right1plus
    "Then she actually stops, looking at one of the boardwalk stalls."

    show ecmc jacket_v2 pin basic at left1plus
    ko "Oh, hold on, I want to look. Some of this stuff is really cute..."
    "She lowers her voice as we look over some pieces."

    show korin casual sad at right1plus
    ko "But I don't want to get ripped off!"

    show ecmc jacket_v2 pin surprised at left1plus
    mckorin "What? Can't you just...do that thing you do to people? Social engineering?"

    show korin casual smirk at right1plus
    ko "What, for some cheap little trinkets? I could never."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    "(Well, I certainly could.)"
    hide ecmc

    show korin casual smirk blush at right1plus
    show ecmc jacket_v2 pin basic at left1plus
    "I pick up one of the rings that Korin had her eye on and hold it up to the vendor."

    show ecmc jacket_v2 pin smile at left1plus
    mckorin "Excuse me...how much for this?"
    vendor "Oh, I love your taste. That one's usually seventy-five, but I'll tell you what--I'll let it go to you for sixty."

    show ecmc jacket_v2 pin determined at left1plus
    mckorin "Sixty? Hmm..."

    show korin casual basic blush at right1plus
    mckorin "Is this pink citrine?"
    vendor "Great eye! Yes, it is."
    mckorin "Oh, that's a shame. I'd shell out sixty if it were topaz, but if it's citrine, I'd only go as high as...twenty-five."

    show korin casual smile blush at right1plus
    "We haggle back and forth for a minute or two more. Even Korin jumps in..."
    ko "Come on, babe, it's getting late. Let's just forget it and go home..."
    vendor "Wait! Wait. Okay, I'll settle for thirty, but that's as low as I can go."

    show ecmc jacket_v2 pin smile at left1plus
    "I happily pay, and Korin and I walk happily away towards the docks. "
    ko "That was {i}chilling{/i}! You barely budged an inch!"
    mckorin "Well, I learned from the best!"
    "Korin pulls my hand up, looking closer at the ring."
    ko "And it's so pretty! It matches your eyes..."
    mckorin "You like it? Here. You keep it!"

    show korin casual surprised blush at right1plus
    ko "What--Really?"

    show ecmc jacket_v2 pin embarrassed at left1plus
    mckorin "It's more your style than mine. I was thinking of you when I picked it out so..."

    show ecmc jacket_v2 pin determined at left1plus
    show korin casual smile blush at right1plus
    "I reach for her hand, pick a finger, and slip the ring on."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(Um..)"
    hide ecmc

    show ecmc jacket_v2 pin surprised blush at left1plus
    show korin casual surprised at right1plus
    "My face grows hot when I realize what this looks like."

    hide ecmc
    hide korin
    show korin casual_cu smirk_cu at korin_cu
    "Korin bites her lip, but a few giggles slip out."
    hide korin

    show ecmc jacket_v2_cu pin_cu surprised_cu blush_cu at ecmc_cu
    mckorin "I didn't mean to, uh..."
    hide ecmc

    show korin casual_cu smile_cu at korin_cu
    ko "It's okay! And look, It's a perfect fit. I love it."
    ko "Thanks, {i}babe{/i}."
    hide korin

    show ecmc jacket_v2_cu pin_cu smile_cu at ecmc_cu
    mckorin "You're welcome, {i}babe{/i}."
    hide ecmc
    show korin casual_cu smile_cu at korin_cu
    "Both of us are all smiles. And before I can do anything else, Korin leans in..."
    hide korin

    stop music fadeout 1.0
    play music ecmromantic3 fadein 0.5
    scene bg ecm_korin_s1_ei4 with fade:
        xpos 0.5 ypos 1.0 xanchor 0.515 yanchor 1 zoom 1.35
        linear 5 xanchor 0.44 yanchor 0.605

    "I feel her lips press against my cheek "
    "My heart skips like a flat stone across calm water. I'm glowing like the sunset."

    window hide
    scene bg ecm_korin_s1_ei4:
        xpos 0.5 ypos 1.0 xanchor 0.44 yanchor 0.605 zoom 1.35
        linear 5 xanchor 0.5 yanchor 1.0 zoom 0.65
    pause
    window show
    "And Korin is close to me, as close as I've wanted her to be since..."
    "(I can't pinpoint the exact moment I knew I wanted this.)"
    "(And all the danger and difficult times I've been through since I started at D.I.V.A.A....)"
    "(This one little moment with Korin makes it all worth it.)"
    "It all feels so natural to me, and yet it still makes my head spin."

    scene bg ecm_marinadelrey_sunset at bg with fade

    show korin casual smile at right1
    show ecmc jacket_v2 pin smile at left1
    "With our arms still linked together, Korin and I lean on the railing and look out at the sunset."
    mckorin "Hey, Korin..."

    show korin casual surprised at right1
    "A breeze rolls in from the ocean, and Korin brushes the hair out of her face as she takes her eyes off the sunset to look at me."

    show ecmc jacket_v2 pin surprised at left1
    "And for one second, I'm struck by how gorgeous she is...and I know I've got to do it."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu determined_cu at ecmc_cu
    "(There's no better moment. I have to shoot my shot.)"
    hide ecmc

    show korin casual surprised at right1
    show ecmc jacket_v2 pin surprised at left1
    mckorin "I know it might complicate things, but..."

    show ecmc jacket_v2 pin determined at left1
    mckorin "We've been through some complicated stuff already, so I bet we could handle it."

    show korin casual smile at right1
    show ecmc jacket_v2 pin surprised at left1
    "Korin Grins."
    ko "Out with it, Scraps. What is it?"
    "Unlike those times before when I'd falter for asking for her help...this time, I don't hesitate."

    show ecmc jacket_v2 pin smile at left1
    mckorin "Would you want to go on a date with me?"
    "Korin breaks into a huge grin, and I feel hope and relief flood me in equal measure."
    mckorin "Like an actual, real date. Like whatever Rhys keeps thinking we're on whenever we go to MegaBites."

    show korin casual surprised at right1
    "She takes a deep breath, and I can see the word forming on her lips: {i}yes{/i}."
    "But...it doesn't come."

    show ecmc jacket_v2 pin sad at left1
    "Something's holding her back."

    show korin casual sad at right1
    "Korin takes a deep breath, and I watch her features crumble. "
    ko "[genericfn]..."

    hide korin
    hide ecmc
    show ecmc jacket_v2_cu pin_cu surprised_cu at ecmc_cu
    "(No. Nononono! What does that look mean?)"
    hide ecmc

    show korin casual_cu sad_cu at korin_cu
    "Gently, Korin takes both of my hands in hers."
    ko "I have something I need to tell you."

    scene bg ecm_tbc at bg with fade

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

