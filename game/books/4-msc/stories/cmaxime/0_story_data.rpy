#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

define mcmax = Character("books.names[\"maximefn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "maxime", story_name = "Maxime Okun", story_book = "msc", story_seasonlength = 12, seasons = 1, episodes = 12, nameablecharacters = 1)
    desc.maxime_maincharacters = ["Siren MC", "Maxime Okun"]
    #desc.maxime_supportingcharacters = {""}
    #desc.maxime_genres = {"Sci-Fi", "Action"}
    desc.maxime_tags = {"Official Route"}

    desc.maxime_author = {"Voltage USA"}
    desc.maxime_colour = "#FF0054"
    desc.maxime_style = "mstyle"

    desc.maxime_season1_description = "You don't want to let anything distract you from surfing. But then, Maxime comes back into your life. "\
    "Unexpectedly, you have the chance to be part of his top secret mer spy mission, and also have him as your coach for a big tournament. "\
    "You're confident you have what it takes to balance two worlds and keep your feelings at bay. "\
    "But, when you realize you might just be in over your head, do you risk everything, even your heart?"
    desc.maxime_season1_episode1_description = "Transcription by: sharif"
    desc.maxime_season1_episode2_description = "Transcription by: sharif"
    desc.maxime_season1_episode3_description = "Transcription by: sharif"
    desc.maxime_season1_episode4_description = "Transcription by: sharif"
    desc.maxime_season1_episode5_description = "Transcription by: sharif"
    desc.maxime_season1_episode6_description = "Transcription by: sharif"
    desc.maxime_season1_episode7_description = "Transcription by: sharif"
    desc.maxime_season1_episode8_description = "Transcription by: sharif"
    desc.maxime_season1_episode9_description = "Transcription by: sharif"
    desc.maxime_season1_episode10_description = "Transcription by: sharif"
    desc.maxime_season1_episode11_description = "Transcription by: sharif"
    desc.maxime_season1_episode12_description = "Transcription by: sharif"
