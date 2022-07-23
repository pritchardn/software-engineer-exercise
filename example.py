import json
from object_analysis import most_common_type, farthest


def main():
    """
    A basic example script showing the farthest and abundant functions on a basic test-case.
    """
    example_input = [
        {"type": "star", "name": "alpha-centaurus", "redshift": 0},
        {"type": "nebula", "name": "crab", "redshift": 0},
        {"type": "galaxy", "name": "sombrero", "redshift": 0},
    ]
    print(f"Example input is:\n{json.dumps(example_input,indent=4)}")
    print(f"Most abundant is {most_common_type(example_input)}")
    print(f"Farthest is {farthest(example_input)}")


if __name__ == "__main__":
    main()