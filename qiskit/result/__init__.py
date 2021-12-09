# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=========================================
Experiment Results (:mod:`qiskit.result`)
=========================================

.. currentmodule:: qiskit.result

.. autosummary::
   :toctree: ../stubs/

   Result
   ResultError
   Counts
   marginal_counts

Distributions
=============

.. autosummary::
   :toctree: ../stubs/

   ProbDistribution
   QuasiDistribution

Mitigation
==========
.. autosummary::
   :toctree: ../stubs/

   BaseReadoutMitigator
   CorrelatedReadoutMitigator
   LocalReadoutMitigator

"""

from __future__ import annotations

from qiskit.result.counts import Counts
from qiskit.result.distributions.probability import ProbDistribution
from qiskit.result.distributions.quasi import QuasiDistribution
from qiskit.result.exceptions import ResultError
from qiskit.result.mitigation.base_readout_mitigator import BaseReadoutMitigator
from qiskit.result.mitigation.correlated_readout_mitigator import CorrelatedReadoutMitigator
from qiskit.result.mitigation.local_readout_mitigator import LocalReadoutMitigator
from qiskit.result.result import Result
from qiskit.result.utils import marginal_counts
