import unittest
from hrv.reader import load_ecg_data
from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_hrv, calculate_sdnn, calculate_pnn50


class TestHRVFunctions(unittest.TestCase):

    def test_load_ecg_data(self):
        # Assuming 'data/test_ecg.txt' is a test file with known floating-point content
        ecg_data = load_ecg_data("data/EST2019201904_2020-03-17_15-22-25.txt")
        self.assertIsInstance(ecg_data, list)
        self.assertTrue(all(isinstance(x, float) for x in ecg_data))

    def test_detect_r_peaks(self):
        # Provide a simple, known ECG-like signal for testing
        ecg_data = [0.0, 2.0, 1.0, 3.0, 1.0, 4.0, 1.0, 3.0, 1.0, 2.0, 1.0, 0.0]
        peaks = detect_r_peaks(ecg_data)
        self.assertIn(5, peaks)  # Assuming peak at index 5 for this simple data

    def test_calculate_rr_intervals(self):
        # RR intervals from detected peaks indices
        rr_intervals = calculate_rr_intervals([100, 200, 300])
        self.assertEqual(rr_intervals, [100, 100])

    def test_calculate_hrv_metrics(self):
        # Using simple RR intervals for testing HRV calculations
        rr_intervals = [100, 150, 100, 150]
        rmssd = calculate_hrv(rr_intervals)
        sdnn = calculate_sdnn(rr_intervals)
        pnn50 = calculate_pnn50(rr_intervals)
        self.assertIsInstance(rmssd, float)
        self.assertIsInstance(sdnn, float)
        self.assertIsInstance(pnn50, float)


if __name__ == "__main__":
    unittest.main()
