layeredimage arin:
    xanchor 120
    ycenter 600

    group outfit auto:
        attribute binder:
            zoom 1.3
        attribute binder_bun:
            zoom 1.3
        attribute binder_bun_hand:
            zoom 1.3
        attribute binder_hand:
            zoom 1.3
        attribute jacket:
            zoom 1.3
        attribute jacket_bun:
            zoom 1.3
        attribute jacket_bun_hand:
            zoom 1.3
        attribute jacket_hand:
            zoom 1.3
        attribute sweater:
            zoom 1.3
        attribute sweater_bun:
            zoom 1.3
        attribute sweater_bun_hand:
            zoom 1.3
        attribute sweater_hand:
            zoom 1.3
        attribute tie:
            zoom 1.3
        attribute tie_bun:
            zoom 1.3
        attribute tie_bun_hand:
            zoom 1.3
        attribute tie_hand:
            zoom 1.3
    group face auto:
        attribute angry:
            animblink("arin_angry_")
            zoom 1.3
        attribute basic:
            animblink("arin_basic_")
            zoom 1.3
        attribute embarrassed:
            animblink("arin_embarrassed_")
            zoom 1.3
        attribute sad:
            animblink("arin_sad_")
            zoom 1.3
        attribute shocked:
            animblink("arin_shocked_")
            zoom 1.3
        attribute sleep:
            animblink("arin_sleep_")
            zoom 1.3
        attribute smile:
            animblink("arin_smile_")
            zoom 1.3
        attribute surprised:
            animblink("arin_surprised_")
            zoom 1.3

        attribute angry_cu:
            animblink("arin_angry_cu")
        attribute basic_cu:
            animblink("arin_basic_cu")
        attribute embarrassed_cu:
            animblink("arin_embarrassed_cu")
        attribute sad_cu:
            animblink("arin_sad_cu")
        attribute shocked_cu:
            animblink("arin_shocked_cu")
        attribute sleep_cu:
            animblink("arin_sleep_cu")
        attribute smile_cu:
            animblink("arin_smile_cu")
        attribute surprised_cu:
            animblink("arin_surprised_cu")

transform arin_cu:
    xanchor 346
    xpos stagepos[1]
    ycenter 333

init python:
    def arin_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 243
            mcy = 258
        else:
            mcx = 70
            mcy = 112