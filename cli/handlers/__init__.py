import inspect
import sys
import os


def get_classes():
    current_module = sys.modules[__name__]
    classes = list(filter(lambda key: inspect.ismodule(getattr(current_module, key)) and key.endswith("_handler"),
                          dir(current_module)))
    return classes
