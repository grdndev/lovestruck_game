#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
define mcariannaprev = Character("books.names[\"ariannapfn1\"]",color="#FFFFFF", image="mscmc", who_underline=True,what_prefix='"', what_suffix='"', what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "ariannap", story_name = "Arianna Nitida (Special Preview)", story_book = "msc", story_seasonlength = 6, seasons = 1, episodes = 6, nameablecharacters = 1)
    desc.ariannap_maincharacters = ["My Siren Crush MC", "Lexi Sweetwater"]
    desc.ariannap_supportingcharacters = {"Trina"}
    desc.ariannap_genres = {"Fantasy", "Modern"}
    desc.ariannap_tags = {"Official Route"}

    desc.ariannap_author = {"Voltage USA"}
    desc.ariannap_colour = "#FF0054"
    desc.ariannap_style = "mstyle"

    desc.ariannap_season1_description = "Working to become a pro-surfer doesn't leave much room for anything else, especially a love life."\
    "That is until the day a gorgeous stranger named Arianna swims up to your board."\
    "She wants to trust you with a deep secret, but will you let your heart believe her?"\

    desc.ariannap_season1_episode1_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode2_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode3_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode4_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode5_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode6_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode7_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode8_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode9_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode10_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode11_description = "Transcript by: Scribbs"
    desc.ariannap_season1_episode12_description = "Transcript by: Scribbs"
