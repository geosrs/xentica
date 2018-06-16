"""Tests for ``xentica.core.mixins`` module."""
import unittest

from xentica.core.mixins import BscaDetectorMixin
from xentica.core.exceptions import XenticaException


class TestBscaDetector(unittest.TestCase):
    """Tests for ``BscaDetectorMixin`` class."""

    def test_not_detected(self):
        """Test exception is raised if BSCA not detected."""
        class Dummy(BscaDetectorMixin):
            """Dummy class for BSCA detecting test."""
            @property
            def bsca(self):
                """Get BSCA class."""
                return self._bsca
        with self.assertRaises(XenticaException):
            dummy = Dummy()
            bsca = dummy.bsca
            self.assertEqual(bsca.__name__, "BSCA", "Wrong class detected.")
