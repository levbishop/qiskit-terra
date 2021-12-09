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
from qiskit.circuit.library.standard_gates.h import CHGate
from qiskit.circuit.library.standard_gates.h import HGate
from qiskit.circuit.library.standard_gates.i import IGate
from qiskit.circuit.library.standard_gates.iswap import iSwapGate
from qiskit.circuit.library.standard_gates.ms import MSGate
from qiskit.circuit.library.standard_gates.multi_control_rotation_gates import mcrx
from qiskit.circuit.library.standard_gates.multi_control_rotation_gates import mcry
from qiskit.circuit.library.standard_gates.multi_control_rotation_gates import mcrz
from qiskit.circuit.library.standard_gates.p import CPhaseGate
from qiskit.circuit.library.standard_gates.p import MCPhaseGate
from qiskit.circuit.library.standard_gates.p import PhaseGate
from qiskit.circuit.library.standard_gates.r import RGate
from qiskit.circuit.library.standard_gates.rx import CRXGate
from qiskit.circuit.library.standard_gates.rx import RXGate
from qiskit.circuit.library.standard_gates.rxx import RXXGate
from qiskit.circuit.library.standard_gates.ry import CRYGate
from qiskit.circuit.library.standard_gates.ry import RYGate
from qiskit.circuit.library.standard_gates.ryy import RYYGate
from qiskit.circuit.library.standard_gates.rz import CRZGate
from qiskit.circuit.library.standard_gates.rz import RZGate
from qiskit.circuit.library.standard_gates.rzx import RZXGate
from qiskit.circuit.library.standard_gates.rzz import RZZGate
from qiskit.circuit.library.standard_gates.s import SdgGate
from qiskit.circuit.library.standard_gates.s import SGate
from qiskit.circuit.library.standard_gates.swap import CSwapGate
from qiskit.circuit.library.standard_gates.swap import SwapGate
from qiskit.circuit.library.standard_gates.sx import CSXGate
from qiskit.circuit.library.standard_gates.sx import SXdgGate
from qiskit.circuit.library.standard_gates.sx import SXGate
from qiskit.circuit.library.standard_gates.t import TdgGate
from qiskit.circuit.library.standard_gates.t import TGate
from qiskit.circuit.library.standard_gates.u import CUGate
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.circuit.library.standard_gates.u1 import CU1Gate
from qiskit.circuit.library.standard_gates.u1 import MCU1Gate
from qiskit.circuit.library.standard_gates.u1 import U1Gate
from qiskit.circuit.library.standard_gates.u2 import U2Gate
from qiskit.circuit.library.standard_gates.u3 import CU3Gate
from qiskit.circuit.library.standard_gates.u3 import U3Gate
from qiskit.circuit.library.standard_gates.x import C3SXGate
from qiskit.circuit.library.standard_gates.x import C3XGate
from qiskit.circuit.library.standard_gates.x import C4XGate
from qiskit.circuit.library.standard_gates.x import CCXGate
from qiskit.circuit.library.standard_gates.x import CXGate
from qiskit.circuit.library.standard_gates.x import MCXGate
from qiskit.circuit.library.standard_gates.x import MCXGrayCode
from qiskit.circuit.library.standard_gates.x import MCXRecursive
from qiskit.circuit.library.standard_gates.x import MCXVChain
from qiskit.circuit.library.standard_gates.x import RC3XGate
from qiskit.circuit.library.standard_gates.x import RCCXGate
from qiskit.circuit.library.standard_gates.x import XGate
from qiskit.circuit.library.standard_gates.y import CYGate
from qiskit.circuit.library.standard_gates.y import YGate
from qiskit.circuit.library.standard_gates.z import CZGate
from qiskit.circuit.library.standard_gates.z import ZGate
