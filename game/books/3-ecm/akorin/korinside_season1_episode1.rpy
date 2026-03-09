label korin_season1_episode1a1:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene bg ecm_office_hq_on at bg
    show ecm_overlay at full_size:
        alpha 0.8
    play music ecmupbeateveryday2

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
    hide ecm_overlay with dissolve
    show ecmc jacket_v2 pin surprised at left3
    show korin nojacket pin basic at right1, grayscale
    show bird normal at right1, birdbob:
        xoffset 200 ypos 100
    mckorin "Korin, what are you doing?"

    show korin nojacket pin angry at normcolor
    "I walk over to Korin's desk where she's rapidly flicking through reports, looking super focused."

    show ecmc at grayscale
    show korin nojacket pin smile
    ko "Oh, hey, [genericfn]."

    show ecmc jacket_v2 pin smile
    ko "I'm just trying to make sure I finish all my work on time so I can leave as soon as possible."

    show ecmc at normcolor
    show korin nojacket pin smile at grayscale
    mckorin "What's the rush? Are you meeting someone?"

    show ecmc at grayscale
    show korin nojacket pin basic blush at normcolor
    ko "Oh, nothing like that."

    show korin nojacket pin smile -blush
    ko "It's my friend's birthday tonight!"

    show ecmc at normcolor
    show korin nojacket pin smile at grayscale
    mckorin "Well, that definitely sounds like something you don't want to miss."
    mckorin "Can I help you?"

    show ecmc at grayscale
    show korin nojacket pin surprised blush at normcolor
    ko "Do you really mean that, [genericfn]"

    hide korin
    hide bird
    hide ecmc
    show ecmc jacket_v2_cu smile_cu blush_cu at ecmc_cu
    "(Korin has always been the first to ask if I need help.)"
    hide ecmc

    $menuhideborder = True
    menu korinsides1e1:
        "Organize the computer files.":
            $menuhideborder = False
        "Finish typing up the investigation reports.":
            $menuhideborder = False
            show ecmc jacket_v2 pin smile at left3
            show korin nojacket pin angry at right1, grayscale
            show bird normal at right1, birdbob:
                xoffset 200 ypos 100
            mckorin "How about I finish up those investigation reports for you?"

            show ecmc at grayscale
            show korin at normcolor
            ko "That would be amazing!"

            hide ecmc
            hide korin
            hide bird
            "I take over typing up the investigation reports as Korin takes care of the e-filing."

            show ecmc at grayscale
            show korin at normcolor
        "Make backup copies of testimonials with Korin.":
            $menuhideborder = False
    show ecmc jacket_v2 pin basic at left3, grayscale
    show korin nojacket pin smile at right1
    show bird normal at right1:
        xoffset 200 ypos 100
        parallel:
            easein 0.4 offset 400
        parallel:
            linear 0.4 alpha 0.0
    ko "Alright, I think we're done here. I think Baby Bird can go take care of the rest."
    hide bird
    ko "Thanks again for the help!"

    show korin nojacket pin smirk
    ko "Now I have more time to put my makeup on and finish wrapping my friend's present."

    show ecmc jacket_v2 pin smile at normcolor
    show korin at grayscale
    mckorin "I'm happy to help."

    show ecmc at grayscale
    show korin at normcolor
    ko "Why don't you come with me tonight and have a couple drinks?"

    show ecmc jacket_v2 pin surprised at normcolor
    show korin at grayscale
    mckorin "Your friend won't mind?"

    show ecmc at grayscale
    show korin nojacket pin smile at normcolor
    ko "Not at all! The more the merrier."
    ko "This is one of my favorite bars in the city. You have to come check it out."

    show ecmc jacket_v2 pin thinking at normcolor
    show korin at grayscale
    mckorin "Well..."

    show ecmc at grayscale
    show korin nojacket pin basic at normcolor
    ko "It's called Y3K if you'd like to look it up."
    ko "It's trendy, yet also modest and quiet. It's the perfect place to go for a couple relaxing drinks after work."

    show ecmc at normcolor
    show korin at grayscale
    mckorin "Hip and trendy does seem to be your thing."

    show ecmc at grayscale
    show korin nojacket pin smile at normcolor
    "I mean, it's a good bar! But it also has a lot of history for D.I.V.A.A. cadets."

    show ecmc at normcolor
    show korin at grayscale
    mckorin "I didn't really go out much when I was a cadet..."

    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
