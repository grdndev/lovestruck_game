#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
define mclexi = Character("books.names[\"lexipfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)

init python:
    addstory(story_id = "lexip", story_name = "Lexi Sweetwater (Special Preview)", story_book = "msc", story_seasonlength = 6, seasons = 1, episodes = 6, nameablecharacters = 1)
    desc.lexip_maincharacters = ["My Siren Crush MC", "Lexi Sweetwater"]
    desc.lexip_supportingcharacters = {"Trina, Ned"}
    desc.lexip_genres = {"Fantasy", "Modern"}
    desc.lexip_tags = {"Official Route"}

    desc.lexip_author = {"Voltage USA"}
    desc.lexip_colour = "#FF0054"
    desc.lexip_style = "mstyle"

    desc.lexip_season1_description = "Everyone's talking about the rumored treasure off the coast but your focus is solely on becoming a pro-surfer. "\
    " That is until you meet a beautiful and feisty treasure hunter with a secret. What lengths would you go to "\
    "protect her secret from those that would use it against her? And will you be able to resist the promise of "\
    "adventure, and maybe more, in her eyes?"
    desc.lexip_season1_episode1_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexip_season1_episode2_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexip_season1_episode3_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexip_season1_episode4_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexip_season1_episode5_description = "Transcription by: {color=#808000}Olive{/color}"
    desc.lexip_season1_episode6_description = "Transcription by: {color=#808000}Olive{/color}"
