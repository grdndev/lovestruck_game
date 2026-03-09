#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

define mcjd = Character("books.names[\"jdfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "jd", story_name = "Jordan 'JD' Davies", story_book = "hifl", story_seasonlength = 12, seasons = 1, episodes = 1, nameablecharacters = 1)
    desc.jd_maincharacters = ["Havenfall MC", "Jordan 'JD' Davies"]
    desc.jd_supportingcharacters = {"Havenfall's Finest, Grace"}
    desc.jd_genres = {"Supernatural", "Action"}
    desc.jd_tags = {"Official Route"}

    desc.jd_author = {"Voltage USA"}
    desc.jd_colour = "#FF0054"
    desc.jd_style = "mstyle"

    desc.jd_season1_description = "JD has always seemed like a wild party animal, stuck in Havenfall on some"\
    " sort of probation, but at least they're fun to be around. When your sister goes missing, "\
    "the rebel without a cause may be your only hope when they turn out to be... the Jersey Devil?! "
    
    desc.jd_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
