##Important! Only include this ONCE. You can move it into a different file, but you only want to define your story once.
##Update the episode and season counts here.
#All this does is tell the game that there's a new story and its basic details, like name and how many episodes there currently is.
#story_book determines which book's UI will be used. hifl means havenfall's ui, vn means villainous nights.
init:
    $addstory(story_id = "llstoryid", story_name = "Custom Story", story_book = "ll", story_seasonlength = 12, seasons = 1, episodes = 1, nameablecharacters = 1)

define llcharacter1 = Character("books.names[\"llstoryidfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
define llcharacter2 = Character("books.names[\"llstoryidfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
##et this to the name, season and episode of your story
label llstoryid_season1_episode1:
    $tbc = False

    ##Change these to suit the story
    show bg reinerhall at bg
    play music helena

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() and tobecontinued() at the bottom.

    show bg reinerhall at bg
    show llmc altcasual altsad at right3
    show helena casual basic at left3

    llcharacter1 "\"I don't know.\""

    
    pause
    $ resets()

