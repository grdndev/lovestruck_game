layeredimage blossom:
    xanchor 138
    ycenter 590
    group outfit auto:
        attribute faerie:
            zoom 1.27
        attribute school:
            zoom 1.27
    group face auto:
        attribute angry:
            animblink("blossom_angry_")
            zoom 1.27
        attribute basic:
            animblink("blossom_basic_")
            zoom 1.27
        attribute sleep:
            animblink("blossom_sleep_")
            zoom 1.27
        attribute smile:
            animblink("blossom_smile_")
            zoom 1.27
        attribute surprised:
            animblink("blossom_surprised_")
            zoom 1.27

        attribute angry_cu:
            animblink("blossom_angry_cu")
        attribute basic_cu:
            animblink("blossom_basic_cu")
        attribute sleep_cu:
            animblink("blossom_sleep_cu")
        attribute smile_cu:
            animblink("blossom_smile_cu")
        attribute surprised_cu:
            animblink("blossom_surprised_cu")


transform blossom_cu:
    xanchor 400
    xpos stagepos[1]
    ycenter 396

init python:
    def blossom_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 292
            mcy = 289
        else:
            mcx = 104
            mcy = 133