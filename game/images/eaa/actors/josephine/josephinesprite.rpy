layeredimage josephine:
    xanchor 270
    ycenter 710
    group outfit auto:
        attribute blouse:
            zoom 1.2
        attribute princess:
            zoom 1.2
        attribute school:
            zoom 1.2
    group face auto:
        attribute angry:
            animblink("josephine_angry_")
            zoom 1.2
        attribute basic:
            animblink("josephine_basic_")
            zoom 1.2
        attribute bigsmile:
            animblink("josephine_bigsmile_")
            zoom 1.2
        attribute smallsmile:
            animblink("josephine_smallsmile_")
            zoom 1.2
        attribute sad:
            animblink("josephine_sad_")
            zoom 1.2
        attribute embarrassed:
            animblink("josephine_embarrassed_")
            zoom 1.2
        attribute sleep:
            animblink("josephine_sleep_")
            zoom 1.2

        attribute angry_cu:
            animblink("josephine_angry_cu")
        attribute basic_cu:
            animblink("josephine_basic_cu")
        attribute bigsmile_cu:
            animblink("josephine_bigsmile_cu")
        attribute smallsmile_cu:
            animblink("josephine_smallsmile_cu")
        attribute embarrassed_cu:
            animblink("josephine_embarrassed_cu")
        attribute sad_cu:
            animblink("josephine_sad_cu")
        attribute sleep_cu:
            animblink("josephine_sleep_cu")

transform josephine_cu:
    xanchor 476
    xpos stagepos[1]
    ycenter 430

init python:
    def josephine_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 308
            mcy = 162
        else:
            mcx = 218
            mcy = 49