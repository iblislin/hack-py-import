import sys

from _frozen_importlib_external import PathFinder
from importlib.abc import MetaPathFinder

from pip import main as pip


class PyPIMetaPathFinder(MetaPathFinder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_finder = PathFinder()

    def find_spec(self, fullname, path, target=None):
        if not fullname.startswith('pypi'):
            return

        mod_name = fullname.rpartition('pypi.')[-1]
        pip_args = ['install', mod_name]
        if pip(pip_args):
            raise ImportError('Not Found "{}" from the Cheese Shop'
                              .format(mod_name))

        return self.path_finder.find_spec(mod_name, None, target)


sys.meta_path.append(PyPIMetaPathFinder())
