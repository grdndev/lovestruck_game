#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
define mchelena = Character("books.names[\"helenafn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "helena", story_name = "Helena Klein", story_book = "ll", story_seasonlength = 12, seasons = 0, episodes = 0, nameablecharacters = 1)
    desc.helena_maincharacters = ["Love & Legends MC", "Helena Klein"]
#    desc.helena_supportingcharacters = {"Havenfall's Finest, Grace"}
    desc.helena_genres = {"Fantasy", "Romance"}
    desc.helena_tags = {"Official Route"}

    desc.helena_author = {"Voltage USA"}
    desc.helena_colour = "#FF0054"
    desc.helena_style = "mstyle"

    desc.helena_season1_description = "What if fate had something else in store for you? Helena Klein ,"\
    " was the Witch Queen's apprentice, cold as ice, but underneath  "\
    "it all you know there's something softer..."\
    " Will you teach this sorceress the meaning of true love?"
    desc.helena_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
