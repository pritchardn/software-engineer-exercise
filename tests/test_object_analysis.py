"""
Tests the functions in object_analysis.py for correctness.
"""

from unittest import TestCase

from object_analysis import most_common_type, farthest


class TestMostCommonType(TestCase):
    """
    Tests the abundant function for correctness
    """

    def test_max_frbs(self):
        """
        Asserts that a list of objects mostly containing frbs will return 'frbs'
        """
        test_data = [
            {"type": "star"},
            {"type": "frb"},
            {"type": "frb"},
        ]
        output_calculated = most_common_type(test_data)
        self.assertEqual("frb", output_calculated)

    def test_max_nebulae(self):
        """
        Asserts that a list of objects mostly containing nebulae will return 'nebulae
        """
        test_data = [
            {"type": "nebula"},
            {"type": "nebula"},
            {"type": "frb"},
        ]
        output_calculated = most_common_type(test_data)
        self.assertEqual("nebula", output_calculated)

    def test_equal_frequency(self):
        """
        Asserts that in the case of a tie, the first object type encountered is returned
        """
        test_data = [
            {"type": "nebula"},
            {"type": "star"},
            {"type": "frb"},
        ]
        output_calculated = most_common_type(test_data)
        self.assertEqual("nebula", output_calculated)

    def test_non_type_objects(self):
        """
        Asserts that having an object with no type is gracefully skipped
        """
        test_data = [
            {"type": "frb"},
            {"other_field": "baseball"},
            {"type": "frb"},
        ]
        output_calculated = most_common_type(test_data)
        self.assertEqual("frb", output_calculated)

    def test_all_non_type_objects(self):
        """
        Asserts that an object list where none of them have 'type' fields raises an exception
        """
        test_data = [
            {"other_field": "basketball"},
            {"other_field": "baseball"},
            {"other_field": "football"},
        ]
        self.assertRaises(ValueError, most_common_type, test_data)


class TestFarthest(TestCase):
    """
    Tests the farthest function for correctness.
    """

    def test_farthest(self):
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
        calculated_output = farthest(test_data)
        self.assertEqual(maximum_redshift_object, calculated_output)

    def test_farthest_equal(self):
        """
        Tests that in the case of a tie, the first object in the list is returned.
        """
        test_data = [
            {"type": "nebula", "name": "crab", "redshift": 0},
            {"type": "galaxy", "name": "sombrero", "redshift": 0},
        ]
        calculated_output = farthest(test_data)
        self.assertEqual(test_data[0], calculated_output)

