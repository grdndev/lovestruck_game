layeredimage ezra:
    xanchor 216
    ycenter 586

    group outfit auto:
        attribute cape:
            zoom 1.32
        attribute cape_claw:
            zoom 1.32
        attribute jacket:
            zoom 1.32
        attribute jacket_claw:
            zoom 1.32
        attribute polo:
            zoom 1.32
        attribute polo_claw:
            zoom 1.32
        attribute red:
            zoom 1.32
        attribute red_claw:
            zoom 1.32
        attribute tie:
            zoom 1.32
        attribute tie_claw:
            zoom 1.32
        attribute under:
            zoom 1.32
        attribute under_claw:
            zoom 1.32
    group face auto:
        attribute angry:
            animblink("ezra_angry_")
            zoom 1.32
        attribute basic:
            animblink("ezra_basic_")
            zoom 1.32
        attribute embarrassed:
            animblink("ezra_embarrassed_")
            zoom 1.32
        attribute grin:
            animblink("ezra_grin_")
            zoom 1.32
        attribute sad:
            animblink("ezra_sad_")
            zoom 1.32
        attribute sleep:
            animblink("ezra_sleep_")
            zoom 1.32
        attribute smile:
            animblink("ezra_smile_")
            zoom 1.32
        attribute smirk:
            animblink("ezra_smirk_")
            zoom 1.32
        attribute surprised:
            animblink("ezra_surprised_")
            zoom 1.32

        attribute angry_cu:
            animblink("ezra_angry_cu")
        attribute basic_cu:
            animblink("ezra_basic_cu")
        attribute embarrassed_cu:
            animblink("ezra_embarrassed_cu")
        attribute grin_cu:
            animblink("ezra_grin_cu")
        attribute smirk_cu:
            animblink("ezra_smirk_cu")
        attribute sad_cu:
            animblink("ezra_sad_cu")
        attribute sleep_cu:
            animblink("ezra_sleep_cu")
        attribute smile_cu:
            animblink("ezra_smile_cu")
        attribute surprised_cu:
            animblink("ezra_surprised_cu")
# glow
        attribute angry_glow:
            animblink("ezra_angry_glow_")
            zoom 1.32
        attribute basic_glow:
            animblink("ezra_basic_glow_")
            zoom 1.32
        attribute embarrassed_glow:
            animblink("ezra_embarrassed_glow_")
            zoom 1.32
        attribute grin_glow:
            animblink("ezra_grin_glow_")
            zoom 1.32
        attribute sad_glow:
            animblink("ezra_sad_glow_")
            zoom 1.32
        attribute smile_glow:
            animblink("ezra_smile_glow_")
            zoom 1.32
        attribute smirk_glow:
            animblink("ezra_smirk_glow_")
            zoom 1.32
        attribute surprised_glow:
            animblink("ezra_surprised_glow_")
            zoom 1.32

        attribute angry_glow_cu:
            animblink("ezra_angry_glow_cu")
        attribute basic_glow_cu:
            animblink("ezra_basic_glow_cu")
        attribute embarrassed_glow_cu:
            animblink("ezra_embarrassed_glow_cu")
        attribute grin_glow_cu:
            animblink("ezra_grin_glow_cu")
        attribute smirk_glow_cu:
            animblink("ezra_smirk_glow_cu")
        attribute sad_glow_cu:
            animblink("ezra_sad_glow_cu")
        attribute smile_glow_cu:
            animblink("ezra_smile_glow_cu")
        attribute surprised_glow_cu:
            animblink("ezra_surprised_glow_cu")

    group accessory auto:
        attribute glove:
            zoom 1.32
            pos(103, 458)
        attribute glove_claw:
            zoom 1.32
            pos(230, 129)
        attribute glove_claw_cu:
            pos(575, 385)


transform ezra_cu:
    xanchor 532
    xpos stagepos[1]
    ycenter 430

init python:
    def ezra_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 394
            mcy = 222
        else:
            mcx = 168
            mcy = 75