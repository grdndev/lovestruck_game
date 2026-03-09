layeredimage darla:
    xanchor 270
    ycenter 625
    group outfit auto:
        attribute blouse:
            zoom 1.35
        attribute blouse_purse:
            zoom 1.35
        attribute jacket:
            zoom 1.35
        attribute jacket_purse:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("darla_angry_")
            zoom 1.35
        attribute basic:
            animblink("darla_basic_")
            zoom 1.35
        attribute sad:
            animblink("darla_sad_")
            zoom 1.35
        attribute sleep:
            animblink("darla_sleep_")
            zoom 1.35
        attribute smile:
            animblink("darla_smile_")
            zoom 1.35
        attribute smirk:
            animblink("darla_smirk_")
            zoom 1.35
        attribute surprised:
            animblink("darla_surprised_")
            zoom 1.35

        attribute angry_glow:
            animblink("darla_angry_glow_")
            zoom 1.35
        attribute basic_glow:
            animblink("darla_basic_glow_")
            zoom 1.35
        attribute sad_glow:
            animblink("darla_sad_glow_")
            zoom 1.35
        attribute sleep_glow:
            animblink("darla_sleep_glow_")
            zoom 1.35
        attribute smile_glow:
            animblink("darla_smile_glow_")
            zoom 1.35
        attribute smirk_glow:
            animblink("darla_smirk_glow_")
            zoom 1.35
        attribute surprised_glow:
            animblink("darla_surprised_glow_")
            zoom 1.35

        attribute angry_cu:
            animblink("darla_angry_cu")
        attribute basic_cu:
            animblink("darla_basic_cu")
        attribute sad_cu:
            animblink("darla_sad_cu")
        attribute sleep_cu:
            animblink("darla_sleep_cu")
        attribute smile_cu:
            animblink("darla_smile_cu")
        attribute smirk_cu:
            animblink("darla_smirk_cu")
        attribute surprised_cu:
            animblink("darla_surprised_cu")

        attribute angry_glow_cu:
            animblink("darla_angry_glow_cu")
        attribute basic_glow_cu:
            animblink("darla_basic_glow_cu")
        attribute sad_glow_cu:
            animblink("darla_sad_glow_cu")
        attribute sleep_glow_cu:
            animblink("darla_sleep_glow_cu")
        attribute smile_glow_cu:
            animblink("darla_smile_glow_cu")
        attribute smirk_glow_cu:
            animblink("darla_smirk_glow_cu")
        attribute surprised_glow_cu:
            animblink("darla_surprised_glow_cu")
    group accessory auto:
        attribute halloween:
            zoom 1.35
            pos(213, -18)
        attribute halloween_cu:
            pos(345, -42)


transform darla_cu:
    xanchor 508
    xpos stagepos[1]
    ycenter 360

init python:
    def darla_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 400
            mcy = 174
        else:
            mcx = 232
            mcy = 59