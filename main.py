import sys
from hrv.reader import load_ecg_data
from hrv.analysis import detect_r_peaks, calculate_rr_intervals
from hrv.metrics import calculate_hrv, calculate_sdnn, calculate_pnn50


def analyze_full_dataset(ecg_data, sampling_rate):
    """
    Analyze the entire ECG dataset to compute HRV metrics.

    Parameters:
        ecg_data (list): The entire ECG dataset.
        sampling_rate (int): The number of samples per second.
    """
    try:
        r_peaks = detect_r_peaks(ecg_data, sampling_rate)
        rr_intervals = calculate_rr_intervals(r_peaks)
        sdnn = calculate_sdnn(rr_intervals)
        print(f"Full dataset HRV (SDNN): {sdnn:.2f} ms\n")
        print("-" * 30)
    except Exception as e:
        print(f"Error processing full dataset: {e}\n")


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


def process_segments(ecg_data, sampling_rate=200):
    """
    Process the ECG data in segments to calculate HRV metrics for each segment
    and for the full data set.

    Parameters:
        ecg_data (list): The full ECG dataset.
        sampling_rate (int): The number of samples per second.
    """
    points_per_segment = sampling_rate * 60  # 60 seconds per segment
    total_points = len(ecg_data)
    num_segments = total_points // points_per_segment
    points_used = num_segments * points_per_segment
    remaining_points = total_points - points_used

    total_duration_minutes = total_points / (sampling_rate * 60)
    minutes = int(total_duration_minutes)
    seconds = int(
        (total_duration_minutes - minutes) * 60
    )  # Convert fraction of a minute to seconds

    print(f"Total data points: {total_points}")
    print(f"Total duration: {minutes} minutes and {seconds} seconds")
    print(f"Data points used in full minute segments: {points_used}")
    print(f"Remaining data points for analysis: {remaining_points}\n")

    analyze_full_dataset(ecg_data, sampling_rate)

    for i in range(num_segments):
        start_index = i * points_per_segment
        end_index = start_index + points_per_segment
        segment = ecg_data[start_index:end_index]
        analyze_segment(
            segment, i + 1, start_index / sampling_rate, end_index / sampling_rate
        )

    if remaining_points > 0:
        remaining_segment = ecg_data[points_used:]
        analyze_remaining_data(
            remaining_segment, points_used / sampling_rate, total_points / sampling_rate
        )


def main():
    """
    Main function to load ECG data and process it for HRV analysis.
    """
    file_path = "data/EST2019201904_2020-03-17_15-22-25.txt"
    try:
        ecg_data = load_ecg_data(file_path)
        if not ecg_data:
            print("Error: ECG data is empty.")
            sys.exit(1)
        process_segments(ecg_data, 200)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
