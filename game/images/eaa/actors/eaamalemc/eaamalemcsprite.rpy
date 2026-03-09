layeredimage eaamalemc:
    xanchor 140
    ycenter 632

    group outfit auto:
        attribute blouse:
            zoom 1.3
        attribute blousetie:
            zoom 1.3
        attribute jacket:
            zoom 1.3
        attribute shirtless:
            zoom 1.3
        attribute underwear:
            zoom 1.3

    group face auto:
        attribute angry:
            animblink("eaamalemc_angry_")
            zoom 1.3
        attribute basic:
            animblink("eaamalemc_basic_")
            zoom 1.3
        attribute embarrassed:
            animblink("eaamalemc_embarrassed_")
            zoom 1.3
        attribute sad:
            animblink("eaamalemc_sad_")
            zoom 1.3
        attribute sleep:
            animblink("eaamalemc_sleep_")
            zoom 1.3
        attribute smile:
            animblink("eaamalemc_smile_")
            zoom 1.3
        attribute smirk:
            animblink("eaamalemc_smirk_")
            zoom 1.3
        attribute surprised:
            animblink("eaamalemc_surprised_")
            zoom 1.3

        attribute angry_cu:
            animblink("eaamalemc_angry_cu")
        attribute basic_cu:
            animblink("eaamalemc_basic_cu")
        attribute embarrassed_cu:
            animblink("eaamalemc_embarrassed_cu")
        attribute smirk_cu:
            animblink("eaamalemc_smirk_cu")
        attribute sad_cu:
            animblink("eaamalemc_sad_cu")
        attribute sleep_cu:
            animblink("eaamalemc_sleep_cu")
        attribute smile_cu:
            animblink("eaamalemc_smile_cu")
        attribute surprised_cu:
            animblink("eaamalemc_surprised_cu")
    group accessory auto:
        attribute hat:
            zoom 1.3
            pos(40, 0)
        attribute hat_cu:
            pos(89, 0)


transform eaamalemc_cu:
    xanchor 376
    xpos stagepos[1]
    ycenter 333

init python:
    def eaamalemc_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 263
            mcy = 190
        else:
            mcx = 104
            mcy = 64