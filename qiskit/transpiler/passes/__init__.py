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
from .layout import (
    SetLayout,
    TrivialLayout,
    DenseLayout,
    NoiseAdaptiveLayout,
    SabreLayout,
    CSPLayout,
    VF2Layout,
    ApplyLayout,
    Layout2qDistance,
    EnlargeWithAncilla,
    FullAncillaAllocation,
)

# routing
from .routing import (
    BasicSwap,
    LayoutTransformation,
    LookaheadSwap,
    StochasticSwap,
    SabreSwap,
    BIPMapping,
)

# basis change
from .basis import Decompose, Unroller, UnrollCustomDefinitions, Unroll3qOrMore, BasisTranslator

# optimization
from .optimization import (
    Optimize1qGates,
    Optimize1qGatesDecomposition,
    Collect2qBlocks,
    Collect1qRuns,
    CollectMultiQBlocks,
    ConsolidateBlocks,
    CommutationAnalysis,
    CommutativeCancellation,
    CXCancellation,
    Optimize1qGatesSimpleCommutation,
    OptimizeSwapBeforeMeasure,
    RemoveResetInZeroState,
    RemoveDiagonalGatesBeforeMeasure,
    CrosstalkAdaptiveSchedule,
    HoareOptimizer,
    TemplateOptimization,
    InverseCancellation,
    EchoRZXWeylDecomposition,
)

# circuit analysis
from .analysis import (
    ResourceEstimation,
    Depth,
    Size,
    Width,
    CountOps,
    CountOpsLongestPath,
    NumTensorFactors,
    DAGLongestPath,
)

# synthesis
from .synthesis import UnitarySynthesis, unitary_synthesis_plugin_names

# calibration
from .calibration import PulseGates, RZXCalibrationBuilder, RZXCalibrationBuilderNoEcho

# circuit scheduling
from .scheduling import (
    TimeUnitConversion,
    ALAPSchedule,
    ASAPSchedule,
    DynamicalDecoupling,
    AlignMeasures,
    ValidatePulseGates,
)

# additional utility passes
from .utils import CheckCXDirection  # Deprecated
from .utils import CXDirection  # Deprecated
from .utils import (
    CheckMap,
    CheckGateDirection,
    GateDirection,
    BarrierBeforeFinalMeasurements,
    RemoveFinalMeasurements,
    MergeAdjacentBarriers,
    DAGFixedPoint,
    FixedPoint,
    Error,
    RemoveBarriers,
    ContainsInstruction,
    GatesInBasis,
)
