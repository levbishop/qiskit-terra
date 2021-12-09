# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""The Amplitude Estimators package."""

from __future__ import annotations

from qiskit.algorithms.amplitude_estimators.ae import AmplitudeEstimation
from qiskit.algorithms.amplitude_estimators.ae import AmplitudeEstimationResult
from qiskit.algorithms.amplitude_estimators.amplitude_estimator import AmplitudeEstimator
from qiskit.algorithms.amplitude_estimators.amplitude_estimator import AmplitudeEstimatorResult
from qiskit.algorithms.amplitude_estimators.estimation_problem import EstimationProblem
from qiskit.algorithms.amplitude_estimators.fae import FasterAmplitudeEstimation
from qiskit.algorithms.amplitude_estimators.fae import FasterAmplitudeEstimationResult
from qiskit.algorithms.amplitude_estimators.iae import IterativeAmplitudeEstimation
from qiskit.algorithms.amplitude_estimators.iae import IterativeAmplitudeEstimationResult
from qiskit.algorithms.amplitude_estimators.mlae import MaximumLikelihoodAmplitudeEstimation
from qiskit.algorithms.amplitude_estimators.mlae import MaximumLikelihoodAmplitudeEstimationResult

__all__ = [
    "AmplitudeEstimator",
    "AmplitudeEstimatorResult",
    "AmplitudeEstimation",
    "AmplitudeEstimationResult",
    "FasterAmplitudeEstimation",
    "FasterAmplitudeEstimationResult",
    "IterativeAmplitudeEstimation",
    "IterativeAmplitudeEstimationResult",
    "MaximumLikelihoodAmplitudeEstimation",
    "MaximumLikelihoodAmplitudeEstimationResult",
    "EstimationProblem",
]
