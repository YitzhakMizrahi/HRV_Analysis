# analysis_module/full_dataset.py

from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_sdnn


def analyze_full_dataset(ecg_data, sampling_rate):
    """
    Analyze the entire ECG dataset to compute HRV metrics.
    Parameters:
        ecg_data (list): The entire ECG dataset.
        sampling_rate (int): The number of samples per second.
    """
    try:
        r_peaks = detect_r_peaks(ecg_data, sampling_rate)
        rr_intervals = calculate_rr_intervals(r_peaks)
        sdnn = calculate_sdnn(rr_intervals)
        print(f"Full dataset HRV (SDNN): {sdnn:.2f} ms\n")
        print("-" * 30)
    except Exception as e:
        print(f"Error processing full dataset: {e}\n")
