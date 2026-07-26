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

    # Handle {a=codex:sicill}...{/a} links from dialogue text.
    config.hyperlink_handlers["codex"] = codex_link
