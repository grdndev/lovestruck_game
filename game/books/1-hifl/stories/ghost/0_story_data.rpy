init -2:
    default persistent.s1e2angerFlag = False
    default persistent.s1e2tamFlag = False

style Daniellescoolstyle:
    color "#74fdd4ff"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20

transform gcentre:
    xpos stagepos[1]
    ypos 1.125
transform gleft3:
    xpos stagepos[1] - 220
    ypos 1.125
transform gright3:
    xpos stagepos[1] + 220
    ypos 1.125
define tam = Character("Tamara",color="#FFFFFF", who_underline=True, what_prefix='"', what_suffix='"', what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define ghostmc = Character("books.names[\"ghostfn1\"]",color="#FFFFFF", what_prefix='"', what_suffix='"',  who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], ctc = "ctc_", dynamic = True)
init python:
    addstory(story_id = "ghost", story_name = "The Ghost", story_book = "hifl", story_seasonlength = 12, seasons = 1, episodes = 5, nameablecharacters = 1, tags = 1)


    desc.hifl_description = ""
    desc.ghost_maincharacters = ["Havenfall MC"]
    desc.ghost_supportingcharacters = {"Grace", "Mackenzie", "JD", "Razi", "Diego"}
    desc.ghost_genres = {"Drama"}
    desc.ghost_tags = {"Platonic"}

    desc.ghost_author = {"Danielle"}
    desc.ghost_colour = "#74fdd4ff"
    desc.ghost_style = "Daniellescoolstyle"


    #desc.ghost_description = "Starring: Havenfall MC\nWith: Grace, Mackenzie, JD, Razi, Diego\nGenre: Drama\n\n\n{color=#90EE90}Platonic{/color}"
    desc.ghost_season1_description = "One moment was all it took- your life will never "\
    "be the same again. Time didn't stop moving just because you did, though, and "\
    "threats you'd never imagined are coming for your town and your friends."\
    " Will you lend a hand from beyond the grave? Or will Havenfall fade away with you?"
    desc.ghost_season1_episode1_description = "Summary: \n{image=images/general/icons/heart.png} You and Grace watch some bad TV.\n"\
    "{image=images/general/icons/heart.png} Someone new starts at the bowling alley.\n{image=images/general/icons/heart.png} JD's prank gets a little weird."
    desc.ghost_season1_episode2_description = "Summary: \n{image=images/general/icons/heart.png}"\
    " Worst hug ever.\n{image=images/general/icons/heart.png}"\
    " You're ignored by even more people.\n{image=images/general/icons/heart.png}"\
    " Awful questions get awful answers."
    desc.ghost_season1_episode3_description = "Summary: \n{image=images/general/icons/heart.png}"\
    " The whole gang gets together.\n{image=images/general/icons/heart.png}"\
    " You learn many secrets.\n{image=images/general/icons/heart.png}"\
    " Forgiveness is the order of the day."
