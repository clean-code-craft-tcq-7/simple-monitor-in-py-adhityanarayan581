import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_temperature_too_high(self):
        self.assertFalse(vitals_ok(103, 80, 95))  # High temp

    def test_temperature_too_low(self):
        self.assertFalse(vitals_ok(94, 80, 95))   # Low temp

    def test_pulse_too_low(self):
        self.assertFalse(vitals_ok(98, 55, 95))   # Low pulse

    def test_pulse_too_high(self):
        self.assertFalse(vitals_ok(98, 105, 95))  # High pulse

    def test_spo2_too_low(self):
        self.assertFalse(vitals_ok(98, 80, 89))   # Low SpO2

    def test_all_vitals_normal(self):
        self.assertTrue(vitals_ok(98.6, 75, 96))  # All normal

    def test_first_vital_out_short_circuit(self):
        self.assertFalse(vitals_ok(103, 120, 85))


if __name__ == '__main__':
    unittest.main()
