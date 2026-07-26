screen empire_overview():
    
    use topbar
    use navigation

    frame:

        xalign 0.5
        yalign 0.5

        padding (25, 25)

        vbox:

            spacing 10

            text "Empire of Suzerain"

            text "Turn: [current_turn]"

            text ""

            text "Treasury: [treasury]"
            text "Popularity: [popularity]"
            text "Authority: [authority]"
            text "Military: [military]"

            text ""

            text "Current Treasury Income: [project_income_bonus]"

            text ""

            text "Active Projects"

            if len(active_projects) == 0:

                text "None"

            else:

                for project in active_projects:

                    text "[project['name']]"

                    text "Locations:"

                    for location in project["locations"]:

                        text "• [location]"

                    text "Remaining: [project['turns_remaining']] Turns"

                    text "Revenue: +[project['income_bonus']] Treasury"

                    text ""

            textbutton "Advance Turn":
                action Return("advance")

            textbutton "Open Galaxy Map":
                action Return("map")