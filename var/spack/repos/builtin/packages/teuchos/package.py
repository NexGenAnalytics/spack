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

from spack import *


class Teuchos(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "git@github.com:MikolajZuzek/Trilinos.git"

    maintainers = ['keitat']

    version('1-teuchos-cmake', branch='1-teuchos-cmake', preferred=True)

    root_cmakelists_dir = "packages/teuchos"

    depends_on('cmake@3.20.0:', type='build')

    # Mandatory TPL dependencies
    # TPL (BLAS, LAPACK)
    #    depends_on('openblas')

    # Optionnal TPL dependencies(MPI, Eigen, BinUtils, QD, ARPREC, Boost, Qt)
    variant('MPI', default=False, description='Compile with MPI parallelism')
    variant('Eigen', default=False, description='Compile with Eigen')
    variant('BinUtils', default=False, description='Compile with BinUtils')
    variant('QD', default=False, description='Compile with QD')
    variant('ARPREC', default=False, description='Compile with ARPREC')
    variant('Boost', default=False, description='Compile with Boost')
    variant('Qt', default=False, description='Compile with Qt')


    # Optionnal Package dependencies (Kokkos)




    # Extra Cmake Options

    def cmake_args(self):

        spec = self.spec
        define = CMakePackage.define
        define_from_variant = self.define_from_variant

        def _make_definer(prefix):
            def define_enable(suffix, value=None):
                key = prefix + suffix
                if value is None:
                    # Default to lower-case spec
                    value = suffix
                elif isinstance(value, bool):
                    # Explicit true/false
                    return define(key, value)
                return define_from_variant(key, value)
            return define_enable

        # Return "Teuchos_ENABLE_XXX" for spec "+xxx" or boolean value
        define_teuchos_enable = _make_definer("Teuchos_ENABLE_")
        # Same but for TPLs
        define_tpl_enable = _make_definer("TPL_ENABLE_")
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
        '-DCMAKE_POSITION_INDEPENDENT_CODE=ON',
        '-DTEUCHOS_STANDALONE_PACKAGE=ON'
        ]

        args.extend([
            define_teuchos_enable('MPI'),
            define_teuchos_enable('Eigen'),
            define_teuchos_enable('BinUtils'),
            define_teuchos_enable('QD'),
            define_teuchos_enable('ARPREC'),
            define_teuchos_enable('Boost'),
            define_teuchos_enable('Qt'),
        ])
        return args
