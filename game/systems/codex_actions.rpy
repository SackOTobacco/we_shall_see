init python:

    def codex_link(key):

        global codex_current

        codex_current = key

        renpy.show_screen("codex_popup")
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

    def codex_hyperlink_callback(target):
        if ":" not in target:
            target = config.hyperlink_protocol + ":" + target

        protocol, _, value = target.partition(":")

        if protocol in config.hyperlink_handlers:
            return config.hyperlink_handlers[protocol](value)

        return renpy.open_url(target)

    config.hyperlink_styler = codex_hyperlink_styler
    config.hyperlink_callback = codex_hyperlink_callback
