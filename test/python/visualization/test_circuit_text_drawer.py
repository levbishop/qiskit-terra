# -*- coding: utf-8 -*-

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

""" `_text_circuit_drawer` "draws" a circuit in "ascii art" """

from codecs import encode
from math import pi
import unittest
import sympy
import numpy

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import text as elements
from qiskit.visualization.circuit_visualization import _text_circuit_drawer
from qiskit.test import QiskitTestCase
from qiskit.circuit import Gate, Parameter
from qiskit.quantum_info.random import random_unitary
from qiskit.quantum_info.operators import SuperOp


class TestTextDrawerElement(QiskitTestCase):
    """ Draw each element"""

    def assertEqualElement(self, expected, element):
        """
        Asserts the top,mid,bot trio
        Args:
            expected (list[top,mid,bot]): What is expected.
            element (DrawElement): The element to check.
        """
        try:
            encode("\n".join(expected), encoding="cp437")
        except UnicodeEncodeError:
            self.fail(
                "_text_circuit_drawer() should only use extended ascii (aka code page 437)."
            )

        self.assertEqual(expected[0], element.top)
        self.assertEqual(expected[1], element.mid)
        self.assertEqual(expected[2], element.bot)

    def test_measure_to(self):
        """ MeasureTo element. """
        element = elements.MeasureTo()
        expected = [" ║ ", "═╩═", "   "]
        self.assertEqualElement(expected, element)

    def test_measure_from(self):
        """ MeasureFrom element. """
        element = elements.MeasureFrom()
        expected = ["┌─┐", "┤M├", "└╥┘"]
        self.assertEqualElement(expected, element)

    def test_text_empty(self):
        """ The empty circuit."""
        expected = ""
        circuit = QuantumCircuit()
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_pager(self):
        """ The pager breaks the circuit when the drawing does not fit in the console."""
        expected = "\n".join(
            [
                "        ┌───┐     »",
                "q_0: |0>┤ X ├──■──»",
                "        └─┬─┘┌─┴─┐»",
                "q_1: |0>──■──┤ X ├»",
                "             └───┘»",
                " c_0: 0 ══════════»",
                "                  »",
                "«     ┌─┐┌───┐     »",
                "«q_0: ┤M├┤ X ├──■──»",
                "«     └╥┘└─┬─┘┌─┴─┐»",
                "«q_1: ─╫───■──┤ X ├»",
                "«      ║      └───┘»",
                "«c_0: ═╩═══════════»",
                "«                  »",
                "«     ┌─┐┌───┐     ",
                "«q_0: ┤M├┤ X ├──■──",
                "«     └╥┘└─┬─┘┌─┴─┐",
                "«q_1: ─╫───■──┤ X ├",
                "«      ║      └───┘",
                "«c_0: ═╩═══════════",
                "«                  ",
            ]
        )

        qr = QuantumRegister(2, "q")
        cr = ClassicalRegister(1, "c")
        circuit = QuantumCircuit(qr, cr)
        circuit.cx(qr[1], qr[0])
        circuit.cx(qr[0], qr[1])
        circuit.measure(qr[0], cr[0])
        circuit.cx(qr[1], qr[0])
        circuit.cx(qr[0], qr[1])
        circuit.measure(qr[0], cr[0])
        circuit.cx(qr[1], qr[0])
        circuit.cx(qr[0], qr[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, line_length=20)), expected)

    def test_text_no_pager(self):
        """ The pager can be disable."""
        qr = QuantumRegister(1, "q")
        circuit = QuantumCircuit(qr)
        for _ in range(100):
            circuit.h(qr[0])
        amount_of_lines = str(_text_circuit_drawer(circuit, line_length=-1)).count("\n")
        self.assertEqual(amount_of_lines, 2)


