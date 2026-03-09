#init -2:
    ##This is where I place my persistent flags for choices, but if you don't know what that means don't worry about it.
    #default persistent.s1e1exampleflag = False

style mstyle:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
define mcarianna = Character("books.names[\"ariannafn1\"]",color="#FFFFFF", image="mscmc", who_underline=True, what_prefix='"', what_suffix='"', what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
init python:
    addstory(story_id = "arianna", story_name = "Arianna Nitida", story_book = "msc", story_seasonlength = 12, seasons = 2, episodes = 24, nameablecharacters = 1)
    desc.arianna_maincharacters = ["My Siren Crush MC", "Lexi Sweetwater"]
    desc.arianna_supportingcharacters = {"Trina"}
    desc.arianna_genres = {"Fantasy", "Modern"}
    desc.arianna_tags = {"Official Route"}

    desc.arianna_author = {"Voltage USA"}
    desc.arianna_colour = "#FF0054"
    desc.arianna_style = "mstyle"

    desc.arianna_season1_description = "A beautiful mermaid, Arianna, comes back into town looking to have some drinks. She needs your help navigating the world above the sea, "\
    " but maybe she can also help you achieve your dreams. Even though you are from completely different worlds, "\
    "an incredible friendship blooms...but is there more between you than friendship?"\
    "Are you ready to fall for this mermaid??"

    desc.arianna_season1_episode1_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode2_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode3_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode4_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode5_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode6_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode7_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode8_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode9_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode10_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode11_description = "Transcript by: Scribbs"
    desc.arianna_season1_episode12_description = "Transcript by: Scribbs"

    desc.arianna_season2_description = "Arianna is briefly stranded on land, but when able to return to the sea, will you go with her?  "\
    "Dive under the surface with Arianna in season 2, and join her in the fight for art, magic, "\
    "and love. You and Arianna have something special, but are you ready to be part of her world?"\

    desc.arianna_season2_episode1_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode2_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode3_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode4_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode5_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode6_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode7_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode8_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode9_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode10_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode11_description = "Transcript by: Scribbs"
    desc.arianna_season2_episode12_description = "Transcript by: Scribbs"
