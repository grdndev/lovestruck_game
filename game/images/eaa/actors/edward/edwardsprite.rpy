layeredimage edward:
    xanchor 158
    ycenter 650
    group outfit auto:
        attribute casual:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("edward_angry_")
            zoom 1.35
        attribute basic:
            animblink("edward_basic_")
            zoom 1.35
        attribute smile:
            animblink("edward_smile_")
            zoom 1.35
        attribute sleep:
            animblink("edward_sleep_")
            zoom 1.35
        attribute sad:
            animblink("edward_sad_")
            zoom 1.35

        attribute angry_cu:
            animblink("edward_angry_cu")
        attribute basic_cu:
            animblink("edward_basic_cu")
        attribute smile_cu:
            animblink("edward_smile_cu")
        attribute sleep_cu:
            animblink("edward_sleep_cu")
        attribute sad_cu:
            animblink("edward_sad_cu")


transform edward_cu:
    xanchor 414
    xpos stagepos[1]
    ycenter 430

init python:
    def edward_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 260
            mcy = 198
        else:
            mcx = 104
            mcy = 69