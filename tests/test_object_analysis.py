from unittest import TestCase

from object_analisis import most_common_type, farthest


class TestFarthest(TestCase):
    def test_farthest(self):
        """
        Asserts that farthest returns the object with the single maximum redshift value
        """
        maximum_redshift_object = {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 100
        }
        test_data = [
            maximum_redshift_object,
            {
                "type": "nebula",
                "name": "crab",
                "redshift": 5
            },
            {
                "type": "galaxy",
                "name": "sombrero",
                "redshift": 0
            }
        ]
        calculated_output = farthest(test_data)
        self.assertEqual(maximum_redshift_object, calculated_output)


class TestMostCommonType(TestCase):
    def test_max_frbs(self):
        """
        Asserts that a list of objects mostly containing frbs will return 'frbs'
        """
        test_data = [
            {
                "type": "star",
            },
            {
                "type": "frb",
            },
            {
                "type": "frb",
            }
        ]
        output_calculated = most_common_type(test_data)
        self.assertEqual("frb", output_calculated)

    def test_max_nebulae(self):
        """
        Asserts that a list of objects mostly containing nebulae will return 'nebulae
        """
        test_data = [
            {
                "type": "nebula",
            },
            {
                "type": "nebula",
            },
            {
                "type": "frb",
            }
        ]
        output_calculated = most_common_type(test_data)
        self.assertEqual("nebula", output_calculated)
