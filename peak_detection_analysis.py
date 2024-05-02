# peak_detection_analysis.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from hrv.reader import load_ppg_data


def plot_peaks(data, channel_name, sampling_rate, figure_number):
    """
    Plot data and the detected peaks for a given channel.
    :param data: The channel data where peaks need to be detected.
    :param channel_name: Name of the channel (for title and labels).
    :param sampling_rate: The sampling rate of the data.
    :param figure_number: The unique identifier for the figure.
    """
    peaks, _ = find_peaks(data, distance=sampling_rate / 2)

    plt.figure(figure_number, figsize=(10, 4))
    plt.plot(data, label="Data")
    plt.plot(peaks, data[peaks], "x", label="Detected Peaks", color="red")
    plt.title(f"{channel_name.capitalize()} Data with Detected Peaks")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.legend()

    # This line ensures the plot is shown without blocking the program execution
    plt.show(block=False)

    return peaks


def main():
    file_path = "data\inconclusive - ECO20192019105_2024-05-01_23-56-38.txt"
    sampling_rate = 250  # Adjust this according to your data's sampling rate

    ppg_data = load_ppg_data(file_path)

    channels = ["red", "ir", "green", "ecg"]
    for i, channel in enumerate(
        channels, 1
    ):  # Start enumeration with 1 for figure numbers
        if channel in ppg_data:
            print(f"Analyzing {channel.capitalize()} Channel")
            channel_data = np.array(ppg_data[channel])
            detected_peaks = plot_peaks(channel_data, channel, sampling_rate, i)
            print(
                f"Detected {len(detected_peaks)} peaks in {channel.capitalize()} Channel.\n"
            )

    # Keep the plots open
    plt.show()


if __name__ == "__main__":
    main()
