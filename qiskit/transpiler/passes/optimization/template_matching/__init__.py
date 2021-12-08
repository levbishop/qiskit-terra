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

"""Module containing template matching methods."""

from __future__ import annotations

from qiskit.transpiler.passes.optimization.template_matching.forward_match import ForwardMatch
from qiskit.transpiler.passes.optimization.template_matching.backward_match import (
    BackwardMatch,
    Match,
    MatchingScenarios,
    MatchingScenariosList,
)
from qiskit.transpiler.passes.optimization.template_matching.template_matching import (
    TemplateMatching,
)
from qiskit.transpiler.passes.optimization.template_matching.maximal_matches import MaximalMatches
from qiskit.transpiler.passes.optimization.template_matching.template_substitution import (
    SubstitutionConfig,
    TemplateSubstitution,
)
