layeredimage warlock:
    xanchor 428
    ycenter 250
    group outfit auto:
        attribute casual:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("warlock_angry_")
            zoom 1.35
        attribute basic:
            animblink("warlock_basic_")
            zoom 1.35
        attribute sleep:
            animblink("warlock_sleep_")
            zoom 1.35
        attribute smile:
            animblink("warlock_smile_")
            zoom 1.35
        attribute surprised:
            animblink("warlock_surprised_")
            zoom 1.35

        attribute angry_cu:
            animblink("warlock_angry_cu")
        attribute basic_cu:
            animblink("warlock_basic_cu")
        attribute sleep_cu:
            animblink("warlock_sleep_cu")
        attribute smile_cu:
            animblink("warlock_smile_cu")
        attribute surprised_cu:
            animblink("warlock_surprised_cu")

transform warlock_cu:
    xanchor 610
    xpos stagepos[1]
    ycenter 270

init python:
    def warlock_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 484
            mcy = 151
        else:
            mcx = 383
            mcy = 186