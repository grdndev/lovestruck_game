layeredimage redriding:
    xanchor 160
    ycenter 710
    group outfit auto:
        attribute casual:
            zoom 1.5
        attribute casual_cu:
            zoom 1.2
    group face auto:
        attribute angry:
            animblink("redriding_angry_")
            zoom 1.5
        attribute basic:
            animblink("redriding_basic_")
            zoom 1.5
        attribute smile:
            animblink("redriding_smile_")
            zoom 1.5
        attribute sleep:
            animblink("redriding_sleep_")
            zoom 1.5
        attribute sad:
            animblink("redriding_sad_")
            zoom 1.5

        attribute angry_cu:
            animblink("redriding_angry_cu")
            zoom 1.2
        attribute basic_cu:
            animblink("redriding_basic_cu")
            zoom 1.2
        attribute smile_cu:
            animblink("redriding_smile_cu")
            zoom 1.2
        attribute sleep_cu:
            animblink("redriding_sleep_cu")
            zoom 1.2
        attribute sad_cu:
            animblink("redriding_sad_cu")
            zoom 1.2


transform redriding_cu:
    xanchor 392
    xpos stagepos[1]
    ycenter 430

init python:
    def redriding_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 301
            mcy = 313
        else:
            mcx = 131
            mcy = 68