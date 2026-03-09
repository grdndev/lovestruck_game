layeredimage mouse:
    xanchor 198
    ycenter 710
    group outfit auto:
        attribute casual:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("mouse_angry_")
            zoom 1.35
        attribute basic:
            animblink("mouse_basic_")
            zoom 1.35
        attribute smile:
            animblink("mouse_smile_")
            zoom 1.35
        attribute sleep:
            animblink("mouse_sleep_")
            zoom 1.35
        attribute sad:
            animblink("mouse_sad_")
            zoom 1.35

        attribute angry_cu:
            animblink("mouse_angry_cu")
        attribute basic_cu:
            animblink("mouse_basic_cu")
        attribute smile_cu:
            animblink("mouse_smile_cu")
        attribute sleep_cu:
            animblink("mouse_sleep_cu")
        attribute sad_cu:
            animblink("mouse_sad_cu")

transform mouse_cu:
    xanchor 500
    xpos stagepos[1]
    ycenter 430

init python:
    def mouse_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 357
            mcy = 211
        else:
            mcx = 151
            mcy = 73