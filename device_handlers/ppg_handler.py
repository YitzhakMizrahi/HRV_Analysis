# device_handlers/ppg_handler.py

import numpy as np
from hrv.reader import load_ppg_data
from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_sdnn
from scipy.signal import find_peaks, medfilt


def process_ppg_data(file_path, file_name):
    """
    Process each channel in PPG data and display HRV metrics.
    """
    ppg_data = load_ppg_data(file_path)
    sampling_rate = 250 # Sample rate in Hz

    print(f"Processing file: {file_name}")
    print("-" * 30)

    for channel in ["red", "ir", "green", "ecg"]:
        if channel in ppg_data:
            channel_data_points = len(ppg_data[channel])
            total_duration_seconds = channel_data_points / sampling_rate
            minutes, seconds = divmod(total_duration_seconds, 60)

            print(f"{channel.capitalize()} Channel HRV Metrics:")
            print(f"Data points: {channel_data_points}")
            print(f"Total duration: {int(minutes)} minutes and {int(seconds)} seconds")

            try:
                analyze_full_dataset(ppg_data[channel], sampling_rate)
            except Exception as e:
                print(f"Error processing {channel} channel: {e}")
            print("-" * 30)


def analyze_full_dataset(channel_data, sampling_rate):
    """
    Analyze a channel to compute HRV metrics, including average heart rate.
    """
    try:
        # Apply a median filter for smoothing
        filtered_data = medfilt(channel_data, kernel_size=5)

        # Adjust peak detection parameters
        peaks, _ = find_peaks(filtered_data, distance=sampling_rate/2, prominence=0.1)

        rr_intervals = np.diff(peaks) * 1000 / sampling_rate  # Convert to milliseconds
        rr_intervals = rr_intervals[(rr_intervals > 300) & (rr_intervals < 2000)]  # Filter out unrealistic intervals

        if len(rr_intervals) > 1:
            average_rr = np.median(rr_intervals)
            average_heart_rate = 60000 / average_rr  # Convert RR interval to heart rate

            sdnn = calculate_sdnn(rr_intervals)
            print(f"HRV (SDNN): {sdnn:.2f} ms")
            print(f"Average Heart Rate: {average_heart_rate:.2f} bpm")
        else:
            print("Insufficient data for HRV and heart rate calculation.")
    except Exception as e:
        print(f"Error in analyzing full dataset: {e}")