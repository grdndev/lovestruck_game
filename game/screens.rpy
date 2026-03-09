################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    if persistent.dialogueBoxOpacity>0.85:
        fixed:
            imagebutton:
                idle im.MatrixColor("gui/textboxback.png",im.matrix.opacity(persistent.dialogueBoxOpacity))
                ycenter 510
    window:
        id "window"
        background Transform(Frame("gui/textbox.png",xalign=0.5, yalign=1.0), alpha=persistent.dialogueBoxOpacity)
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    $ ymod = 0
    fixed:
        ycenter 290
        xcenter 520
        image "gui/backdrop.png"
    vbox:
        for i in items:
            if ymod == 0:
                key "K_1" action i.action
            if ymod == 10:
                key "K_2" action i.action
            if ymod == 20:
                key "K_3" action i.action
            vbox:
                ycenter 100 + ymod
                textbutton i.caption:
                    text_color books.choicecolor[whbook]
                    action i.action
                    if "paidchoice" in i.kwargs:
                        idle_background books.id[whbook] + "paidchoice"
                        hover_background books.id[whbook] + "paidchoice_hl"
                    else:
                        idle_background books.id[whbook] + "freechoice"
                        hover_background books.id[whbook] + "freechoice_hl"
            $ ymod += 10
## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 220
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.


screen navigation():

    predict False


            #textbutton _("Save") action ShowMenu("save")

        #if _in_replay:

            #textbutton _("End Replay") action EndReplay(confirm=True)



        #textbutton _("About") action ShowMenu("about")



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init -1:
    default playingsong = ""
    define startsong = 0
    default currentsong = -1
    default which.page = 0
    default which.gallerychar = 0
    default which.gallery = 0
    default which.book = 0
    default which.story = 0
    default which.season = 0
    default which.episode = 0
    default which.type = False
    define homeposrange = len(books.id*(160))
    default homepos = homeposrange/2
init python:
    settingsscreen = False
    class lovestruck:
        id = ""
        booktitle = ""
        cover = ""
        bg = ""
        storyid = ""
        storytitle = ""
        forbook = ""
        numseason = 0
        seasonlength = 0
        episodes = 0
        stories = 0
    def change():
        which.page = 0
    def book():
        ls = lovestruck()
        # if which.episode > 0:
        # if which.season > 0:

        if which.story > 0:
            ls.storyid = books.stories.sid[which.story-1]
            ls.storytitle = books.stories.title[which.story-1]
            ls.stories = books.stories.forbook[which.story-1]
            ls.numseason = books.stories.numseason[which.story-1]
            ls.seasonlength = books.stories.seasonlength[which.story-1]
            ls.episodes = books.stories.numepisode[which.story-1]
        if which.book > 0:
            ls.stories = len(books.stories.forbook)
            ls.id = books.id[which.book-1]
            ls.title = books.title[which.book-1]
            ls.cover = books.cover[which.book-1]
            ls.bg = books.background[which.book-1]
        return ls


    def looplen():
        if which.season > 0:
            return books.stories.seasonlength[which.story-1]
        elif which.story > 0:
            return books.stories.numseason[which.story-1]
        elif which.book > 0:
            return book().stories
    def timers(x):
        

        print(x)
    def ids(i):
        #if which.episode > 0:
        #    x = [None] * books.numepisode[which.episode-1]
        if which.season > 0:
            return "Valid"
        elif which.story > 0:
            return "Valid"
        elif which.book > 0:
            if books.stories.forbook[i] == book().id:
                return "Valid"
            else:
                return ""
    def tags(tagged):
        if tagged == "Platonic" or tagged == "platonic":
            tagged = "{color=#4FA64F}Platonic{/color}"
        if tagged == "Romantic" or tagged == "romantic":
            tagged = "{color=#FF0054}Romantic{/color}"
        return tagged
    def newqueue():
        global playingsong
        global currentsong
        currentsong += 1
        print(str(currentsong))
        renpy.music.queue(playlist.songs[0], loop = False, fadein = 0.5, clear_queue = True)
        #playingsong = playlist.songs[currentsong]
        
        #renpy.restart_interaction()
