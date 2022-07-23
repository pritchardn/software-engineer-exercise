"""
Contains function to calculate basic stats (frequency and max) on a list of astronomical
object dictionaries
"""

from collections import defaultdict


def most_common_type(object_list: list) -> str:
    """
    Calculates the 'type' attribute with the highest frequency in a list of dictionaries
    :param object_list: A list of dictionary objects. All are assumed to have a 'type' key
    :return: The first, most frequent 'type' in the list of objects.
    """
    type_counts = defaultdict(int)
    for entry in object_list:
        if "type" in entry:
            type_counts[entry["type"]] += 1
    return max(type_counts, key=lambda x: type_counts[x])


def farthest(objects: list) -> dict:
    """
    Finds the object with the largest 'redshift' value in a list of objects.
    :param objects: A list of objects. All are assumed to contain a 'redshift' field.
    :return: The first object with the largest redshift value.
    """
    return max(objects, key=lambda x: x["redshift"])
