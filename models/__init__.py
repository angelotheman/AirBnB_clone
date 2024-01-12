#!/usr/bin/python3
"""
Creating a unique File Storage instance for my application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
