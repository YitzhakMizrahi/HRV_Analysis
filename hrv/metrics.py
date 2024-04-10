import numpy as np


def calculate_hrv(rr_intervals):
    """
    Calculate the Heart Rate Variability (HRV) based on RMSSD.

    :param rr_intervals: List of RR intervals.
    :return: The RMSSD value as a measure of HRV.
    """
    # Calculate the differences between successive RR intervals
    rr_diff = np.diff(rr_intervals)
    # Square the differences
    rr_diff_sq = rr_diff**2
    # Calculate the square root of the mean of the squared differences
    rmssd = np.sqrt(np.mean(rr_diff_sq))
    return rmssd


def calculate_sdnn(rr_intervals):
    """
    Calculate the Standard Deviation of NN intervals (SDNN).

    :param rr_intervals: List of RR intervals.
    :return: The SDNN value.
    """
    # Ensure there are enough intervals to calculate SDNN
    if len(rr_intervals) > 1:
        return np.std(rr_intervals, ddof=1)  # ddof=1 for sample standard deviation
    else:
        return 0  # SDNN is not meaningful for too few intervals


def calculate_pnn50(rr_intervals):
    """
    Calculate the percentage of successive RR intervals that differ by more than 50 ms.

    :param rr_intervals: List of RR intervals.
    :return: The pNN50 value as a percentage.
    """
    # Calculate differences between successive RR intervals
    rr_diff = np.diff(rr_intervals)
    # Count the number of intervals differing by more than 50 ms
    nn50 = np.sum(np.abs(rr_diff) > 50)
    # Calculate the percentage
    pnn50 = (nn50 / len(rr_intervals)) * 100 if rr_intervals else 0
    return pnn50
