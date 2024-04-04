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

    def test_validate_mapping_keys_incomplete(self):
        """Test validation fails with an incomplete mapping."""
        class IncompleteEnum(EnumWithDict):
            A = 1
            B = 2
            C = 3  # C is not included in the mapping, should trigger validation failure

        incomplete_mapping = {
            'A': 1,
            'B': 2,
        }

        with self.assertRaises(KeyError):
            IncompleteEnum.validate_mapping_keys(incomplete_mapping)

    def test_validate_mapping_keys_extended(self):
        """Test validation fails with an extended mapping."""

        class ExtendEnum(EnumWithDict):
            A = 1
            B = 2
            C = 3  # C is not included in the mapping, should trigger validation failure

        dict_mapping = ExtendEnum.to_dict()

        # Add a new value that doesn't correspond to any enum member
        dict_mapping['UNDEFINED'] = 'undefined'

        # Now, validation should fail because of the extra key
        with self.assertRaises(KeyError) as context:
            ExtendEnum.validate_mapping_keys(dict_mapping)

    def test_validate_self_mapping(self):
        """Test validation succeeds against self."""

        class Mixed(EnumWithDict):
            NUMBER = 1
            ZERO = 0
            STRING = "string"
            TRUE = True
            FALSE = False
            FUNCTION = len
            NONE = None

        # Convert enum to dict and validate
        dict_mapping = Mixed.to_dict()
        self.assertTrue(Mixed.validate_mapping_keys(dict_mapping))

    def test_map(self):
        """Test mapping."""
        class TestEnum(EnumWithDict):
            VALUE_1 = 1
            VALUE_2 = 2
            VALUE_3 = 3
        
        # Define the key mapping
        key_mapping = {
            TestEnum.VALUE_1: "some_new_value",
            TestEnum.VALUE_2: "another_new_value",
            TestEnum.VALUE_3: "a new value"
        }

        self.assertEqual(TestEnum.map(key_mapping), {
            TestEnum.VALUE_1.name: "some_new_value",
            TestEnum.VALUE_2.name: "another_new_value",
            TestEnum.VALUE_3.name: "a new value"
        })

    def test_map_invalid_key(self):
        """Test mapping enum members to values with invalid keys."""
        class TestEnum(EnumWithDict):
            VALUE_1 = 1
            VALUE_2 = 2
            VALUE_3 = 3
        
        # Define the key mapping
        key_mapping = {
            TestEnum.VALUE_1: "some_new_value",
            TestEnum.VALUE_2: "another_new_value",
            TestEnum.VALUE_3.value: "a new value"
        }

        # Perform the mapping and validate
        with self.assertRaises(KeyError):
            TestEnum.map(key_mapping)

    def test_incomplete_map(self):
        """Test incomplete mapping enum members to values."""
        class TestEnum(EnumWithDict):
            VALUE_1 = 1
            VALUE_2 = 2
            VALUE_3 = 3
        
        # Define the key mapping
        key_mapping = {
            TestEnum.VALUE_1: "some_new_value",
            TestEnum.VALUE_2: "another_new_value",
        }

        # Perform the mapping and validate
        with self.assertRaises(KeyError):
            TestEnum.map(key_mapping)

    def test_keys_retrieval(self):
        class TestEnum(EnumWithDict):
            VALUE_1 = 1
            VALUE_2 = 2
            VALUE_3 = 3

        self.assertEqual(TestEnum.keys(), ['VALUE_1', 'VALUE_2', 'VALUE_3'])

        self.assertNotEqual(TestEnum.keys(as_list = False), ['VALUE_1', 'VALUE_2', 'VALUE_3'])
        self.assertEqual(list(TestEnum.keys(as_list = False)), ['VALUE_1', 'VALUE_2', 'VALUE_3'])

    def test_values_retrieval(self):
        class TestEnum(EnumWithDict):
            VALUE_1 = 1
            VALUE_2 = 2
            VALUE_3 = 3

        self.assertEqual(TestEnum.values(), [1,2,3])

        self.assertNotEqual(TestEnum.values(as_list = False), [1,2,3])
        self.assertEqual(list(TestEnum.values(as_list = False)), [1,2,3])

    def test_get_with_mapping(self):
        class TestEnum(EnumWithDict):
            VALUE_1 = 1
            VALUE_2 = 2
            VALUE_3 = 3

        custom_mapping = {
            'VALUE_1': 'Mapped 1',
            'VALUE_2': 'Mapped 2',
            'VALUE_3': 'Mapped 3'
        }

        # Test getting a value from custom mapping
        self.assertEqual(TestEnum.get('VALUE_1', mapping=custom_mapping), 'Mapped 1')

        # Test getting a value without custom mapping
        self.assertEqual(TestEnum.get('VALUE_3'), 3)

        # Test getting a value with a default specified, when the key is not in the custom mapping or enum
        self.assertEqual(TestEnum.get('VALUE_4', default='Default', mapping=custom_mapping), 'Default')

        # Test getting a mapped value without a default specified, when the key is not in the custom mapping or enum
        # It should fall back to the custom mapping value with the initial key of the enum
        self.assertEqual(TestEnum.get('VALUE_4', mapping=custom_mapping), 'Mapped 1')  # Initial mapped value

        # Validation should fail because of incomplete mapping
        with self.assertRaises(KeyError) as context:
            TestEnum.get('VALUE_2', mapping={
                'VALUE_2': 'Mapped 2',
            })

        # Validation should fail because of empty mapping
        with self.assertRaises(KeyError) as context:
            TestEnum.get('VALUE_2', mapping={})

        # Validation should fail because of empty mapping
        with self.assertRaises(KeyError) as context:
            invalid_custom_mapping = custom_mapping
            invalid_custom_mapping['VALUE_4'] = 'Mapped 4'

            TestEnum.get('VALUE_2', mapping=invalid_custom_mapping)


if __name__ == '__main__':
    unittest.main()
