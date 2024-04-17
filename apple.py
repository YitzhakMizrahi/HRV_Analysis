import numpy as np
from hrv.metrics import (
    calculate_hrv,
    calculate_sdnn,
)  # Assuming these are already implemented


def test_apple_watch_data():
    # Datasets as tuples of (heart rates, reported HRV)
    datasets = [
        (
            np.array(
                [
                    74,
                    74,
                    73,
                    72,
                    72,
                    78,
                    74,
                    76,
                    74,
                    74,
                    75,
                    75,
                    75,
                    76,
                    76,
                    80,
                    78,
                    76,
                    77,
                    77,
                    76,
                    76,
                    75,
                    75,
                    78,
                    79,
                    83,
                    83,
                    85,
                    85,
                    82,
                    80,
                    75,
                    76,
                    78,
                    
                ]
            ),
            33,
        ),
        (
            np.array(
                [
                    75,
                    75,
                    73,
                    71,
                    72,
                    72,
                    67,
                    67,
                    66,
                    67,
                    68,
                    84,
                    83,
                    81,
                    80,
                    79,
                    76,
                    79,
                    78,
                    76,
                    74,
                    72,
                    70,
                    73,
                    75,
                ]
            ),
            54,
        ),
        (
            np.array(
                [
                    81,
                    85,
                    81,
                    83,
                    81,
                    80,
                    78,
                    78,
                    78,
                    81,
                    79,
                    77,
                    76,
                    75,
                    75,
                    78,
                    78,
                    78,
                    79,
                    80,
                    80,
                    79,
                    79,
                    78,
                    78,
                    81,
                    81,
                    81,
                    79,
                    76,
                    76,
                    77,
                    77,
                    80,
                    80,
                    78,
                    79,
                    76,
                    77,
                    76,
                    77,
                    79,
                    82,
                    79,
                    79,
                  
                ]
            ),
            20,
        ),
    ]

    for heart_rates, reported_hrv in datasets:
        # Convert heart rates to RR intervals in milliseconds
        rr_intervals = 60000 / heart_rates

        # Calculate HRV metrics
        calculated_rmssd = calculate_hrv(rr_intervals)
        calculated_sdnn = calculate_sdnn(rr_intervals)

        # Print results
        print(f"Heart Rates: {heart_rates}")
        print(f"Reported HRV: {reported_hrv} ms")
        print(f"Calculated HRV (RMSSD): {calculated_rmssd:.2f} ms")
        print(f"Calculated HRV (SDNN): {calculated_sdnn:.2f} ms")
        print("")


if __name__ == "__main__":
    test_apple_watch_data()
