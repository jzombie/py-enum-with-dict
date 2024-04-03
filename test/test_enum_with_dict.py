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

    def test_string_values(self):
        class Mood(EnumWithDict):
            HAPPY = "happy"
            SAD = "sad"
            ANGRY = "angry"
        
        expected = {'HAPPY': "happy", 'SAD': "sad", 'ANGRY': "angry"}
        self.assertEqual(Mood.to_dict(), expected)
        self.assertEqual(Mood.get_initial(), "happy")

    def test_tuple_values(self):
        class Coordinates(EnumWithDict):
            POINT_A = (1, 2)
            POINT_B = (3, 4)
        
        expected = {'POINT_A': (1, 2), 'POINT_B': (3, 4)}
        self.assertEqual(Coordinates.to_dict(), expected)
        self.assertEqual(Coordinates.get_initial(), (1, 2))

    def test_function_values(self):        
        class Actions(EnumWithDict):
            ACTION_A = EnumWithDict
            ACTION_B = len
        
        self.assertTrue(callable(Actions.to_dict()['ACTION_A']))
        self.assertTrue(callable(Actions.to_dict()['ACTION_B']))

        self.assertEqual(Actions.get_initial(), EnumWithDict)


if __name__ == '__main__':
    unittest.main()
