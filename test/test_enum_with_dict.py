import unittest
from enum_with_dict import EnumWithDict

class TestEnumWithDict(unittest.TestCase):

    def test_integer_values(self):
        class Color(EnumWithDict):
            RED = 1
            GREEN = 2
            BLUE = 3
        
        expected = {'RED': 1, 'GREEN': 2, 'BLUE': 3}
        self.assertEqual(Color.to_dict(), expected)
        self.assertEqual(Color.get_initial(), 1)
        self.assertEqual(Color.get('RED'), 1)
        self.assertEqual(Color.get('PURPLE', default=0), 0)
        self.assertEqual(Color.get('PURPLE'), 1)  # Using initial value as default

    def test_string_values(self):
        class Mood(EnumWithDict):
            HAPPY = "happy"
            SAD = "sad"
            ANGRY = "angry"
        
        expected = {'HAPPY': "happy", 'SAD': "sad", 'ANGRY': "angry"}
        self.assertEqual(Mood.to_dict(), expected)
        self.assertEqual(Mood.get_initial(), "happy")
        self.assertEqual(Mood.get('HAPPY'), "happy")
        self.assertEqual(Mood.get('CONFUSED', default="unknown"), "unknown")
        self.assertEqual(Mood.get('CONFUSED'), "happy")  # Using initial value as default

    def test_tuple_values(self):
        class Coordinates(EnumWithDict):
            POINT_A = (1, 2)
            POINT_B = (3, 4)
        
        expected = {'POINT_A': (1, 2), 'POINT_B': (3, 4)}
        self.assertEqual(Coordinates.to_dict(), expected)
        self.assertEqual(Coordinates.get_initial(), (1, 2))
        self.assertEqual(Coordinates.get('POINT_A'), (1, 2))
        self.assertEqual(Coordinates.get('POINT_C', default=(0, 0)), (0, 0))
        self.assertEqual(Coordinates.get('POINT_C'), (1, 2))  # Using initial value as default

    def test_function_values(self):        
        class Actions(EnumWithDict):
            ACTION_A = EnumWithDict
            ACTION_B = len
        
        self.assertTrue(callable(Actions.to_dict()['ACTION_A']))
        self.assertTrue(callable(Actions.to_dict()['ACTION_B']))
        self.assertEqual(Actions.get_initial(), EnumWithDict)
        self.assertEqual(Actions.get('ACTION_A'), EnumWithDict)
        self.assertTrue(callable(Actions.get('ACTION_C', default=str)))
        self.assertEqual(Actions.get('ACTION_C'), EnumWithDict)  # Using initial value as default

    def test_validate_mapping_incomplete(self):
        """Test validation fails with an incomplete mapping."""
        class IncompleteEnum(EnumWithDict):
            A = 1
            B = 2
            C = 3  # C is not included in the mapping, should trigger validation failure

        incomplete_mapping = {
            'A': 1,
            'B': 2,
        }

        with self.assertRaises(ValueError):
            IncompleteEnum.validate_mapping(incomplete_mapping)

    def test_validate_mapping_extended(self):
        """Test validation fails with an extended mapping."""

        class ExtendEnum(EnumWithDict):
            A = 1
            B = 2
            C = 3  # C is not included in the mapping, should trigger validation failure

        dict_mapping = ExtendEnum.to_dict()

        # Add a new value that doesn't correspond to any enum member
        dict_mapping['UNDEFINED'] = 'undefined'

        # Now, validation should fail because of the extra key
        with self.assertRaises(ValueError) as context:
            ExtendEnum.validate_mapping(dict_mapping)

    def test_validate_self_mapping(self):
        """Test validation succeeds against self."""

        class Mixed(EnumWithDict):
            NUMBER = 1,
            ZERO = 0,
            STRING = "string",
            TRUE = True,
            FALSE = False,
            FUNCTION = len

        # Convert enum to dict and validate
        dict_mapping = Mixed.to_dict()
        self.assertTrue(Mixed.validate_mapping(dict_mapping))

if __name__ == '__main__':
    unittest.main()
