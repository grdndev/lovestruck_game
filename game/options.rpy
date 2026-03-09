## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.
define config.developer = True
define config.name = _("Lovestruck")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "3.0" #Second number is number of book updates, third is story updates since last book update,
#                                   fourth is number of regular patches since the last story update


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "loves_truck"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


define config.image_cache_size_mb = 400

##Danielle's Variables- For more general variables, like main menu stuff.
define desc.storage = 0
define x.a = 0
init -1:
    define desc.nomessage = "I haven't written this description yet."
    define stagepos = [ 245,520,795]
transform uizoomone:
    zoom globalzoom
define menuspacing = 36
define menuxspacing = 150
define menuoptionsypos = 320 #Where the story titles are displayed
define menuoptionsxpos = 10
define menulistlength = 7 #number of episodes or seasons per line
define menunamex = 780
define menunamey = 326
define menudescriptionx = 540
define menudescriptiony = 361
##Blink delays.
define fastblink = 3.5
define medblink = 5
define slowblink = 7
define slowerblink = 7.5
define evenslowerblink = 10
define blinkpause = .05

style quitmessagecolor:
    color "#ffffff"
    hover_color "#ffffff"
    insensitive_color "#ffffff"
    font "images/general/fonts/tahoma.ttf"
    size 30
style quitbuttoncolor:
    color "#ffffff"
    hover_color "#bdbdbd"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 30

style officialstorycolor:
    color "#00baf8"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
style archivestorycolor:
    color "#FF0054"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
style textbuttoncolor:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
style tabbuttoncolor:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#ffffff"
    font "images/general/fonts/tahoma.ttf"
    size 20
style radiostyle:
    color "#efccff"
    hover_color "#efccff"
    insensitive_color "#efccff"
    font "images/general/fonts/tahoma.ttf"
    size 15
style jukeboxcolor:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#ffffff"
    font "images/general/fonts/tahoma.ttf"
    size 12
style gallerybuttoncolor:
    color "#bdbdbd"
    hover_color "#ffffff"
    insensitive_color "#4a4a4a"
    font "images/general/fonts/tahoma.ttf"
    size 20
style textbuttonalt:
    color "#ffffff"
    hover_color "#ffffff"
    insensitive_color "#ffffff"
    font "images/general/fonts/tahoma.ttf"
    size 20
style mscname:
    font "images/general/fonts/mscfont.otf"
    color "#375959"
style hiflname:
    font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
    color "#FFFFFF"
style llname:
    font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
    color "#FFFFFF"
style ihsname:
    font "images/general/fonts/Swistblnk Duwhoers Brush.ttf"
    color "#FFFFFF"

###THIS IS WHERE YOU ADD IN NEW EPISODES
#default maxepisodes = 500
default persistent.savegame = ["a"] * 500
define globalzoom = 1.3
#default finished = ["a"]*500
define showasnew = ["hifl", "ghost", 1, 1, 3] #book id, story id, season, episode start, episode end
init -2:
    define books.id = ["hifl", "ll", "ecm", "msc", "ihs", "wll", "eaa"] ##The prefix that refers to the book in questions

define books.choicecolor = ["#FFFFFF","#000000","#ffffff","#ffffff","#ffed91","#FFFFFF","#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
define books.namecolor = ["#FFFFFF","#000000","#ffffff","#ffffff","#ffed91","#FFFFFF","#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
define books.inactivenamecolor =['#8888887f','#8888887f',"#8888887f",'#8888887f','#8888887f','#8888887f','#8888887f', "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
define books.activenamecolor =['#000000','#000000',"#000000",'#000000','#000000','#000000','#000000', "#000000", "#000000", "#000000", "#000000"]
define books.title = ["Havenfall is for Lovers", "Love & Legends","Edge Case Machina", "My Siren Crush","Immortal Heart Society","Wicked Lawless Love","Ever After Academy","Sweet Enchantments","Starship Promise","Villainous Nights"] ##Title given to book on the menu
define books.cover = ["hiflcover", "llcover","ecmcover", "msccover","ihscover","wllcover","eaacover","secover","spcover","vncover"] ##Name of the book's cover file, without .png
define books.background = ["hiflstoryselect", "llstoryselect","ecmstoryselect","mscstoryselect","ihsstoryselect","wllstoryselect","eaastoryselect","sestoryselect", "spstoryselect", "vnstoryselect"]
##The game will see books.stories.id[3] and look for books.stories.forboook[3], and so on.
#The game will provide links to 3 episodes for 'ghost', and 6 for 'engineer', even if there's no content for them.
define books.cgnames= [["antonio", "diego", "jd", "mac", "razi", "vanessa"],["alain", "helena"]]
define books.cgcount= [[34, 42, 33, 41, 33, 33],[0],[0],[0],[0],[0],[0],[0]]
define books.cgx = [-66, -60, -53, -47]
define books.cgy = [16, 24, 32, 40]
default activecg = 0
default maxcg = 8
default menucg = [2]*40



##DO NOT TOUCH
default which_menu = 0
default which_story = 0
default which_season = 0
default which_type = 0
default shownew = " {image=images/general/icons/new.png}"
#init:
    #image m_emeril:
        #"menu_emeril"
        #zoom 0.12

label navigation_screen:

    $ renpy.show_screen('navigation')
    $ ui.interact()
    jump _noisy_return


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "LovesTruck"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
