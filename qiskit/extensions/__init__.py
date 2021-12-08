# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=====================================================
Quantum Circuit Extensions (:mod:`qiskit.extensions`)
=====================================================

.. currentmodule:: qiskit.extensions

Unitary Extensions
==================

.. autosummary::
   :toctree: ../stubs/

   UnitaryGate
   HamiltonianGate
   SingleQubitUnitary

Simulator Extensions
====================

.. autosummary::
   :toctree: ../stubs/

   Snapshot

Initialization
==============

.. autosummary::
   :toctree: ../stubs/

   Initialize
"""

# import all standard gates
from __future__ import annotations

from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.barrier import Barrier

from qiskit.extensions.quantum_initializer import Initialize, SingleQubitUnitary
from qiskit.extensions.unitary import UnitaryGate
from qiskit.extensions.hamiltonian_gate import HamiltonianGate
from qiskit.extensions.simulator import Snapshot
