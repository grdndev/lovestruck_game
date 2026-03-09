layeredimage abel:
    xanchor 176
    ycenter 592

    group outfit auto:
        attribute casual:
            zoom 1.25
        attribute casual_axe:
            zoom 1.25
        attribute coat:
            zoom 1.25
        attribute coat_axe:
            zoom 1.25
        attribute shirtless:
            zoom 1.25
        attribute shirtless_axe:
            zoom 1.25
        attribute under:
            zoom 1.25
        attribute under_axe:
            zoom 1.25
    group face auto:
        attribute angry:
            animblink("abel_angry_")
            zoom 1.25
        attribute basic:
            animblink("abel_basic_")
            zoom 1.25
        attribute blush:
            animblink("abel_blush_")
            zoom 1.25
        attribute grin:
            animblink("abel_grin_")
            zoom 1.25
        attribute sad:
            animblink("abel_sad_")
            zoom 1.25
        attribute sleep:
            animblink("abel_sleep_")
            zoom 1.25
        attribute smile:
            animblink("abel_smile_")
            zoom 1.25
        attribute surprised:
            animblink("abel_surprised_")

        attribute angry_cu:
            animblink("abel_angry_cu")
        attribute basic_cu:
            animblink("abel_basic_cu")
        attribute blush_cu:
            animblink("abel_blush_cu")
        attribute grin_cu:
            animblink("abel_grin_cu")
        attribute sad_cu:
            animblink("abel_sad_cu")
        attribute sleep_cu:
            animblink("abel_sleep_cu")
        attribute smile_cu:
            animblink("abel_smile_cu")
        attribute surprised_cu:
            animblink("abel_surprised_cu")

transform abel_cu:
    xanchor 412
    xpos stagepos[1]
    ycenter 350

init python:
    def abel_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 263
            mcy = 213
        else:
            mcx = 128
            mcy = 66
