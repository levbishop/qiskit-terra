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

"""Utility passes used for other main passes."""

from __future__ import annotations

from qiskit.transpiler.passes.utils.check_map import CheckMap
from qiskit.transpiler.passes.utils.check_cx_direction import CheckCXDirection  # Deprecated
from qiskit.transpiler.passes.utils.cx_direction import CXDirection  # Deprecated
from qiskit.transpiler.passes.utils.check_gate_direction import CheckGateDirection
from qiskit.transpiler.passes.utils.gate_direction import GateDirection
from qiskit.transpiler.passes.utils.barrier_before_final_measurements import BarrierBeforeFinalMeasurements
from qiskit.transpiler.passes.utils.remove_final_measurements import RemoveFinalMeasurements
from qiskit.transpiler.passes.utils.merge_adjacent_barriers import MergeAdjacentBarriers
from qiskit.transpiler.passes.utils.dag_fixed_point import DAGFixedPoint
from qiskit.transpiler.passes.utils.fixed_point import FixedPoint
from qiskit.transpiler.passes.utils.error import Error
from qiskit.transpiler.passes.utils.remove_barriers import RemoveBarriers
from qiskit.transpiler.passes.utils.contains_instruction import ContainsInstruction
from qiskit.transpiler.passes.utils.gates_basis import GatesInBasis
