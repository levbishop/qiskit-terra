# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""The arithmetic circuit library."""

from __future__ import annotations

from qiskit.circuit.library.arithmetic.adders import (
    CDKMRippleCarryAdder,
    DraperQFTAdder,
    VBERippleCarryAdder,
)
from qiskit.circuit.library.arithmetic.exact_reciprocal import ExactReciprocal
from qiskit.circuit.library.arithmetic.functional_pauli_rotations import FunctionalPauliRotations
from qiskit.circuit.library.arithmetic.integer_comparator import IntegerComparator
from qiskit.circuit.library.arithmetic.linear_amplitude_function import LinearAmplitudeFunction
from qiskit.circuit.library.arithmetic.linear_pauli_rotations import LinearPauliRotations
from qiskit.circuit.library.arithmetic.multipliers import HRSCumulativeMultiplier, RGQFTMultiplier
from qiskit.circuit.library.arithmetic.piecewise_chebyshev import PiecewiseChebyshev
from qiskit.circuit.library.arithmetic.piecewise_linear_pauli_rotations import (
    PiecewiseLinearPauliRotations,
)
from qiskit.circuit.library.arithmetic.piecewise_polynomial_pauli_rotations import (
    PiecewisePolynomialPauliRotations,
)
from qiskit.circuit.library.arithmetic.polynomial_pauli_rotations import PolynomialPauliRotations
from qiskit.circuit.library.arithmetic.quadratic_form import QuadraticForm
from qiskit.circuit.library.arithmetic.weighted_adder import WeightedAdder
