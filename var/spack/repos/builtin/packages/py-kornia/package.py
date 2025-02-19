# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKornia(PythonPackage):
    """Open Source Differentiable Computer Vision Library for PyTorch."""

    homepage = "https://www.kornia.org/"
    pypi     = "kornia/kornia-0.5.10.tar.gz"

    version('0.6.6', sha256='e29f0f994e3bafec016b101a9a3e89c3751b4fe99ada3ac21d3febb47904faa4')
    version('0.6.5', sha256='14cbd8b4064b3d0fb5a8198d1b5fd9231bcd62b9039351641fca6b294b5069f0')
    version('0.6.4', sha256='ff60307a7244b315db43bfc4d4d6769094cf7d7494cf367c1d71a56343e2c50f')
    version('0.6.3', sha256='0b689b5a47f55f2b08f61e6731760542cc3e3c09c3f0498164b934a3aef0bab3')
    version('0.6.2', sha256='eea722b3ff2f227a9ef8088cdab480cd40dd91d9138649bfd92cfa668204eea9')
    version('0.6.1', sha256='f638fb3309f88666545866c162f510b6d485fd8f7131d5570d4e6c0d295fdcd6')
    version('0.5.10', sha256='428b4b934a2ba7360cc6cba051ed8fd96c2d0f66611fdca0834e82845f14f65d')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-pytest-runner', type='build')
    depends_on('py-torch@1.6.0:', type=('build', 'run'))
    depends_on('py-torch@1.8.1:', when='@0.6:', type=('build', 'run'))
    depends_on('py-packaging', when='@0.6:', type=('build', 'run'))
