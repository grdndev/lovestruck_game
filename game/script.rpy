# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define persistent.dialogueBoxOpacity = 0.50
define persistent.borders = True
define persistent.prompt = False
define config.quit_action = [Quit(confirm=True)]
default persistent.menpos = 0
default persistent.storypos = 0
default persistent.seasonpos = 0
default persistent.episodepos = 0

default persistent.stopauto = False
default storypos = 0
default seasonpos = 0
default whstory = 0
init -2:
    $nevertrue = False
    default ctcimage = "images/general/icons/dialogue_noprompt.png"
    # ---------- CTC blinking arrow -------------------
    image ctc_:
        xpos 750 # Across from right
        ypos 50 # Up from bottom
        xanchor 1.0  # On Right
        yanchor 1.0   # On Bottom
        ctcimage
        ease 0.2 xoffset 4
        ease 0.2 xoffset 0
        repeat
    $refresh = False
    $hideborders = True
    $savegame = False
    $ hidetextbox = False
    $ sidecharone = " "
    $ sidechartwo = " "
    $ sidecharthree = " "
    $ tempfn = ""
    $ templn = ""
    $ config.has_autosave = True
    #game_menu = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ]

    $ config.keymap['game_menu'].remove('K_ESCAPE')
    $ config.keymap['game_menu'].remove('K_MENU')
    $ config.keymap['game_menu'].remove('mouseup_3')
    $ config.keymap['rollforward'].remove('mousedown_5')
    $ config.keymap['rollforward'].remove('K_PAGEDOWN')
    $ config.keymap['rollforward'].remove('repeat_K_PAGEDOWN')
    $ config.keymap['dismiss'].append('mousedown_5')
    $ config.keymap['rollback'].append('K_LEFT')
    $ config.keymap['dismiss'].append('K_RIGHT')
    $ config.keymap['toggle_skip'].remove('K_TAB')
    $ config.keymap['fast_skip'].remove('>')
    #$ config.keymap['fast_skip'].remove('shift_K_PERIOD')
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ episode = ""
    $ episodeid = 1
    $ whbook = 0
    $ genericfn = " "
    $ genericln = " "
    $tsize = 1.5

init -10 python:
    g = Gallery()
    mcdata = MultiPersistent("names")
    if mcdata.mcnames == None:
        mcdata.mcnames = {}
    #mcdata.mcnames = {"hiflln":"Ryan"}
    #mcdata.hifl_fn = None
    #mcdata.save()

define narrator = Character(what_outlines=[ (tsize, "#000") ])
define name_only = Character(color="#FFFFFF", who_underline=True, what_prefix='"', what_suffix='"', what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")])
define vnmc = Character("vn_fn",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], dynamic = True)

define sid1 = Character("sidecharone",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], dynamic = True)
define sid2 = Character("sidechartwo",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], dynamic = True)
define sid3 = Character("sidecharthree",color="#FFFFFF", what_prefix='"', what_suffix='"', who_underline=True, what_outlines=[ (tsize, "#000") ],who_outlines=[(tsize, "#000")], dynamic = True)


# The game starts here.

label start:

    $ genericfn = " "
    $ genericln = " "
    if mcdata.hifl_fn is None:
        $ hifl_fn = "Siobhan"
        $ hifl_ln = "Ryan"
    else:
        $ hifl_fn = mcdata.hifl_fn
        $ hifl_ln = mcdata.hifl_ln

    if mcdata.vn_fn is None:
        $vn_fn = "Lana"
        $vn_ln = "Ryan"
    else:
        $ vn_fn = mcdata.vn_fn
        $ vn_ln = mcdata.vn_ln
    $ quick_menu = False
    show screen gamemenu()
    $renpy.jump (episode)

    #play music "audio/villains/everyday.mp3"
label end:
    # This ends the game.
    return
