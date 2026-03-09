define hiddenonce = False
define rolledback = False
define p = -598#-558 #Menu buttons default height
default persistent.showframe = True
define autoplaystate = 0
define autoplaytint = 1.0
define autoplaytintdown = True
define increaseautoplay = False
define menustuck = False
define menux = 1520
default istextvisible = True
default menuhideborder = False
default tbc = False
default activefn = -1
default activeln = -1
default editchoice = -1
init python:

    class playername(NoRollback):
        def __init__(self):
            self.name = " "
            self.ln = " "

    import pygame
    didmousemove = False
    i = False
    highlightoption = 0
    def resets():
        global hidetextbox
        finished = persistent.savegame
        found = False
        say = ""
        preferences.afm_enable = False
        for j in range(len(finished)):
            if finished[j] == "a":
                for l in range(len(finished)):
                    if finished[l] == episode:
                        found = True
                        break
                if found == False:
                    finished[j] = episode
                    persistent.savegame = finished
                    break
                break
        renpy.unlink_save("1-" + episode)
        hideborders = True
        hidetextbox = False
        #persistent.episodepos += 1


    def hidescreen(open):
        global hiddenonce
        global hidetextbox
        global istextvisible
        if hidetextbox:
            if open:
                hiddenonce = True
                renpy.hide_screen("say")
                renpy.config.rollback_enabled = False
                #istextvisible = False

            else:
                if hiddenonce:
                    if renpy.store._last_say_what != "":
                        renpy.show_screen("say",renpy.store._last_say_who, renpy.store._last_say_what)
                        #gui.rebuild()
                        if renpy.store._last_say_who != None:
                            renpy.say( eval(renpy.store._last_say_who), renpy.store._last_say_what, interact=False)
                        else:
                            renpy.say(renpy.store._last_say_who, renpy.store._last_say_what, interact=False)
                        renpy.config.rollback_enabled = True
                        #istextvisible = True
                        hiddenonce = False;
            return
    def choiceedit():
        global editchoice
        editchoice = 0
    def tobecontinued():
        global tbc
        renpy.store._last_say_who = ""
        renpy.store._last_say_what = ""
        _window_hide() 
        tbc = True
    def findname():
        global genericfn
        global genericln
        genericfn = books.names[str(books.stories.sid[whstory]) + "fn1"]
        genericln = books.names[str(books.stories.sid[whstory]) + "ln1"]
        
        NullAction()
    def setname():
        #mcdata.mcnames.update(books.names)
        mcdata.mcnames = books.names
        mcdata.save()
    def prompttoggle():
        global ctcimage
        #if persistent.prompt == True:
        #    ctcimage = "images/general/icons/dialogue_prompt.png"
        #else:
        #    ctcimage = "images/general/icons/dialogue_noprompt.png"

    def autoplayflicker():
        global autoplaytint
        global autoplaytintdown
        global autoplaystate
        if autoplaystate > 0:
            if persistent.stopauto == True:
                persistent.stopauto = False
                autoplaystate = 0
            if autoplaytintdown:
                autoplaytint -= 0.1
                if autoplaytint < 0.6:
                    autoplaytint = 0.6
                    autoplaytintdown = False

            else:
                autoplaytint += 0.1
                if autoplaytint > 1:
                    autoplaytint = 1.0
                    autoplaytintdown = True


        return
    def checkname():                 ##########WILL HAVE TO BE UPDATED FOR EVERY NEW BOOK DO NOT FORGET ABOUT THIS IT'S IMPORTANT AAAAAAHHHHH
        NullAction()
    def setautoplay(override):
        global autoplaystate
        global rolledback

        if override < 0:
            if override == -1:
                if autoplaystate<10:
                    autoplaystate += 1
                    preferences.afm_enable = True
                else:
                    autoplaystate = 1
                    preferences.afm_enable = True
            elif override == -2:
                autoplaystate = 10
                preferences.afm_enable = True
            elif override == -3:
                autoplaystate = 1
                preferences.aft_enable = True
            elif override == -4:
                autoplaystate = 3
            if autoplaystate == 1:
                preferences.afm_time = 18
            elif autoplaystate == 2:
                preferences.afm_time = 10
            elif autoplaystate == 3:
                preferences.afm_time = 9
            elif autoplaystate == 10:
                preferences.afm_time = 1
            #preferences.afm_after_click = False
            if autoplaystate >=4:
                if autoplaystate < 10:
                    autoplaystate = 1
                    #preferences.afm_enable = False
        elif override == 0:
            autoplaystate = 0
            preferences.afm_enable = False
        elif override == 1:
            preferences.afm_enable = False
        elif override == 2:
            if autoplaystate>0:
                preferences.afm_enable = True
        if (renpy.in_rollback()):
            if rolledback == False:
                rolledback = True
                i = False
                preferences.afm_enable = False
                autoplaystate = 0

        else:
            rolledback = False

        #renpy.restart_interaction()
        if autoplaystate == 0:

            preferences.afm_enable = False
        return
    #def mousemoved():
        #global didmousemove
        #didmousemove = True
