#!/usr/bin/python3
"""
This is the test case for the file storage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    The class to test the storage of the project
    """

    def setUp(self):
        """
        Set's up a clean state for each test
        """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage.__class__.__file_path = self.file_path

    def tearDown(self):
        """
        Clean after each test
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path_default_value(self):
        """
        Test if default value of file path is correct
        """
        self.assertEqual(FileStorage.__file_path, "file.json")

    def test_file_path_custom_value(self):
        """
        Test if custom value of file path is set correctly
        """
        self.assertEqual(self.storage.__class__.__file_path, self.file_path)

    def test_objects_default_empty_dict(self):
        """
        Test if __objects is an empty dictionary by default
        """
        self.assertEqual(self.storage.__class__.__objects, {})

    def test_all_method_empty_storage(self):
        """
        Test the all() method when storage is empty
        """
        self.assertEqual(self.storage.all(), {})

    def test_all_method_with_objects(self):
        """
        Test the all() method when storage has objects
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(self.storage.all(), {key: obj})

    def test_new_method(self):
        """
        Test the new() method to ensure it adds an object to __objects
        """
        obj = BaseModel()
        self.storage.new(obj)

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_method(self):
        """
        Tests the save() method to ensure it writes to the correct file
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, "r", encoding="UTF -8") as text_file:
            data = json.load(text_file)
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_reload_method_empty_file(self):
        """
        Test the reload method when file is empty
        """
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_method_with_data(self):
        """
        Tests the reload method when the file has data
        """
        obj = User()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.__class__.__file_path = self.file_path
        new_storage.reload()

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key], obj)


if __name__ == '__main__':
    unittest.main()
