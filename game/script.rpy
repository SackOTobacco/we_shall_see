label start:

    "Empire of Suzerain"

    call screen galaxy_map

    jump empire_overview


label empire_overview:

    if current_turn > max_turns:

        jump ending

    $ result = renpy.call_screen(
        "empire_overview"
    )

    if result == "advance":

        if events_completed_this_turn < events_required_this_turn:

            "There are still matters of state requiring your attention."

            jump empire_overview

        $ current_turn += 1

        $ process_turn()

        $ events_completed_this_turn = 0

        $ active_event = True

        $ assign_turn_event()

        jump empire_overview

    elif result == "map":

        call screen galaxy_map

        jump empire_overview