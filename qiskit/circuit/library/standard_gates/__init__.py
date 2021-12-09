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
=============================================================
Standard gates (:mod:`qiskit.circuit.library.standard_gates`)
=============================================================

.. autosummary::
   :toctree: ../stubs/

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
   MSGate
   MCPhaseGate
   PhaseGate
   RCCXGate
   RC3XGate
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

"""

from __future__ import annotations

from qiskit.circuit.library.standard_gates.dcx import DCXGate
from qiskit.circuit.library.standard_gates.ecr import ECRGate
from qiskit.circuit.library.standard_gates.h import CHGate, HGate
from qiskit.circuit.library.standard_gates.i import IGate
from qiskit.circuit.library.standard_gates.iswap import iSwapGate
from qiskit.circuit.library.standard_gates.ms import MSGate
from qiskit.circuit.library.standard_gates.multi_control_rotation_gates import mcrx, mcry, mcrz
from qiskit.circuit.library.standard_gates.p import CPhaseGate, MCPhaseGate, PhaseGate
from qiskit.circuit.library.standard_gates.r import RGate
from qiskit.circuit.library.standard_gates.rx import CRXGate, RXGate
from qiskit.circuit.library.standard_gates.rxx import RXXGate
from qiskit.circuit.library.standard_gates.ry import CRYGate, RYGate
from qiskit.circuit.library.standard_gates.ryy import RYYGate
from qiskit.circuit.library.standard_gates.rz import CRZGate, RZGate
from qiskit.circuit.library.standard_gates.rzx import RZXGate
from qiskit.circuit.library.standard_gates.rzz import RZZGate
from qiskit.circuit.library.standard_gates.s import SdgGate, SGate
from qiskit.circuit.library.standard_gates.swap import CSwapGate, SwapGate
from qiskit.circuit.library.standard_gates.sx import CSXGate, SXdgGate, SXGate
from qiskit.circuit.library.standard_gates.t import TdgGate, TGate
from qiskit.circuit.library.standard_gates.u import CUGate, UGate
from qiskit.circuit.library.standard_gates.u1 import CU1Gate, MCU1Gate, U1Gate
from qiskit.circuit.library.standard_gates.u2 import U2Gate
from qiskit.circuit.library.standard_gates.u3 import CU3Gate, U3Gate
from qiskit.circuit.library.standard_gates.x import (
    C3SXGate,
    C3XGate,
    C4XGate,
    CCXGate,
    CXGate,
    MCXGate,
    MCXGrayCode,
    MCXRecursive,
    MCXVChain,
    RC3XGate,
    RCCXGate,
    XGate,
)
from qiskit.circuit.library.standard_gates.y import CYGate, YGate
from qiskit.circuit.library.standard_gates.z import CZGate, ZGate
