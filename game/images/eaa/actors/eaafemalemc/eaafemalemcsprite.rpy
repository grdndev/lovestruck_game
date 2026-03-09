layeredimage eaafemalemc:
    xanchor 174
    ycenter 642

    group outfit auto:
        attribute blouse:
            zoom 1.32
        attribute blousesweater:
            zoom 1.32
        attribute blousetie:
            zoom 1.32
        attribute jacket:
            zoom 1.32
        attribute suit:
            zoom 1.32
        attribute suitsweater:
            zoom 1.32
        attribute top:
            zoom 1.32
        attribute underwear:
            zoom 1.32

    group face auto:
        attribute angry:
            animblink("eaafemalemc_angry_")
            zoom 1.32
        attribute basic:
            animblink("eaafemalemc_basic_")
            zoom 1.32
        attribute embarrassed:
            animblink("eaafemalemc_embarrassed_")
            zoom 1.32
        attribute grin:
            animblink("eaafemalemc_grin_")
            zoom 1.32
        attribute sad:
            animblink("eaafemalemc_sad_")
            zoom 1.32
        attribute sleep:
            animblink("eaafemalemc_sleep_")
            zoom 1.32
        attribute smile:
            animblink("eaafemalemc_smile_")
            zoom 1.32
        attribute smirk:
            animblink("eaafemalemc_smirk_")
            zoom 1.32
        attribute surprised:
            animblink("eaafemalemc_surprised_")
            zoom 1.32

        attribute angry_cu:
            animblink("eaafemalemc_angry_cu")
        attribute basic_cu:
            animblink("eaafemalemc_basic_cu")
        attribute embarrassed_cu:
            animblink("eaafemalemc_embarrassed_cu")
        attribute grin_cu:
            animblink("eaafemalemc_grin_cu")
        attribute smirk_cu:
            animblink("eaafemalemc_smirk_cu")
        attribute sad_cu:
            animblink("eaafemalemc_sad_cu")
        attribute sleep_cu:
            animblink("eaafemalemc_sleep_cu")
        attribute smile_cu:
            animblink("eaafemalemc_smile_cu")
        attribute surprised_cu:
            animblink("eaafemalemc_surprised_cu")
    group accessory multiple variant "accessory":
        attribute headband:
            zoom 1.32
            pos(137, 15)
        attribute mask:
            zoom 1.32
            pos(74, 12)
        attribute ring:
            zoom 1.32
            pos(99, 34)
        attribute headband_cu:
            pos(374, 37)
        attribute mask_cu:
            pos(181, 31)


transform eaafemalemc_cu:
    xanchor 472
    xpos stagepos[1]
    ycenter 336

init python:
    def eaafemalemc_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 341
            mcy = 190
        else:
            mcx = 132
            mcy = 67