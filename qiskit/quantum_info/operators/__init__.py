# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Quantum Operators."""

from __future__ import annotations

from qiskit.quantum_info.operators.operator import Operator

# These must come after to avoid cyclic import problems?
from qiskit.quantum_info.operators.scalar_op import ScalarOp
from qiskit.quantum_info.operators.channel import Choi, SuperOp, Kraus, Stinespring, Chi, PTM
from qiskit.quantum_info.operators.measures import process_fidelity, average_gate_fidelity, gate_error, diamond_norm
from qiskit.quantum_info.operators.symplectic import (
    Clifford,
    Pauli,
    PauliList,
    SparsePauliOp,
    PauliTable,
    StabilizerTable,
    pauli_basis,
)
from qiskit.quantum_info.operators.pauli import pauli_group
from qiskit.quantum_info.operators.dihedral import CNOTDihedral
