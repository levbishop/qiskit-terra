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

from qiskit.transpiler.passes.layout import (
    ApplyLayout,
    CSPLayout,
    DenseLayout,
    EnlargeWithAncilla,
    FullAncillaAllocation,
    Layout2qDistance,
    NoiseAdaptiveLayout,
    SabreLayout,
    SetLayout,
    TrivialLayout,
    VF2Layout,
)

# routing
from qiskit.transpiler.passes.routing import (
    BasicSwap,
    BIPMapping,
    LayoutTransformation,
    LookaheadSwap,
    SabreSwap,
    StochasticSwap,
)

# basis change
from qiskit.transpiler.passes.basis import (
    BasisTranslator,
    Decompose,
    Unroll3qOrMore,
    UnrollCustomDefinitions,
    Unroller,
)

# optimization
from qiskit.transpiler.passes.optimization import (
    Collect1qRuns,
    Collect2qBlocks,
    CollectMultiQBlocks,
    CommutationAnalysis,
    CommutativeCancellation,
    ConsolidateBlocks,
    CrosstalkAdaptiveSchedule,
    CXCancellation,
    EchoRZXWeylDecomposition,
    HoareOptimizer,
    InverseCancellation,
    Optimize1qGates,
    Optimize1qGatesDecomposition,
    Optimize1qGatesSimpleCommutation,
    OptimizeSwapBeforeMeasure,
    RemoveDiagonalGatesBeforeMeasure,
    RemoveResetInZeroState,
    TemplateOptimization,
)

# circuit analysis
from qiskit.transpiler.passes.analysis import (
    CountOps,
    CountOpsLongestPath,
    DAGLongestPath,
    Depth,
    NumTensorFactors,
    ResourceEstimation,
    Size,
    Width,
)

# synthesis
from qiskit.transpiler.passes.synthesis import UnitarySynthesis, unitary_synthesis_plugin_names

# calibration
from qiskit.transpiler.passes.calibration import (
    PulseGates,
    RZXCalibrationBuilder,
    RZXCalibrationBuilderNoEcho,
)

# circuit scheduling
from qiskit.transpiler.passes.scheduling import (
    ALAPSchedule,
    AlignMeasures,
    ASAPSchedule,
    DynamicalDecoupling,
    TimeUnitConversion,
    ValidatePulseGates,
)

# additional utility passes
from qiskit.transpiler.passes.utils import CheckCXDirection  # Deprecated
from qiskit.transpiler.passes.utils import CXDirection  # Deprecated
from qiskit.transpiler.passes.utils import (
    BarrierBeforeFinalMeasurements,
    CheckGateDirection,
    CheckMap,
    ContainsInstruction,
    DAGFixedPoint,
    Error,
    FixedPoint,
    GateDirection,
    GatesInBasis,
    MergeAdjacentBarriers,
    RemoveBarriers,
    RemoveFinalMeasurements,
)
