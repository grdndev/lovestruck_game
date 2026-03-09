###Instructions for adding new episodes:

###Make a copy of this file and paste it in the correct story folder.
###Replace every instance of "storyid" in this file with the intended story's id, including in the filename.
###Set make sure the label below reads the correct season and episode number.
###Follow any instructions in the script. 
###Mac's route, and the Ghost route, both have examples of most techniques you'll need to write the script.

###General advice:
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

label storyid_season1_episode1:
    $tbc = False

    ##Change these to suit the story
    scene hifl_prologue at bg
    play music hifleveryday

    pause #Make sure this happens BEFORE the three $ lines below.

    #Leave these guys right here! Or things will get weird. 
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show bg main_day at bg with dissolve
    show vanessa huntress happy at centre
    mycharacter1 "I am conflicted because you are a vampire and I do not like vampires."
    show vanessa huntress happy at left3
    show diego doctor vampirehappy at right3
    mycharacter2 "This is unfortunate."
    mycharacter1 "Yes."
    play sound applause2
    pause 2

    $tobecontinued() #Do not more or remove this please.
    show bg hifltbc
    hide diego
    hide vanessa
    with fade
    
    pause
    $ resets() #Also do not move or remove this.

