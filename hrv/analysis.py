# hrv/analysis.py

import numpy as np
import scipy.signal as signal


def detect_r_peaks(ecg_data, sampling_rate=200):
    """
    Detect R-peaks in the ECG data.

    This function calculates the minimum distance between peaks based on the sampling rate
    and an assumed average heart rate. This minimum distance helps to avoid false positives
    in R-peak detection.

    :param ecg_data: List or numpy array of ECG data points as floats.
    :param sampling_rate: The sampling rate of the ECG data in Hz.
    :return: Array of indices where R-peaks are detected.
    :raises TypeError: If the ECG data is not a list or numpy array.
    :raises ValueError: If the ECG data is empty or too short for analysis.
    """
    if not isinstance(ecg_data, (list, np.ndarray)):
        raise TypeError("ECG data must be a list or numpy array of numbers.")

    if not ecg_data:
        raise ValueError("ECG data is empty.")

    if len(ecg_data) < sampling_rate:
        raise ValueError("ECG data is too short for reliable peak detection.")

    # The minimum distance between peaks is based on the expected distance at 60 bpm
    # for the given sampling rate, ensuring one peak per cardiac cycle at this rate.
    min_distance = sampling_rate  # for a heart rate of 60 bpm

    # Using scipy's find_peaks function to detect peaks with the specified minimum distance
    peaks, _ = signal.find_peaks(ecg_data, distance=min_distance)

    if len(peaks) == 0:
        raise ValueError("No peaks detected in the ECG data.")

    return peaks


def calculate_rr_intervals(peaks):
    """
    Calculate RR intervals from the detected R-peaks.

    :param peaks: Array of indices where R-peaks are detected.
    :return: List of RR intervals calculated from the R-peaks.
    """
    # Using list comprehension to calculate differences between successive peaks
    return [peaks[i] - peaks[i - 1] for i in range(1, len(peaks))]
