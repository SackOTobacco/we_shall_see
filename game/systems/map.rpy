init python:

    MAP_IMAGE_WIDTH = 3600
    MAP_IMAGE_HEIGHT = 3600

    MAP_INITIAL_ZOOM = 5.5

    MAP_ZOOM_STEP = 0.15
    MAP_MIN_ZOOM = 0.5
    MAP_MAX_ZOOM = 8.0

    # Original starting position.
    MAP_X_INITIAL = 0.49
    MAP_Y_INITIAL = 0.26


    def adjust_map_zoom(amount, x_adjustment, y_adjustment):

        global map_zoom

        old_zoom = map_zoom

        new_zoom = max(
            MAP_MIN_ZOOM,
            min(MAP_MAX_ZOOM, map_zoom + amount)
        )

        # Don't do anything if we're already at the limit.
        if new_zoom == old_zoom:
            return

        # ----------------------------------------------------
        # Find the map point currently underneath the CENTER
        # of the screen.
        # ----------------------------------------------------

        screen_center_x = config.screen_width / 2.0
        screen_center_y = config.screen_height / 2.0

        current_scroll_x = x_adjustment.value
        current_scroll_y = y_adjustment.value

        # Convert the current screen-center position into
        # native map coordinates.

        map_center_x = (
            current_scroll_x + screen_center_x
        ) / old_zoom

        map_center_y = (
            current_scroll_y + screen_center_y
        ) / old_zoom


        # ----------------------------------------------------
        # Change the zoom.
        # ----------------------------------------------------

        map_zoom = new_zoom


        # ----------------------------------------------------
        # Calculate the new viewport position needed to keep
        # the EXACT SAME map point underneath the screen center.
        # ----------------------------------------------------

        new_scroll_x = (
            map_center_x * new_zoom
            - screen_center_x
        )

        new_scroll_y = (
            map_center_y * new_zoom
            - screen_center_y
        )


        # ----------------------------------------------------
        # Keep the viewport inside its legal scrolling range.
        # ----------------------------------------------------

        if x_adjustment.range is not None:

            new_scroll_x = max(
                0,
                min(
                    x_adjustment.range,
                    new_scroll_x
                )
            )

        if y_adjustment.range is not None:

            new_scroll_y = max(
                0,
                min(
                    y_adjustment.range,
                    new_scroll_y
                )
            )


        # Apply the corrected viewport position.

        x_adjustment.value = new_scroll_x
        y_adjustment.value = new_scroll_y

        renpy.restart_interaction()


default map_x_adjustment = ui.adjustment()
default map_y_adjustment = ui.adjustment()
default map_suzerain_hovered = False
default map_eternal_star_hovered = False


