layeredimage fergus:
    xanchor 212
    ycenter 600
    group outfit auto:
        attribute casual:
            zoom 1.3
    group face auto:
        attribute angry:
            animblink("fergus_angry_")
            zoom 1.3
        attribute basic:
            animblink("fergus_basic_")
            zoom 1.3
        attribute sleep:
            animblink("fergus_sleep_")
            zoom 1.3
        attribute smile:
            animblink("fergus_smile_")
            zoom 1.3

        attribute angry_cu:
            animblink("fergus_angry_cu")
        attribute basic_cu:
            animblink("fergus_basic_cu")
        attribute smile_cu:
            animblink("fergus_smile_cu")


transform fergus_cu:
    xanchor 568
    xpos stagepos[1]
    ycenter 380


init python:
    def fergus_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 468
            mcy = 210
        else:
            mcx = 178
            mcy = 70