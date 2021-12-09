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
====================================================================
BasicAer: Python-based Simulators (:mod:`qiskit.providers.basicaer`)
====================================================================

.. currentmodule:: qiskit.providers.basicaer

A module of Python-based quantum simulators.  Simulators are accessed
via the `BasicAer` provider, e.g.:

.. jupyter-execute::

            from qiskit import BasicAer

            backend = BasicAer.get_backend('qasm_simulator')


Simulators
==========

.. autosummary::
   :toctree: ../stubs/

   QasmSimulatorPy
   StatevectorSimulatorPy
   UnitarySimulatorPy

Provider
========

.. autosummary::
   :toctree: ../stubs/

   BasicAerProvider

Job Class
=========

.. autosummary::
   :toctree: ../stubs/

   BasicAerJob

Exceptions
==========

.. autosummary::
   :toctree: ../stubs/

   BasicAerError
"""

from __future__ import annotations

from qiskit.providers.basicaer.basicaerjob import BasicAerJob
from qiskit.providers.basicaer.basicaerprovider import BasicAerProvider
from qiskit.providers.basicaer.exceptions import BasicAerError
from qiskit.providers.basicaer.qasm_simulator import QasmSimulatorPy
from qiskit.providers.basicaer.statevector_simulator import StatevectorSimulatorPy
from qiskit.providers.basicaer.unitary_simulator import UnitarySimulatorPy

# Global instance to be used as the entry point for convenience.
BasicAer = BasicAerProvider()
