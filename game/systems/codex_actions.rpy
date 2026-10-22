init python:

    def codex_smooth_scroll(direction):
        """Accumulate wheel steps, then ease the Codex viewport to the target."""

        viewport = renpy.get_widget(None, "codex_biography")
        if viewport is None:
            return

        adjustment = viewport.yadjustment
        target = renpy.get_screen_variable("codex_scroll_target", screen="codex_popup")
        scroll_range = adjustment.range
        if scroll_range is None:
            return

        # If the viewport is idle, or the player has dragged it, resume from
        # its actual position. During an animation keep the pending target so
        # rapid wheel inputs add to it instead of replacing unfinished travel.
        if target is None or adjustment.animation_target is None:
            target = adjustment.value

        previous_target = target
        increment = adjustment.step or 1
        target = max(0, min(scroll_range, target + direction * increment))
        if target == previous_target and adjustment.animation_target == target:
            return

        renpy.set_screen_variable("codex_scroll_target", target, screen="codex_popup")

        # Starting from the current animated position while targeting the
        # accumulated destination preserves every wheel increment.
        adjustment.animate(target - adjustment.value, 0.14, _warper.ease)

    def codex_link(key):

        global codex_current

        renpy.hide_screen("codex_hover_tooltip")

        codex_current = key

        renpy.show_screen("codex_popup")
        renpy.restart_interaction()

    def codex_hide_hover_tooltip():
        if renpy.get_screen("codex_hover_tooltip") is not None:
            renpy.hide_screen("codex_hover_tooltip")
            renpy.restart_interaction()


    def codex_hyperlink(link):

        if link.startswith("codex:"):

            codex_link(link.split(":")[1])

            return

        return

    # Handle dialogue and speaker-name codex links.
    config.hyperlink_handlers["codex"] = codex_link
    config.hyperlink_handlers["codex_name"] = codex_link

    def codex_hyperlink_styler(target):
        # Nameplate links use the existing speaker-name style, preserving
        # their normal color, size, and emphasis.
        if target.startswith("codex_name:"):
            return style.say_label

        return style.hyperlink_text

    def codex_hyperlink_focus(target):
        """Show codex summaries while a codex hyperlink has focus."""

        if target is None:
            codex_hide_hover_tooltip()
            if _codex_default_hyperlink_focus is not None:
                return _codex_default_hyperlink_focus(target)
            return

        protocol, separator, key = target.partition(":")
        if separator and protocol in ("codex", "codex_name") and key in CODEX:
            entry = CODEX[key]
            # Keep the tooltip above the speaker nameplate so it never covers
            # the dialogue text. Anchor it to the namebox rather than the link
            # position, which may be anywhere inside the dialogue sentence.
            panel_width = 440
            panel_height = 115
            x = gui.name_xpos
            y = config.screen_height - gui.textbox_height + gui.name_ypos - panel_height - 12
            x = max(0, min(x, config.screen_width - panel_width))
            y = max(0, min(y, config.screen_height - panel_height))

            renpy.show_screen(
                "codex_hover_tooltip",
                entry.get("hover_title") or entry.get("name", ""),
                entry.get("hover_description") or entry.get("title", ""),
                x,
                y,
            )
            renpy.restart_interaction()
            return

        codex_hide_hover_tooltip()
        if _codex_default_hyperlink_focus is not None:
            return _codex_default_hyperlink_focus(target)

    def codex_hyperlink_callback(target):
        if ":" not in target:
            target = config.hyperlink_protocol + ":" + target

        protocol, _, value = target.partition(":")

        if protocol in config.hyperlink_handlers:
            return config.hyperlink_handlers[protocol](value)

        return renpy.open_url(target)

    # This init runs after Ren'Py's compatibility setup copies the config
    # callbacks into style.default, so update the text style directly.
    _codex_default_hyperlink_focus = style.default.hyperlink_functions[2]
    style.default.hyperlink_functions = (
        codex_hyperlink_styler,
        codex_hyperlink_callback,
        codex_hyperlink_focus,
        style.default.hyperlink_functions[3],
    )
