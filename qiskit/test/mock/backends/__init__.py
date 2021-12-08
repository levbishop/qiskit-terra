# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.


"""
Mocked versions of real quantum backends.
"""

# BackendV1 Backends
from __future__ import annotations

from qiskit.test.mock.backends.almaden import FakeAlmaden
from qiskit.test.mock.backends.armonk import FakeArmonk
from qiskit.test.mock.backends.athens import FakeAthens
from qiskit.test.mock.backends.belem import FakeBelem
from qiskit.test.mock.backends.boeblingen import FakeBoeblingen
from qiskit.test.mock.backends.bogota import FakeBogota
from qiskit.test.mock.backends.brooklyn import FakeBrooklyn
from qiskit.test.mock.backends.burlington import FakeBurlington
from qiskit.test.mock.backends.cambridge import FakeCambridge, FakeCambridgeAlternativeBasis
from qiskit.test.mock.backends.casablanca import FakeCasablanca
from qiskit.test.mock.backends.essex import FakeEssex
from qiskit.test.mock.backends.guadalupe import FakeGuadalupe
from qiskit.test.mock.backends.jakarta import FakeJakarta
from qiskit.test.mock.backends.johannesburg import FakeJohannesburg
from qiskit.test.mock.backends.lagos import FakeLagos
from qiskit.test.mock.backends.lima import FakeLima
from qiskit.test.mock.backends.london import FakeLondon
from qiskit.test.mock.backends.manhattan import FakeManhattan
from qiskit.test.mock.backends.manila import FakeManila
from qiskit.test.mock.backends.melbourne import FakeMelbourne
from qiskit.test.mock.backends.montreal import FakeMontreal
from qiskit.test.mock.backends.mumbai import FakeMumbai
from qiskit.test.mock.backends.ourense import FakeOurense
from qiskit.test.mock.backends.paris import FakeParis
from qiskit.test.mock.backends.poughkeepsie import FakePoughkeepsie
from qiskit.test.mock.backends.quito import FakeQuito
from qiskit.test.mock.backends.rochester import FakeRochester
from qiskit.test.mock.backends.rome import FakeRome
from qiskit.test.mock.backends.rueschlikon import FakeRueschlikon
from qiskit.test.mock.backends.santiago import FakeSantiago
from qiskit.test.mock.backends.singapore import FakeSingapore
from qiskit.test.mock.backends.sydney import FakeSydney
from qiskit.test.mock.backends.tenerife import FakeTenerife
from qiskit.test.mock.backends.tokyo import FakeTokyo
from qiskit.test.mock.backends.toronto import FakeToronto
from qiskit.test.mock.backends.valencia import FakeValencia
from qiskit.test.mock.backends.vigo import FakeVigo
from qiskit.test.mock.backends.yorktown import FakeYorktown

# Legacy Backends
from qiskit.test.mock.backends.almaden import FakeLegacyAlmaden
from qiskit.test.mock.backends.armonk import FakeLegacyArmonk
from qiskit.test.mock.backends.athens import FakeLegacyAthens
from qiskit.test.mock.backends.belem import FakeLegacyBelem
from qiskit.test.mock.backends.boeblingen import FakeLegacyBoeblingen
from qiskit.test.mock.backends.bogota import FakeLegacyBogota
from qiskit.test.mock.backends.burlington import FakeLegacyBurlington
from qiskit.test.mock.backends.cambridge import FakeLegacyCambridge, FakeLegacyCambridgeAlternativeBasis
from qiskit.test.mock.backends.casablanca import FakeLegacyCasablanca
from qiskit.test.mock.backends.essex import FakeLegacyEssex
from qiskit.test.mock.backends.johannesburg import FakeLegacyJohannesburg
from qiskit.test.mock.backends.lima import FakeLegacyLima
from qiskit.test.mock.backends.london import FakeLegacyLondon
from qiskit.test.mock.backends.manhattan import FakeLegacyManhattan
from qiskit.test.mock.backends.melbourne import FakeLegacyMelbourne
from qiskit.test.mock.backends.montreal import FakeLegacyMontreal
from qiskit.test.mock.backends.mumbai import FakeLegacyMumbai
from qiskit.test.mock.backends.ourense import FakeLegacyOurense
from qiskit.test.mock.backends.paris import FakeLegacyParis
from qiskit.test.mock.backends.poughkeepsie import FakeLegacyPoughkeepsie
from qiskit.test.mock.backends.quito import FakeLegacyQuito
from qiskit.test.mock.backends.rochester import FakeLegacyRochester
from qiskit.test.mock.backends.rome import FakeLegacyRome
from qiskit.test.mock.backends.rueschlikon import FakeLegacyRueschlikon
from qiskit.test.mock.backends.santiago import FakeLegacySantiago
from qiskit.test.mock.backends.singapore import FakeLegacySingapore
from qiskit.test.mock.backends.sydney import FakeLegacySydney
from qiskit.test.mock.backends.tenerife import FakeLegacyTenerife
from qiskit.test.mock.backends.tokyo import FakeLegacyTokyo
from qiskit.test.mock.backends.toronto import FakeLegacyToronto
from qiskit.test.mock.backends.valencia import FakeLegacyValencia
from qiskit.test.mock.backends.vigo import FakeLegacyVigo
from qiskit.test.mock.backends.yorktown import FakeLegacyYorktown
