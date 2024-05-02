# analysis_module/segment_analysis.py

from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_sdnn


def analyze_segment(segment, segment_number, start_time, end_time):
    """
    Analyze a specific segment of ECG data for HRV metrics.

    Parameters:
        segment (list): The ECG data segment to analyze.
        segment_number (int): The identifier number of the segment.
        start_time (float): The start time of the segment in seconds.
        end_time (float): The end time of the segment in seconds.
    """
    try:
        r_peaks = detect_r_peaks(segment, 200)  # Assuming fixed sampling rate
        rr_intervals = calculate_rr_intervals(r_peaks)
        sdnn = calculate_sdnn(rr_intervals)
        print(f"Segment {segment_number}:")
        print(f"Timeframe: {start_time:.2f} sec to {end_time:.2f} sec")
        print(f"HRV (SDNN): {sdnn:.2f} ms")
        print("-" * 30)
    except Exception as e:
        print(f"Error processing segment {segment_number}: {e}")
