# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPrometheusClient(PythonPackage):
    """Prometheus instrumentation library for Python applications."""

    pypi = "prometheus_client/prometheus_client-0.7.1.tar.gz"

    version('0.12.0', sha256='1b12ba48cee33b9b0b9de64a1047cbd3c5f2d0ab6ebcead7ddda613a750ec3c5')
    version('0.7.1', sha256='71cd24a2b3eb335cb800c7159f423df1bd4dcd5171b234be15e3f31ec9f622da')
    version('0.7.0', sha256='ee0c90350595e4a9f36591f291e6f9933246ea67d7cd7d1d6139a9781b14eaae')
    version('0.5.0', sha256='e8c11ff5ca53de6c3d91e1510500611cafd1d247a937ec6c588a0a7cc3bef93c')

    variant('twisted', default=False, description='Expose metrics as a twisted resource')

    depends_on('py-setuptools', type='build')
    # Notice: prometheus_client/twisted/_exposition.py imports 'twisted.web.wsgi'
    # which was not ported to Python 3 until twisted 16.0.0
    depends_on('py-twisted', type=('build', 'run'), when='+twisted')
    depends_on('py-twisted@16:', type=('build', 'run'), when='@0.12.0: +twisted ^python@3:')
    depends_on('python@2.7:2,3.4:', type=('build', 'run'), when='@0.12.0:')

    @property
    def import_modules(self):
        modules = [
            'prometheus_client', 'prometheus_client.openmetrics',
            'prometheus_client.bridge'
        ]

        if '+twisted' in self.spec:
            modules.append('prometheus_client.twisted')

        return modules
