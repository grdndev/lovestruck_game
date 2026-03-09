layeredimage lucas:
    xanchor 184
    ycenter 590
    group outfit auto:
        attribute loose:
            zoom 1.32
        attribute loose_sheathed:
            zoom 1.32
        attribute loose_sword:
            zoom 1.32
        attribute prince:
            zoom 1.32
        attribute prince_sheathed:
            zoom 1.32
        attribute prince_sword:
            zoom 1.32
        attribute school:
            zoom 1.32
        attribute school_sheathed:
            zoom 1.32
        attribute school_sword:
            zoom 1.32
        attribute shirt:
            zoom 1.32
        attribute shirt_sheathed:
            zoom 1.32
        attribute shirt_sword:
            zoom 1.32
        attribute sweater:
            zoom 1.32
        attribute sweater_sheathed:
            zoom 1.32
        attribute sweater_sword:
            zoom 1.32
        attribute under:
            zoom 1.32
    group face auto:
        attribute angry:
            animblink("lucas_angry_")
            zoom 1.32
        attribute basic:
            animblink("lucas_basic_")
            zoom 1.32
        attribute embarrassed:
            animblink("lucas_embarrassed_")
            zoom 1.32
        attribute grin:
            animblink("lucas_grin_")
            zoom 1.32
        attribute sad:
            animblink("lucas_sad_")
            zoom 1.32
        attribute sleep:
            animblink("lucas_sleep_")
            zoom 1.32
        attribute smile:
            animblink("lucas_smile_")
            zoom 1.32
        attribute smirk:
            animblink("lucas_smirk_")
            zoom 1.32
        attribute surprised:
            animblink("lucas_surprised_")
            zoom 1.32

        attribute angry_cu:
            animblink("lucas_angry_cu")
        attribute basic_cu:
            animblink("lucas_basic_cu")
        attribute embarrassed_cu:
            animblink("lucas_embarrassed_cu")
        attribute grin_cu:
            animblink("lucas_grin_cu")
        attribute sad_cu:
            animblink("lucas_sad_cu")
        attribute sleep_cu:
            animblink("lucas_sleep_cu")
        attribute smile_cu:
            animblink("lucas_smile_cu")
        attribute smirk_cu:
            animblink("lucas_smirk_cu")
        attribute surprised_cu:
            animblink("lucas_surprised_cu")

transform lucas_cu:
    xanchor 450
    xpos stagepos[1]
    ycenter 360

init python:
    def lucas_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 317
            mcy = 214
        else:
            mcx = 140
            mcy = 71