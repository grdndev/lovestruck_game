#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
define mclexi = Character("books.names[\"lexifn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "lexi", story_name = "Lexi Sweetwater", story_book = "msc", story_seasonlength = 12, seasons = 1, episodes = 12, nameablecharacters = 1)
    desc.lexi_maincharacters = ["My Siren Crush MC", "Lexi Sweetwater"]
    desc.lexi_supportingcharacters = {"Trina, Hannah, Jerry"}
    desc.lexi_genres = {"Fantasy", "Modern"}
    desc.lexi_tags = {"Official Route"}

    desc.lexi_author = {"Voltage USA"}
    desc.lexi_colour = "#FF0054"
    desc.lexi_style = "mstyle"

    desc.lexi_season1_description = "Lexi Sweetwater, a treasure-hunting mermaid, splashed into your life "\
    " six months ago before dissappearing with the morning tide. Now that "\
    "crazy fling feels like a dream and you've just been killing time since. But "\
    "when Lexi returns like a tidal wave you don't know if you can trust her or"
    "your heart. Is she here for the steal of the century...or for you?"
    desc.lexi_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode2_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode3_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode4_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode5_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode6_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode7_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode8_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode9_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode10_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode11_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexi_season1_episode12_description = "Transcription by: {color=#808000}Olive{/color}"
