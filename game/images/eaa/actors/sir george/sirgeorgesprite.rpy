layeredimage sirgeorge:
    xanchor 170
    ycenter 610
    group outfit auto:
        attribute casual:
            zoom 1.3
    group face auto:
        attribute angry:
            animblink("sirgeorge_angry_")
            zoom 1.3
        attribute basic:
            animblink("sirgeorge_basic_")
            zoom 1.3
        attribute sleep:
            animblink("sirgeorge_sleep_")
            zoom 1.3
        attribute smile:
            animblink("sirgeorge_smile_")
            zoom 1.3
        attribute sad:
            animblink("sirgeorge_sad_")
            zoom 1.3

        attribute angry_cu:
            animblink("sirgeorge_angry_cu")
        attribute basic_cu:
            animblink("sirgeorge_basic_cu")
        attribute sleep_cu:
            animblink("sirgeorge_sleep_cu")
        attribute smile_cu:
            animblink("sirgeorge_smile_cu")
        attribute sad_cu:
            animblink("sirgeorge_sad_cu")


transform sirgeorge_cu:
    xanchor 478
    xpos stagepos[1]
    ycenter 378

init python:
    def sirgeorge_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 375
            mcy = 194
        else:
            mcx = 135
            mcy = 64