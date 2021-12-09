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
================================================
Backend Objects (:mod:`qiskit.providers.models`)
================================================

.. currentmodule:: qiskit.providers.models

Qiskit schema-conformant objects used by the backends and providers.

Backend Objects
===============

.. autosummary::
   :toctree: ../stubs/

   BackendConfiguration
   BackendProperties
   BackendStatus
   QasmBackendConfiguration
   PulseBackendConfiguration
   UchannelLO
   GateConfig
   PulseDefaults
   Command
   JobStatus
"""

from __future__ import annotations

from qiskit.providers.models.backendconfiguration import BackendConfiguration
from qiskit.providers.models.backendconfiguration import GateConfig
from qiskit.providers.models.backendconfiguration import PulseBackendConfiguration
from qiskit.providers.models.backendconfiguration import QasmBackendConfiguration
from qiskit.providers.models.backendconfiguration import UchannelLO
from qiskit.providers.models.backendproperties import BackendProperties
from qiskit.providers.models.backendstatus import BackendStatus
from qiskit.providers.models.jobstatus import JobStatus
from qiskit.providers.models.pulsedefaults import Command
from qiskit.providers.models.pulsedefaults import PulseDefaults
