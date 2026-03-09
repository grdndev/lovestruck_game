layeredimage lavinia:
    xanchor 170
    ycenter 590
    group outfit auto:
        attribute blazer:
            zoom 1.32
        attribute casual:
            zoom 1.32
        attribute icequeen:
            zoom 1.32
        attribute shirt:
            zoom 1.32
        attribute under:
            zoom 1.32
    group face auto:
        attribute angry:
            animblink("lavinia_angry_")
            zoom 1.32
        attribute basic:
            animblink("lavinia_basic_")
            zoom 1.32
        attribute embarrassed:
            animblink("lavinia_embarrassed_")
            zoom 1.32
        attribute sad:
            animblink("lavinia_sad_")
            zoom 1.32
        attribute sleep:
            animblink("lavinia_sleep_")
            zoom 1.32
        attribute smile:
            animblink("lavinia_smile_")
            zoom 1.32
        attribute smirk:
            animblink("lavinia_smirk_")
            zoom 1.32
        attribute surprised:
            animblink("lavinia_surprised_")
            zoom 1.32

        attribute angry_cu:
            animblink("lavinia_angry_cu")
        attribute basic_cu:
            animblink("lavinia_basic_cu")
        attribute embarrassed_cu:
            animblink("lavinia_embarrassed_cu")
        attribute sad_cu:
            animblink("lavinia_sad_cu")
        attribute sleep_cu:
            animblink("lavinia_sleep_cu")
        attribute smile_cu:
            animblink("lavinia_smile_cu")
        attribute smirk_cu:
            animblink("lavinia_smirk_cu")
        attribute surprised_cu:
            animblink("lavinia_surprised_cu")

transform lavinia_cu:
    xanchor 500
    xpos stagepos[1]
    ycenter 290

init python:
    def lavinia_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 341
            mcy = 248
        else:
            mcx = 115
            mcy = 84