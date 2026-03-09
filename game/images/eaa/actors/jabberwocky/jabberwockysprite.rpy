layeredimage jabberwocky:
    xanchor 154
    ycenter 415

    group outfit auto
    group face auto:
        attribute angry:
            animblink("jabberwocky_angry_")
        attribute basic:
            animblink("jabberwocky_basic_")
        attribute sad:
            animblink("jabberwocky_sad_")
        attribute sleep:
            animblink("jabberwocky_sleep_")
        attribute smile:
            animblink("jabberwocky_smile_")
        attribute surprised:
            animblink("jabberwocky_surprised_")

        attribute angry_cu:
            animblink("jabberwocky_angry_cu")
        attribute basic_cu:
            animblink("jabberwocky_basic_cu")
        attribute sad_cu:
            animblink("jabberwocky_sad_cu")
        attribute sleep_cu:
            animblink("jabberwocky_sleep_cu")
        attribute smile_cu:
            animblink("jabberwocky_smile_cu")
        attribute surprised_cu:
            animblink("jabberwocky_surprised_cu")

transform jabberwocky_cu:
    xpos 482
    ycenter 500

init python:
    def jabberwocky_facepos(cu):
        global mcx
        global mcy
        if cu:
            mcx = -322
            mcy = -438
        else:
            mcx = -30
            mcy = -192