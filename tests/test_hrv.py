import unittest
from hrv.reader import load_ecg_data
from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_hrv


class TestHRVFunctions(unittest.TestCase):

    def test_load_ecg_data(self):
        # This test might need a sample file with known content
        ecg_data = load_ecg_data("data/EST2019201904_2020-03-17_15-22-25.txt")
        self.assertIsInstance(ecg_data, list)
        self.assertTrue(all(isinstance(x, int) for x in ecg_data))

    def test_detect_r_peaks(self):
        # Provide a simple, known ECG-like signal for testing
        ecg_data = [0, 2, 1, 3, 1, 4, 1, 3, 1, 2, 1, 0]
        peaks = detect_r_peaks(ecg_data)
        self.assertEqual(peaks, [5])  # Assuming peak is at index 5

    def test_calculate_rr_intervals(self):
        # RR intervals from detected peaks indices
        rr_intervals = calculate_rr_intervals([100, 200, 300])
        self.assertEqual(rr_intervals, [100, 100])

    def test_calculate_hrv(self):
        # RMSSD from a known set of RR intervals
        rmssd = calculate_hrv([100, 100, 100, 100])
        self.assertEqual(rmssd, 0.0)  # RMSSD should be 0 for constant intervals


if __name__ == "__main__":
    unittest.main()
