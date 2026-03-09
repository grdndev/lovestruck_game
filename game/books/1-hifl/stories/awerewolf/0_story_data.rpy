#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
define mcmac = Character("books.names[\"macfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "mac", story_name = "Mackenzie Hunt", story_book = "hifl", story_seasonlength = 12, seasons = 1, episodes = 12, nameablecharacters = 1)
    desc.mac_maincharacters = ["Havenfall MC", "Mackenzie Hunt"]
    desc.mac_supportingcharacters = {"Havenfall's Finest, Grace"}
    desc.mac_genres = {"Supernatural", "Action"}
    desc.mac_tags = {"Official Route"}

    desc.mac_author = {"Voltage USA"}
    desc.mac_colour = "#FF0054"
    desc.mac_style = "mstyle"

    desc.mac_season1_description = "You've always known Sheriff Hunt as the cool and collected protector of the town,"\
    " but when your sister goes missing, some shocking "\
    "truths begin to surface. She offers to help you, but is her "\
    "fierce protectiveness the werewolf inside... or something more?"
    desc.mac_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode2_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode3_description = "Transcription by: {color=#74fdd4ff}Danielle{/color}"
    desc.mac_season1_episode4_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode5_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode6_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode7_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode8_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode9_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode10_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode11_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.mac_season1_episode12_description = "Transcription by: {color=#808000}Olive{/color}"
