# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""The circuit library module on generalized gates."""

from __future__ import annotations

from qiskit.circuit.library.generalized_gates.diagonal import Diagonal
from qiskit.circuit.library.generalized_gates.permutation import Permutation
from qiskit.circuit.library.generalized_gates.mcmt import MCMT, MCMTVChain
from qiskit.circuit.library.generalized_gates.gms import GMS, MSGate
from qiskit.circuit.library.generalized_gates.gr import GR, GRX, GRY, GRZ
from qiskit.circuit.library.generalized_gates.pauli import PauliGate
from qiskit.circuit.library.generalized_gates.rv import RVGate
