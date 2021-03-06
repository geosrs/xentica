"""Tests for ``xentica.core.topology.lattice`` module."""
import unittest

from xentica.core.exceptions import XenticaException
from xentica.core.topology.lattice import (
    OrthogonalLattice,
)


class TestOrthogonalLattice(unittest.TestCase):
    """Tests for ``OrthogonalLattice`` class."""

    def test_incorrect_dimensions(self):
        """Test exception is raised for incorrect dimensionality."""
        lattice = OrthogonalLattice()
        with self.assertRaises(XenticaException):
            lattice.dimensions = 0
