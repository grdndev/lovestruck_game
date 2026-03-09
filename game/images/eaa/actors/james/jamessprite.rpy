layeredimage james:
    xanchor 164
    ycenter 710
    group outfit auto:
        attribute casual:
            zoom 1.35
    group face auto:
        attribute angry:
            animblink("james_angry_")
            zoom 1.35
        attribute basic:
            animblink("james_basic_")
            zoom 1.35
        attribute smile:
            animblink("james_smile_")
            zoom 1.35
        attribute sleep:
            animblink("james_sleep_")
            zoom 1.35
        attribute surprised:
            animblink("james_surprised_")
            zoom 1.35

        attribute angry_cu:
            animblink("james_angry_cu")
        attribute basic_cu:
            animblink("james_basic_cu")
        attribute smile_cu:
            animblink("james_smile_cu")
        attribute sleep_cu:
            animblink("james_sleep_cu")
        attribute surprised_cu:
            animblink("james_surprised_cu")

transform james_cu:
    xanchor 448
    xpos stagepos[1]
    ycenter 400

init python:
    def james_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = 343
            mcy = 234
        else:
            mcx = 124
            mcy = 84