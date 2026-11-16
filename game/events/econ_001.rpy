image econ_001_patio = Transform(
    "images/Catheljunta_Patio_Garden.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image econ_001_isa_background = Transform(
    "images/Isa_Bellmaré_Background.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image econ_001_bar_background = Transform(
    "images/Furique_Bar.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image econ_001_bedroom_background = Transform(
    "images/Pherip_Bedroom.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)


init python:

    import re

    def econ_001_lines():
        with renpy.file("events/econ_001_source.txt") as source:
            return source.read().decode("utf-8-sig").splitlines()


    def econ_001_choice_path(line):
        match = re.match(r"^Dialog Choice #([0-9.]+)\s*$", line.strip())
        if not match:
            return None
        return tuple(int(part) for part in match.group(1).split("."))


    def econ_001_choice_text(lines, marker):
        speakers = {"Pherip IV:", "Furique Vallitu:", "Narrator:"}
        for line in lines[marker + 1:]:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped in speakers:
                continue
            if stripped.startswith(("Dialog Choice", "Reconvene:", "Repeated:", "(", "+", "-")):
                continue
            return stripped
        return "Continue."


    def econ_001_say_range(lines, start, end, apply_hidden=True, show_furique_portrait=False):
        speaker = n
        speaker_map = {
            "Narrator:": n,
            "Pherip IV:": p,
            "Furique Vallitu:": f,
        }
        in_hidden = False
        for raw in lines[start:end]:
            line = raw.strip()
            if not line:
                continue
            if line in speaker_map:
                speaker = speaker_map[line]
                if line == "Furique Vallitu:" and show_furique_portrait:
                    renpy.show("furique", tag="portrait", zorder=0)
                    show_furique_portrait = False
                continue
            if line.startswith("Our guards and servants escorted us away from the patio"):
                renpy.hide("portrait")
            if line.startswith("Rarely had I ever traversed my own capital’s streets during the night"):
                renpy.scene()
                renpy.show("econ_001_isa_background", tag="event_background", zorder=-100)
            if line.startswith("I realized this floor of apartments had been transformed into a unified space"):
                renpy.scene()
                renpy.show("econ_001_bar_background", tag="event_background", zorder=-100)
            if line.startswith("On that note, Furique finished packing up his things"):
                renpy.hide("portrait")
            if line.startswith("I snapped out of this trance and stood up to leave as well"):
                renpy.scene()
                renpy.show("econ_001_bedroom_background", tag="event_background", zorder=-100)
            if line == "(Hidden)":
                in_hidden = True
                continue
            if line.startswith("(") or line.startswith("Dialog Choice") or line in ("Repeated:", "Reconvene:"):
                continue
            if in_hidden and line[:1] in ("+", "-"):
                if apply_hidden:
                    amount_match = re.match(r"^([+-])(\d+)\s+(.+)$", line)
                    if amount_match:
                        amount = int(amount_match.group(2)) * (1 if amount_match.group(1) == "+" else -1)
                        effect = amount_match.group(3).strip().lower()
                        if effect.startswith("furique relationship"):
                            store.furique_relationship += amount
                        elif effect.startswith("legitimacy") or effect.startswith("imperial majesty"):
                            store.imperial_majesty += amount
                continue
            in_hidden = False
            # Ren'Py applies old-style interpolation to say text; quote any
            # literal percent signs after adding codex hyperlink markup.
            renpy.say(speaker, dialogue_codex_markup(line).replace("%", "%%"))


    def econ_001_play_scope(lines, start, end, parent=(), repeated_menu=False):
        """Play numbered sibling groups, reopening Repeated menus until exhausted."""
        i = start
        while i < end:
            first = None
            for pos in range(i, end):
                path = econ_001_choice_path(lines[pos])
                if path is not None and len(path) == len(parent) + 1 and path[:len(parent)] == parent:
                    first = pos
                    break

            if first is None:
                next_choice = next((pos for pos in range(i, end) if econ_001_choice_path(lines[pos]) is not None), None)
                if next_choice is None:
                    econ_001_say_range(lines, i, end)
                    return
                next_path = econ_001_choice_path(lines[next_choice])
                if parent and next_path[:len(parent)] == parent and len(next_path) > len(parent) + 1:
                    parent = next_path[:-1]
                    continue
                if parent and len(next_path) <= len(parent):
                    parent = ()
                    continue
                if not parent and len(next_path) > 1:
                    parent = next_path[:-1]
                    continue
                ancestor = next((pos for pos in range(next_choice, end)
                                 if econ_001_choice_path(lines[pos]) is not None
                                 and len(econ_001_choice_path(lines[pos])) <= len(parent)), None)
                if ancestor is None:
                    return
                i = ancestor
                parent = ()
                continue

            # A top-level menu ends at the next explicit reconvergence/repeat.
            # Nested sibling options may cross their marked reconvergence lines.
            group_end = end
            candidates = []
            first_path = econ_001_choice_path(lines[first])
            for pos in range(first, end):
                path = econ_001_choice_path(lines[pos])
                if len(parent) == 0 and pos > first and lines[pos].strip() in ("Repeated:", "Reconvene:"):
                    group_end = pos
                    break
                if path is not None:
                    if len(path) == len(parent) + 1 and path[:len(parent)] == parent:
                        candidates.append(pos)
                    elif len(parent) > 0 and len(path) <= len(parent):
                        group_end = pos
                        break
                    elif len(parent) > 0 and path[:len(parent)] != parent and len(path) <= len(parent) + 1:
                        group_end = pos
                        break

            if not candidates:
                next_choice = next((pos for pos in range(i, end) if econ_001_choice_path(lines[pos]) is not None), None)
                if next_choice is None:
                    econ_001_say_range(lines, i, end)
                    return
                inferred = econ_001_choice_path(lines[next_choice])[:-1]
                econ_001_play_scope(lines, i, end, inferred)
                return

            econ_001_say_range(lines, i, first)
            group_repeated = repeated_menu or (first > 0 and lines[first - 1].strip() == "Repeated:")
            if not group_repeated:
                group_repeated = any(lines[pos].strip() == "Repeated:" for pos in range(i, first))
            reconverges_to_previous = any(
                lines[pos].strip().startswith("(Reconvenes at previous Repeated)")
                for pos in range(i, group_end)
            )
            reconverges_to_prime = any(
                lines[pos].strip().startswith("(Reconvene at prime Repeated)")
                for pos in range(i, group_end)
            )
            remaining = list(candidates)
            selected_paths = []
            while remaining:
                menu_items = [(econ_001_choice_text(lines, pos), str(index)) for index, pos in enumerate(remaining)]
                # Keep singleton numbered choices interactive too; do not
                # auto-advance through a numbered choice.
                selected = int(renpy.display_menu(menu_items))
                marker = remaining.pop(selected)
                selected_path = econ_001_choice_path(lines[marker])
                selected_paths.append(selected_path)
                original_index = candidates.index(marker)
                branch_end = candidates[original_index + 1] if original_index + 1 < len(candidates) else group_end
                child_result = econ_001_play_scope(lines, marker + 1, branch_end, selected_path)
                if child_result == "prime":
                    if parent:
                        return "prime"
                    continue
                if not group_repeated:
                    break

            # A child passage with this marker returns to its caller's
            # repeated menu immediately after the chosen alternative.
            if reconverges_to_prime:
                if parent:
                    return "prime"
                continue
            if reconverges_to_previous:
                return

            i = group_end
            next_repeated_menu = i < end and lines[i].strip() == "Repeated:"
            if i < end and lines[i].strip() in ("Repeated:", "Reconvene:"):
                i += 1
            if i < end:
                next_path = next((econ_001_choice_path(lines[pos]) for pos in range(i, end)
                                  if econ_001_choice_path(lines[pos]) is not None), None)
                continuation_parent = selected_paths[-1]
                if next_repeated_menu and next_path is not None:
                    for selected_path in selected_paths:
                        if next_path[:len(selected_path)] == selected_path:
                            continuation_parent = next_path[:-1]
                            break
                econ_001_play_scope(lines, i, end, continuation_parent, next_repeated_menu)
                return


    def econ_001_first(lines, prefix, start=0):
        for index in range(start, len(lines)):
            if lines[index].strip().startswith(prefix):
                return index
        return len(lines)


    def econ_001_decree_title(key):
        return {
            "coin": "Mint Pherip Ascension Coin",
            "palace": "Open the Imperial Palace",
            "gardens": "Establish the Grand Gardens",
            "clemency": "Pass Act of Clemency",
            "holiday": "Declare a Week’s Long Holiday",
            "armada": "Imperial Armada Salute",
        }.get(key, "Mint Pherip Ascension Coin")


    def econ_001_choice_positions(lines, start, end):
        return [i for i in range(start, end) if econ_001_choice_path(lines[i]) is not None]


    def econ_001_find_choice(lines, start, end, phrase):
        for pos in range(start, end):
            if econ_001_choice_path(lines[pos]) is not None and phrase in econ_001_choice_text(lines, pos):
                return pos
        return end


    def econ_001_choose_markers(lines, markers):
        options = [(econ_001_choice_text(lines, pos), str(index)) for index, pos in enumerate(markers)]
        return int(renpy.display_menu(options))


label econ_001:

    $ econ_lines = econ_001_lines()
    scene econ_001_patio

    $ first_opening_choice = econ_001_first(econ_lines, "Dialog Choice #1")
    $ first_condition = econ_001_first(econ_lines, "(If “Mint Pherip Ascension Coin”")
    $ econ_001_say_range(econ_lines, 2, first_opening_choice, show_furique_portrait=True)
    $ opening_markers = econ_001_choice_positions(econ_lines, first_opening_choice, first_condition)
    $ opening_answer = econ_001_choose_markers(econ_lines, opening_markers)
    $ opening_end = opening_markers[opening_answer + 1] if opening_answer + 1 < len(opening_markers) else first_condition
    $ econ_001_say_range(econ_lines, opening_markers[opening_answer] + 1, opening_end)

    # The outline has one mutually exclusive report for each decree.
    $ decree_marker = next((i for i, line in enumerate(econ_lines) if line.strip().startswith("(If “" + econ_001_decree_title(first_decree) + "”")), first_condition)
    $ conditional_markers = [i for i, line in enumerate(econ_lines) if line.strip().startswith("(If “") and i >= first_condition]
    $ selected_conditional_index = conditional_markers.index(decree_marker) if decree_marker in conditional_markers else 0
    $ selected_condition_end = conditional_markers[selected_conditional_index + 1] if selected_conditional_index + 1 < len(conditional_markers) else econ_001_first(econ_lines, "Reconvene:", econ_001_first(econ_lines, "Reconvene:", decree_marker + 1) + 1)
    $ econ_001_say_range(econ_lines, decree_marker + 1, selected_condition_end)
    $ last_condition = conditional_markers[-1]
    $ shared_intro_start = econ_001_first(econ_lines, "Reconvene:", econ_001_first(econ_lines, "Reconvene:", last_condition + 1) + 1)
    $ second_menu_start = econ_001_first(econ_lines, "Dialog Choice #1", shared_intro_start)
    $ econ_001_say_range(econ_lines, shared_intro_start + 1, second_menu_start)
    $ second_menu_end = econ_001_first(econ_lines, "Reconvene:", second_menu_start)
    $ second_menu_markers = econ_001_choice_positions(econ_lines, second_menu_start, second_menu_end)
    $ second_answer = econ_001_choose_markers(econ_lines, second_menu_markers)
    $ second_branch_end = second_menu_markers[second_answer + 1] if second_answer + 1 < len(second_menu_markers) else second_menu_end
    $ econ_001_say_range(econ_lines, second_menu_markers[second_answer] + 1, second_branch_end)
    $ shared_report_start = second_menu_end
    $ main_start = econ_001_first(econ_lines, "Repeated:", shared_report_start)
    $ econ_001_say_range(econ_lines, shared_report_start + 1, main_start)

    # These two questions sit across a source reconvergence boundary. Keep
    # them in one explicit repeated menu so neither can fall through as prose.
    $ happy_hour_marker = max(i for i, line in enumerate(econ_lines) if line.strip() == "Dialog Choice #5")
    $ inflation_marker = econ_001_find_choice(econ_lines, main_start + 1, happy_hour_marker, "Inflation has always been the death of any economic boom")
    $ fiscal_margin_marker = econ_001_find_choice(econ_lines, inflation_marker + 1, happy_hour_marker, "This slim fiscal margin warrants further explanation")
    if inflation_marker == happy_hour_marker or fiscal_margin_marker == happy_hour_marker:
        $ renpy.error("econ_001 is missing a required economy discussion choice.")
    $ econ_001_play_scope(econ_lines, main_start + 1, inflation_marker, (), True)
    $ discussion_end = econ_001_first(econ_lines, "Repeated:", fiscal_margin_marker + 1)
    $ discussion_remaining = [inflation_marker, fiscal_margin_marker]
    while discussion_remaining:
        $ discussion_items = [(econ_001_choice_text(econ_lines, pos), str(index)) for index, pos in enumerate(discussion_remaining)]
        $ discussion_selected = int(renpy.display_menu(discussion_items))
        $ discussion_marker = discussion_remaining.pop(discussion_selected)
        if discussion_marker == inflation_marker:
            $ discussion_branch_end = fiscal_margin_marker
        else:
            $ discussion_branch_end = discussion_end
        $ econ_001_say_range(econ_lines, discussion_marker + 1, discussion_branch_end)
    # The fiscal report has four independent questions. They are separated
    # by nested repeated submenus in the outline, so collect the four parent
    # prompts explicitly and reopen the parent menu after each response.
    $ economy_question_markers = [
        econ_001_find_choice(econ_lines, discussion_end + 1, happy_hour_marker, "I see. And are taxes low"),
        econ_001_find_choice(econ_lines, discussion_end + 1, happy_hour_marker, "workforce is less than healthy"),
        econ_001_find_choice(econ_lines, discussion_end + 1, happy_hour_marker, "substantial outstanding loan which exists with Fespia"),
        econ_001_find_choice(econ_lines, discussion_end + 1, happy_hour_marker, "why Autarky isn’t a path worth pursuing"),
    ]
    if any(pos == happy_hour_marker for pos in economy_question_markers):
        $ renpy.error("econ_001 is missing a required economy report question.")
    $ economy_remaining = list(economy_question_markers)
    while economy_remaining:
        $ economy_items = [(econ_001_choice_text(econ_lines, pos), str(index)) for index, pos in enumerate(economy_remaining)]
        $ economy_selected = int(renpy.display_menu(economy_items))
        $ economy_marker = economy_remaining.pop(economy_selected)
        $ economy_ordered = sorted(economy_question_markers)
        $ economy_marker_index = economy_ordered.index(economy_marker)
        $ economy_branch_end = economy_ordered[economy_marker_index + 1] if economy_marker_index + 1 < len(economy_ordered) else happy_hour_marker
        $ econ_001_play_scope(econ_lines, economy_marker + 1, economy_branch_end, econ_001_choice_path(econ_lines[economy_marker]), True)
    $ happy_hour_next = econ_001_first(econ_lines, "Dialog Choice #1", happy_hour_marker + 1)
    # Dialog Choice #5 is a singleton continuation, but it still needs an
    # explicit player confirmation before its response and the happy-hour scene.
    $ happy_hour_answer = econ_001_choose_markers(econ_lines, [happy_hour_marker])
    $ econ_001_say_range(econ_lines, happy_hour_marker + 1, happy_hour_next)

    $ final_root_end = econ_001_first(econ_lines, "Reconvene:", happy_hour_next)
    $ final_root_markers = [i for i in econ_001_choice_positions(econ_lines, happy_hour_next, final_root_end) if len(econ_001_choice_path(econ_lines[i])) == 1]
    $ final_root_answer = econ_001_choose_markers(econ_lines, final_root_markers)
    $ final_root_marker = final_root_markers[final_root_answer]
    $ final_root_path = econ_001_choice_path(econ_lines[final_root_marker])
    $ going_out = False

    if final_root_path == (1,):
        $ child_end = final_root_markers[1] if len(final_root_markers) > 1 else final_root_end
        $ child_markers = econ_001_choice_positions(econ_lines, final_root_marker + 1, child_end)
        $ econ_001_say_range(econ_lines, final_root_marker + 1, child_markers[0])
        $ child_answer = econ_001_choose_markers(econ_lines, child_markers)
        $ child_marker = child_markers[child_answer]
        if econ_001_choice_path(econ_lines[child_marker]) == (1, 1):
            $ going_out = True
        $ child_branch_end = child_markers[child_answer + 1] if child_answer + 1 < len(child_markers) else child_end
        $ econ_001_say_range(econ_lines, child_marker + 1, child_branch_end)
    else:
        $ going_out = final_root_path in ((2,), (3,))
        $ final_branch_end = final_root_markers[final_root_answer + 1] if final_root_answer + 1 < len(final_root_markers) else final_root_end
        $ econ_001_say_range(econ_lines, final_root_marker + 1, final_branch_end)

    $ investment_reconvene = econ_001_first(econ_lines, "Reconvene:", final_root_end)
    $ investment_end = econ_001_first(econ_lines, "(If Dialog Choice #1.1:", investment_reconvene + 1)
    $ econ_001_say_range(econ_lines, investment_reconvene + 1, investment_end)

    if going_out:
        $ bar_start = econ_001_first(econ_lines, "(If Dialog Choice #1.1:", investment_end)
        $ palace_start = econ_001_first(econ_lines, "(If Dialog Choice #1.2:", bar_start)
        $ econ_001_say_range(econ_lines, bar_start + 1, palace_start)
    else:
        $ palace_start = econ_001_first(econ_lines, "(If Dialog Choice #1.2:", investment_end)
        $ econ_001_say_range(econ_lines, palace_start + 1, len(econ_lines))

    hide portrait
    $ current_event = "investment_opportunity_001"
    $ active_event = True
    call screen galaxy_map
    return
