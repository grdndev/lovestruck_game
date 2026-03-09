layeredimage sable:
    xanchor 150
    ycenter 710
    group outfit auto:
        attribute casual:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("sable_angry_")
            zoom 1.35
        attribute basic:
            animblink("sable_basic_")
            zoom 1.35
        attribute smile:
            animblink("sable_smile_")
            zoom 1.35
        attribute sleep:
            animblink("sable_sleep_")
            zoom 1.35
        attribute surprised:
            animblink("sable_surprised_")
            zoom 1.35

        attribute angry_cu:
            animblink("sable_angry_cu")
        attribute basic_cu:
            animblink("sable_basic_cu")
        attribute smile_cu:
            animblink("sable_smile_cu")
        attribute sleep_cu:
            animblink("sable_sleep_cu")
        attribute surprised_cu:
            animblink("sable_surprised_cu")

transform sable_cu:
    xanchor 406
    xpos stagepos[1]
    ycenter 400

init python:
    def sable_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 193
            mcy = 246
        else:
            mcx = 113
            mcy = 85