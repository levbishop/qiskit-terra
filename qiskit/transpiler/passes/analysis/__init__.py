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

"""Module containing circuit analysis passes."""

from __future__ import annotations

from qiskit.transpiler.passes.analysis.count_ops import CountOps
from qiskit.transpiler.passes.analysis.count_ops_longest_path import CountOpsLongestPath
from qiskit.transpiler.passes.analysis.dag_longest_path import DAGLongestPath
from qiskit.transpiler.passes.analysis.depth import Depth
from qiskit.transpiler.passes.analysis.num_qubits import NumQubits
from qiskit.transpiler.passes.analysis.num_tensor_factors import NumTensorFactors
from qiskit.transpiler.passes.analysis.resource_estimation import ResourceEstimation
from qiskit.transpiler.passes.analysis.size import Size
from qiskit.transpiler.passes.analysis.width import Width
