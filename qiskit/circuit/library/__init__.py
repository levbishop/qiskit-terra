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

"""
===============================================
Circuit Library (:mod:`qiskit.circuit.library`)
===============================================

.. currentmodule:: qiskit.circuit.library

Standard Gates
==============

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   Barrier
   C3XGate
   C3SXGate
   C4XGate
   CCXGate
   DCXGate
   CHGate
   CPhaseGate
   CRXGate
   CRYGate
   CRZGate
   CSwapGate
   CSXGate
   CUGate
   CU1Gate
   CU3Gate
   CXGate
   CYGate
   CZGate
   HGate
   IGate
   MCPhaseGate
   MCXGate
   MCXGrayCode
   MCXRecursive
   MCXVChain
   Measure
   MSGate
   PhaseGate
   RCCXGate
   RC3XGate
   Reset
   RGate
   RXGate
   RXXGate
   RYGate
   RYYGate
   RZGate
   RZZGate
   RZXGate
   ECRGate
   SGate
   SdgGate
   SwapGate
   iSwapGate
   SXGate
   SXdgGate
   TGate
   TdgGate
   UGate
   U1Gate
   U2Gate
   U3Gate
   XGate
   YGate
   ZGate

Generalized Gates
=================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   Diagonal
   MCMT
   MCMTVChain
   Permutation
   GMS
   GR
   GRX
   GRY
   GRZ
   RVGate
   PauliGate

Boolean Logic Circuits
======================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   AND
   OR
   XOR
   InnerProduct

Basis Change Circuits
=====================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   QFT

Arithmetic Circuits
===================

Amplitude Functions
-------------------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   LinearAmplitudeFunction

Functional Pauli Rotations
--------------------------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   FunctionalPauliRotations
   LinearPauliRotations
   PolynomialPauliRotations
   PiecewiseLinearPauliRotations
   PiecewisePolynomialPauliRotations
   PiecewiseChebyshev

Adders
------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   DraperQFTAdder
   CDKMRippleCarryAdder
   VBERippleCarryAdder
   WeightedAdder

Multipliers
-----------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   HRSCumulativeMultiplier
   RGQFTMultiplier

Comparators
-----------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   IntegerComparator

Functions on binary variables
-----------------------------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   QuadraticForm

Other arithmetic functions
--------------------------

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   ExactReciprocal

Amplitude Functions
===================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   LinearAmplitudeFunction

Particular Quantum Circuits
===========================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   FourierChecking
   GraphState
   HiddenLinearFunction
   IQP
   QuantumVolume
   PhaseEstimation
   GroverOperator
   PhaseOracle
   EvolvedOperatorAnsatz
   PauliEvolutionGate


Probability distributions
=========================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   UniformDistribution
   NormalDistribution
   LogNormalDistribution


N-local circuits
================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   NLocal
   TwoLocal
   PauliTwoDesign
   RealAmplitudes
   EfficientSU2
   ExcitationPreserving
   QAOAAnsatz


Data encoding circuits
======================

.. autosummary::
   :toctree: ../stubs/
   :template: autosummary/class_no_inherited_members.rst

   PauliFeatureMap
   ZFeatureMap
   ZZFeatureMap

NCT (Not-CNOT-Toffoli) template circuits
========================================

.. autosummary::
   :toctree: ../stubs/

   templates.nct.template_nct_2a_1
   templates.nct.template_nct_2a_2
   templates.nct.template_nct_2a_3
   templates.nct.template_nct_4a_1
   templates.nct.template_nct_4a_2
   templates.nct.template_nct_4a_3
   templates.nct.template_nct_4b_1
   templates.nct.template_nct_4b_2
   templates.nct.template_nct_5a_1
   templates.nct.template_nct_5a_2
   templates.nct.template_nct_5a_3
   templates.nct.template_nct_5a_4
   templates.nct.template_nct_6a_1
   templates.nct.template_nct_6a_2
   templates.nct.template_nct_6a_3
   templates.nct.template_nct_6a_4
   templates.nct.template_nct_6b_1
   templates.nct.template_nct_6b_2
   templates.nct.template_nct_6c_1
   templates.nct.template_nct_7a_1
   templates.nct.template_nct_7b_1
   templates.nct.template_nct_7c_1
   templates.nct.template_nct_7d_1
   templates.nct.template_nct_7e_1
   templates.nct.template_nct_2a_1
   templates.nct.template_nct_9a_1
   templates.nct.template_nct_9c_1
   templates.nct.template_nct_9c_2
   templates.nct.template_nct_9c_3
   templates.nct.template_nct_9c_4
   templates.nct.template_nct_9c_5
   templates.nct.template_nct_9c_6
   templates.nct.template_nct_9c_7
   templates.nct.template_nct_9c_8
   templates.nct.template_nct_9c_9
   templates.nct.template_nct_9c_10
   templates.nct.template_nct_9c_11
   templates.nct.template_nct_9c_12
   templates.nct.template_nct_9d_1
   templates.nct.template_nct_9d_2
   templates.nct.template_nct_9d_3
   templates.nct.template_nct_9d_4
   templates.nct.template_nct_9d_5
   templates.nct.template_nct_9d_6
   templates.nct.template_nct_9d_7
   templates.nct.template_nct_9d_8
   templates.nct.template_nct_9d_9
   templates.nct.template_nct_9d_10

Clifford template circuits
==========================

.. autosummary::
   :toctree: ../stubs/

   clifford_2_1
   clifford_2_2
   clifford_2_3
   clifford_2_4
   clifford_3_1
   clifford_4_1
   clifford_4_2
   clifford_4_3
   clifford_4_4
   clifford_5_1
   clifford_6_1
   clifford_6_2
   clifford_6_3
   clifford_6_4
   clifford_6_5
   clifford_8_1
   clifford_8_2
   clifford_8_3

RZXGate template circuits
=========================

.. autosummary::
   :toctree: ../stubs/

   rzx_yz
   rzx_xz
   rzx_cy
   rzx_zz1
   rzx_zz2
   rzx_zz3

"""

