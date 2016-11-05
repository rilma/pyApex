
from numpy.distutils.core import Extension, setup


sourcePath = 'source/'

f77CompileArgs = ['-std=legacy', '-fno-automatic', '-O', '-w']


# Quasi-dipole magnetic field-line
#

sources1 = []
for tmp in ['apex.pyf', 'apex.f', 'magfld.f']:
	sources1.append(sourcePath + tmp)

ext1 = Extension( name='apex', \
	sources=sources1, \
	extra_f77_compile_args=f77CompileArgs \
        )


# Geodetic to quasi-dipole coordinates
#

sources2 = []

ext2 = None


# Quasi-dipole to geodetic coordinates
#

sources3 = []
for tmp in ['apexqd2gd.pyf', 'qd2gdcoord.f90', 'apexsh.f90']:
	sources3.append(sourcePath + tmp)

ext3 = Extension( name='apexqd2gd', \
	sources=sources3, \
	extra_f77_compile_args=f77CompileArgs \
       )

if __name__ == '__main__':

    setup( name='pyapex', \
        version='0.0.1', \
        author='Ronald Ilma', \
        author_email='rri5@cornell.edu', \
        description='Apex Model Apps', \
        packages=['pyapex'], \
        ext_package='pyapex', \
        ext_modules=[ ext1, ext3 ], \
        data_files=[('pyapex', [sourcePath + 'apexsh.dat'])], \
        )
