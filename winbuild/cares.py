from .utils import *
from .builder import *

class CaresBuilder(StandardBuilder):
    def build(self):
        cares_dir = self.standard_fetch_extract(
            'http://c-ares.haxx.se/download/c-ares-%(my_version)s.tar.gz')
        if self.bconf.cares_version == '1.12.0':
            # msvc_ver.inc is missing in c-ares-1.12.0.tar.gz
            # https://github.com/c-ares/c-ares/issues/69
            fetch('https://raw.githubusercontent.com/c-ares/c-ares/cares-1_12_0/msvc_ver.inc',
                  archive='cares-1.12.0/msvc_ver.inc')
        with in_dir(cares_dir):
            with self.execute_batch() as b:
                if self.bconf.cares_version == '1.10.0':
                    b.add(
                        f"patch -p1 < {require_file_exists(os.path.join(config.winbuild_patch_root, 'c-ares-vs2015.patch'))}"
                    )

                b.add("nmake -f Makefile.msvc")

                # assemble dist
                b.add('mkdir dist dist\\include dist\\lib')
                if self.bconf.cares_version_tuple < (1, 14, 0):
                    subdir = f'ms{self.bconf.vc_version}0'
                else:
                    subdir = 'msvc'
                b.add(f'cp {subdir}/cares/lib-release/*.lib dist/lib')
                b.add('cp *.h dist/include')
