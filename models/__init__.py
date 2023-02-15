#!/usr/bin/python3
"""Initializes package"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
print("This happens first right, from the import")
storage.reload()