from __future__ import annotations

from qiskit.circuit.barrier import Barrier
from qiskit.circuit.library.arithmetic import CDKMRippleCarryAdder
from qiskit.circuit.library.arithmetic import DraperQFTAdder
from qiskit.circuit.library.arithmetic import ExactReciprocal
from qiskit.circuit.library.arithmetic import FunctionalPauliRotations
from qiskit.circuit.library.arithmetic import HRSCumulativeMultiplier
from qiskit.circuit.library.arithmetic import IntegerComparator
from qiskit.circuit.library.arithmetic import LinearAmplitudeFunction
from qiskit.circuit.library.arithmetic import LinearPauliRotations
from qiskit.circuit.library.arithmetic import PiecewiseChebyshev
from qiskit.circuit.library.arithmetic import PiecewiseLinearPauliRotations
from qiskit.circuit.library.arithmetic import PiecewisePolynomialPauliRotations
from qiskit.circuit.library.arithmetic import PolynomialPauliRotations
from qiskit.circuit.library.arithmetic import QuadraticForm
from qiskit.circuit.library.arithmetic import RGQFTMultiplier
from qiskit.circuit.library.arithmetic import VBERippleCarryAdder
from qiskit.circuit.library.arithmetic import WeightedAdder
from qiskit.circuit.library.basis_change import QFT
from qiskit.circuit.library.blueprintcircuit import BlueprintCircuit
from qiskit.circuit.library.boolean_logic import AND
from qiskit.circuit.library.boolean_logic import InnerProduct
from qiskit.circuit.library.boolean_logic import OR
from qiskit.circuit.library.boolean_logic import XOR
from qiskit.circuit.library.data_preparation import PauliFeatureMap
from qiskit.circuit.library.data_preparation import ZFeatureMap
from qiskit.circuit.library.data_preparation import ZZFeatureMap
from qiskit.circuit.library.evolved_operator_ansatz import EvolvedOperatorAnsatz
from qiskit.circuit.library.fourier_checking import FourierChecking
from qiskit.circuit.library.generalized_gates import Diagonal
from qiskit.circuit.library.generalized_gates import GMS
from qiskit.circuit.library.generalized_gates import GR
from qiskit.circuit.library.generalized_gates import GRX
from qiskit.circuit.library.generalized_gates import GRY
from qiskit.circuit.library.generalized_gates import GRZ
from qiskit.circuit.library.generalized_gates import MCMT
from qiskit.circuit.library.generalized_gates import MCMTVChain
from qiskit.circuit.library.generalized_gates import PauliGate
from qiskit.circuit.library.generalized_gates import Permutation
from qiskit.circuit.library.generalized_gates import RVGate
from qiskit.circuit.library.graph_state import GraphState
from qiskit.circuit.library.grover_operator import GroverOperator
from qiskit.circuit.library.hidden_linear_function import HiddenLinearFunction
from qiskit.circuit.library.iqp import IQP
from qiskit.circuit.library.n_local import EfficientSU2
from qiskit.circuit.library.n_local import ExcitationPreserving
from qiskit.circuit.library.n_local import NLocal
from qiskit.circuit.library.n_local import PauliTwoDesign
from qiskit.circuit.library.n_local import QAOAAnsatz
from qiskit.circuit.library.n_local import RealAmplitudes
from qiskit.circuit.library.n_local import TwoLocal
from qiskit.circuit.library.pauli_evolution import PauliEvolutionGate
from qiskit.circuit.library.phase_estimation import PhaseEstimation
from qiskit.circuit.library.phase_oracle import PhaseOracle
from qiskit.circuit.library.probability_distributions import LogNormalDistribution
from qiskit.circuit.library.probability_distributions import NormalDistribution
from qiskit.circuit.library.probability_distributions import UniformDistribution
from qiskit.circuit.library.quantum_volume import QuantumVolume
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library.templates import *
from qiskit.circuit.measure import Measure
from qiskit.circuit.reset import Reset
