# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
================================================
Quantum Information (:mod:`qiskit.quantum_info`)
================================================

.. currentmodule:: qiskit.quantum_info

Operators
=========

.. autosummary::
   :toctree: ../stubs/

   Operator
   Pauli
   Clifford
   ScalarOp
   SparsePauliOp
   CNOTDihedral
   PauliList
   PauliTable
   StabilizerTable
   pauli_basis
   pauli_group

States
======

.. autosummary::
   :toctree: ../stubs/

   Statevector
   DensityMatrix
   StabilizerState

Channels
========
.. autosummary::
   :toctree: ../stubs/

   Choi
   SuperOp
   Kraus
   Stinespring
   Chi
   PTM

Measures
========

.. autosummary::
   :toctree: ../stubs/

   average_gate_fidelity
   process_fidelity
   gate_error
   diamond_norm
   state_fidelity
   purity
   concurrence
   entropy
   entanglement_of_formation
   mutual_information

Utility Functions
=================

.. autosummary::
   :toctree: ../stubs/

   partial_trace
   shannon_entropy

Random
======

.. autosummary::
   :toctree: ../stubs/

   random_statevector
   random_density_matrix
   random_unitary
   random_hermitian
   random_pauli
   random_clifford
   random_quantum_channel
   random_cnotdihedral
   random_pauli_table
   random_pauli_list
   random_stabilizer_table

Analysis
=========

.. autosummary::
   :toctree: ../stubs/

   hellinger_distance
   hellinger_fidelity

Synthesis
=========

.. autosummary::
   :toctree: ../stubs/

   OneQubitEulerDecomposer
   TwoQubitBasisDecomposer
   two_qubit_cnot_decompose
   Quaternion
   decompose_clifford
   XXDecomposer
"""

from __future__ import annotations

from qiskit.quantum_info.analysis import hellinger_distance
from qiskit.quantum_info.analysis import hellinger_fidelity
from qiskit.quantum_info.operators import Clifford
from qiskit.quantum_info.operators import Operator
from qiskit.quantum_info.operators import Pauli
from qiskit.quantum_info.operators import pauli_basis
from qiskit.quantum_info.operators import pauli_group
from qiskit.quantum_info.operators import PauliList
from qiskit.quantum_info.operators import PauliTable
from qiskit.quantum_info.operators import ScalarOp
from qiskit.quantum_info.operators import SparsePauliOp
from qiskit.quantum_info.operators import StabilizerTable
from qiskit.quantum_info.operators.channel import Chi
from qiskit.quantum_info.operators.channel import Choi
from qiskit.quantum_info.operators.channel import Kraus
from qiskit.quantum_info.operators.channel import PTM
from qiskit.quantum_info.operators.channel import Stinespring
from qiskit.quantum_info.operators.channel import SuperOp
from qiskit.quantum_info.operators.dihedral import CNOTDihedral
from qiskit.quantum_info.operators.measures import average_gate_fidelity
from qiskit.quantum_info.operators.measures import diamond_norm
from qiskit.quantum_info.operators.measures import gate_error
from qiskit.quantum_info.operators.measures import process_fidelity
from qiskit.quantum_info.random import random_clifford
from qiskit.quantum_info.random import random_cnotdihedral
from qiskit.quantum_info.random import random_density_matrix
from qiskit.quantum_info.random import random_hermitian
from qiskit.quantum_info.random import random_pauli
from qiskit.quantum_info.random import random_pauli_list
from qiskit.quantum_info.random import random_pauli_table
from qiskit.quantum_info.random import random_quantum_channel
from qiskit.quantum_info.random import random_stabilizer_table
from qiskit.quantum_info.random import random_statevector
from qiskit.quantum_info.random import random_unitary
from qiskit.quantum_info.states import concurrence
from qiskit.quantum_info.states import DensityMatrix
from qiskit.quantum_info.states import entanglement_of_formation
from qiskit.quantum_info.states import entropy
from qiskit.quantum_info.states import mutual_information
from qiskit.quantum_info.states import partial_trace
from qiskit.quantum_info.states import purity
from qiskit.quantum_info.states import shannon_entropy
from qiskit.quantum_info.states import StabilizerState
from qiskit.quantum_info.states import state_fidelity
from qiskit.quantum_info.states import Statevector
from qiskit.quantum_info.synthesis import decompose_clifford
from qiskit.quantum_info.synthesis import OneQubitEulerDecomposer
from qiskit.quantum_info.synthesis import Quaternion
from qiskit.quantum_info.synthesis import two_qubit_cnot_decompose
from qiskit.quantum_info.synthesis import TwoQubitBasisDecomposer
from qiskit.quantum_info.synthesis import XXDecomposer
