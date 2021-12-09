# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

r"""
===========================
Pulse (:mod:`qiskit.pulse`)
===========================

.. currentmodule:: qiskit.pulse

Qiskit-Pulse is a pulse-level quantum programming kit. This lower level of
programming offers the user more control than programming with
:py:class:`~qiskit.circuit.QuantumCircuit`\ s.

Extracting the greatest performance from quantum hardware requires real-time
pulse-level instructions. Pulse answers that need: it enables the quantum
physicist *user* to specify the exact time dynamics of an experiment.
It is especially powerful for error mitigation techniques.

The input is given as arbitrary, time-ordered signals (see: :ref:`Instructions <pulse-insts>`)
scheduled in parallel over multiple virtual hardware or simulator resources
(see: :ref:`Channels <pulse-channels>`). The system also allows the user to recover the
time dynamics of the measured output.

This is sufficient to allow the quantum physicist to explore and correct for
noise in a quantum system.

.. automodule:: qiskit.pulse.instructions
.. automodule:: qiskit.pulse.library
.. automodule:: qiskit.pulse.channels
.. automodule:: qiskit.pulse.schedule
.. automodule:: qiskit.pulse.transforms
.. automodule:: qiskit.pulse.builder

.. currentmodule:: qiskit.pulse

Configuration
=============

.. autosummary::
   :toctree: ../stubs/

   InstructionScheduleMap

Exceptions
==========

.. autoclass:: PulseError
"""

# Builder imports.

# Construction methods:
from __future__ import annotations

from qiskit.pulse.builder import active_backend
from qiskit.pulse.builder import active_circuit_scheduler_settings
from qiskit.pulse.builder import active_transpiler_settings
from qiskit.pulse.builder import build
from qiskit.pulse.builder import num_qubits
from qiskit.pulse.builder import qubit_channels
from qiskit.pulse.builder import samples_to_seconds
from qiskit.pulse.builder import seconds_to_samples

# Instructions:
from qiskit.pulse.builder import acquire
from qiskit.pulse.builder import barrier
from qiskit.pulse.builder import call
from qiskit.pulse.builder import delay
from qiskit.pulse.builder import play
from qiskit.pulse.builder import set_frequency
from qiskit.pulse.builder import set_phase
from qiskit.pulse.builder import shift_frequency
from qiskit.pulse.builder import shift_phase
from qiskit.pulse.builder import snapshot

# Channels:
from qiskit.pulse.builder import acquire_channel
from qiskit.pulse.builder import control_channels
from qiskit.pulse.builder import drive_channel
from qiskit.pulse.builder import measure_channel

# Contexts:
from qiskit.pulse.builder import align_equispaced
from qiskit.pulse.builder import align_func
from qiskit.pulse.builder import align_left
from qiskit.pulse.builder import align_right
from qiskit.pulse.builder import align_sequential
from qiskit.pulse.builder import circuit_scheduler_settings
from qiskit.pulse.builder import frequency_offset
from qiskit.pulse.builder import inline
from qiskit.pulse.builder import pad
from qiskit.pulse.builder import phase_offset
from qiskit.pulse.builder import transpiler_settings

# Macros:
from qiskit.pulse.builder import delay_qubits
from qiskit.pulse.builder import macro
from qiskit.pulse.builder import measure
from qiskit.pulse.builder import measure_all

# Circuit instructions:
from qiskit.pulse.builder import cx
from qiskit.pulse.builder import u1
from qiskit.pulse.builder import u2
from qiskit.pulse.builder import u3
from qiskit.pulse.builder import x
from qiskit.pulse.channels import AcquireChannel
from qiskit.pulse.channels import ControlChannel
from qiskit.pulse.channels import DriveChannel
from qiskit.pulse.channels import MeasureChannel
from qiskit.pulse.channels import MemorySlot
from qiskit.pulse.channels import RegisterSlot
from qiskit.pulse.channels import SnapshotChannel
from qiskit.pulse.configuration import Discriminator
from qiskit.pulse.configuration import Kernel
from qiskit.pulse.configuration import LoConfig
from qiskit.pulse.configuration import LoRange
from qiskit.pulse.exceptions import PulseError
from qiskit.pulse.instruction_schedule_map import InstructionScheduleMap
from qiskit.pulse.instructions import Acquire
from qiskit.pulse.instructions import Call
from qiskit.pulse.instructions import Delay
from qiskit.pulse.instructions import Instruction
from qiskit.pulse.instructions import Play
from qiskit.pulse.instructions import SetFrequency
from qiskit.pulse.instructions import SetPhase
from qiskit.pulse.instructions import ShiftFrequency
from qiskit.pulse.instructions import ShiftPhase
from qiskit.pulse.instructions import Snapshot
from qiskit.pulse.library import Constant
from qiskit.pulse.library import Drag
from qiskit.pulse.library import Gaussian
from qiskit.pulse.library import GaussianSquare
from qiskit.pulse.library import ParametricPulse
from qiskit.pulse.library import Waveform
from qiskit.pulse.library.samplers.decorators import functional_pulse
from qiskit.pulse.schedule import Schedule
from qiskit.pulse.schedule import ScheduleBlock
