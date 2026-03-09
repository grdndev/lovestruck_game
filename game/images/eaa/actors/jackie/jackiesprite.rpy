layeredimage jackie:
    xanchor 134
    ycenter 630
    group outfit auto:
        attribute casual:
            zoom 1.3
        attribute casual_cu:
            zoom 0.9
    group face auto:
        attribute angry:
            animblink("jackie_angry_")
            zoom 1.3
        attribute basic:
            animblink("jackie_basic_")
            zoom 1.3
        attribute sleep:
            animblink("jackie_sleep_")
            zoom 1.3
        attribute smile:
            animblink("jackie_smile_")
            zoom 1.3
        attribute surprised:
            animblink("jackie_surprised_")
            zoom 1.3

        attribute angry_cu:
            animblink("jackie_angry_cu")
            zoom 0.9
        attribute basic_cu:
            animblink("jackie_basic_cu")
            zoom 0.9
        attribute sleep_cu:
            animblink("jackie_sleep_cu")
            zoom 0.9
        attribute smile_cu:
            animblink("jackie_smile_cu")
            zoom 0.9
        attribute surprised_cu:
            animblink("jackie_surprised_cu")
            zoom 0.9

    group accessory auto:
        attribute glasses:
            zoom 1.3
            pos(94, 91)
        attribute glasses_cu:
            zoom 0.9
            pos(217, 248)


transform jackie_cu:
    xanchor 328
    xpos stagepos[1]
    ycenter 310

init python:
    def jackie_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 231
            mcy = 231
        else:
            mcx = 98
            mcy = 85