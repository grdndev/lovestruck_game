layeredimage nora:
    xanchor 162
    ycenter 632

    group outfit auto:
        attribute casual:
            zoom 1.3
        attribute polo:
            zoom 1.3
        attribute school:
            zoom 1.3
        attribute tie:
            zoom 1.3
        attribute under:
            zoom 1.3
        attribute witch:
            zoom 1.3
    group face auto:
        attribute angry:
            animblink("nora_angry_")
            zoom 1.3
        attribute basic:
            animblink("nora_basic_")
            zoom 1.3
        attribute embarrassed:
            animblink("nora_embarrassed_")
            zoom 1.3
        attribute grin:
            animblink("nora_grin_")
            zoom 1.3
        attribute sad:
            animblink("nora_sad_")
            zoom 1.3
        attribute sleep:
            animblink("nora_sleep_")
            zoom 1.3
        attribute smile:
            animblink("nora_smile_")
            zoom 1.3
        attribute smirk:
            animblink("nora_smirk_")
            zoom 1.3
        attribute surprised:
            animblink("nora_surprised_")
            zoom 1.3

        attribute angry_cu:
            animblink("nora_angry_cu")
        attribute basic_cu:
            animblink("nora_basic_cu")
        attribute embarrassed_cu:
            animblink("nora_embarrassed_cu")
        attribute grin_cu:
            animblink("nora_grin_cu")
        attribute sad_cu:
            animblink("nora_sad_cu")
        attribute sleep_cu:
            animblink("nora_sleep_cu")
        attribute smile_cu:
            animblink("nora_smile_cu")
        attribute smirk_cu:
            animblink("nora_smirk_cu")
        attribute surprised_cu:
            animblink("nora_surprised_cu")
    group accessory multiple:
        attribute broom:
            "nora_accessory_broom"
            zoom 1.3
            pos(-3, 17)
        attribute hat:
            "nora_accessory_hat"
            zoom 1.3
            pos(38, -77)
        attribute broom_cu:
            "nora_accessory_broom_cu"
            pos(-144, 57)
        attribute hat_cu:
            "nora_accessory_hat_cu"
            pos(-21, -224)

transform nora_cu:
    xanchor 350
    xpos stagepos[1]
    ycenter 325

init python:
    def nora_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 226
            mcy = 193
        else:
            mcx = 121
            mcy = 62