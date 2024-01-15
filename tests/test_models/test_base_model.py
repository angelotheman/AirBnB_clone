#!/usr/bin/python3
"""
This is the python test cases for the base model class
- Every function def is a test
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """This is the base class for all the test cases"""

    def setUp(self):
        """Initializes the class for the rest of the test cases"""
        self.base_model = BaseModel()

    def test_initialiazation(self):
        """
        - Tests the various initialiazations
        - Test if created_at and updated_at are datetime objects
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        """
        Tests the string method of the class
        """
        str_representation = str(self.base_model)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn("id", str_representation)
        self.assertIn("created_at", str_representation)
        self.assertIn("updated_at", str_representation)

    def test_save_method(self):
        """
        Tests the save method of the class
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Tests if dictionary object was created
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_initialiazation_with_dict(self):
        """
        Testing if init with a dictionary (kwargs) sets attributes correctly
        """
        model_dict =
        {
                'id': 'test_id',
                'created_at', '2022-01-01T00:00:00.000000',
                'updated_at', '2022-02-01T00:00:00.000000',
                'custom_attr', 'custom_value'
        }

        model_instance = BaseModel(**model_dict)

        self.assertEqual(model_instance.id, 'test_id')
        self.assertEqual(model_instance.created_at, datetime(2022, 1, 1))
        self.assertEqual(model_instance.updated_at, datetime(2022, 2, 1))
        self.assertEqual(model_instance.custom_attr, 'custom_value')


if __name__ == '__main__':
    unittest.main()
