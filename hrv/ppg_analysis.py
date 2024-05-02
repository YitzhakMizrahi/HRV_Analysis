# hrv/ppg_analysis.py

import numpy as np
from scipy.signal import find_peaks
from hrv.metrics import calculate_sdnn


def process_ppg_channel(ppg_data, sampling_rate):
    """
    Process a single channel of PPG or ECG data to calculate HRV metrics.

    Parameters:
        ppg_data (list): Data points for a single channel.
        sampling_rate (int): The sampling rate of the data.

    Returns:
        dict: A dictionary containing HRV metrics for the channel.
    """
    try:
        peaks, _ = find_peaks(
            ppg_data, distance=sampling_rate / 2
        )  # or adjust this based on your data
        print(f"Number of peaks detected: {len(peaks)}")  # Diagnostic output

        if len(peaks) < 2:
            print("Not enough peaks for HRV calculation.")
            return {"sdnn": 0}  # Handle insufficient data

        intervals = np.diff(peaks) * 1000 / sampling_rate
        sdnn_value = calculate_sdnn(intervals)
        return {"sdnn": sdnn_value}
    except Exception as e:
        print(f"Error in process_ppg_channel: {e}")
        return {"sdnn": 0}


def analyze_ppg_data(ppg_data, sampling_rate):
    """
    Analyze all PPG and ECG channels of data to extract HRV metrics.

    Parameters:
        ppg_data (dict): Dictionary containing lists of data points for each channel, including ECG.
        sampling_rate (int): The sampling rate of the data.

    Returns:
        dict: A dictionary of HRV metrics for each channel.
    """
    results = {}
    for channel in [
        "red",
        "ir",
        "green",
        "ecg",
    ]:  # Including ECG along with PPG channels
        channel_data = ppg_data[channel]
        results[channel] = process_ppg_channel(channel_data, sampling_rate)
    return results
