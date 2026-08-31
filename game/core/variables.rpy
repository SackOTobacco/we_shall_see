default treasury = 10
default popularity = 5
default imperial_majesty = 5
default military = 50

# Relationship variables

default quixote_relationship = 0
default furique_relationship = 0
default torrez_relationship = 0
default aurgenbia_relationship = 0
default gaucho_relationship = 0
default solene_relationship = 0
default isine_relationship = 0
default robertz_relationship = 0
default charristo_relationship = 0
default mate_relationship = 0
default calitz_relationship = 0
default sicill_relationship = 0

# Political variables

default council_approval = 0
default noble_approval = 0
default burgher_approval = 0
default military_approval = 0

# Foreign policy

default colonial_relations = 0
default galactic_reputation = 0

# Economy

default tourism = 0
default domestic_production = 0

# Story flags

default colony_preference = None

default current_turn = 1
default max_turns = 12

default active_projects = []

default project_income_bonus = 0

default treasury_modifiers = []

default legitimacy_modifiers = []

default popularity_modifiers = []

default military_modifiers = []

init python:

    def modifier_total(modifiers):

        return sum(value for name, value in modifiers)

default events_required_this_turn = 1
default events_completed_this_turn = 0

default map_x = -8400
default map_y = -4800
default map_zoom = 5.5

default active_event = True
default current_event = "reception_001"

