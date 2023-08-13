#!usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """atributes:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the all objects from database"""
        return FileStorage.__objects

    def new(self,obj):
        """set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serialize the objects to the JSON file __file__path."""
        # Create a dictionary `odict` of the objects in the `__objects` dictionary.
        odict = FileStorage.__objects

        # Create a dictionary `objdict` of the objects in the `odict` dictionary,
        # where the key is the object and the value is the object's dictionary representation.
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}

        # Open the JSON file `__file_path` in write mode.
        with open(FileStorage.__file_path, "w") as f:

            # Serialize the dictionary `objdict` to the JSON file `f`.
            json.dump(objdict, f)

   def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
