init python:

    MAP_ZOOM_STEP = 0.25
    MAP_MIN_ZOOM = 3.0
    MAP_MAX_ZOOM = 8.0

    def adjust_map_zoom(amount):
        global map_zoom

        map_zoom = max(MAP_MIN_ZOOM, min(MAP_MAX_ZOOM, map_zoom + amount))
        renpy.restart_interaction()

screen galaxy_map(from_event=False):

    key "mousedown_4" action Function(adjust_map_zoom, MAP_ZOOM_STEP)
    key "mousedown_5" action Function(adjust_map_zoom, -MAP_ZOOM_STEP)

    add Solid("#112233")

    viewport:

        xfill True
        yfill True

        draggable True
        mousewheel False
        scrollbars None

        xinitial 0.49
        yinitial 0.26

        fixed:

            xsize int(3600 * map_zoom)
            ysize int(3600 * map_zoom)

            add "images/world_map.png":

                zoom map_zoom

            # Isa Bellmaré (Capital)

            textbutton "★":

                xpos int(9700 / 5.5 * map_zoom)
                ypos int(5100 / 5.5 * map_zoom)

                text_size int(300 / 5.5 * map_zoom)

                action Show(
                    "location_panel",
                    location="isa_bellmare",
                    from_event=from_event
                )

            # Mestwabele Sturquar

            textbutton "●":

                xpos int(10900 / 5.5 * map_zoom)
                ypos int(3200 / 5.5 * map_zoom)

                text_size int(200 / 5.5 * map_zoom)

                action Show(
                    "location_panel",
                    location="mestwabele",
                    from_event=from_event
                )

            # Paolanii

            textbutton "●":

                xpos int(11900 / 5.5 * map_zoom)
                ypos int(5070 / 5.5 * map_zoom)

                text_size int(200 / 5.5 * map_zoom)

                action Show(
                    "location_panel",
                    location="paolanii",
                    from_event=from_event
                )

            # Rizzi Empeliamus

            textbutton "●":

                xpos int(10200 / 5.5 * map_zoom)
                ypos int(7000 / 5.5 * map_zoom)

                text_size int(200 / 5.5 * map_zoom)

                action Show(
                    "location_panel",
                    location="rizzi",
                    from_event=from_event
                )

            # Troma

            textbutton "●":

                xpos int(9800 / 5.5 * map_zoom)
                ypos int(7600 / 5.5 * map_zoom)

                text_size int(200 / 5.5 * map_zoom)

                action Show(
                    "location_panel",
                    location="troma",
                    from_event=from_event
                )

    if from_event:

        frame:

            xalign 1.0
            xoffset -20
            ypos 10

            textbutton "Return to Event":
                action Hide("galaxy_map")

    use topbar
