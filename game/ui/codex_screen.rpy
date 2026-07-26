default codex_current = None

screen codex_popup():

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

        viewport:

            draggable True
            mousewheel True

            ymaximum 650

            text CODEX[codex_current]["text"]

        textbutton "Close":
            action Hide("codex_popup")