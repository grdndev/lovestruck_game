#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

define mcmaxime = Character("books.names[\"dmaximepfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "dmaximep", story_name = "Maxime Okun (Special Preivew)", story_book = "msc", story_seasonlength = 6, seasons = 1, episodes = 6, nameablecharacters = 1)
    desc.dmaximep_maincharacters = ["Siren MC", "Maxime Okun"]
    #desc.dmaximep_supportingcharacters = {""}
    #desc.dmaximep_genres = {"Sci-Fi", "Action"}
    desc.dmaximep_tags = {"Official Route"}

    desc.dmaximep_author = {"Voltage USA"}
    desc.dmaximep_colour = "#FF0054"
    desc.dmaximep_style = "mstyle"

    desc.dmaximep_season1_description = "There's a big surf competition coming up and you want to win."\
    "A guarded ex-pro is in town and it would be great if he could give you some pointers."\
    "It turns out he's keeping more watery secrets than just his surf technique."\
    "Can you convince him to trust you? Will your world or heart ever be the same if you do?"\
    
    desc.dmaximep_season1_episode1_description = "Transcription by: sharif"
    desc.dmaximep_season1_episode2_description = "Transcription by: sharif"
    desc.dmaximep_season1_episode3_description = "Transcription by: sharif"
    desc.dmaximep_season1_episode4_description = "Transcription by: sharif"
    desc.dmaximep_season1_episode5_description = "Transcription by: sharif"
    desc.dmaximep_season1_episode6_description = "Transcription by: sharif"
