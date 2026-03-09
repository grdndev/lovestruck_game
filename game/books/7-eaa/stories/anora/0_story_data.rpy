#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

define mcnora = Character("books.names[\"norafn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "nora", story_name = "Nora Le Fay", story_book = "eaa", story_seasonlength = 1, seasons = 1, episodes = 1, nameablecharacters = 1)
    desc.nora_maincharacters = ["EAA Female MC", "Nora Le Fay"]
    desc.nora_supportingcharacters = {"EAA Male MC, Oscar"}
    desc.nora_genres = {"Supernatural", "Fantasy"}
    desc.nora_tags = {"Official Route"}

    desc.nora_author = {"Voltage USA"}
    desc.nora_colour = "#FF0054"
    desc.nora_style = "mstyle"

    desc.nora_season1_description = "Nora has always been a self sufficient witch who enjoys learning"\
    " everything she can about everything. She wants to show you the magic "\
    "everything she can about everything. She wants to show you the magic "\
    "she doesn't have to do it alone?"
    desc.nora_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
