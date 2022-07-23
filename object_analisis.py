def aboundant(objects):
    sum_stars = 0
    sum_galaxies = 0
    sum_supernovae = 0
    sum_frbs = 0
    sum_nebulae = 0
    for o in objects:
        if o['type'] == 'star':
            sum_stars += 1
    for o in objects:
        if o['type'] == 'galaxy':
            sum_galaxies += 1
    for o in objects:
        if o['type'] == 'supernovae':
            sum_supernovae += 1
    for o in objects:
        if o['type'] == 'frb':
            sum_frbs += 1
    for o in objects:
        if o['type'] == 'nebula':
            sum_nebulae += 1
    if sum_stars >= sum_galaxies and sum_stars >= sum_supernovae and sum_stars >= sum_frbs and sum_stars >= sum_nebulae:
        return 'stars'
    if sum_galaxies >= sum_stars and sum_galaxies >= sum_supernovae and sum_galaxies >= sum_frbs and sum_galaxies >= sum_nebulae:
        return 'galaxies'
    if sum_supernovae >= sum_stars and sum_supernovae >= sum_galaxies and sum_supernovae >= sum_frbs and sum_supernovae >= sum_nebulae:
        return 'supernovae'
    if sum_frbs >= sum_stars and sum_frbs >= sum_galaxies and sum_frbs >= sum_supernovae and sum_frbs >= sum_nebulae:
        return 'frbs'
    if sum_nebulae >= sum_stars and sum_nebulae >= sum_galaxies and sum_nebulae >= sum_supernovae and sum_nebulae >= sum_frbs:
        return 'nebulae'

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
    highest_redshift = None
    for o in objects:
        if highest_redshift is None or o["redshift"] > highest_redshift:
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o

print(farthest(json.loads(input)))