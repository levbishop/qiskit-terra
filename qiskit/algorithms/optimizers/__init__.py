# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Optimizers (:mod:`qiskit.algorithms.optimizers`)
=====================================================
It  contains a variety of classical optimizers for use by quantum variational algorithms,
such as :class:`~qiskit.algorithms.VQE`.
Logically, these optimizers can be divided into two categories:

`Local Optimizers`_
  Given an optimization problem, a **local optimizer** is a function
  that attempts to find an optimal value within the neighboring set of a candidate solution.

`Global Optimizers`_
  Given an optimization problem, a **global optimizer** is a function
  that attempts to find an optimal value among all possible solutions.

.. currentmodule:: qiskit.algorithms.optimizers

Optimizer Base Class
====================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   OptimizerResult
   OptimizerSupportLevel
   Optimizer

Local Optimizers
================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   ADAM
   AQGD
   CG
   COBYLA
   L_BFGS_B
   GSLS
   GradientDescent
   NELDER_MEAD
   NFT
   P_BFGS
   POWELL
   SLSQP
   SPSA
   QNSPSA
   TNC
   SciPyOptimizer

Qiskit also provides the following optimizers, which are built-out using the optimizers from
the `scikit-quant` package. The `scikit-quant` package is not installed by default but must be
explicitly installed, if desired, by the user - the optimizers therein are provided under various
licenses so it has been made an optional install for the end user to choose whether to do so or
not. To install the `scikit-quant` dependent package you can use
`pip install scikit-quant`.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   BOBYQA
   IMFIL
   SNOBFIT

Global Optimizers
=================
The global optimizers here all use NLopt for their core function and can only be
used if their dependent NLopt package is manually installed. See the following
section for installation instructions.

.. autosummary::
    :toctree: ../stubs/

    nlopts

The global optimizers are as follows:

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   CRS
   DIRECT_L
   DIRECT_L_RAND
   ESCH
   ISRES

"""

from __future__ import annotations

from qiskit.algorithms.optimizers.adam_amsgrad import ADAM
from qiskit.algorithms.optimizers.aqgd import AQGD
from qiskit.algorithms.optimizers.bobyqa import BOBYQA
from qiskit.algorithms.optimizers.cg import CG
from qiskit.algorithms.optimizers.cobyla import COBYLA
from qiskit.algorithms.optimizers.gsls import GSLS
from qiskit.algorithms.optimizers.gradient_descent import GradientDescent
from qiskit.algorithms.optimizers.imfil import IMFIL
from qiskit.algorithms.optimizers.l_bfgs_b import L_BFGS_B
from qiskit.algorithms.optimizers.nelder_mead import NELDER_MEAD
from qiskit.algorithms.optimizers.nft import NFT
from qiskit.algorithms.optimizers.nlopts.crs import CRS
from qiskit.algorithms.optimizers.nlopts.direct_l import DIRECT_L
from qiskit.algorithms.optimizers.nlopts.direct_l_rand import DIRECT_L_RAND
from qiskit.algorithms.optimizers.nlopts.esch import ESCH
from qiskit.algorithms.optimizers.nlopts.isres import ISRES
from qiskit.algorithms.optimizers.optimizer import Optimizer, OptimizerResult, OptimizerSupportLevel
from qiskit.algorithms.optimizers.p_bfgs import P_BFGS
from qiskit.algorithms.optimizers.powell import POWELL
from qiskit.algorithms.optimizers.qnspsa import QNSPSA
from qiskit.algorithms.optimizers.scipy_optimizer import SciPyOptimizer
from qiskit.algorithms.optimizers.slsqp import SLSQP
from qiskit.algorithms.optimizers.snobfit import SNOBFIT
from qiskit.algorithms.optimizers.spsa import SPSA
from qiskit.algorithms.optimizers.tnc import TNC

__all__ = [
    "Optimizer",
    "OptimizerSupportLevel",
    "ADAM",
    "AQGD",
    "CG",
    "COBYLA",
    "GSLS",
    "GradientDescent",
    "L_BFGS_B",
    "NELDER_MEAD",
    "NFT",
    "P_BFGS",
    "POWELL",
    "SciPyOptimizer",
    "SLSQP",
    "SPSA",
    "QNSPSA",
    "TNC",
    "CRS",
    "DIRECT_L",
    "DIRECT_L_RAND",
    "ESCH",
    "ISRES",
    "SNOBFIT",
    "BOBYQA",
    "IMFIL",
]
