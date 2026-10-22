screen codex_hover_tooltip(heading, description, tooltip_x, tooltip_y):
    modal False
    sensitive False
    zorder 200

    frame:
        xpos tooltip_x
        ypos tooltip_y
        xsize 440
        padding (1, 1)
        background "#9a7c3b"

        frame:
            xfill True
            padding (20, 15)
            background "#11110f"

            vbox:
                xfill True
                spacing 10

                text heading:
                    xalign 0.5
                    text_align 0.5
                    size 22
                    color "#d8bd78"

                add Solid("#806a3d") xsize 360 ysize 1 xalign 0.5

                text description:
                    xalign 0.5
                    text_align 0.5
                    xmaximum 380
                    size 18
                    color "#d0cec8"
