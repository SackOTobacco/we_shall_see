screen location_panel(location, from_event=False):

    frame:

        xalign 0.5
        yalign 0.5

        padding (20, 20)

        vbox:

            spacing 15

            text CODEX[location]["name"]

            textbutton "View Codex":

                action [
                    Hide("location_panel"),
                    Show(
                        "codex_screen",
                        location=location
                    )
                ]

            if location == "isa_bellmare" and active_event and from_event:

                textbutton "Return to Event":

                    action [
                        Hide("location_panel"),
                        Hide("galaxy_map")
                    ]

            elif location == "isa_bellmare" and active_event:

                textbutton "Review Matters":

                    action [
                        Hide("location_panel"),
                        Jump(current_event)
                    ]

            if location == "isa_bellmare":

                textbutton "Imperial Administration":

                    action [
                        Hide("location_panel"),
                        Jump("empire_overview")
                    ]

            textbutton "Close":

                action Hide(
                    "location_panel"
                )
                
screen codex_screen(location):

    frame:

        xalign 0.5
        yalign 0.5

        xsize 1000
        ysize 700

        padding (20, 20)

        vbox:

            spacing 15

            text CODEX[location]["name"]

            text CODEX[location]["title"]

            viewport:

                draggable True
                mousewheel True

                xsize 940
                ysize 500

                scrollbars "vertical"

                text CODEX[location]["text"]:

                    xmaximum 920

            null height 20

            textbutton "Close":

                action Hide(
                    "codex_screen"
                )
