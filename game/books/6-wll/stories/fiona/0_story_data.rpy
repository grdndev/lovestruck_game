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


#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style yourstyle:
    color "#6f2384ff"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

#Define your MCs here. You can have several nameable MCs in the same story, so long as you specify the number in addstory below.
#make sure to change "mycharacter1" and "mycharacter2" and so on to a unique name.
#You can also just define normal characters here, too, if you know how to do that.
define mcfiona = Character("books.names[\"fionafn1\"]",color="#FFFFFF", who_underline=True,what_prefix='"', what_suffix='"', what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    #This line will need to be updated every time you add a new season or episode.
    addstory(story_id = "fiona", story_name = "Fiona", story_book = "wll", story_seasonlength = 12, seasons = 1, episodes = 12, nameablecharacters = 1)

    desc.fiona_maincharacters = ["Wicked Lawless Love MC", "Fiona"]
    #desc.fiona_supportingcharacters = {""}
    desc.fiona_genres = {"Western", "Supernatural"}
    desc.fiona_tags = {"Official Route"}

    desc.fiona_author = {"Voltage USA"}
    desc.fiona_colour = "#6f2384ff"
    desc.fiona_style = "yourstyle"

    desc.fiona_season1_description = "In the world of scam artists, the fortune teller's game is the hardest to pull off. " \
    "However, Miss Fiona Eichen almost makes predicting the future appear natural. " \
    "She's taken a shine to you and wants to team up for her next caper, but this job is going to haunt you far more than you expect. " \
    "Will you get caught up in Fiona's master plan or will you make a mess out of this mystic? Developed by: Scribbs"

    desc.fiona_season1_episode1_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode2_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode3_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode4_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode5_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode6_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode7_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode8_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode9_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode10_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode11_description = "Transcript by: Scribbs"
    desc.fiona_season1_episode12_description = "Transcript by: Scribbs"
