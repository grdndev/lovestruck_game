layeredimage gothel:
    xanchor 198
    ycenter 670
    group outfit auto:
        attribute casual:
            zoom 1.22
        attribute hat:
            zoom 1.22
    group face auto:
        attribute angry:
            animblink("gothel_angry_")
            zoom 1.22
        attribute basic:
            animblink("gothel_basic_")
            zoom 1.22
        attribute smile:
            animblink("gothel_smile_")
            zoom 1.22
        attribute sad:
            animblink("gothel_sad_")
            zoom 1.22
        attribute sleep:
            animblink("gothel_sleep_")
            zoom 1.22

        attribute angry_cu:
            animblink("gothel_angry_cu")
        attribute basic_cu:
            animblink("gothel_basic_cu")
        attribute smile_cu:
            animblink("gothel_smile_cu")
        attribute sad_cu:
            animblink("gothel_sad_cu")
        attribute sleep_cu:
            animblink("gothel_sleep_cu")


transform gothel_cu:
    xanchor 368
    xpos stagepos[1]
    ycenter 310

init python:
    def gothel_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 203
            mcy = 336
        else:
            mcx = 146
            mcy = 106