"""
Tests the functions in object_analysis.py for correctness.
"""

from unittest import TestCase

from object_analysis import most_common_type, most_redshifted
from known_types import KNOWN_TYPES_PLURALS


class TestMostCommonType(TestCase):
    """
    Tests the abundant function for correctness
    """

    def _test_max_object(self, target: str, expected: str):
        """
        Constructs and tests that a list of objects with a single majority will return its expected
        plural.
        """
        test_data = [{"type": target}] * 2 + [{"type": "other"}]
        self.assertEqual(expected, most_common_type(test_data))

    def test_all_types(self):
        """
        Asserts the most frequent object is found where each known type is the most frequent
        """
        for object_type, plural in KNOWN_TYPES_PLURALS.items():
            self._test_max_object(object_type, plural)

    def test_equal_frequency(self):
        """
        Asserts that in the case of a tie, the first object type encountered is returned
        """
        test_data = [{"type": object_type} for object_type in KNOWN_TYPES_PLURALS]
        self.assertEqual(KNOWN_TYPES_PLURALS[test_data[0]["type"]], most_common_type(test_data))

    def test_non_valid_type(self):
        """
        Asserts that a list of objects, where one does not contain a valid 'type', is ignored.
        """
        test_data = [{"type": "ufo"}, {"type": "galaxy"}]
        self.assertEqual(KNOWN_TYPES_PLURALS["galaxy"], most_common_type(test_data))

    def test_non_type_objects(self):
        """
        Asserts that having an object with no type is gracefully skipped
        """
        test_data = [
            {"type": "frb"},
            {"other_field": "baseball"},
            {"type": "frb"},
        ]
        self.assertEqual(KNOWN_TYPES_PLURALS[test_data[0]["type"]], most_common_type(test_data))

    def test_empty(self):
        """
        Asserts that an empty list of objects returns ""
        """
        test_data = []
        self.assertEqual("", most_common_type(test_data))

    def test_all_non_type_objects(self):
        """
        Asserts that an object list where none of them have 'type' fields raises an exception
        """
        test_data = [
            {"other_field": "basketball"},
            {"other_field": "baseball"},
            {"other_field": "football"},
        ]
        self.assertEqual("", most_common_type(test_data))


class TestMaxRedShifted(TestCase):
    """
    Tests the farthest function for correctness.
    """

    def test_basic_case(self):
        """
        Asserts that farthest returns the object with the single maximum redshift value
        """
        maximum_redshift_object = {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 100,
        }
        test_data = [
            maximum_redshift_object,
            {"type": "nebula", "name": "crab", "redshift": 5},
            {"type": "galaxy", "name": "sombrero", "redshift": 0},
        ]
        self.assertEqual(maximum_redshift_object, most_redshifted(test_data))

    def test_equal(self):
        """
        Tests that in the case of a tie, the first object in the list is returned.
        """
        test_data = [
            {"type": "nebula", "name": "crab", "redshift": 0},
            {"type": "galaxy", "name": "sombrero", "redshift": 0},
        ]
        self.assertEqual(test_data[0], most_redshifted(test_data))

    def test_some_non_redshift_objects(self):
        """
        Asserts that a few objects containing no redshift field throws an error.
        Handling a default 'smallest' is unreasonable
        since redshift can be positive or negative (blue-shifted)
        """
        test_data = [
            {"type": "nebula", "name": "crab"},
            {"type": "galaxy", "name": "sombrero", "redshift": 0},
        ]
        self.assertEqual(test_data[1], most_redshifted(test_data))

    def test_all_non_redshift(self):
        """
        Asserts that when provided a list of objects, none of which have a redshift value,
        None is returned
        """
        test_data = [
            {"type": "nebula", "name": "crab"},
            {"type": "galaxy", "name": "sombrero"},
        ]
        self.assertEqual(None, most_redshifted(test_data))

    def test_empty(self):
        """
        Asserts that when given an empty list a None type is returned
        """
        test_data = []
        self.assertEqual(None, most_redshifted(test_data))
