layeredimage tinman:
    xanchor 266
    ycenter 660
    group outfit auto:
        attribute armless:
            zoom 1.4
        attribute casual:
            zoom 1.4
        attribute headless:
            zoom 1.4
        attribute headless_armless:
            zoom 1.4
        attribute onearm:
            zoom 1.4

        attribute armless_cu:
            zoom 1.17
        attribute casual_cu:
            zoom 1.17
        attribute onearm_cu:
            zoom 1.17
    group face auto:
        attribute angry:
            animblink("tinman_angry_")
            zoom 1.4
        attribute basic:
            animblink("tinman_basic_")
            zoom 1.4
        attribute surprised:
            animblink("tinman_surprised_")
            zoom 1.4
        attribute smile:
            animblink("tinman_smile_")
            zoom 1.4

        attribute angry_cu:
            animblink("tinman_angry_cu")
            zoom 1.17
        attribute basic_cu:
            animblink("tinman_basic_cu")
            zoom 1.17
        attribute surprised_cu:
            animblink("tinman_surprised_cu")
            zoom 1.17
        attribute smile_cu:
            animblink("tinman_smile_cu")
            zoom 1.17

transform tinman_cu:
    xanchor 588
    xpos stagepos[1]
    ycenter 400

init python:
    def tinman_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 472
            mcy = 277
        else:
            mcx = 225
            mcy = 99