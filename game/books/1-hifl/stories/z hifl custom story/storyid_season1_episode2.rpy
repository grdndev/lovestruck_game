label storyid_season1_episode2:
    #Keep this right here.
    $tbc = False

    ##Change these to suit the story
    scene hifl_prologue at bg
    play music hifleveryday

    #Make sure this pause happens BEFORE the three $ lines below.
    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.
label select1:
    $menuhideborder = True
    menu se2c1:
        "Full Body":
            jump sprite1

        "Closeup":
            jump sprite2

label sprite1:
    $menuhideborder = False
    scene black at bg with dissolve
    #show yovith basic basic at left3
    show altea armour basic at centre
    va "Test 1."

    hide yovith
    jump select1

label sprite2:
    $menuhideborder = False
    scene black at bg with dissolve
    show yovith basic_cu basic_cu at yovith_cu
    va "Test 1."
    hide yovith




    jump select1


    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.

    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.
