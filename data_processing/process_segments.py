# data_processing/process_segments.py

from analysis_module.full_dataset import analyze_full_dataset
from analysis_module.segment_analysis import analyze_segment
from analysis_module.remaining_data import analyze_remaining_data


def process_segments(ecg_data, sampling_rate, file_name):
    """
    Process the ECG data in segments to calculate HRV metrics for each segment
    and for the full data set.

    Parameters:
        ecg_data (list): The full ECG dataset.
        sampling_rate (int): The number of samples per second.
        file_name (str): Name of the file being processed.
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

    print(f"Processing file: {file_name}")
    print(f"Total data points: {total_points}")
    print(f"Total duration: {minutes} minutes and {seconds} seconds")
    print(f"Data points used in full minute segments: {points_used}")
    # print(f"Remaining data points for analysis: {remaining_points}\n")

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
