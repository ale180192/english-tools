import json
import random

def get_random_verb(verbs: list) -> str:
    num = random.randrange(0, len(verbs))
    return verbs.pop(num)


if __name__ == "__main__":
    verbs_path = "assets/verbs.json"
    with open(verbs_path) as json_file:
        verbs = json.load(json_file)

    verb = get_random_verb(verbs["irregulars"])
    print(verb["name"])