screen main_menu():
    $ global homepos
    $ global homeposrange
    $ global menucg
    ## This ensures that any other menu screen is replaced.
    use keynav
    tag menu
    style_prefix "main_menu"
    #$persistent.savegame = ["a"] * 500
    add gui.main_menu_background
    ## This empty frame darkens the main menu.
    #frame:
        #pass
    #$persistent.savegame = ["a"]*500
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    #Radio Handling goes here##########################################

    #python:
        #renpy.music.set_queue_empty_callback(newqueue)
            #renpy.music.queue(playlist.songs, loop = False, fadein = 0.5, clear_queue = True)
        #timer(0.1): 
            #action [Queue("music",playlist.songs, loop = False, fadein = )]

    if persistent.menpos > 0:

        $which.type = persistent.typepos
        $which.book = persistent.menpos
        $which.story = persistent.storypos
        $which.season = persistent.seasonpos
        $which.episode = persistent.episodepos
        $ persistent.typepos = 0
        $ persistent.menpos = 0
        $ persistent.storypos = 0
        $ persistent.seasonpos= 0
        $ persistent.episodepos = 0

    fixed:
        style_prefix "navigation"


        spacing gui.navigation_spacing
        #if renpy.can_load("1-ghost1"): KEEPING THIS SO YOU REMEMBER HOW TO DO THIS
            #imagebutton:
                #idle "hiflcover"
                #action FileLoad("ghost1")
        python:
            ep = "which.episode"
            se = "which.season"
            bo = "which.book"
            st = "which.story"
            wt = "which.type"

            runonce = True

            episodeyreset = 0
            episodex = 0
            seasonyreset = 0
            seasonx = 0
            storyyreset = 0
            storyx = 0
            x = len(books.id)
            xmod = 105
            xmod -= xmod*x
            num = 0
            j = 0
            k = 0
            l = 0
            tempname = " "
            tempdesc = " "
            storynum = 0
            storyextra = 0
            seasonepisode = 0
            ifnew = ""
            newstart = showasnew[3]
            newend = showasnew[4]
            for x in range(40):
                menucg[x] = renpy.random.randint(15, 75)
                menucg[x] = float(menucg[x]*renpy.random.random())
            #x = renpy.random.randint(8,31)
            #menucg[x] = 2
        if main_menu:
            #image "testback"
            #if runonce:
                #timer(0.1): 
                    #action [Play("music", "audio/hifl/vanessahelsing.mp3"), SetScreenVariable("runonce", False)] 
            if which.book == 0:
                image "cgwindow"
                $xi = 0
                #$menucg[10] = 20.0
                #timer 0.1:
                    #action Function(timers,0)
                    #repeat True
                for y in range(5):
                    for x in range(8):
                        image "cgblock" xpos -78 + (x*145) + (x*8) - (4) ypos -50 + (y*80) + y*6 at renpy.random.choice([cg1(menucg[xi]),cg2(menucg[xi]),cg3(menucg[xi]),cg4(menucg[xi]),cg5(menucg[xi]),cg6(menucg[xi])])#cgfade(menucg[xi])
                        $xi += 1

                image "logobackground" xcenter 1040/2 ycenter 150 yanchor 0.5
                image "gui/main_menu_nav.png"
                hbox:
                    ypos 428
                    xpos (520 + xmod)-int(homepos) +(homeposrange/2)
                    for i in books.id:
                        imagebutton:
                            idle books.cover[num]
                            hover books.cover[num] + "hl"
                            action [Play("sound", "audio/sfx/general/catalog_thumbnail.wav"),SetVariable(bo, num+1)]
                            xpos 0 + num*10
                            yanchor 0.5
                            xanchor 0.5
                        python:
                            num += 1
                if len(books.id) > 5:
                    image "gui/balltrack.png":
                        xpos 0
                        ypos 585 - 16
                        yanchor 10
                    bar:
                            ymaximum 30
                            ypos 555
                            xpos 12
                            value FieldValue(store, "homepos", range=homeposrange, style="slider")
                            thumb "gui/mainmenuorb.png"
                            thumb_shadow None

                #textbutton "Start":
                    #ypos 200
                    #action [Play("music", "audio/hifl/vanessahelsing.mp3")]
                #text "Now playing: Helena Theme":
                    #style "jukeboxcolor"
            elif which.book >= 1:
                if which.episode > 0:
                    $tempname = book().storytitle + ": Season " + str(which.season)+", Episode " + str(which.episode)
                    if hasattr(desc, book().storyid +"_season"+str(which.season)+"_episode"+str(which.episode)+"_description"):
                        $tempdesc = getattr(desc, book().storyid +"_season"+str(which.season)+"_episode"+str(which.episode)+"_description")
                    else:
                        $tempdesc = "I haven't written a description yet."
                elif which.season > 0:
                    $tempname = book().storytitle + ": Season " + str(which.season)
                    if hasattr(desc, book().storyid +"_season"+str(which.season)+ "_description"):
                        $tempdesc = getattr(desc, book().storyid +"_season"+str(which.season)+ "_description")
                    else:
                        $tempdesc = "I haven't written a description yet."
                elif which.story > 0:
                    $tempname = book().storytitle
                    $tempdesc = "I haven't written a description yet."
                    if hasattr(desc, book().storyid +"_maincharacters"):
                        $tempdesc = "Starring: "
                        for zz in getattr(desc, book().storyid + "_maincharacters"):
                            $tempdesc += zz
                            $tempdesc += ", "
                        $tempdesc = tempdesc[:-2]
                    if hasattr(desc, book().storyid +"_supportingcharacters"):
                        $tempdesc += "\nWith: "
                        for zz in getattr(desc, book().storyid + "_supportingcharacters"):
                            $tempdesc += zz
                            $tempdesc += ", "
                        $tempdesc = tempdesc[:-2]
                    if hasattr(desc, book().storyid +"_genres"):
                        if len(getattr(desc, book().storyid + "_genres")) > 1:
                            $tempdesc += "\nGenres: "
                        else:
                            $tempdesc += "\nGenre: "
                        for zz in getattr(desc, book().storyid + "_genres"):
                            $tempdesc += zz
                            $tempdesc += ", "
                        $tempdesc = tempdesc[:-2]
                    if hasattr(desc, book().storyid +"_tags"):
                        if len(getattr(desc, book().storyid + "_tags")) > 1:
                            $tempdesc += "\nTags: "
                        else:
                            $tempdesc += "\nTag: "
                        for zz in getattr(desc, book().storyid + "_tags"):
                            #$tempdesc += tags(zz)
                            $tempdesc += zz
                            $tempdesc += ", "
                        $tempdesc = tempdesc[:-2]
                    if hasattr(desc, book().storyid +"_author"):
                        $counter = 0
                        $tempdesc += "\n\nAuthor: "
                        for zz in getattr(desc, book().storyid + "_author"):
                            $tempdesc += "{color=" + getattr(desc, book().storyid + "_colour") + "}"
                            $tempdesc += zz
                            $tempdesc += "{/color}"
                            $tempdesc += ", "
                        $tempdesc = tempdesc[:-2]
                    
                    #if hasattr(desc, book().storyid +"_maincharacters"):
                else:
                    $tempname = book().title
                    if hasattr(desc, book().id +"_description"):
                        $tempdesc = getattr(desc, book().id +"_description")
                    else:
                        $tempdesc = "I haven't written a description yet."
                fixed:
                    imagebutton:
                        idle book().bg
                        action NullAction()
                    image "gui/main_menu_nav2.png"
                #if which.story == 0:
                imagebutton:
                    idle "gui/main_menu_tab_inactive.png"
                    if which.type == False:
                        xpos -17+ 191
                        ypos 283
                            #action [Play("sound","audio/sfx/general/button_generic.wav"),SetVariable(wt, True)]
                    else:
                        xpos -17
                        ypos 283
                            #action [Play("sound","audio/sfx/general/button_generic.wav"),SetVariable(wt, False)]
                imagebutton:
                    idle "gui/main_menu_tab.png"
                    if which.type == False:
                        xpos -17
                        ypos 283
                    else:
                        xpos -17+ 191
                        ypos 283
                textbutton "Canon Routes":
                    ypos 285
                    xpos 21
                    text_style "tabbuttoncolor"
                    if which.type == True:
                        action [Play("sound","audio/sfx/general/button_generic.wav"),SetVariable(wt, False), SetVariable(ep, 0), SetVariable(st, 0), SetVariable(se, 0)]
                textbutton "Custom Routes":
                    ypos 285
                    xpos 21+ 191
                    text_style "tabbuttoncolor"
                    if which.type == False:
                        action [Play("sound","audio/sfx/general/button_generic.wav"),SetVariable(wt, True), SetVariable(ep, 0), SetVariable(st, 0), SetVariable(se, 0)]
                fixed:
                    text tempname style "textbuttonalt":
                        size 20
                        xalign 0.5
                        xanchor 0.5
                        xpos menunamex
                        ypos menunamey
                    text tempdesc style "textbuttonalt":
                        xmaximum 480
                        xpos menudescriptionx
                        ypos menudescriptiony
                    if which.episode > 0:
                        textbutton "Start Episode":
                            text_style "textbuttoncolor"
                            xalign 0.5
                            action [Play("sound","audio/sfx/general/read_story.wav"),SetVariable("whbook", which.book-1),SetVariable("whstory", which.story-1),SetVariable("episode", book().storyid +"_season"+ str(which.season) +"_episode"+ str(which.episode)),SetVariable(bo, -1),\
                            SetVariable("persistent.menpos", which.book),SetVariable("persistent.typepos", which.type), SetVariable("persistent.storypos",which.story),SetVariable("persistent.episodepos",which.episode),\
                            SetVariable("persistent.seasonpos",which.season),SetVariable("savegame", True),Start()]
                            xpos menunamex - 100
                            ypos menunamey + 210
                        if renpy.can_load("1-" + book().storyid +"_season"+ str(which.season) +"_episode"+ str(which.episode)):
                            textbutton "Continue Episode":
                                text_style "textbuttoncolor"
                                xalign 0.5
                                action [SetVariable("persistent.stopauto", True),Play("sound","audio/sfx/general/read_story.wav"),SetVariable("whbook", which.book-1),SetVariable("whstory", which.story-1),SetVariable("episode", book().storyid +"_season"+ str(which.season) +"_episode"+ str(which.episode)),SetVariable(bo, -1),\
                                SetVariable("persistent.menpos", which.book),SetVariable("persistent.typepos", which.type), SetVariable("persistent.storypos",which.story),SetVariable("persistent.episodepos",which.episode),\
                                SetVariable("persistent.seasonpos",which.season),Function(FileLoad(books.stories.sid[which.story-1] +"_season"+ str(which.season) +"_episode"+ str(which.episode)))]
                                xpos menunamex + 100
                                ypos menunamey + 210
                        else:
                            textbutton "Continue Episode":
                                text_style "textbuttoncolor"
                                xalign 0.5
                                xpos menunamex + 100
                                ypos menunamey + 210
                   
                    if which.story == 0:
                        if books.cgcount[which.book-1][0] > 0:
                            imagebutton:
                                xpos 490
                                ypos 560
                                xanchor 0.5
                                yanchor 0.5
                                idle "cg"
                                action [Play("sound","audio/sfx/general/button_generic.wav"),SetVariable("which.gallery", which.book)]
                    imagebutton:
                        xpos 490
                        ypos 340
                        xanchor 0.5
                        yanchor 0.5
                        idle "backbutton"
                        if which.episode > 0:
                            action [Play("sound","audio/sfx/general/close_button.wav"),SetVariable(ep, 0), SetVariable(se, 0)]
                        elif which.season > 0:
                            action [Play("sound","audio/sfx/general/close_button.wav"),SetVariable(se, 0)]
                        elif which.story > 0:
                            action [Play("sound","audio/sfx/general/close_button.wav"),SetVariable(st, 0)]
                        elif which.book > 0:
                            action [Play("sound","audio/sfx/general/close_button.wav"),SetVariable(bo, 0),SetVariable(wt, 0)]
                fixed:
                    default k = 0
                    default j = 0
                    default real = 0
                    default op = ""
                    default optext = ""
                    default whichstyle = "textbuttoncolor"
                    $ofnew = shownew
                    $counter = 1000 #arbitrarily high.
                    if which.season>0:
                        $counter = books.stories.numepisode[which.story-1]-(books.stories.seasonlength[which.story-1]*(which.season-1))
                    for j in range(looplen()):
                        $m = ids(j)
                        #If the story is valid
                        if real > menulistlength-1:
                            $ storyyreset = (real*menuspacing)
                            $ storyyreset -= ((real%(menulistlength))*menuspacing)
                            $ storyx = (real/menulistlength)*menuxspacing
                        
                        $print(storyx)   
                        #$m = ids(j)
                        $tagchecked = "show"
                        if which.story == 0:
                            $tagchecked = ""
                            for tagcheck in getattr(desc, books.stories.sid[j]+ "_tags"):
                                if tagchecked == "":
                                    #if tagcheck == "Custom Route":
                                        #if which.type == False:
                                            #$tagchecked = "noshow"
                                        #else:
                                            #$tagchecked = "show"
                                    if tagcheck == "Official Route":
                                        if which.type == False:
                                            $tagchecked = "show"
                                        else:
                                            $tagchecked = "noshow"
                            if tagchecked == "":
                                if which.type == False:
                                    $tagchecked = "noshow"
                                else:
                                    $tagchecked = "show"
                        if m != "" and tagchecked == "show":
                            $real += 1
                            $ ofnew = shownew
                            if which.season > 0:
                                $wh = "which.episode"
                                $tex = "Episode " + str(j+1)
                                $optext = book().storyid + "_season" + str(which.season) + "_episode" + str(j+1)
                            elif which.story > 0:
                                $wh = "which.season"
                                $optext = book().storyid + "_season" + str(j+1)
                                $tex = "Season " + str(j+1)
                            elif which.book > 0:
                                $wh = "which.story"
                                $optext = books.stories.sid[j]
                                $ tex = books.stories.title[j]
                                if len(tex) >= 16:
                                    $tex = tex[:16]
                                    $tex += "..."
                                #if books.stories.tag[j] == 1:
                                    #$whichstyle = "officialstorycolor"
                                #if books.stories.tag[j] == 2:
                                    #$whichstyle = "archivestorycolor"
                                if hasattr(desc, books.stories.sid[j] +"_style"):
                                    $whichstyle =  getattr(desc, books.stories.sid[j] +"_style")
                            $countvar = 0
                            for op in persistent.savegame:
                                if op.find(optext) > -1:
                                    #$print ("optext: "+optext)
                                    $countvar += 1
                            if which.season>0:
                                if countvar > 0:
                                    $ofnew = ""
                            elif which.story>0:
                                #$print(books.stories.numepisode[which.story])
                                if books.stories.numepisode[which.story-1] < book().seasonlength*(j+1):
                                    $tt = books.stories.numepisode[which.story-1]
                                    $tt -= book().seasonlength*j
                                    if countvar >= tt:
                                        $ofnew = ""
                                    #$print (tt)
                                else:
                                    #$print ("Season is full")
                                    if countvar >= book().seasonlength:
                                        $ofnew = ""
                            elif which.book > 0:
                                if countvar >= books.stories.numepisode[j]:
                                    $ofnew = ""
                            fixed:
                                ypos menuoptionsypos + (menuspacing*k) -storyyreset
                                xpos storyx
                                if counter > 0:
                                    textbutton tex + ofnew:
                                        text_style whichstyle
                                        action [Play("sound","audio/sfx/general/button_generic.wav"),SetVariable(wh, j+1)]
                                    $whichstyle = "textbuttoncolor"
                            $k += 1
                            $counter -= 1
                    $real = 0
            fixed:
                #image "radiowidget"
                #text "Now Playing: " + playingsong
                #imagebutton:
                    #xpos 990
                    #xanchor 50
                    #idle "radio_icon"
                    #action [Play("sound","audio/sfx/general/button_generic.wav"),ToggleVariable("settingsscreen")]
                imagebutton:
                    xpos 1040
                    xanchor 50
                    idle "settings_icon"
                    action [Play("sound","audio/sfx/general/button_generic.wav"),ToggleVariable("settingsscreen")]
                    #fixed:
            #fixed:
                #imagebutton:
                    #xpos 985
                    #xanchor 50
                    #idle "radio_icon"
                    #action [Play("sound","audio/sfx/general/button_generic.wav"),ToggleVariable("settingsscreen")]
                    #fixed:
            
            if which.gallery > 0:
                
                imagebutton:
                    idle "gui/gallery_menu_nav.png"
                    ypos 102
                    action (NullAction())
                vbox:
                    spacing 2
                    for x in range(len(books.cgnames[which.book-1])):
                        $cgname = books.cgnames[which.book-1][x]
                        $cgname = cgname.capitalize()
                        textbutton cgname:
                            #text_style "gallerybuttoncolor"
                            xpos 2
                            ypos 55 + 45
                            action (SetVariable("which.gallerychar", x), Function(change),Play("sound","audio/sfx/general/button_generic.wav"))
                vbox:
                    for x in reversed(range(10)):
                        if x*16 < books.cgcount[which.book-1][which.gallerychar]:
                            textbutton (str(x+1)): 
                                #text_style "gallerybuttoncolor"
                                xpos 200
                                ypos 445 + 45
                                action (SetVariable("which.page", x),Play("sound","audio/sfx/general/button_generic.wav"))
                imagebutton:
                        xpos 195
                        ypos 80 + 45
                        xanchor 0.5
                        yanchor 0.5
                        idle "backbutton" 
                        action (SetVariable("which.gallery", 0), SetVariable("which.page", 0), SetVariable("which.gallerychar", 0),Play("sound","audio/sfx/general/close_button.wav"))
                hbox:
                    xoffset 300
                    yoffset 50 + 45
                    spacing 5
                    #This will show the screen gallery_navigation from gallery_navigation.rpy
                    #use gallery_navigation



                    # This is a grid containing 2 columns and 2 rows.
                    $xc = 0
                    $yc = 0
                    $xp = books.cgx[0]
                    $yp = books.cgy[0]
                    if which.page == 0:
                        $gp = 1
                    else:
                        $gp = which.page*16
                        $gp += 1
                    grid 4 4:
                        for x in range(16):
                            if gp <= books.cgcount[which.book-1][which.gallerychar]:
                                add g.make_button(books.cgnames[which.book-1][which.gallerychar] +str(gp), im.Scale("images/CGs/"+books.cgnames[which.book-1][which.gallerychar]+"/smalls/"+books.cgnames[which.book-1][which.gallerychar] +str(gp)+".webp", 195, 110) , locked = im.Scale("images/buttons/"+books.cgnames[which.book-1][which.gallerychar]+".png", 195, 110), xpos=xp, ypos=yp)
                                $gp += 1
                            else:
                                add g.make_button(books.cgnames[which.book-1][which.gallerychar] +"null", im.Scale("images/CGs/"+books.cgnames[which.book-1][which.gallerychar]+"/smalls/"+books.cgnames[which.book-1][which.gallerychar] +"null"+".png", 195, 110) , locked = im.Scale("images/CGs/"+books.cgnames[which.book-1][which.gallerychar]+"/smalls/"+books.cgnames[which.book-1][which.gallerychar] +"null"+".png", 195, 110), xpos=-66, ypos=16)
                            $xc += 1
                            if xc == 4:
                                $xc = 0
                                $yc += 1
                            if yc <= 3:
                                $xp = books.cgx[xc]
                                $yp = books.cgy[yc] 

                        

            if settingsscreen:
                fixed:
                    imagebutton:
                        idle "settingsnew"
                        xcenter 520
                        ycenter 293
                        action NullAction()
                    imagebutton:
                        idle "settingsorbblank"
                        xcenter 945
                        ycenter 72
                        action [Play("sound","audio/sfx/general/close_button.wav"),ToggleVariable("settingsscreen")]
                    fixed:
                        xcenter 643
                        ycenter 625
                        xmaximum 568
                        imagebutton:
                            if preferences.fullscreen:
                                idle "checkmark"
                                action Preference("display", "window")
                            else:
                                idle "nocheckmark"
                                action Preference("display", "fullscreen")
                            #action [ToggleVariable("persistent.prompt")]
                            xcenter 18
                            ycenter -56
                        imagebutton:
                            if persistent.borders:
                                idle "checkmark"
                            else:
                                idle "nocheckmark"
                            action ToggleVariable("persistent.borders")
                            xcenter 18
                            ycenter -17
                        bar:
                            ymaximum 30
                            ypos 4
                            xpos 12
                            value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider")
                            thumb "gui/slider/orb.png"
                            thumb_shadow None
                        bar:
                            ymaximum 30
                            ypos 44
                            xpos 12
                            value Preference("music volume")
                            thumb "gui/slider/orb.png"
                            thumb_shadow None
                        bar:
                            ymaximum 30
                            ypos 82
                            xpos 12
                            value Preference("sound volume")
                            thumb "gui/slider/orb.png"
                            thumb_shadow None
                        textbutton "Quit Game":
                            text_style "quitbuttoncolor"
                            xpos  165
                            ypos 130
                            action Quit(True)
                            xalign 0.5
        
                #         if which.story == 0:
                #             for i in books.stories.forbook:
                #                 if i == books.id[which.book-1]:
                #                     $ lfnew = ""
                #                     $ storynum += storyextra
                #                     if books.id[which.book-1] == showasnew[0]:
                #                         if books.stories.sid[storynum] == showasnew[1]:
                #                             $lfnew = shownew
                #                     if which.season == 0:
                #                         if j > menulistlength-1:
                #                             $ storyyreset = (j*menuspacing)
                #                             $ storyyreset -= ((j%(menulistlength))*menuspacing)
                #                             $ storyx = (j/menulistlength)*menuxspacing
                #                         textbutton books.stories.title[storynum] + lfnew:
                #                             xpos storyx
                #                             ypos menuoptionsypos + (j*menuspacing) - storyyreset
                #                             text_style "textbuttoncolor"
                #                             action [SetVariable(st, storynum+1)]
                #                     else:
                #                         textbutton books.stories.title[storynum] + lfnew:
                #                             xpos storyx
                #                             ypos menuoptionsypos + (j*menuspacing) - storyyreset
                #                             text_style "textbuttoncolor"
                #                             action [SetVariable(st,1),SetVariable(st, storynum+1)]
                #                     $j += 1
                #                     $ storynum += 1
                #                     $ storyextra = 0
                #                 else:
                #                     $ storyextra += 1
                # if which.story >= 1:
                #     fixed:
                #         if which.season == 0:
                #             for i in range(0, books.stories.numseason[which.story-1]):
                #                 $ ofnew = ""
                #                 if books.id[which.book-1] == showasnew[0]:
                #                     if books.stories.sid[which.story-1] == showasnew[1]:
                #                         if i+1 == showasnew[2]:
                #                             $ofnew = shownew
                #                 if l > menulistlength-1:
                #                     $ seasonyreset = (l*menuspacing)
                #                     $ seasonyreset -= ((l%(menulistlength))*menuspacing)
                #                     $ seasonx = (l/menulistlength)*menuxspacing
                #                 textbutton "Season " + str(i+1) + ofnew:
                #                     xpos seasonx
                #                     ypos menuoptionsypos + (l*menuspacing) - seasonyreset
                #                     text_style "textbuttoncolor"
                #                     action SetVariable(se, i+1)
                #                 $ l += 1
                # if which.season >= 1:
                #     fixed:
                #         for i in range(books.stories.seasonlength[which.story-1]*(which.season-1), books.stories.seasonlength[which.story-1]+books.stories.seasonlength[which.story-1]*(which.season-1)):
                #             if i < books.stories.seasonlength[which.story-1]:
                #                 $ seasonepisode = i
                #             else:
                #                 $ seasonepisode = i-(books.stories.seasonlength[which.story-1]*(which.season-1))
                #             $seasonepisode = seasonepisode +1
                #             $ ifnew = ""
                #             if books.stories.numepisode[which.story-1] > i:
                #                 if books.id[which.book-1] == showasnew[0]:
                #                     if books.stories.sid[which.story-1] == showasnew[1]:
                #                         if which.season == showasnew[2]:
                #                             if seasonepisode >= newstart:
                #                                 if seasonepisode <= newend:
                #                                     $ ifnew = shownew
                #                 if k > menulistlength-1:
                #                     $ episodeyreset = (k*menuspacing)
                #                     $ episodeyreset -= ((k%(menulistlength))*menuspacing)
                #                     $episodex = (k/menulistlength)*menuxspacing
                #                 textbutton "Episode " + str(seasonepisode) + ifnew:
                #                     xpos episodex
                #                     ypos menuoptionsypos + (k*menuspacing) - episodeyreset
                #                     text_style "textbuttoncolor"
                #                     # action [SetVariable("episode", books.stories.sid[which.story-1] +"_season"+ str(which.season) +"_episode"+ str(seasonepisode)),SetVariable("which.book", -1),\
                #                     # SetVariable("persistent.menpos", 1), SetVariable("persistent.storypos",which.story),\
                #                     # SetVariable("persistent.seasonpos",which.season),Start()]
                #                     action SetVariable(ep, seasonepisode)
                #             else:
                #                 if k > menulistlength-1:
                #                     $ episodeyreset = (k*menuspacing)
                #                     $ episodeyreset -= ((k%(menulistlength))*menuspacing)
                #                     $episodex = (k/menulistlength)*menuxspacing
                #                 textbutton "Episode " + str(seasonepisode):
                #                     xpos episodex
                #                     ypos menuoptionsypos + (k*menuspacing) - episodeyreset
                #                     text_style "textbuttoncolor"
                #             $ k += 1
            # textbutton "menpos":
            #     xpos 100
            #     ypos 0
            #     action [SetVariable("persistent.menpos", 0), SetVariable("persistent.storypos", 0)]


    #if gui.show_name:

        vbox:
            #text "[config.name!t]":
                #style "main_menu_title"
            xpos 5
            ypos 562
            #text "[config.version]" color "ffffff":
                #style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 228
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -16
    xmaximum 650
    yalign 1.0
    yoffset -16

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


