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

from qiskit.circuit.library.standard_gates.h import HGate, CHGate
from qiskit.circuit.library.standard_gates.i import IGate
from qiskit.circuit.library.standard_gates.p import PhaseGate, CPhaseGate, MCPhaseGate
from qiskit.circuit.library.standard_gates.ms import MSGate
from qiskit.circuit.library.standard_gates.r import RGate
from qiskit.circuit.library.standard_gates.rx import RXGate, CRXGate
from qiskit.circuit.library.standard_gates.rxx import RXXGate
from qiskit.circuit.library.standard_gates.ry import RYGate, CRYGate
from qiskit.circuit.library.standard_gates.ryy import RYYGate
from qiskit.circuit.library.standard_gates.rz import RZGate, CRZGate
from qiskit.circuit.library.standard_gates.rzz import RZZGate
from qiskit.circuit.library.standard_gates.rzx import RZXGate
from qiskit.circuit.library.standard_gates.ecr import ECRGate
from qiskit.circuit.library.standard_gates.s import SGate, SdgGate
from qiskit.circuit.library.standard_gates.swap import SwapGate, CSwapGate
from qiskit.circuit.library.standard_gates.iswap import iSwapGate
from qiskit.circuit.library.standard_gates.sx import SXGate, SXdgGate, CSXGate
from qiskit.circuit.library.standard_gates.dcx import DCXGate
from qiskit.circuit.library.standard_gates.t import TGate, TdgGate
from qiskit.circuit.library.standard_gates.u import UGate, CUGate
from qiskit.circuit.library.standard_gates.u1 import U1Gate, CU1Gate, MCU1Gate
from qiskit.circuit.library.standard_gates.u2 import U2Gate
from qiskit.circuit.library.standard_gates.u3 import U3Gate, CU3Gate
from qiskit.circuit.library.standard_gates.x import (
    XGate,
    CXGate,
    CCXGate,
    C3XGate,
    C3SXGate,
    C4XGate,
    RCCXGate,
    RC3XGate,
    MCXGate,
    MCXGrayCode,
    MCXRecursive,
    MCXVChain,
)
from qiskit.circuit.library.standard_gates.y import YGate, CYGate
from qiskit.circuit.library.standard_gates.z import ZGate, CZGate
from qiskit.circuit.library.standard_gates.multi_control_rotation_gates import mcrx, mcry, mcrz
