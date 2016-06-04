import subprocess
import sys

from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from itertools import starmap
from typing import Iterable

from pypi import cffi
from cffi import FFI


class CFFIMetaPathFinder(MetaPathFinder):
    mod_prefix = 'c.'

    def find_spec(self, fullname, path, target=None):
        if not fullname.startswith(self.mod_prefix):
            return

        mod_name = self.mod_name(fullname)
        ffi = FFI()
        cdef = self.preproc_header(['{}.h'.format(mod_name)])

        if cdef is None:
            return
        ffi.cdef(cdef)

        return ModuleSpec(mod_name, CFFILoader(),
                          origin=None, loader_state=ffi,
                          is_package=False)

    def preproc_header(self, headers: Iterable) -> str:
        '''
        :param headers: an iterable obj of headers
        '''
        formater = '#include <{}>'.format
        header_src = '\n'.join(map(formater, headers)).encode()
        clang_cmd = ('clang', '-fno-builtin',
                     '-U__GNUC__',
                     '-U__GNUC_MINOR__',
                     '-U__GNUC_PATCHLEVEL__',
                     '-E', '-')

        input_ = header_src
        clang = subprocess.Popen(
            clang_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL)
        output, _ = clang.communicate(input=input_)

        if clang.returncode != 0:
            return None
        return output.decode()

    def mod_name(self, fullname) -> str:
        '''
        >>> mpf = CFFIMetaPathFinder()
        >>> mpf.mod_name('c.stdlib')
        stdlib
        >>> mpf.mod_name('c.sys.types')
        sys.types
        '''
        return fullname.rpartition(self.mod_prefix)[-1]


class CFFILoader(Loader):
    def create_module(self, spec):
        self.spec = spec
        return None

    def exec_module(self, module):
        c = self.spec.loader_state.dlopen(None)
        for key in c.__dir__():
            try:
                setattr(module, key, getattr(c, key))
            except NotImplementedError:
                continue

        module.ffi = self.spec.loader_state


sys.meta_path.append(CFFIMetaPathFinder())