class TestTextDrawerGatesInCircuit(QiskitTestCase):
    """ Gate by gate checks in different settings."""

    def test_text_measure_1(self):
        """ The measure operator, using 3-bit-length registers. """
        expected = "\n".join(
            [
                "        ┌─┐      ",
                "q_0: |0>┤M├──────",
                "        └╥┘┌─┐   ",
                "q_1: |0>─╫─┤M├───",
                "         ║ └╥┘┌─┐",
                "q_2: |0>─╫──╫─┤M├",
                "         ║  ║ └╥┘",
                " c_0: 0 ═╩══╬══╬═",
                "            ║  ║ ",
                " c_1: 0 ════╩══╬═",
                "               ║ ",
                " c_2: 0 ═══════╩═",
                "                 ",
            ]
        )

        qr = QuantumRegister(3, "q")
        cr = ClassicalRegister(3, "c")
        circuit = QuantumCircuit(qr, cr)
        circuit.measure(qr, cr)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_measure_1_reverse_bits(self):
        """ The measure operator, using 3-bit-length registers, with reverse_bits """
        expected = "\n".join(
            [
                "              ┌─┐",
                "q_2: |0>──────┤M├",
                "           ┌─┐└╥┘",
                "q_1: |0>───┤M├─╫─",
                "        ┌─┐└╥┘ ║ ",
                "q_0: |0>┤M├─╫──╫─",
                "        └╥┘ ║  ║ ",
                " c_2: 0 ═╬══╬══╩═",
                "         ║  ║    ",
                " c_1: 0 ═╬══╩════",
                "         ║       ",
                " c_0: 0 ═╩═══════",
                "                 ",
            ]
        )

        qr = QuantumRegister(3, "q")
        cr = ClassicalRegister(3, "c")
        circuit = QuantumCircuit(qr, cr)
        circuit.measure(qr, cr)
        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_text_measure_2(self):
        """ The measure operator, using some registers. """
        expected = "\n".join(
            [
                "               ",
                "q1_0: |0>──────",
                "               ",
                "q1_1: |0>──────",
                "         ┌─┐   ",
                "q2_0: |0>┤M├───",
                "         └╥┘┌─┐",
                "q2_1: |0>─╫─┤M├",
                "          ║ └╥┘",
                " c1_0: 0 ═╬══╬═",
                "          ║  ║ ",
                " c1_1: 0 ═╬══╬═",
                "          ║  ║ ",
                " c2_0: 0 ═╩══╬═",
                "             ║ ",
                " c2_1: 0 ════╩═",
                "               ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        qr2 = QuantumRegister(2, "q2")
        cr2 = ClassicalRegister(2, "c2")
        circuit = QuantumCircuit(qr1, qr2, cr1, cr2)
        circuit.measure(qr2, cr2)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_measure_2_reverse_bits(self):
        """ The measure operator, using some registers, with reverse_bits """
        expected = "\n".join(
            [
                "            ┌─┐",
                "q2_1: |0>───┤M├",
                "         ┌─┐└╥┘",
                "q2_0: |0>┤M├─╫─",
                "         └╥┘ ║ ",
                "q1_1: |0>─╫──╫─",
                "          ║  ║ ",
                "q1_0: |0>─╫──╫─",
                "          ║  ║ ",
                " c2_1: 0 ═╬══╩═",
                "          ║    ",
                " c2_0: 0 ═╩════",
                "               ",
                " c1_1: 0 ══════",
                "               ",
                " c1_0: 0 ══════",
                "               ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        qr2 = QuantumRegister(2, "q2")
        cr2 = ClassicalRegister(2, "c2")
        circuit = QuantumCircuit(qr1, qr2, cr1, cr2)
        circuit.measure(qr2, cr2)
        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_text_swap(self):
        """ Swap drawing. """
        expected = "\n".join(
            [
                "               ",
                "q1_0: |0>─X────",
                "          │    ",
                "q1_1: |0>─┼──X─",
                "          │  │ ",
                "q2_0: |0>─X──┼─",
                "             │ ",
                "q2_1: |0>────X─",
                "               ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.swap(qr1, qr2)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_swap_reverse_bits(self):
        """ Swap drawing with reverse_bits. """
        expected = "\n".join(
            [
                "               ",
                "q2_1: |0>────X─",
                "             │ ",
                "q2_0: |0>─X──┼─",
                "          │  │ ",
                "q1_1: |0>─┼──X─",
                "          │    ",
                "q1_0: |0>─X────",
                "               ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.swap(qr1, qr2)
        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_text_cswap(self):
        """ CSwap drawing. """
        expected = "\n".join(
            [
                "                 ",
                "q_0: |0>─■──X──X─",
                "         │  │  │ ",
                "q_1: |0>─X──■──X─",
                "         │  │  │ ",
                "q_2: |0>─X──X──■─",
                "                 ",
            ]
        )

        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cswap(qr[0], qr[1], qr[2])
        circuit.cswap(qr[1], qr[0], qr[2])
        circuit.cswap(qr[2], qr[1], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cswap_reverse_bits(self):
        """ CSwap drawing with reverse_bits. """
        expected = "\n".join(
            [
                "                 ",
                "q_2: |0>─X──X──■─",
                "         │  │  │ ",
                "q_1: |0>─X──■──X─",
                "         │  │  │ ",
                "q_0: |0>─■──X──X─",
                "                 ",
            ]
        )

        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cswap(qr[0], qr[1], qr[2])
        circuit.cswap(qr[1], qr[0], qr[2])
        circuit.cswap(qr[2], qr[1], qr[0])
        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_text_cu3(self):
        """ cu3 drawing. """
        expected = "\n".join(
            [
                "                                    ┌──────────────────────────┐",
                "q_0: |0>─────────────■──────────────┤ U3(1.5708,1.5708,1.5708) ├",
                "        ┌────────────┴─────────────┐└────────────┬─────────────┘",
                "q_1: |0>┤ U3(1.5708,1.5708,1.5708) ├─────────────┼──────────────",
                "        └──────────────────────────┘             │              ",
                "q_2: |0>─────────────────────────────────────────■──────────────",
                "                                                                ",
            ]
        )

        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cu3(pi / 2, pi / 2, pi / 2, qr[0], qr[1])
        circuit.cu3(pi / 2, pi / 2, pi / 2, qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cu3_reverse_bits(self):
        """ cu3 drawing with reverse_bits"""
        expected = "\n".join(
            [
                "                                                                ",
                "q_2: |0>─────────────────────────────────────────■──────────────",
                "        ┌──────────────────────────┐             │              ",
                "q_1: |0>┤ U3(1.5708,1.5708,1.5708) ├─────────────┼──────────────",
                "        └────────────┬─────────────┘┌────────────┴─────────────┐",
                "q_0: |0>─────────────■──────────────┤ U3(1.5708,1.5708,1.5708) ├",
                "                                    └──────────────────────────┘",
            ]
        )

        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cu3(pi / 2, pi / 2, pi / 2, qr[0], qr[1])
        circuit.cu3(pi / 2, pi / 2, pi / 2, qr[2], qr[0])
        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_text_crz(self):
        """ crz drawing. """
        expected = "\n".join(
            [
                "                      ┌────────────┐",
                "q_0: |0>──────■───────┤ Rz(1.5708) ├",
                "        ┌─────┴──────┐└─────┬──────┘",
                "q_1: |0>┤ Rz(1.5708) ├──────┼───────",
                "        └────────────┘      │       ",
                "q_2: |0>────────────────────■───────",
                "                                    ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.crz(pi / 2, qr[0], qr[1])
        circuit.crz(pi / 2, qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cx(self):
        """ cx drawing. """
        expected = "\n".join(
            [
                "             ┌───┐",
                "q_0: |0>──■──┤ X ├",
                "        ┌─┴─┐└─┬─┘",
                "q_1: |0>┤ X ├──┼──",
                "        └───┘  │  ",
                "q_2: |0>───────■──",
                "                  ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cx(qr[0], qr[1])
        circuit.cx(qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cy(self):
        """ cy drawing. """
        expected = "\n".join(
            [
                "             ┌───┐",
                "q_0: |0>──■──┤ Y ├",
                "        ┌─┴─┐└─┬─┘",
                "q_1: |0>┤ Y ├──┼──",
                "        └───┘  │  ",
                "q_2: |0>───────■──",
                "                  ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cy(qr[0], qr[1])
        circuit.cy(qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cz(self):
        """ cz drawing. """
        expected = "\n".join(
            [
                "              ",
                "q_0: |0>─■──■─",
                "         │  │ ",
                "q_1: |0>─■──┼─",
                "            │ ",
                "q_2: |0>────■─",
                "              ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cz(qr[0], qr[1])
        circuit.cz(qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_ch(self):
        """ ch drawing. """
        expected = "\n".join(
            [
                "             ┌───┐",
                "q_0: |0>──■──┤ H ├",
                "        ┌─┴─┐└─┬─┘",
                "q_1: |0>┤ H ├──┼──",
                "        └───┘  │  ",
                "q_2: |0>───────■──",
                "                  ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.ch(qr[0], qr[1])
        circuit.ch(qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_rzz(self):
        """ rzz drawing. See #1957 """
        expected = "\n".join(
            [
                "                             ",
                "q_0: |0>─■───────────────────",
                "         │zz(0)              ",
                "q_1: |0>─■───────■───────────",
                "                 │zz(1.5708) ",
                "q_2: |0>─────────■───────────",
                "                             ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.rzz(0, qr[0], qr[1])
        circuit.rzz(pi / 2, qr[2], qr[1])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cu1(self):
        """ cu1 drawing. """
        expected = "\n".join(
            [
                "                          ",
                "q_0: |0>─■────────■───────",
                "         │1.5708  │       ",
                "q_1: |0>─■────────┼───────",
                "                  │1.5708 ",
                "q_2: |0>──────────■───────",
                "                          ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cu1(pi / 2, qr[0], qr[1])
        circuit.cu1(pi / 2, qr[2], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_cu1_reverse_bits(self):
        """ cu1 drawing with reverse_bits"""
        expected = "\n".join(
            [
                "                          ",
                "q_2: |0>──────────■───────",
                "                  │       ",
                "q_1: |0>─■────────┼───────",
                "         │1.5708  │1.5708 ",
                "q_0: |0>─■────────■───────",
                "                          ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.cu1(pi / 2, qr[0], qr[1])
        circuit.cu1(pi / 2, qr[2], qr[0])
        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_text_ccx(self):
        """ cx drawing. """
        expected = "\n".join(
            [
                "                  ┌───┐",
                "q_0: |0>──■────■──┤ X ├",
                "          │  ┌─┴─┐└─┬─┘",
                "q_1: |0>──■──┤ X ├──■──",
                "        ┌─┴─┐└─┬─┘  │  ",
                "q_2: |0>┤ X ├──■────■──",
                "        └───┘          ",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.ccx(qr[0], qr[1], qr[2])
        circuit.ccx(qr[2], qr[0], qr[1])
        circuit.ccx(qr[2], qr[1], qr[0])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_reset(self):
        """ Reset drawing. """
        expected = "\n".join(
            [
                "              ",
                "q1_0: |0>─|0>─",
                "              ",
                "q1_1: |0>─|0>─",
                "              ",
                "q2_0: |0>─────",
                "              ",
                "q2_1: |0>─|0>─",
                "              ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.reset(qr1)
        circuit.reset(qr2[1])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_single_gate(self):
        """ Single Qbit gate drawing. """
        expected = "\n".join(
            [
                "         ┌───┐",
                "q1_0: |0>┤ H ├",
                "         ├───┤",
                "q1_1: |0>┤ H ├",
                "         └───┘",
                "q2_0: |0>─────",
                "         ┌───┐",
                "q2_1: |0>┤ H ├",
                "         └───┘",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.h(qr1)
        circuit.h(qr2[1])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_barrier(self):
        """ Barrier drawing. """
        expected = "\n".join(
            [
                "          ░ ",
                "q1_0: |0>─░─",
                "          ░ ",
                "q1_1: |0>─░─",
                "          ░ ",
                "q2_0: |0>───",
                "          ░ ",
                "q2_1: |0>─░─",
                "          ░ ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.barrier(qr1)
        circuit.barrier(qr2[1])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_no_barriers(self):
        """ Drawing without plotbarriers. """
        expected = "\n".join(
            [
                "         ┌───┐     ",
                "q1_0: |0>┤ H ├─────",
                "         ├───┤     ",
                "q1_1: |0>┤ H ├─────",
                "         ├───┤     ",
                "q2_0: |0>┤ H ├─────",
                "         └───┘┌───┐",
                "q2_1: |0>─────┤ H ├",
                "              └───┘",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.h(qr1)
        circuit.barrier(qr1)
        circuit.barrier(qr2[1])
        circuit.h(qr2)
        self.assertEqual(
            str(_text_circuit_drawer(circuit, plotbarriers=False)), expected
        )

    def test_text_measure_html(self):
        """ The measure operator. HTML representation. """
        expected = "\n".join(
            [
                '<pre style="word-wrap: normal;'
                'white-space: pre;line-height: 15px;">        ┌─┐',
                "q_0: |0>┤M├",
                "        └╥┘",
                " c_0: 0 ═╩═",
                "           </pre>",
            ]
        )
        qr = QuantumRegister(1, "q")
        cr = ClassicalRegister(1, "c")
        circuit = QuantumCircuit(qr, cr)
        circuit.measure(qr, cr)
        self.assertEqual(_text_circuit_drawer(circuit)._repr_html_(), expected)

    def test_text_justify_left(self):
        """ Drawing with left justify """
        expected = "\n".join(
            [
                "         ┌───┐   ",
                "q1_0: |0>┤ X ├───",
                "         ├───┤┌─┐",
                "q1_1: |0>┤ H ├┤M├",
                "         └───┘└╥┘",
                " c1_0: 0 ══════╬═",
                "               ║ ",
                " c1_1: 0 ══════╩═",
                "                 ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        circuit = QuantumCircuit(qr1, cr1)
        circuit.x(qr1[0])
        circuit.h(qr1[1])
        circuit.measure(qr1[1], cr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="left")), expected)

    def test_text_justify_right(self):
        """ Drawing with right justify """
        expected = "\n".join(
            [
                "              ┌───┐",
                "q1_0: |0>─────┤ X ├",
                "         ┌───┐└┬─┬┘",
                "q1_1: |0>┤ H ├─┤M├─",
                "         └───┘ └╥┘ ",
                " c1_0: 0 ═══════╬══",
                "                ║  ",
                " c1_1: 0 ═══════╩══",
                "                   ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        circuit = QuantumCircuit(qr1, cr1)
        circuit.x(qr1[0])
        circuit.h(qr1[1])
        circuit.measure(qr1[1], cr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="right")), expected)

    def test_text_justify_none(self):
        """ Drawing with none justify """
        expected = "\n".join(
            [
                "         ┌───┐        ",
                "q1_0: |0>┤ X ├────────",
                "         └───┘┌───┐┌─┐",
                "q1_1: |0>─────┤ H ├┤M├",
                "              └───┘└╥┘",
                " c1_0: 0 ═══════════╬═",
                "                    ║ ",
                " c1_1: 0 ═══════════╩═",
                "                      ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        circuit = QuantumCircuit(qr1, cr1)
        circuit.x(qr1[0])
        circuit.h(qr1[1])
        circuit.measure(qr1[1], cr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="none")), expected)

    def test_text_justify_left_barrier(self):
        """ Left justify respects barriers"""
        expected = "\n".join(
            [
                "         ┌───┐ ░      ",
                "q1_0: |0>┤ H ├─░──────",
                "         └───┘ ░ ┌───┐",
                "q1_1: |0>──────░─┤ H ├",
                "               ░ └───┘",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        circuit = QuantumCircuit(qr1)
        circuit.h(qr1[0])
        circuit.barrier(qr1)
        circuit.h(qr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="left")), expected)

    def test_text_justify_right_barrier(self):
        """ Right justify respects barriers """
        expected = "\n".join(
            [
                "         ┌───┐ ░      ",
                "q1_0: |0>┤ H ├─░──────",
                "         └───┘ ░ ┌───┐",
                "q1_1: |0>──────░─┤ H ├",
                "               ░ └───┘",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        circuit = QuantumCircuit(qr1)
        circuit.h(qr1[0])
        circuit.barrier(qr1)
        circuit.h(qr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="right")), expected)

    def test_text_overlap_cx(self):
        """ Overlapping CX gates are drawn not overlapping"""
        expected = "\n".join(
            [
                "                   ",
                "q1_0: |0>──■───────",
                "           │       ",
                "q1_1: |0>──┼────■──",
                "           │  ┌─┴─┐",
                "q1_2: |0>──┼──┤ X ├",
                "         ┌─┴─┐└───┘",
                "q1_3: |0>┤ X ├─────",
                "         └───┘     ",
            ]
        )

        qr1 = QuantumRegister(4, "q1")
        circuit = QuantumCircuit(qr1)
        circuit.cx(qr1[0], qr1[3])
        circuit.cx(qr1[1], qr1[2])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="left")), expected)

    def test_text_overlap_measure(self):
        """ Measure is drawn not overlapping"""
        expected = "\n".join(
            [
                "         ┌─┐     ",
                "q1_0: |0>┤M├─────",
                "         └╥┘┌───┐",
                "q1_1: |0>─╫─┤ X ├",
                "          ║ └───┘",
                " c1_0: 0 ═╩══════",
                "                 ",
                " c1_1: 0 ════════",
                "                 ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        circuit = QuantumCircuit(qr1, cr1)
        circuit.measure(qr1[0], cr1[0])
        circuit.x(qr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="left")), expected)

    def test_text_overlap_swap(self):
        """ Swap is drawn in 2 separate columns"""
        expected = "\n".join(
            [
                "               ",
                "q1_0: |0>─X────",
                "          │    ",
                "q1_1: |0>─┼──X─",
                "          │  │ ",
                "q2_0: |0>─X──┼─",
                "             │ ",
                "q2_1: |0>────X─",
                "               ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        qr2 = QuantumRegister(2, "q2")
        circuit = QuantumCircuit(qr1, qr2)
        circuit.swap(qr1, qr2)
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="left")), expected)

    def test_text_justify_right_measure_resize(self):
        """ Measure gate can resize if necessary"""
        expected = "\n".join(
            [
                "         ┌───┐",
                "q1_0: |0>┤ X ├",
                "         └┬─┬┘",
                "q1_1: |0>─┤M├─",
                "          └╥┘ ",
                " c1_0: 0 ══╬══",
                "           ║  ",
                " c1_1: 0 ══╩══",
                "              ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        circuit = QuantumCircuit(qr1, cr1)
        circuit.x(qr1[0])
        circuit.measure(qr1[1], cr1[1])
        self.assertEqual(str(_text_circuit_drawer(circuit, justify="right")), expected)

    def test_text_box_length(self):
        """The length of boxes is independent of other boxes in the layer
        https://github.com/Qiskit/qiskit-terra/issues/1882"""
        expected = "\n".join(
            [
                "             ┌───┐    ┌───┐",
                "q1_0: |0>────┤ H ├────┤ H ├",
                "             └───┘    └───┘",
                "q1_1: |0>──────────────────",
                "         ┌───────────┐     ",
                "q1_2: |0>┤ U1(1e-07) ├─────",
                "         └───────────┘     ",
            ]
        )

        qr = QuantumRegister(3, "q1")
        circuit = QuantumCircuit(qr)
        circuit.h(qr[0])
        circuit.h(qr[0])
        circuit.u1(0.0000001, qr[2])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_spacing_2378(self):
        """Small gates in the same layer as long gates.
        See https://github.com/Qiskit/qiskit-terra/issues/2378"""
        expected = "\n".join(
            [
                "                     ",
                "q_0: |0>──────X──────",
                "              │      ",
                "q_1: |0>──────X──────",
                "        ┌───────────┐",
                "q_2: |0>┤ Rz(11111) ├",
                "        └───────────┘",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)
        circuit.swap(qr[0], qr[1])
        circuit.rz(11111, qr[2])
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)


class TestTextDrawerMultiQGates(QiskitTestCase):
    """ Gates impling multiple qubits."""

    def test_2Qgate(self):
        """ 2Q no params. """
        expected = "\n".join(
            [
                "        ┌───────┐",
                "q_1: |0>┤1      ├",
                "        │  twoQ │",
                "q_0: |0>┤0      ├",
                "        └───────┘",
            ]
        )

        qr = QuantumRegister(2, "q")
        circuit = QuantumCircuit(qr)

        my_gate2 = Gate(name="twoQ", num_qubits=2, params=[])
        circuit.append(my_gate2, [qr[0], qr[1]])

        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_2Qgate_cross_wires(self):
        """ 2Q no params, with cross wires """
        expected = "\n".join(
            [
                "        ┌───────┐",
                "q_1: |0>┤0      ├",
                "        │  twoQ │",
                "q_0: |0>┤1      ├",
                "        └───────┘",
            ]
        )

        qr = QuantumRegister(2, "q")
        circuit = QuantumCircuit(qr)

        my_gate2 = Gate(name="twoQ", num_qubits=2, params=[])
        circuit.append(my_gate2, [qr[1], qr[0]])

        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_3Qgate_cross_wires(self):
        """ 3Q no params, with cross wires """
        expected = "\n".join(
            [
                "        ┌─────────┐",
                "q_2: |0>┤1        ├",
                "        │         │",
                "q_1: |0>┤0 threeQ ├",
                "        │         │",
                "q_0: |0>┤2        ├",
                "        └─────────┘",
            ]
        )

        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)

        my_gate3 = Gate(name="threeQ", num_qubits=3, params=[])
        circuit.append(my_gate3, [qr[1], qr[2], qr[0]])

        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_2Qgate_nottogether(self):
        """ 2Q that are not together """
        expected = "\n".join(
            [
                "        ┌───────┐",
                "q_2: |0>┤1      ├",
                "        │       │",
                "q_1: |0>┤  twoQ ├",
                "        │       │",
                "q_0: |0>┤0      ├",
                "        └───────┘",
            ]
        )
        qr = QuantumRegister(3, "q")
        circuit = QuantumCircuit(qr)

        my_gate2 = Gate(name="twoQ", num_qubits=2, params=[])
        circuit.append(my_gate2, [qr[0], qr[2]])

        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_2Qgate_nottogether_across_4(self):
        """ 2Q that are 2 bits apart"""
        expected = "\n".join(
            [
                "        ┌───────┐",
                "q_3: |0>┤1      ├",
                "        │       │",
                "q_2: |0>┤       ├",
                "        │  twoQ │",
                "q_1: |0>┤       ├",
                "        │       │",
                "q_0: |0>┤0      ├",
                "        └───────┘",
            ]
        )

        qr = QuantumRegister(4, "q")
        circuit = QuantumCircuit(qr)

        my_gate2 = Gate(name="twoQ", num_qubits=2, params=[])
        circuit.append(my_gate2, [qr[0], qr[3]])

        self.assertEqual(
            str(_text_circuit_drawer(circuit, reverse_bits=True)), expected
        )

    def test_unitary_nottogether_across_4(self):
        """ Unitary that are 2 bits apart"""
        expected = "\n".join(
            [
                "        ┌──────────┐",
                "q_0: |0>┤0         ├",
                "        │          │",
                "q_1: |0>┤          ├",
                "        │  unitary │",
                "q_2: |0>┤          ├",
                "        │          │",
                "q_3: |0>┤1         ├",
                "        └──────────┘",
            ]
        )

        qr = QuantumRegister(4, "q")
        qc = QuantumCircuit(qr)

        qc.append(random_unitary(4, seed=42), [qr[0], qr[3]])

        self.assertEqual(str(_text_circuit_drawer(qc)), expected)

    def test_kraus(self):
        """ Test Kraus.
        See https://github.com/Qiskit/qiskit-terra/pull/2238#issuecomment-487630014"""
        expected = "\n".join(
            ["        ┌───────┐", "q_0: |0>┤ Kraus ├", "        └───────┘"]
        )

        error = SuperOp(0.75 * numpy.eye(4) + 0.25 * numpy.diag([1, -1, -1, 1]))
        qr = QuantumRegister(1, name="q")
        qc = QuantumCircuit(qr)
        qc.append(error, [qr[0]])

        self.assertEqual(str(_text_circuit_drawer(qc)), expected)

    def test_multiplexer(self):
        """ Test Multiplexer.
        See https://github.com/Qiskit/qiskit-terra/pull/2238#issuecomment-487630014"""
        expected = "\n".join(
            [
                "        ┌──────────────┐",
                "q_0: |0>┤0             ├",
                "        │  multiplexer │",
                "q_1: |0>┤1             ├",
                "        └──────────────┘",
            ]
        )

        cx_multiplexer = Gate(
            "multiplexer", 2, [numpy.eye(2), numpy.array([[0, 1], [1, 0]])]
        )

        qr = QuantumRegister(2, name="q")
        qc = QuantumCircuit(qr)
        qc.append(cx_multiplexer, [qr[0], qr[1]])

        self.assertEqual(str(_text_circuit_drawer(qc)), expected)


class TestTextDrawerParams(QiskitTestCase):
    """Test drawing parameters."""

    def test_text_parameters_mix(self):
        """ cu3 drawing with parameters"""
        expected = "\n".join(
            [
                "                                   ",
                "q_0: |0>─────────────■─────────────",
                "        ┌────────────┴────────────┐",
                "q_1: |0>┤ U3(1.5708,theta,3.1416) ├",
                "        └─────────────────────────┘",
            ]
        )

        qr = QuantumRegister(2, "q")
        circuit = QuantumCircuit(qr)
        circuit.cu3(pi / 2, Parameter("theta"), pi, qr[0], qr[1])

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_sympy_constant(self):
        """ cu3 drawing with sympy pi"""
        expected = "\n".join(
            [
                "                              ",
                "q_0: |0>──────────■───────────",
                "        ┌─────────┴──────────┐",
                "q_1: |0>┤ U3(1.5708,pi/2,pi) ├",
                "        └────────────────────┘",
            ]
        )

        qr = QuantumRegister(2, "q")
        circuit = QuantumCircuit(qr)
        circuit.cu3(pi / 2, sympy.pi / 2, sympy.pi, qr[0], qr[1])

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)


class TestTextDrawerVerticalCompressionLow(QiskitTestCase):
    """Test vertical_compression='low' """

    def test_text_conditional_1(self):
        """ Conditional drawing with 1-bit-length regs."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[1];
        creg c1[1];
        if(c0==1) x q[0];
        if(c1==1) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "         └─┬─┘  └─┬─┘ ",
                "        ┌──┴──┐   │   ",
                "c0_0: 0 ╡ = 1 ╞═══╪═══",
                "        └─────┘   │   ",
                "               ┌──┴──┐",
                "c1_0: 0 ═══════╡ = 1 ╞",
                "               └─────┘",
            ]
        )

        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(
            str(_text_circuit_drawer(circuit, vertical_compression="low")), expected
        )

    def test_text_justify_right(self):
        """ Drawing with right justify """
        expected = "\n".join(
            [
                "              ┌───┐",
                "q1_0: |0>─────┤ X ├",
                "              └───┘",
                "         ┌───┐ ┌─┐ ",
                "q1_1: |0>┤ H ├─┤M├─",
                "         └───┘ └╥┘ ",
                "                ║  ",
                " c1_0: 0 ═══════╬══",
                "                ║  ",
                "                ║  ",
                " c1_1: 0 ═══════╩══",
                "                   ",
            ]
        )

        qr1 = QuantumRegister(2, "q1")
        cr1 = ClassicalRegister(2, "c1")
        circuit = QuantumCircuit(qr1, cr1)
        circuit.x(qr1[0])
        circuit.h(qr1[1])
        circuit.measure(qr1[1], cr1[1])
        self.assertEqual(
            str(
                _text_circuit_drawer(
                    circuit, justify="right", vertical_compression="low"
                )
            ),
            expected,
        )


class TestTextDrawerVerticalCompressionMedium(QiskitTestCase):
    """Test vertical_compression='medium' """

    def test_text_conditional_1(self):
        """ Medium vertical compression avoids box overlap."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[1];
        creg c1[1];
        if(c0==1) x q[0];
        if(c1==1) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "         └─┬─┘  └─┬─┘ ",
                "        ┌──┴──┐   │   ",
                "c0_0: 0 ╡ = 1 ╞═══╪═══",
                "        └─────┘┌──┴──┐",
                "c1_0: 0 ═══════╡ = 1 ╞",
                "               └─────┘",
            ]
        )

        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(
            str(_text_circuit_drawer(circuit, vertical_compression="medium")), expected
        )


class TestTextConditional(QiskitTestCase):
    """Gates with conditionals"""

    def test_text_conditional_1(self):
        """ Conditional drawing with 1-bit-length regs."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[1];
        creg c1[1];
        if(c0==1) x q[0];
        if(c1==1) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "        ┌┴─┴─┴┐ └─┬─┘ ",
                "c0_0: 0 ╡ = 1 ╞═══╪═══",
                "        └─────┘┌──┴──┐",
                "c1_0: 0 ═══════╡ = 1 ╞",
                "               └─────┘",
            ]
        )

        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_2(self):
        """ Conditional drawing with 2-bit-length regs."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[2];
        creg c1[2];
        if(c0==2) x q[0];
        if(c1==2) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "        ┌┴─┴─┴┐ └─┬─┘ ",
                "c0_0: 0 ╡     ╞═══╪═══",
                "        │ = 2 │   │   ",
                "c0_1: 0 ╡     ╞═══╪═══",
                "        └─────┘┌──┴──┐",
                "c1_0: 0 ═══════╡     ╞",
                "               │ = 2 │",
                "c1_1: 0 ═══════╡     ╞",
                "               └─────┘",
            ]
        )
        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_3(self):
        """ Conditional drawing with 3-bit-length regs."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[3];
        creg c1[3];
        if(c0==3) x q[0];
        if(c1==3) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "        ┌┴─┴─┴┐ └─┬─┘ ",
                "c0_0: 0 ╡     ╞═══╪═══",
                "        │     │   │   ",
                "c0_1: 0 ╡ = 3 ╞═══╪═══",
                "        │     │   │   ",
                "c0_2: 0 ╡     ╞═══╪═══",
                "        └─────┘┌──┴──┐",
                "c1_0: 0 ═══════╡     ╞",
                "               │     │",
                "c1_1: 0 ═══════╡ = 3 ╞",
                "               │     │",
                "c1_2: 0 ═══════╡     ╞",
                "               └─────┘",
            ]
        )
        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_4(self):
        """ Conditional drawing with 4-bit-length regs."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[4];
        creg c1[4];
        if(c0==4) x q[0];
        if(c1==4) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "        ┌┴─┴─┴┐ └─┬─┘ ",
                "c0_0: 0 ╡     ╞═══╪═══",
                "        │     │   │   ",
                "c0_1: 0 ╡     ╞═══╪═══",
                "        │ = 4 │   │   ",
                "c0_2: 0 ╡     ╞═══╪═══",
                "        │     │   │   ",
                "c0_3: 0 ╡     ╞═══╪═══",
                "        └─────┘┌──┴──┐",
                "c1_0: 0 ═══════╡     ╞",
                "               │     │",
                "c1_1: 0 ═══════╡     ╞",
                "               │ = 4 │",
                "c1_2: 0 ═══════╡     ╞",
                "               │     │",
                "c1_3: 0 ═══════╡     ╞",
                "               └─────┘",
            ]
        )
        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_5(self):
        """ Conditional drawing with 5-bit-length regs."""
        qasm_string = """
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[1];
        creg c0[5];
        creg c1[5];
        if(c0==5) x q[0];
        if(c1==5) x q[0];
        """
        expected = "\n".join(
            [
                "         ┌───┐  ┌───┐ ",
                "q_0: |0>─┤ X ├──┤ X ├─",
                "        ┌┴─┴─┴┐ └─┬─┘ ",
                "c0_0: 0 ╡     ╞═══╪═══",
                "        │     │   │   ",
                "c0_1: 0 ╡     ╞═══╪═══",
                "        │     │   │   ",
                "c0_2: 0 ╡ = 5 ╞═══╪═══",
                "        │     │   │   ",
                "c0_3: 0 ╡     ╞═══╪═══",
                "        │     │   │   ",
                "c0_4: 0 ╡     ╞═══╪═══",
                "        └─────┘┌──┴──┐",
                "c1_0: 0 ═══════╡     ╞",
                "               │     │",
                "c1_1: 0 ═══════╡     ╞",
                "               │     │",
                "c1_2: 0 ═══════╡ = 5 ╞",
                "               │     │",
                "c1_3: 0 ═══════╡     ╞",
                "               │     │",
                "c1_4: 0 ═══════╡     ╞",
                "               └─────┘",
            ]
        )
        circuit = QuantumCircuit.from_qasm_str(qasm_string)
        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cz_no_space(self):
        """Conditional CZ without space"""
        qr = QuantumRegister(2, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cz(qr[0], qr[1]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───■───",
                "            │   ",
                "qr_1: |0>───■───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cz(self):
        """Conditional CZ with a wire in the middle"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cz(qr[0], qr[1]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───■───",
                "            │   ",
                "qr_1: |0>───■───",
                "            │   ",
                "qr_2: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cx_ct(self):
        """Conditional CX (control-target) with a wire in the middle"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cx(qr[0], qr[1]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───■───",
                "          ┌─┴─┐ ",
                "qr_1: |0>─┤ X ├─",
                "          └─┬─┘ ",
                "qr_2: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cx_tc(self):
        """Conditional CX (target-control) with a wire in the middle"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cx(qr[1], qr[0]).c_if(cr, 1)

        expected = "\n".join(
            [
                "          ┌───┐ ",
                "qr_0: |0>─┤ X ├─",
                "          └─┬─┘ ",
                "qr_1: |0>───■───",
                "            │   ",
                "qr_2: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cu3_ct(self):
        """Conditional Cu3 (control-target) with a wire in the middle"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cu3(pi / 2, pi / 2, pi / 2, qr[0], qr[1]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                                     ",
                "qr_0: |0>─────────────■──────────────",
                "         ┌────────────┴─────────────┐",
                "qr_1: |0>┤ U3(1.5708,1.5708,1.5708) ├",
                "         └────────────┬─────────────┘",
                "qr_2: |0>─────────────┼──────────────",
                "                   ┌──┴──┐           ",
                " cr_0: 0 ══════════╡ = 1 ╞═══════════",
                "                   └─────┘           ",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cu3_tc(self):
        """Conditional Cu3 (target-control) with a wire in the middle"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cu3(pi / 2, pi / 2, pi / 2, qr[1], qr[0]).c_if(cr, 1)

        expected = "\n".join(
            [
                "         ┌──────────────────────────┐",
                "qr_0: |0>┤ U3(1.5708,1.5708,1.5708) ├",
                "         └────────────┬─────────────┘",
                "qr_1: |0>─────────────■──────────────",
                "                      │              ",
                "qr_2: |0>─────────────┼──────────────",
                "                   ┌──┴──┐           ",
                " cr_0: 0 ══════════╡ = 1 ╞═══════════",
                "                   └─────┘           ",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_ccx(self):
        """Conditional CCX with a wire in the middle"""
        qr = QuantumRegister(4, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.ccx(qr[0], qr[1], qr[2]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───■───",
                "            │   ",
                "qr_1: |0>───■───",
                "          ┌─┴─┐ ",
                "qr_2: |0>─┤ X ├─",
                "          └─┬─┘ ",
                "qr_3: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_ccx_no_space(self):
        """Conditional CCX without space"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.ccx(qr[0], qr[1], qr[2]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───■───",
                "            │   ",
                "qr_1: |0>───■───",
                "          ┌─┴─┐ ",
                "qr_2: |0>─┤ X ├─",
                "         ┌┴─┴─┴┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_h(self):
        """Conditional H with a wire in the middle"""
        qr = QuantumRegister(2, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.h(qr[0]).c_if(cr, 1)

        expected = "\n".join(
            [
                "          ┌───┐ ",
                "qr_0: |0>─┤ H ├─",
                "          └─┬─┘ ",
                "qr_1: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_swap(self):
        """Conditional SWAP"""
        qr = QuantumRegister(3, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.swap(qr[0], qr[1]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───X───",
                "            │   ",
                "qr_1: |0>───X───",
                "            │   ",
                "qr_2: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_text_conditional_cswap(self):
        """Conditional CSwap """
        qr = QuantumRegister(4, "qr")
        cr = ClassicalRegister(1, "cr")
        circuit = QuantumCircuit(qr, cr)
        circuit.cswap(qr[0], qr[1], qr[2]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>───■───",
                "            │   ",
                "qr_1: |0>───X───",
                "            │   ",
                "qr_2: |0>───X───",
                "            │   ",
                "qr_3: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_conditional_reset(self):
        """ Reset drawing. """
        qr = QuantumRegister(2, "qr")
        cr = ClassicalRegister(1, "cr")

        circuit = QuantumCircuit(qr, cr)
        circuit.reset(qr[0]).c_if(cr, 1)

        expected = "\n".join(
            [
                "                ",
                "qr_0: |0>──|0>──",
                "            │   ",
                "qr_1: |0>───┼───",
                "         ┌──┴──┐",
                " cr_0: 0 ╡ = 1 ╞",
                "         └─────┘",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(circuit)), expected)

    def test_conditional_multiplexer(self):
        """ Test Multiplexer."""
        cx_multiplexer = Gate(
            "multiplexer", 2, [numpy.eye(2), numpy.array([[0, 1], [1, 0]])]
        )
        qr = QuantumRegister(3, name="qr")
        cr = ClassicalRegister(1, "cr")
        qc = QuantumCircuit(qr, cr)
        qc.append(cx_multiplexer.c_if(cr, 1), [qr[0], qr[1]])

        expected = "\n".join(
            [
                "         ┌──────────────┐",
                "qr_0: |0>┤0             ├",
                "         │  multiplexer │",
                "qr_1: |0>┤1             ├",
                "         └──────┬───────┘",
                "qr_2: |0>───────┼────────",
                "             ┌──┴──┐     ",
                " cr_0: 0 ════╡ = 1 ╞═════",
                "             └─────┘     ",
            ]
        )

        self.assertEqual(str(_text_circuit_drawer(qc)), expected)


if __name__ == "__main__":
    unittest.main()
