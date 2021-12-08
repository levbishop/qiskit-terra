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

"""Module containing transpiler optimization passes."""

from __future__ import annotations

from qiskit.transpiler.passes.optimization.optimize_1q_gates import Optimize1qGates
from qiskit.transpiler.passes.optimization.optimize_1q_decomposition import Optimize1qGatesDecomposition
from qiskit.transpiler.passes.optimization.collect_2q_blocks import Collect2qBlocks
from qiskit.transpiler.passes.optimization.collect_multiqubit_blocks import CollectMultiQBlocks
from qiskit.transpiler.passes.optimization.consolidate_blocks import ConsolidateBlocks
from qiskit.transpiler.passes.optimization.commutation_analysis import CommutationAnalysis
from qiskit.transpiler.passes.optimization.commutative_cancellation import CommutativeCancellation
from qiskit.transpiler.passes.optimization.cx_cancellation import CXCancellation
from qiskit.transpiler.passes.optimization.optimize_1q_commutation import Optimize1qGatesSimpleCommutation
from qiskit.transpiler.passes.optimization.optimize_swap_before_measure import OptimizeSwapBeforeMeasure
from qiskit.transpiler.passes.optimization.remove_reset_in_zero_state import RemoveResetInZeroState
from qiskit.transpiler.passes.optimization.remove_diagonal_gates_before_measure import RemoveDiagonalGatesBeforeMeasure
from qiskit.transpiler.passes.optimization.crosstalk_adaptive_schedule import CrosstalkAdaptiveSchedule
from qiskit.transpiler.passes.optimization.hoare_opt import HoareOptimizer
from qiskit.transpiler.passes.optimization.template_optimization import TemplateOptimization
from qiskit.transpiler.passes.optimization.inverse_cancellation import InverseCancellation
from qiskit.transpiler.passes.optimization.collect_1q_runs import Collect1qRuns
from qiskit.transpiler.passes.optimization.echo_rzx_weyl_decomposition import EchoRZXWeylDecomposition
