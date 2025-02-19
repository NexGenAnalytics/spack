# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExomecopy(RPackage):
    """Copy number variant detection from exome sequencing read depth.

    Detection of copy number variants (CNV) from exome sequencing samples,
    including unpaired samples. The package implements a hidden Markov model
    which uses positional covariates, such as background read depth and
    GC-content, to simultaneously normalize and segment the samples into
    regions of constant copy count."""

    bioc = "exomeCopy"

    version('1.42.0', commit='ba0979cf5fbdefed841022f2dc0604941315c1b8')
    version('1.40.0', commit='ebde39be67baace2c326359421fd17f4a02fd4fe')
    version('1.36.0', commit='cbe3134acbbc9b7d5426ae2f142dc64cadb3fc26')
    version('1.32.0', commit='c9a884427d91b6d62ddc16a939bd808e389d3ea6')

    depends_on('r-iranges@2.5.27:', type=('build', 'run'))
    depends_on('r-genomicranges@1.23.16:', type=('build', 'run'))
    depends_on('r-rsamtools', type=('build', 'run'))
    depends_on('r-genomeinfodb', type=('build', 'run'))
