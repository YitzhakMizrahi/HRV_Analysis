from hrv.reader import load_ecg_data
from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_hrv, calculate_sdnn, calculate_pnn50


def main():
    # Path to your ECG data file
    file_path = "data/EST2019201904_2020-03-17_15-22-25.txt"

    # Load the ECG data from the file
    ecg_data = load_ecg_data(file_path)

    # Detect R-peaks in the ECG data
    r_peaks = detect_r_peaks(ecg_data)

    # Calculate RR intervals from the R-peaks
    rr_intervals = calculate_rr_intervals(r_peaks)

    # Compute HRV metrics
    rmssd = calculate_hrv(rr_intervals)
    sdnn = calculate_sdnn(rr_intervals)
    pnn50 = calculate_pnn50(rr_intervals)

    # Print the HRV results
    print(f"HRV (RMSSD): {rmssd}")
    print(f"HRV (SDNN): {sdnn}")
    print(f"HRV (pNN50): {pnn50}")


if __name__ == "__main__":
    main()
