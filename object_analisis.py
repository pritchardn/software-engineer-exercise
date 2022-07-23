from collections import defaultdict


def aboundant(objects):
    expected_types = {'star', 'galaxy', 'nebula', 'supernova', 'frb'}
    expected_plurals = {'star': 'stars', 'galaxy': 'galaxies', 'nebula': 'nebulae', 'supernova': 'supernovae', 'frb': 'frbs'}
    type_counts = defaultdict(int)
    for o in objects:
        type_counts[o['type']] += 1
    abundant_type = max(type_counts, key=lambda x: type_counts[x])
    if abundant_type in expected_types:
        return expected_plurals[abundant_type]
    else:
        raise ValueError("Object list contains a large number of unidentified objects")


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