screen galaxy_map(from_event=False):

    # The map is a separate interaction from the event underneath it. Keep
    # it above overlay controls and make it modal so pointer and keyboard
    # input cannot fall through to dialogue or other screens.
    zorder 200
    modal True

    # ========================================================
    # MOUSE WHEEL = ZOOM
    # ========================================================

    key "mousedown_4" action Function(
        adjust_map_zoom,
        MAP_ZOOM_STEP,
        map_x_adjustment,
        map_y_adjustment
    )

    key "mousedown_5" action Function(
        adjust_map_zoom,
        -MAP_ZOOM_STEP,
        map_x_adjustment,
        map_y_adjustment
    )

    # ========================================================
    # MAP SCALE
    # ========================================================

    $ map_scale = map_zoom / MAP_INITIAL_ZOOM


    add Solid("#112233")


    # ========================================================
    # VIEWPORT
    # ========================================================
    #
    # The viewport handles:
    #
    #   LEFT CLICK + DRAG = PAN
    #
    # The screen-level keys handle:
    #
    #   MOUSE WHEEL = ZOOM
    #
    # They no longer fight over the map position.
    #

    viewport:

        xfill True
        yfill True

        draggable True
        mousewheel False
        scrollbars None

        xadjustment map_x_adjustment
        yadjustment map_y_adjustment

        # Original starting viewpoint.

        xinitial 0.327
        yinitial 0.169


        fixed:

            # Keep the viewport's content space constant.
            # This MUST NOT depend on map_zoom.

            xsize int(
                MAP_IMAGE_WIDTH * MAP_MAX_ZOOM
            )

            ysize int(
                MAP_IMAGE_HEIGHT * MAP_MAX_ZOOM
            )


            # ====================================================
            # MAP
            # ====================================================

            if map_eternal_star_hovered or (
                renpy.get_screen("codex_popup") is not None
                and codex_current == "eternal_star"
            ):

                add "images/world_map_Eternal_Star_Glow.png":

                    xpos 0
                    ypos 0

                    zoom map_zoom

            elif map_suzerain_hovered:

                add "images/world_map_Suzerain_Glow.png":

                    xpos 0
                    ypos 0

                    zoom map_zoom

            else:

                add "images/world_map.png":

                    xpos 0
                    ypos 0

                    zoom map_zoom

            # The images and hit mask share native map coordinates, so the
            # viewport moves and scales all three together.
            mousearea:

                area (
                    0,
                    0,
                    int(MAP_IMAGE_WIDTH * map_zoom),
                    int(MAP_IMAGE_HEIGHT * map_zoom)
                )

                focus_mask Transform(
                    "images/world_map_suzerain_hitmask.png",
                    zoom=map_zoom
                )

                hovered SetVariable("map_suzerain_hovered", True)
                unhovered SetVariable("map_suzerain_hovered", False)

            mousearea:

                area (
                    0,
                    0,
                    int(MAP_IMAGE_WIDTH * map_zoom),
                    int(MAP_IMAGE_HEIGHT * map_zoom)
                )

                focus_mask Transform(
                    "images/world_map_eternal_star_hitmask.png",
                    zoom=map_zoom
                )

                hovered SetVariable("map_eternal_star_hovered", True)
                unhovered SetVariable("map_eternal_star_hovered", False)

            button:

                xpos 0
                ypos 0

                xsize int(MAP_IMAGE_WIDTH * map_zoom)
                ysize int(MAP_IMAGE_HEIGHT * map_zoom)

                padding (0, 0)
                background None
                hover_background None

                focus_mask Transform(
                    "images/world_map_eternal_star_hitmask.png",
                    zoom=map_zoom
                )

                action Function(codex_link, "eternal_star")

                null:
                    xsize int(MAP_IMAGE_WIDTH * map_zoom)
                    ysize int(MAP_IMAGE_HEIGHT * map_zoom)


            # ====================================================
            # ISA BELLMARÉ
            # ====================================================

            textbutton "★":

                xpos int(
                    (9700 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                ypos int(
                    (5100 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                text_size int(
                    300 * map_scale
                )

                action Show(
                    "location_panel",
                    location="isa_bellmare",
                    from_event=from_event
                )


            # ====================================================
            # MESTWABELE STURQUAR
            # ====================================================

            textbutton "●":

                xpos int(
                    (10900 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                ypos int(
                    (3200 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                text_size int(
                    200 * map_scale
                )

                action Show(
                    "location_panel",
                    location="mestwabele",
                    from_event=from_event
                )


            # ====================================================
            # PAOLANII
            # ====================================================

            textbutton "●":

                xpos int(
                    (11900 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                ypos int(
                    (5070 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                text_size int(
                    200 * map_scale
                )

                action Show(
                    "location_panel",
                    location="paolanii",
                    from_event=from_event
                )


            # ====================================================
            # RIZZI EMPELIAMUS
            # ====================================================

            textbutton "●":

                xpos int(
                    (10200 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                ypos int(
                    (7000 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                text_size int(
                    200 * map_scale
                )

                action Show(
                    "location_panel",
                    location="rizzi",
                    from_event=from_event
                )


            # ====================================================
            # TROMA
            # ====================================================

            textbutton "●":

                xpos int(
                    (9800 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                ypos int(
                    (7600 / MAP_INITIAL_ZOOM)
                    * map_zoom
                )

                text_size int(
                    200 * map_scale
                )

                action Show(
                    "location_panel",
                    location="troma",
                    from_event=from_event
                )


    # ========================================================
    # RETURN TO EVENT
    # ========================================================

    if from_event:

        frame:

            xalign 1.0
            xoffset -20
            ypos 10

            textbutton "Return to Event":

                action Hide("galaxy_map")


    # ========================================================
    # TOP BAR
    # ========================================================

    use topbar
