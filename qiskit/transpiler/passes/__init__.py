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
===================================================
Transpiler Passes (:mod:`qiskit.transpiler.passes`)
===================================================

.. currentmodule:: qiskit.transpiler.passes

Layout Selection (Placement)
============================

.. autosummary::
   :toctree: ../stubs/

   SetLayout
   TrivialLayout
   DenseLayout
   NoiseAdaptiveLayout
   SabreLayout
   CSPLayout
   VF2Layout
   ApplyLayout
   Layout2qDistance
   EnlargeWithAncilla
   FullAncillaAllocation

Routing
=======

.. autosummary::
   :toctree: ../stubs/

   BasicSwap
   LookaheadSwap
   StochasticSwap
   SabreSwap
   BIPMapping

Basis Change
============

.. autosummary::
   :toctree: ../stubs/

   Unroller
   Unroll3qOrMore
   Decompose
   UnrollCustomDefinitions
   BasisTranslator

Optimizations
=============

.. autosummary::
   :toctree: ../stubs/

   Optimize1qGates
   Optimize1qGatesDecomposition
   Collect1qRuns
   Collect2qBlocks
   CollectMultiQBlocks
   ConsolidateBlocks
   CXCancellation
   InverseCancellation
   CommutationAnalysis
   CommutativeCancellation
   Optimize1qGatesSimpleCommutation
   RemoveDiagonalGatesBeforeMeasure
   RemoveResetInZeroState
   CrosstalkAdaptiveSchedule
   TemplateOptimization
   EchoRZXWeylDecomposition

Calibration
=============

.. autosummary::
   :toctree: ../stubs/

   PulseGates
   RZXCalibrationBuilder
   RZXCalibrationBuilderNoEcho

Scheduling
=============

.. autosummary::
   :toctree: ../stubs/

   TimeUnitConversion
   ALAPSchedule
   ASAPSchedule
   DynamicalDecoupling
   AlignMeasures
   ValidatePulseGates

Circuit Analysis
================

.. autosummary::
   :toctree: ../stubs/

   Width
   Depth
   Size
   CountOps
   CountOpsLongestPath
   NumTensorFactors
   DAGLongestPath

Synthesis
=============

.. autosummary::
   :toctree: ../stubs/

   UnitarySynthesis

Additional Passes
=================

.. autosummary::
   :toctree: ../stubs/

   CheckMap
   CheckCXDirection
   CheckGateDirection
   CXDirection
   GateDirection
   MergeAdjacentBarriers
   RemoveBarriers
   BarrierBeforeFinalMeasurements
   RemoveFinalMeasurements
   DAGFixedPoint
   FixedPoint
   ContainsInstruction
   GatesInBasis
