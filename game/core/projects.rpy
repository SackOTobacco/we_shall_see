init python:

    def modifier_total(modifiers):

        return sum(
            value
            for name, value
            in modifiers
        )


    def add_project(
        name,
        locations,
        turns_remaining,
        income_bonus,
        popularity_bonus=0
    ):

        active_projects.append({

            "name": name,

            "locations": locations,

            "turns_remaining": turns_remaining,

            "income_bonus": income_bonus,

            "popularity_bonus": popularity_bonus
        })


    def process_turn():

        completed = []

        for project in active_projects:

            project["turns_remaining"] -= 1

            if project["turns_remaining"] <= 0:

                completed.append(project)

        for project in completed:

            active_projects.remove(project)

            store.treasury_modifiers.append(
                (
                    project["name"],
                    project["income_bonus"]
                )
            )

            if project["popularity_bonus"] != 0:

                store.popularity_modifiers.append(
                    (
                        project["name"],
                        project["popularity_bonus"]
                    )
                )

            renpy.notify(
                "{} completed!".format(
                    project["name"]
                )
            )

        store.treasury += modifier_total(
            store.treasury_modifiers
        )

        store.imperial_majesty += modifier_total(
            store.legitimacy_modifiers
        )

        store.popularity += modifier_total(
            store.popularity_modifiers
        )

        store.military += modifier_total(
            store.military_modifiers
        )
