layeredimage omar:
    xanchor 125
    ycenter 624

    group outfit auto:
        attribute school:
            zoom 1.3
    group face auto:
        attribute angry:
            animblink("omar_angry_")
            zoom 1.3
        attribute basic:
            animblink("omar_basic_")
            zoom 1.3
        attribute sad:
            animblink("omar_sad_")
            zoom 1.3
        attribute sleep:
            animblink("omar_sleep_")
            zoom 1.3
        attribute smile:
            animblink("omar_smile_")
            zoom 1.3
        attribute surprised:
            animblink("omar_surprised_")
            zoom 1.3

        attribute angry_cu:
            animblink("omar_angry_cu")
        attribute basic_cu:
            animblink("omar_basic_cu")
        attribute sad_cu:
            animblink("omar_sad_cu")
        attribute sleep_cu:
            animblink("omar_sleep_cu")
        attribute smile_cu:
            animblink("omar_smile_cu")
        attribute surprised_cu:
            animblink("omar_surprised_cu")

        # glasses
        attribute angry_glasses:
            animblink("omar_angry_glasses_")
            zoom 1.3
        attribute basic_glasses:
            animblink("omar_basic_glasses_")
            zoom 1.3
        attribute sad_glasses:
            animblink("omar_sad_glasses_")
            zoom 1.3
        attribute sleep_glasses:
            animblink("omar_sleep_glasses_")
            zoom 1.3
        attribute smile_glasses:
            animblink("omar_smile_glasses_")
            zoom 1.3
        attribute surprised_glasses:
            animblink("omar_surprised_glasses_")
            zoom 1.3

        attribute angry_glasses_cu:
            animblink("omar_angry_glasses_cu")
        attribute basic_glasses_cu:
            animblink("omar_basic_glasses_cu")
        attribute sad_glasses_cu:
            animblink("omar_sad_glasses_cu")
        attribute sleep_glasses_cu:
            animblink("omar_sleep_glasses_cu")
        attribute smile_glasses_cu:
            animblink("omar_smile_glasses_cu")
        attribute surprised_glasses_cu:
            animblink("omar_surprised_glasses_cu")

        # glow
        attribute angry_glow:
            animblink("omar_angry_glow_")
            zoom 1.3
        attribute basic_glow:
            animblink("omar_basic_glow_")
            zoom 1.3
        attribute sad_glow:
            animblink("omar_sad_glow_")
            zoom 1.3
        attribute sleep_glow:
            animblink("omar_sleep_glow_")
            zoom 1.3
        attribute smile_glow:
            animblink("omar_smile_glow_")
            zoom 1.3
        attribute surprised_glow:
            animblink("omar_surprised_glow_")
            zoom 1.3

        attribute angry_glow_cu:
            animblink("omar_angry_glow_cu")
        attribute basic_glow_cu:
            animblink("omar_basic_glow_cu")
        attribute sad_glow_cu:
            animblink("omar_sad_glow_cu")
        attribute sleep_glow_cu:
            animblink("omar_sleep_glow_cu")
        attribute smile_glow_cu:
            animblink("omar_smile_glow_cu")
        attribute surprised_glow_cu:
            animblink("omar_surprised_glow_cu")

    group accessory auto:
        attribute glasses:
            zoom 1.3
            pos(79, 81)
        attribute glasses_cu:
            pos(224, 242)

transform omar_cu:
    xanchor 376
    xpos stagepos[1]
    ycenter 346

init python:
    def omar_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 224
            mcy = 223
        else:
            mcx = 73
            mcy = 74