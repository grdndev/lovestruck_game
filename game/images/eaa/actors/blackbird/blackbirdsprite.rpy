layeredimage blackbird:
    xanchor 376
    ycenter 620
    group outfit auto:
        attribute casual:
            zoom 1.3
    group face auto:
        attribute angry:
            animblink("blackbird_angry_")
            zoom 1.3
        attribute basic:
            animblink("blackbird_basic_")
            zoom 1.3
        attribute sad:
            animblink("blackbird_sad_")
            zoom 1.3
        attribute sleep:
            animblink("blackbird_sleep_")
            zoom 1.3
        attribute smile:
            animblink("blackbird_smile_")
            zoom 1.3

        attribute angry_cu:
            animblink("blackbird_angry_cu")
        attribute basic_cu:
            animblink("blackbird_basic_cu")
        attribute sad_cu:
            animblink("blackbird_sad_cu")
        attribute sleep_cu:
            animblink("blackbird_sleep_cu")
        attribute smile_cu:
            animblink("blackbird_smile_cu")

transform blackbird_cu:
    xanchor 512
    xpos stagepos[1]
    ycenter 400


init python:
    def blackbird_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 291
            mcy = 125
        else:
            mcx = 302
            mcy = 43