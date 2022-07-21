# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install teuchos
#
# You can edit this file again by typing:
#
#     spack edit teuchos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
import subprocess

from spack import *


class Teuchos(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://localhost/"
    url      = "http://localhost/teuchos-0.1.0.tar.gz"

    maintainers = ['keitat']

    version('0.1.0', sha256=@@@@@, preferred=True)

    root_cmakelists_dir = "packages/teuchos"

    depends_on('cmake@3.20.0:', type='build')
    depends_on('openblas')
    depends_on('lapack')
    depends_on('boost', when='+Boost')
    depends_on('eigen', when='+Eigen')
    depends_on('kokkos', when='+Kokkos')
    depends_on('openmpi', when='+MPI')

    # Optionnal TPL dependencies
    variant('Boost', default=False, description='Compile with Boost')
    variant('Eigen', default=False, description='Compile with Eigen')
    variant('Kokkos', default=False, description='Compile with Kokkos')
    variant('MPI', default=False, description='Compile with MPI parallelism')
    variant('Pthread', default=False, description='Compile with Pthread')
    variant('Qt', default=False, description='Compile with Qt')
    # Not yet supported in Cmake
    variant('ARPREC', default=False, description='Compile with ARPREC')
    variant('BinUtils', default=False, description='Compile with BinUtils')
    variant('QD', default=False, description='Compile with QD')
    variant('Valgrind', default=False, description='Compile with Valgrind')

    def cmake_args(self):
        def define_teuchos_enable(suffix, value=None):
            if value is None:
                return self.define_from_variant(f'Teuchos_ENABLE_{suffix}', suffix)
            elif isinstance(value, bool):
                return self.define(f'Teuchos_ENABLE_{suffix}', value)

        num_of_proc = 1
        try:
            num_of_proc = int(subprocess.run(['nproc', '--all'],
                                             capture_output=True, encoding='utf-8').stdout.replace('\n', ''))
        except:
            pass

        args = [
            '-DBUILD_SHARED_LIBS=ON',
            f'-DMPI_EXEC_DEFAULT_NUMPROCS={num_of_proc}',
            f'-DMPI_EXEC_MAX_NUMPROCS={num_of_proc}',
            '-DTEUCHOS_HAS_TRILINOS=OFF',
            '-DTeuchos_ENABLE_TESTS=ON'
        ]
        args.extend([
            define_teuchos_enable('ARPREC'),
            define_teuchos_enable('BinUtils'),
            define_teuchos_enable('Boost'),
            define_teuchos_enable('Eigen'),
            define_teuchos_enable('Kokkos'),
            define_teuchos_enable('MPI'),
            define_teuchos_enable('Pthread'),
            define_teuchos_enable('QD'),
            define_teuchos_enable('Qt'),
            define_teuchos_enable('Valgrind'),
        ])
        return args
