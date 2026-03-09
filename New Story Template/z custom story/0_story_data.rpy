#INSTRUCTIONS FOR ADDING A NEW STORY:

#Choose a short story id for your story- make sure it's a single lowercase word.

#Replace every instance of "storyid" in this file with your story's id. If your story's id is mermaid, "storyidfn1" will become "mermaidfn1"
#Define your MCs. Make sure to replace "mycharacter" with something else.

#Update the addstory function. Put your story's name in "story_name"- this is what will show up in the menu.
#story_seasonlength allows you to make seasons that are more or less than 12 episodes long. This is useful for shorter form stories.
#seasons and episodes needs to be set to the CURRENT value. If you want 1 season and 6 episodes to be on the menu, set seasons to 1 and episodes to 6.

#Put your own story's description in the desc section, adding new entries based on the existing format.
#It doesn't really matter what you put here, it's just a vibe. Make it as descriptive as you please.
#storyid_author is where you put your name or handle, and storyid_colour will set the colour of your name in the description.


init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    default persistent.s1e1exampleflag = False

style yourstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

#Define your MCs here. You can have several nameable MCs in the same story, so long as you specify the number in addstory below.
#make sure to change "mycharacter1" and "mycharacter2" and so on to a unique name.
#You can also just define normal characters here, too, if you know how to do that.
define mycharacter1 = Character("books.names[\"storyidfn1\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
define mycharacter2 = Character("books.names[\"storyidfn2\"]",color="#FFFFFF", who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    #This line will need to be updated every time you add a new season or episode.
    addstory(story_id = "storyid", story_name = "Custom Story", story_book = "hifl", story_seasonlength = 12, seasons = 1, episodes = 1, nameablecharacters = 2)
    
    desc.storyid_maincharacters = ["Vanessa", "Diego"]
    desc.storyid_supportingcharacters = {"Nobody else"}
    desc.storyid_genres = {"Drama"}
    desc.storyid_tags = {"Platonic"}

    desc.storyid_author = {"Your name"}
    desc.storyid_colour = "#6f2384ff"
    desc.storyid_style = "yourstyle"

    desc.storyid_season1_description = "Example season description."
    desc.storyid_season1_episode1_description = "Example episode description."
