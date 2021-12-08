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
=========================
Qobj (:mod:`qiskit.qobj`)
=========================

.. currentmodule:: qiskit.qobj

Base
====

.. autosummary::
   :toctree: ../stubs/

   Qobj
   QobjExperimentHeader
   QobjHeader

Qasm
====

.. autosummary::
   :toctree: ../stubs/

   QasmQobj
   QasmQobjInstruction
   QasmQobjExperimentConfig
   QasmQobjExperiment
   QasmQobjConfig
   QasmExperimentCalibrations
   GateCalibration

Pulse
=====

.. autosummary::
   :toctree: ../stubs/

   PulseQobj
   PulseQobjInstruction
   PulseQobjExperimentConfig
   PulseQobjExperiment
   PulseQobjConfig
   QobjMeasurementOption
   PulseLibraryItem
"""

from __future__ import annotations

import warnings

from qiskit.qobj.common import QobjExperimentHeader, QobjHeader
from qiskit.qobj.pulse_qobj import (
    PulseQobj,
    PulseQobjInstruction,
    PulseQobjExperimentConfig,
    PulseQobjExperiment,
    PulseQobjConfig,
    QobjMeasurementOption,
    PulseLibraryItem,
)
from qiskit.qobj.qasm_qobj import (
    GateCalibration,
    QasmExperimentCalibrations,
    QasmQobj,
    QasmQobjInstruction,
    QasmQobjExperiment,
    QasmQobjConfig,
    QasmQobjExperimentConfig,
)


class Qobj(QasmQobj):
    """A backwards compat alias for QasmQobj."""

    def __init__(self, qobj_id=None, config=None, experiments=None, header=None):
        """Initialize a Qobj object."""
        warnings.warn(
            "qiskit.qobj.Qobj is deprecated use either QasmQobj or "
            "PulseQobj depending on your application instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(qobj_id=qobj_id, config=config, experiments=experiments, header=header)
