layeredimage galahad:
    xanchor 216
    ycenter 700
    group outfit auto:
        attribute armor:
            zoom 1.45
        attribute surcoat:
            zoom 1.45
        attribute under:
            zoom 1.45

        attribute armor_cu:
            zoom 1.16
        attribute surcoat_cu:
            zoom 1.16
        attribute under_cu:
            zoom 1.16
    group face auto:
        attribute angry:
            animblink("galahad_angry_")
            zoom 1.45
        attribute basic:
            animblink("galahad_basic_")
            zoom 1.45
        attribute embarrassed:
            animblink("galahad_embarrassed_")
            zoom 1.45
        attribute sad:
            animblink("galahad_sad_")
            zoom 1.45
        attribute sleep:
            animblink("galahad_sleep_")
            zoom 1.45
        attribute smile:
            animblink("galahad_smile_")
            zoom 1.45
        attribute smirk:
            animblink("galahad_smirk_")
            zoom 1.45
        attribute surprised:
            animblink("galahad_surprised_")
            zoom 1.45

        attribute angry_cu:
            animblink("galahad_angry_cu")
            zoom 1.16
        attribute basic_cu:
            animblink("galahad_basic_cu")
            zoom 1.16
        attribute embarrassed_cu:
            animblink("galahad_embarrassed_cu")
            zoom 1.16
        attribute sad_cu:
            animblink("galahad_sad_cu")
            zoom 1.16
        attribute sleep_cu:
            animblink("galahad_sleep_cu")
            zoom 1.16
        attribute smile_cu:
            animblink("galahad_smile_cu")
            zoom 1.16
        attribute smirk_cu:
            animblink("galahad_smirk_cu")
            zoom 1.16
        attribute surprised_cu:
            animblink("galahad_surprised_cu")
            zoom 1.16
    group accessory auto:
        attribute helmet:
            zoom 1.45
            pos(145, -12)
        attribute helmet_cu:
            zoom 1.16
            pos(364, -46)


transform galahad_cu:
    xanchor 584
    xpos stagepos[1]
    ycenter 480

init python:
    def galahad_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 445
            mcy = 181
        else:
            mcx = 171
            mcy = 58