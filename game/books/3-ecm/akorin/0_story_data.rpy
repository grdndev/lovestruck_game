#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

define mckorin = Character("books.names[\"korinfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "korin", story_name = "Korin Reyes", story_book = "ecm", story_seasonlength = 12, seasons = 1, episodes = 12, nameablecharacters = 1)
    desc.korin_maincharacters = ["Edge Case MC", "Korin Reyes"]
    #desc.korin_supportingcharacters = {""}
    desc.korin_genres = {"Sci-Fi", "Action"}
    desc.korin_tags = {"Official Route"}

    desc.korin_author = {"Voltage USA"}
    desc.korin_colour = "#FF0054"
    desc.korin_style = "mstyle"

    desc.korin_season1_description = "You joined D.I.V.A.A. to help people, but a mysterious training accident puts your career in jeopardy."\
    "Fortunately, your orientation leader is the cunning and empathetic"\
    "Phoenix Investigator Korin Reyes! Although Korin's your mentor,"\
    "if you can connect with her outside of work, you'll have a chance at salvaging your reputation and lighting a spark between your hearts."\
    " --- "\
    "Developed by: Ant, Olive"
    desc.korin_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.korin_season1_episode2_description = "Transcripton by: Solamentia"
    desc.korin_season1_episode3_description = "Transcription by: subliminallights"
    desc.korin_season1_episode4_description = "Transcription by: freestyle70s"
    desc.korin_season1_episode5_description = "Transcription by: mooreismoore"
    desc.korin_season1_episode6_description = "Transcription by: subliminallights"
    desc.korin_season1_episode7_description = "Transcription by: evane b"
    desc.korin_season1_episode8_description = "Transcription by: Abderian63"
    desc.korin_season1_episode9_description = "Transcription by: evane b"
    desc.korin_season1_episode10_description = "Transcription by: freestyle70s"
    desc.korin_season1_episode11_description = "Transcription by: mooreismoore"
    desc.korin_season1_episode12_description = "Transcription by: RubyChanTheGreat"
