###General advice:

###Hit Shift+R to enable auto reload. This will reload the game every time you save this file- meaning you don't have to
###constantly restart the game while testing. If that doesn't work, please mention it in the discord because it's torture to 
###not have it.

###If a character only shows up a few times, or a character has a temporary name, you don't need to bother defining a new character for that.
###You can simply set the variables $sidecharone, $sidechartwo, or $sidecharthree to the character's name, like so:
#$sidecharone = "Stranger"
#sid1 "I see yer there, varmint."
###This allows you to quickly and easily put a disposable character name in. I'd recommend doing this for all characters other than main characters,
###except in situations where it's unwieldy.

###Characters can refer to your MC's first and last names like this:
#di "I'd trust [genericfn] [genericln] with my life."
###However, if you have more than one MC, you'll have to do it like this instead:
#$namefn = books.names["storyidfn2"]
#$nameln = books.names["storyidln2"]
#di "I'd trust [namefn] [nameln] with my life."
###replacing the 2s with the number of the mc you wish to reference.


#If you run into problems, or have any additional questions, ask @stolenoc on the discord.
#Have fun!

label ecmstoryid_season1_episode1:
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

    ###################Basics####################

    #bg is a transform, which is just a modifier to how the image is drawn. show all background images at bg, to make them the right size.
    #Showing the image with dissolve makes it appear less abruptly.
    show bg main_day at bg with dissolve   

    #centre is also a transform, that puts the characters in the centre of the screen. Please note that it's "centre", not "center."
    show vanessa casual angry at centre

    #Characters have their name, their outfit, and their expression. 
    #You'll need to look at their sprites in images/<book name>/<character name> to know what outfits and expressions they have.
    #Also, you don't have to specify where the character is every time you mention them, they'll sit in place until hidden.
    show vanessa huntress happy
    va "Hello."
    hide vanessa

    #Some also have an accessory slot.
    show wade casual sad at centre
    pause
    show wade casual sad glasses
    pause

    #To hide a character's accessory, use a - sign
    show wade casual sad -glasses
    pause
    show wade casual happy
    pause
    hide wade

    show vanessa huntress happy at centre
    #refer to books/<story>_characters.rpy for a list of character ids. va is "vanessa".
    va "I am conflicted because you are a vampire and I do not like vampires."

    #left3 puts the character at about 1/3 across the screen, and right3 puts them at about 2/3 across the screen.
    #use left1-5 and right1-5 to position characters at different spots on the screen- you can also make a custom transform, but
    #please make it inside this file, rather than editing transforms.rpy.
    show vanessa huntress happy at left3
    show diego doctor vampirehappy at right3
    di "This is unfortunate."
    va "Yes."
    hide diego
    #Transforms can also be used to animate a character, like so.
    show vanessa huntress happy at centre with ease
    show vanessa huntress happy at shake 


    #You can change expressions and outfits with dissolve, too.
    show vanessa casual happy with dissolve

    #Pause just makes the game wait until the user clicks again. 
    pause

    #Put a number after the pause to have it advance on its own after that many seconds.
    pause 2


    hide vanessa
    hide diego

    
    #Things like havenfall MC's truck require a little messing around to work.
    #Notice that you can apply a zoom and offset directly to a sprite. This will continue to apply to them until you 
    #manually set the zoom and offset back to the start, or hide and re show the sprite.
    show truck_back_day at bg behind hiflmc
    show hiflmc beaniecasual surprised at right3 behind truck_front_day:
        zoom 1.25
        yoffset 65
        xoffset -90
    show mac cop basic at left3 behind truck_front_day:
        zoom 1.25
        yoffset -65
        xoffset -80
    show truck_front_day at bg


    #As you can see, MC is now a giant. She will remain a giant until we fix her.
    pause
    show vanessa casual happy at left4
    show hiflmc beaniecasual surprised at centre
    hide mac
    hide truck_front_day
    hide truck_back_day
    pause


    #hiding quickly resets any stuff you've applied to a character, including transforms- any time you hide and reshow a character,
    #you'll need to specify where they are.
    hide hiflmc
    show hiflmc beaniecasual surprised at centre
    show vanessa casual sad

    pause

    ###################Choices####################

    #Use $menuhideborder = True before choices- it hides some UI elements. use $menuhideborder = False immediately after the choice
    #is made.
    $menuhideborder = True
    hide vanessa
    hide hiflmc

    # change "se1c1" to something unique- each choice menu needs its own name. 
    menu ecmse1c1:
        "1. Vanessa.":
            $menuhideborder = False
            show vanessa huntress happy at centre
            va "Vanessa."
            hide vanessa
        "2. Diego.":
            $menuhideborder = False
            show diego doctor sad at centre
            di "Diego."
            hide diego
        "3. Turnip":
            $menuhideborder = False
            show turnip armsup happy at centre
            "!!!"
            hide turnip
    #Make sure to hide anyone who shouldn't still be showing after the choice menu!
    $menuhideborder = True
    menu ecmse1c2:
        "1. Premium Vanessa."(paidchoice = True):
            $menuhideborder = False
            show vanessa huntress hathappy at centre
            va "Hat!"
            hide vanessa
        "3. Regular Vanessa":
            $menuhideborder = False
            show vanessa huntress sad at centre
            va "..."
            hide vanessa

    show vanessa huntress angry at centre



###################Variables####################

#Variables are mostly used to refer to the MC, in this game.
#In most stories, you can refer to the MC's name easily with the premade variables [genericfn] and [genericln],
#which will always equal their first and last name respectively.
    va "[genericfn] [genericln]."


    #In stories with multiple MCs, like EAA, to get the second MC's name, you need to use:
    $namefn = books.names["storyidfn2"]
    $nameln = books.names["storyidln2"]
    va "[namefn] [nameln] is far weaker than [genericfn] [genericln]."


#Custom variables can be set like this:
    $testvariable = "Vampires suck."

#Then, you can use them like this:
    va "[testvariable]"


    hide vanessa
###################Effects####################
    #This plays music or sound. Music will play until you tell it to stop or play another song, sounds will play once. 
    #you can find the songs and their filenames in game/audio/<book name>
    play music suspense
    pause
    play sound applause2
    pause

    #Particle effects will have to be made with an external program, and are still being worked on.
    #Check game\images\general\particles to see which ones are in the game. They can be shown just like any other image.
    show rain
    pause
    hide rain
    #You can use behind to force an image or particle effect to be drawn behind someone else.
    show jd casual angry at centre 
    show jdfire behind jd
    jd "It's JD time."
    pause
    hide jdfire
    hide jd

    #Korin has a bird. You can make it bob up and down like this:
    show korin casual basic at centre
    show bird normal at birdbob:
        xpos 650 #The bird shows up in different places. Experiment with the xpos and ypos to change where it is.
        ypos 50
    pause
    show bird normal at birdgrab #Here's a very specific animation the bird uses in Korin's episode 1.
    pause
    show bird normal: #The bird might also just not be moving at all. You can place it the same way.
        xoffset 0
        yoffset 0 #birdbob and birdgrab work by changing the bird's y and xoffset. This doesn't reset, so if you want to place the bird 
                #somewhere, you might want to set them both back to 0 first.
        xpos 625
        ypos 80

    pause
    $tobecontinued() #Do not more or remove this please. It's okay to do stuff like hide characters
#                     underneath it, though.
    show bg hifltbc
    hide diego
    hide vanessa
    with fade
    
    pause
    $ resets() #Also do not move or remove this, it needs to be the very last thing that happens.

