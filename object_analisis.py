import json
from collections import defaultdict


def most_common_type(objects: list) -> str:
    type_counts = defaultdict(int)
    for o in objects:
        type_counts[o['type']] += 1
    return max(type_counts, key=lambda x: type_counts[x])


def farthest(objects: list) -> dict:
    return max(objects, key=lambda x: x["redshift"])


def main():
    example_input = [
        {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 0
        },
        {
            "type": "nebula",
            "name": "crab",
            "redshift": 0
        },
        {
            "type": "galaxy",
            "name": "sombrero",
            "redshift": 0
        }
    ]
    print(f"Example input is:\n{json.dumps(example_input,indent=4)}")
    print(f"Most abundant is {most_common_type(example_input)}")
    print(f"Farthest is {farthest(example_input)}")


if __name__ == "__main__":
    main()

