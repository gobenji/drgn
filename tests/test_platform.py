import unittest

from drgn import Architecture, Platform, PlatformFlags


class TestPlatform(unittest.TestCase):
    def test_default_flags(self):
        Platform(Architecture.X86_64)
        self.assertRaises(ValueError, Platform, Architecture.UNKNOWN)

    def test_registers(self):
        self.assertIn(
            'rax',
            (reg.name for reg in Platform(Architecture.X86_64).registers))
        self.assertEqual(
            Platform(Architecture.UNKNOWN, PlatformFlags(0)).registers, ())
