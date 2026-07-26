label investment_opportunity_001:

    scene black

    n "Having spent the afternoon at the palace, you sit in one of its many private studies watching the sun set across Isa Bellmaré."

    n "You take a deep breath, enjoying this moment of solitude and peace, rarely afforded to you these turbulent days."

    n "Of course, you know this wasn't to last long."

    n "As if on cue, you hear a knock on the door, and a servant informs you that Furique requested to speak with you."

    menu:

        "Very well. I'll see him in here.":

            n "The servant swiftly leaves the room, and before long, Furique enters in his stead."

            n "He carries with him various folders of considerable size, you only hope he readied cliff notes as well..."

        "Have him meet me in the council chambers, I'll be there soon.":

            n "The servant nods, and leaves to convey your arranged meeting."

            n "You take one final look at the magnificent view."

            n "You march from one end of the palace to the other."

            n "As you enter the council chambers, Furique is already there waiting."

            n "He has sprawled out on the table various folders of considerable size, you only hope he readied cliff notes as well..."

    show furique

    f "Your Majesty, as per your previous request, I have compiled several development plans which we could use to ideally put a spur back into the economy. If you please."

    n "He gestures to his folders."

    n "At first your stomach sinks thinking you'll have to read each one in its entirety."

    n "Upon opening the first, you see a summary page resting on top of a novel's worth of paper."

    n "You peer at Furique."

    n "He wears a humorous grin."

    n "Evidently he found your silent dread quite amusing."

    menu:

        "Cash Crop Plantations in the Tropical Zereck Northern Territories (-4 Budget, 2 Turn Construction, +3 Budget/Turn after completion)":

            $ treasury -= 4

            $ add_project(
                "Cash Crop Development Program",
                [
                    "Mestwabele Sturquar",
                    "Paolanii"
                ],
                2,
                3,
                5
            )

            n "The plantation program is approved."

        "New Mining Sites in the Resource Rich Caetzan Southern Territories (-6 Budget, 2 Turn Construction, +4 Budget/Turn after completion)":

            $ treasury -= 6

            $ add_project(
                "Southern Mining Initiative",
                [
                    "Rizzi Empeliamus",
                    "Troma"
                ],
                2,
                4,
                -3
            )

            n "The mining initiative is approved."

        "Both Plantation and Mining Sites (-9 Budget, 5 Turn Construction, +8 Budget/Turn after completion)":

            $ treasury -= 9

            $ add_project(
                "Imperial Economic Expansion",
                [
                    "Mestwabele Sturquar",
                    "Paolanii",
                    "Rizzi Empeliamus",
                    "Troma"
                ],
                5,
                8,
                3
            )

            n "A comprehensive development package is approved."

    n "The meeting concludes."

    $ events_completed_this_turn += 1

    $ active_event = False

    $ current_event = None

    hide furique

    call screen galaxy_map

    jump empire_overview