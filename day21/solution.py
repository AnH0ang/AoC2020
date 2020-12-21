import re

allergens: list[str] = []
allergens2possible_ingredients: dict[str, set[str]] = {}
allergens2ingredient: dict[str, str] = {}
all_ingredients: set[str] = set()
recepies = []

def parse_line(line: str) -> None:
    global all_ingredients
    start, end = line.split(" (")
    ingrendients = start.split(" ")
    allergens = end[9:-1].split(", ")
    for a in allergens:
        if a not in allergens2possible_ingredients:
            allergens2possible_ingredients[a] = set(ingrendients)
        else:
            allergens2possible_ingredients[a] &= set(ingrendients)

    all_ingredients |= set(ingrendients)
    recepies.append(set(ingrendients))

def main() -> None:
    for line in open("input.txt", "r").read().split("\n"):
        parse_line(line)


    # solution 1
    silver = 0
    candidates = all_ingredients - set.union(*allergens2possible_ingredients.values()) 
    for r in recepies:
        silver += len(candidates & r)
    print(silver)

    # solution 2
    while allergens2possible_ingredients:
        min_candidate: str = min(allergens2possible_ingredients, key=lambda k: len(allergens2possible_ingredients[k]))
        assert len(allergens2possible_ingredients[min_candidate]) == 1
        min_ingredient = allergens2possible_ingredients[min_candidate].pop()
        allergens2ingredient[min_candidate] = min_ingredient
        for v in allergens2possible_ingredients.values():
            v.discard(min_ingredient)
        del allergens2possible_ingredients[min_candidate]
    print(",".join([allergens2ingredient[k] for k in sorted(allergens2ingredient.keys())]))

if __name__ == "__main__":
    main()