from collections import defaultdict


def aboundant(objects):
    type_counts = defaultdict(int)
    for o in objects:
        type_counts[o['type']] += 1
    return max(type_counts, key=lambda x: type_counts[x])

input = """
[
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
"""

import json
print(aboundant(json.loads(input)))


def farthest(objects):
    return max(objects, key=lambda x: x["redshift"])

print(farthest(json.loads(input)))