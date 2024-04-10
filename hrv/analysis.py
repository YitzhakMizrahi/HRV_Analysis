import scipy.signal as signal


def detect_r_peaks(ecg_data):
    """
    Detect R-peaks in the ECG data.

    :param ecg_data: List of integers representing ECG data points.
    :return: Array of indices where R-peaks are detected.
    """
    # Assuming a minimum distance between peaks to avoid false positives
    peaks, _ = signal.find_peaks(ecg_data, distance=50)
    return peaks


def calculate_rr_intervals(peaks):
    """
    Calculate RR intervals from the detected R-peaks.

    :param peaks: Array of indices where R-peaks are detected.
    :return: List of RR intervals calculated from the R-peaks.
    """
    # Using list comprehension to calculate differences between successive peaks
    return [peaks[i] - peaks[i - 1] for i in range(1, len(peaks))]
