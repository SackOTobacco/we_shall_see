image catheljunta_background = Transform(
    "images/Catheljunta_Background.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)

image reception_hall_background = Transform(
    "images/Reception_Hall_Background.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)


init python:

    def reception_source_lines():
        with renpy.file("events/reception_001_source.txt") as event_file:
            return event_file.read().decode("utf-8").splitlines()


    def reception_choice_positions():
        return [index for index, line in enumerate(reception_source_lines())
                if line.strip().startswith("Dialog Choice")]


    def reception_reconvene_positions():
        return [index for index, line in enumerate(reception_source_lines())
                if line.strip() == "Reconvene:"]


    def reception_choice_text(choice_number):
        """Return the first spoken/action line after a numbered choice marker."""
        lines = reception_source_lines()
        start = reception_choice_positions()[choice_number - 1] + 1
        for line in lines[start:]:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                continue
            return line
        raise Exception("Reception choice {} has no text.".format(choice_number))


    def reception_say_content(lines):
        """Display source lines while ignoring event-structure and stat markers."""
        portrait_exit_lines = {
            "Drinks and food were served, eventually dances took up between guests, however most of the foreign species abstained, likely not knowing our fashionable gallenes.",
            "She rejoined the crowd, already looking for a new dance partner.",
            "I nodded my farewell to them.",
        }
        speakers = {
            "Narrator": n, "Pherip": p, "Quixote": q, "Solène Lapis": solene,
            "Robertz fue Tholedo": robertz, "Isine fue Tholedo": isine,
            "Charristo fue Tholedo": charristo, "Sicill fue Tholedo": sicill,
            "Maté fue Tholedo": mate, "Cálitz fue Tholedo": calitz, "Crowd": None,
        }
        portraits = {
            "Quixote": "quixote",
            "Solène Lapis": "solene",
            "Robertz fue Tholedo": "robertz",
            "Isine fue Tholedo": "isine",
            "Charristo fue Tholedo": "charristo",
            "Sicill fue Tholedo": "sicill",
            "Maté fue Tholedo": "mate",
            "Cálitz fue Tholedo": "calitz",
        }
        speaker = n
        for line in lines:
            line = line.strip()
            if not line or line == "(Hidden)" or line.startswith("Dialog Choice") or line == "Reconvene:":
                continue
            if line.endswith(":") and line[:-1] in speakers:
                speaker = speakers[line[:-1]]
                portrait = portraits.get(line[:-1])
                if portrait:
                    renpy.show(portrait, tag="portrait", zorder=0)
                continue
            if line.startswith(("Popularity ", "Burghers Approval ", "Legitimacy ", "Imperial Majesty ", "Budget ", "+", "-")):
                continue

            if line in portrait_exit_lines:
                renpy.hide("portrait")

            if line.startswith("Our ascending and bumpy ride continued to the peak of Mount Esquoraine"):
                renpy.show(
                    "catheljunta_background",
                    tag="event_background",
                    zorder=-100
                )

            if line.startswith("The crowd followed cautiously, not wanting to get too close before I took my seat at my camp throne"):
                renpy.show(
                    "reception_hall_background",
                    tag="event_background",
                    zorder=-100
                )

            renpy.say(n if speaker is None else speaker, line)


    def reception_say_choice(choice_number):
        """Display a selected choice and its branch until the next flow marker."""
        lines = reception_source_lines()
        start = reception_choice_positions()[choice_number - 1]
        markers = reception_choice_positions() + reception_reconvene_positions()
        end = min([marker for marker in markers if marker > start] or [len(lines)])
        reception_say_content(lines[start:end])


    def reception_say_reconvene(reconvene_number):
        """Display shared dialogue after a Reconvene marker until the next choice."""
        lines = reception_source_lines()
        start = reception_reconvene_positions()[reconvene_number - 1]
        end = min([marker for marker in reception_choice_positions() if marker > start] or [len(lines)])
        reception_say_content(lines[start:end])


    def reception_say_intro():
        """Display the opening narration before the first choice."""
        lines = reception_source_lines()
        start = next(index for index, line in enumerate(lines) if line.strip() == "Narrator:")
        end = reception_choice_positions()[0]
        reception_say_content(lines[start:end])


label reception_001:

    scene
    show expression Transform(
        "images/Isa_Bellmaré_Background.png",
        xsize=config.screen_width,
        ysize=config.screen_height
    ) as event_background zorder -100
    $ reception_say_intro()

    $ carriage_choice = renpy.display_menu([
        (reception_choice_text(1), "slow"),
        (reception_choice_text(2), "footboard"),
        (reception_choice_text(3), "encourage"),
        (reception_choice_text(4), "fast"),
    ])
    if carriage_choice == "slow":
        $ popularity += 1
        $ burgher_approval += 1
        $ imperial_majesty -= 1
        $ reception_say_choice(1)
    elif carriage_choice == "footboard":
        $ popularity += 2
        $ imperial_majesty -= 1
        $ reception_say_choice(2)
    elif carriage_choice == "encourage":
        $ imperial_majesty += 1
        $ reception_say_choice(3)
    else:
        $ imperial_majesty += 2
        $ popularity -= 1
        $ reception_say_choice(4)
    $ reception_say_reconvene(1)

    $ solene_choice = renpy.display_menu([
        (reception_choice_text(5), "family"),
        (reception_choice_text(9), "transaction"),
        (reception_choice_text(10), "cordial"),
    ])
    if solene_choice == "family":
        $ solene_relationship += 1
        $ reception_say_choice(5)
        $ solene_family_choice = renpy.display_menu([
            (reception_choice_text(6), "train"),
            (reception_choice_text(7), "dance"),
            (reception_choice_text(8), "nod"),
        ])
        if solene_family_choice == "train":
            $ solene_relationship += 1
            $ reception_say_choice(6)
        elif solene_family_choice == "dance":
            $ reception_say_choice(7)
        else:
            $ reception_say_choice(8)
    elif solene_choice == "transaction":
        $ solene_relationship -= 1
        $ reception_say_choice(9)
    else:
        $ solene_relationship += 1
        $ reception_say_choice(10)
        $ solene_marriage_choice = renpy.display_menu([
            (reception_choice_text(11), "portrait"),
            (reception_choice_text(12), "wait"),
        ])
        if solene_marriage_choice == "portrait":
            $ solene_relationship += 1
            $ reception_say_choice(11)
        else:
            $ reception_say_choice(12)
    $ reception_say_reconvene(2)

    $ burgher_choice = renpy.display_menu([
        (reception_choice_text(13), "reject"),
        (reception_choice_text(14), "receive"),
    ])
    if burgher_choice == "reject":
        $ imperial_majesty += 2
        $ reception_say_choice(13)
    else:
        $ treasury += 1
        $ burgher_approval += 1
        $ reception_say_choice(14)
    $ reception_say_reconvene(3)

    $ family_choice = renpy.display_menu([
        (reception_choice_text(15), "drink"),
        (reception_choice_text(16), "throne"),
        (reception_choice_text(17), "family"),
    ])
    if family_choice == "drink":
        $ robertz_relationship += 1
        $ reception_say_choice(15)
    elif family_choice == "throne":
        $ reception_say_choice(16)
    else:
        $ reception_say_choice(17)
        $ charristo_choice = renpy.display_menu([
            (reception_choice_text(18), "balance"),
            (reception_choice_text(19), "subjects"),
            (reception_choice_text(20), "family"),
        ])
        if charristo_choice == "balance":
            $ charristo_relationship += 1
            $ reception_say_choice(18)
        elif charristo_choice == "subjects":
            $ isine_relationship -= 1
            $ robertz_relationship -= 2
            $ charristo_relationship += 3
            $ mate_relationship -= 1
            $ calitz_relationship -= 1
            $ sicill_relationship -= 1
            $ reception_say_choice(19)
        else:
            $ isine_relationship += 1
            $ robertz_relationship += 2
            $ charristo_relationship -= 2
            $ mate_relationship += 1
            $ calitz_relationship += 1
            $ sicill_relationship += 1
            $ reception_say_choice(20)
    $ reception_say_reconvene(4)

    $ mother_choice = renpy.display_menu([
        (reception_choice_text(21), "miss"),
        (reception_choice_text(22), "spirit"),
        (reception_choice_text(23), "honor"),
        (reception_choice_text(24), "silent"),
    ])
    if mother_choice == "miss":
        $ isine_relationship += 1
        $ reception_say_choice(21)
    elif mother_choice == "spirit":
        $ mate_relationship += 1
        $ reception_say_choice(22)
    elif mother_choice == "honor":
        $ isine_relationship += 1
        $ reception_say_choice(23)
    else:
        $ reception_say_choice(24)
    $ reception_say_reconvene(5)

    hide portrait

    $ current_event = "grand_council_001"
    call screen galaxy_map
    return
