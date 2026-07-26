init python:

    def assign_turn_event():

        if current_turn == 1:
            store.current_event = "grand_council_001"

        elif current_turn == 2:
            store.current_event = "foreign_affairs_001"

        elif current_turn == 3:
            store.current_event = "military_reform_001"