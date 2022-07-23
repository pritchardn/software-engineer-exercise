"""
Contains function to calculate basic stats (frequency and max) on a list of astronomical
object dictionaries
"""

from collections import defaultdict
from known_types import KNOWN_TYPES_PLURALS


def most_common_type(object_list: list) -> str:
    """
    Calculates the 'type' attribute with the highest frequency in a list of dictionaries
    :param object_list: A list of dictionary objects. All are assumed to have a 'type' key
    :return: The first, most frequent 'type' in the list of objects.
    Returns "" if no valid objects are present
    """
    type_counts = defaultdict(int)
    for entry in object_list:
        if "type" in entry and entry.get("type", "") in KNOWN_TYPES_PLURALS:
            type_counts[entry["type"]] += 1
    if len(type_counts) == 0:
        return ""
    most_frequent_type = max(type_counts, key=lambda x: type_counts[x])
    return KNOWN_TYPES_PLURALS[most_frequent_type]


def most_redshifted(object_list: list) -> dict:
    """
    Finds the object with the largest 'redshift' value in a list of objects.
    :param object_list: A list of objects. All are assumed to contain a 'redshift' field.
    :return: The first object with the largest redshift value.
    """
    furthest_object = None
    for entry in object_list:
        if "redshift" in entry and (
            furthest_object is None
            or entry["redshift"] > furthest_object.get("redshift", None)
        ):
            furthest_object = entry
    return furthest_object
