label ecmstoryid_season1_episode2:
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
label ecmselect1:
    $menuhideborder = True
    menu cse2c1:
        "Full Body":
            jump ecmsprite1
        
        "Closeup":
            jump ecmsprite2

label ecmsprite1:
    $menuhideborder = False
    scene black at bg with dissolve
    show korin nojacket basic pin at holo_mask, korin_holo, centre
    va "Test 1."
    show ecmc casual_v2 basic at holo_mask, ecmc_holo ,centre
    va "Test 2"
    show ecmc jacket_v2 pin determined at centre
    va "Test 3"
    show ecmc nojacket_v2 blush embarrassed at centre
    va "Test 4"
    show ecmc jacket_v2 noblush sad at centre
    va "Test 5"
    show ecmc nojacket_v1 nopin sleep at centre
    va "Test 6"
    show ecmc casual_v1 smile at centre
    va "Test 7"
    show ecmc casual_v1 surprised at centre
    va "Test 8"
    hide ecmc
    jump select1

label ecmsprite2:
    $menuhideborder = False
    scene black at bg with dissolve
    show ecmc casual_v1_cu angry_cu headset_cu at ecmc_cu
    va "Test 1."
    show ecmc casual_v2_cu basic_cu noheadset_cu at ecmc_cu
    va "Test 2"
    show ecmc jacket_v1_cu determined_cu pin_cu at ecmc_cu
    va "Test 3"
    show ecmc jacket_v2_cu embarrassed_cu blush_cu at ecmc_cu
    va "Test 4"
    show ecmc nojacket_v1_cu sad_cu noblush_cu at ecmc_cu
    va "Test 5"
    show ecmc nojacket_v2_cu sleep_cu nopin_cu at ecmc_cu
    va "Test 6"
    show ecmc casual_v1_cu smile_cu at ecmc_cu
    va "Test 7"
    show ecmc casual_v1_cu surprised_cu at ecmc_cu
    va "Test 8"
    hide ecmc
    jump select1


    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, so long as it's above that pause down there.
    
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

