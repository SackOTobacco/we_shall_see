default codex_current = None

screen codex_popup():
    default codex_scroll_target = None

    zorder 300
    modal True

    frame:

        xalign 0.5
        yalign 0.08

        xsize 700
        ysize 850

        has vbox

        text CODEX[codex_current]["name"] size 40

        if "title" in CODEX[codex_current]:
            text CODEX[codex_current]["title"] size 22

        null height 20

        # The viewport's native wheel handling is disabled below to avoid it
        # competing with these animated, accumulated wheel steps.
        key "viewport_wheelup" action Function(codex_smooth_scroll, -1)
        key "viewport_wheeldown" action Function(codex_smooth_scroll, 1)

        viewport:
            id "codex_biography"

            draggable True
            mousewheel False

            ymaximum 650

            text CODEX[codex_current]["text"]

        textbutton "Close":
            action Hide("codex_popup")
