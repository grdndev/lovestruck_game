#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

define mcvan = Character("books.names[\"vanfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "van", story_name = "Vanessa Helsing", story_book = "hifl", story_seasonlength = 12, seasons = 1, episodes = 12, nameablecharacters = 1)
    desc.van_maincharacters = ["Havenfall MC", "Vanessa Helsing"]
    desc.van_supportingcharacters = {"Havenfall's Finest, Grace"}
    desc.van_genres = {"Supernatural", "Action"}
    desc.van_tags = {"Official Route"}

    desc.van_author = {"Voltage USA"}
    desc.van_colour = "#FF0054"
    desc.van_style = "mstyle"

    desc.van_season1_description = "It feels like your lucky day when you pick up a beautiful and mysterious woman on the side of the road."\
    " But when she saves you from a vampire attack and reveals herself as a legendary Vampire Huntress "\
    "your entire life is turned upside down. "\
    "She promises to protect you from the monsters of the night, but who will protect your heart from her?"
    desc.van_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode2_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode3_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode4_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode5_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode6_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode7_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode8_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode9_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode10_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode11_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.van_season1_episode12_description = "Transcription by: {color=#808000}Olive{/color}"
