layeredimage sly:
    xanchor 186
    ycenter 610
    group outfit auto:
        attribute casual:
            zoom 1.2
    group face auto:
        attribute angry:
            animblink("sly_angry_")
            zoom 1.2
        attribute basic:
            animblink("sly_basic_")
            zoom 1.2
        attribute smirk:
            animblink("sly_smirk_")
            zoom 1.2
        attribute surprised:
            animblink("sly_surprised_")
            zoom 1.2

        attribute angry_cu:
            animblink("sly_angry_cu")
        attribute smirk_cu:
            animblink("sly_smirk_cu")
        attribute surprised_cu:
            animblink("sly_surprised_cu")


transform sly_cu:
    xanchor 500
    xpos stagepos[1]
    ycenter 380

init python:
    def sly_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 388
            mcy = 209
        else:
            mcx = 152
            mcy = 59