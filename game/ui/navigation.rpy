screen navigation():

    frame:

        xpos 10
        ypos 100

        vbox:

            spacing 15

            textbutton "Empire":
                action Return("map")

            textbutton "Overview":
                action Return("overview")

            textbutton "Codex":
                action Return("codex")