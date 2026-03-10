from database import questions_collection

import math

def update_ability(ability, difficulty, correct):

    probability = 1 / (1 + math.exp(-(ability - difficulty)))

    learning_rate = 0.2

    if correct:
        ability = ability + learning_rate * (1 - probability)
    else:
        ability = ability - learning_rate * probability

    ability = max(0.1, min(1.0, ability))

    return ability


def get_next_question(ability):

    question = questions_collection.find_one(
        {"difficulty": {"$gte": ability}},
        sort=[("difficulty", 1)]
    )

    return question