screen keynav:
    $global i
    $global autoplaystate
    $global didmousemove
    if main_menu:
        $NullAction()
        #$print("Only in menu")
    else:
        if autoplaystate > 0:
            key "K_SPACE" action [Function(setautoplay, 0)]
            key "K_LEFT" action [Function(setautoplay, 0)]
            key "K_RIGHT" action [Function(setautoplay, 0)]
            key "K_ESCAPE" action [Function(setautoplay, 0)]
        else:
            key "K_ESCAPE" action [SetVariable("highlightoption", 0),ToggleVariable("i"),checkname()]
    #if pygame.mouse.get_rel()[0] != 0.0:
        #$didmousemove = True
    #elif pygame.mouse.get_rel()[1] != 0.0:
        #$didmousemove = True
    #if pygame.KEYDOWN:
        #$didmousemove = False

screen navi:
    $global i
    $global autoplaystate
    if main_menu:
        $NullAction()
    else:
        if i:
            $NullAction()
        else:
            key 'K_UP' action Function(setautoplay, -1)
            key 'K_DOWN' action Function(setautoplay, 0)
            key 'K_RCTRL' action Function(setautoplay, -4)


screen gamemenu():
    #bar value Preference("sound volume")
    $global editchoice
    default startmenupos = 2
    $global highlightoption
    $global didmousemove
    $global activefn
    $global activeln
    $global tbc
    $global refresh
    $global genericfn
    use keynav
    #if didmousemove == False:
    use navi
    predict False
    $ menupos = 1
    default firstrun = True
    default jumptolabel = False
    #default i = False
    default settings_open = False
    default nameedit_open = False
    default nameedit_state = 0
    default log_open = False
    default textspeed = 35

    if i == True:
        $istextvisible = False
    else:
        if persistent.borders == True:
            $istextvisible = True
    if hideborders == True:
        $istextvisible = False
    if savegame == True:
        timer 0.01:
            #renpy.save(episode, confirm = False)
            action [SetVariable("savegame", False),FileSave(episode, confirm = False)]
    if autoplaystate != 10:
        $ preferences.text_cps = textspeed
    else:
        $ preferences.text_cps = 0
    zorder 10
    if i:
        $ config.rollback_enabled = False
        $hidescreen(i)
        #timer 0.001:
            ##repeat True
            #action [Function(hidescreen,i)]
        timer 0.001:
            #repeat True
            action [Function(setautoplay, 1)]
    else:
        $ config.rollback_enabled = True
        $hidescreen(i)
        timer 0.1:
            repeat True
            action [Function(setautoplay, 2)]
    $autoplayflicker()
    $findname()
    #$print(genericfn)
    python:            ##########WILL HAVE TO BE UPDATED FOR EVERY NEW BOOK DO NOT FORGET ABOUT THIS IT'S IMPORTANT AAAAAAHHHHH
        if firstrun:
            #findname()
            firstrun = False
            if len(books.names[str(books.stories.sid[whstory]) + "fn1"]) > 10:
                nameedit_open = True
            #if whbook == 0:
                #if mcdata.hifl_fn is None:
                    #nameedit_open = True
                #genericfn = hifl_fn
                #genericln = hifl_ln
            #elif whbook == 1:
                #if mcdata.vn_fn is None:
                   #nameedit_open = True
                #genericfn = vn_fn
                #genericln = vn_ln
    fixed:

        xcenter 0
        fixed:
            if autoplaystate>0:
                if i == False:
                    if not renpy.get_screen("choice"):
                        vbox:
                            imagebutton:
                                idle "clicktoquit"
                                xcenter 1000
                                ycenter 300
                                #action Function(setautoplay, -1)
                                action Function(setautoplay, 0)
            image(ConditionSwitch(
            "autoplaystate == 0", "autoplay0",
            "autoplaystate == 1", books.id[whbook] +"autoplay1",
            "autoplaystate == 2", books.id[whbook] +"autoplay2",
            "autoplaystate == 3", books.id[whbook] +"autoplay3",
            "autoplaystate == 10", books.id[whbook] +"ff1")):
                at uizoomone
                alpha 0.5
                xcenter 630
                ycenter 75
            if autoplaystate > 0:
                imagebutton:
                    idle (ConditionSwitch(
                        "autoplaystate == 0", im.MatrixColor("images/general/backgrounds/autoplay0.png",im.matrix.tint(0.9, 0.9, 1.0,)),
                        "autoplaystate == 1", im.MatrixColor("images/"+books.id[whbook] +"/ui/"+books.id[whbook] +"autoplay1.png",im.matrix.tint(autoplaytint, autoplaytint, autoplaytint)),
                        "autoplaystate == 2", im.MatrixColor("images/"+books.id[whbook] +"/ui/"+books.id[whbook] +"autoplay2.png",im.matrix.tint(autoplaytint, autoplaytint, autoplaytint)),
                        "autoplaystate == 3", im.MatrixColor("images/"+books.id[whbook] +"/ui/"+books.id[whbook] +"autoplay3.png",im.matrix.tint(autoplaytint, autoplaytint, autoplaytint)),
                        "autoplaystate == 10", im.MatrixColor("images/"+books.id[whbook] +"/ui/"+books.id[whbook] +"ff1.png",im.matrix.tint(autoplaytint, autoplaytint, autoplaytint))))
                    at uizoomone
                #idle ConditionSwitch(

                    xcenter 630
                    ycenter 75
                    action Function(setautoplay, -1)

        vbox:
            imagebutton:
                idle "noadvance"
                xcenter 2300
                if i:
                    at noadvon
                else:
                    at advon
                action [SetVariable("highlightoption", 0),ToggleVariable("i"),Function(hidescreen,i)]
    python:
        textmod = 2
        textsize = 45
        #whbook
        s = books.names[books.stories.sid[whstory] + "fn1"]
        n = len(s)
        s = books.names[books.stories.sid[whstory] + "ln1"]
        m = len(s)
        if m>n:
            n = m
        if (textsize-(n*textmod))<1:
            n = 16
    #$print("Book number: "+str(whbook))
    fixed:
        xcenter menux
        if i:
            at slidein

        else:
            at slideout
            #$highlightoption = 0
        if i:
            ##Essentially dummies out the keyboard menu support for now.
            $highlightoption = 0

            if settings_open == False and nameedit_open == False:
                key 'K_SPACE' action ToggleVariable("i")
                key 'K_RIGHT' action ToggleVariable("i")
                if highlightoption == 0:
                    key 'K_DOWN' action SetVariable("highlightoption", startmenupos)
                    key 'K_UP' action SetVariable("highlightoption", startmenupos)
                elif highlightoption == 1:
                    key 'K_DOWN' action [SetVariable("highlightoption", highlightoption + 1),SetScreenVariable("startmenupos", highlightoption + 1)]
                elif highlightoption < 7 and highlightoption >1:
                    key 'K_DOWN' action [SetVariable("highlightoption", highlightoption + 1),SetScreenVariable("startmenupos", highlightoption + 1)]
                    key 'K_UP' action [SetVariable("highlightoption", highlightoption - 1),SetScreenVariable("startmenupos", highlightoption -1)]
                else:
                    key 'K_UP' action SetVariable("highlightoption", highlightoption -1)
                    if highlightoption < 1:
                        $highlightoption = 1
                if highlightoption == 1:
                    if nameedit_open == False:
                        key 'K_z' action [SetScreenVariable("nameedit_state", 1),ToggleScreenVariable("nameedit_open")]
                elif highlightoption == 2:
                    key 'K_z' action [ShowMenu("history"), ToggleVariable("i")]
                elif highlightoption == 3:
                    key 'K_z' action [Function(setautoplay, -3), ToggleVariable("i")]
                elif highlightoption == 4:
                    key 'K_z' action [Function(setautoplay, -2), ToggleVariable("i")]
                elif highlightoption == 5:
                    key 'K_z' action [ToggleScreenVariable("settings_open")]
                elif highlightoption == 6:
                    key 'K_z' action [Play("sound","audio/sfx/general/button_generic.wav"),FileSave(episode, confirm = False)]
                elif highlightoption == 7:
                    key 'K_z'action [Play("sound","audio/sfx/general/hud_back_home.wav"),MainMenu(confirm = False)]
        vbox:
            image books.id[whbook] + "menu" at uizoomone
            fixed:
                imagebutton:
                    if highlightoption == 1:
                        idle books.id[whbook] +"nameedithl"
                    else:
                        idle books.id[whbook] +"nameedit"
                    #at uizoomone
                    action [SetScreenVariable("nameedit_state", 1),ToggleScreenVariable("nameedit_open")]
                    xcenter 205
                    ycenter -550
            fixed:
                text books.names[str(books.stories.sid[whstory]) + "fn1"]:
                    font "images/general/fonts/Ranchers-Regular.ttf"
                    size textsize-(n*textmod)
                    color books.namecolor[whbook]
                    yalign 0.5
                    xalign 0
                xcenter 590
                ycenter -540
            fixed:
                text books.names[str(books.stories.sid[whstory]) + "ln1"]:
                    font "images/general/fonts/Ranchers-Regular.ttf"
                    color books.namecolor[whbook]
                    size textsize-(n*textmod)
                    yalign 0.5
                    xalign 0
                xcenter 590
                ycenter -490
            vbox:
                if not renpy.get_screen("choice"):
                    imagebutton:
                        idle "openmenu"
                        at uizoomone
                        xcenter 23
                        ycenter -515
                        action [SetVariable("persistent.stopauto", False),SetVariable("highlightoption", 0),ToggleVariable("i"), Function(setautoplay, 0), Function(hidescreen,i),checkname()]
            vbox:
                imagebutton:
                    xcenter 142
                    ycenter p
                    if highlightoption == 2:
                        idle books.id[whbook] +"loghl"
                    else:
                        idle books.id[whbook] +"log"
                    at uizoomone
                    action [ShowMenu("history"), ToggleVariable("i")]
            if i == True:
                vbox:
                    imagebutton:
                        xcenter 142
                        ycenter p+3
                        if highlightoption == 3:
                            idle books.id[whbook] +"autoplayhl"
                        else:
                            idle books.id[whbook] +"autoplay"
                        at uizoomone
                        action [Function(setautoplay, -3), ToggleVariable("i")]
            else:
                vbox:
                    imagebutton:
                        xcenter 142
                        ycenter p+3
                        idle books.id[whbook] +"autoplay"
                        at uizoomone
                        #hover "hiflautoplayhover"
                        #action SetVariable("autoplaystate", True)
                        #action [Function(setautoplay, -1), ToggleScreenVariable("i")]

                    #action SetVariable("preferences.auto-forward", True)
            if i == True:

                vbox:
                    imagebutton:
                        xcenter 142
                        ycenter p+6
                        if highlightoption == 4:
                            idle books.id[whbook] +"ffhl"
                        else:
                            idle books.id[whbook] +"ff"
                        at uizoomone
                        action [Function(setautoplay, -2), ToggleVariable("i")]
            else:
                vbox:
                    imagebutton:
                        xcenter 142
                        ycenter p+6
                        idle books.id[whbook] +"ff"
                        at uizoomone
                        action NullAction()
                        #action [Function(setautoplay, -2), ToggleScreenVariable("i")]
            vbox:
                imagebutton:
                    xcenter 142
                    ycenter p+10
                    if highlightoption == 5:
                        idle books.id[whbook] +"settingshl"
                    else:
                        idle books.id[whbook] +"settings"
                    at uizoomone
                    action [ToggleScreenVariable("settings_open")]
            vbox:
                imagebutton:
                    xcenter 142
                    ycenter p+12
                    if highlightoption == 6:
                        idle books.id[whbook] +"savehl"
                    else:
                        idle books.id[whbook] +"save"
                    at uizoomone
                    action [Play("sound","audio/sfx/general/button_generic.wav"), Notify("Game Saved"),FileSave(episode, confirm = False)]
            vbox:
                imagebutton:
                    xcenter 142
                    ycenter p+16
                    if highlightoption == 7:
                        idle books.id[whbook] +"homehl"
                    else:
                        idle books.id[whbook] +"home"
                    at uizoomone
                    action [Play("sound","audio/sfx/general/hud_back_home.wav"),MainMenu(confirm = False)]
    if istextvisible == True:
        if menuhideborder == False:
            if tbc == False:
                fixed:
                    xpos 0
                    ypos 436
                    image books.id[whbook] +"lframe" zoom 0.608
                fixed:
                    xpos 1040-55
                    ypos 436
                    image books.id[whbook] +"rframe" zoom 0.608
    #if log_open:
        #fixed:
            #text "s"
    #$print(whbook)
    if nameedit_open:
        #if key 'K_ESCAPE':
            #nameedit_open = False
        #$print(books.stories.sid[whstory])
        #if activeln < 0 and activefn < 0:
            #key "K_ESCAPE" action [SetScreenVariable("nameedit_open", False),SetVariable("editchoice", -1)] 
        if books.stories.nameablecharacters[whstory] == 1:
            $editchoice = 0
        fixed:
            imagebutton:
                idle books.id[whbook] +"_nameinputbg"
                at uizoomone
                xcenter 520
                ycenter 585/2
                action NullAction()
                
        if editchoice != -1:
            fixed:
                # text "ENTER THEIR NAME":
                #     xcenter 1040/2
                #     ycenter 90
                #     style books.id[whbook] + "name"
                #     #font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
                #     size 70
                #     outlines [ (1, "#000", 1, 1) ]
                # text "FIRST NAME":
                #     xcenter 520 - 200
                #     ycenter 180
                #     size 50
                #     style books.id[whbook] + "name"
                #     #font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
                #     outlines [ (1, "#000", 1, 1) ]
                #     xanchor 0.5
                # text "LAST NAME":
                #     xcenter 520 + 200
                #     ycenter 180
                #     size 50
                #     style books.id[whbook] + "name"
                #     #font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
                #     outlines [ (1, "#000", 1, 1) ]
                #     xanchor 0.5
                if len(books.names[books.stories.sid[whstory] + "fn" + str(editchoice+1)]) < 11 and len(books.names[books.stories.sid[whstory] + "ln" + str(editchoice+1)]) < 11:
                    imagebutton:
                        idle books.id[whbook] + "ok"
                        at uizoomone
                        xcenter 1040/2
                        ycenter 585/2 + 80
                        if books.stories.nameablecharacters[whstory] != 1:
                            if activeln < 0 and activefn < 0:
                                action (SetVariable("editchoice", -1))
                        else:
                            action [SetScreenVariable("nameedit_open", False)]
                imagebutton:
                        idle books.id[whbook] + "fn"
                        at uizoomone
                        xcenter 520 - 203
                        ycenter 189
                        xanchor 0.5
                        action [SetVariable("activefn", editchoice), SetVariable("activeln", -1), SetVariable("tempfn", "")]
                imagebutton:
                        idle books.id[whbook] + "ln"
                        at uizoomone
                        xcenter 520 + 197
                        ycenter 189
                        xanchor 0.5
                        action [SetVariable("activeln", editchoice), SetVariable("activefn", -1), SetVariable("templn", "")]
                if activeln < 0:
                    textbutton books.names[books.stories.sid[whstory] + "ln" + str(editchoice+1)]:
                        xcenter 520 + 200
                        ycenter 212
                        text_color books.inactivenamecolor[whbook]
                        xanchor 0.5
                else:
                    if activeln >-1:
                        input:
                            value VariableInputValue("templn")
                            length 10
                            color books.activenamecolor[whbook]
                            xcenter 520 + 200
                            ycenter 212
                            xanchor 0.5
                        if templn != "":
                            key "K_TAB" action [SetVariable("activefn", 1),SetVariable("activeln", -1), SetDict(books.names,books.stories.sid[whstory] + "ln" + str(editchoice+1), templn),Function(setname),SetVariable("tempfn", "")] 
                            key "K_RETURN" action [SetVariable("activeln", -1), SetDict(books.names,books.stories.sid[whstory] + "ln" + str(editchoice+1), templn),Function(setname)] 
                if activefn < 0:
                    textbutton books.names[books.stories.sid[whstory] + "fn" + str(editchoice+1)]:
                        xcenter 520 - 200
                        ycenter 212
                        text_color books.inactivenamecolor[whbook]
                        xanchor 0.5
                else:
                    if activefn >-1:
                        input:
                            value VariableInputValue("tempfn")
                            length 10
                            xcenter 520 - 200
                            color books.activenamecolor[whbook]
                            ycenter 212
                            xanchor 0.5
                        if tempfn != "":
                            key "K_TAB" action [SetVariable("activeln", 1),SetVariable("activefn", -1), SetDict(books.names,books.stories.sid[whstory] + "fn" + str(editchoice+1), tempfn),Function(setname),SetVariable("templn", "")] 
                            key "K_RETURN" action [SetVariable("activefn", -1), SetDict(books.names,books.stories.sid[whstory] + "fn" + str(editchoice+1), tempfn),Function(setname)] 
        else:
            
            
            fixed:
                imagebutton:
                    idle books.id[whbook] +"_charchoicebg"
                    at uizoomone
                    xcenter 520
                    ycenter 585/2
                    action NullAction()
                # text "SELECT A CHARACTER":
                #     xcenter 1040/2
                #     ycenter 90
                #     #font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
                #     style books.id[whbook] + "name"
                #     size 70
                #     outlines [ (1, "#000", 1, 1) ]
                if len(books.names[books.stories.sid[whstory] + "fn" + str(books.stories.nameablecharacters[whstory])]) < 11 and len(books.names[books.stories.sid[whstory] + "ln" + str(books.stories.nameablecharacters[whstory])]) < 11:
                    imagebutton:
                        idle books.id[whbook] + "ok"
                        at uizoomone
                        xcenter 1040/2
                        ycenter 585/2 + 80
                        action (SetScreenVariable("nameedit_open", False))
                
                
                for x in range(books.stories.nameablecharacters[whstory]):
                    $tempstr = books.stories.sid[whstory].lower()
                    imagebutton:
                        idle tempstr + "_charicon_" + str(x + 1)
                        xpos (520) - (62*books.stories.nameablecharacters[whstory]) + (125*x)
                        ycenter 400/2
                        action SetVariable("editchoice", x)

            #imagebutton:
                    #idle books.id[whbook] +"name"
                    #at uizoomone
                    #xcenter 520
                    #ycenter (585/2) + (nm*40)
    #         if nameedit_state == 1:
    #             fixed:
    #                 input:
    #                     value VariableInputValue("tempfn")
    #                     length 10
    #                     color "#000000"
    #                     xcenter 310
    #                     ycenter 215
    #                     xanchor 0.5
    #         else:
    #             fixed:
    #                 text tempfn:
    #                     color "#000000"
    #                     xcenter 310
    #                     ycenter 215
    #                     xanchor 0.5
    #                     #outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

    #         if nameedit_state == 2:
    #             fixed:
    #                 input:
    #                     value VariableInputValue("templn")
    #                     length 10
    #                     color "#000000"
    #                     xcenter 710
    #                     ycenter 215
    #                     xanchor 0.5
    #         else:
    #             fixed:
    #                 text templn:
    #                     color "#000000"
    #                     xcenter 710
    #                     ycenter 215
    #                     xanchor 0.5
    #         if tempfn is not "":
    #             if templn is not "":

    #                 imagebutton:
    #                     idle books.id[whbook] +"ok"
    #                     at uizoomone
    #                     xcenter 1040/2
    #                     ycenter 585/2 + 80
    #                     action [Function(setname, tempfn, templn),SetVariable("genericfn",tempfn),SetVariable("genericln", templn), SetVariable("tempfn",""),SetVariable("templn", ""),ToggleScreenVariable("nameedit_open")]
    #         if nameedit_state != 1:
    #             imagebutton:
    #                 idle books.id[whbook] +"namebox"
    #                 at uizoomone
    #                 xcenter 190
    #                 ycenter 215
    #                 xanchor 0
    #                 action [SetScreenVariable("nameedit_state", 1)]
    #         if nameedit_state != 2:
    #             imagebutton:
    #                 idle books.id[whbook] +"namebox"
    #                 at uizoomone
    #                 xcenter 590
    #                 ycenter 215
    #                 xanchor 0
    #                 action [SetScreenVariable("nameedit_state", 2)]

    # if tempfn is "":
    #     key "K_RETURN" action SetScreenVariable("nameedit_state", 0)
    # elif templn is "":
    #     key "K_RETURN" action SetScreenVariable("nameedit_state", 0)
    # else:
    #     key "K_RETURN" action [Function(setname, tempfn, templn),SetVariable("genericfn",tempfn),SetVariable("genericln", templn),SetVariable("tempfn",""), SetVariable("templn", ""),ToggleScreenVariable("nameedit_open")]

    # if nameedit_state == 1:
    #     key "K_TAB" action SetScreenVariable("nameedit_state", 2)
    # elif nameedit_state == 2:
    #     key "K_TAB" action SetScreenVariable("nameedit_state", 1)
    if settings_open:
        if i == False:
            $settings_open = False
        fixed:
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
                    action [Play("sound","audio/sfx/general/close_button.wav"),ToggleScreenVariable("settings_open")]
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
                        xpos 12
                        ypos 44
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
                #bar value Preference("sound volume")
transform slidein:
    ease 0.3 xoffset -192
transform slideout:
    ease 0.3 xoffset 0
transform noadvon:
    xoffset -1255
transform advon:
    xoffset 0
