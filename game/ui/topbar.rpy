screen topbar():

    frame:

        xpos 20
        ypos 10

        background "#111111"

        padding (10, 5)

        hbox:

            spacing 10

            textbutton "💰 [treasury]":

                action Show(
                    "modifier_tooltip",
                    title="Treasury",
                    modifiers=treasury_modifiers
                )

            textbutton "👑 [authority]":

                action Show(
                    "modifier_tooltip",
                    title="Authority",
                    modifiers=authority_modifiers
                )

            textbutton "👥 [popularity]":

                action Show(
                    "modifier_tooltip",
                    title="Popularity",
                    modifiers=popularity_modifiers
                )

            textbutton "⚔ [military]":

                action Show(
                    "modifier_tooltip",
                    title="Military",
                    modifiers=military_modifiers
                )

            text "🕰 [current_turn]"


screen modifier_tooltip(title, modifiers):

    frame:

        xalign 0.5
        yalign 0.2

        background "#222222"

        padding (20, 20)

        vbox:

            spacing 10

            text "[title]"

            if len(modifiers) == 0:

                text "No modifiers"

            else:

                for name, value in modifiers:

                    text "[value:+] [name]"

            textbutton "Close":

                action Hide("modifier_tooltip")