##Gallery stuff
screen gallery():
    modal True
    image "gui/gallery_menu_nav.png"
    textbutton "Antonio":
        action Show("galleryF")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            #frame:
                #style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    imagebutton:
        idle "settingsorb"
        xcenter 957
        ycenter 50
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 25
    top_padding 98

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 228
    yfill True

style game_menu_content_frame:
    left_margin 33
    right_margin 17
    top_margin 9

style game_menu_viewport:
    xsize 748

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 9

style game_menu_label:
    xpos 41
    ysize 98

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -24


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 41
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 183

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 285

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 366


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html
define lastwhat = " "
screen history():
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_(" "), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
            if what != lastwhat:
                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    #$ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                    $ lastwhat = what

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 13

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 204
    right_padding 17

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):
    #$print (message)
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    fixed:
        image  "images/general/icons/small_dialog_base.png" xcenter 520 ycenter 292
        vbox:

            xalign .5
            yalign .5
            spacing 25

            label _("Seriously quit?"):
                text_style "quitmessagecolor"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 82
                #if message == "Are you sure you want to quit?":
                textbutton _("Yes"):
                    text_style "textbuttoncolor"
                    action [SetVariable("persistent.menpos", 0),\
                    SetVariable("persistent.storypos", 0),\
                    SetVariable("persistent.seasonpos", 0),SetVariable("persistent.episodepos",0), yes_action]
                textbutton _("No") text_style "textbuttoncolor" action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 5

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 366

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 277

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 325

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 488
