import numpy as np


def calculate_hrv(rr_intervals):
    """
    Calculate the Heart Rate Variability (HRV) based on RMSSD.

    :param rr_intervals: List of RR intervals.
    :return: The RMSSD value as a measure of HRV.
    :raises ValueError: If less than two RR intervals are provided.
    """
    if len(rr_intervals) < 2:
        raise ValueError("At least two RR intervals are required to calculate RMSSD.")
    rr_diff = np.diff(rr_intervals)
    return np.sqrt(np.mean(rr_diff**2))


def calculate_sdnn(rr_intervals):
    """
    Calculate the Standard Deviation of NN intervals (SDNN).

    :param rr_intervals: List of RR intervals.
    :return: The SDNN value.
    :raises ValueError: If less than two RR intervals are provided.
    """
    if len(rr_intervals) < 2:
        raise ValueError("At least two RR intervals are required to calculate SDNN.")
    return np.std(rr_intervals, ddof=1)


def calculate_pnn50(rr_intervals):
    """
    Calculate the percentage of successive RR intervals that differ by more than 50 ms (pNN50).

    :param rr_intervals: List of RR intervals.
    :return: The pNN50 value as a percentage.
    :raises ValueError: If less than two RR intervals are provided.
    """
    if len(rr_intervals) < 2:
        raise ValueError("At least two RR intervals are required to calculate pNN50.")
    rr_diff = np.diff(rr_intervals)
    nn50 = np.sum(np.abs(rr_diff) > 50)
    pnn50 = (nn50 / len(rr_intervals)) * 100 if rr_intervals else 0
    return pnn50
