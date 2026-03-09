layeredimage bosco:
    xanchor 148
    ycenter 606
    group outfit auto:
        attribute casual:
            zoom 1.32
    group face auto:
        attribute confused:
            animblink("bosco_confused_")
            zoom 1.32
        attribute basic:
            animblink("bosco_basic_")
            zoom 1.32
        attribute sleep:
            animblink("bosco_sleep_")
            zoom 1.32
        attribute smile:
            animblink("bosco_smile_")
            zoom 1.32
        attribute surprised:
            animblink("bosco_surprised_")
            zoom 1.32

        attribute confused_cu:
            animblink("bosco_confused_cu")
        attribute basic_cu:
            animblink("bosco_basic_cu")
        attribute sleep_cu:
            animblink("bosco_sleep_cu")
        attribute smile_cu:
            animblink("bosco_smile_cu")
        attribute surprised_cu:
            animblink("bosco_surprised_cu")


transform bosco_cu:
    xanchor 394
    xpos stagepos[1]
    ycenter 386

init python:
    def bosco_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 289
            mcy = 198
        else:
            mcx = 114
            mcy = 66