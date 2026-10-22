label prologue_001:

    menu:
        "Did you befriend Bourbon Landstrouss?"

        "Yes":
            $ prologue_befriended = True

        "No":
            $ prologue_befriended = False

    menu:
        "Choose a nation to have studied..."

        "Aeteran":
            $ prologue_origin = "Aeteran"

    return
