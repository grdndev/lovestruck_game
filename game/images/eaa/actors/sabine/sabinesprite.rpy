layeredimage sabine:
    xanchor 174
    ycenter 710
    group outfit auto:
        attribute casual:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("sabine_angry_")
            zoom 1.35
        attribute basic:
            animblink("sabine_basic_")
            zoom 1.35
        attribute smile:
            animblink("sabine_smile_")
            zoom 1.35
        attribute sleep:
            animblink("sabine_sleep_")
            zoom 1.35
        attribute surprised:
            animblink("sabine_surprised_")
            zoom 1.35

        attribute angry_cu:
            animblink("sabine_angry_cu")
        attribute basic_cu:
            animblink("sabine_basic_cu")
        attribute smile_cu:
            animblink("sabine_smile_cu")
        attribute sleep_cu:
            animblink("sabine_sleep_cu")
        attribute surprised_cu:
            animblink("sabine_surprised_cu")

transform sabine_cu:
    xanchor 406
    xpos stagepos[1]
    ycenter 400

init python:
    def sabine_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 302
            mcy = 247
        else:
            mcx = 139
            mcy = 85