characters = [
    {"name": "Luke Skywalker", "episodes": [4, 5, 6, 7, 8, 9]},
    {"name": "Darth Vader", "episodes": [3, 4, 5, 6]},
    {"name": "Yoda", "episodes": [1, 2, 3, 5, 6, 8]},
    {"name": "Boba Fett", "episodes": [2, 5, 6]},
    {"name": "C3PO", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "Leia", "episodes": [3, 4, 5, 6, 7, 8, 9]},
    {"name": "Rey", "episodes": [7, 8, 9]},
    {"name": "Kylo Ren", "episodes": [7, 8, 9]},
    {"name": "Chewbacca", "episodes": [3, 4, 5, 6, 7, 8, 9]},
    {"name": "Han Solo", "episodes": [4, 5, 6, 7, 9]},
    {"name": "R2D2", "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"name": "BB8", "episodes": [7, 8, 9]},
]

connections = []
for index, character in enumerate(characters):
    for other_character in characters[index + 1:]:
        shared_episodes = set(character["episodes"]) & set(other_character["episodes"])
        if shared_episodes:
            connections.append(
                {
                    "origin": character["name"],
                    "destination": other_character["name"],
                    "weight": len(shared_episodes),
                }
            )
