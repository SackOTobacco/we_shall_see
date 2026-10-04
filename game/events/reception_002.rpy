image almorthy_background = Transform(
    "images/Almörthy_Background.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)

image almorthy_banquet_hall_background = Transform(
    "images/Almörthy_Banquet_Hall_Background.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)

image almorthy_courtyard_background = Transform(
    "images/Almörthy_Courtyard_Background.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)

image royal_great_cabin_background = Transform(
    "images/Royal_Great_Cabin.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)

define zichy = Character("Zichy Hoovitz")
define joziff = Character("Józiff Ivanothy")
define bourbon = Character("Bourbon Landstrouss")
define zladisyormund = Character("Zladisyormund Kesfer")

image zichy_portrait = Transform("images/Zichy_Hoovitz.png", yoffset=-5)
image joziff_portrait = Transform("images/Józiff_Ivanothy.png", yoffset=-5)
image bourbon_portrait = Transform("images/Bourbon_Landstrouss.png", yoffset=-5)
image zladisyormund_portrait = Transform("images/Zladisyormund_Kesfer.png", yoffset=-5)

init python:
    import re

    # Narration keeps the current portrait by default. These lines explicitly
    # mark a break away from the active character presentation in reception_002.
    RECEPTION_002_NARRATOR_SCENE_BREAKS = {
        "He left to find this merchant friend of Józiff.",
        "I was left with the Prince-Regent. We sat in silence whilst working on our plates.",
        "I was escorted outside to a snow covered garden courtyard, the crunch of snow and pebbles beneath my feet were all my mind focused on between the murmurs of the Nobles and the organizing by Józiff to make room for us.",
        "Traversing through the halls I was just gleefully toured in by the same crowd now chasing shoving guards and shouting for Zichy’s release, it was baffling how quickly things had turned sour.",
        "My brothers continued to argue.",
        "Finally we made it to my shuttle. Józiff remained by my side until I stepped on the boarding ramp, after which he turned to the crowd.",
        "I boarded the shuttle and we made off, leaving my guards to help Józiff stave off what to me seemed a potential rebellion.",
        "Back on my flagship, we took a day in orbit to observe the situation.",
        "They disconnected.",
        "Józiff bowed his head and left. I was with my food yet uneaten, and now no company which to distract me from my obligation.",
        "I made my way to Józiff, who introduced me to his entourage of prominent and like-minded Nobles, then we headed off to another wing of the palace. It was a hardy hunting room filled with pelts, trophies, and tapestries of past excursions.",
        "I made my way out of the palace grounds with only my retinue, and from there the shuttle took me back to the fleet and my capital ship.",
        "I awoke the next morning on one of the soft couches, seeing the others in similar states all around the room.",
    }

    def reception_002_parse_source():
        with renpy.file("events/reception_002_source.txt") as source_file:
            lines = source_file.read().decode("utf-8-sig").splitlines()
        events = []
        current = []
        mode = "intro"
        for line in lines[1:]:
            if line.strip() == "Reconvene:":
                events.append(("menu", current))
                current = []
                mode = "shared"
            elif reception_002_choice_header(line):
                if mode in ("intro", "shared") and current:
                    events.append((mode, current))
                    current = []
                mode = "menu"
                current.append(line)
            else:
                current.append(line)
        if current:
            events.append((mode, current))
        expanded = []
        for kind, content in events:
            if kind != "menu":
                expanded.append((kind, content))
                continue
            starts = []
            seen_roots = set()
            for index, line in enumerate(content):
                header = reception_002_choice_header(line)
                if header and "." not in header[0]:
                    if header[0] in seen_roots:
                        boundary = index
                        # Keep an explicit alternate-route condition with the menu it governs.
                        for prior in range(index - 1, -1, -1):
                            if content[prior].strip().startswith("(If player"):
                                boundary = prior
                                break
                            if reception_002_choice_header(content[prior]):
                                break
                        starts.append((boundary, index))
                    seen_roots.add(header[0])
            if not starts:
                expanded.append((kind, content))
                continue
            begin = 0
            for split_number, (boundary, index) in enumerate(starts):
                if boundary > begin:
                    first_menu = content[begin:boundary]
                    if split_number == 0 and any(
                            "if player didn’t chose to befriend" in item.lower()
                            or "if player didn't chose to befriend" in item.lower()
                            for item in content[boundary:index]):
                        first_menu = ["(If player chose to befriend in prologue)"] + first_menu
                    expanded.append(("menu", first_menu))
                    expanded.append(("shared", content[boundary:index]))
                begin = index
            if begin < len(content):
                expanded.append(("menu", content[begin:]))
        return lines, expanded

    def reception_002_choice_header(line):
        match = re.match(r"^\s*Dialog Choice #([0-9.]+)(.*)$", line)
        if not match:
            return None
        return match.group(1).rstrip("."), match.group(2).strip()

    def reception_002_nodes(lines):
        nodes = {}
        order = []
        current = None
        for line in lines:
            header = reception_002_choice_header(line)
            if header:
                current = header[0]
                nodes[current] = {"id": current, "meta": header[1], "body": [], "children": []}
                order.append(current)
            elif current is not None:
                nodes[current]["body"].append(line)
        for choice_id in order:
            parent = choice_id.rpartition(".")[0]
            if parent in nodes:
                nodes[parent]["children"].append(choice_id)
        return nodes, [choice_id for choice_id in order if "." not in choice_id]

    def reception_002_choice_text(node):
        for raw in node["body"]:
            line = raw.strip()
            if not line or line.endswith(":") or line.startswith("(") or line.startswith(("+", "-")):
                continue
            return line
        return node["id"]

    def reception_002_condition(text):
        lower = text.lower()
        if "if“aeteran”chosen" in lower or "if “aeteran” chosen" in lower or "if \"aeteran\" chosen" in lower:
            return prologue_origin == "Aeteran"
        if "aeteran" in lower and "not chosen in prologue" in lower:
            return prologue_origin != "Aeteran"
        if "unlocked if" in lower and "aeteran" in lower:
            return prologue_origin == "Aeteran"
        if "if player chose to befriend" in lower:
            store.reception_002_route_condition = True
            return prologue_befriended
        if "if player didn’t chose to befriend" in lower or "if player didn't chose to befriend" in lower:
            store.reception_002_route_condition = False
            return not prologue_befriended
        if "if dialog choice" in lower and "chosen in reception_002" in lower:
            referenced = re.findall(r"dialog choice #(\d+(?:\.\d+)*)", lower)
            return any(item in reception_002_chosen_choices for item in referenced)
        return True

    def reception_002_apply_effect(line):
        if line.strip() == "Guarantees Aeteran declares independence":
            store.aeteran_independence_guaranteed = True
            return True
        match = re.match(r"^([+-])(\d+)\s+(.+?)\s*$", line.strip())
        if not match:
            return False
        amount = int(match.group(2)) * (1 if match.group(1) == "+" else -1)
        name = match.group(3).strip().lower()
        if name.startswith("aeteran relations"):
            store.aeteran_relations += amount
        elif name.startswith("bourbon relationship"):
            store.bourbon_relationship += amount
        elif name.startswith("imperial majesty"):
            if "per turn" in name:
                store.legitimacy_modifiers.append(("reception_002", amount))
            else:
                store.imperial_majesty += amount
        elif name.startswith("legitimacy"):
            store.imperial_majesty += amount
        elif name.startswith("treasury"):
            if "per turn" in name:
                store.treasury_modifiers.append(("Aeteran", amount))
            else:
                store.treasury += amount
        else:
            return False
        return True

    def reception_002_say(lines):
        speakers = {
            "Narrator": n, "Pherip": p, "Zichy Hoovitz": zichy,
            "Józiff Ivanothy": joziff, "Bourbon Landstrouss": bourbon,
            "Zladisyormund Kesfer": zladisyormund,
            "Charristo fue Tholedo": charristo, "Robertz fue Tholedo": robertz,
        }
        portraits = {
            "Zichy Hoovitz": "zichy_portrait",
            "Józiff Ivanothy": "joziff_portrait",
            "Bourbon Landstrouss": "bourbon_portrait",
            "Zladisyormund Kesfer": "zladisyormund_portrait",
            "Charristo fue Tholedo": "charristo",
            "Robertz fue Tholedo": "robertz",
        }
        speaker = n
        conditional_allowed = True
        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            if line in ("(Hidden)", "(Event Ends Here)", "(Continues Dialog)", "Repeated:"):
                continue
            if line.startswith("Dialog Choice #"):
                continue
            if line.endswith(":") and line[:-1] in speakers:
                speaker = speakers[line[:-1]]
                portrait = portraits.get(line[:-1])
                if portrait:
                    renpy.show(portrait, tag="portrait", zorder=0)
                continue
            if reception_002_apply_effect(line):
                continue
            if line.startswith("(If "):
                conditional_allowed = reception_002_condition(line)
                speaker = n
                continue
            if line.startswith("(Unlocked "):
                if not reception_002_condition(line):
                    conditional_allowed = False
                speaker = n
                continue
            if not conditional_allowed:
                if line.startswith("(Continue as if Dialog Choice #"):
                    continue
                if line.endswith(":"):
                    continue
                if line.startswith("(If "):
                    conditional_allowed = reception_002_condition(line)
                continue
            if line.startswith("(Continue as if Dialog Choice #"):
                target = re.search(r"#([0-9.]+)", line).group(1).rstrip(".")
                reception_002_run_node(target)
                speaker = n
                continue
            if speaker is n and line in RECEPTION_002_NARRATOR_SCENE_BREAKS:
                renpy.hide("portrait")
            if line == "Eventually I was brought to the main dining hall housing a massive decorated tile stove, a staple of Aeteran. It was made of lime green and rose pink ceramic, the only source of color in an otherwise dark chamber.":
                renpy.show(
                    "almorthy_banquet_hall_background",
                    tag="event_background",
                    zorder=-100
                )
            if line == "I was led by enthusiastic Aeteran Nobles through the royal palace, Almörthy. They showed me various turrets and towers which protruded from the main structure, great halls lined with tapestries of various hunts and battles the Nobles took part in, all interiorly designed in dark carved wood and arches that gave a serious character to the whole place.":
                renpy.show(
                    "almorthy_background",
                    tag="event_background",
                    zorder=-100
                )
            if line == "I was escorted outside to a snow covered garden courtyard, the crunch of snow and pebbles beneath my feet were all my mind focused on between the murmurs of the Nobles and the organizing by Józiff to make room for us.":
                renpy.show(
                    "almorthy_courtyard_background",
                    tag="event_background",
                    zorder=-100
                )
            if line == "Finally we made it to my shuttle. Józiff remained by my side until I stepped on the boarding ramp, after which he turned to the crowd.":
                renpy.show(
                    "almorthy_courtyard_background",
                    tag="event_background",
                    zorder=-100
                )
            if line == "Back on my flagship, we took a day in orbit to observe the situation.":
                renpy.show(
                    "royal_great_cabin_background",
                    tag="event_background",
                    zorder=-100
                )
            renpy.say(speaker, line)

    def reception_002_run_node(choice_id):
        if choice_id not in reception_002_all_nodes:
            return
        node = reception_002_all_nodes[choice_id]
        reception_002_say(node["body"])
        if any(line.strip() == "(Event Ends Here)" for line in node["body"]):
            store.reception_002_finished = True
            return
        children = [reception_002_all_nodes[item] for item in node["children"]
                    if reception_002_condition(reception_002_all_nodes[item]["meta"])]
        if children:
            options = [(reception_002_choice_text(child), child["id"]) for child in children]
            selected = renpy.display_menu(options)
            store.reception_002_chosen_choices.add(selected)
            reception_002_run_node(selected)

    def reception_002_run_menu(lines):
        first_choice = next((i for i, line in enumerate(lines) if reception_002_choice_header(line)), len(lines))
        prelude = lines[:first_choice]
        if prelude:
            reception_002_say(prelude)
        nodes, roots = reception_002_nodes(lines[first_choice:])
        store.reception_002_all_nodes = nodes
        roots = [nodes[item] for item in roots if reception_002_condition(nodes[item]["meta"])]
        if (store.reception_002_route_condition is not None
                and store.reception_002_route_condition != prologue_befriended):
            roots = []
        if not roots:
            return
        selected = renpy.display_menu([(reception_002_choice_text(node), node["id"]) for node in roots])
        store.reception_002_chosen_choices.add(selected)
        reception_002_run_node(selected)

    def reception_002_run_event():
        lines, events = reception_002_parse_source()
        store.reception_002_finished = False
        store.reception_002_chosen_choices = set()
        store.reception_002_all_nodes = {}
        store.reception_002_route_condition = None
        for kind, content in events:
            if store.reception_002_finished:
                break
            if kind == "menu":
                reception_002_run_menu(content)
            else:
                has_route_marker = any(
                    "if player chose to befriend" in line.lower()
                    or "if player didn’t chose to befriend" in line.lower()
                    or "if player didn't chose to befriend" in line.lower()
                    for line in content
                )
                if (store.reception_002_route_condition is not None
                        and store.reception_002_route_condition != prologue_befriended
                        and not has_route_marker):
                    continue
                reception_002_say(content)

label reception_002:
    scene
    show black as event_background zorder -100
    $ reception_002_run_event()
    hide portrait
    $ current_event = "grand_council_001"
    call screen galaxy_map
    return
