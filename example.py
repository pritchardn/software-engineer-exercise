"""
A simple example of the functions contained in object_analysis.
"""
import json
from object_analysis import most_common_type, most_redshifted


def main():
    """
    A basic example script showing the farthest and abundant functions on a basic test-case.
    """
    example_input = [
        {"type": "star", "name": "alpha-centaurus", "redshift": 0},
        {"type": "nebula", "name": "crab", "redshift": 0},
        {"type": "galaxy", "name": "sombrero", "redshift": 10},
    ]
    print(f"Example input is:\n{json.dumps(example_input,indent=4)}")
    print(f"Most abundant is {most_common_type(example_input)}")
    print(f"Farthest is {most_redshifted(example_input)}")


if __name__ == "__main__":
    main()