"""

# layout selection (placement)
from __future__ import annotations

from qiskit.transpiler.passes.layout import ApplyLayout
from qiskit.transpiler.passes.layout import CSPLayout
from qiskit.transpiler.passes.layout import DenseLayout
from qiskit.transpiler.passes.layout import EnlargeWithAncilla
from qiskit.transpiler.passes.layout import FullAncillaAllocation
from qiskit.transpiler.passes.layout import Layout2qDistance
from qiskit.transpiler.passes.layout import NoiseAdaptiveLayout
from qiskit.transpiler.passes.layout import SabreLayout
from qiskit.transpiler.passes.layout import SetLayout
from qiskit.transpiler.passes.layout import TrivialLayout
from qiskit.transpiler.passes.layout import VF2Layout

# routing
from qiskit.transpiler.passes.routing import BasicSwap
from qiskit.transpiler.passes.routing import BIPMapping
from qiskit.transpiler.passes.routing import LayoutTransformation
from qiskit.transpiler.passes.routing import LookaheadSwap
from qiskit.transpiler.passes.routing import SabreSwap
from qiskit.transpiler.passes.routing import StochasticSwap

# basis change
from qiskit.transpiler.passes.basis import BasisTranslator
from qiskit.transpiler.passes.basis import Decompose
from qiskit.transpiler.passes.basis import Unroll3qOrMore
from qiskit.transpiler.passes.basis import UnrollCustomDefinitions
from qiskit.transpiler.passes.basis import Unroller

# optimization
from qiskit.transpiler.passes.optimization import Collect1qRuns
from qiskit.transpiler.passes.optimization import Collect2qBlocks
from qiskit.transpiler.passes.optimization import CollectMultiQBlocks
from qiskit.transpiler.passes.optimization import CommutationAnalysis
from qiskit.transpiler.passes.optimization import CommutativeCancellation
from qiskit.transpiler.passes.optimization import ConsolidateBlocks
from qiskit.transpiler.passes.optimization import CrosstalkAdaptiveSchedule
from qiskit.transpiler.passes.optimization import CXCancellation
from qiskit.transpiler.passes.optimization import EchoRZXWeylDecomposition
from qiskit.transpiler.passes.optimization import HoareOptimizer
from qiskit.transpiler.passes.optimization import InverseCancellation
from qiskit.transpiler.passes.optimization import Optimize1qGates
from qiskit.transpiler.passes.optimization import Optimize1qGatesDecomposition
from qiskit.transpiler.passes.optimization import Optimize1qGatesSimpleCommutation
from qiskit.transpiler.passes.optimization import OptimizeSwapBeforeMeasure
from qiskit.transpiler.passes.optimization import RemoveDiagonalGatesBeforeMeasure
from qiskit.transpiler.passes.optimization import RemoveResetInZeroState
from qiskit.transpiler.passes.optimization import TemplateOptimization

# circuit analysis
from qiskit.transpiler.passes.analysis import CountOps
from qiskit.transpiler.passes.analysis import CountOpsLongestPath
from qiskit.transpiler.passes.analysis import DAGLongestPath
from qiskit.transpiler.passes.analysis import Depth
from qiskit.transpiler.passes.analysis import NumTensorFactors
from qiskit.transpiler.passes.analysis import ResourceEstimation
from qiskit.transpiler.passes.analysis import Size
from qiskit.transpiler.passes.analysis import Width

# synthesis
from qiskit.transpiler.passes.synthesis import unitary_synthesis_plugin_names
from qiskit.transpiler.passes.synthesis import UnitarySynthesis

# calibration
from qiskit.transpiler.passes.calibration import PulseGates
from qiskit.transpiler.passes.calibration import RZXCalibrationBuilder
from qiskit.transpiler.passes.calibration import RZXCalibrationBuilderNoEcho

# circuit scheduling
from qiskit.transpiler.passes.scheduling import ALAPSchedule
from qiskit.transpiler.passes.scheduling import AlignMeasures
from qiskit.transpiler.passes.scheduling import ASAPSchedule
from qiskit.transpiler.passes.scheduling import DynamicalDecoupling
from qiskit.transpiler.passes.scheduling import TimeUnitConversion
from qiskit.transpiler.passes.scheduling import ValidatePulseGates

# additional utility passes
from qiskit.transpiler.passes.utils import BarrierBeforeFinalMeasurements
from qiskit.transpiler.passes.utils import CheckCXDirection  # Deprecated
from qiskit.transpiler.passes.utils import CheckGateDirection
from qiskit.transpiler.passes.utils import CheckMap
from qiskit.transpiler.passes.utils import ContainsInstruction
from qiskit.transpiler.passes.utils import CXDirection  # Deprecated
from qiskit.transpiler.passes.utils import DAGFixedPoint
from qiskit.transpiler.passes.utils import Error
from qiskit.transpiler.passes.utils import FixedPoint
from qiskit.transpiler.passes.utils import GateDirection
from qiskit.transpiler.passes.utils import GatesInBasis
from qiskit.transpiler.passes.utils import MergeAdjacentBarriers
from qiskit.transpiler.passes.utils import RemoveBarriers
from qiskit.transpiler.passes.utils import RemoveFinalMeasurements
