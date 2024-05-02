# analysis_module/remaining_data.py

from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_sdnn


def analyze_remaining_data(remaining_segment, start_time, end_time):
    """
    Analyze any remaining ECG data that doesn't fit into the full segments.

    Parameters:
        remaining_segment (list): The leftover ECG data points.
        start_time (float): The start time of the remaining data in seconds.
        end_time (float): The end time of the remaining data in seconds.
    """
    try:
        r_peaks = detect_r_peaks(remaining_segment, 200)
        rr_intervals = calculate_rr_intervals(r_peaks)
        sdnn = calculate_sdnn(rr_intervals)
        print(f"Remaining Segment:")
        print(f"Timeframe: {start_time:.2f} sec to {end_time:.2f} sec")
        print(f"HRV (SDNN): {sdnn:.2f} ms")
        print("-" * 30)
    except Exception as e:
        print(f"Error processing remaining data: {e}")
