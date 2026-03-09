layeredimage rapunzel:
    xanchor 226
    ycenter 650
    group outfit auto:
        attribute casual:
            zoom 1.22
    group face auto:
        attribute angry:
            animblink("rapunzel_angry_")
            zoom 1.22
        attribute basic:
            animblink("rapunzel_basic_")
            zoom 1.22
        attribute grin:
            animblink("rapunzel_grin_")
            zoom 1.22
        attribute sad:
            animblink("rapunzel_sad_")
            zoom 1.22
        attribute surprised:
            animblink("rapunzel_surprised_")
            zoom 1.22

        attribute angry_cu:
            animblink("rapunzel_angry_cu")
        attribute basic_cu:
            animblink("rapunzel_basic_cu")
        attribute grin_cu:
            animblink("rapunzel_grin_cu")
        attribute sad_cu:
            animblink("rapunzel_sad_cu")
        attribute surprised_cu:
            animblink("rapunzel_surprised_cu")

transform rapunzel_cu:
    xanchor 398
    xpos stagepos[1]
    ycenter 340

init python:
    def rapunzel_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 293
            mcy = 236
        else:
            mcx = 193
            mcy = 74